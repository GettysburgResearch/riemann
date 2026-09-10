"""E2 extra modes: self-contained zero census, Laguerre hunt, and Lambda ladder.

census : scan H_0 on a real z-grid with auto-scaled precision. Records
         (a) certified sign changes  -> a zero census built from Phi alone,
             with no zeta evaluator and no imported zero table, and
         (b) the certified sign of the Laguerre form L_0 at every grid point.
         Any certified L_0 < 0 means Xi has a non-real zero: RH IS FALSE.

ladder : bisect in t over a fixed z window for the largest t carrying a
         CERTIFIED L_t < 0. Such a t is a certified lower bound Lambda > t,
         because a Laguerre violation at t exhibits a non-real zero of H_t.
         A violation at t >= 0 would refute RH.
"""

import argparse
import json
import sys
import time

from flint import arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import ball, certified_negative, set_prec, write_json  # noqa: E402
from e2_dbn_laguerre import H_derivs  # noqa: E402

# |Xi(z/2)| ~ exp(-pi z / 8); this many bits keeps the enclosure informative.
def prec_for(z, margin=260):
    return int(0.5665 * float(z)) + margin


def eval_point(t, z, margin=260):
    p = prec_for(z, margin)
    H0, H1, H2 = H_derivs(t, arb(z), p)
    L = (H1 * H1 - H0 * H2).real
    return H0.real, L, p


def census(z_lo, z_hi, step, budget_s, margin=260):
    t0 = time.time()
    zs, Hs, rows = [], [], []
    laguerre_negatives, uninformative = [], 0
    z = arb(z_lo)
    prev_z = prev_H = None
    sign_changes = []
    n = 0
    while float(z.mid()) <= z_hi:
        if time.time() - t0 > budget_s:
            break
        H, L, p = eval_point(arb(0), z, margin)
        conclusive_H = bool(H > 0) or bool(H < 0)
        conclusive_L = bool(L > 0) or certified_negative(L)
        if not conclusive_H or not conclusive_L:
            uninformative += 1
        if certified_negative(L):
            laguerre_negatives.append({"z": float(z.mid()), "L": ball(L), "prec": p})
        if prev_H is not None and conclusive_H:
            if (bool(prev_H > 0) and bool(H < 0)) or (bool(prev_H < 0) and bool(H > 0)):
                sign_changes.append([float(prev_z.mid()), float(z.mid())])
        rows.append(
            {
                "z": float(z.mid()),
                "H_sign": (1 if bool(H > 0) else (-1 if bool(H < 0) else 0)),
                "L_pos": bool(L > 0),
                "L_neg": certified_negative(L),
                "L_lower": float(arb(L).lower()),
                "prec": p,
            }
        )
        prev_z, prev_H = z, H
        z = z + arb(step)
        n += 1
    # tightest bracketed gap between consecutive certified sign changes
    mids = [(a + b) / 2 for a, b in sign_changes]
    gaps = [(mids[i + 1] - mids[i], mids[i], mids[i + 1]) for i in range(len(mids) - 1)]
    gaps.sort()
    return {
        "mode": "census",
        "z_range": [z_lo, z_hi],
        "step": step,
        "points_done": n,
        "elapsed_s": round(time.time() - t0, 1),
        "certified_sign_changes": len(sign_changes),
        "uninformative_points": uninformative,
        "n_laguerre_certified_negative_at_t0": len(laguerre_negatives),
        "laguerre_certified_negatives": laguerre_negatives[:20],
        "tightest_gaps": [
            {"gap_z": g, "z_left": a, "z_right": b, "predicted_collision_t": -(g * g) / 8}
            for g, a, b in gaps[:12]
        ],
        "brackets": sign_changes,
        "rows": rows,
    }


def ladder(z_center, half_width, n_probe, t_lo, t_hi, iters, budget_s, margin=260):
    """Largest t in [t_lo, t_hi] with a certified L_t < 0 on the probe grid."""
    t0 = time.time()

    def violates(t):
        for i in range(n_probe):
            z = z_center - half_width + 2 * half_width * arb(i) / arb(max(n_probe - 1, 1))
            _, L, _ = eval_point(arb(t), z, margin)
            if certified_negative(L):
                return True, float(z.mid()), ball(L)
        return False, None, None

    lo, hi = arb(t_lo), arb(t_hi)   # expect violation at lo, none at hi
    v_lo, z_lo_hit, L_lo = violates(lo)
    v_hi, _, _ = violates(hi)
    trace = [{"t": float(lo.mid()), "violates": v_lo},
             {"t": float(hi.mid()), "violates": v_hi}]
    if not v_lo:
        return {"mode": "ladder", "z_center": z_center, "status": "no violation at t_lo",
                "t_lo": float(lo.mid()), "t_hi": float(hi.mid()), "trace": trace,
                "elapsed_s": round(time.time() - t0, 1)}
    if v_hi:
        return {"mode": "ladder", "z_center": z_center,
                "status": "VIOLATION AT t_hi - widen bracket upward",
                "certified_lower_bound_on_Lambda": float(hi.mid()),
                "witness_z": z_lo_hit, "trace": trace,
                "elapsed_s": round(time.time() - t0, 1)}
    best_z, best_L = z_lo_hit, L_lo
    for _ in range(iters):
        if time.time() - t0 > budget_s:
            break
        mid = (lo + hi) / 2
        v, zz, LL = violates(mid)
        trace.append({"t": float(mid.mid()), "violates": v})
        if v:
            lo, best_z, best_L = mid, zz, LL
        else:
            hi = mid
    return {
        "mode": "ladder",
        "z_center": z_center,
        "half_width": half_width,
        "status": "bracketed",
        "certified_lower_bound_on_Lambda": float(lo.mid()),
        "no_violation_found_above": float(hi.mid()),
        "witness_z": best_z,
        "witness_L": best_L,
        "trace": trace,
        "elapsed_s": round(time.time() - t0, 1),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["census", "ladder"])
    ap.add_argument("--zlo", type=float, default=20.0)
    ap.add_argument("--zhi", type=float, default=600.0)
    ap.add_argument("--step", type=float, default=0.25)
    ap.add_argument("--zc", type=float, default=66.0)
    ap.add_argument("--hw", type=float, default=3.0)
    ap.add_argument("--probe", type=int, default=13)
    ap.add_argument("--tlo", type=float, default=-8.0)
    ap.add_argument("--thi", type=float, default=0.0)
    ap.add_argument("--iters", type=int, default=26)
    ap.add_argument("--margin", type=int, default=260)
    ap.add_argument("--budget", type=float, default=1800.0)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.mode == "census":
        res = census(a.zlo, a.zhi, a.step, a.budget, a.margin)
    else:
        res = ladder(a.zc, a.hw, a.probe, a.tlo, a.thi, a.iters, a.budget, a.margin)
    write_json(a.out, res)
    print(json.dumps({k: v for k, v in res.items()
                      if k not in ("rows", "brackets", "trace")}, indent=1)[:2200])


if __name__ == "__main__":
    main()
