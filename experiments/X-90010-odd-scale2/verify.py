#!/usr/bin/env python3
"""Regression harness for R-90009 / L-90010.

The cofinal reserve theorem is analytic.  This script checks the exact finite
carry identities and the compact-current two-tap routing, then scans the
quarter-balanced scale-two reserve increment on a moderate range.
"""

import math


def mobius(n: int) -> int:
    x = n
    mu = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            mu = -mu
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        mu = -mu
    return mu


def carry(n, j, d):
    return n // d - j // d - (n - j) // d


def L(n, j, f):
    return sum(f(d) * carry(n, j, d) for d in range(1, n + 1))


def b_odd(n):
    return mobius(n) if n & 1 else 0


def q_odd(n):
    return -b_odd(n) * math.log(n)


def y_odd(n, j):
    return L(n, j, b_odd)


def qrow_odd(n, j):
    return L(n, j, q_odd)


def c2(x):
    if x <= 0:
        return 0
    return 1 + x.bit_length() - 1


def y_formula(n, j):
    return c2(n) - c2(j) - c2(n - j)


def q_circ_coeff(n):
    # q_circ = T q_odd + T' b_odd,
    # T=1-z-4z^2+4z^3, T'=log2(z+8z^2-12z^3).
    out = 0.0
    for a, coeff in ((0, 1), (1, -1), (2, -4), (3, 4)):
        d = 1 << a
        if n % d == 0:
            out += coeff * q_odd(n // d)
    for a, coeff in ((1, 1), (2, 8), (3, -12)):
        d = 1 << a
        if n % d == 0:
            out += math.log(2) * coeff * b_odd(n // d)
    return out


def qrow_circ(n, j):
    return L(n, j, q_circ_coeff)


def v2(n):
    out = 0
    while n and n % 2 == 0:
        out += 1
        n //= 2
    return out


def odd_log(n):
    return math.log(n) - v2(n) * math.log(2)


MAX_N = 5000
F = [0.0] * (2 * MAX_N + 1)
G = [0.0] * (2 * MAX_N + 1)
for m in range(1, len(F)):
    g = odd_log(m)
    F[m] = F[m - 1] + g
    G[m] = G[m - 1] + g * g


def O(n, j):
    return F[n] - F[j] - F[n - j]


def S(n, j):
    return G[n] - G[j] - G[n - j]


def R(n, j):
    o = O(n, j)
    return o * o - S(n, j)


# Exact integer carry/prefix identities and corrected scaling.
for n in range(2, 257):
    for j in range(1, n):
        y = y_odd(n, j)
        assert y == y_formula(n, j), (n, j, y, y_formula(n, j))
        assert y_odd(2 * n, 2 * j) == y - 1
        assert y_odd(4 * n, 4 * j) == y - 2
        assert L(2 * n, 2 * j, mobius) == -1

# Concrete counterexample to the old L-34406 formula.
assert y_odd(10, 3) == -1
assert sum(carry(10, 3, 1 << r) for r in range(1, 5)) == 3

# Compact-current routing on many aligned chains.
for n in range(2, 65):
    for j in range(1, n):
        q = [qrow_odd((1 << r) * n, (1 << r) * j) for r in range(4)]
        i3 = q[3] - q[2]
        i1 = q[1] - q[0]
        yr = y_odd(8 * n, 8 * j)
        rhs = i3 - 4 * i1 - math.log(2) * (3 * yr + 19)
        lhs = qrow_circ(8 * n, 8 * j)
        assert abs(lhs - rhs) < 2e-10 * (1 + abs(lhs)), (n, j, lhs, rhs)

# The algebraic scale-four decomposition of the reserve.
for n in range(2, 1000):
    for j in (1, max(1, n // 4), max(1, n // 2), min(n - 1, 3 * n // 4)):
        if not (1 <= j < n):
            continue
        d2 = R(2 * n, 2 * j) - 4 * R(n, j)
        d2_next = R(4 * n, 4 * j) - 4 * R(2 * n, 2 * j)
        d4 = R(4 * n, 4 * j) - 16 * R(n, j)
        assert abs(d4 - (d2_next + 4 * d2)) < 1e-8 * (1 + abs(d4))

# Reconnaissance only: quarter-balanced Delta_2 R is already positive on this
# whole finite range.  The written theorem proves positivity cofinally.
min_ratio = (float("inf"), None)
for n in range(8, MAX_N + 1):
    lo = max(1, math.ceil(n / 4))
    hi = min(n - 1, math.floor(3 * n / 4))
    for j in range(lo, hi + 1):
        d2 = R(2 * n, 2 * j) - 4 * R(n, j)
        assert d2 > -1e-8, (n, j, d2)
        ratio = d2 / (n * math.log(n))
        if ratio < min_ratio[0]:
            min_ratio = (ratio, (n, j, d2))

print("PASS_X90010")
print("minimum scanned Delta2R/(n log n):", min_ratio)
