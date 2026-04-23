---
name: workflow-sdd
description: SDD workflow detail layer for spec-driven development after workflow selection is known. Use when the task is already confirmed as SDD, the user explicitly requests @sdd, or intake has classified the task as spec-first delivery where implementation, tests, and acceptance derive from an approved spec bundle. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow SDD

Use this skill only when the workflow type is already known to be `SDD`.

Treat this skill as a detail layer, not a public governance entry.

- If the request still needs intake, routing, or cross-role governance, enter through `@intake` first.
- Use this skill after workflow selection is settled.
- Keep global handoff policy in `intake-governance`; keep SDD stage rules here and in `references/sdd.md`.

## Activation response

> ✅ Spec-Driven Development 工作流（SDD）已激活
> 当前阶段：Spec（规格定义）

## Execution contract

This skill enforces:

- spec-first workflow only
- required docs as mandatory deliverables
- docs under `docs/YYYY_MM_DD_中文任务名_vN/`
- refined internal gates: Init, Explore, Propose, Spec, Plan, Design, Atomize, Approve, Execute, Verify, and Archive
- implementation derived from approved specs
- pre-spec discovery and proposal work before formal spec finalization
- requirement, task, implementation, test, and acceptance traceability
- user clarification when the spec cannot safely determine behavior, scope, or acceptance
- explicit user confirmation of the spec bundle before code generation
- test-first implementation when the project test setup supports it
- post-verify archive and closure records
- no execution before the required spec bundle exists and the user has confirmed it

## Read next

- `references/sdd.md`
