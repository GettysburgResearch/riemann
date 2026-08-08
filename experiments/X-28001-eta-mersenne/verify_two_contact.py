#!/usr/bin/env python3
"""Exact replay of L-28005 through a finite endpoint.

Checks Dirichlet inverses, the finite eta filter, and the pointwise two-contact
carry identity.  It does not certify physical transference or RH.
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt

N = 384


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


def conv(x: list[int], y: list[int]) -> list[int]:
    out = [0] * (N + 1)
    for n in range(1, N + 1):
        out[n] = sum(x[d] * y[n // d] for d in divisors(n))
    return out


mu = mobius_sieve(N)
b_eta = [0] * (N + 1)
b2 = [0] * (N + 1)
a2 = [0] * (N + 1)
for n in range(1, N + 1):
    m = n
    r = 0
    while m % 2 == 0:
        r += 1
        m //= 2
    b_eta[n] = mu[m] if r == 0 else (1 << (r - 1)) * mu[m]
    b2[n] = mu[n] - (mu[n // 2] if n % 2 == 0 else 0)
    a2[n] = r + 1

# Finite filter b2=(epsilon-3 delta_2+2 delta_4)*b_eta.
for n in range(1, N + 1):
    rhs = b_eta[n]
    if n % 2 == 0:
        rhs -= 3 * b_eta[n // 2]
    if n % 4 == 0:
        rhs += 2 * b_eta[n // 4]
    assert b2[n] == rhs, (n, b2[n], rhs)

# b2 and a2 are convolution inverses.
ba = conv(b2, a2)
assert ba[1] == 1
assert all(ba[n] == 0 for n in range(2, N + 1))
assert all(a2[n] > 0 for n in range(1, N + 1))

# Divisor prefix and pointwise two-contact identity.
prefix_checks = 0
carry_checks = 0
for x in range(0, N + 1):
    prefix = sum(b2[q] * (x // q) for q in range(1, x + 1))
    expected = 1 if x == 1 else 0
    assert prefix == expected, (x, prefix, expected)
    prefix_checks += 1

for n in range(2, 257):
    for j in range(0, n + 1):
        value = 0
        for q in range(2, n + 1):
            chi = n // q - j // q - (n - j) // q
            value += b2[q] * chi
        expected = -(1 if j == 1 else 0) - (1 if j == n - 1 else 0)
        assert value == expected, (n, j, value, expected)
        carry_checks += 1

proof = {
    "schema": "riemann.x28001.two-contact.v1",
    "N": N,
    "filter_rows": N,
    "inverse_rows": N,
    "prefix_checks": prefix_checks,
    "carry_checks": carry_checks,
    "verdict": "PASS_EXACT_FILTERED_ETA_TWO_CONTACT_ALGEBRA",
}
canonical = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
proof["sha256"] = hashlib.sha256(canonical).hexdigest()
print(json.dumps(proof, indent=2, sort_keys=True))
