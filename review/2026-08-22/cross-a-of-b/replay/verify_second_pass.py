#!/usr/bin/env python3
from pathlib import Path
import csv, json

root = Path(__file__).resolve().parent.parent
tsv = root / "SECOND_PASS_VERDICT_DELTA.tsv"
addendum = root / "SECOND_PASS_ADDENDUM.md"
assert tsv.is_file()
assert addendum.is_file()

with tsv.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
assert len(rows) == 2
by = {r["semantic_id"]: r for r in rows}
assert by["OPERATOR.SUZUKI.FOCK_FIRST_CHAOS"]["reviewer_a_cross_verdict"] == "WEAKEN_TO_CONDITIONAL"
assert by["OPERATOR.SUZUKI.FOCK_FIRST_CHAOS"]["exact_source_sha"] == "7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e"
assert by["OPERATOR.XI.CURVATURE.ANCHOR_DOMINATION"]["reviewer_a_cross_verdict"] == "AGREE_VERIFIED_WITH_FIXES"
assert by["OPERATOR.XI.CURVATURE.ANCHOR_DOMINATION"]["exact_source_sha"] == "db9a767e312d9928f5ef827762dcb4ef95494af0"

text = addendum.read_text(encoding="utf-8")
assert "K_r=rK_1" in text
assert "shared reserve-ledger node" in text
assert "RH remains unproved" in text
assert "No heavy computation was rerun" in text

result = {
    "verdict": "PASS_REVIEWER_A_CROSS_REVIEW_B_SECOND_PASS",
    "second_pass_delta_rows": len(rows),
    "suzuki_first_chaos_scope": "CONDITIONAL",
    "xi_shared_reserve_alias_required": True,
    "heavy_campaigns_rerun": False,
    "rh_proved": False,
}
out = Path(__file__).with_name("second_pass_verification.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
