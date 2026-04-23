# Intake Governance

Portable multi-agent governance skill for role-based planning, review, dispatch, and execution.

This repository is a reusable skill package, not an application or SDK. It provides an intake-first operating model for complex agent collaboration, with explicit role boundaries, workflow routing, document gates, and schema-backed handoffs.

Chinese documentation is also included:

- [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
- [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
- [TEAM_SHARE_MULTI_AGENT_GOVERNANCE.zh-CN.md](TEAM_SHARE_MULTI_AGENT_GOVERNANCE.zh-CN.md)

## What this package contains

The repository currently includes:

- one root governance skill: `SKILL.md`
- four standalone workflow detail skills:
  - `workflow-6a`
  - `workflow-6ayh`
  - `workflow-ppw`
  - `workflow-sdd`
- governance references, schemas, examples, and routing rules under `references/`
- validation and sync scripts under `scripts/`
- a lightweight app-facing surface in `agents/openai.yaml`

## Core model

The role system is:

- `intake`: entry hub
- `planner`: planning office
- `review-gate`: quality and risk gate
- `orchestrator`: dispatch hub
- worker departments: `data-ops`, `docs-spec`, `engineering`, `security`, `platform`, `governance`

Default flow for substantial tasks:

```text
intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator
```

## Entry rule

`intake` is the only public entry point.

External requests must not bypass directly to `planner`, `review-gate`, `orchestrator`, or any worker department.

Accepted entry patterns:

- `@intake`
- governance aliases that must still normalize back to `intake` first:
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
  - `@PPW`
  - `@sdd`

If `intake` classifies the request into `6A`, `6AYH`, `PPW`, or `SDD`, it must emit that workflow's fixed activation response before any additional planning text.

## Workflow modes

`intake` first classifies work into one of these modes:

- `6A`: new feature development
- `6AYH`: progressive optimization and refactor
- `PPW`: project inventory and process clarification
- `SDD`: spec-driven development
- `generic_governance`: governance routing without a workflow-specific contract

The standalone workflow skills are detail layers, not public entry points. They are meant to be used only after workflow selection is already known.

## Document gate

For `6A`, `6AYH`, `PPW`, and `SDD`:

- required workflow docs are mandatory deliverables
- docs must live under the active project's root `docs/YYYY_MM_DD_中文任务名_vN/`
- generated workflow docs should not be written into this skill repository unless this repository is the active project being changed
- if code changes are involved, workflow docs must record file path, line range, before context, and after context
- the document bundle must be presented to the user before any implementation starts
- `user_confirmation.status` must stay `pending` until the user explicitly confirms
- code generation, code edits, and `engineering` dispatch must stay blocked until `user_confirmation.status=confirmed`

## Required task card shape

This package expects structured handoff artifacts rather than free-form delegation prose.

Minimum required task-card fields:

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
- `document_bundle_version`
- `user_confirmation`
- `code_change_targets`
- `handoff_history`
- `status`

Source of truth:

- [references/task-card.schema.json](references/task-card.schema.json)
- [references/handoff-record.schema.json](references/handoff-record.schema.json)
- [references/status-transitions.json](references/status-transitions.json)

## Repository layout

```text
.
├── README.md
├── SKILL.md
├── OVERVIEW.md
├── BEGINNER_GUIDE.md
├── PUBLISHING.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── activation-examples.json
│   ├── activation-examples.md
│   ├── agents.json
│   ├── engineering-governance.md
│   ├── handoff-record.example.json
│   ├── handoff-record.schema.json
│   ├── intake-classification.md
│   ├── maintainer-upgrade-guide.md
│   ├── reference-loading.md
│   ├── regression-checklist.md
│   ├── role-permissions.md
│   ├── role-prompts.json
│   ├── routing-rules.json
│   ├── status-transitions.json
│   ├── task-card.example.json
│   ├── task-card.schema.json
│   ├── templates/
│   │   └── 01_SPEC.template.md
│   ├── workflow-routing.json
│   └── workflows/
│       ├── 6a.md
│       ├── 6ayh.md
│       ├── ppw.md
│       └── sdd.md
├── scripts/
│   ├── smoke_test_prompts.py
│   ├── sync_installed_skill.py
│   └── validate_governance_skill.py
└── skills/
    ├── workflow-6a/
    ├── workflow-6ayh/
    ├── workflow-ppw/
    └── workflow-sdd/
```

## Install

Clone or copy this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/intake-governance ~/.codex/skills/intake-governance
```

Then restart Codex so the skill is reloaded.

## Validate and sync

Validate the package:

```bash
python3 scripts/validate_governance_skill.py
```

Validate and compare with an installed copy:

```bash
python3 scripts/validate_governance_skill.py --compare-installed
```

Sync the runtime-relevant files into the installed skill copy:

```bash
python3 scripts/sync_installed_skill.py
```

The validator currently checks:

- required files exist
- JSON references parse correctly
- example artifacts satisfy required schema keys
- `agents/openai.yaml` parses as YAML
- prompt smoke tests still match routing expectations

## First prompt

Example:

```text
@intake Help me plan a feature that spans frontend, documentation, and deployment
```

Expected behavior:

1. `intake` normalizes the request and classifies the workflow.
2. `planner` decomposes the task and identifies the required departments.
3. `review-gate` is used if the task is risky, cross-functional, or ambiguous.
4. `orchestrator` dispatches work and aggregates returns.
5. Workers report only back to `orchestrator`.

## Related docs

- [OVERVIEW.md](OVERVIEW.md)
- [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
- [references/engineering-governance.md](references/engineering-governance.md)
- [references/maintainer-upgrade-guide.md](references/maintainer-upgrade-guide.md)
- [PUBLISHING.md](PUBLISHING.md)

## Publishing note

If this repository is being published as a shareable public skill, keep `SKILL.md` lean, move detailed rules into `references/`, and keep workflow-specific behavior in `skills/workflow-*`.

---

# 中文版

## Intake Governance

一个可移植的多 Agent 治理 skill，用于基于角色的规划、评审、调度与执行。

这个仓库是一个可复用的 skill 包，不是应用或 SDK。它提供了一套以 `intake` 为入口的协作模型，用于处理复杂 Agent 协作场景，并通过明确的角色边界、工作流路由、文档门禁和 schema 约束的交接结构来保持治理一致性。

仓库内也包含中文相关文档：

- [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
- [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
- [TEAM_SHARE_MULTI_AGENT_GOVERNANCE.zh-CN.md](TEAM_SHARE_MULTI_AGENT_GOVERNANCE.zh-CN.md)

## 这个包包含什么

当前仓库包括：

- 一个根治理 skill：`SKILL.md`
- 四个独立的 workflow 细分 skill：
  - `workflow-6a`
  - `workflow-6ayh`
  - `workflow-ppw`
  - `workflow-sdd`
- 位于 `references/` 下的治理规则、schema、示例和路由配置
- 位于 `scripts/` 下的校验与同步脚本
- 位于 `agents/openai.yaml` 中的轻量应用侧配置入口

## 核心模型

角色体系如下：

- `intake`：接入中心
- `planner`：规划中心
- `review-gate`：质量与风险评审门
- `orchestrator`：调度中心
- 执行部门：`data-ops`、`docs-spec`、`engineering`、`security`、`platform`、`governance`

对于非简单任务，默认流转路径为：

```text
intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator
```

## 入口规则

`intake` 是唯一允许的公开入口。

外部请求不得直接绕过到 `planner`、`review-gate`、`orchestrator` 或任何执行部门。

允许的外部触发形式：

- `@intake`
- 仍然必须先归一化回 `intake` 的治理别名：
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
  - `@PPW`
  - `@sdd`

如果 `intake` 将请求识别为 `6A`、`6AYH`、`PPW` 或 `SDD`，它必须先输出对应工作流要求的固定激活响应，再进入后续规划文本。

## 工作流模式

`intake` 会先把任务归类到以下模式之一：

- `6A`：新功能开发
- `6AYH`：渐进式优化与重构
- `PPW`：项目盘点与流程梳理
- `SDD`：规格驱动开发
- `generic_governance`：不绑定特定 workflow 的通用治理路由

这些独立 workflow skills 是细节层，不是公开入口。它们只应在 workflow 已经被确认后使用。

## 文档门禁

对于 `6A`、`6AYH`、`PPW` 和 `SDD`：

- workflow 文档是强制交付物
- 文档必须位于当前项目根目录下的 `docs/YYYY_MM_DD_中文任务名_vN/`
- 除非当前正在修改的项目就是这个 skill 仓库，否则不应把生成的 workflow 文档写回本仓库
- 如果涉及代码修改，workflow 文档必须记录文件路径、行范围、修改前上下文和修改后上下文
- 在任何实现开始前，必须先向用户展示文档包摘要
- 在用户明确确认之前，`user_confirmation.status` 必须保持为 `pending`
- 在 `user_confirmation.status=confirmed` 之前，代码生成、代码编辑和 `engineering` 调度都必须被阻止

## 任务卡结构要求

这个包要求使用结构化交接产物，而不是自由文本式委派。

任务卡至少需要这些字段：

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
- `document_bundle_version`
- `user_confirmation`
- `code_change_targets`
- `handoff_history`
- `status`

以下文件是权威来源：

- [references/task-card.schema.json](references/task-card.schema.json)
- [references/handoff-record.schema.json](references/handoff-record.schema.json)
- [references/status-transitions.json](references/status-transitions.json)

## 仓库结构

```text
.
├── README.md
├── SKILL.md
├── OVERVIEW.md
├── BEGINNER_GUIDE.md
├── PUBLISHING.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── activation-examples.json
│   ├── activation-examples.md
│   ├── agents.json
│   ├── engineering-governance.md
│   ├── handoff-record.example.json
│   ├── handoff-record.schema.json
│   ├── intake-classification.md
│   ├── maintainer-upgrade-guide.md
│   ├── reference-loading.md
│   ├── regression-checklist.md
│   ├── role-permissions.md
│   ├── role-prompts.json
│   ├── routing-rules.json
│   ├── status-transitions.json
│   ├── task-card.example.json
│   ├── task-card.schema.json
│   ├── templates/
│   │   └── 01_SPEC.template.md
│   ├── workflow-routing.json
│   └── workflows/
│       ├── 6a.md
│       ├── 6ayh.md
│       ├── ppw.md
│       └── sdd.md
├── scripts/
│   ├── smoke_test_prompts.py
│   ├── sync_installed_skill.py
│   └── validate_governance_skill.py
└── skills/
    ├── workflow-6a/
    ├── workflow-6ayh/
    ├── workflow-ppw/
    └── workflow-sdd/
```

## 安装

把仓库 clone 或复制到你的 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/intake-governance ~/.codex/skills/intake-governance
```

然后重启 Codex，让 skill 重新加载。

## 校验与同步

校验这个 skill 包：

```bash
python3 scripts/validate_governance_skill.py
```

校验并对比已安装副本：

```bash
python3 scripts/validate_governance_skill.py --compare-installed
```

把运行时相关文件同步到已安装 skill 副本：

```bash
python3 scripts/sync_installed_skill.py
```

当前校验器会检查：

- 必需文件是否存在
- JSON references 是否能正常解析
- 示例产物是否满足 schema 的必填字段要求
- `agents/openai.yaml` 是否是合法 YAML
- prompt smoke tests 是否仍然符合当前路由预期

## 第一个提示词

示例：

```text
@intake Help me plan a feature that spans frontend, documentation, and deployment
```

预期行为：

1. `intake` 归一化请求并识别 workflow。
2. `planner` 拆解任务并判断需要哪些执行部门。
3. 如果任务高风险、跨职能或定义不清，则进入 `review-gate`。
4. `orchestrator` 负责分发执行并聚合回传结果。
5. 所有 worker 只能回传到 `orchestrator`。

## 相关文档

- [OVERVIEW.md](OVERVIEW.md)
- [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
- [references/engineering-governance.md](references/engineering-governance.md)
- [references/maintainer-upgrade-guide.md](references/maintainer-upgrade-guide.md)
- [PUBLISHING.md](PUBLISHING.md)

## 发布说明

如果这个仓库要作为可公开分发的 skill 发布，建议保持 `SKILL.md` 精简，把详细规则放到 `references/`，并把 workflow 细节维持在 `skills/workflow-*` 下。
