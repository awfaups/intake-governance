# Intake Governance 中文说明

> 这份文档给人看，不作为模型入口说明。

## 这是什么

`intake-governance` 是一个可移植的多 Agent 治理 skill 包。

它不是应用程序，也不是 SDK，而是一套可复用的治理规则、工作流参考和任务卡约束，适合在 Agent Skills 场景中直接挂载使用。

这套 skill 的核心角色是：

- `intake`：接入中心
- `planner`：规划中心
- `review-gate`：评审中心
- `orchestrator`：调度中心
- 执行部门：`data-ops`、`docs-spec`、`engineering`、`security`、`platform`、`governance`

当前仓库除了主治理 skill，还拆出了 4 个独立 workflow skill：

- `workflow-6a`
- `workflow-6ayh`
- `workflow-ppw`
- `workflow-sdd`

## 适用场景

在以下场景启用这套模型：

- 多 Agent 设计或编排
- 基于角色的任务委派
- 规划 / 审议 / 调度 / 执行分层协作
- 工程治理型流程，如规划、审计、风险评估、重构治理
- 用户显式输入 `@intake`

对于简单的一步式请求，不应强行套用这套多 Agent 流程。

## 最新入口规则

- `intake` 是唯一允许的外部入口
- 外部请求不能直接进入 `planner`、`review-gate`、`orchestrator` 或执行部门
- 标准流转链路为 `intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator`
- 执行部门只能向 `orchestrator` 回传结果，禁止横向派单
- 高风险、跨部门、目标不清或涉及安全 / 部署 / 权限的任务必须经过 `review-gate`
- `scheduler` 只用于内部定时触发，不是外部入口

## 角色分工

| 角色 | 中文名 | 中文含义 | 职责 |
| --- | --- | --- | --- |
| `intake` | 接入中心 | 接收入口、初步分流 | 入口接收、需求归一、标题标准化、工作流识别 |
| `planner` | 规划中心 | 任务规划、拆解设计 | 规划、拆解、方案设计、验收标准定义 |
| `review-gate` | 评审中心 | 风险审查、质量把关 | 风险审议、质量把关、批准或驳回 |
| `orchestrator` | 调度中心 | 调度协调、结果汇总 | 派发、协调、汇总、状态跟踪 |
| `data-ops` | 数据资源组 | 数据与资源处理 | 数据、资源、核算、报表 |
| `docs-spec` | 文档规范组 | 文档与规格输出 | 文档、规范、报告 |
| `engineering` | 工程实施组 | 代码与功能实现 | 代码、功能开发、Bug 修复、巡检 |
| `security` | 安全合规组 | 安全与合规审查 | 安全、合规、审计 |
| `platform` | 平台发布组 | 部署与工具链支持 | 部署、CI/CD、工具、自动化 |
| `governance` | Agent 治理组 | Agent 管理与规则维护 | Agent 注册、权限、培训、治理维护 |
| `scheduler` | 定时调度器 | 内部定时触发器 | 内部定时触发、晨报聚合，不作为外部入口 |

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

## SDD 细化阶段

当前仓库中的 `workflow-sdd` 在不改变公开治理面的前提下，把内部阶段细化为：

`Init -> Explore -> Propose -> Spec -> Plan -> Design -> Atomize -> Approve -> Execute -> Verify -> Archive`

这意味着：

- `@intake` 仍然是唯一公开入口
- `workflow-sdd` 仍然只是内部细节层
- 在正式写 Spec 之前，可以先做项目接入、现状分析和变更提案
- 在 Verify 之后，可以用 Archive 做归档收尾，而不是重新打开 scope

对于非简单的 SDD 任务，推荐补充这些支持文档：

- `00_INIT_CONTEXT_项目接入.md`
- `00_EXPLORE_现状分析.md`
- `00_PROPOSE_变更提案.md`
- `09_ARCHIVE_归档记录.md`

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
- `document_bundle_version`
- `required_documents`
- `document_status`
- `user_confirmation`
- `code_change_targets`
- `handoff_history`
- `status`

完整 schema 见 [references/task-card.schema.json](references/task-card.schema.json)。

## 状态治理

推荐的硬状态流转为：

`submitted -> triaged -> planned -> under_review -> approved -> dispatched -> executing -> aggregated -> completed`

返工与异常状态包括：

- `needs_revision`
- `blocked`
- `rejected`
- `cancelled`

每次状态变化都应附带 handoff 记录，详见：

- [references/status-transitions.json](references/status-transitions.json)
- [references/handoff-record.schema.json](references/handoff-record.schema.json)

每条 handoff 记录都应该显式带上 `responsibility_notice`，用于提示职责如何从上一个角色转移到下一个角色。

## 文档门禁

`6A`、`6AYH`、`PPW`、`SDD` 的文档目录统一使用：

`docs/YYYY_MM_DD_中文任务名_vN/`

这个 `docs/` 必须位于当前 IDE / 当前打开项目的根目录下，而不是 skill 包自己的目录里。

如果工作流涉及代码修改，文档里还必须记录：

- 要修改的文件路径
- 具体行号范围
- 修改前代码片段
- 修改后代码片段

代码生成或代码修改必须在文档包输出后等待用户显式确认。用户确认前，任务卡中的 `user_confirmation.status` 应保持为 `pending`，不得派发 `engineering`，也不得生成或修改代码。

## 目录结构

