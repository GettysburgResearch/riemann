#!/usr/bin/env python3
"""Certified lower bound on N_0: count sign changes of Z with Arb ball arithmetic.

Agent: opus5-01   Issue: #55

`slab_discrepancy.py` computes `N(a,b)` rigorously.  To get
`D = N - N_0` we need `N_0`, and enumerating zeros with
`acb_dirichlet_zeta_zeros` at index `~2e13` is slow.  There is a much cheaper
route to a certified **lower bound**, which is all that is needed: if
`N_0 >= N`, then since `N_0 <= N` always, `N_0 = N` and `D = 0`.

A certified sign change of Hardy's `Z` between two points is a certified zero of
`zeta` on the critical line between them.  So it suffices to exhibit sample
points at which the sign of `Z` is certified, and count alternations.

`Z(t) = e^{i theta(t)} zeta(1/2 + it)` with

    theta(t) = Im log Gamma(1/4 + it/2) - (t/2) log pi .

The branch is not a problem: `Re(1/4 + it/2) = 1/4 > 0`, and on the right
half-plane `log Gamma` is the analytic continuation from `log Gamma(1) = 0`,
which is exactly what Arb's `lgamma` computes.  This was checked against the
independent Stirling expansion
`theta = (t/2)log(t/2pi) - t/2 - pi/8 + 1/(48t) + 7/(5760 t^3)`; the two agree
to `5e-63` at the test ordinate, so no branch correction is needed and no
asymptotic remainder bound is imported.

Everything is Arb ball arithmetic, so a reported sign is certified: the program
counts a sign only when the ball for `Z` lies strictly on one side of zero, and
refuses otherwise.  Sample points are exact dyadic rationals.
"""
from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction as Fr

from flint import acb, arb, ctx


def dyadic_near(x: float, bits: int = 20) -> Fr:
    """The exact dyadic rational with `bits` fractional bits nearest to x."""
    return Fr(round(x * (1 << bits)), 1 << bits)


def as_arb(f: Fr):
    v = arb(f.numerator) / arb(f.denominator)
    if not v.is_exact():
        raise ValueError("sample point %s is not exact in arb" % f)
    return v


def Z_ball(t_fr: Fr):
    """Rigorous enclosure of Hardy's Z(t) at the exact dyadic t."""
    t = as_arb(t_fr)
    theta = acb(arb(1) / 4, t / 2).lgamma().imag - (t / 2) * arb.pi().log()
    return (acb(0, theta).exp() * acb(arb(1) / 2, t).zeta()).real


def certified_sign(z):
    """+1 / -1 if the ball lies strictly on one side of 0, else None."""
    if z > 0:
        return 1
    if z < 0:
        return -1
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("zeros", help="approximate zero ordinates, one per line; "
                                  "used ONLY to choose sample points")
    ap.add_argument("--a", required=True, help="left endpoint, exact dyadic")
    ap.add_argument("--b", required=True, help="right endpoint, exact dyadic")
    ap.add_argument("--prec", type=int, default=192)
    ap.add_argument("--bits", type=int, default=20,
                    help="fractional bits for the dyadic sample points")
    ap.add_argument("--expected-N", type=int, default=None,
                    help="the rigorous N(a,b); if given, D is reported")
    ap.add_argument("--out", default="sign-changes.json")
    args = ap.parse_args()

    ctx.prec = args.prec
    a, b = Fr(args.a), Fr(args.b)

    g = sorted(float(x) for x in open(args.zeros))
    g = [x for x in g if float(a) < x < float(b)]
    if not g:
        raise SystemExit("no approximate zeros inside the slab")

    # Sample points: strictly between consecutive approximate zeros, plus one
    # just inside each endpoint.  Their exact positions do not matter -- only
    # the CERTIFIED signs at them do.  A wrong guide zero costs a sign change,
    # it cannot manufacture one.
    pts = [dyadic_near((float(a) + g[0]) / 2, args.bits)]
    for i in range(len(g) - 1):
        pts.append(dyadic_near((g[i] + g[i + 1]) / 2, args.bits))
    pts.append(dyadic_near((g[-1] + float(b)) / 2, args.bits))
    pts = [p for p in pts if a < p < b]
    pts = sorted(set(pts))

    print("slab (%s, %s), %d guide zeros, %d sample points"
          % (float(a), float(b), len(g), len(pts)), flush=True)

    t0 = time.time()
    signs, undecided = [], []
    for i, p in enumerate(pts):
        z = Z_ball(p)
        s = certified_sign(z)
        if s is None:
            undecided.append({"index": i, "t": str(p), "Z": z.str(15, radius=True)})
        signs.append(s)
        if (i + 1) % 25 == 0:
            print("  %d/%d  [%.0f s]" % (i + 1, len(pts), time.time() - t0), flush=True)
    dt = time.time() - t0

    # count alternations across consecutive DECIDED samples
    changes, last = 0, None
    for s in signs:
        if s is None:
            last = None            # a gap in the chain: conservatively break it
            continue
        if last is not None and s != last:
            changes += 1
        last = s

    res = {
        "schema": "riemann.x5604-certified-sign-changes.v1",
        "agent": "opus5-01",
        "classification": "RIGOROUS lower bound on N_0. Every sign is an Arb "
                          "ball certified strictly on one side of zero. The "
                          "guide zero list only chooses sample points and "
                          "cannot manufacture a sign change.",
        "a": str(a), "b": str(b), "prec_bits": args.prec,
        "sample_points": len(pts),
        "undecided_samples": undecided,
        "certified_sign_changes": changes,
        "seconds": dt,
        "N0_lower_bound": changes,
    }
    print("\ncertified sign changes in the slab: %d   [%.0f s]" % (changes, dt))
    if undecided:
        print("WARNING: %d samples had an undecided sign" % len(undecided))

    if args.expected_N is not None:
        N = args.expected_N
        res["N_total"] = N
        if changes > N:
            res["verdict"] = ("INCONSISTENT: more certified critical-line zeros "
                              "(%d) than the rigorous total count (%d). One of "
                              "the two computations is wrong; refusing to "
                              "conclude anything." % (changes, N))
        elif changes == N:
            res["D_upper_bound"] = 0
            res["D"] = 0
            res["verdict"] = (
                "CERTIFIED D = 0: N_0 >= %d certified sign changes, and "
                "N_0 <= N = %d, so N_0 = N and the slab contains NO zero off "
                "the critical line. Unconditional." % (changes, N))
        else:
            res["D_upper_bound"] = N - changes
            res["verdict"] = (
                "INCOMPLETE: N = %d, certified N_0 >= %d, so D <= %d. Not yet "
                "zero -- add sample points, or the guide list is missing zeros."
                % (N, changes, N - changes))
        print(res["verdict"])

    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("wrote", args.out)


if __name__ == "__main__":
    main()
