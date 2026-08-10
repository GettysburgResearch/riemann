#!/usr/bin/env python3
"""Finite regressions for coherent Gabor collapse and off-line pair spectrum.

The first regression is an exact finite cyclic analogue of the full-lattice
coisometry theorem. The second checks the analytically continued Shannon/Poisson
identities for a rectangular window and the resulting hyperbolic eigenvalues.

The script is a regression, not a substitute for the proofs in the companion
notes.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def unitary_fourier(n: int) -> np.ndarray:
    j = np.arange(n)[:, None]
    k = np.arange(n)[None, :]
    return np.exp(2j * np.pi * j * k / n) / np.sqrt(n)


def coherent_collapse(
    seed: int = 20260810, n: int = 32, channels: int = 4
) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    fourier = unitary_fourier(n)
    windows = rng.normal(size=(channels, n)) + 1j * rng.normal(
        size=(channels, n)
    )
    windows += np.linspace(0.3, 1.0, n)[None, :]
    psi = np.sqrt(np.sum(np.abs(windows) ** 2, axis=0))

    scalar = np.diag(psi) @ fourier
    blocks = [np.diag(windows[a]) @ fourier for a in range(channels)]
    multi = np.concatenate(blocks, axis=1)

    time_coisometry = np.concatenate(
        [np.diag(windows[a] / psi) for a in range(channels)], axis=1
    )
    block_fourier = np.kron(np.eye(channels), fourier)
    coisometry = fourier.conj().T @ time_coisometry @ block_fourier

    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    operator = (z + z.conj().T) / 2.0
    g_scalar = scalar.conj().T @ operator @ scalar
    g_multi = multi.conj().T @ operator @ multi
    predicted = coisometry.conj().T @ g_scalar @ coisometry

    coisometry_error = np.linalg.norm(
        coisometry @ coisometry.conj().T - np.eye(n), ord=2
    )
    congruence_error = np.linalg.norm(g_multi - predicted, ord="fro") / max(
        1.0, np.linalg.norm(g_multi, ord="fro")
    )

    evals_scalar = np.linalg.eigvalsh(g_scalar)
    evals_multi = np.linalg.eigvalsh(g_multi)
    nonzero_multi = evals_multi[np.abs(evals_multi) > 2e-9]
    spectral_error = np.max(
        np.abs(np.sort(evals_scalar) - np.sort(nonzero_multi))
    )

    trace_errors: dict[str, float] = {}
    for power in (1, 2, 3, 4):
        left = np.trace(np.linalg.matrix_power(g_scalar, power))
        right = np.trace(np.linalg.matrix_power(g_multi, power))
        trace_errors[str(power)] = float(
            abs(left - right) / max(1.0, abs(left))
        )

    return {
        "n": n,
        "channels": channels,
        "coisometry_error": float(coisometry_error),
        "congruence_relative_error": float(congruence_error),
        "spectral_error": float(spectral_error),
        "trace_power_errors": trace_errors,
        "extra_zero_eigenvalues": int(g_multi.shape[0] - len(nonzero_multi)),
    }


def rect_hat(
    z: np.ndarray | complex, length: float
) -> np.ndarray | complex:
    z_arr = np.asarray(z, dtype=np.complex128)
    out = np.empty_like(z_arr)
    small = np.abs(z_arr) < 1e-13
    out[small] = length
    out[~small] = (
        2.0 * np.sin(z_arr[~small] * length / 2.0) / z_arr[~small]
    )
    if np.ndim(z) == 0:
        return complex(out)
    return out


def offline_pair(
    length: float = 8.0,
    x: float = 0.37,
    y: float = 0.12,
    cutoff: int = 30000,
) -> dict[str, object]:
    spacing = 2.0 * np.pi / length
    k = np.arange(-cutoff, cutoff + 1, dtype=np.float64)
    z = x + 1j * y
    values = rect_hat(z - spacing * k, length)
    norm_sq = float(np.sum(np.abs(values) ** 2).real)
    bilinear = complex(np.sum(values**2))

    expected_norm = length * np.sinh(y * length) / y
    expected_bilinear = length**2
    ratio = np.sinh(y * length) / (y * length)
    gram = np.array([[ratio, 1.0], [1.0, ratio]], dtype=np.float64)
    hyperbolic = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.float64)
    eigenvalues = np.linalg.eigvalsh(hyperbolic @ gram)
    expected_eigenvalues = np.array([1.0 - ratio, 1.0 + ratio])

    return {
        "length": length,
        "x": x,
        "y": y,
        "cutoff": cutoff,
        "norm_relative_error": abs(norm_sq - expected_norm)
        / expected_norm,
        "bilinear_relative_error": abs(bilinear - expected_bilinear)
        / expected_bilinear,
        "ratio": float(ratio),
        "negative_eigenvalue": float(eigenvalues[0]),
        "positive_eigenvalue": float(eigenvalues[1]),
        "eigenvalue_error": float(
            np.max(np.abs(eigenvalues - expected_eigenvalues))
        ),
        "quadratic_lower_bound": float((y * length) ** 2 / 6.0),
        "actual_negative_magnitude": float(ratio - 1.0),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--seed", type=int, default=20260810)
    args = parser.parse_args()

    collapse = coherent_collapse(seed=args.seed)
    pair = offline_pair()

    gates = {
        "coisometry": bool(collapse["coisometry_error"] < 2e-12),
        "congruence": bool(
            collapse["congruence_relative_error"] < 2e-12
        ),
        "spectrum": bool(collapse["spectral_error"] < 2e-8),
        "rect_norm": bool(pair["norm_relative_error"] < 2e-5),
        "rect_bilinear": bool(pair["bilinear_relative_error"] < 2e-5),
        "pair_eigenvalues": bool(pair["eigenvalue_error"] < 1e-12),
        "depth_lower_bound": bool(
            pair["actual_negative_magnitude"] + 1e-15
            >= pair["quadratic_lower_bound"]
        ),
    }
    payload = {
        "status": "PASS_ZETA23_GABOR_FUSION"
        if all(gates.values())
        else "FAIL",
        "gates": gates,
        "coherent_multiwindow": collapse,
        "offline_pair": pair,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
