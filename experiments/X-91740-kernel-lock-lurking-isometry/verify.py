#!/usr/bin/env python3
"""Finite replay for the kernel-lock lurking-isometry reduction."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def gram(x):
    return x.conj().T @ x


def psd_factor(matrix, tol=1e-13):
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2)
    keep = values > tol
    return np.sqrt(values[keep])[:, None] * vectors[:, keep].conj().T


def build():
    rng = np.random.default_rng(91740)
    c_feat = rng.normal(size=(3, 5)) + 1j * rng.normal(size=(3, 5))
    h_feat = 0.17 * (rng.normal(size=(2, 5)) + 1j * rng.normal(size=(2, 5)))
    e_feat = 0.09 * (rng.normal(size=(2, 5)) + 1j * rng.normal(size=(2, 5)))

    C = gram(c_feat)
    H = gram(h_feat)
    E = gram(e_feat)
    A = C + H + E
    R = A - C

    r_factor = psd_factor(R)
    reconstructed = C + gram(r_factor)
    reconstruction_error = float(np.max(np.abs(A - reconstructed)))

    source_factor = psd_factor(A)
    target_factor = np.vstack([psd_factor(C), r_factor])
    source_gram_error = float(np.max(np.abs(gram(source_factor) - gram(target_factor))))

    eta = 50.0
    delta = 0.03
    upper = 0.06
    Y = np.sqrt(eta**2 - upper**2)
    moat = 2 * delta / (np.sqrt(upper**2 + Y**2) + upper)
    threshold = np.expm1(moat) / (2 * eta)

    scalar_residual = 0.4 * threshold
    entropy_bound = np.log1p(2 * eta * scalar_residual)

    rho = 0.8
    same_diag_a = np.array([[1.0, rho], [rho, 1.0]])
    same_diag_c = np.array([[1.0, -rho], [-rho, 1.0]])
    diagonal_difference_eigs = np.linalg.eigvalsh(same_diag_a - same_diag_c)

    gates = {
        "positive_residual": bool(np.linalg.eigvalsh(R).min() > -1e-11),
        "kolmogorov_reconstruction": bool(reconstruction_error < 1e-10),
        "lurking_isometry_gram": bool(source_gram_error < 1e-10),
        "moving_node_threshold": bool(entropy_bound < moat),
        "diagonal_firewall": bool(diagonal_difference_eigs.min() < 0 < diagonal_difference_eigs.max()),
    }
    assert all(gates.values())

    return {
        "status": "PASS_KERNEL_LOCK_LURKING_ISOMETRY",
        "gates": gates,
        "residual_min_eigenvalue": float(np.linalg.eigvalsh(R).min()),
        "reconstruction_error": reconstruction_error,
        "source_target_gram_error": source_gram_error,
        "moving_node_eta": eta,
        "moving_node_height": float(Y),
        "zero_moat": float(moat),
        "kernel_residual_threshold": float(threshold),
        "test_scalar_residual": float(scalar_residual),
        "entropy_upper_bound": float(entropy_bound),
        "same_diagonal_difference_eigenvalues": [
            float(x) for x in diagonal_difference_eigs
        ],
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
