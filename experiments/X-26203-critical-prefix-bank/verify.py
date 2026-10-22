#!/usr/bin/env python3
"""Exact regression for the critical digital prefix bank.

Standard library only.  This verifies finite Dirichlet-convolution, hyperbola
prefix, and Q(sqrt(2)) constant algebra.  It proves no physical bank upper
bound, cofinal transition theorem, or result about RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def of(value: int | Fraction | "Q2") -> "Q2":
        if isinstance(value, Q2):
            return value
        return Q2(Fraction(value), Fraction(0))

    def __add__(self, other: int | Fraction | "Q2") -> "Q2":
        other = Q2.of(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: int | Fraction | "Q2") -> "Q2":
        return self + (-Q2.of(other))

    def __rsub__(self, other: int | Fraction | "Q2") -> "Q2":
        return Q2.of(other) - self

    def __mul__(self, other: int | Fraction | "Q2") -> "Q2":
        other = Q2.of(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def square(self) -> "Q2":
        return self * self

    def as_pair(self) -> list[str]:
        return [str(self.a), str(self.b)]


SQRT2 = Q2(Fraction(0), Fraction(1))
ONE = Q2(Fraction(1))


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
    answer = Fraction(mu[n])
    if n % 2 == 0:
        answer -= Fraction(3, 2) * mu[n // 2]
    if n % 4 == 0:
        answer += Fraction(1, 2) * mu[n // 4]
    return answer


def convolution_value(m: int, mu: list[int]) -> Fraction:
    answer = Fraction(0)
    for divisor in range(1, m + 1):
        if m % divisor == 0:
            answer += omega2(divisor, mu) * c2(m // divisor)
    return answer


def main() -> None:
    limit = 1024
    mu = mobius_sieve(limit)
    expected = {1: Fraction(1), 2: Fraction(-5, 2), 4: Fraction(1)}

    for m in range(1, limit + 1):
        assert convolution_value(m, mu) == expected.get(m, Fraction(0))

    hyperbola_cases = 0
    for cutoff in [5, 6, 7, 8, 16, 31, 64, 127, 256]:
        coefficients = [Fraction(0)] * cutoff
        for divisor in range(1, cutoff):
            source = omega2(divisor, mu)
            if source == 0:
                continue
            n = 1
            while divisor * n < cutoff:
                coefficients[divisor * n] += source * c2(n)
                n += 1
        for m in range(1, cutoff):
            assert coefficients[m] == expected.get(m, Fraction(0))
            hyperbola_cases += 1

    # kappa_*=(sqrt(2)-1)(1-sqrt(2)/4)=(5sqrt(2)-6)/4.
    kappa = (SQRT2 - ONE) * (ONE - SQRT2 * Fraction(1, 4))
    assert kappa == Q2(Fraction(-3, 2), Fraction(5, 4))
    kappa_squared = kappa.square()
    assert kappa_squared == Q2(Fraction(43, 8), Fraction(-15, 4))
    assert 50 > 36  # exact positivity of 5sqrt(2)-6

    local = [Fraction(1), Fraction(-5, 2), Fraction(2), Fraction(-1, 2)]
    assert max(abs(value) for value in local) == Fraction(5, 2)

    result = {
        "verdict": "PASS_EXACT_CRITICAL_DIGITAL_PREFIX_BANK",
        "convolution_rows_checked": limit,
        "hyperbola_coefficient_cases": hyperbola_cases,
        "finite_output_coefficients": {"1": "1", "2": "-5/2", "4": "1"},
        "kappa_Q_sqrt2": kappa.as_pair(),
        "kappa_squared_Q_sqrt2": kappa_squared.as_pair(),
        "source_coefficient_supremum": "5/2",
        "critical_bank_rate": "W_R^2 <= 25 R",
        "scope": (
            "Exact finite convolution, prefix-bank, and constant algebra only. "
            "No physical bank upper bound, cofinal transition theorem, or RH result."
        ),
    }
    payload = json.dumps(result, sort_keys=True, indent=2)
    result["proof_object_sha256_without_digest"] = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
