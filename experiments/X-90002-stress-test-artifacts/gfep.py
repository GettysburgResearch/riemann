"""GFEP scanner.

Exact definitions implemented (quoted from branch research/gpt56-sol-280-global-fragmentation-spine):

L-28002.1 (critical source):
    w_X(q) = q^{-1/2} log(X/q)  (2<=q<=X; w(1)=0 per L-23810.5, irrelevant for m>=2)
    U_X(m) = sum_{k<=X/m} mu(k) w_X(mk),   R_X(m) = U_X(m) - U_X(m+1)

L-28001.3 (kernel): children of m: a2=floor(m/2), b2=m-a2, a3=ceil(m/3), b3=m-a3;
    Q(m,c) = (c/2m) * multiplicity of c among the four children.

L-28001.10/11 (first entrance): tau_n = first t with Z_t < 2n,
    E_n(m,p) = P_m(Z_{tau_n}=p), = delta_{m,p} for n<=m<2n; paths below n contribute 0.
    Sigma_{X,n}(p) = sum_{m=n}^{X} m R_X(m) E_n(m,p),   n<=p<min(2n,X+1)

L-28001.7: n A_X(n) = sum_{m=n}^X m R_X(m) h_n(m)
L-28001.12: n A_X(n) = sum_p Sigma_{X,n}(p) h_n(p)
"""
import numpy as np


def mobius_sieve(n):
    mu = np.ones(n + 1, dtype=np.int64)
    mu[0] = 0
    primes = []
    comp = np.zeros(n + 1, dtype=bool)
    mu_l = [0] * (n + 1)
    mu_l[1] = 1
    for i in range(2, n + 1):
        if not comp[i]:
            primes.append(i)
            mu_l[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            comp[ip] = True
            if i % p == 0:
                mu_l[ip] = 0
                break
            mu_l[ip] = -mu_l[i]
    return np.array(mu_l, dtype=np.int64)


def critical_r(X, mu=None):
    """Return r[0..X+1] float64, r[m]=R_X(m); w(1)=0 convention (only affects r[1])."""
    if mu is None:
        mu = mobius_sieve(X)
    q = np.arange(1, X + 1, dtype=np.float64)
    w = np.zeros(X + 2)
    w[2:X + 1] = np.log(X / q[1:]) / np.sqrt(q[1:])
    u = np.zeros(X + 2)
    for k in range(1, X + 1):
        mk = mu[k]
        if mk:
            top = X // k
            m = np.arange(1, top + 1)
            u[1:top + 1] += mk * w[m * k]
    r = np.zeros(X + 2)
    r[1:X + 1] = u[1:X + 1] - u[2:X + 2]
    return r


def sigma_first_entrance(r, X, n):
    """Sigma_{X,n}(p) for p in [n, min(2n,X+1)). Vectorized block descent.

    far[m] = m*r[m] for m>=2n propagated down through kernel Q until first
    entrance into [n,2n) (below n: discarded). Diagonal part p*r[p] added.
    """
    upper = min(2 * n, X + 1)
    ps = np.arange(n, upper)
    sigma = ps * r[n:upper]
    if 2 * n > X:
        return ps, sigma
    far = np.zeros(X + 1)
    m_all = np.arange(2 * n, X + 1)
    far[2 * n:] = m_all * r[2 * n:X + 1]
    entrance = np.zeros(2 * n)
    hi = X
    while hi >= 2 * n:
        lo = max(2 * n, (2 * hi) // 3 + 1)
        M = np.arange(lo, hi + 1)
        fm = far[lo:hi + 1]
        g = fm / (2.0 * M)
        a2 = M // 2
        b2 = M - a2
        a3 = (M + 2) // 3
        b3 = M - a3
        idx = np.concatenate((a2, b2, a3, b3))
        wts = np.concatenate((a2 * g, b2 * g, a3 * g, b3 * g))
        buf = np.bincount(idx, weights=wts, minlength=hi)
        # children all < lo (since max child = floor(2m/3) <= floor(2hi/3) < lo)
        if len(buf) > 2 * n:
            far[2 * n:len(buf)] += buf[2 * n:]
        entrance[n:] += buf[n:2 * n]
        hi = lo - 1
    sigma += entrance[n:]
    return ps, sigma


def producer_A(r, X):
    """A[m] from descending recursion (float, loop). O(X)."""
    A = np.zeros(X + 2)
    inc = np.zeros(X + 2)
    for m in range(X, 1, -1):
        A[m] = r[m] + inc[m]
        half = A[m] / 2.0
        a2 = m // 2
        b2 = m - a2
        a3 = (m + 2) // 3
        b3 = m - a3
        for c in (a2, b2, a3, b3):
            if c >= 2:
                inc[c] += half
    return A


def hitting(X, n):
    """h[m] = P_m(hit n), for m in [n, X]."""
    h = np.zeros(X + 1)
    h[n] = 1.0
    for m in range(n + 1, X + 1):
        a2 = m // 2
        b2 = m - a2
        a3 = (m + 2) // 3
        b3 = m - a3
        s = 0.0
        for c in (a2, b2, a3, b3):
            if c >= n:
                s += c * h[c]
        h[m] = s / (2.0 * m)
    return h
