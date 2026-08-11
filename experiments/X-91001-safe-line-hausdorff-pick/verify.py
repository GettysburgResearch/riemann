#!/usr/bin/env python3
"""Finite regression for the single-safe-line Hausdorff/Pick completion.

This script checks exact algebraic identities and high-precision synthetic
controls. It does not prove RH, the analytic zero-sum statements, or any
prime-side positivity theorem.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any

import mpmath as mp

mp.mp.dps = 80


def q_coefficients(k: int) -> list[int]:
    """Ascending coefficients of Q_k=2^(k+1) P_k."""
    coeff = [1, 1, -1]
    for n in range(k):
        nxt = [0] * (len(coeff) + 1)
        for j, value in enumerate(coeff):
            nxt[j] += (2 * n + 3 - j) * value
            nxt[j + 1] += value
        coeff = nxt
    return coeff


def p_value(k: int, t: mp.mpf) -> mp.mpf:
    coeff = q_coefficients(k)
    return mp.fsum(mp.mpf(value) * t**j for j, value in enumerate(coeff)) / (mp.mpf(2) ** (k + 1))


def beta_euler_polynomial(k: int, m: int, t: mp.mpf) -> mp.mpf:
    return mp.fsum(
        (-1) ** j * comb(m, j) * p_value(k + j, t) / mp.factorial(k + j + 2)
        for j in range(m + 1)
    )


def beta_euler_laguerre_integral(k: int, m: int, t: mp.mpf) -> mp.mpf:
    integrand = lambda q: (
        q ** (k + mp.mpf("0.5"))
        * mp.exp(-q - t * t / (4 * q))
        * mp.laguerre(m, k + 2, q)
        * (1 - t * t / (2 * q))
    )
    return (
        mp.exp(t)
        * mp.factorial(m)
        / (mp.sqrt(mp.pi) * mp.factorial(k + m + 2))
        * mp.quad(integrand, [0, mp.inf])
    )


def safe_line_euler_generating_closed(w: mp.mpc, t: mp.mpf) -> mp.mpc:
    r = mp.sqrt(1 - w)
    return ((2 - w + w * t) * mp.exp(-t) - 2 * r * mp.exp(-t * r)) / (w * w)


def safe_line_euler_generating_series(w: mp.mpc, t: mp.mpf, terms: int = 50) -> mp.mpc:
    return mp.fsum(
        mp.exp(-t) * p_value(k, t) * w**k / mp.factorial(k + 2)
        for k in range(terms)
    )


def normalized_kernel(k: int, z: mp.mpc) -> mp.mpc:
    return -2 * z * z / (1 - z * z) ** (k + 3)


def beta_kernel(k: int, m: int, z: mp.mpc) -> mp.mpc:
    return -2 * ((-1) ** m) * z ** (2 * m + 2) / (1 - z * z) ** (k + m + 3)


def finite_difference_kernel(k: int, m: int, z: mp.mpc) -> mp.mpc:
    return mp.fsum(
        (-1) ** j * comb(m, j) * normalized_kernel(k + j, z)
        for j in range(m + 1)
    )


def line_moment(k: int, u: mp.mpf) -> mp.mpf:
    return 2 * u * u / (1 + u * u) ** (k + 3)


def line_beta(k: int, m: int, u: mp.mpf) -> mp.mpf:
    return 2 * u ** (2 * m + 2) / (1 + u * u) ** (k + m + 3)


def right_pair_moment(k: int, z: mp.mpc) -> mp.mpf:
    return -4 * mp.re(z * z / (1 - z * z) ** (k + 3))


def right_pair_beta(k: int, m: int, z: mp.mpc) -> mp.mpf:
    return -4 * ((-1) ** m) * mp.re(z ** (2 * m + 2) / (1 - z * z) ** (k + m + 3))


def line_generating(w: mp.mpc, u: mp.mpf) -> mp.mpc:
    return 2 * u * u / ((1 + u * u) ** 2 * (1 + u * u - w))


def right_pair_generating(w: mp.mpc, z: mp.mpc) -> mp.mpc:
    term = z * z / ((1 - z * z) ** 2 * (1 - z * z - w))
    zc = mp.conj(z)
    reflected = zc * zc / ((1 - zc * zc) ** 2 * (1 - zc * zc - w))
    return -2 * (term + reflected)


def line_measure_moments(us: list[mp.mpf], multiplicities: list[int], count: int) -> list[mp.mpf]:
    return [
        mp.fsum(mult * line_moment(k, u) for u, mult in zip(us, multiplicities, strict=True))
        for k in range(count)
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    checks = 0
    max_difference_error = mp.mpf(0)
    max_line_error = mp.mpf(0)
    max_partition_error = Fraction(0)
    max_generating_error = mp.mpf(0)
    max_laguerre_error = mp.mpf(0)
    max_square_root_generating_error = mp.mpf(0)
    min_line_beta = mp.inf
    min_hankel_eigenvalue = mp.inf
    min_pick_eigenvalue = mp.inf

    # Exact finite-difference kernel identity.
    z_values = [mp.mpc("0.17", "0.43"), mp.mpc("0.31", "1.10"), mp.mpc("-0.12", "0.73")]
    for k in range(6):
        for m in range(7):
            for z in z_values:
                lhs = finite_difference_kernel(k, m, z)
                rhs = beta_kernel(k, m, z)
                err = abs(lhs - rhs) / max(mp.mpf(1), abs(rhs))
                max_difference_error = max(max_difference_error, err)
                assert err < mp.mpf("1e-65")
                checks += 1

    # Critical-line beta kernel is nonnegative and matches the closed formula.
    for k in range(6):
        for m in range(7):
            for u in [mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2.5"), mp.mpf("8")]:
                lhs = mp.re(beta_kernel(k, m, mp.mpc(0, u)))
                rhs = line_beta(k, m, u)
                err = abs(lhs - rhs)
                max_line_error = max(max_line_error, err)
                min_line_beta = min(min_line_beta, lhs)
                assert err < mp.mpf("1e-65") and lhs >= -mp.mpf("1e-65")
                checks += 1

    # A real off-line target has parity-alternating beta cells; even m detects negatively.
    y = mp.mpf("0.23")
    target_by_m: dict[str, str] = {}
    for m in range(8):
        value = right_pair_beta(11, m, mp.mpc(y))
        target_by_m[str(m)] = mp.nstr(value, 24)
        assert (value < 0) if m % 2 == 0 else (value > 0)
        checks += 1

    # Exact Bernstein partition in lambda coordinates.
    for denominator in [5, 11, 37]:
        for numerator in range(1, denominator):
            lam = Fraction(numerator, denominator)
            base = 2 * (1 - lam) * lam * lam
            for n in range(0, 13):
                total = sum(
                    Fraction(comb(n, j))
                    * 2
                    * (1 - lam) ** (n - j + 1)
                    * lam ** (j + 2)
                    for j in range(n + 1)
                )
                err = abs(total - base)
                max_partition_error = max(max_partition_error, err)
                assert err == 0
                checks += 1

    # Synthetic line-only packet: complete finite differences and beta-Hankel matrices are PSD.
    us = [mp.mpf("0.35"), mp.mpf("1.10"), mp.mpf("2.40"), mp.mpf("5.0")]
    mults = [1, 2, 1, 3]
    moments = line_measure_moments(us, mults, 100)
    minimum_difference = mp.inf
    for k in range(12):
        for m in range(10):
            value = mp.fsum((-1) ** j * comb(m, j) * moments[k + j] for j in range(m + 1))
            closed = mp.fsum(mult * line_beta(k, m, u) for u, mult in zip(us, mults, strict=True))
            assert abs(value - closed) < mp.mpf("1e-65")
            minimum_difference = min(minimum_difference, value)
            assert value >= -mp.mpf("1e-65")
            checks += 1

    for m in range(5):
        size = 5
        matrix = mp.matrix(
            [
                [
                    mp.fsum(mult * line_beta(i + j, m, u) for u, mult in zip(us, mults, strict=True))
                    for j in range(size)
                ]
                for i in range(size)
            ]
        )
        eigvals = mp.eigsy(matrix, eigvals_only=True)
        min_hankel_eigenvalue = min(min_hankel_eigenvalue, min(eigvals))
        assert min(eigvals) > -mp.mpf("1e-55")
        checks += size * size

    # Pick matrix of the line-only Stieltjes transform is PSD.
    points = [mp.mpc("-0.4", "0.2"), mp.mpc("0.1", "0.35"), mp.mpc("0.55", "0.15")]

    def line_A(w: mp.mpc) -> mp.mpc:
        return mp.fsum(mult * line_generating(w, u) for u, mult in zip(us, mults, strict=True))

    pick = mp.matrix(
        [
            [
                (line_A(points[i]) - mp.conj(line_A(points[j])))
                / (points[i] - mp.conj(points[j]))
                for j in range(len(points))
            ]
            for i in range(len(points))
        ]
    )
    pick = (pick + pick.transpose_conj()) / 2
    eigvals = mp.eighe(pick, eigvals_only=True)
    min_pick_eigenvalue = min(eigvals)
    assert min_pick_eigenvalue > -mp.mpf("1e-55")
    checks += len(points) ** 2

    # Power series agrees with the closed Stieltjes generating function.
    for w in [mp.mpc("0.2", "0.1"), mp.mpc("-0.5", "0.2"), mp.mpc("0.7", "0.0")]:
        partial = mp.fsum(moments[k] * w**k for k in range(80))
        closed = line_A(w)
        err = abs(partial - closed)
        max_generating_error = max(max_generating_error, err)
        assert err < mp.mpf("1e-13")
        checks += 1

    # Synthetic terminal packet: an off-line pair creates an interior pole at w=1-y^2
    # and normalized coefficients grow at rate 1/(1-y^2)>1.
    y = mp.mpf("0.27")
    pole = 1 - y * y
    residue = mp.re(mp.limit(lambda w: (w - pole) * right_pair_generating(w, mp.mpc(y)), pole))
    expected_residue = 4 * y * y / pole**2
    assert abs(residue - expected_residue) < mp.mpf("1e-50") and residue > 0
    checks += 1

    growth_samples: dict[str, str] = {}
    for k in [4, 8, 16, 32, 64, 96]:
        coefficient = abs(right_pair_moment(k, mp.mpc(y)))
        root = coefficient ** (mp.mpf(1) / k)
        growth_samples[str(k)] = mp.nstr(root, 24)
        checks += 1
    growth_limit = 1 / pole
    assert abs(mp.mpf(growth_samples["96"]) - growth_limit) < mp.mpf("0.05")

    # The complete order hierarchy sums to one square-root Euler weight.
    for w, t in [
        (mp.mpc("0.20", "0.10"), mp.mpf("0.7")),
        (mp.mpc("-0.45", "0.15"), mp.mpf("2.4")),
        (mp.mpc("0.70", "0.00"), mp.mpf("5.1")),
        (mp.mpc("0.10", "-0.30"), mp.mpf("1.3")),
    ]:
        direct = safe_line_euler_generating_series(w, t, terms=180)
        closed = safe_line_euler_generating_closed(w, t)
        err = abs(direct - closed) / max(mp.mpf(1), abs(closed))
        max_square_root_generating_error = max(max_square_root_generating_error, err)
        assert err < mp.mpf("1e-25")
        checks += 1

    # The real radial threshold 3/4 is exactly where the moving Euler sample
    # reaches Re(s)=1 from s=1/2+ix.
    below_margin = mp.mpf("0.5") + mp.sqrt(1 - mp.mpf("0.74")) - 1
    boundary_margin = mp.mpf("0.5") + mp.sqrt(1 - mp.mpf("0.75")) - 1
    above_margin = mp.mpf("0.5") + mp.sqrt(1 - mp.mpf("0.76")) - 1
    assert below_margin > 0 and abs(boundary_margin) < mp.mpf("1e-75") and above_margin < 0
    checks += 3

    # Source-side beta Euler weights equal the exact Laguerre-Gamma transform.
    for k, m, t in [
        (0, 0, mp.mpf("1.2")),
        (1, 2, mp.mpf("3.4")),
        (3, 4, mp.mpf("2.1")),
        (2, 1, mp.mpf("0.7")),
        (5, 3, mp.mpf("6.0")),
    ]:
        direct = beta_euler_polynomial(k, m, t)
        integral = beta_euler_laguerre_integral(k, m, t)
        err = abs(direct - integral) / max(mp.mpf(1), abs(direct))
        max_laguerre_error = max(max_laguerre_error, err)
        assert err < mp.mpf("1e-50")
        checks += 1

    result: dict[str, Any] = {
        "classification": "PASS_SINGLE_SAFE_LINE_HAUSDORFF_PICK_COMPLETION",
        "checks": checks,
        "max_finite_difference_kernel_error": mp.nstr(max_difference_error, 12),
        "max_critical_line_kernel_error": mp.nstr(max_line_error, 12),
        "minimum_sampled_critical_line_beta_kernel": mp.nstr(min_line_beta, 12),
        "max_exact_bernstein_partition_error": str(max_partition_error),
        "minimum_synthetic_hausdorff_difference": mp.nstr(minimum_difference, 12),
        "minimum_synthetic_beta_hankel_eigenvalue": mp.nstr(min_hankel_eigenvalue, 12),
        "minimum_synthetic_pick_eigenvalue": mp.nstr(min_pick_eigenvalue, 12),
        "max_stieltjes_generating_series_error": mp.nstr(max_generating_error, 12),
        "synthetic_interior_pole": mp.nstr(pole, 24),
        "synthetic_interior_pole_residue": mp.nstr(residue, 24),
        "synthetic_coefficient_root_growth": growth_samples,
        "synthetic_coefficient_root_growth_limit": mp.nstr(growth_limit, 24),
        "target_beta_cell_by_difference_order": target_by_m,
        "max_laguerre_gamma_relative_error": mp.nstr(max_laguerre_error, 12),
        "max_square_root_generating_relative_error": mp.nstr(max_square_root_generating_error, 12),
        "absolute_euler_radial_threshold": "0.75",
        "scope": "finite algebra and synthetic controls only; no Riemann-data sign or RH claim",
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print("PASS_SINGLE_SAFE_LINE_HAUSDORFF_PICK_COMPLETION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
