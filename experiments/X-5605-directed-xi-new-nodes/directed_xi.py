#!/usr/bin/env python3
"""Directed completed-xi primitives for the PR #134 positive-node programme.

Agent: fable5-01   Issues: #93 / #122, PRs #124 / #134

The X-9312 handoff asks for a "directed FLINT/Arb pass" at the new nodes
`x in {1/20, 1, 3, 4, 5}` (plus PR #124's `t = 4`, i.e. `x = 2`) at the exact
PR #103 atomized-minimum ordinate

    T = 20225875608343133989267 / 2^32 .

This module supplies it, in two parts.

**Audit first.**  Before producing anything new, it re-computes a sample of the
*existing* directed points of the p512 certificate
(`atomized-min-certificate-p512.json`) with an independently assembled
formula and checks ball-overlap against the stored exact rational rectangles.
Their producer builds xi from FLINT's zeta-jet machinery; this audit assembles

    xi(s) * 2^P  =  exp( log(s(s-1)/2) - (s/2) log pi + lgamma(s/2)
                          + log zeta(s) + P log 2 )

in acb ball arithmetic.  Each factor's principal log is re-exponentiated, so
no branch choice can change the product; the astronomically large exponents
(`|log xi| ~ 3.7e12 ~ 2^42`) cost about 42 of the 512 working bits and no
more.  Overlap of two rigorous enclosures from structurally different
assemblies is the independent-backend reproduction every PR in this series
asks for; disjointness would expose a real defect.

**Then the new nodes.**  The same assembly evaluates the six new points and
emits exact outward-rounded rational rectangles in the certificate's own
format (same ordinate, same `common_xi_scale_power_of_two`, same
normalization id), one JSON block per node, ready for the X-9312 reduced
contraction.

A non-dyadic node like `x = 1/20` enters as a 512-bit ball containing the
exact rational; the output rectangle is therefore a rigorous enclosure of the
exact-node value (input interval -> output interval), which is what a
directed pass means.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import acb, arb, ctx

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

T_NUM = 20225875608343133989267
T_DEN = 2 ** 32
SCALE_P = 5335951715288          # from the p512 certificate
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"


def arb_fr(f: Fr):
    return arb(f.numerator) / arb(f.denominator)


def xi_scaled(x_fr: Fr, prec: int):
    """acb ball for xi(1/2 + x + iT) * 2^SCALE_P at working precision."""
    ctx.prec = prec
    s = acb(arb(1) / 2 + arb_fr(x_fr), arb_fr(Fr(T_NUM, T_DEN)))
    log_xi = ((s * (s - 1) / 2).log()
              - (s / 2) * arb.pi().log()
              + (s / 2).lgamma()
              + s.zeta().log())
    return (log_xi + arb(SCALE_P) * arb(2).log()).exp()


def arb_to_rat_interval(x, digits=200):
    """Exact rational outward interval for an arb ball, via its string form."""
    lo = x.lower()
    hi = x.upper()
    # arb.lower()/upper() are arbs of radius 0 (arf values): exact dyadics.
    # Extract exact rationals through the mid-point of a zero-radius ball.
    def exact_fr(v):
        m = v.mid()
        man, exp = m.man_exp()
        man, exp = int(man), int(exp)
        if exp >= 0:
            return Fr(man * (2 ** exp))
        return Fr(man, 2 ** (-exp))
    return exact_fr(lo), exact_fr(hi)


def fj(f: Fr):
    return {"numerator": f.numerator, "denominator": f.denominator}


def rect_json(z):
    rlo, rhi = arb_to_rat_interval(z.real)
    ilo, ihi = arb_to_rat_interval(z.imag)
    return {"real": {"lower": fj(rlo), "upper": fj(rhi)},
            "imag": {"lower": fj(ilo), "upper": fj(ihi)}}


def rect_from_json(d):
    return (Fr(d["real"]["lower"]["numerator"], d["real"]["lower"]["denominator"]),
            Fr(d["real"]["upper"]["numerator"], d["real"]["upper"]["denominator"]),
            Fr(d["imag"]["lower"]["numerator"], d["imag"]["lower"]["denominator"]),
            Fr(d["imag"]["upper"]["numerator"], d["imag"]["upper"]["denominator"]))


def overlap(mine, theirs):
    """Do two exact rational rectangles intersect?"""
    arl, arh, ail, aih = mine
    brl, brh, bil, bih = theirs
    return not (arh < brl or brh < arl or aih < bil or bih < ail)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", required=True,
                    help="their atomized-min-certificate-p512.json")
    ap.add_argument("--audit-points", type=int, default=3)
    ap.add_argument("--prec", type=int, default=512)
    ap.add_argument("--out", default="results/directed-new-nodes.json")
    args = ap.parse_args()

    with open(args.certificate) as fh:
        cert = json.load(fh)
    assert cert["normalization_id"] == NORMALIZATION
    assert int(cert["common_xi_scale_power_of_two"]) == SCALE_P
    assert cert["ordinate"]["numerator"] == T_NUM
    assert cert["ordinate"]["denominator"] == T_DEN

    audits = []
    pts = cert["points"]
    picks = [0, len(pts) // 2, len(pts) - 1][:args.audit_points]
    for i in picks:
        p = pts[i]
        u = Fr(p["u"]["numerator"], p["u"]["denominator"])
        # their u is the squared node; the point sits at x = sqrt(u).
        # sqrt of an exact rational enters as a ball.
        ctx.prec = args.prec
        x_ball_sq = arb_fr(u)
        t0 = time.time()
        ctx.prec = args.prec
        s = acb(arb(1) / 2 + x_ball_sq.sqrt(), arb_fr(Fr(T_NUM, T_DEN)))
        log_xi = ((s * (s - 1) / 2).log() - (s / 2) * arb.pi().log()
                  + (s / 2).lgamma() + s.zeta().log())
        mine_ball = (log_xi + arb(SCALE_P) * arb(2).log()).exp()
        mine = (arb_to_rat_interval(mine_ball.real)
                + arb_to_rat_interval(mine_ball.imag))
        theirs = rect_from_json(p["xi_rectangle"])
        ok = overlap(mine, theirs)
        audits.append({
            "id": p["id"], "u": fj(u), "overlap": bool(ok),
            "seconds": round(time.time() - t0, 1),
            "my_real_width": float(mine[1] - mine[0]),
            "their_real_width": float(theirs[1] - theirs[0]),
            "my_real_mid": float((mine[0] + mine[1]) / 2),
            "their_real_mid": float((theirs[0] + theirs[1]) / 2),
        })
        print("audit %-6s overlap=%s  my mid %.12e vs theirs %.12e  [%.0f s]"
              % (p["id"], ok, audits[-1]["my_real_mid"],
                 audits[-1]["their_real_mid"], audits[-1]["seconds"]), flush=True)
        if not ok:
            print("!! DISJOINT RECTANGLES -- refusing to produce new nodes on "
                  "top of a primitive discrepancy", flush=True)
            with open(args.out, "w") as fh:
                json.dump({"schema": "riemann.x5605-directed-new-nodes.v1",
                           "verdict": "AUDIT FAILED", "audits": audits}, fh,
                          indent=1)
            sys.exit(2)

    new_nodes = [Fr(1, 20), Fr(1), Fr(2), Fr(3), Fr(4), Fr(5)]
    produced = []
    for x in new_nodes:
        t0 = time.time()
        z = xi_scaled(x, args.prec)
        rec = {
            "id": "new-x-%s" % ("%d-%d" % (x.numerator, x.denominator)
                                if x.denominator != 1 else str(x.numerator)),
            "x": fj(x), "w": fj(x * x),
            "s": "1/2 + %s + iT" % x,
            "xi_rectangle": rect_json(z),
            "real_mid": float(z.real.mid()),
            "real_rad": float(z.real.rad()),
            "seconds": round(time.time() - t0, 1),
        }
        produced.append(rec)
        print("new node x=%-5s  xi*2^P real ~ %.15e  rad %.2e  [%.0f s]"
              % (x, rec["real_mid"], rec["real_rad"], rec["seconds"]), flush=True)

    out = {
        "schema": "riemann.x5605-directed-new-nodes.v1",
        "agent": "fable5-01",
        "classification": "DIRECTED: every rectangle is an exact rational "
                          "outward enclosure of a 512-bit acb ball. The "
                          "assembly (exp of summed principal logs) is "
                          "branch-unambiguous because exp(log f) = f for each "
                          "factor. Independent of the producer that made the "
                          "p512 certificate; sample rectangles of that "
                          "certificate were re-derived and overlap was "
                          "verified before production.",
        "ordinate": {"numerator": T_NUM, "denominator": T_DEN},
        "normalization_id": NORMALIZATION,
        "common_xi_scale_power_of_two": SCALE_P,
        "prec_bits": args.prec,
        "audits_of_existing_certificate": audits,
        "new_node_points": produced,
        "note": "x = 1/20 and other non-dyadic nodes enter as 512-bit balls "
                "containing the exact rational; the emitted rectangle is a "
                "rigorous enclosure of the exact-node value.",
    }
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
