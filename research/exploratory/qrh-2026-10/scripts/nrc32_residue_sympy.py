#!/usr/bin/env python3
"""NRC32 twists: symbolic regression for the Perron/Mellin separation (option O1).

Status: EXPLORATORY. Uses sympy series algebra only. It checks the residue
bookkeeping in NRC32_TWISTS.md section 3 (Proposition P3); it does NOT check the
Perron formula itself (classical) or any estimate.

Checks
  (R1) principal: Res_{w=0} zeta(1+w) D(1+w)^2 W_I(w) with
       W_I(w) = ((a+h)^(1+w) - a^(1+w)) / (w(1+w)),
       zeta(1+w) = 1/w + gamma + g1 w + ..., D(1+w) = m + D1 w + D2 w^2 + ...
       equals m^2 [(a+h)log(a+h) - a log a - h + gamma h] + 2 h m D1.
  (R2) nonprincipal: with L(1+w,chi) = lam + l1 w + ..., the residue is h lam m^2,
       and 2m - lam m^2 - 1/lam = -lam (m - 1/lam)^2 (exact Newton square).
  (R3) Perron kernel residues: Res_{w=0} + Res_{w=-1} of x^(w+1) n^(-w)/(w(w+1))
       equals x - n.
"""
import sympy as sp

w, a, h, m, D1, D2, g, g1, lam, l1, x, n = sp.symbols(
    "w a h m D1 D2 gamma g1 lam l1 x n", positive=True)

zeta1 = 1 / w + g + g1 * w
D = m + D1 * w + D2 * w**2
W = ((a + h) ** (1 + w) - a ** (1 + w)) / (w * (1 + w))
expr = sp.series(zeta1 * D**2 * W, w, 0, 1).removeO()
res = sp.simplify(sp.expand(expr).coeff(w, -1))
target = m**2 * ((a + h) * sp.log(a + h) - a * sp.log(a) - h + g * h) + 2 * h * m * D1
assert sp.simplify(sp.expand_log(res - target, force=True)) == 0, (res, target)

Lc = lam + l1 * w
expr2 = sp.series(Lc * D**2 * W, w, 0, 1).removeO()
res2 = sp.simplify(sp.expand(expr2).coeff(w, -1))
assert sp.simplify(res2 - h * lam * m**2) == 0, res2
assert sp.simplify(2 * m - lam * m**2 - 1 / lam + lam * (m - 1 / lam) ** 2) == 0

k = x ** (w + 1) * n ** (-w) / (w * (w + 1))
r0 = sp.residue(k, w, 0)
r1 = sp.residue(k, w, -1)
assert sp.simplify(r0 + r1 - (x - n)) == 0, (r0, r1)

print("PASS R1 R2 R3")
