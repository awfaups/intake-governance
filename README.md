# Role-Based Agent Governance 中文说明

这是一个面向多 Agent 协作场景的可移植治理 skill 包。当前仓库已经对齐到最新的角色治理模型，包含根 skill、独立 workflow skills、任务卡 schema 和文档门禁规则。

这个仓库以 `SKILL.md` 作为模型入口，以 `OVERVIEW.zh-CN.md` 作为中文仓库总览。

## 这套 skill 做什么

- 让复杂任务按 `intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator` 的链路推进
- 用结构化任务卡约束委派、审议、调度和回传
- 对 `6A`、`6AYH`、`PPW`、`SDD` 这类 workflow 先产出文档包，再等待用户确认
- 把代码修改和文档修改的边界写清楚，减少越权和返工

## 快速开始

1. 安装到 `~/.codex/skills/role-based-agent-governance`
2. 重启 Codex
3. 用 `@intake` 作为统一入口开始

## 当前仓库包含什么

- `SKILL.md`：模型可读的入口规则
- `OVERVIEW.md`：英文仓库总览
- `OVERVIEW.zh-CN.md`：中文仓库总览
- `BEGINNER_GUIDE.md` 和 `BEGINNER_GUIDE.zh-CN.md`：新手说明
- `references/`：角色定义、路由规则、任务卡 schema、状态流转和 workflow 参考
- `skills/`：拆分后的独立 workflow skills

## 最新入口规则

- `intake` 是唯一允许的外部入口
- 外部请求不能直接进入 `planner`、`review-gate`、`orchestrator` 或执行部门
- `@intake` 会先归一化需求，再分类到 `6A`、`6AYH`、`PPW`、`SDD` 或 `generic_governance`
- 如果自动识别到 `6A`、`6AYH`、`PPW`、`SDD`，`intake` 会先输出对应工作流的激活响应
- `scheduler` 只用于内部定时触发，不是外部入口

## 工作流模式

- `@init`
- `@plan`
- `@refactor`
- `@risk`
- `@decision`
- `@audit`
- `@ask`
- `@ppw`
- `@6A`
- `@6AYH`
- `@sdd`

这些别名仍然由 `intake` 统一接管，然后再转入相应流程。

## 需要记住的门禁

- `6A`、`6AYH`、`PPW`、`SDD` 都要先输出工作流文档包
- 文档目录统一是 `docs/YYYY_MM_DD_中文任务名_vN/`
- 涉及代码修改时，任务卡和文档都要写 `code_change_targets`
- 代码生成或修改前，`user_confirmation.status` 必须保持 `pending`
- 用户确认文档包后，才允许进入代码生成或实现阶段

## 推荐阅读

- [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
- [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
- [OVERVIEW.md](OVERVIEW.md)
- [PUBLISHING.md](PUBLISHING.md)

## 这个仓库适合做什么

- 多 Agent 设计或编排
- 基于角色的任务委派
- 规划 / 审议 / 调度 / 执行分层协作
- 工程治理型流程，如规划、审计、风险评估和重构治理

## 模型入口说明

如果你要看真正的模型入口规则，请直接读 [SKILL.md](SKILL.md)。
