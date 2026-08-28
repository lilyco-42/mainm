#!/usr/bin/env python3
"""导出 lilyco codegraph 索引 → Obsidian 知识图谱 md 档案

数据源:  <lilyco>/.codegraph/codegraph.db  (Sourcegraph CodeGraph v1.5, SQLite)
输出:    mainm/docs/lilyco-graph/*.md  +  _index.md

用法:
  python tools/export-lilyco-graph.py \
      --db   D:/code/rust/lilyco/.codegraph/codegraph.db \
      --out  D:/code/rust/mainm/docs/lilyco-graph
"""
import argparse
import json
import os
import re
import sqlite3
from collections import defaultdict

KIND_ICON = {
    "struct": "🧱", "enum": "🔠", "trait": "🎯", "function": "⚙️",
    "method": "🔧", "route": "🛣️", "type_alias": "🏷️", "variable": "📦",
    "file": "📄", "import": "🔗", "enum_member": "🔹",
}
KIND_CN = {
    "struct": "结构体", "enum": "枚举", "trait": "Trait", "function": "函数",
    "method": "方法", "route": "路由", "type_alias": "类型别名", "variable": "变量",
    "file": "文件", "import": "导入", "enum_member": "枚举成员",
}
EDGE_CN = {
    "calls": "调用", "contains": "包含", "references": "引用",
    "instantiates": "实例化", "imports": "导入", "implements": "实现",
}

# 只导出有意义的符号节点,过滤内部噪音
SYMBOL_KINDS = {"struct", "enum", "trait", "function", "method", "route", "type_alias"}


def load_graph(db_path: str):
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    nodes = {}
    for r in con.execute(
        "SELECT id, kind, name, qualified_name, file_path, start_line, end_line, "
        "signature, visibility FROM nodes"
    ):
        nodes[r["id"]] = dict(r)
    edges = []
    for r in con.execute(
        "SELECT source, target, kind, line FROM edges"
    ):
        edges.append(dict(r))
    con.close()
    return nodes, edges


def file_base(file_path: str) -> str:
    return os.path.basename(file_path)


