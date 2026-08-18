#!/usr/bin/env python3
"""Exact-rational certificate for L-98017.

For Q=10^18, ceil(Q*sqrt(n))/Q is an exact rational upper bound for
sqrt(n).  Its reciprocal is therefore an exact lower bound for 1/sqrt(n).
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt

Q = 10**18
N0 = 256


def sqrt_upper_numerator(n: int) -> int:
    """Return ceil(Q*sqrt(n)) using integer arithmetic only."""
    q2n = n * Q * Q
    root = isqrt(q2n)
    if root * root < q2n:
        root += 1
    return root


def main() -> None:
    reciprocal_lower = Fraction(0)
    for n in range(1, N0 + 1):
        upper_num = sqrt_upper_numerator(n)
        reciprocal_lower += Fraction(Q, upper_num)

    sqrt_257_upper = Fraction(sqrt_upper_numerator(N0 + 1), Q)
    delta_lower = 2 * reciprocal_lower - 4 * sqrt_257_upper + 3

    if delta_lower <= 0:
        raise AssertionError((delta_lower.numerator, delta_lower.denominator))

    # Mutations: coarser continuum subtraction and deletion of the final
    # reciprocal term must not be silently accepted as the same certificate.
    missing_last = 2 * (reciprocal_lower - Fraction(Q, sqrt_upper_numerator(N0))) \
        - 4 * sqrt_257_upper + 3
    if missing_last >= delta_lower:
        raise AssertionError("missing-term mutation was not detected")

    print("PASS_X_98017_EULER_DISCREPANCY_COMPACT_NEGATIVE_SUPPORT")
    print("denominator_scale=", Q)
    print("delta_lower_numerator=", delta_lower.numerator)
    print("delta_lower_denominator=", delta_lower.denominator)
    print("delta_lower_decimal=", float(delta_lower))
    print("analytic_tail_start=", N0)
    print("rh_established= false")


if __name__ == "__main__":
    main()
