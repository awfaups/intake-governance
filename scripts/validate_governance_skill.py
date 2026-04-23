#!/usr/bin/env python3
"""Lightweight validator for the role-based-agent-governance skill package."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/intake-classification.md",
    "references/workflow-routing.json",
    "references/activation-examples.json",
    "references/task-card.schema.json",
    "references/task-card.example.json",
    "references/handoff-record.schema.json",
    "references/handoff-record.example.json",
    "references/activation-examples.md",
    "references/reference-loading.md",
    "references/maintainer-upgrade-guide.md",
    "references/regression-checklist.md",
    "scripts/smoke_test_prompts.py",
    "scripts/sync_installed_skill.py",
    "skills/workflow-6a/SKILL.md",
    "skills/workflow-6ayh/SKILL.md",
    "skills/workflow-ppw/SKILL.md",
    "skills/workflow-sdd/SKILL.md",
]

JSON_FILES = [
    "references/workflow-routing.json",
    "references/activation-examples.json",
    "references/task-card.schema.json",
    "references/task-card.example.json",
    "references/handoff-record.schema.json",
    "references/handoff-record.example.json",
]


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_required_files(root: Path) -> None:
    missing = [rel for rel in REQUIRED_FILES if not (root / rel).exists()]
    if missing:
        raise SystemExit("Missing required files:\n- " + "\n- ".join(missing))


def validate_json_files(root: Path) -> None:
    for rel in JSON_FILES:
        read_json(root / rel)


def validate_examples_against_required_keys(root: Path) -> None:
    task_schema = read_json(root / "references/task-card.schema.json")
    task_example = read_json(root / "references/task-card.example.json")
    handoff_schema = read_json(root / "references/handoff-record.schema.json")
    handoff_example = read_json(root / "references/handoff-record.example.json")

    task_missing = [key for key in task_schema.get("required", []) if key not in task_example]
    handoff_missing = [key for key in handoff_schema.get("required", []) if key not in handoff_example]

    if task_missing:
        raise SystemExit("Task-card example missing required keys: " + ", ".join(task_missing))
    if handoff_missing:
        raise SystemExit("Handoff example missing required keys: " + ", ".join(handoff_missing))


def validate_yaml_with_ruby(root: Path) -> None:
    yaml_path = root / "agents/openai.yaml"
    cmd = ["ruby", "-e", "require 'yaml'; YAML.load_file(ARGV[0]);", str(yaml_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip() or "unknown Ruby YAML failure"
        raise SystemExit(f"YAML validation failed for {yaml_path}: {stderr}")


def validate_installed_copy(root: Path, installed_root: Path) -> None:
    if not installed_root.exists():
        raise SystemExit(f"Installed copy not found: {installed_root}")

    mismatches = []
    for rel in REQUIRED_FILES:
        repo_file = root / rel
        installed_file = installed_root / rel
        if not installed_file.exists():
            mismatches.append(f"{rel}: missing in installed copy")
            continue
        if repo_file.read_bytes() != installed_file.read_bytes():
            mismatches.append(f"{rel}: content differs")

    if mismatches:
        raise SystemExit("Installed copy mismatch:\n- " + "\n- ".join(mismatches))


def run_smoke_tests(root: Path) -> None:
    script_path = root / "scripts/smoke_test_prompts.py"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip() or "unknown smoke-test failure"
        raise SystemExit(f"Prompt smoke tests failed: {stderr}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--compare-installed",
        action="store_true",
        help="Also verify that the installed skill copy matches this repository.",
    )
    parser.add_argument(
        "--installed-root",
        default="/Users/caiyanning/.codex/skills/role-based-agent-governance",
        help="Installed skill root to compare when --compare-installed is set.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent

    validate_required_files(root)
    validate_json_files(root)
    validate_examples_against_required_keys(root)
    validate_yaml_with_ruby(root)
    run_smoke_tests(root)

    if args.compare_installed:
        validate_installed_copy(root, Path(args.installed_root))

    print("role-based-agent-governance validation: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
