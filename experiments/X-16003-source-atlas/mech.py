"""
[!] WARNING (added after PR #173 review): the inertia routine in this file uses 1x1
    diagonal pivots only and returns (0,0,2) on [[0,1],[1,0]], whose true inertia is
    (1,1,0) -- it cannot see a hyperbolic negative direction.  Use inertia_correct.py
    instead.  Re-running this file's published tables with the correct routine
    reproduced them identically, but do not reuse the routine below.
"""
"""Is the CvS finite gate a POLE DETECTOR for the source?

Two exact structural identities, then a synthetic control.

(I)  P_xi(s) = sum_j xi_j prod_{k!=j}(lam_k - s) = Omega(s) * <xi, ell(s)>,
     Omega(s) = prod_k (lam_k - s),  ell(s)_j = 1/(lam_j - s).
     [Exact: prod_{k!=j}(lam_k-s) = Omega(s)/(lam_j-s).]

(II) If psi(x) = sum_mu a_mu/(mu - x) with a_mu real, then (L-16004)
     Loewner(psi) = sum_mu a_mu ell(mu) ell(mu)^T,  EXACT.
     So <ell(mu), xi> = P_xi(mu)/Omega(mu): the Gram coefficients of the kernel
     vector ARE the values of its polynomial at the poles of the source.

Prediction: the roots of P_xi should sit at (or near) the poles mu of psi -- for ANY
source of this shape, arithmetic or not.  If a synthetic source with poles at, say,
{11, 19, 27, ...} produces roots at {11, 19, 27, ...}, then O-16004's "the roots are
the zeta zeros" is fully explained by "psi_W's poles are the zeta zeros", i.e. by the
explicit formula, and carries no extra information.

Everything below is HIGH-PRECISION FLOAT (mpmath) unless marked EXACT.
"""
import sys
from mpmath import mp, mpf, nstr, matrix, lu_solve, polyroots

mp.dps = 60


def loewner(psi, dpsi, nodes):
    n = len(nodes)
    Q = matrix(n, n)
    for i in range(n):
        for j in range(n):
            Q[i, j] = dpsi(nodes[i]) if i == j else (psi(nodes[i]) - psi(nodes[j])) / (nodes[i] - nodes[j])
    return Q


def pole_source(poles, weights):
    """psi(x) = sum a_mu/(mu - x), summed over +-mu so psi is odd."""
    def psi(x):
        return sum(a * (1 / (m - x) + 1 / (-m - x)) for m, a in zip(poles, weights))
    def dpsi(x):
        return sum(a * (1 / (m - x) ** 2 + 1 / (-m - x) ** 2) for m, a in zip(poles, weights))
    return psi, dpsi


def build_P(xis, nodes):
    """P(s) = sum_j xi_j prod_{k!=j}(lam_k - s), ascending coefficients."""
    n = len(nodes)
    Om = [mpf(1)]
    for k in nodes:
        Om = [(Om[i - 1] if i > 0 else mpf(0)) * (-1) + (Om[i] * k if i < len(Om) else mpf(0))
              for i in range(len(Om) + 1)]
    P = [mpf(0)] * n
    for a, lj in enumerate(nodes):
        Omd = Om[::-1]; acc = mpf(0); Qd = []
        for i in range(len(Omd) - 1):
            acc = Omd[i] + acc * lj; Qd.append(acc)
        Qj = [-c for c in Qd[::-1]]
        for i in range(len(Qj)):
            P[i] += xis[a] * Qj[i]
    return P


def peval(P, s):
    acc = mpf(0) * s
    for c in reversed(P):
        acc = acc * s + c
    return acc


def inertia_ldl(Q):
    """Numerical LDL^T inertia with symmetric pivoting; HIGH-PRECISION FLOAT."""
    n = Q.rows
    A = [[Q[i, j] for j in range(n)] for i in range(n)]
    piv = []
    idx = list(range(n))
    for k in range(n):
        # pick largest |diagonal| among remaining
        best = max(range(k, n), key=lambda t: abs(A[t][t]))
        if best != k:
            A[k], A[best] = A[best], A[k]
            for r in range(n):
                A[r][k], A[r][best] = A[r][best], A[r][k]
        d = A[k][k]
        piv.append(d)
        if d == 0:
            continue
        for i in range(k + 1, n):
            f = A[i][k] / d
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
            for j in range(k, n):
                A[j][i] = A[i][j]
    tol = max(abs(p) for p in piv) * mpf(10) ** (-mp.dps + 8)
    return (sum(1 for p in piv if p > tol), sum(1 for p in piv if p < -tol),
            sum(1 for p in piv if abs(p) <= tol)), piv


