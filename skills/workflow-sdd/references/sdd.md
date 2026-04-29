# SDD Workflow

## When to use

Use when the task is clearly about spec-driven development, spec-first delivery, or a spec-plan-implement loop where implementation, tests, and acceptance must derive from an approved spec.

## Activation

When the user input contains `@SDD`, legacy alias `@sdd`, or clearly requests specification-driven development, output exactly:

> ✅ Specification-Driven Development 工作流（SDD）已激活
> 当前阶段：Spec（规格定义）

## Core principle

The specification is the source of truth. Init, exploration, proposal, plan, design, tasks, implementation, tests, acceptance, and archive must stay traceable to the approved spec bundle once it is confirmed.

## Required documents

Create or update these files under `docs/YYYY_MM_DD_中文任务名_vN/` in the active project root. The parent directory carries the task name; file names use the workflow stage meaning.

Core required bundle:

- `01_SPEC_规格定义.md`
- `02_PLAN_实施计划.md`
- `03_DESIGN_架构设计.md`
- `04_TASK_任务拆分.md`
- `05_APPROVE_审批确认.md`
- `06_IMPLEMENTATION_LOG_实施记录.md`
- `07_ACCEPTANCE_验收记录.md`
- `08_FINAL_最终报告.md`

Recommended supporting docs for the refined SDD flow:

- `00_INIT_CONTEXT_项目接入.md`
- `00_EXPLORE_现状分析.md`
- `00_PROPOSE_变更提案.md`
- `09_ARCHIVE_归档记录.md`

## Recommended starter templates

- `references/templates/00_INIT_CONTEXT.template.md`
- `references/templates/00_EXPLORE.template.md`
- `references/templates/00_PROPOSE.template.md`
- `references/templates/01_SPEC.template.md`
- `references/templates/07_ACCEPTANCE.template.md`
- `references/templates/08_FINAL.template.md`
- `references/templates/09_ARCHIVE.template.md`

## Stage gates

- Init: capture active project root, stack, test/build setup, and blocking environment gaps.
- Explore: record current behavior, affected modules, constraints, and verified facts vs unknowns.
- Propose: define problem statement, scope, non-goals, rollout posture, rollback posture, and major risks.
- Spec: create an explicit, testable spec with goals, non-goals, scope, requirements, constraints, acceptance criteria, risks, and open questions.
- Plan: derive milestones, dependencies, worker routing, environment needs, validation strategy, and risk controls from the spec.
- Design: define architecture, components, interfaces, data flow, error handling, and spec-traced design decisions.
- Atomize: split work into spec-traceable tasks with contracts, dependencies, validation, and acceptance criteria.
- Approve: review spec completeness, consistency, feasibility, risk, security, testability, and acceptance traceability.
- Execute: implement from approved tasks, record implementation evidence, tests, validation, blockers, and spec trace.
- Verify: validate implementation against acceptance criteria and produce acceptance and final reports.
- Archive: preserve final closure and audit history without reopening scope.

## Rules

- use the current date and append a bundle version, for example `docs/2026_04_16_支付重构_v1/`
- if the same topic is rerun, increment to `v2`, `v3`, and so on
- use Init, Explore, and Propose when project context, current behavior, or scope boundaries are not already clear
- initialize `01_SPEC_规格定义.md` using the bundled template when useful
- block implementation until `01_SPEC_规格定义.md`, `02_PLAN_实施计划.md`, and `05_APPROVE_审批确认.md` exist
- output the spec bundle and wait for explicit user confirmation before generating or modifying code
- every plan item, design decision, task, implementation note, test, and acceptance result should trace to the spec
- keep supporting docs synchronized with the core spec bundle when they exist
- do not introduce requirements outside the approved spec
- if code changes are planned or completed, record target file paths, line ranges, before context, after context, and spec trace
- prefer test-first implementation when the project has a usable test setup
- stop and return for clarification if the spec is not strong enough to derive tasks
