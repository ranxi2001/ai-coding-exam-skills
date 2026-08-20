#!/usr/bin/env python3
"""Validate skill metadata and local Markdown references."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_frontmatter(skill_file: Path) -> list[str]:
    errors: list[str] = []
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return [f"{skill_file}: missing YAML frontmatter"]

    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f"{skill_file}: invalid YAML: {exc}"]

    if not isinstance(metadata, dict):
        return [f"{skill_file}: frontmatter must be a mapping"]

    extra = set(metadata) - {"name", "description"}
    missing = {"name", "description"} - set(metadata)
    if extra:
        errors.append(f"{skill_file}: unsupported frontmatter keys: {sorted(extra)}")
    if missing:
        errors.append(f"{skill_file}: missing frontmatter keys: {sorted(missing)}")
        return errors

    name = metadata["name"]
    description = metadata["description"]
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file}: invalid skill name {name!r}")
    elif skill_file.parent.name != name:
        errors.append(
            f"{skill_file}: folder {skill_file.parent.name!r} must match name {name!r}"
        )
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_file}: description must be a non-empty string")

    return errors


def validate_links(markdown_file: Path) -> list[str]:
    errors: list[str] = []
    text = markdown_file.read_text(encoding="utf-8")
    for raw_target in LINK_RE.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if path_part and not (markdown_file.parent / path_part).exists():
            errors.append(f"{markdown_file}: broken local link {raw_target!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        errors.append(f"No SKILL.md files found under {SKILLS_DIR}")

    for skill_file in skill_files:
        errors.extend(validate_frontmatter(skill_file))
        for markdown_file in sorted(skill_file.parent.rglob("*.md")):
            errors.extend(validate_links(markdown_file))

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

