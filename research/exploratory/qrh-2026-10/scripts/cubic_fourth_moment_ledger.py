"""cubic_fourth_moment_ledger.py -- exact exponent bookkeeping for transferring the scheme of
Lemma 18.1 (lem:plain, case 1, z = 0) of the OpenAI QRH manuscript (30 Sep 2026, unreviewed;
pr908 = 31c706bb..., paper.tex sha256 42a5ee0f...deac6a3) from the sextic family to the cubic
(n = 3) and quadratic (n = 2) families over Q(omega).

Status: EXPLORATION.  The script checks AFFINE EXPONENT LEDGERS ONLY.  It does not check that the
ledgers describe the analysis correctly, and it proves no moment bound.  The order n enters
through theta = 1/n (density of n-th powers) and through the residues mod n listed below.

Parametrisation (everything in units of log Z, exactly as in paper.tex l. 13114-14777):
  theta = 1/n                    density exponent of n-th powers (sextic paper: theta = 1/6)
  exceptional child rows (h') = h_0 v^n, count Z^{theta (m' - f)}       (l. 14365-14380)
  E(theta) = theta (m' - f) + a_0 - b_2 - (M' + Delta_child)          (l. 14436-14449)
           = A - (1 - theta) M - F1(theta) - F2(theta)
  centred lattice saving r = (L - v)_+,  v = c + w + min(c_2, d_2)      (l. 14694, 14752)
  comparison after reflecting the long factor:  A_comp = M - A + 2L    (l. 12952-12968)

Sections:
  [A] symbolic identities for general theta (reduce to the paper's at theta = 1/6)
  [B] first-transform allowance B_c: best kappa_1 with / without forcing at r-primes
  [C] second-transform F2 table: best kappa_2 with / without forcing
  [D] comparison-length window, deficit at A = M, failing A-range, self-consistent loss eta
  [E] Gauss-row zero (h = 0) inequality for order n
  [F] explicit cubic paths (generic; (2,1)-common support) at A = M
  [G] brute-force grid confirmation of [D] with exact Fractions

Run: python3 -I cubic_fourth_moment_ledger.py      (a few seconds, single process)
"""
from fractions import Fraction as Fr
import sympy as sp

results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def pos(x):
    return x if x > 0 else 0


# --------------------------------------------------------------------------------------------
print("=== [A] symbolic identities, general theta ===")
A, c, d, R, E, m, q, w, wo, g, ell, Bc, Dk, g2, t2, V, p2, b2, f, s0, th = sp.symbols(
    "A c d R E m q w w_o g ell B_c Dk g_2 t_2 V p_2 b_2 f s_0 theta", real=True)
M = m + q
qt = q + R + E
K0 = 2 * A - c - d + R + E - m
K = K0 - Dk
a0 = A - c - w
J = d - c + Dk - 2 * w + wo
mp = 2 * a0 - K - g - g2 - V
qp = qt + wo + t2 + V
Mp = mp + qp
Dchild = b2 - p2 + w + Bc + ell
Eth = th * (mp - f) + a0 - b2 - (Mp + Dchild)
F1 = th * c + (1 - th) * (d + Dk) + 2 * th * w + th * qt + wo + Bc - (1 - th) * g + ell
F2 = 2 * b2 - (1 - th) * g2 - p2 + t2 + th * V + th * f
check("[A1] E(theta) = A - (1-theta)M - F1(theta) - F2(theta)",
      sp.simplify(Eth - (A - (1 - th) * M - F1 - F2)) == 0)
F1_paper = c / 6 + sp.Rational(5, 6) * (d + Dk) + w / 3 + qt / 6 + wo + Bc - sp.Rational(5, 6) * g + ell
F2_paper = 2 * b2 - sp.Rational(5, 6) * g2 - p2 + t2 + V / 6 + f / 6
check("[A2] at theta = 1/6, F1, F2 equal the paper's (old-eq:2.16)",
      sp.simplify(F1.subs(th, sp.Rational(1, 6)) - F1_paper) == 0
      and sp.simplify(F2.subs(th, sp.Rational(1, 6)) - F2_paper) == 0)
check("[A3] (2.13) M' = M + J - g - g_2 + t_2 does not involve theta",
      sp.simplify(Mp - (M + J - g - g2 + t2)) == 0)
Bd, pp = sp.symbols("B_d p", real=True)
led = (m - A - R / 2 - E) + (pp + s0) + sp.Rational(1, 2) * (A - c + qt + Bc - s0 + A - d + qt + Bd - s0)
check("[A4] first-transform ledger = M + (B_c + B_d - (c+d-2p-R))/2, theta-free",
      sp.simplify(led - (M + (Bc + Bd - (c + d - 2 * pp - R)) / 2)) == 0)
