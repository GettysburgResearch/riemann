#!/usr/bin/env python3
"""
X-0015 -- The tuned scalar detector: null-steering with certified ordinates.

Agent: claude-02
Implements: the "consequences for practice" section of L-0009.

THE IDEA.  L-0009 shows the Pick form along a direction v responds to an
off-line pair at ordinate gamma_0 at order delta^2 iff the rational filter
Ahat_v vanishes at ±gamma_0, while every OTHER on-line zero contributes
+|Ahat_v(gamma_k)|^2 to the statistic.  So the certified census ordinates are
DESIGN INPUTS: choose v to null Ahat at the target AND at the nearest
neighbours, and the floor -- previously an emergent property of the LDL rank
tail -- is suppressed by construction.  The verdict becomes ONE certified real
number q = v* P v / v*v:

    q < 0 certified  ==>  RH is false        (T-0005 + L-0008),

and the witness is (probes, v, q): checkable by anyone with O(N^2) arithmetic
and N evaluations of xi'/xi.  No LDL, no matrix at all in the verification.

MEASUREMENTS.
  1.  FLOOR: q on real zeta at the target (nothing planted), for N = 5, 7, 9,
      nulling the target and the 2(N-1)/2 - 1... i.e. N-1 ordinates: the pair
      ±gamma_0 plus the nearest census neighbours (both signs).
  2.  SENSITIVITY: inject an off-line quadruple of depth delta at gamma_0 into
      the real certified F (the X-0011 counterfactual construction) and find
      the smallest delta with certified q < 0.  Controls: the on-line DOUBLE
      at the same spot must keep q >= 0 -- and additionally q(DOUBLE) should
      sit at the pure floor since gamma_0 is nulled.
  3.  HEAD-TO-HEAD: the LDL detector (X-0012b) needed N = 20 probes for
      delta = 1e-10 at height 1e4.  What N does the tuned statistic need?

Usage: python3 run.py [gamma0] [count]
"""
from __future__ import annotations

import json
import os
import platform
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


def census_ordinates():
    p = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "zeros-T5000.json")
    out = []
    for s in json.load(open(p))["zeros"]:
        seg = s[s.index("[") + 1:s.index("]")]
        out.append(float(seg.split("+/-")[0]))
    return out


def build(gamma0, N, ords, spare=3):
    """Probes and tuned v: null +-gamma0 and nearby census ordinates, but
    keep `spare` degrees of freedom for the response optimiser (see the
    X-0015 postmortem in pick.tuned_vector: nulling every degree of freedom
    also nulled the sensitivity)."""
    al = PK.probe_cluster(gamma0 + 0.8, gamma0 + 1.6, N)
    nbr = sorted((g for g in ords if abs(g - gamma0) > 1e-9),
                 key=lambda g: abs(g - gamma0))
    nulls = [gamma0, -gamma0]
    for g in nbr:
        if len(nulls) >= N - spare:
            break
        nulls.append(g)
        if len(nulls) < N - spare:
            nulls.append(-g)
    v = PK.tuned_vector(al, nulls, opt_ordinate=gamma0)
    return al, v, nulls


def with_extra(extra, tol_bits):
    def F(s):
        s = acb(s)
        base = PK.xi_logderiv(s, tol_bits=tol_bits)
        return base + sum(1 / (s - z) for z in extra)
    return F


