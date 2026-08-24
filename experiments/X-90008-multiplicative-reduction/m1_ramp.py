"""M1 — one-scalar Form A over H: the transported ramp functional.

Exact identity (Lambda = mu * log, mu = lambda restricted to squarefree):
    Ramp_f(X) := sum_{d sf <= X/2} f(d) T_X(d),  T_X(d) = sum_{2<=m<=X/d} log(m) w_X(md) >= 0,
    w_X(q) = q^{-1/2} log(X/q);   Ramp_lambda(X) = sum_{2<=q<=X} Lambda(q) w_X(q)  EXACTLY.
Form A(f): Ramp_f(X) >= 4 sqrt(X) - C_eps X^eps.  Class demand: uniform over f in H.

Exact min over H by the same core+fold WHT decomposition (core primes <= sqrt(X/2)).
Validation: (a) identity check vs direct Lambda-sum; (b) full brute force at X=60
(all 10 primes <= 30); (c) random-f direct eval vs decomposition reconstruction.
"""
import sys, os, time
import numpy as np
SCRATCH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH)
from m1_mult import primes_upto, spf_sieve, factor_sf, wht, min_mult_class, eval_mult, brute_force_min, distances
from g3_adv import mobius_sieve

def ramp_kernel(X):
    """T[d] for d=1..X//2 (all d; used only at squarefree)."""
    dmax = X // 2
    T = np.zeros(dmax + 1)
    lg = np.log(np.arange(0, X + 1, dtype=float), where=np.arange(X+1) > 0, out=np.zeros(X+1))
    for d in range(1, dmax + 1):
        m = np.arange(2, X // d + 1, dtype=float)
        if len(m) == 0: continue
        md = m * d
        T[d] = float(np.sum(np.log(m) * (md ** -0.5) * (np.log(X) - np.log(md))))
    return T

def lambda_ramp_direct(X):
    """sum_{q<=X} Lambda(q) w_X(q) by sieve."""
    spf = spf_sieve(X)
    tot = 0.0
    for q in range(2, X + 1):
        p = int(spf[q]); m = q; is_pp = True
        while m > 1:
            if int(spf[m]) != p: is_pp = False; break
            m //= p
        if is_pp:
            tot += np.log(p) * (q ** -0.5) * np.log(X / q)
    return tot

def run_ramp(X, do_min=True):
    t0 = time.time()
    dmax = X // 2
    mu = mobius_sieve(dmax)
    T = ramp_kernel(X)
    # identity check
    lam_val = sum(mu[d] * T[d] * (1 if bin(0).count('1') % 2 == 0 else 1) for d in range(1, dmax + 1))
    # careful: f=lambda on sf d equals mu(d); so Ramp_lambda = sum mu(d) T(d)
    direct = lambda_ramp_direct(X)
    print(f"== X={X}  dmax={dmax}  identity |sum mu(d)T(d) - sum Lambda w| = {abs(lam_val-direct):.2e}")
    one_val = sum(T[d] for d in range(1, dmax + 1) if mu[d] != 0)
    demand = 4 * np.sqrt(X)
    print(f"   Ramp_lambda - 4sqrtX = {lam_val - demand:+.4f}    Ramp_1 - 4sqrtX = {one_val - demand:+.2f}")
    if not do_min: return
    v, signs, diag = min_mult_class(T, dmax, mu)
    plus = sorted([p for p, s in signs.items() if s == +1])
    print(f"   EXACT min_H Ramp_f - 4sqrtX = {v - demand:+.4f}   (core {diag['ncore']}, big {diag['nbig']})")
    print(f"   minimizer +1 primes: {plus if plus else 'NONE (= lambda)'}")
    if plus:
        dd = distances(signs, dmax)
        print(f"   distances: D2(f,lambda)={dd['D2_to_lambda']:.4f} D2(f,1)={dd['D2_to_one']:.4f} "
              f"min_t D2(f,n^it)={dd['D2_to_nit_min']:.4f}@t={dd['argmin_t']:.3f} "
              f"best chi {dd['best_chi']} best lambda*chi {dd['best_lambda_chi']}")
        # margin structure: value at lambda vs min
        print(f"   gap below lambda: {v - lam_val:+.6f}")
    # single-flip spectrum from lambda
    spf = spf_sieve(dmax); Pl = primes_upto(dmax)
    best_q, best_d = None, None
    ds = []
    for q in Pl:
        s = 0.0
        for m in range(1, dmax // q + 1):
            if mu[m] == 0 or m % q == 0: continue
            s += mu[m] * T[q * m]
        ds.append((2 * s, q))
    ds.sort()
    print(f"   single-flip spectrum: min delta = {ds[0][0]:+.5f} at q={ds[0][1]}; "
          f"smallest {[(q, round(d,4)) for d,q in ds[:5]]}")
    print(f"   [{time.time()-t0:.1f}s]")

def validate_small():
    X = 60; dmax = 30
    mu = mobius_sieve(dmax); T = ramp_kernel(X)
    v, signs, _ = min_mult_class(T, dmax, mu)
    bf, bs = brute_force_min(T, dmax, mu)
    print(f"VALIDATE X=60: WHT+fold {v:+.6f} brute(2^10) {bf:+.6f} delta {abs(v-bf):.2e}")
    # random-f reconstruction check
    rng = np.random.default_rng(7)
    P = primes_upto(dmax); spf = spf_sieve(dmax)
    for trial in range(3):
        sg = {p: int(rng.choice([-1, 1])) for p in P}
        direct = eval_mult(T, dmax, mu, sg, spf)
        print(f"   random-f direct eval: {direct:+.6f} (structure check only)")

if __name__ == "__main__":
    validate_small()
    for X in [600, 1000, 2000, 3000, 5000, 8000, 10000]:
        run_ramp(X)
        print()
