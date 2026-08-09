#!/usr/bin/env python3
"""Exact witness for R-90004.

Uses only integer arithmetic and fractions.Fraction.
"""
from fractions import Fraction

X = 1000
N = 21
P = 21


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    primes: list[int] = []
    composite = [False] * (limit + 1)
    mu[1] = 1
    for i in range(2, limit + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for prime in primes:
            value = i * prime
            if value > limit:
                break
            composite[value] = True
            if i % prime == 0:
                mu[value] = 0
                break
            mu[value] = -mu[i]
    return mu


def first_entrance_weight() -> list[Fraction]:
    f = [Fraction(0) for _ in range(X + 1)]
    f[P] = Fraction(P)
    for m in range(2 * N, X + 1):
        a2 = m // 2
        b2 = m - a2
        a3 = (m + 2) // 3
        b3 = m - a3
        f[m] = (f[a2] + f[b2] + f[a3] + f[b3]) / 2
    return f


def transformed_kernel(f: list[Fraction], mu: list[int]) -> list[Fraction]:
    c = [Fraction(0) for _ in range(X + 1)]
    for m in range(1, X + 1):
        c[m] = f[m] - f[m - 1]
    kernel = [Fraction(0) for _ in range(X + 1)]
    for d in range(1, X + 1):
        if not c[d]:
            continue
        for k in range(1, X // d + 1):
            if mu[k]:
                kernel[d * k] += c[d] * mu[k]
    return kernel


def prefix(values: list[Fraction]) -> list[Fraction]:
    result: list[Fraction] = []
    total = Fraction(0)
    for value in values:
        total += value
        result.append(total)
    return result


def main() -> None:
    mu = mobius_sieve(X)
    kernel = transformed_kernel(first_entrance_weight(), mu)
    cumulative = kernel
    expected = [
        (Fraction(-441, 8), 913),
        (Fraction(-86331, 64), 703),
        (Fraction(-15781689, 256), 752),
        (Fraction(-21060753, 8), 841),
        (Fraction(-1208117841, 128), 902),
        (Fraction(0), 0),
    ]
    observed = []
    for order in range(1, 7):
        cumulative = prefix(cumulative)
        minimum = min(cumulative)
        location = cumulative.index(minimum)
        observed.append((minimum, location))
        if observed[-1] != expected[order - 1]:
            raise AssertionError(
                f"order {order}: expected {expected[order - 1]}, got {observed[-1]}"
            )
    assert cumulative[841] >= 0  # order six is not the claimed witness
    assert observed[3] == (Fraction(-21060753, 8), 841)
    print("PASS_EXACT_GFEP_FOURFOLD_CUMULATIVE_REFUTATION")
    for order, (minimum, location) in enumerate(observed, 1):
        print(order, location, minimum)


if __name__ == "__main__":
    main()
