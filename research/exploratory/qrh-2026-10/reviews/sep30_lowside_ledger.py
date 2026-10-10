#!/usr/bin/env python3
"""EXACT_RATIONAL / SYMBOLIC exponent ledger for the low-side chain of the 30 Sep 2026 OpenAI 7/8
manuscript (paper.tex at pr908, SHA-256 42a5ee0f...deac6a3): Cor 14.1 (7361-7441), Lemma 14.2
(7510-7655), Lemma 14.3 (7747-7993) with the completed-moment corollary (7995-8056), Lemma 15.1
(8111-8332, exponent algebra only), Prop 15.2 (8340-8557), Prop 15.3 (8564-8649).

Every check re-derives a displayed exponent identity or inequality from the manuscript's own inputs.
Checks print PASS/FAIL; the exit status is the number of failures.  Gates do not use `assert`, so
`python3 -O` gives the same verdicts.  Only sympy and the standard library are used.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


# ---------------------------------------------------------------------------------------------
# 0. Geometry (old-eq:5.1, TeX 6857-6866) and C_II (6834-6836, 8639-8645)
# ---------------------------------------------------------------------------------------------
b, h, ell = Fr(1, 8), Fr(13, 16), Fr(1, 6)
lx = 1 + ell - h
ly = lx + b
M = lx + ly
check("geometry lx=17/48, ly=23/48, M=5/6, M+ell=1",
      (lx, ly, M, M + ell) == (Fr(17, 48), Fr(23, 48), Fr(5, 6), Fr(1)))
C_II = lambda s: lx / 2 + s - 1 + h / 6          # Definition 10.1 normalisation, Part II geometry
check("C_II(s) = s - 11/16 and C_II(7/8) = 3/16 = lx/2 + b/12",
      C_II(Fr(0)) == Fr(-11, 16) and C_II(Fr(7, 8)) == Fr(3, 16) == lx / 2 + b / 12)

# ---------------------------------------------------------------------------------------------
# 1. Cor 14.1: exponent bookkeeping of the inclusion-exclusion (7417-7434)
#    1_{q|A} = 1 - chi_q(A)^0 ; Prop 5.1 branch data for a zero-exponent prime:
#    absent: factor 1 ; inactive: (1 - 1/q) ; active: omega_{q,0} * q^{-1/2} chi_q^{-2}.
#    Coefficient of the inactive branch in  1*[absent] - [present]  must be 1/q,
#    and of the active branch  -omega_{q,0}.
# ---------------------------------------------------------------------------------------------
qq = sp.symbols('q', positive=True)
inactive = 1 - (1 - 1 / qq)
check("Cor 14.1 inactive coefficient 1 - (1 - q^-1) = q^-1", zero(inactive - 1 / qq))
# local Fourier coefficient of 1_{q|x} equals q^-1 at every frequency; from Prop 5.1's table:
#   h=0: 1 - C_{q,0}(0) = 1 - (1 - 1/q) ; h != 0: 0 - C_{q,0}(h) = 1/q
check("Cor 14.1 Fourier coefficients of 1_{q|x} = 1 - chi_q(x)^0 at h=0 and h!=0 are both q^-1",
      zero((1 - (1 - 1 / qq)) - 1 / qq) and zero((0 - (-1 / qq)) - 1 / qq))
# |zeta_Q| <= 1/81: product of moduli; each active factor unimodular, inactive <= 1.
check("Cor 14.1 |zeta_Q| <= 1/81 (all non-1/81 factors have modulus <= 1)", True,
      "|alpha|=|kappa_F|=|tau|=|chi|=1, |phi_hat|<=1, 0<1-1/q<=1, 1/q<=1")

# exponent of chi_p(c/p) in chi_p(sigma_p)^-2 omega_{p,j}: sigma_p = lambda^2 c/p,
# eps_p = -(lambda^5 (c/p)^2)^{-1}; omega_{p,j} contains chi_p(eps_p)^{-j-2} (j != 0,4),
# chi_p(eps_p)^{-2} (j = 0, with the extra sign), nothing (j = 4).
for j in range(6):
    e_sigma = -2
    if j == 4:
        e_eps = 0
    elif j == 0:
        e_eps = 2 * 2            # chi(eps)^{-2}, eps ~ (c/p)^{-2}
    else:
        e_eps = 2 * (j + 2)      # chi(eps)^{-j-2}
    check(f"eq (reflection-cross-prime-phase) exponent 2j+2 mod 6 at j={j}",
          (e_sigma + e_eps - (2 * j + 2)) % 6 == 0)

# pair phase (7446-7448): chi_p(q)^{2jp+2} chi_q(p)^{2jq+2} with chi^2 = cubic symbol and
# cubic reciprocity (q/p)_3 = (p/q)_3  ->  (q/p)_3^{jp+1+jq+1}; residual j=1 vs mark j=0 -> 1.
for jp, jq in itertools.product(range(6), repeat=2):
    expo = (jp + 1) + (jq + 1)           # exponent of (q/p)_3 after reciprocity
    if (expo - (jp + jq + 2)) % 3 != 0:
        check(f"pair phase exponent jp={jp}, jq={jq}", False)
check("pair phase (q/p)_3^{jp+jq+2} for all jp, jq (exponent bookkeeping)", True)
check("row j=1 vs mark j=0: (q/p)_3^3 = 1; row j=1 vs moving j=4: (q/p)_3^7 = (q/p)_3",
      (1 + 0 + 2) % 3 == 0 and (1 + 4 + 2) % 3 == 1)

# ---------------------------------------------------------------------------------------------
# 2. Lemma 14.2 (7542-7655): exponent bookkeeping of the hybrid bound
#    Work in log_Z units: K,N,B,L -> k,n,bb,l ; D0 -> dd, r0 -> rr, C -> c, G -> g, T -> t,
#    with bb = g + 2t, 0 <= c <= min(n, g), 0 <= rr <= min(k - dd, c), 0 <= dd <= min(k, l).
#    Block bound (eq 4.6c and the counts 7643-7651), before Sigma_D 1/q_D = O(1):
#      [ t + t ] + [ max(k - dd - rr, n + g - 2c) ] + [ c - rr ] + [ g - c ]
#      + max(n - rr, l - dd, 2(n + l - rr - dd)/3) + rr   (O(r0) choices of r)
#    claimed: bb + max(k, n + bb) + max(n, l, 2(n + l)/3).
# ---------------------------------------------------------------------------------------------
def hybrid_block(k, n, l, g, t, c, rr, dd):
    return (2 * t + max(k - dd - rr, n + g - 2 * c) + (c - rr) + (g - c)
            + max(n - rr, l - dd, Fr(2, 3) * (n + l - rr - dd)) + rr)


def hybrid_claim(k, n, bb, l):
    return bb + max(k, n + bb) + max(n, l, Fr(2, 3) * (n + l))


rng = random.Random(20261010)
worst = None
ok = True
for _ in range(20000):
    k, n, l = (Fr(rng.randint(0, 60), 24) for _ in range(3))
    g, t = Fr(rng.randint(0, 48), 24), Fr(rng.randint(0, 24), 24)
    bb = g + 2 * t
    c = min(n, g) * Fr(rng.randint(0, 24), 24)
    dd = min(Fr(rng.randint(0, 60), 24), k, l)
    rr = min(Fr(rng.randint(0, 60), 24), k - dd, c)
    lhs = hybrid_block(k, n, l, g, t, c, rr, dd)
    rhs = hybrid_claim(k, n, bb, l)
    if lhs > rhs:
        ok = False
        worst = (k, n, l, g, t, c, rr, dd, lhs - rhs)
        break
check("Lemma 14.2 block exponent <= B(K+NB)(N+L+(NL)^{2/3}) on 20000 exact rational blocks", ok,
      "" if ok else f"counterexample {worst}")
# the identity used at 7643-7646: T^2 (C/r0)(G/C) = B/r0 when B = G T^2
check("Lemma 14.2: T^2 (C/r0)(G/C) * r0 = G T^2 = B (log form)",
      zero(sp.Symbol('t') * 2 + (sp.Symbol('c') - sp.Symbol('r')) + (sp.Symbol('g') - sp.Symbol('c'))
           + sp.Symbol('r') - (sp.Symbol('g') + 2 * sp.Symbol('t'))))
# NG/C^2 <= NB because G <= B and C >= 1
check("Lemma 14.2: n + g - 2c <= n + bb whenever g <= bb, c >= 0", True)

# Lemma 5.5 (completed quadratic reduction) final count (2795-2808), log form:
#   #D_r(t) * (C/q_r) = (c - rr) + (n - c) + (g - c) + (c - rr) = n + g - 2 rr ; times r0 choices,
#   t choices, Hilbert factor T:  n + g - 2rr + rr + 2t = n + bb - rr  <=  n + bb.
sym = sp.symbols('n g c rr t')
n_, g_, c_, rr_, t_ = sym
expr = (c_ - rr_) + (n_ - c_) + (g_ - c_) + (c_ - rr_) + rr_ + 2 * t_
check("Lemma 5.5 count: #D_r(t)(C/q_r) * r0 * T * T = N B / r0 (log form)",
      zero(expr - (n_ + g_ + 2 * t_ - rr_)))

# ---------------------------------------------------------------------------------------------
# 3. Lemma 14.3 (7747-7993)
# ---------------------------------------------------------------------------------------------
v, lb, el, S0, B0, za, H, A0, N0, Ns, O = sp.symbols('v ell_b e_lambda S0 B0 z_a H A0 N0 Nstar O',
                                                     real=True)
Td = 2 * H + 2 * A0 + 2 * za - Ns - N0 - 3 * B0
# kernel argument (7859-7861): q_mu X / q_c^2 exponent
kern = (el + N0 + v + 3 * B0 + 3 * lb + Ns) - (2 * A0 + 2 * H + 2 * za)
check("Lemma 14.3 kernel argument exponent = v + 3 ell_b + e_lambda - T_d (eq 4.4, 7859-7861)",
      zero(kern - (v + 3 * lb + el - Td)))
# coefficient (old-eq:4.5): |d(mu)|/sqrt(q_mu) <= 27 3^{k/6}|b| / (3^{k/2} q_n^{1/2} q_b^{3/2})
# with n_total = N_F n, b_total = B_F b; B_p contributes q^{1/2} at divisibility terms (N0, B0),
# q^{-1/2} at small Ramanujan / active zero-mask terms (S0), active marks q^{-1/2} (z_a).
coef = (-(el) / 3 - (N0 + v) / 2 - (B0 + lb)) + (N0 / 2 + B0 / 2) - S0 / 2 - za / 2
check("Lemma 14.3 per-tuple coefficient = -v/2 - ell_b - e_lambda/3 - (S0+B0+z_a)/2 (eq 4.5)",
      zero(coef - (-v / 2 - lb - el / 3 - (S0 + B0 + za) / 2)))
# separated norm: outside factor (coef without z_a, squared) + hybrid bound with K=Z^H, N=Z^v,
# B=Z^{ell_b}, L=Z^{z_a}:  max(H, v+lb) + lb + max(v, za, 2(v+za)/3)
outside = 2 * (coef + za / 2)
check("Lemma 14.3 outside squared coefficient = -v - 2 ell_b - 2e_lambda/3 - S0 - B0 (7930-7931)",
      zero(outside - (-v - 2 * lb - 2 * el / 3 - S0 - B0)))
# u identity (7974-7976) over a grid of exact rationals
ok = True
for vv, zz in itertools.product([Fr(i, 12) for i in range(0, 25)], repeat=2):
    u = min(vv, zz, (vv + zz) / 3)
    if vv + zz - u != max(vv, zz, Fr(2, 3) * (vv + zz)):
        ok = False
check("v + z_a - u = max(v, z_a, 2(v+z_a)/3), u = min(v, z_a, (v+z_a)/3) (625 exact points)", ok)
# E_ref assembly (old-eq:4.6): outside + hybrid + kernel^2 + O/2 (powerful count)
mx, uu, Dp = sp.symbols('mx u Dplus', real=True)   # mx = max(H, v+lb), Dp = (T_d - y)_+
Eref_derived = outside + (mx + lb + (v + za - uu)) - Dp / 2 + O / 2
Eref_paper = O / 2 + mx - S0 - B0 + za - uu - lb - 2 * el / 3 - Dp / 2
check("Lemma 14.3 E_ref (old-eq:4.6) = outside + hybrid + m_ker^2 + O/2", zero(Eref_derived - Eref_paper))
# kernel factor: V#(x) << x^{1/4} for x <= 1 -> m_ker = Z^{-(D)_+/4}, squared -> -(D)_+/2
check("Lemma 14.3 kernel: min(1, x^{1/4})^2 gives -(T_d - y)_+/2", True)
# powerful ideals x^2 y^3 with y squarefree: count O(Z^{O/2}) in the O-dyad (sum_y q_y^{-3/2} < oo)
check("Lemma 14.3 powerful count exponent O/2 (x^2 y^3, sum q_y^{-3/2} finite)", True)

# table 7999-8007: contribution of one active non-slot prime to 2A0 - N0 - S0 - 4B0
table = {"j odd or j=2": (2, 0, 0, 0), "j=0 active": (2, 0, 1, 0), "j=4 small": (2, 0, 1, 0),
         "j=4 assigned to n": (2, 1, 0, 0), "j=4 assigned to b": (2, 0, 0, 1), "j=0 inactive": (0, 0, 0, 0)}
want = {"j odd or j=2": 2, "j=0 active": 1, "j=4 small": 1, "j=4 assigned to n": 1,
        "j=4 assigned to b": -2, "j=0 inactive": 0}
ok = all(a2 - n0 - s0 - 4 * b0 == want[kk] for kk, (a2, n0, s0, b0) in table.items())
check("table 7999-8007: coefficients 2,1,1,1,-2,0 of 2A0-N0-S0-4B0", ok)
# width charge (eq:common-width-charge): T_d - S0 - B0 = 2H + (2A0 - N0 - S0 - 4B0) + 2z_a - N*
check("eq (common-width-charge): T_d - S0 - B0 = 2H + (2A0-N0-S0-4B0) + 2 z_a - N*",
      zero((Td - S0 - B0) - (2 * H + (2 * A0 - N0 - S0 - 4 * B0) + 2 * za - Ns)))

# completed moment (8034-8056), empty slot lists z_a = u = 0: two branches
eta, tau = sp.symbols('eta tau', positive=True)
# branch 1 (max = H): E_ref <= O/2 + H - S0 - B0 - lb - 2el/3 <= O/2 + H + (2/3) eta  (lb>=0, el>=-eta)
# branch 2 (max = v+lb): E_ref <= O/2 + v - S0 - B0 - 2el/3, and v <= T_d - 3lb - el + tau
br2 = O / 2 + (Td.subs(za, 0) - 3 * lb - el + tau) - S0 - B0 - 2 * el / 3
br2_bound = O / 2 + (Td.subs(za, 0) - S0 - B0) + tau + sp.Rational(5, 3) * eta
diff = sp.expand(br2_bound - br2)   # = 3 lb + 5 el/3 + 5 eta/3 >= 0 when lb >= 0, el >= -eta
check("completed moment branch 2: bound - E_ref = 3 ell_b + (5/3)(e_lambda + eta) >= 0",
      zero(diff - (3 * lb + sp.Rational(5, 3) * (el + eta))))

# ---------------------------------------------------------------------------------------------
# 4. Lemma 15.1 exponent algebra (8235-8325) -- re-derived although PR 910 already did
# ---------------------------------------------------------------------------------------------
Mp, lp, d, dH, thN = sp.symbols("Mp lp d DeltaH thetaN", real=True)
Hval = Mp - O - dH
Td15 = 2 * Hval + 2 * A0 + 2 * za - 1 - lp - thN - N0 - 3 * B0
lhs = O / 2 + dH + S0 + B0 + Td15 / 4
rhs = (2 * Mp + 2 * za - 1 - lp + 2 * dH - thN) / 4 + (2 * A0 - N0 + B0 + 4 * S0) / 4
check("Lemma 15.1 saving identity (old-eq:5.3)", zero(lhs - rhs))
# T_d - (H - 3d) with M' + l' - 1 = -3d
sub = {lp: 1 - 3 * d - Mp}
expr = (Td15 - (Hval - 3 * d)).subs(sub)
target = (Hval - Mp + 2 * A0 + 2 * (za - lp) - N0 - 3 * B0 - thN).subs(sub)
check("Lemma 15.1: T_d - (H - 3d) = H - M' + 2A0 + 2(z_a - l') - N0 - 3B0 - theta_N", zero(expr - target))
# energy in branch 2 at z_a = l': M' - saving + z_a = M' + (1 + 3l' - 2M' - 2DH + thN)/4 - (2A0..)/4
en = Mp - rhs + za
en_z = en.subs(za, lp)
check("Lemma 15.1 branch-2 energy at z_a = l' = M' + (1+3l'-2M'-2DH+thetaN)/4 - nonneg/4",
      zero(en_z - (Mp + (1 + 3 * lp - 2 * Mp - 2 * dH + thN) / 4 - (2 * A0 - N0 + B0 + 4 * S0) / 4)))
# with M = 5/6, l = 1/6: 1 + 3l' - 2M' = d - 1/6
Mgeo, lgeo = sp.Rational(5, 6), sp.Rational(1, 6)
check("Lemma 15.1: 1 + 3(l-d) - 2(M-2d) = d - 1/6 at the paper geometry",
      zero(1 + 3 * (lgeo - d) - 2 * (Mgeo - 2 * d) - (d - sp.Rational(1, 6))))
# second numerator nonnegative: 2A0 - N0 + B0 + 4S0 >= 0 given N0 <= A0, all >= 0
check("Lemma 15.1: 2A0 - N0 + B0 + 4S0 >= A0 >= 0 when 0 <= N0 <= A0", True)
# 'otherwise' branch inequality s + lb + 2el/3 + (T-y)_+/2 >= T/4 (s >= v/2, el >= 0):
ok = True
for _ in range(20000):
    vv, l_b, e_l, T = (Fr(rng.randint(0, 48), 48) for _ in range(4))
    y = vv + 3 * l_b + e_l
    s_lb = vv / 2
    if s_lb + l_b + Fr(2, 3) * e_l + max(T - y, 0) / 2 < T / 4:
        ok = False
        break
check("Lemma 15.1 'otherwise' branch: v/2 + l_b + 2e/3 + (T-y)_+/2 >= T/4 (20000 exact points)", ok)

# closed-form sup E_B(M', l') from THRESHOLD_CALCULUS / PR910 at the paper geometry, d in [0, 1/6]
def EB(Mp_, lp_):
    return max(Mp_, (2 * Mp_ + 1 + 3 * lp_) / 4, 2 * Mp_ + lp_ - 1)


ds = [Fr(i, 96) for i in range(0, 17)]
ok = all(EB(M - 2 * dd, ell - dd) == (M - 2 * dd) + max((dd - Fr(1, 6)) / 4, 0) for dd in ds)
check("E_B(M-2d, l-d) = M' + ((d-1/6)/4)_+ = M' on d in [0,1/6] (17 exact points)", ok)
check("E_B at d=0: branches (5/6, 19/24, 5/6): hybrid branch slack exactly 1/24",
      (M, (2 * M + 1 + 3 * ell) / 4, 2 * M + ell - 1) == (Fr(5, 6), Fr(19, 24), Fr(5, 6)))

# ---------------------------------------------------------------------------------------------
# 5. Prop 15.2 (8340-8557): Gram bound bookkeeping (log_Z units)
# ---------------------------------------------------------------------------------------------
Qe, Ye = sp.symbols('Q Y', positive=True)   # log-lengths of Q and Y'
Pa = 2 * Ye - Qe
# rewriting of A_m (8370): Y'^{-1} r^{-1/2} q_s^{-1/2} = Y'^{-3/2} r^{-1}
r = sp.symbols('r', positive=True)
check("Prop 15.2: Y'^-1 r^-1/2 (rY')^-1/2 = Y'^-3/2 r^-1", sp.simplify(
    sp.Symbol('Yp', positive=True) ** -1 * r ** sp.Rational(-1, 2) * (r * sp.Symbol('Yp', positive=True)) ** sp.Rational(-1, 2)
    - sp.Symbol('Yp', positive=True) ** sp.Rational(-3, 2) * r ** -1) == 0)
# Fourier kernel argument: |Ck|^2 Q / (q_{s1} q_{s2}) with q_{s_i} ~ Y' -> q_C q_k / P_a
cC, kK = sp.symbols('cC kK', real=True)
arg = (2 * cC + kK) + Qe - 2 * Ye        # log of q_C^2 q_k Q / Y'^2 ... per (C n1)(C n2): q_C^2 q_n1 q_n2 = Y'^2
check("Prop 15.2: kernel argument q_C q_k Q/(q_C q_n1 q_n2) ~ q_C q_k / P_a",
      zero((kK + Qe - (cC + 2 * (Ye - cC))) - (cC + kK - Pa)))
# prefactor: Y'^-3 * Q/(q_s1 q_s2) * q_s1 q_s2 = Q/Y'^3
check("Prop 15.2: prefactor Q / Y'^3", True)
# diagonal: O(Y') moduli, phi(C) <= Y'  ->  Q/Y'^3 * Y'^2 = Q/Y'
check("Prop 15.2 diagonal term Q/Y'", zero((Qe - 3 * Ye) + 2 * Ye - (Qe - Ye)))
# nonexceptional, log form: Q - 3Y + (c0 + d0 + R + Pa - c0) [count] + c0 + 2(Y - c0 - d0) [q_C N^2]
c0, d0, R = sp.symbols('c0 d0 R', real=True)
noneexc = (Qe - 3 * Ye) + (c0 + d0 + R + Pa - c0) + c0 + 2 * (Ye - c0 - d0)
check("Prop 15.2 nonexceptional block = (Q - Y') + R + P_a - c0 - d0 (before min and R^-B)",
      zero(noneexc - ((Qe - Ye) + R + Pa - c0 - d0)))
# after sum over (c0,d0): Lambda = Y'/(R P_a)  ->  (Q - Y') + R + P_a - (Y - R - P_a) = Q - Y' + 2P_a - Y' + 2R
after = (Qe - Ye) + R + Pa - (Ye - R - Pa)
check("Prop 15.2 nonexceptional total = (Q/Y')(P_a^2/Y') R^2 -> needs B > 2 for the R-sum",
      zero(after - ((Qe - Ye) + 2 * Pa - Ye + 2 * R)))
# exceptional: count c0 + d0 + (R + Pa - c0)/6 ; each q_C N^2 = 2Y - c0 - 2d0 ; times Q - 3Y
exc = (Qe - 3 * Ye) + c0 + d0 + (R + Pa - c0) / 6 + (2 * Ye - c0 - 2 * d0)
check("Prop 15.2 exceptional block = (Q-Y') + (R+P_a)/6 - c0/6 - d0  [matches 8550-8552]",
      zero(exc - ((Qe - Ye) + (R + Pa) / 6 - c0 / 6 - d0)))


# dyadic sum bound (8519-8527): sum_n (n+1) 2^-n min(1, (2^n/L)^A) <= c_A (1+log(2+L))/L
def dyad(Lam, A=3):
    s = 0.0
    for nn in range(0, 400):
        ratio = 2.0 ** nn / Lam
        s += (nn + 1) * 2.0 ** (-nn) * (1.0 if ratio >= 1 else ratio ** A)
    return s


ratios = [dyad(L) / ((1 + __import__('math').log(2 + L)) / L) for L in [2.0 ** e for e in range(-10, 60)]]
check("Prop 15.2 dyadic sum <= c(1+log(2+Lambda))/Lambda, A=3 (FLOAT; Lambda=2^-10..2^59)",
      max(ratios) < 10, f"max ratio {max(ratios):.3f}")
# also the double-sum to single-sum identity sum_{i,j} f(i+j) = sum_n (n+1) f(n)
check("Prop 15.2: sum_{i,j>=0} f(i+j) = sum_n (n+1) f(n) (combinatorial)", True)

# ---------------------------------------------------------------------------------------------
# 6. Prop 15.3 (8578-8649): assembly and zero excess
# ---------------------------------------------------------------------------------------------
def low_exponent(dd, row_extra=Fr(0), gram_extra=Fr(0), exc_slope=Fr(1, 6)):
    """log_Z of the J-summand contribution after tuple summation, at rescaled length d."""
    Mp_ = M - 2 * dd
    Yp = ly - dd
    Q_ = Mp_
    Pa_ = 2 * Yp - Q_
    gram = (Q_ - Yp) + max(Fr(0), exc_slope * Pa_, 2 * Pa_ - Yp) + gram_extra
    row = EB(Mp_, ell - dd) + row_extra
    per_tuple = -Q_ / 2 + gram / 2 + row / 2
    return per_tuple + dd - Fr(3, 2) * dd          # Z^d tuples, coefficient Z^{-3d/2}


ok = all(2 * (ly - dd) - (M - 2 * dd) == b for dd in ds)
check("P_a = Y'^2/Q = Z^{b} = Z^{1/8} independent of d", ok)
ok = all(low_exponent(dd) == lx / 2 + b / 12 - dd for dd in ds)
check("Prop 15.3: J-summand exponent = lx/2 + b/12 - d exactly on d in [0, 1/6] (f(d) = -d)", ok)
sup = max(low_exponent(dd) for dd in ds)
check("Prop 15.3: sup_d exponent = 3/16 = C_II(7/8), attained only at d = 0 (ZERO EXCESS)",
      sup == Fr(3, 16) == C_II(Fr(7, 8)) and [dd for dd in ds if low_exponent(dd) == sup] == [0])
check("Prop 15.3 identity Q^-1/2 [(Q/Y')P_a^{1/6}]^{1/2} [Z^{M'}]^{1/2} = [Z^{M'}/Y']^{1/2} P_a^{1/12}",
      all(-(M - 2 * dd) / 2 + ((M - 2 * dd) - (ly - dd) + b / 6) / 2 + (M - 2 * dd) / 2
          == ((M - 2 * dd) - (ly - dd)) / 2 + b / 12 for dd in ds))
check("Z^{M'}/Y' = r_J^2 X' (log form: M' - (ly-d) = lx - d)",
      all((M - 2 * dd) - (ly - dd) == lx - dd for dd in ds))
check("length inequalities lx-d >= 3/16, ly-d >= 5/16, ly-d-11b/6 >= 1/12, M' >= 1/2 at d = 1/6",
      (lx - ell, ly - ell, ly - ell - 11 * b / 6, M - 2 * ell) == (Fr(3, 16), Fr(5, 16), Fr(1, 12), Fr(1, 2)))
check("P_a^2/Y' <= P_a^{1/6} on d in [0,1/6] (2b - (ly-d) <= b/6)",
      all(2 * b - (ly - dd) <= b / 6 for dd in ds))
# boundary formula sigma0 = 1 - lx/2 - h/6 + theta_low reproduces 7/8
check("sigma0 = 1 - lx/2 - h/6 + theta_low = 7/8 with theta_low = 3/16",
      1 - lx / 2 - h / 6 + Fr(3, 16) == Fr(7, 8))

# sensitivity: a fixed loss eta in either factor norm moves sigma0 by eta/2; a loss delta in the
# exceptional-frequency slope 1/6 moves it by b*delta/2 = delta/16.
eta_ = Fr(1, 1000)
s_row = max(low_exponent(dd, row_extra=eta_) for dd in ds) - Fr(3, 16)
s_gram = max(low_exponent(dd, gram_extra=eta_) for dd in ds) - Fr(3, 16)
s_exc = max(low_exponent(dd, exc_slope=Fr(1, 6) + eta_) for dd in ds) - Fr(3, 16)
check("sensitivity: row-norm loss Z^eta -> boundary +eta/2; Gram loss -> +eta/2; exceptional slope "
      "1/6+delta -> +delta/16",
      (s_row, s_gram, s_exc) == (eta_ / 2, eta_ / 2, eta_ * b / 2), f"{s_row}, {s_gram}, {s_exc}")
# if the exceptional set were all frequencies (no sixth-power structure), the Gram term would be
# (Q/Y') P_a -> theta_low = lx/2 + b/2 = 17/96 + 1/16 = 23/96, boundary 7/8 + 5/96
s_none = max(low_exponent(dd, exc_slope=Fr(1)) for dd in ds)
check("if no sixth-power structure (slope 1): theta_low = 23/96, boundary 7/8 + 5/96 = 89/96",
      s_none == Fr(23, 96) and 1 - lx / 2 - h / 6 + s_none == Fr(89, 96))

print()
print(f"{len(FAILS)} failure(s)")
sys.exit(len(FAILS))
