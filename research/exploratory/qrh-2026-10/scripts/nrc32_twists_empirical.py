#!/usr/bin/env python3
"""NRC32 twists: EMPIRICAL double-precision display of CENTRED twisted energies.

Status: EXPLORATORY display only. Not an acceptance check, not directed, not
certified. The exact identities are certified by nrc32_twists_check.py, which
proves the centred split for EVERY complex centre via the polynomial-in-c
reduction (NRC32_TWISTS.md section 5). Here the centre 1/L(1,chi) is evaluated
with mpmath (L(1,chi) = -(1/q) sum_a chi(a) digamma(a/q), chi nonprincipal).
A finite panel of S/F cannot supply BM-3's hypothesis.
"""
import cmath
import importlib.util
import math
import os

import mpmath

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "nrc32_twists_check", os.path.join(_here, "nrc32_twists_check.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)


def chi_complex(chi, n):
    k = chi.exp(n)
    return 0j if k is None else cmath.exp(2j * math.pi * k / chi.e)


def centre(chi):
    if chi.q == 1:
        return 0j
    mpmath.mp.dps = 30
    s = mpmath.mpf(0)
    s = sum(mpmath.mpc(chi_complex(chi, a)) * mpmath.digamma(mpmath.mpf(a) / chi.q)
            for a in range(1, chi.q + 1) if chi.exp(a) is not None)
    L1 = -s / chi.q
    return complex(1 / L1)


def main():
    ys = (31, 63, 127, 255)
    nmax = (max(ys) + 1) ** 2
    mu = chk.mobius_sieve(nmax)
    prims = chk.primitive_characters(12)
    print("chi      q ord  Y    F_Y^c        annular^c    S^c          D        S^c/(1+F_Y^c)^2")
    for chi in prims:
        c = centre(chi)
        m = [0j]
        for n in range(1, nmax):
            m.append(m[-1] + mu[n] * chi_complex(chi, n) / n)
        for Y in ys:
            b = Y + 1
            fy = sum(abs(m[k] - c) ** 2 for k in range(1, Y + 1))
            fa = s = d = 0.0
            for a, h in chk.mesh(b):
                vals = [m[k] - c for k in range(a, a + h)]
                mean = sum(vals) / h
                fa += sum(abs(x) ** 2 for x in vals)
                s += h * abs(mean) ** 2
                d += sum(abs(x - mean) ** 2 for x in vals)
            print(f"{chi.label:8s} {chi.q:2d} {chi.order:3d} {Y:4d} {fy:12.6f} {fa:12.6f} "
                  f"{s:12.6f} {d:8.6f} {s / (1 + fy) ** 2:10.6f}")


if __name__ == "__main__":
    main()
