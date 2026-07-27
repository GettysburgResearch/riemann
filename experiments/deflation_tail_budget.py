#!/usr/bin/env python3
"""X-9506: deflation feasibility as a function of the zero-side weight decay.

Every "zero-deflation" route in this repository has the same shape.  Some
RH-equivalent quantity Q admits, under RH, a nonnegative zero expansion

    Q = sum_gamma w(gamma),        w(gamma) >= 0,

with Q computable from arithmetic data and w computable per zero.  Certifying
the zeros with |gamma| <= T gives the RH-consequence

    sum_{|gamma| <= T} w(gamma)  <=  Q,

and the route hunts for a violation.  The slack that a violation must overcome
is exactly the uncertified tail, so the figure of merit is the

    tail fraction   F(T) = sum_{|gamma| > T} w(gamma) / sum_gamma w(gamma),

and the route can only close if F(T) is driven below the combined relative
width of the directed enclosures on the two sides.

F(T) is decided by how fast w decays.  This script computes the certification
height T that each weight class would require, and hence ranks the routes.

Zero density: dN = (1/2 pi) log(gamma / 2 pi) d gamma (Riemann-von Mangoldt).
Low zeros are summed exactly from the X-9503 ordinate list; the tail is
integrated against the density.  Both signs of gamma are counted.

Standard library only.  This is a scaling/feasibility calculator, not a
certificate: the density is used heuristically, not as a proved tail bound.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

TWO_PI = 2.0 * math.pi


def density(g):
    return math.log(g / TWO_PI) / TWO_PI


def tail_integral(w, T, upper=1e18, panels=200000):
    """2 * int_T^upper w(g) density(g) dg, on a log grid."""
    if T >= upper:
        return 0.0
    a, b = math.log(T), math.log(upper)
    tot = 0.0
    prev = None
    for i in range(panels + 1):
        x = a + (b - a) * i / panels
        g = math.exp(x)
        f = w(g) * density(g) * g          # dg = g dx
        if prev is not None:
            tot += 0.5 * (prev + f) * (b - a) / panels
        prev = f
    return 2.0 * tot


def total_mass(w, zs, split=None):
    """2 * sum over known low ordinates + integrated tail above them."""
    split = split or zs[-1]
    low = 2.0 * sum(w(g) for g in zs if g <= split)
    return low + tail_integral(w, split)


def required_T(w, zs, target, lo=20.0, hi=1e17):
    tot = total_mass(w, zs)
    if tot <= 0.0:
        return None, None
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if tail_integral(w, mid) / tot > target:
            lo = mid
        else:
            hi = mid
    T = math.sqrt(lo * hi)
    nz = (T / TWO_PI) * (math.log(T / TWO_PI) - 1.0)
    return T, nz


def sinc_pow(a, k):
    """|f-hat|^2 for a B-spline / Fejer-power test function: decays like g^-2k."""
    def w(g):
        x = a * g
        if abs(x) < 1e-12:
            return 1.0
        return (math.sin(x) / x) ** (2 * k)
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zeros", required=True)
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--target", type=float, default=1e-12,
                    help="relative deficit a directed certificate must beat")
    args = ap.parse_args()

    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    zs = json.load(open(args.zeros))["zeros"]

    classes = [
        ("1/gamma^2   (screw Psi; xi'/xi Pick at a fixed point)",
         lambda g: 1.0 / g ** 2, "heavy"),
        ("1/gamma^4   (a hypothetical second-order kernel)",
         lambda g: 1.0 / g ** 4, "moderate"),
        ("1/gamma^6",
         lambda g: 1.0 / g ** 6, "moderate"),
        ("Weil, C^0 test fn  (sinc^2,  support ~2)", sinc_pow(1.0, 1), "heavy"),
        ("Weil, C^2 test fn  (sinc^4,  support ~2)", sinc_pow(0.5, 2), "moderate"),
        ("Weil, C^6 test fn  (sinc^8,  support ~2)", sinc_pow(0.25, 4), "light"),
        ("Weil, C^10 test fn (sinc^12, support ~2)", sinc_pow(1.0 / 6, 6), "light"),
        ("Gaussian test fn   exp(-gamma^2/200)",
         lambda g: math.exp(-g * g / 200.0), "light"),
    ]

    print("=" * 78)
    print("X-9506  deflation feasibility vs. zero-side weight decay")
    print("=" * 78)
    print(f"target relative deficit a directed certificate must beat: "
          f"{args.target:.0e}")
    print(f"low ordinates available for the exact part: {len(zs)} "
          f"(up to {zs[-1]:.1f})\n")
    print(f"{'zero-side weight w(gamma)':<52} {'F(1000)':>10} "
          f"{'required T':>12} {'certified zeros':>16}")
    print("-" * 94)

    rows = []
    for name, w, band in classes:
        tot = total_mass(w, zs)
        F1000 = tail_integral(w, 1000.0) / tot
        T, nz = required_T(w, zs, args.target)
        rows.append({"weight": name, "band": band, "F_at_1000": F1000,
                     "required_T": T, "certified_zeros": nz})
        tstr = f"{T:.3e}" if T is not None else "n/a"
        nstr = f"{nz:.3e}" if nz is not None else "n/a"
        print(f"{name:<52} {F1000:>10.3e} {tstr:>12} {nstr:>16}")

    print("\nReading:")
    print("  heavy   tail fraction falls like log(T)/T  -> certification is")
    print("          the binding constraint, and it is astronomical.")
    print("  light   tail fraction collapses by T of order 10^2-10^3, so the")
    print("          zero count is trivial and the binding constraint moves to")
    print("          the PRECISION of the arithmetic side.")
    print("\nThe screw route sits in the heavy band by construction: Krein's")
    print("screw normalization fixes the weight at exactly 1/gamma^2, the")
    print("slowest decay for which the expansion still converges.  A Weil")
    print("carrier route chooses its weight, so its band is a design decision.")

    out = {"experiment": "X-9506", "agent": "claude-09",
           "script_sha256": digest,
           "environment": {"python": platform.python_version(),
                           "platform": platform.platform(),
                           "third_party_libraries": "none (standard library only)",
                           "arithmetic": "IEEE binary64"},
           "status": "EMPIRICAL - heuristic scaling calculator, not a certificate",
           "target_deficit": args.target, "rows": rows}
    if args.json_out:
        p = Path(args.json_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=1, sort_keys=True))
        print(f"\nwrote {args.json_out}")


if __name__ == "__main__":
    main()
