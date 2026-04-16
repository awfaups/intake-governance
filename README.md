# Role-Based Agent Governance 中文说明

这是一个面向多 Agent 协作场景的可移植治理 skill 包，用于角色化规划、审议、调度和执行。

这个仓库以 `SKILL.md` 作为模型入口，以 `OVERVIEW.zh-CN.md` 作为中文仓库总览。

## 快速开始

1. 安装到 `~/.codex/skills/role-based-agent-governance`
2. 重启 Codex
3. 用 `@intake` 作为统一入口开始

## 仓库包含什么

- `SKILL.md`：模型可读的入口规则
- `OVERVIEW.md`：英文仓库总览
- `OVERVIEW.zh-CN.md`：中文仓库总览
- `BEGINNER_GUIDE.md` 和 `BEGINNER_GUIDE.zh-CN.md`：新手说明
- `references/`：工作流规则、schema 和路由配置
- `skills/`：拆分后的独立 workflow skills

## 推荐阅读

- [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
- [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
- [OVERVIEW.md](OVERVIEW.md)
- [PUBLISHING.md](PUBLISHING.md)

## 支持的工作流模式

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

## 这个仓库适合做什么

- 多 Agent 设计或编排
- 基于角色的任务委派
- 规划 / 审议 / 调度 / 执行分层协作
- 工程治理型流程，如规划、审计、风险评估和重构治理

## 模型入口说明

如果你要看真正的模型入口规则，请直接读 [SKILL.md](SKILL.md)。
