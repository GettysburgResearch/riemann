"""Arithmetic helpers for relative-first Adams replay."""

from __future__ import annotations

from functools import lru_cache


def validate_positive_integer(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")


@lru_cache(maxsize=None)
def factorization(value: int) -> tuple[tuple[int, int], ...]:
    validate_positive_integer(value)
    result: list[tuple[int, int]] = []
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            result.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        result.append((remaining, 1))
    return tuple(result)


@lru_cache(maxsize=None)
def mobius(value: int) -> int:
    sign = 1
    for _, exponent in factorization(value):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


@lru_cache(maxsize=None)
def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value)
    result = [1]
    for prime, exponent in factorization(value):
        old = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= prime
            result.extend(item * power for item in old)
    return tuple(sorted(result))


def omega(value: int) -> int:
    return len(factorization(value))
