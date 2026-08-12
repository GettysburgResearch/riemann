#!/usr/bin/env python3
"""Finite replay for the dyadic Clark martingale identities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def q(a: mp.mpf, s: complex) -> complex:
    return mp.zeta(s) / mp.zeta(s + 2 * a)


def multiplier(a: mp.mpf, sigma: mp.mpf, t: mp.mpf) -> complex:
    return q(a, sigma + 1j * t) / q(a, sigma)


def ell(a: mp.mpf, sigma: mp.mpf, t: mp.mpf) -> complex:
    return -mp.log(multiplier(a, sigma, t))


def build() -> dict:
    sigma = mp.mpf("1.7")
    a = mp.mpf("0.12")
    carriers = [mp.mpf("0"), mp.mpf("0.37"), mp.mpf("0.91"), mp.mpf("1.43")]

    cocycle_errors = [
        abs(ell(2 * a, sigma, t) - ell(a, sigma, t) - ell(a, sigma + 2 * a, t))
        for t in carriers
    ]

    base_split_errors = []
    for t in carriers:
        rhs = sum(ell(a, sigma + 2 * k * a, t) for k in range(8))
        base_split_errors.append(abs(ell(8 * a, sigma, t) - rhs))

    def innovation(t: mp.mpf) -> complex:
        return ell(a, sigma + 2 * a, t)

    gram = np.empty((len(carriers), len(carriers)), dtype=np.complex128)
    for i, ti in enumerate(carriers):
        for j, tj in enumerate(carriers):
            value = innovation(ti) + mp.conj(innovation(tj)) - innovation(ti - tj)
            gram[i, j] = complex(value)
    gram = (gram + gram.conj().T) / 2
    eigs = np.linalg.eigvalsh(gram)

    positive_real_samples = [float(mp.re(innovation(t))) for t in carriers[1:]]
    resonance = mp.mpf("2") * mp.pi / mp.log(2)
    atom_resonance_loss = 1 - mp.cos(resonance * mp.log(2))

    gates = {
        "cocycle": max(cocycle_errors) < mp.mpf("1e-55"),
        "base_split": max(base_split_errors) < mp.mpf("1e-55"),
        "innovation_gram_psd": float(eigs.min()) > -1e-11,
        "positive_real": min(positive_real_samples) > 0,
        "returned_atom": abs(atom_resonance_loss) < mp.mpf("1e-55"),
    }
    assert all(gates.values())

    return {
        "status": "PASS_DYADIC_CLARK_MARTINGALE",
        "gates": gates,
        "sigma": float(sigma),
        "base_scale": float(a),
        "cocycle_errors": [float(x) for x in cocycle_errors],
        "eight_section_errors": [float(x) for x in base_split_errors],
        "innovation_gram_eigenvalues": [float(x) for x in eigs],
        "innovation_positive_real_samples": positive_real_samples,
        "prime_two_resonance_loss": float(atom_resonance_loss),
    }


def main() -> None:
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
