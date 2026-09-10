# Direct evaluation of the repository's canonical fixed detectors and comparison with
# their zero-side (Mellin residue) expansions.  All formulas taken from the reviewed
# lemmas L-99270/L-99272 (h), L-96000 (rows), L-99261 (5:3 scalar W), and the
# minimal-wavelet PROOF.md (G_mu).
import numpy as np, mpmath as mp, sys, time
mp.mp.dps = 20
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
t0 = time.time()
# ---- Möbius sieve
mu = np.ones(NMAX+1, dtype=np.int8); mu[0] = 0
is_comp = np.zeros(NMAX+1, dtype=bool)
for p in range(2, int(NMAX**0.5)+1):
    if not is_comp[p]:
        is_comp[p*p::p] = True
for p in range(2, NMAX+1):
    if not is_comp[p]:
        mu[p::p] *= -1
        if p*p <= NMAX: mu[p*p::p*p] = 0
print("sieve done %.1fs" % (time.time()-t0), flush=True)
n = np.arange(NMAX+1, dtype=np.float64); n[0] = 1.0
sq = np.sqrt(n); ln = np.log(n)
muf = mu.astype(np.float64)
A1 = np.cumsum(muf / n)            # sum mu(k)/k
A2 = np.cumsum(muf / sq)           # sum mu(k)/sqrt k
A3 = np.cumsum(muf * ln / sq)      # sum mu(k) log k / sqrt k
S12 = np.cumsum(1.0 / sq); S12[0] = 0   # sum m^{-1/2}
SLG = np.cumsum(ln / sq); SLG[0] = 0    # sum m^{-1/2} log m
def pref(arr, y):   # arr[floor(y)] with y>=0 float
    idx = np.floor(np.asarray(y)).astype(np.int64); idx = np.clip(idx, 0, NMAX); return arr[idx]
# ---- detectors
def h_mu(x):  return 4*np.sqrt(x)*pref(A1, x) - 3*pref(A2, x)
def h_67(x):  return h_mu(x) - 67**-0.5 * np.where(x >= 67, h_mu(np.maximum(x/67, 1.0)), 0.0)
def W53(X):
    L = np.log(X)
    return (6*L - 6*(L*pref(A2,X) - pref(A3,X))
            + 9*2**-0.5*((L-np.log(2))*pref(A2,X/2) - pref(A3,X/2))
            - 1.5*((L-np.log(4))*pref(A2,X/4) - pref(A3,X/4)))
