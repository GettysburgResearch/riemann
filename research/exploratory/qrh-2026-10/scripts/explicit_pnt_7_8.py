#!/usr/bin/env python3
"""Explicit prime-number-theorem consequences of the zero-free half-plane Re s > 7/8.

Companion to ../EXPLICIT_PNT_7_8.md.  Run from any directory:

    python3 -I explicit_pnt_7_8.py            # main run, writes ../results/explicit_pnt_7_8.{txt,json}
    python3 -I explicit_pnt_7_8.py --zeros    # adds an EMPIRICAL float sanity check with mpmath.zetazero

Arithmetic classes
------------------
* Every constant that the note CLAIMS is computed with mpmath interval arithmetic (mpmath.iv,
  outward rounding, 128-bit working precision).  Inputs from the literature are entered as
  decimal strings, which mpmath.iv encloses exactly.  Only upper endpoints of enclosures are used
  for upper bounds and only lower endpoints for lower bounds.
* Monotonicity facts used to pass from finitely many evaluations to all x are proved in the note
  (each is an elementary calculus fact about functions such as x^(-3/8) log x); the script only
  evaluates at the points the note specifies, or on cells, where naive interval evaluation over
  the whole cell is itself a rigorous enclosure.
* Crossover estimates against published unconditional tables and the --zeros check use the same
  interval routines for our bound, but the published table values are transcribed decimals, and
  the --zeros check uses ordinary floating point.  Those parts are labelled EMPIRICAL/COMPARISON.

Imported inputs (see the note for exact statements):
  H0  = 3e12                                  Platt-Trudgian, arXiv:2004.09765v1, Thm 1
  N(T) bound 0.1038 log T + 0.2573 loglog T + 9.3675, T >= e
                                              Hasanalizade-Shen-Wong, arXiv:2107.06506v1, Cor 1.2
  truncated explicit formula, error M x log x / T, M = 6.431, log x >= 40, alpha = 1/2,
     max{51, log x} < T < (x^(1/2) - 2)/2      Cully-Hugill-Johnston, arXiv:2111.10001v5,
                                              Thm 1.2 with Table 4
  |psi(x)-x|, |theta(x)-x|, |pi(x)-li(x)| <= sqrt(x) log^2 x/(8 pi) on the stated ranges up to
     2.169e25                                 Platt-Trudgian, arXiv:2004.09765v1, Cor 1
  sum_rho 1/(rho(1-rho)) = 2 + gamma - log(4 pi)
                                              Nicolas, arXiv:1202.0729v2, eq. (1.3)
  Lemma 2.1 (N2) of Nicolas, arXiv:1202.0729v2 (used only in the note, not numerically here)
  first zero ordinate > 14 (classical)
  H(7/8): zeta(s) != 0 for Re s > 7/8         Lean theorem OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
"""

import json
import os
import sys

from mpmath import iv, mp

iv.prec = 128
mp.prec = 128
I = iv.mpf
PI = iv.pi
EG = iv.euler
LOG2 = iv.log(I(2))
LOG4 = iv.log(I(4))

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "..", "results")

OUT = []


def say(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s)


def up(x):
    """upper endpoint as an ordinary mpf (exact, no rounding)"""
    if isinstance(x, (int, float)) or not hasattr(x, "_mpi_"):
        return mp.mpf(x)
    return mp.make_mpf(x._mpi_[1])


def lo(x):
    """lower endpoint as an ordinary mpf (exact, no rounding)"""
    if isinstance(x, (int, float)) or not hasattr(x, "_mpi_"):
        return mp.mpf(x)
    return mp.make_mpf(x._mpi_[0])


def fmt(x, n=6):
    """upper endpoint, printed with n significant digits (rounded up in the last digit is NOT
    attempted; printed values are for reading; the claimed constants are compared as mpf)."""
    return mp.nstr(up(x), n)


# ---------------------------------------------------------------------------------------------
# Imported constants (decimal strings, enclosed exactly)
# ---------------------------------------------------------------------------------------------
H0 = I(3) * I(10) ** 12                  # Platt-Trudgian Thm 1 (they reach 3 000 175 332 800)
M_CHJ = I("6.431")                       # Cully-Hugill-Johnston Table 4, log x_M = 40, alpha = 1/2
LOG_XM = 40                              # log x_M
HSW1, HSW2, HSW3 = I("0.1038"), I("0.2573"), I("9.3675")   # HSW Cor 1.2
XP = I("2.169e25")                       # Platt-Trudgian Cor 1 upper end
LXP = iv.log(XP)
GAMMA1_LOWER = I(14)                     # no zero with 0 < gamma <= 14 (classical)
SUM_INV_RHO_1MRHO = 2 + EG - iv.log(4 * PI)   # Nicolas (1.3): sum 1/(rho(1-rho))

A_HAT = iv.log(H0 / (2 * PI))            # a = log(H0/2pi)


# ---------------------------------------------------------------------------------------------
# Zero sums from the N(T) bound by partial summation (Sec. 2 of the note)
# ---------------------------------------------------------------------------------------------
def Q(t):
    """HSW error envelope Q(t) = 0.1038 log t + 0.2573 log log t + 9.3675, t >= e."""
    lt = iv.log(t)
    return HSW1 * lt + HSW2 * iv.log(lt) + HSW3


def intQ2(a):
    """Upper bound for int_a^oo Q(t)/t^2 dt (a >= e)."""
    la = iv.log(a)
    return HSW1 * (la + 1) / a + HSW2 * (iv.log(la) + 1 / la) / a + HSW3 / a


