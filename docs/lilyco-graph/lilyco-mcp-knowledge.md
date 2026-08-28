# lilyco · lilyco-mcp

> Sourcegraph CodeGraph 自动提取 · 观察即可,勿手改
> 再生成:`python tools/export-lilyco-graph.py`

## 概览

| 函数/方法 | 结构体 | 枚举/别名 | Trait | 路由 | 文件 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 23 | 1 | 0 | 0 | 0 | 1 |

## crate 依赖

```mermaid
flowchart LR
    lilyco-mcp[lilyco-mcp] --> lilyco-core[lilyco-core]
    lilyco-mcp[lilyco-mcp] --> lilyco-ffmpeg[lilyco-ffmpeg]
```

## 公共符号 (public)

- 🧱 **`McpServer`** — 结构体 · `lib.rs:37`
- 🔧 **`handle_line`** — 方法 · `lib.rs:50` `(&self, line: &str) -> Option<String>`
- 🔧 **`new`** — 方法 · `lib.rs:43` `(registry: Registry) -> Self`
- 🔧 **`serve`** — 方法 · `lib.rs:89` `(&self, mut reader: R, mut writer: W) -> std::io::Result<()>`
- 🔧 **`serve_stdio`** — 方法 · `lib.rs:110` `(&self) -> std::io::Result<()>`

## 调用关系 (top)

- **`run_brush`** → `read_with_cap`(×2), `resolve_shell`(×1), `build_path_env`(×1), `emit`(×1), `new`(×1), `done`(×1)
- **`resolve_shell`** → `find_on_path`(×2)
- **`resolve_git_usr_bin`** → `iter`(×1)
- **`path_entries`** → `path_sep`(×1)
- **`build_path_env`** → `resolve_git_usr_bin`(×1), `path_entries`(×1)
- **`find_on_path`** → `path_entries`(×1), `path_exts`(×1)
- **`run`** → `as_str`(×5), `done`(×5), `emit`(×2), `init_project`(×2), `validate_project`(×2), `new_test`(×1)
- **`shell_available`** → `resolve_shell`(×1)
- **`echo_runs_and_captures_stdout`** → `shell_available`(×1), `run`(×1)
- **`exit_code_is_propagated_not_errored`** → `shell_available`(×1), `run`(×1)
- **`stderr_is_captured`** → `shell_available`(×1), `run`(×1)
- **`cwd_is_honored`** → `shell_available`(×1), `run`(×1)

## 文件清单

- `lilyco-mcp/src/lib.rs`

---
[[lilyco-mcp-knowledge|lilyco-mcp 知识图谱]] · [[lilyco-core-knowledge|← lilyco-core]] · [[lilyco-ffmpeg-knowledge|← lilyco-ffmpeg]] · [[lilyco-macros-knowledge|← lilyco-macros]]
