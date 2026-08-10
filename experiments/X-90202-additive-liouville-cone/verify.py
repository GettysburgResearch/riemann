#!/usr/bin/env python3
"""Exact Fraction replay for L-90202."""
from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"


def factorization(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def squarefree_divisors(primes: list[int]) -> list[int]:
    out = [1]
    for p in primes:
        out += [p * d for d in list(out)]
    return out


def prime_cost(p: int) -> Fraction:
    return Fraction((11 * p + 7) % 19 + 1, (5 * p + 3) % 13 + 2)


def additive_value(n: int) -> Fraction:
    return sum((a * prime_cost(p) for p, a in factorization(n).items()), Fraction(0))


def direct(n: int, x: dict[int, Fraction]) -> Fraction:
    fac = factorization(n)
    primes = list(fac)
    total = Fraction(0)
    for d in squarefree_divisors(primes):
        f = Fraction(1)
        for p in primes:
            if d % p == 0:
                f *= x[p]
        total += f * additive_value(n // d)
    return total


def formula(n: int, x: dict[int, Fraction]) -> Fraction:
    fac = factorization(n)
    primes = list(fac)
    y = {p: (1 + x[p]) / 2 for p in primes}
    first = Fraction(0)
    for q in primes:
        mon = Fraction(1)
        for p in primes:
            if p != q:
                mon *= y[p]
        first += prime_cost(q) * mon
    first *= 2 ** (len(primes) - 1)
    all_mon = Fraction(1)
    for p in primes:
        all_mon *= y[p]
    second = (2 ** len(primes)) * (additive_value(n) - additive_value(prod(primes))) * all_mon
    return first + second


def prod(values: list[int]) -> int:
    out = 1
    for v in values:
        out *= v
    return out


def liouville_slice(n: int) -> Fraction:
    fac = factorization(n)
    if len(fac) == 1:
        return prime_cost(next(iter(fac)))
    return Fraction(0)


def main() -> None:
    vertices = 0
    interiors = 0
    minimum_gap = None
    grid = [Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(1)]
    for n in range(2, 181):
        primes = list(factorization(n))
        for values in product((-1, 1), repeat=len(primes)):
            x = {p: Fraction(v) for p, v in zip(primes, values)}
            lhs = direct(n, x)
            rhs = formula(n, x)
            assert lhs == rhs
            gap = rhs - liouville_slice(n)
            assert gap >= 0
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
            vertices += 1
        if len(primes) <= 3:
            for values in product(grid, repeat=len(primes)):
                x = {p: v for p, v in zip(primes, values)}
                lhs = direct(n, x)
                rhs = formula(n, x)
                assert lhs == rhs
                gap = rhs - liouville_slice(n)
                assert gap >= 0
                minimum_gap = min(minimum_gap, gap)
                interiors += 1
    result = {
        "verdict": "PASS_X_90202_ADDITIVE_LIOUVILLE_CONE",
        "vertex_cases": vertices,
        "interior_cases": interiors,
        "minimum_domination_gap": str(minimum_gap),
    }
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
