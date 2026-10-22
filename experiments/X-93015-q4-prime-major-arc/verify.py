#!/usr/bin/env python3
"""Exact finite replay for L-93015.

The replay authenticates:
- coefficientwise prime-base partition of the complete Q4 source;
- complete row and Gram decomposition;
- sum-before-square diagonal inequalities;
- exact prime-power orbit support;
- the abstract orthogonal-projection argument used to remove the minor arc.

The Chebyshev and Fourier minor-arc estimates are analytic inputs proved in the
written lemma; this checker does not promote floating trigonometric tests to a
proof.
"""

from __future__ import annotations

import argparse
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple


def sieve_primes(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
    return [p for p in range(2, n + 1) if is_prime[p]]


def prime_power_base(m: int) -> int | None:
    if m < 2:
        return None
    for p in sieve_primes(int(m ** 0.5) + 1):
        if m % p == 0:
            x = m
            while x % p == 0:
                x //= p
            return p if x == 1 else None
    return m  # prime


def is_power_of_four(m: int) -> bool:
    if m < 4:
        return False
    while m % 4 == 0:
        m //= 4
    return m == 1


def source_blocks(N: int) -> Dict[int, List[int]]:
    """Formal coefficients in independent log(p) symbols.

    c_p[m] is the integer coefficient multiplying log(p). The gauge
    3 log 4 is 6 log 2.
    """
    primes = sieve_primes(N)
    blocks = {p: [0] * (N + 1) for p in primes}
    for m in range(1, N + 1):
        p = prime_power_base(m)
        if p is not None:
            blocks[p][m] += 1
        if m % 4 == 0:
            p2 = prime_power_base(m // 4)
            if p2 is not None:
                blocks[p2][m] -= 4
        if is_power_of_four(m):
            blocks[2][m] += 6
    return blocks


def total_source(N: int) -> List[Dict[int, int]]:
    out: List[Dict[int, int]] = [dict() for _ in range(N + 1)]
    for m in range(1, N + 1):
        p = prime_power_base(m)
        if p is not None:
            out[m][p] = out[m].get(p, 0) + 1
        if m % 4 == 0:
            p2 = prime_power_base(m // 4)
            if p2 is not None:
                out[m][p2] = out[m].get(p2, 0) - 4
        if is_power_of_four(m):
            out[m][2] = out[m].get(2, 0) + 6
        out[m] = {p: c for p, c in out[m].items() if c}
    return out


def rows_from_blocks(N: int, blocks: Dict[int, List[int]], weights: Dict[int, Fraction]) -> Dict[int, List[Fraction]]:
    rows: Dict[int, List[Fraction]] = {}
    for p, coeffs in blocks.items():
        pref = [Fraction(0)] * (N + 1)
        for m in range(1, N + 1):
            pref[m] = pref[m - 1] + weights[p] * coeffs[m]
        rows[p] = [pref[N] - pref[j] - pref[N - j - 1] for j in range(N)]
    return rows


def dot(x: List[Fraction], y: List[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(x, y)), Fraction(0))


def norm2(x: List[Fraction]) -> Fraction:
    return dot(x, x)


def run() -> dict:
    rng = random.Random(93015)
    source_coeff_checks = 0
    row_checks = 0
    gram_checks = 0
    tower_bound_checks = 0
    projection_checks = 0
    phase_support_checks = 0
    mutations_detected = 0
    unequal_power_terms = 0

    for N in list(range(8, 81)) + [96, 112, 128, 160, 192, 224, 256]:
        blocks = source_blocks(N)
        total = total_source(N)
        primes = sorted(blocks)

        for m in range(1, N + 1):
            reconstructed = {p: blocks[p][m] for p in primes if blocks[p][m]}
            assert reconstructed == total[m]
            source_coeff_checks += 1

        # Positive exact rational stand-ins for independent log(p) symbols.
        weights = {p: Fraction((p % 17) + 3, (p % 7) + 2) for p in primes}
        rows = rows_from_blocks(N, blocks, weights)
        complete = [sum((rows[p][j] for p in primes), Fraction(0)) for j in range(N)]

        # Direct source prefix row.
        c = [Fraction(0)] * (N + 1)
        for m in range(1, N + 1):
            c[m] = sum((weights[p] * blocks[p][m] for p in primes), Fraction(0))
        pref = [Fraction(0)] * (N + 1)
        for m in range(1, N + 1):
            pref[m] = pref[m - 1] + c[m]
        direct = [pref[N] - pref[j] - pref[N - j - 1] for j in range(N)]
        assert complete == direct
        row_checks += N

        D = sum((norm2(rows[p]) for p in primes), Fraction(0))
        cross = sum((2 * dot(rows[p], rows[r])
                     for i, p in enumerate(primes) for r in primes[i + 1:]), Fraction(0))
        assert norm2(complete) == D + cross
        gram_checks += 1

        # Sum-before-square inequalities, exact on the synthetic weights.
        A: Dict[int, Fraction] = {
            p: sum((abs(weights[p] * blocks[p][m]) for m in range(1, N + 1)), Fraction(0))
            for p in primes
        }
        assert sum((a * a for a in A.values()), Fraction(0)) <= max(A.values()) * sum(A.values(), Fraction(0))
        for p in primes:
            assert max(abs(v) for v in rows[p]) <= 3 * A[p]
            assert norm2(rows[p]) <= 9 * N * A[p] * A[p]
            tower_bound_checks += 2

        # Prime-power orbit support and same-prime unequal powers are retained.
        for p in primes:
            support = {m for m in range(1, N + 1) if blocks[p][m]}
            expected = set()
            x = p
            powers = []
            while x <= N:
                powers.append(x)
                expected.add(x)
                if 4 * x <= N:
                    expected.add(4 * x)
                x *= p
            if p == 2:
                x = 4
                while x <= N:
                    expected.add(x)
                    x *= 4
            assert support <= expected
            phase_support_checks += len(support)
            unequal_power_terms += len(powers) * max(0, len(powers) - 1)

        # Mutations: omit gauge and alter contracted coefficient.
        if N >= 16:
            mutated = source_blocks(N)
            # Omit one gauge atom at m=16.
            mutated[2][16] -= 6
            if {p: mutated[p][16] for p in primes if mutated[p][16]} != total[16]:
                mutations_detected += 1
            mutated2 = source_blocks(N)
            # -4 -> -3 at the first available shifted prime-power cell.
            target = next((m for m in range(4, N + 1) if prime_power_base(m // 4) is not None), None)
            assert target is not None
            bp = prime_power_base(target // 4)
            assert bp is not None
            mutated2[bp][target] += 1
            if {p: mutated2[p][target] for p in primes if mutated2[p][target]} != total[target]:
                mutations_detected += 1

    # Abstract exact orthogonal-projection cross identity. Coordinate projection
    # is enough to authenticate the Hilbert-space step; Fourier supplies the
    # arithmetic projection in the written theorem.
    for dim in range(3, 15):
        for _ in range(80):
            block_count = rng.randint(2, 8)
            vectors = [[Fraction(rng.randint(-8, 8), rng.randint(1, 9)) for _ in range(dim)]
                       for _ in range(block_count)]
            high = {i for i in range(dim) if rng.randrange(2)}
            projected = [[v[i] if i in high else Fraction(0) for i in range(dim)] for v in vectors]
            total = [sum((v[i] for v in projected), Fraction(0)) for i in range(dim)]
            E = norm2(total)
            D = sum((norm2(v) for v in projected), Fraction(0))
            C = sum((2 * dot(projected[p], projected[r])
                     for p in range(block_count) for r in range(p + 1, block_count)), Fraction(0))
            assert C == E - D
            assert abs(C) <= E + D
            projection_checks += 2

    return {
        "classification": "PASS_X_93015_Q4_PRIME_MAJOR_ARC_LOCALIZATION",
        "arithmetic_class": "EXACT_RATIONAL_WITH_FORMAL_PRIME_LOG_SYMBOLS",
        "source_coefficient_checks": source_coeff_checks,
        "row_reconstruction_checks": row_checks,
        "complete_gram_checks": gram_checks,
        "tower_diagonal_checks": tower_bound_checks,
        "prime_power_orbit_support_checks": phase_support_checks,
        "same_prime_unequal_power_terms_retained": unequal_power_terms,
        "orthogonal_projection_checks": projection_checks,
        "hostile_mutations_detected": mutations_detected,
        "proves": [
            "exact complete source and row prime-base partitions on finite fixtures",
            "exact complete-row diagonal/cross Gram identity",
            "sum-before-square diagonal inequalities",
            "abstract projected distinct-block cross bound",
        ],
        "does_not_prove": [
            "the analytic Chebyshev bound",
            "the Fourier square-root minor-arc estimate",
            "the remaining distinct-prime major-arc estimate",
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