diag = (K + g - ell - s0) - (a0 + qt + wo + w + Bc - s0)
check("[A5] (2.12) diagonal excess = (A-M) - d - Dk - w_o - B_c + g - ell, theta-free",
      sp.simplify(diag - ((A - M) - d - Dk - wo - Bc + g - ell)) == 0)
F1_Jpos = sp.simplify(F1.subs({g: J, ell: 0}))
check("[A6] J >= 0 branch (g = J, ell = 0): F1 = c + 2w + theta(q~ + w_o) + B_c for every theta",
      sp.simplify(F1_Jpos - (c + 2 * w + th * qt + th * wo + Bc)) == 0)
F1_Jneg = sp.simplify(F1.subs({g: 0, ell: 0, w: 0, wo: 0, Dk: 0}))
print("   J < 0 branch (g = ell = w = Dk = 0): F1 =", F1_Jneg)


# --------------------------------------------------------------------------------------------
print("\n=== [B] first transform: allowance B_c and the coefficient kappa_1 ===")
# Local model at one common prime of the first transform with multiplicities i = v_p(C), j = v_p(D).
#   r = 1 if n does not divide i - j (prime in the conductor r of xi_r; paper l. 13210-13220)
#   budget for B_c + B_d (old-eq:2.6):  i + j - 2 - r
#   J < 0 branch, worst case E = 0, q = 0:  F1 >= theta i + (1-theta) j + theta r + B_c (+ forcing)
#   forcing (NOT used in the paper): the C-norm child character contains chi_p^{1 + (i - j)} at p | r
#   (tau_C(a) = tau(a) chi_a(e r) xi_r(a), l. 13228; xi_r = prod chi_p^{i-j}; cubic/sextic
#   reciprocity turns chi_a(p) into chi_p(a) up to a fixed-ray phase).  An exceptional child row
#   needs v_p(h') = -(1 + i - j) mod n, so h_0 contains p^{that residue}: count saving theta*residue.
#   D side: exponent 1 - (i - j).


def kappa_local(i, j, n, forcing):
    th_ = Fr(1, n)
    r = 1 if (i - j) % n else 0
    fC = ((-(1 + i - j)) % n) if (forcing and r) else 0
    fD = ((-(1 + j - i)) % n) if (forcing and r) else 0
    aC = th_ * i + (1 - th_) * j + th_ * r + th_ * fC
    aD = th_ * j + (1 - th_) * i + th_ * r + th_ * fD
    b = i + j - 2 - r
    # largest kappa with (kappa i - aC)_+ + (kappa j - aD)_+ <= b   (piecewise linear, increasing)
    k1, k2 = aC / i, aD / j
    lo, hi = min(k1, k2), max(k1, k2)
    # on [lo, hi] only one term is active
    if b == 0:
        return lo
    # first segment: one active term with slope s1
    s1 = i if k1 <= k2 else j
    kap = lo + Fr(b, s1)
    if kap <= hi:
        return kap
    # both active beyond hi
    used = s1 * (hi - lo)
    return hi + (b - used) / (i + j)


def kappa1(n, forcing, N=120):
    best, arg = None, None
    for i in range(1, N):
        for j in range(1, N):
            k = kappa_local(i, j, n, forcing)
            if best is None or k < best:
                best, arg = k, (i, j)
    return best, arg


K1 = {}
for n in (6, 3, 2):
    for forcing in (False, True):
        k, arg = kappa1(n, forcing)
        K1[(n, forcing)] = k
        print("   n=%d forcing at r-primes=%-5s  kappa_1 = %s  (first minimiser (i,j) = %s)" % (n, forcing, k, arg))
check("[B1] sextic, paper bookkeeping (no forcing): kappa_1 = 2/3 at (i,j) = (2,1)", K1[(6, False)] == Fr(2, 3))
check("[B2] cubic, mechanical transfer (no forcing): kappa_1 = 5/6 < 1", K1[(3, False)] == Fr(5, 6))
check("[B3] cubic with forcing at r-primes: kappa_1 >= 1", K1[(3, True)] >= 1)
check("[B4] quadratic: kappa_1 >= 1 already without forcing", K1[(2, False)] >= 1)

# the paper's sextic B_c = ((3c - 5d - R)/6)_+ gives F1 >= 2c/3 locally, i.e. reproduces kappa_1 = 2/3
ok = True
for i in range(1, 150):
    for j in range(1, 150):
        r = 1 if (i - j) % 6 else 0
        Bl = pos(Fr(3 * i - 5 * j - r, 6))
        if Fr(i, 6) + Fr(5 * j, 6) + Fr(r, 6) + Bl < Fr(2, 3) * i:
            ok = False
