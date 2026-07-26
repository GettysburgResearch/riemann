#!/usr/bin/env python3
"""Independent audit of the zero counter, by the argument principle.

Agent: opus5-01   Issue: #55

Every certificate in `X-5604` rests on `arb_zeta_nzeros` for the total count
`N`.  That is a single external code path, and `O-5608` flagged it as the one
assumption the results cannot escape.  This module checks it against a
genuinely different computation.

`xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)` is entire and its zeros are
exactly the nontrivial zeros of `zeta`, so for a rectangle `R` whose boundary
misses every zero,

    #\{rho in R\}  =  (1/2 pi i) * contour-integral over dR of (xi'/xi)(s) ds,

counted with multiplicity.  With `R = [-1, 2] x [y0, y1]`, which contains the
whole critical strip, this counts exactly the zeros with `y0 < Im rho < y1`.

The integrand is assembled from
`xi'/xi = 1/s + 1/(s-1) - (1/2) log pi + (1/2) psi(s/2) + zeta'/zeta`, with
`zeta` and `zeta'` taken from an `acb_series` jet.  The integration uses Arb's
rigorous adaptive integrator, so the result is a **ball**, and the audit passes
only when that ball isolates a single integer and that integer agrees with
`zeta_nzeros`.

The two routes share Arb's `zeta` implementation but nothing else: one is
Platt's grid plus Turing's method on the real line, the other is complex
contour integration of a logarithmic derivative.  Agreement is meaningful;
disagreement would be decisive.
"""
from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction as Fr

from flint import acb, acb_series, arb, ctx


def xi_log_deriv(s, _analytic=False):
    """xi'/xi(s), assembled from a zeta jet."""
    jet = acb_series([s, 1]).zeta()
    z, zp = jet[0], jet[1]
    return (1 / s + 1 / (s - 1) - acb(arb.pi().log()) / 2
            + (s / 2).digamma() / 2 + zp / z)


def count_in_rectangle(x0, x1, y0, y1, prec, rel_tol=None, verbose=False):
    """(1/2 pi i) * closed contour integral of xi'/xi around [x0,x1] x [y0,y1]."""
    ctx.prec = prec
    c = [acb(x0, y0), acb(x1, y0), acb(x1, y1), acb(x0, y1)]
    total = acb(0)
    kw = {}
    if rel_tol is not None:
        kw["rel_tol"] = rel_tol
    for i in range(4):
        a, b = c[i], c[(i + 1) % 4]
        t0 = time.time()
        seg = acb.integral(lambda s, an: xi_log_deriv(s), a, b, **kw)
        total += seg
        if verbose:
            print("   side %d  %s -> %s   [%.0f s]"
                  % (i, a.str(6, radius=False), b.str(6, radius=False),
                     time.time() - t0), flush=True)
    return total / (acb(0, 1) * 2 * arb.pi())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--y0", default="1/2")
    ap.add_argument("--y1", required=True)
    ap.add_argument("--x0", type=int, default=-1)
    ap.add_argument("--x1", type=int, default=2)
    ap.add_argument("--prec", type=int, default=128)
    ap.add_argument("--rel-tol", type=float, default=None)
    ap.add_argument("--out", default="argument-principle.json")
    args = ap.parse_args()

    y0, y1 = Fr(args.y0), Fr(args.y1)
    ctx.prec = args.prec
    a0 = arb(y0.numerator) / arb(y0.denominator)
    a1 = arb(y1.numerator) / arb(y1.denominator)

    print("rectangle [%d, %d] x [%s, %s]  prec=%d"
          % (args.x0, args.x1, float(y0), float(y1), args.prec), flush=True)

    t0 = time.time()
    val = count_in_rectangle(args.x0, args.x1, a0, a1, args.prec,
                             args.rel_tol, verbose=True)
    dt = time.time() - t0
    print("contour value = %s   [%.0f s]" % (val.str(20, radius=True), dt), flush=True)

    n_contour = val.real.unique_fmpz()
    imag_ok = val.imag.contains(arb(0))

    t1 = time.time()
    N1 = a1.zeta_nzeros().unique_fmpz()
    N0 = a0.zeta_nzeros().unique_fmpz()
    n_nzeros = None if (N1 is None or N0 is None) else int(N1) - int(N0)
    print("zeta_nzeros   = %s   [%.0f s]" % (n_nzeros, time.time() - t1), flush=True)

    agree = (n_contour is not None and n_nzeros is not None
             and int(n_contour) == n_nzeros)
    res = {
        "schema": "riemann.x5604-argument-principle.v1",
        "agent": "opus5-01",
        "classification": "RIGOROUS on both sides: the contour value is an Arb "
                          "ball from the adaptive integrator, the reference is "
                          "an Arb ball from zeta_nzeros. The audit passes only "
                          "when both isolate the same integer.",
        "rectangle": {"x0": args.x0, "x1": args.x1,
                      "y0": str(y0), "y1": str(y1)},
        "prec_bits": args.prec,
        "contour_value": val.str(25, radius=True),
        "contour_imag_contains_zero": bool(imag_ok),
        "contour_integer": None if n_contour is None else int(n_contour),
        "zeta_nzeros_integer": n_nzeros,
        "agree": bool(agree),
        "seconds_contour": dt,
        "verdict": ("AUDIT PASSED: two independent Arb code paths -- contour "
                    "integration of xi'/xi, and Platt/Turing counting on the "
                    "real line -- return the same integer."
                    if agree else
                    "AUDIT INCONCLUSIVE OR FAILED: see the values."),
    }
    print(res["verdict"], flush=True)
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
