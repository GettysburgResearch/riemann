#!/usr/bin/env python3
"""Exact rational replay for L-20804."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_eval(p: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def encode(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def build_level(r: int) -> dict[str, object]:
    if r < 1:
        raise ValueError("r must be positive")

    numerator = [Fraction(0)] * r + [Fraction(1)]
    denominator = [Fraction(1)]
    for n in range(1, r + 1):
        denominator = poly_mul(denominator, [-Fraction(n * n), Fraction(1)])

    u = [Fraction(0)]
    for n in range(1, r + 1):
        u.append(
            Fraction(
                (-1) ** (r - n) * n ** (2 * r),
                math.factorial(r - n) * math.factorial(r + n),
            )
        )

    source = 2 * sum(u[1:], Fraction(0))
    if source != 1:
        raise AssertionError(f"source identity failed: {source}")

    probes = [
        Fraction(-2, 5),
        Fraction(1, 7),
        Fraction(3, 2),
        Fraction(17, 3),
        Fraction(101, 11),
    ]
    replay = []
    for x in probes:
        den = poly_eval(denominator, x)
        if den == 0:
            continue
        product_value = poly_eval(numerator, x) / den
        partial_value = 2 * sum(
            (u[n] * x / (x - n * n) for n in range(1, r + 1)),
            Fraction(0),
        )
        if product_value != partial_value:
            raise AssertionError(f"partial fraction failed at {x}")
        replay.append({"x": encode(x), "value": encode(product_value)})

    metric = 2 * sum((value * value for value in u[1:]), Fraction(0))
    bound_factor = Fraction(2) * sum(
        (
            Fraction(r ** (2 * r), math.factorial(2 * r))
            * math.comb(2 * r, k)
        )
        ** 2
        for k in range(0, 2 * r + 1)
    )
    if metric > bound_factor:
        raise AssertionError("finite binomial metric bound failed")

    payload = {
        "r": r,
        "source": encode(source),
        "metric": encode(metric),
        "binomial_metric_bound": encode(bound_factor),
        "u": [encode(value) for value in u],
        "probes": replay,
    }
    payload["digest"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return payload


def verify(max_r: int) -> dict[str, object]:
    return {
        "schema": "riemann.x20804.flat-endpoint-source-notch.v1",
        "classification": "EXACT_RATIONAL_FINITE_ALGEBRA",
        "levels": [build_level(r) for r in range(1, max_r + 1)],
        "verdict": "PASS_EXACT_FACTORIAL_SOURCE_NOTCH",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.max_r)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
