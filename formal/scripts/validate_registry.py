#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
MAP = ROOT / "formal" / "registry" / "FORMALIZATION_MAP.tsv"
ALLOWED = {
    "UNSTATED", "STATED", "PROVED", "PROVED_CONDITIONAL", "UPSTREAM_PROVED",
    "BLOCKED_LIBRARY", "BLOCKED_MATHEMATICS", "REFUTED_FORMALIZED", "SUPERSEDED",
}
SHA = re.compile(r"^[0-9a-f]{40}$")


def read(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    source = read(SOURCE)
    formal = read(MAP)
    if len(source) != 139 or len(formal) != 139:
        raise SystemExit(f"claim-count mismatch: canonical={len(source)} formal={len(formal)}")
    sids = [r["semantic_id"] for r in source]
    fids = [r["semantic_id"] for r in formal]
    if len(set(fids)) != len(fids):
        raise SystemExit("duplicate semantic_id in FORMALIZATION_MAP.tsv")
    if set(sids) != set(fids):
        raise SystemExit("formal semantic IDs do not exactly match the canonical release")
    canonical = {r["semantic_id"]: r for r in source}
    for row in formal:
        sid = row["semantic_id"]
        if row["formal_status"] not in ALLOWED:
            raise SystemExit(f"invalid formal status for {sid}: {row['formal_status']}")
        src = canonical[sid]
        if row["scientific_verdict"] != src["final_verdict"]:
            raise SystemExit(f"scientific verdict drift for {sid}")
        if row["source_pr"] != src["source_pr"] or row["source_path"] != src["source_path"]:
            raise SystemExit(f"source provenance drift for {sid}")
        if not SHA.fullmatch(row["source_sha"]):
            raise SystemExit(f"malformed source SHA for {sid}: {row['source_sha']}")
    print("PASS_FORMALIZATION_REGISTRY claims=139")


if __name__ == "__main__":
    main()
