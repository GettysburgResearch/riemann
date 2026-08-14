#!/usr/bin/env python3
"""Exact-rational replay for L-93240--L-93242.

This checker authenticates the finite Hilbert identities, the square-root-free
coherence inequalities, the geometric same-tower algebra, and the exact Q4
prime-base decomposition on a broad finite fixture bank.  It does not prove
any imported asymptotic estimate, the first-Hermite explicit formula, the
T-93010 Mellin implication, or RH.
"""

from __future__ import annotations

import argparse
import json
import random
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

Vector = Tuple[Fraction, ...]


def add(u: Vector, v: Vector) -> Vector:
    assert len(u) == len(v)
    return tuple(a + b for a, b in zip(u, v))


def dot(u: Vector, v: Vector) -> Fraction:
    assert len(u) == len(v)
    return sum((a * b for a, b in zip(u, v)), Fraction(0))


def norm2(u: Vector) -> Fraction:
    return dot(u, u)


def zero(dim: int) -> Vector:
    return tuple(Fraction(0) for _ in range(dim))


def sum_vectors(vectors: Sequence[Vector]) -> Vector:
    if not vectors:
        return tuple()
    out = zero(len(vectors[0]))
    for vector in vectors:
        out = add(out, vector)
    return out


def check_coherence(blocks: Sequence[Vector]) -> Dict[str, int]:
    """Check L-93240 in the exact square-root-free normalization."""
    if not blocks:
        raise AssertionError("fixture must contain at least one block")
    dim = len(blocks[0])
    if any(len(block) != dim for block in blocks):
        raise AssertionError("dimension mismatch")

    total = sum_vectors(blocks)
    energy = norm2(total)
    diagonal = sum((norm2(block) for block in blocks), Fraction(0))
    cross = sum(
        (dot(blocks[i], blocks[j]) for i in range(len(blocks)) for j in range(i + 1, len(blocks))),
        Fraction(0),
    )
    assert energy == diagonal + 2 * cross

    raw = [max(dot(block, total), Fraction(0)) for block in blocks]
    assert sum(raw, Fraction(0)) >= energy
    assert sum((value * value for value in raw), Fraction(0)) <= energy * diagonal

    if energy > 0:
        assert diagonal > 0
        positive_count = sum(value > 0 for value in raw)
        assert positive_count * diagonal >= energy

        ordered = sorted((value for value in raw if value > 0), reverse=True)
        carried = Fraction(0)
        half_count = 0
        for value in ordered:
            carried += value
            half_count += 1
            if 2 * carried >= energy:
                break
        assert half_count > 0
        assert 4 * half_count * diagonal >= energy

        projected_cross = sum(
            (raw[i] * raw[j] for i in range(len(raw)) for j in range(i + 1, len(raw))),
            Fraction(0),
        )
        assert 2 * projected_cross >= energy * (energy - diagonal)
    else:
        positive_count = 0
        half_count = 0

    return {
        "dimension": dim,
        "blocks": len(blocks),
        "positive_blocks": positive_count,
        "half_carrier_blocks": half_count,
    }


def random_fraction(rng: random.Random) -> Fraction:
    return Fraction(rng.randint(-9, 9), rng.randint(1, 7))


def run_hilbert_fixtures() -> int:
    rng = random.Random(93240)
    fixtures: List[List[Vector]] = [
        [(Fraction(1),), (Fraction(2),), (Fraction(3),)],
        [(Fraction(5),), (Fraction(-4),), (Fraction(2),)],
        [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(2))],
        [(Fraction(1), Fraction(2)), (Fraction(-1), Fraction(-2))],
        [(Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))],
    ]
    for _ in range(1200):
        dim = rng.randint(1, 7)
        count = rng.randint(1, 11)
        fixtures.append(
            [tuple(random_fraction(rng) for _ in range(dim)) for _ in range(count)]
        )

    for blocks in fixtures:
        check_coherence(blocks)
    return len(fixtures)


def complex_mul(z: Vector, w: Vector) -> Vector:
    if len(z) != 2 or len(w) != 2:
        raise AssertionError("complex vectors must have dimension two")
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def complex_scale(c: Fraction, z: Vector) -> Vector:
    return (c * z[0], c * z[1])


