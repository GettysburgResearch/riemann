#!/usr/bin/env python3
"""Lightweight consistency checks for the timestamped integration metadata.

This script does not verify mathematics, replay numerical artifacts, or query GitHub.
It checks only the checked-in integration structure.
"""

from __future__ import annotations

import collections
import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
STATE = ROOT / "integration" / "2026-08-01"
HEX40 = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def ids_from_yaml(path: pathlib.Path, key: str) -> list[str]:
    pattern = re.compile(rf"^\s*-\s+{re.escape(key)}:\s+([A-Za-z0-9_.:-]+)\s*$")
    values: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            values.append(match.group(1))
    return values


def read_rows(manifest: dict) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for batch in manifest["batches"]:
        path = STATE / batch["path"]
        with path.open(encoding="utf-8", newline="") as stream:
            batch_rows = list(csv.DictReader(stream, delimiter="\t"))
        if len(batch_rows) != batch["row_count"]:
            fail(f"{path}: expected {batch['row_count']} rows, got {len(batch_rows)}")
        rows.extend(batch_rows)
    return rows


def main() -> int:
    manifest = json.loads((STATE / "pr-ledger.json").read_text(encoding="utf-8"))
    if manifest.get("schema") != "riemann.integration.pr-ledger-manifest.v1":
        fail("unexpected ledger manifest schema")

    rows = read_rows(manifest)
    if len(rows) != 127:
        fail(f"expected 127 cutoff PR rows, got {len(rows)}")

    numbers = [int(row["pr"]) for row in rows]
    if len(set(numbers)) != len(numbers):
        fail("duplicate PR number")
    if 212 not in numbers or 213 in numbers:
        fail("cutoff population must contain #212 and exclude #213")

    source_rows = [row for row in rows if int(row["pr"]) != 212]
    verdicts = collections.Counter(row["review_verdict"] for row in source_rows)
    expected = {
        "VERIFIED": 29,
        "VERIFIED WITH FIXES": 55,
        "GAP/BLOCKED": 39,
        "REJECTED": 3,
    }
    if verdicts != expected:
        fail(f"review aggregate mismatch: {dict(verdicts)}")

    for row in rows:
        sha = row["reviewed_sha"]
        if not HEX40.fullmatch(sha):
            fail(f"bad reviewed SHA for PR #{row['pr']}: {sha!r}")
        present = row["present_head"]
        if present and not HEX40.fullmatch(present):
            fail(f"bad present SHA for PR #{row['pr']}: {present!r}")
        if present and present != sha and row["head_evidence"] != "D_DELTA_NOT_REVIEWED":
            fail(f"unmarked post-review delta for PR #{row['pr']}")

    schema = json.loads((ROOT / "canonical" / "provenance.schema.json").read_text(encoding="utf-8"))
    if schema.get("properties", {}).get("source", {}).get("properties", {}).get("commit") is None:
        fail("provenance schema lacks source commit binding")

    canonical_ids = ids_from_yaml(ROOT / "canonical" / "registry.yaml", "id")
    if not canonical_ids or len(canonical_ids) != len(set(canonical_ids)):
        fail("canonical registry IDs are empty or duplicated")

    collision_sets = ids_from_yaml(ROOT / "canonical" / "aliases.yaml", "collision_set")
    if len(collision_sets) != len(set(collision_sets)):
        fail("duplicate alias collision_set")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "RH remains unsolved" not in readme:
        fail("root README must state that RH remains unsolved")

    workflow = (ROOT / ".github" / "workflows" / "integration-snapshot.yml").read_text(encoding="utf-8")
    if "immutable snapshot" in workflow.lower():
        fail("workflow must not describe a temporary Actions artifact as immutable")

    print("PASS: integration metadata is internally consistent")
    print("  cutoff PR rows: 127")
    print("  reviewed source PRs: 126")
    print("  aggregate: 29 VERIFIED / 55 VERIFIED WITH FIXES / 39 GAP/BLOCKED / 3 REJECTED")
    print(f"  canonical packet IDs: {len(canonical_ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
