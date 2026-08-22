#!/usr/bin/env python3
"""Exact/floating replay for L-90025.

The proof is analytic.  This checker authenticates the thirteen finite aligned
radical inequalities, the three nonaligned polynomial remainders, the m>=14
rational tail comparison, and a broad floating factor-four scan.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCALE = 10**30


def sqrt_bounds(n: int) -> tuple[Fraction, Fraction]:
    root = math.isqrt(n * SCALE * SCALE)
    lower = Fraction(root, SCALE)
    if root * root == n * SCALE * SCALE:
        return lower, lower
    return lower, Fraction(root + 1, SCALE)


def inverse_sqrt_bounds(n: int) -> tuple[Fraction, Fraction]:
    lower, upper = sqrt_bounds(n)
    return Fraction(1, 1) / upper, Fraction(1, 1) / lower


def aligned_finite_base() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for m in range(1, 14):
        _, denominator_upper = sqrt_bounds(4 * m + 1)
        lower = Fraction(4 * m, 1) / denominator_upper
        for k in range(m + 1, 4 * m + 1):
            _, term_upper = inverse_sqrt_bounds(k)
            lower -= term_upper
        if lower <= 0:
            raise AssertionError((m, lower))
        rows.append(
            {
                "m": m,
                "directed_lower_bound": str(lower),
                "decimal": float(lower),
            }
        )
    return rows


def nonaligned_remainders() -> dict[str, object]:
    # Positive numerator polynomials after the two squarings in L-90025.10.
    samples = []
    for m in range(1, 1001):
        numerators = {
            1: 8 * m + 3,
            2: 64 * m**3 + 135 * m**2 + 92 * m + 20,
            3: 96 * m**3 + 272 * m**2 + 240 * m + 63,
        }
        if min(numerators.values()) <= 0:
            raise AssertionError((m, numerators))
        if m in (1, 2, 10, 100, 1000):
            samples.append({"m": m, "numerators": numerators})
    return {
        "symbolic_positive_coefficient_polynomials": {
            "r=1": "8m+3",
            "r=2": "64m^3+135m^2+92m+20",
            "r=3": "96m^3+272m^2+240m+63",
        },
        "sample_checks": samples,
    }


def aligned_tail() -> dict[str, object]:
    # The final lower bound is m^{-5/2}(m/192-37/512), positive for m>=14.
    at_14 = Fraction(14, 192) - Fraction(37, 512)
    if at_14 <= 0:
        raise AssertionError(at_14)
    return {
        "tail_remainder": "m^(-5/2)(m/192-37/512)",
        "value_of_bracket_at_m_14": str(at_14),
        "positive_for_every_m_at_least_14": True,
    }


def harmonic_sqrt_prefix(n: int) -> list[float]:
    prefix = [0.0] * (n + 1)
    total = 0.0
    for k in range(1, n + 1):
        total += 1.0 / math.sqrt(k)
        prefix[k] = total
    return prefix


def floating_scan(max_x: int) -> dict[str, object]:
    prefix = harmonic_sqrt_prefix(max_x)
    minimum = float("inf")
    minimum_x = None
    # Scan integer cells at their worst right endpoint x -> n+1.
    for n in range(4, max_x + 1):
        m = n // 4
        value = 2.0 * (n - 2 * m) / math.sqrt(n + 1.0) - (
            prefix[n] - prefix[m]
        )
        if value < minimum:
            minimum = value
            minimum_x = n
        if value <= 0:
            raise AssertionError((n, m, value))
    return {
        "max_integer_cell": max_x,
        "minimum_worst_endpoint_lower_bound": minimum,
        "attained_at_floor_x": minimum_x,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output", type=Path, default=HERE / "results" / "verification.json"
    )
    args = parser.parse_args()
    if args.max_x < 100:
        raise SystemExit("--max-x must be at least 100")
    result = {
        "classification": "PASS_FACTOR4_ENDPOINT_RENEWAL_CERTIFICATE",
        "aligned_finite_base": aligned_finite_base(),
        "nonaligned": nonaligned_remainders(),
        "aligned_tail": aligned_tail(),
        "floating_scan": floating_scan(args.max_x),
        "scope": (
            "The finite base and rational tail bracket authenticate the exact "
            "proof. The million-cell scan is regression only."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(args.output)


if __name__ == "__main__":
    main()
