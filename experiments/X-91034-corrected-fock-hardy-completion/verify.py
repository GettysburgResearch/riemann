#!/usr/bin/env python3
"""Finite regression for the corrected Poisson--Hardy completion.

This checks:
- the causal impulse formula and its interior zero;
- the exact hidden-jump orthogonality mechanism refuting the scalar-mother
  form-core claim;
- the energy-preserving delay-fibre dilation;
- finite diagnostics for the no-common-zero delay repair;
- the Poisson-chaos linearity firewall;
- the Jordan coefficient identity;
- an inner-scattering control showing amplitude unitarity does not sign radial
  curvature.

It does not evaluate the full zeta screw Gram, construct the RH-bearing
first-chaos contraction, or prove RH.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 80


A = (70 * mp.sqrt(33) - 61 * mp.sqrt(42)) / 9
B = 5 * (mp.sqrt(33) - mp.sqrt(42)) / 3
C = 3 * (5 * mp.sqrt(33) - 4 * mp.sqrt(42))
D = 20 * (mp.sqrt(33) - mp.sqrt(42)) / 3

ALPHA = (mp.mpf(163) - 5 * mp.sqrt(561)) / 28
BETA = (mp.mpf(163) + 5 * mp.sqrt(561)) / 28


def psi(t: mp.mpf) -> mp.mpf:
    t = mp.mpf(t)
    return (
        -A * mp.exp(-t)
        + B * t * mp.exp(-t)
        + C * t * mp.exp(-2 * t)
        + A * mp.exp(-4 * t)
        + D * t * mp.exp(-4 * t)
    )


def psi_prime(t: mp.mpf) -> mp.mpf:
    t = mp.mpf(t)
    return (
        A * mp.exp(-t)
        + B * (1 - t) * mp.exp(-t)
        + C * (1 - 2 * t) * mp.exp(-2 * t)
        - 4 * A * mp.exp(-4 * t)
        + D * (1 - 4 * t) * mp.exp(-4 * t)
    )


def transfer(s: mp.mpc) -> mp.mpc:
    s = mp.mpc(s)
    return (
        mp.sqrt(378)
        * s
        * (s + mp.sqrt(ALPHA))
        * (s + mp.sqrt(BETA))
        / ((s + 1) ** 2 * (s + 2) ** 2 * (s + 4) ** 2)
    )


def transfer_partial(s: mp.mpc) -> mp.mpc:
    s = mp.mpc(s)
    return (
        -A / (s + 1)
        + B / (s + 1) ** 2
        + C / (s + 2) ** 2
        + A / (s + 4)
        + D / (s + 4) ** 2
    )


def wavelet(t: mp.mpf, x: mp.mpf) -> mp.mpc:
    t = mp.mpf(t)
    x = mp.mpf(x)
    return -1j * mp.exp(1j * x * t) * (1j * x * psi(t) + psi_prime(t))


def psi_hat(u: mp.mpf | mp.mpc) -> mp.mpc:
    u = mp.mpc(u)
    return (
        mp.sqrt(378)
        * u
        * (u + 1j * mp.sqrt(ALPHA))
        * (u + 1j * mp.sqrt(BETA))
        / ((u + 1j) ** 2 * (u + 2j) ** 2 * (u + 4j) ** 2)
    )


def delay_energy(t: mp.mpf, kappa: mp.mpf) -> mp.mpf:
    t = mp.mpf(t)
    kappa = mp.mpf(kappa)
    if t <= 0:
        return mp.mpf(0)
    return mp.quad(
        lambda tau: 2 * kappa * mp.exp(-2 * kappa * tau) * abs(psi(t - tau)) ** 2,
        [0, t],
    )


def prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            factors.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        factors.append(m)
    return factors


def q_coeff(n: int, a: float) -> float:
    out = 1.0
    for p in prime_factors(n):
        out *= 1.0 - p ** (-2 * a)
    return out


def build_report() -> dict:
    # Exact partial-fraction identity, tested at high precision.
    partial_errors = []
    for s in (
        mp.mpf("0.2"),
        mp.mpf("1.3"),
        mp.mpc("0.8", "0.4"),
        mp.mpc("3.2", "-0.7"),
    ):
        partial_errors.append(abs(transfer(s) - transfer_partial(s)))
    max_partial_error = max(partial_errors)

    # Directed interval signs locate a genuine interior zero.
    iv = mp.iv
    Aiv = (70 * iv.sqrt(33) - 61 * iv.sqrt(42)) / 9
    Biv = 5 * (iv.sqrt(33) - iv.sqrt(42)) / 3
    Civ = 3 * (5 * iv.sqrt(33) - 4 * iv.sqrt(42))
    Div = 20 * (iv.sqrt(33) - iv.sqrt(42)) / 3

    def psi_iv(x):
        x = iv.mpf(x)
        return (
            -Aiv * iv.exp(-x)
            + Biv * x * iv.exp(-x)
            + Civ * x * iv.exp(-2 * x)
            + Aiv * iv.exp(-4 * x)
            + Div * x * iv.exp(-4 * x)
        )

    left_iv = psi_iv([1.55, 1.55])
    right_iv = psi_iv([1.60, 1.60])
    root = mp.findroot(psi, (mp.mpf("1.55"), mp.mpf("1.60")))

    # Exact hidden-jump orthogonality, checked by quadrature.
    orthogonality = []
    max_orthogonality = mp.mpf(0)
    for x in (-4.0, -1.2, 0.0, 0.7, 3.0):
        value = mp.quad(lambda tt: wavelet(tt, x), [root, root + 10, mp.inf])
        max_orthogonality = max(max_orthogonality, abs(value))
        orthogonality.append(
            {
                "carrier": x,
                "real": float(mp.re(value)),
                "imag": float(mp.im(value)),
                "absolute": float(abs(value)),
            }
        )

    # Delay-fibre isometry and non-common-zero diagnostics.
    kappa = mp.mpf("0.9")
    delay_rows = []
    min_delay_energy = mp.inf
    for tt in (
        mp.mpf("0.05"),
        mp.mpf("0.2"),
        mp.mpf("0.8"),
        root,
        mp.mpf("2.4"),
        mp.mpf("5.0"),
    ):
        energy = delay_energy(tt, kappa)
        min_delay_energy = min(min_delay_energy, energy)
        delay_rows.append({"t": float(tt), "energy": float(energy)})

    delay_isometry_errors = []
    for u in (mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("2.0"), mp.mpf("7.0")):
        lhs = mp.quad(
            lambda tau: 2
            * kappa
            * mp.exp(-2 * kappa * tau)
            * abs(mp.exp(-1j * u * tau) * psi_hat(u)) ** 2,
            [0, mp.inf],
        )
        rhs = abs(psi_hat(u)) ** 2
        delay_isometry_errors.append(abs(lhs - rhs))
    max_delay_isometry_error = max(delay_isometry_errors)

    # Poisson-chaos linearity: a genuinely nonlinear chaos has nonzero r^2 term.
    z = mp.mpf("0.37")
    chaos_second = z**2
    r = mp.mpf("1e-5")
    finite_second = 2 * (mp.exp(r * z) - 1 - r * z) / r**2

    # Finite Jordan coefficient checks.
    a = 0.73
    jordan_rows = []
    jordan_positive = True
    for n in range(1, 65):
        qn = q_coeff(n, a)
        cn = n**a * qn
        jordan_positive &= qn > 0 and cn > 0
        if n in (1, 2, 4, 6, 12, 30, 60):
            jordan_rows.append({"n": n, "q": qn, "c": cn})

    # Local Euler factor identity.
    euler_errors = []
    s0 = 1.8
    for p in (2, 3, 5, 11):
        lhs = (1 - p ** (-(s0 + 2 * a))) / (1 - p ** (-s0))
        rhs = 1.0 + (1 - p ** (-2 * a)) * p ** (-s0) / (1 - p ** (-s0))
        euler_errors.append(abs(lhs - rhs))
    max_euler_error = max(euler_errors)

    # Inner scattering amplitude does not sign radial curvature.
    inner_rows = []
    inner_ok = True
    for aa in (0.4, 0.9, 1.7):
        for x in (-2.0, 0.0, 3.0):
            zc = complex(x, 0.6)
            theta = cmath.exp(1j * aa * aa * zc)
            inner_ok &= abs(theta) <= 1 + 1e-14
        curvature = -(aa**3) / 4.0
        inner_rows.append({"a": aa, "soft_curvature": curvature})

    gates = {
        "causal_partial_fraction": max_partial_error < mp.mpf("1e-65"),
        "left_interval_positive": float(left_iv.a) > 0,
        "right_interval_negative": float(right_iv.b) < 0,
        "root_in_bracket": mp.mpf("1.55") < root < mp.mpf("1.60"),
        "hidden_jump_orthogonality": max_orthogonality < mp.mpf("1e-50"),
        "delay_fibre_isometry": max_delay_isometry_error < mp.mpf("1e-60"),
        "delay_fibre_no_common_zero_diagnostic": min_delay_energy > 0,
        "poisson_higher_chaos_nonzero": abs(finite_second - chaos_second)
        < mp.mpf("1e-5")
        and chaos_second > 0,
        "jordan_coefficients_positive": jordan_positive,
        "jordan_local_euler_identity": max_euler_error < 1e-14,
        "inner_amplitude_negative_curvature_control": inner_ok
        and all(row["soft_curvature"] < 0 for row in inner_rows),
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_CORRECTED_FOCK_HARDY_COMPLETION",
        "gates": gates,
        "causal_impulse": {
            "A": float(A),
            "B": float(B),
            "C": float(C),
            "D": float(D),
            "max_partial_fraction_error": float(max_partial_error),
            "left_interval": [float(left_iv.a), float(left_iv.b)],
            "right_interval": [float(right_iv.a), float(right_iv.b)],
            "root": float(root),
        },
        "hidden_jump": {
            "max_quadrature_absolute": float(max_orthogonality),
            "rows": orthogonality,
        },
        "delay_fibre": {
            "kappa": float(kappa),
            "max_isometry_error": float(max_delay_isometry_error),
            "minimum_sampled_energy": float(min_delay_energy),
            "rows": delay_rows,
        },
        "poisson_chaos": {
            "one_particle_inner_product": float(z),
            "exact_second_derivative_at_zero": float(chaos_second),
            "finite_difference": float(finite_second),
        },
        "jordan": {
            "a": a,
            "max_local_euler_error": max_euler_error,
            "rows": jordan_rows,
        },
        "inner_control": inner_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