def crate_of(file_path: str) -> str:
    """从 file_path (lilyco-core/src/app.rs) 提取 crate 名。"""
    parts = file_path.replace("\\", "/").split("/")
    return parts[0] if parts else "?"
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    nodes, edges = load_graph(args.db)

    # ---- 1. 按 crate 聚合符号节点 ----
    crates = defaultdict(lambda: {"symbols": [], "file_count": 0, "files": set()})
    symbol_by_id = {}
    for nid, n in nodes.items():
        if n["kind"] in SYMBOL_KINDS:
            cr = crate_of(n["file_path"])
            crates[cr]["symbols"].append(n)
            symbol_by_id[nid] = n
            crates[cr]["files"].add(n["file_path"])
        if n["kind"] == "file":
            cr = crate_of(n["file_path"])
            crates[cr]["files"].add(n["file_path"])

    for cr, info in crates.items():
        info["file_count"] = len(info["files"])
        info["symbols"].sort(key=lambda s: (s["kind"], s["name"]))

    # ---- 2. 边: 只保留符号↔符号/文件→符号(供调用/引用关系) ----
    call_graph = defaultdict(lambda: defaultdict(int))
    dep_edges = defaultdict(lambda: defaultdict(int))  # crate -> crate
    for e in edges:
        src, tgt, kind = e["source"], e["target"], e["kind"]
        if src in symbol_by_id and tgt in symbol_by_id:
            s_name, t_name = symbol_by_id[src]["name"], symbol_by_id[tgt]["name"]
            s_crate, t_crate = crate_of(symbol_by_id[src]["file_path"]), crate_of(symbol_by_id[tgt]["file_path"])
            if kind == "calls":
                call_graph[s_name][t_name] += 1
            if s_crate != t_crate:
                dep_edges[s_crate][t_crate] += 1
        # 文件级 import: crate 依赖
        if kind == "imports" and src in nodes and tgt in nodes:
            s_c, t_c = crate_of(nodes[src]["file_path"]), crate_of(nodes[tgt]["file_path"])
            if s_c != t_c:
                dep_edges[s_c][t_c] += 1

    # ---- 3. 生成每 crate 页面 ----
    os.makedirs(args.out, exist_ok=True)
    page_count = 0
    for cr, info in sorted(crates.items()):
        n_sym = len(info["symbols"])
        n_fn = sum(1 for s in info["symbols"] if s["kind"] in ("function", "method"))
        n_struct = sum(1 for s in info["symbols"] if s["kind"] == "struct")
        n_enum = sum(1 for s in info["symbols"] if s["kind"] in ("enum", "type_alias"))
        n_trait = sum(1 for s in info["symbols"] if s["kind"] == "trait")
        n_route = sum(1 for s in info["symbols"] if s["kind"] == "route")

        title = f"lilyco · {cr}"
        backlinks = []
        related = set(dep_edges.get(cr, {})) | {a for a, b in dep_edges.items() if cr in b}
        for r in sorted(related):
            if r in crates:
                backlinks.append(f"[[{r}-knowledge|← {r}]]")
        wikilinks = " · ".join([f"[[{cr}-knowledge|{cr} 知识图谱]]"] + backlinks)

        lines = []
        lines.append(f"# {title}")
        lines.append("")
        lines.append("> Sourcegraph CodeGraph 自动提取 · 观察即可,勿手改")
        lines.append("> 再生成:`python tools/export-lilyco-graph.py`")
        lines.append("")
        lines.append("## 概览")
        lines.append("")
        lines.append("| 函数/方法 | 结构体 | 枚举/别名 | Trait | 路由 | 文件 |")
        lines.append("|:--:|:--:|:--:|:--:|:--:|:--:|")
        lines.append(f"| {n_fn} | {n_struct} | {n_enum} | {n_trait} | {n_route} | {info['file_count']} |")
        lines.append("")

        lines.append("## crate 依赖")
        lines.append("")
        if dep_edges.get(cr):
            lines.append("```mermaid")
            lines.append("flowchart LR")
            for tgt_c, _w in sorted(dep_edges[cr].items()):
                if tgt_c in crates:
                    lines.append(f"    {cr}[{cr}] --> {tgt_c}[{tgt_c}]")
            lines.append("```")
        else:
            lines.append("_无跨 crate 依赖。_")
        lines.append("")

        public = [s for s in info["symbols"] if s.get("visibility") == "public"]
        lines.append("## 公共符号 (public)")
        lines.append("")
        if public:
            by_kind = defaultdict(list)
            for s in public:
                by_kind[s["kind"]].append(s)
            for kind in ("struct", "enum", "trait", "type_alias", "route", "function", "method"):
                for s in by_kind.get(kind, []):
                    icon = KIND_ICON[kind]
                    cn = KIND_CN[kind]
                    sig = (s.get("signature") or "").strip()
                    line_info = f"`{file_base(s['file_path'])}:{s['start_line']}`"
                    lines.append(f"- {icon} **`{s['name']}`** — {cn} · {line_info}" +
                                 (f" `{sig}`" if sig else ""))
        else:
            lines.append("_无 public 符号。_")
        lines.append("")

        lines.append("## 调用关系 (top)")
        lines.append("")
        if call_graph:
            for src_name in list(call_graph)[:12]:
                targets = call_graph[src_name]
                top_t = sorted(targets.items(), key=lambda kv: -kv[1])[:6]
                lines.append(f"- **`{src_name}`** → " + ", ".join(
                    f"`{t}`(×{w})" for t, w in top_t))
        else:
            lines.append("_无调用关系。_")
        lines.append("")

        lines.append("## 文件清单")
        lines.append("")
        for f in sorted(info["files"]):
            lines.append(f"- `{f}`")
        lines.append("")
        lines.append("---")
        lines.append(wikilinks)
        lines.append("")

        page_count += 1
        out_path = os.path.join(args.out, f"{cr}-knowledge.md")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        print(f"  ✓ {out_path}")

    # ---- 4. _index.md ----
    idx = []
    idx.append("# lilyco 知识图谱 (codegraph)")
    idx.append("")
    idx.append(f"> 由 Sourcegraph CodeGraph v1.5 索引 **{len(nodes)} 节点 / {len(edges)} 边** → 自动生成 Obsidian 笔记")
    idx.append("> 数据源: `lilyco/.codegraph/codegraph.db` · 生成器: `tools/export-lilyco-graph.py`")
    idx.append("")
    idx.append("## 模块地图")
    idx.append("")
    idx.append("| crate | 符号 | 函数/方法 | 结构体 | Trait | 依赖数 | 页面 |")
    idx.append("|---|---|---|---|---|---|---|")
    for cr, info in sorted(crates.items()):
        n_fn = sum(1 for s in info["symbols"] if s["kind"] in ("function", "method"))
        n_struct = sum(1 for s in info["symbols"] if s["kind"] == "struct")
        n_trait = sum(1 for s in info["symbols"] if s["kind"] == "trait")
        n_dep = len(dep_edges.get(cr, {}))
        idx.append(f"| {cr} | {len(info['symbols'])} | {n_fn} | {n_struct} | {n_trait} | {n_dep} | [[{cr}-knowledge]] |")
    idx.append("")
    idx.append("## 总体依赖 (crate 级 Mermaid)")
    idx.append("")
    idx.append("```mermaid")
    idx.append("flowchart LR")
    for src_c, tgts in sorted(dep_edges.items()):
        for tgt_c in sorted(tgts):
            if src_c in crates and tgt_c in crates:
                idx.append(f"    {src_c}[{src_c}] --> {tgt_c}[{tgt_c}]")
    idx.append("```")
    idx.append("")
    idx.append("## 边语义")
    idx.append("")
    idx.append("| kind | 含义 | 数量 |")
    idx.append("|---|---|---|")
    ecount = defaultdict(int)
    for e in edges:
        ecount[e["kind"]] += 1
    for k, c in sorted(ecount.items(), key=lambda kv: -kv[1]):
        idx.append(f"| `{k}` | {EDGE_CN.get(k, k)} | {c} |")
    idx.append("")
    idx_path = os.path.join(args.out, "_index.md")
    with open(idx_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx))
    print(f"  ✓ {idx_path}")

    # 总览 JSON(进 docs)
    overview = {
        "meta": {
            "title": "lilyco knowledge graph",
            "source": "codegraph",
            "version": "1.5.0",
            "nodes": len(nodes),
            "edges": len(edges),
            "crates": sorted(crates.keys()),
        }
    }
    ov_path = os.path.join(args.out, "knowledge-graph.json")
    with open(ov_path, "w", encoding="utf-8") as fh:
        json.dump(overview, fh, ensure_ascii=False, indent=2)
    print(f"  ✓ {ov_path}")
    print(f"\n共生成 {page_count} 个 crate 页面")


if __name__ == "__main__":
    main()