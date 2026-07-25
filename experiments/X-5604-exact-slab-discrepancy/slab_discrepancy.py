#!/usr/bin/env python3
"""The exact slab discrepancy D(a,b) = N(a,b) - N_0(a,b), computed with Arb.

Agent: opus5-01   Issue: #55

Everything this repository has said about the PR #71 ordinate has been
*conditional*: the census is empirical, and the Turing argument in `turing.py`
imports an unproved bound on `\\int S` and rests on an uncertified `Z`.  This
module removes both conditions by using rigorous primitives instead.

    N(a,b)    total zeros of zeta with a < Im rho < b, IN THE WHOLE STRIP,
              counted with multiplicity.  Arb's `zeta_nzeros` computes N(t)
              rigorously (Platt/Turing); every value it returns is a ball, and
              a result is used only when the ball isolates a single integer.

    N_0(a,b)  zeros ON the critical line in the same range.  Arb's `zeta_zeros`
              returns rigorously isolated zeros.

    D(a,b) = N(a,b) - N_0(a,b)  is exactly the number of off-critical zeros in
              the slab, counted with multiplicity, and is >= 0.

Hence, with no conditions at all:

    D(a,b) > 0  ==>  RH is false.
    D(a,b) = 0  ==>  every zero in the slab is on the critical line.

The special case that needs no line-count at all, and is therefore the cleanest
object to aim a search at:

    if (a,b) contains no zero of Z and N(a,b) > 0, then RH is false.

`N(a,b) = 0` is stronger still: the slab is empty of zeros of every kind.

The endpoints are taken as exact dyadic rationals so that they are represented
in Arb without rounding; the script refuses any endpoint that is not exact.
"""
from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction as Fr

from flint import arb, acb, ctx


def dyadic(s):
    """Parse an exact dyadic rational 'p/q' (q a power of two) or a decimal."""
    if "/" in s:
        f = Fr(s)
    else:
        f = Fr(s)
    q = f.denominator
    if q & (q - 1):
        raise ValueError("endpoint %s is not dyadic (denominator %d)" % (s, q))
    return f


def as_arb(f: Fr):
    x = arb(f.numerator) / arb(f.denominator)
    if not x.is_exact():
        raise ValueError("endpoint %s did not survive as an exact arb" % f)
    return x


