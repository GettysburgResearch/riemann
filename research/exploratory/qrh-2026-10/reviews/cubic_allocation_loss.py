"""cubic_allocation_loss.py -- EXACT re-instantiation at n = 3 of the complete-common-support
allocations of the two finite Poisson transforms in case 1 (z = 0) of Lemma 18.1 (lem:plain) of
the external, unreviewed OpenAI manuscript "The Quasi-Riemann Hypothesis" (30 Sep 2026; pr908
paper.tex, sha256 42a5ee0f...deac6a3).  Line numbers refer to that file.  Risk item 10 of
proposed/CUBIC_FOURTH_MOMENT/SKETCH.md.

ARITHMETIC CLASS.  EXACT: Python Fractions, sympy rationals/identities, integer cyclotomic
vectors.  The linear programs are solved by an exact two-phase simplex in Fractions (Bland's
rule).  scipy.optimize.linprog (HiGHS, float64) is run only as a cross-check and is labelled
FLOAT; no PASS criterion depends on it.

Logic copied (and parametrised by the order n) from reviews/lemma18_support_checks.py
(A1 bijection, A4 Moebius, A5 t-allocation, L1-L3 label ledgers) and reviews/lemma18_ledger.py
((2.6) local inequality, (2.13), (2.12), (2.15)-(2.16) identities).  Neither file is modified.

Sections (each line prints PASS/FAIL; lines marked CTRL are failing controls that must be DETECTED):
  [P] closing-condition tolerances (SKETCH Sec. 3.5) recomputed exactly, for four loss models.
  [A] first transform (A2): order-free ledger, (2.6) budget over all local types, exact LP for the
      budget slack and for min F_1/c, Gauss-sum normalisation |tau|^2 = P at n = 3.
  [G] Gauss-row zero h = 0 (enters through the s-label of A2): count of n-th powers, slack in n.
  [S] second transform (A4): common extraction, local table, moving support, width, child
      allowance, Moebius t, child normalisation, clipped shell, exceptional volume.
  [D] joint LP over the allocation polytope of both transforms: worst centred-deficit slack.
Run: nice -n 10 python3 -I reviews/cubic_allocation_loss.py   (about 1 minute, one process)
"""
import itertools
import math
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

RES = []
T0 = time.time()


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("\n       " + detail) if detail else ""))
    sys.stdout.flush()


def ctrl(name, detected, detail=""):
    """A failing control: PASS means the deliberately wrong input WAS detected."""
    check("CTRL " + name, detected, detail)


# =============================================================================================
# exact two-phase simplex (Fractions, Bland's rule).  min c.x  s.t.  A_ub x <= b_ub, A_eq x = b_eq,
# x >= 0.  Returns (status, value, x).
# =============================================================================================
def lp_min(c, A_ub=(), b_ub=(), A_eq=(), b_eq=()):
    n = len(c)
    rows, rhs, slack_sign = [], [], []
    for a, b in zip(A_ub, b_ub):
        rows.append([Fr(x) for x in a]); rhs.append(Fr(b)); slack_sign.append(1)
    for a, b in zip(A_eq, b_eq):
        rows.append([Fr(x) for x in a]); rhs.append(Fr(b)); slack_sign.append(0)
    m = len(rows)
    nsl = sum(1 for s in slack_sign if s)
    N = n + nsl + m                       # originals, slacks, artificials
    T = []
    k = 0
    for i in range(m):
        row = rows[i] + [Fr(0)] * (nsl + m)
        if slack_sign[i]:
            row[n + k] = Fr(1); k += 1
        b = rhs[i]
        if b < 0:
            row = [-x for x in row]; b = -b
        row[n + nsl + i] = Fr(1)
        T.append(row + [b])
    basis = [n + nsl + i for i in range(m)]

    def pivot(r, col):
        pv = T[r][col]
        T[r] = [x / pv for x in T[r]]
        for i in range(m):
            if i != r and T[i][col] != 0:
                f = T[i][col]
                T[i] = [a - f * b for a, b in zip(T[i], T[r])]
        basis[r] = col

    def run(cost, allowed):
        while True:
            cb = [cost[b] for b in basis]
            enter = None
            for j in allowed:
                if j in basis:
                    continue
                rc = cost[j] - sum(cb[i] * T[i][j] for i in range(m))
                if rc < 0:
                    enter = j
                    break
            if enter is None:
                return "optimal"
            best, r = None, None
            for i in range(m):
                if T[i][enter] > 0:
                    ratio = T[i][-1] / T[i][enter]
                    if best is None or ratio < best or (ratio == best and basis[i] < basis[r]):
                        best, r = ratio, i
            if r is None:
                return "unbounded"
            pivot(r, enter)

    cost1 = [Fr(0)] * (n + nsl) + [Fr(1)] * m
    run(cost1, list(range(N)))
    if sum(T[i][-1] for i in range(m) if basis[i] >= n + nsl) != 0:
        return "infeasible", None, None
    for i in range(m):                      # drive zero-level artificials out
        if basis[i] >= n + nsl:
            for j in range(n + nsl):
                if T[i][j] != 0 and j not in basis:
                    pivot(i, j)
                    break
    cost2 = [Fr(x) for x in c] + [Fr(0)] * (nsl + m)
    st = run(cost2, list(range(n + nsl)))
    if st != "optimal":
        return st, None, None
    x = [Fr(0)] * N
    for i in range(m):
        x[basis[i]] = T[i][-1]
    val = sum(Fr(c[j]) * x[j] for j in range(n))
    return "optimal", val, x[:n]


def float_lp(c, A_ub, b_ub, A_eq=None, b_eq=None):
    try:
        from scipy.optimize import linprog
    except Exception:
        return None
    r = linprog([float(x) for x in c],
                A_ub=[[float(x) for x in a] for a in A_ub] or None, b_ub=[float(x) for x in b_ub] or None,
                A_eq=[[float(x) for x in a] for a in A_eq] if A_eq else None,
                b_eq=[float(x) for x in b_eq] if b_eq else None, bounds=(0, None), method="highs")
    return r.fun if r.status == 0 else None


