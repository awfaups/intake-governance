# Workflow Naming

Use this file as the source of truth for workflow display names, abbreviations, and legacy aliases.

## Canonical names

| Canonical abbreviation | English name | Chinese name | Existing internal mode | Legacy alias |
| --- | --- | --- | --- | --- |
| `6A` | Align, Architect, Atomize, Approve, Automate, Assess | 6A 新增功能开发工作流 | `6a` | none |
| `6AO` | 6A Optimization | 6A 优化型工作流 | `6ayh` | `@6AYH` |
| `PMW` | Project Mapping Workflow | 项目流程梳理工作流 | `ppw` | `@ppw`, `@PPW` |
| `SDD` | Specification-Driven Development | 规范驱动开发工作流 | `sdd` | `@sdd` |
| `GGW` | Generic Governance Workflow | 通用治理工作流 | `generic_governance` | none |

## Naming policy

- Prefer canonical abbreviations in new docs, activation responses, and examples.
- Keep legacy aliases accepted by routing when they already exist in user prompts or older docs.
- Do not rename existing internal modes or directories only for display-name cleanup; those ids are part of the package compatibility surface.
- When adding a new workflow, define the canonical abbreviation, English name, Chinese name, internal mode, activation response, and any legacy alias together.
