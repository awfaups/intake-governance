# Regression Checklist

Use this checklist after changing routing, schemas, examples, or installed-skill sync behavior.

## Fast checks

1. Validate core package files:

```bash
python3 scripts/validate_governance_skill.py
```

This also runs prompt smoke tests from `references/activation-examples.json`.

2. Validate installed-copy sync as well:

```bash
python3 scripts/validate_governance_skill.py --compare-installed
```

3. Refresh the installed copy before compare checks when needed:

```bash
python3 scripts/sync_installed_skill.py
```

## What the script should catch

- required files are present
- JSON references parse cleanly
- `agents/openai.yaml` is structurally valid
- example payloads contain required schema fields
- installed copy matches the repository copy when requested
- runtime files can be pushed to the installed copy with one command

## Manual spot checks

After the script passes, still review these behavior-level checks:

1. Alias normalization still routes through `intake`.
2. `@6A`, `@6AYH`, `@PPW`, and `@sdd` still keep exact activation responses.
3. Workflow-free governance prompts still classify into `generic_governance` when appropriate.
4. Root `SKILL.md` still reads like an entry console, not a duplicated policy dump.
5. Workflow subskills still read like detail layers, not public entry points.
6. Example JSON files still look like realistic outputs, not schema-only placeholders.

## Trigger sanity prompts

Use `references/activation-examples.md` as the minimum trigger sanity set.
Machine-checked cases live in `references/activation-examples.json`.

If a change affects routing or classification, update both:

- `references/workflow-routing.json`
- `references/activation-examples.md`
- `references/activation-examples.json`

If a change affects task-card or handoff structure, update both:

- `references/task-card.schema.json` and `references/task-card.example.json`
- `references/handoff-record.schema.json` and `references/handoff-record.example.json`
