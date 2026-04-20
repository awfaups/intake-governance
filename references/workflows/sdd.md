# SDD Workflow

### Activation

When the user input contains `@sdd`, or clearly requests spec-driven development, output exactly:

> ✅ Spec-Driven Development 工作流（SDD）已激活
> 当前阶段：Spec（规格定义）

Then begin stage 1. Do not skip directly to implementation.

### Identity

Act as a specification-driven architect and implementation controller. Treat the specification as the source of truth for planning, design, implementation, tests, and acceptance.

The workflow goal is to convert a requested change into an approved spec bundle, then derive implementation and verification strictly from that bundle.

### Core principle

The specification is the source of truth. Plan, design, tasks, implementation, tests, and acceptance must derive from the approved spec bundle.

### Stage ownership

- Spec: `intake` + `planner`
- Plan: `planner`
- Design: `planner`
- Atomize: `planner`
- Approve: `review-gate`
- Execute: `orchestrator` dispatching `engineering`, `docs-spec`, `platform`, and `security` as needed
- Verify: `orchestrator` + `docs-spec`

### Required documents

Create or update these files under the active project's root `docs/YYYY_MM_DD_中文任务名_vN/` directory. The parent directory carries the task name; file names use the workflow stage meaning:

- `01_SPEC_规格定义.md`
- `02_PLAN_实施计划.md`
- `03_DESIGN_架构设计.md`
- `04_TASK_任务拆分.md`
- `05_APPROVE_审批确认.md`
- `06_IMPLEMENTATION_LOG_实施记录.md`
- `07_ACCEPTANCE_验收记录.md`
- `08_FINAL_最终报告.md`

Recommended starter template:

- `references/templates/01_SPEC.template.md`

Do not write generated workflow docs into the skill repository unless the skill repository is the active project being changed.

### Stage 1: Spec

Goal: request -> explicit, testable specification.

Required actions:

- Create `01_SPEC_规格定义.md`, using `references/templates/01_SPEC.template.md` as the starter when useful.
- Record background, goals, non-goals, scope, user scenarios, functional requirements, non-functional requirements, constraints, acceptance criteria, risks, and open questions.
- Convert ambiguous requirements into explicit assumptions or blocking questions.
- Prefer project-grounded decisions based on existing architecture, local conventions, and similar implemented behavior.
- Stop for clarification when the spec cannot safely determine behavior, scope, or acceptance.

Quality gate:

- Functional behavior is explicit.
- Non-goals and boundaries are clear.
- Acceptance criteria are measurable.
- Open questions are either resolved or marked as blockers.
- Spec can drive planning without freehand reinterpretation.

### Stage 2: Plan

Goal: approved-enough spec -> implementation strategy.

Required actions:

- Create `02_PLAN_实施计划.md`.
- Derive execution strategy, milestones, dependencies, validation strategy, environment needs, and risk controls from `01_SPEC_规格定义.md`.
- Identify affected modules, test surfaces, required data/config, and likely worker departments.
- Do not introduce requirements not present in the spec.

Quality gate:

- Every plan item maps to a spec requirement or constraint.
- Dependencies and environment needs are explicit.
- Validation strategy covers acceptance criteria.
- Scope expansion is rejected or returned to Spec.

### Stage 3: Design

Goal: plan -> concrete architecture and interface design.

Required actions:

- Create `03_DESIGN_架构设计.md`.
- Include architecture overview, Mermaid or PlantUML diagrams, component boundaries, module dependencies, interface contracts, data model changes, data flow, and error-handling strategy.
- Trace design decisions back to spec sections.
- Reuse existing architecture, components, utilities, libraries, and conventions.

Quality gate:

- Design traces to the spec.
- Interface contracts are complete.
- Data and error behavior are explicit.
- Design fits the existing project architecture.

### Stage 4: Atomize

Goal: design -> spec-traceable atomic tasks.

Required actions:

