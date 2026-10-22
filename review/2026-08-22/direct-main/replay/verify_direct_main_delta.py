#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, getcontext
import csv, hashlib, json, re, sys

root = Path(__file__).resolve().parent.parent
replay = Path(__file__).resolve().parent

required = [
    "FREEZE.json",
    "COMMIT_PACKETS.tsv",
    "CLAIMS.tsv",
    "REFUTATIONS.tsv",
    "COMPUTATIONS.tsv",
    "OVERLAP_WITH_EXISTING_REVIEWS.tsv",
    "PROVENANCE_DEFECTS.tsv",
    "REPORT.md",
    "INTEGRATION_HANDOFF.md",
]
for name in required:
    p = root / name
    assert p.is_file() and p.stat().st_size > 0, name

sha40 = re.compile(r"^[0-9a-f]{40}$")

with (root / "COMMIT_PACKETS.tsv").open(newline="", encoding="utf-8") as f:
    packets = list(csv.DictReader(f, delimiter="\t"))
expected_packet_header = [
    "packet_id","first_commit","last_commit","family","principal_files","claim_ids",
    "existing_review_coverage","controlling_later_review","strongest_surviving_result",
    "first_broken_arrow","final_verdict","integration_action","notes","commit_count",
    "cumulative_end_index"
]
assert packets and list(packets[0].keys()) == expected_packet_header
assert len(packets) == 11
assert len({p["packet_id"] for p in packets}) == len(packets)
assert all(sha40.fullmatch(p["first_commit"]) and sha40.fullmatch(p["last_commit"]) for p in packets)
counts = [int(p["commit_count"]) for p in packets]
ends = [int(p["cumulative_end_index"]) for p in packets]
assert counts == [7,9,10,1,5,16,5,11,2,1,18]
assert ends == [7,16,26,27,32,48,53,64,66,67,85]
assert sum(counts) == 85
assert all(ends[i] == sum(counts[:i+1]) for i in range(len(ends)))
assert packets[0]["first_commit"] == "de605b718682b588dfad6736235347923f194dab"
assert packets[-1]["last_commit"] == "677203992eb0168920365ee45ae9db76bfa97dcf"

with (root / "CLAIMS.tsv").open(newline="", encoding="utf-8") as f:
    claims = list(csv.DictReader(f, delimiter="\t"))
assert len(claims) == 40
assert len({c["semantic_id"] for c in claims}) == len(claims)
allowed_verdicts = {
    "VERIFIED","VERIFIED_WITH_FIXES","CONDITIONAL_EXACT","OPEN_RH_EQUIVALENT",
    "GAP_BLOCKED","FALSE","SUPERSEDED"
}
assert all(c["review_verdict"] in allowed_verdicts for c in claims)
claim_by_id = {c["semantic_id"]: c for c in claims}
expected = {
    "DIRECTMAIN.CJ.T91006": "OPEN_RH_EQUIVALENT",
    "DIRECTMAIN.P79.L91350": "FALSE",
    "DIRECTMAIN.P79.T91304": "GAP_BLOCKED",
    "DIRECTMAIN.MELLIN.T96000": "GAP_BLOCKED",
    "DIRECTMAIN.TAYLOR.T99930": "CONDITIONAL_EXACT",
    "DIRECTMAIN.TAYLOR.L99932.CONSUMER": "OPEN_RH_EQUIVALENT",
}
for semantic_id, verdict in expected.items():
    assert claim_by_id[semantic_id]["review_verdict"] == verdict

substantive = {"DM-002A","DM-002B","DM-002C","DM-003A","DM-003B","DM-003C","DM-004","DM-007"}
assert substantive <= {c["packet_id"] for c in claims}

with (replay / "PACKET_BOUNDARIES.json").open(encoding="utf-8") as f:
    boundary = json.load(f)
assert boundary["commit_count"] == 85
assert boundary["targeted_review_required_count"] == 0
assert [p["packet_id"] for p in boundary["packets"]] == [p["packet_id"] for p in packets]
assert [p["cumulative_end_index"] for p in boundary["packets"]] == ends

# Exact light fixtures.
# L-91026: alpha and beta have sum 163/14 and product 16.
assert Fraction(163,14) == Fraction(326,28)
assert Fraction(163**2 - 25*561, 28**2) == 16

# Fixed rows 2 and 3 elimination used by the later consumer.
# P2=2x-1-y and 3P3=5y-x-1-3x^2. Substitute y=2x-1.
# The result must equal -3(x-1)(x-2).
for x in map(Fraction, [-3,-1,0,1,2,5,17]):
    y = 2*x - 1
    lhs = 5*y - x - 1 - 3*x*x
    rhs = -3*(x-1)*(x-2)
    assert lhs == rhs

# L-91355: exact survival/first-hazard partition and <1/8 child mass.
rs = [Fraction(1,9), Fraction(1,10), Fraction(1,11)]
survival = Fraction(1)
lambdas = []
alphas = []
for r in rs:
    lam = r * survival
    lambdas.append(lam)
    alphas.append(r * lam)
    survival *= (1-r)
assert survival + sum(lambdas, Fraction(0)) == 1
assert sum(alphas, Fraction(0)) < Fraction(1,8)

# L-99930: the explicit labelled prime-mass bound is strictly below one.
getcontext().prec = 70
S = (
    Decimal(2) ** Decimal("-1.5") +
    Decimal(3) ** Decimal("-1.5") +
    Decimal(5) ** Decimal("-1.5") +
    Decimal(7) ** Decimal("-1.5") +
    Decimal(11) ** Decimal("-1.5") +
    Decimal(1)/(Decimal(3)*Decimal(11).sqrt()) +
    Decimal(13) ** Decimal("-1.5") +
    Decimal(1)/(Decimal(3)*Decimal(13).sqrt()) +
    Decimal(67) ** Decimal("-1.5")
)
assert S < 1

# L-99932 quadratic kernel, at exact square arguments.
def k2_square_root(r):
    y = r*r
    if y < 1:
        return 16*y
    return 16*(2*r-1)
assert k2_square_root(Fraction(1,2)) == 4
assert k2_square_root(Fraction(2)) == 48
assert k2_square_root(Fraction(1)) == 16

# Freeze and report assertions.
freeze = json.loads((root / "FREEZE.json").read_text(encoding="utf-8"))
assert freeze["range"]["commit_count"] == 85
assert freeze["heavy_computation_rerun"] is False
assert freeze["scientific_status"] == "RH_UNPROVED"
report = (root / "REPORT.md").read_text(encoding="utf-8")
assert "DIRECT_MAIN_PACKET_CHANGES_RH_STATUS: false" in report
assert "No direct-main packet proves RH" in report

result = {
    "status": "PASS_DIRECT_MAIN_DELTA_REVIEW",
    "repository": "gfreund123/riemann",
    "base_exclusive": freeze["range"]["base"],
    "head_inclusive": freeze["range"]["head"],
    "commit_count": 85,
    "packet_count": len(packets),
    "substantive_packet_count": len(substantive),
    "claim_rows": len(claims),
    "targeted_review_required_count": 0,
    "direct_main_packet_changes_rh_status": False,
    "heavy_campaigns_rerun": False,
    "packet_commit_counts": counts,
    "cumulative_packet_end_indices": ends,
    "light_exact_fixtures": [
        "L-91026 alpha/beta sum-product",
        "fixed rows 2/3 elimination",
        "L-91355 nonduplication and child-mass bound",
        "L-99930 labelled prime-mass bound",
        "L-99932 quadratic kernel samples",
    ],
}
(replay / "RESULTS.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
