#!/usr/bin/env python3
"""Exact formal-additive replay for L-26903.

A distinct integer weight is assigned to each prime.  This verifies the
Dirichlet-convolution and carry-synthesis algebra without using floating-point
logarithms.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


LIMIT = 100
EXPECTED_SHA256 = "11e5e76a49b49ab2f838d7a829936b4e46bed5482c0d0a717fb4161f6b99eeda"


def mobius_table(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
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


def primes_up_to(limit: int) -> list[int]:
    return [
        n
        for n in range(2, limit + 1)
        if all(n % d for d in range(2, int(n**0.5) + 1))
    ]


MU = mobius_table(4 * LIMIT + 10)
PRIMES = primes_up_to(4 * LIMIT + 10)
PRIME_WEIGHT = {p: index + 1 for index, p in enumerate(PRIMES)}


def v2(n: int) -> int:
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    return exponent


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def b2(n: int) -> int:
    return MU[n] - (MU[n // 2] if n % 2 == 0 else 0)


def omega2(n: int) -> Fraction:
    return Fraction(b2(n)) - Fraction(
        b2(n // 2) if n % 2 == 0 else 0, 2
    )


def inverse_coefficient(n: int) -> Fraction:
    exponent = v2(n)
    return Fraction(2 * exponent) + Fraction(1, 2**exponent)


def additive_weight(n: int) -> int:
    value = 0
    for p in PRIMES:
        while n % p == 0:
            value += PRIME_WEIGHT[p]
            n //= p
        if n == 1:
            break
    if n != 1:
        raise AssertionError("prime table too short")
    return value


def prime_power_base(n: int) -> int | None:
    for p in PRIMES:
        power = p
        while power < n:
            power *= p
        if power == n:
            return p
        if p > n:
            break
    return None


def generalized_lambda(n: int) -> Fraction:
    p = prime_power_base(n)
    value = Fraction(PRIME_WEIGHT[p]) if p is not None else Fraction(0)
    if n & (n - 1) == 0:
        exponent = v2(n)
        if exponent >= 1:
            value += Fraction(PRIME_WEIGHT[2]) * (
                1 + Fraction(1, 2**exponent)
            )
    return value


def carry(n: int, q: int, j: int) -> int:
    return n // q - j // q - (n - j) // q


def check_inverse_and_lambda() -> tuple[dict[str, int], dict[str, int]]:
    inverse_cases = 0
    lambda_cases = 0
    for n in range(1, LIMIT + 1):
        inverse = sum(
            omega2(d) * inverse_coefficient(n // d) for d in divisors(n)
        )
        assert inverse == (1 if n == 1 else 0), ("inverse", n, inverse)
        inverse_cases += 1

        value = sum(
            omega2(d)
            * inverse_coefficient(n // d)
            * additive_weight(n // d)
            for d in divisors(n)
        )
        assert value == generalized_lambda(n), (
            "generalized lambda",
            n,
            value,
            generalized_lambda(n),
        )
        lambda_cases += 1
    return {"cases": inverse_cases}, {"cases": lambda_cases}


def check_positive_synthesis() -> tuple[dict[str, int], dict[str, int]]:
    synthesis_cases = 0
    digital_cases = 0
    for n in range(2, LIMIT + 1):
        for j in range(n + 1):
            prime_profile = sum(
                generalized_lambda(q) * carry(n, q, j)
                for q in range(2, n + 1)
            )

            synthesis = Fraction(0)
            for m in range(1, n + 1):
                source_wavelet = sum(
                    omega2(k) * carry(n, m * k, j)
                    for k in range(1, n // m + 1)
                )
                synthesis += (
                    inverse_coefficient(m)
                    * additive_weight(m)
                    * source_wavelet
                )
            assert prime_profile == synthesis, (
                "positive synthesis",
                n,
                j,
                prime_profile,
                synthesis,
            )
            synthesis_cases += 1

            ordinary_profile = sum(
                (
                    Fraction(PRIME_WEIGHT[p])
                    if (p := prime_power_base(q)) is not None
                    else Fraction(0)
                )
                * carry(n, q, j)
                for q in range(2, n + 1)
            )
            digital_correction = sum(
                Fraction(PRIME_WEIGHT[2])
                * (1 + Fraction(1, 2**r))
                * carry(n, 2**r, j)
                for r in range(1, n.bit_length())
                if 2**r <= n
            )
            assert prime_profile == ordinary_profile + digital_correction, (
                "digital correction",
                n,
                j,
            )
            digital_cases += 1

    return {"cases": synthesis_cases}, {"cases": digital_cases}


def build_result() -> dict[str, object]:
    inverse, generalized = check_inverse_and_lambda()
    synthesis, digital = check_positive_synthesis()
    return {
        "schema": "X-26903-positive-wavelet-synthesis-v1",
        "checks": {
            "positive_inverse_convolution": inverse,
            "generalized_von_mangoldt_convolution": generalized,
            "positive_wavelet_synthesis": synthesis,
            "digital_prime_correction": digital,
        },
        "scope": (
            "exact formal additive-weight algebra only; no asymptotic reserve "
            "threshold, physical transference, DSS, or RH"
        ),
    }


def main() -> None:
    result = build_result()
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(("proof-object digest mismatch", digest, EXPECTED_SHA256))
    result["sha256_without_digest"] = digest
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "positive-synthesis-verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
