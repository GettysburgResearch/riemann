#!/usr/bin/env python3
"""Numerical verification of the D-0801 explicit-formula dictionary (T-5601).

Agent: opus5-01   Issue: #55 / #28

The whole D-0801 counterexample route rests on the identity

    sum_rho g_{T,v}(z_rho)  =  A(g) + R(g) - (prime side)

with the specific constants of T-2801 / L-0702 / L-0801.  A wrong factor of 2,
a wrong `2 pi`, a `Gamma(s)` versus `Gamma(s/2)` slip, or a sign flip would
invalidate every certified number in the repository while remaining completely
invisible to the internal consistency tests, which all share the convention.

This script closes that hole empirically.  At small parameters it evaluates
BOTH sides independently:

  * the right-hand side from the compact formulas actually used by the
    producers, and
  * the left-hand side by summing g over genuine nontrivial zeros of zeta,
    obtained from `mpmath.zetazero`, plus a Riemann-von Mangoldt density tail.

The carrier is placed exactly on a low zero so that the sum is dominated by a
handful of terms and the tail is small.
"""
from __future__ import annotations

import argparse
import json

from mpmath import (mp, mpf, mpc, exp, log, sqrt, pi, e1, psi, quad, sin,
                    zetazero, inf, re as mre)


def cells(delta, k):
    h = delta / k
    return [(-delta / 2 + j * h, -delta / 2 + (j + 1) * h) for j in range(k)], h


def W(z, v, delta):
    """W_v(z) = int_I w_v(x) e^{2 pi i z x} dx, evaluated exactly cell by cell."""
    k = len(v)
    cs, _ = cells(delta, k)
    if abs(z) < mpf(10) ** (-mp.dps + 5):
        return sum(v[j] * (cs[j][1] - cs[j][0]) for j in range(k))
    tot = mpc(0)
    for j in range(k):
        lo, hi = cs[j]
        tot += v[j] * (exp(2 * pi * 1j * z * hi) - exp(2 * pi * 1j * z * lo))
    return tot / (2 * pi * 1j * z)


def g_test(z, v, delta, T):
    """g_{T,v}(z) = (A(z) + A(-z))/2 with A(z) = W(z-T) W^#(z-T)."""
    def A(w):
        return W(w - T, v, delta) * mp.conj(W(mp.conj(w) - T, v, delta))
    return (A(z) + A(-z)) / 2


def ghat(xi, v, delta, T):
    """ghat(xi) = Re(e^{-2 pi i T xi} R_v(xi)), zero outside [-delta, delta]."""
    k = len(v)
    h = delta / k
    if abs(xi) > delta:
        return mpf(0)
    R = mpc(0)
    for j in range(k):
        for m in range(k):
            ov = 1 - abs(j - m - xi / h)
            if ov > 0:
                R += v[j] * mp.conj(v[m]) * h * ov
    return mre(exp(-2 * pi * 1j * T * xi) * R)


def prime_side(v, delta, T, cutoff):
    """(1/pi) sum_{q=p^a<=c} Lambda(q)/sqrt(q) * ghat(log q / 2 pi)."""
    n = int(cutoff)
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    tot = mpf(0)
    terms = 0
    for p in range(2, n + 1):
        if sieve[p]:
            q = p
            while q <= n:
                tot += log(mpf(p)) / sqrt(mpf(q)) * ghat(log(mpf(q)) / (2 * pi),
                                                         v, delta, T)
                terms += 1
                q *= p
    return tot / pi, terms