check("[B5] paper's sextic B_c gives F1 >= (2/3) c prime by prime (J<0 branch), i,j < 150", ok)

# explicit cubic allowance with forcing: beta_C = (i - a_C)_+, beta_D = (j - a_D)_+; check budget


def cubic_beta(i, j, forcing):
    th_ = Fr(1, 3)
    r = 1 if (i - j) % 3 else 0
    fC = ((-(1 + i - j)) % 3) if (forcing and r) else 0
    fD = ((-(1 + j - i)) % 3) if (forcing and r) else 0
    aC = th_ * i + (1 - th_) * j + th_ * r + th_ * fC
    aD = th_ * j + (1 - th_) * i + th_ * r + th_ * fD
    return pos(i - aC), pos(j - aD), i + j - 2 - r


bad = [(i, j) for i in range(1, 200) for j in range(1, 200)
       if sum(cubic_beta(i, j, True)[:2]) > cubic_beta(i, j, True)[2]]
check("[B6] cubic allowance beta_C=(i-a_C)_+, beta_D=(j-a_D)_+ fits budget i+j-2-r, all i,j<200 (forcing)", not bad)
tight = [(i, j) for i in range(1, 8) for j in range(1, 8)
         if sum(cubic_beta(i, j, True)[:2]) == cubic_beta(i, j, True)[2]]
print("   zero-budget-slack configurations (i,j < 8) with forcing:", tight)
bC, bD, bud = cubic_beta(2, 1, False)
print("   cubic (2,1) without forcing: needs beta_C = %s, beta_D = %s, budget = %s" % (bC, bD, bud))
check("[B7] cubic (2,1) without forcing: need exceeds budget by exactly 1/3 (log P units)", bC + bD - bud == Fr(1, 3))


# --------------------------------------------------------------------------------------------
print("\n=== [C] second transform: F2 >= kappa_2 b_2 ===")
# local values (paper l. 13740-13788, 14349-14380, 14504-14524) for order n:
#  equal i, n !| i, unit:     b2=i, g2=i, p2=1, t2=1, V=0
#  equal i, n !| i, nonunit:  b2=i, g2=i, p2=1, t2=0, V=1
#  equal i, n | i:            b2=i, g2=i, p2=1, t2=0, V=0
#  unequal i > j0, n | j0:    b2=(i+j0)/2, g2=j0, p2=1, t2=V=0
# forcing variants for the exceptional count saving f (in log-P units):
#  'none'  : f = 0
#  'i1'    : nonunit i = 1 only, residue -(i+1) mod n   (paper's device; for n = 6 the paper uses
#            the weaker 2 instead of the true residue 4, giving the same theta*f = 1/3)
#  'full'  : nonunit residue -(i+1) mod n, unit residue -i mod n (all equal n !| i primes)


def F2_table(n, variant, N=120):
    th_ = Fr(1, n)
    rows = []
    for i in range(1, N):
        if i % n:
            for unit in (True, False):
                t2_, V_ = (1, 0) if unit else (0, 1)
                if variant == "none":
                    f_ = 0
                elif variant == "i1":
                    f_ = ((-(i + 1)) % n) if (not unit and i == 1) else 0
                    if n == 6 and f_:
                        f_ = 2
                else:
                    f_ = ((-i) % n) if unit else ((-(i + 1)) % n)
                F = 2 * i - (1 - th_) * i - 1 + t2_ + th_ * V_ + th_ * f_
                rows.append((F / i, ("unit" if unit else "nonunit", i), F, i))
        else:
            F = 2 * i - (1 - th_) * i - 1
            rows.append((F / i, ("n|i", i), F, i))
        for j0 in range(n, i, n):
            b = Fr(i + j0, 2)
            F = 2 * b - (1 - th_) * j0 - 1
            rows.append((F / b, ("uneq", i, j0), F, b))
    return min(rows, key=lambda x: x[0])


K2 = {}
for n in (6, 3, 2):
    for variant in ("none", "i1", "full"):
        k, where, F, b = F2_table(n, variant)
        K2[(n, variant)] = k
        print("   n=%d forcing=%-4s kappa_2 = %s at %s" % (n, variant, k, where))