def intQ3(a):
    """Upper bound for int_a^oo Q(t)/t^3 dt (a >= e)."""
    la = iv.log(a)
    return (HSW1 * (2 * la + 1) / (4 * a ** 2) + HSW2 * (iv.log(la) + 1 / (2 * la)) / (2 * a ** 2)
            + HSW3 / (2 * a ** 2))


def Z1(T):
    """Upper bound for sum_{0<gamma<=T} 1/gamma (T >= 14)."""
    l = iv.log(T / (2 * PI))
    l14 = iv.log(GAMMA1_LOWER / (2 * PI))
    return (l ** 2 / (4 * PI) - 1 / (2 * PI) - l14 ** 2 / (4 * PI) + l14 / (2 * PI)
            + Q(T) / T + intQ2(GAMMA1_LOWER))


def Z2(T):
    """Upper bound for sum_{H0<gamma<=T} 1/gamma (T >= H0)."""
    l = iv.log(T / (2 * PI))
    return (l ** 2 - A_HAT ** 2) / (4 * PI) + Q(T) / T + Q(H0) / H0 + intQ2(H0)


def EPS_BAR():
    """eps_bar >= Q(T)/T + Q(H0)/H0 + int_{H0}^oo Q/t^2 for every T >= H0."""
    return 2 * Q(H0) / H0 + intQ2(H0)


def S_HIGH():
    """Upper bound for sum_{|gamma|>H0} 1/gamma^2."""
    return 2 * ((A_HAT + 1) / (2 * PI * H0) + Q(H0) / H0 ** 2 + 2 * intQ3(H0))


S_LOW = SUM_INV_RHO_1MRHO   # >= sum_{|gamma|<=H0} 1/|rho|^2 (Sec. 2)


# ---------------------------------------------------------------------------------------------
# Theorem 1: psi bound.  A_eff(L) = B(x) / (x^(7/8) L^2) with L = log x, by regime.
# ---------------------------------------------------------------------------------------------
L_A = 2 * iv.log(4 * H0)                 # regime I/II boundary: x^(1/2)/4 = H0
L_B_MIN = 8 * iv.log(H0 / (8 * PI * M_CHJ))  # regime III needs T = 8 pi M x^(1/8) >= H0
L_B = I(190)
C1_HAT = iv.log(4 * M_CHJ)               # log(T/2pi) - L/8 in regime III


def aeff_I(L):
    """Regime I (40 <= L <= L_A): T = e^(L/2)/4, all zeros used lie on the line."""
    T = iv.exp(L / 2) / 4
    return 2 * Z1(T) * iv.exp(-3 * L / 8) / L ** 2 + 4 * M_CHJ * iv.exp(-3 * L / 8) / L


def aeff_II(L):
    """Regime II (L_A <= L <= L_B): T = H0."""
    return 2 * Z1(H0) * iv.exp(-3 * L / 8) / L ** 2 + M_CHJ * iv.exp(L / 8) / (H0 * L)


def aeff_III(L):
    """Regime III (L >= L_B): T = 8 pi M e^(L/8)."""
    T = 8 * PI * M_CHJ * iv.exp(L / 8)
    return (2 * Z1(H0) * iv.exp(-3 * L / 8) / L ** 2 + 2 * Z2(T) / L ** 2 + 1 / (8 * PI * L))


def regime_III_coeffs():
    b = (C1_HAT + 1) / (8 * PI)
    d = (A_HAT ** 2 - C1_HAT ** 2) / (2 * PI) - 2 * EPS_BAR()
    return b, d


def aeff_III_sup(L0):
    """Rigorous sup over L >= L0 (L0 >= L_B) of the regime-III bound:
    A_eff(L) <= 1/(128 pi) + b/L - d/L^2 + 2 Z1(H0) e^{-3L/8}/L^2."""
    b, d = regime_III_coeffs()
    Lstar = 2 * d / b
    if lo(Lstar) >= up(L0):
        # max of b/L - d/L^2 is b^2/(4d); enclose with outward rounding from the safe endpoints
        hmax = I(up(b)) ** 2 / (4 * I(lo(d)))
    else:
        hmax = b / L0 - d / L0 ** 2
    expo = 2 * Z1(H0) * iv.exp(-3 * L0 / 8) / L0 ** 2
    return 1 / (128 * PI) + hmax + expo, Lstar


def cells(a, b, w):
    """Cover [a,b] (mpf endpoints) by closed cells of width <= w."""
    out = []
    x = mp.mpf(a)
    b = mp.mpf(b)
    while x < b:
        y = min(x + w, b)
        out.append(I([x, y]))
        x = y
    return out


def aeff_on_cell(c):
    """Upper bound of A_eff over the L-cell c.  Cell assignment: [40, lo(L_A)] -> regime I
    (T = x^(1/2)/4 <= H0 there); [lo(L_A), 190] -> regime II (T = H0, admissible for
    L >= 2 log(2 H0 + 2) ~ 58.85); [190, oo) -> regime III."""
    if up(c) <= lo(L_A):
        return aeff_I(c)
    if lo(c) >= lo(L_A) and up(c) <= lo(L_B):
        return aeff_II(c)
    if lo(c) >= up(L_B):
        return aeff_III(c)
    raise ValueError("cell straddles a regime boundary")


def psi_theta_extra(L):
    """(psi - theta)(x) / (x^(7/8) L^2) <= log 4 (x^(1/2) + x^(1/3) L / log 2)/(x^(7/8) L^2)."""
    return LOG4 * (iv.exp(-3 * L / 8) + iv.exp(-13 * L / 24) * L / LOG2) / L ** 2


