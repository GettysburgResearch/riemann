#!/usr/bin/env python3
"""Exact/directed regression for the corrected L-91030 threshold and L-91029.

This replay certifies the finite rational zeta lower bound used at s=2/3,
checks the three-scale storage identity, and stress-tests the unit-atom barrier.
It proves no analytic monotonicity theorem, boundary intertwiner, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

mp.mp.dps = 80


def cube_root_upper(n: int, denominator: int) -> int:
    """Least integer U with (U/denominator)^3 >= n."""
    target = n * denominator**3
    lo = 0
    hi = max(denominator, int(round(n ** (1 / 3) * denominator)) + 10)
    while hi**3 < target:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 >= target:
            hi = mid
        else:
            lo = mid
    return hi


def storage_closed(y: Fraction) -> Fraction:
    return (
        Fraction(27) * y * (14 * y * y + 163 * y + 224)
        / ((y + 1) ** 2 * (y + 4) ** 2 * (y + 16) ** 2)
    )


def storage_partial(y: Fraction) -> Fraction:
    return -1 / (y + 1) ** 2 + 17 / (y + 4) ** 2 - 16 / (y + 16) ** 2


def wavelet(t: mp.mpf) -> mp.mpf:
    return (
        -mp.mpf(1) / 4 * (1 + t) * mp.exp(-t)
        + mp.mpf(17) / 32 * (1 + 2 * t) * mp.exp(-2 * t)
        - mp.mpf(1) / 16 * (1 + 4 * t) * mp.exp(-4 * t)
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path)
    args = ap.parse_args()

    checks = 0

    # Exact rational certificate:
    # (2/3) sum_{n<=30} n^{-5/3} + 31^{-2/3} > 1.414214 > sqrt(2).
    D = 10**6
    lower = Fraction(0)
    cube_checks = 0
    for n in range(1, 31):
        U = cube_root_upper(n, D)
        assert U**3 >= n * D**3
        assert U == 0 or (U - 1) ** 3 < n * D**3
        lower += Fraction(2, 3) * Fraction(D * D, n * U * U)
        cube_checks += 2
    U31 = cube_root_upper(31, D)
    assert U31**3 >= 31 * D**3
    lower += Fraction(D * D, U31 * U31)
    sqrt2_upper = Fraction(1414214, 10**6)
    assert lower > sqrt2_upper
    assert sqrt2_upper * sqrt2_upper > 2
    checks += cube_checks + 3

    # e > 8/3, hence 3/(2e)+e^-2 < 45/64 < 1.
    factorial = 1
    e_lower = Fraction(0)
    for k in range(5):
        if k > 0:
            factorial *= k
        e_lower += Fraction(1, factorial)
    assert e_lower == Fraction(65, 24) > Fraction(8, 3)
    assert Fraction(9, 16) + Fraction(9, 64) == Fraction(45, 64) < 1
    checks += 3

    # Exact three-scale partial-fraction identity on a dense rational grid.
    partial_checks = 0
    for d in [1, 2, 3, 7, 11, 29]:
        for n in range(0, 101):
            y = Fraction(n, d)
            assert storage_closed(y) == storage_partial(y)
            partial_checks += 1
    checks += partial_checks

    # High-precision one-switch and zero-mean controls.
    root = mp.findroot(wavelet, (mp.mpf("1"), mp.mpf("1.5")))
    assert mp.mpf("1.1646") < root < mp.mpf("1.1647")
    for t in [mp.mpf("0"), mp.mpf("0.2"), mp.mpf("0.8"), root - mp.mpf("1e-8")]:
        assert wavelet(t) > 0
        checks += 1
    for t in [root + mp.mpf("1e-8"), mp.mpf("2"), mp.mpf("5"), mp.mpf("12")]:
        assert wavelet(t) < 0
        checks += 1
    half_mass = mp.quad(wavelet, [0, mp.inf])
    assert abs(half_mass) < mp.mpf("1e-70")
    checks += 2

    # Unit-barrier criterion at representative s >= 2/3.
    terminal_rows: list[dict[str, str]] = []
    min_margin = mp.inf
    for s in [mp.mpf(2) / 3, mp.mpf("0.7"), mp.mpf("1"), mp.mpf("2"), mp.mpf("5")]:
        r = 1 / (s * mp.zeta(1 + s))
        assert r < 1 / mp.sqrt(2)
        margin = 1 / r - 2 * r
        assert margin > 0
        min_margin = min(min_margin, margin)
        terminal_rows.append({
            "s": mp.nstr(s, 18),
            "r_s": mp.nstr(r, 24),
            "unit_barrier_margin": mp.nstr(margin, 24),
        })
        checks += 2

    result: dict[str, Any] = {
        "classification": "PASS_CORRECTED_GREEN_REMOVAL_THRESHOLD",
        "checks": checks,
        "exact_cube_root_checks": cube_checks,
        "exact_partial_fraction_checks": partial_checks,
        "rational_zeta_lower_bound": str(lower),
        "rational_zeta_lower_bound_decimal": float(lower),
        "sqrt2_rational_upper": str(sqrt2_upper),
        "one_switch_root": mp.nstr(root, 30),
        "half_line_wavelet_mass": mp.nstr(half_mass, 12),
        "minimum_terminal_unit_barrier_margin": mp.nstr(min_margin, 24),
        "terminal_rows": terminal_rows,
        "scope": (
            "exact finite/directed threshold certificate and algebraic regression only; "
            "no proof of the analytic derivative bound, CJHI, or RH"
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print("PASS_CORRECTED_GREEN_REMOVAL_THRESHOLD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
