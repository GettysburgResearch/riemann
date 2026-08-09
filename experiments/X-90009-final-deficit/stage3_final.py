"""STAGE 3 FINAL: deficit-theorem closure computations.

(A) SIGNED-TELESCOPE ESCAPE, mu point: exact shells T^s_{X_j}(2) on the exact dyadic
    chain X_j = 2^20 / 2^j down to 2^7 (floors exact: powers of two). Verify the exact
    telescope sum_j T^s_{X_j}(2) = A_{2^20} - A_{2^7}, A_X := T^r_X(2) = sum_p log p r_X(p).
    Report signs, sum of positive parts vs signed sum, consecutive-shell correlation.
(B) SIGNED-TELESCOPE ESCAPE, class H: at X0 = 2^17, per-shell kernels c^(j)(k)
    (E_c at scale X_j), fiber sums g_j(d) = sum_a c^(j)(d a^2) (d squarefree);
    exact class moments over uniform H: Var_j = sum g_j^2, Cov(i,j) = <g_i, g_j>,
    Var(total) = sum (sum_j g_j)^2. Verify kernel telescope sum_j c^(j) = C_top - C_bot
    (r-profile E kernels) and sample-check with 30 random f. If RMS(total) ~ c sqrt(X),
    signed inter-shell cancellation cannot rescue any class-uniform argument.
(C) PRETENDER DISTANCES of random f: M_f = min over {chi_q n^{it}: real chi mod q<=12,
    |t|<=60} of D^2(f chibar, n^{it}; X) at X = 2^17, 25 samples; compare lambda's M and
    loglog X. Existence pair: f far from every pretender AND |shell| ~ sqrt X.
(D) DEFICIT ARITHMETIC with the pinned sharp class-H bound (Hall kappa = 0.32867416320,
    optimal for D = [-1,1], GS Decay Ex.1): floors vs demand at X = 1e6..1e40.
"""
import numpy as np, math, time, sys

t0 = time.time()
KAPPA = 0.32867416320  # Hall's optimal constant for D=[-1,1], GS Decay Example 1

def sieve(X):
    pr = np.ones(X+1, bool); pr[:2] = False
    for i in range(2, int(X**.5)+1):
        if pr[i]: pr[i*i::i] = False
    return np.nonzero(pr)[0]

def spf_sieve(X):
    spf = np.zeros(X+1, np.int64)
    for i in range(2, X+1):
        if spf[i] == 0: spf[i::i][spf[i::i] == 0] = i
    return spf

def mobius(X, spf):
    mu = np.ones(X+1, np.int64)
    for n in range(2, X+1):
        p = spf[n]; m = n//p
        mu[n] = 0 if m % p == 0 else -mu[m]
    return mu

def profile_tables(Nmax):
    k = np.arange(Nmax+1, dtype=float); k[0] = 1
    t1 = k**-0.5; t1[0] = 0.0
    t2 = (k**-0.5)*np.log(k); t2[0] = 0.0
    return np.cumsum(t1), np.cumsum(t2)

def E_at(n, Z, S, A):
    n = np.asarray(n, np.int64); N = Z//n; th = n/Z
    return th**-0.5*(A[N]+(S[N]+1)*np.log(th)+4*S[N])-4*N

def bX(m, X):
    m = np.asarray(m, float)
    v = 2*np.sqrt(m)*(np.log(X/m)-2*(1-np.sqrt(m/X)))
    return np.where((m >= 2) & (m <= X), v, 0.0)

