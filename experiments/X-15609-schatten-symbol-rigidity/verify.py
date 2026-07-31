#!/usr/bin/env python3
"""Exact Fraction-only regression for L-15623.

The script verifies:

1. the exact three-defect decomposition of the symbol moment excess;
2. a strict passing case with nonzero symbol slack and nonzero uncaptured tail;
3. an extra-low-mode case whose moment excess exceeds one complete gap quantum.

This is finite synthetic arithmetic only.  It does not evaluate Suzuki's symbol
or prove the Riemann hypothesis.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F


def fj(x: F) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def main() -> int:
    G = F(3)
    alpha = F(1)
    Gamma = F(2)
    t = F(3, 2)
    r = 2
    d = 2
    kappa = G - alpha
    theta = G - Gamma

    # Passing case.  A=G I-D and L=span(e1,e2).
    deficit_pass = [F(2), F(2), F(1, 2), F(1, 4)]
    operator_pass = [G - value for value in deficit_pass]
    true_moment = sum((value**r for value in deficit_pass), F(0))

    # Deliberately include nonzero symbol/KSS slack.
    symbol_moment_upper = true_moment + F(1, 10)
    symbol_slack = symbol_moment_upper - true_moment
    packet_flatness_slack = (
        sum((value**r for value in deficit_pass[:d]), F(0))
        - d * kappa**r
    )
    uncaptured_tail = sum((value**r for value in deficit_pass[d:]), F(0))
    total_excess = symbol_moment_upper - d * kappa**r

    assert symbol_slack == F(1, 10)
    assert packet_flatness_slack == 0
    assert uncaptured_tail == F(5, 16)
    assert total_excess == symbol_slack + packet_flatness_slack + uncaptured_tail
    assert total_excess == F(33, 80)
    assert total_excess <= theta**r
    assert sum(value < t for value in operator_pass) == d
    assert sum(value < Gamma for value in operator_pass) == d
    assert min(operator_pass[d:]) >= Gamma

    # Failure case: the third coordinate is an additional direction below t.
    deficit_fail = [F(2), F(2), F(8, 5), F(1, 4)]
    operator_fail = [G - value for value in deficit_fail]
    fail_true_moment = sum((value**r for value in deficit_fail), F(0))
    fail_excess = fail_true_moment - d * kappa**r
    one_gap_quantum = (G - t) ** r

    assert operator_fail[2] < t
    assert sum(value < t for value in operator_fail) == d + 1
    assert fail_excess == F(1049, 400)
    assert fail_excess > one_gap_quantum
    assert one_gap_quantum > theta**r

    result = {
        "schema": "riemann.x15609-schatten-symbol-rigidity.v1",
        "pass_case": {
            "G": fj(G),
            "alpha": fj(alpha),
            "Gamma": fj(Gamma),
            "t": fj(t),
            "r": r,
            "dimension": d,
            "deficit_eigenvalues": [fj(value) for value in deficit_pass],
            "operator_eigenvalues": [fj(value) for value in operator_pass],
            "symbol_moment_upper": fj(symbol_moment_upper),
            "true_schatten_moment": fj(true_moment),
            "symbol_to_operator_slack": fj(symbol_slack),
            "packet_flatness_slack": fj(packet_flatness_slack),
            "uncaptured_tail_moment": fj(uncaptured_tail),
            "total_symbol_excess": fj(total_excess),
            "right_side": fj(theta**r),
            "exact_low_count_below_t": sum(value < t for value in operator_pass),
            "exact_low_count_below_Gamma": sum(
                value < Gamma for value in operator_pass
            ),
            "classification": (
                "EXACT_PASS_WITH_NONZERO_SYMBOL_SLACK_AND_UNCAPTURED_TAIL"
            ),
        },
        "extra_low_mode_case": {
            "deficit_eigenvalues": [fj(value) for value in deficit_fail],
            "operator_eigenvalues": [fj(value) for value in operator_fail],
            "true_schatten_excess": fj(fail_excess),
            "one_gap_quantum": fj(one_gap_quantum),
            "right_side": fj(theta**r),
            "exact_low_count_below_t": sum(
                value < t for value in operator_fail
            ),
            "exact_low_count_below_Gamma": sum(
                value < Gamma for value in operator_fail
            ),
            "classification": "EXACT_EXTRA_LOW_MODE_FORCES_TARGET_FAILURE",
        },
        "verdict": "PASS_EXACT_L15623_SCHATTEN_DEFECT_DECOMPOSITION",
    }

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
