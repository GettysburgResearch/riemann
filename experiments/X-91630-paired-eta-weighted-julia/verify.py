#!/usr/bin/env python3
"""Finite replay for the paired-eta weighted Julia completion."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def eta_d(s):
    return (1 - mp.power(2, 1 - s)) * mp.zeta(s)


def i_eta(s):
    return eta_d(s) / s


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def f_l(z):
    L = mp.log(2)
    if abs(z) < mp.mpf("1e-40"):
        return L
    return (1 - mp.e ** (-L * z)) / z


def gamma_factor(s, omega):
    return mp.power(mp.pi, omega) * mp.gamma((s - omega) / 2) / mp.gamma((s + omega) / 2)


def gamma_integral(s, omega):
    a = (s - omega) / 2
    integrand = lambda u: (1 / omega) * mp.power(1 - mp.power(u, 1 / omega), a - 1)
    return mp.power(mp.pi, omega) / mp.gamma(omega) * mp.quad(integrand, [0, 1])


def completed_factor_rhs(s, omega):
    s0 = 1 - omega
    s1 = 1 + omega
    b = (s - omega) / (s + omega)
    return (
        i_eta(s - omega)
        / i_eta(s + omega)
        * b**2
        * f_l(s - s0)
        / f_l(s - s1)
        * gamma_factor(s, omega)
    )


def kernel(sigma, carriers):
    out = np.empty((len(carriers), len(carriers)), dtype=np.complex128)
    for i, x in enumerate(carriers):
        for j, y in enumerate(carriers):
            z = mp.mpf(str(sigma)) + 1j * (mp.mpf(str(x)) - mp.mpf(str(y)))
            out[i, j] = complex(i_eta(z))
    return (out + out.conj().T) / 2


def interval_integral_truncated(z, nmax):
    total = mp.mpc(0)
    for m in range(1, nmax + 1):
        lo = mp.log(2 * m - 1)
        hi = mp.log(2 * m)
        total += (mp.e ** (-z * lo) - mp.e ** (-z * hi)) / z
    return total


def build():
    sigma = mp.mpf("1.3")
    omega = mp.mpf("0.2")
    carriers = [0.0, 0.37, 0.91, 1.44]

    k_hard = kernel(float(sigma - omega), carriers)
    k_safe = kernel(float(sigma + omega), carriers)
    k_detail = (k_hard - k_safe + (k_hard - k_safe).conj().T) / 2
    detail_eig = np.linalg.eigvalsh(k_detail)

    nmax = 5000
    max_kernel_split_error = mp.mpf("0")
    for x in carriers:
        for y in carriers:
            z = sigma - omega + 1j * (mp.mpf(str(x)) - mp.mpf(str(y)))
            hard = interval_integral_truncated(z, nmax)
            safe = interval_integral_truncated(z + 2 * omega, nmax)
            detail = hard - safe
            exact = i_eta(z) - i_eta(z + 2 * omega)
            max_kernel_split_error = max(max_kernel_split_error, abs(detail - exact))

    factor_errors = []
    gamma_errors = []
    samples = [mp.mpf("1.7") + 0.4j, mp.mpf("2.3") + 1.1j, mp.mpf("1.45") + 0.73j]
    for s in samples:
        factor_errors.append(float(abs(xi(s - omega) / xi(s + omega) - completed_factor_rhs(s, omega))))
        gamma_errors.append(float(abs(gamma_factor(s, omega) - gamma_integral(s, omega))))

    ys = np.linspace(0.0, np.log(20000.0), 1001)
    m = np.exp(-float(omega) * ys)
    d = np.sqrt(1 - m * m)
    julia_error = float(np.max(np.abs(m * m + d * d - 1)))
    forward_norm = float(np.max(m))
    inverse_truncation_norm = float(np.max(np.exp(float(omega) * ys)))

    ts = np.linspace(-20.0, 20.0, 401)
    bvals = (1j * ts - float(omega)) / (1j * ts + float(omega))
    inner_error = float(np.max(np.abs(np.abs(bvals) - 1.0)))

    gates = {
        "eta_detail_psd": float(np.min(detail_eig)) > 0,
        "eta_kernel_split": max_kernel_split_error < mp.mpf("5e-4"),
        "julia_column": julia_error < 2e-15,
        "completed_factorization": max(factor_errors) < 1e-55,
        "gamma_laplace": max(gamma_errors) < 1e-45,
        "rational_inner": inner_error < 2e-15,
        "forward_contraction": forward_norm <= 1.0 + 1e-15,
        "inverse_same_space_unbounded_control": inverse_truncation_norm > 5.0,
    }
    gates = {k: bool(v) for k, v in gates.items()}
    assert all(gates.values())

    return {
        "status": "PASS_PAIRED_ETA_WEIGHTED_JULIA",
        "gates": gates,
        "sigma": float(sigma),
        "omega": float(omega),
        "eta_detail_eigenvalues": [float(v) for v in detail_eig],
        "truncated_eta_kernel_split_error": float(max_kernel_split_error),
        "julia_column_error": julia_error,
        "completed_factorization_errors": factor_errors,
        "gamma_laplace_errors": gamma_errors,
        "rational_inner_error": inner_error,
        "forward_multiplier_norm": forward_norm,
        "inverse_same_space_truncation_norm": inverse_truncation_norm,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
