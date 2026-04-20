# SDD Workflow

## When to use

Use when the task is clearly about spec-driven development, spec-first delivery, or a spec-plan-implement loop where implementation, tests, and acceptance must derive from an approved spec.

## Activation

When the user input contains `@sdd`, or clearly requests spec-driven development, output exactly:

> ✅ Spec-Driven Development 工作流（SDD）已激活
> 当前阶段：Spec（规格定义）

## Core principle

The specification is the source of truth. Plan, design, tasks, implementation, tests, and acceptance must derive from the approved spec bundle.

## Required documents

Create or update these files under `docs/YYYY_MM_DD_中文任务名_vN/` in the active project root. The parent directory carries the task name; file names use the workflow stage meaning:

- `01_SPEC_规格定义.md`
- `02_PLAN_实施计划.md`
- `03_DESIGN_架构设计.md`
- `04_TASK_任务拆分.md`
- `05_APPROVE_审批确认.md`
- `06_IMPLEMENTATION_LOG_实施记录.md`
- `07_ACCEPTANCE_验收记录.md`
- `08_FINAL_最终报告.md`

## Stage gates

- Spec: create an explicit, testable spec with goals, non-goals, scope, requirements, constraints, acceptance criteria, risks, and open questions.
- Plan: derive milestones, dependencies, worker routing, environment needs, validation strategy, and risk controls from the spec.
- Design: define architecture, components, interfaces, data flow, error handling, and spec-traced design decisions.
- Atomize: split work into spec-traceable tasks with contracts, dependencies, validation, and acceptance criteria.
- Approve: review spec completeness, consistency, feasibility, risk, security, testability, and acceptance traceability.
- Execute: implement from approved tasks, record implementation evidence, tests, validation, blockers, and spec trace.
- Verify: validate implementation against acceptance criteria and produce acceptance and final reports.

## Rules

- use the current date and append a bundle version, for example `docs/2026_04_16_支付重构_v1/`
- if the same topic is rerun, increment to `v2`, `v3`, and so on
- initialize `01_SPEC_规格定义.md` using the bundled template when useful
- block implementation until `01_SPEC_规格定义.md`, `02_PLAN_实施计划.md`, and `05_APPROVE_审批确认.md` exist
- output the spec bundle and wait for explicit user confirmation before generating or modifying code
- every plan item, design decision, task, implementation note, test, and acceptance result should trace to the spec
- do not introduce requirements outside the approved spec
- if code changes are planned or completed, record target file paths, line ranges, before context, after context, and spec trace
- prefer test-first implementation when the project has a usable test setup
- stop and return for clarification if the spec is not strong enough to derive tasks
