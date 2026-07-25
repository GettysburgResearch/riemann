#!/usr/bin/env python3
"""L-5604(c'), sharp form — the optimal detection threshold over all vectors.

Agent: opus5-01   Issue: #55

`detection_threshold.py` evaluates `eta_min` at the vector that minimizes the
on-line value.  That vector need not be the one that maximizes the response to
a displacement, so its `eta_min` is an over-estimate of the family's true
sensitivity.  This module computes the optimum.

Near the carrier `g(T+u) = (1/2) v^* M(u) v` with `M(u) = conj(beta) beta^T`
rank one, `beta_j(u) = h sinc(uh) e^{2 pi i u c_j}`.  Hence

    g''(T+u) = (1/2) v^* M''(u) v,
    M'' = conj(beta'') beta^T + 2 conj(beta') beta'^T + conj(beta) beta''^T,

which is Hermitian of rank at most three: with `C = [conj(beta), conj(beta'),
conj(beta'')]` and `S = [[0,0,1],[0,2,0],[1,0,0]]`, `M'' = C S C^*`.

By L-5604 the form goes negative for a quadruple at `T+u` displaced by `eta`
exactly when `v^* Q v < eta^2 v^* M''(u) v` for some `v`, i.e. when

    eta^2  >  1 / lambda_max( Q^{-1/2} M'' Q^{-1/2} )
           =  1 / lambda_max( S * C^* Q^{-1} C ),

the last being a 3x3 eigenproblem.  Minimizing over `u` gives the family's best
possible sensitivity at these parameters, attained by an explicit vector.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
from mpmath import mp, mpf, log, pi as mp_pi

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze_stream as A                                    # noqa: E402
import archimedean_block as AB                                # noqa: E402
import archimedean_asymptotic as AA                           # noqa: E402


def sinc_and_derivs(x):
    """sinc(x)=sin(pi x)/(pi x) and its first two derivatives, vectorised."""
    x = np.asarray(x, dtype=float)
    px = np.pi * x
    s, c = np.sin(px), np.cos(px)
    small = np.abs(x) < 1e-6
    f = np.where(small, 1 - px ** 2 / 6, s / np.where(small, 1.0, px))
    f1 = np.where(small, -np.pi ** 2 * x / 3,
                  (px * c - s) / np.where(small, 1.0, np.pi * x ** 2))
    f2 = np.where(small, -np.pi ** 2 / 3,
                  (-(px ** 2) * s - 2 * px * c + 2 * s) /
                  np.where(small, 1.0, np.pi ** 2 * x ** 3) * np.pi)
    return f, f1, f2


def beta_and_derivs(u, centers, h):
    """beta_j(u) = h sinc(uh) e^{2 pi i u c_j} and its first two u-derivatives."""
    f, f1, f2 = sinc_and_derivs(np.array([u * h]))
    f, f1, f2 = float(f[0]), float(f1[0]), float(f2[0])
    e = np.exp(2j * np.pi * u * centers)
    a = 2j * np.pi * centers
    b0 = h * f * e
    b1 = h * (h * f1 * e + f * a * e)
    b2 = h * (h * h * f2 * e + 2 * h * f1 * a * e + f * a * a * e)
    return b0, b1, b2


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("stream")
    ap.add_argument("--carrier-num", type=int, required=True)
    ap.add_argument("--carrier-den", type=int, required=True)
    ap.add_argument("--u-range", type=float, default=4.0)
    ap.add_argument("--u-points", type=int, default=801)
    ap.add_argument("--out", default="optimal-detection.json")
    args = ap.parse_args()

    st = A.load_stream(args.stream)
    k = st["cells"]
    cutoff = st["cutoff"]

    mp.dps = 40
    L = log(mpf(cutoff))
    delta = float(L / (2 * mp_pi))
    h = delta / k
    centers = -delta / 2 + (np.arange(k) + 0.5) * h

    # exact form Q = A_K + R_K - S_K, blocks assembled (L-5603, L-4203)
    za, _rem, _b, _om, _psi = AA.asymptotic_lags(cutoff, k, args.carrier_num,
                                                 args.carrier_den, 3)
    z1, shift, _bb, _oo = AA.lag_one_and_diagonal(cutoff, k, args.carrier_num,
                                                  args.carrier_den, 3)
    za[1] = z1
    gate = A.correction_gate(cutoff, k, args.carrier_num, args.carrier_den)
    alpha0 = gate["ell_T_float"] + shift
    q = (AB.archimedean_matrix(alpha0, za)
         + AB.pole_matrix(cutoff, k, args.carrier_num / args.carrier_den)
         - A.toeplitz_matrix(st))
    q = 0.5 * (q + q.conj().T)
    lam_min = float(np.linalg.eigvalsh(q)[0])
    assert lam_min > 0, "Q is not positive definite; the reduction needs Q > 0"
    qinv = np.linalg.inv(q)          # one factorization, reused for every u

    s3 = np.array([[0, 0, 1], [0, 2, 0], [1, 0, 0]], dtype=np.complex128)
    us = np.linspace(-args.u_range, args.u_range, args.u_points)
    best = None
    rows = []
    for u in us:
        b0, b1, b2 = beta_and_derivs(float(u), centers, h)
        cmat = np.stack([np.conj(b0), np.conj(b1), np.conj(b2)], axis=1)
        g3 = cmat.conj().T @ (qinv @ cmat)      # C^* Q^{-1} C
        ev = np.linalg.eigvals(s3 @ g3).real
        lam = float(ev.max())
        if lam <= 0:
            continue
        eta = float(np.sqrt(1.0 / lam))
        rows.append({"u": float(u), "eta_min": eta})
        if best is None or eta < best["eta_min"]:
            best = {"u": float(u), "eta_min": eta, "lambda_max_pencil": lam}

    etas = np.array([r["eta_min"] for r in rows])
    res = {
        "schema": "riemann.x5601-optimal-detection.v1",
        "agent": "opus5-01",
        "classification": "floating; the blocks are assembled by L-5603 in "
                          "ordinary arithmetic. Order of magnitude is the "
                          "claim, not the digits.",
        "cutoff": cutoff, "cells": k,
        "carrier": f"{args.carrier_num}/{args.carrier_den}",
        "lambda_min_exact_form": lam_min,
        "u_points": len(rows),
        "eta_min_optimal": best,
        "eta_min_median_over_u": float(np.median(etas)) if len(etas) else None,
        "eta_min_max_over_u": float(etas.max()) if len(etas) else None,
        "admissible_bound": 0.5,
        "detectable_anywhere": bool(len(etas) and etas.min() < 0.5),
        "note": "eta_min(u) is the smallest displacement of a quadruple at "
                "height T+u that SOME vector in the family could turn into a "
                "negative exact form. |eta| < 1/2 always, so eta_min >= 1/2 "
                "means undetectable in principle.",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
