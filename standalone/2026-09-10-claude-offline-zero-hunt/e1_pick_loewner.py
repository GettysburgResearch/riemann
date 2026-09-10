"""E1 - directed sweep of the repository's derivative-free RH-necessary predicates.

Source of the predicates:
  research/integrated/xi/derivative-free-pick-loewner.md
  (integrated packet, review verdict VERIFIED for PR #48 and PR #52)

Under RH the following are all >= 0 at every admissible node set. A CERTIFIED
strict negative at a point where the xi enclosure justifies division is a finite
RH disproof witness.

  P1 secant           S(i,j)   = (J_j - J_i)/(u_j - u_i)
  P2 channel A        A(i,j)   = (H_i - H_j)/(u_j - u_i)
  P4 Loewner 2x2      det of [(J(u_p) - J(v_q))/(u_p - v_q)]
  P5 barycentric Pick sum_i d_i R_i,  d_i = 2 c_i sum_j c_j/(x_i + x_j)
  P6 divided diff     (-1)^(n-1) [u_0..u_n] J

with R_i = Re F(1/2 + x_i + i T), J_i = x_i R_i, H_i = R_i / x_i, u_i = x_i^2.

The packet reports, for every evaluated ordinate, the certified sign verdict and
the enclosure of each predicate. Midpoints are orientation only.

Two modes:
  sweep      - run the predicates against actual zeta over an ordinate band
  calibrate  - inject a synthetic off-line pair into the RH resolvent form and
               locate the detection boundary in (delta, tau); this quantifies
               exactly which off-line pairs a given ordinate grid can exclude.
"""

import argparse
import json
import sys
import time

from flint import acb, arb, ctx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import R_of, ball, certified_negative, set_prec, write_json  # noqa: E402

# Offsets are exact negative powers of two, matching the node style of the
# integrated finite Pick controls (Control A used 2^-17 ... 2^-5).
OFFSET_EXPS = list(range(5, 18))


def offsets(exps):
    return [arb(1) / arb(2) ** e for e in exps]


def responses(T, xs):
    """R_T(x) for each offset; returns (list, rejected_count)."""
    out, rejected = [], 0
    for x in xs:
        R, ok = R_of(T, x)
        if not ok:
            rejected += 1
            out.append(None)
        else:
            out.append(R)
    return out, rejected


def synthetic_responses(xs, tau, delta, gaps):
    """R_T(x) built from an explicit zero configuration, no zeta involved.

    `gaps` are ordinate offsets (T - gamma) of ordinary critical-line zeros,
    each contributing x/(x^2 + gap^2). If delta > 0 an off-line mirror pair at
    horizontal displacement delta and ordinate offset tau is added, contributing
    (x-delta)/((x-delta)^2 + tau^2) + (x+delta)/((x+delta)^2 + tau^2).
    """
    out = []
    for x in xs:
        acc = arb(0)
        for g in gaps:
            acc += x / (x * x + g * g)
        if delta > 0:
            a = x - delta
            b = x + delta
            acc += a / (a * a + tau * tau) + b / (b * b + tau * tau)
        out.append(acc)
    return out


def predicates(xs, Rs):
    """Evaluate every predicate. Returns list of (name, ball_or_None)."""
    n = len(xs)
    us = [x * x for x in xs]
    J = [None if R is None else xs[i] * R for i, R in enumerate(Rs)]
    H = [None if R is None else R / xs[i] for i, R in enumerate(Rs)]
    res = []

    # P1 / P2 over all pairs i < j (x decreasing in exponent order, so u_i > u_j
    # when exps ascend; normalise by sorting on u).
    order = sorted(range(n), key=lambda i: float(arb(us[i]).mid()))
    for a in range(n):
        for b in range(a + 1, n):
            i, j = order[a], order[b]  # u_i < u_j
            if J[i] is None or J[j] is None:
                continue
            res.append(("P1_secant_%d_%d" % (i, j), (J[j] - J[i]) / (us[j] - us[i])))
            res.append(("P2_chanA_%d_%d" % (i, j), (H[i] - H[j]) / (us[j] - us[i])))

    # P4 cross-Loewner 2x2 minors on cross-disjoint node pairs.
    def Lentry(ui, uj, Ji, Jj):
        return (Ji - Jj) / (ui - uj)

    for a in range(0, n - 3, 2):
        p1, p2, q1, q2 = order[a], order[a + 2], order[a + 1], order[a + 3]
        if any(J[k] is None for k in (p1, p2, q1, q2)):
            continue
        m11 = Lentry(us[p1], us[q1], J[p1], J[q1])
        m12 = Lentry(us[p1], us[q2], J[p1], J[q2])
        m21 = Lentry(us[p2], us[q1], J[p2], J[q1])
        m22 = Lentry(us[p2], us[q2], J[p2], J[q2])
        res.append(("P4_loewner2x2_%d" % a, m11 * m22 - m12 * m21))

    # P5 barycentric Pick and P6 divided differences on consecutive triples and
    # quadruples (spanning sets are catastrophically ill-conditioned here).
    for width in (3, 4):
        for a in range(0, n - width + 1):
            idx = [order[a + t] for t in range(width)]
            if any(J[k] is None for k in idx):
                continue
            xi = [xs[k] for k in idx]
            ui = [us[k] for k in idx]
            c = []
            for p in range(width):
                d = arb(1)
                for q in range(width):
                    if q != p:
                        d *= xi[p] - xi[q]
                c.append(1 / d)
            dvec, amp = [], arb(0)
            for p in range(width):
                acc = arb(0)
                for q in range(width):
                    acc += c[q] / (xi[p] + xi[q])
                dvec.append(2 * c[p] * acc)
                amp += abs(dvec[p])
            val = arb(0)
            for p in range(width):
                val += dvec[p] * Rs[idx[p]]
            res.append(("P5_pick%d_%d" % (width, a), val))

            dd = arb(0)
            for p in range(width):
                den = arb(1)
                for q in range(width):
                    if q != p:
                        den *= ui[p] - ui[q]
                dd += J[idx[p]] / den
            sign = 1 if (width - 2) % 2 == 0 else -1
            res.append(("P6_divdiff%d_%d" % (width, a), sign * dd))
    return res