def run(name, poles, weights, N, show=8):
    nodes = [mpf(k) for k in range(-N, N + 1)]
    psi, dpsi = pole_source(poles, weights)
    Q = loewner(psi, dpsi, nodes)
    ine, piv = inertia_ldl(Q)
    dim = 2 * N + 1
    eta = matrix([1] * dim)
    x = lu_solve(Q, eta)
    denom = sum(x[i] for i in range(dim))
    tstar = 1 / denom
    xi = [x[i] * tstar for i in range(dim)]
    P = build_P(xi, nodes)
    rts = polyroots(P[::-1], maxsteps=500, extraprec=4000)
    rr = sorted([mp.re(r) for r in rts if abs(mp.im(r)) < mpf(10) ** (-20) * max(1, abs(mp.re(r)))])
    pos = [v for v in rr if v > 0]
    print(f"--- {name}  N={N}  dim={dim} ---")
    print(f"  inertia(Q)          {ine}   (L-16004: PSD iff all poles real & weights>0)")
    print(f"  t* = 1/(eta^T Q^-1 eta) = {nstr(tstar, 10)}")
    print(f"  #real roots of P    {len(rr)}/{len(P)-1}")
    print(f"  true poles (+)      {[nstr(m, 10) for m in poles[:show]]}")
    print(f"  recovered roots (+) {[nstr(v, 10) for v in pos[:show]]}")
    if pos:
        k = min(len(pos), len(poles))
        rel = [abs(pos[i] - poles[i]) / poles[i] for i in range(k)]
        print(f"  rel. error          {[nstr(r, 3) for r in rel[:show]]}")
    m = max(abs(v) for v in xi)
    print(f"  (-1)^j xi_j / max   {[nstr((-1) ** j * xi[a] / m, 6) for a, j in enumerate(range(-N, N + 1))][N:]}")
    print()
    return pos


print("=" * 100)
print("(I) EXACT identity check: P_xi(s) == Omega(s) * <xi, ell(s)> on random xi, random s")
print("=" * 100)
import random
random.seed(11)
N = 5
nodes = [mpf(k) for k in range(-N, N + 1)]
xi = [mpf(random.randint(-50, 50)) for _ in nodes]
P = build_P(xi, nodes)
worst = mpf(0)
for _ in range(6):
    s = mpf(random.randint(-400, 400)) / 7
    Om = mpf(1)
    for k in nodes:
        Om *= (k - s)
    rhs = Om * sum(xi[j] / (nodes[j] - s) for j in range(len(nodes)))
    worst = max(worst, abs(peval(P, s) - rhs) / max(mpf(1), abs(rhs)))
print(f"  worst relative discrepancy over 6 random s : {nstr(worst, 5)}   (0 = identity holds)\n")

print("=" * 100)
print("(II) SYNTHETIC CONTROL -- non-arithmetic poles.  Does the gate find them?")
print("=" * 100)
# Poles deliberately unrelated to zeta.  Weights ~ 1 (like sum_rho 1/(s-rho) residues).
run("poles at 11,19,27,35,43,51 (arith. progression), unit weights",
    [mpf(v) for v in [11, 19, 27, 35, 43, 51]], [mpf(1)] * 6, N=6)
run("poles at the first 6 primes*7 = 14,21,35,49,77,91, unit weights",
    [mpf(v) for v in [14, 21, 35, 49, 77, 91]], [mpf(1)] * 6, N=6)
run("poles at 5, 6.5, 40, 41.3, 200, 201 (two close pairs + one), unit weights",
    [mpf(5), mpf(13)/2, mpf(40), mpf(413)/10, mpf(200), mpf(201)], [mpf(1)] * 6, N=6)
run("poles at 11,19,27,35,43,51 -- SAME, but N=10 (more nodes than poles)",
    [mpf(v) for v in [11, 19, 27, 35, 43, 51]], [mpf(1)] * 6, N=10)
