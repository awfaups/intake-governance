#!/usr/bin/env python3
"""Sync the runtime-relevant skill files into the installed Codex skill copy."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


MANAGED_PATHS = [
    "SKILL.md",
    "agents",
    "references",
    "scripts",
    "skills",
]


def copy_path(src: Path, dst: Path) -> None:
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def sync_paths(repo_root: Path, installed_root: Path) -> None:
    installed_root.mkdir(parents=True, exist_ok=True)
    for rel in MANAGED_PATHS:
        src = repo_root / rel
        if not src.exists():
            raise SystemExit(f"Managed path missing in repository: {src}")
        copy_path(src, installed_root / rel)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--installed-root",
        default="/Users/caiyanning/.codex/skills/intake-governance",
        help="Installed skill root to update.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    installed_root = Path(args.installed_root)
    sync_paths(repo_root, installed_root)
    print(f"installed skill sync: ok -> {installed_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