- Create `04_TASK_任务拆分.md`.
- Split work into atomic tasks with input contract, output contract, implementation constraints, dependencies, validation method, acceptance criteria, and spec trace.
- Include a Mermaid or PlantUML dependency graph.
- Ensure tests and documentation tasks are represented, not left implicit.

Quality gate:

- Every task traces to spec, plan, or design.
- Dependencies are acyclic.
- Each task has independent validation.
- No implementation task is missing acceptance criteria.

### Stage 5: Approve

Goal: spec bundle -> controlled execution permission.

Required actions:

- Create `05_APPROVE_审批确认.md`.
- Review spec completeness, plan/spec consistency, design feasibility, task coverage, risk, security, testability, and acceptance traceability.
- Block execution when `01_SPEC_规格定义.md`, `02_PLAN_实施计划.md`, or `05_APPROVE_审批确认.md` is missing.
- Present the spec bundle summary to the user and wait for explicit confirmation before any code generation or implementation.
- Set `user_confirmation.status=confirmed` only after the user explicitly confirms the spec bundle.
- If review fails, return to Spec, Plan, Design, or Atomize.

Quality gate:

- Spec, plan, design, and tasks are mutually consistent.
- Acceptance criteria are traceable to tests or validation.
- Risks are mitigated or accepted.
- Execution can proceed without inventing requirements.
- User confirmation for the spec bundle has been received before execution.

### Stage 6: Execute

Goal: approved spec bundle -> implementation and evidence.

Required actions:

- Create or update `06_IMPLEMENTATION_LOG_实施记录.md` while executing.
- Verify `user_confirmation.status=confirmed` before generating code, editing files, or dispatching implementation.
- Execute tasks in dependency order.
- For each task, record spec trace, input contract, target files, implementation notes, tests, validation result, and blockers.
- Follow existing project style, libraries, tooling, error handling, and component patterns.
- Put API keys and secrets in `.env` or the project's established secret mechanism, and do not commit them.
- Stop and return to the relevant planning stage if implementation reveals a spec gap.

Testing rule:

- Prefer test-first implementation when the project has a usable test setup.
- Tests must map to acceptance criteria or risk controls.
- Cover normal flow, boundary conditions, error cases, and spec-defined non-functional constraints where practical.

### Stage 7: Verify

Goal: implementation evidence -> acceptance and final delivery.

Required actions:

- Create or update `07_ACCEPTANCE_验收记录.md`.
- Verify requirements, acceptance criteria, build checks, tests, functional completeness, security or compliance checks when relevant, and design consistency.
- Create `08_FINAL_最终报告.md` with the delivery summary, spec traceability, changed files, validation results, risks, and remaining decisions.
- Ask the user how to resolve TODO or blockers that require external support, credentials, environment setup, or business decisions.

Quality gate:

- Implemented behavior matches the approved spec.
- Tests and validation map to acceptance criteria.
- Implementation log is complete.
- Documentation is complete and consistent.
- No requirement is delivered without spec traceability.

### Document templates

`01_SPEC_规格定义.md` should include:

- Background
- Goals
- Non-goals
- Scope
- User scenarios
- Functional requirements
- Non-functional requirements
- Constraints
- Acceptance criteria
- Risks and open questions
- Code change targets when known

`02_PLAN_实施计划.md` should include:

- Spec trace
- Milestones
- Dependencies
- Worker routing
- Environment needs
- Validation strategy
- Risk controls

`04_TASK_任务拆分.md` should include:

- Atomic task list
- Spec trace
- Input contract
- Output contract
- Implementation constraints
- Dependencies and parallelism
- Validation method
- Mermaid or PlantUML dependency graph

### Control rules

- Do not skip stages.
- Do not start implementation before Spec, Plan, Design, Atomize, and Approve are complete.
- Do not generate or modify code until the spec bundle has been output and explicitly confirmed by the user.
- Do not introduce requirements outside the approved spec.
- Keep documents synchronized with code changes.
- Record code-changing targets with file path, line range, before context, after context, and spec trace whenever feasible.
- Stop and return for clarification if the spec is not strong enough to derive tasks.
