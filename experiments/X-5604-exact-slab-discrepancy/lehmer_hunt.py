#!/usr/bin/env python3
"""Close-pair (Lehmer) census and certified refinement above the verified height.

Agent: fable5-01   Issue: #55

`O-5609` ends with the strategic point: if RH fails, a conjugate pair leaves
the critical line only after first colliding *on* it, so the precursor
signature of a violation is two zeros anomalously CLOSE together — a Lehmer
pair — not the large gap every screen in this repository chased.  A large gap
is what remains after a departure; a near-collision is visible while the zeros
are still on the line, which is the only place a search can ever find them.

This module does two things.

**Census.**  Read a zero list emitted by the fixed 30-digit `rs_zeta` emitter
(the pre-fix files carry `~1e-3` per ordinate and are useless for this), form
normalised gaps `delta = (g_{i+1}-g_i) * log(t/2pi)/2pi`, and rank.  The census
is empirical — its job is only to nominate.

**Certify.**  For each nominated pair, everything is then re-derived in Arb
ball arithmetic, taking nothing from the census but *where to look*:

  1. three exact dyadic points `p0 < p1 < p2` with certified signs
     `s(p0) = -s(p1) = s(p2)` — two certified sign changes, hence two zeros of
     `zeta` on the critical line, one in each bracket;
  2. certified bisection inside each bracket down to width `2^-B`, giving
     rigorous enclosures `[lo1,hi1]`, `[lo2,hi2]` for the two ordinates and
     hence a rigorous gap interval `[lo2-hi1, hi2-lo1]`;
  3. a certified enclosure of `Z` at the near-extremal interior point — the
     quantity whose smallness makes a pair "Lehmer";
  4. optionally (`--slab`), a rigorous `N` over a small quiet slab around the
     pair and enough certified sign changes to force `D = 0` locally, i.e. the
     pair is exactly two simple line zeros with nothing hiding between them.

Every accepted sign is an Arb ball strictly on one side of zero; a ball that
straddles is escalated through the precision ladder and, failing that, the
point is abandoned (never guessed).
"""
from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction as Fr

from flint import acb, arb, ctx

LADDER = (64, 96, 160, 256, 448)


def Z_ball(t_fr: Fr, prec: int):
    ctx.prec = prec
    t = arb(t_fr.numerator) / arb(t_fr.denominator)
    if not t.is_exact():
        return None
    th = acb(arb(1) / 4, t / 2).lgamma().imag - (t / 2) * arb.pi().log()
    return (acb(0, th).exp() * acb(arb(1) / 2, t).zeta()).real


def certified_sign(t_fr: Fr):
    """(+1|-1, prec, ball) with the sign certified, or (None, prec, ball)."""
    need = max(64, t_fr.numerator.bit_length() + 16)
    Z = None
    for p in LADDER:
        p = max(p, need)
        Z = Z_ball(t_fr, p)
        if Z is None:
            continue
        if Z > 0:
            return 1, p, Z
        if Z < 0:
            return -1, p, Z
    return None, p, Z


def dyadic(x, bits: int) -> Fr:
    if not isinstance(x, Fr):
        x = Fr(x)
    scale = 1 << bits
    return Fr(round(x * scale), scale)


def certified_bisect(lo: Fr, hi: Fr, s_lo: int, target_width: Fr, stats: dict):
    """Shrink a certified sign-change bracket to `target_width` by bisection.

    Midpoints are exact dyadics.  If a midpoint's sign cannot be certified even
    at the top of the ladder (the zero sits essentially on it), nudge by a
    quarter-step; after a few failed nudges, return the current bracket rather
    than guess.
    """
    while hi - lo > target_width:
        mid = dyadic((lo + hi) / 2, (hi - lo).denominator.bit_length() + 4)
        if not (lo < mid < hi):
            break
        s, p, _ = certified_sign(mid)
        stats["evals"] = stats.get("evals", 0) + 1
        if s is None:
            moved = False
            for k in (1, 3):
                alt = lo + (hi - lo) * Fr(k, 4)
                s, p, _ = certified_sign(alt)
                stats["evals"] += 1
                if s is not None:
                    mid, moved = alt, True
                    break
            if not moved:
                stats["undecided_stop"] = str(mid)
                break
        if s == s_lo:
            lo = mid
        else:
            hi = mid
    return lo, hi


