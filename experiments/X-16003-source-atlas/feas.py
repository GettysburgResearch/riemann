"""When is the ONE-SCALAR CvS gate feasible at all?

The pencil is Q - c*eta*eta^T (L-16004 / e2: Loewner(lambda) = eta eta^T exactly).
Claim to test:

  (N)  necessary:   if Q - c eta eta^T >= 0 for some real c, then Q restricted to
                    eta^perp is PSD.     [x perp eta => x^T(Q - c eta eta^T)x = x^T Q x]
  (S)  sufficient:  if Q|_{eta^perp} > 0 (strictly), then such a c exists, the extremal
                    one is unique, and there the kernel is one-dimensional.
  (X)  and the gap is real: Q|_{eta^perp} PSD-but-singular need NOT be enough.

Consequence, since eta is even and the parity involution sends e_j -> e_{-j}: the ENTIRE
odd sector lies in eta^perp, so the one scalar cannot repair a single negative direction
there.  Reading B requires Q_W|_odd >= 0 outright.

Also check: when Q is indefinite but t* = 1/(eta^T Q^{-1} eta) is positive (which O-16005
shows can happen), does Q - t* eta eta^T fail the "PSD with 1-dim kernel" test?  It should.

HIGH-PRECISION FLOAT / EXACT where marked.
"""
import random
from fractions import Fraction as F
import mpmath as mp
from mpmath import mpf, matrix, nstr

mp.mp.dps = 50


def inertia_exact(M):
    """EXACT symmetric congruence over Q, with 2x2 hyperbolic blocks. Returns (n+, n-, n0)."""
    A = [row[:] for row in M]
    n = len(A)
    idx = list(range(n))
    pos = neg = zer = 0
    while idx:
        k = None
        for i in idx:
            if A[i][i] != 0:
                k = i; break
        if k is None:
            piv = None
            for a_ in range(len(idx)):
                for b_ in range(a_ + 1, len(idx)):
                    if A[idx[a_]][idx[b_]] != 0:
                        piv = (idx[a_], idx[b_]); break
                if piv: break
            if piv is None:
                zer += len(idx); break
            i, j = piv
            for r in idx:
                A[r][i] = A[r][i] + A[r][j]
            for r in idx:
                A[i][r] = A[i][r] + A[j][r]
            continue
        d = A[k][k]
        pos += 1 if d > 0 else 0
        neg += 1 if d < 0 else 0
        rest = [i for i in idx if i != k]
        for i in rest:
            f = A[i][k] / d
            if f != 0:
                for j in rest:
                    A[i][j] = A[i][j] - f * A[k][j]
        idx = rest
    return (pos, neg, zer)


def restrict_perp_eta(M):
    """EXACT: Q restricted to eta^perp, in the basis f_i = e_i - e_{i+1}, i=0..n-2."""
    n = len(M)
    B = [[F(0)] * n for _ in range(n - 1)]
    for i in range(n - 1):
        B[i][i] = F(1); B[i][i + 1] = F(-1)
    return [[sum(B[a][i] * M[i][j] * B[b][j] for i in range(n) for j in range(n))
             for b in range(n - 1)] for a in range(n - 1)]


def rand_sym(n, seed):
    random.seed(seed)
    M = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            v = F(random.randint(-9, 9))
            M[i][j] = v; M[j][i] = v
    return M


print("EXACT test on 300 random rational symmetric matrices, n = 5..7.")
print("  For each: inertia(Q), inertia(Q|_eta^perp), and min over a c-grid of n_-(Q - c J).")
print()
bad_nec = bad_suf = 0
tally = {}
for t in range(300):
    n = 5 + (t % 3)
    M = rand_sym(n, 1000 + t)
    ineQ = inertia_exact(M)
    Mp = restrict_perp_eta(M)
    ineP = inertia_exact(Mp)
    best = None
    for num, den in [(-10 ** 6, 1), (-1000, 1), (-100, 1), (-10, 1), (-1, 1), (-1, 10), (0, 1),
                     (1, 10), (1, 1), (10, 1), (100, 1), (1000, 1), (10 ** 6, 1)]:
        c = F(num, den)
        Mc = [[M[i][j] - c for j in range(n)] for i in range(n)]
        ine = inertia_exact(Mc)
        if best is None or ine[1] < best[1]:
            best = ine
    feasible_grid = (best[1] == 0)
    # (N) necessary: feasible => Q|perp PSD
    if feasible_grid and ineP[1] > 0:
        bad_nec += 1
    # (S) sufficient: Q|perp strictly PD => feasible
    if ineP[1] == 0 and ineP[2] == 0 and not feasible_grid:
        bad_suf += 1
    key = (ineP[1] == 0 and ineP[2] == 0, feasible_grid)
    tally[key] = tally.get(key, 0) + 1

