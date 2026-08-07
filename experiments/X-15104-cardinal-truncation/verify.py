#!/usr/bin/env python3
"""Exact standard-library regression for R-15102.

The analytic theorem proves every finite cardinal numerator has no real root.
This checker independently reconstructs the integer polynomial and counts its
real roots with an exact Fraction-based Sturm chain for a declared finite
ladder. It is a regression, not the proof of the all-N theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable

SCHEMA = "riemann.cardinal-truncation-obstruction.v1"


def trim(poly: list[Fraction]) -> list[Fraction]:
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max(len(a), len(b)))]
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def multiply(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def divide_polynomials(
    numerator: list[Fraction], denominator: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    num = trim([Fraction(value) for value in numerator])
    den = trim([Fraction(value) for value in denominator])
    if den == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(num) < len(den):
        return [Fraction(0)], num

    quotient = [Fraction(0) for _ in range(len(num) - len(den) + 1)]
    remainder = list(num)
    while remainder != [0] and len(remainder) >= len(den):
        offset = len(remainder) - len(den)
        factor = remainder[-1] / den[-1]
        quotient[offset] += factor
        for j, value in enumerate(den):
            remainder[offset + j] -= factor * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * poly[i] for i in range(1, len(poly))])


def evaluate(poly: list[Fraction], x: int | Fraction) -> Fraction:
    point = Fraction(x)
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * point + coefficient
    return value


def scalar_sign(value: Fraction) -> int:
    return int(value > 0) - int(value < 0)


def sign_at_infinity(poly: list[Fraction], positive: bool) -> int:
    reduced = trim(poly)
    out = scalar_sign(reduced[-1])
    if not positive and (len(reduced) - 1) % 2:
        out = -out
    return out


def variations(signs: Iterable[int]) -> int:
    nonzero = [value for value in signs if value]
    return sum(nonzero[i] != nonzero[i - 1] for i in range(1, len(nonzero)))


def sturm_chain(poly: list[Fraction]) -> list[list[Fraction]]:
    first = trim(poly)
    second = derivative(first)
    chain = [first, second]
    while second != [0]:
        _, remainder = divide_polynomials(first, second)
        if remainder == [0]:
            break
        remainder = [-value for value in remainder]
        chain.append(remainder)
        first, second = second, remainder
    return chain


def real_root_count(poly: list[Fraction]) -> int:
    chain = sturm_chain(poly)
    at_minus = variations(sign_at_infinity(item, False) for item in chain)
    at_plus = variations(sign_at_infinity(item, True) for item in chain)
    return at_minus - at_plus


def alternating_sign(index: int) -> int:
    return -1 if index % 2 else 1


def cardinal_polynomial(
    degree_parameter: int, signs: dict[int, int] | None = None
) -> tuple[list[Fraction], list[Fraction]]:
    denominator = [Fraction(1)]
    for node in range(-degree_parameter, degree_parameter + 1):
        denominator = multiply(denominator, [Fraction(-node), Fraction(1)])

    numerator = [Fraction(0)]
    residues = signs or {
        node: alternating_sign(node)
        for node in range(-degree_parameter, degree_parameter + 1)
    }
    for node in range(-degree_parameter, degree_parameter + 1):
        quotient, remainder = divide_polynomials(
            denominator, [Fraction(-node), Fraction(1)]
        )
        if remainder != [0]:
            raise AssertionError("nonzero exact division remainder")
        numerator = add(
            numerator,
            [Fraction(residues[node]) * value for value in quotient],
        )
    return trim(numerator), denominator


def canonical_digest(data: dict) -> str:
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def verify(data: dict) -> dict:
    if data.get("schema") != SCHEMA:
        raise ValueError("bad schema")

    maximum = data.get("max_n")
    if (
        isinstance(maximum, bool)
        or not isinstance(maximum, int)
        or maximum < 1
        or maximum > 64
    ):
        raise ValueError("max_n must be an integer in [1,64]")

    rows = []
    for parameter in range(1, maximum + 1):
        numerator, _ = cardinal_polynomial(parameter)
        root_count = real_root_count(numerator)
        node_nonzero = all(
            evaluate(numerator, node) != 0
            for node in range(-parameter, parameter + 1)
        )
        even = all(
            exponent % 2 == 0 or coefficient == 0
            for exponent, coefficient in enumerate(numerator)
        )
        row = {
            "N": parameter,
            "degree": len(numerator) - 1,
            "distinct_real_roots": root_count,
            "node_nonzero": node_nonzero,
            "even": even,
        }
        if (
            root_count != 0
            or not node_nonzero
            or not even
            or len(numerator) - 1 != 2 * parameter
        ):
            raise ValueError(f"cardinal obstruction failed: {row}")
        rows.append(row)

    result = {
        "schema": SCHEMA,
        "status": "VERIFIED_EXACT_CARDINAL_OBSTRUCTION",
        "max_n": maximum,
        "rows": rows,
    }
    result["proof_digest"] = canonical_digest(result)

    expected = data.get("expected_status")
    if expected and expected != result["status"]:
        raise ValueError("false expected status")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text(encoding="utf-8"))
    print(json.dumps(verify(data), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
