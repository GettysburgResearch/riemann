#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import csv, json, sys

root = Path(__file__).resolve().parent

def rows(name):
    with (root / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))

claims = rows("CLAIMS.tsv")
edges = rows("EDGES.tsv")
by_id = {r["semantic_id"]: r for r in claims}

required = {
    "CONSUMER.MELLIN.TWO_ROW",
    "CONSUMER.MELLIN.FIVE_THREE",
    "CONSUMER.MELLIN.SPECIALIZED_LANDAU",
    "API.MELLIN.SUBPOWER_NEGATIVE_MASS",
    "OPEN.ARITH.ROWS23_NATIVE",
    "OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS",
    "OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS",
}
assert required <= set(by_id)
assert by_id["OPEN.ARITH.ROWS23_NATIVE"]["final_verdict"].startswith("OPEN_")
assert by_id["OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS"]["final_verdict"].startswith("OPEN_")
assert by_id["OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS"]["final_verdict"].startswith("OPEN_")

# Exact two-row elimination:
# P2=2a-1-b, 3P3=5b-a-1-3a^2.
for a in map(Fraction, [-7, -1, 0, 1, 2, 5, 19]):
    b = 2*a - 1
    lhs = 5*b - a - 1 - 3*a*a
    rhs = -3*(a-1)*(a-2)
    assert lhs == rhs

# Every active RH edge has an explicit open premise.
for edge in edges:
    if edge["conclusion_id"] != "RH" or edge["final_verdict"] == "FALSE":
        continue
    premises = json.loads(edge["premise_ids"])
    assert any(by_id[p]["final_verdict"].startswith("OPEN_") for p in premises), edge["edge_id"]

result = {
    "status": "PASS_MELLIN_LANDAU_CONSUMER",
    "claims": len(claims),
    "edges": len(edges),
    "consumer_alone_reaches_rh": False,
    "two_row_elimination": "exact",
    "five_three_factorization": "-3(a-1)(a-2)",
    "rh_status": "UNPROVED",
}
(root / "validation.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
