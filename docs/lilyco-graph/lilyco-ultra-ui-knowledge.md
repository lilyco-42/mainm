# lilyco · lilyco-ultra-ui

> Sourcegraph CodeGraph 自动提取 · 观察即可,勿手改
> 再生成:`python tools/export-lilyco-graph.py`

## 概览

| 函数/方法 | 结构体 | 枚举/别名 | Trait | 路由 | 文件 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 42 | 3 | 4 | 0 | 4 | 5 |

## crate 依赖

```mermaid
flowchart LR
    lilyco-ultra-ui[lilyco-ultra-ui] --> lilyco-core[lilyco-core]
```

## 公共符号 (public)

- 🧱 **`UiSpec`** — 结构体 · `spec.rs:10`
- 🧱 **`UltraUiServer`** — 结构体 · `lib.rs:22`
- 🧱 **`WindowSpec`** — 结构体 · `spec.rs:17`
- 🔠 **`ButtonVariant`** — 枚举 · `spec.rs:62`
- 🔠 **`CalcMode`** — 枚举 · `spec.rs:226`
- 🔠 **`ElementSpec`** — 枚举 · `spec.rs:82`
- 🔠 **`WindowSize`** — 枚举 · `spec.rs:35`
- ⚙️ **`builder_html`** — 函数 · `builder.rs:5` `() -> String`
- ⚙️ **`calculator_example_json`** — 函数 · `spec.rs:331` `() -> String`
- ⚙️ **`default_example_json`** — 函数 · `spec.rs:309` `() -> String`
- ⚙️ **`generate_react_html`** — 函数 · `generator.rs:9` `(spec: &UiSpec) -> String`
- 🔧 **`css_class`** — 方法 · `spec.rs:49` `(&self) -> &'static str`
- 🔧 **`css_class`** — 方法 · `spec.rs:70` `(&self) -> &'static str`
- 🔧 **`from_json`** — 方法 · `spec.rs:234` `(json: &str) -> Result<Self, serde_json::Error>`
- 🔧 **`new`** — 方法 · `lib.rs:27` `(port: u16) -> Self`
- 🔧 **`serve`** — 方法 · `lib.rs:32` `(&self)`
- 🔧 **`to_json_pretty`** — 方法 · `spec.rs:238` `(&self) -> String`
- 🔧 **`type_name`** — 方法 · `spec.rs:289` `(&self) -> &'static str`
- 🔧 **`validate`** — 方法 · `spec.rs:242` `(&self) -> Vec<String>`
- 🔧 **`var_name`** — 方法 · `spec.rs:277` `(&self) -> Option<&str>`

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

- `lilyco-ultra-ui/src/builder.rs`
- `lilyco-ultra-ui/src/generator.rs`
- `lilyco-ultra-ui/src/lib.rs`
- `lilyco-ultra-ui/src/spec.rs`
- `lilyco-ultra-ui/tests/spec_tests.rs`

---
[[lilyco-ultra-ui-knowledge|lilyco-ultra-ui 知识图谱]] · [[lilyco-core-knowledge|← lilyco-core]] · [[lilyco-ffmpeg-knowledge|← lilyco-ffmpeg]] · [[lilyco-gui-knowledge|← lilyco-gui]] · [[lilyco-tui-knowledge|← lilyco-tui]] · [[lilyco-ultra-ui-example-knowledge|← lilyco-ultra-ui-example]]
