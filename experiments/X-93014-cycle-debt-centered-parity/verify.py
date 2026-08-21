#!/usr/bin/env python3
"""Exact finite replay for L-93014.

Arithmetic:
- fractions.Fraction for rational LP fixtures;
- Q(sqrt(2)) for the critical dyadic source pairing;
- integer/formal-radical coefficient checks for doubled carry capacities.

This script does not prove the cofinal CDP bound or RH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class Q2:
    """a + b*sqrt(2), exactly."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Q2":
        o = q2(other)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: object) -> "Q2":
        return self + (-q2(other))

    def __rsub__(self, other: object) -> "Q2":
        return q2(other) - self

    def __mul__(self, other: object) -> "Q2":
        o = q2(other)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Q2":
        o = q2(other)
        den = o.a * o.a - 2 * o.b * o.b
        if den == 0:
            raise ZeroDivisionError
        return Q2((self.a * o.a - 2 * self.b * o.b) / den,
                  (self.b * o.a - self.a * o.b) / den)

    def __eq__(self, other: object) -> bool:
        try:
            o = q2(other)
        except TypeError:
            return False
        return self.a == o.a and self.b == o.b

    def as_json(self) -> List[str]:
        return [str(self.a), str(self.b)]


def q2(x: object) -> Q2:
    if isinstance(x, Q2):
        return x
    if isinstance(x, Fraction):
        return Q2(x, Fraction(0))
    if isinstance(x, int):
        return Q2(Fraction(x), Fraction(0))
    raise TypeError(type(x))


SQRT2 = Q2(Fraction(0), Fraction(1))
ALPHA = SQRT2 / 2  # 1/sqrt(2)


