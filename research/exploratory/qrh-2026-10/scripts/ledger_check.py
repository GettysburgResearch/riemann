#!/usr/bin/env python3
"""Exact-rational ledger for the explicit exponent arithmetic of the OpenAI QRH manuscript
("The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", 30 Sep 2026), Sections 10-20,
and of the Kintali short proof (47/48, 7 Oct 2026), Section 4.4.

Scope: this checks ONLY the stated rational arithmetic / polynomial identities that turn the
lemma outputs into margins. It does not check any lemma, sieve, moment or reflection argument.
Arithmetic class: EXACT_RATIONAL (fractions + sympy polynomial identities).
Run: python3 ledger_check.py   (requires sympy)
"""
from fractions import Fraction as Fr
import sympy as sp

checks = []
def check(name, cond):
    checks.append((name, bool(cond)))

# ---------------- Part I (Section 10.5, 11) ----------------
zeta = Fr(1, 1000)
check("Part I central margin 1/24 - (62/75) zeta = 1021/25000", Fr(1,24) - Fr(62,75)*zeta == Fr(1021,25000))
lxI = lyI = hI = Fr(1,2)
check("Part I principal w margin ly/20 = 1/40", lyI/20 == Fr(1,40))
check("Part I principal z margin h/600 = 1/1200", hI/600 == Fr(1,1200))
dminI = Fr(1,63)
small_I = hI*(Fr(17,50)-Fr(1,6)) - lyI/2
check("Part I small-row base exponent = -49/300", small_I == Fr(-49,300))
check("Part I small-row margin 49/300 - (63/50) dmin = 43/300", -small_I - Fr(63,50)*dminI == Fr(43,300))
check("Part I low exponent C_I(11/12) = 1/4", Fr(11,12) - Fr(2,3) == Fr(1,4))
# E_I(h) piecewise: R(delta) = min(1, 4/3 - delta, 1 - delta/2)
dl = sp.symbols('delta')
for lo, hi, R in [(0, Fr(1,3), 1), (Fr(1,3), Fr(2,3), sp.Rational(4,3)-dl), (Fr(2,3), 1, 1-dl/2)]:
    EI = sp.Rational(-3,4) + (dl + R)/2
    vals = [EI.subs(dl, sp.Rational(lo)), EI.subs(dl, sp.Rational(hi))]
    check(f"E_I(h) piece on [{lo},{hi}] <= -1/12 or = -(1-delta)/4", all(v <= sp.Rational(-1,12) for v in vals) or sp.simplify(EI + (1-dl)/4) == 0)
# third piece with delta <= 5/6 + 2 Delta1:  E_I(h) - Delta1 <= -1/24 - Delta1/2
D1 = sp.symbols('Delta1', nonnegative=True)
check("Part I third piece: -(1-delta)/4 - Delta1 at delta=5/6+2Delta1 equals -1/24 - Delta1/2",
      sp.simplify(-(1-(sp.Rational(5,6)+2*D1))/4 - D1 - (sp.Rational(-1,24) - D1/2)) == 0)
# frequency slope range [33/50, 62/75]
check("Part I slope max 149/150 - 1/6 = 62/75 (at delta=1/3)", Fr(149,150) - Fr(1,6) == Fr(62,75) and Fr(33,50) + Fr(1,6) == Fr(62,75))

# ---------------- Part II geometry (Sections 12, 15, 20) ----------------
b, h, ell = Fr(1,8), Fr(13,16), Fr(1,6)
lx = 1 + ell - h; ly = lx + b
check("lx = 17/48, ly = 23/48", lx == Fr(17,48) and ly == Fr(23,48))
check("M = lx+ly = 5/6 and M + ell = 1", lx+ly == Fr(5,6) and lx+ly+ell == 1)
check("C_II(s) = s - 11/16 i.e. lx/2 - 1 + h/6 = -11/16", lx/2 - 1 + h/6 == Fr(-11,16))
check("C_II(7/8) = 3/16 = lx/2 + b/12", Fr(7,8) - Fr(11,16) == Fr(3,16) == lx/2 + b/12)
check("Prop 15.3 length inequalities lx-ell>=3/16, ly-ell>=5/16, ly-ell-11b/6>=1/12",
      lx-ell >= Fr(3,16) and ly-ell >= Fr(5,16) and ly-ell-Fr(11,6)*b >= Fr(1,12))
