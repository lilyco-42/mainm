# lilyco · lilyco-ffmpeg

> Sourcegraph CodeGraph 自动提取 · 观察即可,勿手改
> 再生成:`python tools/export-lilyco-graph.py`

## 概览

| 函数/方法 | 结构体 | 枚举/别名 | Trait | 路由 | 文件 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 28 | 3 | 3 | 0 | 0 | 1 |

## crate 依赖

```mermaid
flowchart LR
    lilyco-ffmpeg[lilyco-ffmpeg] --> lilyco-core[lilyco-core]
    lilyco-ffmpeg[lilyco-ffmpeg] --> lilyco-ultra-ui[lilyco-ultra-ui]
```

## 公共符号 (public)

_无 public 符号。_

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

- `lilyco-ffmpeg/src/main.rs`

---
[[lilyco-ffmpeg-knowledge|lilyco-ffmpeg 知识图谱]] · [[lilyco-knowledge|← lilyco]] · [[lilyco-brush-knowledge|← lilyco-brush]] · [[lilyco-cli-knowledge|← lilyco-cli]] · [[lilyco-core-knowledge|← lilyco-core]] · [[lilyco-example-knowledge|← lilyco-example]] · [[lilyco-gui-knowledge|← lilyco-gui]] · [[lilyco-letsgal-knowledge|← lilyco-letsgal]] · [[lilyco-macros-knowledge|← lilyco-macros]] · [[lilyco-mcp-knowledge|← lilyco-mcp]] · [[lilyco-ultra-ui-knowledge|← lilyco-ultra-ui]] · [[lilyco-vision-knowledge|← lilyco-vision]]
