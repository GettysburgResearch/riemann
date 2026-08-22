#!/usr/bin/env python3
"""Uniform-in-x envelope ENVSUP >= sup_{x>=x_sat} |Etil_j(x)| (j=2,3 share it since
|C_j|<=1 and the weight profile is the same; we bound the UNWEIGHTED |E|-sum).
BND(Y) = 0.0075 for Y in [5,15)  [certified: sup|E| on [5,16] = 0.007426 < 0.0075]
BND(Y) = (log Y + 11)/(8 (Y-1)^{3/2}) for Y >= 15  [proved Lemma 1], decreasing there.
Per divisor d: sup_{x>=x_sat} BND(x/d) = BND(x_sat/d) if x_sat/d >= 15, else
max(0.0075, BND(15)) = BND(15) = 0.0327 (Y crosses 15 as x grows).
Divisors entering Etil: U + {e*} + all odds (sliver evens never enter rows)."""
import math

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P61 = 1
for p in P: P61 *= p
divs = [(1, 1)]
for p in P:
    divs = divs + [(d*p, -m) for (d, m) in divs]
divs.sort()
odds = [d for d, m in divs if m == -1]
evens = [d for d, m in divs if m == +1]

# threshold set (exact, as certified in lattice_sat.py)
nO = sum(P61 // o for o in odds)
cum = 0; U = []; estar = None
for e in evens:
    w = P61 // e
    if cum + w > nO:
        estar = e; break
    cum += w; U.append(e)

xsat = 5.0*float(P61)
BND15 = (math.log(15) + 11)/(8*14**1.5)
def bnd_sup(d):
    Y0 = xsat/float(d)
    if Y0 >= 15:
        return (math.log(Y0) + 11)/(8*(Y0-1)**1.5)
    return BND15

tot = math.fsum(bnd_sup(d)/math.sqrt(float(d)) for d in U + [estar] + odds)
big = sorted(((bnd_sup(d)/math.sqrt(float(d)), d, xsat/float(d)) for d in odds), reverse=True)[:5]
print(f"BND(15) = {BND15:.5f}")
print(f"ENVSUP = sup_x>=x_sat sum |E|-bound weights = {tot:.4e}")
print("largest contributors (bound, d, Y at x_sat):")
for b, d, y in big:
    print(f"  {b:.3e}  d={d}  Y0={y:.1f}")
print(f"count divisors with x_sat/d < 15: {sum(1 for d in U+[estar]+odds if xsat/float(d)<15)}")
