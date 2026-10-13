#!/usr/bin/env python3
"""O7: closed forms for the Gram-zero barriers (sympy, exact).  PROPOSED; checked against the LP values
of floor_rows_scan.py.  Active sets were read off the LP solutions (geometry ly = 2 lx at the kink of
the kept Gram branch max(0, 2b - ly), b = ly - lx)."""
import sympy as sp
lx, ly, l, s, d, t = sp.symbols('lx ly ell s delta0 theta', real=True)
h = 1 - lx + l
L1 = sp.Rational(5, 6) + (lx - l)/6                                   # E = M, gram 0
L2 = sp.Rational(23, 24) - lx/12 - ly/4 + sp.Rational(5, 24)*l        # E = (2M+1+3ell)/4
L3 = sp.Rational(1, 3) + 2*lx/3 + ly/2 + l/3                          # E = 2M+ell-1
def binF(a, R):
    dl = 2*a - 1
    return a*(1 - ly) + h*(R + dl/2 - sp.Rational(1, 6)) - l/2 + dl*l/2
# (1) raised floor with kappa = 1: floor a0 = (1+d)/2, R = 1 - d
fl = binF((1 + d)/2, 1 - d)
sol = sp.solve([sp.Eq(s, L1), sp.Eq(s, L3), sp.Eq(ly, 2*lx), sp.Eq(s, fl)], [lx, ly, l, s], dict=True)
for so in sol:
    print("raised floor, kappa=1, active {L1,L3,kink,floor}: sigma0(delta0) =", sp.simplify(so[s]),
          " geometry", [sp.simplify(so[v]) for v in (lx, ly, l)])
    for dv in (0, sp.Rational(1, 50), sp.Rational(1, 10), sp.Rational(1, 6), sp.Rational(1, 4), sp.Rational(1, 3), sp.Rational(1, 2)):
        print("   delta0 =", dv, "->", sp.nsimplify(so[s].subs(d, dv)), " L2 slack:", sp.nsimplify((so[s] - L2.subs(so)).subs(d, dv)))
# (2) floor at 1/2 with near-critical saving theta in every bin (limit bin delta -> 0+, R = 1 - theta)
fl2 = binF(sp.Rational(1, 2), 1 - t)
sol2 = sp.solve([sp.Eq(s, L1), sp.Eq(s, L3), sp.Eq(ly, 2*lx), sp.Eq(s, fl2)], [lx, ly, l, s], dict=True)
for so in sol2:
    print("a0 -> 1/2, NC(theta): sigma0(theta) =", sp.factor(sp.simplify(so[s])), [sp.simplify(so[v]) for v in (lx, ly, l)])
# (3) floor at 51/100 with floor saving theta (0 <= theta <= 1/50), any counting above
fl3 = binF(sp.Rational(51, 100), 1 - t)
sol3 = sp.solve([sp.Eq(s, L1), sp.Eq(s, L3), sp.Eq(ly, 2*lx), sp.Eq(s, fl3)], [lx, ly, l, s], dict=True)
for so in sol3:
    print("a0 = 51/100, floor saving theta: sigma0(theta) =", sp.factor(sp.simplify(so[s])))
# (4) general kappa: floor a0=(1+d)/2, R = 1 - kappa d
k = sp.symbols('kappa', real=True)
fl4 = binF((1 + d)/2, 1 - k*d)
sol4 = sp.solve([sp.Eq(s, L1), sp.Eq(s, L3), sp.Eq(ly, 2*lx), sp.Eq(s, fl4)], [lx, ly, l, s], dict=True)
for so in sol4:
    ss = sp.simplify(so[s])
    print("general kappa: sigma0 =", sp.factor(ss), "; d sigma0/d delta0 at 0 =", sp.simplify(sp.diff(ss, d).subs(d, 0)))
