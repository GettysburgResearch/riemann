#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt, prod
import json
from pathlib import Path

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
NEXT_PRIME = 59
P = prod(PRIMES)
DEN = 10**50


def generate_divisors():
    values = [(1, 1)]
    for prime in PRIMES:
        values += [(d * prime, -sign) for d, sign in list(values)]
    return sorted(values)


def invsqrt_interval_num(value: int):
    if value == 1:
        return DEN, DEN
    lower = isqrt((DEN * DEN) // value)
    return lower, lower + 1


def sqrt_interval_num(value: int):
    if value == 1:
        return DEN, DEN
    lower = isqrt(value * DEN * DEN)
    return lower, lower + 1


def mobius_sieve(limit: int):
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes = []
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
    return mu, primes


def rough_divisors(value: int, primes):
    factors = []
    remainder = value
    for prime in primes:
        if prime * prime > remainder:
            break
        if remainder % prime == 0:
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            if prime >= NEXT_PRIME:
                factors.append((prime, exponent))
    if remainder > 1 and remainder >= NEXT_PRIME:
        factors.append((remainder, 1))

    divisors = [1]
    for prime, exponent in factors:
        old = divisors
        divisors = []
        for divisor in old:
            power = 1
            for _ in range(exponent + 1):
                divisors.append(divisor * power)
                power *= prime
    return divisors


def certify():
    divisors = generate_divisors()
    assert len(divisors) == 2 ** len(PRIMES)

    # A=sum mu(d)/d has common denominator P because every d divides P.
    a_numerator = 0
    # B=sum mu(d)/sqrt(d) is enclosed at the fixed denominator DEN.
    b_lower_numerator = 0
    b_upper_numerator = 0

    minimum = {1: None, 2: None}
    minimum_reserve_positive = None
    negative_cells = {1: 0, 2: 0}

    for index, (divisor, sign) in enumerate(divisors):
        a_numerator += sign * (P // divisor)
        lower, upper = invsqrt_interval_num(divisor)
        if sign == 1:
            b_lower_numerator += lower
            b_upper_numerator += upper
        else:
            b_lower_numerator -= upper
            b_upper_numerator -= lower

        right = divisors[index + 1][0] if index + 1 < len(divisors) else None
        for channel in (1, 2):
            # F(x)=channel*A*sqrt(x)-B. Its cell minimum is at the left
            # endpoint when A>=0 and at the right endpoint from the left when A<0.
            if a_numerator >= 0 or right is None:
                x = divisor
                sqrt_lower, _ = sqrt_interval_num(x)
                sqrt_used = sqrt_lower
            else:
                x = right
                _, sqrt_upper = sqrt_interval_num(x)
                sqrt_used = sqrt_upper

            lower_bound = (
                Fraction(channel * a_numerator * sqrt_used, P * DEN)
                - Fraction(b_upper_numerator, DEN)
            )
            if channel == 1 and x == 1:
                lower_bound = Fraction(0)

            record = (lower_bound, x, index)
            if minimum[channel] is None or lower_bound < minimum[channel][0]:
                minimum[channel] = record
            if channel == 1 and x >= 2:
                if minimum_reserve_positive is None or lower_bound < minimum_reserve_positive[0]:
                    minimum_reserve_positive = record
            if lower_bound < 0:
                negative_cells[channel] += 1

    assert negative_cells == {1: 0, 2: 0}
    assert minimum[1][0] == 0 and minimum[1][1] == 1
    assert minimum_reserve_positive[0] > Fraction(4142, 10000)
    assert minimum[2][0] > Fraction(3186, 10000)
    assert minimum[2][1] == 33

    # Coefficient-wise rough-prime renewal check.
    limit = 200000
    mu, primes = mobius_sieve(limit)
    coefficient_checks = 0
    for value in range(1, limit + 1):
        coefficient = sum(mu[value // divisor] for divisor in rough_divisors(value, primes))

        remainder = value
        has_large_prime = False
        for prime in primes:
            if prime * prime > remainder:
                break
            if remainder % prime == 0:
                if prime >= NEXT_PRIME:
                    has_large_prime = True
                while remainder % prime == 0:
                    remainder //= prime
        if remainder > 1 and remainder >= NEXT_PRIME:
            has_large_prime = True

        expected = 0 if has_large_prime else mu[value]
        assert coefficient == expected, (value, coefficient, expected)
        coefficient_checks += 1

    return {
        "classification": "PASS_FACTOR54_BOOLEAN_SHADOW_FORCING",
        "small_primes": PRIMES,
        "next_prime": NEXT_PRIME,
        "divisor_states": len(divisors),
        "product_P53": P,
        "reserve_global_minimum": {
            "lower": str(minimum[1][0]),
            "decimal": float(minimum[1][0]),
            "x": minimum[1][1],
        },
        "reserve_minimum_for_x_ge_2": {
            "lower": str(minimum_reserve_positive[0]),
            "decimal": float(minimum_reserve_positive[0]),
            "x": minimum_reserve_positive[1],
        },
        "equality_global_minimum": {
            "lower": str(minimum[2][0]),
            "decimal": float(minimum[2][0]),
            "x": minimum[2][1],
        },
        "rough_prime_renewal_coefficient_checks": coefficient_checks,
        "coefficient_check_limit": limit,
        "scope": (
            "All sign assertions use exact integer/Fraction arithmetic and "
            "directed fixed-denominator square-root enclosures. The renewal "
            "replay is coefficient-wise integer arithmetic."
        ),
    }


if __name__ == "__main__":
    result = certify()
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
