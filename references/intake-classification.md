# Intake Classification Rules

`intake` is the only external entry role.

When the user input contains `@intake`, do these steps in order:

1. Normalize the request and extract the main goal.
2. Classify the task as one of:
- `6A`
- `6AYH`
- `PPW`
- `SDD`
- `generic_governance`
3. Build the first structured task card with:
   - `workflow_mode`
   - `current_stage`
   - `document_bundle_version`
   - `code_change_targets`
   - `status=triaged`
   - the first `handoff_history` entry
4. If the result is `6A`, `6AYH`, `PPW`, or `SDD`, output the workflow activation response exactly.
5. Attach the workflow's required-document list to the task card and resolve it against the active project's root `docs/` directory.
6. Default the document bundle version to `v1`. If the same topic already has an existing bundle, increment to `v2`, `v3`, and so on.
7. If required workflow files are missing, mark document bootstrap as required and set `document_status=pending`.
8. Hand off only to `planner`.

Classification heuristics:

- Choose `6A` for new pages, modules, features, or greenfield systems.
- Choose `6AYH` for refactor, optimization, performance cleanup, or maintenance-cost reduction.
- Choose `PPW` for inventory, current-state clarification, asset mapping, or process discovery.
- Choose `SDD` for spec-driven development, spec-first delivery, or spec-plan-implement loops.
- Choose `generic_governance` when none of the above clearly match but the task still needs planning, review, and dispatch.

Activation-output rule:

- For `6A`, `6AYH`, `PPW`, and `SDD`, `intake` must output the workflow activation response before any additional planning text.
- The first handoff record must explain why the selected workflow was chosen and why the task was handed to `planner`.

Non-bypass rule:

- Even if the content strongly resembles planning, risk review, audit, or a known workflow, the external request must still start at `intake`.
- No other role may be the first external recipient.
