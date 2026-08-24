"""Adversarial re-verification of Strike B claims (independent implementations)."""
import numpy as np, math, sys
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r, sigma_first_entrance

# ---------- 1. B1 Theorem 5: last-far-state decomposition, independent plain-loop check ----------
def children(m):
    a2 = m // 2; b2 = m - a2; a3 = (m + 2) // 3; b3 = m - a3
    return (a2, b2, a3, b3)

def decomposition_check(X, n):
    r = critical_r(X)
    # far occupancy by plain loop (n-independent: recursion over [2n, X] only)
    G = np.zeros(X + 2)
    inflow = np.zeros(X + 2)
    for m in range(X, 2 * n - 1, -1):
        G[m] = m * r[m] + inflow[m]
        g = G[m] / (2.0 * m)
        for c in children(m):
            if c >= 2 * n:
                inflow[c] += c * g
    # parents of p (full set), exact Q via child multiplicity
    def par_candidates(p):
        cands = {2 * p - 1, 2 * p, 2 * p + 1, 3 * p - 2, 3 * p - 1, 3 * p}
        if p % 2 == 0:
            cands |= {3 * p // 2, 3 * p // 2 + 1}
        else:
            cands.add((3 * p + 1) // 2)
        return cands
    ps, sig = sigma_first_entrance(r, X, n)
    worst = 0.0
    for i, p in enumerate(ps):
        tot = p * r[p]
        for m in par_candidates(int(p)):
            if 2 * n <= m <= X:
                mult = sum(1 for c in children(m) if c == p)
                if mult:
                    tot += G[m] * (p / (2.0 * m)) * mult
        worst = max(worst, abs(tot - sig[i]))
    return worst

for (X, n) in [(2997, 311), (2997, 570), (1499, 160), (2000, 250)]:
    w = decomposition_check(X, n)
    print(f"decomposition X={X} n={n}: max |Sigma_branch - (pR+sum G Q)| = {w:.3e}")

# G n-independence: G over [2n,X] depends only on states >= 2n; compare G computed with n=311 vs n=150 on overlap
def farG(X, lo):
    r = critical_r(X)
    G = np.zeros(X + 2); inflow = np.zeros(X + 2)
    for m in range(X, lo - 1, -1):
        G[m] = m * r[m] + inflow[m]
        g = G[m] / (2.0 * m)
        for c in children(m):
            if c >= lo:
                inflow[c] += c * g
    return G
Ga = farG(2997, 622); Gb = farG(2997, 300)
print("G n-independence on [622,2997]: max diff =", np.abs(Ga[622:] - Gb[622:]).max())

# ---------- 2. B1 Theorem 3: Mellin transform identity check ----------
from mpmath import mp, mpf, log, sqrt, zeta, quad
mp.dps = 25
def mob_list(n):
    mu = [0] * (n + 1); mu[1] = 1
    for i in range(1, n + 1):
        if mu[i]:
            for j in range(2 * i, n + 1, i):
                mu[j] -= mu[i]
    return mu
NT = 4000
mul = mob_list(NT + 1)
# D(t) = sum_{k<=t} mu(k) k^{-1/2} (1 + (1/2) log(t/k)); on [N,N+1): D = P_N + (M_N/2) log t
# with M_N = sum mu k^{-1/2}, P_N = M_N - (1/2) sum mu k^{-1/2} log k
M = mpf(0); Aa = mpf(0)
def cell_int(N, s, Mv, Av):
    # int_N^{N+1} [Mv(1+log t/2) - Av/2] t^{-s-1} dt exact
    a, b = mpf(N), mpf(N + 1)
    I0 = (a**-s - b**-s) / s
    I1 = (a**-s * log(a) - b**-s * log(b)) / s + (a**-s - b**-s) / s**2
    return (Mv - Av / 2) * I0 + (Mv / 2) * I1
for s in (mpf(2), mpf('1.2'), mpf('0.8')):
    tot = mpf(0); M = mpf(0); Aa = mpf(0)
    for N in range(1, NT):
        M += mul[N] / sqrt(N); Aa += mul[N] * log(N) / sqrt(N)
        tot += cell_int(N, s, M, Aa)
    rhs = (1 / s + 1 / (2 * s**2)) / zeta(s + mpf('0.5'))
    # crude tail estimate: |D(t)| <= 2 sqrt(t)(1+log t): tail <= int_NT^inf 2 t^{-s-1/2}(1+log t) dt
    print(f"Mellin s={float(s)}: partial={float(tot):+.6f} rhs={float(rhs):+.6f} diff={float(abs(tot-rhs)):.2e}")

# ---------- 3. B3 Theorem Q identity at 50 digits incl q|Y ----------
mp.dps = 50
def bZ(m, Z):
    if m < 2 or m > Z: return mpf(0)
    return 2 * sqrt(m) * (log(mpf(Z) / m) - 2 * (1 - sqrt(mpf(m) / Z)))
def vq(q, Z):
    return sum(bZ(k * q, Z) - bZ(k * q + 1, Z) for k in range(1, Z // q + 1))
def sX(q, X):
    Y = X // 2
    out = vq(q, X) - log(mpf(X) / q) / sqrt(q)
    if q <= Y:
        out -= vq(q, Y) - log(mpf(Y) / q) / sqrt(q)
    return out
def ident(q, X):
    Y = X // 2; L = log(mpf(X) / Y); KY = Y // q; KX = X // q
    t1 = -2 * L * sum(sqrt(k * q + 1) - sqrt(k * q) for k in range(1, KY + 1))
    t2 = 4 * KY * (1 / sqrt(Y) - 1 / sqrt(X))
    t3 = sum(bZ(k * q, X) - bZ(k * q + 1, X) for k in range(KY + 1, KX + 1))
    beta = mpf(0)
    if Y % q == 0:
        beta = 2 * sqrt(Y + 1) * (2 * (sqrt(1 + mpf(1) / Y) - 1) - log(1 + mpf(1) / Y))
    return t1 + t2 + t3 - L / sqrt(q) - beta
for (X, q) in [(200, 5), (200, 4), (201, 10), (1000, 7), (998, 499 // 3)]:
    d = abs(sX(q, X) - ident(q, X))
    print(f"two-scale identity X={X} q={q} (q|Y={ (X//2)%q==0 }): |diff| = {float(d):.2e}")

# ---------- 4. B2 three-crossings claim at c=0.45; single crossing at c=0.5,1/3 ----------
mp.dps = 15
sys.path.insert(0, "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad")
from b2_core import Ec
tg = np.linspace(1e-4, 0.499, 2_000_000)
for c in (0.45, 0.46, 0.5, 1/3):
    v = np.sqrt(tg[tg <= c]) * Ec(tg[tg <= c], c)
    sgn = np.sign(v); flips = np.nonzero(sgn[:-1] * sgn[1:] < 0)[0]
    print(f"c={c:.4f}: sign changes of sqrt(th)E_c on (0,c]: {len(flips)} at theta={[round(float(tg[i]),5) for i in flips[:5]]}")
