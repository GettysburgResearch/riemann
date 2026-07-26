#!/usr/bin/env python3
"""
X-0015b -- The compact scalar witness, end to end: search fires, direction is
extracted, one certified number refutes.

Agent: claude-02

X-0015's three explicit filter designs FAILED (see run.py and R-0011): the
implicit optimum the LDL search finds beats explicit null-steering and MVDR by
~12 orders of magnitude in response/floor.  The correct division of labour
turned out to be:

    search:  LDL over the full Pick matrix (as in X-0012) -- it optimises the
             direction implicitly and needs no design;
    witness: when a pivot d_k < 0 fires, x = L^{-*} e_k gives x* P x = d_k
             EXACTLY, so the direction is one triangular solve away.  Freeze
             x at midpoints, then certify q = x* P x / x*x in ball
             arithmetic.  By L-0008, q < 0 certified refutes RH regardless of
             how x was found -- the extraction may be sloppy, the certificate
             cannot be.

Two dead ends are recorded in-file because both are tempting: unshifted
inverse iteration converges to the eigenvalue of smallest MAGNITUDE (here
+1.5e-38, not the negative -1.5e-26); and shifting by the pivot estimate does
not converge either, because the shift sits below the entire near-zero cluster
and the convergence ratio is ~1.01 per step.  The triangular solve has neither
problem and is exact.

This script demonstrates the full pipeline on a counterfactual world: the real
certified F with an off-line quadruple of depth 1e-6 planted at a zero-free
ordinate.  Expected output: LDL NOT_PSD, certified q < 0, re-verified at a
second tolerance.

Usage: python3 extract.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import certzeta as cz  # noqa: E402
import pick as PK  # noqa: E402
from flint import acb, arb  # noqa: E402

HALF = arb(1) / 2


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def main():
    cz.set_prec(4000)
    tol = 400
    ords = []
    p = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "zeros-T5000.json")
    for s in json.load(open(p))["zeros"]:
        seg = s[s.index("[") + 1:s.index("]")]
        ords.append(float(seg.split("+/-")[0]))
    below = max(g for g in ords if g < 1000.351)
    above = min(g for g in ords if g > 1000.351)
    target = (below + above) / 2
    c, d = arb(repr(target)), arb("0.000001")
    off = [acb(HALF - d, c), acb(HALF + d, c),
           acb(HALF - d, -c), acb(HALF + d, -c)]

    def F(s):
        s = acb(s)
        return PK.xi_logderiv(s, tol_bits=tol) + sum(1 / (s - z) for z in off)

    N = 16
    al = PK.probe_cluster(target + 0.8, target + 1.6, N)
    t0 = time.time()
    cert = PK.pick_certificate(al, tol_bits=tol, F=F)
    print(f"1. LDL search: {cert['verdict']}  min_pivot={cert['min_pivot']:.3e}")
    P = PK.pick_matrix(al, tol_bits=tol, F=F)
    x = PK.ldl_witness_direction(P)
    q = PK.tuned_form(al, x, tol_bits=tol, F=F)
    q2 = PK.tuned_form(al, x, tol_bits=250, F=F)
    secs = round(time.time() - t0, 1)
    print(f"2. witness direction extracted (triangular solve, midpoints)")
    print(f"3. certified q = {float(q.mid()):.6e} (rad {float(q.rad()):.1e})  "
          f"negative: {bool(q < 0)}")
    print(f"4. re-verified at tol_bits=250: q = {float(q2.mid()):.6e}  "
          f"negative: {bool(q2 < 0)}   [{secs}s total]")

    out = {"experiment": "X-0015b", "agent": "claude-02", "git_sha": git_sha(),
           "prec_bits": 4000, "target": target, "planted_delta": "1e-6",
           "N": N, "ldl_verdict": cert["verdict"],
           "ldl_min_pivot": cert["min_pivot"],
           "q_certified": float(q.mid()), "q_rad": float(q.rad()),
           "q_negative": bool(q < 0),
           "q_reverified_tol250": float(q2.mid()),
           "q_reverified_negative": bool(q2 < 0),
           "witness_v": [[str(t.real), str(t.imag)] for t in x],
           "seconds": secs,
           "conclusion": ("compact witness pipeline works: search fires, "
                          "extraction is one triangular solve, certificate is "
                          "one ball-arithmetic real number"
                          if q < 0 and q2 < 0 else "INVESTIGATE")}
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    fp = os.path.join(HERE, "results", "extract-demo.json")
    with open(fp, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", fp)


if __name__ == "__main__":
    main()
