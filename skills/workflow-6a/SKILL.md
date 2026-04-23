---
name: workflow-6a
description: 6A workflow detail layer for new feature development after workflow selection is known. Use when the task is already confirmed as 6A, the user explicitly requests @6A, or intake has classified the task as greenfield feature, page, or module development. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow 6A

Use this skill only when the workflow type is already known to be `6A`.

Treat this skill as a detail layer, not a public governance entry.

- If the request still needs intake, routing, or cross-role governance, enter through `@intake` first.
- Use this skill after workflow selection is settled.
- Keep global handoff policy in `intake-governance`; keep 6A stage rules here and in `references/6a.md`.

## Activation response

> 6A工作流已激活
> 当前阶段：Align（需求对齐）

## Execution contract

This skill enforces:

- new-feature workflow only
- required docs as mandatory deliverables
- docs under `docs/YYYY_MM_DD_中文任务名_vN/`
- Align, Architect, Atomize, Approve, Automate, and Assess gates
- project-context analysis before design
- user clarification for risky or preference-heavy decisions
- explicit user confirmation of the document bundle before code generation
- test-first implementation when the project test setup supports it
- code-change records with file path, line range, before context, and after context
- no implementation before workflow docs exist and the user has confirmed them

## Read next

- `references/6a.md`
