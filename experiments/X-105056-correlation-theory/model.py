uHome = "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/progA2/laneM"
import numpy as np, math, json
from mpmath import mp, hyp2f1, primezeta, taylor, log as mlog, gamma as mgamma, mpf
mp.dps = 30

# g(p^k) = (-1/2)_k / k!  (coefficients of (1-z)^{1/2}); eta(p^k) = C(2k,k)/4^k
K = 60
gk = [mpf(1)]
for k in range(1, K): gk.append(gk[-1]*(k - mpf(3)/2)/k)
etak = [mpf(1)]
for k in range(1, K): etak.append(etak[-1]*(2*k-1)/mpf(2*k))

# --- Check 1: hypergeometric identity f_p(x;alpha) = g_alpha * 2F1(alpha-1/2,-1/2;alpha+1;x)
def f_direct(x, alpha):
    return sum(gk[j+alpha]*gk[j]*mpf(x)**j for j in range(0, K-alpha))
err = 0.0
for alpha in range(0, 6):
    for x in [0.5, 0.2, 1.0/7]:
        d = f_direct(x, alpha)
        h = gk[alpha]*hyp2f1(alpha-0.5, -0.5, alpha+1, x)
        err = max(err, abs(float(d-h)))
print("hypergeom identity max err:", err)

# --- local diagonal factor and ratio r_p(alpha; s)
from functools import lru_cache
@lru_cache(maxsize=None)
def diag_factor(p, s):  # 2F1(-1/2,-1/2;1;p^-s)
    return hyp2f1(-0.5, -0.5, 1, mpf(p)**(-s))
@lru_cache(maxsize=None)
def r_local(p, alpha, s):  # f_p(alpha)/f_p(0)
    x = mpf(p)**(-s)
    return gk[alpha]*hyp2f1(alpha-0.5, -0.5, alpha+1, x)/diag_factor(p, s)

def factorize(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d,0)+1; n//=d
        d += 1
    if n > 1: f[n] = f.get(n,0)+1
    return f

def rho(a, b, s=1):  # (a,b)=1 assumed; finite Euler product
    out = mpf(1)
    for n in (a, b):
        for p, al in factorize(n).items(): out *= r_local(p, al, s)
    return out

# --- G(s) at s=1 via log-series + prime zeta:  G = prod_p (1-p^-s)^{1/4} 2F1(-.5,-.5;1;p^-s)
# log factor h(x) = (1/4)log(1-x) + log(2F1(...;x)) = sum_{m>=2} c_m x^m  (c_1 = 0 exactly)
def hfun(x): return mpf(1)/4*mlog(1-x) + mlog(hyp2f1(-0.5,-0.5,1,x))
cs = taylor(hfun, 0, 25)
print("c_1 (must be 0):", float(cs[1]))
logG1 = sum(cs[m]*primezeta(m) for m in range(2, 26))
G1 = float(mp.e**logG1)
C_SD = G1/float(mgamma(mpf(5)/4))
print("G(1) =", G1, " C_SD = G(1)/Gamma(5/4) =", C_SD)

# --- sieve g(q) up to Q
Q = 2_000_000
spf = np.zeros(Q+1, dtype=np.int32)
for i in range(2, int(Q**0.5)+1):
    if spf[i] == 0: spf[i*i::i][spf[i*i::i] == 0] = i
spf[spf == 0] = 0  # primes have spf 0 marker; fix below
gkf = [float(v) for v in gk]
g = np.zeros(Q+1); g[1] = 1.0
for n in range(2, Q+1):
    p = spf[n] if spf[n] else n
    m, a = n, 0
    while m % p == 0: m //= p; a += 1
    g[n] = g[m]*gkf[a]
print("g sieve done; g[2],g[4],g[6],g[12] =", g[2], g[4], g[6], g[12])

inv = np.zeros(Q+1); inv[1:] = 1.0/np.arange(1, Q+1)
# A_{1,1}(Q) = sum g(q)^2/q vs C_SD (log Q)^{1/4}
cum = np.cumsum(g*g*inv)
for Qc in [10**4, 10**5, 10**6, Q]:
    pred = C_SD*math.log(Qc)**0.25
    print(f"A11({Qc:.0e}) = {cum[Qc]:.5f}  SD pred = {pred:.5f}  ratio = {cum[Qc]/pred:.4f}")

# --- factorization check at s>1: F_ab(s)/F_11(s) vs rho_ab(s), direct sums
def F_direct(a, b, s, Qm):
    q = np.arange(1, Qm+1)
    return float(np.sum(g[q*a]*g[q*b]*np.power(q, -float(s))))
pairs = [(2,1),(3,1),(3,2),(4,1),(4,3),(5,2),(8,3),(9,2),(6,1),(12,7)]
print("\nfactorization check (s=1.5, direct Q-truncated):")
for s in [1.5, 1.25]:
    Qm = Q//13
    F11 = F_direct(1, 1, s, Qm)
    print(f"s={s}:")
    for (a, b) in pairs:
        r_dir = F_direct(a, b, s, Qm)/F11
        r_th = float(rho(a, b, s))
        print(f"  ({a},{b}): direct {r_dir:+.6f}  rho {r_th:+.6f}  relerr {abs(r_dir-r_th)/abs(r_th):.2e}")

# --- correlation ratio law at s=1 (slow log corrections expected)
print("\nA_ab(Q)/A_11(Q) vs rho_ab(1)  [Q = 2e6/max(a,b)]:")
res = {}
for (a, b) in pairs:
    Qm = Q//max(a, b)
    q = np.arange(1, Qm+1)
    Aab = float(np.sum(g[q*a]*g[q*b]/q))
    r = Aab/cum[Qm]
    rt = float(rho(a, b, 1))
    res[f"{a},{b}"] = (r, rt)
    print(f"  ({a},{b}): empir {r:+.5f}  rho(1) {rt:+.5f}")

# exact kernel second moment check: (8-6sqrt2) log 2
h2 = math.log(2)
def R(v):
    v = abs(v)
    if v <= h2: return 3*h2-(3+math.sqrt(2))*v
    if v <= 2*h2: return -math.sqrt(2)*(2*h2-v)
    return 0.0
import scipy.integrate as si
I2 = si.quad(lambda v: R(v)*math.exp(v/2)*v, -2*h2, 2*h2, limit=200)[0]
print("\nint R v e^{v/2} dv =", I2, " exact (8-6sqrt2)log2 =", (8-6*math.sqrt(2))*math.log(2))
np.save(uHome+"/g_array.npy", g)
json.dump({"G1": G1, "C_SD": C_SD}, open(uHome+"/model_consts.json", "w"))
