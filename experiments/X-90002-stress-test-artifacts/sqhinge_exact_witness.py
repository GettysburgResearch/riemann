#!/usr/bin/env python3
"""Exact directed-interval certification of a single coefficient c_T(j).

Uses integer interval enclosures of 1/sqrt(n) at denominator 10^DIGITS,
propagated with directed rounding through the L-32701.4 formula
(validated exactly against the direct triangular solve of B^T c = h).

Usage: sqhinge_exact_witness.py T j [DIGITS]
Prints exact rational interval [lo, hi] for c_T(j) and its certified sign.
"""
import sys
from math import isqrt


def mobius_sieve(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    comp = bytearray(n + 1)
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            comp[i * p] = 1
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def main():
    T = int(sys.argv[1])
    j = int(sys.argv[2])
    DIG = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    SC = 10 ** DIG
    mu = mobius_sieve(T)
    # scaled enclosures of 1/sqrt(n)
    S2 = SC * SC

    def inv_lo(n):
        a = isqrt(S2 // n)
        while (a + 1) * (a + 1) * n <= S2:
            a += 1
        while a * a * n > S2:
            a -= 1
        return a

    lo = [0] * (T + 1)
    for n in range(1, T + 1):
        lo[n] = inv_lo(n)
    # h(q) in [lo[q]-lo[T]-1, lo[q]+1-lo[T]] / SC
    hloT, hhiT = lo[T], lo[T] + 1
    # u_m interval
    ulo = [0] * (T + 3)
    uhi = [0] * (T + 3)
    for k in range(1, T + 1):
        mk = mu[k]
        if mk == 0:
            continue
        for m in range(1, T // k + 1):
            n = m * k
            a, b = lo[n] - hhiT, lo[n] + 1 - hloT
            if mk > 0:
                ulo[m] += a
                uhi[m] += b
            else:
                ulo[m] -= b
                uhi[m] -= a
    tl = th = 0
    for m in range(T, j + 1, -1):
        tl += ulo[m]
        th += uhi[m]
        if m == j + 2:
            break
    if j + 2 > T:
        tl = th = 0
    a_lo = j * ulo[j] - (j - 2) * uhi[j + 1]
    a_hi = j * uhi[j] - (j - 2) * ulo[j + 1]
    num_lo = (j + 1) * a_lo + 2 * tl
    num_hi = (j + 1) * a_hi + 2 * th
    den = SC * j * (j - 1)
    print(f"c_{T}({j}) in [{num_lo}/{den}, {num_hi}/{den}]")
    print(f"        ~ [{num_lo/den:.6e}, {num_hi/den:.6e}]")
    if num_lo > 0:
        print("SIGN CERTIFIED: strictly POSITIVE")
    elif num_hi < 0:
        print("SIGN CERTIFIED: strictly NEGATIVE")
    else:
        print("INCONCLUSIVE at this precision; raise DIGITS")


if __name__ == "__main__":
    main()
