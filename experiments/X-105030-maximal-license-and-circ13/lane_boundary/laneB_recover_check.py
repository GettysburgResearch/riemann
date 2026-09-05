"""Recovery cross-check for crashed Lane B agent (a9bd6d6fb35dff45e).
Independent numeric evaluation of F_1(s) (one-large-prime piece, theta=1/2)
via the closed-form term split
  F_1(s) = K(s) D_1(z) + 4/(s-1/2) S2(s) - (3/s) S3(s),  z = s+1/2,
  K(s) = (s+3/2)/(s(s-1/2)),
  D_1(z) = -sum_p p^{-z} M_z(p-),      M_z(t) = sum_{m<=t} mu(m) m^{-z}
  S2(s)  =  sum_p p^{-2s} A(p-),       A(t)   = sum_{m<=t} mu(m)/m
  S3(s)  =  sum_p p^{-2s-1/2} S_h(p-), S_h(t) = sum_{m<=t} mu(m) m^{-1/2}
Also kappa_1 = sum_p A(p-)/p (partial), and full F(s) = K(s)/zeta(z).
"""
import numpy as np
from mpmath import mp, zeta
mp.dps = 20

N = 10**6          # prime/mobius sieve limit for F_1 sums
NK = 10**7         # limit for kappa_1 partial sum

def mobius(n):
    mu = np.ones(n + 1, dtype=np.int8)
    primes_mask = np.ones(n + 1, dtype=bool); primes_mask[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if primes_mask[i]:
            primes_mask[i*i::i] = False
    primes = np.nonzero(primes_mask)[0]
    mu = np.ones(n + 1, dtype=np.float64)
    for p in primes:
        mu[p::p] *= -1
        pp = p * p
        if pp <= n:
            mu[pp::pp] = 0
    mu[0] = 0
    return mu, primes

mu, primes = mobius(N)
m = np.arange(N + 1, dtype=np.float64); m[0] = 1.0

def F1(s):
    z = s + 0.5
    K = (s + 1.5) / (s * (s - 0.5))
    # cumulative sums over m (index t gives sum_{m<=t}); use value at p-1 for m<p
    Mz = np.cumsum(mu * m**(-z))
    A  = np.cumsum(mu / m)
    Sh = np.cumsum(mu * m**(-0.5))
    pm = primes.astype(np.float64)
    D1 = -np.sum(pm**(-z) * Mz[primes - 1])
    S2 =  np.sum(pm**(-2*s) * A[primes - 1])
    S3 =  np.sum(pm**(-2*s - 0.5) * Sh[primes - 1])
    val = K * D1 + 4.0/(s - 0.5) * S2 - (3.0/s) * S3
    return val, D1, S2, S3, K

print("s      F_1(s)      D_1(z)      S2(s)      S3(s)     F(s)=K/zeta(z)  pole-coef 4*(D1+S2)")
for s in [0.6, 0.55, 0.52, 0.51, 0.505]:
    val, D1, S2, S3, K = F1(s)
    F = float(K / zeta(s + 0.5))
    print(f"{s:6.3f} {val:10.4f} {D1:11.5f} {S2:10.5f} {S3:10.5f} {F:12.4f}  {4*(D1+S2):12.6f}")

# kappa_1 partial to 1e7
muK, primesK = mobius(NK)
mK = np.arange(NK + 1, dtype=np.float64); mK[0] = 1.0
AK = np.cumsum(muK / mK)
kappa1 = np.sum(AK[primesK - 1] / primesK.astype(np.float64))
print(f"kappa_1 partial (p<=1e7) = {kappa1:.6f}   (orchestrator reported 0.7372)")

# ledger at s=1/2: F(1/2+)=4 (limit); F_1(1/2) ~ extrapolate; F_sm = F - F_1
for s in [0.505, 0.502, 0.501]:
    val, D1, S2, S3, K = F1(s)
    F = float(K / zeta(s + 0.5))
    print(f"s={s}: F={F:8.4f}  F_1={val:8.4f}  F_sm=F-F_1={F-val:8.4f}")
