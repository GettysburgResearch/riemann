#!/usr/bin/env python3
"""Exact finite-source regression for the Fisher-feature renormalization.

A three-point exponential tilt is chosen so that all probabilities and all
quarter-turn characters are Gaussian rationals. The script checks the
algebraic identities behind L-91325 without floating point.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Tuple

G = Tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))


def add(a: G, b: G) -> G:
    return (a[0] + b[0], a[1] + b[1])


def neg(a: G) -> G:
    return (-a[0], -a[1])


def sub(a: G, b: G) -> G:
    return add(a, neg(b))


def mul(a: G, b: G) -> G:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conj(a: G) -> G:
    return (a[0], -a[1])


def scale(q: Fraction, a: G) -> G:
    return (q * a[0], q * a[1])


def norm2(a: G) -> Fraction:
    return a[0] * a[0] + a[1] * a[1]


def div(a: G, b: G) -> G:
    d = norm2(b)
    if d == 0:
        raise ZeroDivisionError
    return scale(Fraction(1, 1) / d, mul(a, conj(b)))


def expect(probabilities: Iterable[Fraction], values: Iterable[G]) -> G:
    out = ZERO
    for p, v in zip(probabilities, values, strict=True):
        out = add(out, scale(p, v))
    return out


def i_power(n: int) -> G:
    return (ONE, (Fraction(0), Fraction(1)), neg(ONE), (Fraction(0), Fraction(-1)))[n % 4]


def phase(frequency_quarters: int, y: int) -> G:
    return i_power(frequency_quarters * y)


def frac_text(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def g_text(z: G) -> str:
    return f"({frac_text(z[0])},{frac_text(z[1])})"


def run() -> dict:
    # Base masses (1,2,3), tilt exp(-a)=1/2, support (-1,0,2).
    # Normalized tilted probabilities are exactly (8,8,3)/19.
    ys = [-1, 0, 2]
    ps = [Fraction(8, 19), Fraction(8, 19), Fraction(3, 19)]
    mean = sum((p * y for p, y in zip(ps, ys, strict=True)), Fraction(0))
    sigmas = [Fraction(y) - mean for y in ys]

    checks = []
    for n in (1, 2, 3):
        forward = [phase(n, y) for y in ys]
        backward = [phase(-n, y) for y in ys]
        phi = expect(ps, forward)
        phi_minus = expect(ps, backward)
        if phi_minus != conj(phi) or norm2(phi) == 0:
            raise AssertionError("characteristic symmetry/nonvanishing failed")

        theta = div(phi_minus, phi)
        theta_inv = div(ONE, theta)

        hs = [
            sub(div(em, phi_minus), div(ep, phi))
            for em, ep in zip(backward, forward, strict=True)
        ]
        ks = [mul(phi, h) for h in hs]
        ks_direct = [
            sub(mul(theta_inv, em), ep)
            for em, ep in zip(backward, forward, strict=True)
        ]
        if ks != ks_direct:
            raise AssertionError("k=phi h identity failed")

        if expect(ps, hs) != ZERO or expect(ps, ks) != ZERO:
            raise AssertionError("centering failed")

        sigma_h = expect(ps, [scale(s, h) for s, h in zip(sigmas, hs, strict=True)])
        sigma_k = expect(ps, [scale(s, k) for s, k in zip(sigmas, ks, strict=True)])
        dlogtheta = neg(sigma_h)
        renormalized = neg(div(sigma_k, phi))
        if dlogtheta != renormalized:
            raise AssertionError("score covariance renormalization failed")

        h_diag = sum((p * norm2(h) for p, h in zip(ps, hs, strict=True)), Fraction(0))
        k_diag = sum((p * norm2(k) for p, k in zip(ps, ks, strict=True)), Fraction(0))
        if k_diag != norm2(phi) * h_diag:
            raise AssertionError("renormalized diagonal covariance failed")
        if k_diag > 4 or any(norm2(k) > 4 for k in ks):
            raise AssertionError("uniform bound failed")

        checks.append(
            {
                "frequency_quarters": n,
                "phi": g_text(phi),
                "theta": g_text(theta),
                "d_log_theta_da": g_text(dlogtheta),
                "normalized_diagonal_H": frac_text(h_diag),
                "renormalized_diagonal_K": frac_text(k_diag),
                "K_equals_abs_phi_sq_H": True,
                "pointwise_abs_k_sq_le_4": True,
            }
        )

    return {
        "verdict": "PASS_RENORMALIZED_FISHER_FEATURE",
        "arithmetic": "exact Gaussian rationals; no floating point",
        "support": ys,
        "tilted_probabilities": [frac_text(p) for p in ps],
        "mean": frac_text(mean),
        "frequencies_checked": len(checks),
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.json is None:
        print(text, end="")
    else:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