check("Pa = Y'^2/Q exponent = b = 1/8", 2*ly - (lx+ly) == Fr(1,8))
C0 = Fr(-1,48)
check("C0 = (1-ly)/2 - 7/8 - h/6 - ell/2 + h = -1/48 (E(h) constant at R=1, delta=q=0)",
      (1-ly)/2 - Fr(7,8) - h/6 - ell/2 + h == C0)
check("delta-coefficient at d=h: (1-ly)/2 + h/2 - h = 2/3 - 13/16 = -7/48", (1-ly)/2 + h/2 - h == Fr(2,3) - h)
d0 = Fr(1,50)
check("(20.5) floor: C0 + 3 delta0/4 = -7/1200", C0 + Fr(3,4)*d0 == Fr(-7,1200))
check("(20.6) small rows h(17/50-1/6) - ly/2 = -79/800", h*(Fr(17,50)-Fr(1,6)) - ly/2 == Fr(-79,800))
check("msmall = 79/800 - 2/100 = 63/800", Fr(79,800) - 2*Fr(1,100) == Fr(63,800))
check("(20.3) mw = ly/20 = 23/960, mz = h/600 = 13/9600", ly/20 == Fr(23,960) and h/600 == Fr(13,9600))
check("(20.7) delta=alpha: C0 + (3/4 - h) delta = -1/48 - delta/16", Fr(3,4) - h == Fr(-1,16))
check("large rows B0 = lx/2 + 1 + ly = 53/32", lx/2 + 1 + ly == Fr(53,32))
check("supply l/h = 8/39 > 1/5 > 7/37, 8/39-7/37 = 23/1443", ell/h == Fr(8,39) and Fr(8,39) > Fr(1,5) > Fr(7,37) and Fr(8,39)-Fr(7,37) == Fr(23,1443))
check("extension zeta < 5 ell - h = 1/48", 5*ell - h == Fr(1,48))
check("1/5 - 7/37 = 2/185", Fr(1,5) - Fr(7,37) == Fr(2,185))
check("frequency slope lower bound 33/50 - 5/12 >= 4/25 (delta<=5/6)", Fr(33,50) - Fr(5,12) >= Fr(4,25))
check("R* + Delta/4 <= 17/12 + 1/96 = 137/96 <= 139/96 (stated)", Fr(17,12) + Fr(1,96) <= Fr(139,96))
check("139/96 + 1/2 - 17/50 < 2", Fr(139,96) + Fr(1,2) - Fr(17,50) < 2)

# (20.11): d = 1/2, R = 76/75 - 2 delta/3, q = delta/2
dd = sp.symbols('delta')
R = sp.Rational(76,75) - 2*dd/3; q = dd/2
E = sp.Rational(-1,48) + 2*dd/3 + q/6 - sp.Rational(13,16)*(1-R) + (sp.Rational(1,2)-sp.Rational(13,16))*(R + dd/2 - sp.Rational(17,50))
check("(20.11) E(1/2) = -529/2400 + 25 delta/96", sp.simplify(E - (sp.Rational(-529,2400) + 25*dd/96)) == 0)
check("(20.11) at delta=5/6: -49/14400", sp.Rational(-529,2400) + sp.Rational(25,96)*sp.Rational(5,6) == sp.Rational(-49,14400))
check("R=76/75-2delta/3 equals 1 at delta=1/50", sp.Rational(76,75) - sp.Rational(2,3)*sp.Rational(1,50) == 1)

# Section 19 constants
x = sp.symbols('x')
Dx = 3 - 17*x/9; Px = (2 - 8*x/9)*(1 - x)
check("Dx in [37/18,3] on [0,1/2]", Dx.subs(x, sp.Rational(1,2)) == sp.Rational(37,18) and Dx.subs(x,0) == 3)
check("Px in [7/9,2] endpoints", Px.subs(x, sp.Rational(1,2)) == sp.Rational(7,9) and Px.subs(x,0) == 2)
check("Px decreasing on [0,1/2]", all(sp.diff(Px,x).subs(x, sp.Rational(k,20)) < 0 for k in range(11)))
check("Dx - Px = 1 + x - 8x^2/9", sp.expand(Dx - Px - (1 + x - 8*x**2/9)) == 0)
t = sp.symbols('t')
rstar = ((2 - 8*x/9)*t - 5*x/9)/Dx
check("r*(3/2) = 1", sp.simplify(rstar.subs(t, sp.Rational(3,2)) - 1) == 0)
check("r*(1) at x=1/2 = 23/37 (its minimum over x)", rstar.subs({t:1, x:sp.Rational(1,2)}) == sp.Rational(23,37)
      and all(sp.diff(rstar.subs(t,1),x).subs(x, sp.Rational(k,20)) < 0 for k in range(11)))
