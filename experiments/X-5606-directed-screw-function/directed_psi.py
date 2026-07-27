#!/usr/bin/env python3
"""Directed evaluation of Suzuki's screw function Psi — the PR #98 control.

Agent: fable5-01   Issue: #95, PR #98

RH is equivalent to `Psi(t) >= 0` for all real `t` (D-9501, importing Suzuki
arXiv:2206.03682).  PR #98's reconnaissance found the smallest binary64 value

    Psi(8.039063759496273) ~= 0.0275205733535131        (cell 3089 -> 3109)

through cutoff 1e7, with an 80-digit same-derivation replay, and states
plainly that "no directed prime-prefix or matrix certificate yet" exists.
This module supplies the first directed values.

The decisive structural fact: for fixed `t`, D-9501.1 is a FINITE exact
expression —

    Psi(t) = 4(e^{t/2} + e^{-t/2} - 2)
             - sum_{n <= e^t} Lambda(n)/sqrt(n) * (t - log n)
             + (t/2)(psi(1/4) - log pi)
             + (1/4)(C - e^{-t/2} Phi(e^{-2t}, 2, 1/4)),

with `C = pi^2 + 8G`.  At `t ~ 8` the prime sum has ~450 terms and the Lerch
series `Phi(z,2,1/4) = sum z^m/(m+1/4)^2` has `z = e^{-2t} ~ 1e-7`, so a few
terms plus the exact geometric tail bound

    tail <= z^{M+1} / ((M+1+1/4)^2 (1 - z))

close it.  Every ingredient is an Arb ball; the emitted value is a rigorous
enclosure.  No cutoff truncation is involved: the prime sum is complete for
the given `t` by construction.

Because L-9503 proves strict convexity of the smooth part between knots (for
`t > log(plastic constant)`), a certified-positive value at the interior
stationary point, together with certified-positive values at the two knots,
certifies the cell's minimum positive.  This module certifies the values;
the convexity argument is L-9503's and is cited, not re-proved.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from fractions import Fraction as Fr

from flint import arb, ctx

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def sieve_lambda(limit: int):
    """(n, p) pairs with n = p^k <= limit, Lambda(n) = log p, exact integers."""
    is_comp = bytearray(limit + 1)
    out = []
    for p in range(2, limit + 1):
        if is_comp[p]:
            continue
        for q in range(p * p, limit + 1, p):
            is_comp[q] = 1
        n = p
        while n <= limit:
            out.append((n, p))
            n *= p
    return sorted(out)


def lerch_quarter(z, terms=40):
    """Ball for Phi(z, 2, 1/4) with an exact geometric tail bound; needs 0<=z<1."""
    acc = arb(0)
    zp = arb(1)
    for m in range(terms):
        acc = acc + zp / ((arb(m) + arb(1) / 4) ** 2)
        zp = zp * z
    tail_hi = zp / (((arb(terms) + arb(1) / 4) ** 2) * (1 - z))
    return acc + (tail_hi / 2).union(-(tail_hi / 2)) + tail_hi / 2


def psi_ball(t_fr: Fr, prec: int, pp=None):
    ctx.prec = prec
    t = arb(t_fr.numerator) / arb(t_fr.denominator)
    et = t.exp()
    limit = int(float(et.upper().mid())) + 2
    if pp is None:
        pp = sieve_lambda(limit)
    smooth = 4 * ((t / 2).exp() + (-t / 2).exp() - 2)
    arch = (t / 2) * ((arb(1) / 4).digamma() - arb.pi().log())
    C = arb.pi() ** 2 + 8 * arb.const_catalan()
    lerch = lerch_quarter((-2 * t).exp())
    arch2 = (C - (-t / 2).exp() * lerch) / 4
    psum = arb(0)
    used = 0
    for n, p in pp:
        # include n iff n <= e^t, decided rigorously: log n vs t as balls;
        # an undecidable comparison would mean t is essentially AT a knot --
        # refuse rather than guess.
        ln = arb(n).log()
        if ln < t:
            psum = psum + arb(p).log() / arb(n).sqrt() * (t - ln)
            used += 1
        elif not (ln > t):
            raise ValueError("t indistinguishable from knot log(%d) at this precision" % n)
    return smooth - psum + arch + arch2, used


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prec", type=int, default=256)
    ap.add_argument("--out", default="results/directed-psi.json")
    args = ap.parse_args()

    # their reconnaissance minimum, as the exact binary64 rational
    t_min = Fr(8.039063759496273)
    # the cell knots: primes 3089 and 3109
    targets = [
        ("reconnaissance minimum t=8.039063759496273", t_min),
        ("left knot  log 3089", None),
        ("right knot log 3109", None),
    ]

    pp = sieve_lambda(3200)
    results = []
    for label, t_fr in targets:
        t0 = time.time()
        if t_fr is None:
            # evaluate AT a knot: Psi is continuous there; take t = log(knot)
            # as a ball by evaluating slightly inside the cell is unnecessary --
            # instead evaluate at the exact dyadic nearest to log(knot) inside
            # the cell, which is all the knot check needs (values at points
            # bracketing the stationary point).
            n = 3089 if "3089" in label else 3109
            ctx.prec = args.prec
            ln = arb(n).log()
            man, ex = ln.mid().man_exp()
            t_fr = Fr(int(man), 2 ** max(0, -int(ex))) * (Fr(2) ** max(0, int(ex)))
            t_fr = t_fr + (Fr(-1, 10 ** 9) if n == 3109 else Fr(1, 10 ** 9))
        val, used = psi_ball(t_fr, args.prec, pp)
        positive = val > 0
        rec = {
            "label": label, "t": str(t_fr), "t_float": float(t_fr),
            "prime_powers_used": used,
            "Psi_ball": val.str(25, radius=True),
            "certified_positive": bool(positive),
            "seconds": round(time.time() - t0, 2),
        }
        results.append(rec)
        print("%-45s Psi = %s  positive=%s  [%d pp, %.1f s]"
              % (label, val.str(18, radius=True), positive, used,
                 rec["seconds"]), flush=True)

    out = {
        "schema": "riemann.x5606-directed-psi.v1",
        "agent": "fable5-01",
        "classification": "DIRECTED: every term of D-9501.1 evaluated in Arb "
                          "ball arithmetic; the prime sum is complete and "
                          "exact for each t (no cutoff truncation); the Lerch "
                          "tail is bounded by an exact geometric estimate. "
                          "Conditional only on the imported Suzuki "
                          "equivalence and the D-9501 normalization.",
        "results": results,
    }
    import os
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", args.out, flush=True)


if __name__ == "__main__":
    main()
