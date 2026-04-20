# 6AYH Workflow

## When to use

Use when the task is clearly about gradual optimization, refactoring, performance work, state cleanup, dependency cleanup, or reducing maintenance cost without a big rewrite.

## Activation

When the user input contains `@6AYH`, output exactly:

> ✅ 6A 优化工作流（6AYH · 前端渐进式优化模式）已激活
> 当前阶段：Align（目标与风险对齐）

## Required documents

Create or update these files under `docs/YYYY_MM_DD_中文任务名_vN/` in the active project root. The parent directory carries the task name; file names use the workflow stage meaning:

- `01_ALIGNMENT_目标与风险对齐.md`
- `02_DESIGN_优化设计.md`
- `03_TASK_优化任务拆分.md`
- `04_APPROVE_审批确认.md`
- `05_ACCEPTANCE_验收记录.md`
- `06_FINAL_最终报告.md`
- `07_TODO_待办清单.md`
- `99_REFERENCES_参考资料.md`

## Stage gates

- Align: analyze current implementation, symptoms, baseline evidence, behavior contracts, risks, and rollback expectations.
- Architect: design a progressive, reversible optimization strategy with compatibility and validation plans.
- Atomize: split into safe tasks with target files, validation, rollback notes, and dependency graph.
- Approve: review behavior preservation, contract compatibility, rollback practicality, risk, and testability.
- Automate: execute tasks in dependency order, update tests, run validation, and keep acceptance docs synchronized.
- Assess: verify compatibility, tests, improvement evidence, rollback notes, final report, TODO, and references.

## Rules

- use the current date and append a bundle version, for example `docs/2026_04_16_首页优化_v1/`
- if the same feature is optimized again, increment to `v2`, `v3`, and so on
- initialize the doc skeleton before optimization work
- output the document bundle and wait for explicit user confirmation before generating or modifying code
- prefer progressive and reversible changes over rewrites
- preserve existing behavior and external contracts unless explicitly approved
- ask the user when a change may alter user-visible behavior, public API contracts, data semantics, deployment behavior, or product preference
- prefer characterization tests before refactoring when existing behavior is underspecified
- every optimization step must have validation, and code-changing steps should have rollback or containment notes
- any code-changing stage must document target file paths, line ranges, and before/after code context
- if approval fails, return to design or task breakdown before executing
