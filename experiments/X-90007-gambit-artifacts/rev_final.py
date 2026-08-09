"""Adversarial reviewer: fully independent re-implementation from T-90003/T-90005/T-90006/T-90007 definitions.
No imports from campaign scripts."""
import numpy as np
from math import log, sqrt, floor, ceil

def mobius_sieve(N):
    mu = np.ones(N+1, dtype=np.int64)
    primes = []
    is_comp = np.zeros(N+1, dtype=bool)
    # linear sieve
    smallest = np.zeros(N+1, dtype=np.int64)
    for i in range(2, N+1):
        if not is_comp[i]:
            primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > N: break
            is_comp[i*p] = True
            if i % p == 0:
                mu[i*p] = 0
                break
            else:
                mu[i*p] = -mu[i]
    mu[0] = 0
    return mu

def children(m):
    a2 = m//2; b2 = m - a2; a3 = -(-m//3); b3 = m - a3
    return [a2, b2, a3, b3]

class Model:
    def __init__(self, X, n):
        self.X, self.n = X, n
        self.mu = mobius_sieve(X+2)
        self.Wlo, self.Whi = n, min(2*n, X+1)   # window [n, Whi)
        self.wp = list(range(self.Wlo, self.Whi))
        # w, U, R, S
        self.w = np.zeros(X+2)
        q = np.arange(1, X+1, dtype=float)
        self.w[1:X+1] = q**-0.5 * np.log(X/q)
        self.U = np.zeros(X+3)
        for m in range(1, X+1):
            K = X//m
            k = np.arange(1, K+1)
            self.U[m] = np.sum(self.mu[k]*self.w[m*k])
        self.R = np.zeros(X+2)
        self.R[1:X+1] = self.U[1:X+1] - self.U[2:X+2]
        self.S = np.zeros(X+2)
        self.S[1:X+1] = np.arange(1, X+1)*self.R[1:X+1]

    def E_table(self):
        """E[m] = first-entrance distribution over window pixels, m in [n,X]."""
        X, n = self.X, self.n
        nw = len(self.wp)
        E = np.zeros((X+2, nw))
        for m in range(n, self.Whi):
            E[m, m-self.Wlo] = 1.0
        for m in range(self.Whi, X+1):
            v = np.zeros(nw)
            for c in children(m):
                if c >= n:
                    v += (c/(2*m))*E[c]
            E[m] = v
        return E

    def sigma_backward(self, E):
        X, n = self.X, self.n
        Sig = np.zeros(len(self.wp))
        for m in range(n, X+1):
            Sig += self.S[m]*E[m]
        return Sig

    def forward_g(self):
        """g on F=[2n,X] by push-down; returns g, window sinks, absorbed-below-n leak."""
        X, n = self.X, self.n
        g = np.zeros(X+2)
        sink = np.zeros(X+2)
        leak = 0.0
        for m in range(2*n, X+1):
            g[m] = self.S[m]
        for m in range(X, 2*n-1, -1):
            for c in children(m):
                q = c/(2*m)
                if c >= 2*n:  g[c] += g[m]*q
                elif c >= n:  sink[c] += g[m]*q
                else:         leak += g[m]*q
        return g, sink, leak

X, n = 2000, 20
M = Model(X, n)
E = M.E_table()
Sig_b = M.sigma_backward(E)
g, sink, leak = M.forward_g()
Sig_f = np.array([M.S[p] + sink[p] for p in M.wp])
print("== delivery identity (backward E vs forward g), (2000,20):",
      np.max(np.abs(Sig_b - Sig_f)))
print("   min_p sqrt-normalized:", min(Sig_b), "at p =", M.wp[int(np.argmin(Sig_b))])
print("   g >= 0 on F:", bool(np.all(g[2*n:X+1] >= 0)))

# Green pairing with random h
rng = np.random.default_rng(7)
h = rng.random(X+2)
lhs = sum(M.S[m]*h[m] for m in range(n, X+1))
Lh = np.zeros(X+2)
for m in range(2*n, X+1):
    Lh[m] = h[m] - sum((c/(2*m))*h[c] for c in children(m) if c >= n)
rhs = sum(Sig_b[i]*h[p] for i, p in enumerate(M.wp)) + sum(g[m]*Lh[m] for m in range(2*n, X+1))
print("== Green pairing random h:", abs(lhs-rhs))

# capture identity h=1
cap_l = sum(M.S[m] for m in range(n, X+1))
Pbelow = np.zeros(X+2)
for m in range(2*n, X+1):
    Pbelow[m] = sum((c/(2*m)) for c in children(m) if c < n)
cap_r = Sig_b.sum() + sum(g[m]*Pbelow[m] for m in range(2*n, X+1))
print("== capture identity:", abs(cap_l-cap_r), " capture frac:", Sig_b.sum()/cap_l)

# Theorem B superharmonicity spot check: h = 1_[k,X]
k = 37
ok = True; strict = True
for m in range(2*n, X+1):
    val = 1.0 - sum((c/(2*m)) for c in children(m) if c >= k)
    pb = sum((c/(2*m)) for c in children(m) if c < k)
    if abs(val-pb) > 1e-15: ok = False
    if k <= m < 2*k and val <= 0: strict = False
print("== Thm B: (L 1_[k,X])(m)=P_m(Z1<k) all m:", ok, "; strict>0 on [k,2k):", strict)
