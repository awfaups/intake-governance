# Intake Governance

Portable multi-agent governance skill for role-based planning, review, dispatch, and execution.

This repository is a reusable skill package, not an application or SDK. It provides an intake-first operating model for complex agent collaboration, with explicit role boundaries, workflow routing, document gates, and schema-backed handoffs.

Chinese documentation is also included:

- [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
- [BEGINNER_GUIDE.zh-CN.md](BEGINNER_GUIDE.zh-CN.md)
- [TEAM_SHARE_MULTI_AGENT_GOVERNANCE.zh-CN.md](TEAM_SHARE_MULTI_AGENT_GOVERNANCE.zh-CN.md)

## What this package contains

The repository currently includes:

- one root governance skill: `SKILL.md`
- four standalone workflow detail skills:
  - `workflow-6a`
  - `workflow-6ayh`
  - `workflow-ppw`
  - `workflow-sdd`
- governance references, schemas, examples, and routing rules under `references/`
- validation and sync scripts under `scripts/`
- a lightweight app-facing surface in `agents/openai.yaml`

## Core model

The role system is:

- `intake`: entry hub
- `planner`: planning office
- `review-gate`: quality and risk gate
- `orchestrator`: dispatch hub
- worker departments: `data-ops`, `docs-spec`, `engineering`, `security`, `platform`, `governance`

Default flow for substantial tasks:

```text
intake -> planner -> review-gate? -> orchestrator -> worker(s) -> orchestrator
```

## Entry rule

`intake` is the only public entry point.

External requests must not bypass directly to `planner`, `review-gate`, `orchestrator`, or any worker department.

Accepted entry patterns:

- `@intake`
- governance aliases that must still normalize back to `intake` first:
  - `@init`
  - `@plan`
  - `@refactor`
  - `@risk`
  - `@decision`
  - `@audit`
  - `@ask`
  - `@ppw`
  - `@6A`
  - `@6AYH`
  - `@PPW`
  - `@sdd`

If `intake` classifies the request into `6A`, `6AYH`, `PPW`, or `SDD`, it must emit that workflow's fixed activation response before any additional planning text.

## Workflow modes

`intake` first classifies work into one of these modes:

- `6A`: new feature development
- `6AYH`: progressive optimization and refactor
- `PPW`: project inventory and process clarification
- `SDD`: spec-driven development
- `generic_governance`: governance routing without a workflow-specific contract

The standalone workflow skills are detail layers, not public entry points. They are meant to be used only after workflow selection is already known.

## Document gate

For `6A`, `6AYH`, `PPW`, and `SDD`:

- required workflow docs are mandatory deliverables
- docs must live under the active project's root `docs/YYYY_MM_DD_中文任务名_vN/`
- generated workflow docs should not be written into this skill repository unless this repository is the active project being changed
- if code changes are involved, workflow docs must record file path, line range, before context, and after context
- the document bundle must be presented to the user before any implementation starts
- `user_confirmation.status` must stay `pending` until the user explicitly confirms
- code generation, code edits, and `engineering` dispatch must stay blocked until `user_confirmation.status=confirmed`

## Required task card shape

This package expects structured handoff artifacts rather than free-form delegation prose.

Minimum required task-card fields:

- `task_id`
- `title`
- `from`
- `to`
- `goal`
- `brief`
- `tags`
- `constraints`
- `deliverables`
- `review_required`
- `workflow_mode`
- `current_stage`
- `required_documents`
- `document_status`
- `document_bundle_version`
- `user_confirmation`
- `code_change_targets`
- `handoff_history`
- `status`

Source of truth:

- [references/task-card.schema.json](references/task-card.schema.json)
- [references/handoff-record.schema.json](references/handoff-record.schema.json)
- [references/status-transitions.json](references/status-transitions.json)

## Repository layout

```text
.
├── README.md
├── SKILL.md
├── OVERVIEW.md
├── BEGINNER_GUIDE.md
├── PUBLISHING.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── activation-examples.json
│   ├── activation-examples.md
│   ├── agents.json
│   ├── engineering-governance.md
│   ├── handoff-record.example.json
│   ├── handoff-record.schema.json
│   ├── intake-classification.md
│   ├── maintainer-upgrade-guide.md
│   ├── reference-loading.md
│   ├── regression-checklist.md
│   ├── role-permissions.md
│   ├── role-prompts.json
│   ├── routing-rules.json
│   ├── status-transitions.json
│   ├── task-card.example.json
│   ├── task-card.schema.json
│   ├── templates/
│   │   └── 01_SPEC.template.md
│   ├── workflow-routing.json
│   └── workflows/
│       ├── 6a.md
│       ├── 6ayh.md
│       ├── ppw.md
│       └── sdd.md
├── scripts/
│   ├── smoke_test_prompts.py
│   ├── sync_installed_skill.py
│   └── validate_governance_skill.py
└── skills/
    ├── workflow-6a/
    ├── workflow-6ayh/
    ├── workflow-ppw/
    └── workflow-sdd/
```

## Install

Clone or copy this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/intake-governance ~/.codex/skills/intake-governance
```

Then restart Codex so the skill is reloaded.

## Validate and sync

Validate the package:

```bash
python3 scripts/validate_governance_skill.py
```

Validate and compare with an installed copy:

```bash
python3 scripts/validate_governance_skill.py --compare-installed
```

Sync the runtime-relevant files into the installed skill copy:

```bash
python3 scripts/sync_installed_skill.py
```

The validator currently checks:

- required files exist
- JSON references parse correctly
- example artifacts satisfy required schema keys
- `agents/openai.yaml` parses as YAML
- prompt smoke tests still match routing expectations

## First prompt

Example:

```text
@intake Help me plan a feature that spans frontend, documentation, and deployment
```

Expected behavior:

1. `intake` normalizes the request and classifies the workflow.
2. `planner` decomposes the task and identifies the required departments.
3. `review-gate` is used if the task is risky, cross-functional, or ambiguous.
4. `orchestrator` dispatches work and aggregates returns.
5. Workers report only back to `orchestrator`.

## Related docs

- [OVERVIEW.md](OVERVIEW.md)
- [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)
- [references/engineering-governance.md](references/engineering-governance.md)
- [references/maintainer-upgrade-guide.md](references/maintainer-upgrade-guide.md)
- [PUBLISHING.md](PUBLISHING.md)

## Publishing note

If this repository is being published as a shareable public skill, keep `SKILL.md` lean, move detailed rules into `references/`, and keep workflow-specific behavior in `skills/workflow-*`.
