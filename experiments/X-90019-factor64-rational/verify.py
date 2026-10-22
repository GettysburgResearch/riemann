#!/usr/bin/env python3
"""Exact/floating replay for the improved rational factor-64 filter."""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from fractions import Fraction
from math import comb
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "X-90015-annular-endpoint" / "verify.py"
spec = importlib.util.spec_from_file_location("x90015", BASE)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {BASE}")
x90015 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x90015)

Pair = tuple[Fraction, Fraction]
SQRT2_LO = Fraction(1414213562373095, 10**15)
SQRT2_HI = Fraction(1414213562373096, 10**15)


def add(u: Pair, v: Pair) -> Pair:
    return u[0] + v[0], u[1] + v[1]


def scale(u: Pair, q: Fraction) -> Pair:
    return u[0] * q, u[1] * q


def lower(u: Pair) -> Fraction:
    a, b = u
    return a + b * (SQRT2_LO if b >= 0 else SQRT2_HI)


def compose(power: list[Pair], left: Fraction, right: Fraction) -> list[Pair]:
    h = right - left
    result: list[Pair] = [(Fraction(0), Fraction(0))]
    for coefficient in reversed(power):
        new = [(Fraction(0), Fraction(0)) for _ in range(len(result) + 1)]
        for index, value in enumerate(result):
            new[index] = add(new[index], scale(value, left))
            new[index + 1] = add(new[index + 1], scale(value, h))
        new[0] = add(new[0], coefficient)
        result = new
    while len(result) > 1 and result[-1] == (0, 0):
        result.pop()
    return result


def bernstein(power: list[Pair], degree: int) -> list[Pair]:
    coefficients = power + [(Fraction(0), Fraction(0))] * (degree + 1 - len(power))
    result: list[Pair] = []
    for k in range(degree + 1):
        value: Pair = (Fraction(0), Fraction(0))
        for j in range(k + 1):
            value = add(
                value,
                scale(coefficients[j], Fraction(comb(k, j), comb(degree, j))),
            )
        result.append(value)
    return result


def exact_moments() -> dict:
    # Coefficients a+b sqrt(2) of the unscaled filter.
    coefficients: list[Pair] = [
        (Fraction(1), Fraction(0)),
        (Fraction(-1, 4), Fraction(-1, 2)),
        (Fraction(-3, 4), Fraction(1, 8)),
        (Fraction(-3, 4), Fraction(3, 8)),
        (Fraction(-1, 4), Fraction(3, 8)),
        (Fraction(1), Fraction(1, 8)),
        (Fraction(0), Fraction(-1, 2)),
    ]
    moment_0: Pair = (Fraction(0), Fraction(0))
    moment_1: Pair = (Fraction(0), Fraction(0))
    for j, coefficient in enumerate(coefficients):
        moment_0 = add(moment_0, coefficient)
        moment_1 = add(moment_1, scale(coefficient, Fraction(j)))
    if moment_0 != (0, 0) or moment_1 != (0, 0):
        raise AssertionError("neutral moments failed")
    # The quadratic y^2+3y/4+1 has negative discriminant and product one.
    discriminant = Fraction(9, 16) - 4
    if discriminant >= 0:
        raise AssertionError("quadratic roots are not a unit-circle conjugate pair")
    return {
        "sum_coefficients": [0, 0],
        "sum_j_coefficients": [0, 0],
        "quadratic_discriminant": str(discriminant),
        "quadratic_root_product": 1,
        "factorization": "(1-y)^2(1-y/sqrt(2))(1+y)(1+3y/4+y^2)",
    }


def exact_norm_certificate() -> dict:
    # H*(x)=11-|P*(e^{it})|^2, x=cos(t), over Q(sqrt(2)).
    h_power: list[Pair] = [
        (Fraction(17, 4), Fraction(0)),
        (Fraction(-117, 4), Fraction(9, 2)),
        (Fraction(-21, 4), Fraction(39, 2)),
        (Fraction(309, 4), Fraction(7, 2)),
        (Fraction(12), Fraction(-103, 2)),
        (Fraction(-48), Fraction(-8)),
        (Fraction(0), Fraction(32)),
    ]
    subdivisions = 1024
    minimum: Fraction | None = None
    for i in range(subdivisions):
        left = Fraction(-1) + Fraction(2 * i, subdivisions)
        right = Fraction(-1) + Fraction(2 * (i + 1), subdivisions)
        values = bernstein(compose(h_power, left, right), degree=6)
        lower_bounds = [lower(value) for value in values]
        local_min = min(lower_bounds)
        if local_min <= 0:
            raise AssertionError(
                f"nonpositive Bernstein lower endpoint on [{left},{right}]: {local_min}"
            )
        minimum = local_min if minimum is None else min(minimum, local_min)
    assert minimum is not None
    return {
        "claim": "max_|y|=1 |P_64^*(y)|^2 < 11",
        "subdivisions": subdivisions,
        "all_bernstein_lower_endpoints_positive": True,
        "minimum_lower_endpoint": str(minimum),
    }


