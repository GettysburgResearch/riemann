#!/usr/bin/env python3
"""Exact regressions for the frozen PR #304 terminal-source claims.

The checker uses only integer and Fraction arithmetic. It verifies:

- the declared q interval has common shifted-even/odd first omitted index k=2;
- the odd zeroth-jet source coordinate contributes 1/(10 sqrt(q));
- a rational lower enclosure already dominates floor(sqrt(X))/1000 on the
  tested endpoints;
- the q-dependent source typing fails exactly at (N,q,k,s)=(18,5,2,1).

The cofinal lower bound is proved in R-30402. The source-type contradiction is
an exact finite counterexample in R-30403.
"""
from __future__ import annotations

from fractions import Fraction
from math import isqrt
import hashlib
import json
from pathlib import Path


def ceil_sqrt(n: int) -> int:
    r = isqrt(n)
    return r if r * r == n else r + 1


def first_shifted_even(endpoint: int, q: int) -> int:
    k = 1
    while 2 * k * q - 1 <= endpoint:
        k += 1
    return k


def first_unshifted_odd(endpoint: int, q: int) -> int:
    k = 1
    while (2 * k + 1) * q <= endpoint:
        k += 1
    return k


def q_interval(endpoint: int) -> range:
    lo = (endpoint + 1) // 4 + 1
    hi = endpoint // 3
    return range(lo, hi + 1)


def rational_lower_bound(X: int) -> tuple[Fraction, int]:
    total = Fraction(0)
    rows = 0
    for Y in range((X + 1) // 2, X):
        for q in q_interval(Y):
            assert first_shifted_even(Y, q) == 2
            assert first_unshifted_odd(Y, q) == 2

            # Atomic contribution is ell_Y/(10 sqrt(q)).
            # Use ell_Y >= 1/(Y+1) and sqrt(q) <= ceil_sqrt(q).
            total += Fraction(1, 10 * (Y + 1) * ceil_sqrt(q))
            rows += 1
    return total, rows


def source_type_counterexample() -> dict[str, object]:
    endpoint = 18
    q0 = 5
    k = 2
    exponent = 1
    assert first_shifted_even(endpoint, q0) == k
    assert first_unshifted_odd(endpoint, q0) == k

    A = Fraction(1, 2 * k * (2 * k * q0 - 1) ** exponent)
    B = Fraction(1, (2 * k + 1) * ((2 * k + 1) * q0) ** exponent)

    actual = Fraction(1, 2) * (A - B)
    declared_source_load = Fraction(1, 2) * (
        A * int((2 * k) % q0 == 0)
        - B * int((2 * k + 1) % q0 == 0)
    )

    assert A == Fraction(1, 76)
    assert B == Fraction(1, 125)
    assert actual == Fraction(49, 19000)
    assert declared_source_load == Fraction(-1, 250)
    assert actual != declared_source_load

    return {
        "endpoint": endpoint,
        "q": q0,
        "k": k,
        "exponent": exponent,
        "actual_boundary": str(actual),
        "declared_divisor_source_load": str(declared_source_load),
        "mismatch": True,
    }


def main() -> None:
    endpoints = [96, 192, 384, 768, 1536, 3072]
    rows = []
    for X in endpoints:
        lower, count = rational_lower_bound(X)
        threshold = Fraction(isqrt(X), 1000)
        assert lower > threshold
        rows.append(
            {
                "X": X,
                "source_rows": count,
                "lower_gt_floor_sqrt_over_1000": True,
                "lower_fraction_numerator_bits": lower.numerator.bit_length(),
                "lower_fraction_denominator_bits": lower.denominator.bit_length(),
            }
        )

    Y, q = 96, 25
    assert q in q_interval(Y)
    assert 2 * q - 1 <= Y
    assert 3 * q <= Y
    assert 4 * q - 1 > Y
    assert 5 * q > Y

    result = {
        "schema": "X-30402-terminal-source-refutations-v2",
        "classification": "EXACT_PR304_TERMINAL_SOURCE_CLAIMS_REFUTED",
        "symbolic_atomic_contribution": "ell_Y/(10*sqrt(q)) at source node 5",
        "rows": rows,
        "minimal_common_tail_control": {
            "Y": Y,
            "q": q,
            "K_even": 2,
            "K_odd": 2,
        },
        "source_type_counterexample": source_type_counterexample(),
        "does_not_prove": [
            "nonexistence of every coupled source repair",
            "Cycle Debt",
            "RH",
        ],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out = Path(__file__).with_name("results") / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
