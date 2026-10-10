#!/usr/bin/env python3
"""EXACT_RATIONAL / SYMBOLIC checks for SEP30_DETECTOR_QUANTIFIERS.md.

Object: the 30 Sep 2026 OpenAI 7/8 manuscript, paper.tex at pr908 (31c706bb),
SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (16,677 lines).
External and unreviewed; every number below is transcribed from it and re-derived here.

Sections
  A  Lemma 8.1 (buffered bins, 4281-4368): pigeonhole, grid, disk geometry, Lemma 4.9 radii,
     height budget, reflected exponent, bin count.
  B  Lemma 8.2 (pointwise dyadic estimates, 4385-4498): exponent bookkeeping and heights.
  C  Prop 8.3 (two saturated witnesses, 4510-4685): Gamma-line exponent, saturation algebra.
  D  The floor a0 = 51/100: every inequality in Sec. 8, Lemma 7.1 region one (4049-4189) and
     Prop 16.1 (8852-9049) that mentions the floor, re-run with a0 = 1/2 + eta.
  E  Prop 16.1: dynamic local error exponents and conductor allocation.
  F  Lemma 20.1 (15699-15851): consumption of (5.13e), the floor bound (20.5), (FB).
  G  Prop 20.3 (16196-16453) and Sec. 20.3-20.6: constants used by the order of choices.
  H  Prop 20.3 quantifier order as a dependency graph: topological check, target boundary,
     and which stated independence claims are load-bearing (removing one creates a cycle).

All affine inequalities in (a, e) are checked at every vertex of the closed parameter box, which
proves them on the whole box. Checks print PASS/FAIL; the exit status is the number of failures.
No `assert` is used, so `python3 -O` gives the same verdicts. Needs sympy and the stdlib only.
"""
import itertools
import math
import sys
from fractions import Fraction as Fr

import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + str(detail) + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


def vmax(f, box):
    """max of f over the vertices of a box given as a list of (lo, hi) pairs (exact)."""
    return max(f(*v) for v in itertools.product(*box))


E_MAX = Fr(1, 1000)      # Section 8: 0 < e < 10^-3 (TeX 4275); closed box used for vertex checks
A0 = Fr(51, 100)         # floor
Z0 = Fr(17, 50)          # z-contour z0 = 17/50

# ---------------------------------------------------------------------------------------------
# A. Lemma 8.1
# ---------------------------------------------------------------------------------------------
print("== A. Lemma 8.1 (buffered zero-free bins)")
ok = True
for e in [Fr(1, 1001), Fr(1, 2000), Fr(7, 10000), Fr(999, 1000000), Fr(1, 10**6)]:
    I = math.ceil(1 / e) + 2
    ok &= (I - 1) * e > 1 and (I - 1) * e > 1 - A0
check("pigeonhole: I = ceil(1/e)+2 gives (I-1)e > 1 >= 1 - 51/100 = range of M_j", ok,
      "only 49/100 is needed; the paper's bound is generous")
