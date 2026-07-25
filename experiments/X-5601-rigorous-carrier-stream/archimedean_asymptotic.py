#!/usr/bin/env python3
"""L-5603 — the exact archimedean block by endpoint expansion, at any carrier.

Agent: opus5-01   Issue: #55

`archimedean_block.py` computes the L-4201 coefficients

    z_d = -(1/2 pi) int k(t) e^{-i omega t} tau_d(t/b) dt,   omega = T/2,

by direct quadrature, which needs `O(omega b)` panels per lag and therefore
dies well before the production carrier `T = 4.7e12`.  This module computes the
same coefficients in `O(1)` work per lag, and gets *more* accurate as `T` grows.

The integrand `phi_d = k * tau_d` is supported on `[(d-1)b, (d+1)b]`, vanishes
at both ends, and is smooth except for the kink of `tau_d` at `t = db`.  Split
the support at `db`, integrate by parts `n` times on each half, and note that
the linear hat factor `u` satisfies `u((d-1)b) = u((d+1)b) = 0`, `u(db) = 1`,
`u' = +-1/b`, `u'' = 0`, so `phi^{(m)} = k^{(m)} u + m k^{(m-1)} u'`.  All
interior boundary values collapse and one is left with

    int phi_d e^{-i omega t} dt
      = sum_{m>=1} (i omega)^{-(m+1)} (m/b) D_d^{(m-1)} + R_n ,

    D_d^{(j)} = k^{(j)}((d-1)b) e^{-i omega (d-1) b}
              - 2 k^{(j)}(d b)   e^{-i omega d b}
              +   k^{(j)}((d+1)b) e^{-i omega (d+1) b} ,

with `|R_n| <= omega^{-n} int |phi_d^{(n)}|`.  The `m = 0` terms vanish because
`phi_d` is continuous and has vanishing outer endpoint values, which is why the
series starts at `omega^{-2}` rather than `omega^{-1}`: the archimedean
off-diagonals are `O(1/T^2)`, not `O(1/T)`, for every `d >= 2`.  That single
observation is worth about a factor `omega b` over L-4202's total-variation
bound.

Lag `d = 1` is different: its support reaches `t = 0`, where `k(t) ~ 1/t` and
the hat factor `t/b` cancels the pole, leaving `phi_1(0) = 1/b` — a genuine
nonzero endpoint that contributes at order `omega^{-1}`.  It is treated
separately, by direct quadrature over `[0, 2b]` (a single lag, always cheap in
the regime where it matters) or by its own expansion about `t = 0`.

The phases `exp(-i omega m b) = exp(-i T L m / K)` are huge at the production
carrier and are evaluated once per lag with MPFR, exactly as in L-5601.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
from mpmath import mp, mpf, mpc, log, pi as mp_pi, exp as mexp, diff as mdiff

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import archimedean_block as AB                                # noqa: E402


def k_mp(t):
    return mexp(-t / 4) / (1 - mexp(-t))


def k_derivs(points, nmax, dps=40):
    """k^{(j)}(t) for j = 0..nmax at the given points, via mpmath."""
    mp.dps = dps
    out = np.zeros((nmax + 1, len(points)))
    for i, t in enumerate(points):
        tm = mpf(t)
        for j in range(nmax + 1):
            out[j, i] = float(mdiff(k_mp, tm, j))
    return out


def g_mp(t):
    """g(t) = t k(t), smooth at 0 with g(0) = 1; needed for the d = 1 lag."""
    if t == 0:
        return mpf(1)
    return t * mexp(-t / 4) / (1 - mexp(-t))


def q_mp(t, b):
    """q_b(t) = 1/t - k(t)(1 - t/b), removable at 0 with value 1/b - 1/4."""
    if t == 0:
        return 1 / mpf(b) - mpf(1) / 4
    return 1 / t - k_mp(t) * (1 - t / mpf(b))


def kink_phases(cutoff, cells, tnum, tden, dps=60):
    """exp(-i omega m b) for m = 0..cells, with omega b = T log(c) / K."""
    mp.dps = dps
    L = log(mpf(cutoff))
    T = mpf(tnum) / mpf(tden)
    psi = T * L / cells                     # = omega * b
    two_pi = 2 * mp_pi
    out = np.empty(cells + 2, dtype=np.complex128)
    for m in range(cells + 2):
        ang = mp.fmod(psi * m, two_pi)
        out[m] = complex(mexp(mpc(0, -ang)))
    return out, float(psi)


def asymptotic_lags(cutoff, cells, tnum, tden, nterms=3, dps=40):
    """z_1..z_{K-1} of L-4201 by the endpoint expansion (d >= 2)."""
    mp.dps = dps
    L = log(mpf(cutoff))
    b = float(2 * L / cells)
    omega = float(mpf(tnum) / mpf(tden)) / 2.0
    ph, psi = kink_phases(cutoff, cells, tnum, tden)

    pts = [m * b for m in range(1, cells + 2)]
    kd = k_derivs(pts, nterms, dps)          # kd[j, m-1] = k^{(j)}(m b)

    z = np.zeros(cells, dtype=np.complex128)
    rem = np.zeros(cells)
    for d in range(2, cells):
        acc = 0j
        for m in range(1, nterms + 1):
            j = m - 1
            dj = (kd[j, d - 2] * ph[d - 1]
                  - 2.0 * kd[j, d - 1] * ph[d]
                  + kd[j, d] * ph[d + 1])
            acc += dj * (m / b) / (1j * omega) ** (m + 1)
        z[d] = -acc / (2 * np.pi)
        # remainder: |R_n| <= omega^{-n} int |phi^{(n)}|
        # <= omega^{-n} [ 2b max|k^{(n)}| + 2 n max|k^{(n-1)}| ] on the support
        n = nterms + 1
        kn = abs(float(mdiff(k_mp, mpf((d - 1) * b), n)))
        knm = abs(float(mdiff(k_mp, mpf((d - 1) * b), n - 1)))
        rem[d] = (2 * b * kn + 2 * n * knm) / (omega ** n) / (2 * np.pi)
    return z, rem, b, omega, psi


def lag_one_and_diagonal(cutoff, cells, tnum, tden, nterms=3, dps=40):
    """z_1 and alpha_0 - ell_T by the same endpoint expansion.

    Lag 1 reaches t = 0, where k has a pole that the hat factor cancels.  On
    [0, b] write phi_1 = g(t)/b with g(t) = t k(t) analytic at 0, so

        int phi_1 e^{-i omega t} dt
          = sum_m (i omega)^{-(m+1)} [ g^{(m)}(0)/b
                                       - (2 m k^{(m-1)}(b)/b) e^{-i omega b}
                                       + (m k^{(m-1)}(2b)/b) e^{-2 i omega b} ]

    whose m = 0 term is 1/(i omega b) -- the only O(1/T) piece of the whole
    archimedean block.

    The diagonal uses the L-4202 identity
    alpha_0 = ell_T + (1/2pi)[ -Ci(omega b) + int_0^b q_b cos(omega t) dt ]
    with the standard asymptotics of Ci and two integrations by parts of the
    q_b integral.
    """
    mp.dps = dps
    L = log(mpf(cutoff))
    b = mpf(2) * L / cells
    omega = mpf(tnum) / mpf(tden) / 2
    psi = omega * b
    two_pi = 2 * mp_pi
    ang = mp.fmod(psi, two_pi)
    e1 = mexp(mpc(0, -ang))
    e2 = mexp(mpc(0, -mp.fmod(2 * psi, two_pi)))

    acc = mpc(0)
    for m in range(0, nterms + 1):
        gm = mdiff(g_mp, mpf(0), m)
        term = mpc(gm / b)
        if m >= 1:
            km1_b = mdiff(k_mp, b, m - 1)
            km1_2b = mdiff(k_mp, 2 * b, m - 1)
            term += -2 * m * km1_b / b * e1 + m * km1_2b / b * e2
        acc += term / (mpc(0, 1) * omega) ** (m + 1)
    z1 = complex(-acc / (2 * mp_pi))

    cs, sn = mp.cos(ang), mp.sin(ang)
    ci_asym = sn / psi - cs / psi ** 2 - 2 * sn / psi ** 3
    qb = q_mp(b, b)
    qp0 = mdiff(lambda t: q_mp(t, b), mpf(0), 1)
    qpb = mdiff(lambda t: q_mp(t, b), b, 1)
    iq = qb * sn / omega - (qp0 - qpb * cs) / omega ** 2
    alpha_shift = float((-ci_asym + iq) / (2 * mp_pi))
    return z1, alpha_shift, float(b), float(omega)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff-power10", type=int, required=True)
    ap.add_argument("--cells", type=int, required=True)
    ap.add_argument("--carrier-num", type=int, required=True)
    ap.add_argument("--carrier-den", type=int, required=True)
    ap.add_argument("--nterms", type=int, default=3)
    ap.add_argument("--compare-quadrature", action="store_true")
    ap.add_argument("--out", default="asymptotic.json")
    args = ap.parse_args()

    cutoff = 10 ** args.cutoff_power10
    T = args.carrier_num / args.carrier_den
    z, rem, b, omega, psi = asymptotic_lags(cutoff, args.cells,
                                            args.carrier_num, args.carrier_den,
                                            args.nterms)
    z1, alpha_shift, _b, _om = lag_one_and_diagonal(
        cutoff, args.cells, args.carrier_num, args.carrier_den, args.nterms)
    z[1] = z1
    res = {
        "schema": "riemann.x5601-arch-asymptotic.v1",
        "agent": "opus5-01",
        "cutoff": cutoff, "cells": args.cells,
        "carrier": f"{args.carrier_num}/{args.carrier_den}",
        "b": b, "omega": omega, "omega_b": psi,
        "nterms": args.nterms,
        "z_1": [z1.real, z1.imag],
        "abs_z_1": abs(z1),
        "alpha_0_minus_ell_T": alpha_shift,
        "arch_total_rowsum": float(abs(z1) + np.abs(z[2:]).sum()
                                   + abs(alpha_shift)),
        "abs_sum_z_d_ge_2": float(np.abs(z[2:]).sum()),
        "max_abs_z": float(np.abs(z).max()),
        "remainder_bound_sum": float(rem.sum()),
        "remainder_bound_max": float(rem.max()),
    }
    if args.compare_quadrature:
        zq_alpha, zq, _b, _ell = AB.archimedean_lags(cutoff, args.cells, T,
                                                     per_osc=1, order=10)
        d = np.abs(z[2:] - zq[2:])
        res["quadrature_comparison"] = {
            "max_abs_difference_d_ge_2": float(d.max()),
            "sum_abs_difference_d_ge_2": float(d.sum()),
            "quadrature_abs_sum_d_ge_2": float(np.abs(zq[2:]).sum()),
            "relative_sum_difference":
                float(d.sum() / max(1e-300, np.abs(zq[2:]).sum())),
        }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