def unique_int(ball, what):
    """The unique integer in `ball`, or raise.  This is the fail-closed gate:
    Arb returns a ball, and a count is only usable when the ball admits exactly
    one integer.  `unique_fmpz` returns None when it does not."""
    n = ball.unique_fmpz()
    if n is None:
        raise ValueError("%s does not isolate a unique integer: %s"
                         % (what, ball.str(30, radius=True)))
    return int(n)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="left endpoint, exact dyadic")
    ap.add_argument("--b", required=True, help="right endpoint, exact dyadic")
    ap.add_argument("--prec", type=int, default=192)
    ap.add_argument("--target", default=None,
                    help="an ordinate that must lie strictly inside (a,b)")
    ap.add_argument("--list-zeros", action="store_true",
                    help="also enumerate the critical-line zeros and compute D")
    ap.add_argument("--max-list", type=int, default=400)
    ap.add_argument("--out", default="slab.json")
    args = ap.parse_args()

    ctx.prec = args.prec
    a, b = dyadic(args.a), dyadic(args.b)
    if not a < b:
        raise SystemExit("need a < b")

    res = {
        "schema": "riemann.x5604-slab-discrepancy.v1",
        "agent": "opus5-01",
        "classification": "RIGOROUS: every zero count below is an Arb ball that "
                          "isolates a single integer. No conjecture, no imported "
                          "bound, no floating-point sign decision.",
        "backend": "FLINT/Arb via python-flint, arb_zeta_nzeros (Platt/Turing) "
                   "and acb_dirichlet_zeta_zeros",
        "prec_bits": args.prec,
        "a": {"fraction": "%d/%d" % (a.numerator, a.denominator), "float": float(a)},
        "b": {"fraction": "%d/%d" % (b.numerator, b.denominator), "float": float(b)},
    }
    if args.target:
        T = dyadic(args.target)
        inside = a < T < b
        res["target"] = {"fraction": "%d/%d" % (T.numerator, T.denominator),
                         "float": float(T), "strictly_inside": bool(inside)}
        if not inside:
            raise SystemExit("target is not strictly inside (a,b)")

    t0 = time.time()
    Na_ball = as_arb(a).zeta_nzeros()
    Nb_ball = as_arb(b).zeta_nzeros()
    dt = time.time() - t0
    Na = unique_int(Na_ball, "N(a)")
    Nb = unique_int(Nb_ball, "N(b)")
    if Nb < Na:
        raise SystemExit("N decreased; impossible, refusing to continue")
    N_slab = Nb - Na

    res["N_a"] = {"ball": Na_ball.str(30, radius=True), "integer": Na}
    res["N_b"] = {"ball": Nb_ball.str(30, radius=True), "integer": Nb}
    res["N_total_in_slab"] = N_slab
    res["seconds_counting"] = dt
    print("N(a) = %d   N(b) = %d   ->  N(a,b) = %d   [%.1f s]"
          % (Na, Nb, N_slab, dt))

    if N_slab == 0:
        res["verdict"] = ("CERTIFIED_EMPTY_SLAB: the open slab contains no zero "
                          "of zeta of any kind -- on the critical line or off "
                          "it -- counted with multiplicity. Hence D = 0.")
        res["D"] = 0
        res["rh_consequence"] = "none: an empty slab is consistent with RH"
        print(res["verdict"])
    elif args.list_zeros:
        if N_slab > args.max_list:
            raise SystemExit("slab holds %d zeros; raise --max-list to enumerate"
                             % N_slab)
        t0 = time.time()
        zs = acb.zeta_zeros(Na + 1, N_slab)
        dt = time.time() - t0
        lo_a, hi_b = as_arb(a), as_arb(b)
        on_line, inside, ims = 0, 0, []
        for z in zs:
            if (z.real - arb(1) / 2).contains_zero() and z.real.is_exact():
                on_line += 1
            elif (z.real - arb(1) / 2).contains_zero():
                on_line += 1
            im = z.imag
            if (im - lo_a).lower() > 0 and (hi_b - im).lower() > 0:
                inside += 1
            ims.append(im)
        res["N0_line_zeros_returned"] = len(zs)
        res["N0_verified_inside_slab"] = inside
        res["N0_verified_on_critical_line"] = on_line
        res["seconds_listing"] = dt
        D = N_slab - inside
        res["D"] = D
        res["first_zero"] = ims[0].str(30, radius=True) if ims else None
        res["last_zero"] = ims[-1].str(30, radius=True) if ims else None
        if inside != len(zs):
            res["verdict"] = ("INCONCLUSIVE: %d of %d enumerated line zeros could "
                              "not be certified strictly inside the slab; widen "
                              "or move the endpoints" % (len(zs) - inside, len(zs)))
        elif D == 0:
            res["verdict"] = ("CERTIFIED_ALL_ON_LINE: D = 0, so every zero in the "
                              "slab lies on the critical line and is simple.")
            res["rh_consequence"] = "none: consistent with RH, and it certifies this slab"
        elif D > 0 and D % 2 == 0:
            res["verdict"] = ("CERTIFIED_OFF_CRITICAL_ZERO: D = %d > 0. RH IS "
                              "FALSE. This must be independently reproduced "
                              "before it is believed." % D)
            res["rh_consequence"] = "RH is false"
        else:
            res["verdict"] = ("REFUSING: D = %d is positive and odd, which "
                              "contradicts functional-equation symmetry; the "
                              "computation is inconsistent and must not be used"
                              % D)
        print(res["verdict"])
    else:
        res["D"] = None
        res["verdict"] = ("slab is non-empty (%d zeros); rerun with --list-zeros "
                          "to separate N_0 and compute D" % N_slab)
        print(res["verdict"])

    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("wrote", args.out)


if __name__ == "__main__":
    main()