def main():
    gamma0 = float(sys.argv[1]) if len(sys.argv) > 1 else 1000.351  # near a real zero? no: pick midpoint
    cz.set_prec(4000)
    tol_bits = 400
    ords = census_ordinates()
    # place the target at the midpoint of the two nearest census zeros, so the
    # planted pair is a NEW zero pair (the X-0011 counterfactual style is to
    # move an existing pair; here we instead test at a zero-free ordinate and
    # plant a fresh quadruple, which needs no Newton refinement)
    below = max(g for g in ords if g < gamma0)
    above = min(g for g in ords if g > gamma0)
    target = (below + above) / 2
    print(f"target ordinate {target:.6f} (midpoint of census zeros "
          f"{below:.4f} / {above:.4f})")

    out = {"experiment": "X-0015", "agent": "claude-02", "git_sha": git_sha(),
           "python": sys.version.split()[0],
           "platform": platform.platform(), "prec_bits": 4000,
           "tol_bits": tol_bits, "target": target, "rows": []}

    c = arb(repr(target))
    for N, design in ((9, "nulls"), (9, "mvdr"), (12, "mvdr"), (16, "mvdr"),
                      (16, "ldl-extracted")):
        if design == "nulls":
            al, v, nulls = build(target, N, ords)
        elif design == "mvdr":
            al = PK.probe_cluster(target + 0.8, target + 1.6, N)
            window = sorted((g for g in ords if abs(g - target) < 40.0))
            v = PK.mvdr_vector(al, target, window)
            nulls = [f"mvdr window +-40 ({len(window)} ordinates)"]
        else:
            # design 4: take the direction the LDL detector implicitly
            # optimises -- the bottom eigenvector of the REAL Pick matrix --
            # by inverse iteration at midpoints, then certify along it.
            al = PK.probe_cluster(target + 0.8, target + 1.6, N)
            P = PK.pick_matrix(al, tol_bits=tol_bits)
            Pm = [[acb(arb(P[i][j].real.mid()), arb(P[i][j].imag.mid()))
                   for j in range(N)] for i in range(N)]
            x = [acb(1)] * N
            for _ in range(40):
                A = [row[:] + [x[i]] for i, row in enumerate(Pm)]
                for cc in range(N):
                    pv = max(range(cc, N),
                             key=lambda rr: float(abs(A[rr][cc]).mid()))
                    A[cc], A[pv] = A[pv], A[cc]
                    for rr in range(N):
                        if rr != cc:
                            f = A[rr][cc] / A[cc][cc]
                            for c2 in range(cc, N + 1):
                                A[rr][c2] = A[rr][c2] - f * A[cc][c2]
                z = [A[i][N] / A[i][i] for i in range(N)]
                nrm = sum((t * t.conjugate()).real for t in z).sqrt()
                x = [acb(arb((t / nrm).real.mid()), arb((t / nrm).imag.mid()))
                     for t in z]
            v = x
            nulls = ["bottom eigenvector of the real Pick matrix "
                     "(inverse iteration, midpoints)"]
        # diagnostic: the delta^2 response coefficient (L-0009), from the v
        # actually in use
        ap = [a - acb(1) / 2 for a in al]
        g0 = acb(arb(repr(target)))
        Apg = acb(0, 1) * sum(v[j].conjugate() / (ap[j] - acb(0, 1) * g0) ** 2
                              for j in range(N))
        Apm = acb(0, 1) * sum(v[j].conjugate() / (ap[j] + acb(0, 1) * g0) ** 2
                              for j in range(N))
        vv = sum((z * z.conjugate()).real for z in v)
        sens = float((2 * ((Apg * Apg.conjugate()).real
                           + (Apm * Apm.conjugate()).real) / vv).mid())
        t0 = time.time()
        floor = PK.tuned_form(al, v, tol_bits=tol_bits)
        tf = round(time.time() - t0, 1)
        ffl = float(floor.mid())
        print(f"\n  N={N} [{design}]: {nulls if design != 'nulls' else str(len(nulls)) + ' hard nulls'}")
        print(f"    floor q(real zeta) = {ffl:+.3e}  rad {float(floor.rad()):.1e}"
              f"  [{tf}s]  {'(q<0 would be a P1 alert!)' if floor < 0 else ''}")
        dstar = (ffl / sens) ** 0.5 if sens > 0 and ffl > 0 else float("inf")
        print(f"    response coefficient 2|Ahat'|^2/v*v = {sens:.3e}  "
              f"-> predicted detectable delta* ~ {dstar:.2e}")
        row = {"N": N, "design": design, "nulls": nulls, "floor": ffl,
               "floor_rad": float(floor.rad()), "seconds_floor": tf,
               "floor_negative": bool(floor < 0),
               "response_coefficient": sens, "predicted_delta_star": dstar,
               "sensitivity": []}

        # DOUBLE control: on-line double zero at the (nulled) target
        dbl = [acb(HALF, c), acb(HALF, c), acb(HALF, -c), acb(HALF, -c)]
        qd = PK.tuned_form(al, v, tol_bits=tol_bits, F=with_extra(dbl, tol_bits))
        print(f"    control DOUBLE at target: q = {float(qd.mid()):+.3e}  "
              f"({'PASS: at floor, nulled' if abs(float(qd.mid()) - ffl) < abs(ffl) * 0.5 + 1e-40 else 'note: shifted'})"
              f"  {'*** CONTROL NEGATIVE ***' if qd < 0 else ''}")
        row["double_q"] = float(qd.mid())
        row["double_negative"] = bool(qd < 0)

        smallest = None
        for dstr in ("0.01", "0.0001", "0.000001", "0.00000001",
                     "0.0000000001", "0.000000000001"):
            d = arb(dstr)
            off = [acb(HALF - d, c), acb(HALF + d, c),
                   acb(HALF - d, -c), acb(HALF + d, -c)]
            q = PK.tuned_form(al, v, tol_bits=tol_bits,
                              F=with_extra(off, tol_bits))
            neg = bool(q < 0)
            if neg:
                smallest = dstr
            row["sensitivity"].append({"delta": dstr, "q": float(q.mid()),
                                       "negative": neg})
            print(f"    OFF delta={dstr:<15} q = {float(q.mid()):+.3e}  "
                  f"q-floor = {float(q.mid()) - ffl:+.3e}  "
                  f"{'NEG (refutation-grade)' if neg else '-'}")
        row["smallest_delta_detected"] = smallest
        print(f"    -> smallest delta detected: {smallest}")
        out["rows"].append(row)

    bad = [r for r in out["rows"] if r["floor_negative"] or r["double_negative"]]
    detected = [r["smallest_delta_detected"] for r in out["rows"]]
    out["conclusion"] = (
        "INVESTIGATE: a control or floor came out negative" if bad else
        f"controls clean; smallest detected delta by N: {detected}"
        + ("" if any(detected) else "  -- NO detection at any tested delta: "
           "the design does not work as built"))
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"tuned-{int(target)}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n " + out["conclusion"])
    print("wrote", p)


if __name__ == "__main__":
    main()
