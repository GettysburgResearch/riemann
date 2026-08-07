#!/usr/bin/env python3
"""Exact finite regression for R-23702.

Standard library only.  The checker freezes eight disjoint close prime pairs,
forms the 2^8 squarefree products, verifies that they lie in one fixed-ratio
2/3 shell, and reconstructs the affine rank of their multiplicative Bohr
exponent vectors.

This is a finite counterexample to any schema that requires an absolute rank
ceiling below 8 for all balanced faces.  The all-order refutation in R-23702
uses the prime number theorem to repeat the construction for arbitrary K.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

PAIRS = (
    (1000003, 1000033),
    (1000037, 1000039),
    (1000081, 1000099),
    (1000117, 1000121),
    (1000133, 1000151),
    (1000159, 1000171),
    (1000183, 1000187),
    (1000193, 1000199),
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def rational_rank(rows: list[list[int]]) -> int:
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    nrows = len(a)
    ncols = len(a[0])
    rank = 0
    col = 0
    while rank < nrows and col < ncols:
        pivot = next((r for r in range(rank, nrows) if a[r][col]), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for r in range(nrows):
            if r == rank or not a[r][col]:
                continue
            factor = a[r][col]
            a[r] = [x - factor * y for x, y in zip(a[r], a[rank])]
        rank += 1
        col += 1
    return rank


def canonical_sha256(obj: object) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def verify() -> dict[str, object]:
    primes = [p for pair in PAIRS for p in pair]
    assert len(primes) == len(set(primes))
    assert all(is_prime(p) for p in primes)

    products: list[int] = []
    exponent_vectors: list[list[int]] = []
    for bits in itertools.product((0, 1), repeat=len(PAIRS)):
        products.append(math.prod(PAIRS[i][bit] for i, bit in enumerate(bits)))
        vector = [0] * len(primes)
        for i, bit in enumerate(bits):
            vector[2 * i + bit] = 1
        exponent_vectors.append(vector)

    assert len(products) == 2 ** len(PAIRS)
    assert len(products) == len(set(products))
    minimum = min(products)
    maximum = max(products)
    assert 2 * maximum < 3 * minimum
    assert all(3 * n > 2 * maximum for n in products)

    base = exponent_vectors[0]
    edge_rows = []
    for i in range(len(PAIRS)):
        vertex = exponent_vectors[1 << (len(PAIRS) - 1 - i)]
        edge_rows.append([x - y for x, y in zip(vertex, base)])
    rank = rational_rank(edge_rows)
    assert rank == len(PAIRS)

    # Every product contains exactly eight distinct primes, so mu(n)=+1.
    mobius_sign = (-1) ** len(PAIRS)
    assert mobius_sign == 1

    # At t=log(maximum), every fixed-ratio shell translate is active.  After
    # multiplying the squared signal by maximum, the exact common-overlap
    # energy of this same-sign subfamily is (#products)^2.
    scaled_energy = len(products) ** 2

    result: dict[str, object] = {
        "schema": "riemann.x23702-mobius-hypercube.v1",
        "classification": "EXACT_FINITE_REFUTATION_CONTROL",
        "K": len(PAIRS),
        "pairs": [list(pair) for pair in PAIRS],
        "products": len(products),
        "distinct_products": len(set(products)),
        "minimum_product": str(minimum),
        "maximum_product": str(maximum),
        "shell_ratio_numerator": str(maximum),
        "shell_ratio_denominator": str(minimum),
        "all_inside_two_thirds_shell": True,
        "mobius_sign": mobius_sign,
        "affine_bohr_rank": rank,
        "scaled_common_overlap_energy": str(scaled_energy),
        "verdict": "BOUNDED_RANK_CONTAGION_REFUTED_AT_FINITE_K8_SCHEMA",
    }
    result["proof_object_sha256"] = canonical_sha256(result)
    return result


def main() -> None:
    result = verify()
    output = Path(__file__).resolve().parent / "results" / "exact-verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
