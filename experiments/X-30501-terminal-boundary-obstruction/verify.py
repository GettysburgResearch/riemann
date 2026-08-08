#!/usr/bin/env python3
"""Exact and directed replay for L/R-30501.

The proof of the all-X lower bound is symbolic. The finite replay uses
standard-library Decimal arithmetic only as an additional mutation check.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


def exact_gate() -> dict[str, str]:
    # Euler lower bound for eta(1/2):
    # 29/32 - 11/(16 sqrt(2)) + 5/(16 sqrt(3)) > 3/5.
    # Rational square enclosures:
    assert Fraction(1, 2) < Fraction(7072, 10000) ** 2
    assert Fraction(5773, 10000) ** 2 < Fraction(1, 3)
    eta_lower = (
        Fraction(29, 32)
        - Fraction(11, 16) * Fraction(7072, 10000)
        + Fraction(5, 16) * Fraction(5773, 10000)
    )
    assert eta_lower > Fraction(3, 5)

    # Faster-power tail at q>=100:
    # (1-x)^(-1/2)-1 < 200/79401 for x<=1/200,
    # and 3/sqrt(2)<3.
    assert Fraction(199, 200) ** 2 < Fraction(199, 200)
    tail_upper = Fraction(600, 79401)
    assert tail_upper < Fraction(1, 132)

    analytic_upper = Fraction(2, 5) + Fraction(1, 132)
    assert analytic_upper == Fraction(269, 660)

    point_lower = Fraction(7, 10)
    gap = point_lower - analytic_upper
    assert gap == Fraction(193, 660)

    log_lower = Fraction(1, 10)
    moat = gap * log_lower
    assert moat == Fraction(193, 6600)
    assert moat > Fraction(1, 35)

    norm_constant = Fraction(1, 25) * Fraction(3, 5) * Fraction(1, 35)
    assert norm_constant == Fraction(3, 4375)
    assert norm_constant > Fraction(1, 1500)

    return {
        "eta_lower_rational": str(eta_lower),
        "tail_upper": str(tail_upper),
        "analytic_upper": str(analytic_upper),
        "point_gap": str(gap),
        "boundary_moat": str(moat),
        "atomic_norm_constant": str(norm_constant),
    }


def cp_power(q: int, terms: int = 100000) -> Decimal:
    total = Decimal(0)
    for k in range(1, terms + 1):
        a = Decimal(2 * k * q - 1).sqrt()
        b = Decimal((2 * k + 1) * q).sqrt()
        total += Decimal(1) / a - Decimal(1) / b
    return total


def finite_mutation() -> dict[str, object]:
    getcontext().prec = 50
    checked = 0
    largest_scaled = None
    for X in (400, 800, 1600):
        lo = (2 * X + 4) // 5
        hi = 9 * X // 20
        for q in range(lo, hi + 1):
            ratio_log = (Decimal(X) / Decimal(2 * q - 1)).ln()
            boundary = ratio_log * (
                cp_power(q, 2000) - Decimal(1) / Decimal(2 * q - 1).sqrt()
            )
            scaled = boundary * Decimal(X).sqrt()
            if largest_scaled is None or scaled > largest_scaled:
                largest_scaled = scaled
            assert scaled < -Decimal(1) / Decimal(35)
            checked += 1
    return {
        "annulus_rows": checked,
        "largest_scaled_boundary": str(largest_scaled),
        "classification": "HIGH_PRECISION_RECONNAISSANCE_ONLY",
    }


def main() -> None:
    results = {
        "schema": "X-30501-terminal-boundary-obstruction-v2",
        "classification": "EXACT_RATIONAL_GATE_PLUS_DECIMAL_RECONNAISSANCE",
        "exact_gate": exact_gate(),
        "finite_mutation": finite_mutation(),
        "does_not_prove": [
            "a lower bound for optimized Cycle Debt",
            "impossibility of an activated finite/analytic flow repair",
            "RH or its negation",
        ],
    }
    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    out = Path(__file__).with_name("results") / "verification.json"
    out.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
