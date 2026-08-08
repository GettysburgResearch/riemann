#!/usr/bin/env python3
"""Exact Q(sqrt(2)) replay for the critical Euler-filtered annular split frame.

Finite algebra only.  Does not prove ASSD or RH.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib
import json
from pathlib import Path


Pair = tuple[Fraction, Fraction]  # a+b sqrt(2)


def add(x: Pair, y: Pair) -> Pair:
    return (x[0] + y[0], x[1] + y[1])


def mul(x: Pair, y: Pair) -> Pair:
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def scale(x: Pair, q: Fraction) -> Pair:
    return (q * x[0], q * x[1])


def evaluate(coefficients: list[Pair], z: Pair) -> Pair:
    out = (Fraction(0), Fraction(0))
    z_power = (Fraction(1), Fraction(0))
    for coefficient in coefficients:
        out = add(out, mul(coefficient, z_power))
        z_power = mul(z_power, z)
    return out


def square(x: Pair) -> Pair:
    return mul(x, x)


def g(m: int, r: int) -> Fraction:
    if m <= r < 2 * m:
        return Fraction(1)
    if 2 * m <= r < 4 * m:
        return Fraction(-1, 2)
    return Fraction(0)


P = [
    (Fraction(1), Fraction(0)),
    (Fraction(-3), Fraction(-2)),
    (Fraction(4), Fraction(6)),
    (Fraction(-6), Fraction(-4)),
    (Fraction(4), Fraction(0)),
]


def scaled_coefficient(j: int) -> Pair:
    coefficient = P[j]
    if j % 2 == 0:
        return scale(coefficient, Fraction(2 ** (j // 2)))
    return mul(coefficient, (Fraction(0), Fraction(2 ** ((j - 1) // 2))))


def deterministic_coefficients(m: int) -> dict[int, Fraction]:
    return {
        index: Fraction(((index * index + 5 * index + 3) % 13) - 6, index + 3)
        for index in range(m, 2 * m)
    }


def main() -> None:
    assert evaluate(P, (Fraction(1, 2), Fraction(0))) == (0, 0)
    half_root_two = (Fraction(0), Fraction(1, 2))
    assert evaluate(P, half_root_two) == (0, 0)
    derivative = [scale(P[j], Fraction(j)) for j in range(1, len(P))]
    assert evaluate(derivative, half_root_two) == (0, 0)

    cell_rows = 0
    isometries = 0
    for m in range(1, 9):
        x = deterministic_coefficients(m)

        def base(r: int) -> Fraction:
            return sum(value * g(index, r) for index, value in x.items())

        def filtered(r: int) -> Pair:
            out = (Fraction(0), Fraction(0))
            for j in range(5):
                out = add(out, scale(scaled_coefficient(j), base(r // (2**j))))
            return out

        upper = 128 * m
        endpoint = 256 * m - 1
        assert all(filtered(r) == (0, 0) for r in range(0, m))
        assert all(filtered(r) == (0, 0) for r in range(upper, endpoint + 1))

        physical = (Fraction(0), Fraction(0))
        split = (Fraction(0), Fraction(0))
        for r in range(1, upper):
            physical = add(
                physical, scale(square(filtered(r)), Fraction(1, r * (r + 1)))
            )
            defect = add(
                filtered(endpoint),
                scale(add(filtered(r), filtered(endpoint - r)), Fraction(-1)),
            )
            split = add(
                split, scale(square(defect), Fraction(1, r * (r + 1)))
            )
            cell_rows += 1
        assert physical == split
        isometries += 1

    m = 4
    x = deterministic_coefficients(m)

    def base(r: int) -> Fraction:
        return sum(value * g(index, r) for index, value in x.items())

    def filtered(r: int) -> Pair:
        out = (Fraction(0), Fraction(0))
        for j in range(5):
            out = add(out, scale(scaled_coefficient(j), base(r // (2**j))))
        return out

    bad_endpoint = 128 * m - 1
    physical = (Fraction(0), Fraction(0))
    bad_split = (Fraction(0), Fraction(0))
    for r in range(1, 128 * m):
        physical = add(
            physical, scale(square(filtered(r)), Fraction(1, r * (r + 1)))
        )
        defect = add(
            filtered(bad_endpoint),
            scale(add(filtered(r), filtered(bad_endpoint - r)), Fraction(-1)),
        )
        bad_split = add(
            bad_split, scale(square(defect), Fraction(1, r * (r + 1)))
        )
    assert physical != bad_split

    result = {
        "schema": "X-26803-critical-filter-annular-v1",
        "classification": "EXACT_CRITICAL_FILTERED_ANNULAR_SPLIT_VERIFIED",
        "critical_polynomial_degree": 4,
        "pole_zero": "p(1/2)=0",
        "half_pole_double_zero": "p(1/sqrt(2))=p'(1/sqrt(2))=0",
        "filtered_cell_rows": cell_rows,
        "weighted_isometries": isometries,
        "mutations_rejected": 1,
        "proof_boundary": "finite Q(sqrt(2)) algebra only; ASSD and RH remain unproved",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
