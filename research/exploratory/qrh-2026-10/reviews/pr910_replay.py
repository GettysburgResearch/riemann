#!/usr/bin/env python3
"""Independent reviewer replay of the exponent arithmetic in draft PR 910
(standalone/2026-10-10-quasi-riemann-height-descent, head 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c).

Status: review instrument (exploration-level), written from scratch by the reviewer.
Scope:  the exponent arithmetic and the stated geometric adapters ONLY.  Every imported analytic
        lemma of the 30 Sep 2026 OpenAI manuscript is treated as a black box whose stated output
        exponent is transcribed here.  Nothing below checks a moment estimate, a sieve, a contour
        move, or any analytic adapter's proof.
Arithmetic: exact rationals (fractions.Fraction) and sympy (exact rationals / Q(sqrt 921)) for every
        acceptance gate.  Floating point is used only for (i) our own exponent model
        (scripts/threshold_calculus.py, FLOATING_RECONNAISSANCE) and (ii) locating minima that are
        then certified exactly; no float result is used as a proof gate.
Run:    python3 pr910_replay.py   (writes pr910_replay_output.json next to this file)
"""
from fractions import Fraction as F
import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def rec(section, claim, ok, detail="", finding=False):
    """finding=True marks a check that tests a PR statement which this review reports as incorrect;
    its failure is the documented finding, not a defect of the replay."""
    OUT.append({"section": section, "claim": claim, "pass": bool(ok), "detail": str(detail),
                "documented_finding": finding})
    tag = "PASS " if ok else ("FINDING " if finding else "FAIL ")
    print(tag + f"[{section}] {claim}" + (f" :: {detail}" if detail else ""))


def fr(x):
    """sympy Rational -> Fraction"""
    x = sp.nsimplify(x)
    return F(int(x.p), int(x.q))


# =============================================================================================
# 0. Perturbed geometry (PR GEOMETRY_PERTURBATION.md eq. 2.1)
# =============================================================================================
s0 = F(1, 40000)
b = F(1, 8)
ell = F(1, 6) + s0
lx = (1 - ell - b) / 2
ly = (1 - ell + b) / 2
h = 1 - lx + ell
M = lx + ly
z0 = F(17, 50)
alpha = F(5, 6)
S = "0 geometry"
rec(S, "tuple ell,lx,ly,h = 20003/120000, 84997/240000, 114997/240000, 65003/80000",
    (ell, lx, ly, h) == (F(20003, 120000), F(84997, 240000), F(114997, 240000), F(65003, 80000)))
rec(S, "M + ell = 1 and h = (1+3 ell+b)/2", M + ell == 1 and h == (1 + 3 * ell + b) / 2)
cconst = lx / 2 - 1 + h / 6           # C(s) = s + cconst (manuscript Def. 10.1)
rec(S, "C(s) = s - 11/16 at the perturbed geometry (independent of ell)", cconst == F(-11, 16), cconst)

# =============================================================================================
# 1. Low side, rebuilt from the black-box outputs (Lemma 14.3 maximised, Prop 15.2, Prop 15.3)
# =============================================================================================
S = "1 low side"


def energy_branches(Mp, lp):
    """sup of E_ref (14.14) over admissible dyads: three affine branches (our LP-verified closed form)."""
    return [Mp, (2 * Mp + 1 + 3 * lp) / 4, 2 * Mp + lp - 1]


def low_excess(d):
    """log_Z of one rescaled-subset contribution of total length d, minus lx/2 + b/12.
    Gram (Prop 15.2): (Q/Y')(1 + Pa^{1/6} + Pa^2/Y'), Pa = Y'^2/Q = Z^b (up to N(b*)), Q ~ Z^{M'}.
    Separation: Q^{-1/2} (Gram)^{1/2} (row energy)^{1/2}; then Z^d tuples, coefficient Z^{-3d/2}."""
    Mp, lp, Yp = M - 2 * d, ell - d, ly - d
    Pa = 2 * Yp - Mp
    gram = Mp - Yp + max(F(0), Pa / 6, 2 * Pa - Yp)
    EB = max(energy_branches(Mp, lp))
    sep = -Mp / 2 + (gram + EB) / 2
    return sep + d - F(3, 2) * d - (lx / 2 + b / 12)


rec(S, "Pa exponent 2(ly-d) - (M-2d) = b for every d", all(2 * (ly - d) - (M - 2 * d) == b
                                                          for d in [F(0), ell / 3, ell]))
# piecewise-affine in d: collect all breakpoints of the max() branches on [0, ell]
cands = {F(0), ell}
br_lin = []  # (slope, intercept) pieces of the inner maxima, in d
# energy branches as functions of d
Eb = [(F(-2), M), (F(-2) * 2 / 4 - F(3, 4), (2 * M + 1 + 3 * ell) / 4), (F(-5), 2 * M + ell - 1)]
Gb = [(F(0), F(0)), (F(0), b / 6), (F(1), 2 * b - ly)]
for fam in (Eb, Gb):
    for i in range(len(fam)):
        for j in range(i + 1, len(fam)):
            (a1, c1), (a2, c2) = fam[i], fam[j]
            if a1 != a2:
                dd = (c2 - c1) / (a1 - a2)
                if 0 <= dd <= ell:
                    cands.add(dd)