# =============================================================================================
# [P] closing-condition tolerances (M = 1).  Stage C_j, total A, previous proved ceiling bprev:
#   (C)  kap*L >= A - 2/3 + cC + mu        (cC: loss in the Theta-row deficit; mu: margin)
#   (R)  1 - A + 2L <= bprev - mu
#   caps L <= A/2,  L <= A - 1/2 - mu
# lo(A) is a max of affine maps and hi(A) a min of affine maps, so lo - hi is convex in A and a
# stage [a0, a1] is covered iff both endpoints are feasible: the endpoint test is exact.
# =============================================================================================
def feas(A, bprev, kap, cC, mu):
    lo = max(Fr(0), (A - Fr(2, 3) + cC + mu) / kap)
    hi = min((bprev - 1 + A - mu) / 2, A / 2, A - Fr(1, 2) - mu)
    return lo <= hi


def ceiling(b0, top, kap, cC, mu):
    """largest A in [b0, top] with stage feasible from bprev = b0.  lo - hi is convex in A, so the
    feasible set is an interval [b0, s1]; s1 is the least crossing of the affine part of lo with an
    affine piece of hi (slope of lo is 1/kap > 1 >= slope of every piece).  EXACT."""
    if not feas(b0, b0, kap, cC, mu):
        return None
    a = Fr(2, 3) - cC - mu                      # lo = (A - a)/kap
    cands = [top]
    # (A - a)/kap = (b0 - 1 + A - mu)/2
    cands.append(((b0 - 1 - mu) / 2 + a / kap) / (1 / kap - Fr(1, 2)))
    # (A - a)/kap = A/2
    cands.append((a / kap) / (1 / kap - Fr(1, 2)))
    # (A - a)/kap = A - 1/2 - mu
    if kap < 1:
        cands.append((a / kap - Fr(1, 2) - mu) / (1 / kap - 1))
    s1 = min(x for x in cands if x >= b0)
    assert feas(s1, b0, kap, cC, mu)
    return s1


def two_stage(top, kap, cC=Fr(0), mu=Fr(0), b0=Fr(2, 3)):
    s1 = ceiling(b0, top, kap, cC, mu)
    if s1 is None:
        return False, None
    # C_2's ceiling increases with b1 and A = b1 is feasible for C_2 once it is for C_1, so b1 = s1 is optimal
    b1 = s1
    return (b1 > b0 and feas(b1, b1, kap, cC, mu) and feas(top, b1, kap, cC, mu)), b1


def part_P():
    out = {}
    for delta in (Fr(0), Fr(1, 100)):
        top = 1 + delta
        mu_s = (11 - 147 * delta) / 612
        c432 = (11 - 147 * delta) / 432
        c507 = (11 - 147 * delta) / 507
        eps = Fr(1, 10 ** 7)
        # model 1: margin mu demanded in every constraint (SKETCH mu*)
        ok1 = two_stage(top, Fr(5, 6), mu=mu_s)[0] and not two_stage(top, Fr(5, 6), mu=mu_s + eps)[0]
        # model 2: additive loss confined to the centred deficit (SKETCH c*, the register's tolerance)
        ok2 = two_stage(top, Fr(5, 6), cC=c432)[0] and not two_stage(top, Fr(5, 6), cC=c432 + eps)[0]
        # model 3: additive loss in the Theta-row deficit everywhere, so also in U (U ceiling 2/3 - c)
        ok3 = (two_stage(top, Fr(5, 6), cC=c507, b0=Fr(2, 3) - c507)[0]
               and not two_stage(top, Fr(5, 6), cC=c507 + eps, b0=Fr(2, 3) - c507 - eps)[0])
        out[delta] = (mu_s, c432, c507)
        check("[P1] delta=%s: mu*(delta) = (11-147d)/612 = %s (%.5f) reproduced (margin in every constraint)"
              % (delta, mu_s, float(mu_s)), ok1)
        check("[P2] delta=%s: c*(delta) = (11-147d)/432 = %s (%.5f) reproduced (loss confined to the centred deficit)"
              % (delta, c432, float(c432)), ok2)
        check("[P3] delta=%s: additive Theta-deficit loss that also hits U: tolerance (11-147d)/507 = %s (%.5f)"
              % (delta, c507, float(c507)), ok3)
    # model 4: loss proportional to the extracted length v, i.e. F_1 + F_2 >= kappa*v with kappa < 5/6.
    k = sp.Symbol("k", positive=True)
    res = {}
    for delta in (Fr(0), Fr(1, 100)):
        sol = [s for s in sp.solve(sp.Eq(2 * k ** 2 - 6 * k + 8, 3 * (1 + sp.Rational(delta.numerator, delta.denominator)) * (2 - k) ** 2), k)
               if 0 < float(s) < 1]
        kc = sol[0]
        kf = Fr(str(sp.N(kc, 40)))
        okk = two_stage(1 + delta, kf + Fr(1, 10 ** 6))[0] and not two_stage(1 + delta, kf - Fr(1, 10 ** 6))[0]
        res[delta] = kc
        check("[P4] delta=%s: two stages close iff kappa >= kappa_crit = %s = %.6f (exact root; solver agrees at +-1e-6)"
              % (delta, sp.simplify(kc), float(kc)), okk,
              "v-proportional allocation loss tolerated per unit extracted length: 5/6 - kappa_crit = %.5f"
              % (5 / 6 - float(kc)))
    # every nested version at delta = 0: kappa > 2/3 (at A = 1 need L >= 1/(3 kappa) and 2L < 1)
    check("[P5] any number of nested stages, delta=0: needs kappa > 2/3 (L = 1/(3 kappa) < 1/2); equivalently a "
          "(C)-only loss < 1/12 at kappa = 5/6", Fr(5, 6) * Fr(1, 2) - Fr(1, 3) == Fr(1, 12))
    return out, res


# =============================================================================================
# local data.  First transform: a common prime with multiplicities (i, j) contributes per unit
# log-norm  c = i, d = j, p = 1, R = r = 1_{n !| i-j}.  Allowances:
#   cubic   B_c = ((3c - 4d - 2R)/6)_+   (CUBIC_N3_GAPS Sec. 1.3; SKETCH Lemma 4.E)
#   sextic  B_c = ((3c - 5d - R)/6)_+    (paper l. 13379)
# =============================================================================================
def rflag(i, j, n):
    return 1 if (i - j) % n else 0


ALLOW = {"cubic": (Fr(3, 6), Fr(-4, 6), Fr(-2, 6)), "sextic": (Fr(3, 6), Fr(-5, 6), Fr(-1, 6)),
         "kappa1": (Fr(3, 6), Fr(-3, 6), Fr(-2, 6))}   # kappa1: an over-generous allowance (control)


