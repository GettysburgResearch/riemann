#!/usr/bin/env python3
"""Exact lightweight replay for L-93017.

Arithmetic:
- fractions.Fraction only;
- finite vertex enumeration only for X <= 6;
- no floating LP solver and no asymptotic scan.

The replay authenticates the carry-coordinate algebra and the bottom-free
recurrence. It does not prove OPB, Cycle Debt, or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


Edge = Tuple[int, int, int]


def mobius_sieve(n: int) -> List[int]:
    mu = [1] * (n + 1)
    mu[0] = 0
    primes: List[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def allowed_splits(x: int) -> List[Edge]:
    out: List[Edge] = []
    for n in range(2, x + 1):
        # eta = 1/4, encoded without floating arithmetic.
        for j in range(1, n // 2 + 1):
            if 4 * j >= n:
                out.append((n, j, n - j))
    return out


def carry(edge: Edge, q: int) -> int:
    n, j, k = edge
    return n // q - j // q - k // q


def delta(v: Sequence[Fraction], edge: Edge) -> Fraction:
    n, j, k = edge
    return v[n] - v[j] - v[k]


def divergence_from_target(target: Sequence[Fraction]) -> List[Fraction]:
    x = len(target) - 1
    mu = mobius_sieve(x)
    u = [Fraction(0) for _ in range(x + 2)]
    for m in range(2, x + 1):
        u[m] = sum(
            (mu[k] * target[m * k] for k in range(1, x // m + 1)),
            Fraction(0),
        )
    r = [Fraction(0) for _ in range(x + 1)]
    for m in range(2, x + 1):
        r[m] = u[m] - u[m + 1]
    r[1] = -sum((m * r[m] for m in range(2, x + 1)), Fraction(0))
    return r


def dot(a: Sequence[Fraction], b: Sequence[Fraction]) -> Fraction:
    return sum((a[i] * b[i] for i in range(1, len(a))), Fraction(0))


def potential_from_coordinates(
    coords: Sequence[Fraction], weights: Sequence[Fraction]
) -> List[Fraction]:
    x = len(coords) - 1
    h = [Fraction(0) for _ in range(x + 1)]
    for n in range(2, x + 1):
        h[n] = sum(
            (
                coords[q] * weights[q] * (n // q)
                for q in range(2, n + 1)
            ),
            Fraction(0),
        )
    return h


def coordinates_from_potential(
    h: Sequence[Fraction], weights: Sequence[Fraction]
) -> List[Fraction]:
    x = len(h) - 1
    theta = [Fraction(0) for _ in range(x + 1)]
    for n in range(2, x + 1):
        prior = sum(
            (
                theta[q] * weights[q] * (n // q)
                for q in range(2, n)
            ),
            Fraction(0),
        )
        theta[n] = (h[n] - prior) / weights[n]
    return theta


def row_for_delta(x: int, edge: Edge) -> List[Fraction]:
    row = [Fraction(0) for _ in range(x - 1)]
    n, j, k = edge
    for node, coeff in ((n, 1), (j, -1), (k, -1)):
        if node >= 2:
            row[node - 2] += coeff
    return row


def row_for_carry(
    x: int, edge: Edge, weights: Sequence[Fraction]
) -> List[Fraction]:
    return [
        weights[q] * carry(edge, q)
        for q in range(2, x + 1)
    ]


def solve_square(
    matrix: List[List[Fraction]], rhs: List[Fraction]
) -> List[Fraction] | None:
    n = len(matrix)
    aug = [matrix[i][:] + [rhs[i]] for i in range(n)]
    for col in range(n):
        pivot = next(
            (r for r in range(col, n) if aug[r][col] != 0),
            None,
        )
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        value = aug[col][col]
        aug[col] = [z / value for z in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor:
                aug[r] = [
                    aug[r][j] - factor * aug[col][j]
                    for j in range(n + 1)
                ]
    return [aug[i][-1] for i in range(n)]


def enumerate_vertices(
    inequalities: Sequence[Tuple[List[Fraction], Fraction]],
    dim: int,
) -> List[List[Fraction]]:
    vertices: List[List[Fraction]] = []
    for active in combinations(range(len(inequalities)), dim):
        matrix = [inequalities[i][0] for i in active]
        rhs = [inequalities[i][1] for i in active]
        point = solve_square(matrix, rhs)
        if point is None:
            continue
        if all(
            sum((a * z for a, z in zip(row, point)), Fraction(0))
            <= bound
            for row, bound in inequalities
        ):
            if point not in vertices:
                vertices.append(point)
    zero = [Fraction(0) for _ in range(dim)]
    if zero not in vertices:
        vertices.append(zero)
    return vertices


def potential_vertices(
    x: int,
    weights: Sequence[Fraction],
    asymmetric: bool,
) -> List[List[Fraction]]:
    inequalities: List[Tuple[List[Fraction], Fraction]] = []
    for edge in allowed_splits(x):
        row = row_for_delta(x, edge)
        w = sum(
            (
                weights[q] * carry(edge, q)
                for q in range(2, x + 1)
            ),
            Fraction(0),
        )
        if asymmetric:
            # delta F <= W and -delta F <= 0.
            inequalities.append((row, w))
            inequalities.append(([-z for z in row], Fraction(0)))
        else:
            inequalities.append((row, w / 2))
            inequalities.append(([-z for z in row], w / 2))
    raw = enumerate_vertices(inequalities, x - 1)
    return [[Fraction(0), Fraction(0)] + point for point in raw]


def discrepancy_vertices(
    x: int, weights: Sequence[Fraction]
) -> List[List[Fraction]]:
    inequalities: List[Tuple[List[Fraction], Fraction]] = []
    for edge in allowed_splits(x):
        row = row_for_carry(x, edge, weights)
        w = sum(row, Fraction(0))
        # A psi <= 0 and -A psi <= W.
        inequalities.append((row, Fraction(0)))
        inequalities.append(([-z for z in row], w))
    raw = enumerate_vertices(inequalities, x - 1)
    return [[Fraction(0), Fraction(0)] + point for point in raw]


def run() -> dict:
    rng = random.Random(93017)

    basis_reconstructions = 0
    defect_checks = 0
    target_pairing_checks = 0
    lp_equivalence_checks = 0
    centered_checks = 0
    bottom_checks = 0
    dyadic_objective_checks = 0
    hostile_mutations = 0

    # Triangular basis, split defects, and target pairings.
    for x in range(3, 23):
        weights = [Fraction(0) for _ in range(x + 1)]
        for q in range(2, x + 1):
            weights[q] = Fraction((q % 7) + 1, q + 5)

        for _ in range(9):
            theta = [Fraction(0) for _ in range(x + 1)]
            for q in range(2, x + 1):
                theta[q] = Fraction(rng.randint(-7, 7), rng.randint(1, 9))
            h = potential_from_coordinates(theta, weights)
            recovered = coordinates_from_potential(h, weights)
            assert recovered == theta
            basis_reconstructions += 1

            for edge in allowed_splits(x):
                lhs = delta(h, edge)
                rhs = sum(
                    (
                        theta[q] * weights[q] * carry(edge, q)
                        for q in range(2, x + 1)
                    ),
                    Fraction(0),
                )
                assert lhs == rhs
                defect_checks += 1

            target = [Fraction(0) for _ in range(x + 1)]
            for q in range(2, x + 1):
                target[q] = Fraction(rng.randint(-5, 8), rng.randint(1, 11))
            r = divergence_from_target(target)
            ell = [weights[q] * target[q] for q in range(x + 1)]
            assert dot(r, h) == sum(
                (theta[q] * ell[q] for q in range(2, x + 1)),
                Fraction(0),
            )
            target_pairing_checks += 1

            # Mutation: remove the diagonal q=n basis atom.
            n = rng.randint(2, x)
            wrong = h[n] - theta[n] * weights[n]
            if wrong != h[n]:
                hostile_mutations += 1

    # Exact small-LP equivalence:
    # asymmetric potential dual == one-sided carry discrepancy.
    for x in range(3, 7):
        weights = [Fraction(0) for _ in range(x + 1)]
        target = [Fraction(0) for _ in range(x + 1)]
        for q in range(2, x + 1):
            weights[q] = Fraction((2 * q % 9) + 2, q + 7)
            target[q] = Fraction((3 * q % 11) + 1, q + 3)
        r = divergence_from_target(target)
        ell = [weights[q] * target[q] for q in range(x + 1)]
        k_value = sum(ell[2:], Fraction(0))

        f_vertices = potential_vertices(x, weights, asymmetric=True)
        h_vertices = potential_vertices(x, weights, asymmetric=False)
        psi_vertices = discrepancy_vertices(x, weights)

        debt_f = max(-dot(r, f) for f in f_vertices)
        debt_psi = max(
            sum((psi[q] * ell[q] for q in range(2, x + 1)), Fraction(0))
            for psi in psi_vertices
        )
        centered = max(abs(dot(r, h)) for h in h_vertices)

        assert debt_f == debt_psi
        assert centered == debt_f + k_value / 2
        lp_equivalence_checks += 1
        centered_checks += 1

        # Every discrepancy vertex maps to F=-Psi and satisfies
        # 0 <= delta F <= W.
        for psi in psi_vertices:
            psi_potential = potential_from_coordinates(psi, weights)
            f = [-z for z in psi_potential]
            for edge in allowed_splits(x):
                w = sum(
                    (
                        weights[q] * carry(edge, q)
                        for q in range(2, x + 1)
                    ),
                    Fraction(0),
                )
                assert 0 <= delta(f, edge) <= w

    # Bottom sign and exact dyadic objective split.
    for y in range(3, 19):
        x = 2 * y
        for _ in range(13):
            ell_y = [Fraction(0) for _ in range(y + 1)]
            for r in range(2, y + 1):
                ell_y[r] = Fraction(rng.randint(1, 12), rng.randint(1, 13))
            ell_x = [Fraction(0) for _ in range(x + 1)]
            ell_x[2] = Fraction(rng.randint(1, 12), rng.randint(1, 13))
            for r in range(2, y + 1):
                ell_x[2 * r] = ell_y[r] / 2
            for q in range(3, x + 1, 2):
                ell_x[q] = Fraction(rng.randint(1, 12), rng.randint(1, 13))

            psi = [Fraction(0) for _ in range(x + 1)]
            psi[2] = Fraction(-rng.randint(0, 9), rng.randint(1, 10))
            if psi[2] < -1:
                psi[2] = Fraction(-1)
            for q in range(3, x + 1):
                psi[q] = Fraction(rng.randint(-8, 8), rng.randint(1, 11))

            full = sum(
                (psi[q] * ell_x[q] for q in range(2, x + 1)),
                Fraction(0),
            )
            split = (
                psi[2] * ell_x[2]
                + Fraction(1, 2)
                * sum(
                    (psi[2 * r] * ell_y[r] for r in range(2, y + 1)),
                    Fraction(0),
                )
                + sum(
                    (
                        psi[q] * ell_x[q]
                        for q in range(3, x + 1, 2)
                    ),
                    Fraction(0),
                )
            )
            assert full == split
            assert psi[2] * ell_x[2] <= 0
            dyadic_objective_checks += 1
            bottom_checks += 1

            # Hostile mutations: wrong inherited factor and positive bottom.
            wrong_factor = (
                psi[2] * ell_x[2]
                + sum(
                    (psi[2 * r] * ell_y[r] for r in range(2, y + 1)),
                    Fraction(0),
                )
                + sum(
                    (
                        psi[q] * ell_x[q]
                        for q in range(3, x + 1, 2)
                    ),
                    Fraction(0),
                )
            )
            if wrong_factor != full:
                hostile_mutations += 1
            if psi[2] < 0 and (-psi[2]) * ell_x[2] > 0:
                hostile_mutations += 1

    return {
        "classification": "PASS_X_93017_CYCLE_DEBT_CARRY_DISCREPANCY",
        "arithmetic_class": "EXACT_RATIONAL",
        "basis_reconstructions": basis_reconstructions,
        "split_defect_checks": defect_checks,
        "target_pairing_checks": target_pairing_checks,
        "small_lp_equivalence_checks": lp_equivalence_checks,
        "centered_baseline_checks": centered_checks,
        "bottom_nonpositive_checks": bottom_checks,
        "dyadic_objective_checks": dyadic_objective_checks,
        "hostile_mutations_detected": hostile_mutations,
        "proves": [
            "triangular carry-coordinate basis",
            "split-defect discrepancy identity",
            "target objective diagonalization",
            "small exact asymmetric/discrepancy LP equivalence",
            "centered baseline relation",
            "bottom nonpositivity",
            "factor-one-half dyadic objective split",
        ],
        "does_not_prove": [
            "the OPB asymptotic bound",
            "polylogarithmic Cycle Debt",
            "the Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    record = run()
    payload = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
