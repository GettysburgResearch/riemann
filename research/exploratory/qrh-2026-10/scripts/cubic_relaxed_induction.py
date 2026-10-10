"""cubic_relaxed_induction.py -- relaxed and nested induction ledgers for the cubic transfer of
Lemma 18.1 (lem:plain, case 1, z = 0) of the external, unreviewed OpenAI QRH manuscript
(30 Sep 2026; pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, paper.tex sha256 42a5ee0f...deac6a3),
plus finite local checks in Z[omega] of the PROPOSED (2,1) forcing step.

Status: EXPLORATION.  Nothing here proves a moment bound.  The ledgers are AFFINE EXPONENT MODELS
of the scheme (units of log Z, M = 1 after scaling); they inherit every unverified step of the
paper (common-support bookkeeping l. 13192-13349, 13686-13933, Lemmas smooth-calculus and
kernel-seminorms).

Arithmetic classes:
  [R] [S] [N] [P]      EXACT_RATIONAL (fractions.Fraction; sympy only for identities in [R])
  [L1] [L4] [L5] [L6a] EXACT (residue symbols computed by exact modular exponentiation in Z[omega];
                       character sums recorded as exact counts of cube roots of unity)
  [L2] [L3] [L6b]      FLOATING_RECONNAISSANCE (double-precision additive-character Gauss sums;
                       only zero / nonzero and equality to 1e-9 relative are read off; NOT certified)

Dependencies (read-only imports, not modified):
  cubic_fourth_moment_ledger.py (same folder; imported silently, its 31 checks are re-run and
    must all pass), ../a2/eis.py (exact Eisenstein-integer arithmetic, sextic symbols).

Notation (as in cubic_fourth_moment_ledger.py): theta = 1/n density exponent of n-th powers;
kappa = min(kappa_1, kappa_2, 1) the coefficient in F1 + F2 >= kappa v; s0 = 1 - theta + eta the
relaxed uncentred threshold; a centred stage at total length A with comparison length L needs
    (C)  A - s0 - kappa L <= 0                      (exceptional rows, saving (L - v)_+)
    (R)  A_comp = 1 - A + 2L lies in an already proved range at the SAME width,
plus the caps L <= A/2 (comparison sides >= L) and L <= A - 1/2 (reflected comparison stays in
the padded core).  Single-window ordering (the paper's): proved range = [0, s0].  Nested
ordering (PROPOSED here): proved range = [0, s_k] after k centred stages.

Sections:
  [R] relaxed hypothesis H(M; eta): symbolic step ledger (sympy, reusing the old identities)
  [S] single-window relaxed induction: optimal eta, necessity and sufficiency
  [N] nested comparisons: reach recursion s_k, optimal eta = (theta - kappa/2)_+, margins
  [P] explicit (2,1)-path and generic path along a nested chain
  [L] finite Z[omega] computations for the (2,1) forcing step
  [V] verdict table

Run: python3 -I scripts/cubic_relaxed_induction.py      (about 20 s, single process)
"""
import contextlib
import cmath
import io
import math
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "a2"))

results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def pos(x):
    return x if x > 0 else 0


# ---- import the existing ledger silently (it re-runs its own 31 checks) ---------------------
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import cubic_fourth_moment_ledger as L0  # noqa: E402
import eis  # noqa: E402
import sympy as sp  # noqa: E402

_old = L0.results
check("[0] existing ledger cubic_fourth_moment_ledger.py re-run on import: %d/%d PASS"
      % (sum(x for _, x in _old), len(_old)), all(x for _, x in _old) and len(_old) == 31)

TH3 = Fr(1, 3)
KAP1_MECH = L0.K1[(3, False)]           # 5/6, first transform without (2,1) forcing
KAP1_FORCED = min(L0.K1[(3, True)], 1)  # 1
KAP2_DEVICE = L0.K2[(3, "i1")]          # 1, with the paper's nonunit i = 1 device (residue 1 mod 3)
KAP2_NONE = L0.K2[(3, "none")]          # 2/3, no second-transform forcing at all

