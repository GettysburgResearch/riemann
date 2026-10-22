#!/usr/bin/env python3
"""Exact formal replay for the RH-sensitive half-scale source change.

Standard-library only. Verifies Dirichlet-convolution identities. Does not prove
the strict annular reserve, ASSD, or RH.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path

MAX_N = 128


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
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


def v2(n: int) -> int:
    result = 0
    while n % 2 == 0:
        result += 1
        n //= 2
    return result


def factorization(n: int) -> dict[int, int]:
    answer: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            answer[p] = answer.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        answer[n] = answer.get(n, 0) + 1
    return answer


Linear = dict[int, Fraction]


def add(left: Linear, right: Linear, scale: Fraction = Fraction(1)) -> Linear:
    out = defaultdict(Fraction)
    out.update(left)
    for key, value in right.items():
        out[key] += scale * value
    return {key: value for key, value in out.items() if value}


def convolve_scalar_linear(
    scalar: list[Fraction], linear: list[Linear], n: int
) -> Linear:
    out: Linear = {}
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            out = add(out, linear[divisor], scalar[n // divisor])
    return out


def main() -> None:
    mu = mobius_sieve(MAX_N)
    omega = [Fraction(0)] * (MAX_N + 1)
    a = [Fraction(0)] * (MAX_N + 1)
    a_log: list[Linear] = [{} for _ in range(MAX_N + 1)]

    for n in range(1, MAX_N + 1):
        omega[n] = Fraction(mu[n])
        if n % 2 == 0:
            omega[n] -= Fraction(3, 2) * mu[n // 2]
        if n % 4 == 0:
            omega[n] += Fraction(1, 2) * mu[n // 4]

        valuation = v2(n)
        a[n] = Fraction(2 * valuation) + Fraction(1, 2**valuation)
        a_log[n] = {
            prime: a[n] * exponent
            for prime, exponent in factorization(n).items()
        }

    generalized_lambda: list[Linear] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        generalized_lambda[n] = convolve_scalar_linear(omega, a_log, n)

    sensitive: list[Linear] = [{} for _ in range(MAX_N + 1)]
    for n in range(1, MAX_N + 1):
        sensitive[n] = convolve_scalar_linear(omega, generalized_lambda, n)

    proper_divisor_checks = 0
    for n in range(1, MAX_N + 1):
        reconstructed = convolve_scalar_linear(a, sensitive, n)
        assert reconstructed == generalized_lambda[n]

        lower: Linear = {}
        for divisor in range(2, n + 1):
            if n % divisor == 0:
                lower = add(lower, sensitive[n // divisor], a[divisor])
                proper_divisor_checks += 1
        assert add(generalized_lambda[n], lower, Fraction(-1)) == sensitive[n]

    result = {
        "schema": "X-26804-source-change-v1",
        "classification": "EXACT_RH_SENSITIVE_SOURCE_CHANGE_HALF_SCALE_VERIFIED",
        "max_n": MAX_N,
        "source_change_rows": MAX_N,
        "proper_divisor_destinations_checked": proper_divisor_checks,
        "proof_boundary": (
            "finite formal Dirichlet-convolution algebra only; the strict "
            "annular reserve, ASSD, and RH remain unproved"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
