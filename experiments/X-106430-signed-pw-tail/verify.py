#!/usr/bin/env python3
"""Exact finite replay for T-106430.

The replay checks Laguerre coverage algebra, the finite-rank coverage ledger,
the signed Hankel trace split, cancellation of equal absolute complement
charges, and the exact ninety-percent constants.  It does not evaluate Xi or
prove SIGNEDTAIL106430.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return out


def poly_derivative(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * a[i] for i in range(1, len(a))] or [Fraction(0)]


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def laguerre(order: int) -> list[Fraction]:
    return [
        Fraction((-1) ** k * comb(order, k), factorial(k))
        for k in range(order + 1)
    ]


def tail_polynomial(poly: list[Fraction]) -> list[Fraction]:
    """P such that integral_x^infty exp(-t) poly(t) dt = exp(-x) P(x)."""
    out = [Fraction(0)] * len(poly)
    for degree, coefficient in enumerate(poly):
        for power in range(degree + 1):
            out[power] += coefficient * Fraction(
                factorial(degree), factorial(power)
            )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def diagonal_trace(values: list[Fraction], keep: set[int]) -> Fraction:
    return sum((value for index, value in enumerate(values) if index in keep), Fraction(0))


def run() -> dict[str, object]:
    # L-106430.1--3.  Orthogonality and the incomplete-gamma tail polynomial.
    for order in range(9):
        square = poly_mul(laguerre(order), laguerre(order))
        full_integral = sum(
            coefficient * factorial(power)
            for power, coefficient in enumerate(square)
        )
        assert full_integral == 1

        tail = tail_polynomial(square)
        # d[e^-x P]/dx = -e^-x L_q(x)^2, equivalently P-P'=L_q^2.
        left = poly_add(tail, [-value for value in poly_derivative(tail)])
        assert left == square

    assert tail_polynomial(poly_mul(laguerre(0), laguerre(0))) == [Fraction(1)]

    getcontext().prec = 50
    simple_tail = (Decimal(-1) / Decimal(100)).exp()
    assert simple_tail > Decimal(99) / Decimal(100)

    # L-106430.7.  A rank-d positive contraction on an m-space misses at
    # least m-d trace units.
    coverage_eigenvalues = [
        Fraction(1),
        Fraction(3, 4),
        Fraction(1, 2),
        Fraction(1, 4),
        Fraction(0),
        Fraction(0),
        Fraction(0),
    ]
    dimension = len(coverage_eigenvalues)
    rank = sum(value != 0 for value in coverage_eigenvalues)
    trace_deficit = Fraction(dimension) - sum(coverage_eigenvalues)
    assert trace_deficit >= dimension - rank

    # L-106431.4.  Exact visible/complement signed trace decomposition.
    a_minus = [Fraction(3, 4), Fraction(1, 2), Fraction(1, 4), Fraction(0)]
    a_plus = [Fraction(1, 4), Fraction(1, 4), Fraction(0), Fraction(0)]
    visible_indices = {0, 1}
    total_signed = sum(a_minus) - sum(a_plus)
    visible_signed = diagonal_trace(a_minus, visible_indices) - diagonal_trace(
        a_plus, visible_indices
    )
    complement_indices = set(range(4)) - visible_indices
    complement_signed = diagonal_trace(a_minus, complement_indices) - diagonal_trace(
        a_plus, complement_indices
    )
    assert total_signed == visible_signed + complement_signed
    assert visible_signed <= diagonal_trace(a_minus, visible_indices)

    # Large absolute pole and zero tails may cancel exactly in the index.
    equal_minus = [Fraction(1)] * 7
    equal_plus = [Fraction(1)] * 7
    absolute_tail = sum(equal_minus) + sum(equal_plus)
    signed_tail = sum(equal_minus) - sum(equal_plus)
    assert absolute_tail == 14
    assert signed_tail == 0

    source_budget = Fraction(1, 600)
    ninety_margin = Fraction(599, 625) - Fraction(9, 10)
    ninety_five_margin = Fraction(599, 625) - Fraction(19, 20)
    signed_ninety = ninety_margin - source_budget
    signed_ninety_five = ninety_five_margin - source_budget
    assert signed_ninety == Fraction(851, 15000)
    assert signed_ninety_five == Fraction(101, 15000)

    result: dict[str, object] = {
        "schema": "riemann.x106430.signed-pw-tail.v1",
        "classification": "PASS_T106430_SIGNED_PALEY_WIENER_TAIL_REDUCTION",
        "laguerre_orders_checked": 9,
        "simple_factor_tail_formula_checked": True,
        "simple_factor_tail_above_99_percent": True,
        "rank_ledger_checked": True,
        "signed_trace_split_checked": True,
        "absolute_deficit_cancellation_fixture_checked": True,
        "visible_source_budget": "1/600",
        "signed_tail_ninety_threshold": "851/15000",
        "signed_tail_ninety_five_threshold": "101/15000",
        "pwsamp106420_proved": False,
        "signedtail106430_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
