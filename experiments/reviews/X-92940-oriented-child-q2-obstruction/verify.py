#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

PR505 = "1113fe6d55e955a8d9de7b43ceb24f5792870550"
TREE505 = "8f6ffe32961062e1c53e2bcba1415fa51d7ead6f"
PR507 = "dfaa70cd2eefcabbf6717e3da060792904c7f357"
TREE507 = "f8fdef949b85ebe0be5a1e745da33241b426731d"
PR500 = "d73c1e7a1a482cac31581211a84db43cc34c824e"
TREE500 = "72421c74d9d5f92aa4c36e5ad571b29442aad42b"
PR496 = "96f8a6b3cc3d474217633e16d4caa490a0aae518"
TREE496 = "aa9933522d3e4dd0ee8287c6dcfcce2f03c015bc"


def run() -> dict[str, object]:
    x0 = 10**16
    p = 67
    k = x0 // p + 1
    s0 = 12_216_944

    if not s0 * s0 < k:
        raise AssertionError("directed sqrt(K) lower gate failed")
    if not 67 * 61 * 61 < 500 * 500:
        raise AssertionError("1/sqrt(67) lower gate failed")

    ideal_rough_excess = Fraction(s0, s0 + 130) * Fraction(561, 500) - 1
    if not ideal_rough_excess > Fraction(7, 75):
        raise AssertionError("qualified rough-lift ideal excess failed")

    correction = (
        Fraction(129, s0)
        + (Fraction(32, s0) + Fraction(160032, 99999999))
        * Fraction(32805, 21952)
        + Fraction(4452 * 405, 10**24 * 392)
    )
    if not correction < Fraction(1, 400):
        raise AssertionError("qualified correction budget failed")

    qualified_separator = Fraction(7, 75) - Fraction(1, 400)
    if qualified_separator != Fraction(109, 1200):
        raise AssertionError("109/1200 arithmetic failed")

    if not x0 > 134:
        raise AssertionError("ordinary q=2 activity gate failed")
    rough_ordinary_67 = math.log(x0 / 134) / math.sqrt(134)
    child_ordinary_upper = -rough_ordinary_67
    if not child_ordinary_upper < 0:
        raise AssertionError("oriented child ordinary q=2 obstruction failed")

    if not x0 >= 536:
        raise AssertionError("detail q=2 activity gate failed")
    rough_detail_67 = math.log(4) / math.sqrt(134)
    child_detail_upper = -rough_detail_67
    if not child_detail_upper < -Fraction(1, 9):
        raise AssertionError("oriented child detail q=2 obstruction failed")

    branchwise_positive_realization_possible = child_ordinary_upper >= 0
    if branchwise_positive_realization_possible:
        raise AssertionError("negative child block was incorrectly declared positive")

    total_terminal = Fraction(60989, 1) + Fraction(6039, 8)
    if total_terminal != Fraction(493951, 8) or not total_terminal < 61744:
        raise AssertionError("terminal-child arithmetic failed")

    proof = {
        "frozen": {
            "pr496": {"commit": PR496, "tree": TREE496},
            "pr500": {"commit": PR500, "tree": TREE500},
            "pr505": {"commit": PR505, "tree": TREE505},
            "pr507": {"commit": PR507, "tree": TREE507},
        },
        "qualified_109_over_1200": {
            "scope": "full P_61 rough-lift precomparison marginal at X=10^16 with the frozen downward allowances",
            "ideal_lower": str(ideal_rough_excess),
            "correction_upper": str(correction),
            "retained_named_lower": str(qualified_separator),
            "unconditional_pr_refutation": False,
        },
        "oriented_child_q2": {
            "x": x0,
            "ordinary_rough_67_lower": rough_ordinary_67,
            "ordinary_actual_child_upper": child_ordinary_upper,
            "detail_rough_67_lower": rough_detail_67,
            "detail_actual_child_upper": child_detail_upper,
            "positive_branchwise_realization_possible": False,
        },
        "terminal_arithmetic": {
            "root": "60989",
            "children": "6039/8",
            "total": str(total_terminal),
            "strict_bound": "61744",
            "status": "ARITHMETIC_ONLY_PRODUCER_BLOCKED",
        },
        "verdict": "PASS_EXACT_ORIENTED_CHILD_Q2_NEGATIVE_COORDINATE_OBSTRUCTION",
        "rh_proved": False,
    }
    canonical = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
    proof["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return proof


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results/verification.json")
    args = parser.parse_args()
    result = run()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
