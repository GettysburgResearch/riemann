"""Exact arithmetic helpers for the primitive core-wavelet replay."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd

EXCEPTIONAL_PRIME = 67


def validate_positive_integer(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")


@lru_cache(maxsize=None)
def factorization(value: int) -> tuple[tuple[int, int], ...]:
    validate_positive_integer(value)
    factors: list[tuple[int, int]] = []
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


@lru_cache(maxsize=None)
def mobius(value: int) -> int:
    sign = 1
    for _, exponent in factorization(value):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


def is_squarefree(value: int) -> bool:
    return mobius(value) != 0


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


@lru_cache(maxsize=None)
def tau(value: int) -> int:
    result = 1
    for _, exponent in factorization(value):
        result *= exponent + 1
    return result


def validate_squarefree_67_free(value: int) -> None:
    validate_positive_integer(value)
    if value % EXCEPTIONAL_PRIME == 0 or not is_squarefree(value):
        raise ValueError("value must be squarefree and 67-free")


@dataclass(frozen=True)
class Radical:
    """An exact element of the finite Q-span of square-root monomials."""

    terms: tuple[tuple[int, Fraction], ...] = ()

    @staticmethod
    def _normalize(items: dict[int, Fraction]) -> "Radical":
        cleaned = tuple(sorted((rad, coeff) for rad, coeff in items.items() if coeff))
        for rad, _ in cleaned:
            if rad < 1 or not is_squarefree(rad):
                raise ValueError("radicands must be positive and squarefree")
        return Radical(cleaned)

    @staticmethod
    def rational(value: Fraction | int) -> "Radical":
        coefficient = Fraction(value)
        return Radical._normalize({1: coefficient})

    @staticmethod
    def sqrt(squarefree_value: int) -> "Radical":
        validate_squarefree_67_free(squarefree_value)
        return Radical._normalize({squarefree_value: Fraction(1)})

    @staticmethod
    def inv_sqrt(squarefree_value: int) -> "Radical":
        validate_squarefree_67_free(squarefree_value)
        return Radical._normalize(
            {squarefree_value: Fraction(1, squarefree_value)}
        )

    def as_dict(self) -> dict[int, Fraction]:
        return dict(self.terms)

    def __add__(self, other: "Radical") -> "Radical":
        result = self.as_dict()
        for rad, coeff in other.terms:
            result[rad] = result.get(rad, Fraction()) + coeff
        return Radical._normalize(result)

    def __sub__(self, other: "Radical") -> "Radical":
        return self + other.scale(-1)

    def scale(self, scalar: Fraction | int) -> "Radical":
        scalar = Fraction(scalar)
        return Radical._normalize({rad: scalar * coeff for rad, coeff in self.terms})

    def __mul__(self, other: "Radical") -> "Radical":
        result: dict[int, Fraction] = {}
        for left_rad, left_coeff in self.terms:
            for right_rad, right_coeff in other.terms:
                common = gcd(left_rad, right_rad)
                radicand = (left_rad // common) * (right_rad // common)
                coefficient = left_coeff * right_coeff * common
                result[radicand] = result.get(radicand, Fraction()) + coefficient
        return Radical._normalize(result)

    def json_terms(self) -> list[dict[str, object]]:
        return [
            {"coefficient": str(coefficient), "sqrt_radicand": radicand}
            for radicand, coefficient in self.terms
        ]

    def digest(self) -> str:
        payload = json.dumps(self.json_terms(), separators=(",", ":")).encode("ascii")
        return hashlib.sha256(payload).hexdigest()


ZERO = Radical()
