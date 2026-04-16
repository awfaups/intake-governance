# PPW Workflow

## When to use

Use when the task is clearly about project inventory, current-state clarification, asset mapping, process discovery, contract discovery, risk inventory, or roadmap preparation.

## Activation

When the user input contains `@PPW` or clearly requests project-process inventory, output exactly:

> ✅ 项目流程梳理工作流（PPW）已激活
> 当前阶段：A1 – 项目资产盘点（Inventory）

## Required documents

Create or update these files under `docs/YYYY_MM_DD_中文任务名_vN/` in the active project root. The parent directory carries the task name; file names use the workflow stage meaning:

- `01_INVENTORY_资产盘点.md`
- `02_GOALS_目标梳理.md`
- `03_FLOWS_流程梳理.md`
- `04_CONTRACTS_契约梳理.md`
- `05_RISK_REGISTER_风险登记.md`
- `06_ROADMAP_路线图.md`
- `07_CONSENSUS_共识确认.md`
- `08_DECISIONS_决策记录.md`

## Stage gates

- A1 Inventory: map repositories, modules, entry points, services, scripts, configs, docs, owners, dependencies, environments, and missing access.
- A2 Goals: clarify goals, non-goals, stakeholders, scope boundaries, and success criteria.
- A3 Flows: map user, data, build, deployment, release, operational, and responsibility flows.
- A4 Contracts: record API, config, data, deployment, ownership, and process contracts.
- A5 Risks: identify technical, operational, security, compliance, data, dependency, ownership, and process risks.
- A6 Roadmap: prioritize blockers, gaps, documentation work, decision needs, access needs, and candidate follow-up workflows.
- A7 Sign-off: create consensus and decision logs with confirmed facts, assumptions, open questions, and next steps.

## Rules

- use the current date and append a bundle version, for example `docs/2026_04_16_项目流程梳理_v1/`
- if the same project topic is rerun, increment to `v2`, `v3`, and so on
- keep output factual, traceable, and evidence-based
- separate verified facts, inferred facts, and unknowns
- do not invent facts, owners, contracts, or roadmap items
- do not start code implementation inside PPW
- recommend `6A`, `6AYH`, `SDD`, or `generic_governance` only when evidence supports it
- stop before deeper planning if critical repositories, configs, credentials, or provenance are missing
