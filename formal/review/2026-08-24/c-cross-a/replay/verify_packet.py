#!/usr/bin/env python3
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]
required = [
    "FREEZE.json","COMPLETION_CHECKLIST.tsv","UPSTREAM_DECLARATION_AUDIT.tsv",
    "THEOREM_VERDICTS.tsv","TRUST_BOUNDARY_AUDIT.tsv",
    "MELLIN_NORMALIZATION_AUDIT.md","BUILD_AND_AXIOM_AUDIT.md",
    "FIXES_REQUIRED.md","CROSS_REVIEW_REPORT.md","INTEGRATION_HANDOFF.md",
]
for name in required:
    p=ROOT/name
    if not p.is_file() or p.stat().st_size == 0:
        raise SystemExit(f"missing/empty {name}")
freeze=json.loads((ROOT/"FREEZE.json").read_text())
assert freeze["final_verdict"]=="NOT_INTEGRATION_READY"
assert freeze["rh_proved"] is False
for name, minimum in [
    ("COMPLETION_CHECKLIST.tsv",20),
    ("UPSTREAM_DECLARATION_AUDIT.tsv",25),
    ("THEOREM_VERDICTS.tsv",20),
    ("TRUST_BOUNDARY_AUDIT.tsv",10),
]:
    with (ROOT/name).open(newline="",encoding="utf-8") as f:
        rows=list(csv.DictReader(f,delimiter="\t"))
    if len(rows)<minimum:
        raise SystemExit(f"{name}: expected at least {minimum}, found {len(rows)}")
print("PASS_C_CROSS_A_PACKET")
print("RH_PROVED=false")