cands = sorted(cands)
vals = {d: low_excess(d) for d in cands}
theta_excess = max(vals.values())
rec(S, "max over d in [0,ell] of the low excess is exactly 0, attained at d=0",
    theta_excess == 0 and vals[F(0)] == 0 and all(v < 0 for d, v in vals.items() if d > 0),
    {str(k): str(v) for k, v in vals.items()})
L0 = lx / 2 + b / 12
rec(S, "L0 = lx/2 + b/12 = 3/16 - 1/160000", L0 == F(3, 16) - F(1, 160000), L0)
beta0 = L0 - cconst
rec(S, "beta0 = L0 + 11/16 = 139999/160000 = 7/8 - 1/160000",
    beta0 == F(139999, 160000) and F(7, 8) - beta0 == F(1, 160000), beta0)
rec(S, "beta0 = 11/12 - ell/4 = 1 - h/6 + b/12", beta0 == F(11, 12) - ell / 4 == 1 - h / 6 + b / 12)

# PR's corrected row loss f_ell(d) = -d + (5 ell - 1 + d)_+/8 versus my rebuilt excess
def f_pr(d):
    return -d + max(F(0), 5 * ell - 1 + d) / 8


test_d = sorted(set(cands) | {ell * k / 97 for k in range(98)})
rec(S, "PR f_ell(d) equals my rebuilt excess at all breakpoints and 98 rational d",
    all(f_pr(d) == low_excess(d) for d in test_d))
rec(S, "PR (4.1): energy sup = M' + (5ell-1+d)_+/4 (third branch 2M'+ell'-1 = M'-3d never binds)",
    all(max(energy_branches(M - 2 * d, ell - d)) == (M - 2 * d) + max(F(0), 5 * ell - 1 + d) / 4
        for d in test_d))
kink = 1 - 5 * ell
row_loss_at_ell = max(F(0), 5 * ell - 1 + ell) / 4
rec(S, "row-norm loss is genuinely positive for d > 1-5ell = 1/6 - 1/8000 (max 3/80000 at d=ell)",
    kink == F(1, 6) - F(1, 8000) and row_loss_at_ell == F(3, 80000), f"kink={kink}, loss(ell)={row_loss_at_ell}")
rec(S, "f_ell slopes -1 and -7/8; f_ell(ell) = -ell + 6 s0/8 < 0",
    f_pr(ell) == -ell + F(6, 8) * s0 and f_pr(ell) < 0)
rec(S, "length gates: lx-ell = 44991/240000, M-2ell = 19997/40000, ly-ell-11b/6 = 19991/240000 (all > 0)",
    lx - ell == F(44991, 240000) and M - 2 * ell == F(19997, 40000)
    and ly - ell - F(11, 6) * b == F(19991, 240000))

# symbolic: on the line M+ell=1 with ell <= 1/5, beta0(ell,b) = 11/12 - ell/4 (b cancels)
l_, b_ = sp.symbols("ell b", real=True)
lx_s, ly_s = (1 - l_ - b_) / 2, (1 - l_ + b_) / 2
h_s = 1 - lx_s + l_
beta0_s = sp.simplify(lx_s / 2 + b_ / 12 - (lx_s / 2 - 1 + h_s / 6))
rec(S, "symbolic: beta0(ell,b) = 1 - h/6 + b/12 = 11/12 - ell/4 on M+ell=1",
    sp.simplify(beta0_s - (sp.Rational(11, 12) - l_ / 4)) == 0, beta0_s)
rec(S, "symbolic: C(s)-s = -2/3 - b/6 on M+ell=1 (ell-free)",
    sp.simplify(lx_s / 2 - 1 + h_s / 6 - (-sp.Rational(2, 3) - b_ / 6)) == 0)

# =============================================================================================
# 2. High side
# =============================================================================================
S = "2 high side"
a_, sig_, z_, q_, d_, R_, de_, x_ = sp.symbols("a sigma0 z0 q d R delta x", real=True)
# (2a) PR eq. (3.6) rebuilt from the outside Mellin powers X^{1/2-z} Z^{s+z-1} Y^{w-1} on the central
#      contour Re s=a, Re w=1-a, Re z=z0, the source's common factor U^{delta/2} Z^{ell(z0-1/2)+q ell},
#      row count U^R, q_u^{-z0}, all relative to C(sigma0).
lxg, lyg, lg = sp.symbols("lx ly ell", real=True)
hg = 1 - lxg + lg
outside = lxg * (sp.Rational(1, 2) - z_) + (a_ + z_ - 1) - a_ * lyg + lg * (z_ - sp.Rational(1, 2)) + q_ * lg \
    + d_ * (R_ + de_ / 2) - d_ * z_ - (sig_ + lxg / 2 - 1 + hg / 6)
