"""Task A: (i) verify Shimura relation a(|D| n^2)/a(|D|) = (mu*chi_D * sigma)(n) [H] and
(mu*chi_D * sigma)(n_odd) [r_3]; compare S_d(X;s) with zeta(s)zeta(s-1)/L(s,chi_D);
(ii) Moebius part M_d(X;s)=sum mu(n)chi_D(n)n^{-s}: growth exponents vs GRH prediction 1/2-s,
and periodogram of X^{-1/2} sum mu chi vs log X compared with low zeros of L(s,chi_D)."""
import numpy as np, mpmath as mp, time, os, sys
OUT = os.path.dirname(os.path.abspath(__file__))
r3 = np.load(os.path.join(OUT,"r3.npy")); H = np.load(os.path.join(OUT,"H.npy"))
R3MAX = len(r3)-1; HMAX = len(H)-1
XMAX = 10**7
mp.mp.dps = 20

def kron2(D):
    if D % 2 == 0: return 0
    return 1 if D % 8 in (1,7) else -1
def jacobi(a, n):  # n odd positive
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3,5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
def kronecker(D, n):
    if n == 0: return 1 if abs(D)==1 else 0
    r = 1
    while n % 2 == 0:
        n //= 2; r *= kron2(D)
    return r * jacobi(D, n) if n>0 else 0
def chi_table(D):
    q = abs(D); return np.array([kronecker(D, r) for r in range(q)], dtype=np.int8)
def chi_vals(D, n):  # n: array of positive ints
    return chi_table(D)[n % abs(D)]

# --- Moebius sieve ---
t0=time.time()
def mobius(N):
    mu = np.ones(N+1, dtype=np.int8); isp = np.ones(N+1, dtype=bool); isp[:2]=False
    for p in range(2, int(N**0.5)+1):
        if isp[p]: isp[p*p::p] = False
    primes = np.nonzero(isp)[0]
    for p in primes:
        mu[p::p] *= -1
        if p*p <= N: mu[p*p::p*p] = 0
    mu[0]=0; return mu
mu = mobius(XMAX); print("mu sieve done", time.time()-t0, flush=True)

def sigma(N):
    s = np.zeros(N+1, dtype=np.int64)
    for d in range(1, N+1): s[d::d] += d
    return s
