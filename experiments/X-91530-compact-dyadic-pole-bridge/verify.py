#!/usr/bin/env python3
"""Finite regression for the compact dyadic pole-bridge continuation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70
LOG2 = mp.log(2)


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def eta_d(s):
    return (1 - mp.power(2, 1 - s)) * mp.zeta(s)


def f_interval(z):
    if abs(z) < mp.mpf("1e-40"):
        return LOG2
    return -mp.expm1(-LOG2 * z) / z


def factored_xi_ratio(s, omega):
    s0 = 1 - omega
    s1 = 1 + omega
    return (
        eta_d(s - omega)
        / eta_d(s + omega)
        * f_interval(s - s0)
        / f_interval(s - s1)
        * mp.pi**omega
        * (s - omega)
        / (s + omega)
        * mp.gamma((s - omega) / 2)
        / mp.gamma((s + omega) / 2)
    )


def bridge_gram(q, omega, carriers):
    matrix = np.empty((len(carriers), len(carriers)), dtype=complex)
    transported = np.empty_like(matrix)
    normalizer = mp.sqrt(f_interval(q) / f_interval(q + 2 * omega))

    for i, x in enumerate(carriers):
        for j, y in enumerate(carriers):
            delta = mp.mpf(x - y)
            source = f_interval(q + 2 * omega + 1j * delta) / f_interval(q + 2 * omega)
            target = mp.quad(
                lambda t: (
                    normalizer
                    * mp.e ** (-omega * t)
                    * mp.e ** (-1j * x * t)
                )
                * mp.conj(
                    normalizer
                    * mp.e ** (-omega * t)
                    * mp.e ** (-1j * y * t)
                )
                * mp.e ** (-q * t)
                / f_interval(q),
                [0, LOG2],
            )
            matrix[i, j] = complex(source)
            transported[i, j] = complex(target)
    return matrix, transported


def build():
    samples = (
        (mp.mpc("1.3", "0.7"), mp.mpf("0.2")),
        (mp.mpc("2.1", "1.1"), mp.mpf("0.37")),
        (mp.mpc("0.9", "0.2"), mp.mpf("0.1")),
    )
    factorization_error = mp.mpf("0")
    for s, omega in samples:
        direct = xi(s - omega) / xi(s + omega)
        factorization_error = max(factorization_error, abs(direct - factored_xi_ratio(s, omega)))

    omega = mp.mpf("0.23")
    endpoint_values = {
        "s0": float(f_interval(0) / f_interval(-2 * omega)),
        "s1": float(f_interval(2 * omega) / f_interval(0)),
    }

    compact_norm = mp.quad(
        lambda t: mp.e ** ((1 - 2 * omega) * t),
        [0, LOG2],
    )
    compact_norm_formula = (mp.power(2, 1 - 2 * omega) - 1) / (1 - 2 * omega)
    compact_norm_error = abs(compact_norm - compact_norm_formula)

    carriers = [0.0, 0.31, 0.83, 1.37]
    source, transported = bridge_gram(mp.mpf("-0.17"), omega, carriers)
    carrier_unitary_error = float(np.max(np.abs(source - transported)))
    source_eigenvalues = np.linalg.eigvalsh((source + source.conj().T) / 2)

    truncations = [10, 100, 1000, 10000]
    eta_tail_norms = [(2 * n) ** float(omega) for n in truncations]

    gates = {
        "completed_factorization": factorization_error < mp.mpf("1e-55"),
        "compact_pole_bridge": compact_norm_error < mp.mpf("1e-60"),
        "carrier_covariant_unitary": carrier_unitary_error < 2e-13,
        "positive_bridge_gram": float(source_eigenvalues[0]) > -2e-12,
        "eta_tail_growth": all(
            eta_tail_norms[j + 1] > eta_tail_norms[j]
            for j in range(len(eta_tail_norms) - 1)
        ),
    }
    assert all(gates.values())

    return {
        "status": "PASS_COMPACT_DYADIC_POLE_BRIDGE",
        "gates": gates,
        "omega": float(omega),
        "completed_factorization_error": float(factorization_error),
        "bridge_endpoint_values": endpoint_values,
        "compact_hardy_norm": float(compact_norm),
        "compact_hardy_norm_formula": float(compact_norm_formula),
        "compact_hardy_norm_error": float(compact_norm_error),
        "carrier_unitary_error": carrier_unitary_error,
        "bridge_gram_eigenvalues": [float(x) for x in source_eigenvalues],
        "eta_tail_truncations": truncations,
        "eta_tail_multiplier_norms": eta_tail_norms,
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
