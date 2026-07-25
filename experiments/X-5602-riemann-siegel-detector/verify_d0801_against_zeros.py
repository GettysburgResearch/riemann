#!/usr/bin/env python3
"""End-to-end check of the D-0801 production value against the ACTUAL zeta zeros.

Agent: opus5-01   Issue: #55

The explicit formula (T-5601) says

    sum_rho g_{T,v}(z_rho)  =  h * v^* (A_K + R_K - S_K) v ,

where the right-hand side is what X-5601 computed from 4,118,082,969 prime
powers, and the left-hand side is a sum over the nontrivial zeros of zeta.

Until now the repository has only ever evaluated the right-hand side.  X-5602
can locate the actual zeros near the production carrier, so for the first time
both sides can be compared at the production parameters.  `g_{T,v} >= 0` on the
real axis and decays like `1/u^2`, so the sum is dominated by the zeros within a
few units of the carrier, and the tail is estimated from the smooth density.

This is the strongest available check on the whole D-0801 stack: the
normalization (T-5601), the prime enumeration, the huge-phase arithmetic
(L-5601), the archimedean and pole blocks, and the eigenvector freeze all feed
the right-hand side, and none of them touch the left.
"""
from __future__ import annotations

import argparse
import json
import math

import numpy as np
from mpmath import mp, mpf, log, pi as mp_pi


def envelope(cutoff, cells, coords, bits):
    mp.dps = 40
    L = log(mpf(cutoff))
    delta = float(L / (2 * mp_pi))
    h = delta / cells
    scale = float(1 << bits)
    v = (np.array(coords["real"], dtype=float)
         + 1j * np.array(coords["imag"], dtype=float)) / scale
    centers = -delta / 2 + (np.arange(cells) + 0.5) * h
    return v, centers, h, delta


def W(u, v, centers, h, chunk=4000):
    """W_v(u) = h sinc(u h) sum_j v_j exp(2 pi i u c_j), vectorised in u."""
    u = np.atleast_1d(np.asarray(u, dtype=float))
    out = np.empty(len(u), dtype=complex)
    for i in range(0, len(u), chunk):
        uu = u[i:i + chunk]
        ph = np.exp(2j * np.pi * np.outer(uu, centers))
        f = ph @ v
        x = uu * h
        sinc = np.where(np.abs(x) < 1e-12, 1.0, np.sin(np.pi * x) / (np.pi * x))
        out[i:i + chunk] = h * sinc * f
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate")
    ap.add_argument("zeros")
    ap.add_argument("--bits", type=int, default=64)
    ap.add_argument("--carrier-num", type=int, default=94184072727073)
    ap.add_argument("--carrier-den", type=int, default=20)
    ap.add_argument("--out", default="d0801-vs-zeros.json")
    args = ap.parse_args()

    with open(args.certificate) as fh:
        cert = json.load(fh)
    cells, cutoff = cert["cells"], cert["cutoff"]
    coords = cert["frozen_vectors"][str(args.bits)]["_coords"]
    lam = cert["universal_margin_lower"]
    lam_float = float(cert["ell_T"]) - cert["lambda_max_floating"]

    v, centers, h, delta = envelope(cutoff, cells, coords, args.bits)
    norm2 = float(np.vdot(v, v).real)
    T = args.carrier_num / args.carrier_den

    g = np.array(sorted(float(x) for x in open(args.zeros)))
    u = g - T
    # g_{T,v}(gamma) = (1/2)(|W(gamma-T)|^2 + |W(-gamma-T)|^2); the second term
    # is evaluated near -2T and is utterly negligible at this carrier.
    w = W(u, v, centers, h)
    contrib = np.abs(w) ** 2                      # = 2 * (1/2)|W|^2, i.e. +-gamma
    total = float(contrib.sum())

    # Tail beyond the scanned window, done exactly rather than by a 1/u^2 fit.
    # Parseval: int_R |W(u)|^2 du = int |w_v(x)|^2 dx = h ||v||^2 = ghat(0).
    # The zeros have smooth density ell_T per unit u, so
    #     tail  ~  ell_T * ( ghat(0) - int_{-edge}^{edge} |W|^2 du ).
    ell_T = math.log(T / (2 * math.pi)) / (2 * math.pi)
    edge = float(max(abs(u.min()), abs(u.max())))
    ghat0 = h * norm2
    ngrid = 2_000_000
    uu = np.linspace(-edge, edge, ngrid)
    wq = W(uu, v, centers, h, chunk=20000)
    inner = float(np.trapezoid(np.abs(wq) ** 2, uu))
    tail_mass = ghat0 - inner
    tail_est = ell_T * tail_mass

    rhs = h * lam_float
    rhs_cert = h * lam

    res = {
        "schema": "riemann.x5602-d0801-vs-zeros.v1",
        "agent": "opus5-01",
        "classification": "both sides are ordinary floating computations; the "
                          "point is agreement between two entirely disjoint "
                          "routes, not certified digits",
        "cutoff": cutoff, "cells": cells,
        "carrier": f"{args.carrier_num}/{args.carrier_den}",
        "h": h, "Delta": delta, "norm_squared": norm2, "ell_T": float(cert["ell_T"]),
        "zeros_used": int(len(g)),
        "window_half_width": edge,
        "LHS_sum_over_located_zeros": total,
        "parseval_total_int_W2": ghat0,
        "int_W2_inside_window": inner,
        "tail_mass_outside_window": tail_mass,
        "LHS_tail_estimate": tail_est,
        "LHS_total_estimate": total + tail_est,
        "RHS_prime_side_floating": rhs,
        "RHS_prime_side_certified_lower": rhs_cert,
        "ratio_LHS_over_RHS": (total + tail_est) / rhs if rhs else None,
        "relative_difference": abs((total + tail_est) - rhs) / abs(rhs) if rhs else None,
        "note": "LHS is a sum over real zeta zeros located by Riemann-Siegel; "
                "RHS is h * lambda_min from 4.1e9 prime powers. They share no "
                "code, no data and no method.",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