pr36 = a_ - sig_ + hg * (z_ - sp.Rational(1, 6)) - a_ * lyg - lg / 2 + q_ * lg + d_ * (R_ + de_ / 2 - z_)
rec(S, "PR (3.6) equals the sum of outside powers and source factors minus C(sigma0) (any geometry)",
    sp.expand(outside - pr36) == 0)
# (2b) specialise d=h, a=(1+delta)/2, sigma0=beta0(ell,b), q=x delta -> PR (6.1) / envelope (1.3)
E_dh = pr36.subs({d_: hg}).subs({lxg: lx_s, lyg: ly_s, lg: l_}).subs(
    {a_: (1 + de_) / 2, sig_: sp.Rational(11, 12) - l_ / 4, q_: x_ * de_, z_: sp.Rational(17, 50)})
pr61 = -sp.Rational(1, 4) + 5 * l_ / 4 + b_ / 6 + de_ * (sp.Rational(1, 2) + l_) + x_ * de_ * l_ \
    - (1 + 3 * l_ + b_) / 2 * (1 - R_)
rec(S, "PR (6.1): E(h) = -1/4+5ell/4+b/6+delta(1/2+ell)+x delta ell - h(1-R) (z0 drops out at d=h)",
    sp.expand(E_dh - pr61) == 0)
# (2c) source (20.4) at ell=1/6, b=1/8, sigma0=7/8
src204 = -sp.Rational(1, 48) + 2 * de_ / 3 + x_ * de_ / 6 - sp.Rational(13, 16) * (1 - R_)
rec(S, "at ell=1/6,b=1/8 PR (6.1) reduces to source (20.4) at d=h: C0+2delta/3+q/6-h(1-R)",
    sp.expand(pr61.subs({l_: sp.Rational(1, 6), b_: sp.Rational(1, 8)}) - src204) == 0)
# (2d) R_* : balance R_short(t) = L(t) from source Prop 19.2 at Delta = 0 (kappa = 3/4)
t_ = sp.symbols("t", real=True)
Dx = 3 - sp.Rational(17, 9) * x_
Px = (2 - sp.Rational(8, 9) * x_) * (1 - x_)
al = sp.Rational(5, 6)
Rshort = 1 - de_ + de_ * Px / Dx * (sp.Rational(3, 2) - t_)
Lt = 1 - de_ + (al - de_) * (t_ - 1)
tsol = sp.solve(sp.Eq(Rshort, Lt), t_)[0]
Rstar = sp.simplify(Lt.subs(t_, tsol))
J = (al - de_) * Dx + de_ * Px
Rstar_pr = 1 - de_ + (al - de_) * de_ * Px / (2 * J)
rec(S, "R_* from balancing source R_short(t)=L(t) equals PR (5.2)", sp.simplify(Rstar - Rstar_pr) == 0)
rec(S, "plain capacity at kappa=3/4: (1-2m)/(6 kappa) = 2(1-2m)/9",
    sp.simplify((1 - 2 * sp.Symbol('m')) / (6 * sp.Rational(3, 4)) - 2 * (1 - 2 * sp.Symbol('m')) / 9) == 0)
rec(S, "P_x = 2 - 26x/9 + 8x^2/9 (envelope note form) equals (2-8x/9)(1-x)",
    sp.expand(Px - (2 - sp.Rational(26, 9) * x_ + sp.Rational(8, 9) * x_ ** 2)) == 0)
# 1 - R_* = delta [ (alpha-delta)(2Dx - Px) + 2 delta Px ] / (2J) >= 0
one_minus = sp.simplify(1 - Rstar_pr - de_ * ((al - de_) * (2 * Dx - Px) + 2 * de_ * Px) / (2 * J))
rec(S, "identity 1-R_* = delta[(alpha-delta)(2Dx-Px)+2delta Px]/(2J), hence R_* <= 1 on 0<=delta<=5/6",
    one_minus == 0)
E_full = pr61.subs(R_, Rstar_pr)
dE = sp.diff(E_full, l_)
dE_pr = sp.Rational(5, 4) + de_ * (1 + x_) - sp.Rational(3, 2) * (1 - Rstar_pr)
rec(S, "PR Lemma 6.1 derivative: dE/d ell = 5/4 + delta(1+x) - (3/2)(1-R_*) at fixed b",
    sp.simplify(dE - dE_pr) == 0)
rec(S, "E is exactly affine in ell at fixed (delta,x,b) (second derivative 0)", sp.simplify(sp.diff(E_full, l_, 2)) == 0)
rec(S, "dE/d ell <= 5/4 + (5/6)(3/2) = 5/2 on the rectangle (since 1-R_* >= 0)",
    sp.Rational(5, 4) + sp.Rational(5, 6) * sp.Rational(3, 2) == sp.Rational(5, 2))
