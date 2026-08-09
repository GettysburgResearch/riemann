"""Sign search for the carry profile  C(y) = sum_{d<=y} mu(d)/sqrt(d) * h(y/d),
h(y) = 8 sqrt(y) - 7 - (3/2) log y  (y>=1),  h = 0 below 1.   [T-23601.1, PR 243]

C(y) >= 0 for all y >= 1 is the open sign statement shared by PRs 243/247/252.
On [n, n+1):  C(y) = 8 sqrt(y) S1(n) - 7 S2(n) - (3/2)(log(y) S2(n) - S3(n))
  with S1 = sum mu(d)/d, S2 = sum mu(d)/sqrt(d), S3 = sum mu(d) log(d)/sqrt(d).
Interior critical point: dC/dy = 4 S1/sqrt(y) - (3/2) S2 / y = 0 -> sqrt(y*) = 3 S2/(8 S1).
Checks y=n, y=(n+1)^-, and y* when inside. Exact-ish float64; flags any value < 0.05
for later exact verification.
"""
import numpy as np
import math

N = 10_000_000

def mobius_sieve(n):
    mu = np.ones(n + 1, dtype=np.int8)
    primes_done = np.zeros(n + 1, dtype=bool)
    for p in range(2, int(n**0.5) + 1):
        if not primes_done[p]:
            primes_done[p*p::p] = True  # mark composites' smallest-prime flags crudely
            mu[p::p] *= -1
            mu[p*p::p*p] = 0
    # crude sieve above misses primes > sqrt(n) toggles; redo properly:
    mu = np.ones(n + 1, dtype=np.int8)
    spf = np.zeros(n + 1, dtype=np.int32)
    for p in range(2, n + 1):
        if spf[p] == 0:
            spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    # factor via spf
    mu[0] = 0
    for i in range(2, n + 1):
        x, last, m, sq = i, 0, 1, False
        while x > 1:
            p = spf[x]
            if p == last:
                sq = True
                break
            last = p
            m = -m
            x //= p
        mu[i] = 0 if sq else m
    return mu

# The pure-python factor loop is too slow for 2e7; do a standard vectorized mobius:
def mobius_fast(n):
    mu = np.ones(n + 1, dtype=np.float64)
    is_comp = np.zeros(n + 1, dtype=bool)
    for p in range(2, n + 1):
        if not is_comp[p]:
            if p <= int(n**0.5) + 1:
                is_comp[p*p::p] = True
            mu[p::p] *= -1
            if p * p <= n:
                mu[p*p::p*p] = 0
    mu[0] = 0
    return mu

print("sieving...")
mu = mobius_fast(N)
d = np.arange(N + 1, dtype=np.float64)
d[0] = 1.0
print("prefix sums...")
S1 = np.cumsum(mu / d)
S2 = np.cumsum(mu / np.sqrt(d))
S3 = np.cumsum(mu * np.log(d) / np.sqrt(d))

print("scanning...")
n = np.arange(1, N, dtype=np.float64)          # interval [n, n+1)
s1, s2, s3 = S1[1:N], S2[1:N], S3[1:N]
sq_n  = np.sqrt(n)
sq_n1 = np.sqrt(n + 1)
C_left  = 8*sq_n *s1 - 7*s2 - 1.5*(np.log(n)*s2 - s3)
C_right = 8*sq_n1*s1 - 7*s2 - 1.5*(np.log(n+1)*s2 - s3)
with np.errstate(divide="ignore", invalid="ignore"):
    sq_star = 3.0*s2/(8.0*s1)
    y_star = sq_star**2
    inside = (s1 != 0) & (y_star > n) & (y_star < n + 1) & (sq_star > 0)
    C_star = np.where(inside,
                      8*sq_star*s1 - 7*s2 - 1.5*(2*np.log(np.maximum(sq_star,1e-300))*s2 - s3),
                      np.inf)
C_min = np.minimum(np.minimum(C_left, C_right), C_star)
gmin = np.nanmin(C_min)
gargmin = int(np.nanargmin(C_min)) + 1
print(f"global min over scan: C = {gmin:.6f} near y = {gargmin}")
bad = np.where(C_min < 0.05)[0]
print(f"points with C < 0.05: {len(bad)}")
for i in bad[:20]:
    print(f"  y~{i+1}: C_left={C_left[i]:.6f} C_right={C_right[i]:.6f}")
for Y in [10, 100, 1000, 10**4, 10**5, 10**6, 2*10**7 - 2]:
    i = Y - 1
    print(f"C({Y}) = {C_left[i]:.4f}   1.027*log y = {1.02715*math.log(Y):.4f}")
