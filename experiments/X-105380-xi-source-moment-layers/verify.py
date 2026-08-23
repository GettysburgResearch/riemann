#!/usr/bin/env python3
"""Exact rational replay for L-105380--L-105383.

This checker authenticates formal quotient-series identities, low-order
determinants, concentration implications on rational fixtures, and exact
trigonometric moment coefficients. It does not evaluate Xi, prove the needed
concentration/capacity gates, or establish RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

Q = Fraction


def series_divide(num: list[Q], den: list[Q], count: int) -> list[Q]:
    assert den and den[0] != 0
    out: list[Q] = []
    for n in range(count):
        rhs = num[n] if n < len(num) else Q(0)
        rhs -= sum(
            (den[j] * out[n - j] for j in range(1, min(n, len(den) - 1) + 1)),
            Q(0),
        )
        out.append(rhs / den[0])
    return out


def determinant_2(a: Q, b: Q, c: Q) -> Q:
    return a * c - b * b


def odd_coefficients(x: Q, y: Q, z3: Q, z4: Q, count: int = 5) -> list[Q]:
    num = [
        Q(1),
        -x / Q(factorial(3)),
        y / Q(factorial(5)),
        -z3 / Q(factorial(7)),
        z4 / Q(factorial(9)),
    ]
    den = [
        Q(1),
        -x / Q(factorial(2)),
        y / Q(factorial(4)),
        -z3 / Q(factorial(6)),
        z4 / Q(factorial(8)),
    ]
    return series_divide(num, den, count)


def check_odd_formulas() -> int:
    fixtures = [
        (Q(1), Q(1), Q(1), Q(1)),
        (Q(2), Q(5), Q(14), Q(42)),
        (Q(3, 2), Q(7, 2), Q(19, 2), Q(61, 2)),
        (Q(5, 3), Q(31, 9), Q(215, 27), Q(1651, 81)),
        (Q(7, 4), Q(53, 16), Q(451, 64), Q(4103, 256)),
    ]
    checks = 0
    for x, y, z3, z4 in fixtures:
        a = odd_coefficients(x, y, z3, z4)
        assert a[0] == 1
        checks += 1
        assert a[1] == x / 3
        checks += 1
        assert a[2] == x * x / 6 - y / 30
        checks += 1
        assert a[3] == x**3 / 12 - Q(11) * x * y / 360 + z3 / 840
        checks += 1

        det0 = determinant_2(a[0], a[1], a[2])
        assert det0 == (5 * x * x - 3 * y) / 90
        checks += 1
        det1 = determinant_2(a[1], a[2], a[3])
        assert det1 == (35 * x * x * y + 15 * x * z3 - 42 * y * y) / 37800
        checks += 1
    return checks


def even_coefficients(h: Q, x: Q, y: Q, z3: Q, count: int = 4) -> list[Q]:
    # R(t) = -N(t)/D(t), and the regularized a_n is coeff t^(n+1).
    num = [
        -h,
        Q(1, 2),
        -x / 24,
        y / 720,
        -z3 / 40320,
    ]
    den = [
        Q(1),
        -x / 6,
        y / 120,
        -z3 / 5040,
    ]
    ratio = series_divide(num, den, count + 1)
    assert ratio[0] == -h
    return ratio[1 : count + 1]


def check_even_formulas() -> int:
    fixtures = [
        (Q(1), Q(1), Q(1), Q(1)),
        (Q(2, 3), Q(2), Q(5), Q(14)),
        (Q(3, 4), Q(3, 2), Q(7, 2), Q(19, 2)),
        (Q(4, 5), Q(5, 4), Q(29, 16), Q(185, 64)),
        (Q(7, 9), Q(9, 7), Q(95, 49), Q(1125, 343)),
    ]
    checks = 0
    for h, x, y, z3 in fixtures:
        a = even_coefficients(h, x, y, z3)
        assert a[0] == (3 - h * x) / 6
        checks += 1
        assert a[1] == (15 * x - 10 * h * x * x + 3 * h * y) / 360
        checks += 1
        assert a[2] == (
            105 * x * x
            - 42 * y
            - 70 * h * x**3
            + 42 * h * x * y
            - 3 * h * z3
        ) / 15120
        checks += 1

    # Point-mass/cotangent calibration for five rational x.
    for x in (Q(1), Q(2), Q(3, 2), Q(5, 3), Q(7, 4)):
        a = even_coefficients(Q(1) / x, x, x * x, x**3)
        assert a[0] == Q(1, 3)
        checks += 1
        assert a[1] == x / 45
        checks += 1
        assert a[2] == 2 * x * x / 945
        checks += 1
    return checks


def check_concentration_implications() -> int:
    checks = 0

    # Odd valid moment fixtures, represented by q=y/x^2 and r3=z3/x^3.
    odd = [
        (Q(1), Q(1)),
        (Q(10, 9), Q(4, 3)),
        (Q(6, 5), Q(3, 2)),
        (Q(35, 27), Q(1225, 729)),
    ]
    for q, r3 in odd:
        assert q <= Q(35, 27)
        checks += 1
        assert r3 >= q * q
        checks += 1
        assert 5 - 3 * q >= 0
        checks += 1
        assert 35 * q + 15 * r3 - 42 * q * q >= 0
        checks += 1

    # Even fixtures: alpha=E[X]E[1/X], q=E[X^2]/E[X]^2.
    even = [
        (Q(1), Q(1)),
        (Q(4, 3), Q(6, 5)),
        (Q(3, 2), Q(5, 4)),
        (Q(15, 7), Q(1)),
    ]
    for alpha, q in even:
        assert alpha <= Q(15, 7)
        checks += 1
        assert q >= 1
        checks += 1
        assert 3 - alpha >= 0
        checks += 1
        assert 15 - 10 * alpha + 3 * alpha * q >= 0
        checks += 1

    return checks


def check_trigonometric_moments() -> int:
    # Exact rational values zeta(2m)/pi^(2m).
    zeta_over_pi = {
        2: Q(1, 6),
        4: Q(1, 90),
        6: Q(1, 945),
        8: Q(1, 9450),
        10: Q(1, 93555),
    }
    odd_expected = [Q(1), Q(1, 3), Q(2, 15), Q(17, 315), Q(62, 2835)]
    even_expected = [Q(1, 3), Q(1, 45), Q(2, 945), Q(1, 4725), Q(2, 93555)]
    checks = 0

    for n in range(5):
        power = 2 * n + 2
        odd_moment = (
            Q(8)
            * Q(4) ** n
            * (Q(1) - Q(1, 2**power))
            * zeta_over_pi[power]
        )
        assert odd_moment == odd_expected[n]
        checks += 1

        even_moment = Q(2) * zeta_over_pi[power]
        assert even_moment == even_expected[n]
        checks += 1

    # Point-mass odd source coefficients agree with tangent moments.
    for x in (Q(1), Q(2), Q(3, 2), Q(5, 3), Q(7, 4)):
        a = odd_coefficients(x, x * x, x**3, x**4)
        for n in range(4):
            assert a[n] == odd_expected[n] * x**n
            checks += 1

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "odd_formula_checks": check_odd_formulas(),
        "even_formula_checks": check_even_formulas(),
        "concentration_implication_checks": check_concentration_implications(),
        "trigonometric_moment_checks": check_trigonometric_moments(),
    }
    total = sum(counts.values())
    assert total == 122

    result = {
        "verdict": "PASS_X_105380_XI_SOURCE_MOMENT_LAYERS",
        "arithmetic_class": "EXACT_RATIONAL_SERIES_MOMENTS",
        "checks": total,
        "counts": counts,
        "odd_concentration_proved_for_xi": False,
        "even_concentration_proved_for_xi": False,
        "critical_capacity_proved_for_xi": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print("PASS_X_105380_XI_SOURCE_MOMENT_LAYERS")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
