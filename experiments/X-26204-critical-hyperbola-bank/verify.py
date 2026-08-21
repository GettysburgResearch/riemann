#!/usr/bin/env python3
"""Exact regression for L-26211, the critical hyperbola bank split.

Standard library only.  This verifies finite coefficient coverage,
inclusion-exclusion, and strict lower-scale support.  It proves no physical
remainder estimate and no result about RH.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json


def valuation_two(n: int) -> int:
    value = 0
    while n % 2 == 0:
        n //= 2
        value += 1
    return value


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            value = n * prime
            if value > limit:
                break
            composite[value] = True
            if n % prime == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]
    return mu


def c2(n: int) -> int:
    return 1 - valuation_two(n)


def omega2(n: int, mu: list[int]) -> Fraction:
    value = Fraction(mu[n])
    if n % 2 == 0:
        value -= Fraction(3, 2) * mu[n // 2]
    if n % 4 == 0:
        value += Fraction(1, 2) * mu[n // 4]
    return value


def add(target: dict[int, Fraction], index: int, value: Fraction) -> None:
    target[index] += value
    if target[index] == 0:
        del target[index]


def main() -> None:
    maximum_n = 64
    mu = mobius_sieve(maximum_n * maximum_n)
    expected = {1: Fraction(1), 2: Fraction(-5, 2), 4: Fraction(1)}

    coefficient_cases = 0
    remainder_rows = 0
    mutation_failures = 0
    for nscale in range(3, maximum_n + 1):
        cutoff = nscale * nscale
        first: dict[int, Fraction] = defaultdict(Fraction)
        second: dict[int, Fraction] = defaultdict(Fraction)
        overlap: dict[int, Fraction] = defaultdict(Fraction)
        remainder: dict[int, Fraction] = defaultdict(Fraction)

        for d in range(1, nscale):
            wd = omega2(d, mu)
            if wd == 0:
                continue
            k = 1
            while d * k < cutoff:
                add(first, d * k, wd * c2(k))
                k += 1

        for k in range(1, nscale):
            ck = Fraction(c2(k))
            if ck == 0:
                continue
            d = 1
            while k * d < cutoff:
                add(second, k * d, ck * omega2(d, mu))
                d += 1
            for d in range(1, nscale):
                wd = omega2(d, mu)
                if wd:
                    add(overlap, k * d, ck * wd)
            for d in range(nscale, (cutoff - 1) // k + 1):
                wd = omega2(d, mu)
                if wd:
                    product = k * d
                    assert nscale <= product < cutoff
                    add(remainder, product, ck * wd)
                    remainder_rows += 1

        total: dict[int, Fraction] = defaultdict(Fraction)
        for dictionary, sign in ((first, 1), (second, 1), (overlap, -1)):
            for index, value in dictionary.items():
                add(total, index, sign * value)

        split_total: dict[int, Fraction] = defaultdict(Fraction)
        for dictionary in (first, remainder):
            for index, value in dictionary.items():
                add(split_total, index, value)

        for index in range(1, cutoff):
            wanted = expected.get(index, Fraction(0))
            assert total.get(index, Fraction(0)) == wanted
            assert split_total.get(index, Fraction(0)) == wanted
            coefficient_cases += 1

        # Mandatory mutation: omit the overlap correction.  At least one
        # coefficient must then disagree.
        mutated = defaultdict(Fraction)
        for dictionary in (first, second):
            for index, value in dictionary.items():
                mutated[index] += value
        if any(mutated.get(index, Fraction(0)) != expected.get(index, Fraction(0))
               for index in range(1, cutoff)):
            mutation_failures += 1

    assert mutation_failures == maximum_n - 2

    result = {
        "verdict": "PASS_EXACT_CRITICAL_HYPERBOLA_BANK_SPLIT",
        "scales_checked": maximum_n - 2,
        "coefficient_cases": coefficient_cases,
        "remainder_monomials_checked": remainder_rows,
        "overlap_omission_mutations_rejected": mutation_failures,
        "fixed_output": {"1": "1", "2": "-5/2", "4": "1"},
        "remainder_support": "N <= product < N^2",
        "scope": (
            "Exact finite hyperbola coverage and support only. "
            "No physical remainder estimate, cofinal recurrence, or RH result."
        ),
    }
    payload = json.dumps(result, sort_keys=True, indent=2)
    result["proof_object_sha256_without_digest"] = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
