#!/usr/bin/env python3
"""Finite reconnaissance for the target-root scalar TRP67.

This is not a proof of the infinite sign.  It checks both one-sided integer
states because the target kernel has a nonzero activation value at Y=1.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal


def mobius_sieve(n: int) -> list[int]:
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    mu[0] = 0
    primes: list[int] = []
    mu[1] = 1
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def value(x: int, a: Decimal, b: Decimal) -> Decimal:
    return D(4) * D(x).sqrt() * a - D(3) * b


def scan(limit: int) -> None:
    mu = mobius_sieve(limit)
    a = D(0)  # sum mu(n)/n
    b = D(0)  # sum mu(n)/sqrt(n)

    minimum = None
    minimum_state = None
    first_negative = None

    for n in range(1, limit + 1):
        left = value(n, a, b)
        if minimum is None or left < minimum:
            minimum = left
            minimum_state = (n, "left")
        if left < 0 and first_negative is None:
            first_negative = (n, "left", left)

        if mu[n]:
            a += D(mu[n]) / D(n)
            b += D(mu[n]) / D(n).sqrt()

        right = value(n, a, b)
        if right < minimum:
            minimum = right
            minimum_state = (n, "right")
        if right < 0 and first_negative is None:
            first_negative = (n, "right", right)

    print("TARGET_ROOT_FINITE_RECONNAISSANCE")
    print("limit=", limit)
    print("minimum_state=", minimum_state)
    print("minimum_value=", minimum)
    print("first_negative=", first_negative)
    print("rh_established= false")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1_000_000)
    args = parser.parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be positive")
    scan(args.limit)


if __name__ == "__main__":
    main()
