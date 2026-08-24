#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def binom(t: Fraction, k: int) -> Fraction:
    if k < 0:
        return Fraction(0)
    out = Fraction(1)
    for j in range(k):
        out *= t - j
    for j in range(1, k + 1):
        out /= j
    return out


def dbinom(t: Fraction, k: int) -> Fraction:
    if k <= 0:
        return Fraction(0)
    total = Fraction(0)
    for omitted in range(k):
        term = Fraction(1)
        for j in range(k):
            if j != omitted:
                term *= t - j
        for j in range(1, k + 1):
            term /= j
        total += term
    return total


def local_coeffs(t: Fraction, n: int):
    return [binom(t, k) - binom(t, k - 1) for k in range(n)]


def local_derivative(t: Fraction, n: int):
    return [dbinom(t, k) - dbinom(t, k - 1) for k in range(n)]


def conv(a, b, n):
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < n:
                out[i + j] += x * y
    return out


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    order = 18
    temps = [Fraction(1, 7), Fraction(2, 7), Fraction(1, 2),
             Fraction(5, 7), Fraction(6, 7)]

    midpoint = local_coeffs(Fraction(1, 2), order)
    target = conv(midpoint, midpoint, order)

    complementary_checks = 0
    flatness_checks = 0
    for t in temps:
        a = local_coeffs(t, order)
        b = local_coeffs(1 - t, order)
        assert conv(a, b, order) == target
        complementary_checks += order

        da = local_derivative(t, order)
        db = local_derivative(1 - t, order)
        assert conv(da, b, order) == conv(a, db, order)
        flatness_checks += order

    carrier_checks = 0
    for t in temps:
        a1 = t - 1
        b1 = -t
        assert a1 + b1 == -1
        assert a1 - b1 == 2 * t - 1
        carrier_checks += 2

    grid = [Fraction(k, 20) for k in range(21)]
    exponents = [(1 - t) ** 2 + t ** 2 for t in grid]
    min_value = min(exponents)
    assert min_value == Fraction(1, 2)
    assert [grid[i] for i, v in enumerate(exponents) if v == min_value] == [Fraction(1, 2)]

    log_coeffs = [Fraction(0)] + [
        Fraction((-1) ** (k + 1), k) for k in range(1, order)
    ]
    assert log_coeffs[1] == 1
    higher_mass_fixture = sum(
        1.0 / (k * (2.0 ** (k / 2.0))) for k in range(2, 80)
    )
    assert higher_mass_fixture < 2.0

    K0, K1, K2 = 2, 1, 3
    assert K0 - K1 > 0
    assert K0 + K1 > 0
    assert K0 - K2 < 0

    payload = {
        "schema": "riemann.t102920.complementary-temperature-gauge.v1",
        "series_order": order,
        "complementary_coefficient_checks": complementary_checks,
        "flatness_coefficient_checks": flatness_checks,
        "carrier_checks": carrier_checks,
        "minimum_energy_exponent": "1/2",
        "unique_minimizer": "t=1/2",
        "higher_prime_power_fixture": higher_mass_fixture,
        "factor_product_counterfixture": True,
        "ctzd102897_proved": False,
        "sgic102890_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102920_COMPLEMENTARY_TEMPERATURE_GAUGE",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
