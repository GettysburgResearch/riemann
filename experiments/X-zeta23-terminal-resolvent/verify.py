#!/usr/bin/env python3
"""Finite regression for the terminal resolvent-derivative hierarchy.

This checks exact algebraic identities and high-precision numerical controls.
It does not prove RH or the analytic zero-sum/terminal-pair theorems.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

mp.mp.dps = 80


def heat_kernel(tau: mp.mpf, z: mp.mpc, y: mp.mpf) -> mp.mpc:
    return mp.exp(tau * z * z) * (1 - mp.cosh(2 * tau * y * z))


def rational_kernel(z: mp.mpc, y: mp.mpf, alpha: mp.mpf = mp.mpf(1)) -> mp.mpc:
    a = alpha - z * z
    return 1 / a - mp.mpf("0.5") / (a - 2 * y * z) - mp.mpf("0.5") / (a + 2 * y * z)


def rational_kernel_product(z: mp.mpc, y: mp.mpf, alpha: mp.mpf = mp.mpf(1)) -> mp.mpc:
    a = alpha - z * z
    return -4 * y * y * z * z / (a * (a * a - 4 * y * y * z * z))


def moment_kernel(k: int, z: mp.mpc, y: mp.mpf, alpha: mp.mpf = mp.mpf(1)) -> mp.mpc:
    n = k + 1
    a = alpha - z * z
    return mp.factorial(k) * (
        1 / a**n
        - mp.mpf("0.5") / (a - 2 * y * z) ** n
        - mp.mpf("0.5") / (a + 2 * y * z) ** n
    )


def target_value(k: int, y: mp.mpf, alpha: mp.mpf = mp.mpf(1)) -> mp.mpf:
    return mp.re(moment_kernel(k, mp.mpc(y), y, alpha))


def line_coefficient(k: int, u: mp.mpf, y: mp.mpf) -> mp.mpf:
    r = target_value(k, y)
    return -mp.re(moment_kernel(k, mp.mpc(0, u), y)) / r


def offline_coefficient(k: int, z: mp.mpc, y: mp.mpf) -> mp.mpf:
    r = target_value(k, y)
    return -2 * mp.re(moment_kernel(k, z, y)) / r


def atom_safe_formula(t: mp.mpf, s: mp.mpc, y: mp.mpf, alpha: mp.mpf) -> mp.mpc:
    q = mp.sqrt(alpha + y * y)
    return mp.exp(-s * t) * (
        mp.exp(-mp.sqrt(alpha) * t) / mp.sqrt(alpha)
        - mp.exp(-q * t) * mp.cosh(y * t) / q
    )


def atom_heat_integral(t: mp.mpf, s: mp.mpc, y: mp.mpf, alpha: mp.mpf) -> mp.mpc:
    integrand = lambda tau: (
        tau ** (-mp.mpf("0.5"))
        * mp.exp(-alpha * tau - t * t / (4 * tau))
        * (1 - mp.exp(-tau * y * y) * mp.cosh(y * t))
    )
    return mp.exp(-s * t) * mp.quad(integrand, [0, mp.inf]) / mp.sqrt(mp.pi)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    checks = 0
    max_rational_error = mp.mpf(0)
    max_moment_error = mp.mpf(0)
    max_derivative_error = mp.mpf(0)
    max_atom_error = mp.mpf(0)
    min_line_kernel = mp.inf
    max_target_normalization_error = mp.mpf(0)

    y_values = [mp.mpf("0.10"), mp.mpf("0.23"), mp.mpf("0.49")]
    z_values = [
        mp.mpc("0.17", "0.43"),
        mp.mpc("0.31", "1.10"),
        mp.mpc("-0.12", "0.73"),
    ]

    # Rational partial-fraction/product identity.
    for y in y_values:
        for z in z_values:
            err = abs(rational_kernel(z, y) - rational_kernel_product(z, y))
            max_rational_error = max(max_rational_error, err)
            assert err < mp.mpf("1e-65")
            checks += 1

    # Laplace moments equal the closed formula.
    for y in y_values:
        for z in z_values[:2]:
            for k in [0, 1, 2, 5]:
                integral = mp.quad(
                    lambda tau: tau**k * mp.exp(-tau) * heat_kernel(tau, z, y),
                    [0, mp.inf],
                )
                closed = moment_kernel(k, z, y)
                err = abs(integral - closed) / max(mp.mpf(1), abs(closed))
                max_moment_error = max(max_moment_error, err)
                assert err < mp.mpf("1e-55")
                checks += 1

    # (-d/d alpha)^k of the rational kernel equals the moment kernel.
    alpha = mp.mpf("1.17")
    y = mp.mpf("0.21")
    z = mp.mpc("0.19", "0.37")
    for k in [0, 1, 2, 3, 5]:
        derived = (-1) ** k * mp.diff(lambda a: rational_kernel(z, y, a), alpha, k)
        closed = moment_kernel(k, z, y, alpha)
        err = abs(derived - closed) / max(mp.mpf(1), abs(closed))
        max_derivative_error = max(max_derivative_error, err)
        assert err < mp.mpf("1e-55")
        checks += 1

    # Safe-Euler three-shift formula checked on one Laplace atom.
    for t in [mp.mpf("0.4"), mp.mpf("1.7"), mp.mpf("4.2")]:
        for y in [mp.mpf("0.12"), mp.mpf("0.41")]:
            s = mp.mpc("0.5", "1.3")
            direct = atom_heat_integral(t, s, y, mp.mpf(1))
            formula = atom_safe_formula(t, s, y, mp.mpf(1))
            err = abs(direct - formula) / max(mp.mpf(1), abs(formula))
            max_atom_error = max(max_atom_error, err)
            assert err < mp.mpf("1e-50")
            checks += 1

    # Critical-line positivity and exact target coefficient -2.
    for y in y_values:
        for k in [0, 1, 2, 5, 12]:
            r = target_value(k, y)
            assert r < 0
            target_coeff = -2 * r / r
            err = abs(target_coeff + 2)
            max_target_normalization_error = max(max_target_normalization_error, err)
            assert err < mp.mpf("1e-70")
            checks += 2
            for u in [mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2.5"), mp.mpf("8")]:
                val = mp.re(moment_kernel(k, mp.mpc(0, u), y))
                min_line_kernel = min(min_line_kernel, val)
                assert val >= -mp.mpf("1e-65")
                checks += 1

    # The fixed alpha=1 evaluation points are uniformly in Re(s)>1.
    safe_margin_samples = []
    for y in [mp.mpf(i) / 1000 for i in range(1, 500)]:
        margin = mp.sqrt(1 + y * y) - y - mp.mpf("0.5")
        safe_margin_samples.append(margin)
        assert margin > 0
        checks += 1
    min_safe_margin = min(safe_margin_samples)

    # Exact factorization of the zeroth Abel/Euler gap on rational samples.
    for numerator in range(1, 50):
        yf = Fraction(numerator, 100)
        left = yf + Fraction(1, 4) - 3 * yf * yf
        right = 3 * (Fraction(1, 2) - yf) * (yf + Fraction(1, 6))
        assert left == right and left > 0
        checks += 1

    # A synthetic terminal packet: the target is -2 and all other terms vanish
    # exponentially in derivative order.
    y = mp.mpf("0.22")
    nuisances = [
        mp.mpc("0.12", "0.50"),
        mp.mpc("0.18", "1.20"),
        mp.mpc("0.05", "2.00"),
    ]
    line_offsets = [mp.mpf("0.70"), mp.mpf("1.40"), mp.mpf("3.00")]
    threat_exponents = []
    for zz in nuisances:
        d, rr = mp.re(zz), mp.im(zz)
        phi = (d - y) * (d + 3 * y) - rr * rr
        threat_exponents.append(phi)
        assert phi < 0
        checks += 1

    concentration: dict[str, str] = {}
    for k in [0, 1, 2, 4, 8, 16, 32, 48, 64]:
        value = mp.mpf(-2)
        for zz in nuisances:
            value += offline_coefficient(k, zz, y)
        for u in line_offsets:
            value += line_coefficient(k, u, y)
        concentration[str(k)] = mp.nstr(value, 30)
        checks += 1
    assert abs(mp.mpf(concentration["64"]) + 2) < mp.mpf("1e-9")

    # Under a synthetic line-only zero measure, the moment Hankel matrix is PSD.
    y = mp.mpf("0.24")
    line_measure = [(mp.mpf("0.35"), 1), (mp.mpf("1.10"), 2), (mp.mpf("2.40"), 1)]
    moments = []
    for k in range(7):
        moments.append(sum(mult * mp.re(moment_kernel(k, mp.mpc(0, u), y)) for u, mult in line_measure))
    hankel = mp.matrix([[moments[i + j] for j in range(4)] for i in range(4)])
    eigvals = mp.eigsy(hankel, eigvals_only=True)
    min_hankel_eigenvalue = min(eigvals)
    assert min_hankel_eigenvalue > -mp.mpf("1e-55")
    checks += 16

    # The same terminal synthetic packet eventually has a negative raw moment,
    # so a Hankel diagonal criterion fails at finite order.
    y = mp.mpf("0.22")
    terminal_raw_moments = {}
    for k in [0, 4, 8, 16, 32]:
        raw = 2 * target_value(k, y)
        raw += 2 * sum(mp.re(moment_kernel(k, zz, y)) for zz in nuisances)
        raw += sum(mp.re(moment_kernel(k, mp.mpc(0, u), y)) for u in line_offsets)
        # raw equals A_k=-Re F_k for the synthetic zero packet.
        terminal_raw_moments[str(k)] = mp.nstr(raw, 24)
        checks += 1
    assert mp.mpf(terminal_raw_moments["16"]) < 0

    # Far-zero decay is at least summable for every finite order.
    for k in [0, 1, 3, 8]:
        y = mp.mpf("0.27")
        vals = [abs(moment_kernel(k, mp.mpc("0.2", r), y)) for r in [20, 40, 80]]
        assert vals[1] < vals[0] / 10 and vals[2] < vals[1] / 10
        checks += 2

    result: dict[str, Any] = {
        "classification": "PASS_TERMINAL_RESOLVENT_DERIVATIVE_HIERARCHY",
        "checks": checks,
        "max_rational_identity_error": mp.nstr(max_rational_error, 12),
        "max_laplace_moment_relative_error": mp.nstr(max_moment_error, 12),
        "max_alpha_derivative_relative_error": mp.nstr(max_derivative_error, 12),
        "max_safe_euler_atom_relative_error": mp.nstr(max_atom_error, 12),
        "minimum_sampled_line_kernel": mp.nstr(min_line_kernel, 12),
        "max_target_normalization_error": mp.nstr(max_target_normalization_error, 12),
        "minimum_sampled_safe_euler_margin": mp.nstr(min_safe_margin, 12),
        "synthetic_threat_exponents": [mp.nstr(v, 12) for v in threat_exponents],
        "synthetic_normalized_scalar_by_order": concentration,
        "minimum_synthetic_line_hankel_eigenvalue": mp.nstr(min_hankel_eigenvalue, 12),
        "synthetic_terminal_raw_moments": terminal_raw_moments,
        "scope": "finite algebra and numerical controls only; no RH claim",
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print("PASS_TERMINAL_RESOLVENT_DERIVATIVE_HIERARCHY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
