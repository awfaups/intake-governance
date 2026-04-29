#!/usr/bin/env python3
"""Prompt smoke tests for intake-governance routing behavior."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_token(text: str) -> str:
    return text.lower()


def detect_alias(prompt: str, aliases: dict) -> str | None:
    for alias in aliases:
        if re.search(rf"(^|\s){re.escape(alias)}(?=\s|$)", prompt):
            return alias
    return None


def classify_prompt(prompt: str, routing: dict) -> dict:
    aliases = routing["aliases"]
    alias = detect_alias(prompt, aliases)
    if alias:
        return {
            "entry_agent": aliases[alias]["owner"],
            "alias": alias,
            "mode": aliases[alias]["workflow"],
        }

    lowered = normalize_token(prompt)
    for mode, config in routing["auto_classification"].items():
        if config.get("fallback"):
            continue
        for signal in config.get("match_any_signals", []):
            if normalize_token(signal) in lowered:
                return {
                    "entry_agent": routing["entry_agent"],
                    "alias": None,
                    "mode": mode,
                }

    return {
        "entry_agent": routing["entry_agent"],
        "alias": None,
        "mode": "generic_governance",
    }


def activation_response_for_result(result: dict, routing: dict) -> str | None:
    alias = result.get("alias")
    if alias:
        return routing["aliases"].get(alias, {}).get("activation_response")

    config = routing["auto_classification"].get(result["mode"], {})
    return config.get("activation_response")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    routing = read_json(root / "references/workflow-routing.json")
    cases = read_json(root / "references/activation-examples.json")

    failures = []
    for case in cases:
        result = classify_prompt(case["prompt"], routing)
        if result["entry_agent"] != case["expected_entry_agent"]:
            failures.append(
                f"{case['id']}: expected entry {case['expected_entry_agent']}, got {result['entry_agent']}"
            )
        if "expected_alias" in case and result["alias"] != case["expected_alias"]:
            failures.append(
                f"{case['id']}: expected alias {case['expected_alias']}, got {result['alias']}"
            )
        if result["mode"] not in case["allowed_modes"]:
            failures.append(
                f"{case['id']}: expected mode in {case['allowed_modes']}, got {result['mode']}"
            )
        if "expected_activation_contains" in case:
            activation_response = activation_response_for_result(result, routing) or ""
            if case["expected_activation_contains"] not in activation_response:
                failures.append(
                    f"{case['id']}: expected activation containing {case['expected_activation_contains']!r}"
                )

    if failures:
        raise SystemExit("Prompt smoke tests failed:\n- " + "\n- ".join(failures))

    print(f"prompt smoke tests: ok ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
