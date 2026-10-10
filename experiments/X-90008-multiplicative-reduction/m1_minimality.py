"""M1 — minimality probe for the class H: multiplicative head + FREE tail block.

Adversary: f completely multiplicative +-1 on squarefree k <= K0, arbitrary +-1 signs
on squarefree k in (K0, K] (multiplicativity broken only there). If this hybrid class
breaks the functional for K0/K bounded below 1, then multiplicativity is load-bearing
at all depths and H admits no tail relaxation. Complements T-90007 s.3(ii) prefix-death
(true-mu head + free tail breaks once K/K0 >= 3/2) from the multiplicative side.
Exact: head minimized by the core+fold WHT over the full multiplicative class; free
tail contributes -sum |c| independently (signs decouple: tail k are not products of
head k times class primes in the objective, which is linear with per-k free signs).
"""
import numpy as np, sys, os
SCRATCH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH)
from m1_mult import min_mult_class
from g3_adv import mobius_sieve, coeffs
from mpmath import mp, mpf, log as mlog, sqrt as msqrt
mp.dps = 30

def probe(X, n, ratios=(2, 3/2, 6/5)):
    mu = mobius_sieve(X)
    w = [mpf(0)]*(X+2)
    for q in range(1, X+1): w[q] = mlog(mpf(X)/q)/msqrt(mpf(q))
    K = X//n; W = list(range(n, min(2*n, X+1)))
    print(f"== ({X},{n}) K={K}")
    C = {p: coeffs(X, n, p, w) for p in W}
    for r in ratios:
        K0 = int(K/r)
        worst = 1e9; wp = None
        for p in W:
            c = C[p]
            chead = np.array([c[k] if k <= K0 else 0.0 for k in range(K+1)])
            vhead, _, _ = min_mult_class(chead, K, mu)
            tail = sum(abs(c[k]) for k in range(K0+1, K+1) if mu[k] != 0)
            v = vhead - tail
            if v < worst: worst, wp = v, p
        tag = "BREAKS" if worst < 0 else "holds"
        print(f"   mult head k<={K0} + free tail ({K0},{K}]: min_p = {worst:+.4f} at p={wp}  [{tag}]")

if __name__ == "__main__":
    for (X, n) in [(2000,20), (3000,25), (4000,15)]:
        probe(X, n)