def mobius_sieve(n: int) -> List[int]:
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    primes: List[int] = []
    mu[0] = 0
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def divergence_from_target(w: Sequence[Q2]) -> List[Q2]:
    """w[q], q>=2. Return r[1..X] with size conservation."""
    X = len(w) - 1
    mu = mobius_sieve(X)
    u = [Q2() for _ in range(X + 2)]
    for m in range(2, X + 1):
        total = Q2()
        for k in range(1, X // m + 1):
            total += mu[k] * w[m * k]
        u[m] = total
    r = [Q2() for _ in range(X + 1)]
    for m in range(2, X + 1):
        r[m] = u[m] - u[m + 1]
    r[1] = -sum((m * r[m] for m in range(2, X + 1)), Q2())
    return r


def dot_q2(x: Sequence[Q2], y: Sequence[Q2]) -> Q2:
    assert len(x) == len(y)
    return sum((x[i] * y[i] for i in range(1, len(x))), Q2())


def allowed_splits(X: int) -> List[Tuple[int, int, int]]:
    return [(n, j, n - j) for n in range(2, X + 1) for j in range(1, n // 2 + 1)]


def delta(v: Sequence[Fraction], e: Tuple[int, int, int]) -> Fraction:
    n, j, k = e
    return v[n] - v[j] - v[k]


def source_from_flow(X: int, flows: Dict[Tuple[int, int, int], Fraction]) -> List[Fraction]:
    r = [Fraction(0) for _ in range(X + 1)]
    for (n, j, k), d in flows.items():
        r[n] += d
        r[j] -= d
        r[k] -= d
    return r


def dot_frac(x: Sequence[Fraction], y: Sequence[Fraction]) -> Fraction:
    return sum((x[i] * y[i] for i in range(1, len(x))), Fraction(0))


def solve_square(A: List[List[Fraction]], b: List[Fraction]) -> List[Fraction] | None:
    n = len(A)
    aug = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [z / p for z in aug[col]]
        for r in range(n):
            if r == col:
                continue
            c = aug[r][col]
            if c:
                aug[r] = [aug[r][j] - c * aug[col][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def dual_vertices(X: int, omega: Dict[Tuple[int, int, int], Fraction], centered: bool) -> List[List[Fraction]]:
    """Enumerate vertices in variables v[2..X], with v[1]=0."""
    edges = allowed_splits(X)
    dim = X - 1
    inequalities: List[Tuple[List[Fraction], Fraction]] = []
    # a dot x <= b
    for e in edges:
        n, j, k = e
        row = [Fraction(0) for _ in range(dim)]
        for idx, coeff in ((n, 1), (j, -1), (k, -1)):
            if idx >= 2:
                row[idx - 2] += coeff
        if centered:
            inequalities.append((row, omega[e] / 2))
            inequalities.append(([-z for z in row], omega[e] / 2))
        else:
            inequalities.append((row, omega[e]))
            inequalities.append(([-z for z in row], Fraction(0)))
    out: List[List[Fraction]] = []
    for active in combinations(range(len(inequalities)), dim):
        A = [inequalities[i][0] for i in active]
        b = [inequalities[i][1] for i in active]
        x = solve_square(A, b)
        if x is None:
            continue
        if all(sum(a * z for a, z in zip(row, x)) <= rhs for row, rhs in inequalities):
            v = [Fraction(0), Fraction(0)] + x
            if v not in out:
                out.append(v)
    # zero is feasible, and can be the sole point in degenerate fixtures
    zero = [Fraction(0) for _ in range(X + 1)]
    if zero not in out:
        out.append(zero)
    return out


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def run() -> dict:
    rng = random.Random(93014)
    centered_fixture_checks = 0
    centered_vertex_checks = 0
    variation_checks = 0
    dyadic_pair_checks = 0
    trace_gauge_checks = 0
    carry_split_checks = 0
    mutations_detected = 0

    # Centering and exact optimum identity on small rational LPs.
    for X in range(3, 7):
        edges = allowed_splits(X)
        # G(n)=n^2 gives omega=2jk >0.
        G = [Fraction(n * n) for n in range(X + 1)]
        G[1] = Fraction(1)
        # Gauge to G(1)=0 without changing defects: subtract n.
        G = [G[n] - n for n in range(X + 1)]
        omega = {e: delta(G, e) for e in edges}
        assert all(v > 0 for v in omega.values())

        asym = dual_vertices(X, omega, centered=False)
        cent = dual_vertices(X, omega, centered=True)
        for _ in range(12):
            flows = {e: Fraction(rng.randint(-3, 3), rng.randint(1, 5)) for e in edges}
            r = source_from_flow(X, flows)
            K = dot_frac(r, G)
            max_asym = max(-dot_frac(r, F) for F in asym)
            max_cent = max(abs(dot_frac(r, H)) for H in cent)
            assert max_asym + K / 2 == max_cent
            centered_vertex_checks += 1

            # Flow identity |d| = d + 2 d_- after capacity pairing.
            signed_capacity = sum((flows[e] * omega[e] for e in edges), Fraction(0))
            negative = sum((omega[e] * max(-flows[e], Fraction(0)) for e in edges), Fraction(0))
            variation = sum((omega[e] * abs(flows[e]) for e in edges), Fraction(0))
            assert signed_capacity == K
            assert variation == K + 2 * negative
            variation_checks += 1

            # Sample centered H=tG and map to F=H+G/2.
            t = Fraction(rng.randint(-4, 4), 10)
            H = [t * z for z in G]
            F = [H[n] + G[n] / 2 for n in range(X + 1)]
            assert all(abs(delta(H, e)) <= omega[e] / 2 for e in edges)
            assert all(0 <= delta(F, e) <= omega[e] for e in edges)
            assert -dot_frac(r, F) + K / 2 == -dot_frac(r, H)
            centered_fixture_checks += 1

    # Exact Q(sqrt(2)) dyadic source and pairing identity.
    for Y in range(3, 15):
        X = 2 * Y
        for _ in range(16):
            wY = [Q2() for _ in range(Y + 1)]
            for q in range(2, Y + 1):
                wY[q] = Q2(Fraction(rng.randint(-4, 7), rng.randint(1, 7)))
            wX = [Q2() for _ in range(X + 1)]
            for q in range(2, Y + 1):
                wX[2 * q] = ALPHA * wY[q]
            # Bottom q=2 is not set by q>=2 scaling; choose it independently.
            wX[2] = Q2(Fraction(rng.randint(-3, 5), rng.randint(1, 6)),
                        Fraction(rng.randint(-2, 2), rng.randint(1, 7)))
            for q in range(3, X + 1, 2):
                wX[q] = Q2(Fraction(rng.randint(-4, 4), rng.randint(1, 8)),
                            Fraction(rng.randint(-2, 2), rng.randint(1, 9)))
            rY = divergence_from_target(wY)
            rX = divergence_from_target(wX)

            H = [Q2() for _ in range(X + 1)]
            for n in range(2, X + 1):
                H[n] = Q2(Fraction(rng.randint(-5, 5), rng.randint(1, 9)),
                           Fraction(rng.randint(-3, 3), rng.randint(1, 10)))

            Rtrace = [Q2() for _ in range(Y + 1)]
            for m in range(1, Y + 1):
                Rtrace[m] = SQRT2 * (H[2 * m] - m * H[2])
            assert Rtrace[1] == Q2()
            trace_gauge_checks += 1

            odd = sum((rX[2 * a + 1] * (H[2 * a + 1] - H[2 * a])
                       for a in range(1, Y)), Q2())
            lhs = dot_q2(rX, H)
            rhs = dot_q2(rY, Rtrace) / 2 + wX[2] * H[2] + odd
            assert lhs == rhs
            dyadic_pair_checks += 1

            # Hostile mutations: wrong half-scale factor or reversed odd sign.
            wrong_trace = [Q2() for _ in range(Y + 1)]
            for m in range(1, Y + 1):
                wrong_trace[m] = H[2 * m] - m * H[2]
            if dot_q2(rY, wrong_trace) / 2 + wX[2] * H[2] + odd != lhs:
                mutations_detected += 1
            if dot_q2(rY, Rtrace) / 2 + wX[2] * H[2] - odd != lhs:
                mutations_detected += 1

    # Formal carry-column decomposition: even columns + odd leakage.
    for n in range(2, 65):
        for j in range(1, n // 2 + 1):
            for q in range(2, n + 1):
                assert carry(2 * n, 2 * j, 2 * q) == carry(n, j, q)
                carry_split_checks += 1
            # No even column is lost and odd columns are disjoint by parity.
            even_support = {2 * q for q in range(2, n + 1) if carry(n, j, q)}
            doubled_even_support = {q for q in range(4, 2 * n + 1, 2) if carry(2 * n, 2 * j, q)}
            assert even_support == doubled_even_support
            carry_split_checks += 1

    return {
        "classification": "PASS_X_93014_CYCLE_DEBT_CENTERED_PARITY",
        "arithmetic_class": "EXACT_RATIONAL_AND_Q_SQRT2_WITH_FORMAL_RADICAL_SUPPORT",
        "centered_fixture_checks": centered_fixture_checks,
        "centered_vertex_optimum_checks": centered_vertex_checks,
        "weighted_variation_checks": variation_checks,
        "dyadic_pairing_checks": dyadic_pair_checks,
        "even_trace_gauge_checks": trace_gauge_checks,
        "formal_doubled_carry_checks": carry_split_checks,
        "hostile_mutations_detected": mutations_detected,
        "proves": [
            "finite centered/asymmetric dual equivalence on exact fixtures",
            "weighted variation identity",
            "gauge-corrected dyadic source pairing",
            "formal even-column capacity decomposition",
        ],
        "does_not_prove": [
            "the cofinal centered dyadic parity bound",
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
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