SCEN = [  # name, theta, kappa
    ("sextic (paper)", Fr(1, 6), min(L0.K1[(6, False)], L0.K2[(6, "i1")], Fr(1))),
    ("cubic mechanical: kappa1=5/6, nonunit-i=1 device", TH3, min(KAP1_MECH, KAP2_DEVICE, Fr(1))),
    ("cubic, no forcing anywhere: kappa2=2/3", TH3, min(KAP1_MECH, KAP2_NONE, Fr(1))),
    ("cubic + (2,1) forcing", TH3, min(KAP1_FORCED, KAP2_DEVICE, Fr(1))),
    ("quadratic", Fr(1, 2), min(L0.K1[(2, False)], L0.K2[(2, "i1")], Fr(1))),
]
check("[0b] scenario kappas: sextic 2/3, cubic mech 5/6, cubic unforced 2/3, cubic forced 1, quadratic 1",
      [k for _, _, k in SCEN] == [Fr(2, 3), Fr(5, 6), Fr(2, 3), Fr(1), Fr(1)])

# --------------------------------------------------------------------------------------------
print("\n=== [R] relaxed hypothesis H(M; eta): every step's excess over (1+eta) M ===")
eta = sp.symbols("eta", real=True)
M, A, th = L0.M, L0.A, L0.th
# first-transform ledger with relaxed norm targets: N_C <= target_C + x_C (x_C = excess over the
# UNRELAXED target).  Parent exponent - (1+eta)M must equal (budget term + x_C + x_D)/2 - eta M.
xC, xD = sp.symbols("x_C x_D", real=True)
Bc, Bd, pp, s0s, qt, c, d, R, E, m = L0.Bc, L0.Bd, L0.pp, L0.s0, L0.qt, L0.c, L0.d, L0.R, L0.E, L0.m
par = (m - A - R / 2 - E) + (pp + s0s) + sp.Rational(1, 2) * (
    (A - c + qt + Bc - s0s + xC) + (A - d + qt + Bd - s0s + xD))
check("[R1] relaxed first-transform ledger: parent - (1+eta)M = (B_c+B_d-(c+d-2p-R))/2 + (x_C+x_D)/2 - eta M",
      sp.simplify(par - (1 + eta) * M - ((Bc + Bd - (c + d - 2 * pp - R)) / 2 + (xC + xD) / 2 - eta * M)) == 0)
# nonexceptional child: child bound (1+eta)M' + Delta_child -> x = eta M'; average over the two sides
# with M' = M + J - g - g_2 + t_2 (old-eq:2.13): excess eta (M' - M) = eta (J - g - g_2 + t_2) <= -eta sigma
J, g, g2, t2, sig = L0.J, L0.g, L0.g2, L0.t2, sp.symbols("sigma", positive=True)
check("[R2] nonexceptional children: eta M' - eta M = eta (J - g - g_2 + t_2), theta-free (uses [A3])",
      sp.simplify(eta * L0.Mp - eta * M - eta * (J - g - g2 + t2)) == 0)
check("[R2b] with g = J_+ + sigma >= J + sigma and g_2 >= t_2 the child excess is <= -eta sigma (sample grid)",
      all(Fr(e_) * (Fr(j_) - (max(Fr(j_), 0) + Fr(1, 10)) - Fr(gg) + Fr(tt)) <= -Fr(e_) * Fr(1, 10)
          for e_ in (0, Fr(2, 51), Fr(1, 6)) for j_ in (-1, 0, Fr(1, 3)) for gg in (0, Fr(1, 5))
          for tt in (0, Fr(1, 5)) if tt <= gg))
# exceptional rows: excess over the relaxed parent target
check("[R3] exceptional rows: E(theta) - eta M = A - (1-theta+eta)M - F1 - F2 (from [A1])",
      sp.simplify(L0.Eth - eta * M - (A - (1 - th + eta) * M - L0.F1 - L0.F2)) == 0)
check("[R4] diagonal: excess over relaxed target = (A-M) - d - Dk - w_o - B_c + g - ell - eta M (from [A5])",
      sp.simplify(L0.diag - eta * M - ((A - M) - d - L0.Dk - L0.wo - Bc + g - L0.ell - eta * M)) == 0)
print("   zero frequency: m - (1+eta)M <= -eta M;  Gauss-row zero h = 0: [E1], eta-free;"
      "  base M <= rho: terminal")
print("   => H(M;eta) closes iff (U) uncentred: A <= (1-theta+eta)M, and (C)+(R) at every centred A.")


# --------------------------------------------------------------------------------------------
print("\n=== [S] single-window ordering (paper's): comparisons call only the uncentred stage ===")


def eta_single(theta, kap):
    k = min(kap, Fr(1))
    return pos((2 * theta - k * (1 - theta)) / (2 + k))


