"""lemma18_ledger.py -- symbolic / exhaustive checks of the exponent ledgers in the proof of
Lemma 18.1 (lem:plain) of the OpenAI QRH manuscript (30 Sep 2026, PR 908 import, paper.tex).

Checks only the displayed affine identities and finite local inequalities; it does not check that the
ledgers are the right ones (i.e. that each displayed exponent correctly describes the analysis).
Line numbers refer to paper.tex at pr908 (git show pr908:standalone/.../build/paper.tex).

Run: python3 -I lemma18_ledger.py
"""
from fractions import Fraction as Fr
import itertools
import sympy as sp

ok = []


def check(name, cond):
    ok.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


A, c, d, R, E, m, q, w, wo, g, ell, Bc, Dk, g2, t2, V, p2, b2, f, s0, sig, z, kap = sp.symbols(
    "A c d R E m q w w_o g ell B_c Dk g_2 t_2 V p_2 b_2 f s_0 sigma z kappa", real=True)
M = m + q
qt = q + R + E                                  # q-tilde (l. 13278)
K0 = 2 * A - c - d + R + E - m                  # (old-eq:2.3), l. 13284
K = K0 - Dk                                     # Dk = K0 - K
a0 = A - c - w                                  # l. 13417
J = d - c + Dk - 2 * w + wo                     # (old-eq:2.8), l. 13444
mp = 2 * a0 - K - g - g2 - V                    # (old-eq:2.13), l. 13793
qp = qt + wo + t2 + V
Mp = mp + qp

# (old-eq:2.13): M' = M + J - g - g2 + t2
check("(2.13) M' = M + J - g - g_2 + t_2   [l.13790-13797]", sp.simplify(Mp - (M + J - g - g2 + t2)) == 0)

# (old-eq:2.12): diagonal exponent minus allowance
lhs = (K + g - ell - s0) - (a0 + qt + wo + w + Bc - s0)
rhs = (A - M) - d - Dk - wo - Bc + g - ell
check("(2.12) diagonal ledger identity   [l.13642-13649]", sp.simplify(lhs - rhs) == 0)

# (old-eq:2.14)/(old-eq:2.15)-(2.16): exceptional ledger identity
Dchild = b2 - p2 + w + Bc + ell
lhs = (mp - f) / 6 + a0 - b2 - (Mp + Dchild)
F1 = c / 6 + sp.Rational(5, 6) * (d + Dk) + w / 3 + qt / 6 + wo + Bc - sp.Rational(5, 6) * g + ell
F2 = 2 * b2 - sp.Rational(5, 6) * g2 - p2 + t2 + V / 6 + f / 6
rhs = A - sp.Rational(5, 6) * M - F1 - F2
check("(2.15)-(2.16) exceptional excess = A - 5M/6 - F1 - F2   [l.14436-14449]", sp.simplify(lhs - rhs) == 0)
mid = a0 - 2 * b2 + p2 - w - Bc - ell - sp.Rational(5, 6) * mp - qp - f / 6
check("(2.15) intermediate form   [l.14455-14457]", sp.simplify(lhs - mid) == 0)

# (old-eq:3.14)
Ap = A - c - w - sp.Symbol("c_2")
c2 = sp.Symbol("c_2")
lhs = (Ap - Mp) - (A - M)
rhs = g + w - d - c2 - Dk - wo + g2 - t2
check("(3.14) (A'-M')-(A-M) identity   [l.14184-14189]", sp.simplify(lhs - rhs) == 0)

# first-transform ledger (l. 13384-13392)
Bd = sp.Symbol("B_d")
p_ = sp.Symbol("p")
lhs = (m - A - R / 2 - E) + (p_ + s0) + sp.Rational(1, 2) * (A - c + qt + Bc - s0 + A - d + qt + Bd - s0)
rhs = M + sp.Rational(1, 2) * (Bc + Bd - (c + d - 2 * p_ - R))
check("first-transform ledger identity   [l.13384-13392]", sp.simplify(lhs - rhs) == 0)

# (old-eq:2.6) local inequality: at a common prime with multiplicities i >= j >= 1, r = 1_{6 !| i-j}:
#  (3i - 5j - r)_+/6 <= i + j - 2 - r     (only the i side can have a positive local numerator)
bad = [(i, j) for i in range(1, 200) for j in range(1, i + 1)
       if Fr(max(3 * i - 5 * j - (1 if (i - j) % 6 else 0), 0), 6) > i + j - 2 - (1 if (i - j) % 6 else 0)]
check("(2.6) local inequality, all 1<=j<=i<200   [l.13398-13408]", not bad)
# and the j-side numerator (3j - 5i - r) is never positive when i >= j:
check("(2.6) j-side numerator <= 0", all(3 * j - 5 * i - 1 <= 0 for i in range(1, 200) for j in range(1, i + 1)))
# NB the ledger also needs the GLOBAL statement B_c + B_d <= c + d - 2p - R from local ones: B_c is the
# positive part of a SUM of local numerators; positive part of a sum <= sum of positive parts.  OK.