def shimura_coeffs(D, N):
    """c(n) = sum_{m|n} mu(m) chi_D(m) sigma(n/m), n<=N  (coefficients of zeta(s)zeta(s-1)/L(s,chi_D))"""
    sg = sigma(N); ch = chi_table(D); c = np.zeros(N+1, dtype=np.int64)
    for m in range(1, N+1):
        if mu[m]==0 or ch[m%abs(D)]==0: continue
        w = int(mu[m])*int(ch[m%abs(D)])
        k = np.arange(1, N//m+1); c[m*k] += w*sg[k]
    return c
def oddpart(n):
    n = n.copy()
    while True:
        e = (n%2==0)
        if not e.any(): return n
        n[e] //= 2

def L_chi(s, D):
    q = abs(D); ch = chi_table(D)
    if s == 1:   # L(1,chi) = -(1/q) sum chi(a) psi(a/q)
        return -mp.fsum(int(ch[a])*mp.digamma(mp.mpf(a)/q) for a in range(1,q) if ch[a]!=0)/q
    return mp.mpf(q)**(-s) * mp.fsum(int(ch[a])*mp.zeta(s, mp.mpf(a)/q) for a in range(1,q) if ch[a]!=0)

ds = [1,2,3,5,7,11,15,23,31,39,47]
print("\n=== (A.i) Shimura relation check ===")
print("d   D    form   n_max   max|a(|D|n^2)/a(|D|) - c(n)|   [c = mu*chi_D conv sigma; r3 uses n_odd]")
rows=[]
for d in ds:
    D = -d if d%4==3 else -4*d
    q = abs(D)
    # H: row at |D| (requires -N discriminant); r3: row at d (odd part rule)
    nH = int(np.sqrt(HMAX//q)); nR = int(np.sqrt(R3MAX//d))
    c = shimura_coeffs(D, max(nH,nR))
    n = np.arange(1, nH+1)
    errH = np.max(np.abs(H[q*n*n]/H[q] - c[n]))
    n = np.arange(1, nR+1)
    if r3[d]>0:
        errR = np.max(np.abs(r3[d*n*n]/r3[d] - c[oddpart(n)]))
        # also check that the "d n^2 with full Shimura coefficient" would be wrong:
        errR_naive = np.max(np.abs(r3[d*n*n]/r3[d] - c[n]))
    else:
        errR = float(np.max(np.abs(r3[d*n*n]))); errR_naive=float('nan')
    print(f"{d:3d} {D:4d}  H      {nH:5d}   {errH:.3e}")
    print(f"{d:3d} {D:4d}  r3     {nR:5d}   {errR:.3e}   (naive c(n) instead of c(n_odd): {errR_naive:.3e}; r3(d)={r3[d]})")
    rows.append((d,D,nH,errH,nR,errR,errR_naive))

print("\n=== (A.i') S_d(X;s) vs analytic zeta(s)zeta(s-1)/L(s,chi_D) (H row), and 2-adjusted for r3 ===")
print("d    D    s    X     S_d(X;s) [H data]    S_d(X;s) [r3 data]   analytic(H)        analytic(r3)     tail bound ~X^{2-s}/(s-2)")
for d in [3,5,7,11,23]:
    D = -d if d%4==3 else -4*d; q=abs(D)
    nH = int(np.sqrt(HMAX//q)); nR = int(np.sqrt(R3MAX//d))
    for s in [3.0, 4.0]:
        n = np.arange(1,nH+1); SH = np.sum(H[q*n*n]/H[q] * n**(-s))
        n = np.arange(1,nR+1); SR = np.sum(r3[d*n*n]/r3[d] * n**(-s))
        Ls = L_chi(s, D); anH = mp.zeta(s)*mp.zeta(s-1)/Ls
        anR = anH * (1-mp.mpf(2)**(1-s))/(1-kron2(D)*mp.mpf(2)**(-s))
        print(f"{d:3d} {D:4d} {s:.1f} {nH:5d}/{nR:5d} {SH:16.10f} {SR:16.10f}  {float(anH):16.10f} {float(anR):16.10f}   {nH**(2-s)/(s-2):.2e}/{nR**(2-s)/(s-2):.2e}")

# ---------------- (A.ii) Moebius part ----------------
print("\n=== (A.ii) Moebius part M_d(X;s) = sum_{n<=X} mu(n) chi_D(n) n^{-s}, X<=1e7 ===")
nn = np.arange(1, XMAX+1)
grid = np.unique(np.logspace(3, 7, 500).astype(np.int64))
def fit(xs, ys):
    A = np.vstack([np.log(xs), np.ones(len(xs))]).T
    coef, res, _, _ = np.linalg.lstsq(A, np.log(ys), rcond=None)
    pred = A@coef; dof = max(len(xs)-2,1)
    se = np.sqrt(np.sum((np.log(ys)-pred)**2)/dof / np.sum((np.log(xs)-np.log(xs).mean())**2))
    return coef[0], se
def dyadic_rms(X, vals, lo=10, hi=23):
    xs=[]; ys=[]
    for j in range(lo, hi+1):
        a, b = 2**j, min(2**(j+1), len(vals))
        if a>=b: break
        xs.append(np.sqrt(a*b)); ys.append(np.sqrt(np.mean(np.abs(vals[a:b])**2)))
    return np.array(xs), np.array(ys)
svals = [0.0, 0.25, 0.5, 0.6, 0.75, 1.0]
print("d    D    s     LS slope log|M| (+-se)   dyadic-RMS slope (+-se)   runmax slope   [GRH prediction: 1/2-s]   (for s>1/2: slopes refer to |M - 1/L(s,chi_D)|)")
tableA=[]
for d in ds:
    if d in (1,2): continue
    D = -d if d%4==3 else -4*d
    chi = chi_vals(D, nn).astype(np.float64)
    muchi = mu[1:].astype(np.float64)*chi
    for s in svals:
        M = np.cumsum(muchi * nn**(-s))
        if s > 0.5:
            target = float(1/L_chi(mp.mpf(s), D)); E = M - target
        else:
            target = None; E = M
        E = np.concatenate([[0.0], E])   # index by X
        absE = np.abs(E)
        ys = absE[grid]; ok = ys>0
        sl, se = fit(grid[ok], ys[ok])
        xs2, ys2 = dyadic_rms(None, E); sl2, se2 = fit(xs2, ys2)
        if s <= 0.5:
            rm = np.maximum.accumulate(absE)[grid]; sl3,se3 = fit(grid, rm)
        else:
            # tail sup: sup_{X'>=X} |E(X')|
            ts = np.maximum.accumulate(absE[::-1])[::-1][grid]; sl3,se3 = fit(grid, ts)
        tgt = f"{target:.6f}" if target is not None else "   -   "
        print(f"{d:3d} {D:4d} {s:5.2f}   {sl:+.3f} +- {se:.3f}          {sl2:+.3f} +- {se2:.3f}         {sl3:+.3f} +- {se3:.3f}     [{0.5-s:+.2f}]   1/L={tgt}")
        tableA.append((d,D,s,sl,se,sl2,se2,sl3,se3))
    # value table at a few X for s=1/2 and s=0
    M0 = np.concatenate([[0],np.cumsum(muchi)]); Mh = np.concatenate([[0],np.cumsum(muchi*nn**(-0.5))])
    print("     X:        " + "  ".join(f"{X:>9d}" for X in [10**3,10**4,10**5,10**6,10**7]))
    print("     M(X;0)/sqrt(X): " + "  ".join(f"{M0[X]/np.sqrt(X):+9.4f}" for X in [10**3,10**4,10**5,10**6,10**7]))
    print("     M(X;1/2):       " + "  ".join(f"{Mh[X]:+9.4f}" for X in [10**3,10**4,10**5,10**6,10**7]))
    sys.stdout.flush()
np.save(os.path.join(OUT,"tableA.npy"), np.array(tableA))

# ---------------- (A.iii) periodogram of X^{-1/2} sum mu chi vs log X, compared with zeros ----------------
print("\n=== (A.iii) Oscillation frequencies of X^{-1/2} M_d(X;0) in u=log X vs ordinates of low zeros of L(s,chi_D) ===")
def low_zeros(D, tmax=14.0, npts=140):
    q=abs(D); a = 0 if kronecker(D,-1 % q if q>1 else 1)==1 else 1
    a = 0 if kronecker(D, q-1)==1 else 1   # chi(-1)
    def Zf(t):
        s = mp.mpc(0.5, t); g = mp.gamma((s+a)/2)
        val = (mp.mpf(q)/mp.pi)**(mp.mpc(0,t)/2) * g/abs(g) * L_chi(s, D)
        return val.real, val.imag
    ts = np.linspace(0.1, tmax, npts); vals=[Zf(t) for t in ts]
    re = np.array([v[0] for v in vals]); im = np.array([v[1] for v in vals])
    assert np.max(np.abs(im)) < 1e-6*max(1,np.max(np.abs(re))), ("not real", np.max(np.abs(im)))
    zs=[]
    for i in range(len(ts)-1):
        if re[i]*re[i+1] < 0:
            zs.append(float(mp.findroot(lambda t: Zf(t)[0], (ts[i], ts[i+1]), solver='bisect', tol=1e-10)))
    return zs
for d in [3,7,11,23,47]:
    D = -d; chi = chi_vals(D, nn).astype(np.float64)
    M0 = np.concatenate([[0],np.cumsum(mu[1:]*chi)])
    u = np.linspace(np.log(1e3), np.log(1e7), 4096); X = np.exp(u).astype(np.int64)
    f = M0[X]/np.sqrt(X); f = f - f.mean()
    # periodogram
    w = np.hanning(len(f)); F = np.fft.rfft(f*w); freqs = 2*np.pi*np.fft.rfftfreq(len(f), d=u[1]-u[0])
    P = np.abs(F)**2; sel = (freqs>1.5)&(freqs<40)
    idx = np.argsort(P[sel])[::-1][:5]; peaks = sorted(freqs[sel][idx])
    t0=time.time(); zs = low_zeros(D)
    print(f"d={d}: zeros of L(1/2+it,chi_{D}) with t<14: {[round(z,3) for z in zs]}  ({time.time()-t0:.1f}s)")
    print(f"      top-5 periodogram frequencies of X^(-1/2)M(X;0) in log X: {[round(p,2) for p in peaks]}  (resolution ~{2*np.pi/(u[-1]-u[0]):.2f})")
print("done")