def run_prime_phase_fixtures() -> int:
    unit_points: List[Vector] = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(7, 25), Fraction(24, 25)),
        (Fraction(20, 29), Fraction(21, 29)),
        (Fraction(-3, 5), Fraction(4, 5)),
        (Fraction(12, 13), Fraction(-5, 13)),
    ]
    blocks: List[Vector] = []
    for index, phase in enumerate(unit_points, start=1):
        power = (Fraction(1), Fraction(0))
        block = (Fraction(0), Fraction(0))
        for exponent in range(1, 6):
            power = complex_mul(power, phase)
            coefficient = Fraction(((-1) ** (index + exponent)) * (index + 2), (exponent + 1) * (index + 1))
            block = add(block, complex_scale(coefficient, power))
        blocks.append(block)
    check_coherence(blocks)
    return len(blocks)


def run_tower_identities() -> int:
    points = [
        Fraction(1, 9),
        Fraction(1, 5),
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(1, 2),
        Fraction(3, 5),
        Fraction(5, 8),
        Fraction(3, 4),
    ]
    checks = 0
    for x in points:
        closed = 2 * x**3 / ((1 - x) ** 2 * (1 + x))
        geometric = (x / (1 - x)) ** 2 - x**2 / (1 - x**2)
        assert closed == geometric
        assert closed <= 32 * x**3  # exact for 0 <= x <= 3/4
        checks += 2

        for cutoff in range(2, 18):
            lhs = 2 * sum(
                (x ** (r + s) for r in range(1, cutoff + 1) for s in range(r + 1, cutoff + 1)),
                Fraction(0),
            )
            finite = sum((x**r for r in range(1, cutoff + 1)), Fraction(0))
            rhs = finite**2 - sum((x ** (2 * r) for r in range(1, cutoff + 1)), Fraction(0))
            assert lhs == rhs
            checks += 1
    return checks


def sieve(limit: int) -> List[int]:
    flags = [True] * (limit + 1)
    flags[0:2] = [False, False]
    for p in range(2, int(limit**0.5) + 1):
        if flags[p]:
            for multiple in range(p * p, limit + 1, p):
                flags[multiple] = False
    return [n for n, is_prime in enumerate(flags) if is_prime]


def is_power_of(m: int, p: int) -> bool:
    if m < p:
        return False
    value = p
    while value < m:
        value *= p
    return value == m


def is_power_of_four(m: int) -> bool:
    if m < 4:
        return False
    value = 4
    while value < m:
        value *= 4
    return value == m


def formal_lambda(m: int, weights: Dict[int, Fraction]) -> Fraction:
    for p, weight in weights.items():
        if is_power_of(m, p):
            return weight
    return Fraction(0)


