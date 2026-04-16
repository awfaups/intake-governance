# Role-Based Agent Governance 中文说明

> 这份文档给人看，不作为模型入口说明。

## 这是什么

`role-based-agent-governance` 是一个可移植的多 Agent 治理 skill 包。

它不是应用程序，也不是 SDK，而是一套可复用的治理规则、工作流参考和任务卡约束，适合在 Agent Skills 场景中直接挂载使用。

这套 skill 的核心角色是：

- `intake`：接入中心
- `planner`：规划中心
- `review-gate`：评审中心
- `orchestrator`：调度中心
- 执行部门：`data-ops`、`docs-spec`、`engineering`、`security`、`platform`、`governance`

## 适用场景

在以下场景启用这套模型：

- 多 Agent 设计或编排
- 基于角色的任务委派
- 规划 / 审议 / 调度 / 执行分层协作
- 工程治理型流程，如规划、审计、风险评估、重构治理
- 用户显式输入 `@intake`

对于简单的一步式请求，不应强行套用这套多 Agent 流程。

## 核心原则

- `intake` 是唯一允许的外部入口
- 外部请求不能直接进入 `planner`、`review-gate`、`orchestrator` 或执行部门
- 标准流转链路为 `intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator`
- 执行部门只能向 `orchestrator` 回传结果，禁止横向派单
- 高风险、跨部门、目标不清或涉及安全 / 部署 / 权限的任务必须经过 `review-gate`

## 角色分工

| 角色 | 中文名 | 职责 |
| --- | --- | --- |
| `intake` | 接入中心 | 入口接收、需求归一、标题标准化、工作流识别 |
| `planner` | 规划中心 | 规划、拆解、方案设计、验收标准定义 |
| `review-gate` | 评审中心 | 风险审议、质量把关、批准或驳回 |
| `orchestrator` | 调度中心 | 派发、协调、汇总、状态跟踪 |
| `data-ops` | 数据资源组 | 数据、资源、核算、报表 |
| `docs-spec` | 文档规范组 | 文档、规范、报告 |
| `engineering` | 工程实施组 | 代码、功能开发、Bug 修复、巡检 |
| `security` | 安全合规组 | 安全、合规、审计 |
| `platform` | 平台发布组 | 部署、CI/CD、工具、自动化 |
| `governance` | Agent治理组 | Agent 注册、权限、培训、治理维护 |
| `scheduler` | 定时调度器 | 内部定时触发、晨报聚合，不作为外部入口 |

## 支持的工作流别名

入口仍然由 `intake` 统一接管，但可根据别名路由到不同治理模式：

- `@init`：项目初始化分析
- `@plan`：任务规划
- `@refactor`：渐进式重构
- `@risk`：风险评估
- `@decision`：技术决策
- `@audit`：架构 / 代码审计
- `@ask`：快速问题拆解
- `@ppw` / `@PPW`：项目流程梳理
- `@6A`：新增功能开发
- `@6AYH`：渐进式优化
- `@sdd`：规格驱动开发

当请求内容匹配 `6A`、`6AYH`、`PPW` 或 `SDD` 的自动识别信号时，`intake` 也应先输出对应工作流规定的激活响应，再继续内部流转。

## 标签到执行部门的默认路由

- `code`、`bugfix`、`feature`、`algorithm`、`performance` -> `engineering`
- `docs`、`api`、`report`、`spec` -> `docs-spec`
- `data`、`cost`、`reporting`、`resource` -> `data-ops`
- `security`、`compliance`、`audit` -> `security`
- `deploy`、`cicd`、`tooling`、`automation` -> `platform`
- `agent`、`permission`、`training`、`registry` -> `governance`

如果没有合适的执行部门，任务应回退到 `planner` 重新规划。

## 任务卡要求

推荐使用结构化任务卡，而不是自由文本委派。至少包含以下字段：

- `task_id`
- `title`
- `from`
- `to`
- `goal`
- `brief`
- `tags`
- `constraints`
- `deliverables`
- `review_required`
- `workflow_mode`
- `current_stage`
- `required_documents`
- `document_status`
- `handoff_history`
- `status`

完整 schema 见 [task-card.schema.json](references/task-card.schema.json)。

## 状态治理

推荐的硬状态流转为：

`submitted -> triaged -> planned -> under_review -> approved -> dispatched -> executing -> aggregated -> completed`

返工与异常状态包括：

- `needs_revision`
- `blocked`
- `rejected`
- `cancelled`

每次状态变化都应附带 handoff 记录，详见：

- [status-transitions.json](references/status-transitions.json)
- [handoff-record.schema.json](references/handoff-record.schema.json)

每条 handoff 记录都应该显式带上 `responsibility_notice`，用于提示职责如何从上一个角色转移到下一个角色。

## 关键文件

- [SKILL.md](SKILL.md)：主 skill 定义，给模型读
- [OVERVIEW.md](OVERVIEW.md)：仓库说明
- [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)：新手说明
- [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)：独立中文新手说明
- [agents.json](references/agents.json)：角色定义与可收发关系
- [workflow-routing.json](references/workflow-routing.json)：别名、自动分类信号、激活响应
- [role-permissions.md](references/role-permissions.md)：越权边界与强制职责链

## 工作流文档目录命名

`6A`、`6AYH`、`PPW`、`SDD` 的文档目录统一使用：

`docs/YYYY_MM_DD_中文任务名_vN/`

例如：

- `docs/2026_03_23_首页优化_v1/`
- `docs/2026_03_23_首页优化_v2/`

这个 `docs/` 必须位于当前 IDE / 当前打开项目的根目录下，而不是 skill 包自己的目录里。

如果工作流涉及代码修改，文档里还必须记录：

- 要修改的文件路径
- 具体行号范围
- 修改前代码片段
- 修改后代码片段

## 设计目标

- 可移植：不依赖特定平台的全局配置文件
- 可治理：通过显式 handoff 图防止越权和角色混乱
- 可扩展：通过引用文件维护工作流、路由规则和任务卡 schema
- 可复用：适合作为独立 skill 包对外发布或集成到其他 Agent 体系

## 进一步阅读

建议按这个顺序看：

1. [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
2. [OVERVIEW.md](OVERVIEW.md)
3. [role-permissions.md](references/role-permissions.md)
4. [workflow-routing.json](references/workflow-routing.json)
