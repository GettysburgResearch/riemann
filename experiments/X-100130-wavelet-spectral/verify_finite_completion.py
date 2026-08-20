#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from math import prod

VERDICT = "PASS_R100131_FINITE_POSITIVE_COMPLETION_ISOLATION"


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def primes() -> list[int]:
    out = []
    n = 2
    while len(out) < 30:
        if all(n % p for p in range(2, int(n**0.5) + 1)):
            out.append(n)
        n += 1
    return out


def support_distinct(n: int) -> int:
    return len(factor(n))


def abstract_A(k: int, n: int) -> F:
    """A positive fixture with the only property needed by the proof."""
    if support_distinct(n) > k:
        return F(0)
    fs = factor(n)
    if len(fs) != k or any(e != 1 for e in fs.values()):
        return F(0)
    return F(1)


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return ds


def main() -> None:
    D = (1, 2, 6, 25, 42)
    coeff = {1: F(3), 2: F(5, 2), 6: F(7), 25: F(11, 3), 42: F(13, 5)}
    plist = primes()
    checks = 0

    for k in range(1, 5):
        fresh = [p for p in plist if all(d % p for d in D)]
        R = prod(fresh[:k])
        for d in D:
            n = d * R
            value = F(0)
            survivors = []
            for e in divisors(n):
                if e in coeff:
                    term = coeff[e] * abstract_A(k, n // e)
                    if term:
                        survivors.append(e)
                    value += term
            assert survivors == [d], (k, d, survivors)
            assert value == coeff[d]
            assert value >= 0
            checks += 1

    # A negative multiplier coefficient is exposed at its fresh-prime test.
    bad = dict(coeff)
    bad[25] = F(-1)
    for k in (1, 2, 3):
        fresh = [p for p in plist if all(d % p for d in D)]
        R = prod(fresh[:k])
        n = 25 * R
        value = sum((bad.get(e, F(0)) * abstract_A(k, n // e) for e in divisors(n)), F(0))
        assert value == -1
        assert value < 0

    print(VERDICT)
    print(f"isolation_checks={checks}")


if __name__ == "__main__":
    main()
