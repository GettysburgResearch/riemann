#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, getcontext
import csv, json

root = Path(__file__).resolve().parent.parent
required = [
    "FREEZE.json", "VERDICT_DELTA.tsv", "GRAPH_DEFECTS.tsv",
    "SOURCE_PROVENANCE_FIXES.tsv", "MISSED_CLAIM_CANDIDATES.tsv",
    "COMPUTATION_AUDIT.tsv", "CROSS_REVIEW_REPORT.md",
    "INTEGRATION_HANDOFF.md",
]
for name in required:
    assert (root / name).is_file(), name

def rows(name):
    with (root / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))

delta = rows("VERDICT_DELTA.tsv")
graph = rows("GRAPH_DEFECTS.tsv")
missed = rows("MISSED_CLAIM_CANDIDATES.tsv")
assert len({r["semantic_id"] for r in delta}) == len(delta)
assert len({r["defect_id"] for r in graph}) == len(graph)
assert len({r["candidate_semantic_id"] for r in missed}) == len(missed)

by = {r["semantic_id"]: r for r in delta}
assert by["OPERATOR.XI.PICK_ORDER3"]["reviewer_a_cross_verdict"] == "AGREE_VERIFIED_WITH_FIXES"
assert by["CRITERION.Q4.SACF"]["reviewer_a_cross_verdict"] == "WEAKEN_TO_CONDITIONAL"
assert by["CRITERION.Q4.UOSACF"]["reviewer_a_cross_verdict"] == "AGREE_OPEN_RH_EQUIVALENT"
assert by["CONSUMER.MELLIN.FIVE_THREE"]["reviewer_a_cross_verdict"] == "MISSED_CLAIM_CANDIDATE"
assert any(r["defect_id"] == "G-A-B-001" for r in graph)

# Exact Mellin numerator algebra on representative rationals.
for a in [Fraction(0), Fraction(1, 2), Fraction(-2, 3), Fraction(7, 11)]:
    assert -3 * (a - 1) * (a - 2) == -3*a*a + 9*a - 6
    assert -3 * (a - 1) * (a - 2) == -3 * ((a - 1) * (a - 2))

# Conservative Xi reserve budget is far below one.
getcontext().prec = 50
H = Decimal("3000175332800")
budget = Decimal(18) * (H.ln() + Decimal(1)) / H
assert budget < Decimal("1.8e-10")
assert budget < Decimal(1)

report = (root / "CROSS_REVIEW_REPORT.md").read_text(encoding="utf-8")
assert "RH remains unproved" in report
assert "No headline actual-`Xi` claim is overturned" in report
assert "OPEN_SUFFICIENT_FOR_RH" in report

result = {
    "verdict": "PASS_REVIEWER_A_CROSS_REVIEW_B_DELTA",
    "delta_rows": len(delta),
    "graph_defects": len(graph),
    "missed_claim_candidates": len(missed),
    "xi_budget_upper": str(budget),
    "rh_proved": False,
    "heavy_campaigns_rerun": False,
}
out = Path(__file__).with_name("verification.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
