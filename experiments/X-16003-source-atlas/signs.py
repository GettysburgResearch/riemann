"""
[!] WARNING (added after PR #173 review): the inertia routine in this file uses 1x1
    diagonal pivots only and returns (0,0,2) on [[0,1],[1,0]], whose true inertia is
    (1,1,0) -- it cannot see a hyperbolic negative direction.  Use inertia_correct.py
    instead.  Re-running this file's published tables with the correct routine
    reproduced them identically, but do not reuse the routine below.
"""
"""Do the recovered zeta zeros CERTIFY the relative signs of the three Weil blocks?

D-0001 warns: "A sign swap among source blocks would invalidate all searches", and two
threads in this repo disagree about the archimedean sign.  X-0001 assembles

        value = w_02 - w_r - w_p          (pole, archimedean, prime)

Here we rebuild with independent signs (s0, sr, sp) on the three blocks, and for each
sign pattern ask the two questions that matter:

  (1) is Q positive definite (inertia via LDL^T pivots)?
  (2) do the roots of the CvS kernel polynomial, in the frequency coordinate
      w = 2 pi r / L, reproduce gamma_1 = 14.1347251, gamma_2 = 21.0220396, ... ?

If only the D-0001 pattern passes (2), then the zero recovery is a non-circular
regression test on the sign convention, and the question is settled empirically.

HIGH-PRECISION FLOAT.  Uses X-0001's own closed-form sequences, so this tests the
SIGNS, not the block formulas.
"""
import sys; sys.path.insert(0, '.')
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve, polyroots
import x0001

DPS = 60
CUT, N = '200', 6
GAM = [mpf(v) for v in ['14.134725141734693790', '21.022039638771554993',
                        '25.010857580145688763', '30.424876125859513210']]


def build(cut, N, s0, sr, sp, dps=DPS):
    """Replicates x0001.build_cutoff_free_matrix with per-block signs."""
    with mp.mp.workdps(dps):
        c_value = x0001.coerce_cutoff(cut)
        S, CC, XC, L, _ = x0001.closed_form_sequences(c_value, N, dps=dps)
        pi = mp.pi
        sixteen_pi_sq = 16 * pi * pi
        L2 = L * L
        prefactor = 32 * L * mp.sinh(L / 4) ** 2
        kappa = x0001._kappa(L)
        J = x0001._j_term(L)
        pp = x0001.prime_powers_up_to(int(mp.floor(c_value)))
        weights = [mp.log(p) / mp.sqrt(q) for q, p in pp]
        positions = [mp.log(q) for q, _ in pp]
        dim = 2 * N + 1
        A = mp.matrix(dim, dim)
        for i in range(dim):
            n = i - N
            for j in range(i, dim):
                m = j - N
                w_02 = prefactor * (L2 - sixteen_pi_sq * m * n) / (
                    (L2 + sixteen_pi_sq * m * m) * (L2 + sixteen_pi_sq * n * n))
                if n == m:
                    w_r = kappa + 2 * CC[abs(n)] + J - (2 / L) * XC[abs(n)]
                else:
                    w_r = (x0001._signed_odd_sequence(S, m) - x0001._signed_odd_sequence(S, n)) / (pi * (n - m))
                w_p = mp.mpf("0")
                for weight, y in zip(weights, positions):
                    if n == m:
                        kernel = 2 * (1 - y / L) * mp.cos(2 * pi * n * y / L)
                    else:
                        kernel = (mp.sin(2 * pi * m * y / L) - mp.sin(2 * pi * n * y / L)) / (pi * (n - m))
                    w_p += weight * kernel
                A[i, j] = s0 * w_02 + sr * w_r + sp * w_p
                A[j, i] = A[i, j]
        return A, L


def ldl_inertia(Q):
    n = Q.rows
    A = [[Q[i, j] for j in range(n)] for i in range(n)]
    piv = []
    for k in range(n):
        best = max(range(k, n), key=lambda t: abs(A[t][t]))
        if best != k:
            A[k], A[best] = A[best], A[k]
            for r in range(n):
                A[r][k], A[r][best] = A[r][best], A[r][k]
        d = A[k][k]; piv.append(d)
        if d == 0:
            continue
        for i in range(k + 1, n):
            f = A[i][k] / d
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
            for j in range(k, n):
                A[j][i] = A[i][j]
    tol = max(abs(p) for p in piv) * mpf(10) ** (-mp.mp.dps + 10)
    return (sum(1 for p in piv if p > tol), sum(1 for p in piv if p < -tol),
            sum(1 for p in piv if abs(p) <= tol))


def build_P(xis, N):
    nodes = [mpf(k) for k in range(-N, N + 1)]
    Om = [mpf(1)]
    for k in nodes:
        Om = [(Om[i - 1] if i > 0 else mpf(0)) * (-1) + (Om[i] * k if i < len(Om) else mpf(0))
              for i in range(len(Om) + 1)]
    P = [mpf(0)] * len(nodes)
    for a, lj in enumerate(nodes):
        Omd = Om[::-1]; acc = mpf(0); Qd = []
        for i in range(len(Omd) - 1):
            acc = Omd[i] + acc * lj; Qd.append(acc)
        Qj = [-c for c in Qd[::-1]]
        for i in range(len(Qj)):
            P[i] += xis[a] * Qj[i]
    return P


mp.mp.dps = DPS
print(f"cutoff {CUT}, N={N}, dim={2*N+1}, dps={DPS}.  D-0001 / X-0001 pattern is (+,-,-).")
print(f"{'signs (pole,arch,prime)':>24} {'inertia':>12} {'t*':>15} {'#real':>6}   "
      f"w_1, w_2, w_3, w_4  (targets 14.1347251 21.0220396 25.0108576 30.4248761)")
print("-" * 132)
for s0, sr, sp in [(1, -1, -1), (1, 1, -1), (1, -1, 1), (-1, -1, -1),
                   (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (-1, 1, -1)]:
    A, L = build(CUT, N, s0, sr, sp)
    dim = A.rows
    ine = ldl_inertia(A)
    try:
        x = lu_solve(A, matrix([1] * dim))
        ts = 1 / sum(x[i] for i in range(dim))
        xi = [x[i] * ts for i in range(dim)]
        P = build_P(xi, N)
        rts = polyroots(P[::-1], maxsteps=500, extraprec=4000)
        rr = sorted([mp.re(r) for r in rts if abs(mp.im(r)) < mpf(10) ** (-20) * max(1, abs(mp.re(r)))])
        pos = sorted([v for v in rr if v > 0])
        ws = [2 * mp.pi * v / L for v in pos[:4]]
        hit = sum(1 for k in range(min(4, len(ws))) if abs(ws[k] - GAM[k]) / GAM[k] < mpf('1e-4'))
        tag = f"  <-- matches gamma_1..gamma_{hit}" if hit else "  (no match)"
        print(f"{str((s0,sr,sp)):>24} {str(ine):>12} {nstr(ts,8):>15} {len(rr):>6}   "
              f"{[nstr(w,9) for w in ws]}{tag}")
    except Exception as e:
        print(f"{str((s0,sr,sp)):>24} {str(ine):>12}   solve/roots failed: {type(e).__name__}")
