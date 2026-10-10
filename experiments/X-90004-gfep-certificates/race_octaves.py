"""T2b prong 2: octave-race dominance bookkeeping for GFEP.

G[m] = full descending occupancy: G(m) = S(m) + sum_{parents} G(par) Q(par,m), S(m)=m R_X(m).
Descending chain => G restricted to m >= 2n equals the first-entrance far mass W for ANY n.
Sigma_{X,n}(p) = S(p) + sum_{parents m'' of p, m''>=2n} G(m'') Q(m'',p),  n<=p<2n.

Sources are split into dyadic-N buckets (N = X//m):
  bucket 0: N=1; 1: N in {2,3}; 2: N=4; g>=3: N in [2^(g-1), 2^g) ... concretely
  label(N): 0 if N==1, 1 if N<=3, 2 if N==4, else floor(log2(N))+1  (N in {5,6,7}->3, [8,16)->4, ...)
Buckets 0..2 are the proved-positive source region (C_N>0, N<=4); g>=3 negative/unknown.
"""
import numpy as np, sys, math, time
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r, sigma_first_entrance

def labels_for(X):
    m = np.arange(1, X + 1)
    N = X // m
    g = np.zeros(X + 1, dtype=np.int64)
    lg = np.zeros_like(N)
    big = N >= 5
    lg[big] = np.floor(np.log2(N[big])).astype(np.int64) + 1
    lg[N == 4] = 2
    lg[(N == 2) | (N == 3)] = 1
    lg[N == 1] = 0
    g[1:] = lg
    return g

def full_G_split(X, r):
    """G[g, m] occupancy split by source bucket. Block descent (children of [lo,hi] all < lo)."""
    glab = labels_for(X)
    gmax = int(glab.max())
    S = np.zeros(X + 1)
    m = np.arange(2, X + 1)
    S[2:] = m * r[2:X + 1]
    far = np.zeros((gmax + 1, X + 1))
    far[glab[2:], np.arange(2, X + 1)] = S[2:]
    G = np.zeros_like(far)
    hi = X
    while hi >= 2:
        lo = max(2, (2 * hi) // 3 + 1)
        M = np.arange(lo, hi + 1)
        a2 = M // 2; b2 = M - a2; a3 = (M + 2) // 3; b3 = M - a3
        idx = np.concatenate((a2, b2, a3, b3))
        G[:, lo:hi + 1] = far[:, lo:hi + 1]          # finalized
        for g in range(gmax + 1):
            fm = far[g, lo:hi + 1]
            if not np.any(fm):
                continue
            gg = fm / (2.0 * M)
            wts = np.concatenate((a2 * gg, b2 * gg, a3 * gg, b3 * gg))
            buf = np.bincount(idx, weights=wts, minlength=lo)
            far[g, :len(buf)] += buf
        hi = lo - 1
    return G, glab, S

def parents_of(p):
    """[(m'', multiplicity), ...] exact."""
    out = [(2 * p, 2), (2 * p + 1, 1), (2 * p - 1, 1), (3 * p - 2, 1), (3 * p - 1, 1), (3 * p, 1)]
    mlo = -(-3 * p // 2)                       # ceil(3p/2)
    mhi = -(-3 * (p + 1) // 2) - 1
    for mm in range(mlo, mhi + 1):
        out.append((mm, 1))
    return out

def sigma_split(X, G, glab, S, n):
    """Sigma_g(p) array [gmax+1, #p] for p in [n, min(2n,X+1))."""
    up = min(2 * n, X + 1)
    ps = np.arange(n, up)
    out = np.zeros((G.shape[0], len(ps)))
    out[glab[n:up], np.arange(len(ps))] += S[n:up]   # diagonal
    for j, p in enumerate(ps):
        for mpar, mult in parents_of(int(p)):
            if mpar >= 2 * n and mpar <= X:
                out[:, j] += G[:, mpar] * (p * mult / (2.0 * mpar))
    return ps, out

def report(X, ns):
    t0 = time.time()
    mu = mobius_sieve(X); r = critical_r(X, mu)
    G, glab, S = full_G_split(X, r)
    print(f"# X={X}  (G built in {time.time()-t0:.1f}s)  sqrt(X)={math.sqrt(X):.1f}")
    # per-bucket source l1 mass and C_N magnitude proxy
    sx = math.sqrt(X)
    for n in ns:
        ps, sg = sigma_split(X, G, glab, S, n)
        tot = sg.sum(axis=0)
        j = int(np.argmin(tot)); pstar = int(ps[j])
        print(f"\n## n={n}  (n/X={n/X:.3e})  min sqrt(X)*Sigma = {sx*tot[j]:.6f} at p={pstar} (p/n={pstar/n:.3f})"
              f"   [#p={len(ps)}, all>0: {bool((tot>0).all())}, #nonpos={(tot<=0).sum()}]")
        pos = sx * sg[:3, j].sum()
        neg = sx * sg[3:, j].sum()
        print(f"   at p*: positive base (N<=4 buckets) = {pos:+.4f}; total from N>=5 buckets = {neg:+.4f}; margin ratio |neg|/pos = {abs(neg)/pos:.4f}")
        print(f"   {'g':>2} {'N-range':>12} {'srcL1*sqrtX':>12} {'Phi_g(p*)*sqrtX':>16} {'|Phi_g/Phi_g-1|':>16}")
        prev = None
        for g in range(G.shape[0]):
            msk = (glab == g)
            msk[:max(2, 2 * n)] = False   # sources actually feeding far mass (>=2n); diag separate
            l1 = sx * np.abs(S[msk]).sum()
            phi = sx * sg[g, j]
            ratio = abs(phi / prev) if (prev not in (None, 0.0) and abs(prev) > 1e-15) else float('nan')
            nlo = 1 if g == 0 else (2 if g == 1 else (4 if g == 2 else 2 ** (g - 1)))
            nhi = 1 if g == 0 else (3 if g == 1 else (4 if g == 2 else 2 ** g - 1))
            if l1 == 0 and abs(phi) < 1e-14 and g > 3:
                continue
            print(f"   {g:>2} {f'{nlo}-{nhi}':>12} {l1:>12.4f} {phi:>16.6f} {ratio:>16.3f}")
            prev = phi
    return G, glab, S, r

# cross-validation of the G-based Sigma against the independent block-descent implementation
Xv = 10000
mu = mobius_sieve(Xv); rv = critical_r(Xv, mu)
Gv, gl, Sv = full_G_split(Xv, rv)
ok = True
for n in [4990, 3000, 1100, 500, 101, 47]:
    ps1, s1 = sigma_first_entrance(rv, Xv, n)
    ps2, s2 = sigma_split(Xv, Gv, gl, Sv, n)
    err = np.abs(s1 - s2.sum(axis=0)).max()
    ok &= err < 1e-10
    print(f"xval X={Xv} n={n}: max|Sigma_blockdescent - Sigma_G| = {err:.2e}")
print("CROSS-VALIDATION:", "OK" if ok else "FAIL")

for X, ns in [(10**5, [10001, 8334, 317, 133, 47]),
              (10**6, [100001, 83334, 1000, 191, 100])]:
    report(X, ns)