def lc(name, c, d, R):
    a, b, e = ALLOW[name]
    return a * c + b * d + e * R


def part_A():
    # A1 ledger identity is order-free (sympy; no n appears)
    m, A, c, d, p, R, E_, q, s0, Bc, Bd = sp.symbols("m A c d p R E q s_0 B_c B_d", real=True)
    qt = q + R + E_
    lhs = (m - A - R / 2 - E_) + (p + s0) + sp.Rational(1, 2) * (A - c + qt + Bc - s0 + A - d + qt + Bd - s0)
    rhs = (m + q) + sp.Rational(1, 2) * (Bc + Bd - (c + d - 2 * p - R))
    check("[A1] first-transform ledger (l. 13384-13392) = M + (B_c + B_d - (c+d-2p-R))/2: sympy identity with no "
          "order-dependent constant (outside factor m-A-R/2-E, count p+s_0, targets)", sp.simplify(lhs - rhs) == 0)

    # A2 (2.6) local budget slack over all local types, exhaustive
    for n, al in ((6, "sextic"), (3, "cubic"), (3, "sextic")):
        worst, zeros = None, []
        for i in range(1, 121):
            for j in range(1, 121):
                r = rflag(i, j, n)
                budget = Fr(i + j - 2 - r)
                s = budget - max(Fr(0), lc(al, i, j, r)) - max(Fr(0), lc(al, j, i, r))
                worst = s if worst is None else min(worst, s)
                if s == 0 and i <= 6 and j <= 6:
                    zeros.append((i, j))
        check("[A2] (2.6) local slack, n=%d, %s allowance, all 1<=i,j<=120: min = %s >= 0" % (n, al, worst),
              worst == 0, "zero-slack local types (i,j<=6): %s" % zeros)
    # control: an allowance that would give kappa_1 = 1 without forcing breaks (2.6) at (2,1)
    i, j = 2, 1
    r = rflag(i, j, 3)
    s = Fr(i + j - 2 - r) - max(Fr(0), lc("kappa1", i, j, r))
    ctrl("[A2-CTRL] allowance ((3c-3d-2R)/6)_+ (would make kappa_1 = 1) violates (2.6) at a cubic (2,1) prime: "
         "local slack %s < 0" % s, s < 0,
         "ledger excess = |slack|/2 per unit log q_p = c/24 when all common primes are (2,1): a positive multiple of M")

    # A3 exact LP: min over the first-transform cone of budget - B_c - B_d, normalised c + d = 1.
    # The slack is a minimum of four linear forms (B = max(0, l)), so min = min over 4 LPs.
    IM = 12
    gens = [(i, j) for i in range(1, IM + 1) for j in range(1, IM + 1)]
    for n, al in ((6, "sextic"), (3, "cubic")):
        best = None
        for sc, sd in itertools.product((0, 1), repeat=2):
            cost = []
            for (i, j) in gens:
                r = rflag(i, j, n)
                v = Fr(i + j - 2 - r) - sc * lc(al, i, j, r) - sd * lc(al, j, i, r)
                cost.append(v)
            st, val, x = lp_min(cost, A_eq=[[Fr(i + j) for (i, j) in gens]], b_eq=[1])
            best = val if best is None else min(best, val)
        check("[A3] exact LP over the first-transform allocation cone (local types i,j<=%d), n=%d %s: "
              "min (c+d-2p-R - B_c - B_d)/(c+d) = %s" % (IM, n, al, best), best == 0)

    # A4 exact LP: min F_1 at c = 1 on both branches.  Variables: lambda_g (types), q, E, Dk >= 0 (delta_fr = 0),
    # beta (epigraph of B_c).  F_1(theta) = theta c + (1-theta) D0 + theta q~ + B_c - (1-theta) g,  g = J_+, J = D0 - c.
    def min_F1(n, al, IMx=12):
        th = Fr(1, n)
        G = [(i, j) for i in range(1, IMx + 1) for j in range(1, IMx + 1)]
        nv = len(G) + 4          # + q, E, Dk, beta
        iq, iE, iD, ib = len(G), len(G) + 1, len(G) + 2, len(G) + 3
        best = None
        for branch in ("J<0", "J>=0"):
            cost = [Fr(0)] * nv
            Aub, bub = [], []
            # aggregates
            cc = [Fr(i) for (i, j) in G] + [0, 0, 0, 0]
            dd = [Fr(j) for (i, j) in G] + [0, 0, 0, 0]
            RR = [Fr(rflag(i, j, n)) for (i, j) in G] + [0, 0, 0, 0]
            pp = [Fr(1)] * len(G) + [0, 0, 0, 0]
            for t in range(len(G)):
                if branch == "J<0":
                    cost[t] = th * cc[t] + (1 - th) * dd[t] + th * RR[t]
                else:
                    cost[t] = cc[t] + th * RR[t]
            cost[iq] = th
            cost[iE] = th
            cost[iD] = (1 - th) if branch == "J<0" else Fr(0)
            cost[ib] = Fr(1)
            # beta >= l_c
            a, b, e = ALLOW[al]
            row = [a * cc[t] + b * dd[t] + e * RR[t] for t in range(nv)]
            row[ib] = Fr(-1)
            Aub.append(row); bub.append(0)
            # E <= p - R
            row = [RR[t] - pp[t] for t in range(nv)]
            row[iE] = Fr(1)
            Aub.append(row); bub.append(0)
            # branch: J = d + Dk - c  (<= 0 or >= 0)
            row = [dd[t] - cc[t] for t in range(nv)]
            row[iD] = Fr(1)
            if branch == "J<0":
                Aub.append(row); bub.append(0)
            else:
                Aub.append([-x for x in row]); bub.append(0)
            st, val, x = lp_min(cost, Aub, bub, A_eq=[cc], b_eq=[1])
            if best is None or val < best[0]:
                best = (val, branch, [(G[t], x[t]) for t in range(len(G)) if x[t] != 0])
        return best
    for n, al, target in ((6, "sextic", Fr(2, 3)), (3, "cubic", Fr(5, 6))):
        val, br, sup = min_F1(n, al)
        check("[A4] exact LP: min F_1/c over the first-transform cone, n=%d %s allowance = %s (expected %s)"
              % (n, al, val, target), val == target, "attained on branch %s by %s" % (br, sup))
    val, br, sup = min_F1(3, "sextic")
    ctrl("[A4-CTRL] n=3 with the SEXTIC allowance: min F_1/c = %s < 5/6 (detected)" % val, val < Fr(5, 6),
         "attained on branch %s by %s.  Run 1 asserted '== 19/24' (the per-prime (4,1) value of CUBIC_N3_GAPS "
         "[A3-CTRL]) and FAILED: B_c is the positive part of a GLOBAL sum, so a mixture with 3c = 5d, R = 0 does "
         "worse, F_1 = c/3 + 2c/5 = 11c/15" % (br, sup))
    ok = all(Fr(i, 3) + Fr(2 * j, 3) + max(Fr(0), lc("sextic", i, j, 0)) == Fr(11 * i, 15) for i, j in ((15, 9), (30, 18)))
    check("[A4c] single r = 0 type with 3i = 5j at n = 3 ((15,9), (30,18)): sextic-allowance F_1 = 11c/15 exactly", ok)
    # cross-check with an exhaustive per-type evaluation (types up to 60): F_1 - 5c/6 = (2d/3 + R/3 - c/2)_+ on J<0
    ok = True
    for i in range(1, 61):
        for j in range(1, i):
            r = rflag(i, j, 3)
            F1 = Fr(i, 3) + Fr(2 * j, 3) + Fr(r, 3) + max(Fr(0), lc("cubic", i, j, r))
            ok &= F1 - Fr(5 * i, 6) == max(Fr(0), Fr(2 * j, 3) + Fr(r, 3) - Fr(i, 2))
    check("[A4b] per-type identity F_1 - 5c/6 = (2d/3 + R/3 - c/2)_+ on J<0 (q = E = 0, D0 = d), i<=60", ok)

    # A5 Gauss-sum normalisation at n = 3 in Z[omega][zeta_P] (exact).  O/p = F_P for a split prime.
    def gauss_check(P):
        g = next(x for x in range(2, P) if all(pow(x, (P - 1) // f, P) != 1 for f in sp.primefactors(P - 1)))
        ind = {pow(g, k, P): k for k in range(P - 1)}

        def tau(e, h):            # sum_x omega^{e ind(x)} zeta^{h x}: 3 x P integer array
            M = [[0] * P for _ in range(3)]
            for x in range(1, P):
                M[(e * ind[x]) % 3][(h * x) % P] += 1
            return M

        def mul(X, Y):
            Z = [[0] * P for _ in range(3)]
            for a in range(3):
                for b in range(P):
                    if X[a][b]:
                        for c_ in range(3):
                            for d_ in range(P):
                                if Y[c_][d_]:
                                    Z[(a + c_) % 3][(b + d_) % P] += X[a][b] * Y[c_][d_]
            return Z

        def conj(X):
            return [[X[(-a) % 3][(-b) % P] for b in range(P)] for a in range(3)]

        def is_int(X, val):      # X == val exactly in Z[zeta_{3P}] (3 does not divide P)
            Y = [row[:] for row in X]
            Y[0][0] -= val
            for b in range(P):   # remove omega^2 = -1 - omega
                t = Y[2][b]; Y[2][b] = 0; Y[0][b] -= t; Y[1][b] -= t
            for a in range(2):   # remove zeta^{P-1} = -(1 + ... + zeta^{P-2})
                t = Y[a][P - 1]; Y[a][P - 1] = 0
                for b in range(P - 1):
                    Y[a][b] -= t
            return all(v == 0 for row in Y for v in row)
        okp = True
        for e in (1, 2):
            for h in range(1, P):
                T_ = tau(e, h)
                okp &= is_int(mul(T_, conj(T_)), P)
        # trivial character (e = 0): Ramanujan sum, |.|^2 = (P-1)^2 at h = 0 mod p
        T0_ = tau(0, 0)
        triv = is_int(mul(T0_, conj(T0_)), (P - 1) ** 2)
        return okp, triv
    for P in (7, 13):
        okp, triv = gauss_check(P)
        check("[A5] n=3, P=%d: |tau(chi^e, h)|^2 = P exactly for e = 1, 2 and all h != 0 (primitive xi_r: the outside "
              "factor's -R/2 holds)" % P, okp)
        ctrl("[A5-CTRL] P=%d: sextic r-rule at a cubic (4,1) prime makes xi_r = chi^3 trivial; normalised |G|^2 = "
             "(P-1)^2/P = %s > 1 at p | h, so |G_xi| <= 1 fails by ~P^{1/2} (ledger loss R'/2)" % (P, Fr((P - 1) ** 2, P)),
             triv and Fr((P - 1) ** 2, P) > 1)

    # A6 Moebius label s nets to zero; A7 bijection; A8 Moebius identity (copied, order-free)
    check("[A6] s-label nets to zero in the first-transform ledger: s_0 + (-s_0 - s_0)/2 = 0",
          all(s + Fr(1, 2) * (-s - s) == 0 for s in [Fr(k, 4) for k in range(17)]))
    NP, EMAX = 3, 6
    vecs = list(itertools.product(range(EMAX + 1), repeat=NP))
    seen = set()
    okb = True
    cnt_r = {3: 0, 6: 0}
    for nn in vecs:
        for mm in vecs:
            common = [t for t in range(NP) if nn[t] and mm[t]]
            C = tuple(nn[t] if t in common else 0 for t in range(NP))
            D = tuple(mm[t] if t in common else 0 for t in range(NP))
            a = tuple(nn[t] - C[t] for t in range(NP))
            b = tuple(mm[t] - D[t] for t in range(NP))
            okb &= all(not (a[t] and b[t]) for t in range(NP))
            okb &= all(not ((a[t] or b[t]) and C[t]) for t in range(NP))
            seen.add((C, D, a, b))
            for n in (3, 6):
                cnt_r[n] += sum(1 for t in common if (C[t] - D[t]) % n)
    check("[A7] complete-common-support decomposition (n,n') -> (C,D,a,b) injective with (a,b)=1, (ab,CD)=1 "
          "(3 primes, exps 0..6); order-free", okb and len(seen) == len(vecs) ** 2,
          "r-prime incidences: n=6 %d, n=3 %d (n=3 has fewer r-primes: more e-mask primes)" % (cnt_r[6], cnt_r[3]))
    okm = True
    for a in itertools.product(range(3), repeat=4):
        for b in itertools.product(range(3), repeat=4):
            tot = sum((-1) ** sum(s) for s in itertools.product(range(2), repeat=4)
                      if all(s[t] <= min(a[t], b[t]) for t in range(4)))
            okm &= tot == (1 if all(min(a[t], b[t]) == 0 for t in range(4)) else 0)
    check("[A8] Moebius extension sum_{s|a,b} mu(s) = 1_{(a,b)=1} (4 primes, exps 0..2); order-free", okm)
    # zero frequency: exponents equal mod n forbid total multiplicity one (powerful product), n = 3 and 6
    check("[A9] zero frequency: v = v' (mod n) and v + v' = 1 impossible for n = 3, 6 (product powerful; "
          "exponent m - M = -q <= 0, order-free)",
          all(not ((v - w) % n == 0 and v + w == 1) for n in (3, 6) for v in range(3) for w in range(3)))


# =============================================================================================
# [G] Gauss-row zero (l. 13572-13594): G(u,0) = 0 unless u is an n-th power; |G(u,0)| <= q_u^{1/2}.
# =============================================================================================
def part_G():
    a0, s0, th, nn = sp.symbols("a_0 s_0 theta_N n", real=True)
    # crude count Y^{1/n}, s_0 <= (a_0 + theta_N)/n:  slack = (a_0 - s_0 + 2 th) - (2 a_0/n + (1 + 2/n) th)
    slack_crude = (a0 - (a0 + th) / nn + 2 * th) - (2 * a0 / nn + (1 + 2 / nn) * th)
    target = (1 - 3 / nn) * (a0 + th)
    check("[G1] crude-count slack = (1 - 3/n)(a_0 + theta_N) (sympy identity, worst s_0)",
          sp.simplify(slack_crude - target) == 0)
    s3 = sp.simplify(slack_crude.subs(nn, 3))
    s6 = sp.simplify(slack_crude.subs(nn, 6))
    check("[G2] n=3: crude-count slack is IDENTICALLY 0 (no loss, no spare); n=6: (a_0+theta_N)/2 >= 0",
          s3 == 0 and sp.simplify(s6 - (a0 + th) / 2) == 0, "n=3: %s;  n=6: %s" % (s3, s6))
    # refined count (Y/q_s^3)^{1/3} = Y^{1/3}/q_s at n = 3
    refined = (a0 - s0 + 2 * th) - (2 * a0 / 3 + sp.Rational(5, 3) * th - 2 * s0)
    check("[G3] n=3 refined count: slack = a_0/3 + s_0 + theta_N/3 >= 0 for a_0 >= -theta_N, s_0 >= 0",
          sp.simplify(refined - (a0 / 3 + s0 + th / 3)) == 0)
    s2 = sp.simplify(slack_crude.subs(nn, 2))
    ctrl("[G1-CTRL] n=2 crude count: slack %s < 0 for a_0 > -theta_N (the quadratic failure)" % s2,
         sp.simplify(s2 + (a0 + th) / 2) == 0)
    # control: the SEXTIC exponent 1/6 used for the number of cubes.  Exact count of cube ideals v^3, N v <= T.
    def ideals_upto(T):          # number of nonzero ideals of Z[omega] of norm <= T (elements / 6 units)
        cnt = 0
        B = int(math.isqrt(4 * T // 3)) + 2
        for a in range(-B, B + 1):
            for b in range(-B, B + 1):
                if (a or b) and a * a - a * b + b * b <= T:
                    cnt += 1
        return cnt // 6
    rows = []
    for Y in (10 ** 6, 10 ** 12, 10 ** 18):
        T = round(Y ** (1 / 3))
        assert T ** 3 == Y
        cubes = ideals_upto(T)
        rows.append((Y, cubes, round(Y ** (1 / 6))))
    ctrl("[G4-CTRL] sextic count Y^{1/6} for cube moduli at n=3 is wrong: exact #cubes of norm <= Y vs Y^{1/6}",
         all(cu > 2 * y6 for (_, cu, y6) in rows[1:]),
         "; ".join("Y=1e%d: cubes=%d, Y^(1/6)=%d" % (round(math.log10(Y)), cu, y6) for Y, cu, y6 in rows)
         + " (EXACT counts; the known asymptotic is c*Y^(1/3); not a trend fit)")


# =============================================================================================
# second-transform local generators (per unit log-norm): (c2, d2, g2, p2, t2, V, f) at order n.
# =============================================================================================
def gens2(n, IM=12, fmode="forced"):
    G = []
    for i in range(1, IM + 1):
        if i % n:
            G.append(("eq-unit", i, (i, i, i, 1, 1, 0, 0)))
            if fmode == "forced":
                fl = Fr(1) if (n == 3 and i == 1) else (Fr(2) if (n == 6 and i == 1) else Fr(0))
            else:
                fl = Fr(0)
            G.append(("eq-nonunit", i, (i, i, i, 1, 0, 1, fl)))
        else:
            G.append(("eq-ndiv", i, (i, i, i, 1, 0, 0, 0)))
    for j0 in range(n, IM, n):
        for i in range(j0 + 1, IM + 1):
            G.append(("uneq", (i, j0), (i, j0, j0, 1, 0, 0, 0)))
            G.append(("uneq", (j0, i), (j0, i, j0, 1, 0, 0, 0)))
    return G


def F2_of(n, v):
    th = Fr(1, n)
    c2, d2, g2, p2, t2, V, f = [Fr(x) for x in v]
    b2 = (c2 + d2) / 2
    return 2 * b2 - (1 - th) * g2 - p2 + t2 + th * V + th * f, b2


def forced_min_valuation(n, i):
    """nonunit equal-multiplicity prime with multiplicity i: v_p(G_c V_id) = i + 1; exceptional needs
    v_p(h') = -(i+1) mod n.  Returns the least admissible valuation."""
    return (-(i + 1)) % n


def part_S():
    # S1 local absolute table vs exact correlation maxima (closed forms of Lemma FC3 at n = 3), symbolic in P
    P = sp.Symbol("P", positive=True)
    ok = True
    for i in range(1, 31):
        for j0 in range(1, 31):
            g = min(i, j0)
            if i == j0:
                if i % 3:
                    cases = [("unit", P ** (i - 1), i - 1), ("nonunit", P ** (i - 1) * (P - 1), i)]
                else:
                    cases = [("unit", P ** (i - 1) * (P - 2), i), ("nonunit", P ** (i - 1) * (P - 1), i)]
            else:
                cases = [("uneq", P ** (g - 1) * (P - 1), g)] if g % 3 == 0 else [("uneq", 0, None)]
            for _, val, ex in cases:
                if ex is None:
                    continue
                d = sp.expand(P ** ex - val)
                ok &= all(float(d.subs(P, Pv)) >= 0 for Pv in (7, 13, 19, 25, 31))
                ok &= ex <= g        # g_2 - t_2 <= g_2 = min(i, j0) <= min(c_2, d_2)
    check("[S1] n=3 local table: |F(p^i,p^j0;j)| <= P^{g_2 - t_2} with g_2 - t_2 <= min(c_2,d_2), i,j0 <= 30 "
          "(closed forms of Lemma FC3; brute force in CUBIC_N3_GAPS [F1],[T1])", ok)
    # S2 moving support: e_p = v_p(G_c V_id) mod n nonzero only on unit or nonunit (equal, n !| i) primes
    ok = True
    for n in (3, 6):
        for i in range(1, 61):
            for j0 in range(1, 61):
                if i == j0:
                    for unit in (True, False):
                        in_V = (not unit) and (i % n != 0)
                        e = (i + (1 if in_V else 0)) % n
                        counted = (i % n != 0)          # unit -> t_2, nonunit -> V
                        ok &= (e == 0) or counted
                else:
                    if min(i, j0) % n:
                        continue                         # correlation vanishes: no allocation
                    e = min(i, j0) % n
                    ok &= e == 0
    check("[S2] moving support q' = q~ + w_o + t_2 + V: every active (e_p != 0) prime is a unit or nonunit "
          "equal-multiplicity prime, n = 3 and 6, i,j0 <= 60", ok)
    # S3-S4 width identity and child allowance (order-free sympy)
    A, c, d, R, E_, m, q, w, wo, g, ell, Bc, Dk, g2, t2, V, p2, b2, s0, sig = sp.symbols(
        "A c d R E m q w w_o g ell B_c Dk g_2 t_2 V p_2 b_2 s_0 sigma", real=True)
    M = m + q
    qt = q + R + E_
    K0 = 2 * A - c - d + R + E_ - m
    K = K0 - Dk
    a0 = A - c - w
    J = d - c + Dk - 2 * w + wo
    mp = 2 * a0 - K - g - g2 - V
    qp = qt + wo + t2 + V
    check("[S3] (2.13) M' = M + J - g - g_2 + t_2 (sympy; no order-dependent constant)",
          sp.simplify(mp + qp - (M + J - g - g2 + t2)) == 0)
    Lam = a0 + qt + wo + w + Bc - s0
    expo = K + g - ell - a0 + p2 - s0 + (sp.Symbol("G2") - t2) - b2
    expo = expo.subs(sp.Symbol("G2"), g2)
    Dchild = b2 - p2 + w + Bc + ell
    check("[S4] (2.14) allowance - (table exponents) = M' + Delta_child, Delta_child = b_2 - p_2 + w + B_c + ell "
          "(sympy; order-free)", sp.simplify(Lam - expo - (mp + qp + Dchild)) == 0)
    # (2.12) diagonal: order-free, uses only B_c >= 0
    lhs = (K + g - ell - s0) - (a0 + qt + wo + w + Bc - s0)
    rhs = (A - M) - d - Dk - wo - Bc + g - ell
    check("[S5] (2.12) diagonal identity (sympy; order-free; the bound uses only B_c >= 0, true for both "
          "allowances)", sp.simplify(lhs - rhs) == 0)
    # S6 t-allocation identity (copied from lemma18_support_checks A5; exhaustive, order-free)
    okA5, nchk = True, 0
    for n1 in itertools.product(range(3), repeat=3):
        for n2 in itertools.product(range(3), repeat=3):
            full = [n1[k] + n2[k] for k in range(3)]
            for t in itertools.product(range(2), repeat=3):
                tp = [k for k in range(3) if t[k]]
                lhs_ = 1 if all(full[k] >= 1 for k in tp) else 0
                rhs_ = 0
                for Js in itertools.product([1, 2, 3], repeat=len(tp)):
                    sign = 1
                    d1 = [0] * 3
                    d2 = [0] * 3
                    for k, Jb in zip(tp, Js):
                        sign *= (-1) ** (bin(Jb).count("1") + 1)
                        if Jb & 1:
                            d1[k] += 1
                        if Jb & 2:
                            d2[k] += 1
                    if all(n1[k] >= d1[k] for k in range(3)) and all(n2[k] >= d2[k] for k in range(3)):
                        rhs_ += sign
                okA5 &= lhs_ == rhs_
                nchk += 1
    check("[S6] t-allocation inclusion-exclusion 1_{p | n1 n2} = sum_J (-1)^{|J|+1} prod 1_{p|n_i} (z = 0; "
          "exhaustive, order-free)", okA5, "%d cases" % nchk)
    # S7 exact LP: child normalisation / exceptional volume  max e1 + e2 + t_- - r1 - r2 = 2 theta_N
    # variables shifted by theta_N = 1: E1 = e1+1, E2 = e2+1, W1 = w1+1, W2 = w2+1 in [0,2]; r1, r2, t >= 0
    # constraints: |e_j + w_j| <= 1, r_j + w_j >= t.  maximise -> minimise negative.
    cost = [-1, -1, 0, 0, 1, 1, -1]          # E1 E2 W1 W2 r1 r2 t   (constant +2 handled below)
    Aub, bub = [], []
    for k in range(4):
        row = [0] * 7; row[k] = 1; Aub.append(row); bub.append(2)
    for (Ei, Wi) in ((0, 2), (1, 3)):
        row = [0] * 7; row[Ei] = 1; row[Wi] = 1; Aub.append(row); bub.append(3)     # e+w <= 1
        row = [0] * 7; row[Ei] = -1; row[Wi] = -1; Aub.append(row); bub.append(-1)  # e+w >= -1
    for (Wi, ri) in ((2, 4), (3, 5)):
        row = [0] * 7; row[Wi] = -1; row[ri] = -1; row[6] = 1; Aub.append(row); bub.append(-1)  # t <= r + w
    st, val, x = lp_min(cost, Aub, bub)
    vmax = -(val) - 2                        # undo the shift e = E - 1 (two copies)
    check("[S7] exact LP: max over child normalisations of e_1 + e_2 + t_- - r~_1 - r~_2 = %s theta_N "
          "(eq:centered-divisor-boundary; the exceptional volume exponent <= a_0 - b_2 + 2 theta_N)" % vmax,
          st == "optimal" and vmax == 2)
    # S8 (2.18h) and the clipped shell (copied L2, L3 grids; order-free)
    grid = [Fr(k, 4) for k in range(0, 9)]
    ok = all(t_ - r1 - r2 - max(Fr(0), r - r1) == (t_ - r2) - max(r, r1)
             for t_, r1, r2, r in itertools.product(grid, repeat=4))
    ok2 = True
    for t_, r1, r2, r, om in itertools.product(grid[:7], grid[:7], grid[:7], grid[:7], [Fr(0), Fr(1, 8)]):
        if t_ <= r2 + om and t_ <= r1 + om:
            ok2 &= (t_ - r1 - r2 - max(Fr(0), r - r1)) <= om - r
    check("[S8] (2.18h) identity and t-count <= omega_2 - r (lattice saving r = (L - v)_+ survives the "
          "t-allocation; order-free)", ok and ok2)

    # S9 F_2 at theta = 1/3 per local type; zero set; exact LP min (F_2 - min(c_2,d_2)) with c_2 + d_2 = 2
    for n, fmode, target, label in ((3, "forced", Fr(1), "kappa_2 = 1"), (6, "forced", Fr(2, 3), "paper (2.17)")):
        G = gens2(n)
        mn = min(F2_of(n, v)[0] / F2_of(n, v)[1] for _, _, v in G)
        zeros = sorted(set((k, i) for k, i, v in G if F2_of(n, v)[0] == target * F2_of(n, v)[1]))
        check("[S9] n=%d F_2 table: min F_2/b_2 over local types = %s (%s)" % (n, mn, label), mn == target,
              "tight local types: %s" % zeros)
    G = gens2(3)
    # LP: variables mu_h, rho (epigraph of max(F2 - c2, F2 - d2)) ; normalise c2 + d2 = 2
    nv = len(G) + 1
    cost = [Fr(0)] * len(G) + [Fr(1)]
    Aub, bub = [], []
    for side in (0, 1):
        row = [F2_of(3, v)[0] - Fr(v[side]) for _, _, v in G] + [Fr(-1)]
        Aub.append(row); bub.append(0)
    st, val, x = lp_min(cost, Aub, bub, A_eq=[[Fr(v[0] + v[1]) for _, _, v in G] + [0]], b_eq=[2])
    check("[S10] exact LP over the second-transform cone (n=3): min [F_2 - min(c_2,d_2)] at c_2 + d_2 = 2 is %s"
          % val, val == 0)
    G0 = gens2(3, fmode="none")
    mn0 = min(F2_of(3, v)[0] / F2_of(3, v)[1] for _, _, v in G0)
    ctrl("[S9-CTRL] n=3 without the forced residue (f = 0): min F_2/b_2 = %s = 2 theta < 1 (detected)" % mn0,
         mn0 == Fr(2, 3))
    fv = forced_min_valuation(3, 1)
    ctrl("[S11-CTRL] sextic f = 2 v_1 plugged in at n = 3 is unjustified: least forced valuation at a nonunit i=1 "
         "prime is %d mod 3 (sextic: %d mod 6), so q_{h_0} >= Z^{v_1} only and f = v_1" % (fv, forced_min_valuation(6, 1)),
         fv == 1 and forced_min_valuation(6, 1) == 4)


# =============================================================================================
# [D] joint LP over the allocation polytope of both transforms (z = 0):
#   min  F_1 + F_2 + (L - v)_+ - kappa_t L,   v = c + min(c_2, d_2)
#   F_1 = theta c + (1-theta) D0 + theta q~ + B_c - (1-theta) g,  g = J_+ + sigma,  J = D0 - c,
#   D0 = d + Dk,  Dk >= -delta_fr,  q~ = q + R + E,  E <= p - R.
#   The objective is the slack of  [A - 2M/3 - F_1 - F_2 - (L-v)_+] <= [A - 2M/3 - kappa_t L]  (Lemma 4.J).
# =============================================================================================
def joint_lp(n, al, kap_t, L, sig=Fr(0), dfr=Fr(0), fmode="forced", IM1=10, IM2=10):
    th = Fr(1, n)
    G1 = [(i, j) for i in range(1, IM1 + 1) for j in range(1, IM1 + 1)]
    G2 = gens2(n, IM2, fmode)
    n1, n2 = len(G1), len(G2)
    iq, iE, iD, ib, ir = n1 + n2, n1 + n2 + 1, n1 + n2 + 2, n1 + n2 + 3, n1 + n2 + 4
    nv = n1 + n2 + 5
    cc = [Fr(i) for i, j in G1] + [Fr(0)] * (n2 + 5)
    dd = [Fr(j) for i, j in G1] + [Fr(0)] * (n2 + 5)
    RR = [Fr(rflag(i, j, n)) for i, j in G1] + [Fr(0)] * (n2 + 5)
    pp = [Fr(1)] * n1 + [Fr(0)] * (n2 + 5)
    c2 = [Fr(0)] * n1 + [Fr(v[0]) for _, _, v in G2] + [Fr(0)] * 5
    d2 = [Fr(0)] * n1 + [Fr(v[1]) for _, _, v in G2] + [Fr(0)] * 5
    F2 = [Fr(0)] * n1 + [F2_of(n, v)[0] for _, _, v in G2] + [Fr(0)] * 5
    best = None
    for branch in ("J<0", "J>=0"):
        cost = [Fr(0)] * nv
        for t in range(n1):
            cost[t] = (th * cc[t] + (1 - th) * dd[t] + th * RR[t]) if branch == "J<0" else (cc[t] + th * RR[t])
        for t in range(n1, n1 + n2):
            cost[t] = F2[t]
        cost[iq] = th
        cost[iE] = th
        cost[iD] = (1 - th) if branch == "J<0" else Fr(0)      # Dk' = Dk + dfr >= 0
        cost[ib] = Fr(1)
        cost[ir] = Fr(1)
        const = -(1 - th) * sig - kap_t * L - ((1 - th) * dfr if branch == "J<0" else Fr(0))
        Aub, bub = [], []
        a, b, e = ALLOW[al]
        row = [a * cc[t] + b * dd[t] + e * RR[t] for t in range(nv)]; row[ib] = Fr(-1)
        Aub.append(row); bub.append(0)                                   # beta >= l_c
        row = [RR[t] - pp[t] for t in range(nv)]; row[iE] = Fr(1)
        Aub.append(row); bub.append(0)                                   # E <= p - R
        row = [dd[t] - cc[t] for t in range(nv)]; row[iD] = Fr(1)       # J + dfr = d + Dk' - c
        if branch == "J<0":
            Aub.append(row); bub.append(dfr)
        else:
            Aub.append([-x for x in row]); bub.append(-dfr)
        for side in (c2, d2):                                            # rho >= L - c - c2 (and d2)
            row = [-(cc[t] + side[t]) for t in range(nv)]; row[ir] = Fr(-1)
            Aub.append(row); bub.append(-L)
        st, val, x = lp_min(cost, Aub, bub)
        val = val + const
        if best is None or val < best[0]:
            vv = sum(cc[t] * x[t] for t in range(nv))
            vc2 = sum(c2[t] * x[t] for t in range(nv))
            vd2 = sum(d2[t] * x[t] for t in range(nv))
            sup1 = [(G1[t], x[t]) for t in range(n1) if x[t]]
            sup2 = [(G2[t - n1][0], G2[t - n1][1], x[t]) for t in range(n1, n1 + n2) if x[t]]
            best = (val, branch, vv + min(vc2, vd2), sup1, sup2, (Aub, bub, cost, const))
    return best


def part_D(tols, kcrit):
    Ltop = Fr(43, 102)
    for L in (Fr(1, 4), Ltop, Fr(1, 2)):
        val, br, v, s1, s2, _ = joint_lp(3, "cubic", Fr(5, 6), L)
        check("[D1] n=3 joint exact LP, L=%s: min slack of the centred deficit over ALL allocations = %s" % (L, val),
              val == 0, "minimiser: branch %s, v = %s (= L), first-transform support %s, second %s"
              % (br, v, s1[:3], s2[:3]))
    val, *_ = joint_lp(6, "sextic", Fr(2, 3), Fr(1, 4))
    check("[D2] calibration n=6, paper allowance, kappa_t = 2/3, L = M/4: min slack = %s (paper's (2.19), zero "
          "slack at v = L)" % val, val == 0)
    val, *_ = joint_lp(3, "cubic", Fr(5, 6) + Fr(1, 100), Ltop)
    check("[D3] sharpness: kappa_t = 5/6 + 1/100 gives min slack %s = -L/100 (5/6 is exact, no hidden spare)"
          % val, val == -Ltop / 100)
    sig, dfr = Fr(1, 100), Fr(1, 200)
    vals = []
    for L in (Fr(1, 4), Ltop, Fr(1, 2)):
        val, *_ = joint_lp(3, "cubic", Fr(5, 6), L, sig=sig, dfr=dfr)
        vals.append(val)
    T = Fr(2, 3) * (sig + dfr)
    check("[D4] with sigma = 1/100, delta_fr,1 = 1/200: min slack = -(2/3)(sigma + delta_fr,1) = %s for every L "
          "(terminal, does not scale with L or M)" % (-T), all(v == -T for v in vals), "values %s" % vals)
    # float cross-check of D1 at L = Ltop (labelled FLOAT)
    _, _, _, _, _, (Aub, bub, cost, const) = joint_lp(3, "cubic", Fr(5, 6), Ltop)
    fl = float_lp(cost, Aub, bub)
    print("       FLOAT cross-check (scipy HiGHS, minimising branch LP of D1 at L = 43/102): %s" %
          ("n/a" if fl is None else "%.3e" % (fl + float(const))))
    # controls
    val, br, v, s1, s2, _ = joint_lp(3, "sextic", Fr(5, 6), Ltop)
    ctrl("[D5-CTRL] n=3 with the SEXTIC allowance: min slack = %s = %s*L < 0 (loss %.5f M at L(top) = 43/102)"
         % (val, val / Ltop, float(-val)), val < 0,
         "run 1 asserted -L/24 (from 19/24) and FAILED; the exact value is -(5/6 - 11/15)L = -L/10.  Compare c*(0) = "
         "%.5f; kappa = 11/15 < kappa_crit = %.4f, two stages close at kappa = 11/15: %s"
         % (float(tols[Fr(0)][1]), float(kcrit[Fr(0)]), two_stage(Fr(1), Fr(11, 15))[0]))
    val, *_ = joint_lp(3, "cubic", Fr(5, 6), Ltop, fmode="none")
    ctrl("[D6-CTRL] n=3 without the nonunit forcing (f = 0): min slack = %s = -L/6 (loss %.4f M > c*): route "
         "broken (kappa = 2/3 <= kappa_crit; no nested version closes)" % (val, float(-val)),
         val == -Ltop / 6 and not two_stage(Fr(1), Fr(2, 3))[0])
    val, *_ = joint_lp(6, "sextic", Fr(5, 6), Ltop)
    ctrl("[D7-CTRL] sextic theta = 1/6 data with the cubic target kappa = 5/6: min slack = %s < 0 (n=6 only "
         "supplies kappa = 2/3)" % val, val == -Ltop / 6)


def main():
    print("cubic_allocation_loss.py  (EXACT unless labelled FLOAT)")
    tols, kcrit = part_P()
    print("  [%.0fs]" % (time.time() - T0))
    part_A()
    print("  [%.0fs]" % (time.time() - T0))
    part_G()
    print("  [%.0fs]" % (time.time() - T0))
    part_S()
    print("  [%.0fs]" % (time.time() - T0))
    part_D(tols, kcrit)
    nf = sum(1 for _, o in RES if not o)
    nc = sum(1 for nm, _ in RES if nm.startswith("CTRL"))
    print("\n%d/%d PASS (%d of them failing controls, detected)  (%.0f s)" % (len(RES) - nf, len(RES), nc, time.time() - T0))
    return nf


if __name__ == "__main__":
    sys.exit(main())
