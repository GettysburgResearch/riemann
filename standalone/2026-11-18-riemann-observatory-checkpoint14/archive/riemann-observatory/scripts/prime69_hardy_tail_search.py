#!/usr/bin/env python3
"""Numerical parameter search. Each proposal is rounded before evaluation."""
import argparse
import json
from fractions import Fraction
from math import ceil, log

from flint import ctx
from scipy.optimize import minimize

from prime69_parameterized_hardy_tail_checks import Parameters, calculate


def proposal(x):
    r, d, w, a1, a2 = x
    return Parameters(Fraction(round(r*1000), 1000), Fraction(round(d*1000), 1000),
                      Fraction(round(w)), (Fraction(round(a1*1000), 1000),
                                            Fraction(round(a2*1000), 1000)))


def search(height, max_calls):
    ctx.prec = 96
    attempts = {}
    best = (float("inf"), None)

    def objective(x):
        nonlocal best
        p = proposal(x)
        if p in attempts:
            return attempts[p][1]
        n = max(8, ceil(log(3e6)/log(float(p.ratio))))
        try:
            value = float(calculate(height, n, p)[0].upper())
        except (AssertionError, ZeroDivisionError) as error:
            attempts[p] = (n, 10.0, str(error) or type(error).__name__)
            return 10.0
        attempts[p] = (n, value, "")
        if value < best[0]:
            best = value, p
        return value

    for bad in ((1.9, .24, 160, .16, .32), (1.12, .4, 1400, .16, .32),
                (1.8, .4, 160, .16, .5)):
        objective(bad)
    fits = [minimize(objective, initial, method="Powell", bounds=bounds,
                     options={"maxfev": max_calls, "xtol": 1e-4, "ftol": 1e-7})
            for initial, bounds in (
                ((1.8, .38, 170, .17, .34),
                 [(1.15, 2.6), (.22, .59), (20, 450), (.1, .3), (.24, .49)]),
                ((1.607, .286, 57, .219, .433),
                 [(1.35, 1.9), (.245, .36), (20, 110), (.18, .25), (.39, .48)]))]
    return {"height": height, "calls": len(attempts), "status": [fit.message for fit in fits],
            "best": repr(best[1]),
            "attempts": [{"parameters": repr(p), "blocks": n, "upper_diagnostic": value,
                          "failure": failure}
                         for p, (n, value, failure) in attempts.items()]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=10000)
    parser.add_argument("--max-calls", type=int, default=400)
    args = parser.parse_args()
    print(json.dumps(search(args.height, args.max_calls), indent=2))
