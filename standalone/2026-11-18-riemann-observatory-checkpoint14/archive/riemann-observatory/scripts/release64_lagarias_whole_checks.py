#!/usr/bin/env python3
"""Independent Arb checks of Lagarias's finite range, rounded Robin bound and Table 1."""

from collections import Counter
from math import isqrt, prod

from flint import arb, ctx


CAP = 10**18
PRINTED_FACTORIZATIONS = (
    (1,), (1,1), (2,1), (2,1,1), (3,1,1), (3,2,1), (3,2,1,1), (4,2,1,1),
    (4,2,1,1,1), (4,2,1,1,1,1), (5,2,1,1,1,1), (5,3,1,1,1,1),
    (5,3,2,1,1,1), (5,3,2,1,1,1,1), (5,3,2,1,1,1,1,1), (5,3,2,1,1,1,1,1,1),
    (6,3,2,1,1,1,1,1,1), (6,3,2,1,1,1,1,1,1,1), (6,3,2,1,1,1,1,1,1,1,1),
    (6,3,2,2,1,1,1,1,1,1,1), (6,4,2,2,1,1,1,1,1,1,1), (6,4,2,2,1,1,1,1,1,1,1,1),
)
PRINTED_MILLI_RATIOS = (
    1500, 2000, 2333, 2800, 3000, 3250, 3714, 3838, 4187, 4509, 4581,
    4699, 4855, 5141, 5412, 5647, 5692, 5888, 6078, 6187, 6238, 6407,
)
PRINTED_TABLE = (
    2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720, 1441440, 4324320, 21621600,
    367567200, 6983776800, 160626866400, 321253732800, 9316358251200, 288807105787200,
    2021649740510400, 6064949221531200, 224403121196654400,
)


def sigma(n):
    total = 0
    for divisor in range(1, isqrt(n) + 1):
        quotient, remainder = divmod(n, divisor)
        if remainder == 0:
            total += divisor if divisor == quotient else divisor + quotient
    return total


def finite_inequalities():
    harmonic = arb(1)
    assert sigma(1) == 1 and harmonic + harmonic.exp() * harmonic.log() == arb(1)
    min_gap = None
    for n in range(2, 5042):
        harmonic += 1 / arb(n)
        exponential_gap = harmonic.exp() * harmonic.log() - sigma(n)
        gap = harmonic + exponential_gap
        if n == 60:
            assert exponential_gap < 0
            print(f"Kaneko strict exponential-only gap n=60: {exponential_gap}")
        if n > 60:
            assert exponential_gap > 0, (n, exponential_gap)
        assert gap > 0, (n, gap)
        if n == 2:
            min_gap = gap
        else:
            assert gap > min_gap, (n, gap, min_gap)
        if n in (2, 19, 20, 5040, 5041):
            print(f"Lagarias gap n={n}: {gap}")
    print("Smallest certified finite gap occurs at n=2.")
    loglog12 = arb(12).log().log()
    k = (arb(sigma(12)) / 12 - arb.const_euler().exp() * loglog12) * loglog12
    assert k > arb("0.6482") and k < arb("0.6483")
    print(f"Robin equality constant at n=12: {k}")


def prime_prefix():
    primorial = 1
    p = 1
    while primorial <= CAP:
        p += 1
        if all(p % d for d in range(2, isqrt(p) + 1)):
            primorial *= p
            yield p


def ca_table():
    thresholds = []
    for p in prime_prefix():
        a = 1
        power = p
        partial_sum = p
        while True:
            critical_epsilon = (1 + 1 / arb(partial_sum)).log() / arb(p).log()
            thresholds.append((critical_epsilon, p, a))
            if power > CAP:
                break
            a += 1
            power *= p
            partial_sum += power
    # The midpoint only proposes an order. Strict ball comparisons certify it.
    thresholds.sort(key=lambda item: item[0].mid(), reverse=True)
    assert all(left[0] > right[0] for left, right in zip(thresholds, thresholds[1:]))
    n = 1
    exponents = Counter()
    observed = []
    for _, prime, _ in thresholds:
        n *= prime
        if n > CAP:
            print(f"First crossing of 10^18: {n}")
            break
        exponents[prime] += 1
        factorization = tuple(exponents[p] for p in sorted(exponents))
        divisor_sum = prod((p**(exponent + 1) - 1) // (p - 1) for p, exponent in exponents.items())
        milli_ratio = (1000 * divisor_sum) // n
        observed.append((n, factorization, milli_ratio))
    assert len(PRINTED_TABLE) == len(PRINTED_FACTORIZATIONS) == len(PRINTED_MILLI_RATIOS)
    assert observed == list(zip(PRINTED_TABLE, PRINTED_FACTORIZATIONS, PRINTED_MILLI_RATIOS))
    print(f"All {len(observed)} Table 1 integers, factorizations, and truncated sigma(n)/n ratios reproduced.")


if __name__ == "__main__":
    ctx.prec = 192
    finite_inequalities()
    ca_table()