check("t - r*(t) = ((1-x)t + 5x/9)/Dx", sp.simplify(t - rstar - ((1-x)*t + 5*x/9)/Dx) == 0)
check("inverse capacity max (1-23/37)/2 = 7/37; plain capacity max 2/27", (1-Fr(23,37))/2 == Fr(7,37) and Fr(2,9)*(1-Fr(2,3)) == Fr(2,27))
# Rshort weighted average identity (19.7)
dlt, r = sp.symbols('delta r')
AI = 1 - dlt*(x + (1-x)*r)
St = 1 - dlt*(4*x/9 + (2 - 8*x/9)*(t - r))
Rs = ((2 - 8*x/9)*AI + (1-x)*St)/Dx
check("(19.7) weighted average independent of r and = 1 - delta + delta Px (3/2 - t)/Dx",
      sp.simplify(sp.diff(Rs, r)) == 0 and sp.simplify(Rs - (1 - dlt + dlt*Px*(sp.Rational(3,2)-t)/Dx)) == 0)
# (19.6) capacity replacement bound
Dl = sp.symbols('Delta', positive=True)
check("(19.6) 2/9 - 1/(9/2+12Delta) = 12 Delta /((9/2)(9/2+12 Delta))",
      sp.simplify(sp.Rational(2,9) - 1/(sp.Rational(9,2)+12*Dl) - 12*Dl/(sp.Rational(9,2)*(sp.Rational(9,2)+12*Dl))) == 0)

# Lemma 20.2 identity (20.9) and bound
d_, y = sp.symbols('delta y', nonnegative=True)
xx = sp.Rational(1,2) - y
alpha = sp.Rational(5,6)
Dxy = 3 - 17*xx/9; Pxy = (2 - 8*xx/9)*(1 - xx); J = (alpha - d_)*Dxy + d_*Pxy
Rst = 1 - d_ + (alpha - d_)*d_*Pxy/(2*J)
Estar = C0 + sp.Rational(2,3)*d_ + xx*d_/6 - sp.Rational(13,16)*(1 - Rst)
v = 51 + 41*y
lhs = sp.together(10368*v*J*(-Estar))
rhs = (3+5*y)*((4*v*d_-79)**2 + 49) + 4*y*(4*v*d_*((1+3*y)*(15+32*y)*d_ + 9 - 13*y) + 265 + 3485*y)
check("(20.9) identity 10368 v J (-E*) = (3+5y)((4v delta-79)^2+49) + 4y(...)", sp.simplify(lhs - rhs) == 0)
check("Lemma 20.2: v <= 17(3+5y) on y in [0,1/2]", sp.simplify(17*(3+5*y) - v - 44*y) == 0)
check("Lemma 20.2: 49/(176256 * 5/2) = 49/440640 > 1/10000", Fr(49, 176256)*Fr(2,5) == Fr(49,440640) and Fr(49,440640) > Fr(1,10000))
check("10368*17 = 176256", 10368*17 == 176256)
check("(20.10) 1 - h/4 = 51/64", 1 - h/4 == Fr(51,64))

# ---------------- Kintali 47/48 (Section 4.4) ----------------
check("Kintali: 29/30 + 1/80 = 47/48", Fr(29,30) + Fr(1,80) == Fr(47,48))
check("Kintali: max_a (a + R(a)/2 - 1/3) with R=min(1,5(1-a)) is 29/30 at a=4/5",
      Fr(4,5) + Fr(1,2) - Fr(1,3) == Fr(29,30) and Fr(13,6) - Fr(3,2)*Fr(4,5) == Fr(29,30))
check("Kintali: max of h(sigma)=min(3/(2-sigma),2/sigma) is 5/2 at sigma=4/5", Fr(3)/(2-Fr(4,5)) == Fr(5,2) == 2/Fr(4,5))
check("Kintali: C(11/12) = 1/4 so low estimate Z^(1/4) matches 11/12", Fr(11,12) - Fr(2,3) == Fr(1,4))

ok = sum(c for _, c in checks)
for name, c in checks:
    print(("PASS " if c else "FAIL ") + name)
print(f"\n{ok}/{len(checks)} checks passed")
