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
    # sqrt(2/3) < 5/6 because 2/3 < 25/36.
    assert Fraction(2, 3) < Fraction(25, 36)

    # log 2 > 2/3 from 2*atanh(1/3).
    # Retain only the first positive term.
    log2_lower = Fraction(2, 3)

    analytic_lower = Fraction(1, 6) * log2_lower
    assert analytic_lower == Fraction(1, 9)

    # sqrt(100/97) < 51/50.
    assert Fraction(100, 97) < Fraction(51 * 51, 50 * 50)

    # log(100/97) < 3/97 < 1/32.
    assert Fraction(3, 97) < Fraction(1, 32)
    finite_upper = Fraction(51, 50) * Fraction(1, 32)
    assert finite_upper == Fraction(51, 1600)

    moat = analytic_lower - finite_upper
    assert moat == Fraction(1141, 14400)
    assert moat > Fraction(1, 13)

    norm_constant = Fraction(1, 200) * Fraction(7, 10) * Fraction(1, 13)
    assert norm_constant > Fraction(1, 4000)

    return {
        "analytic_lower": str(analytic_lower),
        "finite_upper": str(finite_upper),
        "moat": str(moat),
        "atomic_norm_constant": str(norm_constant),
    }


def eta_half() -> Decimal:
    # Alternating eta series with pairwise positive terms and a rigorous
    # tail smaller than the first omitted pair. For the finite replay we use
    # high precision reconnaissance only; no verdict depends on it.
    total = Decimal(0)
    for k in range(1, 200000):
        even = Decimal(2 * k).sqrt()
        odd = Decimal(2 * k + 1).sqrt()
        total += Decimal(1) / even - Decimal(1) / odd
    return Decimal(1) - total


def cp_power(q: int, terms: int = 100000) -> Decimal:
    # Direct positive paired series.
    total = Decimal(0)
    for k in range(1, terms + 1):
        a = Decimal(2 * k * q - 1).sqrt()
        b = Decimal((2 * k + 1) * q).sqrt()
        total += Decimal(1) / a - Decimal(1) / b
    # Positive omitted tail means this is a lower approximation.
    return total


def finite_mutation() -> dict[str, object]:
    getcontext().prec = 50
    checked = 0
    minimum_scaled = None
    for X in (400, 800, 1600, 3200):
        lo = (49 * X + 99) // 100
        hi = X // 2
        for q in range(lo, hi + 1):
            analytic = (Decimal(X) / Decimal(q)).ln() * cp_power(q, 20000)
            n = 2 * q - 1
            finite = (Decimal(X) / Decimal(n)).ln() / Decimal(n).sqrt()
            boundary = analytic - finite
            scaled = boundary * Decimal(X).sqrt()
            if minimum_scaled is None or scaled < minimum_scaled:
                minimum_scaled = scaled
            assert scaled > Decimal(1) / Decimal(13)
            checked += 1
    return {
        "annulus_rows": checked,
        "minimum_scaled_boundary": str(minimum_scaled),
        "classification": "HIGH_PRECISION_RECONNAISSANCE_ONLY",
    }


def main() -> None:
    results = {
        "schema": "X-30501-terminal-boundary-obstruction-v1",
        "classification": "EXACT_RATIONAL_GATE_PLUS_DECIMAL_RECONNAISSANCE",
        "exact_gate": exact_gate(),
        "finite_mutation": finite_mutation(),
        "does_not_prove": [
            "a lower bound for optimized Cycle Debt",
            "impossibility of a coupled analytic/finite flow repair",
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
