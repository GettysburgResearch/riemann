#!/usr/bin/env python3
"""S(t) census: is any zero missing from the critical line?

Agent: opus5-01   Issue: #55

For the zeros of `zeta` with `0 < gamma < t`,

    N(t) = theta(t)/pi + 1 + S(t),

where `S(t) = (1/pi) arg zeta(1/2 + it)` is small and oscillatory: it has mean
zero, and `|S(t)| < 2` for every `t` in the ranges computed to date.  If the
`k`-th located sign change of `Z` in a scan sits at `gamma_k`, then

    S(gamma_k) = N(gamma_k) - theta(gamma_k)/pi - 1
               = (k + c) - theta(gamma_k)/pi - 1

for an unknown integer offset `c` fixed by the start of the window.  So the
*shape* of `k - theta(gamma_k)/pi` across a window is `S` up to a constant.

The diagnostic: if a pair of zeros has left the critical line somewhere in the
window, every located zero after that point is one index behind, so the tracked
quantity takes a **permanent step of 2** there.  If all zeros are on the line it
merely oscillates in a band of width about 2 and returns.  A step is what a
counterexample would look like; a wander is what RH looks like.

This is the empirical form of Turing's method.  It is *not* the rigorous form:
that needs an explicit bound on `\\int S` to certify the count exactly.  A step
found here would be a nomination requiring that rigorous follow-up, not a
disproof.
"""
from __future__ import annotations

import argparse
import json

import numpy as np
from mpmath import mp, mpf, log, pi as mp_pi


def theta(t, dps=30):
    """theta(t) = (t/2) log(t/2pi) - t/2 - pi/8 + 1/(48t) + 7/(5760 t^3)."""
    mp.dps = dps
    t = mpf(t)
    return (t / 2) * log(t / (2 * mp_pi)) - t / 2 - mp_pi / 8 \
        + 1 / (48 * t) + 7 / (5760 * t ** 3)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zeros")
    ap.add_argument("--out", default="census.json")
    ap.add_argument("--step-threshold", type=float, default=1.5)
    args = ap.parse_args()

    g = [float(x) for x in open(args.zeros)]
    g.sort()
    n = len(g)
    mp.dps = 30
    th = np.array([float(theta(x) / mp_pi) for x in g])
    k = np.arange(n, dtype=float)
    # S up to an additive constant; centre it
    s = k - th
    s -= s.mean()

    # a permanent step of 2 would show as a jump in the running median
    win = max(5, n // 40)
    med = np.array([np.median(s[max(0, i - win):i + win + 1]) for i in range(n)])
    jumps = np.abs(np.diff(med))
    worst = int(np.argmax(jumps)) if n > 1 else 0

    gaps = np.diff(g)
    dens = float(log(mpf(g[len(g) // 2]) / (2 * mp_pi)) / (2 * mp_pi))
    ngaps = gaps * dens

    res = {
        "schema": "riemann.x5602-census.v1",
        "agent": "opus5-01",
        "classification": "empirical Turing diagnostic; a step is a nomination "
                          "requiring a rigorous S-integral bound, not a proof",
        "zeros": n,
        "t_range": [g[0], g[-1]],
        "S_range": [float(s.min()), float(s.max())],
        "S_std": float(s.std()),
        "smoothed_S_step_max": float(jumps.max()) if n > 1 else 0.0,
        "smoothed_S_step_at_t": float(g[worst]) if n > 1 else 0.0,
        "step_threshold": args.step_threshold,
        "permanent_step_detected": bool(n > 1 and jumps.max() > args.step_threshold),
        "normalised_gap_mean": float(ngaps.mean()),
        "normalised_gap_max": float(ngaps.max()),
        "normalised_gap_max_at_t": float(g[int(np.argmax(ngaps))]),
        "normalised_gap_min": float(ngaps.min()),
        "normalised_gap_min_at_t": float(g[int(np.argmin(ngaps))]),
        "note": "S(t) is expected to oscillate with |S| < 2 and return; a "
                "permanent step of 2 is the signature of a pair of zeros "
                "leaving the critical line",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