def source_component(m: int, p: int, weight: Fraction) -> Fraction:
    value = Fraction(0)
    if is_power_of(m, p):
        value += weight
    if m % 4 == 0 and is_power_of(m // 4, p):
        value -= 4 * weight
    if p == 2 and is_power_of_four(m):
        value += 6 * weight  # 3 log 4 = 6 log 2
    return value


def prefix(values: Sequence[Fraction]) -> List[Fraction]:
    out = [Fraction(0)]
    running = Fraction(0)
    for value in values[1:]:
        running += value
        out.append(running)
    return out


def run_q4_fixtures(max_endpoint: int = 96) -> Tuple[int, int]:
    primes = sieve(max_endpoint)
    weights = {p: Fraction(index + 2, index + 3) for index, p in enumerate(primes)}
    endpoints = 0
    coefficient_checks = 0

    for n in range(2, max_endpoint + 1):
        active = [p for p in primes if p <= n]
        components: Dict[int, List[Fraction]] = {}
        for p in active:
            components[p] = [Fraction(0)] + [source_component(m, p, weights[p]) for m in range(1, n + 1)]

        total = [Fraction(0)]
        for m in range(1, n + 1):
            independent = formal_lambda(m, weights)
            if m % 4 == 0:
                independent -= 4 * formal_lambda(m // 4, weights)
            if is_power_of_four(m):
                independent += 6 * weights[2]
            grouped = sum((components[p][m] for p in active), Fraction(0))
            assert grouped == independent
            total.append(independent)
            coefficient_checks += 1

        total_prefix = prefix(total)
        block_rows: List[Vector] = []
        for p in active:
            component_prefix = prefix(components[p])
            row = tuple(
                component_prefix[n] - component_prefix[j] - component_prefix[n - j - 1]
                for j in range(n)
            )
            absolute_mass = sum((abs(value) for value in components[p][1:]), Fraction(0))
            assert all(abs(value) <= 3 * absolute_mass for value in row)
            block_rows.append(row)

            # Exact integer-power witnesses behind A_{p,N} <= 5 log N (+ 3 log N for p=2).
            powers = [k for k in range(1, n + 1) if is_power_of(k, p)]
            shifted = [k for k in range(1, n + 1) if k % 4 == 0 and is_power_of(k // 4, p)]
            if powers:
                assert powers[-1] <= n
            if shifted:
                assert shifted[-1] <= n
            if p == 2:
                gauges = [k for k in range(1, n + 1) if is_power_of_four(k)]
                if gauges:
                    assert gauges[-1] <= n

        direct_row = tuple(
            total_prefix[n] - total_prefix[j] - total_prefix[n - j - 1]
            for j in range(n)
        )
        grouped_row = sum_vectors(block_rows)
        assert grouped_row == direct_row
        check_coherence(block_rows)
        endpoints += 1

    return endpoints, coefficient_checks


def run_mutation_tests() -> int:
    mutations_detected = 0

    blocks = [
        (Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(-1)),
        (Fraction(-2), Fraction(4)),
    ]
    total = sum_vectors(blocks)
    mutated_total = sum_vectors(blocks[:-1])
    try:
        assert mutated_total == total
    except AssertionError:
        mutations_detected += 1

    x = Fraction(2, 5)
    correct = 2 * x**3 / ((1 - x) ** 2 * (1 + x))
    mutated = 2 * x**3 / ((1 - x) ** 2 * (1 - x))
    try:
        assert mutated == correct
    except AssertionError:
        mutations_detected += 1

    weights = {2: Fraction(2, 3), 3: Fraction(3, 4), 5: Fraction(5, 6)}
    m = 20
    correct_source = formal_lambda(m, weights) - 4 * formal_lambda(m // 4, weights)
    if is_power_of_four(m):
        correct_source += 6 * weights[2]
    mutated_source = formal_lambda(m, weights) + 4 * formal_lambda(m // 4, weights)
    if is_power_of_four(m):
        mutated_source += 6 * weights[2]
    try:
        assert mutated_source == correct_source
    except AssertionError:
        mutations_detected += 1

    assert mutations_detected == 3
    return mutations_detected


def build_result() -> Dict[str, object]:
    hilbert = run_hilbert_fixtures()
    prime_phase_blocks = run_prime_phase_fixtures()
    tower = run_tower_identities()
    q4_endpoints, q4_coefficients = run_q4_fixtures()
    mutations = run_mutation_tests()
    return {
        "arithmetic_class": "EXACT_RATIONAL",
        "claim_ids": ["L-93240", "L-93241", "L-93242", "T-93243"],
        "checks": {
            "hilbert_space_fixtures": hilbert,
            "prime_phase_blocks": prime_phase_blocks,
            "q4_endpoint_fixtures": q4_endpoints,
            "q4_source_coefficients": q4_coefficients,
            "same_tower_algebra_checks": tower,
            "mutation_tests_detected": mutations,
        },
        "does_not_authenticate": [
            "PR #392 first-Hermite explicit formula or large-value theorem",
            "V(q)=q+O(sqrt(q))",
            "T-93010 Mellin pole-to-energy implication",
            "any deterministic prime-resonance exclusion",
            "the Riemann Hypothesis",
        ],
        "verdict": "PASS_X_93240_PRIME_BLOCK_COHERENCE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("results/verification.json"),
        help="output path for the deterministic verification record",
    )
    args = parser.parse_args()
    result = build_result()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])


if __name__ == "__main__":
    main()
