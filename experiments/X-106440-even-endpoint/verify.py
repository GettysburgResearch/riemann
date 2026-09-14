#!/usr/bin/env python3
"""Exact finite replay for L/T-106440--106443.

The replay checks endpoint Gaussian algebra, the even-power exterior-square
factorization, rational source inequalities and the fourth-derivative constant
ledger.  It does not evaluate Xi, companion zeros or EVENST106440.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

Gaussian = tuple[Fraction, Fraction]


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] + b[0], a[1] + b[1])


def gsub(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] - b[0], a[1] - b[1])


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def endpoint_difference(f0: Fraction, f1: Fraction, fk: Fraction,
                        fk1: Fraction, lam: Fraction) -> Gaussian:
    n = gmul((f0, -lam * f1), (fk, lam * fk1))
    d = gmul((f0, lam * f1), (fk, -lam * fk1))
    return gsub(n, d)


def source_checks() -> int:
    checks = 0
    c = Fraction(1, 200)
    lam = c  # normalize L=1
    for k in (2, 4, 6, 8):
        for ui in range(21):
            for vi in range(21):
                u = Fraction(ui, 20)
                v = Fraction(vi, 20)
                same_a = (
                    (1 - lam * u) * (1 + lam * v) * v**k
                    + (1 - lam * v) * (1 + lam * u) * u**k
                ) / 2
                same_r = lam * abs(u - v) * abs(u**k - v**k)
                assert same_a >= 0
                assert same_r * (1 - c) <= 2 * c * same_a

                cross_a = (
                    (1 - lam * u) * (1 - lam * v) * v**k
                    + (1 + lam * u) * (1 + lam * v) * u**k
                )
                cross_r = 2 * lam * (u + v) * abs(u**k - v**k)
                assert cross_a >= 0
                assert cross_r * (1 - c) ** 2 <= 4 * c * cross_a
                checks += 2
    return checks


def main() -> dict[str, object]:
    lam = Fraction(3, 17)
    fixtures = [
        (Fraction(5), Fraction(-2), Fraction(7), Fraction(11)),
        (Fraction(-3, 5), Fraction(8, 7), Fraction(9, 4), Fraction(-6, 11)),
        (Fraction(0), Fraction(2), Fraction(-5), Fraction(3)),
    ]
    endpoint_checks = 0
    for f0, f1, fk, fk1 in fixtures:
        observed = endpoint_difference(f0, f1, fk, fk1, lam)
        expected = (Fraction(0), 2 * lam * (f0 * fk1 - f1 * fk))
        assert observed == expected
        endpoint_checks += 1

    factor_checks = 0
    for m in range(1, 7):
        for u in range(-5, 6):
            for v in range(-5, 6):
                lhs = (v - u) * (v ** (2 * m) - u ** (2 * m))
                sum_even = sum(
                    u ** (2 * j) * v ** (2 * (m - 1 - j))
                    for j in range(m)
                )
                rhs = (u + v) * (u - v) ** 2 * sum_even
                assert lhs == rhs
                assert (u - v) ** 2 * sum_even >= 0
                factor_checks += 2

    rational_grid_checks = source_checks()

    same_square = Fraction(4, 39601)
    reflected_square = Fraction(640000, 1568239201)
    four_channel = 2 * same_square + 2 * reflected_square
    assert four_channel == Fraction(1596808, 1568239201)
    assert four_channel < Fraction(1, 982)

    fourth_entry = Fraction(2487, 2500)
    ninety = Fraction(9, 10)
    safe_source = Fraction(1, 982)
    signed_allowance = fourth_entry - ninety - safe_source
    assert signed_allowance == Fraction(115117, 1227500)
    assert signed_allowance > Fraction(9, 100)

    payload: dict[str, object] = {
        "schema": "riemann.x106440.even-endpoint.v1",
        "classification": "PASS_T106440_EVEN_ENDPOINT_FRONTIER",
        "endpoint_checks": endpoint_checks,
        "exterior_square_factor_checks": factor_checks,
        "rational_source_grid_checks": rational_grid_checks,
        "same_sign_squared_constant": "4/39601",
        "reflected_squared_constant": "640000/1568239201",
        "four_channel_constant": "1596808/1568239201",
        "four_channel_below_one_over_982": True,
        "fourth_derivative_entry": "2487/2500",
        "signed_tail_allowance": "115117/1227500",
        "evenst106440_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(text, encoding="utf-8")
    print(text, end="")
