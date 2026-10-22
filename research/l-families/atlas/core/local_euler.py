from __future__ import annotations

from fractions import Fraction
from math import isqrt
from typing import Iterable


def primes_up_to(bound: int) -> list[int]:
    if bound < 2:
        return []
    sieve = [True] * (bound + 1)
    sieve[0:2] = [False, False]
    for prime in range(2, isqrt(bound) + 1):
        if sieve[prime]:
            for multiple in range(prime * prime, bound + 1, prime):
                sieve[multiple] = False
    return [value for value, prime in enumerate(sieve) if prime]


def quadratic_character(value: int, modulus: int) -> int:
    residue = value % modulus
    if residue == 0:
        return 0
    symbol = pow(residue, (modulus - 1) // 2, modulus)
    return -1 if symbol == modulus - 1 else symbol


def count_weierstrass_points(prime: int, ainvs: Iterable[int]) -> int:
    """Count y^2+a1*x*y+a3*y=x^3+a2*x^2+a4*x+a6 over F_p."""
    a1, a2, a3, a4, a6 = tuple(ainvs)
    affine = 0
    for x in range(prime):
        right = (x**3 + a2 * x**2 + a4 * x + a6) % prime
        for y in range(prime):
            left = (y**2 + a1 * x * y + a3 * y) % prime
            affine += left == right
    return affine + 1


def elliptic_trace(prime: int, ainvs: Iterable[int]) -> int:
    return prime + 1 - count_weierstrass_points(prime, ainvs)


def moment(values: list[Fraction], exponent: int) -> Fraction:
    if not values:
        raise ValueError("moment requires at least one value")
    return sum((value**exponent for value in values), Fraction()) / len(values)


def normalized_even_moment_term(trace: int, prime: int, exponent: int, weight: int) -> Fraction:
    if exponent % 2:
        raise ValueError("only even moments remain rational in this exact pilot")
    return Fraction(trace**exponent, prime ** (weight * exponent // 2))
