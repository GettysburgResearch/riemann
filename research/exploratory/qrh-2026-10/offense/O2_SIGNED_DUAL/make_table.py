#!/usr/bin/env python3
"""Markdown table + least-squares exponent fits from signed_dual_numerics.py output (EMPIRICAL, finite).

Usage: python3 -I make_table.py results/signed_dual_main.json [more.json ...]
"""
import json
import math
import sys

rows = []
for p in sys.argv[1:]:
    rows += json.load(open(p))
rows.sort(key=lambda r: (r["rho"], r["D"]))
print("| D | ρ | H | 𝓜_D | Z | S = 𝓜_D − Z | Off/Diag | P (proxy) | Prin | \\|A₁(D)\\| | e = log(P/\\|S\\|)/log D | 1 − ρ | (1 − ρ)/6 |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    print("| %d | %.2f | %.0f | %.3f | %.3f | %.4f | %.2e | %.0f | %.3f | %.1f | %.3f | %.2f | %.3f |" % (
        r["D"], r["rho"], r["H"], r["M"], r["Z"], r["S"], r["offdiag_rel"], r["P"], r["Prin"], r["A1"],
        r["saving_exp"], 1 - r["rho"], (1 - r["rho"]) / 6))


def fit(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    res = [y - my - b * (x - mx) for x, y in zip(xs, ys)]
    se = math.sqrt(sum(e * e for e in res) / max(n - 2, 1) / sxx)
    return b, se


print()
print("| ρ | fitted exponent of \\|S\\| in D (± s.e.) | of P | of H | fitted e(D) = log(P/\\|S\\|)/log D, mean |")
print("|---|---|---|---|---|")
for rho in sorted({r["rho"] for r in rows}):
    rr = [r for r in rows if r["rho"] == rho and r["D"] >= 2000]
    xs = [math.log(r["D"]) for r in rr]
    bS, sS = fit(xs, [math.log(abs(r["S"])) for r in rr])
    bP, sP = fit(xs, [math.log(r["P"]) for r in rr])
    em = sum(r["saving_exp"] for r in rr) / len(rr)
    print("| %.2f | %.2f ± %.2f | %.3f ± %.3f | %.2f | %.2f |" % (rho, bS, sS, bP, sP, rho, em))