check("[C1] sextic, paper's device: kappa_2 = 2/3 (paper's F2 >= 2b2/3, tight at nonunit i=1)", K2[(6, "i1")] == Fr(2, 3))
check("[C2] cubic with the paper's i=1 device (residue 1 mod 3): kappa_2 = 1", K2[(3, "i1")] == 1)
check("[C3] cubic without forcing: kappa_2 = 2/3 < 1", K2[(3, "none")] == Fr(2, 3))
check("[C4] quadratic: kappa_2 = 1 (residue -(1+1) = 0 mod 2: no forcing exists or is needed)", K2[(2, "i1")] == 1)
check("[C5] cubic, full forcing still has kappa_2 = 1 (tight at nonunit i=2 and equal i=3)", K2[(3, "full")] == 1)


# --------------------------------------------------------------------------------------------
print("\n=== [D] comparison window, deficit at A = M, failing range, self-consistent loss ===")
# Requirements (M = 1, zero-slot core A in ((1-theta), 1]):
#   comparison:  M - A + 2L <= (1 - theta) M + eta     ->  L <= (A - theta + eta)/2
#   centred:     max_v [A - (1-theta) - kappa v - (L - v)_+] = A - (1-theta) - min(kappa,1) L <= eta
# (for v <= L the bracket is A-(1-theta)-L+(1-kappa)v; for v >= L it is A-(1-theta)-kappa v).


def window(n, kap):
    th_ = Fr(1, n)
    k = min(kap, Fr(1))
    lowM = th_ / k                       # needed L at A = M (eta = 0)
    upM = (1 - th_) / 2                  # allowed L at A = M
    deficit = pos(th_ - k * (1 - th_) / 2)
    Astar = (2 * (1 - th_) - th_ * k) / (2 - k)   # largest A with nonempty window (eta = 0)
    eta = pos((2 * th_ - k * (1 - th_)) / (2 + k))
    return lowM, upM, deficit, Astar, eta


cases = [("sextic, paper (kappa=2/3)", 6, Fr(2, 3)),
         ("cubic, mechanical (kappa=5/6)", 3, Fr(5, 6)),
         ("cubic, paper devices only (kappa=min(5/6,1))", 3, min(K1[(3, False)], K2[(3, "i1")])),
         ("cubic + r-prime forcing (kappa=1)", 3, Fr(1)),
         ("quadratic (kappa=1)", 2, Fr(1))]
W = {}
for name, n, kap in cases:
    lowM, upM, deficit, Astar, eta = window(n, kap)
    W[name] = (lowM, upM, deficit, Astar, eta)
    print("   %-46s threshold (1-theta)M = %s M; at A=M need L >= %s M, allowed L <= %s M; "
          "deficit %s M; window empty for A > %s M; self-consistent eta = %s"
          % (name, 1 - Fr(1, n), lowM, upM, deficit, Astar if Astar <= 1 else ">M", eta))
check("[D1] sextic: window at A = M is [1/4, 5/12] (paper's L = M/4 at its lower end)",
      W[cases[0][0]][:2] == (Fr(1, 4), Fr(5, 12)) and W[cases[0][0]][2] == 0)
check("[D2] cubic kappa=5/6: window empty for A > 19M/21; deficit M/18 at A = M; eta = 2/51",
      W[cases[1][0]][3] == Fr(19, 21) and W[cases[1][0]][2] == Fr(1, 18) and W[cases[1][0]][4] == Fr(2, 51))
check("[D3] cubic kappa=1: window at A = M is the single point L = M/3; deficit 0",
      W[cases[3][0]][0] == W[cases[3][0]][1] == Fr(1, 3) and W[cases[3][0]][2] == 0)
check("[D4] quadratic: window empty for A > M/2; deficit M/4 at A = M; eta = 1/6",
      W[cases[4][0]][3] == Fr(1, 2) and W[cases[4][0]][2] == Fr(1, 4) and W[cases[4][0]][4] == Fr(1, 6))
# critical order: window at A=M nonempty for some kappa <= 1 iff theta <= (1-theta)/2 iff n >= 3
check("[D5] with kappa <= 1 the A = M window is nonempty iff theta <= 1/3 (n >= 3); n = 3 is critical",
      all((Fr(1, n) <= (1 - Fr(1, n)) / 2) == (n >= 3) for n in range(2, 13)))
# consistency: principal rows of the full ball, Z^{theta m + A}, fit Z^M exactly at the threshold
check("[D6] full-ball principal rows Z^{theta M + A} <= Z^M  <=>  A <= (1-theta)M (q = 0)",
      all(Fr(1, n) + (1 - Fr(1, n)) == 1 for n in (2, 3, 6)))