def regime_cells(La, Lb, w=mp.mpf("0.25")):
    """Cells covering [La, Lb], split at lo(L_A) and 190 (the regime boundaries)."""
    pts = [mp.mpf(La)]
    for bd in (lo(L_A), lo(L_B)):
        if pts[-1] < bd < mp.mpf(Lb):
            pts.append(bd)
    pts.append(mp.mpf(Lb))
    out = []
    for i in range(len(pts) - 1):
        out += cells(pts[i], pts[i + 1], w)
    return out


def aeff_cell_safe(c):
    return aeff_on_cell(c)


def psi_constant():
    """Rigorous sup of A_eff over L >= 40, split by regime; also sup over L >= L0 for a table."""
    s_I = mp.mpf(0)
    for c in cells(LOG_XM, lo(L_A), mp.mpf("0.25")):
        s_I = max(s_I, up(aeff_I(c)))
    s_II = mp.mpf(0)
    for c in cells(lo(L_A), lo(L_B), mp.mpf("0.25")):
        s_II = max(s_II, up(aeff_II(c)))
    s_III, Lstar = aeff_III_sup(L_B)
    return s_I, s_II, up(s_III), Lstar


# ---------------------------------------------------------------------------------------------
# small-x checks by exact enumeration (interval logs)
# ---------------------------------------------------------------------------------------------
def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = bytearray(len(s[p * p::p]))
    return [i for i in range(n + 1) if s[i]]


def small_x_threshold(A, which, nmax):
    """Least integer n0 >= 2 such that for every integer n in [n0, nmax] and every real x in
    [n, n+1):  |F(x) - x| <= A x^(7/8) log^2 x, where F = psi or theta (step function constant
    on [n, n+1)).  Since the right side increases in x, it suffices that
    max(|F(n)-n|, |F(n)-(n+1)|) <= A n^(7/8) log^2 n."""
    ps = primes_upto(nmax + 1)
    lp = {p: iv.log(I(p)) for p in ps}
    val = I(0)
    ok = {}
    pp = {}
    for p in ps:
        if which == "theta":
            pp[p] = lp[p]
        else:
            q = p
            while q <= nmax + 1:
                pp[q] = pp.get(q, I(0)) + lp[p]
                q *= p
    for n in range(2, nmax + 1):
        if n in pp:
            val = val + pp[n]
        lhs = max(up(abs(val - n)), up(abs(val - (n + 1))))
        rhs = lo(A * I(n) ** (I(7) / 8) * iv.log(I(n)) ** 2)
        ok[n] = lhs <= rhs
    n0 = nmax
    while n0 > 2 and ok[n0 - 1]:
        n0 -= 1
    return n0 if ok[nmax] else None


def pt_threshold(A):
    """Least x (as a bound) with sqrt(x) log^2 x/(8 pi) <= A x^(7/8) log^2 x, i.e.
    x >= (8 pi A)^(-8/3)."""
    return (8 * PI * A) ** (-I(8) / 3)


# ---------------------------------------------------------------------------------------------
# Robin / Nicolas bookkeeping (Sec. 5 of the note)
# ---------------------------------------------------------------------------------------------
def Jtail_scaled(L):
    """x^(1/8) L * Jtail(x), Jtail = bound for |J(x)| from the CHJ formula (x >= e^40)."""
    e38 = iv.exp(-3 * L / 8)
    return (S_LOW * e38 * (1 + (1 + 4 / L) / L) + S_HIGH() * (1 + (1 + 16 / L) / L)
            + 8 * M_CHJ * e38 * L * (1 + 1 / L))


def J0_scaled(L):
    """x^(1/8) L * J0bound(x), J0 = int (psi - theta) w."""
    return LOG4 * (2 * iv.exp(-3 * L / 8) * (1 + 1 / L)
                   + 3 / (2 * LOG2) * iv.exp(-13 * L / 24) * L * (1 + 1 / L))


def Ta_scaled(L):
    """x^(1/8) L * (1/4pi) x^(-1/2)(L + 3): the Platt-Trudgian part of J on [x, XP]."""
    return iv.exp(-3 * L / 8) * L * (L + 3) / (4 * PI)


def Te_scaled(L):
    """x^(1/8) L * S(x)^2/(x^2 L) with |S| <= sqrt(x) L^2/(8pi) (599 < x <= XP)."""
    return iv.exp(-7 * L / 8) * L ** 4 / (64 * PI ** 2)


def half_scaled(L, x1):
    """x^(1/8) L / (2(x-1)) <= x^(-7/8) L * x1/(2(x1-1)) for x >= x1."""
    return iv.exp(-7 * L / 8) * L * x1 / (2 * (x1 - 1))


_CELL_TABLE = []


def _cell_table():
    """(cell, A_eff upper + (psi-theta) extra) on cells covering [log XP, 400]."""
    if not _CELL_TABLE:
        for c in regime_cells(lo(LXP), 400):
            ae = up(aeff_cell_safe(c) + psi_theta_extra(c))
            _CELL_TABLE.append((c, ae))
    return _CELL_TABLE


def big_S2_sup(Lfrom):
    """sup over x >= max(e^Lfrom, XP) of S(x)^2 x^(-15/8) (= x^(1/8) log x * S^2/(x^2 log x)),
    with |S| <= B(x) + (psi - theta)(x).  Cells up to log x = 400 (every cell meeting
    [Lfrom, 400] is used), then the tail, where (A + extra)^2 L^4 e^{-L/8} decreases (L > 32)."""
    best = mp.mpf(0)
    for c, ae in _cell_table():
        if up(c) >= mp.mpf(Lfrom):
            best = max(best, up(I(ae) ** 2 * c ** 4 * iv.exp(-c / 8)))
    s3, _ = aeff_III_sup(I(400))
    tail = (s3 + psi_theta_extra(I(400))) ** 2 * I(400) ** 4 * iv.exp(-I(400) / 8)
    return max(best, up(tail))


