---
name: workflow-ppw
description: Standalone PPW workflow skill for project inventory and process clarification. Use when the task is already confirmed as PPW, the user explicitly requests @PPW, or the request is clearly about project inventory, asset mapping, current-state clarification, or process discovery. Produces dated and versioned workflow docs under the active project's root docs/YYYY_MM_DD_中文任务名_vN/ directory.
---

# Workflow PPW

Use this skill when the workflow type is already known to be `PPW`.

If the request still needs global intake, routing, or cross-role governance, enter through `@intake` first and use this skill as the workflow detail layer.

Activation response:

> ✅ 项目流程梳理工作流（PPW）已激活
> 当前阶段：A1 – 项目资产盘点（Inventory）

This skill enforces:

- inventory and process-clarification workflow only
- required docs as mandatory deliverables
- docs under `docs/YYYY_MM_DD_中文任务名_vN/`
- A1 Inventory, A2 Goals, A3 Flows, A4 Contracts, A5 Risks, A6 Roadmap, and A7 Sign-off gates
- fact-based output instead of speculative conclusions
- explicit separation of verified facts, inferred facts, and unknowns
- traceable evidence for important claims
- no implementation inside PPW
- later code-changing workflows must wait for explicit user confirmation of their documents before code generation
- stop before deeper planning when critical repositories, configs, credentials, or provenance are missing

Read next: `references/ppw.md`
