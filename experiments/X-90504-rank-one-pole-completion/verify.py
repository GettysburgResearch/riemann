#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"


def inertia(a: np.ndarray, tol: float = 1e-10) -> tuple[int, int, int]:
    e = np.linalg.eigvalsh((a + a.conj().T) / 2)
    return int(np.sum(e > tol)), int(np.sum(e < -tol)), int(np.sum(np.abs(e) <= tol))


def main() -> None:
    H = np.array([[0.0, 1.0], [1.0, 0.0]])
    ep = np.array([1.0, 1.0]) / np.sqrt(2.0)
    em = np.array([1.0, -1.0]) / np.sqrt(2.0)
    Rp = np.outer(ep, ep)
    Rm = np.outer(em, em)

    completed = H + Rm
    if not np.allclose(completed, Rp, atol=1e-14):
        raise AssertionError((completed, Rp))
    if inertia(completed) != (1, 0, 1):
        raise AssertionError(inertia(completed))

    thresholds = []
    for t in (0.0, 0.25, 0.75, 1.0, 1.25, 2.0):
        eig = np.linalg.eigvalsh(H + t * Rm)
        thresholds.append({"t": t, "eigenvalues": eig.tolist()})
        if (t >= 1.0) != bool(eig.min() >= -1e-12):
            raise AssertionError((t, eig))

    rng = np.random.default_rng(90504)
    minimality_checks = 0
    for _ in range(500):
        X = rng.normal(size=(2, 2))
        R = X @ X.T
        # Scale R until H+R is PSD, then verify trace >= 1.
        lo, hi = 0.0, 1.0
        while np.linalg.eigvalsh(H + hi * R).min() < 0:
            hi *= 2.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if np.linalg.eigvalsh(H + mid * R).min() >= 0:
                hi = mid
            else:
                lo = mid
        C = hi * R
        if np.trace(C) < 1.0 - 1e-9:
            raise AssertionError(C)
        minimality_checks += 1

    # W has q hyperbolic zero blocks; adding the pole completion adds only one PSD line.
    index_cases = []
    for q in range(9):
        blocks = [Rp]
        for j in range(q):
            m = 1.0 + j / 7.0
            blocks.append(np.array([[0.0, m], [m, 0.0]]))
        n = sum(b.shape[0] for b in blocks)
        A = np.zeros((n, n))
        k = 0
        for b in blocks:
            d = b.shape[0]
            A[k:k+d, k:k+d] = b
            k += d
        neg = inertia(A)[1]
        if neg != q:
            raise AssertionError((q, neg))
        index_cases.append({"off_line_pairs": q, "completed_negative_index": neg})

    # Bilinear identity in arbitrary complex pole coordinates.
    bilinear_error = 0.0
    for _ in range(1000):
        x = rng.normal(size=2) + 1j * rng.normal(size=2)
        y = rng.normal(size=2) + 1j * rng.normal(size=2)
        pole = x[0] * np.conj(y[1]) + x[1] * np.conj(y[0])
        minus = ((x[0] - x[1]) / np.sqrt(2)) * np.conj((y[0] - y[1]) / np.sqrt(2))
        plus = ((x[0] + x[1]) / np.sqrt(2)) * np.conj((y[0] + y[1]) / np.sqrt(2))
        bilinear_error = max(bilinear_error, abs(pole + minus - plus))
    if bilinear_error > 1e-12:
        raise AssertionError(bilinear_error)

    result = {
        "verdict": "PASS_X_90504_RANK_ONE_POLE_COMPLETION",
        "completed_pole_eigenvalues": np.linalg.eigvalsh(completed).tolist(),
        "threshold_family": thresholds,
        "minimality_checks": minimality_checks,
        "bilinear_identity_max_error": bilinear_error,
        "index_cases": index_cases,
        "scope": "Exact finite pole algebra and synthetic index checks only; no prime-side sign theorem or RH claim.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