def window_single(theta, kap, eta_, A_):
    """[L_lo, L_hi] at total length A_ (units of M) for the single-window ordering."""
    k = min(kap, Fr(1))
    s0 = 1 - theta + eta_
    lo = pos((A_ - s0) / k)
    hi = min((A_ - theta + eta_) / 2, A_ / 2)
    return lo, hi


for name, theta, kap in SCEN:
    e_ = eta_single(theta, kap)
    lo, hi = window_single(theta, kap, e_, Fr(1))
    print("   %-50s eta_single = %-6s  L at A=M: [%s, %s]  bound X^(%s)" % (name, e_, lo, hi, 1 + e_))
eS = eta_single(TH3, KAP1_MECH)
check("[S1] cubic mechanical (kappa = 5/6): eta_single = 2/51 exactly (matches old [D2])", eS == Fr(2, 51)
      and eS == L0.window(3, Fr(5, 6))[4])
lo, hi = window_single(TH3, KAP1_MECH, eS, Fr(1))
check("[S2] at eta = 2/51 the A = M window is the single point L = 6/17", lo == hi == Fr(6, 17))
ok = True
for t_ in range(1, 2001):
    e2 = eS - Fr(t_, 10 ** 6)
    lo2, hi2 = window_single(TH3, KAP1_MECH, e2, Fr(1))
    if lo2 <= hi2:
        ok = False
check("[S3] necessity: for eta = 2/51 - t/10^6 (t = 1..2000) the A = M window is empty", ok)
ok = True
s0 = 1 - TH3 + eS
for t_ in range(0, 1201):
    A_ = s0 + (1 - s0) * Fr(t_, 1200)
    lo2, hi2 = window_single(TH3, KAP1_MECH, eS, A_)
    if lo2 > hi2:
        ok = False
check("[S4] sufficiency: at eta = 2/51 every A in [s0, M] (1201 exact points) has a nonempty window", ok)
check("[S5] single-window values: no forcing at all (kappa=2/3) -> 1/12; forced -> 0; quadratic -> 1/6; sextic -> 0",
      eta_single(TH3, Fr(2, 3)) == Fr(1, 12) and eta_single(TH3, Fr(1)) == 0
      and eta_single(Fr(1, 2), Fr(1)) == Fr(1, 6) and eta_single(Fr(1, 6), Fr(2, 3)) == 0)
# the forced scheme has zero balanced slack in this ordering (old [D7]); its window at A = M is {1/3}
check("[S6] forced cubic, single window: A = M window is {M/3} (zero slack, old [D3])",
      window_single(TH3, Fr(1), Fr(0), Fr(1)) == (Fr(1, 3), Fr(1, 3)))


# --------------------------------------------------------------------------------------------
print("\n=== [N] nested comparisons (PROPOSED reordering inside a band) ===")
# Stage U proves A <= s0.  Stage C_k proves A in (s_{k-1}, s_k] using comparisons with
# A_comp = 1 - A + 2L <= s_{k-1}.  s_k = max A such that some L satisfies
#   L >= (A - s0)/kappa,  L <= (s_{k-1} - 1 + A)/2,  L <= A/2,  L <= A - 1/2.


def reach_step(theta, kap, eta_, s_prev):
    k = min(kap, Fr(1))
    s0_ = 1 - theta + eta_
    caps = []
    # (a) (A - s0)/k <= (s_prev - 1 + A)/2
    caps.append((s0_ / k + (s_prev - 1) / 2) / (1 / k - Fr(1, 2)))
    # (b) (A - s0)/k <= A/2
    caps.append((s0_ / k) / (1 / k - Fr(1, 2)))
    # (c) (A - s0)/k <= A - 1/2
    if k < 1:
        caps.append((s0_ / k - Fr(1, 2)) / (1 / k - 1))
    elif s0_ < Fr(1, 2):
        caps.append(Fr(-1))
    return max(s_prev, min(caps))


def reach(theta, kap, eta_, kmax=5000, target=Fr(1)):
    s = [1 - theta + eta_]
    while len(s) <= kmax:
        s.append(reach_step(theta, kap, eta_, s[-1]))
        if s[-1] > target or s[-1] == s[-2]:
            break
    return s


def eta_nested(theta, kap):
    return pos(theta - min(kap, Fr(1)) / 2)


