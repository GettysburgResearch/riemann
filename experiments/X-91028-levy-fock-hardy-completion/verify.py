#!/usr/bin/env python3
"""Finite regression for the Lévy--Fock--Hardy completion.

This checks exact rational identities and finite synthetic controls only.
It does not evaluate the full zeta screw kernel, prove the proposed form-core
theorem, establish the prime-side fixed-scale Gram sign, or prove RH.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def sieve_lambdas(limit: int) -> list[tuple[int, float, float]]:
    """Return (n, Lambda(n), Lambda(n)/log(n)) for prime powers."""
    is_prime = [True] * (limit + 1)
    is_prime[:2] = [False, False]
    primes: list[int] = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            if p * p <= limit:
                for k in range(p * p, limit + 1, p):
                    is_prime[k] = False
    rows: list[tuple[int, float, float]] = []
    for p in primes:
        n = p
        r = 1
        while n <= limit:
            rows.append((n, math.log(p), 1.0 / r))
            if n > limit // p:
                break
            n *= p
            r += 1
    rows.sort()
    return rows


ALPHA = (mp.mpf(163) - 5 * mp.sqrt(561)) / 28
BETA = (mp.mpf(163) + 5 * mp.sqrt(561)) / 28


def psi_hat(a: mp.mpf, u: mp.mpf | mp.mpc) -> mp.mpc:
    return (
        mp.sqrt(378)
        * a**3
        * u
        * (u + 1j * mp.sqrt(ALPHA) * a)
        * (u + 1j * mp.sqrt(BETA) * a)
        / ((u + 1j * a) ** 2 * (u + 2j * a) ** 2 * (u + 4j * a) ** 2)
    )


def residual(a: mp.mpf, u: mp.mpf) -> mp.mpf:
    y = (u / a) ** 2
    return y * (378 * y**2 + 4401 * y + 6048) / (
        (1 + y) ** 2 * (4 + y) ** 2 * (16 + y) ** 2
    )


def log_q_finite(rows, a: complex, z: complex) -> complex:
    total = 0j
    for n, _lam, omega in rows:
        total += omega * (1 - n ** (-2 * a)) * n ** (-z)
    return total


def fock_inner_quadrature(rows, a: float, s: complex, t: complex) -> complex:
    total = 0j
    z = s + t.conjugate()
    for n, lam, _omega in rows:
        integrand = lambda tau: 2 * lam * mp.power(n, -z - 2 * tau)
        total += complex(mp.quad(integrand, [0, a]))
    return total


def min_eigenvalue_hermitian(matrix: list[list[complex]]) -> float:
    array = np.asarray(matrix, dtype=np.complex128)
    array = (array + array.conj().T) / 2
    return float(np.linalg.eigvalsh(array).min())


def build_report() -> dict:
    rows = sieve_lambdas(250)

    spectral_rows = []
    max_spectral_error = mp.mpf(0)
    max_scaling_error = mp.mpf(0)
    for a in (mp.mpf("0.6"), mp.mpf("1.0"), mp.mpf("1.7")):
        for u in (mp.mpf("0.13"), mp.mpf("0.7"), mp.mpf("2.4"), mp.mpf("8.0")):
            lhs = abs(psi_hat(a, u)) ** 2
            rhs = residual(a, u)
            error = abs(lhs - rhs)
            max_spectral_error = max(max_spectral_error, error)
            scaling_error = abs(psi_hat(a, u) - psi_hat(1, u / a))
            max_scaling_error = max(max_scaling_error, scaling_error)
            spectral_rows.append(
                {
                    "a": float(a),
                    "u": float(u),
                    "absolute_error": float(error),
                    "scaling_error": float(scaling_error),
                }
            )

    integrand = lambda u: abs(psi_hat(1, u)) ** 2 / u
    admissibility_numeric = mp.quad(integrand, [0, 1, mp.inf])
    admissibility_closed = mp.mpf(15) * mp.log(2) / 16
    admissibility_error = abs(admissibility_numeric - admissibility_closed)

    a = 0.73
    b = 0.41
    s = 0.82 + 0.31j
    t = 0.91 - 0.17j
    z = s + t.conjugate()
    fock_series = log_q_finite(rows, a, z)
    fock_quad = fock_inner_quadrature(rows, a, s, t)
    fock_error = abs(fock_series - fock_quad)
    cocycle_lhs = log_q_finite(rows, a + b, z)
    cocycle_rhs = log_q_finite(rows, a, z) + log_q_finite(rows, b, z + 2 * a)
    cocycle_error = abs(cocycle_lhs - cocycle_rhs)

    c = 1 + 2 * a
    theta = 1.37
    log_char = 0j
    for n, _lam, omega in rows:
        intensity = omega * (1 - n ** (-2 * a)) * n ** (-c)
        log_char += intensity * (cmath.exp(-1j * theta * math.log(n)) - 1)
    ratio_log = log_q_finite(rows, a, c + 1j * theta) - log_q_finite(rows, a, c)
    poisson_error = abs(cmath.exp(log_char) - cmath.exp(ratio_log))

    points = [0.62 + 0.1j, 0.77 - 0.25j, 1.05 + 0.42j, 0.69 + 0.55j]
    fock_gram = []
    for sj in points:
        row = []
        for tk in points:
            row.append(cmath.exp(log_q_finite(rows, a, sj + tk.conjugate())))
        fock_gram.append(row)
    fock_gram_min = min_eigenvalue_hermitian(fock_gram)

    gammas = [-37.0, -24.5, -14.2, 14.2, 24.5, 37.0]
    multiplicities = [1, 2, 1, 1, 2, 1]
    packet = [
        ("+", 0.8, -3.0),
        ("+", 1.1, 5.5),
        ("-", 0.9, -8.0),
        ("-", 1.4, 2.0),
    ]

    def oriented_value(sign: str, aa: float, xx: float, gamma: float) -> complex:
        value = complex(psi_hat(mp.mpf(aa), mp.mpf(gamma - xx)))
        return value if sign == "+" else value.conjugate()

    screw_gram = []
    for sign_j, aa, xx in packet:
        row = []
        for sign_k, bb, yy in packet:
            value = 0j
            for gamma, mult in zip(gammas, multiplicities):
                vj = oriented_value(sign_j, aa, xx, gamma)
                vk = oriented_value(sign_k, bb, yy, gamma)
                value += mult * vj * vk.conjugate()
            row.append(value)
        screw_gram.append(row)
    screw_gram_min = min_eigenvalue_hermitian(screw_gram)

    diagonal_rows = []
    max_diagonal_error = 0.0
    for aa, xx in ((0.8, -3.0), (1.2, 4.0), (1.6, 0.5)):
        gram_diag = sum(
            mult * abs(complex(psi_hat(mp.mpf(aa), mp.mpf(gamma - xx)))) ** 2
            for gamma, mult in zip(gammas, multiplicities)
        )
        residual_diag = sum(
            mult * float(residual(mp.mpf(aa), mp.mpf(gamma - xx)))
            for gamma, mult in zip(gammas, multiplicities)
        )
        error = abs(gram_diag - residual_diag)
        max_diagonal_error = max(max_diagonal_error, error)
        diagonal_rows.append(
            {
                "a": aa,
                "x": xx,
                "gram": gram_diag,
                "residual": residual_diag,
                "absolute_error": error,
            }
        )

    a_bridge = mp.mpf("1.25")
    eps = mp.mpf("1e-25")
    bridge_numeric = psi_hat(a_bridge, eps) / eps
    bridge_closed = mp.sqrt(378) / (16 * a_bridge)
    bridge_error = abs(bridge_numeric - bridge_closed)

    diagonal_firewall = [[1.0, 1.75], [1.75, 1.0]]
    firewall_min = min_eigenvalue_hermitian(diagonal_firewall)

    gates = {
        "spectral_factor_identity": max_spectral_error < mp.mpf("1e-60"),
        "scale_covariance": max_scaling_error < mp.mpf("1e-60"),
        "admissibility_constant": admissibility_error < mp.mpf("1e-45"),
        "fock_one_particle_identity": fock_error < 1e-12,
        "fock_scale_cocycle": cocycle_error < 1e-12,
        "compound_poisson_boundary": poisson_error < 1e-12,
        "fock_coherent_kernel_psd": fock_gram_min > -1e-11,
        "screw_wavelet_gram_psd": screw_gram_min > -1e-11,
        "diagonal_residual_identity": max_diagonal_error < 1e-12,
        "bridge_removable_value": bridge_error < mp.mpf("1e-20"),
        "diagonal_only_firewall": firewall_min < -0.1,
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    return {
        "status": "PASS_LEVY_FOCK_HARDY_COMPLETION",
        "gates": gates,
        "spectral_factor": {
            "max_absolute_error": float(max_spectral_error),
            "max_scaling_error": float(max_scaling_error),
            "rows": spectral_rows,
        },
        "admissibility": {
            "numeric": float(admissibility_numeric),
            "closed": float(admissibility_closed),
            "absolute_error": float(admissibility_error),
            "formula": "(15/16) log 2",
        },
        "fock": {
            "prime_power_terms": len(rows),
            "one_particle_absolute_error": fock_error,
            "scale_cocycle_absolute_error": abs(cocycle_error),
            "coherent_gram_min_eigenvalue": fock_gram_min,
        },
        "compound_poisson": {
            "absolute_error": poisson_error,
            "a": a,
            "c": c,
            "theta": theta,
        },
        "screw_wavelet": {
            "gram_min_eigenvalue": screw_gram_min,
            "packet_size": len(packet),
            "diagonal_rows": diagonal_rows,
            "max_diagonal_error": max_diagonal_error,
        },
        "bridge": {
            "numeric_real": float(mp.re(bridge_numeric)),
            "numeric_imag": float(mp.im(bridge_numeric)),
            "closed": float(bridge_closed),
            "absolute_error": float(bridge_error),
        },
        "firewall": {
            "matrix": diagonal_firewall,
            "minimum_eigenvalue": firewall_min,
        },
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
