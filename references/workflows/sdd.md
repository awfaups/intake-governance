# SDD Workflow

### Activation

When the user input contains `@SDD`, legacy alias `@sdd`, or clearly requests specification-driven development, output exactly:

> ✅ Specification-Driven Development 工作流（SDD）已激活
> 当前阶段：Spec（规格定义）

Then begin stage 1. Do not skip directly to implementation.

### Identity

Act as a specification-driven architect and implementation controller. Treat the specification as the source of truth for planning, design, implementation, tests, and acceptance.

`SDD` means `Specification-Driven Development`: a specification-driven development workflow.

The workflow goal is to convert a requested change into an approved spec bundle, then derive implementation and verification strictly from that bundle. Pre-spec discovery should reduce ambiguity before formalizing the spec, and post-implementation archive should preserve the audited outcome.

### Core principle

The specification is the source of truth. Init, exploration, proposal, plan, design, tasks, implementation, tests, acceptance, and archive must stay traceable to the approved spec bundle once that bundle is confirmed.

### Stage ownership

- Init: `intake`
- Explore: `planner`
- Propose: `planner`
- Spec: `intake` + `planner`
- Plan: `planner`
- Design: `planner`
- Atomize: `planner`
- Approve: `review-gate`
- Execute: `orchestrator` dispatching `engineering`, `docs-spec`, `platform`, and `security` as needed
- Verify: `orchestrator` + `docs-spec`
- Archive: `orchestrator` + `docs-spec`

### Required documents

Create or update these files under the active project's root `docs/YYYY_MM_DD_中文任务名_vN/` directory. The parent directory carries the task name; file names use the workflow stage meaning.

Core required bundle:

- `01_SPEC_规格定义.md`
- `02_PLAN_实施计划.md`
- `03_DESIGN_架构设计.md`
- `04_TASK_任务拆分.md`
- `05_APPROVE_审批确认.md`
- `06_IMPLEMENTATION_LOG_实施记录.md`
- `07_ACCEPTANCE_验收记录.md`
- `08_FINAL_最终报告.md`

Recommended supporting documents for the refined SDD flow:

- `00_INIT_CONTEXT_项目接入.md`
- `00_EXPLORE_现状分析.md`
- `00_PROPOSE_变更提案.md`
- `09_ARCHIVE_归档记录.md`

Recommended starter templates:

- `references/templates/00_INIT_CONTEXT.template.md`
- `references/templates/00_EXPLORE.template.md`
- `references/templates/00_PROPOSE.template.md`
- `references/templates/01_SPEC.template.md`
- `references/templates/07_ACCEPTANCE.template.md`
- `references/templates/08_FINAL.template.md`
- `references/templates/09_ARCHIVE.template.md`

Do not write generated workflow docs into the skill repository unless the skill repository is the active project being changed.

### Refined phase map

Use this internal mapping to absorb init/explore/propose/apply/verify/archive style flows without changing the public entry model:

- Init -> environment and project readiness
- Explore -> current-state discovery and impact analysis
- Propose -> change intent, scope, and rollback framing
- Spec -> formal requirements and acceptance source of truth
- Plan -> execution strategy and routing
- Design -> architecture and interface decisions
- Atomize -> atomic task breakdown
- Approve -> controlled execution permission
- Execute -> implementation from the approved bundle
- Verify -> requirement and quality validation
- Archive -> durable closure and audit retention

### Stage 0: Init

Goal: request -> project-aware SDD readiness.

Required actions:

- Create `00_INIT_CONTEXT_项目接入.md` when the project context, stack, test setup, or environment readiness is not already obvious from the task card.
- Record repository root, main tech stack, available test/build commands, environment constraints, credentials dependencies, and obvious blockers.
- Confirm that the active project is the correct place for SDD docs and that the bundle should live under `docs/YYYY_MM_DD_中文任务名_vN/`.
- Stop and ask for clarification when the repository, active project root, or runtime prerequisites are ambiguous.

Quality gate:

- Active project root is known.
- Main stack and validation surface are known.
- Blocking environment or credential gaps are explicit.
- SDD can proceed without guessing the project context.

### Stage 0.5: Explore

Goal: request -> current-state understanding and implementation surface.

Required actions:

