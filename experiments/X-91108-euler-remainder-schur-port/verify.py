#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(100000)

class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        assert not (other.lo <= 0 <= other.hi)
        return self * Interval(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_interval(other) / self


def as_interval(value):
    return value if isinstance(value, Interval) else Interval(value)


DEN = 10**90


def sqrt_interval(value):
    value = Fraction(value)
    assert value >= 0
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return Interval(Fraction(root, DEN), Fraction(root + 1, DEN))


def inverse_sqrt_interval(n):
    return 1 / sqrt_interval(n)


def eta_euler_lower(terms=16):
    total = Interval(0)
    smallest_difference = None
    for order in range(terms):
        difference = Interval(0)
        for k in range(order + 1):
            difference += (
                (-1) ** k
                * comb(order, k)
                * inverse_sqrt_interval(k + 1)
            )
        assert difference.lo > 0
        if smallest_difference is None:
            smallest_difference = difference.lo
        else:
            smallest_difference = min(smallest_difference, difference.lo)
        total += difference / 2 ** (order + 1)
    return total, smallest_difference


def main():
    eta, smallest_difference = eta_euler_lower(16)
    sqrt2 = sqrt_interval(2)

    # c=-zeta(1/2)=eta(1/2)/(sqrt(2)-1).
    c_lower = eta.lo / (sqrt2.hi - 1)
    sharp_cell_one_threshold = (10 * sqrt2.hi - 1) / 9

    assert c_lower > sharp_cell_one_threshold
    assert c_lower > Fraction(5, 4)
    assert c_lower > Fraction(17, 16)
    assert c_lower > sqrt2.hi

    # The N>=2 cell inequality used in L-91316 reduces to its N=2 gate.
    assert 30 * sqrt2.lo > 40

    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)

    endpoint_mass = Fraction(1)
    for p in primes:
        endpoint_mass *= Fraction(p + 1, p)

    assert endpoint_mass < Fraction(9, 2)
    off_diagonal_mass = Fraction(8, 9) * endpoint_mass
    assert off_diagonal_mass < 4

    # Directed checks of beta_Q Gamma_Q = product_p(1-1/p).
    tested_cube_sizes = []
    for subset in (primes[:1], primes[:3], primes[:8], primes):
        beta = Interval(1)
        gamma = Interval(1)
        delta = Fraction(1)
        for p in subset:
            r = inverse_sqrt_interval(p)
            beta *= 1 - r
            gamma *= 1 + r
            delta *= Fraction(p - 1, p)
        product = beta * gamma
        assert product.lo <= delta <= product.hi
        assert beta.lo > 0
        assert gamma.lo > 0
        tested_cube_sizes.append(len(subset))

    result = {
        "classification": "PASS_EULER_REMAINDER_SCHUR_PORT_AND_POSITIVE_CUBES",
        "eta_euler_terms": 16,
        "eta_lower": float(eta.lo),
        "smallest_positive_euler_difference_lower": float(smallest_difference),
        "zeta_half_abs_lower": float(c_lower),
        "sharp_cell_one_threshold_upper": float(sharp_cell_one_threshold),
        "strict_threshold_margin_lower": float(
            c_lower - sharp_cell_one_threshold
        ),
        "small_prime_endpoint_mass": {
            "exact": f"{endpoint_mass.numerator}/{endpoint_mass.denominator}",
            "decimal": float(endpoint_mass),
            "upper": "9/2",
        },
        "off_diagonal_mass_bound": {
            "exact": (
                f"{off_diagonal_mass.numerator}/"
                f"{off_diagonal_mass.denominator}"
            ),
            "decimal": float(off_diagonal_mass),
            "upper": "4",
        },
        "tested_boolean_cube_sizes": tested_cube_sizes,
        "scope": (
            "Exact Fraction arithmetic with directed rational square-root "
            "enclosures. The script certifies the sharp N=1 zeta-half gate, "
            "the finite endpoint-mass corridor, and representative exact "
            "Euler-cube products. The all-cell and general-cube identities "
            "are proved analytically in L-91316 and L-91317."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
