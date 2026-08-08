#!/usr/bin/env python3
"""Exact regression for Pascal-cycle generation and balanced fundamental bases."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parent
Edge = Tuple[int, int]
Vector = Dict[Edge, int]


def edge(n: int, j: int) -> Edge:
    if not (2 <= n and 1 <= j < n):
        raise ValueError((n, j))
    return (n, min(j, n - j))


def add_term(v: Vector, e: Edge, c: int) -> None:
    if c:
        v[e] = v.get(e, 0) + c
        if v[e] == 0:
            del v[e]


def add_vectors(*terms: Tuple[int, Vector]) -> Vector:
    out: Vector = {}
    for scale, vec in terms:
        for e, c in vec.items():
            add_term(out, e, scale * c)
    return out


def singleton(e: Edge, c: int = 1) -> Vector:
    return {e: c} if c else {}


def divergence(v: Vector, X: int) -> List[int]:
    r = [0] * (X + 1)
    for (n, j), c in v.items():
        r[n] += c
        r[j] -= c
        r[n - j] -= c
    return r


def l1(v: Vector) -> int:
    return sum(abs(c) for c in v.values())


def full_edges(X: int) -> List[Edge]:
    return [(n, j) for n in range(2, X + 1) for j in range(1, n // 2 + 1)]


def balanced_edges(X: int) -> List[Edge]:
    out = []
    for n in range(2, X + 1):
        lo = (n + 3) // 4
        for j in range(lo, n // 2 + 1):
            out.append((n, j))
    return out


def pascal_cycle(n: int, j: int) -> Vector:
    if not (2 <= j <= n // 2):
        raise ValueError((n, j))
    out: Vector = {}
    add_term(out, edge(n, j), 1)
    add_term(out, edge(j, 1), 1)
    add_term(out, edge(n, 1), -1)
    add_term(out, edge(n - 1, j - 1), -1)
    return out


def canonical_child(n: int) -> int:
    return n // 2


def tree(n: int, memo: Dict[int, Vector]) -> Vector:
    if n <= 1:
        return {}
    if n not in memo:
        a = canonical_child(n)
        b = n - a
        memo[n] = add_vectors(
            (1, singleton(edge(n, a))),
            (1, tree(a, memo)),
            (1, tree(b, memo)),
        )
    return dict(memo[n])


def fundamental_cycle(n: int, j: int, memo: Dict[int, Vector]) -> Vector:
    return add_vectors(
        (1, singleton(edge(n, j))),
        (1, tree(j, memo)),
        (1, tree(n - j, memo)),
        (-1, tree(n, memo)),
    )


def rank_mod(matrix: List[List[int]], p: int = 1_000_003) -> int:
    if not matrix:
        return 0
    a = [[x % p for x in row] for row in matrix]
    m, n = len(a), len(a[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((i for i in range(rank, m) if a[i][col]), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], p - 2, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(m):
            if i != rank and a[i][col]:
                f = a[i][col]
                a[i] = [(a[i][k] - f * a[rank][k]) % p for k in range(n)]
        rank += 1
        col += 1
    return rank


def columns_matrix(vectors: Iterable[Vector], edges: List[Edge]) -> List[List[int]]:
    vecs = list(vectors)
    return [[v.get(e, 0) for v in vecs] for e in edges]


def proof_object() -> Dict[str, object]:
    full_cycle_checks = 0
    balanced_cycle_checks = 0
    reduction_checks = 0
    tree_checks = 0
    basis_checks = 0
    canonical_solution_checks = 0

    for X in range(4, 31):
        edges = full_edges(X)
        cycles = [pascal_cycle(n, j) for n, j in edges if j >= 2]
        for c in cycles:
            assert divergence(c, X) == [0] * (X + 1)
            full_cycle_checks += 1
        expected = len(edges) - (X - 1)
        assert len(cycles) == expected
        assert rank_mod(columns_matrix(cycles, edges)) == expected

        for n, j in edges:
            rhs: Vector = {}
            for t in range(n - j + 1, n + 1):
                add_term(rhs, edge(t, 1), 1)
            for t in range(2, j + 1):
                add_term(rhs, edge(t, 1), -1)
            assert divergence(singleton((n, j)), X) == divergence(rhs, X)
            reduction_checks += 1

        bedges = balanced_edges(X)
        memo: Dict[int, Vector] = {}
        canonical = {edge(n, canonical_child(n)) for n in range(2, X + 1)}
        for n in range(2, X + 1):
            t = tree(n, memo)
            r = divergence(t, X)
            expected_r = [0] * (X + 1)
            expected_r[n] = 1
            expected_r[1] = -n
            assert r == expected_r
            assert l1(t) == n - 1
            assert set(t).issubset(set(bedges))
            tree_checks += 1

        noncanonical = [e for e in bedges if e not in canonical]
        fcycles = [fundamental_cycle(n, j, memo) for n, j in noncanonical]
        for e, c in zip(noncanonical, fcycles):
            assert divergence(c, X) == [0] * (X + 1)
            assert c.get(e) == 1
            assert all((x == e or x in canonical) for x in c)
            assert l1(c) <= 2 * e[0] - 2
            balanced_cycle_checks += 1
        assert rank_mod(columns_matrix(fcycles, bedges)) == len(noncanonical)
        basis_checks += 1

        target = [0] * (X + 1)
        for m in range(2, X + 1):
            target[m] = ((-1) ** m) * (1 + (m % 3))
        target[1] = -sum(m * target[m] for m in range(2, X + 1))
        d: Vector = {}
        for m in range(2, X + 1):
            d = add_vectors((1, d), (target[m], tree(m, memo)))
        assert divergence(d, X) == target
        canonical_solution_checks += 1

        if noncanonical:
            repaired = add_vectors((1, d), (7, fcycles[0]), (-3, fcycles[-1]))
            assert divergence(repaired, X) == target

    bad = pascal_cycle(10, 4)
    add_term(bad, edge(10, 1), 2)
    assert divergence(bad, 10) != [0] * 11

    return {
        "classification": "EXACT_PASCAL_AND_BALANCED_FUNDAMENTAL_CYCLE_BASES_VERIFIED",
        "full_pascal_cycle_checks": full_cycle_checks,
        "explicit_reduction_checks": reduction_checks,
        "canonical_tree_checks": tree_checks,
        "balanced_fundamental_cycle_checks": balanced_cycle_checks,
        "balanced_basis_levels": basis_checks,
        "canonical_solution_checks": canonical_solution_checks,
        "maximum_X": 30,
        "scope": (
            "Exact finite chain-complex algebra only. This result does not construct "
            "nonnegative cofinal cycle coordinates, prove MFT, or prove RH."
        ),
    }


def canonical_json(obj: Dict[str, object]) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main() -> None:
    obj = proof_object()
    obj["proof_object_sha256"] = hashlib.sha256(canonical_json(obj)).hexdigest()
    out = ROOT / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    print(json.dumps(obj, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
