"""Does the SIGNED shallow field equidistribute like its aggregate (min_p ~ c_- * tau),
or does two-sided GL (c_- on pos, K on neg separately) destroy the floor?
Measure at X=1e5: per-bucket in-flow profiles Phi_g(p), their proportionality, and
min_p / mean_p of the signed shallow sum vs c_-*P - K*Neg prediction.
Also GL constants per octave from uniform seeds (reproduce c_-, K ranges)."""
import numpy as np, math, sys
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r, sigma_first_entrance

X = 100000
mu = mobius_sieve(X); r = critical_r(X, mu)
m_all = np.arange(0, X+1); src = m_all*r[:X+1]
Nof = np.zeros(X+1, dtype=int); Nof[1:] = X // m_all[1:]
lab = np.zeros(X+1, dtype=int)
big = Nof >= 5
lab[big] = np.floor(np.log2(Nof[big])).astype(int) + 1
lab[Nof == 4] = 2; lab[(Nof == 2) | (Nof == 3)] = 1

def descend(seed, n):
    far = seed.astype(float).copy(); far[:2*n] = 0.0
    entrance = np.zeros(2*n); hi = X
    while hi >= 2*n:
        lo = max(2*n, (2*hi)//3 + 1)
        M = np.arange(lo, hi+1); fm = far[lo:hi+1]; g = fm/(2.0*M)
        a2 = M//2; b2 = M-a2; a3 = (M+2)//3; b3 = M-a3
        idx = np.concatenate((a2, b2, a3, b3))
        wts = np.concatenate((a2*g, b2*g, a3*g, b3*g))
        buf = np.bincount(idx, weights=wts, minlength=hi)
        if len(buf) > 2*n: far[2*n:len(buf)] += buf[2*n:]
        entrance[n:] += buf[n:2*n]
        hi = lo - 1
    return entrance[n:]

for n in [317, 47]:
    gmax = int(lab.max())
    prof = []
    for g in range(gmax+1):
        seed = np.zeros(X+2); msk = lab == g
        seed[:X+1][msk] = src[msk]
        e = descend(seed, n)
        p0 = np.zeros(min(2*n, X+1)-n); p0[:] = e[:len(p0)]
        ps = np.arange(n, min(2*n, X+1))
        dmask = lab[ps] == g
        p0[dmask] += src[ps][dmask]
        prof.append(p0)
    prof = np.array(prof)
    # GL constants from uniform seeds per true octave nu = log2(X/m)
    gl = []
    for nu in range(0, int(math.log2(X/n))-1):
        lo_m, hi_m = int(X/2**(nu+1))+1, int(X/2**nu)
        if lo_m < 2*n: lo_m = 2*n
        if hi_m <= lo_m: continue
        seed = np.zeros(X+2); seed[lo_m:hi_m+1] = 1.0
        e = descend(seed, n)
        if e.mean() > 0: gl.append((nu, e.min()/e.mean(), e.max()/e.mean()))
    print(f"\nn={n}: GL per-octave (nu, c-, K): " + " ".join(f"({a},{b:.2f},{c:.2f})" for a, b, c in gl))
    sx = math.sqrt(X)
    # shallow signed field, cutoff bucket g0 (buckets 0..g0 = certified region N < 2^g0)
    for g0 in [4, 6, 8]:
        sh = prof[:g0+1].sum(axis=0)
        P = prof[:3].sum(axis=0)   # positive part (N<=4)
        Ng = prof[3:g0+1].sum(axis=0)  # negative buckets
        agg = sh.sum(); mean = sh.mean()
        print(f"  g0={g0}: shallow signed: sqrtX*(min,mean)=({sx*sh.min():+.3f},{sx*mean:+.3f}) "
          f"min/mean={sh.min()/mean:+.3f} | pos min/mean={P.min()/P.mean():.3f} "
          f"neg(min,max)/mean={Ng.min()/Ng.mean():.2f},{Ng.max()/Ng.mean():.2f} "
          f"| naive floor c-*P-K*|N| ={sx*(0.62*P.mean()-1.56*np.abs(Ng.mean())):+.3f}")
    # profile proportionality: correlation of each bucket profile with the mean shape
    shape = prof[:3].sum(axis=0); shape /= np.linalg.norm(shape)
    cors = []
    for g in range(3, gmax+1):
        v = prof[g]
        if np.linalg.norm(v) > 1e-12:
            cors.append(abs(float(np.dot(v, shape)/np.linalg.norm(v))))
    print(f"  |corr(bucket profile, positive-base shape)| g>=3: " +
          " ".join(f"{c:.3f}" for c in cors))
