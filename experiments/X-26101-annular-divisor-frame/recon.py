#!/usr/bin/env python3
"""Floating reconnaissance for the slack-anchored annular frame.

Usage:
    python recon.py X [alpha] [beta]

Arithmetic class: FLOATING_RECONNAISSANCE.
No output is a proof certificate.
"""

from __future__ import annotations

import math
import sys
from collections import defaultdict

import numpy as np


def primes(limit: int) -> list[int]:
    flags = np.ones(limit + 1, dtype=bool)
    flags[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if flags[p]:
            flags[p * p : limit + 1 : p] = False
    return np.nonzero(flags)[0].tolist()


def prime_powers(limit: int) -> list[int]:
    out: set[int] = set()
    for p in primes(limit):
        q = p
        while q <= limit:
            out.add(q)
            if q > limit // p:
                break
            q *= p
    return sorted(out)


def seed(limit: int) -> np.ndarray:
    b = np.zeros(limit + 2)
    for m in range(2, limit + 1):
        b[m] = 2 * math.sqrt(m) * (
            math.log(limit / m) - 2 * (1 - math.sqrt(m / limit))
        )
    return b


def constraint(values: np.ndarray, q: int, limit: int) -> float:
    return sum(
        values[k * q] - values[k * q + 1]
        for k in range(1, limit // q + 1)
    )


def row(q: int, indices: np.ndarray) -> np.ndarray:
    return (
        2 * (indices % q == 0)
        - ((indices - 1) % q == 0)
        - ((indices + 1) % q == 0)
    ).astype(float)


def compress_active(matrix: np.ndarray, active: np.ndarray, residual: np.ndarray):
    groups: dict[bytes, list[int]] = defaultdict(list)
    signed = matrix.astype(np.int8, copy=False)
    for i in active:
        groups[signed[i].tobytes()].append(int(i))
    representatives: list[int] = []
    for members in groups.values():
        representatives.append(max(members, key=lambda i: residual[i]))
    return np.asarray(representatives, dtype=int)


def main() -> None:
    if len(sys.argv) not in (2, 3, 4):
        raise SystemExit("usage: python recon.py X [alpha] [beta]")
    limit = int(sys.argv[1])
    alpha = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.45
    beta = float(sys.argv[3]) if len(sys.argv) >= 4 else 0.80
    if limit < 100 or not (0 < alpha < beta < 1):
        raise SystemExit("require X>=100 and 0<alpha<beta<1")

    powers = prime_powers(limit)
    indices = np.arange(math.ceil(alpha * limit), math.floor(beta * limit) + 1)
    matrix = np.vstack([row(q, indices) for q in powers])
    base = seed(limit)
    target = np.asarray(
        [math.log(limit / q) / math.sqrt(q) for q in powers]
    )
    residual = np.asarray(
        [constraint(base, q, limit) for q in powers]
    ) - target
    initial_positive = np.maximum(residual, 0)
    flow = np.zeros(len(indices))
    eta = 0.5
    tolerance = 1e-10
    min_frame = math.inf
    iterations = 0

    for iterations in range(1, 401):
        active = np.flatnonzero(residual > tolerance)
        if active.size == 0:
            break
        reps = compress_active(matrix, active, residual)
        active_matrix = matrix[reps]
        active_residual = residual[reps]
        gram = active_matrix @ active_matrix.T
        eig = np.linalg.eigvalsh(gram)
        positive_eig = eig[eig > 1e-10]
        if positive_eig.size == 0:
            raise RuntimeError("active Gram has no positive eigenvalue")
        min_frame = min(min_frame, float(positive_eig[0]))
        dual = np.linalg.lstsq(gram, active_residual, rcond=1e-12)[0]
        increment = active_matrix.T @ dual
        flow += eta * increment
        residual -= eta * (matrix @ increment)
    else:
        raise RuntimeError("active projection did not converge")

    repaired = base.copy()
    full_flow = np.zeros(limit + 1)
    full_flow[indices] = flow
    for m in range(2, limit + 1):
        repaired[m] += full_flow[m - 1] - full_flow[m]

    final_defect = max(
        constraint(repaired, q, limit)
        - math.log(limit / q) / math.sqrt(q)
        for q in powers
    )
    cost = sum(
        full_flow[j] * math.log(j * j / (j * j - 1))
        for j in indices
    )
    initial_active = np.flatnonzero(initial_positive > tolerance)
    initial_gram = matrix[initial_active] @ matrix[initial_active].T
    initial_floor = (
        float(np.linalg.eigvalsh(initial_gram)[0])
        if initial_active.size else math.inf
    )

    top = sorted(
        (
            (abs(float(value)), int(j), float(value))
            for j, value in zip(indices, flow)
            if abs(value) > 1e-10
        ),
        reverse=True,
    )[:12]

    print("FLOATING_RECONNAISSANCE_ONLY")
    print(f"X={limit} alpha={alpha} beta={beta}")
    print(f"prime_power_rows={len(powers)}")
    print(f"initial_positive_rows={initial_active.size}")
    print(f"initial_positive_l2={np.linalg.norm(initial_positive):.17g}")
    print(f"initial_frame_floor={initial_floor:.17g}")
    print(f"iterations={iterations}")
    print(f"minimum_generated_frame_floor={min_frame:.17g}")
    print(f"flow_l2={np.linalg.norm(flow):.17g}")
    print(f"flow_linf={np.max(np.abs(flow)):.17g}")
    print(f"objective_cost={cost:.17g}")
    print(f"minimum_repaired_b={np.min(repaired[2:limit+1]):.17g}")
    print(f"maximum_final_constraint_defect={final_defect:.17g}")
    print("largest_flow_coordinates=" + repr(top))


if __name__ == "__main__":
    main()
