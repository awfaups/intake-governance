# Beginner Guide

`intake-governance` is a skill package for multi-agent collaboration.

Its job is not to write business code for you. It gives agents a clear governance flow so that complex work can move forward by role:

- `intake`: receive the request, identify intent, and decide which flow to enter
- `planner`: plan, decompose, and design the approach
- `review-gate`: review risk and quality
- `orchestrator`: dispatch, coordinate, and aggregate
- worker departments: carry out the actual work

This repository now includes the root skill plus four standalone workflow skills:

- `workflow-6a`
- `workflow-6ayh`
- `workflow-ppw`
- `workflow-sdd`

If you are new to it, think of it as:

> a rule set that says "understand first, plan next, review when needed, then execute."

## 1. Who it is for

Good fits:

- you want agents to split work by role
- you need a layered flow for planning, review, and execution
- you are building multi-agent orchestration, task delegation, or workflow governance
- you want `@intake` as a single entry point for complex work

Not a good fit:

- you only need a simple question answered
- you only need a one-step task
- you do not want extra process or role separation

## 2. Installation path

In Codex, skills are usually installed under:

```text
~/.codex/skills/
```

After installation, the structure should look like:

```text
~/.codex/skills/intake-governance/
├── README.md
├── SKILL.md
├── OVERVIEW.md
├── OVERVIEW.zh-CN.md
├── BEGINNER_GUIDE.md
├── BEGINNER_GUIDE.zh-CN.md
├── LICENSE
├── PUBLISHING.md
├── agents/
├── references/
├── scripts/
└── skills/
```

## 3. How to install

### Option 1: copy from a local checkout

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/intake-governance ~/.codex/skills/intake-governance
```

Replace `/path/to/intake-governance` with your actual local path.

### Option 2: clone from GitHub

```bash
git clone https://github.com/awfaups/intake-governance.git
mkdir -p ~/.codex/skills
cp -R intake-governance ~/.codex/skills/intake-governance
```

You must restart Codex after installation, otherwise the new skill may not be picked up immediately.

## 4. How to verify installation

Run:

```bash
ls ~/.codex/skills/intake-governance
```

If you can see:

- `SKILL.md`
- `references/`
- `skills/`

the files are in the right place.

## 5. First use

The most important entry point is:

```text
@intake
```

Example:

```text
@intake help me plan a multi-agent collaboration setup
```

Or:

```text
@intake break this complex request into planning, review, and execution layers
```

## 6. What happens next

After `@intake`, the system usually follows this order:

1. identify the task type
2. decide which internal flow to use
3. build a structured task card
4. write the workflow docs under the active project's root `docs/` directory
5. present the document bundle to the user for confirmation
6. only after confirmation, let `orchestrator` coordinate code generation or code changes

The latest gating rules are:

- `6A`, `6AYH`, `PPW`, and `SDD` all require a workflow document bundle first
- the document directory format is `docs/YYYY_MM_DD_中文任务名_vN/`
- if code changes are involved, the docs must record file paths, line ranges, before context, and after context
- before confirmation, `user_confirmation.status` must stay `pending`
- without confirmation, `engineering` may not be dispatched and code may not be generated or edited

`docs/` means the root of the project you are currently working on, not the skill package installation directory.

## 7. Common triggers

### Universal entry

```text
@intake
```

### Workflow aliases

- `@plan`: task planning
- `@risk`: risk review
- `@audit`: architecture / code audit
- `@refactor`: progressive refactor
- `@6A`: new feature development
- `@6AYH`: progressive optimization
- `@PPW`: project-process inventory
- `@sdd`: spec-driven development

If you want `SDD` to work more reliably, generate the spec file using:

- [references/templates/01_SPEC.template.md](references/templates/01_SPEC.template.md)

If you are not sure which one to use, `@intake` is enough.

## 8. Good first prompts

### Prompt 1: ask it to plan

```text
@intake I want to build something complex, please break it down in multi-agent mode
```

### Prompt 2: ask it to split roles

```text
@intake design a collaboration flow with planning, review, and execution layers
```

### Prompt 3: ask for governance analysis

```text
@intake help me judge whether this task needs a review gate and risk control
```

### Prompt 4: specify constraints

```text
@intake plan this requirement with risk control, execution order, and delivery criteria
```

## 9. Why this feels slower

Because the skill is designed to make complex tasks more controllable, not to answer a one-line question as fast as possible.

If the task is simple, do not force it through this flow.

## 10. Why `@intake` is recommended

Because the rules require:

- external requests enter only through `intake`
- you may not jump directly to `planner`, `review-gate`, or a worker role

That avoids role overreach and flow confusion.

## 11. When `review-gate` appears

Usually when:

- risk is high
- the task spans multiple responsibility domains
- security, deployment, or permissions are involved
- acceptance criteria are unclear

## 12. What to check if it does not work

1. the skill is installed at `~/.codex/skills/intake-governance`
2. the root really contains `SKILL.md`
3. Codex has been restarted

## 13. Suggested reading order

1. [OVERVIEW.md](OVERVIEW.md)
2. [OVERVIEW.zh-CN.md](OVERVIEW.zh-CN.md)
3. [references/role-permissions.md](references/role-permissions.md)
4. [references/workflow-routing.json](references/workflow-routing.json)

## 14. One-line summary

If you are new, remember this:

> For complex tasks, start with `@intake`. For simple tasks, do not force multi-agent flow.
