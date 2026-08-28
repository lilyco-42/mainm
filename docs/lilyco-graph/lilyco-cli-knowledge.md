# lilyco · lilyco-cli

> Sourcegraph CodeGraph 自动提取 · 观察即可,勿手改
> 再生成:`python tools/export-lilyco-graph.py`

## 概览

| 函数/方法 | 结构体 | 枚举/别名 | Trait | 路由 | 文件 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 36 | 0 | 1 | 0 | 0 | 1 |

## crate 依赖

```mermaid
flowchart LR
    lilyco-cli[lilyco-cli] --> lilyco-core[lilyco-core]
    lilyco-cli[lilyco-cli] --> lilyco-ffmpeg[lilyco-ffmpeg]
```

## 公共符号 (public)

- ⚙️ **`run`** — 函数 · `lib.rs:146` `(
    runner: fn(&A, &Context) -> Result<serde_json::Value, AppError>,
)`
- 🔧 **`extract_args`** — 方法 · `lib.rs:81` `(
        schema: &CommandSchema,
        matches: &clap::ArgMatches,
    ) -> std::collections::HashMap<String, serde_json::Value>`
- 🔧 **`handle_builtin_flags`** — 方法 · `lib.rs:45` `(schema: &CommandSchema, matches: &clap::ArgMatches) -> bool`
- 🔧 **`new`** — 方法 · `lib.rs:38` `() -> Self`
- 🔧 **`output_format`** — 方法 · `lib.rs:68` `(matches: &clap::ArgMatches) -> OutputFormat`

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

- `lilyco-cli/src/lib.rs`

---
[[lilyco-cli-knowledge|lilyco-cli 知识图谱]] · [[lilyco-core-knowledge|← lilyco-core]] · [[lilyco-ffmpeg-knowledge|← lilyco-ffmpeg]]
