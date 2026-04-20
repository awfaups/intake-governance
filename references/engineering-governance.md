# Engineering Governance For Role-Based Agent Governance

This reference adapts engineering-governance discipline into the layered role model used by this skill.

### Purpose

Use AI as a controlled, auditable, engineering-disciplined team member.

Default objectives:

- controlled execution
- auditable decisions
- explicit risk handling
- workflow-based delivery

### Role mapping

`intake` owns:

- request intake
- requirement contracting
- intent extraction
- workflow alias detection
- the `Understand` stage

`planner` owns:

- planning
- architecture
- option comparison
- task decomposition
- the `Plan` stage

`review-gate` owns:

- quality review
- risk gating
- policy fit
- approval or rejection

`orchestrator` owns:

- dispatch
- execution coordination
- artifact aggregation
- final reporting

Worker departments own domain execution only:

- `engineering`
- `docs-spec`
- `data-ops`
- `security`
- `platform`
- `governance`

### Engineering principles

Apply these principles by default:

- KISS
- YAGNI
- DRY
- SOLID where useful, not ritualistically
- explicit scope boundaries
- observable outcomes
- reversible changes when risk is non-trivial

### Planning discipline

When the task is non-trivial, `planner` should:

- provide at least two viable options where comparison matters
- compare complexity, risk, cost, and delivery speed
- define acceptance criteria
- identify dependencies and rollback constraints
- identify which worker departments are needed

### Review discipline

`review-gate` should check:

- whether assumptions are valid
- whether risk is bounded
- whether destructive changes require explicit approval
- whether acceptance criteria are testable
- whether the chosen plan still matches the requested scope

If the plan fails review:

- emit `rejection_reason`
- emit `required_fixes` when revision is possible
- return the task to `planner`

### Execution discipline

`orchestrator` should:

- dispatch only according to routing rules
- keep worker outputs scoped to the assigned domain
- require every worker to return evidence, not final closure
- aggregate all results before completion
- keep workflow-document status visible for governed workflows

When code changes are involved:

- output or update the required workflow documents before code generation
- present the document bundle summary to the user and wait for explicit confirmation
- keep `user_confirmation.status=pending` until the user confirms the documents
- do not dispatch `engineering`, generate code, or edit code until `user_confirmation.status=confirmed`
- record target file paths
- record line ranges
- record before context
- record after context
- keep those records in workflow docs and task-card artifacts

### Delivery discipline

A task is not complete until:

- required workflow documents exist and are updated
- required worker outputs are received
- risks and open items are summarized
- the final result is aggregated by `orchestrator`
