import numpy as np
from math import comb, log, sqrt
NMAX = 200000
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
    return np.where((y > 0.5) & (y <= 1.0), np.log(2*np.asarray(y,dtype=float))/ln2, 0.0)
