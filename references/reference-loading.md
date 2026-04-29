# Reference Loading Map

This package should be read like a router with optional detail modules.

Start with `SKILL.md`. Load additional files only when the current turn needs them.

## Read by need

- Need to classify an external request or normalize an alias:
  - `references/intake-classification.md`
  - `references/workflow-routing.json`
  - `references/workflow-naming.md`

- Need to validate who can send to whom:
  - `references/agents.json`
  - `references/role-permissions.md`

- Need task-card or handoff structure:
  - `references/task-card.schema.json`
  - `references/handoff-record.schema.json`
  - `references/status-transitions.json`

- Need starter examples for prompts or payloads:
  - `references/activation-examples.md`
  - `references/activation-examples.json`
  - `references/task-card.example.json`
  - `references/handoff-record.example.json`

- Need repeatable package validation:
  - `references/regression-checklist.md`
  - `scripts/validate_governance_skill.py`
  - `scripts/smoke_test_prompts.py`
  - `scripts/sync_installed_skill.py`

- Need department routing or dispatch rules:
  - `references/routing-rules.json`
  - `references/workflow-routing.json`
  - `references/workflow-naming.md`

- Need workflow-specific execution contracts:
  - `references/workflows/6a.md`
  - `references/workflows/6ayh.md`
  - `references/workflows/ppw.md`
  - `references/workflows/sdd.md`
  - `references/workflows/generic-governance.md`

- Need role phrasing or response style:
  - `references/role-prompts.json`
  - `references/engineering-governance.md`

- Need to maintain or extend this package:
  - `references/maintainer-upgrade-guide.md`

## Do not preload everything

- Do not load every workflow file just because the package triggered.
- Do not load Chinese companion docs unless the user explicitly wants Chinese wording.
- Do not read the whole repository when a single schema or workflow file is enough.

## Package shape

- `SKILL.md` is the runtime console.
- `references/` contains rules, schemas, and workflow contracts.
- `references/` also contains small example artifacts for maintenance and regression checks.
- `scripts/` contains deterministic maintenance helpers when prose alone is too fragile.
- `skills/workflow-*` are detail layers for already-selected workflows.
- `agents/openai.yaml` is UI metadata, not runtime policy.
