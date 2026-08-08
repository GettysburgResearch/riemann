#!/usr/bin/env python3
"""Exact standard-library replay for L-28001--L-28004.

This checks finite coefficient identities only.  It does not prove RMBR or RH.
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt

N = 512


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return out


def dirichlet_convolution(x: list[int], y: list[int], nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        out[n] = sum(x[d] * y[n // d] for d in divisors(n))
    return out


def highbit(n: int) -> int:
    return 1 << (n.bit_length() - 1)


mu = mobius_sieve(N)
e = [0] * (N + 1)
a = [0] * (N + 1)
b = [0] * (N + 1)
for n in range(1, N + 1):
    e[n] = 1 if n % 2 else -1
    a[n] = 0 if n == 1 else (1 if n % 2 == 0 else -1)
    r = 0
    m = n
    while m % 2 == 0:
        r += 1
        m //= 2
    b[n] = mu[m] if r == 0 else (1 << (r - 1)) * mu[m]

# eta inverse.
conv = dirichlet_convolution(e, b, N)
assert conv[1] == 1
assert all(conv[n] == 0 for n in range(2, N + 1))

# Coefficientwise Neumann series sum_j a^{*j}.
power = [0] * (N + 1)
power[1] = 1
neumann = power.copy()
stages = 0
while (1 << (stages + 1)) <= N:
    power = dirichlet_convolution(power, a, N)
    for n in range(1, N + 1):
        neumann[n] += power[n]
    stages += 1
assert neumann == b

# Product-six mutation.
a2 = dirichlet_convolution(a, a, N)
assert a2[4] == 1
assert a2[6] == -2
assert b[6] == -1

# Dyadic divisor prefix and carry image.
prefix_checks = 0
carry_checks = 0
central_checks = 0
average_checks = 0
for x in range(1, N + 1):
    D = sum(b[q] * (x // q) for q in range(1, x + 1))
    expected = 2 * highbit(x) - 1
    assert D == expected, (x, D, expected)
    prefix_checks += 1

for n in range(2, 257):
    P = highbit(n)
    ys: list[int] = []
    for j in range(0, n + 1):
        direct = 0
        for q in range(2, n + 1):
            chi = n // q - j // q - (n - j) // q
            direct += b[q] * chi
        Dj = 0 if j == 0 else 2 * highbit(j) - 1
        Dnj = 0 if n - j == 0 else 2 * highbit(n - j) - 1
        formula = (2 * P - 1) - Dj - Dnj
        assert direct == formula, (n, j, direct, formula)
        ys.append(direct)
        carry_checks += 1

    central = ys[n // 2]
    if n + 1 & n == 0:  # n=2^r-1
        expected_central = 1 - ((n + 1) // 2)
    else:
        expected_central = 1
    assert central == expected_central, (n, central, expected_central)
    central_checks += 1

    r = n - P
    numerator = (2 * P - 1) * (P - 1 - 3 * r)
    assert 3 * sum(ys) == numerator, (n, sum(ys), numerator)
    average_checks += 1

proof_object = {
    "schema": "riemann.x28001.eta-mersenne.v1",
    "N": N,
    "neumann_stages": stages,
    "eta_inverse_rows": N,
    "prefix_checks": prefix_checks,
    "carry_checks": carry_checks,
    "central_checks": central_checks,
    "average_checks": average_checks,
    "a2_4": a2[4],
    "a2_6": a2[6],
    "b6": b[6],
    "verdict": "PASS_EXACT_ETA_MERSENNE_ALGEBRA",
}
canonical = json.dumps(proof_object, sort_keys=True, separators=(",", ":")).encode()
proof_object["sha256"] = hashlib.sha256(canonical).hexdigest()
print(json.dumps(proof_object, sort_keys=True, indent=2))