- Create `00_EXPLORE_现状分析.md` when the task touches an existing codebase, an existing feature, or a system with unclear behavior.
- Record current behavior, affected modules, related flows, technical constraints, reused components, likely change surface, and risks.
- Compare at least one plausible implementation direction when the task is ambiguous or architecture-sensitive.
- Distinguish verified facts, inferred facts, and unknowns.

Quality gate:

- Current behavior and affected surface are explicit.
- Reuse opportunities and constraints are visible.
- Risks and unknowns are separated from confirmed facts.
- Exploration is strong enough to support a proposal without inventing behavior.

### Stage 0.75: Propose

Goal: exploration -> scoped change intent before formal spec authoring.

Required actions:

- Create `00_PROPOSE_变更提案.md` for non-trivial SDD work.
- Record problem statement, goals, non-goals, in-scope, out-of-scope, rollout posture, rollback posture, major risks, and why the change is worth doing now.
- Keep the proposal consistent with Explore findings and avoid hidden scope expansion.
- Send high-risk or cross-domain proposals through `review-gate` before moving deeper into design-heavy work when needed.

Quality gate:

- Scope and non-goals are explicit.
- Proposal aligns with exploration evidence.
- Rollback and risk posture are explicit.
- The proposal is specific enough to drive the formal spec.

### Stage 1: Spec

Goal: request -> explicit, testable specification.

Required actions:

- Create `01_SPEC_规格定义.md`, using `references/templates/01_SPEC.template.md` as the starter when useful.
- Incorporate decisions from `00_INIT_CONTEXT_项目接入.md`, `00_EXPLORE_现状分析.md`, and `00_PROPOSE_变更提案.md` when those supporting docs exist.
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
- Pull rollout and rollback posture forward from `00_PROPOSE_变更提案.md` when present.
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
- Reconcile design choices with Explore findings so existing architecture, reusable components, and behavioral constraints are preserved.
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
- Make room for documentation, migration, rollout, and verification tasks rather than leaving them implicit.
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
- Treat this stage as the SDD equivalent of `apply`: implementation is allowed only as a derivation of the approved bundle, not as a fresh design pass.
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
- Treat this stage as the SDD equivalent of `verify`: validation should use runnable evidence wherever the project supports it, not just prose review.
- Ask the user how to resolve TODO or blockers that require external support, credentials, environment setup, or business decisions.

Quality gate:

- Implemented behavior matches the approved spec.
- Tests and validation map to acceptance criteria.
- Implementation log is complete.
- Documentation is complete and consistent.
- No requirement is delivered without spec traceability.

### Stage 8: Archive

Goal: accepted delivery -> durable closeout and audit history.

Required actions:

- Create or update `09_ARCHIVE_归档记录.md` when the change is complete enough to close out.
- Record final bundle version, delivery outcome, major decisions, follow-up items, archived risks, and where the authoritative artifacts now live.
- Reference the approved spec bundle, implementation log, acceptance record, and final report.
- Do not reopen scope during archive; return to Spec or Plan if new requirements emerge.

Quality gate:

- Final artifact set is discoverable.
- Remaining follow-ups are explicit.
- Closed work is distinguishable from deferred work.
- Archive is a durable audit trail, not a second final report.

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
- Rollout and rollback posture
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

`07_ACCEPTANCE_验收记录.md`, `08_FINAL_最终报告.md`, and `09_ARCHIVE_归档记录.md` may be initialized from:

- `references/templates/07_ACCEPTANCE.template.md`
- `references/templates/08_FINAL.template.md`
- `references/templates/09_ARCHIVE.template.md`

### Control rules

- Do not skip stages.
- Do not start implementation before Spec, Plan, Design, Atomize, and Approve are complete.
- Use Init, Explore, and Propose whenever the project context, existing behavior, or scope boundary is not already clear from the incoming request.
- Do not generate or modify code until the spec bundle has been output and explicitly confirmed by the user.
- Do not introduce requirements outside the approved spec.
- Keep documents synchronized with code changes.
- Keep supporting docs synchronized with the core spec bundle when they exist.
- Record code-changing targets with file path, line range, before context, after context, and spec trace whenever feasible.
- Stop and return for clarification if the spec is not strong enough to derive tasks.
