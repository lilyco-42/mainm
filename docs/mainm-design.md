# mainm — 一个命令从零产出成片

> Rust CLI · 模板优先 · 约定大于配置
> 三域：视频生成（主）/ 数学讲题 / 代码研究

## 定位（一句话）

`mainm` = 一个命令从零产出成片：把「脚本 → 分镜 → 资产 → 渲染 → MP4」
收敛成模板化单命令。核心价值是**省掉每次手动搭管线的步骤**；"统一三域
入口""模板可复用"只是载体，不是目标。

## 已确认决策（三方 agent 评审 + 预研共识）

| 维度 | 决策 |
|------|------|
| 形态 | 单 bin + 子命令树（三域共享同一编排管线，不拆多 bin） |
| 模板 | 内置模板用 `include_dir!` 编译进二进制（离线、防篡改、随版本）；外扩 `~/.mainm/templates/` 与项目 `templates/` 按优先级覆盖 |
| 引擎接入 | 不用 FFI 内嵌；一律**子进程 + JSON 协议**，统一 `EngineAdapter` trait |
| agent 层 | **黑盒编排**：mainm 生成 prompt+上下文文件，用 `claude -p` / `opencode run` 拉起，只收「产物文件+退出码」，不解析 LLM 内部输出 |
| MVP 范围 | 只做视频**最窄闭环**「脚本→分镜→MP4」；数学/代码研究后置留接口；数学讲题只做第一个内置模板 |

## 命令集

```
mainm init [name]            # 在项目内自举约定目录
mainm new <type> <name>      # 从内置模板脚手架项目
mainm video <brief>          # 一句话 brief → 数学讲题/视频成片
mainm math <topic>           # 数学讲题（第一个内置模板，后置）
mainm study <repo|topic>     # 代码研究（后置）
mainm run <name>             # 按约定目录跑管线
mainm agent <task>           # 分派子任务给 cline/claude-code/opencode
```

## 约定目录（约定即 schema）

```
<project>/
  templates/        # 可覆盖内置模板
  scripts/          # 生成的脚本/分镜（brief → script）
  assets/           # 中间资产（图片/音频/字体）
  scenes/           # 渲染单元（remotion index.ts / manim scene）
  render-spec.json  # 引擎输入契约
  out/              # 最终产物 mp4 / 文档
```

## 落地验收（PM 反判据）

1. **默认路径零配置**：`mainm video "讲题"` 无 flag 即产片。
2. **目录即状态**：约定目录本身就是输入+状态，无隐式配置 / DB。
3. **模板是数据不是代码**：改 YAML/JSON 即改形态；反判据＝须懂 Remotion 才用得起＝未落地。

## 架构要点

- **统一 pipeline 契约 + 契约测试**：三域是同一「模板实例化→清单→执行→产物」管线的不同模板族；首要不变量是契约，用 fitness-function 测试锁死（防变"脆弱胶水调度器"）。
- **Rust 只编排/校验/调度**，不重述业务逻辑；跨运行时只传序列化数据（JSON/文件）；每运行时一个 `EngineAdapter` adapter 模块，上层只见统一 pipeline 接口。
- **agent 黑盒**：收窄为统一 subagent 接口（上下文目录/产物目录/超时/取消），适配器只写「如何交任务 + 如何等结束」。

## 技术选型 / 现有资产

- 复用 **lilyco**（path 依赖）：`#[derive(App)]` 参数、`executor/registry`、进度事件流（`command -progress pipe:1` 心智模型）；`Backend::Cli` 为主。
- 复用 **oma-video Remotion 管线**：本机存在 `resources/remotion/{src/index.ts, src/render-spec.ts, remotion.config.ts}` → `npx remotion render src/index.ts --props <render-spec.json>` 出 MP4。
- 模板填充：`minijinja`（贴近 {n} 模板作者心智）。
- Windows os error 193 坑：spawn `.CMD` 统一 `cmd /C "<resolved>.cmd"` 包裹。

## MVP 里程碑

| # | 里程碑 | 优先级 | 依赖 |
|---|--------|--------|------|
| M1 | CLI 骨架 + 子命令表 + 约定目录规范 | P0 | 无 |
| M2 | 模板加载（约定目录扫描 + 数学讲题模板 + brief→script） | P0 | M1 |
| M3 | 窄闭环：桥接 oma-video，`brief→mp4` 单命令 | P0 | M1, M2 |
| M4 | 确定性：seed 固定、rerender 增量、失败定位 | P1 | M3 |
| M5 | 可复用：模板数据化 + 本地 agent 稳定接口(JSON) | P1 | M4 |

> 数学 / 代码研究：M5 后置，不进 MVP。

## 最小可运行验证（第一根桩）

`mainm new video hello` → 从 include_dir 生成含 `render-spec.json` 的项目 →
`mainm run` 调 Remotion 出一个 3s 的 mp4。同时验证「模板填充 + 约定目录 +
引擎 JSON 协议」三根桩。
