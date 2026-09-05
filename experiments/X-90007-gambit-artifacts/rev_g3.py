"""G3 re-verification: kernel form, positivity census, adversarial refutation, pattern check, tau dictionary."""
import numpy as np
from math import log, sqrt
from rev_final import Model, children

def kernels(M, E):
    """c_p(k) = sum_{m>=n, mk<=X} dG_p(m) w(mk); returns dict k -> vector over window p."""
    X, n = M.X, M.n
    nw = len(M.wp)
    G = np.zeros((X+2, nw))
    for m in range(n, X+1):
        G[m] = m*E[m]
    dG = np.zeros((X+2, nw))
    dG[n] = G[n]
    for m in range(n+1, X+1):
        dG[m] = G[m] - G[m-1]
    c = {}
    for k in range(1, X//n + 1):
        mmax = X//k
        if mmax < n: break
        v = np.zeros(nw)
        for m in range(n, mmax+1):
            v += dG[m]*M.w[m*k]
        c[k] = v
    return c

def check_config(X, n, K0=40):
    M = Model(X, n)
    E = M.E_table()
    Sig = M.sigma_backward(E)
    c = kernels(M, E)
    Kmax = X//n
    # identity: Sigma(p) = sum_k mu(k) c_p(k)
    rec = np.zeros(len(M.wp))
    for k, v in c.items():
        rec += M.mu[k]*v
    print(f"({X},{n}): kernel-form identity max|diff| = {np.max(np.abs(rec-Sig)):.2e}")
    # census over squarefree k
    sf = [k for k in c if M.mu[k] != 0]
    minc = min(c[k].min() for k in sf)
    npairs = sum(len(M.wp) for k in sf)
    print(f"   kernel census: {npairs} (p,k) sf pairs, min c_p(k) = {minc:.3e}  (>=0? {minc >= 0})")
    # adversarial eps: true mu below K0, -1 on squarefree above
    eps = np.zeros(Kmax+1)
    for k in range(1, Kmax+1):
        eps[k] = M.mu[k] if k <= K0 else (-1.0 if M.mu[k] != 0 else 0.0)
    SigE = np.zeros(len(M.wp))
    for k in sf:
        SigE += eps[k]*c[k]
    pmin = M.wp[int(np.argmin(SigE))]
    print(f"   adversarial (kernel path): min_p Sigma^eps = {SigE.min():.6f} at p={pmin}")
    # independent path: U^eps -> S^eps -> pair with E
    Ue = np.zeros(X+3)
    for m in range(n, X+2):
        tot = 0.0
        for k in range(1, X//m + 1 if m <= X else 1):
            if k <= Kmax and eps[k] != 0:
                tot += eps[k]*M.w[m*k]
        Ue[m] = tot
    Se = np.zeros(X+2)
    for m in range(n, X+1):
        Se[m] = m*(Ue[m]-Ue[m+1])
    SigE2 = np.zeros(len(M.wp))
    for m in range(n, X+1):
        SigE2 += Se[m]*E[m]
    print(f"   adversarial (flow path):   min_p = {SigE2.min():.6f}; paths agree to {np.max(np.abs(SigE-SigE2)):.2e}")
    # NOTE: eps has support only k <= Kmax=X//n; for m >= n all mk<=X terms have k<=Kmax. OK.
    # pattern check: C^eps_N <= 0 at both endpoints, N in [5, Kmax]
    viol = 0; tot = 0
    Mn = 0.0; An = 0.0
    Mv = np.zeros(Kmax+1); Av = np.zeros(Kmax+1)
    for k in range(1, Kmax+1):
        Mn += eps[k]/sqrt(k); An += eps[k]*log(k)/sqrt(k)
        Mv[k] = Mn; Av[k] = An
    for N in range(5, Kmax+1):
        for L in (log(N), log(N+1)):
            tot += 1
            if (1+L/2)*Mv[N] - Av[N]/2 > 1e-12:
                viol += 1
    print(f"   pattern C^eps_N<=0, N in [5,{Kmax}]: {viol}/{tot} endpoint violations")
    # true-mu margin for contrast
    print(f"   true-mu min_p Sigma = {Sig.min():.6f} at p={M.wp[int(np.argmin(Sig))]}")
    return M, E, c

check_config(2000, 20)
check_config(3000, 25)

# tau dictionary (Theorem 1a) for a random eps, numerically integrated
import mpmath as mp
mp.mp.dps = 30
rng = np.random.default_rng(11)
Kbig = 60
from rev_final import mobius_sieve
mub = mobius_sieve(Kbig+1)
eps = {k: float(rng.choice([-1.0, 1.0])) for k in range(1, Kbig+1) if mub[k] != 0}
def MA(N):
    Mn = sum(e/mp.sqrt(k) for k, e in eps.items() if k <= N)
    An = sum(e*mp.log(k)/mp.sqrt(k) for k, e in eps.items() if k <= N)
    return Mn, An
def Ceps(N, L):
    Mn, An = MA(N)
    return (1+L/2)*Mn - An/2
for theta in (mp.mpf(1)/mp.mpf('7.3'), mp.mpf(1)/mp.mpf('20.5'), mp.mpf(1)/mp.mpf(43)):
    K = int(mp.floor(1/theta))
    # integrate cell by cell
    I = mp.mpf(0)
    lo = theta
    for N in range(K, 0, -1):
        hi = mp.mpf(1)/N if N > 1 else mp.mpf(1)
        a = max(lo, mp.mpf(1)/(N+1))
        I += mp.quad(lambda t: t**mp.mpf('-0.5')*Ceps(N, mp.log(1/t)), [a, hi])
        lo = hi
    m_eps = sum(e/k for k, e in eps.items() if k <= 1/theta)
    Mn, An = MA(K)
    closed = 4*m_eps - mp.sqrt(theta)*((4+mp.log(1/theta))*Mn - An)
    print(f"tau dictionary at 1/theta={float(1/theta):.2f}: |integral-closed| = {float(abs(I-closed)):.2e}")

# counting inversion sum_{k<=X/m} U(mk) = w(m), and R integral form vs cells
X = 1000
M1000 = Model(X, 2)
for m in (1, 3, 7, 50, 313):
    s = sum(M1000.U[m*k] for k in range(1, X//m + 1))
    print(f"inversion m={m}: |sum_k U(mk) - w(m)| = {abs(s - M1000.w[m]):.2e}")
# R integral form (T-90003 Lemma 1) spot check with mpmath
def Rint(X, m):
    def integrand(t):
        N = int(mp.floor(1/t))
        Mn = sum(int(M1000.mu[k])/mp.sqrt(k) for k in range(1, N+1))
        An = sum(int(M1000.mu[k])*mp.log(k)/mp.sqrt(k) for k in range(2, N+1))
        L = mp.log(1/t)
        return t**mp.mpf('-1.5')*((1+L/2)*Mn - An/2)
    lo = mp.mpf(m)/X; hi = mp.mpf(m+1)/X
    knots = sorted({lo, hi} | {mp.mpf(1)/N for N in range(int(mp.ceil(1/hi)), int(mp.floor(1/lo))+1) if lo < mp.mpf(1)/N < hi})
    I = mp.mpf(0)
    for a, b in zip(knots[:-1], knots[1:]):
        I += mp.quad(integrand, [a, b])
    return I/mp.sqrt(X)
for m in (137, 249):
    print(f"R integral form m={m}: |int - R| = {float(abs(Rint(X, m) - M1000.R[m])):.2e}")