def big_eta_sup(Lfrom):
    """sup over x >= max(e^Lfrom, XP) of |theta(x) - x|/x <= (A_eff + extra) L^2 e^{-L/8}."""
    best = mp.mpf(0)
    for c, ae in _cell_table():
        if up(c) >= mp.mpf(Lfrom):
            best = max(best, up(I(ae) * c ** 2 * iv.exp(-c / 8)))
    s3, _ = aeff_III_sup(I(400))
    tail = (s3 + psi_theta_extra(I(400))) * I(400) ** 2 * iv.exp(-I(400) / 8)
    return max(best, up(tail))


_S2_CACHE = {}
_ETA_CACHE = {}


def robin_cU(L1):
    """Return (cU_up, cU_two) rigorous: for all x >= e^L1 (L1 >= log 600):
      upper side  -K + S^2/(x^2 log x) <= cU_up x^(-1/8)/log x
      two-sided   |log(f_phi(N_k)/e^gamma)| <= cU_two p^(-1/8)/log p at p = x prime.
    """
    L1 = I(L1)
    x1 = iv.exp(L1)
    key = mp.nstr(lo(L1), 30)
    if up(L1) < lo(LXP):
        # x in [x1, XP]: decreasing pieces at x1, plus J(XP) scaled at XP
        T_b = Jtail_scaled(LXP)
        dec_up = Ta_scaled(L1) + J0_scaled(L1) + Te_scaled(L1)
        dec_two = Ta_scaled(L1) + iv.mpf(max(up(J0_scaled(L1) + Te_scaled(L1)),
                                             up(half_scaled(L1, x1))))
        part1_up = up(dec_up + T_b)
        part1_two = up(dec_two + T_b)
        # x >= XP
        if "XP" not in _S2_CACHE:
            _S2_CACHE["XP"] = big_S2_sup(up(LXP))
        s2 = _S2_CACHE["XP"]
        part2_up = up(Jtail_scaled(LXP) + J0_scaled(LXP) + I(s2))
        part2_two = up(Jtail_scaled(LXP) + I(max(up(J0_scaled(LXP) + I(s2)),
                                                 up(half_scaled(LXP, x1)))))
        return max(part1_up, part2_up), max(part1_two, part2_two)
    else:
        s2 = big_S2_sup(lo(L1))
        cu = up(Jtail_scaled(L1) + J0_scaled(L1) + I(s2))
        ct = up(Jtail_scaled(L1) + I(max(up(J0_scaled(L1) + I(s2)), up(half_scaled(L1, x1)))))
        return cu, ct


def robin_eta(L1):
    """sup_{x >= e^L1} (theta(x) - x)/x, rigorous upper bound."""
    L1 = I(L1)
    if up(L1) < lo(LXP):
        pt = up(L1 ** 2 * iv.exp(-L1 / 2) / (8 * PI))     # decreasing for L > 4
        if "XP" not in _ETA_CACHE:
            _ETA_CACHE["XP"] = big_eta_sup(up(LXP))
        return max(pt, _ETA_CACHE["XP"])
    return big_eta_sup(lo(L1))


def robin_c_needed(L1):
    cu, ct = robin_cU(L1)
    eta = I(robin_eta(L1))
    L1i = I(L1)
    umax = I(cu) * iv.exp(-L1i / 8) / L1i
    fac = iv.exp(umax) * (1 + eta) ** (I(1) / 8) * (1 + iv.log(1 + eta) / L1i)
    return up(I(cu) * fac), cu, ct, up(eta)


def theta_at_next_prime(x1):
    """theta(p) for p the least prime >= x1 (x1 integer-valued mpf, small), as an interval."""
    n = int(mp.ceil(x1))
    N = n + 2000
    ps = primes_upto(N)
    p_next = next(p for p in ps if p >= n)
    th = I(0)
    for p in ps:
        if p > p_next:
            break
        th = th + iv.log(I(p))
    return p_next, th


def sensitivity():
    """Recompute the Theorem-1 supremum with M replaced by 2M and 4M (rigorous for those M)."""
    global M_CHJ, C1_HAT, L_B_MIN
    M_save, C1_save, LBm_save = M_CHJ, C1_HAT, L_B_MIN
    sens = []
    try:
        for fac in ("2", "4"):
            M_CHJ = M_save * I(fac)
            C1_HAT = iv.log(4 * M_CHJ)
            L_B_MIN = 8 * iv.log(H0 / (8 * PI * M_CHJ))
            assert up(L_B_MIN) <= lo(L_B)
            sI, sII, sIII, _ = psi_constant()
            sens.append((fac, float(max(sI, sII, sIII))))
            say("   sensitivity: with M multiplied by", fac, "the sup over x >= e^40 becomes <=",
                mp.nstr(max(sI, sII, sIII), 6))
    finally:
        M_CHJ, C1_HAT, L_B_MIN = M_save, C1_save, LBm_save
    return sens