m_new = F(49, 440640) - F(5, 2) * s0
rec(S, "margin 49/440640 - (5/2)(1/40000) = 49/440640 - 1/16000 = 1073/22032000",
    m_new == F(1073, 22032000) and F(5, 2) * s0 == F(1, 16000), m_new)


# ---- exact branch-and-bound certificate (independent of the source's SOS identity (20.9)) ----
def poly_dict(expr):
    P = sp.Poly(sp.expand(expr), de_, x_)
    return {mon: fr(c) for mon, c in P.terms()}


def ev(pd, d, x):
    return sum(c * d ** i * x ** j for (i, j), c in pd.items())


def ival(pd, d0, d1, x0, x1):
    lo = hi = F(0)
    for (i, j), c in pd.items():
        mlo, mhi = d0 ** i * x0 ** j, d1 ** i * x1 ** j
        if c >= 0:
            lo += c * mlo; hi += c * mhi
        else:
            lo += c * mhi; hi += c * mlo
    return lo, hi


def deriv(pd, k):
    out = {}
    for (i, j), c in pd.items():
        e = (i, j)[k]
        if e:
            mon = (i - 1, j) if k == 0 else (i, j - 1)
            out[mon] = out.get(mon, F(0)) + c * e
    return out


def certify_nonneg(pd, box, max_boxes=400000):
    """Prove pd >= 0 on box (all coordinates >= 0) by exact interval arithmetic:
    natural extension combined with the mean-value form, adaptive bisection."""
    pdd, pdx = deriv(pd, 0), deriv(pd, 1)
    stack, done, n, worst = [box], 0, 0, None
    while stack:
        d0, d1, x0, x1 = stack.pop()
        n += 1
        if n > max_boxes:
            return False, n, "box budget exhausted"
        lo_nat = ival(pd, d0, d1, x0, x1)[0]
        cd, cx = (d0 + d1) / 2, (x0 + x1) / 2
        gd, gx = ival(pdd, d0, d1, x0, x1), ival(pdx, d0, d1, x0, x1)
        rd, rx = (d1 - d0) / 2, (x1 - x0) / 2
        lo_mv = ev(pd, cd, cx) - max(abs(gd[0]), abs(gd[1])) * rd - max(abs(gx[0]), abs(gx[1])) * rx
        lo = max(lo_nat, lo_mv)
        if lo >= 0:
            done += 1
            continue
        if ev(pd, cd, cx) < 0:
            return False, n, f"negative at ({cd},{cx})"
        if d1 - d0 >= x1 - x0:
            stack += [(d0, cd, x0, x1), (cd, d1, x0, x1)]
        else:
            stack += [(d0, d1, x0, cx), (d0, d1, cx, x1)]
    return True, n, f"{done} certified boxes"


def margin_poly(ell_val, b_val, m):
    """-2J (E + m) as a polynomial: nonnegative <=> E <= -m (J>0)."""
    Eh = pr61.subs({l_: sp.Rational(ell_val.numerator, ell_val.denominator),
                    b_: sp.Rational(b_val.numerator, b_val.denominator)})
    A = Eh.subs(R_, 1)                               # E with R=1
    hh = (1 + 3 * sp.Rational(ell_val.numerator, ell_val.denominator) + sp.Rational(1, 8)) / 2
    # E = A - h*delta + h (alpha-delta) delta Px/(2J)
    chk = sp.simplify(Eh.subs(R_, Rstar_pr) - (A - hh * de_ + hh * (al - de_) * de_ * Px / (2 * J)))
    if chk != 0:
        raise RuntimeError("E decomposition A - h delta + h(alpha-delta)delta Px/(2J) failed")
    return -2 * J * (A - hh * de_ + sp.Rational(m.numerator, m.denominator)) - hh * (al - de_) * de_ * Px


BOX = (F(0), F(5, 6), F(0), F(1, 2))
okJ = certify_nonneg(poly_dict(J - sp.Rational(1, 2)), BOX)
rec(S, "B&B: J >= 1/2 > 0 on [0,5/6]x[0,1/2] (true min 35/54 at the corner)", okJ[0], okJ[1:])
t0 = time.time()
ok_old = certify_nonneg(poly_dict(margin_poly(F(1, 6), b, F(49, 440640))), BOX)
rec(S, "B&B (independent of (20.9)): source Lemma 20.2, -E_old >= 49/440640 on [0,5/6]x[0,1/2]",
    ok_old[0], f"{ok_old[1:]} in {time.time()-t0:.1f}s")
t0 = time.time()
ok_new = certify_nonneg(poly_dict(margin_poly(ell, b, m_new)), BOX)
rec(S, "B&B DIRECT at perturbed geometry: -E_new >= 1073/22032000 on [0,5/6]x[0,1/2]",
    ok_new[0], f"{ok_new[1:]} in {time.time()-t0:.1f}s")
