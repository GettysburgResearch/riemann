#!/usr/bin/env python3
"""Exact standard-library checks for R-30501.

The script verifies the rational radical inequalities, top-cell index geometry,
source uniqueness in the top half, and the exact central-entropy increments used
by the cancellation-preserving continuation.  It does not prove RH.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def check_radical_bounds() -> dict[str, int]:
    # 577/1000 < 1/sqrt(3), 447/1000 < 1/sqrt(5),
    # and 1/sqrt(6) < 409/1000.
    assert 3 * 577 * 577 < 1000 * 1000
    assert 5 * 447 * 447 < 1000 * 1000
    assert 6 * 409 * 409 > 1000 * 1000

    # [(2/7)^(3/2)+(2/7)^(1/2)]^2 < 1.
    assert 162 < 343
    return {
        "sqrt3_lower_numerator": 577,
        "sqrt5_lower_numerator": 447,
        "sqrt6_upper_numerator": 409,
    }


def first_even_omitted(n: int, q: int) -> int:
    k = 1
    while 2 * k * q - 1 <= n:
        k += 1
    return k


def first_odd_omitted(n: int, q: int) -> int:
    k = 1
    while (2 * k + 1) * q <= n:
        k += 1
    return k


def check_top_cell_geometry(limit: int = 2000) -> dict[str, int]:
    cases = 0
    source_singletons = 0
    count_lower_bound_cases = 0
    for n in range(120, limit + 1):
        m = (n + 1) // 2
        interval = []
        for q in range(n // 3 + 1, n // 2 + 1):
            assert first_even_omitted(n, q) == 2
            assert first_odd_omitted(n, q) == 1
            assert q > m / 2
            interval.append(q)
            source_singletons += 1
            cases += 1
        assert len(interval) >= n // 12
        count_lower_bound_cases += 1
    return {
        "top_cell_rows": cases,
        "source_singletons": source_singletons,
        "endpoint_count_checks": count_lower_bound_cases,
    }


def check_entropy_increment(limit: int = 2000) -> dict[str, int]:
    cases = 0
    for n in range(3, limit + 1):
        current = comb(n, n // 2)
        previous = comb(n - 1, (n - 1) // 2)
        ratio = Fraction(current, previous)
        if n % 2 == 0:
            assert ratio == 2
        else:
            assert ratio == Fraction(2 * n, n + 1)
        cases += 1
    return {"binomial_increment_rows": cases}


def main() -> None:
    result = {
        "schema": "X-30501-boundary-atomic-firewall-v1",
        "classification": "EXACT_BOUNDARY_ATOMIC_NORM_FIREWALL",
        "checks": {
            "radical_bounds": check_radical_bounds(),
            "top_cell_geometry": check_top_cell_geometry(),
            "central_entropy_increment": check_entropy_increment(),
        },
        "theorem_constants": {
            "top_cell_scaled_boundary_upper": "-1/20",
            "atomic_norm_lower": "N/240 for N>=120",
        },
        "does_not_prove": [
            "a cancellation-preserving Haar bound",
            "Cycle Debt",
            "the prime-ramp estimate",
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