# --------------------------------------------------------------------------------------------
print("\n=== [E] Gauss-row zero h = 0 (paper l. 13572-13594) ===")
# G(u,0) = 0 unless u is an n-th power; |G(u,0)| <= q_u^{1/2}; count of n-th powers u with s | u
# on the shell is <= Y^{1/n} / q_s.  Contribution exponent 2 a0/n - 2 s0 (refined) or 2 a0/n
# (paper's count without /q_s, using s0 <= a0/n); allowance a0 - s0.
for n in (6, 3, 2):
    ok_ref, ok_crude = True, True
    for a in range(0, 61):
        a0_ = Fr(a, 4)
        for s in range(0, 61):
            s0_ = Fr(s, 4)
            if s0_ > a0_ / n:
                continue
            if 2 * a0_ / n - 2 * s0_ > a0_ - s0_:
                ok_ref = False
            if 2 * a0_ / n > a0_ - s0_:
                ok_crude = False
    print("   n=%d: refined count fits = %s; paper's cruder count fits = %s" % (n, ok_ref, ok_crude))
    if n == 3:
        check("[E1] cubic Gauss-row zero fits the allowance (crude count tight at s0 = a0/3)", ok_ref and ok_crude)
    if n == 2:
        check("[E2] quadratic Gauss-row zero fits only with the refined count", ok_ref and not ok_crude)


# --------------------------------------------------------------------------------------------
print("\n=== [F] explicit cubic paths at A = M = m (q = 0), L = M/3 ===")
Mv = Fr(1)
th3 = Fr(1, 3)
# generic path: no common support in either transform.  K = 2A - m, m' = 2A - K = m (minus sigma)
Aa, Lc = Mv, Mv / 3
mprime = 2 * Aa - (2 * Aa - Mv)
excess_generic = th3 * mprime + Aa - Lc - mprime            # count + volume - centred saving - allowance M'
print("   generic: exceptional count M/3, volume A, saving L, allowance M -> excess", excess_generic, "(+2 sigma/3)")
check("[F1] generic cubic path at A = M, L = M/3 has excess exactly 0", excess_generic == 0)
# (2,1) path: every first-transform common prime has v_p(C)=2, v_p(D)=1; c = 2p, d = p, R = p, E = 0.
for pv in (Fr(1, 6), Fr(1, 12), Fr(1, 4)):
    cc, dd, RR = 2 * pv, pv, pv
    K0v = 2 * Aa - cc - dd + RR - Mv
    a0v = Aa - cc
    mpv = 2 * a0v - K0v                                      # g = sigma ignored
    qpv = RR
    Mpv = mpv + qpv
    led1 = (Mv - Aa - RR / 2) + pv + ((Aa - cc + RR) + (Aa - dd + RR)) / 2 - Mv
    exc_no = th3 * mpv + a0v - Mpv - pos(Lc - cc)
    exc_yes = th3 * (mpv - RR) + a0v - Mpv - pos(Lc - cc)
    print("   (2,1) path p=%s: first-transform ledger slack %s; exceptional excess without forcing %s, with forcing %s"
          % (pv, led1, exc_no, exc_yes))
    if pv == Fr(1, 6):
        check("[F2] (2,1) path, c = M/3: excess M/18 without r-forcing, 0 with it", exc_no == Fr(1, 18) and exc_yes == 0)


# --------------------------------------------------------------------------------------------
print("\n=== [G] grid confirmation of [D] (exact Fractions) ===")


def grid_deficit(n, kap, A_):
    th_ = Fr(1, n)
    best = None
    Lmax = (A_ - th_) / 2
    for t in range(0, 241):
        L_ = Lmax * Fr(t, 240)
        worst = max(A_ - (1 - th_) - kap * v - pos(L_ - v) for v in [Fr(k, 240) for k in range(0, 481)])
        worst -= pos(A_ - 1)
        best = worst if best is None else min(best, worst)
    return best


g1 = grid_deficit(3, Fr(5, 6), Fr(1))
g2 = grid_deficit(3, Fr(1), Fr(1))
g3 = grid_deficit(2, Fr(1), Fr(1))
g4 = grid_deficit(6, Fr(2, 3), Fr(1))
print("   min_L max_v deficit at A = M: cubic 5/6 -> %s, cubic 1 -> %s, quadratic -> %s, sextic -> %s" % (g1, g2, g3, g4))
check("[G1] grid reproduces deficits 1/18, 0, 1/4, <=0", g1 == Fr(1, 18) and g2 == 0 and g3 == Fr(1, 4) and g4 <= 0)

print("\nSUMMARY: %d/%d checks passed" % (sum(x for _, x in results), len(results)))