# ---------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------
def main():
    res = {}
    say("=" * 96)
    say("explicit_pnt_7_8.py: explicit consequences of H(7/8) + RH to H0 (mpmath.iv, prec 128)")
    say("=" * 96)

    # ---- sanity checks of identities (sympy, exact symbolic) ----------------------------------
    try:
        import sympy as sp
        t, x, z = sp.symbols("t x z", positive=True)
        zz = sp.Symbol("zz")
        g = t ** (zz - 1) / ((1 - zz) * sp.log(t))
        integrand = t ** (zz - 2) * (1 / sp.log(t) + 1 / sp.log(t) ** 2)
        lhs = -sp.diff(g, t) + (-zz * t ** (zz - 2) / ((1 - zz) * sp.log(t) ** 2))
        ok1 = sp.simplify(lhs - integrand) == 0
        h = t ** (zz - 1) / ((zz - 1) * sp.log(t) ** 2)
        ok2 = sp.simplify(sp.diff(h, t) - (t ** (zz - 2) / sp.log(t) ** 2
                                           - 2 * t ** (zz - 2) / ((zz - 1) * sp.log(t) ** 3))) == 0
        w = t ** -2 * (1 / sp.log(t) + 1 / sp.log(t) ** 2)
        ok3 = sp.simplify(sp.diff(-1 / (t * sp.log(t)), t) - w) == 0
        P = t / (2 * sp.pi) * sp.log(t / (2 * sp.pi * sp.E))
        F = sp.log(t / (2 * sp.pi)) ** 2 / (4 * sp.pi) - sp.log(t / (2 * sp.pi)) / (2 * sp.pi)
        ok4 = sp.simplify(sp.diff(F, t) - P / t ** 2) == 0
        say("[sympy] Nicolas (2.2) integrand identity:", ok1, "| (2.6) step:", ok2,
            "| int w = 1/(x log x):", ok3, "| int P/t^2 antiderivative:", ok4)
        res["sympy_identities"] = [bool(ok1), bool(ok2), bool(ok3), bool(ok4)]
    except Exception as e:  # pragma: no cover
        say("[sympy] skipped:", e)

    # ---- zero sums ------------------------------------------------------------------------------
    say("")
    say("--- Section 2: zero sums (upper bounds) ---")
    z1 = Z1(H0)
    sh = S_HIGH()
    eb = EPS_BAR()
    say("a = log(H0/2pi)                          in [", mp.nstr(lo(A_HAT), 14), ",", mp.nstr(up(A_HAT), 14), "]")
    say("Z1(H0) >= sum_{0<g<=H0} 1/g              <=", fmt(z1, 10))
    say("s_low  >= sum_{|g|<=H0} 1/|rho|^2        <=", fmt(S_LOW, 12), "(= 2 + gamma - log 4pi)")
    say("s_high >= sum_{|g|>H0} 1/g^2             <=", fmt(sh, 8))
    say("eps_bar (Z2 slack)                       <=", fmt(eb, 8))
    say("int_14^oo Q/t^2                          <=", fmt(intQ2(GAMMA1_LOWER), 8))
    res["Z1_H0_up"] = float(up(z1))
    res["s_low_up"] = float(up(S_LOW))
    res["s_high_up"] = float(up(sh))
    res["eps_bar_up"] = float(up(eb))

    # ---- Theorem 1 ------------------------------------------------------------------------------
    say("")
    say("--- Section 3: Theorem 1 (psi) ---")
    say("regime boundaries: L_A = 2 log(4 H0) =", mp.nstr(up(L_A), 10),
        "; L_B used =", mp.nstr(up(L_B), 6), "(needs >=", mp.nstr(up(L_B_MIN), 10), ")")
    assert up(L_B_MIN) <= lo(L_B)
    assert lo(L_A) > up(2 * iv.log(2 * H0 + 2))   # T = H0 admissible for L >= L_A
    s_I, s_II, s_III, Lstar = psi_constant()
    b, d = regime_III_coeffs()
    say("sup A_eff, regime I  (40 <= L <= L_A, T = x^(1/2)/4)      <=", mp.nstr(s_I, 6))
    say("sup A_eff, regime II (L_A <= L <= 190, T = H0)            <=", mp.nstr(s_II, 6))
    say("sup A_eff, regime III (L >= 190, T = 8 pi M x^(1/8))      <=", mp.nstr(s_III, 8))
    say("   regime III: A_eff <= 1/(128pi) + b/L - d/L^2 + 2 Z1(H0) e^{-3L/8}/L^2,")
    say("   b =", fmt(b, 8), " d >=", mp.nstr(lo(d), 8), " L* = 2d/b ~", mp.nstr(lo(Lstar), 6),
        " 1/(128 pi) =", fmt(1 / (128 * PI), 10))
    A_sup = max(s_I, s_II, s_III)
    A_PSI = I("0.0026")
    assert A_sup < lo(A_PSI)
    say("=> sup_{x >= e^40} B(x)/(x^(7/8) log^2 x) <=", mp.nstr(A_sup, 8), " < A = 0.0026")
    res["A_sup_x_ge_e40"] = float(A_sup)
    res["regime_sups"] = [float(s_I), float(s_II), float(s_III)]
    res["regime_III_b"] = float(up(b))
    res["regime_III_d_low"] = float(lo(d))

    # tail table A(L0)
    say("")
    say("table: sup over L >= L0 of the bound / (x^(7/8) log^2 x)")
    tabA = []
    for L0 in [190, 250, 500, 1000, 1500, 2000, 5000, 10 ** 4, 10 ** 5, 10 ** 6]:
        v, _ = aeff_III_sup(I(L0))
        tabA.append((L0, float(up(v))))
        say("   L0 = %-8s  A(L0) <= %s" % (L0, mp.nstr(up(v), 7)))
    res["A_of_L0"] = tabA

    # clean two-term form for L >= 190
    ctwo = (C1_HAT ** 2 - A_HAT ** 2) / (2 * PI) + 2 * eb
    say("two-term form (x >= e^190): |psi(x)-x| <= x^(7/8)[L^2/(128 pi) + b L + c0] + 2 Z1(H0) x^(1/2),")
    say("   with b <=", fmt(b, 8), ", c0 <=", fmt(ctwo, 8), "(negative), 2 Z1(H0) <=", fmt(2 * z1, 8))
    # check the sqrt term is absorbed: 2 Z1 e^{-3L/8} <= -c0 - 100 at L = 190 (decreasing)
    absorb = 2 * z1 * iv.exp(-3 * I(190) / 8)
    say("   2 Z1(H0) x^(-3/8) at L=190 <=", fmt(absorb, 4), "; so for x >= e^190:")
    say("   |psi(x)-x| <= x^(7/8) (log^2 x/(128 pi) + 0.17 log x - 113)")
    assert up(b) < 0.17 and up(ctwo + absorb) < -113
    res["two_term"] = {"b_up": float(up(b)), "c0_up": float(up(ctwo))}

    # small x
    say("")
    say("small x for Theorem 1:")
    xpt = pt_threshold(A_PSI)
    say("   Platt-Trudgian Cor. 1 bound is <= 0.0026 x^(7/8) log^2 x once x >=", fmt(xpt, 8),
        "(and x <= 2.169e25; e^40 =", mp.nstr(up(iv.exp(I(40))), 6), "< 2.169e25)")
    n_psi = small_x_threshold(A_PSI, "psi", 1500)
    n_th = small_x_threshold(A_PSI, "theta", 1500)
    say("   exact enumeration (interval logs) on [n, n+1), n <= 1500: psi bound holds for all x >=",
        n_psi, "; theta bound for all x >=", n_th)
    assert up(xpt) < 1500
    res["psi_x0"] = n_psi
    res["theta_x0"] = n_th

    # theta: extra term
    ext = psi_theta_extra(I(40))
    say("   (psi - theta) adds at most", fmt(ext, 4), "x^(7/8) log^2 x for x >= e^40 (decreasing),")
    say("   so A_theta := A_sup + extra <=", mp.nstr(up(I(A_sup) + ext), 8), "< 0.0026 as well.")
    assert up(I(A_sup) + ext) < lo(A_PSI)
    A_TH = A_PSI

    # ---- pi(x) - li(x) ---------------------------------------------------------------------------
    say("")
    say("--- Section 4: corollaries ---")
    # Buthe Thm 2 (arXiv:1410.7015v4) with T = 3 000 175 332 800 (Platt-Trudgian Thm 1) needs
    # 4.92 sqrt(x/log x) <= T; check it at x = 2.169e25.
    T_PT = I(3000175332800)
    cond = 4.92 * 0 + I("4.92") * iv.sqrt(XP / LXP)
    say("Buthe Thm 2 condition at x = 2.169e25: 4.92 sqrt(x/log x) <=", fmt(cond, 10), "<= T =",
        "3000175332800:", up(cond) <= lo(T_PT))
    assert up(cond) <= lo(T_PT)
    # pi - li, x > XP: |pi(XP)-li(XP)| <= sqrt(XP) log XP/(8pi) (Buthe (7.2)) and
    # |theta(XP)-XP|/log XP <= sqrt(XP) log XP/(8pi)
    CP = iv.sqrt(XP) * LXP / (4 * PI)
    A_pi = A_TH * (1 + I(8) / (7 * LXP)) + CP / (XP ** (I(7) / 8) * LXP)
    say("pi - li: for x > 2.169e25, |pi(x)-li(x)| <= A_pi x^(7/8) log x with A_pi <=", fmt(A_pi, 8))
    A_PI = I("0.00266")
    assert up(A_pi) < lo(A_PI)
    # Buthe range: sqrt(x) log x/(8pi) <= A_pi x^(7/8) log x  <=>  x >= (8 pi A_pi)^(-8/3)
    xpi = pt_threshold(A_PI)
    say("   Buthe (7.2) bound sqrt(x) log x/(8 pi) on (2657, 2.169e25] is <= 0.00266 x^(7/8) log x for x >=",
        fmt(xpi, 8))
    # if instead one uses the weaker printed form of Platt-Trudgian Cor. 1 (log^2 x):
    lo_L, hi_L = mp.mpf(8), mp.mpf(58)
    def gL(Lm):
        Li = I(Lm)
        return lo(8 * PI * A_PI * iv.exp(3 * Li / 8) - Li)
    for _ in range(80):
        mid = (lo_L + hi_L) / 2
        if gL(mid) >= 0:
            hi_L = mid
        else:
            lo_L = mid
    say("   (with Platt-Trudgian Cor. 1 as printed, sqrt(x) log^2 x/(8pi), the threshold would be x >=",
        mp.nstr(up(iv.exp(I(hi_L))), 6), ")")
    assert up(xpi) < 2657
    say("   => |pi(x) - li(x)| <= 0.00266 x^(7/8) log x for every x > 2657 (Buthe's range starts there)")
    res["A_pi"] = float(up(A_pi))
    res["pi_x0"] = "x > 2657"

    # ---- short intervals -------------------------------------------------------------------------
    cS = I("0.006")
    rmax = I(256) * iv.exp(I(-2))   # max of x^(-1/8) log^2 x (at log x = 16)
    x0s = I(n_th)
    delta = (1 + cS * rmax) ** (I(7) / 8) * (1 + iv.log(1 + cS * rmax) / iv.log(x0s)) ** 2 - 1
    need = A_TH * (2 + delta)
    say("short intervals: h = 0.006 x^(7/8) log^2 x; need c > A_theta (2 + delta), delta <=", fmt(delta, 6),
        "; A_theta(2+delta) <=", fmt(need, 6))
    assert up(need) < lo(cS)
    # asymptotic constant
    res["short_c"] = 0.006
    res["short_need"] = float(up(need))

    # ---- Robin -----------------------------------------------------------------------------------
    say("")
    say("--- Section 5: Robin / Nicolas, explicit ---")
    say("Jtail(XP) * XP^(1/8) log XP <=", fmt(Jtail_scaled(LXP), 6))
    say("  of which s_high part ~", fmt(S_HIGH() * (1 + (1 + 16 / LXP) / LXP), 6),
        "and the CHJ truncation part 8M XP^(-3/8)(log XP + 1) <=",
        fmt(8 * M_CHJ * iv.exp(-3 * LXP / 8) * (LXP + 1), 6))
    EGx = iv.exp(EG)
    targets = ["1.41", "1", "0.5", "0.1", "0.01", "1e-3", "1e-4", "1e-5", "1e-6", "1e-8", "1e-10"]
    rob = []
    say("%-8s %-12s %-14s %-14s %-12s %-26s" % ("C", "c=C e^-g", "log x1", "c_U (upper)", "eta",
                                               "log n1 = L1 (bound)"))
    for Cs in targets:
        C = I(Cs)
        c = C / EGx
        # bisection on L1 in [log 600, 2000] for least L1 with c_needed(L1) <= c
        a_, b_ = mp.log(600), mp.mpf(4000)
        if robin_c_needed(b_)[0] > lo(c):
            say(Cs, "not reached by L = 4000")
            continue
        if robin_c_needed(a_)[0] <= lo(c):
            b_ = a_
        else:
            for _ in range(60):
                mid = (a_ + b_) / 2
                if robin_c_needed(mid)[0] <= lo(c):
                    b_ = mid
                else:
                    a_ = mid
                if b_ - a_ < mp.mpf("0.01"):
                    break
        # round L1 up to 2 decimals and re-verify
        L1 = mp.ceil(b_ * 100) / 100
        cn, cu, ct, eta = robin_c_needed(L1)
        assert cn <= lo(c)
        x1 = iv.exp(I(L1))
        if up(x1) < 10 ** 7:
            p1, th = theta_at_next_prime(up(x1))
            Ln1 = up(th)
            how = "theta(%d) exactly" % p1
        else:
            Ln1 = up(x1 * (1 + I(eta)) + iv.log(2 * x1))
            how = "x1(1+eta)+log(2 x1)"
        # violator corollary (S1): L - y < c e^c L^(7/8) when log n >= max(L1, y1 e^{c y1^(-1/8)})
        y1 = I(Ln1)
        Ln1_S1 = up(y1 * iv.exp(c * y1 ** (-I(1) / 8)))
        rob.append({"C": Cs, "c": float(up(c)), "log_x1": float(L1), "x1": mp.nstr(up(x1), 6),
                    "cU_upper": float(cu), "cU_two_sided": float(ct), "eta": float(eta),
                    "log_n1": mp.nstr(Ln1, 8), "log_n1_method": how,
                    "log_n1_S1": mp.nstr(Ln1_S1, 8)})
        # COMPARISON with Robin's unconditional R2 (secondhand, via Lagarias): 0.6483/log log n
        Ln1i = I(Ln1)
        beatsR2 = up(C * Ln1i ** (-I(1) / 8) * iv.log(Ln1i)) < lo(I("0.6483"))
        rob[-1]["beats_R2_at_n1"] = bool(beatsR2)
        say("%-8s %-12s %-14s %-14s %-12s %-26s" % (Cs, mp.nstr(up(c), 5), mp.nstr(L1, 6),
                                                   mp.nstr(cu, 5), mp.nstr(eta, 3),
                                                   mp.nstr(Ln1, 8) + " (" + how + ")"))
        say("         two-sided Nicolas c_U = %s; (S1) holds for log n >= %s; sharper than R2 at n1: %s"
            % (mp.nstr(ct, 5), mp.nstr(Ln1_S1, 8), beatsR2))
    res["robin"] = rob

    # ---- comparison with unconditional tables (COMPARISON; published values transcribed) -------
    say("")
    say("--- Section 6: comparison with unconditional explicit PNT (COMPARISON) ---")

    def best_rel_bound(L):
        """min over candidate admissible T of B(x)/x; each candidate gives a rigorous bound."""
        Li = I(L)
        x = iv.exp(Li)
        Tmax = lo((iv.exp(Li / 2) - 2) / 2) * mp.mpf("0.999")
        Tmin = mp.mpf(max(51, L)) * mp.mpf("1.001")
        topt = up(8 * PI * M_CHJ * iv.exp(Li / 8))
        cands = [Tmax, lo(H0)] + [topt * mp.mpf("1.25") ** k for k in range(-40, 41)]
        best = None
        for T in cands:
            if not (Tmin < T <= Tmax):
                continue
            Ti = I(T)
            if up(Ti) <= lo(H0):
                Bx = 2 * iv.sqrt(x) * Z1(Ti) + M_CHJ * x * Li / Ti
            else:
                Bx = (2 * iv.sqrt(x) * Z1(H0) + 2 * x ** (I(7) / 8) * Z2(Ti) + M_CHJ * x * Li / Ti)
            r = up(Bx / x)
            best = r if best is None else min(best, r)
        return best

    # FKS Table 3 (eps_theta,num, which equals eps_psi,num after rounding per their caption) and
    # Johnston-Yang Table 1 (eps_0 for psi).  Transcribed values.
    FKS = {60: "1.1851e-11", 100: "2.0097e-12", 150: "1.8461e-12", 200: "1.7684e-12",
           240: "1.7304e-12", 250: "1.7229e-12", 260: "1.7160e-12", 270: "1.7095e-12",
           280: "1.7036e-12", 300: "1.6930e-12", 400: "1.6560e-12", 500: "1.6341e-12",
           1000: "1.5907e-12", 2000: "1.5692e-12", 3000: "4.9678e-15", 5000: "2.9942e-20",
           10000: "1.3680e-30"}
    cmp_rows = []
    for L in sorted(FKS):
        ours = best_rel_bound(L)
        fks = mp.mpf(FKS[L])
        jy = I("9.39") * I(L) ** I("1.515") * iv.exp(-I("0.8274") * iv.sqrt(I(L)))
        cmp_rows.append((L, float(ours), float(fks), float(lo(jy))))
        say("   log x = %-6d ours (H(7/8)) <= %-12s FKS Table 3: %-12s JY Thm 1.1 closed form: %s"
            % (L, mp.nstr(ours, 4), FKS[L], mp.nstr(lo(jy), 4)))
    res["comparison"] = cmp_rows
    # crossover against FKS: scan L in [190, 300] using FKS step values (their eps at log x0 holds
    # for all x >= x0, so on [L_i, L_{i+1}) the unconditional bound is eps(L_i)) -- informational
    fks_steps = [(150, "1.8461e-12"), (160, "1.8264e-12"), (170, "1.8092e-12"), (180, "1.7940e-12"),
                 (190, "1.7805e-12"), (200, "1.7684e-12"), (210, "1.7575e-12"), (220, "1.7476e-12"),
                 (230, "1.7386e-12"), (240, "1.7304e-12"), (250, "1.7229e-12"), (260, "1.7160e-12"),
                 (270, "1.7095e-12"), (280, "1.7036e-12"), (290, "1.6981e-12"), (300, "1.6930e-12")]
    cross = None
    for L in range(190, 301):
        ours = best_rel_bound(L)
        eps = [mp.mpf(v) for (l0, v) in fks_steps if l0 <= L][-1]
        if ours < eps and cross is None:
            cross = L
        if ours >= eps:
            cross = None
    say("   first integer log x in [190,300] from which ours < FKS step value for every larger tested",
        "log x:", cross)
    res["crossover_logx_vs_FKS"] = cross
    # vs closed forms (JY Thm 1.1 and Thm 1.4) using the clean A = 0.0026 shape
    def cross_closed(f):
        for L in range(41, 3000):
            ours = A_PSI * I(L) ** 2 * iv.exp(-I(L) / 8)
            if up(ours) < lo(f(I(L))):
                return L
        return None
    jy11 = lambda L: I("9.39") * L ** I("1.515") * iv.exp(-I("0.8274") * iv.sqrt(L))
    jy14 = lambda L: I("0.026") * L ** I("1.801") * iv.exp(-I("0.1853") * L ** (I(3) / 5)
                                                         * iv.log(L) ** (-I(1) / 5))
    c11, c14 = cross_closed(jy11), cross_closed(jy14)
    say("   clean shape 0.0026 x^(7/8) log^2 x beats JY Thm 1.1 closed form from log x =", c11,
        "and JY Thm 1.4 (VK) closed form from log x =", c14, "(checked to log x < 3000; both",
        "ratios then move monotonically in our favour)")
    res["crossover_clean_vs_JY11"] = c11
    res["crossover_clean_vs_JY14"] = c14

    # pi: clean shape 0.00266 x^(7/8) log x, relative to x/log x, vs FKS Table 4 (eps_pi,num)
    fks_pi = [(200, "1.7789e-12"), (210, "1.7675e-12"), (220, "1.7571e-12"), (230, "1.7476e-12"),
              (240, "1.7390e-12"), (250, "1.7311e-12"), (260, "1.7238e-12"), (270, "1.7171e-12"),
              (280, "1.7108e-12"), (290, "1.7051e-12"), (300, "1.6997e-12")]
    crossp = None
    for L in range(200, 301):
        ours = up(I("0.00266") * I(L) ** 2 * iv.exp(-I(L) / 8))
        eps = [mp.mpf(v) for (l0, v) in fks_pi if l0 <= L][-1]
        if ours < eps and crossp is None:
            crossp = L
        if ours >= eps:
            crossp = None
    say("   pi: 0.00266 x^(7/8) log x < eps_pi(FKS Table 4) x/log x from log x =", crossp,
        "(clean shape; tested to 300, then monotone)")
    res["crossover_pi_vs_FKS"] = crossp

    # ---- sensitivity of Theorem 1 to the truncation constant M (rigorous for the altered M) ----
    res["sensitivity_M"] = sensitivity()

    # ---- optional empirical zero check ---------------------------------------------------------
    if "--zeros" in sys.argv:
        say("")
        say("--- EMPIRICAL (float) sanity: partial sums over the first 200 zeros ---")
        from mpmath import zetazero
        mp.dps = 20
        s1 = 0.0
        s2 = 0.0
        for n in range(1, 201):
            g = float(zetazero(n).imag)
            s1 += 2 / (0.25 + g * g)
            s2 += 1 / g
        say("   sum_{n<=200} 2/(1/4+g^2) =", s1, "(< s_low = 0.0461914 as it must be)")
        say("   sum_{n<=200} 1/g_n       =", s2, " vs Z1(g_200) bound", float(up(Z1(I(g)))))

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "explicit_pnt_7_8.txt"), "w") as fh:
        fh.write("\n".join(OUT) + "\n")
    with open(os.path.join(RESULTS, "explicit_pnt_7_8.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    say("")
    say("wrote results/explicit_pnt_7_8.txt and .json")


if __name__ == "__main__":
    main()
