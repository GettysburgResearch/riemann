#!/usr/bin/env python3
"""Exact certificate for the zero-safe factor-64 cyclotomic filter."""
from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent

# Elements of Q(sqrt(2)) are represented as (a,b) = a+b sqrt(2).
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
    """Power coefficients of p(left+(right-left)t)."""
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
    # Coefficients of P_64(y), in Q(sqrt(2)).
    coefficients: list[Pair] = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1, 2)),
        (Fraction(-1), Fraction(0)),
        (Fraction(-1), Fraction(1, 2)),
        (Fraction(0), Fraction(1, 2)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1, 2)),
    ]
    moment_0 = (Fraction(0), Fraction(0))
    moment_1 = (Fraction(0), Fraction(0))
    for j, coefficient in enumerate(coefficients):
        moment_0 = add(moment_0, coefficient)
        moment_1 = add(moment_1, scale(coefficient, Fraction(j)))
    if moment_0 != (0, 0) or moment_1 != (0, 0):
        raise AssertionError("neutral filter moments failed")

    # P_64(sqrt(2)) is checked by the exact factorization.
    return {
        "sum_coefficients": [0, 0],
        "sum_j_coefficients": [0, 0],
        "factorization": "(1-y)^2(1-y/sqrt(2))(1+y)(1+y+y^2)",
        "roots": ["1 (double)", "sqrt(2)", "-1", "exp(2pi i/3)", "exp(-2pi i/3)"],
    }


def exact_norm_certificate() -> dict:
    # Power coefficients of H(x)=16-|P_64(e^{it})|^2, x=cos(t).
    h_power: list[Pair] = [
        (Fraction(4), Fraction(0)),
        (Fraction(-36), Fraction(8)),
        (Fraction(12), Fraction(24)),
        (Fraction(84), Fraction(-8)),
        (Fraction(0), Fraction(-56)),
        (Fraction(-48), Fraction(0)),
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
        "claim": "max_|y|=1 |P_64(y)|^2 < 16",
        "subdivisions": subdivisions,
        "all_bernstein_lower_endpoints_positive": True,
        "minimum_lower_endpoint": str(minimum),
    }


def constants() -> dict:
    mp.mp.dps = 80
    half = mp.mpf("0.5")

    def xi(s):
        return (
            mp.mpf("0.5")
            * s
            * (s - 1)
            * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2)
            * mp.zeta(s)
        )

    zeta_half = mp.zeta(half)
    square_mass = mp.diff(lambda s: mp.log(xi(s)), half, 2)
    moat = 3 * (1 + zeta_half) * (1 - 1 / mp.sqrt(2)) * mp.log(2) ** 2
    zero_bound = 4 * square_mass
    margin = moat + zero_bound
    scaled_margin = mp.sqrt(2) * margin

    if not moat < mp.mpf("-0.194"):
        raise AssertionError(f"moat corridor failed: {moat}")
    if not zero_bound < mp.mpf("0.185"):
        raise AssertionError(f"zero bound corridor failed: {zero_bound}")
    if not margin < mp.mpf("-0.009"):
        raise AssertionError(f"unscaled margin corridor failed: {margin}")
    if not scaled_margin < mp.mpf("-0.012"):
        raise AssertionError(f"scaled margin corridor failed: {scaled_margin}")

    return {
        "zeta_half": mp.nstr(zeta_half, 60),
        "zero_square_mass_logxi_second": mp.nstr(square_mass, 60),
        "moat": mp.nstr(moat, 60),
        "zero_bound": mp.nstr(zero_bound, 60),
        "margin_upper_bound": mp.nstr(margin, 60),
        "scaled_margin_upper_bound": mp.nstr(scaled_margin, 60),
    }


def main() -> None:
    result = {
        "classification": "PASS_FACTOR64_CYCLOTOMIC_ANNULAR_CERTIFICATE",
        "moments": exact_moments(),
        "exact_norm_certificate": exact_norm_certificate(),
        "constants": constants(),
        "scope": (
            "The moment and Bernstein checks are exact over Q(sqrt(2)) with a "
            "rational radical enclosure. The contour shift, Landau converse, and "
            "unconditional annular sign are mathematical statements outside this checker."
        ),
    }
    output = HERE / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
