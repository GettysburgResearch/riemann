#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import json
from pathlib import Path

getcontext().prec = 60

ROUGH_SCALES = [64, 67, 71, 101, 127, 257]
MAX_M = 1500
EPSILON = Decimal(1) / (Decimal(10) ** 30)


def prefix_inverse_square_roots(limit: int) -> list[Decimal]:
    values = [Decimal(0)] * (limit + 1)
    for n in range(1, limit + 1):
        values[n] = values[n - 1] + Decimal(1) / Decimal(n).sqrt()
    return values


def endpoint_port(x: Decimal, prefixes: list[Decimal]) -> Decimal:
    n = int(x)
    return Decimal(2 * n) / x.sqrt() - prefixes[n]


def verify() -> dict:
    # Exact constants in the analytic proof.
    assert Fraction(21, 64) - Fraction(5, 48) == Fraction(43, 192)
    assert Fraction(43, 192) > 0

    polynomial_checks = 0
    for n in range(1, 10001):
        assert n * (n + 2) ** 2 - (n + 1) ** 3 == n * n + n - 1
        assert n * n + n - 1 > 0
        polynomial_checks += 1

    maximum_n = max(ROUGH_SCALES) * MAX_M + max(ROUGH_SCALES)
    prefixes = prefix_inverse_square_roots(maximum_n)

    scale_checks = 0
    minimum = None
    for scale in ROUGH_SCALES:
        residues = [0, 1, scale // 2, scale - 2, scale - 1]
        for m in range(1, MAX_M + 1):
            for residue in residues:
                n = scale * m + residue
                for x in (Decimal(n), Decimal(n + 1) - EPSILON):
                    difference = (
                        endpoint_port(x, prefixes)
                        - endpoint_port(x / Decimal(scale), prefixes)
                    )
                    assert difference > 0, (scale, m, residue, x, difference)
                    scale_checks += 1
                    record = (difference, scale, m, residue, str(x))
                    if minimum is None or record[0] < minimum[0]:
                        minimum = record

    # Exact geometric normalization:
    # sum_(j=0)^J (1-r)r^j + r^(J+1) = 1.
    geometric_checks = 0
    for denominator in (8, 9, 11, 13, 17):
        r = Fraction(1, denominator)
        for cutoff in range(0, 30):
            partial = sum((1 - r) * r**j for j in range(cutoff + 1))
            assert partial + r ** (cutoff + 1) == 1
            geometric_checks += 1

    return {
        "classification": "PASS_ROUGH_SCALE_ENDPOINT_PORT_RENEWAL",
        "analytic_margin": "43/192",
        "rough_scales_scanned": ROUGH_SCALES,
        "maximum_quotient_block": MAX_M,
        "directed_decimal_scale_checks": scale_checks,
        "minimum_scanned_difference": {
            "lower_decimal": str(minimum[0]),
            "scale": minimum[1],
            "block": minimum[2],
            "residue": minimum[3],
            "x": minimum[4],
        },
        "exact_derivative_polynomial_checks": polynomial_checks,
        "exact_geometric_normalization_checks": geometric_checks,
        "scope": (
            "The theorem is analytic. Decimal scans are high-precision mutation "
            "guards at cell endpoints; all displayed proof constants and "
            "geometric normalizations are exact."
        ),
    }


if __name__ == "__main__":
    result = verify()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
