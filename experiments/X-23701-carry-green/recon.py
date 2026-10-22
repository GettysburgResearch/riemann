#!/usr/bin/env python3
"""Floating reconnaissance for the four-band carry phase frame.

Usage: python recon.py X H

Arithmetic class: FLOATING_RECONNAISSANCE.
No output of this script is a proof certificate.
"""

from __future__ import annotations

import math
import sys

import numpy as np
from scipy.optimize import linprog


def mobius_sieve(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    mu[0] = 0
    least = np.zeros(n + 1, dtype=np.int32)
    primes: list[int] = []
    for i in range(2, n + 1):
        if least[i] == 0:
            least[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if p > least[i] or i * p > n:
                break
            least[i * p] = p
            mu[i * p] = 0 if p == least[i] else -mu[i]
    return mu


def beta_vector(n: int) -> np.ndarray:
    q = np.arange(2, n + 1, dtype=np.int64)
    return (n // q) * (q - 1 - (n % q)) / (n + 1)


def outer_inverse(T: int, mu: np.ndarray) -> np.ndarray:
    u = np.zeros(T + 3)
    for m in range(2, T + 1):
        u[m] = sum(
            int(mu[k]) / math.sqrt(m * k) * math.log(T / (m * k))
            for k in range(1, T // m + 1)
            if mu[k]
        )
    tail = np.zeros(T + 4)
    for m in range(T, 1, -1):
        tail[m] = tail[m + 1] + u[m]
    c = np.zeros(T + 2)
    for m in range(2, T + 1):
        s_m = (m * u[m] + tail[m + 1]) / (m * (m - 1))
        s_next = (
            ((m + 1) * u[m + 1] + tail[m + 2]) / ((m + 1) * m)
            if m < T
            else 0.0
        )
        c[m] = (m + 1) * (s_m - s_next)
    return c


def average_binomial_logs(X: int) -> np.ndarray:
    G = np.zeros(X + 1)
    F = 0.0
    for n in range(2, X + 1):
        F += (n - 1) * math.log(n) - math.lgamma(n)
        G[n] = F / (n + 1)
    return G


def von_mangoldt(X: int) -> np.ndarray:
    out = np.zeros(X + 1)
    sieve = np.ones(X + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, X + 1):
        if not sieve[p]:
            continue
        if p * p <= X:
            sieve[p * p : X + 1 : p] = False
        q = p
        while q <= X:
            out[q] = math.log(p)
            q *= p
    return out


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: python recon.py X H")
    X = int(sys.argv[1])
    H = int(sys.argv[2])
    if X < 10 or H < 1:
        raise SystemExit("require X>=10 and H>=1")

    mu = mobius_sieve(X)
    G = average_binomial_logs(X)
    step = math.log(5) / H

    endpoints: list[int] = []
    j = 0
    while True:
        T = int(math.floor(X * math.exp(-j * step)))
        if T < 2:
            break
        if not endpoints or endpoints[-1] != T:
            endpoints.append(T)
        j += 1

    columns: list[np.ndarray] = []
    scores: list[float] = []
    labels: list[tuple[int, int]] = []

    for T in endpoints:
        c = outer_inverse(T, mu)
        for r in range(1, 5):
            lo = max(2, T // (r + 1) + 1)
            hi = T // r
            if lo > hi:
                continue
            n_values = np.arange(lo, hi + 1, dtype=np.int64)
            coeffs = c[n_values]
            if np.min(coeffs, initial=0.0) < -1e-10:
                raise RuntimeError(f"outer negativity at T={T}, r={r}")
            coeffs = np.maximum(coeffs, 0.0)
            column = np.zeros(X - 1)
            for n, value in zip(n_values, coeffs):
                if value:
                    column[: n - 1] += value * beta_vector(int(n))
            columns.append(column)
            scores.append(float(np.dot(coeffs, G[n_values])))
            labels.append((T, r))

    A = np.column_stack(columns)
    objective = np.asarray(scores)
    target = np.asarray(
        [math.log(X / q) / math.sqrt(q) for q in range(2, X + 1)]
    )

    keep = np.any(A > 1e-16, axis=0) & (objective > 1e-16)
    A = A[:, keep]
    objective = objective[keep]
    labels = [label for label, flag in zip(labels, keep) if flag]

    result = linprog(
        -objective,
        A_ub=A,
        b_ub=target,
        bounds=(0, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    lamb = von_mangoldt(X)
    finite_ramp = sum(lamb[q] * target[q - 2] for q in range(2, X + 1))
    value = -float(result.fun)
    slack = target - A @ result.x

    print("FLOATING_RECONNAISSANCE_ONLY")
    print(f"X={X} H={H} endpoints={len(endpoints)} atoms={A.shape[1]}")
    print(f"objective={value:.15g}")
    print(f"finite_prime_ramp={finite_ramp:.15g}")
    print(f"ratio={value / finite_ramp:.15g}")
    print(f"gap={finite_ramp - value:.15g}")
    print(f"minimum_solver_slack={float(np.min(slack)):.15g}")
    print(f"active_atoms={int(np.sum(result.x > 1e-9))}")
    active = sorted(
        (
            (float(weight), label)
            for weight, label in zip(result.x, labels)
            if weight > 1e-7
        ),
        reverse=True,
    )
    print("largest_weights=" + repr(active[:12]))


if __name__ == "__main__":
    main()