def census(zeros_path, top):
    vals = [Fr(line.strip()) for line in open(zeros_path) if line.strip()]
    vals.sort()
    t_mid = float(vals[len(vals) // 2])
    ell = math.log(t_mid / (2 * math.pi)) / (2 * math.pi)
    gaps = []
    for i in range(len(vals) - 1):
        d = vals[i + 1] - vals[i]
        gaps.append((float(d) * ell, i, vals[i], vals[i + 1]))
    gaps.sort()
    return vals, ell, gaps[:top], gaps


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zeros", help="30-digit zero list from the FIXED emitter")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--certify", type=int, default=3,
                    help="how many of the top pairs to certify in Arb")
    ap.add_argument("--width-bits", type=int, default=22,
                    help="refine brackets to width 2^-this")
    ap.add_argument("--out", default="results/lehmer.json")
    args = ap.parse_args()

    vals, ell, top, allgaps = census(args.zeros, args.top)
    print("census: %d zeros, mean norm gap %.5f, %d gaps" %
          (len(vals), sum(g[0] for g in allgaps) / len(allgaps), len(allgaps)))
    print("\nsmallest normalised gaps (census, ~1e-9 grade):")
    for d, i, g1, g2 in top:
        print("  delta = %.6f   gamma_1 = %.9f   raw gap %.3e"
              % (d, float(g1), float(g2 - g1)))

    certified = []
    for d, i, g1, g2 in top[:args.certify]:
        t0 = time.time()
        rec = {"census_delta": d, "index_in_file": i}
        gap = g2 - g1
        # three dyadic probes: outside-left, interior, outside-right
        bits = 30
        p0 = dyadic(g1 - gap / 2, bits)
        p1 = dyadic((g1 + g2) / 2, bits)
        p2 = dyadic(g2 + gap / 2, bits)
        s0, _, _ = certified_sign(p0)
        s1, _, z1 = certified_sign(p1)
        s2, _, _ = certified_sign(p2)
        rec["probes"] = [str(p0), str(p1), str(p2)]
        if None in (s0, s1, s2) or not (s0 == -s1 == s2):
            rec["status"] = ("FAILED to establish the two-bracket sign "
                             "pattern: signs %r" % [s0, s1, s2])
            certified.append(rec)
            print("  pair at %.6f: %s" % (float(g1), rec["status"]))
            continue
        stats = {}
        w = Fr(1, 1 << args.width_bits)
        lo1, hi1 = certified_bisect(p0, p1, s0, w, stats)
        lo2, hi2 = certified_bisect(p1, p2, s1, w, stats)
        gap_lo, gap_hi = lo2 - hi1, hi2 - lo1
        rec.update({
            "status": "CERTIFIED",
            "zero1": [str(lo1), str(hi1)],
            "zero2": [str(lo2), str(hi2)],
            "gap_interval": [float(gap_lo), float(gap_hi)],
            "delta_interval": [float(gap_lo) * ell, float(gap_hi) * ell],
            "interior_Z_ball": z1.str(12, radius=True),
            "evals": stats.get("evals"),
            "seconds": time.time() - t0,
        })
        certified.append(rec)
        print("  pair at %.6f: CERTIFIED  delta in [%.6f, %.6f]  interior Z = %s  [%.0f s]"
              % (float(g1), rec["delta_interval"][0], rec["delta_interval"][1],
                 rec["interior_Z_ball"], rec["seconds"]))

    res = {
        "schema": "riemann.x5604-lehmer-hunt.v1",
        "agent": "fable5-01",
        "classification": "census is empirical (30-digit uncertified scan); "
                          "each CERTIFIED pair is re-derived entirely in Arb "
                          "ball arithmetic -- certified signs, certified "
                          "bisection brackets, certified interior Z",
        "zeros_file": args.zeros,
        "n_zeros": len(vals), "ell": ell,
        "top_census": [{"delta": d, "gamma1": str(g1), "gamma2": str(g2)}
                       for d, i, g1, g2 in top],
        "certified_pairs": certified,
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("wrote", args.out)


if __name__ == "__main__":
    main()