for name, theta, kap in SCEN:
    s = reach(theta, kap, Fr(0), kmax=60)
    ok_close = s[-1] > 1
    print("   %-50s eta=0: s = %s%s  closes: %s ; eta_nested = %s"
          % (name, [str(x) for x in s[:4]], " ..." if len(s) > 4 else "", ok_close, eta_nested(theta, kap)))
s_mech = reach(TH3, KAP1_MECH, Fr(0))
check("[N1] cubic mechanical, eta = 0: s0 = 2/3, s1 = 19/21, s2 = 158/147 > 1 (closes after 2 centred stages)",
      s_mech[:3] == [Fr(2, 3), Fr(19, 21), Fr(158, 147)] and s_mech[2] > 1)
s_forced = reach(TH3, Fr(1), Fr(0))
check("[N2] cubic + (2,1) forcing, eta = 0: s1 = 1 exactly (zero slack), s2 = 4/3 (cap L <= A/2)",
      s_forced[:3] == [Fr(2, 3), Fr(1), Fr(4, 3)])
s_unf = reach(TH3, Fr(2, 3), Fr(0), kmax=40)
check("[N3] cubic, no forcing anywhere (kappa = 2/3 = 2 theta), eta = 0: s_k = 1 - (1/3)/2^k < 1 for k <= 40",
      all(s_unf[i] == 1 - Fr(1, 3) / 2 ** i for i in range(len(s_unf))) and max(s_unf) < 1)
stages = []
for e_ in (Fr(1, 100), Fr(1, 1000), Fr(1, 10 ** 4)):
    s = reach(TH3, Fr(2, 3), e_, kmax=200)
    stages.append((e_, len(s) - 1, s[-1] > 1))
print("   cubic unforced (kappa=2/3): (eta, centred stages to pass M, closes) =", [(str(a), b, c) for a, b, c in stages])
check("[N4] cubic unforced: every eta in {1e-2,1e-3,1e-4} closes in finitely many stages (~log2(1/eta))",
      all(cl for _, _, cl in stages) and all(n_ <= 2 + math.ceil(math.log2(1 / float(e_))) for e_, n_, _ in stages))
stq = []
for e_ in (Fr(1, 100), Fr(1, 1000)):
    s = reach(Fr(1, 2), Fr(1), e_, kmax=5000)
    stq.append((e_, len(s) - 1, s[-1] > 1))
print("   quadratic (kappa=1=2 theta): (eta, stages, closes) =", [(str(a), b, c) for a, b, c in stq])
check("[N5] quadratic calibration: eta = 0 never closes (s_k = 1/2), every eta > 0 closes (~1/(4 eta) stages)",
      reach(Fr(1, 2), Fr(1), Fr(0), kmax=10)[-1] == Fr(1, 2) and all(cl for _, _, cl in stq))
check("[N6] sextic: closes after one centred stage at eta = 0 (paper's single window)",
      len(reach(Fr(1, 6), Fr(2, 3), Fr(0))) == 2 and reach(Fr(1, 6), Fr(2, 3), Fr(0))[1] > 1)
# closed form eta_nested = (theta - kappa/2)_+ on a grid of (theta, kappa)
ok = True
for nn in range(2, 9):
    theta = Fr(1, nn)
    for kk in range(4, 13):
        kap = Fr(kk, 12)
        en = eta_nested(theta, kap)
        up = reach(theta, kap, en + Fr(1, 200), kmax=4000)
        if not up[-1] > 1:
            ok = False
        if en > Fr(1, 200):
            dn = reach(theta, kap, en - Fr(1, 200), kmax=4000)
            if dn[-1] > 1:
                ok = False
check("[N7] closed form: closes iff eta > theta - kappa/2 (grid theta = 1/2..1/8, kappa = 1/3..1; +-1/200 test)", ok)


def equalized_margin(theta, kap, depth, A0=Fr(1)):
    """largest mu with a nested chain of `depth` centred stages starting at A0 in which every
    centred inequality (C) and the final uncentred inequality hold with margin mu (eta = 0).
    Minimal L at each level is optimal because A_i is increasing in A_{i-1} and in L_i."""
    k = min(kap, Fr(1))
    s0_ = 1 - theta
    al, be = A0, Fr(0)                     # A_i = al + be * mu
    for _ in range(depth):
        # L = (A - s0 + mu)/k ;  A_next = 1 - A + 2L
        al, be = 1 - al + 2 * (al - s0_) / k, -be + 2 * (be + 1) / k
    mu = (s0_ - al) / (1 + be)
    # rebuild the chain and verify caps
    chain, Acur = [], A0
    for _ in range(depth):
        L_ = (Acur - s0_ + mu) / k
        chain.append((Acur, L_))
        Acur = 1 - Acur + 2 * L_
    caps_ok = all(L_ <= A_ / 2 and L_ <= A_ - Fr(1, 2) + Fr(10 ** -9) * 0 or L_ <= A_ / 2 and A_ - L_ <= 1
                  for A_, L_ in chain)
    return mu, chain, Acur, caps_ok


