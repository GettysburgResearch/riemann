"""CORRECTED blind-cutoff detectability.  My published version had two defects, both found
by review; this fixes both and the conclusion INVERTS.

Defect 1 (physics).  The reviewer's exact packet identity is
      g_u(z) = (L/pi^2) sin^2(pi mu) <u, ell(mu)>^2,     mu = Delta z.
The residue is NOT a frozen real constant a(gamma): the sin^2 factor is part of the
analytic packet and must be continued with the pole.  blinddet.py froze a(gamma) at its
tiny real value and moved only the poles, so it never introduced the term that matters.
At mu = k + i y with k an integer, sin^2(pi(k+iy)) = -sinh^2(pi y) < 0.

Defect 2 (numerics).  The inertia routine used 1x1 diagonal pivots only and 'continue'd on
a zero pivot; on [[0,1],[1,0]] it reports (0,0,2) instead of (1,1,0).  Replaced by an
exact-style congruence with hyperbolic 2x2 blocks.

Model: Q = sum over zeros of (L/pi^2) sin^2(pi mu) ell(mu) ell(mu)^T, mu = Delta*z.
On-line zero -> z = +-gamma (2 zeros).  Off-line -> the functional equation forces the
quadruple z = +-gamma +- i*delta (4 zeros), each taken with weight 1/2 to preserve count.
|Re rho - 1/2| = delta.
"""
import mpmath as mp
from mpmath import mpf, mpc, nstr

def inertia(Q):
    """Congruence with 1x1 AND hyperbolic 2x2 pivots.  Returns (n+, n-, n0)."""
    n = len(Q); A = [[Q[i][j] for j in range(n)] for i in range(n)]
    idx = list(range(n)); pos = neg = zer = 0
    tol = mpf(10) ** (-mp.mp.dps + 10)
    scale = max((abs(A[i][j]) for i in range(n) for j in range(n)), default=mpf(1))
    if scale == 0: scale = mpf(1)
    while idx:
        k = None
        for i in idx:
            if abs(A[i][i]) > tol * scale: k = i; break
        if k is None:
            piv = None
            for a_ in range(len(idx)):
                for b_ in range(a_ + 1, len(idx)):
                    if abs(A[idx[a_]][idx[b_]]) > tol * scale:
                        piv = (idx[a_], idx[b_]); break
                if piv: break
            if piv is None:
                zer += len(idx); break
            i, j = piv                      # hyperbolic block: e_i -> e_i + e_j
            for r in range(n): A[r][i] = A[r][i] + A[r][j]
            for r in range(n): A[i][r] = A[i][r] + A[j][r]
            continue
        d = A[k][k]
        pos += 1 if d > 0 else 0
        neg += 1 if d < 0 else 0
        rest = [i for i in idx if i != k]
        for i in rest:
            f = A[i][k] / d
            if f != 0:
                for j in rest: A[i][j] = A[i][j] - f * A[k][j]
        idx = rest
    return (pos, neg, zer)

GAMS = None
def gammas(n):
    global GAMS
    if GAMS is None or len(GAMS) < n:
        GAMS = [mp.im(mp.zetazero(k)) for k in range(1, n + 1)]
    return GAMS[:n]

def build(L, N, M, delta, dps):
    mp.mp.dps = dps
    Delta = L / (2 * mp.pi); dim = 2 * N + 1
    nodes = [mpf(j) for j in range(-N, N + 1)]
    Q = [[mpf(0)] * dim for _ in range(dim)]
    def add(z, wt):
        mu = Delta * z
        ell = [1 / (nodes[j] - mu) for j in range(dim)]
        pref = wt * (L / mp.pi ** 2) * mp.sin(mp.pi * mu) ** 2   # <-- continued, not frozen
        for i in range(dim):
            for j in range(dim):
                Q[i][j] += mp.re(pref * ell[i] * ell[j])
    for idx, g in enumerate(gammas(M)):
        if idx == 0 and delta > 0:
            for zz in (g - mpc(0,1)*delta, g + mpc(0,1)*delta,
                       -g - mpc(0,1)*delta, -g + mpc(0,1)*delta):
                add(zz, mpf(1)/2)
        else:
            add(mpf(g), mpf(1)); add(-mpf(g), mpf(1))
    return Q

def delta_c(L, N, M, dps, lo=mpf('1e-30'), hi=mpf('1e2')):
    if inertia(build(L, N, M, hi, dps))[1] == 0: return None
    if inertia(build(L, N, M, lo, dps))[1] > 0: return lo
    for _ in range(45):
        mid = mp.sqrt(lo * hi)
        if inertia(build(L, N, M, mid, dps))[1] > 0: hi = mid
        else: lo = mid
    return mp.sqrt(lo * hi)

N, M, dps = 10, 25, 110
mp.mp.dps = dps
G1 = gammas(1)[0]
print(f"N={N}, M={M} zeros, dps={dps}.  CORRECTED: residue continued, 2x2 pivots enabled.")
print(f"{'c':>10} {'g1*Delta':>11} {'frac':>8} {'sin^2(pi mu) at':>0}")
print(f"{'c':>10} {'g1*Delta':>11} {'frac':>8} {'a_1 (on-line)':>15} {'unpert n_-':>11} "
      f"{'delta_c':>14}  reading")
print("-" * 96)
for c in ['9.23136','11.529','14.3985','17.9823','22.458','28.0478','35.0288','43.7473','54.6359']:
    mp.mp.dps = dps
    L = mp.log(mpf(c)); r1 = G1 * L / (2 * mp.pi); frac = r1 - mp.floor(r1)
    a1 = (L / mp.pi ** 2) * mp.sin(mp.pi * r1) ** 2
    ne = inertia(build(L, N, M, mpf(0), dps))[1]
    dc = delta_c(L, N, M, dps)
    mp.mp.dps = 25
    near_int = (frac < mpf('0.05') or frac > mpf('0.95'))
    tag = "INTEGER (was called 'blind')" if near_int else "half-integer"
    print(f"{c:>10} {nstr(r1,9):>11} {nstr(frac,3):>8} {nstr(a1,8):>15} {ne:>11} "
          f"{(nstr(dc,8) if dc else 'never'):>14}  {tag}")
