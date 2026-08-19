#!/usr/bin/env python3
"""Validate the structure and high-risk conventions of the UG_COSEAT_08 hub."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[4]

REQUIRED_PATHS = (
    "AGENTS.md",
    "README.md",
    "PROJECT_INTAKE.md",
    "TEAM.md",
    "REQUIREMENTS.md",
    "DECISIONS.md",
    "RISKS.md",
    "MEETINGS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "AI_USAGE_LOG.md",
    "knowledge-base/README.md",
    "knowledge-base/CURRENT_STATE.md",
    "knowledge-base/REPOSITORY_MAP.md",
    "knowledge-base/WAYS_OF_WORKING.md",
    "knowledge-base/PLAYBOOKS.md",
    "knowledge-base/project.json",
    "meeting-minutes/supervisor",
    "meeting-minutes/group",
    "meeting-minutes/client",
)

ID_FILES = {
    "REQUIREMENTS.md": r"(?m)^\|\s*(REQ-\d{3})\s*\|",
    "DECISIONS.md": r"(?m)^\|\s*(DEC-\d{3})\s*\|",
    "RISKS.md": r"(?m)^\|\s*(RISK-\d{3})\s*\|",
    "AI_USAGE_LOG.md": r"(?m)^\|\s*(AI-\d{3})\s*\|",
}

FORBIDDEN_TRACKED = (
    re.compile(r"(?i)(^|/)\.env($|\.)"),
    re.compile(r"(?i)\.(m4a|mp3|wav|aac|mov|mp4|srt|vtt)$"),
    re.compile(r"(?i)(^|/)(raw[-_ ]?)?transcripts?(/|$)"),
)


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    ]


def local_link_errors() -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            destination = (source.parent / path_text).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)} links outside the repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{source.relative_to(ROOT)} has a broken local link: {target}")
    return errors


def duplicate_id_errors() -> list[str]:
    errors: list[str] = []
    for relative_path, pattern in ID_FILES.items():
        path = ROOT / relative_path
        if not path.exists():
            continue
        identifiers = re.findall(pattern, path.read_text(encoding="utf-8"))
        duplicates = sorted(item for item, count in Counter(identifiers).items() if count > 1)
        if duplicates:
            errors.append(f"{relative_path} contains duplicate IDs: {', '.join(duplicates)}")
    return errors


def project_context_errors() -> list[str]:
    errors: list[str] = []
    path = ROOT / "knowledge-base/project.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"knowledge-base/project.json cannot be parsed: {exc}"]

    if data.get("project", {}).get("code") != "UG_COSEAT_08":
        errors.append("project.json project.code must be UG_COSEAT_08")
    team = data.get("team", [])
    if len(team) != 6:
        errors.append(f"project.json must contain 6 team members; found {len(team)}")
    usernames = [member.get("github") for member in team]
    if any(not username or username == "TBD" for username in usernames):
        errors.append("project.json team members must have verified GitHub usernames")
    if len(usernames) != len(set(usernames)):
        errors.append("project.json GitHub usernames must be unique")
    return errors


def tracked_file_errors() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        return [f"Could not inspect tracked files with git: {exc}"]

    errors: list[str] = []
    for tracked in result.stdout.splitlines():
        normalized = tracked.replace("\\", "/")
        if any(pattern.search(normalized) for pattern in FORBIDDEN_TRACKED):
            errors.append(f"Sensitive or raw evidence file is tracked: {tracked}")
    return errors


def advisory_warnings() -> list[str]:
    warnings: list[str] = []
    client_dir = ROOT / "meeting-minutes/client"
    client_records = (
        [path for path in client_dir.glob("*.md") if path.name.casefold() != "readme.md"]
        if client_dir.exists()
        else []
    )
    if not client_records:
        warnings.append("No client meeting record exists yet; keep client scope provisional and UGC08-3 blocked.")

    tbd_count = 0
    for path in markdown_files():
        tbd_count += len(re.findall(r"\bTBD\b", path.read_text(encoding="utf-8")))
    if tbd_count:
        warnings.append(f"{tbd_count} explicit TBD marker(s) remain; review them without inventing answers.")
    return warnings


def main() -> int:
    errors = [
        f"Required path is missing: {relative_path}"
        for relative_path in REQUIRED_PATHS
        if not (ROOT / relative_path).exists()
    ]
    errors.extend(local_link_errors())
    errors.extend(duplicate_id_errors())
    errors.extend(project_context_errors())
    errors.extend(tracked_file_errors())
    warnings = advisory_warnings()

    print(f"UG_COSEAT_08 project-hub validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        return 1
    print("PASS: required structure, local links, identifiers, project context, and tracked-file guardrails are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