def row(j, X):
    Aj = (j+1)/(j-1); Bj = (j+1)*(j-2)/(j*(j-1)); Cj = 2/(j*(j-1))
    K = int(X//j); k = np.arange(1, K+1, dtype=np.float64); Y = X/k
    q = np.where(Y >= j, Aj/np.sqrt(j)*np.log(np.maximum(Y/j,1)), 0.0)
    q -= np.where(Y >= j+1, Bj/np.sqrt(j+1)*np.log(np.maximum(Y/(j+1),1)), 0.0)
    Ym = np.minimum(Y, j+1)
    T = (np.log(Y)*pref(S12,Y) - pref(SLG,Y)) - (np.log(Y)*pref(S12,Ym) - pref(SLG,Ym))
    q += Cj*T
    return np.sum(muf[1:K+1]/sq[1:K+1]*q)
def K0(y):
    r2 = np.sqrt(2.0); l = np.log(y); s = np.sqrt(y)
    b1 = 8*s - 8 - 3*l
    b2 = -8*r2*s + 8*(1+r2) + 3*(1+r2)*l - 3*(2+r2)*np.log(2)
    b3 = 4*s - 8*r2 + 9*r2*np.log(2) - 3*r2*l
    return np.where((y>=1)&(y<2), b1, np.where((y>=2)&(y<4), b2, np.where((y>=4)&(y<8), b3, 0.0)))
def G_mu(X):
    lo = int(X//8); ks = np.arange(lo, int(X)+1); ks = ks[ks>=1]
    return np.sum(muf[ks]/sq[ks]*K0(X/ks))
print("G_mu(4) =", G_mu(4.0), " (packet: -1.4620 < G_mu(4) < -1.4618)")
# ---- zero data
Z = np.loadtxt('zetaprime_100k.txt', comments='#')
NZ = len(Z); gam = Z[:,1]; zp = Z[:,2] + 1j*Z[:,3]; rho = 0.5 + 1j*gam
print("zeros with zeta' available:", NZ)
r2 = np.sqrt(2.0)
def P2(z): return 2*2.0**(-z) - 1 - 3.0**(-z)
def P3(z): return (5*3.0**(-z) - 2.0**(-z) - 1 - 3*4.0**(-z))/3
res = {}
res['h_mu']  = (rho+1)/((rho-0.5)*(rho-1)*zp)
res['h_67']  = res['h_mu']*(1-67.0**(-rho))
res['row2']  = P2(rho)/((rho-0.5)**2*zp)
res['row3']  = P3(rho)/((rho-0.5)**2*zp)
a = 2.0**(-rho)
res['W53']   = -3*(a-1)*(a-2)/((rho-0.5)**2*zp)
s = rho - 0.5
res['G_mu']  = (rho+1)*(1-r2*2.0**(-s))*(1-2.0**(-s))**2/((rho-0.5)**2*(rho-1)*zp)
res['box67'] = res['h_67']*(1-67.0**(-1j*gam))/(1j*gam)
# ---- main terms (real poles at s=0)
z12 = mp.mpf('0.5'); zeta_half = mp.zeta(z12); zeta_half_d = mp.zeta(z12, derivative=1)
c0_mu = float(-3/zeta_half); c0_67 = c0_mu*(1-67**-0.5)
def g(j):  # coefficient of log X and constant for row j
    Cj = 2/(j*(j-1))
    Pj = lambda z: (2*mp.power(2,-z)-1-mp.power(3,-z)) if j==2 else (5*mp.power(3,-z)-mp.power(2,-z)-1-3*mp.power(4,-z))/3
    gz = lambda z: Cj + Pj(z)/mp.zeta(z)
    return float(gz(z12)), float(mp.diff(gz, z12))
g2, g2d = g(2); g3, g3d = g(3)
a0 = 2**-0.5
Wlog = 6 + float(-3*(a0-1)*(a0-2)/zeta_half)
Wconst = float(mp.diff(lambda z: 6 - 3*(mp.power(2,-z)-1)*(mp.power(2,-z)-2)/mp.zeta(z), z12))
print("main terms: c0(h_mu)=%.6f c0(h_67)=%.6f | row2: %.6f log X + %.6f | row3: %.6f log X + %.6f | W: %.6f log X + %.6f | box67 c0=%.4f | G_mu: none"
      % (c0_mu, c0_67, g2, g2d, g3, g3d, Wlog, Wconst, c0_67*np.log(67)))
# ---- zero masses
print("\nzero mass  2*sum_{gamma<=T} |r_gamma|  (partial sums; divergence => pointwise target false under LI)")
print("%-8s" % "N", *["%12s" % k for k in res])
for N in [10,100,1000,10000,NZ]:
    if N > NZ: continue
    print("%-8d" % N, *["%12.5f" % (2*np.sum(np.abs(res[k][:N]))) for k in res], "  T=%.0f" % gam[N-1])
# ---- direct vs expansion
def expansion(key, X, N):
    return np.sum(2*np.real(res[key][:N]*np.exp(1j*gam[:N]*np.log(X))))
print("\ndirect evaluation vs main term + first N zeros (N=%d)" % min(NZ, 20000))
N = min(NZ, 20000)
Xs = [10**3, 10**4, 10**5, 10**6, 3*10**6, 10**7] if NMAX >= 10**7 else [10**3, 10**4, 10**5, 10**6]
Xs = [x for x in Xs if x <= NMAX]
for X in Xs:
    X = float(X); L = np.log(X)
    d = {'h_mu': h_mu(np.array([X]))[0], 'h_67': h_67(np.array([X]))[0], 'row2': row(2,X), 'row3': row(3,X), 'W53': W53(np.array([X]))[0], 'G_mu': G_mu(X)}
    m = {'h_mu': c0_mu, 'h_67': c0_67, 'row2': g2*L+g2d, 'row3': g3*L+g3d, 'W53': Wlog*L+Wconst, 'G_mu': 0.0}
    print("X=%.0e" % X)
    for k in d:
        e = m[k] + expansion(k, X, N)
        print("   %-5s direct=%12.6f  main=%10.6f  main+zeros=%12.6f  diff=%10.6f" % (k, d[k], m[k], e, d[k]-e))
    print("   check 5*row2+3*row3 - W = %.3e" % (5*d['row2']+3*d['row3']-d['W53']))
# ---- sign census on a log grid
print("\nsign census on log grid up to %d" % NMAX)
grid = np.exp(np.linspace(np.log(2), np.log(NMAX), 4000))
for name, f in [('h_mu', h_mu), ('h_67', h_67), ('W53', W53)]:
    v = f(grid); print("   %-5s min=%.4f at X=%.3e ; #negative=%d/%d ; last negative X=%s" % (name, v.min(), grid[v.argmin()], (v<0).sum(), len(v), ("%.3e" % grid[v<0].max()) if (v<0).any() else "none"))
gv = np.array([G_mu(x) for x in grid[::4]])
print("   G_mu  min=%.4f max=%.4f ; #negative=%d/%d ; last negative X=%.3e" % (gv.min(), gv.max(), (gv<0).sum(), len(gv), grid[::4][gv<0].max()))
print("total %.0fs" % (time.time()-t0))
