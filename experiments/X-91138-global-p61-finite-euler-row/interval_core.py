from __future__ import annotations

from fractions import Fraction
from math import isqrt

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)
MAX_J = 66
DILATION = 67
MAX_BASE = DILATION * MAX_J
DEN = 10**28
LOG_TERMS = 34


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def floor_scaled(x: Fraction, scale: int) -> int:
    return (x.numerator * scale) // x.denominator


def ceil_scaled(x: Fraction, scale: int) -> int:
    return ceil_div(x.numerator * scale, x.denominator)


def base_log_interval(y: Fraction) -> tuple[Fraction, Fraction]:
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for k in range(LOG_TERMS):
        partial += power / Fraction(2 * k + 1)
        power *= z2
    partial *= 2
    tail = 2 * power / (Fraction(2 * LOG_TERMS + 1) * (1 - z2))
    return partial, partial + tail


def build_log_intervals(max_n: int) -> list[tuple[int, int]]:
    log2_lo, log2_hi = base_log_interval(Fraction(2))
    out = [(0, 0)] * (max_n + 1)
    for n in range(1, max_n + 1):
        exponent = n.bit_length() - 1
        y = Fraction(n, 1 << exponent)
        lo, hi = base_log_interval(y)
        lo += exponent * log2_lo
        hi += exponent * log2_hi
        out[n] = floor_scaled(lo, DEN), ceil_scaled(hi, DEN)
    return out


def build_inverse_sqrt_intervals(max_n: int) -> list[tuple[int, int]]:
    out = [(0, 0)] * (max_n + 1)
    den2 = DEN * DEN
    for n in range(1, max_n + 1):
        sqrt_lo = isqrt(n * den2)
        sqrt_hi = sqrt_lo if sqrt_lo * sqrt_lo == n * den2 else sqrt_lo + 1
        out[n] = den2 // sqrt_hi, ceil_div(den2, sqrt_lo)
    return out


def mul_interval(x_lo: int, x_hi: int, y_lo: int, y_hi: int) -> tuple[int, int]:
    values = (x_lo * y_lo, x_lo * y_hi, x_hi * y_lo, x_hi * y_hi)
    return min(values), max(values)


def rational_mul_interval(
    lo: int, hi: int, numerator: int, denominator: int
) -> tuple[int, int]:
    if numerator >= 0:
        return (numerator * lo) // denominator, ceil_div(numerator * hi, denominator)
    return (numerator * hi) // denominator, ceil_div(numerator * lo, denominator)


def squarefree_divisors() -> list[tuple[int, int]]:
    divisors = [(1, 1)]
    for prime in PRIMES:
        divisors += [(d * prime, -mu) for d, mu in divisors.copy()]
    return sorted(divisors)


def add_signed(
    acc_lo: int, acc_hi: int, term_lo: int, term_hi: int, sign: int
) -> tuple[int, int]:
    if sign > 0:
        return acc_lo + term_lo, acc_hi + term_hi
    return acc_lo - term_hi, acc_hi - term_lo
