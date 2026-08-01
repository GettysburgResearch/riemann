#!/usr/bin/env python3
"""Exact rational replay for L-20803.

This checker verifies the shifted-lattice numerator, its positive partial
fractions, source normalization, and the rational response identity.  It uses
only Python integers and fractions.Fraction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


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


def poly_derivative(p: list[Fraction]) -> list[Fraction]:
    return [Fraction(i) * p[i] for i in range(1, len(p))]


def encode(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def build_level(nmax: int, theta: Fraction) -> dict[str, object]:
    if nmax < 1:
        raise ValueError("nmax must be positive")
    if not (Fraction(1, 2) < theta < 1):
        raise ValueError("theta must lie strictly between 1/2 and 1")

    numerator = [Fraction(1)]
    denominator = [Fraction(1)]
    for n in range(1, nmax + 1):
        numerator = poly_mul(
            numerator,
            [-(Fraction(n) - theta) ** 2, Fraction(1)],
        )
        denominator = poly_mul(
            denominator,
            [-Fraction(n * n), Fraction(1)],
        )

    derivative = poly_derivative(denominator)
    u = [poly_eval(numerator, Fraction(0)) / poly_eval(denominator, Fraction(0))]
    residues: list[Fraction] = []
    for n in range(1, nmax + 1):
        x = Fraction(n * n)
        residue = poly_eval(numerator, x) / poly_eval(derivative, x)
        residues.append(residue)
        u.append(residue / (2 * x))

    if not all(value > 0 for value in u):
        raise AssertionError("interlacing did not produce positive coefficients")

    source = u[0] + 2 * sum(u[1:], Fraction(0))
    if source != 1:
        raise AssertionError(f"source normalization failed: {source}")

    for n, residue in enumerate(residues, start=1):
        if residue != 2 * n * n * u[n]:
            raise AssertionError("residue-to-even-coefficient identity failed")

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
        partial_value = u[0] + 2 * sum(
            (u[n] * x / (x - n * n) for n in range(1, nmax + 1)),
            Fraction(0),
        )
        if product_value != partial_value:
            raise AssertionError(f"partial-fraction replay failed at x={x}")
        replay.append({"x": encode(x), "value": encode(product_value)})

    metric = u[0] ** 2 + 2 * sum((value * value for value in u[1:]), Fraction(0))
    payload = {
        "N": nmax,
        "theta": encode(theta),
        "source": encode(source),
        "metric": encode(metric),
        "u": [encode(value) for value in u],
        "probes": replay,
    }
    payload["digest"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return payload


def verify_range(levels: Iterable[int], theta: Fraction) -> dict[str, object]:
    records = [build_level(level, theta) for level in levels]
    return {
        "schema": "riemann.x20803.shifted-lattice-source-notch.v1",
        "classification": "EXACT_RATIONAL_FINITE_ALGEBRA",
        "theta": encode(theta),
        "levels": records,
        "verdict": "PASS_EXACT_SHIFTED_LATTICE_SOURCE_NOTCH",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=8)
    parser.add_argument("--theta-num", type=int, default=3)
    parser.add_argument("--theta-den", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    theta = Fraction(args.theta_num, args.theta_den)
    result = verify_range(range(1, args.max_n + 1), theta)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
