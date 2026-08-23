#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
OUTPUT = ROOT / "formal" / "registry" / "FORMALIZATION_MAP.tsv"

FIELDS = [
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

BOOTSTRAP = {
    "RH": ("STATED", "RiemannFormal.RH", "RiemannFormal.Statement.RH", "open mathematics"),
    "OPEN.ARITH.ROWS23_NATIVE": ("STATED", "RiemannFormal.OpenCut.rows23Native", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS": ("STATED", "RiemannFormal.OpenCut.fiveThreeNegativeMass", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS": ("STATED", "RiemannFormal.OpenCut.fixedDetectorNegativeMass", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.ARITH.CV": ("STATED", "RiemannFormal.OpenCut.criticalVariation", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.ARITH.XD": ("STATED", "RiemannFormal.OpenCut.crossCoreDispersion", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.ARITH.HCNC": ("STATED", "RiemannFormal.OpenCut.halfDivisorNearCollision", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.ARITH.BPOE": ("STATED", "RiemannFormal.OpenCut.physicalOccupancy", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
    "OPEN.OPERATOR.XI.PICK_ORDER4_PLUS": ("STATED", "RiemannFormal.OpenCut.xiPickOrderFour", "RiemannFormal.Statement.OpenCuts", "open mathematics"),
}


def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if len(rows) != 139:
        raise SystemExit(f"expected 139 canonical claims, found {len(rows)}")
    seen: set[str] = set()
    out = []
    for row in rows:
        sid = row["semantic_id"]
        if sid in seen:
            raise SystemExit(f"duplicate semantic_id in canonical source: {sid}")
        seen.add(sid)
        status, decl, module, blocked = BOOTSTRAP.get(
            sid, ("UNSTATED", "", "", "proof formalization")
        )
        out.append({
            "semantic_id": sid,
            "family": row["family"],
            "scientific_verdict": row["final_verdict"],
            "formal_status": status,
            "lean_declaration": decl,
            "lean_module": module,
            "source_pr": row["source_pr"],
            "source_sha": row["source_head_sha"],
            "source_path": row["source_path"],
            "formal_dependency_ids": "",
            "blocked_on": blocked,
            "notes": "bootstrap registry; statement/proof status is independent of scientific review status",
        })
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(out)


if __name__ == "__main__":
    main()
