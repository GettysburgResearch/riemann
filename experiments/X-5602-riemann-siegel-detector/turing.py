#!/usr/bin/env python3
"""Turing's method: certify that no zero has left the critical line in a window.

Agent: opus5-01   Issue: #55

`census.py` gives an empirical diagnostic.  This is the real argument.

Write `N(t)` for the number of zeros of `zeta` with `0 < gamma < t`, counted with
multiplicity, and `S(t) = N(t) - theta(t)/pi - 1`.  Turing's lemma bounds the
*integral* of `S`: for `t2 > t1 >= 168 pi`,

    | int_{t1}^{t2} S(u) du |  <=  B(t2),

with an explicit `B`.  This module uses a deliberately conservative
`B(t) = 3 + 0.1 log t`, which is weaker than any published constant known to me
(Trudgian's `2.067 + 0.059 log t` is sharper), so a conclusion drawn here would
only be strengthened by substituting the literature value.  The bound itself is
an EXTERNAL DEPENDENCY and is not proved in this repository.

The argument.  Let `gamma_1 < ... < gamma_m` be the sign changes of `Z` located
in `[t1, t2]` — these are zeros ON the critical line.  Suppose in addition there
are `k` off-line quadruple-halves at ordinates `tau_1 <= ... ` inside the window
(off-line zeros contribute to `N` but produce no sign change).  Then for
`t in [t1, t2]`,

    int_{t1}^{t} S = D_c(t) + M(t),
    D_c(t) = c (t - t1) + sum_{gamma_i <= t} (t - gamma_i) - int_{t1}^{t}(theta/pi + 1),
    M(t)   = sum_{tau_j <= t} (t - tau_j)   >= 0, non-decreasing, convex,

where `c = N(t1)` is an unknown integer.  Requiring `|D_c(t) + M(t)| <= B` for
every `t` in the window is a finite feasibility problem in `(c, k, tau)`:

  * `M >= 0`, so `D_c(t) <= B` is necessary for every `t` — this pins `c` from
    above;
  * a large negative excursion of `D_c` can only be repaired by `M > 0`, i.e. by
    postulating off-line zeros — this pins `c` from below;
  * once `c` is pinned, an off-line ordinate at `tau` forces
    `D_c(t2) + (#) (t2 - tau) <= B`, i.e. `tau` must lie within `(B - D_c(t2))/#`
    of the right endpoint.  Everything to the left of that is CERTIFIED clean.

The integral of `theta` is taken in closed form:

    int (theta(t)/pi + 1) dt = [ (t^2/4) log(t/2pi) - 3t^2/8 - pi t/8
                                 + log(t)/48 - 7/(11520 t^2) ] / pi  +  t.
"""
from __future__ import annotations

import argparse
import json

from mpmath import mp, mpf, log, pi as mp_pi


