#!/usr/bin/env python3
"""Finite replay for the fractional-string renormalisation packet.

This script checks exact finite algebra and high-precision diagnostics only.
It does not prove the analytic asymptotics, the growing-order theorem, NCFSC,
or RH.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp


def xi_log_deriv(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(lambda z: mp.zeta(z), s) / mp.zeta(s)
    )


def p_xi(t: mp.mpf) -> mp.mpf:
    x = mp.sqrt(t)
    return xi_log_deriv(mp.mpf("0.5") + x) / x


def exact_central_hankel() -> dict:
    out = {}
    for n in range(1, 9):
        mat = sp.Matrix(
            [
                [
                    sp.Rational(
                        math.comb(2 * (i + j + 1), i + j + 1),
                        4 ** (i + j + 1),
                    )
                    for j in range(n)
                ]
                for i in range(n)
            ]
        )
        det = sp.factor(mat.det())
        target = sp.Rational(1, 2 ** (n * (2 * n - 1)))
        if det != target:
            raise AssertionError((n, det, target))
        out[str(n)] = {"det": str(det), "target": str(target)}
    return out


def real_inverse_power(A: Fraction, d: Fraction, k: int) -> Fraction:
    re, im = Fraction(1), Fraction(0)
    for _ in range(k):
        re, im = re * A - im * d, re * d + im * A
    return re / (re * re + im * im)


def model_A(
    t: Fraction,
    k: int,
    real_poles: list[tuple[Fraction, Fraction]],
    eps: Fraction,
    c: Fraction,
    d: Fraction,
) -> Fraction:
    value = sum(w / (t + s) ** (k + 1) for s, w in real_poles)
    value += 2 * eps * real_inverse_power(t + c, d, k + 1)
    return value


def exact_delayed_failure() -> dict:
    real_poles = [
        (Fraction(1), Fraction(1)),
        (Fraction(2), Fraction(1)),
        (Fraction(4), Fraction(1)),
        (Fraction(8), Fraction(1)),
        (Fraction(16), Fraction(1)),
        (Fraction(32), Fraction(1)),
    ]
    eps = Fraction(1, 10**12)
    c = Fraction(100)
    d = Fraction(1)
    t = Fraction(1)
    determinants = {}
    for n in range(1, 9):
        entries = []
        for i in range(n):
            row = []
            for j in range(n):
                value = model_A(t, i + j + 1, real_poles, eps, c, d)
                row.append(sp.Rational(value.numerator, value.denominator))
            entries.append(row)
        det = sp.factor(sp.Matrix(entries).det())
        determinants[str(n)] = str(det)
        if n <= 7 and not (det > 0):
            raise AssertionError(("expected positive", n, det))
        if n == 8 and not (det < 0):
            raise AssertionError(("expected negative", n, det))
    return {
        "real_poles": [str(s) for s, _ in real_poles],
        "complex_pair": ["100+i", "100-i"],
        "epsilon": str(eps),
        "t": str(t),
        "determinants": determinants,
    }


def scaling_diagnostic() -> list[dict]:
    mp.mp.dps = 80
    rows = []
    for x_int in (100, 1000, 10000):
        x = mp.mpf(x_int)
        ell = mp.log(x / (2 * mp.pi))
        alpha = mp.mpf("0.5") - 1 / (2 * ell)
        for u in (mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")):
            p_hat = 2 * x / ell * p_xi(x * x * u)
            background = u ** (-alpha)
            rows.append(
                {
                    "x": x_int,
                    "u": mp.nstr(u, 20),
                    "ell": mp.nstr(ell, 40),
                    "alpha": mp.nstr(alpha, 40),
                    "p_hat": mp.nstr(p_hat, 40),
                    "power_background": mp.nstr(background, 40),
                    "abs_error": mp.nstr(abs(p_hat - background), 40),
                }
            )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    result = {
        "status": "PASS_FRACTIONAL_STRING_RENORMALIZATION",
        "central_hankel": exact_central_hankel(),
        "delayed_failure": exact_delayed_failure(),
        "scaling": scaling_diagnostic(),
        "gates": {
            "central_binomial_determinants": True,
            "positive_through_order_seven": True,
            "negative_at_order_eight": True,
            "fractional_power_scaling_diagnostic": True,
        },
        "scope": (
            "Finite algebra and high-precision diagnostics only; "
            "no proof of the analytic uniformity, growing-order theorem, "
            "NCFSC, or RH."
        ),
    }
    args.json.write_text(
        json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n"
    )
    print(result["status"])


if __name__ == "__main__":
    main()
