#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json
from pathlib import Path


@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        other = as_i(other)
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(value):
    if isinstance(value, I):
        return value
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return I(value, value)


DEN = 10**80


@lru_cache(maxsize=None)
def sqrt_q(value):
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


@lru_cache(maxsize=None)
def invsqrt(n: int):
    return 1 / sqrt_q(Fraction(n))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def directed_decimal(value: Fraction, places: int, upper: bool) -> str:
    if value < 0:
        raise ValueError("only positive displays are used")
    scale = 10**places
    quotient, remainder = divmod(value.numerator * scale, value.denominator)
    if upper and remainder:
        quotient += 1
    return f"{quotient // scale}.{quotient % scale:0{places}d}"


def euler_support_bound(primes: tuple[int, ...]) -> I:
    product = I(Fraction(1), Fraction(1))
    for q in primes:
        product *= 1 + invsqrt(q)
    return 2 * (4 * sqrt_q(Fraction(67)) - 3) * product


def certify():
    primes_79 = tuple(n for n in range(2, 80) if is_prime(n))
    primes_61 = tuple(n for n in primes_79 if n <= 61)

    assert primes_79 == (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
    )
    assert len(primes_61) == 18

    bound_79 = euler_support_bound(primes_79)
    bound_61 = euler_support_bound(primes_61)

    assert bound_79.hi < 5600
    assert bound_61.hi < 3600

    result = {
        "classification": "PASS_FINITE_EULER_FRONTIER_SUMMABILITY",
        "checks": 4,
        "support": {
            "P79_prime_count": len(primes_79),
            "P61_prime_count": len(primes_61),
        },
        "P79": {
            "directed_lower_decimal": directed_decimal(
                bound_79.lo, places=18, upper=False
            ),
            "directed_upper_decimal": directed_decimal(
                bound_79.hi, places=18, upper=True
            ),
            "certified_below": 5600,
        },
        "P61": {
            "directed_lower_decimal": directed_decimal(
                bound_61.lo, places=18, upper=False
            ),
            "directed_upper_decimal": directed_decimal(
                bound_61.hi, places=18, upper=True
            ),
            "certified_below": 3600,
        },
        "formula": (
            "2*(4*sqrt(67)-3)*product_{q|P}(1+q^(-1/2)); "
            "all square roots use directed rational enclosures."
        ),
        "scope": (
            "This replay certifies only the explicit finite Euler-product "
            "constants in L-91554. The parent-index support, Hall coefficient "
            "domination, score telescope, physical capacity assembly, and RH "
            "implication are mathematical interfaces requiring independent "
            "reconstruction."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    certify()
