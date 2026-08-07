#!/usr/bin/env python3
"""Exact tuple expansion and deterministic first-crossing partition check."""
from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from itertools import product
from typing import Tuple

Vector = Tuple[int, ...]


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return [i for i, ok in enumerate(sieve) if ok]


def factors(n, primes):
    out = []
    x = n
    for p in primes:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out.append(e)
    if x != 1:
        raise ValueError(n)
    return tuple(out)


def mobius(n, primes):
    exps = factors(n, primes)
    if any(e > 1 for e in exps):
        return 0
    return -1 if sum(exps) % 2 else 1


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def zero(dim):
    return (0,) * dim


def product_tuples(limit, count):
    def rec(prefix, remaining):
        if len(prefix) == count:
            yield tuple(prefix)
            return
        for value in range(1, remaining + 1):
            yield from rec(prefix + [value], remaining // value)

    yield from rec([], limit)


def classify(variables, n, delta_num=1, delta_den=5):
    first = 1
    stop = len(variables) - 1
    for index, value in enumerate(variables):
        first *= value
        if first**delta_den >= n**delta_num:
            stop = index
            break
    second = n // first
    upper = delta_den - delta_num
    type_two = (
        first**delta_den <= n**upper
        and second**delta_den <= n**upper
    )
    return ("II" if type_two else "I", stop, first, second)


def build(K=2, V=3):
    X = V**K
    primes = primes_up_to(X)
    dim = len(primes)
    total = defaultdict(lambda: zero(dim))
    counts = defaultdict(int)
    failures = []

    for j in range(1, K + 1):
        coefficient = (-1) ** (j - 1) * math.comb(K, j)
        for ds in product(range(1, V + 1), repeat=j):
            mu_weight = 1
            for d in ds:
                mu_weight *= mobius(d, primes)
            if mu_weight == 0:
                continue
            remaining = X // math.prod(ds)
            for tail in product_tuples(remaining, j):
                q = tail[0]
                rs = tail[1:]
                n = math.prod(ds) * math.prod(tail)
                contribution = scale(
                    coefficient * mu_weight, factors(q, primes)
                )
                total[n] = add(total[n], contribution)
                variables = tuple(ds) + (q,) + tuple(rs)
                kind, stop, first, second = classify(variables, n)
                counts[(j, kind)] += 1
                if first * second != n or kind not in {"I", "II"}:
                    failures.append(
                        (j, variables, n, kind, stop, first, second)
                    )

    direct = {}
    for n in range(1, X + 1):
        value = zero(dim)
        for d in range(1, n + 1):
            if n % d == 0:
                value = add(
                    value,
                    scale(mobius(d, primes), factors(n // d, primes)),
                )
        direct[n] = value

    mismatches = [n for n in range(1, X + 1) if total[n] != direct[n]]
    core = {
        "schema": "X-15125-row-partition-v1",
        "K": K,
        "V": V,
        "X": X,
        "delta": "1/5",
        "classification": "EXACT_TUPLE_AND_FIRST_CROSSING_REGRESSION",
        "tuple_counts": {
            f"j{j}_{kind}": count
            for (j, kind), count in sorted(counts.items())
        },
        "partition_failures": failures,
        "coefficient_mismatches": mismatches,
        "sample_total": {
            str(n): list(total[n]) for n in range(2, X + 1)
        },
        "verdict": "PASS" if not failures and not mismatches else "FAIL",
        "proof_boundary": (
            "Finite tuple and deterministic Type-I/II partition check only; "
            "no analytic CP(K) estimate."
        ),
    }
    payload = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_sha256"] = hashlib.sha256(payload).hexdigest()
    return core


if __name__ == "__main__":
    print(json.dumps(build(), indent=2, sort_keys=True))
