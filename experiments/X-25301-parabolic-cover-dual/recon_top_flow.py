#!/usr/bin/env python3
"""Floating sparse-LP reconnaissance for the signed parabolic carry flow.

Usage:
    python recon_top_flow.py X [support_fraction]

Arithmetic class: FLOATING_RECONNAISSANCE.
No output is a proof certificate.
"""

from __future__ import annotations

import math
import sys
from typing import Dict

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, vstack


def prime_sieve(limit: int) -> list[int]:
    flags = np.ones(limit + 1, dtype=bool)
    flags[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if flags[p]:
            flags[p * p : limit + 1 : p] = False
    return np.nonzero(flags)[0].tolist()


def prime_powers(limit: int) -> tuple[list[int], Dict[int, float]]:
    weights: Dict[int, float] = {}
    for p in prime_sieve(limit):
        q = p
        while q <= limit:
            weights[q] = math.log(p)
            if q > limit // p:
                break
            q *= p
    return sorted(weights), weights


def factor_prime_powers(value: int) -> list[int]:
    result: list[int] = []
    n = value
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        q = p
        for _ in range(exponent):
            result.append(q)
            q *= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def seed(limit: int) -> np.ndarray:
    values = np.zeros(limit + 2)
    for m in range(2, limit + 1):
        values[m] = 2 * math.sqrt(m) * (
            math.log(limit / m) - 2 * (1 - math.sqrt(m / limit))
        )
    return values


def constraint_value(values: np.ndarray, q: int, limit: int) -> float:
    return sum(
        values[k * q] - values[k * q + 1]
        for k in range(1, limit // q + 1)
    )


def main() -> None:
    if len(sys.argv) not in (2, 3):
        raise SystemExit("usage: python recon_top_flow.py X [support_fraction]")
    limit = int(sys.argv[1])
    support_fraction = float(sys.argv[2]) if len(sys.argv) == 3 else 0.45
    if limit < 100 or not (0 < support_fraction < 1):
        raise SystemExit("require X>=100 and 0<support_fraction<1")

    powers, _ = prime_powers(limit)
    power_index = {q: i for i, q in enumerate(powers)}
    base = seed(limit)
    target = np.asarray(
        [math.log(limit / q) / math.sqrt(q) for q in powers]
    )
    initial = np.asarray(
        [constraint_value(base, q, limit) for q in powers]
    )
    defect = initial - target

    first = max(2, math.ceil(support_fraction * limit))
    indices = np.arange(first, limit, dtype=int)
    n_vars = len(indices)

    constraint_matrix = lil_matrix((len(powers), n_vars))
    for column, j in enumerate(indices):
        for value, coefficient in ((j - 1, 1), (j, -2), (j + 1, 1)):
            if not (1 <= value <= limit):
                continue
            for q in factor_prime_powers(value):
                row = power_index.get(q)
                if row is not None:
                    constraint_matrix[row, column] += coefficient

    positivity_matrix = lil_matrix((n_vars, n_vars))
    positivity_rhs = np.zeros(n_vars)
    for row, m in enumerate(indices):
        positivity_matrix[row, row] = 1
        if m - 1 >= first:
            positivity_matrix[row, row - 1] = -1
        positivity_rhs[row] = base[m]

    matrix = vstack(
        [constraint_matrix.tocsr(), positivity_matrix.tocsr()]
    ).tocsr()
    rhs = np.concatenate([-defect, positivity_rhs])
    objective = np.asarray(
        [math.log(j * j / (j * j - 1)) for j in indices]
    )

    result = linprog(
        objective,
        A_ub=matrix,
        b_ub=rhs,
        bounds=(0, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    repaired = base.copy()
    flow = np.zeros(limit + 1)
    flow[indices] = result.x
    for m in range(2, limit + 1):
        repaired[m] += flow[m - 1] - flow[m]

    final_defect = max(
        constraint_value(repaired, q, limit)
        - math.log(limit / q) / math.sqrt(q)
        for q in powers
    )

    print("FLOATING_RECONNAISSANCE_ONLY")
    print(f"X={limit}")
    print(f"support_fraction={support_fraction}")
    print(f"objective_cost={result.fun:.17g}")
    print(f"scaled_X_3_over_2_cost={result.fun * limit**1.5:.17g}")
    print(f"active_variables={int(np.count_nonzero(result.x > 1e-10))}")
    print(f"flow_total={float(np.sum(result.x)):.17g}")
    print(f"maximum_flow={float(np.max(result.x)):.17g}")
    print(f"minimum_repaired_b={float(np.min(repaired[2:limit+1])):.17g}")
    print(f"maximum_constraint_defect={final_defect:.17g}")


if __name__ == "__main__":
    main()