mus = []
for dpt in (1, 2, 3, 4, 6):
    mu, chain, Aend, caps_ok = equalized_margin(TH3, KAP1_MECH, dpt)
    mus.append(mu)
    print("   cubic mechanical, depth %d: best uniform margin mu = %s (= %.4f M); chain (A, L) = %s -> A_end = %s"
          % (dpt, mu, float(mu), [(str(a), str(l)) for a, l in chain][:3], Aend))
check("[N8] cubic mechanical equalized margins at A = M: depth 1 -> -2/51 (old balanced slack), depth 2 -> 11/507",
      mus[0] == -Fr(2, 51) and mus[1] == Fr(11, 507))
check("[N9] margins increase with depth and stay below the limit kappa/2 - theta = 1/12",
      all(mus[i] < mus[i + 1] for i in range(len(mus) - 1)) and all(x < Fr(1, 12) for x in mus))
# explicit, simple chain at A = M (and at A = M + delta with delta = 1/100)
for A_top in (Fr(1), Fr(101, 100)):
    L1, L2 = Fr(21, 50), Fr(23, 100)
    A1 = 1 - A_top + 2 * L1
    A2 = 1 - A1 + 2 * L2
    cC1 = A_top - Fr(2, 3) - KAP1_MECH * L1
    cC2 = A1 - Fr(2, 3) - KAP1_MECH * L2
    cU = A2 - Fr(2, 3)
    caps = (L1 <= A_top / 2, L1 <= A_top - Fr(1, 2), L2 <= A1 / 2, L2 <= A1 - Fr(1, 2), L2 <= min(L1, 1 - A_top + L1))
    print("   explicit chain from A = %s: L1 = 21/50 -> A_comp = %s; L2 = 23/100 -> A_comp' = %s;"
          " margins (C1, C2, U) = (%s, %s, %s); caps %s" % (A_top, A1, A2, cC1, cC2, cU, all(caps)))
    if A_top == 1:
        check("[N10] explicit chain at A = M: (C1) -1/60, (C2) -1/120, uncentred end 31/50 <= 2/3 - 7/150, caps hold",
              cC1 == -Fr(1, 60) and cC2 == -Fr(1, 120) and A2 == Fr(31, 50) and cU == -Fr(7, 150) and all(caps))
    else:
        check("[N11] the same L1, L2 still work at A = M + 1/100 (all margins < 0, caps hold)",
              cC1 < 0 and cC2 < 0 and cU < 0 and all(caps))


# --------------------------------------------------------------------------------------------
print("\n=== [P] explicit paths along the nested chain (no (2,1) forcing) ===")
# (2,1) path model of old [F2]: all first-transform common primes of type (2,1), radical P:
# c = 2P, d = P, R = P, q = E = 0, no second common support.  Exceptional excess at total A with
# comparison length L:  exc = A - 2/3 - F1 - (L - c)_+,  F1 = c/3 + 2d/3 + R/3 = 5P/3.


def exc21(A_, L_, P_, forcing=False):
    c_, d_, R_ = 2 * P_, P_, P_
    K0 = 2 * A_ - c_ - d_ + R_ - 1
    a0 = A_ - c_
    mp = 2 * a0 - K0
    Mp = mp + R_
    f_ = R_ if forcing else 0
    return TH3 * (mp - f_) + a0 - Mp - pos(L_ - c_)


worst = []
for (A_, L_) in ((Fr(1), Fr(21, 50)), (Fr(21, 25), Fr(23, 100))):
    vals = [exc21(A_, L_, Fr(t_, 2400)) for t_ in range(0, 1201)]
    worst.append(max(vals))
    print("   stage at A = %s, L = %s: max over P of (2,1)-path exceptional excess = %s" % (A_, L_, max(vals)))
check("[P1] (2,1)-path excess <= 0 at both nested stages without forcing (max -1/60 and -1/120)",
      worst == [-Fr(1, 60), -Fr(1, 120)])