print(f"  violations of NECESSITY  (feasible but Q|perp indefinite): {bad_nec} / 300")
print(f"  violations of SUFFICIENCY (Q|perp PD but no c on the grid): {bad_suf} / 300")
print(f"  joint tally  (Q|perp strictly PD, feasible on grid) -> count: {tally}")
print()

print("Sanity: eta is even, so the whole ODD sector sits inside eta^perp.")
n = 7
eta = [F(1)] * n
for seed in range(3):
    M = rand_sym(n, 77 + seed)
    odd = []
    for j in range(1, (n - 1) // 2 + 1):
        v = [F(0)] * n
        v[(n - 1) // 2 - j] = F(1); v[(n - 1) // 2 + j] = F(-1)
        odd.append(v)
    ok = all(sum(v) == 0 for v in odd)
    print(f"  n={n} seed={seed}: every odd basis vector orthogonal to eta? {ok}")
print()

print("The X-0001 case O-16005 flagged: Q indefinite yet t* > 0.  Does the gate fail there?")
import sys; sys.path.insert(0, '.')
try:
    import signs as SG
    for pat in [(1, -1, -1), (-1, -1, -1), (1, 1, -1)]:
        A, L = SG.build('200', 6, *pat, dps=60)
        dim = A.rows
        ineA = SG.ldl_inertia(A)
        from mpmath import lu_solve
        x = lu_solve(A, matrix([1] * dim))
        ts = 1 / sum(x[i] for i in range(dim))
        B = matrix(dim, dim)
        for i in range(dim):
            for j in range(dim):
                B[i, j] = A[i, j] - ts
        ineB = SG.ldl_inertia(B)
        gate = (ineB[1] == 0 and ineB[2] == 1)
        print(f"  signs {str(pat):>12}  inertia(Q) {str(ineA):>10}  t* {nstr(ts,8):>13}  "
              f"inertia(Q - t* J) {str(ineB):>10}   PSD with 1-dim kernel? {gate}")
except Exception as e:
    print(f"  (skipped: {type(e).__name__}: {e})")

print()
print("=" * 96)
print("SUFFICIENCY, on instances DESIGNED to satisfy the hypothesis (the random test above")
print("was vacuous: no random integer matrix had Q|_eta^perp strictly PD).")
print("Take Q = M - s*eta*eta^T with M = G^T G + I positive definite and s >= 0 growing.")
print("Then Q|_eta^perp = M|_eta^perp is PD for every s, while Q itself goes indefinite.")
print("=" * 96)
print(f"{'n':>3} {'seed':>5} {'s':>8} {'inertia(Q)':>12} {'inertia(Q|perp)':>16} "
      f"{'min_c n_-(Q-cJ)':>16} {'feasible?':>10}")
print("-" * 88)
for n in (5, 6, 7):
    for seed in (3, 4):
        random.seed(seed * 31 + n)
        G = [[F(random.randint(-4, 4)) for _ in range(n)] for _ in range(n)]
        M = [[sum(G[k][i] * G[k][j] for k in range(n)) + (F(1) if i == j else F(0))
              for j in range(n)] for i in range(n)]
        for s in (F(0), F(1), F(10), F(100), F(10000)):
            Q = [[M[i][j] - s for j in range(n)] for i in range(n)]
            ineQ = inertia_exact(Q)
            ineP = inertia_exact(restrict_perp_eta(Q))
            best = None
            for num, den in [(-10**8,1),(-10**6,1),(-10**4,1),(-100,1),(-10,1),(-1,1),(0,1),
                             (1,1),(10,1),(100,1),(10**4,1),(10**6,1),(10**8,1)]:
                c = F(num, den)
                ine = inertia_exact([[Q[i][j] - c for j in range(n)] for i in range(n)])
                if best is None or ine[1] < best[1]:
                    best = ine
            feas = best[1] == 0
            pd_perp = (ineP[1] == 0 and ineP[2] == 0)
            flag = "OK" if (pd_perp == feas or (pd_perp and feas)) else "MISMATCH"
            if pd_perp and not feas:
                flag = "*** SUFFICIENCY VIOLATED ***"
            print(f"{n:>3} {seed:>5} {str(s):>8} {str(ineQ):>12} {str(ineP):>16} "
                  f"{best[1]:>16} {str(feas):>10}   {flag}")
