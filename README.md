# mainm

**一个命令从零产出成片** — Rust CLI · 模板优先 · 约定大于配置

三域:视频生成(主)/ 数学讲题 / 代码研究。

## 定位

`mainm` = 把「脚本 → 分镜 → 资产 → 渲染 → MP4」收敛成**模板化单命令**,省掉每次手动搭管线。
三域共用同一编排管线:模板实例化 → 清单 → 执行 → 产物。

> 开发首日闭环:lilyco 知识图谱(Obsidian,由 codegraph 生成)+ 设计文档已就位。

## 快速开始(规划)

```bash
cargo run -- init [name]        # 自举约定目录
cargo run -- video "brief"      # 一句话 brief → 成片(规划中)
cargo run -- run <name>         # 按约定目录跑管线(规划中)
```

## 约定目录(约定即 schema)

```
<project>/
  templates/        # 可覆盖内置模板
  scripts/          # 生成的脚本/分镜(brief → script)
  assets/           # 中间资产(图片/音频/字体)
  scenes/           # 渲染单元(remotion index.ts / manim scene)
  render-spec.json  # 引擎输入契约
  out/              # 最终产物 mp4 / 文档
```

## 设计决策

| 维度 | 决策 |
|------|------|
| 形态 | 单 bin + 子命令树(clap derive),复用 lilyco 执行层 |
| 模板 | `include_dir!` 内置 + 外扩覆盖(`~/.mainm/templates/`、项目 `templates/`) |
| 引擎 | 子进程 + JSON 协议,统一 `EngineAdapter` trait(Remotion / Manim) |
| agent | 黑盒编排:`claude -p` / `opencode run` 拉起,只收产物 |
| MVP | 最窄闭环「脚本→分镜→MP4」;数学/代码研究后置留接口 |

详见 [`docs/mainm-design.md`](docs/mainm-design.md)。

## 知识图谱

`docs/lilyco-graph/` 是用 [CodeGraph](https://github.com/sourcegraph/codegraph) 索引
`lilyco` workspace 后自动生成的 **Obsidian 知识库**:

- `_index.md` — 模块地图 + crate 依赖 Mermaid + 边语义
- `lilyco-*-knowledge.md` — 每个 crate 一页(公共符号 / 调用关系 / 文件清单)
- `knowledge-graph.json` — 机器可读总览

再生成:

```bash
codegraph init ../lilyco            # 首次;增量用 codegraph sync
python tools/export-lilyco-graph.py \
  --db D:/code/rust/lilyco/.codegraph/codegraph.db \
  --out docs/lilyco-graph
```

用 Obsidian「打开文件夹作为仓库」选择 `docs/lilyco-graph/`,即可看图形视图。

## 里程碑

| # | 里程碑 | 优先级 |
|---|--------|--------|
| M1 | CLI 骨架 + 子命令表 + 约定目录规范 | P0 |
| M2 | 模板加载 + 数学讲题模板 + brief→script | P0 |
| M3 | 窄闭环:桥接 oma-video,`brief→mp4` 单命令 | P0 |
| M4 | 确定性:seed 固定、rerender 增量、失败定位 | P1 |
| M5 | 可复用:模板数据化 + 本地 agent 稳定接口(JSON) | P1 |

## License

MIT OR Apache-2.0