def theta_antideriv(t):
    """Antiderivative of theta(t)/pi + 1."""
    t = mpf(t)
    F = (t ** 2 / 4) * log(t / (2 * mp_pi)) - 3 * t ** 2 / 8 - mp_pi * t / 8 \
        + log(t) / 48 - mpf(7) / (11520 * t ** 2)
    return F / mp_pi + t


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zeros")
    ap.add_argument("--t1", type=str, required=True)
    ap.add_argument("--t2", type=str, required=True)
    ap.add_argument("--dps", type=int, default=50)
    ap.add_argument("--grid", type=int, default=4000)
    ap.add_argument("--multiplicity", type=int, default=2,
                    help="zeros added per off-line event (a quadruple puts two "
                         "ordinates +-gamma in the upper strip; 2 is the "
                         "conservative choice, 1 is even more conservative)")
    ap.add_argument("--out", default="turing.json")
    args = ap.parse_args()

    mp.dps = args.dps
    t1, t2 = mpf(args.t1), mpf(args.t2)
    g = sorted(mpf(x) for x in open(args.zeros) if t1 <= mpf(x) <= t2)
    m = len(g)

    B = 3 + mpf(1) / 10 * log(t2)          # conservative Turing bound
    B_trudgian = mpf('2.067') + mpf('0.059') * log(t2)

    A0 = theta_antideriv(t1)

    def D(c, t):
        """int_{t1}^{t} S du assuming exactly the located zeros and N(t1) = c."""
        acc = mpf(0)
        for x in g:
            if x <= t:
                acc += (t - x)
            else:
                break
        return c * (t - t1) + acc - (theta_antideriv(t) - A0)

    # grid for the sup/inf of D
    ts = [t1 + (t2 - t1) * mpf(i) / args.grid for i in range(1, args.grid + 1)]

    # a first estimate of c from requiring D(c, t2) ~ 0
    acc_all = sum(t2 - x for x in g)
    c_est = int(mp.nint(((theta_antideriv(t2) - A0) - acc_all) / (t2 - t1)))

    def offline_feasible(vals_f, lo_wall, up_wall, xs, mult, kmax=3, ngrid=240):
        """Is there an admissible off-line correction M fitting the corridor?

        M(t) = sum_j mult*(t - tau_j)_+ is convex, non-decreasing, M(t1)=0, and
        crucially its SLOPE IS QUANTISED in units of `mult`: it is 0 until the
        first off-line ordinate, then mult, then 2*mult, ...  A slope of, say,
        1 is simply not available.  That quantisation is what rules out the
        otherwise-plausible "N(t1) is one lower and some zeros are missing"
        alternatives, so it is enumerated explicitly rather than relaxed.

        Returns (feasible, witness).  k = 0 is the no-off-line-zeros case.
        """
        import itertools
        span = xs[-1]
        # k = 0
        if all(l <= 0.0 <= u for l, u in zip(lo_wall, up_wall)):
            return True, []
        cand = [span * i / ngrid for i in range(ngrid + 1)]
        for k in range(1, kmax + 1):
            for taus in itertools.combinations_with_replacement(cand, k):
                ok = True
                for x, l, u in zip(xs, lo_wall, up_wall):
                    mval = 0.0
                    for tau in taus:
                        if x > tau:
                            mval += mult * (x - tau)
                    if mval < l - 1e-9 or mval > u + 1e-9:
                        ok = False
                        break
                if ok:
                    return True, list(taus)
        return False, None

    feasible = []
    for c in range(c_est - 3, c_est + 4):
        vals = [D(c, t) for t in ts]
        hi, lo = max(vals), min(vals)
        vf = [float(v) for v in vals]
        Bf = float(B)
        lo_wall = [max(0.0, -Bf - v) for v in vf]
        up_wall = [Bf - v for v in vf]
        xs = [float(t - t1) for t in ts]
        # subsample for the enumeration; the walls are piecewise linear
        step = max(1, len(xs) // 400)
        ok, wit = offline_feasible(vf[::step], lo_wall[::step], up_wall[::step],
                                   xs[::step], args.multiplicity)
        if hi > Bf:
            verdict = "excluded: D exceeds +B, impossible for any off-line set"
            adm = False
        elif not ok:
            verdict = ("excluded: no admissible off-line correction exists "
                       "(slope of M is quantised in units of %d)"
                       % args.multiplicity)
            adm = False
        elif wit == []:
            verdict = "consistent with NO off-line zeros"
            adm = True
        else:
            verdict = ("requires off-line zeros at %s and that is admissible"
                       % ["%.3f" % w for w in wit])
            adm = True
        feasible.append({"c_offset": c - c_est, "max_D": float(hi),
                         "min_D": float(lo), "verdict": verdict,
                         "admissible": adm,
                         "witness_offsets": wit})

    # For every admissible c, which ordinates tau could actually host off-line
    # zeros?  This is the question that matters: a surviving alternative that
    # can only put them at the extreme edge of the window says nothing about
    # the interior.
    def admissible_taus(c, ngrid=200):
        vals = [float(D(c, t)) for t in ts]
        Bf = float(B)
        lo_wall = [max(0.0, -Bf - v) for v in vals]
        up_wall = [Bf - v for v in vals]
        xs = [float(t - t1) for t in ts]
        step = max(1, len(xs) // 300)
        xs_s, lo_s, up_s = xs[::step], lo_wall[::step], up_wall[::step]
        span = xs[-1]
        cand = [span * i / ngrid for i in range(ngrid + 1)]
        out = []
        for tau0 in cand:
            hit = False
            for partner in [None] + cand[::8]:
                taus = [tau0] if partner is None else sorted([tau0, partner])
                ok = True
                for x, l, u in zip(xs_s, lo_s, up_s):
                    mval = sum(args.multiplicity * (x - tt) for tt in taus if x > tt)
                    if mval < l - 1e-9 or mval > u + 1e-9:
                        ok = False
                        break
                if ok:
                    hit = True
                    break
            if hit:
                out.append(tau0)
        return out

    tau_map = {}
    for f in feasible:
        if f["admissible"] and f["witness_offsets"]:
            ts_ok = admissible_taus(c_est + f["c_offset"])
            tau_map[str(f["c_offset"])] = {
                "count": len(ts_ok),
                "min_offset": min(ts_ok) if ts_ok else None,
                "max_offset": max(ts_ok) if ts_ok else None,
            }

    # the unique c that is consistent with no off-line zeros
    clean = [f for f in feasible if f["verdict"].startswith("consistent")]
    admissible = [f for f in feasible if f["admissible"]]
    certified_upto = None
    if len(clean) == 1:
        c = c_est + clean[0]["c_offset"]
        Dt2 = D(c, t2)
        slack = (B - Dt2) / args.multiplicity
        certified_upto = float(t2 - slack)

    res = {
        "schema": "riemann.x5602-turing.v1",
        "agent": "opus5-01",
        "classification": "conditional on the cited Turing bound on int S, "
                          "which is an EXTERNAL dependency, and on the "
                          "correctness of the Z evaluation, which is not yet "
                          "interval-certified",
        "t1": float(t1), "t2": float(t2),
        "sign_changes_located": m,
        "smooth_census": float((theta_antideriv(t2) - A0) - (t2 - t1)),
        "turing_bound_used": float(B),
        "turing_bound_trudgian_for_reference": float(B_trudgian),
        "N_t1_estimate": c_est,
        "candidates": feasible,
        "unique_clean_c": len(clean) == 1,
        "admissible_candidates": len(admissible),
        "all_admissible_are_clean": len(admissible) == len(clean) == 1,
        "certified_free_of_offline_zeros_up_to": certified_upto,
        "admissible_tau_offsets_per_alternative": tau_map,
        "certified_window": ([float(t1), certified_upto]
                             if certified_upto else None),
        "certified_fraction": (float((certified_upto - t1) / (t2 - t1))
                               if certified_upto else 0.0),
        "note": "any off-line zero in the window must lie to the right of "
                "'certified_free_of_offline_zeros_up_to'; everything to the "
                "left is excluded by the integrated-S bound",
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
