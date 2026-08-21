#!/usr/bin/env python3
"""Exact finite replay for L-93013.

The checker treats every von-Mangoldt prime power as a formal variable, verifies
the five-channel quadratic expansion for both Q4 kernels, partitions all terms
by prime base, checks the tower-count envelope, and detects equality-diagonal
and coefficient mutations.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Callable, DefaultDict, Dict, Optional, Tuple

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"
KAPPA = (1, 1, 1, 1, -4)
Monomial = Tuple[int, int]
Polynomial = Dict[Monomial, int]


def smallest_prime_factor(n: int) -> int:
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1 if d == 2 else 2
    return n


def prime_power_base(n: int) -> Optional[int]:
    if n < 2:
        return None
    p = smallest_prime_factor(n)
    while n % p == 0:
        n //= p
    return p if n == 1 else None


def phi(r: int, a: int) -> int:
    return 4 * a - r if r < 4 else a


def linear_b(a: int, kappas: Tuple[int, ...] = KAPPA) -> Dict[int, int]:
    out: DefaultDict[int, int] = defaultdict(int)
    for r, kappa in enumerate(kappas):
        m = phi(r, a)
        if prime_power_base(m) is not None:
            out[m] += kappa
    return {m: c for m, c in out.items() if c}


def add_poly(dst: DefaultDict[Monomial, int], m1: int, m2: int, value: int) -> None:
    key = (m1, m2) if m1 <= m2 else (m2, m1)
    dst[key] += value


def direct_quadratic(n: int, kernel: Callable[[int, int], int]) -> Polynomial:
    lines = {a: linear_b(a) for a in range(1, n)}
    out: DefaultDict[Monomial, int] = defaultdict(int)
    for a in range(1, n):
        for b in range(1, n):
            w = kernel(a, b)
            if not w:
                continue
            for m1, c1 in lines[a].items():
                for m2, c2 in lines[b].items():
                    add_poly(out, m1, m2, w * c1 * c2)
    return {k: v for k, v in out.items() if v}


def channel_partition(
    n: int,
    kernel: Callable[[int, int], int],
    kappas: Tuple[int, ...] = KAPPA,
) -> Tuple[Polynomial, Polynomial, Polynomial, int, int]:
    full: DefaultDict[Monomial, int] = defaultdict(int)
    same: DefaultDict[Monomial, int] = defaultdict(int)
    cross: DefaultDict[Monomial, int] = defaultdict(int)
    same_abs_weight = 0
    same_different_power_terms = 0

    for r, kr in enumerate(kappas):
        for s, ks in enumerate(kappas):
            for a in range(1, n):
                m1 = phi(r, a)
                p1 = prime_power_base(m1)
                if p1 is None:
                    continue
                for b in range(1, n):
                    w = kernel(a, b)
                    if not w:
                        continue
                    m2 = phi(s, b)
                    p2 = prime_power_base(m2)
                    if p2 is None:
                        continue
                    value = w * kr * ks
                    add_poly(full, m1, m2, value)
                    if p1 == p2:
                        add_poly(same, m1, m2, value)
                        same_abs_weight += w * abs(kr * ks)
                        if m1 != m2:
                            same_different_power_terms += 1
                    else:
                        add_poly(cross, m1, m2, value)

    clean = lambda d: {k: v for k, v in d.items() if v}
    return clean(full), clean(same), clean(cross), same_abs_weight, same_different_power_terms


def tower_count_envelope(n: int) -> Tuple[int, int, int]:
    by_prime_channel: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    primes = set()
    for r in range(5):
        for a in range(1, n):
            m = phi(r, a)
            p = prime_power_base(m)
            if p is not None:
                by_prime_channel[p, r] += 1
                primes.add(p)

    envelope = 0
    max_weighted_count = 0
    for p in primes:
        weighted = sum(abs(KAPPA[r]) * by_prime_channel[p, r] for r in range(5))
        max_weighted_count = max(max_weighted_count, weighted)
        envelope += n * weighted * weighted
        for r in range(5):
            count = by_prime_channel[p, r]
            if count:
                assert p**count <= 4 * n
    return envelope, len(primes), max_weighted_count


def run() -> Dict[str, object]:
    polynomial_identities = 0
    partition_identities = 0
    envelope_checks = 0
    coefficient_mutations = 0
    equality_diagonal_mutations = 0
    same_different_power_terms = 0
    max_same_abs_over_envelope_num = 0
    max_same_abs_over_envelope_den = 1

    for n in range(8, 65):
        kernels = {
            "plus": lambda a, b, n=n: n + 1 - a - b if a + b <= n else 0,
            "max": lambda a, b, n=n: n - max(a, b),
        }
        envelope, prime_count, max_weighted_count = tower_count_envelope(n)
        assert prime_count <= 4 * n
        assert max_weighted_count >= 1
        envelope_checks += 2

        for kernel in kernels.values():
            direct = direct_quadratic(n, kernel)
            full, same, cross, same_abs, different_power = channel_partition(n, kernel)
            assert direct == full
            polynomial_identities += 1

            recombined: DefaultDict[Monomial, int] = defaultdict(int)
            for source in (same, cross):
                for key, value in source.items():
                    recombined[key] += value
            assert {k: v for k, v in recombined.items() if v} == full
            assert all(prime_power_base(a) == prime_power_base(b) for a, b in same)
            assert all(prime_power_base(a) != prime_power_base(b) for a, b in cross)
            partition_identities += 3

            assert same_abs <= envelope
            envelope_checks += 1
            if same_abs * max_same_abs_over_envelope_den > max_same_abs_over_envelope_num * envelope:
                max_same_abs_over_envelope_num = same_abs
                max_same_abs_over_envelope_den = envelope

            same_different_power_terms += different_power
            if different_power:
                equality_only = {k: v for k, v in full.items() if k[0] == k[1]}
                assert equality_only != same
                equality_diagonal_mutations += 1

            mutated, _, _, _, _ = channel_partition(n, kernel, (1, 1, 1, 1, -3))
            if mutated != direct:
                coefficient_mutations += 1
            else:
                raise AssertionError("contracted-channel coefficient mutation escaped")

    return {
        "verdict": "PASS_X_93013_Q4_PRIME_TOWER_EXTRACTION",
        "arithmetic": "EXACT_INTEGER_FORMAL_VON_MANGOLDT",
        "polynomial_expansion_identities": polynomial_identities,
        "same_cross_partition_identities": partition_identities,
        "tower_envelope_checks": envelope_checks,
        "same_prime_different_power_terms_seen": same_different_power_terms,
        "equality_diagonal_mutations_detected": equality_diagonal_mutations,
        "contracted_coefficient_mutations_detected": coefficient_mutations,
        "maximum_same_abs_to_count_envelope_ratio": (
            f"{max_same_abs_over_envelope_num}/{max_same_abs_over_envelope_den}"
        ),
        "proves": [
            "finite five-channel formal expansion",
            "finite same-prime versus distinct-prime partition",
            "finite prime-tower count envelope",
        ],
        "does_not_prove": [
            "analytic Chebyshev-to-asymptotic bound",
            "distinct-prime correlation estimate",
            "endpoint PIG",
            "Riemann Hypothesis",
        ],
    }


def main() -> None:
    payload = run()
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
