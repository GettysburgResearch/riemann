#!/usr/bin/env python3
"""Lightweight repository-front-door checks.

This script validates only checked-in information architecture and Markdown
links. It performs no mathematical, zero, prime, interval, spectral, or
special-function computation.
"""

from __future__ import annotations

import pathlib
import re
import sys
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parents[2]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "START_HERE.md",
    "RESEARCH_MAP.md",
    "FRONTIERS.md",
    "CONTRIBUTING.md",
    "research/README.md",
    "research/integrated/README.md",
    "research/integrated/corrections/proof-boundary-corrections.md",
    "research/integrated/robin/finite-robin-foundations.md",
    "research/integrated/xi/derivative-free-pick-loewner.md",
    "research/integrated/xi/finite-pick-controls.md",
    "research/exploratory/README.md",
    "internal/README.md",
    "internal/archive/README.md",
    "internal/registry/README.md",
    "internal/registry/registry.yaml",
    "internal/registry/aliases.yaml",
    "internal/registry/provenance.schema.json",
    "internal/tools/README.md",
    "integration/README.md",
]

CURATED_MARKDOWN = [
    pathlib.Path(path)
    for path in REQUIRED
    if path.endswith(".md")
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def check_required() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def check_status_language() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "RH remains unsolved" not in readme:
        fail("README must state exactly that RH remains unsolved")
    if "integration/2026-08-01/PR_LEDGER.md" in readme:
        fail("README must not route newcomers directly to the full PR ledger")

    for packet in CURATED_MARKDOWN:
        text = (ROOT / packet).read_text(encoding="utf-8")
        if packet.parts[:2] == ("research", "integrated"):
            required_terms = ("source", "review", "scope")
            lowered = text.lower()
            for term in required_terms:
                if term not in lowered:
                    fail(f"{packet}: integrated packet lacks {term!r} language")


def check_links() -> None:
    errors: list[str] = []
    for relative in CURATED_MARKDOWN:
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target = unquote(target)
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{relative}: link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{relative}: missing link target: {raw_target}")
    if errors:
        fail("\n  ".join(errors))


def check_retired_workflow() -> None:
    workflow = ROOT / ".github" / "workflows" / "integration-snapshot.yml"
    if workflow.exists():
        fail("retired integration-snapshot workflow is still present")


def main() -> int:
    check_required()
    check_status_language()
    check_links()
    check_retired_workflow()
    print("PASS: front-door information architecture is internally consistent")
    print(f"  curated Markdown files checked: {len(CURATED_MARKDOWN)}")
    print("  retired integration snapshot workflow: absent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
