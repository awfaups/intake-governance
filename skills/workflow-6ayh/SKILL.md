---
name: workflow-6ayh
description: Standalone 6AYH workflow skill for progressive optimization and refactor work. Use when the task is already confirmed as 6AYH, the user explicitly requests @6AYH, or the request is clearly about gradual optimization, refactoring, maintenance-cost reduction, or performance cleanup. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow 6AYH

Use this skill when the workflow type is already known to be `6AYH`.

If the request still needs global intake, routing, or cross-role governance, enter through `@intake` first and use this skill as the workflow detail layer.

Activation response:

> ✅ 6A 优化工作流（6AYH · 前端渐进式优化模式）已激活
> 当前阶段：Align（目标与风险对齐）

This skill enforces:

- progressive optimization only
- required docs as mandatory deliverables
- docs under `docs/YYYY_MM_DD_中文任务名_vN/`
- Align, Architect, Atomize, Approve, Automate, and Assess gates
- current-state and risk analysis before design
- explicit behavior-preservation and rollback expectations
- user clarification for contract changes, risky changes, or preference-heavy decisions
- explicit user confirmation of the document bundle before code generation
- characterization tests before refactoring when existing behavior is underspecified
- code-change records with file path, line range, before context, and after context
- no execution before workflow docs exist and the user has confirmed them

Read next: `references/6ayh.md`
