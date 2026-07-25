#!/usr/bin/env python3
"""L-5604(c) — the off-line displacement the executed certificate could detect.

Agent: opus5-01   Issue: #55

L-5604 shows that an off-critical quadruple at height `gamma`, displaced by
`eta` from the critical line, changes the D-0801 functional by
`-2 eta^2 g''(gamma) + O(eta^4)`.  With `lambda_min` the certified on-line
margin, the form can only go negative if

    eta  >  eta_min = sqrt( lambda_min * ghat(0) / (2 g''(gamma)) ).

This driver computes `g''` for the actual frozen production vector rather than
estimating it.  Two facts make it easy.  For the D-0801 envelope,

    W_v(u) = h * sinc(u h) * F(u),   F(u) = sum_j v_j exp(2 pi i u c_j),

and near the carrier `g(T+u) = (1/2)|W_v(u)|^2` up to a term evaluated near
`-2T`.  At a real zero `u_0` of `W_v` the square has a double zero and

    g''(T + u_0) = |W_v'(u_0)|^2 .

So the sensitivity is governed entirely by the slopes of `W_v` at its real
zeros, and `ghat(0) = h ||v||^2`.
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


def w_and_deriv(u, v, centers, h):
    """W_v(u) and W_v'(u) for a vector of real u."""
    u = np.atleast_1d(np.asarray(u, dtype=float))
    ph = np.exp(2j * np.pi * np.outer(u, centers))
    f = ph @ v
    fp = (2j * np.pi * (ph * centers[None, :])) @ v
    x = u * h
    sinc = np.where(np.abs(x) < 1e-12, 1.0, np.sin(np.pi * x) / (np.pi * x))
    dsinc = np.where(
        np.abs(x) < 1e-8, 0.0,
        (np.pi * x * np.cos(np.pi * x) - np.sin(np.pi * x)) / (np.pi * x ** 2))
    w = h * sinc * f
    wp = h * (dsinc * h * f + sinc * fp)
    return w, wp


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate")
    ap.add_argument("--bits", type=int, default=64)
    ap.add_argument("--u-range", type=float, default=6.0)
    ap.add_argument("--grid", type=int, default=400000)
    ap.add_argument("--out", default="detection-threshold.json")
    args = ap.parse_args()

    with open(args.certificate) as fh:
        cert = json.load(fh)
    cells = cert["cells"]
    cutoff = cert["cutoff"]
    coords = cert["frozen_vectors"][str(args.bits)]["_coords"]
    lam = cert["universal_margin_lower"]

    v, centers, h, delta = envelope(cutoff, cells, coords, args.bits)
    norm2 = float(np.vdot(v, v).real)
    ghat0 = h * norm2

    u = np.linspace(-args.u_range, args.u_range, args.grid)
    # chunk: the phase matrix is len(u) x cells and must not be materialised
    chunks = max(1, int(np.ceil(len(u) * cells / 4.0e6)))
    ws, wps = [], []
    for part in np.array_split(u, chunks):
        a, bb = w_and_deriv(part, v, centers, h)
        ws.append(a)
        wps.append(bb)
    w = np.concatenate(ws)
    wp = np.concatenate(wps)
    aw = np.abs(w)

    # local minima of |W| that are close to zero -> real (or near-real) zeros
    interior = np.arange(1, len(u) - 1)
    is_min = (aw[interior] < aw[interior - 1]) & (aw[interior] < aw[interior + 1])
    idx = interior[is_min]
    thresh = 0.05 * float(np.median(aw))
    zeros = idx[aw[idx] < thresh]

    slopes = np.abs(wp[zeros])
    gpp = slopes ** 2                        # g'' at those points
    with np.errstate(divide="ignore"):
        eta = np.sqrt(lam * ghat0 / (2.0 * gpp))

    res = {
        "schema": "riemann.x5601-detection-threshold.v1",
        "agent": "opus5-01",
        "classification": "floating evaluation of the frozen vector; the "
                          "conversion formula is L-5604(c). Order of the "
                          "answer is what matters, not its last digits.",
        "cutoff": cutoff, "cells": cells,
        "freeze_bits": args.bits,
        "Delta": delta, "h": h,
        "norm_squared": norm2,
        "ghat_zero": ghat0,
        "lambda_min_certified": lam,
        "u_window": args.u_range,
        "real_zeros_found": int(len(zeros)),
        "zero_spacing_mean": (float(np.mean(np.diff(u[zeros])))
                              if len(zeros) > 1 else None),
        "g_second_derivative": {
            "max": float(gpp.max()) if len(gpp) else None,
            "median": float(np.median(gpp)) if len(gpp) else None,
            "min": float(gpp.min()) if len(gpp) else None,
        },
        "eta_min": {
            "best_case_at_steepest_zero": float(eta.min()) if len(eta) else None,
            "median_zero": float(np.median(eta)) if len(eta) else None,
            "worst_case_at_flattest_zero": float(eta.max()) if len(eta) else None,
        },
        "note": "eta_min is the smallest off-critical displacement at which "
                "this configuration's exact form could have turned negative; "
                "a zero closer to the line than eta_min is invisible to it.",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
