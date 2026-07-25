#!/usr/bin/env python3
"""Independent high-precision reference for the X-5601 carrier stream.

Agent: opus5-01   Issue: #55 / #28

This module recomputes the L-0801 lag coefficients

    z_d = sum_{q = p^a <= c} b_q exp(-i T log q) tau_d(K log q / log c)

from scratch with mpmath at a user-chosen decimal precision, using a naive
trial-division prime enumeration.  It shares no code, no algorithm and no
argument-reduction strategy with `carrier_stream.c`: logarithms, the huge
carrier phase and the trigonometric functions are all evaluated directly at
working precision.  It is deliberately slow and is only usable for small
cutoffs; its purpose is to be an independent oracle for the fast producer.
"""
from __future__ import annotations

import argparse
import json

from mpmath import mp, mpf, log, sqrt, sin, cos, floor


def prime_powers(cutoff: int):
    """Yield (q, p, a) for every prime power q = p^a <= cutoff, once each."""
    n = cutoff
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    for p in range(2, n + 1):
        if sieve[p]:
            q, a = p, 1
            while q <= n:
                yield q, p, a
                q *= p
                a += 1


def stream(cutoff: int, cells: int, carrier_num: int, carrier_den: int, dps: int):
    mp.dps = dps
    T = mpf(carrier_num) / mpf(carrier_den)
    logc = log(mpf(cutoff))
    zre = [mpf(0)] * cells
    zim = [mpf(0)] * cells
    wgt = [mpf(0)] * cells
    nprime = npower = 0
    for q, p, a in prime_powers(cutoff):
        if a == 1:
            nprime += 1
        else:
            npower += 1
        lq = log(mpf(q))
        b = log(mpf(p)) / (mp.pi * sqrt(mpf(q)))
        theta = T * lq
        cth, sth = cos(theta), sin(theta)
        r = cells * lq / logc
        d = int(floor(r))
        f = r - d
        for lag, w in ((d, (1 - f) * b), (d + 1, f * b)):
            if 0 <= lag < cells:
                zre[lag] += w * cth
                zim[lag] -= w * sth
                wgt[lag] += w
    return {
        "cutoff": cutoff,
        "cells": cells,
        "prime_count": nprime,
        "higher_prime_power_count": npower,
        "z_real": [mp.nstr(v, 40) for v in zre],
        "z_imag": [mp.nstr(v, 40) for v in zim],
        "weight": [mp.nstr(v, 40) for v in wgt],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cutoff-power10", type=int, default=5)
    ap.add_argument("--cells", type=int, default=16)
    ap.add_argument("--carrier-num", type=int, default=94184072727073)
    ap.add_argument("--carrier-den", type=int, default=20)
    ap.add_argument("--dps", type=int, default=60)
    ap.add_argument("--out", default="reference.json")
    args = ap.parse_args()
    res = stream(10 ** args.cutoff_power10, args.cells,
                 args.carrier_num, args.carrier_den, args.dps)
    res["dps"] = args.dps
    res["carrier_numerator"] = args.carrier_num
    res["carrier_denominator"] = args.carrier_den
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in
                      ("cutoff", "cells", "prime_count",
                       "higher_prime_power_count")}))


if __name__ == "__main__":
    main()
