# Intake Governance

Portable multi-agent governance skill for role-based planning, review, dispatch, and execution.

This package is not an application or an SDK. It is a reusable set of governance rules, workflow references, and task-card constraints that can be mounted directly in an Agent Skills environment.

The repository currently includes the root governance skill plus four standalone workflow skills:

- `workflow-6a`
- `workflow-6ayh`
- `workflow-ppw`
- `workflow-sdd`

The core roles are:

- `intake`: entry hub
- `planner`: planning office
- `review-gate`: review gate
- `orchestrator`: dispatch hub
- worker departments: `data-ops`, `docs-spec`, `engineering`, `security`, `platform`, `governance`

The governance model is inspired by the Edict project, but this repository keeps the lighter, portable skill-package form that focuses on rules, workflow constraints, and task-card schema.

## Current usage model

- `intake` is the only public entry point
- external requests may not bypass directly to `planner`, `review-gate`, `orchestrator`, or any worker department
- `@intake` normalizes the request and classifies it into `6A`, `6AYH`, `PPW`, `SDD`, or `generic_governance`
- if `intake` auto-classifies the task as `6A`, `6AYH`, `PPW`, or `SDD`, it must emit that workflow's activation response exactly before any further planning text
- `scheduler` is internal-only and is not an external entry point

For substantial tasks, use the default path:

`intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator`

## When to use this skill

- the user wants multi-agent design or orchestration
- the user wants role-based delegation rules
- the user wants a planner / reviewer / dispatcher / worker split
- the user wants layered role collaboration or worker-group coordination
- the user input contains `@intake`

Do not force this skill onto trivial single-step tasks.

## Role table

| Role | Chinese label | Notes | Responsibility |
| --- | --- | --- | --- |
| `intake` | 接入中心 | public entry | ingest request, normalize intent, classify workflow, standardize title |
| `planner` | 规划中心 | planning office | plan, decompose, design the approach, define acceptance criteria |
| `review-gate` | 评审中心 | quality gate | assess risk, review quality, approve or reject |
| `orchestrator` | 调度中心 | dispatch hub | dispatch, coordinate, aggregate, track state |
| `data-ops` | 数据资源组 | worker department | data, cost, resource, reporting |
| `docs-spec` | 文档规范组 | worker department | docs, specs, reports |
| `engineering` | 工程实施组 | worker department | code, feature work, bug fixes, inspections |
| `security` | 安全合规组 | worker department | security, compliance, audits |
| `platform` | 平台发布组 | worker department | deployment, CI/CD, tools, automation |
| `governance` | Agent 治理组 | worker department | agent registry, permissions, training, governance maintenance |
| `scheduler` | 定时调度器 | internal-only | internal timed triggers and morning aggregation, never an external entry |

## Workflow aliases

The external entry still goes through `intake`, but aliases can route the request into different governance modes:

- `@init`: project initialization analysis
- `@plan`: task planning
- `@refactor`: progressive refactor
- `@risk`: risk review
- `@decision`: technical decision
- `@audit`: architecture / code audit
- `@ask`: quick decomposition
- `@ppw` / `@PPW`: project-process inventory
- `@6A`: new feature development
- `@6AYH`: progressive optimization
- `@sdd`: spec-driven development

## Task-card requirements

Use a structured task card instead of a free-form delegation message. The required fields are:

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

See [references/task-card.schema.json](references/task-card.schema.json) for the full schema.

## Document gate

For `6A`, `6AYH`, `PPW`, and `SDD`:

- workflow documents are mandatory deliverables
- workflow docs must live under the active project's root `docs/YYYY_MM_DD_中文任务名_vN/` directory
- do not write generated workflow docs into the skill repository unless the skill repository is the active project being changed
- if code changes are involved, record file path, line range, before context, and after context
- present the document bundle summary to the user and wait for explicit confirmation before any code generation or implementation
- keep `user_confirmation.status=pending` until the user confirms the documents
- do not dispatch `engineering`, generate code, or edit code until `user_confirmation.status=confirmed`

## Source of truth

Read these references when precise behavior matters:

- `references/agents.json`
- `references/status-transitions.json`
- `references/handoff-record.schema.json`
- `references/role-permissions.md`
- `references/routing-rules.json`
- `references/task-card.schema.json`
- `references/role-prompts.json`
- `references/workflow-routing.json`
- `references/engineering-governance.md`
- `references/intake-classification.md`

Read these workflow references when the selected mode needs them:

- `references/workflows/6a.md`
- `references/workflows/6ayh.md`
- `references/workflows/ppw.md`
- `references/workflows/sdd.md`

Treat each workflow file's `Required documents` section as an execution contract.

## Routing policy

Route from `orchestrator` by tags:

- `code`, `bugfix`, `feature`, `algorithm`, `performance` -> `engineering`
- `docs`, `api`, `report`, `spec` -> `docs-spec`
- `data`, `cost`, `reporting`, `resource` -> `data-ops`
- `security`, `compliance`, `audit` -> `security`
- `deploy`, `cicd`, `tooling`, `automation` -> `platform`
- `agent`, `permission`, `training`, `registry` -> `governance`

If no worker matches, return to `planner` for replanning.

## Review policy

Send the task through `review-gate` when any of the following is true:

- the task is high risk
- the task spans multiple worker departments
- the acceptance criteria are unclear
- the task touches security, compliance, deployment, or permissions

When `review-gate` rejects or returns a task, it must emit `rejection_reason` and, when applicable, `required_fixes`.

## Directory structure

```text
.
├── SKILL.md
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

## Minimal example

User input:

```text
@intake Help me plan a feature that spans frontend, documentation, and deployment
```

Expected behavior:

1. `intake` classifies the request and normalizes the goal, title, and constraints
2. `planner` decomposes the plan, stages the work, and defines acceptance criteria
3. `review-gate` reviews the task when it spans multiple domains or carries risk
4. `orchestrator` dispatches to the appropriate worker departments
5. Workers return only to `orchestrator`

## Design goals

- portable: no dependency on platform-specific global configuration
- governable: explicit handoff graph prevents role confusion and overreach
- extensible: workflow, routing, and task-card schema live in reference files
- reusable: suitable as a standalone skill package for publication or integration

## Further reading

Recommended order:

1. [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
2. [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
3. [references/role-permissions.md](references/role-permissions.md)
4. [references/workflow-routing.json](references/workflow-routing.json)