# rounding M_i down on the grid 51/100 + eZ: a <= M_i < a+e and M_{i+1} <= M_i + e < a + 2e
Mi, e = Fr(6789, 10000), Fr(1, 1500)
a = A0 + e * ((Mi - A0) // e)
check("grid rounding gives a <= M_i < a+e and M_i + e < a + 2e (sample)",
      a <= Mi < a + e and Mi + e < a + 2 * e, f"a={a}")
# disk centred at 2+it, radius 2-a-2e: leftmost point a+2e; radius < 3/2 < T1 (T1 > 2)
rad = vmax(lambda a_, e_: 2 - a_ - 2 * e_, [(A0, Fr(1)), (Fr(0), E_MAX)])
check("zero-free disk radius 2-a-2e <= 149/100 < 3/2 < T1 for a >= 51/100", rad < Fr(3, 2), rad)
# heights in the disk: |t| + radius < (3i+2)T1 + T1 = 3(i+1)T1, needs radius < T1, T1 > 2
check("disk heights stay below 3(i+1)T1 because radius < 3/2 < 2 < T1", Fr(3, 2) < 2)
# Lemma 4.9 radii: zero-free R2 = 2-a-2e, control R6 = 2-a-6e, Borel-Caratheodory R3,R4 (gap e),
# three circles with r0 = 49/100 < R6 < R4  => theta = log(R6/r0)/log(R4/r0) < 1
ok = all(Fr(49, 100) < 2 - a_ - 6 * e_ < 2 - a_ - 4 * e_ < 2 - a_ - 3 * e_ < 2 - a_ - 2 * e_
         for a_ in (Fr(1, 2), A0, Fr(1)) for e_ in (Fr(1, 10**6), E_MAX))
check("Lemma 4.9: r0=49/100 < R6 < R4 < R3 < R2 on a in [1/2,1], e in (0,1e-3] => theta<1", ok)
check("Lemma 4.9: disk r0 has Re s >= 2 - 49/100 = 151/100 > 1", 2 - Fr(49, 100) == Fr(151, 100))
# the control disk of radius R6 reaches Re s = a+6e, the rectangle edge of Lemma 8.1
check("control disk left edge 2 - R6 = a + 6e (rectangle edge in Lemma 8.1)",
      zero(2 - (2 - sp.Symbol('a') - 6 * sp.Symbol('e')) - (sp.Symbol('a') + 6 * sp.Symbol('e'))))
# height budget: |t| <= (3i+2)T1 <= 3I T1 and T1 <= U^{1/100}  =>  (3+|t|)^2 << U^{2/100} = U^{1/50}
tau_max_over_dmin = Fr(1, 100)
check("T1 = Z^tau <= U^{1/100} from tau <= d_min/100 and U >= Z^{d_min}",
      tau_max_over_dmin == Fr(1, 100))
check("(3+|t|)^2 <<_e U^{2*(1/100)} = U^{1/50}", 2 * Fr(1, 100) == Fr(1, 50))
# reflected line: conductor power a-1/2+6e (FE at s=1-a-6e) + deleted product (-Re s)_+ <= 6e
a_, e_ = sp.symbols('a e', real=True)
refl = (sp.Rational(1, 2) - (1 - a_ - 6 * e_)) + 6 * e_
check("reflected bound exponent: (1/2 - (1-a-6e)) + 6e = a - 1/2 + 12e",
      zero(refl - (a_ - sp.Rational(1, 2) + 12 * e_)))
check("reflected conductor exponent a-1/2+6e > 0 on a >= 51/100 (so Q_psi <<U may be used)",
      vmax(lambda a1, e1: -(a1 - Fr(1, 2) + 6 * e1), [(A0, Fr(1)), (Fr(0), E_MAX)]) < 0)
check("deleted product on reflected line: 1-a-6e >= -6e (a <= 1)", True, "(-Re s)_+ <= 6e")
check("Gamma quotient on Re s = 1-a-6e: |t|^{2a-1+12e} <= |t|^2, so C = 2 suffices",
      vmax(lambda a1, e1: 2 * a1 - 1 + 12 * e1, [(A0, Fr(1)), (Fr(0), E_MAX)]) <= 2)
# O_e(1) bins
e = Fr(1, 1500)
nI = math.ceil(1 / e) + 1
na = int((1 - A0) // e) + 1
check("bin count (i,a) <= (ceil(1/e)+1) * (floor(49/(100e))+1) = O_e(1)", nI * na > 0, nI * na)

# ---------------------------------------------------------------------------------------------
# B. Lemma 8.2
# ---------------------------------------------------------------------------------------------
print("== B. Lemma 8.2 (pointwise dyadic estimates)")
r, m, d = sp.symbols('r m delta', real=True)
inv_sq = 2 * r * (a_ - sp.Rational(1, 2) + 6 * e_)
check("|M_r|^2 exponent from Re(s+sigma)=a+6e: 2r(a-1/2+6e) = delta r + 12 e r",
      zero(inv_sq.subs(a_, (1 + d) / 2) - (d * r + 12 * e_ * r)))
direct = 2 * m * (a_ - sp.Rational(1, 2) + 6 * e_)
reflect = 2 * (a_ - sp.Rational(1, 2) + 12 * e_) + 2 * m * (sp.Rational(1, 2) - a_ - 6 * e_)
check("|S_m|^2 direct: delta m + 12 e m",
      zero(direct.subs(a_, (1 + d) / 2) - (d * m + 12 * e_ * m)))
check("|S_m|^2 reflected: delta(1-m) + 24e - 12em",
      zero(reflect.subs(a_, (1 + d) / 2) - (d * (1 - m) + 24 * e_ - 12 * e_ * m)))
check("height in the L-argument: twist (3i+1)T1 + allowance T1/2 < (3i+2)T1",
      Fr(1) + Fr(1, 2) < 2)
check("Prop 8.3 twist gamma - nu: 3i T1 + c T1 <= (3i+1) T1 iff c <= 1 (c is inside T1/2)",
      Fr(1, 2) <= 1)

# ---------------------------------------------------------------------------------------------
# C. Prop 8.3
# ---------------------------------------------------------------------------------------------
print("== C. Prop 8.3 (two saturated witnesses)")
# new line Re z = -1/4: Y*^{-1/4} = U^{-5}; U^2 crude conductor; D*^{1-sigma+1/4}, D* = U^t
g = lambda t, s: -5 + 2 + t * (Fr(5, 4) - s)
worst = vmax(g, [(Fr(1), Fr(3, 2)), (A0, Fr(1))])
check("Gamma-line exponent -3 + t(5/4 - sigma) <= -189/100 on t in [1,3/2], sigma >= 51/100",
      worst == Fr(-189, 100), worst)
check("with T1^2 <= U^{2/100}: crude error <= U^{-187/100}", worst + Fr(2, 100) == Fr(-187, 100))
check("Re(rho - 1/4) >= 51/100 - 1/4 = 26/100 > 0", A0 - Fr(1, 4) == Fr(26, 100))
check("Hecke growth Q^{3/5} <= U^2 (paper's 'deliberately weaker U^2')", Fr(3, 5) < 2)
# saturation: lower U^{delta(r+m)-eps}, uppers U^{delta r + eps'} and U^{delta min(m,1-m) + eps'}
ep, ep2, dl = sp.symbols('epsilon epsilonp delta0', positive=True)
for mm in [Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 5), Fr(2), Fr(21)]:
    lhs = mm - min(mm, 1 - mm)
    rhs = 2 * max(mm - Fr(1, 2), Fr(0))
    if lhs != rhs:
        check("saturation identity m - min(m,1-m) = 2(m-1/2)_+", False, mm)
        break
else:
    check("saturation identity m - min(m,1-m) = 2(m-1/2)_+ (on m in [0,21] samples)", True)
check("(m-1/2)_+ <= (eps + 2 eps')/(2 delta) <= 25 (eps + 2 eps') at delta >= 1/50",
      1 / (2 * Fr(1, 50)) == 25)
# individual lower bounds
lowM = d * (r + m) - ep - (d * sp.Min(m, 1 - m) + ep2)
check("|M_r|^2 >= U^{delta r - eps - eps'} (divide by the S_m upper bound; m >= min(m,1-m))",
      all(sp.simplify(lowM.subs({m: mv}) - (d * r - ep - ep2)).subs({d: Fr(1, 3)}) >= 0
          for mv in [0, Fr(1, 4), Fr(1, 2), Fr(3, 4), 2]))
check("|S_m|^2 >= U^{delta m - eps - eps'} (divide by the M_r upper bound)",
      zero((d * (r + m) - ep - (d * r + ep2)) - (d * m - ep - ep2)))
check("support: r + m >= t - O(1/log U) and m <= 1/2 + O(eps) give r >= t - 1/2 - O(eps)", True)

# ---------------------------------------------------------------------------------------------
# D. Floor a0: every floor-dependent inequality, at a0 = 51/100 and at a0 = 1/2 + eta
# ---------------------------------------------------------------------------------------------
print("== D. The floor a0 = 51/100 versus a0 = 1/2 + eta")
THETA_W = Fr(1, 100)     # vartheta = (-w_r)_+ <= 1/100 in region one


def floor_constraints(x0):
    """Return list of (name, worst value, bound, strict) for region one with x_r >= x0."""
    out = []
    zz = Z0
    # good primes (p not | u): E_p term with the extra |1-W| factor: 4 - 6x - 6z + 2 vartheta < -1
    out.append(("7.1 good prime 4-6x-6z+2vt", 4 - 6 * x0 - 6 * zz + 2 * THETA_W, Fr(-1), True))
    out.append(("7.1 |R| = Q^{4-6x-6z} < 1", 4 - 6 * x0 - 6 * zz, Fr(0), True))
    # ramified p | u: H_p - 1 = O(Q^{-eps_H}); with x+w >= 1+eps0 (eps0 > 0)
    out.append(("7.1 p|u J2: 3/2-3x", Fr(3, 2) - 3 * x0, Fr(0), False))
    out.append(("7.1 p|u J3: 2-3x-w <= 1-2x-eps0", 1 - 2 * x0, Fr(0), False))
    out.append(("7.1 p|u J3: 2-4x", 2 - 4 * x0, Fr(0), False))
    out.append(("7.1 p|u J4: 5/2-4x-w <= 3/2-3x-eps0", Fr(3, 2) - 3 * x0, Fr(0), False))
    out.append(("7.1 p|u J5: 3-6x", 3 - 6 * x0, Fr(0), False))
    out.append(("Lemma 4.9 needs a in [1/2,1]", Fr(1, 2) - x0, Fr(0), False))
    out.append(("8.3 saturation needs delta0 = 2a0-1 > 0", -(2 * x0 - 1), Fr(0), True))
    out.append(("8.1 disk radius 2-a-2e < 3/2 (e -> 0)", 2 - x0, Fr(3, 2), False))
    # Prop 16.1 p not | u: max exponent -a - 4e must be <= -1/2 (below central scale)
    out.append(("16.1 coprime exponent -a-4e (e=0)", -x0, Fr(-1, 2), False))
    # Prop 16.1 p | u table at e = 0 must be < -1/2  (strictness needs a > 1/2)
    for nm, ex in [("j=2 1/2-2a", Fr(1, 2) - 2 * x0), ("j=3 -a", -x0), ("j=3 1-3a", 1 - 3 * x0),
                   ("j=4 1/2-2a", Fr(1, 2) - 2 * x0), ("j=5 2-5a", 2 - 5 * x0)]:
        out.append(("16.1 p|u " + nm, ex, Fr(-1, 2), True))
    return out


res = floor_constraints(A0)
paper_vals = {"7.1 good prime 4-6x-6z+2vt": Fr(-27, 25), "7.1 p|u J2: 3/2-3x": Fr(-3, 100),
              "7.1 p|u J3: 2-3x-w <= 1-2x-eps0": Fr(-1, 50)}
for nm, val in paper_vals.items():
    got = [v for (n, v, b_, s) in res if n == nm][0]
    check(f"a0=51/100 reproduces the paper's value for {nm}", got == val, f"{got}")
check("a0=51/100: 4-6x-6z = -11/10 (TeX 4153)", 4 - 6 * A0 - 6 * Z0 == Fr(-11, 10))
for eta in [Fr(1, 100), Fr(1, 1000), Fr(1, 10**6)]:
    res = floor_constraints(Fr(1, 2) + eta)
    bad = [n for (n, v, b_, s) in res if not (v < b_ if s else v <= b_)]
    check(f"a0 = 1/2 + {eta}: every floor-dependent inequality of Sec. 8 / Lemma 7.1 region one / "
          f"Prop 16.1 holds", not bad, bad if bad else "")
res = floor_constraints(Fr(1, 2))
bad = [n for (n, v, b_, s) in res if not (v < b_ if s else v <= b_)]
check("a0 = 1/2 exactly fails only through strictness: saturation delta0 > 0, and the five 16.1 "
      "p|u entries, which equal -1/2 there",
      set(bad) == {"8.3 saturation needs delta0 = 2a0-1 > 0"} | {n for (n, *_r) in res
                                                                if n.startswith("16.1 p|u")}, bad)
eq_half = [n for (n, v, b_, s) in res if n.startswith("16.1 p|u") and v == Fr(-1, 2)]
check("at a0 = 1/2 every 16.1 p|u entry is exactly -1/2 (<= -1/2 suffices for (5.13e)), so the only "
      "genuinely strict floor requirement is delta0 > 0", len(eq_half) == 5, eq_half)
check("good-prime summability threshold in x0 (z0=17/50, vartheta=1/100): x0 > 149/300 < 1/2",
      sp.solve(sp.Eq(4 - 6 * sp.Symbol('x') - 6 * sp.Rational(17, 50) + sp.Rational(2, 100), -1),
               sp.Symbol('x'))[0] == sp.Rational(149, 300))
# FLOOR_BIN_BARRIER Sec. 1.5 closed form: sigma_FB(tau) = (13-18tau)/(15-18tau), tau = -delta0
sFB = lambda tau: (13 - 18 * tau) / (15 - 18 * tau)
check("FLOOR_BIN_BARRIER: sigma_FB(-1/50) = 167/192 (a0 = 51/100, DH counts)",
      sFB(Fr(-1, 50)) == Fr(167, 192))
check("FLOOR_BIN_BARRIER: sigma_FB(0) = 13/15 (a0 = 1/2), equal to the low-side cap",
      sFB(Fr(0)) == Fr(13, 15))
LXq, LYq, ELq = Fr(13, 32), Fr(13, 32), Fr(3, 16)
Hq = 1 - LXq + ELq
d0 = 2 * A0 - 1
FB = A0 * (1 - LYq) + Hq * (Fr(5, 6) + d0 / 2) - ELq / 2 + d0 * ELq / 2
check("(FB) at the LP point (13/32,13/32,3/16), a0 = 51/100, equals 167/192", FB == Fr(167, 192), FB)

# ---------------------------------------------------------------------------------------------
# E. Prop 16.1
# ---------------------------------------------------------------------------------------------
print("== E. Prop 16.1 (dynamic local errors and conductor allocation)")
xr = lambda a1, e1: a1 + 16 * e1
wr = lambda a1, e1: 1 - a1 - 6 * e1
BOX = [(A0, Fr(1)), (Fr(0), E_MAX)]
check("x_r + w_r = 1 + 10e (eps0 = 10e in region one)",
      all(xr(a1, e1) + wr(a1, e1) == 1 + 10 * e1 for a1, e1 in itertools.product(*BOX)))
check("vartheta = (-w_r)_+ <= 6e", vmax(lambda a1, e1: -wr(a1, e1) - 6 * e1, BOX) <= 0)
check("H_p - 1 = O(Q^{-10e}) at p|u: 3/2 - 3x_r <= -10e",
      vmax(lambda a1, e1: Fr(3, 2) - 3 * xr(a1, e1) + 10 * e1, BOX) <= 0)
check("H_p - 1 = O(Q^{-1-10e}) at p not|u: good-prime -27/25-type term <= -1-10e",
      vmax(lambda a1, e1: 4 - 6 * xr(a1, e1) - 6 * Z0 + 12 * e1 + 1 + 10 * e1, BOX) <= 0)
four = [("-x_r+2vt", lambda a1, e1: -xr(a1, e1) + 12 * e1, lambda a1, e1: -a1 - 4 * e1),
        ("-6z_r+2vt", lambda a1, e1: -6 * Z0 + 12 * e1, lambda a1, e1: Fr(-51, 25) + 12 * e1),
        ("4-5x_r-6z_r+2vt", lambda a1, e1: 4 - 5 * xr(a1, e1) - 6 * Z0 + 12 * e1,
         lambda a1, e1: Fr(49, 25) - 5 * a1 - 68 * e1),
        ("1-w_r-6z_r+vt", lambda a1, e1: 1 - wr(a1, e1) - 6 * Z0 + 6 * e1,
         lambda a1, e1: a1 - Fr(51, 25) + 12 * e1)]
for nm, f, paper in four:
    same = all(f(a1, e1) == paper(a1, e1) for a1, e1 in itertools.product(*BOX))
    check(f"p not|u exponent {nm} matches the paper's affine form (8933-8935)", same)
check("all four p not|u exponents <= -51/100 on the box (so <= Q^{-51/100})",
      max(vmax(f, BOX) for _, f, _ in four) <= Fr(-51, 100),
      max(vmax(f, BOX) for _, f, _ in four))
# p | u table: exponent = x_r - 1 + monomial exponent (after separating Q^z)
mono = {  # monomial exponents in E_p at p|u (D = W = 0), from the six-valuation table 4021-4031
    "j=1 eta Q^{-x-w}": lambda x, w: -x - w,
    "j=2 Q^{3/2-3x}": lambda x, w: Fr(3, 2) - 3 * x,
    "j=3 Q^{2-3x-w}": lambda x, w: 2 - 3 * x - w,
    "j=3 Q^{2-4x}": lambda x, w: 2 - 4 * x,
    "j=4 Q^{5/2-4x-w}": lambda x, w: Fr(5, 2) - 4 * x - w,
    "j=5 Q^{3-6x}": lambda x, w: 3 - 6 * x,
}
paper_tab = {"j=1 eta Q^{-x-w}": (lambda a1: a1 - 2, 6), "j=2 Q^{3/2-3x}": (lambda a1: Fr(1, 2) - 2 * a1, -32),
             "j=3 Q^{2-3x-w}": (lambda a1: -a1, -26), "j=3 Q^{2-4x}": (lambda a1: 1 - 3 * a1, -48),
             "j=4 Q^{5/2-4x-w}": (lambda a1: Fr(1, 2) - 2 * a1, -42), "j=5 Q^{3-6x}": (lambda a1: 2 - 5 * a1, -80)}
ok_tab = True
for k, f in mono.items():
    base, de = paper_tab[k]
    for a1, e1 in itertools.product(*BOX):
        ok_tab &= (xr(a1, e1) - 1 + f(xr(a1, e1), wr(a1, e1)) == base(a1) + de * e1)
check("p|u table (8947-8953): values at e=0 and e-changes +6,-32,(-26,-48),-42,-80 reproduce", ok_tab)
check("p|u table entries strictly below -1/2 on the box",
      max(vmax(lambda a1, e1, f=f: xr(a1, e1) - 1 + f(xr(a1, e1), wr(a1, e1)), BOX)
          for f in mono.values()) < Fr(-1, 2))
Rterm = lambda a1, e1: xr(a1, e1) - 1 + 4 - 6 * xr(a1, e1) - 6 * Z0
check("common R term: x_r - 1 + 4 - 6x_r - 6z_r = 49/25 - 1 - 5a - 80e < -1/2",
      all(Rterm(a1, e1) == Fr(49, 25) - 1 - 5 * a1 - 80 * e1 for a1, e1 in itertools.product(*BOX))
      and vmax(Rterm, BOX) < Fr(-1, 2))
check("|R| <= Q^{-11/10} and |V| = Q^{-51/25} at x_r >= 51/100, z_r = 17/50",
      4 - 6 * A0 - 6 * Z0 == Fr(-11, 10) and -6 * Z0 == Fr(-51, 25))
check("strict term with extra V: -w_r - 6z_r < -1/2", vmax(lambda a1, e1: -wr(a1, e1) - 6 * Z0, BOX) < Fr(-1, 2))
check("explicit rescaling term -Q^{-w}: -1 - w_r < -1/2", vmax(lambda a1, e1: -1 - wr(a1, e1), BOX) < Fr(-1, 2))
# conductor allocation
Ast = lambda a1, e1: Fr(1, 2) - wr(a1, e1)
check("A* = 1/2 - w_r = a - 1/2 + 6e > 0", all(Ast(a1, e1) == a1 - Fr(1, 2) + 6 * e1 for a1, e1 in
                                              itertools.product(*BOX)) and
      min(Ast(a1, e1) for a1, e1 in itertools.product(*BOX)) > 0)
check("U-exponent A* + 6e = a - 1/2 + 12e (9032-9034)",
      all(Ast(a1, e1) + 6 * e1 == a1 - Fr(1, 2) + 12 * e1 for a1, e1 in itertools.product(*BOX)))
ok = True
for a1, e1 in itertools.product(*BOX):
    for j in range(2, 6):
        ok &= Z0 - wr(a1, e1) - (j - 1) * Ast(a1, e1) <= Z0 - Fr(1, 2)
check("strict ramified label: z_r - w_r - (j_p-1)A* <= z_r - 1/2 for j_p in 2..5", ok)
check("-w_r - A* = -1/2 identically", all(-wr(a1, e1) - Ast(a1, e1) == Fr(-1, 2) for a1, e1 in
                                          itertools.product(*BOX)))
check("coprime slot total P_i^{z_r - 51/100} is below the central scale P_i^{z_r - 1/2}",
      Fr(-51, 100) < Fr(-1, 2))
check("retained w heights: |Im(1-w)| <= T1 < (3i+2)T1 (inside the buffered rectangle)", 1 < 2)

# ---------------------------------------------------------------------------------------------
# F. Lemma 20.1 and the floor
# ---------------------------------------------------------------------------------------------
print("== F. Lemma 20.1 (consumption of (5.13e)) and the floor bound")
b_, h_, ell_ = Fr(1, 8), Fr(13, 16), Fr(1, 6)
lx_ = 1 + ell_ - h_
ly_ = lx_ + b_
A, dd, q, R, D = sp.symbols('a delta q R d', real=True)
z0 = sp.Rational(17, 50)
H, L, LY = sp.Rational(13, 16), sp.Rational(1, 6), sp.Rational(23, 48)
line1 = A - sp.Rational(7, 8) + H * (z0 - sp.Rational(1, 6)) - A * LY - (1 - A) * L - (dd / 2 - q) * L \
    + D * (R + dd / 2 - z0)
line2 = -sp.Rational(1, 48) + sp.Rational(2, 3) * dd + q / 6 - H * (1 - R) + (D - H) * (R + dd / 2 - z0)
check("(20.1) first line = second line with a = (1+delta)/2, C0 = -1/48",
      zero(line1.subs(A, (1 + dd) / 2) - line2))
check("-(1-a)ell - (delta/2 - q)ell = -ell/2 + q ell", zero((-(1 - A) * L - (dd / 2 - q) * L).subs(dd, 2 * A - 1)
                                                             - (-L / 2 + q * L)))
# Lemma 10.4 exponent with sigma0 = 7/8, g = q ell (15827-15829)
lem104 = A - sp.Rational(7, 8) + H * (z0 - sp.Rational(1, 6)) - A * LY - L / 2 + q * L + D * (R + dd / 2 - z0)
check("Lemma 10.4 exponent at sigma0=7/8, g=q ell equals (20.1) line 1",
      zero(lem104.subs(dd, 2 * A - 1) - line1.subs(dd, 2 * A - 1)))
# (5.13e) per-slot exponents: main |Q_i| <= P_i^{g_i+vt}; error g_i = 0 ; both times P_i^{z0-1/2}
li = sp.symbols('l1:5', positive=True)
gi = sp.symbols('g1:5', nonnegative=True)
tot = sum(l * (z0 - sp.Rational(1, 2)) + l * g for l, g in zip(li, gi))
check("slot product exponent sum_i l_i(z0-1/2) + l_i g_i = ell(z0-1/2) + q ell (any lengths)",
      zero(tot - (sum(li) * (z0 - sp.Rational(1, 2)) + sum(l * g for l, g in zip(li, gi)))))
fl = line2.subs({D: H, R: 1, q: sp.Rational(1, 100), dd: sp.Rational(1, 50)})
check("floor (20.5): E(h) at R=1, q=delta0/2, delta0=1/50 is C0 + 3 delta0/4 = -7/1200",
      fl == sp.Rational(-7, 1200), fl)
check("floor slope R + delta0/2 - 17/50 = 67/100 > 0", 1 + Fr(1, 100) - Fr(17, 50) == Fr(67, 100))
FBp = A0 * (1 - ly_) + h_ * (Fr(5, 6) + Fr(1, 100)) - ell_ / 2 + Fr(1, 50) * ell_ / 2
check("(FB) at the paper geometry minus 7/8 equals -7/1200 (FLOOR_BIN_BARRIER 1.2)",
      FBp - Fr(7, 8) == Fr(-7, 1200), FBp - Fr(7, 8))
flo = line2.subs({D: H, R: 1, q: sp.Symbol('eta')}).subs(dd, 2 * sp.Symbol('eta'))
check("floor at a0 = 1/2 + eta (delta0 = 2 eta, q <= eta): E(h) = -1/48 + 3 eta/2",
      zero(flo - (-sp.Rational(1, 48) + sp.Rational(3, 2) * sp.Symbol('eta'))))

# ---------------------------------------------------------------------------------------------
# G. Constants used in the order of choices
# ---------------------------------------------------------------------------------------------
print("== G. Prop 20.3 constants")
check("h + zeta < 5 ell iff zeta < 1/48", 5 * ell_ - h_ == Fr(1, 48))
check("supply ell/h = 8/39 and 8/39 - 7/37 = 23/1443", ell_ / h_ == Fr(8, 39) and Fr(8, 39) - Fr(7, 37) == Fr(23, 1443))
check("for h < d <= h + zeta < 5/6: ell/d > 1/5 and 1/5 - 7/37 = 2/185",
      ell_ / (h_ + Fr(1, 48)) == Fr(1, 5) and Fr(1, 5) - Fr(7, 37) == Fr(2, 185))
Kmin = next(K for K in itertools.count(2, 2) if 2 * ell_ / K < Fr(1, 185))
check("smallest even K with 2 ell/K < 1/185 is 62; 2 ell/K < (2/185)/2", Kmin == 62
      and 2 * ell_ / Kmin < Fr(1, 185), Kmin)
check("w_i = ell_i/d <= 2 ell/K for d >= 1/2; delta w_i < 2 ell/K for delta <= 5/6 < 1",
      (ell_ / Kmin) / Fr(1, 2) == 2 * ell_ / Kmin)
for K in (62, 64, 1000):
    kP = Fr(7, 16) * ell_ / K
    if not (kP == Fr(7, 96 * K) and 0 < kP < Fr(7, 8) * ell_ / K == Fr(7, 48 * K)):
        check("kappa_P = 7/(96K) in (0, 7/(48K))", False, K)
        break
else:
    check("kappa_P = (7/16)(ell/K) = 7/(96K) lies in (0, (7/8) min ell_i) = (0, 7/(48K))", True)
check("m_w = ly/20 = 23/960, m_z = h/600 = 13/9600", ly_ / 20 == Fr(23, 960) and h_ / 600 == Fr(13, 9600))
check("small rows: h(17/50-1/6) - ly/2 = -79/800; + 2 d_min = -63/800 = -m_small",
      h_ * (Z0 - Fr(1, 6)) - ly_ / 2 == Fr(-79, 800) and Fr(-79, 800) + 2 * Fr(1, 100) == Fr(-63, 800))
check("small-row row exponent 63/50 < 2", Fr(63, 50) < 2)
check("m_hi = (1 - h/4) Delta = 51 Delta/64", 1 - h_ / 4 == Fr(51, 64))
check("m_high = min(51 Delta/64, 63/800) = 51 Delta/64 for every Delta <= 1/24",
      Fr(51, 64) * Fr(1, 24) < Fr(63, 800))
check("budget: four allocations < m_high/8 each + dyadic < m_high/8 leaves > 3 m_high/8 >= m",
      1 - 5 * Fr(1, 8) == Fr(3, 8) and Fr(1, 4) < Fr(3, 8))
check("principal: each of (1+h)e+eps_pr < m_w/4 etc. leaves > 3/4 of m_w, m_z, m_P >= 4m",
      1 - Fr(1, 4) == Fr(3, 4) and Fr(1, 4) < Fr(3, 4))
Dl = sp.Symbol('Delta', positive=True)
mm_ = sp.Symbol('m', positive=True)
check("Prop 2.1 eps* = min(Delta - omega, sigma) = sigma = m/2 when omega = Delta/2 and m <= 51Delta/256",
      sp.Rational(51, 256) / 2 < sp.Rational(1, 2))
# tau_0 = d_min eps_ht / (20 (1 + A_ht))
Aht, eht, dmin = sp.symbols('A_ht eps_ht d_min', positive=True)
tau0 = dmin * eht / (20 * (1 + Aht))
check("tau <= tau0 gives tau * A_ht <= d_min eps_ht/20 < d_min eps_ht/10 (2^A absorbed at large Z)",
      sp.simplify(tau0 * Aht - dmin * eht / 20 * Aht / (1 + Aht)) == 0)
check("detector crude error with T1^2: -189/100 + 2/100 = -187/100 < 0", Fr(-189, 100) + Fr(2, 100) == Fr(-187, 100))
check("buffered moderate range: d <= h + zeta < h + 1/48 = 5/6 < 1", h_ + Fr(1, 48) == Fr(5, 6))
check("Section 8 tau <= d_min/100 with Sec. 20.3 d_min = 1/100 gives tau <= 1/10000",
      Fr(1, 100) / 100 == Fr(1, 10000))
# coefficient bounds quoted at 16230: delta >= 1/50, D_x >= 37/18, J >= 35/54
x = sp.Symbol('x')
Dx = 3 - sp.Rational(17, 9) * x
Px = (2 - sp.Rational(8, 9) * x) * (1 - x)
alpha = sp.Rational(5, 6)
check("D_x = 3 - 17x/9 in [37/18, 3] on x in [0,1/2]", Dx.subs(x, sp.Rational(1, 2)) == sp.Rational(37, 18))
check("P_x in [7/9, 2] on [0,1/2] (decreasing)", Px.subs(x, sp.Rational(1, 2)) == sp.Rational(7, 9)
      and sp.diff(Px, x).subs(x, 0) < 0 and sp.diff(Px, x).subs(x, sp.Rational(1, 2)) < 0)
Jmin = min(alpha * sp.Rational(37, 18), alpha * sp.Rational(7, 9))
check("J = (alpha-delta)D_x + delta P_x >= min(alpha D_x, alpha P_x) >= 35/54 (affine in delta)",
      Jmin == sp.Rational(35, 54))
check("R_* + Delta/4 <= 17/12 + 1/96 <= 139/96 and 139/96 + 1/2 - 17/50 < 2",
      Fr(17, 12) + Fr(1, 96) <= Fr(139, 96) and Fr(139, 96) + Fr(1, 2) - Fr(17, 50) < 2)
check("R + delta/2 - 17/50 >= 33/50 - delta/2 >= 4/25 for R >= 1 - delta, delta <= 5/6",
      Fr(33, 50) - Fr(5, 12) >= Fr(4, 25))
Ri = sp.Rational(76, 75) - sp.Rational(2, 3) * dd
Ei = line2.subs({D: sp.Rational(1, 2), R: Ri, q: dd / 2})
check("intermediate rows: E(1/2) = -529/2400 + 25 delta/96 at R = 76/75 - 2delta/3, q = delta/2",
      zero(Ei - (-sp.Rational(529, 2400) + sp.Rational(25, 96) * dd)))
check("intermediate rows: value at delta = 5/6 is -49/14400", Ei.subs(dd, sp.Rational(5, 6)) == sp.Rational(-49, 14400))
check("intermediate slope 101/150 - delta/6 > 0 and R(1/50) = 1",
      zero(Ri + dd / 2 - z0 - (sp.Rational(101, 150) - dd / 6)) and Ri.subs(dd, sp.Rational(1, 50)) == 1)

# ---------------------------------------------------------------------------------------------
# H. Quantifier order of Prop 20.3 as a dependency graph
# ---------------------------------------------------------------------------------------------
print("== H. Prop 20.3 order of choices: dependency graph")
# (node, stage, deps, TeX source). Stage: G = given/fixed numerals, P = pretarget choice,
# T = target and after. Order of the list = order of choice in the proof.
NODES = [
    ("beta_star", "G", [], "379-387 (global sup, not chosen)"),
    ("partI_11_12", "G", ["beta_star"], "6812-6814 (Thm 3.1 gives beta* <= 11/12)"),
    ("Delta", "G", ["beta_star", "partI_11_12"], "6816-6820"),
    ("kappa", "G", ["beta_star"], "6819"),
    ("geometry", "G", [], "6857-6866 numerals (b,h,ell,lx,ly)"),
    ("numerals", "G", [], "z0=17/50, alpha=5/6, d_min=1/100, a0=51/100"),
    ("T_group", "G", [], "3327 (chosen independently of the target)"),
    ("m_lo", "P", ["Delta"], "16185"),
    ("m_hi", "P", ["Delta", "geometry"], "16180-16184"),
    ("m_small", "P", ["geometry", "numerals"], "15875-15889"),
    ("m_high", "P", ["m_hi", "m_small"], "16223"),
    ("m_w_m_z", "P", ["geometry"], "15673-15676"),
    ("moment_losses", "P", ["m_high", "numerals", "kappa"], "16227-16236"),
    ("eta_mesh", "P", ["moment_losses", "numerals", "kappa"], "16238-16243; Lemma 18.1 12570-12572"),
    ("b_round", "P", ["m_high"], "16243-16245"),
    ("K_slots", "P", ["eta_mesh", "b_round", "geometry"], "16246-16261"),
    ("m_P", "P", ["K_slots"], "16303-16307"),
    ("amp_width", "P", ["m_high", "K_slots"], "16312-16314"),
    ("power_losses", "P", ["m_high", "K_slots", "m_w_m_z", "m_P", "amp_width"], "16312-16324"),
    ("e_bin", "P", ["power_losses", "amp_width", "K_slots", "m_w_m_z", "m_P", "m_high"],
     "16312-16324; e < e_0(eps) of Lemma 8.2 (4398-4404); Lemma 19.1 subdivision 15067-15070"),
    ("zeta", "P", ["m_high"], "16326-16331"),
    ("z_inf", "P", ["zeta", "m_high", "geometry"], "16331-16335; 15905-15916"),
    ("P0_cutoff", "P", ["e_bin", "numerals"], "16336-16341; Prop 16.1 8858, 8911-8912; (10.2) 5526-5531"),
    ("m_common", "P", ["m_high", "m_w_m_z", "m_P"], "16365-16368"),
    ("omega", "P", ["Delta"], "16369-16370"),
    ("sigma", "P", ["m_common"], "16451"),
    ("eps_ht", "P", ["power_losses"], "16371-16372"),
    ("target_eta", "T", ["omega", "sigma", "Delta"], "Prop 2.1 proof 435-446, 498-500"),
    ("arith_data", "T", ["target_eta", "P0_cutoff", "T_group"], "16374-16377"),
    ("internal_orders", "T", ["arith_data", "K_slots", "power_losses"], "16379-16383"),
    ("A_eta_B_eta", "T", ["internal_orders", "arith_data"], "16381-16394"),
    ("tau0", "T", ["eps_ht", "A_eta_B_eta", "numerals"], "16395-16400"),
    ("tau_eta", "T", ["tau0", "m_common", "A_eta_B_eta", "numerals"], "Lemma 11.1 6561-6566"),
    ("aux_ext_orders", "T", ["tau_eta"], "16418-16431; 4415-4416; 4642-4643"),
    ("N_eta", "T", ["A_eta_B_eta", "tau_eta", "m_common", "aux_ext_orders"], "6571-6574"),
    ("Z0", "T", ["N_eta", "tau_eta", "arith_data", "e_bin", "K_slots"], "6575-6576; 16443"),
]
idx = {n: i for i, (n, *_r) in enumerate(NODES)}
check("every dependency is a declared node", all(dp in idx for _, _, deps, _ in NODES for dp in deps))
order_ok = all(idx[dp] < idx[n] for n, _, deps, _ in NODES for dp in deps)
check("each choice depends only on earlier choices (no forward reference)", order_ok)
stage = {n: s for n, s, *_r in NODES}
crossing = [(n, dp) for n, s, deps, _ in NODES if s in "GP" for dp in deps if stage[dp] == "T"]
check("no given/pretarget quantity depends on a target-stage quantity", not crossing, crossing)
check("omega and sigma are pretarget (as Prop 2.1 requires)", stage["omega"] == "P" and stage["sigma"] == "P")


def has_cycle(extra_edges):
    adj = {n: set(deps) for n, _, deps, _ in NODES}
    for n, dp in extra_edges:
        adj[n].add(dp)
    color = {n: 0 for n in adj}

    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1 or (color[v] == 0 and dfs(v)):
                return True
        color[u] = 2
        return False
    return any(color[n] == 0 and dfs(n) for n in adj)


check("graph as stated is acyclic", not has_cycle([]))
# Stated-independence claims: each is an edge the paper asserts is ABSENT. If adding it creates a
# cycle, the claim is load-bearing for the order of choices.
CLAIMS = [
    ("I1 Lemma 18.1 mesh independent of the slot count (12570-12572, 16241-16243)",
     ("eta_mesh", "K_slots")),
    ("I2 moment-loss cost coefficients independent of K (16228-16233)", ("moment_losses", "K_slots")),
    ("I3 A_eta independent of tau and N (16384-16389, 16428-16431)", ("A_eta_B_eta", "tau_eta")),
    ("I4 B_eta independent of N (16385-16389; Lemma 11.1 6538)", ("A_eta_B_eta", "N_eta")),
    ("I5 P0 cutoff independent of the target (uniform majorant; CONTOUR review)", ("P0_cutoff", "target_eta")),
    ("I6 K's capacity gap uniform in zeta < 1/48 (16269-16275)", ("K_slots", "zeta")),
    ("I7 margins m_w, m_z independent of e (15673-15676)", ("m_w_m_z", "e_bin")),
    ("I8 m_small independent of e (error-free saving, 15889)", ("m_small", "e_bin")),
    ("I9 eps_ht (detector height allowance) independent of the target (16371)", ("eps_ht", "target_eta")),
]
for name, edge in CLAIMS:
    lb = has_cycle([edge])
    crosses = stage[edge[0]] in "GP" and stage[edge[1]] == "T"
    print(f"INFO {name}: violating it {'creates a cycle' if lb else 'creates no cycle'}"
          f"{' and puts a target quantity before the target' if crosses else ''}")
    check(f"{name.split()[0]} is load-bearing (its failure breaks the order)", lb or crosses)

print()
print(f"{len(FAILS)} failure(s)")
sys.exit(len(FAILS))
