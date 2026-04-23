# Maintainer Upgrade Guide

Use this guide when the task is to evolve `role-based-agent-governance` itself rather than to run it on a user task.

## Design stance

Keep the package shaped like a runtime router:

- one public entry
- clear internal routing
- lean root instructions
- detailed rules in references
- workflow-specific depth in dedicated subskills

This mirrors the strongest part of command-runner skills such as OpenProse: the entry surface stays simple while the behavior stays extensible.

## Preferred upgrade order

1. Tighten trigger metadata in `SKILL.md` frontmatter.
2. Keep `SKILL.md` focused on entry rules, routing, document gates, and what to read next.
3. Move detailed policy, schemas, and examples into `references/`.
4. Keep workflow-specific behavior in `skills/workflow-*`.
5. Add or update deterministic validation in `scripts/` when repeated checks are emerging.
6. Update `agents/openai.yaml` if the user-facing positioning changed.

## Good changes

- add a missing routing rule
- add a new schema-backed field
- improve alias normalization
- add a minimal example artifact when a schema is hard to apply from prose alone
- split verbose guidance out of `SKILL.md`
- add a missing maintainer or loading reference
- clarify which file is the source of truth for a decision
- add a small validation script when consistency checks are repeated by hand

## Bad changes

- creating alternative public entry roles
- duplicating the same rule across `SKILL.md`, workflow skills, and references
- embedding long examples in `SKILL.md` when a reference file would do
- letting worker departments define cross-department routing
- mixing package-maintenance instructions into normal runtime flow

## Consistency checklist

When changing the package, verify these files together:

- `SKILL.md`
- `references/intake-classification.md`
- `references/workflow-routing.json`
- `references/task-card.schema.json`
- `references/task-card.example.json`
- `references/handoff-record.example.json`
- `references/activation-examples.json`
- `references/status-transitions.json`
- `references/role-permissions.md`
- `references/regression-checklist.md`
- `scripts/validate_governance_skill.py`
- `scripts/smoke_test_prompts.py`
- `scripts/sync_installed_skill.py`
- `skills/workflow-6a/SKILL.md`
- `skills/workflow-6ayh/SKILL.md`
- `skills/workflow-ppw/SKILL.md`
- `skills/workflow-sdd/SKILL.md`
- `agents/openai.yaml`

## Change policy

- Preserve `intake` as the only public entry.
- Preserve exact activation responses for workflow modes that require fixed wording.
- Prefer extending schemas and references before expanding root prose.
- Keep examples short, valid, and aligned with current schemas.
- If a new workflow family is introduced, add its routing rule, activation response, workflow reference, and standalone workflow skill together.