def scan_ordinate(T, xs):
    Rs, rejected = responses(T, xs)
    preds = predicates(xs, Rs)
    worst_name, worst_lower, worst_ball = None, None, None
    violations = []
    inconclusive = 0
    for name, v in preds:
        if v is None:
            continue
        lo = float(arb(v).lower())
        if certified_negative(v):
            violations.append({"predicate": name, "enclosure": ball(v)})
        elif not bool(arb(v) > 0):
            inconclusive += 1
        if worst_lower is None or lo < worst_lower:
            worst_lower, worst_name, worst_ball = lo, name, v
    return {
        "n_predicates": len(preds),
        "rejected_points": rejected,
        "violations": violations,
        "inconclusive": inconclusive,
        "worst_predicate": worst_name,
        "worst_enclosure": ball(worst_ball) if worst_ball is not None else None,
    }


def run_sweep(label, T0_num, T0_den, step_num, step_den, count, exps, budget_s, prec):
    set_prec(prec)
    xs = offsets(exps)
    t_start = time.time()
    rows, all_violations = [], []
    worst = None
    done = 0
    for k in range(count):
        if time.time() - t_start > budget_s:
            break
        T = arb(T0_num) / arb(T0_den) + arb(k) * arb(step_num) / arb(step_den)
        r = scan_ordinate(T, xs)
        r["T_mid"] = float(arb(T).mid())
        r["k"] = k
        done += 1
        if r["violations"]:
            all_violations.append(r)
        wl = r["worst_enclosure"]["lower"] if r["worst_enclosure"] else None
        if wl is not None and (worst is None or wl < worst["worst_enclosure"]["lower"]):
            worst = r
        rows.append(
            {
                "k": k,
                "T": r["T_mid"],
                "worst": r["worst_predicate"],
                "worst_lower": wl,
                "incon": r["inconclusive"],
                "rej": r["rejected_points"],
            }
        )
    return {
        "label": label,
        "prec_bits": prec,
        "offset_exponents": exps,
        "T_start": float((arb(T0_num) / arb(T0_den)).mid()),
        "step": float((arb(step_num) / arb(step_den)).mid()),
        "ordinates_requested": count,
        "ordinates_done": done,
        "elapsed_s": round(time.time() - t_start, 1),
        "certified_violations": all_violations,
        "n_certified_violations": len(all_violations),
        "worst_case": worst,
        "rows": rows,
    }


def run_calibration(exps, prec):
    """Locate the (delta, tau) detection boundary of the predicates.

    Background: a realistic local zero field at height ~1e12, mean gap
    2*pi/log(T/2pi) ~ 0.22, represented by 41 neighbours on that spacing.
    """
    set_prec(prec)
    xs = offsets(exps)
    mean_gap = arb("0.22")
    gaps = [arb(m) * mean_gap for m in range(-20, 21) if m != 0]
    out = []
    for de in range(6, 18):
        delta = arb(1) / arb(2) ** de
        # bisect on tau: detection succeeds for small |tau|, fails for large.
        lo_t, hi_t = arb(0), arb(4) * delta * arb(2) ** 6
        detected_at_zero = False
        r0 = predicates(xs, synthetic_responses(xs, arb(0), delta, gaps))
        detected_at_zero = any(certified_negative(v) for _, v in r0 if v is not None)
        if not detected_at_zero:
            out.append({"delta_exp": de, "delta": float(arb(delta).mid()), "tau_max": 0.0,
                        "detected_at_tau0": False})
            continue
        for _ in range(40):
            mid = (lo_t + hi_t) / 2
            rs = predicates(xs, synthetic_responses(xs, mid, delta, gaps))
            if any(certified_negative(v) for _, v in rs if v is not None):
                lo_t = mid
            else:
                hi_t = mid
        out.append(
            {
                "delta_exp": de,
                "delta": float(arb(delta).mid()),
                "tau_max": float(arb(lo_t).mid()),
                "detected_at_tau0": True,
                "required_ordinate_step": float(arb(2 * lo_t).mid()),
            }
        )
    return {"prec_bits": prec, "offset_exponents": exps, "mean_gap": 0.22, "boundary": out}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["sweep", "calibrate"])
    ap.add_argument("--label", default="band")
    ap.add_argument("--t0-num", type=int, default=3 * 10**12)
    ap.add_argument("--t0-den", type=int, default=1)
    ap.add_argument("--step-num", type=int, default=1)
    ap.add_argument("--step-den", type=int, default=8)
    ap.add_argument("--count", type=int, default=100)
    ap.add_argument("--budget", type=float, default=600.0)
    ap.add_argument("--prec", type=int, default=220)
    ap.add_argument("--exps", default=",".join(str(e) for e in OFFSET_EXPS))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    exps = [int(t) for t in a.exps.split(",")]
    if a.mode == "calibrate":
        res = run_calibration(exps, a.prec)
    else:
        res = run_sweep(
            a.label, a.t0_num, a.t0_den, a.step_num, a.step_den, a.count, exps,
            a.budget, a.prec,
        )
    write_json(a.out, res)
    print(json.dumps({k: v for k, v in res.items() if k not in ("rows", "boundary")},
                     indent=1)[:1500])


if __name__ == "__main__":
    main()