# (old-eq:2.17) F2 >= 2 b2/3 table, prime by prime (units of log-norm)  [l.14504-14524]
fails = []
for i in range(1, 120):
    rows = []
    if i % 6:
        rows.append((Fr(7 * i, 6), i))                                     # equal, unit
        rows.append((Fr(7 * i - 5, 6) + (Fr(1, 3) if i == 1 else 0), i))   # equal, nonunit
    else:
        rows.append((Fr(7 * i, 6) - 1, i))                                 # equal, 6 | i
    for (F2loc, b2loc) in rows:
        if F2loc < Fr(2, 3) * b2loc:
            fails.append(("eq", i, F2loc, b2loc))
    for j0 in range(6, i, 6):                                              # unequal, 6 | j0 < i
        F2loc, b2loc = Fr(i) + Fr(j0, 6) - 1, Fr(i + j0, 2)
        if F2loc < Fr(2, 3) * b2loc:
            fails.append(("uneq", i, j0))
check("(2.17) F2 >= 2b2/3 local table, i<120   [l.14504-14524]", not fails)


# Now recompute the F2 local entries from the definition F2 = 2b2 - 5g2/6 - p2 + t2 + V/6 + f/6,
# using the local values of (b2, g2, p2, t2, V, f) at one common prime with multiplicities (i, j0).
# g2 = log of G_c = (D2, E2): min(i, j0).  p2: radical, 1.  t2: 1 if unit case (equal mult, 6 !| i).
# V: 1 if nonunit (equal mult, 6 !| i) [or a nonunit 6|i prime, which only enlarges]; f = 2 v1: 2 if
# nonunit with i = 1.  Unequal case i > j0 (6 | j0), unit: g2 = j0, t2 = 0, V = 0.
def F2loc(i, j0, unit):
    b2l = Fr(i + j0, 2)
    g2l = min(i, j0)
    p2l = 1
    if i == j0 and i % 6:
        t2l = 1 if unit else 0
        Vl = 0 if unit else 1
        fl = 2 if (not unit and i == 1) else 0
    else:
        t2l, Vl, fl = 0, 0, 0
    return 2 * b2l - Fr(5, 6) * g2l - p2l + t2l + Fr(Vl, 6) + Fr(fl, 6), b2l


mism = []
for i in range(1, 60):
    if i % 6:
        if F2loc(i, i, True)[0] != Fr(7 * i, 6):
            mism.append(("unit", i, F2loc(i, i, True)[0]))
        if F2loc(i, i, False)[0] != Fr(7 * i - 5, 6) + (Fr(1, 3) if i == 1 else 0):
            mism.append(("nonunit", i, F2loc(i, i, False)[0]))
    else:
        if F2loc(i, i, True)[0] != Fr(7 * i, 6) - 1:
            mism.append(("6|i", i, F2loc(i, i, True)[0]))
    for j0 in range(6, i, 6):
        if F2loc(i, j0, True)[0] != Fr(i) + Fr(j0, 6) - 1:
            mism.append(("uneq", i, j0, F2loc(i, j0, True)[0]))
check("(2.17) table entries re-derived from F2 definition (with stated local g2,t2,V,f)", not mism)
if mism:
    print("   first mismatches:", mism[:6])

# (old-eq:2.19): max_{v>=0} [A - 5M/6 - 2v/3 - (L - v)_+] = A - M at v = L = M/4
Mv = sp.Symbol("M", positive=True)
Av = sp.Symbol("A", real=True)
L = Mv / 4
vals = []
for vv in [Fr(k, 400) for k in range(0, 1201)]:
    v = vv * Mv
    pos = sp.Max(L - v, 0)
    vals.append(sp.simplify((Av - sp.Rational(5, 6) * Mv - sp.Rational(2, 3) * v - pos) - (Av - Mv)))
check("(2.19) centered deficit <= A - M on a grid of v in [0, 3M]   [l.14759-14768]",
      all(sp.simplify(x.subs(Mv, 1)) <= 0 for x in vals))

# Comparison margins (old-eq:3.11) and (eq:comparison-uncentered-margin), z = 0 and z > 0
# For z=0: A in (5M/6, M + delta]: A_comp <= 3M/2 - A + xi < 5M/6 - M/6 + xi + ...
Mn = Fr(1)
worst0 = max(Fr(3, 2) * Mn - Ai for Ai in [Fr(5, 6) + Fr(k, 6000) for k in range(1, 1001)])
check("z=0 comparison: A_comp - 5M/6 <= -M/6 (before xi)   [l.12969-12970]", worst0 - Fr(5, 6) <= -Fr(1, 6) + Fr(1, 6000))
# z>0: (6k-1) z <= M - A, A > 5M/6, kappa in [3/4,1]
worst = Fr(-10)
worst2 = Fr(-10)
for kk in [Fr(3, 4) + Fr(k, 40) for k in range(0, 11)]:
    for Ai in [Fr(5, 6) + Fr(k, 600) for k in range(1, 101)]:
        zmax = (1 - Ai) / (6 * kk - 1)
        for zz in [zmax * Fr(t, 20) for t in range(1, 21)]:
            Acomp = Fr(3, 2) - Ai + 2 * zz
            worst = max(worst, Acomp)
            worst2 = max(worst2, Acomp + (6 * kk - 1) * zz)
check("z>0 comparison: A_comp <= 23M/30   [l.12971-12979]", worst <= Fr(23, 30))
check("z>0 comparison: A_comp + (6k-1)z <= 14M/15   [l.12974-12977]", worst2 <= Fr(14, 15))
print("   max A_comp = %s, max A_comp + (6k-1)z = %s (M = 1)" % (worst, worst2))

print("\nSUMMARY: %d/%d checks passed" % (sum(x for _, x in ok), len(ok)))