def v_q(q, X):
    k = np.arange(1, X//q+1, dtype=np.int64)
    return float(np.sum(bX(k*q, X)-bX(k*q+1, X)))

def r_X(q, X):
    return v_q(q, X) - q**-0.5*math.log(X/q)

def exact_Ts2(X, primes):
    Y = X//2; tot = 0.0
    for p in primes[primes <= X]:
        r = r_X(int(p), X)
        if p <= Y: r -= r_X(int(p), Y)
        tot += math.log(p)*r
    return tot

def exact_Tr2(X, primes):
    return sum(math.log(int(p))*r_X(int(p), X) for p in primes[primes <= X])

# ---------------- (A) exact mu shells on the exact dyadic chain ----------------
def partA():
    TOP, BOT = 20, 7
    X0 = 1 << TOP
    primes = sieve(X0)
    shells = []
    for j in range(TOP-BOT):
        Xj = X0 >> j
        s = exact_Ts2(Xj, primes)
        shells.append((Xj, s))
        print(f"  X_j=2^{TOP-j}={Xj:>8d}  T^s(2) = {s:+9.4f}   [t={time.time()-t0:.0f}s]", flush=True)
    Atop = exact_Tr2(X0, primes)
    Abot = exact_Tr2(1 << BOT, primes)
    ss = np.array([s for _, s in shells])
    print(f"(A) signed sum = {ss.sum():+.6f}   A(2^{TOP}) - A(2^{BOT}) = {Atop-Abot:+.6f}   gap = {ss.sum()-(Atop-Abot):+.2e}")
    print(f"(A) A(2^{TOP}) = {Atop:+.4f}  A(2^{BOT}) = {Abot:+.4f}")
    print(f"(A) sum of positive parts = {np.maximum(ss,0).sum():+.4f}   sum|s_j| = {np.abs(ss).sum():.4f}")
    print(f"(A) signs: {''.join('+' if v>0 else '-' for v in ss)}   #neg = {(ss<0).sum()}/{len(ss)}")
    if len(ss) > 2:
        c = np.corrcoef(ss[:-1], ss[1:])[0, 1]
        print(f"(A) consecutive-shell correlation (mu, across j): {c:+.3f}")
    return shells

# ---------------- (B) class-H moments of shells and of the signed total ----------------
def kernel_c(Xj, S, A, lg, differenced=True):
    """c^(j)(k) = Xj^{-1/2} sum_m log m * E_c^{(Xj)}(km/Xj); if differenced=False use E."""
    Y = Xj//2
    n_all = np.arange(1, Xj+1)
    E_X = E_at(n_all, Xj, S, A)
    if differenced:
        nY = np.arange(1, Y+1)
        E_X[:Y] -= (Xj/Y)**0.5 * E_at(nY, Y, S, A)
    Ec_all = np.concatenate(([0.0], E_X))
    ck = np.zeros(Xj+1)
    for k in range(1, Xj+1):
        M = Xj//k
        if M < 1: break
        ck[k] = np.dot(lg[1:M+1], Ec_all[k*np.arange(1, M+1)])
    return ck * Xj**-0.5

def fiber_sums(ck, mu, X):
    """g(d) = sum_a ck[d a^2], d squarefree <= X (f(d a^2)=f(d) for f in H)."""
    g = np.zeros(X+1)
    for d in range(1, X+1):
        if mu[d] == 0: continue
        s = 0.0; a = 1
        while d*a*a <= X:
            s += ck[d*a*a]; a += 1
        g[d] = s
    return g

def partB():
    TOP, BOT = 17, 7
    X0 = 1 << TOP
    S, A = profile_tables(X0+2)
    lg = np.log(np.arange(0, X0+1, dtype=float)); lg[0] = 0
    spf = spf_sieve(X0); mu = mobius(X0, spf); primes = sieve(X0)
    J = TOP-BOT
    G = np.zeros((J, X0+1))
    Ctot = np.zeros(X0+1)
    shells_mu = []
    for j in range(J):
        Xj = X0 >> j
        ck = kernel_c(Xj, S, A, lg, differenced=True)
        ckf = np.zeros(X0+1); ckf[:Xj+1] = ck
        Ctot += ckf
        G[j] = fiber_sums(ckf, mu, X0)
        shells_mu.append(float(np.dot(mu[:Xj+1], ck)))
        print(f"  [B] scale 2^{TOP-j}: kernel+fibers done  (t={time.time()-t0:.0f}s)", flush=True)
    # kernel telescope check: Ctot = C_top - C_bot (r-profile E kernels)
    Ct = kernel_c(X0, S, A, lg, differenced=False)
    Xb = 1 << BOT
    Sb, Ab = profile_tables(Xb+2)
    Cb = kernel_c(Xb, Sb, Ab, lg, differenced=False)
    Cchk = Ct.copy(); Cchk[:Xb+1] -= Cb
    gap = float(np.max(np.abs(Cchk - Ctot)))
    print(f"(B) kernel telescope: max|sum_j c^(j) - (C_top - C_bot)| = {gap:.2e}")
    # exact class moments: E shell_j = g_j(1) (d=1 deterministic, f(1)=+1);
    # Cov(i,j) = sum_{d>=2 sf} g_i(d)g_j(d) (E f(d)f(d') = delta_{dd'}, d,d' distinct sf)
    means = G[:, 1].copy()
    Gf = G.copy(); Gf[:, 1] = 0.0
    Cov = Gf @ Gf.T
    gtot = Gf.sum(axis=0)
    mean_tot = float(means.sum())
    var_tot = float(np.dot(gtot, gtot))
    m2_tot = mean_tot**2 + var_tot
    sd = np.sqrt(np.diag(Cov))
    corr = Cov / np.outer(sd, sd)
    print(f"(B) per-shell class MEAN E[shell_j] = " + " ".join(f"{means[j]:+.2f}" for j in range(J)))
    print(f"(B) per-shell class SD/sqrt(X_j):    " +
          " ".join(f"{sd[j]/math.sqrt(X0>>j):.3f}" for j in range(J)))
    print(f"(B) consecutive shell corr over H (fluctuation part): " +
          " ".join(f"{corr[j,j+1]:+.3f}" for j in range(J-1)))
    print(f"(B) signed total over H: mean = {mean_tot:+.2f}, SD = {var_tot**0.5:.2f} "
          f"= {var_tot**0.5/math.sqrt(X0):.4f} sqrt(X0), sqrt(E total^2) = {m2_tot**0.5:.2f}")
    print(f"(B) sum_j SD(shell_j) = {sd.sum():.2f}   SD(top shell) = {sd[0]:.2f} "
          f"= {sd[0]/math.sqrt(X0):.4f} sqrt(X0)")
    print(f"(B) full-anticorrelation floor (|SD_top - sum_others|) = {abs(sd[0]-sd[1:].sum()):.2f}")
    # mu point at these scales
    print(f"(B) mu shells at 2^17..2^8: " + " ".join(f"{v:+.3f}" for v in shells_mu))
    # sample check
    rng = np.random.default_rng(90009)
    f = np.ones(X0+1, np.int64)
    pr = primes[primes <= X0]
    tots = []; EPS = []
    idx_of_p = np.zeros(X0+1, np.int64); idx_of_p[pr] = np.arange(len(pr))
    for s_i in range(30):
        ev = rng.integers(0, 2, size=len(pr))*2-1
        EPS.append(ev)
        eps = {int(p): int(ev[i]) for i, p in enumerate(pr)}
        for n in range(2, X0+1):
            f[n] = eps[int(spf[n])]*f[n//spf[n]]
        tots.append(float(np.dot(f, Ctot)))
    tots = np.array(tots)
    print(f"(B) 30 random f: sample mean = {np.mean(tots):+.2f} (exact {mean_tot:+.2f}), "
          f"sample SD = {np.std(tots, ddof=1):.2f} (exact {var_tot**0.5:.2f}); "
          f"mean|total| = {np.mean(np.abs(tots)):.2f}; max|total| = {np.max(np.abs(tots)):.2f}")
    return G, Ctot, primes, spf, mu, X0, np.array(tots), np.stack(EPS, axis=1)

# ---------------- (C) pretender distances of random f ----------------
def partC(Ctot, primes, spf, X0, nsamp=25, wit_eps=None, wit_tot=None):
    pr = primes[primes <= X0].astype(np.int64)
    logp = np.log(pr.astype(float)); invp = 1.0/pr
    LL = math.log(math.log(X0))
    tgrid = np.arange(0.0, 60.0+1e-9, 0.05)   # D^2 even in t for real f*chi
    # real characters: Kronecker symbols mod q for q in {1,3,4,5,7,8,11,12}
    def kron(q, parr):
        if q == 1: return np.ones_like(parr, float)
        out = np.zeros_like(parr, float)
        for i, p in enumerate(parr):
            p = int(p)
            if math.gcd(p, q) > 1: out[i] = 0.0
            else:
                r = pow(p % q, 1, q); v = 0
                # Jacobi symbol (p|q) for odd q; handle q=4,8,12 via standard kronecker
                v = jacobi_or_kron(p, q)
                out[i] = v
        return out
    def jacobi_or_kron(a, n):
        # Kronecker symbol (a/n), n>0
        t = 1; a = a % (2*n) if n % 2 == 0 else a % n
        n0 = n
        # factor out 2s from n
        while n0 % 2 == 0:
            n0 //= 2
            t *= (1 if a % 8 in (1, 7) else -1) if a % 2 else 0
            if t == 0: return 0
        # Jacobi (a/n0)
        a %= n0; s = 1
        while a:
            while a % 2 == 0:
                a //= 2
                if n0 % 8 in (3, 5): s = -s
            a, n0 = n0, a
            if a % 4 == 3 and n0 % 4 == 3: s = -s
            a %= n0
        return t*s if n0 == 1 else 0
    chars = {q: kron(q, pr) for q in [1, 3, 4, 5, 7, 8, 11, 12]}
    # cos matrix chunks
    rng = np.random.default_rng(424242)
    fs = []
    f = np.ones(X0+1, np.int64)
    for s_i in range(nsamp):
        eps = rng.integers(0, 2, size=len(pr))*2-1
        fs.append(eps.astype(float))
    nwit = 0
    if wit_eps is not None:
        nwit = wit_eps.shape[1]
        fs = [wit_eps[:, i].astype(float) for i in range(nwit)] + fs
    fs.append(-np.ones(len(pr)))          # lambda (= mu on primes)
    Fp = np.stack(fs, axis=1)             # (npr, nwit+nsamp+1)
    sum_invp_chi = {q: float(np.sum(invp[chars[q] != 0])) for q in chars}
    M = np.full(Fp.shape[1], np.inf)
    argq = [None]*Fp.shape[1]; argt = [0.0]*Fp.shape[1]
    for q, chi in chars.items():
        W = (Fp * (chi*invp)[:, None])    # w_p = f(p)chi(p)/p
        best = np.full(Fp.shape[1], np.inf)
        bt = np.zeros(Fp.shape[1])
        for i0 in range(0, len(tgrid), 240):
            tc = tgrid[i0:i0+240]
            cosM = np.cos(np.outer(tc, logp))         # (nt, npr)
            B = cosM @ W                               # (nt, nsamp+1)
            D2 = sum_invp_chi[q] - B
            k = np.argmin(D2, axis=0)
            v = D2[k, np.arange(D2.shape[1])]
            upd = v < best
            bt[upd] = tc[k[upd]]; best = np.minimum(best, v)
        upd = best < M
        for i in np.where(upd)[0]: argq[i] = q; argt[i] = bt[i]
        M = np.minimum(M, best)
    # shells of the same samples (top shell at X0)
    print(f"(C) X0=2^17, loglog X0 = {LL:.3f}; pretender family: real chi mod q<=12, |t|<=60")
    print(f"(C) lambda: M = {M[-1]:.3f} at (q={argq[-1]}, t={argt[-1]:.2f})")
    Ms = M[nwit:-1]
    print(f"(C) {nsamp} random f: min M = {Ms.min():.3f}, median = {np.median(Ms):.3f}, max = {Ms.max():.3f}")
    if nwit:
        Mw = M[:nwit]
        k = int(np.argmax(np.abs(wit_tot)))
        print(f"(C) WITNESS (seed 90009, sample #{k}): signed telescope total = {wit_tot[k]:+.2f} "
              f"= {wit_tot[k]/math.sqrt(X0):+.3f} sqrt(X0);  M_f = {Mw[k]:.3f} "
              f"(vs lambda M = {M[-1]:.3f});  min over 30 B-samples M = {Mw.min():.3f}")
        big = np.abs(wit_tot) >= 2*math.sqrt(X0)
        print(f"(C) B-samples with |total| >= 2 sqrt(X0): {int(big.sum())}/30, all with M >= {Mw[big].min():.3f}")
    print(f"(C) => every sampled f has M >= {Ms.min():.3f} (vs cap 2loglogX+O(1) ~ {2*LL:.2f}): "
          f"far from EVERY pretender, yet (B) shells are ~sqrt(X)-scale.")

# ---------------- (D) deficit arithmetic ----------------
def partD():
    print("(D) floors vs demand   [shell scale: divide by sqrt(X); entries are eta = supply/sqrt X]")
    print(f"    Hall-sharp class-H floor: (log X)^(-2kappa), 2kappa = {2*KAPPA:.5f} (optimal, GS Decay Ex.1)")
    hdr = f"{'X':>7} {'LL':>5} {'eta_Hall=(logX)^-.657':>22} {'eta_GHS2nd=LL/L':>16} {'eta_cplx@Mcap':>14} {'demand@eps=.1':>14} {'deficit=HallvsX^.1':>18}"
    print("    "+hdr)
    for lx in [6, 12, 20, 40]:
        X = 10.0**lx; L = lx*math.log(10); LL = math.log(L)
        hall = L**(-2*KAPPA)
        ghs2 = LL/L
        cplx = (1+2*LL)*math.exp(-2*LL)   # (1+M)e^-M at the structural cap
        dem = X**0.1/X**0.5               # relative demand at eps=0.1
        print(f"    1e{lx:<4d} {LL:5.2f} {hall:22.3e} {ghs2:16.3e} {cplx:14.3e} {dem:14.3e} {hall/dem:18.3e}")
    print("    (deficit column = X^{0.4-o(1)}: a full power at every scale; at eps->0 it is X^{1/2-o(1)})")

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('all', 'A'):
        print("=== (A) exact mu shells, chain 2^20 -> 2^7 ===")
        partA()
    if which in ('all', 'B', 'C'):
        print("=== (B) class-H shell moments, chain 2^17 -> 2^8 ===")
        G, Ctot, primes, spf, mu, X0, tots, EPS = partB()
        print("=== (C) pretender distances of random f ===")
        partC(Ctot, primes, spf, X0, wit_eps=EPS, wit_tot=tots)
    print("=== (D) deficit arithmetic ===")
    partD()
    print(f"[total t={time.time()-t0:.0f}s]")
