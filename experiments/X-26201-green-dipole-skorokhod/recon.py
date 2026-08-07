#!/usr/bin/env python3
"""Double-precision reconnaissance for the parabolic Green carry state.

Discovery only. This script is not an interval producer and must not be used
as a proof certificate.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np


def prime_powers(limit: int):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    roots = {}
    for p in np.nonzero(sieve)[0]:
        q = int(p)
        while q <= limit:
            roots[q] = int(p)
            q *= int(p)
    return sorted(roots), roots


def seed(X: int):
    b = np.zeros(X + 2, dtype=float)
    for m in range(2, X + 1):
        b[m] = 2.0 * math.sqrt(m) * (
            math.log(X / m) - 2.0 * (1.0 - math.sqrt(m / X))
        )
    return b


def coordinates(b, qs, X):
    out = np.empty(len(qs), dtype=float)
    for i, q in enumerate(qs):
        idx = np.arange(q, X + 1, q)
        out[i] = np.sum(b[idx] - b[idx + 1])
    return out


def objective(b, X):
    m = np.arange(2, X + 1, dtype=float)
    return float(np.dot(b[2 : X + 1], np.log(m / (m - 1.0))))


def one_level(X: int):
    qs, roots = prime_powers(X)
    qarr = np.asarray(qs, dtype=int)
    f = np.zeros((len(qs), X + 1), dtype=float)
    for i, q in enumerate(qs):
        j = np.arange(1, X + 1)
        f[i, 1:] = (j % q == 0).astype(float)
        if X % q == 0:
            f[i, 1:] -= j / X
    grad = np.diff(f, axis=1)
    G = grad @ grad.T

    b0 = seed(X)
    w = np.log(X / qarr) / np.sqrt(qarr)
    v0 = coordinates(b0, qs, X)
    r = v0 - w
    T = np.linalg.solve(G, r)
    F = T @ f
    bstar = b0.copy()
    bstar[2 : X + 1] += F[1:X] - F[2 : X + 1]
    equality_radius = float(np.max(np.abs(coordinates(bstar, qs, X) - w)))

    obstacle = np.maximum(-bstar, 0.0)
    bclip = bstar + obstacle
    eps = coordinates(bclip, qs, X) - w
    lambdas = np.log(np.array([roots[q] for q in qs], dtype=float))
    Dplus = float(lambdas @ np.maximum(eps, 0.0))
    Dminus = float(lambdas @ np.maximum(-eps, 0.0))
    P = float(lambdas @ w)
    Jclip = objective(bclip, X)
    Lclip = Jclip - Dplus
    Uclip = Jclip + Dminus
    J0 = objective(b0, X)

    sigma = np.zeros(X + 2)
    for m in range(2, X + 1):
        sigma[m] = max(sigma[m - 1], obstacle[m])
    lam = sigma[2 : X + 1] - sigma[1:X]
    contact_indices = np.nonzero(lam > 1e-13)[0] + 2
    prefix_debt = 0.0
    for j, amount in zip(contact_indices, lam[contact_indices - 2]):
        prefix_debt += amount * math.log((j - 1) / math.gcd(X, int(j - 1)))

    negative = np.nonzero(bstar[2 : X + 1] < -1e-13)[0] + 2
    return {
        "X": X,
        "green_rank": len(qs),
        "equality_radius": equality_radius,
        "negative_count": int(len(negative)),
        "negative_first": int(negative[0]) if len(negative) else None,
        "negative_last": int(negative[-1]) if len(negative) else None,
        "minimum_green_coordinate": float(np.min(bstar[2 : X + 1])),
        "clipped_D_plus": Dplus,
        "clipped_D_minus": Dminus,
        "clipped_total_gap": Dplus + Dminus,
        "clipped_lower_minus_seed": Lclip - J0,
        "clipped_upper_minus_prime_ramp": Uclip - P,
        "prefix_contact_count": int(len(contact_indices)),
        "prefix_contact_debt": prefix_debt,
        "maximum_negative_depth": float(np.max(obstacle)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--levels",
        default="50,100,200,500,1000,2000,5000,10000,20000",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    levels = [int(x) for x in args.levels.split(",") if x]
    result = {
        "classification": "FLOAT64_RECONNAISSANCE_ONLY",
        "numpy_version": np.__version__,
        "python_version": platform.python_version(),
        "proof_boundary": (
            "The Green solves and signs are ordinary binary64 computations. "
            "They nominate the GDS theorem but do not certify a finite level, "
            "a cofinal bound, the prime-ramp asymptotic, or RH."
        ),
        "levels": [one_level(X) for X in levels],
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
