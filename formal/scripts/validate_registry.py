#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
MAP = ROOT / "formal" / "registry" / "FORMALIZATION_MAP.tsv"
ALLOWED = {
    "UNSTATED",
    "STATED",
    "PROVED",
    "PROVED_CONDITIONAL",
    "UPSTREAM_PROVED",
    "BLOCKED_LIBRARY",
    "BLOCKED_MATHEMATICS",
    "REFUTED_FORMALIZED",
    "SUPERSEDED",
}
DECLARATION_REQUIRED = {
    "STATED",
    "PROVED",
    "PROVED_CONDITIONAL",
    "UPSTREAM_PROVED",
    "REFUTED_FORMALIZED",
}
EXPECTED_FIELDS = [
    "semantic_id",
    "family",
    "scientific_verdict",
    "formal_status",
    "lean_declaration",
    "lean_module",
    "source_pr",
    "source_sha",
    "source_path",
    "formal_dependency_ids",
    "blocked_on",
    "notes",
]
SHA = re.compile(r"^[0-9a-f]{40}$")


def read(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def main() -> None:
    _, source = read(SOURCE)
    fields, formal = read(MAP)
    if fields != EXPECTED_FIELDS:
        raise SystemExit(f"unexpected FORMALIZATION_MAP.tsv fields: {fields}")
    if len(source) != 139 or len(formal) != 139:
        raise SystemExit(f"claim-count mismatch: canonical={len(source)} formal={len(formal)}")

    sids = [r["semantic_id"] for r in source]
    fids = [r["semantic_id"] for r in formal]
    if len(set(fids)) != len(fids):
        raise SystemExit("duplicate semantic_id in FORMALIZATION_MAP.tsv")
    if fids != sids:
        raise SystemExit("formal semantic IDs/order do not exactly match the canonical release")

    canonical = {r["semantic_id"]: r for r in source}
    known = set(canonical)
    for row in formal:
        sid = row["semantic_id"]
        status = row["formal_status"]
        if status not in ALLOWED:
            raise SystemExit(f"invalid formal status for {sid}: {status}")
        src = canonical[sid]
        if row["family"] != src["family"]:
            raise SystemExit(f"family drift for {sid}")
        if row["scientific_verdict"] != src["final_verdict"]:
            raise SystemExit(f"scientific verdict drift for {sid}")
        if (
            row["source_pr"] != src["source_pr"]
            or row["source_sha"] != src["source_head_sha"]
            or row["source_path"] != src["source_path"]
        ):
            raise SystemExit(f"source provenance drift for {sid}")
        if not SHA.fullmatch(row["source_sha"]):
            raise SystemExit(f"malformed source SHA for {sid}: {row['source_sha']}")
        if status in DECLARATION_REQUIRED:
            if not row["lean_declaration"] or not row["lean_module"]:
                raise SystemExit(f"{status} row lacks declaration/module: {sid}")
        dependencies = [x.strip() for x in row["formal_dependency_ids"].split(";") if x.strip()]
        unknown = [x for x in dependencies if x not in known]
        if unknown:
            raise SystemExit(f"unknown formal dependency IDs for {sid}: {unknown}")
        if not row["notes"]:
            raise SystemExit(f"missing formal notes for {sid}")

    proved = sum(r["formal_status"] in {"PROVED", "UPSTREAM_PROVED", "REFUTED_FORMALIZED"} for r in formal)
    conditional = sum(r["formal_status"] == "PROVED_CONDITIONAL" for r in formal)
    stated = sum(r["formal_status"] == "STATED" for r in formal)
    print(
        "PASS_FORMALIZATION_REGISTRY "
        f"claims=139 stated={stated} proved={proved} conditional={conditional}"
    )


if __name__ == "__main__":
    main()
