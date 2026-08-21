#!/usr/bin/env python3
"""Exact dyadic-interval certificate for R-100705."""

from fractions import Fraction
from math import isqrt

BITS = 120
SCALE = 1 << BITS
P = 67
LATER = (71, 73, 79, 83, 89, 97, 101, 103, 107)
Y = 5500


def sqrt_interval(q):
    if q == 0:
        return Fraction(0), Fraction(0)
    integer = (q.numerator * SCALE * SCALE) // q.denominator
    root = isqrt(integer)
    return Fraction(root, SCALE), Fraction(root + 1, SCALE)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(values), max(values)


def scale(a, c):
    return mul(a, (c, c))


def divide_positive(a, c):
    assert c > 0
    return a[0] / c, a[1] / c


def invsqrt_integer(n):
    lo, hi = sqrt_interval(Fraction(n))
    return Fraction(1, 1) / hi, Fraction(1, 1) / lo


def critical_kernel(y):
    if y <= 1:
        value = 16 * y
        return value, value
    root = sqrt_interval(y)
    return add(scale(root, Fraction(32)), (Fraction(-16), Fraction(-16)))


def normalized_transition(y, p):
    # [(p^-1 U_(p^2)) -(1+p^-1)p^-1/2 U_p + p^-1 I]/(1-p^-2)
    out = scale(critical_kernel(y / (p * p)), Fraction(1, p))
    middle_coefficient = mul(
        (Fraction(1) + Fraction(1, p),) * 2,
        invsqrt_integer(p),
    )
    out = sub(out, mul(middle_coefficient, critical_kernel(y / p)))
    out = add(out, scale(critical_kernel(y), Fraction(1, p)))
    return divide_positive(out, Fraction(1) - Fraction(1, p * p))


def completed_transition():
    total = (Fraction(0), Fraction(0))
    count = len(LATER)
    for mask in range(1 << count):
        product = 1
        parity = 0
        for i, prime in enumerate(LATER):
            if (mask >> i) & 1:
                product *= prime
                parity ^= 1
        coefficient = invsqrt_integer(product)
        if parity:
            coefficient = neg(coefficient)
        term = normalized_transition(Fraction(Y, product), P)
        total = add(total, mul(coefficient, term))
    return total


def main():
    lower, upper = completed_transition()
    assert upper < 0
    # Simple rational decimal barriers used in the theorem statement.
    assert lower > Fraction(-469702012716840, 10**16)
    assert upper < Fraction(-469702012716839, 10**16)
    print("PASS_R_100705_NINE_PRIME_TRANSITION_SEPARATOR")
    print("upper_bound_is_negative=true")
    print("rh_established=false")


if __name__ == "__main__":
    main()
