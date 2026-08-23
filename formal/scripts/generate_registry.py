#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "canonical" / "2026-08-22" / "claims.tsv"
OUTPUT = ROOT / "formal" / "registry" / "FORMALIZATION_MAP.tsv"
DELTAS = ROOT / "formal" / "registry" / "deltas"

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

DELTA_FIELDS = {
    "lean_declaration",
    "lean_module",
    "formal_status",
    "formal_dependency_ids",
    "blocked_on",
    "notes",
}

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


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    rows = read_tsv(SOURCE)
    if len(rows) != 139:
        raise SystemExit(f"expected 139 canonical claims, found {len(rows)}")

    seen: set[str] = set()
    ordered_ids: list[str] = []
    joined: dict[str, dict[str, str]] = {}
    for row in rows:
        sid = row["semantic_id"]
        if sid in seen:
            raise SystemExit(f"duplicate semantic_id in canonical source: {sid}")
        seen.add(sid)
        ordered_ids.append(sid)
        status, decl, module, blocked = BOOTSTRAP.get(
            sid, ("UNSTATED", "", "", "proof formalization")
        )
        joined[sid] = {
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
        }

    claimed_by: dict[str, str] = {}
    for delta_path in sorted(DELTAS.glob("*.tsv")):
        owner = delta_path.stem
        for delta in read_tsv(delta_path):
            sid = delta.get("semantic_id", "").strip()
            if not sid:
                continue
            if sid not in joined:
                raise SystemExit(f"{delta_path}: unknown semantic_id {sid}")
            if sid in claimed_by:
                raise SystemExit(
                    f"semantic_id {sid} occurs in both {claimed_by[sid]} and {delta_path.name}"
                )
            claimed_by[sid] = delta_path.name
            for field in DELTA_FIELDS:
                value = delta.get(field, "").strip()
                if value:
                    joined[sid][field] = value
            joined[sid]["notes"] = (
                f"[{owner}] {joined[sid]['notes']}" if joined[sid]["notes"] else f"[{owner}]"
            )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(joined[sid] for sid in ordered_ids)
    print(f"GENERATED_FORMALIZATION_MAP claims={len(ordered_ids)} delta_rows={len(claimed_by)}")


if __name__ == "__main__":
    main()
