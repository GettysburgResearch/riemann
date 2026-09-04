#!/usr/bin/env python3
"""Adversarial numerical stress tests for the rank--trace inequality.

The tested theorem is

  ||P+Q||_F^2 >= c tr(P) - c^2 rank(P)/4
                  + 2c tr(Q) - c^2 n_+(Q),

for Hermitian P >= 0 and arbitrary Hermitian Q.

Floating-point tests do not prove the theorem. They are intended to catch sign,
normalization, and coefficient regressions in implementations and downstream use.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class Summary:
    trials: int
    dimension: int
    minimum_gap: float
    equality_gap: float
    failures: int
    seed: int


def random_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
    return q * np.conjugate(phases)


def hermitian_from_spectrum(
    rng: np.random.Generator, spectrum: np.ndarray
) -> np.ndarray:
    u = random_unitary(rng, len(spectrum))
    return (u * spectrum) @ u.conj().T


def numerical_rank_psd(p: np.ndarray, tol: float = 1e-10) -> int:
    vals = np.linalg.eigvalsh(p)
    return int(np.count_nonzero(vals > tol))


def positive_index(q: np.ndarray, tol: float = 1e-10) -> int:
    vals = np.linalg.eigvalsh(q)
    return int(np.count_nonzero(vals > tol))


def inequality_gap(p: np.ndarray, q: np.ndarray, c: float) -> float:
    if c <= 0:
        raise ValueError("c must be positive")
    r = numerical_rank_psd(p)
    b = positive_index(q)
    lhs = float(np.linalg.norm(p + q, "fro") ** 2)
    rhs = (
        c * float(np.trace(p).real)
        - c * c * r / 4.0
        + 2.0 * c * float(np.trace(q).real)
        - c * c * b
    )
    return lhs - rhs


def equality_case(n: int, r: int, b: int, c: float) -> tuple[np.ndarray, np.ndarray]:
    if r + b > n:
        raise ValueError("need r+b <= n")
    p = np.zeros((n, n), dtype=np.complex128)
    q = np.zeros((n, n), dtype=np.complex128)
    p[np.arange(r), np.arange(r)] = c / 2.0
    q[np.arange(r, r + b), np.arange(r, r + b)] = c
    return p, q


def run(trials: int, n: int, seed: int) -> Summary:
    rng = np.random.default_rng(seed)
    min_gap = float("inf")
    failures = 0

    # Exact equality configuration, represented in floating point.
    p_eq, q_eq = equality_case(n, max(1, n // 4), max(1, n // 5), 2.7)
    equality_gap = inequality_gap(p_eq, q_eq, 2.7)

    for _ in range(trials):
        c = float(rng.uniform(0.05, 8.0))
        r = int(rng.integers(0, n + 1))
        b = int(rng.integers(0, n + 1))

        # Mix tiny, ordinary, and huge eigenvalues to probe cancellation.
        p_spec = np.zeros(n)
        if r:
            scales = 10.0 ** rng.uniform(-8.0, 8.0, size=r)
            p_spec[:r] = scales * rng.uniform(0.05, 3.0, size=r)
        rng.shuffle(p_spec)
        p = hermitian_from_spectrum(rng, p_spec)

        q_spec = np.empty(n)
        if b:
            q_spec[:b] = 10.0 ** rng.uniform(-8.0, 8.0, size=b)
        if b < n:
            q_spec[b:] = -(10.0 ** rng.uniform(-8.0, 8.0, size=n - b))
        rng.shuffle(q_spec)
        q = hermitian_from_spectrum(rng, q_spec)

        gap = inequality_gap(p, q, c)
        min_gap = min(min_gap, gap)
        scale = 1.0 + np.linalg.norm(p + q, "fro") ** 2
        if gap < -2e-7 * scale:
            failures += 1

        # A deliberately aligned/cancelling case, where von Neumann is sharp.
        vals = np.sort(np.linalg.eigvalsh(p))[::-1]
        neg = np.zeros(n)
        k = min(r, n - b)
        if k:
            neg[:k] = -vals[:k] * rng.uniform(0.8, 1.2, size=k)
        if b:
            neg[-b:] = c * rng.uniform(0.2, 2.0, size=b)
        q_aligned = np.diag(neg)
        p_aligned = np.diag(vals)
        gap_aligned = inequality_gap(p_aligned, q_aligned, c)
        min_gap = min(min_gap, gap_aligned)
        scale_aligned = 1.0 + np.linalg.norm(p_aligned + q_aligned, "fro") ** 2
        if gap_aligned < -2e-7 * scale_aligned:
            failures += 1

    return Summary(
        trials=trials,
        dimension=n,
        minimum_gap=min_gap,
        equality_gap=equality_gap,
        failures=failures,
        seed=seed,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=2000)
    parser.add_argument("--dimension", type=int, default=18)
    parser.add_argument("--seed", type=int, default=20260810)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    if args.trials <= 0 or args.dimension < 5:
        raise SystemExit("trials must be positive and dimension at least 5")

    summary = run(args.trials, args.dimension, args.seed)
    payload = {
        "status": "PASS_ZETA23_RANK_TRACE" if summary.failures == 0 else "FAIL",
        **summary.__dict__,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")
    if summary.failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