check("[P2] (2,1)-path with the paper's own single window (A=M, L=1/3) still has +1/18 (old [F2])",
      max(exc21(Fr(1), Fr(1, 3), Fr(t_, 2400)) for t_ in range(0, 1201)) == Fr(1, 18))
gen = [TH3 * 1 + A_ - L_ - 1 for (A_, L_) in ((Fr(1), Fr(21, 50)), (Fr(21, 25), Fr(23, 100)))]
check("[P3] generic path (no common support) at the two stages: excess -3/50 and -1/30 (old [F1] had 0 at L=1/3)",
      gen == [-Fr(3, 50), -Fr(1, 30)])


# --------------------------------------------------------------------------------------------
print("\n=== [L] finite computations in Z[omega] for the (2,1) forcing step ===")
mul, conj, norm = eis.mul, eis.conj, eis.norm
PR = eis.primes_upto(400)
byN = {}
for q_ in PR:
    byN.setdefault(norm(q_), []).append(q_)


def c3(u, p):
    """cubic residue symbol (u/p)_3 as exponent in Z/3 (value zeta_3^e), None if p | u.
    (u/p)_3 = (u/p)_6^2 and zeta_6^(2k) = zeta_3^k."""
    k = eis.sym_prime(u, p)
    return None if k is None else k % 3


Z3 = [cmath.exp(2j * math.pi * k / 3) for k in range(3)]

# [L1] cubic reciprocity for primary primes
pairs, bad = 0, 0
for i1 in range(len(PR)):
    for i2 in range(len(PR)):
        a_, p_ = PR[i1], PR[i2]
        if a_ == p_ or norm(a_) == norm(p_) and a_ == conj(p_) and False:
            continue
        if a_ == p_:
            continue
        x1, x2 = c3(a_, p_), c3(p_, a_)
        if x1 is None or x2 is None:
            continue
        pairs += 1
        if x1 != x2:
            bad += 1
check("[L1] cubic reciprocity (a/p)_3 = (p/a)_3 for all %d ordered pairs of distinct primary primes, norm <= 400" % pairs,
      bad == 0 and pairs > 1000)

p7, p13, p19 = byN[7][0], byN[13][0], byN[19][0]


def residues(n):
    R_, N_ = eis.residues(n)
    assert N_ == norm(n)
    return R_


def divides_pow(p, t, z):
    n = (1, 0)
    for _ in range(t):
        n = mul(n, p)
    return eis.divides(n, z)


def vp(z, p, cap=8):
    if z == (0, 0):
        return 10 ** 6
    t = 0
    while t < cap and divides_pow(p, t + 1, z):
        t += 1
    return t


# [L2] cubic prime-power Gauss sums: eq:gauss-local with 6 -> 3 (FLOATING)
ok = True
for p_, amax in ((p7, 3), (p13, 2)):
    P_ = norm(p_)
    for a in range(1, amax + 1):
        n = (1, 0)
        for _ in range(a):
            n = mul(n, p_)
        Rn = residues(n)
        chi = {x: c3(x, p_) for x in Rn}
        for k_ in Rn:
            s_ = 0
            for x in Rn:
                if chi[x] is None:
                    continue
                s_ += Z3[(a * chi[x]) % 3] * eis.e_of(mul(k_, x), n)
            G = s_ / math.sqrt(P_ ** a)
            v = vp(k_, p_)
            if a % 3:
                exp_ = P_ ** ((a - 1) / 2) if v == a - 1 else 0.0
                if abs(abs(G) - exp_) > 1e-8 * max(1, exp_):
                    ok = False
            else:
                exp_ = (P_ ** (a / 2) if v >= a else 0) - (P_ ** (a / 2 - 1) if v >= a - 1 else 0)
                if abs(G - exp_) > 1e-8 * max(1, abs(exp_)):
                    ok = False
check("[L2] cubic eq:gauss-local (6 -> 3) holds at N p = 7 (a = 1,2,3) and N p = 13 (a = 1,2)  [FLOATING]", ok)

# [L3] first-transform CRT phase with cubic symbols: modulus r a b, r = p (N 7), a (N 13), b (N 19)
#   T(h) = sum_{k mod pab} xi(k) chi_a(k) conj chi_b(k) e(kh/(pab)),  xi = chi_p^{i-j}, (i,j) = (2,1)
#   claim: T(h) = xi(ab) chi_a(p b) conj chi_b(p a) g_xi(h) g_a(h) conj g_b(-h)       (FLOATING)
eij = 1  # i - j at a (2,1) prime
pab = mul(mul(p7, p13), p19)
Rpab = residues(pab)


