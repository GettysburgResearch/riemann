#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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
        values = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(value) -> I:
    if isinstance(value, I):
        return value
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return I(value, value)


DEN = 10**80
ROOT_LO = Fraction(1844367547103, 10**14)
WINDOW_X_MAX = 1 / ROOT_LO


def sqrt_q(value: Fraction) -> I:
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            if prime > least[n] or prime * n > limit:
                break
            least[prime * n] = prime
            if n % prime == 0:
                mu[prime * n] = 0
                break
            mu[prime * n] = -mu[n]
    return mu


MU = mobius_sieve(55)


def prefixes(active_max: int) -> tuple[Fraction, I]:
    b = Fraction(0)
    a = I(Fraction(0), Fraction(0))
    for n in range(1, active_max + 1):
        if MU[n] == 0:
            continue
        b += Fraction(MU[n], n)
        a += MU[n] / sqrt_q(Fraction(n))
    return b, a


def main() -> None:
    maximum_l = None
    minimum_r_after_two = None

    # Each state is affine in sqrt(x) on a cell with fixed active support, so
    # the extrema occur at one-sided cell endpoints.
    for active_max in range(1, 55):
        b, a = prefixes(active_max)
        right = Fraction(active_max + 1) if active_max < 54 else WINDOW_X_MAX
        for x in (Fraction(active_max), right):
            root = sqrt_q(x)
            l_value = 2 * root * b - a
            r_value = root * b - a

            assert l_value.hi < Fraction(183, 100), (
                active_max,
                x,
                l_value,
            )
            assert r_value.lo >= 0, (
                active_max,
                x,
                r_value,
            )
            if x >= 2:
                assert r_value.lo > Fraction(41, 100), (
                    active_max,
                    x,
                    r_value,
                )

            if maximum_l is None or l_value.hi > maximum_l[0]:
                maximum_l = (l_value.hi, active_max, x)
            if x >= 2 and (
                minimum_r_after_two is None
                or r_value.lo < minimum_r_after_two[0]
            ):
                minimum_r_after_two = (r_value.lo, active_max, x)

    assert maximum_l is not None
    assert minimum_r_after_two is not None
    result = {
        "classification": "PASS_FACTOR54_EQUALITY_RESERVE_WINDOW_BOUNDS",
        "equality_weight_upper": {
            "upper": float(maximum_l[0]),
            "cell_N": maximum_l[1],
            "x": float(maximum_l[2]),
            "certified_below": 1.83,
        },
        "reserve_lower_for_x_at_least_2": {
            "lower": float(minimum_r_after_two[0]),
            "cell_N": minimum_r_after_two[1],
            "x": float(minimum_r_after_two[2]),
            "certified_above": 0.41,
        },
        "reserve_nonnegative_on_full_window": True,
        "window_x_upper": float(WINDOW_X_MAX),
        "scope": (
            "All assertions use exact Fraction arithmetic and directed rational "
            "square-root enclosures. Decimal fields are readable summaries only."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "window_bounds.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