# a much stronger rational margin also certifies directly (shows how much slack the PR leaves)
m_strong = F(19, 100000)
ok_strong = certify_nonneg(poly_dict(margin_poly(ell, b, m_strong)), BOX)
rec(S, "B&B: in fact -E_new >= 19/100000 (about 4x the PR's stated margin)", ok_strong[0], ok_strong[1:])
# locate the true minimum (float, informative only)
try:
    import numpy as np
    from scipy.optimize import minimize
    fE = sp.lambdify((de_, x_), -E_full.subs({b_: sp.Rational(1, 8)}).subs(l_, sp.Rational(20003, 120000)), "numpy")
    fE0 = sp.lambdify((de_, x_), -E_full.subs({b_: sp.Rational(1, 8)}).subs(l_, sp.Rational(1, 6)), "numpy")
    best = {}
    for name, f in (("new", fE), ("old", fE0)):
        G = [(f(dd, xx), dd, xx) for dd in np.linspace(0, 5 / 6, 841) for xx in np.linspace(0, .5, 101)]
        v, dd, xx = min(G)
        r = minimize(lambda p: f(p[0], p[1]), [dd, xx], bounds=[(0, 5 / 6), (0, .5)], method="L-BFGS-B",
                     options=dict(ftol=1e-15, gtol=1e-13))
        best[name] = (float(r.fun), float(r.x[0]), float(r.x[1]))
    rec(S, "float location of min(-E): old geometry vs new geometry (informative)", True, best)
except Exception as exc:  # pragma: no cover
    rec(S, "float minimum location", False, exc)

# =============================================================================================
# 3. Other row ranges at the perturbed geometry, evaluated DIRECTLY (not via derivative bounds)
# =============================================================================================
S = "3 other ranges"


def E_at(d, delta, q, R, sig=beta0):
    a = (1 + delta) / 2
    return a - sig + h * (z0 - F(1, 6)) - a * ly - ell / 2 + q * ell + d * (R + delta / 2 - z0)


d0f = F(1, 50)
floor_new = E_at(h, d0f, d0f / 2, F(1))
rec(S, "floor bin (delta=1/50, R=1, q=delta/2) at d=h: exact value < 0 and >= PR bound -7/1200+(32/25)s0",
    floor_new < 0 and floor_new <= -F(7, 1200) + F(32, 25) * s0, f"{floor_new} = {float(floor_new):.6e}")
rec(S, "floor frequency slope R+delta0/2-z0 > 0", 1 + d0f / 2 - z0 > 0)
inter = [E_at(F(1, 2), dl, dl / 2, F(76, 75) - F(2, 3) * dl) for dl in (d0f, F(5, 6))]
rec(S, "intermediate rows d=1/2, R=76/75-2delta/3, q=delta/2: affine in delta, endpoints < 0",
    max(inter) < 0 and max(inter) <= -F(49, 14400) + F(177, 200) * s0, [f"{float(v):.6e}" for v in inter])
rec(S, "intermediate slope in d positive for delta<=5/6: 76/75-delta/6-17/50 > 0",
    F(76, 75) - F(5, 6) / 6 - z0 > 0)
dmin = F(1, 100)
small = h * (z0 - F(1, 6)) - ly / 2
rec(S, "small rows: h(z0-1/6)-ly/2 + 2 dmin < 0, and = -(63/800 - (51/100) s0) exactly",
    small + 2 * dmin < 0 and small + 2 * dmin == -(F(63, 800) - F(51, 100) * s0), f"{float(small+2*dmin):.6e}")
rec(S, "principal margins ly/20, h/600 > 0", ly / 20 > 0 and h / 600 > 0)
rec(S, "prime supply ell/h > 8/39 > 7/37 and 5ell - h = 1/48 + (7/2)s0",
    ell / h > F(8, 39) > F(7, 37) and 5 * ell - h == F(1, 48) + F(7, 2) * s0)
rec(S, "moderate frequency slope R_*+delta/2-z0 >= 33/50 - delta/2 > 0 for delta <= 5/6",
    F(33, 50) - F(5, 12) > 0)
rec(S, "bin ceiling delta <= 2*(7/8)-1 = 3/4 under the imported 7/8 theorem; kappa = 3/4 admissible "
       "(Lemma 18.1 hypothesis beta* <= (1+kappa)/2 = 7/8)", 2 * F(7, 8) - 1 == F(3, 4) and (1 + F(3, 4)) / 2 == F(7, 8))

# =============================================================================================
# 4. Enlarged principal Euler region alpha0 = 437/500 (Lemma 7.1-type exponents)
# =============================================================================================
S = "4 Euler domain"
A0 = F(437, 500)
wmin, zmin = F(19, 20), F(33, 200)
# good primes: H_p - 1 = [D(V+W-VW) - VW + (1-V)(1-W)E_p]/(1-D), |E_p| << Q^{4-6x-6z} + Q^{1-x-w-6z}
good = {"DV": -A0 - 6 * zmin, "DW": -A0 - wmin, "VW": -6 * zmin - wmin,
        "E_p first (R)": 4 - 6 * A0 - 6 * zmin, "E_p second": 1 - A0 - wmin - 6 * zmin}