def gsum(mod_res, mod, chifun, h):
    s_ = 0
    for x in mod_res:
        e_ = chifun(x)
        if e_ is None:
            continue
        s_ += Z3[e_ % 3] * eis.e_of(mul(h, x), mod)
    return s_


def chi_xi(x):
    e_ = c3(x, p7)
    return None if e_ is None else (eij * e_) % 3


def chi_a(x):
    return c3(x, p13)


def chi_b_conj(x):
    e_ = c3(x, p19)
    return None if e_ is None else (-e_) % 3


def psi(x):
    e1, e2, e3 = chi_xi(x), chi_a(x), chi_b_conj(x)
    if e1 is None or e2 is None or e3 is None:
        return None
    return (e1 + e2 + e3) % 3


Rp, Ra, Rb = residues(p7), residues(p13), residues(p19)
hs = [(1, 0), (2, 1), (3, -1), mul(p7, (1, 1)), (5, 7), mul(p13, (2, 0))]
ok, maxdev = True, 0.0
for h in hs:
    T = gsum(Rpab, pab, psi, h)
    ph = (eij * c3(mul(p13, p19), p7) + c3(mul(p7, p19), p13) - c3(mul(p7, p13), p19)) % 3
    gx = gsum(Rp, p7, chi_xi, h)
    ga = gsum(Ra, p13, chi_a, h)
    gb = gsum(Rb, p19, lambda x: c3(x, p19), (-h[0], -h[1]))
    rhs = Z3[ph] * gx * ga * gb.conjugate()
    dev = abs(T - rhs) / max(1.0, abs(rhs))
    maxdev = max(maxdev, dev)
    if dev > 1e-9:
        ok = False
check("[L3] cubic CRT phase of the first-transform bridge: T = xi(ab) chi_a(pb) conj chi_b(pa) g_xi g_a conj g_b(-h)"
      " (6 frequencies, max rel dev %.1e)  [FLOATING]" % maxdev, ok)
#   consequence: a-dependence of the C side at p is xi(a) chi_a(p) = (a/p)^(i-j) (p/a) = (a/p)^(1+i-j)
ok = True
for a_ in PR:
    if norm(a_) in (7,) or a_ == p7:
        continue
    lhs = (eij * c3(a_, p7) + c3(p7, a_)) % 3
    if lhs != ((1 + eij) * c3(a_, p7)) % 3:
        ok = False
check("[L3b] C-side character at a (2,1) prime: xi(a) chi_a(p) = chi_p(a)^(1+i-j) = chi_p(a)^2 for all primes a, N a <= 400", ok)

# [L4] full correlation F(u,v;j) for coprime primes u, v (EXACT): F = chi_u(j) conj chi_v(-j) * const,
#      the constant conj chi_u(v) chi_v(u) = 1 by cubic reciprocity.  Fixes the child sign: chi_u(j).
u_, v_ = p13, p19
Ru, Rv = residues(u_), residues(v_)
Ruv = residues(mul(u_, v_))
ok, nchk = True, 0
for j in Ruv[:120]:
    cnt = [0, 0, 0]
    for x in Ru:
        for y in Rv:
            z = (mul(v_, x)[0] - mul(u_, y)[0] - j[0], mul(v_, x)[1] - mul(u_, y)[1] - j[1])
            if eis.divides(mul(u_, v_), z):
                ex, ey = c3(x, u_), c3(y, v_)
                if ex is None or ey is None:
                    continue
                cnt[(ex - ey) % 3] += 1
    ej, emj = c3(j, u_), c3((-j[0], -j[1]), v_)
    if ej is None or emj is None:
        if sum(cnt) != 0:
            ok = False
        continue
    target = (ej - emj) % 3
    nchk += 1
    if cnt != [1 if r_ == target else 0 for r_ in range(3)]:
        ok = False
check("[L4] full correlation (cubic, coprime primes): F(u,v;j) = chi_u(j) conj chi_v(-j) exactly, %d frequencies" % nchk,
      ok and nchk >= 100)

