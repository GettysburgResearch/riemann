#!/usr/bin/env python3
"""
X-0005 -- Reading the zeros out of the primes: the spectrum of psi(x) - x.

Agent: claude-01
Addresses: Q-0010, candidate Z-0004.

THE IDEA

The explicit formula (unconditional) says

    psi(x) = x - sum_rho x^rho / rho - log(2 pi) - (1/2) log(1 - x^-2).

Substituting x = e^u and normalising by e^{u/2},

    f(u) := (psi(e^u) - e^u) / e^{u/2}
          = - sum_rho e^{(rho - 1/2) u} / rho  + O(u e^{-u/2}) .

If RH holds, every rho = 1/2 + i gamma and f(u) is an almost periodic function
of u with **frequencies exactly the zero ordinates gamma** and amplitudes
2/|rho|.  If some zero has Re rho = 1/2 + delta, its component instead grows
like e^{delta u} = x^delta.

So a Fourier transform of f over a window in u is a **spectrometer for the
zeros**, computed from the primes alone -- no zeta evaluation, no contour, no
analytic continuation in the computation.  Two things come out of it:

  (1) CROSS-VALIDATION.  The peaks should sit at the ordinates certified
      independently in X-0001/X-0004.  The analytic half and the arithmetic
      half of this repository have no code in common, so agreement is a real
      check on both.

  (2) A SEARCH THAT COVERS ALL HEIGHTS AT ONCE.  Every contour method costs
      more as the height grows.  This one costs the same: one sieve, one
      transform, and every gamma in the resolvable band is examined
      simultaneously.  A peak that is NOT at a known zero, or a peak whose
      amplitude grows with the window, is a lead pointing at Re rho > 1/2.

STATUS: EMPIRICAL.  Nothing here is certified -- floating point throughout, a
truncated window, and a finite sieve.  A lead found here must be converted into
a rectangle and handed to L-0002 / T-0001, which are the certified tools.
This file is a SCREEN, not a proof, and per README rule 2 its output must never
be called evidence on its own.

Usage: python3 run.py [X] [ngrid]
"""
from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def psi_samples(X: int, us: list[float]) -> list[float]:
    """psi(e^u) for each u in the (increasing) list us, via a sieve.

    psi(x) = sum over prime powers p^k <= x of log p.
    """
    sieve = bytearray([1]) * (X + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(X**0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))

    # (value, log p) events for every prime power <= X
    events = []
    for p in range(2, X + 1):
        if sieve[p]:
            lp = math.log(p)
            q = p
            while q <= X:
                events.append((q, lp))
                q *= p
    events.sort()

    out = []
    idx = 0
    run = 0.0
    for u in us:
        x = math.exp(u)
        while idx < len(events) and events[idx][0] <= x:
            run += events[idx][1]
            idx += 1
        out.append(run)
    return out


def main():
    X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
    ngrid = int(sys.argv[2]) if len(sys.argv) > 2 else 60000
    u0, u1 = math.log(1000.0), math.log(X)
    us = [u0 + (u1 - u0) * i / (ngrid - 1) for i in range(ngrid)]

    t0 = time.time()
    psis = psi_samples(X, us)
    sieve_s = time.time() - t0
    print(f"sieve + psi samples: {sieve_s:.1f}s  (X = {X:.3g}, {ngrid} grid points)")

    # f(u) = (psi(e^u) - e^u) / e^{u/2}
    f = [(p - math.exp(u)) / math.exp(u / 2) for u, p in zip(us, psis)]
    du = us[1] - us[0]
    W = u1 - u0

    # Periodogram.  For a single zero rho = beta + i gamma the component of f is
    # -e^{(beta-1/2)u} e^{i gamma u}/rho, so
    #   A(gamma) := (2/W) | INT f(u) e^{-i gamma u} du |
    # equals 2/|rho| at gamma = Im rho when beta = 1/2 (up to windowing).
    def amplitude(g: float) -> float:
        cr = ci = 0.0
        for u, fv in zip(us, f):
            cr += fv * math.cos(g * u)
            ci -= fv * math.sin(g * u)
        return 2.0 * math.hypot(cr, ci) * du / W

    gmax = 60.0
    dg = 0.02
    ng = int(gmax / dg)
    t0 = time.time()
    spec = []
    for i in range(1, ng + 1):
        g = i * dg
        spec.append((g, amplitude(g)))
    print(f"periodogram: {time.time()-t0:.1f}s  (resolution ~ {2*math.pi/W:.3f})")

    # local maxima
    peaks = []
    for i in range(1, len(spec) - 1):
        if spec[i][1] > spec[i - 1][1] and spec[i][1] >= spec[i + 1][1]:
            peaks.append({"gamma": spec[i][0], "amplitude": spec[i][1]})
    peaks.sort(key=lambda d: -d["amplitude"])
    top = peaks[:14]

    known = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
             37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
             52.970321, 56.446248, 59.347044]
    matched = []
    for g in known:
        if g > gmax:
            continue
        best = min(peaks, key=lambda d: abs(d["gamma"] - g)) if peaks else None
        matched.append({
            "known_gamma": g,
            "nearest_peak": best["gamma"] if best else None,
            "offset": (best["gamma"] - g) if best else None,
            "amplitude": best["amplitude"] if best else None,
            "predicted_amplitude_2_over_abs_rho": 2.0 / math.hypot(0.5, g),
        })

    unexplained = [
        p for p in top
        if all(abs(p["gamma"] - g) > 0.4 for g in known) and p["gamma"] > 5
    ]

    out = {
        "experiment": "X-0005",
        "agent": "claude-01",
        "git_sha": git_sha(),
        "status": "EMPIRICAL -- floating point, finite window, no certification",
        "X": X,
        "n_grid": ngrid,
        "u_window": [u0, u1],
        "frequency_resolution_2pi_over_W": 2 * math.pi / W,
        "gamma_max_scanned": gmax,
        "sieve_seconds": round(sieve_s, 1),
        "top_peaks": top,
        "known_zero_matches": matched,
        "unexplained_peaks": unexplained,
        "interpretation": (
            "Peaks at the known ordinates confirm that the arithmetic and "
            "analytic halves of this repository agree.  An unexplained peak, or "
            "an amplitude that grows when X is increased, is the signature of a "
            "zero with Re > 1/2 and must be converted into a rectangle for "
            "L-0002 / T-0001.  Nothing here is certified."
        ),
    }
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    path = os.path.join(HERE, "results", f"spectrum-X{X}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)

    print("\n top spectral peaks (gamma, amplitude):")
    for p in top[:12]:
        mark = "  <-- known zero" if any(abs(p["gamma"] - g) < 0.4 for g in known) else ""
        print(f"   {p['gamma']:8.3f}   {p['amplitude']:.5f}{mark}")
    print(f"\n unexplained peaks among the top 14: {len(unexplained)}")
    print("wrote", path)


if __name__ == "__main__":
    main()
