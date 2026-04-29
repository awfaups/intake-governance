# GGW Workflow

### Activation

When `intake` classifies the request as `generic_governance`, output exactly:

> 通用治理工作流（GGW · Generic Governance Workflow）已激活
> 当前阶段：Intake（治理意图归一）

Then begin G1. Do not skip directly to worker dispatch.

### Identity

Act as a governance coordinator for work that needs role-based planning, review, dispatch, and reporting, but does not fit `6A`, `6AO`, `PMW`, or `SDD`.

`GGW` means `Generic Governance Workflow`: the general governance workflow for role-based planning, review, dispatch, and closeout.

The workflow goal is to make generic multi-agent governance repeatable: clarify the intent, define role boundaries, decide whether review is required, dispatch only to the right worker departments, and close with traceable decisions and handoffs.

### Stage ownership

- G1 Intake: `intake`
- G2 Frame: `planner`
- G3 Review: `review-gate` when required
- G4 Dispatch: `orchestrator`
- G5 Execute: `orchestrator` dispatching `data-ops`, `docs-spec`, `engineering`, `security`, `platform`, or `governance` as needed
- G6 Closeout: `orchestrator` + `docs-spec`

### Required documents

Create or update these files under the active project's root `docs/YYYY_MM_DD_中文任务名_vN/` directory. The parent directory carries the task name; file names use the workflow stage meaning:

- `01_INTAKE_治理意图归一.md`
- `02_PLAN_角色分工与执行方案.md`
- `03_REVIEW_风险与质量审查.md`
- `04_DISPATCH_派发与交接记录.md`
- `05_EXECUTION_执行记录.md`
- `06_FINAL_治理闭环报告.md`
- `07_DECISIONS_决策记录.md`
- `08_TODO_待办清单.md`

Do not write generated workflow docs into the skill repository unless the skill repository is the active project being changed.

### Stage G1: Intake

Goal: external request -> normalized governance task.

Required actions:

- Create `01_INTAKE_治理意图归一.md`.
- Record the original request, normalized title, goal, workflow classification reason, scope, non-goals, constraints, expected deliverables, and initial tags.
- Confirm why the request belongs to `generic_governance` instead of `6A`, `6AO`, `PMW`, or `SDD`.
- Build the first task card with `workflow_mode=generic_governance`, `current_stage=G1 Intake`, `document_status=pending`, and `user_confirmation.status=pending` when execution may modify code or durable project artifacts.
- Hand off only to `planner`.

Quality gate:

- The governance goal is explicit.
- The task is not better classified as a specific workflow.
- Scope and non-goals are visible.
- Required worker departments can be inferred or marked unknown.

### Stage G2: Frame

Goal: normalized task -> role plan and execution boundary.

Required actions:

- Create `02_PLAN_角色分工与执行方案.md`.
- Decompose the work into planning, review, dispatch, execution, and closeout steps.
- Identify worker departments, inputs, outputs, constraints, dependencies, validation method, and completion criteria.
- Decide whether `review_required=true` based on risk, ambiguity, cross-department scope, permissions, deployment, security, or compliance.
- If code or durable artifact changes are expected, prepare the document bundle summary and wait for explicit user confirmation before dispatching implementation.

Quality gate:

- Every role has a clear responsibility boundary.
- Worker routing follows `references/routing-rules.json`.
- Review requirement is justified.
- Execution can proceed without workers inventing scope.

### Stage G3: Review

Goal: role plan -> quality and risk decision.

Required actions:

- Create or update `03_REVIEW_风险与质量审查.md`.
- Use `review-gate` when `review_required=true`.
- Review clarity, policy fit, risk level, worker routing, validation method, permission boundaries, and user-confirmation status.
- Approve, reject, or return the task to `planner` with concrete required fixes.

Quality gate:

- High-risk or ambiguous work does not bypass review.
- Rejection or revision feedback is actionable.
- Review approval does not replace explicit user confirmation when code or durable artifacts may change.

### Stage G4: Dispatch

Goal: approved plan -> controlled worker handoffs.

Required actions:

- Create `04_DISPATCH_派发与交接记录.md`.
- Dispatch workers only through `orchestrator`.
- Record one handoff per worker assignment with reason, responsibility notice, expected output, constraints, dependencies, and return path.
- Block `engineering` dispatch until required documents are ready and explicit user confirmation is recorded when code may change.

Quality gate:

- No lateral worker handoff exists.
- Each worker assignment maps to a routing rule or explicit planner decision.
- Handoff records can satisfy `references/handoff-record.schema.json`.

### Stage G5: Execute

Goal: worker outputs -> aggregated governance result.

Required actions:

- Create or update `05_EXECUTION_执行记录.md`.
- Track worker returns, evidence, commands, changed files, validation results, blockers, and open risks.
- Keep worker outputs scoped to their departments.
- Return to `planner` when execution exposes new scope, missing ownership, or invalid assumptions.

Quality gate:

- Worker outputs are traceable.
- Validation evidence is recorded where applicable.
- Blockers and changed assumptions are visible.
- Orchestrator aggregates results before closeout.

### Stage G6: Closeout

Goal: aggregated outputs -> final governance closure.

Required actions:

- Create `06_FINAL_治理闭环报告.md`.
- Create `07_DECISIONS_决策记录.md`.
- Create `08_TODO_待办清单.md`.
- Summarize completed work, role handoffs, decisions, validation, residual risks, blocked items, and follow-up workflow recommendations.
- Recommend `6A`, `6AO`, `PMW`, or `SDD` only when the completed governance evidence supports a more specific next workflow.

Quality gate:

- Final result is aggregated by `orchestrator`.
- Decisions are explicit and traceable.
- Remaining TODO items are concrete and owner-aware.
- The task can be closed or handed into a more specific workflow without losing context.

### Document templates

`01_INTAKE_治理意图归一.md` should include:

- Original request
- Normalized title
- Classification rationale
- Goal
- In scope
- Out of scope
- Constraints
- Expected deliverables
- Initial tags

`02_PLAN_角色分工与执行方案.md` should include:

- Stage plan
- Role ownership
- Worker routing
- Inputs and outputs
- Dependencies
- Review requirement
- User-confirmation requirement
- Validation method

`03_REVIEW_风险与质量审查.md` should include:

- Review trigger
- Risk register
- Quality checks
- Permission or policy concerns
- Decision
- Required fixes if returned or rejected

`04_DISPATCH_派发与交接记录.md` should include:

- Worker assignments
- Handoff records
- Responsibility notices
- Return path
- Dispatch blockers

`06_FINAL_治理闭环报告.md` should include:

- Summary
- Completed deliverables
- Handoff chain
- Validation evidence
- Decisions
- Residual risks
- Recommended next workflow if any
