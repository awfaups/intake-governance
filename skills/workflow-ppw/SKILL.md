---
name: workflow-ppw
description: PMW workflow detail layer for project inventory and process clarification after workflow selection is known. Use when the task is already confirmed as PMW, the user explicitly requests @PMW or legacy alias @PPW, or intake has classified the task as project inventory, asset mapping, current-state clarification, or process discovery. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow PMW

Use this skill only when the workflow type is already known to be `PMW`.

Treat this skill as a detail layer, not a public governance entry.

- If the request still needs intake, routing, or cross-role governance, enter through `@intake` first.
- Use this skill after workflow selection is settled.
- Keep global handoff policy in `intake-governance`; keep PMW stage rules here and in `references/ppw.md`.

## Activation response

> ✅ Project Mapping Workflow（PMW · 项目流程梳理工作流）已激活
> 当前阶段：A1 – 项目资产盘点（Inventory）

## Execution contract

This skill enforces:

- inventory and process-clarification workflow only
- required docs as mandatory deliverables
- docs under `docs/YYYY_MM_DD_中文任务名_vN/`
- A1 Inventory, A2 Goals, A3 Flows, A4 Contracts, A5 Risks, A6 Roadmap, and A7 Sign-off gates
- fact-based output instead of speculative conclusions
- explicit separation of verified facts, inferred facts, and unknowns
- traceable evidence for important claims
- no implementation inside PMW
- later code-changing workflows must wait for explicit user confirmation of their documents before code generation
- stop before deeper planning when critical repositories, configs, credentials, or provenance are missing

## Read next

- `references/ppw.md`