rec(S, "good-prime exponents match PR list and max = -907/500 (< -1: summable)",
    max(good.values()) == F(-907, 500) and max(good.values()) < -1
    and sorted(good.values()) == sorted([-A0 - F(99, 100), -A0 - F(19, 20), F(-97, 50), F(301, 100) - 6 * A0, -A0 - F(47, 50)]),
    {k: str(v) for k, v in good.items()})
# ramified p | u: D = W = 0, defect (1-V) P_p^*, terms from (7.11) J_1..J_5, R, strict second family
ram = {"R": 6 * A0 + 6 * zmin - 4, "strict 2nd family (Q-1)Q^{-x-w}": A0 + wmin - 1,
       "J1 Q^{-x-w}": A0 + wmin, "J2 Q^{3/2-3x}": 3 * A0 - F(3, 2), "J3a Q^{2-3x-w}": 3 * A0 + wmin - 2,
       "J3b Q^{2-4x}": 4 * A0 - 2, "J4 Q^{5/2-4x-w}": 4 * A0 + wmin - F(5, 2), "J5 Q^{3-6x}": 6 * A0 - 3}
pr_ram = [6 * A0 - F(301, 100), A0 - F(1, 20), A0 + F(19, 20), 3 * A0 - F(3, 2), 3 * A0 - F(21, 20),
          4 * A0 - 2, 4 * A0 - F(31, 20), 6 * A0 - 3]
rec(S, "ramified decay exponents match PR list; min = 103/125 > 0",
    sorted(ram.values()) == sorted(pr_ram) and min(ram.values()) == F(103, 125), {k: str(v) for k, v in ram.items()})
rec(S, "|R| <= Q^{301/100-6alpha0} < Q^{-1}", F(301, 100) - 6 * A0 < -1, F(301, 100) - 6 * A0)
rec(S, "principal tail sum over Np>P0 of Q^{-907/500} is O(P0^{-407/500})", 1 - F(907, 500) == F(-407, 500))
sel = {"Q^-x": A0, "Q^-6z": 6 * zmin, "Q^{4-5x-6z}": 5 * A0 + 6 * zmin - 4, "Q^{1-w-6z}": wmin + 6 * zmin - 1}
rec(S, "selected principal error decays (alpha0, 99/100, 5alpha0-301/100, 47/50): min = 437/500",
    min(sel.values()) == A0 and sel["Q^{4-5x-6z}"] == 5 * A0 - F(301, 100) and sel["Q^{1-w-6z}"] == F(47, 50),
    {k: str(v) for k, v in sel.items()})
rec(S, "reproduces source at alpha=7/8: good -363/200, ramified 33/40",
    max([-F(7, 8) - F(99, 100), -F(7, 8) - F(19, 20), F(-97, 50), F(301, 100) - F(21, 4), -F(7, 8) - F(47, 50)]) == F(-363, 200)
    and min([F(21, 4) - F(301, 100), F(7, 8) - F(1, 20), F(7, 8) + F(19, 20), F(21, 8) - F(3, 2), F(21, 8) - F(21, 20),
             F(7, 2) - 2, F(7, 2) - F(31, 20), F(21, 4) - 3]) == F(33, 40))
rec(S, "alpha0 = 437/500 < beta0 (gap 1/1000 - 1/160000 = 159/160000)",
    A0 < beta0 and beta0 - A0 == F(159, 160000), beta0 - A0)
rec(S, "small-row lines (beta*+e, 1/2, 17/50) lie in D1(1/3): beta0 > 5/6", beta0 > F(5, 6))
sm_good = [-A0, -F(51, 25), F(49, 25) - 5 * A0, -F(77, 50)]
sm_ram = [-F(1, 2), F(3, 2) - 2 * A0, 2 - 3 * A0, 3 - 5 * A0]
rec(S, "small-row selected exponents at Re s >= alpha0: good all < 0, ramified (after Q^{Re s}) all <= 1/2",
    all(v < 0 for v in sm_good) and all(v <= F(1, 2) for v in sm_ram))
mu = F(437, 1000) * ell  # / K, K >= 1
rec(S, "mu = (437/1000) ell/K satisfies 0 < mu < (437/500) min ell_i", 0 < mu < F(437, 500) * ell)
# a uniformly larger domain for the same exponent families (TAIL_AND_EULER Lemma 2.1 claims alpha > 401/600)
al_s = sp.symbols("alpha", positive=True)
lam = sp.Min(6 * al_s - sp.Rational(401, 100), al_s - sp.Rational(3, 50))
rec(S, "good-prime excess decay min(6a-401/100, a-3/50) vanishes exactly at a = 401/600",
    sp.solve(sp.Eq(6 * al_s - sp.Rational(401, 100), 0), al_s) == [sp.Rational(401, 600)])

