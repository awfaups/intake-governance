---
name: role-based-agent-governance
description: Portable Agent Skills package for a role-based multi-agent workflow using intake, planner, review-gate, orchestrator, and worker departments. Use when the user wants multi-agent orchestration, role-based delegation, planning-review-dispatch pipelines, modern role collaboration, or explicitly uses @intake as the only public entry token.
metadata:
  short-description: Portable role-based agent governance workflow
---

# Role-Based Agent Governance

This skill defines a portable multi-agent operating model based on `intake`, `planner`, `review-gate`, `orchestrator`, and worker departments.

Use this skill when:

- the user wants multi-agent design or orchestration
- the user wants role-based delegation rules
- the user wants a planner, reviewer, dispatcher, and worker split
- the user refers to layered role collaboration or worker-group coordination
- the user input contains `@intake`

Do not force this skill onto trivial single-step tasks.

### Reading rule

Model-facing instructions in this package are English-only by design.
Do not spend model context reading separate Chinese explanation files unless the user explicitly asks for Chinese wording.

### Entry rule

`@intake` is the only public entry token for this package.

- No request may bypass directly to `planner`, `review-gate`, `orchestrator`, or any worker department.
- Use this default path for substantial tasks:

`intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator`

`intake` must first classify the request into one of these internal modes:

- `6A`
- `6AYH`
- `PPW`
- `SDD`
- `generic_governance`

If `intake` auto-classifies the request as `6A`, `6AYH`, `PPW`, or `SDD`, output that workflow's activation response exactly before any additional planning text.

### Workflow document rules

For `6A`, `6AYH`, `PPW`, and `SDD`:

- required documents are mandatory deliverables
- workflow docs must live under the active project's root `docs/` directory
- use the directory pattern `docs/YYYY_MM_DD_中文任务名_vN/`
- do not write generated workflow docs into the skill repository unless it is the active project
- if code changes are involved, record file path, line range, before context, and after context

Implementation must not start until the required workflow document bundle has been initialized or updated to the stage being executed.

For any workflow that may generate or modify code:

- output or update the required workflow documents first
- present the document bundle summary to the user for confirmation
- set `user_confirmation.status` to `pending` while waiting for the user
- do not generate code, edit code, run code-changing commands, or dispatch `engineering` until the user explicitly confirms the documents
- set `user_confirmation.status` to `confirmed` only after an explicit positive user response
- `review-gate` approval is not a substitute for user confirmation

### Role guidance

- `intake`: normalize the request, extract intent, assign title and tags
- `intake`: include workflow mode and required-document manifest in the first task card for `6A`, `6AYH`, `PPW`, and `SDD`
- `planner`: decompose the task, define execution steps, and assign likely worker departments
- `planner`: turn required documents into a document-bootstrap plan
- `review-gate`: approve, reject, or return for revision based on quality, risk, and policy fit
- `orchestrator`: dispatch to workers, track returns, and aggregate outputs
- `orchestrator`: block code generation and `engineering` dispatch until document review has explicit user confirmation
- `orchestrator`: dispatch `docs-spec` before code execution or final reporting when docs must be created or updated
- workers: execute only within their domain and return only to `orchestrator`

### Source of truth

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

### Routing policy

Route from `orchestrator` by tags:

- `code`, `bugfix`, `feature`, `algorithm`, `performance` -> `engineering`
- `docs`, `api`, `report`, `spec` -> `docs-spec`
- `data`, `cost`, `reporting`, `resource` -> `data-ops`
- `security`, `compliance`, `audit` -> `security`
- `deploy`, `cicd`, `tooling`, `automation` -> `platform`
- `agent`, `permission`, `training`, `registry` -> `governance`

If no worker matches, return to `planner` for replanning.

### Review policy

Send the task through `review-gate` when any of the following is true:

- the task is high risk
- the task spans multiple worker departments
- the acceptance criteria are unclear
- the task touches security, compliance, deployment, or permissions

When `review-gate` rejects or returns a task, it must emit `rejection_reason` and, when applicable, `required_fixes`.

### Task-card requirements

Use a structured task card rather than a loose message. Required fields:

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

### Output discipline

- record why each handoff happened
- ensure every handoff can be represented by `references/handoff-record.schema.json`
- include a `responsibility_notice` in every handoff
- follow `references/status-transitions.json` for all status moves
- keep worker outputs scoped to their own domain
- aggregate final results in `orchestrator`
- do not let workers bypass the handoff graph
- do not let workers close a task directly
- output fixed activation responses verbatim when a workflow requires them
