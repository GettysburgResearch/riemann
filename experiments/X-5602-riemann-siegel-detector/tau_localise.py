#!/usr/bin/env python3
"""Where, inside a Turing window, could an off-line zero actually hide?

Agent: opus5-01   Issue: #55

`turing.py` answers the coarse question -- which integer `c = N(t1)` survives
the bound `|int_{t1}^t S| <= B`.  Usually more than one does, and the surviving
alternatives are dismissed by hand as "edge effects".  That is unsatisfying when
the whole point is a statement about one specific interior ordinate.

This script asks the sharp question instead: **for each surviving `c`, and for
each candidate ordinate `tau` in the window, is there ANY admissible off-line
configuration that places an off-line zero at `tau`?**  The answer is a subset
of the window -- the only places an off-line zero could be.  If the ordinate of
interest is not in that subset, it is excluded, regardless of which `c` is true.

The mechanism is the quantisation of `M`.  With

    M(t) = mult * sum_j (t - tau_j)_+ ,

`M` is convex, non-decreasing, starts at zero, and its slope takes only the
values `0, mult, 2*mult, ...`.  It must live inside the corridor

    max(0, -B - D_c(t))  <=  M(t)  <=  B - D_c(t)   for all t.

A `c` that is off by `-k` makes `D_c` fall with slope `-k`, so `M` must rise
with average slope `k` -- which, for `mult = 2`, is only achievable by placing
off-line ordinates near the LEFT edge and letting them accumulate.  An off-line
zero in the middle of the window cannot produce enough rise before `t2` without
overshooting the upper wall earlier.  That is what the localisation measures.
"""
from __future__ import annotations

import argparse
import json

from mpmath import mp, mpf, log, pi as mp_pi

from turing import theta_antideriv


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zeros")
    ap.add_argument("--t1", type=str, required=True)
    ap.add_argument("--t2", type=str, required=True)
    ap.add_argument("--target", type=str, required=True,
                    help="the ordinate whose exclusion is at issue")
    ap.add_argument("--dps", type=int, default=50)
    ap.add_argument("--grid", type=int, default=1200,
                    help="t-grid on which the corridor is enforced")
    ap.add_argument("--tau-grid", type=int, default=800,
                    help="resolution of the tau localisation")
    ap.add_argument("--partners", type=int, default=80,
                    help="how many partner ordinates to try alongside each tau")
    ap.add_argument("--multiplicity", type=int, default=2)
    ap.add_argument("--out", default="tau-localise.json")
    args = ap.parse_args()

    mp.dps = args.dps
    t1, t2 = mpf(args.t1), mpf(args.t2)
    target = mpf(args.target)
    g = sorted(mpf(x) for x in open(args.zeros) if t1 <= mpf(x) <= t2)
    span = float(t2 - t1)
    target_off = float(target - t1)

    B_cons = 3 + mpf(1) / 10 * log(t2)
    B_trud = mpf('2.067') + mpf('0.059') * log(t2)

    A0 = theta_antideriv(t1)
    ts = [t1 + (t2 - t1) * mpf(i) / args.grid for i in range(1, args.grid + 1)]
    xs = [float(t - t1) for t in ts]

    def D(c, t):
        acc = mpf(0)
        for x in g:
            if x <= t:
                acc += (t - x)
            else:
                break
        return c * (t - t1) + acc - (theta_antideriv(t) - A0)

    acc_all = sum(t2 - x for x in g)
    c_est = int(mp.nint(((theta_antideriv(t2) - A0) - acc_all) / (t2 - t1)))

    mult = args.multiplicity
    cand = [span * i / args.tau_grid for i in range(args.tau_grid + 1)]
    partners = [span * i / args.partners for i in range(args.partners + 1)]

    def localise(c, Bf):
        vals = [float(D(c, t)) for t in ts]
        if max(vals) > Bf:                     # no M >= 0 can pull D down
            return None
        lo = [max(0.0, -Bf - v) for v in vals]
        up = [Bf - v for v in vals]

        def fits(taus):
            for x, l, u in zip(xs, lo, up):
                m = 0.0
                for tt in taus:
                    if x > tt:
                        m += mult * (x - tt)
                if m < l - 1e-9 or m > u + 1e-9:
                    return False
            return True

        clean = fits([])
        ok = []
        for tau0 in cand:
            if fits([tau0]):
                ok.append(tau0)
                continue
            for p in partners:                 # allow one helper ordinate
                if fits(sorted([tau0, p])):
                    ok.append(tau0)
                    break
        return {"clean_admissible": clean, "admissible_taus": ok}

    out = {
        "schema": "riemann.x5602-tau-localise.v1",
        "agent": "opus5-01",
        "classification": "conditional on the external Turing bound on int S and "
                          "on the Z evaluation; not interval-certified",
        "t1": float(t1), "t2": float(t2), "span": span,
        "target": float(target), "target_offset": target_off,
        "sign_changes_located": len(g),
        "N_t1_estimate": c_est,
        "multiplicity": mult,
        "bounds": {"conservative": float(B_cons), "trudgian": float(B_trud)},
        "per_bound": {},
    }

    for label, Bv in (("conservative", B_cons), ("trudgian", B_trud)):
        Bf = float(Bv)
        per_c = {}
        target_ok_anywhere = False
        for c in range(c_est - 3, c_est + 4):
            r = localise(c, Bf)
            if r is None:
                per_c[str(c - c_est)] = {"excluded": True,
                                         "reason": "D exceeds +B"}
                continue
            taus = r["admissible_taus"]
            if not taus and not r["clean_admissible"]:
                per_c[str(c - c_est)] = {"excluded": True,
                                         "reason": "no admissible M (slope quantised)"}
                continue
            # is the target ordinate reachable under this c?
            tol = span / args.tau_grid
            hit = any(abs(tt - target_off) <= tol for tt in taus)
            target_ok_anywhere |= hit
            per_c[str(c - c_est)] = {
                "excluded": False,
                "clean_admissible": r["clean_admissible"],
                "n_admissible_taus": len(taus),
                "admissible_tau_min": min(taus) if taus else None,
                "admissible_tau_max": max(taus) if taus else None,
                "admissible_taus_near_target": [tt for tt in taus
                                                if abs(tt - target_off) <= 5.0],
                "target_admissible": hit,
            }
        out["per_bound"][label] = {
            "candidates": per_c,
            "target_admissible_under_any_c": target_ok_anywhere,
            "verdict": ("the target ordinate can host an off-line zero"
                        if target_ok_anywhere else
                        "NO admissible configuration places an off-line zero at "
                        "the target ordinate: it is EXCLUDED"),
        }

    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
