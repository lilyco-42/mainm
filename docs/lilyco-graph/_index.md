# lilyco 知识图谱 (codegraph)

> 由 Sourcegraph CodeGraph v1.5 索引 **967 节点 / 3612 边** → 自动生成 Obsidian 笔记
> 数据源: `lilyco/.codegraph/codegraph.db` · 生成器: `tools/export-lilyco-graph.py`

## 模块地图

| crate | 符号 | 函数/方法 | 结构体 | Trait | 依赖数 | 页面 |
|---|---|---|---|---|---|---|
| lilyco | 23 | 20 | 1 | 0 | 4 | [[lilyco-knowledge]] |
| lilyco-brush | 20 | 19 | 1 | 0 | 2 | [[lilyco-brush-knowledge]] |
| lilyco-cli | 37 | 36 | 0 | 0 | 2 | [[lilyco-cli-knowledge]] |
| lilyco-core | 109 | 91 | 7 | 3 | 3 | [[lilyco-core-knowledge]] |
| lilyco-example | 25 | 20 | 3 | 0 | 3 | [[lilyco-example-knowledge]] |
| lilyco-ffmpeg | 34 | 28 | 3 | 0 | 2 | [[lilyco-ffmpeg-knowledge]] |
| lilyco-grep | 13 | 11 | 2 | 0 | 1 | [[lilyco-grep-knowledge]] |
| lilyco-gui | 87 | 80 | 3 | 0 | 3 | [[lilyco-gui-knowledge]] |
| lilyco-letsgal | 37 | 33 | 2 | 0 | 2 | [[lilyco-letsgal-knowledge]] |
| lilyco-macros | 36 | 25 | 9 | 0 | 3 | [[lilyco-macros-knowledge]] |
| lilyco-mcp | 24 | 23 | 1 | 0 | 2 | [[lilyco-mcp-knowledge]] |
| lilyco-tui | 61 | 55 | 3 | 0 | 3 | [[lilyco-tui-knowledge]] |
| lilyco-ultra-ui | 53 | 42 | 3 | 0 | 1 | [[lilyco-ultra-ui-knowledge]] |
| lilyco-ultra-ui-example | 1 | 1 | 0 | 0 | 1 | [[lilyco-ultra-ui-example-knowledge]] |
| lilyco-vision | 71 | 62 | 9 | 0 | 2 | [[lilyco-vision-knowledge]] |

## 总体依赖 (crate 级 Mermaid)

```mermaid
flowchart LR
    lilyco[lilyco] --> lilyco-core[lilyco-core]
    lilyco[lilyco] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco[lilyco] --> lilyco-macros[lilyco-macros]
    lilyco[lilyco] --> lilyco-tui[lilyco-tui]
    lilyco-brush[lilyco-brush] --> lilyco-core[lilyco-core]
    lilyco-brush[lilyco-brush] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-cli[lilyco-cli] --> lilyco-core[lilyco-core]
    lilyco-cli[lilyco-cli] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-core[lilyco-core] --> lilyco-cli[lilyco-cli]
    lilyco-core[lilyco-core] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-core[lilyco-core] --> lilyco-ultra-ui[lilyco-ultra-ui]
    lilyco-example[lilyco-example] --> lilyco-core[lilyco-core]
    lilyco-example[lilyco-example] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-example[lilyco-example] --> lilyco-macros[lilyco-macros]
    lilyco-ffmpeg[lilyco-ffmpeg] --> lilyco-core[lilyco-core]
    lilyco-ffmpeg[lilyco-ffmpeg] --> lilyco-ultra-ui[lilyco-ultra-ui]
    lilyco-grep[lilyco-grep] --> lilyco-core[lilyco-core]
    lilyco-gui[lilyco-gui] --> lilyco-core[lilyco-core]
    lilyco-gui[lilyco-gui] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-gui[lilyco-gui] --> lilyco-ultra-ui[lilyco-ultra-ui]
    lilyco-letsgal[lilyco-letsgal] --> lilyco-core[lilyco-core]
    lilyco-letsgal[lilyco-letsgal] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-macros[lilyco-macros] --> lilyco-core[lilyco-core]
    lilyco-macros[lilyco-macros] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-macros[lilyco-macros] --> lilyco-mcp[lilyco-mcp]
    lilyco-mcp[lilyco-mcp] --> lilyco-core[lilyco-core]
    lilyco-mcp[lilyco-mcp] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-tui[lilyco-tui] --> lilyco-core[lilyco-core]
    lilyco-tui[lilyco-tui] --> lilyco-gui[lilyco-gui]
    lilyco-tui[lilyco-tui] --> lilyco-ultra-ui[lilyco-ultra-ui]
    lilyco-ultra-ui[lilyco-ultra-ui] --> lilyco-core[lilyco-core]
    lilyco-ultra-ui-example[lilyco-ultra-ui-example] --> lilyco-ultra-ui[lilyco-ultra-ui]
    lilyco-vision[lilyco-vision] --> lilyco-core[lilyco-core]
    lilyco-vision[lilyco-vision] --> lilyco-ffmpeg[lilyco-ffmpeg]
```

## 边语义

| kind | 含义 | 数量 |
|---|---|---|
| `calls` | 调用 | 1844 |
| `contains` | 包含 | 1012 |
| `references` | 引用 | 528 |
| `instantiates` | 实例化 | 114 |
| `imports` | 导入 | 113 |
| `implements` | 实现 | 1 |
