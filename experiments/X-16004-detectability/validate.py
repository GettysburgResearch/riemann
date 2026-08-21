"""Sanity checks on the machinery before any measurement is trusted."""
import time, sys
import mpmath as mp
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/det')
from loewner import *

mp.mp.dps = 60

print("=== 1. closed form (L-16004) vs divided differences ===")
mus = [mp.mpf(x) for x in ["1.5", "3.25", "7.1", "12.9", "21.2"]]
ws = [mp.mpf(1)] * 5
for N in (3, 5):
    lam = nodes(N)
    for d in (0, "1e-3"):
        P = make_poles(mus, ws, star_index=2, delta=(None if d == 0 else mp.mpf(d)))
        Q1, ir = build_Q_rank1(P, lam)
        Q2 = build_Q_divdiff(P, lam)
        err = max(abs(Q1[i][j] - Q2[i][j]) for i in range(len(lam)) for j in range(len(lam)))
        print("  N=%d delta=%-6s  max|rank1-divdiff| = %.3e   max imag residue = %.3e"
              % (N, d, float(err), float(ir)))

print()
print("=== 2. inertia routine on matrices with known inertia ===")
# diag with known signs, conjugated by a random orthogonal-ish congruence
import random
random.seed(7)
for trial in range(4):
    n = 9
    signs = [random.choice([1, -1]) for _ in range(n)]
    D = [[mp.mpf(0)] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = mp.mpf(signs[i]) * mp.mpf(10) ** random.randint(-25, 3)
    # random unit-triangular congruence  L D L^T  (same inertia by Sylvester)
    L = [[mp.mpf(1) if i == j else (mp.mpf(random.uniform(-2, 2)) if i > j else mp.mpf(0))
          for j in range(n)] for i in range(n)]
    M = [[sum(L[i][k] * D[k][k] * L[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    got = inertia(M)
    want = (sum(1 for s in signs if s > 0), sum(1 for s in signs if s < 0), 0)
    print("  trial %d: got %s want %s  %s" % (trial, got, want, "OK" if got == want else "MISMATCH"))

print()
print("=== 3. L-16004 (ii): #neg eigenvalues == #conjugate pairs ===")
lam = nodes(5)
for nstar, d in ((None, None), (0, mp.mpf("1e-2")), (1, mp.mpf("1e-2"))):
    P = make_poles(mus, ws, nstar, d)
    Q, _ = build_Q_rank1(P, lam)
    print("  star=%-4s delta=%-8s inertia=%s" % (nstar, d, inertia(Q)))

print()
print("=== 4. lambda_min bisection vs eigsy (for reference only) ===")
P = make_poles(mus, ws, None, None)
Q, _ = build_Q_rank1(P, nodes(4))
lmin = lambda_min(Q)
try:
    E = mp.eigsy(mp.matrix(Q), eigvals_only=True)
    print("  bisection lambda_min = %.6e ;  eigsy min = %.6e" % (float(lmin), float(min(E))))
except Exception as e:
    print("  eigsy failed:", e)

print()
print("=== 5. pilot timing ===")
gam = zeta_ordinates(20)
Delta = mp.mpf("1.5")
MUS = [g * Delta for g in gam]
WS = [mp.mpf(1)] * len(MUS)
for N in (4, 6, 8):
    mp.mp.dps = 40 + 5 * N
    t0 = time.time()
    Q = Q_of_delta(N, MUS, WS, None, None)
    t1 = time.time()
    inr = inertia(Q)
    t2 = time.time()
    lm = lambda_min(Q)
    t3 = time.time()
    print("  N=%2d dim=%2d dps=%3d  build %.2fs  inertia %.2fs (%s)  lambda_min %.2fs = %.4e"
          % (N, 2 * N + 1, mp.mp.dps, t1 - t0, t2 - t1, inr, t3 - t2, float(lm)))
