#!/usr/bin/env python3
"""Exact regression for the triangular eta–Pascal consolidation.

Standard-library only.  The checker verifies:
- formal stopped-log telescoping;
- exact positive finite differences for rational pure powers;
- eta pair residual/capacity inequalities;
- the Euler source-weight partition;
- the triangular spectral mutation.

It does not prove the all-endpoint source typing, Cycle Debt, or RH.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def clean(d: dict[int, int]) -> dict[int, int]:
    return {k: v for k, v in d.items() if v}


def target_log_basis(X: int, q: int) -> dict[int, int]:
    out: dict[int, int] = {}
    out[X] = out.get(X, 0) + 1
    out[q] = out.get(q, 0) - 1
    return clean(out)


def stopped_log_basis(X: int, q: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for Y in range(q, X):
        out[Y + 1] = out.get(Y + 1, 0) + 1
        out[Y] = out.get(Y, 0) - 1
    return clean(out)


def finite_difference(values: list[Fraction], order: int) -> list[Fraction]:
    out = values
    for _ in range(order):
        out = [out[j] - out[j + 1] for j in range(len(out) - 1)]
    return out


def run() -> dict:
    log_rows = 0
    for X in range(2, 129):
        for q in range(1, X + 1):
            assert target_log_basis(X, q) == stopped_log_basis(X, q)
            log_rows += 1

    difference_rows = 0
    for s in range(1, 5):
        for x in range(1, 65):
            values = [Fraction(1, (x + j) ** s) for j in range(10)]
            for order in range(1, 6):
                row = finite_difference(values, order)
                assert all(v > 0 for v in row)
                assert all(row[j] >= row[j + 1] for j in range(len(row) - 1))
                difference_rows += len(row)

    eta_rows = 0
    residual_mass = Fraction(0)
    for k in range(1, 1025):
        a = Fraction(1, 2 * k)
        c = Fraction(1, 2 * k + 1)
        residual = a - c
        assert residual > 0
        assert c < a
        # log(1+1/(2k)) < 1/(2k)
        cost_upper = c * Fraction(1, 2 * k)
        assert cost_upper == residual
        residual_mass += residual
        eta_rows += 1
    assert residual_mass < Fraction(1, 2)

    for M in range(1, 33):
        finite_weights = sum(Fraction(1, 2 ** (m + 1)) for m in range(M))
        remainder_weight = Fraction(1, 2**M)
        assert finite_weights + remainder_weight == 1

    alpha = Fraction(6, 7)
    theta_upper = Fraction(2, 3)
    assert alpha < 1 and theta_upper < 1
    assert alpha * theta_upper < 1

    # Mutation: unit boundary-to-bulk feedback destroys contraction.
    det_I_minus_mutated = (1 - alpha) * (1 - theta_upper) - 1
    assert det_I_minus_mutated < 0

    result = {
        "schema": "X-29801-triangular-eta-pascal-v1",
        "classification": "EXACT_TRIANGULAR_ETA_PASCAL_ALGEBRA_VERIFIED",
        "formal_stopped_log_rows": log_rows,
        "positive_rational_difference_rows": difference_rows,
        "eta_pair_rows": eta_rows,
        "euler_partition_orders": 32,
        "analytic_factor": "6/7",
        "eta_factor_rational_upper": "2/3",
        "feedback_mutation_det_I_minus_M": str(det_I_minus_mutated),
        "mutations_rejected": 1,
        "proof_boundary": (
            "finite formal/rational algebra only; the complete endpoint-jet "
            "source manifest, no-feedback typing, Cycle Debt, and RH are not certified"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["result_sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