```text
.
├── README.md
├── SKILL.md
├── OVERVIEW.md
├── OVERVIEW.zh-CN.md
├── BEGINNER_GUIDE.md
├── BEGINNER_GUIDE.zh-CN.md
├── PUBLISHING.md
├── LICENSE
├── agents
│   └── openai.yaml
├── scripts
│   ├── smoke_test_prompts.py
│   ├── sync_installed_skill.py
│   └── validate_governance_skill.py
├── skills
│   ├── workflow-6a
│   ├── workflow-6ayh
│   ├── workflow-ppw
│   └── workflow-sdd
└── references
    ├── agents.json
    ├── engineering-governance.md
    ├── handoff-record.schema.json
    ├── intake-classification.md
    ├── role-permissions.md
    ├── role-prompts.json
    ├── routing-rules.json
    ├── status-transitions.json
    ├── task-card.schema.json
    ├── templates
    │   └── 01_SPEC.template.md
    ├── workflow-routing.json
    └── workflows
        ├── 6a.md
        ├── 6ayh.md
        ├── ppw.md
        └── sdd.md
```

## 关键文件说明

- [README.md](README.md)：GitHub 首页总览，包含英文与中文摘要、安装、校验与发布说明
- [SKILL.md](SKILL.md)：主 skill 定义、启用条件、总流程、读取策略
- [agents/openai.yaml](agents/openai.yaml)：应用侧展示名、短描述和默认提示入口
- [references/agents.json](references/agents.json)：角色定义与可收发关系
- [references/status-transitions.json](references/status-transitions.json)：合法状态迁移与角色权限
- [references/handoff-record.schema.json](references/handoff-record.schema.json)：标准流转记录结构
- [references/role-permissions.md](references/role-permissions.md)：越权边界与强制职责链
- [references/workflow-routing.json](references/workflow-routing.json)：别名、自动分类信号、激活响应
- [references/task-card.schema.json](references/task-card.schema.json)：任务卡 JSON Schema
- [references/workflows/6a.md](references/workflows/6a.md)：新增功能开发工作流
- [references/workflows/6ayh.md](references/workflows/6ayh.md)：渐进式优化工作流
- [references/workflows/ppw.md](references/workflows/ppw.md)：项目流程梳理工作流
- [references/workflows/sdd.md](references/workflows/sdd.md)：规格驱动开发工作流
- [references/templates/01_SPEC.template.md](references/templates/01_SPEC.template.md)：SDD 的规格文档模板
- [scripts/validate_governance_skill.py](scripts/validate_governance_skill.py)：仓库结构、schema、示例和 YAML 的一致性校验
- [scripts/smoke_test_prompts.py](scripts/smoke_test_prompts.py)：入口别名和自动分类的 smoke test
- [scripts/sync_installed_skill.py](scripts/sync_installed_skill.py)：把运行时相关文件同步到已安装 skill 副本
- [skills/workflow-6a/SKILL.md](skills/workflow-6a/SKILL.md)：独立 6A workflow skill
- [skills/workflow-6ayh/SKILL.md](skills/workflow-6ayh/SKILL.md)：独立 6AYH workflow skill
- [skills/workflow-ppw/SKILL.md](skills/workflow-ppw/SKILL.md)：独立 PPW workflow skill
- [skills/workflow-sdd/SKILL.md](skills/workflow-sdd/SKILL.md)：独立 SDD workflow skill

## 最小使用示例

用户输入：

```text
@intake 帮我规划一个跨前端、文档和部署的功能开发流程
```

期望行为：

1. `intake` 识别请求并归一化标题、目标、约束
2. `planner` 拆解方案、划分执行阶段、定义验收标准
3. `review-gate` 在跨部门或高风险场景下进行审议
4. `orchestrator` 根据标签派发到相应执行部门
5. 执行部门仅在各自职责范围内产出，并统一回传给 `orchestrator`

## 工作流文档目录命名

`6A`、`6AYH`、`PPW`、`SDD` 生成的文档目录，统一使用：

`docs/YYYY_MM_DD_中文任务名_vN/`

这个 `docs/` 必须位于**当前 IDE / 当前打开项目的根目录**下，而不是 skill 包自己的目录里。

例如：

`docs/2026_03_23_首页优化_v1/`

如果是同一个功能的第二版、第三版文档，就递增为：

- `docs/2026_03_23_首页优化_v2/`
- `docs/2026_03_23_首页优化_v3/`

如果工作流涉及代码修改，文档里还必须记录：

- 要修改的文件路径
- 具体行号范围
- 修改前代码片段
- 修改后代码片段

代码生成或代码修改必须在文档包输出后等待用户显式确认。用户确认前，任务卡中的 `user_confirmation.status` 应保持为 `pending`，不得派发 `engineering`，也不得生成或修改代码。

## 设计目标

- 可移植：不依赖特定平台的全局配置文件
- 可治理：通过显式 handoff 图防止越权和角色混乱
- 可扩展：通过引用文件维护工作流、路由规则和任务卡 schema
- 可复用：适合作为独立 skill 包对外发布或集成到其他 Agent 体系

## 推荐阅读顺序

建议按这个顺序看：

1. [README.md](README.md)
2. [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
3. [OVERVIEW.md](OVERVIEW.md)
4. [role-permissions.md](references/role-permissions.md)
5. [workflow-routing.json](references/workflow-routing.json)