def arch_compact(v, delta, T, L):
    """The compact cutoff-free archimedean functional of L-0702 / L-4201."""
    g0 = ghat(mpf(0), v, delta, T)

    def integrand(t):
        k_t = exp(-t / 4) / (1 - exp(-t))
        if t < mpf(10) ** (-mp.dps // 2):
            # combined value has a removable singularity at 0
            t = mpf(10) ** (-mp.dps // 2)
            k_t = exp(-t / 4) / (1 - exp(-t))
        return exp(-t) * g0 / t - k_t * ghat(t / (4 * pi), v, delta, T)

    knots = [mpf(0)] + [2 * L * j / (4 * len(v)) for j in range(1, 4 * len(v))] + [2 * L]
    val = quad(integrand, knots)
    return (val + g0 * e1(2 * L) - g0 * log(pi)) / (2 * pi)


def arch_direct(v, delta, T, rmax):
    """(1/2pi) int h_+(r) g(r) dr with h_+ = Re psi(1/4+ir/2) - log pi."""
    def f(r):
        return (mre(psi(0, mpf(1) / 4 + 1j * r / 2)) - log(pi)) * \
               mre(g_test(mpf(r), v, delta, T))
    nodes = [-rmax, -T - 8, -T + 8, mpf(0), T - 8, T + 8, rmax]
    nodes = sorted(set(nodes))
    return quad(f, nodes) / (2 * pi)


def zero_sum(v, delta, T, nzeros, tail_to):
    """2 * sum_{n>=1} g(gamma_n) plus a Riemann-von Mangoldt density tail."""
    tot = mpf(0)
    last = mpf(0)
    for n in range(1, nzeros + 1):
        gam = zetazero(n).imag
        last = gam
        tot += 2 * mre(g_test(gam, v, delta, T))
    tail = 2 * quad(lambda r: mre(g_test(mpf(r), v, delta, T)) *
                    log(mpf(r) / (2 * pi)) / (2 * pi), [last, tail_to, inf])
    return tot, tail, last


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff", type=int, default=30)
    ap.add_argument("--cells", type=int, default=4)
    ap.add_argument("--carrier", default="first-zero")
    ap.add_argument("--nzeros", type=int, default=300)
    ap.add_argument("--dps", type=int, default=30)
    ap.add_argument("--out", default="dictionary-check.json")
    args = ap.parse_args()

    mp.dps = args.dps
    L = log(mpf(args.cutoff))
    delta = L / (2 * pi)
    k = args.cells
    T = zetazero(1).imag if args.carrier == "first-zero" else mpf(args.carrier)

    # a deliberately non-trivial complex envelope
    v = [mpc(1, 0), mpc(0, mpf(1) / 2), mpc(mpf(-1) / 3, mpf(1) / 4),
         mpc(mpf(2) / 5, mpf(-1) / 7)][:k]
    while len(v) < k:
        v.append(mpc(1, 0))

    prime, nterms = prime_side(v, delta, T, args.cutoff)
    arch_c = arch_compact(v, delta, T, L)
    arch_ladder = {}
    for rr in (100, 200, 400, 800):
        arch_ladder[str(rr)] = arch_direct(v, delta, T, T + rr)
    arch_d = arch_ladder["800"]
    pole = 2 * mre(g_test(mpc(0, mpf(1) / 2), v, delta, T))
    rhs = arch_c + pole - prime

    zsum, ztail, last = zero_sum(v, delta, T, args.nzeros, T + 400)
    lhs = zsum + ztail

    res = {
        "cutoff": args.cutoff, "cells": k, "carrier": mp.nstr(T, 20),
        "dps": args.dps, "prime_terms": nterms, "zeros_used": args.nzeros,
        "highest_zero": mp.nstr(last, 12),
        "archimedean_compact": mp.nstr(arch_c, 20),
        "archimedean_direct_quadrature": mp.nstr(arch_d, 20),
        "archimedean_direct_truncation_ladder": {
            rr: mp.nstr(abs(arch_c - val), 6) for rr, val in arch_ladder.items()},
        "archimedean_agreement": mp.nstr(abs(arch_c - arch_d), 6),
        "pole": mp.nstr(pole, 20),
        "prime_side": mp.nstr(prime, 20),
        "rhs_A_plus_R_minus_S": mp.nstr(rhs, 20),
        "zero_sum_explicit": mp.nstr(zsum, 20),
        "zero_sum_density_tail": mp.nstr(ztail, 12),
        "lhs_sum_over_zeros": mp.nstr(lhs, 20),
        "absolute_difference": mp.nstr(abs(rhs - lhs), 8),
        "relative_difference": mp.nstr(abs(rhs - lhs) / abs(rhs), 8),
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
