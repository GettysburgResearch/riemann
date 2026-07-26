#!/usr/bin/env python3
"""X-9504: how the L-9507 zero-accounting deficit scales in T, n and h.

L-9506 showed that increasing `n` drives lambda_min to zero and so cannot
decide anything.  L-9507 replaced the target with the scale-free ratio
rho_Gamma = lambda_max(Z_Gamma, H), which RH forces below 1.  The route can
only produce a witness if the deficit 1 - rho_Gamma can be pushed below the
width of a directed enclosure.

This experiment measures the deficit as a function of

  T   the height through which zero ordinates are supplied,
  n   the matrix dimension,
  h   the arithmetic-progression step,

and extrapolates the height T that the route would require.

Standard library only; IEEE binary64; round-to-nearest.  DISCOVERY code, not
a certificate.

Usage:
    python3 experiments/screw_deficit_law.py \
        --zeros    experiments/results/X-9503-screw-audit-ratio/zeros1000.json \
        --json-out experiments/results/X-9504-screw-deficit-law/deficit.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from screw_lib import Psi, jacobi_eig, rayleigh, screw_toeplitz
from screw_audit_and_ratio import pencil_max, zero_toeplitz, zero_tail_estimate

H_LOG2_3 = math.log(2.0) / 3.0


def deficit(psi, zs, n, h, T):
    """1 - rho_Gamma for Gamma = {ordinates <= T}."""
    G = [g for g in zs if g <= T]
    if not G:
        return None
    Hm = screw_toeplitz(psi, n, h)
    Z, _ = zero_toeplitz(G, n, h)
    rho, b = pencil_max(Z, Hm)
    return {"n": n, "h": h, "T": T, "zeros": len(G), "rho": rho,
            "deficit": 1.0 - rho, "S_T": zero_tail_estimate(T),
            "deficit_over_S_T": (1.0 - rho) / zero_tail_estimate(T)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zeros", required=True)
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--tmax-prime", type=float, default=16.0,
                    help="prime table extends to e^this; requires n*h <= this")
    args = ap.parse_args()

    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    zs = json.load(open(args.zeros))["zeros"]
    limit = int(math.exp(args.tmax_prime)) + 2
    print(f"building prime-power table to e^{args.tmax_prime} = {limit} ...")
    psi = Psi(limit)
    print(f"primes={psi.n_primes}  prime powers={psi.n_pp}  "
          f"zero ordinates={len(zs)} (max {zs[-1]:.1f})")

    out = {"experiment": "X-9504", "agent": "claude-09",
           "script_sha256": digest,
           "environment": {"python": platform.python_version(),
                           "platform": platform.platform(),
                           "third_party_libraries": "none (standard library only)",
                           "arithmetic": "IEEE binary64"},
           "status": "EMPIRICAL - binary64 reconnaissance, not a certificate"}

    # ---- A. deficit vs T, at the X-9502 proof-replay parameters ----
    print(f"\n[A] deficit vs T   (n=53, h=log2/3)")
    print(f"    {'T':>6} {'#zeros':>7} {'rho':>13} {'deficit':>12} "
          f"{'S_T':>11} {'deficit/S_T':>12}")
    rowsA = []
    for T in (100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000):
        r = deficit(psi, zs, 53, H_LOG2_3, T)
        rowsA.append(r)
        print(f"    {T:>6} {r['zeros']:>7} {r['rho']:>13.9f} "
              f"{r['deficit']:>12.4e} {r['S_T']:>11.3e} "
              f"{r['deficit_over_S_T']:>12.3f}")
    out["part_a_deficit_vs_T"] = rowsA

    tailK = [r["deficit_over_S_T"] for r in rowsA[-5:]]
    K = sum(tailK) / len(tailK)
    spread = max(tailK) - min(tailK)
    print(f"\n    deficit/S_T over the last 5 heights: mean {K:.3f}, "
          f"spread {spread:.3f}")
    out["deficit_law_constant"] = {"K": K, "spread": spread,
                                   "fit_range_T": [rowsA[-5]["T"], rowsA[-1]["T"]]}

    # ---- B. deficit vs n, fixed h and T ----
    print(f"\n[B] deficit vs n   (h=log2/3, T=1000)")
    print(f"    {'n':>4} {'rho':>13} {'deficit':>12}")
    rowsB = []
    for n in (8, 16, 24, 32, 40, 48, 53, 60, 68):
        if n * H_LOG2_3 > args.tmax_prime:
            continue
        r = deficit(psi, zs, n, H_LOG2_3, 1000)
        rowsB.append(r)
        print(f"    {n:>4} {r['rho']:>13.9f} {r['deficit']:>12.4e}")
    out["part_b_deficit_vs_n"] = rowsB

    # ---- C. deficit vs h, fixed n and T ----
    n_h = 40
    hmax = args.tmax_prime / n_h
    print(f"\n[C] deficit vs h   (n={n_h}, T=1000, h up to {hmax:.3f})")
    print(f"    {'h':>8} {'n*h':>7} {'rho':>13} {'deficit':>12}")
    rowsC = []
    steps = 40
    for i in range(1, steps + 1):
        h = hmax * i / steps
        r = deficit(psi, zs, n_h, h, 1000)
        rowsC.append(r)
    best = max(rowsC, key=lambda r: r["rho"])
    for r in rowsC[::2]:
        mark = "  <-- best" if r is best else ""
        print(f"    {r['h']:>8.4f} {r['n']*r['h']:>7.3f} {r['rho']:>13.9f} "
              f"{r['deficit']:>12.4e}{mark}")
    # the two structurally interesting steps
    for label, h in (("log(2)/3", H_LOG2_3), ("pi/gamma_1", math.pi / zs[0])):
        r = deficit(psi, zs, n_h, h, 1000)
        print(f"    {h:>8.4f} {n_h*h:>7.3f} {r['rho']:>13.9f} "
              f"{r['deficit']:>12.4e}  <-- {label}")
        rowsC.append(dict(r, label=label))
    out["part_c_deficit_vs_h"] = rowsC
    out["best_h"] = best
    print(f"\n    sup over the scanned h: rho = {best['rho']:.9f} "
          f"at h = {best['h']:.5f}  (deficit {best['deficit']:.4e})")

    # ---- D. extrapolation ----
    print(f"\n[D] height required by the route, using deficit ~ K * S_T with "
          f"K = {K:.3f}")
    print(f"    {'target deficit':>16} {'required T':>14} {'zeros below T':>16}")
    rowsD = []
    for target in (1e-6, 1e-9, 1e-12, 1e-15):
        lo, hi = 1e3, 1e40
        for _ in range(400):
            mid = math.sqrt(lo * hi)
            if K * zero_tail_estimate(mid) > target:
                lo = mid
            else:
                hi = mid
        Treq = math.sqrt(lo * hi)
        nz = (Treq / (2 * math.pi)) * (math.log(Treq / (2 * math.pi)) - 1.0)
        rowsD.append({"target_deficit": target, "required_T": Treq,
                      "zeros_below_T": nz})
        print(f"    {target:>16.0e} {Treq:>14.3e} {nz:>16.3e}")
    out["part_d_extrapolation"] = rowsD

    if args.json_out:
        p = Path(args.json_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=1, sort_keys=True))
        print(f"\nwrote {args.json_out}")


if __name__ == "__main__":
    main()
