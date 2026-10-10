"""Recovery check 2: (a) P-truncation sweep of closed-form F_1(s);
(b) direct x-space sieve of Psi_1(x), Psi_sm(x), Psi(x) with partition check
    and growth measurement vs prediction Psi_1(x) ~ -4 sqrt(x)/log x."""
import numpy as np

NMAX = 10**7

def mobius_primes(n):
    sieve_ = np.ones(n + 1, dtype=bool); sieve_[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve_[i]: sieve_[i*i::i] = False
    primes = np.nonzero(sieve_)[0]
    mu = np.ones(n + 1, dtype=np.float64)
    for p in primes:
        mu[p::p] *= -1
        pp = p * p
        if pp <= n: mu[pp::pp] = 0
    mu[0] = 0
    return mu, primes

mu, primes = mobius_primes(NMAX)
marr = np.arange(NMAX + 1, dtype=np.float64); marr[0] = 1.0

def F1_partial(s, P):
    z = s + 0.5
    K = (s + 1.5) / (s * (s - 0.5))
    pr = primes[primes <= P]
    Mz = np.cumsum(mu * marr**(-z))
    A  = np.cumsum(mu / marr)
    Sh = np.cumsum(mu * marr**(-0.5))
    pm = pr.astype(np.float64)
    D1 = -np.sum(pm**(-z) * Mz[pr - 1])
    S2 =  np.sum(pm**(-2*s) * A[pr - 1])
    S3 =  np.sum(pm**(-2*s - 0.5) * Sh[pr - 1])
    return K * D1 + 4.0/(s - 0.5) * S2 - (3.0/s) * S3

print("=== (a) P-truncation sweep of F_1(s) ===")
print("P        s=0.6      s=0.55     s=0.52     s=0.51     s=0.505")
for P in [10**4, 10**5, 10**6, 3*10**6, 10**7]:
    vals = [F1_partial(s, P) for s in (0.6, 0.55, 0.52, 0.51, 0.505)]
    print(f"{P:<8d} " + " ".join(f"{v:9.4f}" for v in vals))

print()
print("=== (b) x-space: Psi_1, Psi_sm, Psi at sample x; partition check ===")
mu_i = mu  # float with 0/+-1

def Psi_total(x):
    n = np.arange(1, x + 1, dtype=np.float64)
    T = 4.0*np.sqrt(x/n) - 3.0
    return float(np.sum(mu[1:x+1] * n**(-0.5) * T))

def Psi_1(x):
    # n = m p, p > sqrt(x), m <= x/p; mu(n) = -mu(m)
    sx = int(np.floor(np.sqrt(x)))
    pr = primes[(primes > sx) & (primes <= x)]
    tot = 0.0
    for p in pr:
        M = int(x // p)
        mm = np.arange(1, M + 1, dtype=np.float64)
        n = mm * p
        T = 4.0*np.sqrt(x/n) - 3.0
        tot += float(np.sum(-mu[1:M+1] * n**(-0.5) * T))
    return tot

print("x        Psi(x)      Psi_1(x)    Psi_sm=Psi-Psi_1   -4sqrt(x)/log(x)   Psi_1*logx/sqrtx")
for x in [10**4, 10**5, 3*10**5, 10**6, 3*10**6, 10**7]:
    Pt = Psi_total(x); P1 = Psi_1(x)
    pred = -4.0*np.sqrt(x)/np.log(x)
    print(f"{x:<8d} {Pt:10.4f} {P1:11.3f} {Pt-P1:12.3f} {pred:14.3f} {P1*np.log(x)/np.sqrt(x):12.4f}")

print()
print("=== direct partition validation at x=10^4 (independent classification) ===")
x = 10**4
sx = np.sqrt(x)
# classify each n<=x: does n have a prime factor > sqrt(x)?
n_arr = np.arange(x + 1)
largest = np.zeros(x + 1, dtype=np.int64)
for p in primes[primes <= x]:
    largest[p::p] = p
P1_direct = 0.0; Psm_direct = 0.0
nn = np.arange(1, x + 1, dtype=np.float64)
T = 4.0*np.sqrt(x/nn) - 3.0
contrib = mu[1:x+1] * nn**(-0.5) * T
mask_rough = largest[1:x+1] > sx
print("Psi_1 by classification:", float(np.sum(contrib[mask_rough])),
      " | by pair formula:", Psi_1(x))
print("Psi_sm by classification:", float(np.sum(contrib[~mask_rough])))
