#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from typing import List


def beta(n: int, q: int) -> Fraction:
    if not (2 <= q <= n):
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def mobius_values(limit: int) -> List[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def valuation(n: int, p: int) -> int:
    total = 0
    while n and n % p == 0:
        n //= p
        total += 1
    return total


def divisors(n: int) -> List[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def build_result() -> dict[str, object]:
    corridor_checks = 0
    for modulus in range(2, 13):
        for k in range(2, 51):
            for e in range(2, k + 1):
                lhs = beta(modulus * (k + 1) - 1, modulus * e)
                rhs = beta(k, e)
                if lhs != rhs:
                    raise AssertionError(
                        f"corridor mismatch L={modulus}, k={k}, e={e}"
                    )
                corridor_checks += 1

    limit = 500
    mu = mobius_values(limit)
    convolution_checks = 0
    digit_increment_checks = 0
    sample_digit_sums: dict[str, dict[str, int]] = {}
    for p in (2, 3, 5, 7):
        b = [0] * (limit + 1)
        c = [0] * (limit + 1)
        digit_sum = 0
        samples: dict[str, int] = {}
        for n in range(1, limit + 1):
            b[n] = mu[n] - (mu[n // p] if n % p == 0 else 0)
            c[n] = 1 - (p - 1) * valuation(n, p)
            digit_sum += c[n]
            # Direct base-p digit sum.
            value = n
            direct = 0
            while value:
                direct += value % p
                value //= p
            if digit_sum != direct:
                raise AssertionError(f"digit increment mismatch p={p}, n={n}")
            digit_increment_checks += 1
            if n in (1, p, p * p, 64, 125, 500):
                samples[str(n)] = direct

        for n in range(1, limit + 1):
            convolution = sum(c[d] * b[n // d] for d in divisors(n))
            expected = 1 if n == 1 else (-p if n == p else 0)
            if convolution != expected:
                raise AssertionError(
                    f"Euler-aligned convolution mismatch p={p}, n={n}"
                )
            convolution_checks += 1
        sample_digit_sums[str(p)] = samples

    return {
        "schema": "X-23703-v1",
        "corridor_renormalization_checks": corridor_checks,
        "base_p_digit_increment_checks": digit_increment_checks,
        "base_p_convolution_checks": convolution_checks,
        "sample_digit_sums": sample_digit_sums,
        "verdict": "PASS_EXACT_DIGITAL_FREEZE_AND_BASE_P_PHASE_ALGEBRA",
        "scope": (
            "exact finite carry self-similarity and base-p digital convolution "
            "only; does not verify the boundary-charge recurrence, Greedy Slack, "
            "DCRS, or RH"
        ),
    }


def main() -> None:
    print(json.dumps(build_result(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