# =============================================================================================
# 5. Exact envelope limit (GEOMETRY_ENVELOPE_LIMIT.md)
# =============================================================================================
S = "5 envelope"
Rh = Rstar_pr.subs(x_, sp.Rational(1, 2))
num = sp.factor(sp.together(Rh - sp.Rational(2, 3)))
rec(S, "R_*(delta,1/2) - 2/3 = (288 delta^2 - 588 delta + 185)/(3(185-138 delta))",
    sp.simplify(Rh - sp.Rational(2, 3) - (288 * de_ ** 2 - 588 * de_ + 185) / (3 * (185 - 138 * de_))) == 0, num)
roots = sp.solve(288 * de_ ** 2 - 588 * de_ + 185, de_)
dlt0 = (49 - sp.sqrt(921)) / 48
rec(S, "smaller root delta0 = (49 - sqrt 921)/48 ~ 0.3885789, inside (3/8, 19/48), other root > 5/6",
    any(sp.simplify(r - dlt0) == 0 for r in roots) and sp.Rational(3, 8) < dlt0 < sp.Rational(19, 48)
    and max(roots) > sp.Rational(5, 6), [sp.N(r, 12) for r in roots])
rec(S, "dE/db = (R_* - 2/3)/2, so b cancels exactly where R_* = 2/3",
    sp.simplify(sp.diff(pr61, b_) - (R_ - sp.Rational(2, 3)) / 2) == 0)
E_corner = sp.expand(pr61.subs({x_: sp.Rational(1, 2), R_: sp.Rational(2, 3)}))
rec(S, "E at R_*=2/3, x=1/2: -5/12 + delta/2 + ell(3/4 + 3 delta/2) (b-free)",
    sp.simplify(E_corner - (-sp.Rational(5, 12) + de_ / 2 + l_ * (sp.Rational(3, 4) + 3 * de_ / 2))) == 0)
ell_star = sp.radsimp((sp.Rational(5, 12) - dlt0 / 2) / (sp.Rational(3, 4) + 3 * dlt0 / 2))
beta_star = sp.radsimp(sp.Rational(11, 12) - ell_star / 4)
rec(S, "ell* = (8 sqrt 921 + 33)/1653 and beta_limit = (1507 - 2 sqrt 921)/1653",
    sp.simplify(ell_star - (8 * sp.sqrt(921) + 33) / 1653) == 0
    and sp.simplify(beta_star - (1507 - 2 * sp.sqrt(921)) / 1653) == 0, f"{sp.N(beta_star, 15)}")
# exact rational enclosure of sqrt(921) (integer square root), hence of the limit, without floats
from math import isqrt
SC = 10 ** 20
r_lo = F(isqrt(921 * SC * SC), SC)
r_hi = r_lo + F(1, SC)
if not (r_lo * r_lo < 921 < r_hi * r_hi):
    raise RuntimeError("sqrt enclosure")
lim_lo, lim_hi = (1507 - 2 * r_hi) / 1653, (1507 - 2 * r_lo) / 1653
rec(S, "exact enclosure: 0.8749570697 < (1507-2sqrt921)/1653 < 0.8749570698, and beta0 = 0.87499375 lies above it "
       "(gap 3.668e-5)",
    F(8749570697, 10 ** 10) < lim_lo < lim_hi < F(8749570698, 10 ** 10) and lim_hi < beta0,
    f"[{float(lim_lo):.12f}, {float(lim_hi):.12f}]; beta0-limit ~ {float(beta0-lim_hi):.6e}")
rec(S, "PR's displayed decimal '0.874957067...' (ENVELOPE_LIMIT.md:110, README.md:90, REVIEW.md:101) is a "
       "correct truncation of the exact limit",
    F(874957067, 10 ** 9) <= lim_lo and lim_hi < F(874957068, 10 ** 9),
    f"exact value lies in [{float(lim_lo):.12f}, {float(lim_hi):.12f}]: correct truncation is 0.874957069...; "
    f"PR checker bracket (0.87495706, 0.87495708) is too coarse to see this", finding=True)
# Is x=1/2 the best point on the b-free curve R_*=2/3?  ell_thr(x) = (5/12 - delta_x/2)/(3/4 + delta_x(1+x))
xs, thr = [], []
import math
for k in range(0, 51):
    xv = sp.Rational(k, 100)
    eq = sp.together(Rstar_pr.subs(x_, xv) - sp.Rational(2, 3))
    rts = [r for r in sp.solve(sp.numer(eq), de_) if r.is_real and 0 <= r <= sp.Rational(5, 6)]
    for r in rts:
        lt = (sp.Rational(5, 12) - r / 2) / (sp.Rational(3, 4) + r * (1 + xv))
        xs.append(float(xv)); thr.append(float(lt))
imin = min(range(len(thr)), key=lambda i: thr[i])
rec(S, "on the b-free curve R_*=2/3 the ell-threshold is smallest at x = 1/2 (scan x=0..1/2 step 1/100)",
    xs[imin] == 0.5, f"min ell_thr = {thr[imin]:.9f} at x={xs[imin]}; at x=0: {thr[0]:.6f}")