# [L5] forced residue: the child u-character at a (2,1) prime p is u -> chi_p(u)^(1+i-j) chi_u(j).
#      For j = p^t it is trivial on every prime u iff t = -(1+i-j) = 1 (mod 3).  (EXACT symbols)
ok = True
table = {}
for t in range(0, 7):
    jt = (1, 0)
    for _ in range(t):
        jt = mul(jt, p7)
    trivial = True
    for uu in PR:
        if uu == p7:
            continue
        ex = ((1 + eij) * c3(uu, p7) + (c3(jt, uu) if t else 0)) % 3
        if ex != 0:
            trivial = False
            break
    table[t] = trivial
    if trivial != (t % 3 == 1):
        ok = False
print("   (2,1) prime, child row j = p^t: u-character principal?", table)
check("[L5] (2,1) forcing: the child u-character is unramified at p iff v_p(j) = 1 (mod 3) (t = 0..6, all u, N u <= 400)", ok)
# residue table for the C and D sides (i, j < 6), p in r iff 3 does not divide i - j
tab = {}
for i in range(1, 6):
    for jj in range(1, 6):
        if (i - jj) % 3 == 0:
            continue
        tab[(i, jj)] = ((-(1 + i - jj)) % 3, (-(1 - (i - jj))) % 3)
print("   forced residues (C side, D side) at r-primes:", tab)
check("[L5b] C side forced residue is 1 exactly when i - j = 1 (mod 3) (types (2,1), (5,1), (3,2), (1,3), ...)",
      all((tab[k][0] == 1) == ((k[0] - k[1]) % 3 == 1) for k in tab))

# [L6] Z[omega]/p^2 at a (2,1) prime: row character chi_{p^2}(k) conj chi_p(k) equals chi_p(k) (EXACT) and its
#      Gauss sum mod p^2 vanishes unless p | h, where it is N(p) g_p(h/p) (FLOATING): effective modulus p.
p2 = mul(p7, p7)
Rp2 = residues(p2)
ok_exact = all((c3(x, p7) is None) or ((2 * c3(x, p7) - c3(x, p7)) % 3 == c3(x, p7)) for x in Rp2)
check("[L6a] chi_{p^2}(k) conj chi_p(k) = chi_p(k) on all of Z[omega]/p^2 (N p = 7)", ok_exact)
ok = True
for h in Rp2:
    G2 = gsum(Rp2, p2, lambda x: (None if c3(x, p7) is None else c3(x, p7)), h)
    if eis.divides(p7, h):
        hq = eis.reduce_mod(h, p2)
        # h = p * h1  ->  sum = N(p) * g_p(h1)
        c_, d_ = mul(hq, conj(p7))
        h1 = (c_ // norm(p7), d_ // norm(p7))
        exp_ = norm(p7) * gsum(Rp, p7, lambda x: c3(x, p7), h1)
        if abs(G2 - exp_) > 1e-8 * max(1, abs(exp_)):
            ok = False
    elif abs(G2) > 1e-8:
        ok = False
check("[L6b] its Gauss sum mod p^2 is 0 unless p | h, and N(p) g_p(h/p) otherwise (all 49 h)  [FLOATING]", ok)


# --------------------------------------------------------------------------------------------
print("\n=== [V] verdict table: exponent theta_X in sum_{N c <= X} |L(1/2, chi_c)|^4 << X^(theta_X + eps) ===")
rows = []
for name, theta, kap in SCEN:
    rows.append((name, 1 + eta_single(theta, kap), 1 + eta_nested(theta, kap),
                 (min(kap, 1) / 2 - theta) if eta_nested(theta, kap) == 0 else None))
for r_ in rows:
    print("   %-50s single-window: X^%-6s nested: X^%-3s nested margin limit at A=M: %s M"
          % (r_[0], r_[1], r_[2], r_[3]))
check("[V1] cubic mechanical: single window X^(53/51); nested X^1 with margin limit M/12",
      rows[1][1] == Fr(53, 51) and rows[1][2] == 1 and rows[1][3] == Fr(1, 12))
check("[V2] cubic, no forcing anywhere: single window X^(13/12); nested X^(1+eps) only in the limit (margin 0)",
      rows[2][1] == Fr(13, 12) and rows[2][2] == 1 and rows[2][3] == 0)
check("[V3] quadratic calibration: single window X^(7/6) (old), nested X^(1+eps) in the limit = Heath-Brown's bound",
      rows[4][1] == Fr(7, 6) and rows[4][2] == 1 and rows[4][3] == 0)

print("\nSUMMARY: %d/%d checks passed" % (sum(x for _, x in results), len(results)))
