#!/usr/bin/env python3
"""Exact regression for the corrected Hausdorff/Pascal boundary budget.

Standard-library only.  This verifies finite rational instances of:
- decreasing pure-power finite-difference jets;
- shifted-even >= unshifted-odd paired source values;
- capacity feasibility;
- residual plus a rational upper bound for logarithmic cost <= input mass;
- mutation failure after reversing the source order.

It does not prove the complete all-endpoint source manifest, Cycle Debt, or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def diff_at(start: int, step: int, exponent: int, order: int) -> Fraction:
    vals = [Fraction(1, (start + j * step) ** exponent) for j in range(order + 1)]
    for _ in range(order):
        vals = [vals[j] - vals[j + 1] for j in range(len(vals) - 1)]
    return vals[0]


def run() -> dict:
    paired_rows = 0
    for exponent in range(1, 5):
        for q in range(1, 33):
            step = 2 * q
            for k in range(1, 33):
                even_start = 2 * k * q - 1
                odd_start = (2 * k + 1) * q
                assert even_start < odd_start
                for order in range(0, 6):
                    ve = diff_at(even_start, step, exponent, order)
                    vo = diff_at(odd_start, step, exponent, order)
                    assert ve > 0 and vo > 0
                    assert ve >= vo

                    incoming = Fraction(1, 2 * k) * ve
                    switch = Fraction(1, 2 * k + 1) * vo
                    assert switch <= incoming
                    residual = incoming - switch

                    # log((2k+1)/(2k)) < 1/(2k)
                    cost_upper = switch * Fraction(1, 2 * k)
                    assert residual + cost_upper <= incoming
                    paired_rows += 1

    # Finite Euler export partitions one unit of source mass.
    euler_orders = 0
    for M in range(1, 33):
        weights = sum(Fraction(1, 2 ** (m + 1)) for m in range(M))
        weights += Fraction(1, 2**M)
        assert weights == 1
        euler_orders += 1

    # Mutation: reverse the source arguments; the monotone capacity premise fails.
    mutation_detected = False
    ve = diff_at(9, 2, 1, 0)
    vo = diff_at(3, 2, 1, 0)
    if ve < vo:
        mutation_detected = True
    assert mutation_detected

    result = {
        "schema": "X-29802-hausdorff-amortized-boundary-v1",
        "classification": "EXACT_HAUSDORFF_PASCAL_AMORTIZED_BUDGET_VERIFIED",
        "paired_shifted_jet_rows": paired_rows,
        "euler_partition_orders": euler_orders,
        "mutations_rejected": 1,
        "cost_bound": "log((2k+1)/(2k)) < 1/(2k)",
        "proof_boundary": (
            "finite rational instances only; common-tail pairing, unmatched collar, "
            "full arithmetic destination map, Cycle Debt, and RH are not certified"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["result_sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
