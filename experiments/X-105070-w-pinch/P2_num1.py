import numpy as np
from math import comb, log, sqrt

NMAX = 200000
# sieve mu and eta (coeffs of zeta^{1/2}: eta(p^k)=C(2k,k)/4^k), via spf
spf = np.zeros(NMAX+1, dtype=np.int64)
for i in range(2, NMAX+1):
    if spf[i] == 0:
        spf[i::i][spf[i::i] == 0] = i  # wrong for slices; do below properly
spf = np.zeros(NMAX+1, dtype=np.int64)
for p in range(2, NMAX+1):
    if spf[p] == 0:
        spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
mu = np.zeros(NMAX+1, dtype=np.int64); mu[1] = 1
eta = np.zeros(NMAX+1); eta[1] = 1.0
etapk = [comb(2*k, k)/4**k for k in range(0, 40)]
for n in range(2, NMAX+1):
    p = spf[n]; m = n // p; k = 1
    while m % p == 0: m //= p; k += 1
    mu[n] = 0 if k > 1 else -mu[m]
    eta[n] = eta[m] * etapk[k]

ln2 = log(2.0)
def v(y):
    return np.where((y > 0.5) & (y <= 1.0), np.log(2*y)/ln2, 0.0)

def Lambda_true(X):
    U = int(X**(1/3)); N = int(X/U)
    n = np.arange(N//2+1, N+1)
    # h_U(n) = sum_{d|n, d>U} mu(d) eta(n/d): compute via pair loop over d
    h = np.zeros(len(n))
    for d in range(U+1, N+1):
        if mu[d] == 0: continue
        lo = ((N//2)//d+1)*d
        if lo > N: continue
        m = np.arange(lo, N+1, d)
        h[(m - (N//2+1))] += mu[d]*eta[m//d]
    tent = np.log(2*n/N)/ln2
    return float(np.sum(h*n**(-0.5)*tent)), U, N

def Lambda_star(X):
    X23 = X**(2/3); X13 = X**(1/3)
    tot = 0.0
    dmax = int(X23)
    d = np.arange(int(np.floor(X13))+1, dmax+1)
    d = d[mu[d] != 0]
    # e-range per d: e in (X23/(2d), X23/d]
    ehi = np.floor(X23/d).astype(np.int64)
    elo = np.floor(X23/(2*d)).astype(np.int64)
    for di, eh, el in zip(d, ehi, elo):
        if eh <= el: continue
        e = np.arange(el+1, eh+1)
        y = di*e/X23
        tot += mu[di]*di**(-0.5)*np.sum(eta[e]*e**(-0.5)*v(y))
    return tot

def V_true(X):
    L, U, N = Lambda_true(X)
    return L*sqrt(log(N))/X**(1/6)

def V_star(X):
    return Lambda_star(X)*sqrt((2/3)*log(X))/X**(1/6)

print("== A0 check: V vs V* ==")
rng = np.random.default_rng(7)
Xs = sorted(np.exp(rng.uniform(log(100), log(2.0e6), 14)))
diffs = []
for X in Xs:
    a, b = V_true(X), V_star(X)
    diffs.append((X, a, b, a-b))
    print(f"X={X:12.1f}  V={a:+.5f}  V*={b:+.5f}  diff={a-b:+.2e}")
print("max|diff|", max(abs(d[3]) for d in diffs))