# Tightness (beyond the PR's claim): is the necessary condition also sufficient for the d=h envelope?
import numpy as np
fEgen = sp.lambdify((de_, x_, l_, b_), pr61.subs(R_, Rstar_pr), "numpy")
ls = float(ell_star)
DD, XX = np.meshgrid(np.linspace(0, 0.75, 1501), np.linspace(0, 0.5, 201))


def supE(lv, bv):
    return float(np.max(fEgen(DD, XX, lv, bv)))


bgrid = np.linspace(0.05, 0.17, 241)
sups = [supE(ls, bv) for bv in bgrid]
ib = int(np.argmin(sups))
rec(S, "tightness probe: at ell = ell*, min_b sup_{delta<=3/4,x} E is ~0 (b-window where the corner binds)",
    abs(sups[ib]) < 2e-6, f"min_b supE = {sups[ib]:.3e} at b = {bgrid[ib]:.4f}; "
    f"supE(ell*-1e-5, b) = {supE(ls-1e-5, bgrid[ib]):.3e}")

# Compare with our optimiser (results/A, B): back out the slack
res = {}
for nm in ("A_paper_bp11_12", "B_paper_bp7_8"):
    with open(os.path.join(HERE, "..", "results", nm + ".json")) as fh:
        res[nm] = json.load(fh)
for nm, r in res.items():
    dl, xv, dd, Rv = eval(r["arg"].replace("np.float64", ""))
    slope = 5 / 4 + 1.5 * dl - 1.5 * (1 - Rv)      # dE/d ell at the binding point (x = 1/2)
    beta_pred = r["sigma0"] - (-r["high_sup"]) / slope / 4
    res[nm]["slack_corrected_sigma0"] = beta_pred
rec(S, "our optimiser optimum (0.8749602 / 0.8749610 with 2e-5 slack) corrected for its slack lands on "
       "(1507-2sqrt921)/1653 to < 2e-7",
    all(abs(r["slack_corrected_sigma0"] - float(beta_star)) < 2e-7 for r in res.values()),
    {k: f"{v['sigma0']:.8f} -> {v['slack_corrected_sigma0']:.8f}" for k, v in res.items()})

# =============================================================================================
# 6. Our own exponent model at the PR geometry (FLOATING_RECONNAISSANCE)
# =============================================================================================
S = "6 model"
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import threshold_calculus as tc  # noqa: E402
lo_model = tc.low_threshold(float(lx), float(ly), float(ell), nd=4001)
rec(S, "model low_threshold at PR geometry = 0.87499375", abs(lo_model - float(beta0)) < 1e-12, lo_model)
t0 = time.time()
hs11 = tc.high_sup(float(lx), float(ly), float(ell), lo_model, 11 / 12, nde=401, nx=51, nd=41)
t1 = time.time()
hs78 = tc.high_sup(float(lx), float(ly), float(ell), lo_model, 7 / 8, nde=401, nx=51, nd=41)
t2 = time.time()
hs_src = tc.high_sup(17 / 48, 23 / 48, 1 / 6, 0.875, 11 / 12, nde=401, nx=51, nd=41)
rec(S, "model sup F at PR geometry, beta_prev=11/12 (nde=401,nx=51,nd=41) < -1073/22032000",
    hs11[0] < -float(m_new), f"{hs11[0]:.6e} at {hs11[1]} ({t1-t0:.0f}s)")
rec(S, "model sup F at PR geometry, beta_prev=7/8 (the PR's bootstrap setting, delta<=3/4)",
    hs78[0] < -float(m_new), f"{hs78[0]:.6e} at {hs78[1]} ({t2-t1:.0f}s)")
rec(S, "model sup F at source geometry (reference; expect ~ -2.28e-4)", hs_src[0] < 0, f"{hs_src[0]:.6e} at {hs_src[1]}")
rec(S, "shift in sup F from source to PR geometry ~ s0 * dE/dell at binding point (~1.333 s0 = 3.3e-5)",
    abs((hs11[0] - hs_src[0]) - 1.3333 * float(s0)) < 5e-6, f"{hs11[0]-hs_src[0]:.4e} vs {1.3333*float(s0):.4e}")

# =============================================================================================
summary = {"reviewed_sha": "670a76c1a3a8f325c43c1755b1cfc24d313a3e3c",
           "n_checks": len(OUT), "n_pass": sum(r["pass"] for r in OUT),
           "n_documented_findings": sum((not r["pass"]) and r["documented_finding"] for r in OUT),
           "n_unexpected_fail": sum((not r["pass"]) and not r["documented_finding"] for r in OUT),
           "arithmetic": "EXACT_RATIONAL + sympy exact (Q(sqrt 921)); float only in section 6 and minimum location",
           "checks": OUT}
with open(os.path.join(HERE, "pr910_replay_output.json"), "w") as fh:
    json.dump(summary, fh, indent=1)
print(f"\n{summary['n_pass']}/{summary['n_checks']} checks passed; "
      f"{summary['n_documented_findings']} documented finding(s); {summary['n_unexpected_fail']} unexpected failure(s)")
sys.exit(0 if summary["n_unexpected_fail"] == 0 else 1)
