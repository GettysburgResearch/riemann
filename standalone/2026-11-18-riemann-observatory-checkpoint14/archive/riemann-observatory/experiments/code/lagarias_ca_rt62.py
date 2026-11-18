#!/usr/bin/env python3
"""Independent Decimal interval replay of the shared CA support certificate."""

from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from math import isqrt

PRECISION = 65
NEAREST = Context(prec=PRECISION, rounding=ROUND_HALF_EVEN)
LOW = Context(prec=PRECISION, rounding=ROUND_FLOOR)
HIGH = Context(prec=PRECISION, rounding=ROUND_CEILING)
SCALE = 10**PRECISION


def log_bounds(lower, upper):
    # Decimal's ln is correctly rounded to nearest. Widen by one context ulp.
    return NEAREST.next_minus(NEAREST.ln(lower)), NEAREST.next_plus(NEAREST.ln(upper))


def exp_bounds(lower, upper):
    return NEAREST.next_minus(NEAREST.exp(lower)), NEAREST.next_plus(NEAREST.exp(upper))


def threshold(prime, exponent):
    numerator = Decimal(prime ** (exponent + 1) - 1)
    denominator = Decimal(prime * (prime**exponent - 1))
    ratio_lower = LOW.divide(numerator, denominator)
    ratio_upper = HIGH.divide(numerator, denominator)
    numerator_lower, numerator_upper = log_bounds(ratio_lower, ratio_upper)
    denominator_lower, denominator_upper = log_bounds(Decimal(prime), Decimal(prime))
    assert numerator_lower > 0 and denominator_lower > 0
    return (
        LOW.divide(numerator_lower, denominator_upper),
        HIGH.divide(numerator_upper, denominator_lower),
    )


def divisor_sum(n):
    total = 0
    for divisor in range(1, isqrt(n) + 1):
        other, remainder = divmod(n, divisor)
        if remainder == 0:
            total += divisor
            if divisor != other:
                total += other
    return total


def gap_bounds(n, harmonic_floor):
    harmonic_lower = LOW.divide(Decimal(harmonic_floor), Decimal(SCALE))
    harmonic_upper = HIGH.divide(Decimal(harmonic_floor + n), Decimal(SCALE))
    log_lower, log_upper = log_bounds(harmonic_lower, harmonic_upper)
    exp_lower, exp_upper = exp_bounds(harmonic_lower, harmonic_upper)
    assert log_lower > 0 and exp_lower > 0
    rhs_lower = LOW.add(harmonic_lower, LOW.multiply(exp_lower, log_lower))
    rhs_upper = HIGH.add(harmonic_upper, HIGH.multiply(exp_upper, log_upper))
    sigma = Decimal(divisor_sum(n))
    return LOW.subtract(rhs_lower, sigma), HIGH.subtract(rhs_upper, sigma)


def main():
    if not __debug__:
        raise RuntimeError("certificate checks require Python assertions")
    epsilon_lower, epsilon_upper = threshold(13, 1)
    for prime, exponent in [(2, 4), (3, 2), (5, 1), (7, 1), (11, 1)]:
        assert threshold(prime, exponent)[0] > epsilon_upper
        assert threshold(prime, exponent + 1)[1] < epsilon_lower
    assert threshold(13, 2)[1] < epsilon_lower
    assert threshold(17, 1)[1] < epsilon_lower

    floors = {55440: 9051, 720720: 143828}
    harmonic_floor = 0
    for n in range(1, max(floors) + 1):
        harmonic_floor += SCALE // n
        if n in floors:
            lower, upper = gap_bounds(n, harmonic_floor)
            assert floors[n] < lower <= upper < floors[n] + 1
            print(f"{n}: sigma={divisor_sum(n)}, gap in [{lower}, {upper}]")
    print(f"epsilon in [{epsilon_lower}, {epsilon_upper}]")


if __name__ == "__main__":
    main()