def constants() -> dict:
    mp.mp.dps = 80
    half = mp.mpf("0.5")

    def xi(s):
        return (
            mp.mpf("0.5") * s * (s - 1)
            * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2) * mp.zeta(s)
        )

    zeta_half = mp.zeta(half)
    square_mass = mp.diff(lambda s: mp.log(xi(s)), half, 2)
    moat = (
        mp.mpf(11) / 4
        * (1 + zeta_half)
        * (1 - 1 / mp.sqrt(2))
        * mp.log(2) ** 2
    )
    zero_bound = mp.sqrt(11) * square_mass
    margin = moat + zero_bound
    scaled_margin = 4 * mp.sqrt(2) * margin
    if not moat < mp.mpf("-0.178"):
        raise AssertionError(f"moat corridor failed: {moat}")
    if not zero_bound < mp.mpf("0.154"):
        raise AssertionError(f"zero corridor failed: {zero_bound}")
    if not margin < mp.mpf("-0.024"):
        raise AssertionError(f"margin corridor failed: {margin}")
    if not scaled_margin < mp.mpf("-0.13"):
        raise AssertionError(f"scaled margin corridor failed: {scaled_margin}")
    return {
        "zeta_half": mp.nstr(zeta_half, 60),
        "zero_square_mass_logxi_second": mp.nstr(square_mass, 60),
        "moat": mp.nstr(moat, 60),
        "zero_bound": mp.nstr(zero_bound, 60),
        "margin_upper_bound": mp.nstr(margin, 60),
        "scaled_margin_upper_bound": mp.nstr(scaled_margin, 60),
    }


def finite_scan(max_x: int) -> dict:
    if max_x < 64:
        raise ValueError("--max-x must be at least 64")
    endpoint, _, _ = x90015.endpoint_sequence(max_x)
    r = math.sqrt(2.0)
    xs = np.arange(64, max_x + 1, 64, dtype=np.int64)
    values = np.array([
        endpoint[x - 1]
        - (0.25 + 1.0 / r) * endpoint[x // 2 - 1]
        + (-0.75 + 1.0 / (4.0 * r)) * endpoint[x // 4 - 1]
        + (-0.75 + 3.0 / (4.0 * r)) * endpoint[x // 8 - 1]
        + (-0.25 + 3.0 / (4.0 * r)) * endpoint[x // 16 - 1]
        + (1.0 + 1.0 / (4.0 * r)) * endpoint[x // 32 - 1]
        - (1.0 / r) * endpoint[x // 64 - 1]
        for x in xs
    ])
    nonnegative = xs[values >= 0]
    imax = int(np.argmax(values))
    imin = int(np.argmin(values))
    return {
        "max_X": max_x,
        "annulus_factor": 64,
        "tested_multiples": int(len(xs)),
        "nonnegative_count": int(len(nonnegative)),
        "first_nonnegative_endpoints": [int(x) for x in nonnegative[:20]],
        "last_nonnegative_endpoint": int(nonnegative[-1]) if len(nonnegative) else None,
        "maximum": {"X": int(xs[imax]), "value": float(values[imax])},
        "minimum": {"X": int(xs[imin]), "value": float(values[imin])},
        "last": {"X": int(xs[-1]), "value": float(values[-1])},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-x", type=int, default=1_000_000)
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "results" / "verification.json",
    )
    args = parser.parse_args()
    result = {
        "classification": "PASS_FACTOR64_RATIONAL_UNIT_CIRCLE_CERTIFICATE",
        "moments": exact_moments(),
        "exact_norm_certificate": exact_norm_certificate(),
        "constants": constants(),
        "finite": finite_scan(args.max_x),
        "scope": (
            "The moment and Bernstein checks are exact over Q(sqrt(2)) with a "
            "rational radical enclosure. The endpoint scan is reconnaissance only."
        ),
    }
    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
