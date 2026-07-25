#!/usr/bin/env python3
"""Exact L-4201 archimedean block and L-4203 pole block, assembled directly.

Agent: opus5-01   Issue: #55

Past the Nyquist barrier of C-5601 the D-0801 leading margin collapses like
`K^{-2}` while the L-4202 *uniform* gate `B_A` only shrinks like `1/T` and grows
like `K`.  So beyond the barrier the binding constraint stops being the prime
side and becomes the archimedean bound — and `B_A` is a bound, not the
correction.  This module computes the correction itself.

L-4201 gives, with `b = 2L/K`, `omega = T/2`, `k(t) = e^{-t/4}/(1-e^{-t})`:

    alpha_0 = ell_T + (1/2pi) [ -Ci(omega b) + int_0^b q_b(t) cos(omega t) dt ]
    z_d     = -(1/2pi) int k(t) e^{-i omega t} tau_d(t/b) dt      (1 <= d < K)

with `q_b(t) = 1/t - k(t)(1 - t/b)` (removable at 0, value `1/b - 1/4`) and the
`d`-th integrand supported on `[(d-1)b, (d+1)b]`.  The upper `d`-th diagonal of
`A_K` is `z_d/2`, the lower is its conjugate, and the diagonal is `alpha_0`.

The integrands oscillate `omega b/pi` times per lag, so the quadrature splits
each support into one subinterval per oscillation and applies fixed Gauss-
Legendre there.  That is affordable while `T b` stays below roughly `10^5`,
which covers exactly the low-carrier calibration regime where RH is already
known and the framework can therefore be validated end to end.

L-4203's pole block is assembled exactly from its two rank-one factors.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
from mpmath import mp, mpf, mpc, log, pi as mp_pi, ci, exp as mexp, sin as msin

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze_stream as A                                     # noqa: E402


def k_fun(t):
    """k(t) = e^{-t/4}/(1-e^{-t}), vectorised, safe for small t."""
    t = np.asarray(t, dtype=np.float64)
    out = np.empty_like(t)
    small = t < 1e-4
    ts = t[small]
    # 1/(1-e^{-t}) = 1/t + 1/2 + t/12 - t^3/720 + ...
    out[small] = np.exp(-ts / 4) * (1.0 / ts + 0.5 + ts / 12.0 - ts ** 3 / 720.0)
    tb = t[~small]
    out[~small] = np.exp(-tb / 4) / (1.0 - np.exp(-tb))
    return out


def q_fun(t, b):
    """q_b(t) = 1/t - k(t)(1 - t/b), removable at t = 0."""
    t = np.asarray(t, dtype=np.float64)
    out = np.empty_like(t)
    small = t < 1e-4
    ts = t[small]
    # k(t) = 1/t + 1/4 + 3 t/32 + O(t^2)
    kt = 1.0 / ts + 0.25 + 3.0 * ts / 32.0
    out[small] = 1.0 / ts - kt * (1.0 - ts / b)
    tb = t[~small]
    out[~small] = 1.0 / tb - k_fun(tb) * (1.0 - tb / b)
    return out


def osc_quad(f, lo, hi, omega, per_osc=1, order=10):
    """int_lo^hi f(t) e^{-i omega t} dt with one panel per oscillation."""
    if hi <= lo:
        return 0j
    span = hi - lo
    npanel = max(1, int(np.ceil(per_osc * omega * span / (2 * np.pi))) + 1)
    edges = np.linspace(lo, hi, npanel + 1)
    x, w = np.polynomial.legendre.leggauss(order)
    mid = 0.5 * (edges[:-1] + edges[1:])[:, None]
    half = 0.5 * (edges[1:] - edges[:-1])[:, None]
    t = mid + half * x[None, :]
    vals = f(t.ravel()).reshape(t.shape)
    integ = (vals * np.exp(-1j * omega * t) * w[None, :] * half).sum()
    return complex(integ)


def cos_quad(f, lo, hi, omega, per_osc=1, order=10):
    if hi <= lo:
        return 0.0
    span = hi - lo
    npanel = max(1, int(np.ceil(per_osc * omega * span / (2 * np.pi))) + 1)
    edges = np.linspace(lo, hi, npanel + 1)
    x, w = np.polynomial.legendre.leggauss(order)
    mid = 0.5 * (edges[:-1] + edges[1:])[:, None]
    half = 0.5 * (edges[1:] - edges[:-1])[:, None]
    t = mid + half * x[None, :]
    vals = f(t.ravel()).reshape(t.shape)
    return float((vals * np.cos(omega * t) * w[None, :] * half).sum())


def archimedean_lags(cutoff, cells, T, per_osc=1, order=10):
    """alpha_0 and z_1..z_{K-1} of L-4201."""
    mp.dps = 40
    L = log(mpf(cutoff))
    b = float(2 * L / cells)
    omega = T / 2.0
    ell = float(log(mpf(T) / (2 * mp_pi)) / (2 * mp_pi))

    iq = cos_quad(lambda t: q_fun(t, b), 0.0, b, omega, per_osc, order)
    ciq = float(ci(mpf(omega) * mpf(b)))
    alpha0 = ell + (-ciq + iq) / (2 * np.pi)

    two_l = float(2 * L)
    z = np.zeros(cells, dtype=np.complex128)
    for d in range(1, cells):
        lo = max(0.0, (d - 1) * b)
        hi = min(two_l, (d + 1) * b)
        if hi <= lo:
            continue
        mid = d * b
        val = 0j
        if mid > lo:
            val += osc_quad(lambda t, d=d: k_fun(t) * (1.0 - np.abs(t / b - d)),
                            lo, min(mid, hi), omega, per_osc, order)
        if hi > mid:
            val += osc_quad(lambda t, d=d: k_fun(t) * (1.0 - np.abs(t / b - d)),
                            max(mid, lo), hi, omega, per_osc, order)
        z[d] = -val / (2 * np.pi)
    return alpha0, z, b, ell


def archimedean_matrix(alpha0, z):
    k = len(z)
    row = np.zeros(k, dtype=np.complex128)
    row[0] = alpha0
    row[1:] = 0.5 * z[1:]
    idx = np.arange(k)
    diff = idx[None, :] - idx[:, None]
    return np.where(diff >= 0, row[np.abs(diff)], np.conj(row[np.abs(diff)]))


def pole_matrix(cutoff, cells, T):
    """L-4203: R_K = (1/h)[beta(T-i/2) beta(-T+i/2)^T + adjoint]."""
    mp.dps = 60
    L = log(mpf(cutoff))
    delta = L / (2 * mp_pi)
    h = delta / cells
    centers = [-delta / 2 + (j + mpf(1) / 2) * h for j in range(cells)]
    zc = mpc(T, -mpf(1) / 2)
    arg = mp_pi * h * zc
    s = msin(arg) / arg                                  # sinc(h(T - i/2))
    # beta_j(T-i/2) = h s exp(2 pi i T c_j + pi c_j)
    ba = np.empty(cells, dtype=np.complex128)
    bb = np.empty(cells, dtype=np.complex128)
    for j, c in enumerate(centers):
        ph = 2 * mp_pi * mpf(T) * c
        ea = h * s * mexp(mpc(mp_pi * c, 0)) * mexp(mpc(0, ph))
        eb = h * s * mexp(mpc(-mp_pi * c, 0)) * mexp(mpc(0, -ph))
        ba[j] = complex(ea)
        bb[j] = complex(eb)
    m = np.outer(ba, bb)
    return (m + m.conj().T) / float(h)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("stream")
    ap.add_argument("--carrier-num", type=int, required=True)
    ap.add_argument("--carrier-den", type=int, required=True)
    ap.add_argument("--per-osc", type=int, default=1)
    ap.add_argument("--order", type=int, default=10)
    ap.add_argument("--out", default="exact-form.json")
    args = ap.parse_args()

    st = A.load_stream(args.stream)
    cells = st["cells"]
    cutoff = st["cutoff"]
    T = args.carrier_num / args.carrier_den

    alpha0, z, b, ell = archimedean_lags(cutoff, cells, T,
                                         args.per_osc, args.order)
    ak = archimedean_matrix(alpha0, z)
    rk = pole_matrix(cutoff, cells, T)
    sk = A.toeplitz_matrix(st)

    q_exact = ak + rk - sk
    q_lead = ell * np.eye(cells) - sk

    ev_exact = float(np.linalg.eigvalsh(0.5 * (q_exact + q_exact.conj().T))[0])
    ev_lead = float(np.linalg.eigvalsh(0.5 * (q_lead + q_lead.conj().T))[0])

    gate = A.correction_gate(cutoff, cells, args.carrier_num, args.carrier_den)
    res = {
        "schema": "riemann.x5601-exact-form.v1",
        "agent": "opus5-01",
        "classification": "floating quadrature; NOT interval-certified. "
                          "Sign claims require a rigorous quadrature bound.",
        "cutoff": cutoff, "cells": cells,
        "carrier": f"{args.carrier_num}/{args.carrier_den}",
        "carrier_float": T,
        "Delta": float(np.log(cutoff) / (2 * np.pi)),
        "ell_T": ell,
        "deficit": float(np.log(cutoff) / (2 * np.pi)) - ell,
        "alpha_0": alpha0,
        "alpha_0_minus_ell_T": alpha0 - ell,
        "arch_offdiag_abs_sum": float(np.abs(z).sum()),
        "arch_correction_norm_measured":
            float(np.linalg.norm(ak - alpha0 * np.eye(cells), 2)),
        "arch_correction_norm_including_diagonal":
            float(np.linalg.norm(ak - ell * np.eye(cells), 2)),
        "L4202_uniform_bound_B_A": gate["B_arch_float"],
        "pole_norm_measured": float(np.linalg.norm(rk, 2)),
        "L4203_uniform_bound": gate["R_norm_float"],
        "lambda_min_leading_screen": ev_lead,
        "lambda_min_exact_form": ev_exact,
        "leading_screen_is_negative": bool(ev_lead < 0),
        "exact_form_is_negative": bool(ev_exact < 0),
        "quadrature": {"per_osc": args.per_osc, "order": args.order},
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
