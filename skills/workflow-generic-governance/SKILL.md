---
name: workflow-generic-governance
description: GGW workflow detail layer for role-based planning, review, dispatch, and closeout after intake has classified a task as generic_governance. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow GGW

Use this skill only when the workflow type is already known to be `generic_governance`.

Treat this skill as a detail layer, not a public governance entry.

- If the request still needs intake, routing, or cross-role governance, enter through `@intake` first.
- Keep global handoff policy in `intake-governance`; keep generic governance stage rules here and in `references/generic-governance.md`.

### Activation response

When `intake` classifies the request as `generic_governance`, output exactly:

> 通用治理工作流（GGW · Generic Governance Workflow）已激活
> 当前阶段：Intake（治理意图归一）

Then follow `references/generic-governance.md`.

### Required behavior

This workflow enforces:

- intake-first normalization
- role-bound planning
- review-gate use when risk, ambiguity, or cross-department scope requires it
- orchestrator-only worker dispatch
- required workflow documents before execution
- explicit user confirmation before code or durable artifact changes
- final aggregation and decision logging by `orchestrator`

### References

Load only when needed:

- `references/generic-governance.md`
