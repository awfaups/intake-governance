---
name: workflow-sdd
description: Standalone SDD workflow skill for spec-driven development. Use when the task is already confirmed as SDD, the user explicitly requests @sdd, or the request is clearly about spec-first delivery where implementation, tests, and acceptance must derive from an approved spec bundle. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow SDD

Use this skill when the workflow type is already known to be `SDD`.

If the request still needs global intake, routing, or cross-role governance, enter through `@intake` first and use this skill as the workflow detail layer.

Activation response:

> ✅ Spec-Driven Development 工作流（SDD）已激活
> 当前阶段：Spec（规格定义）

This skill enforces:

- spec-first workflow only
- required docs as mandatory deliverables
- docs under `docs/YYYY_MM_DD_中文任务名_vN/`
- Spec, Plan, Design, Atomize, Approve, Execute, and Verify gates
- implementation derived from approved specs
- requirement, task, implementation, test, and acceptance traceability
- user clarification when the spec cannot safely determine behavior, scope, or acceptance
- explicit user confirmation of the spec bundle before code generation
- test-first implementation when the project test setup supports it
- no execution before the required spec bundle exists and the user has confirmed it

Read next: `references/sdd.md`
