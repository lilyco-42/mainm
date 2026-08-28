# lilyco · lilyco-macros

> Sourcegraph CodeGraph 自动提取 · 观察即可,勿手改
> 再生成:`python tools/export-lilyco-graph.py`

## 概览

| 函数/方法 | 结构体 | 枚举/别名 | Trait | 路由 | 文件 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 25 | 9 | 2 | 0 | 0 | 4 |

## crate 依赖

```mermaid
flowchart LR
    lilyco-macros[lilyco-macros] --> lilyco-core[lilyco-core]
    lilyco-macros[lilyco-macros] --> lilyco-ffmpeg[lilyco-ffmpeg]
    lilyco-macros[lilyco-macros] --> lilyco-mcp[lilyco-mcp]
```

## 公共符号 (public)

- ⚙️ **`derive_app`** — 函数 · `lib.rs:20` `(input: proc_macro::TokenStream) -> proc_macro::TokenStream`
- ⚙️ **`derive_app_impl`** — 函数 · `app_derive.rs:229` `(input: TokenStream) -> TokenStream`
- ⚙️ **`derive_value_enum`** — 函数 · `lib.rs:28` `(input: proc_macro::TokenStream) -> proc_macro::TokenStream`
- ⚙️ **`derive_value_enum_impl`** — 函数 · `value_enum.rs:5` `(input: TokenStream) -> TokenStream`

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

- `lilyco-macros/src/app_derive.rs`
- `lilyco-macros/src/lib.rs`
- `lilyco-macros/src/value_enum.rs`
- `lilyco-macros/tests/derive_tests.rs`

---
[[lilyco-macros-knowledge|lilyco-macros 知识图谱]] · [[lilyco-knowledge|← lilyco]] · [[lilyco-core-knowledge|← lilyco-core]] · [[lilyco-example-knowledge|← lilyco-example]] · [[lilyco-ffmpeg-knowledge|← lilyco-ffmpeg]] · [[lilyco-mcp-knowledge|← lilyco-mcp]]
