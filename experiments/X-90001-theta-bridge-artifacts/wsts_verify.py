import numpy as np, math
from math import log, sqrt, fsum

# ---------- primes ----------
def sieve(n):
    s = np.ones(n+1, dtype=bool); s[:2] = False
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

# ---------- seed and exact finite objects ----------
def bX(m, X):
    if m < 2 or m > X: return 0.0
    return 2*sqrt(m)*(log(X/m) - 2*(1 - sqrt(m/X)))

def v_p(p, X):
    K = X // p
    return fsum(bX(k*p, X) - bX(k*p+1, X) for k in range(1, K+1))

def r_all(X, primes):
    pr = primes[primes <= X]
    return pr, np.array([v_p(int(p), X) - log(X/p)/sqrt(p) for p in pr])

def B_and_tail(X, primes):
    """returns primes<=X, s_X(p), suffix sums T(z)=sum_{p>=z} logp*s, B_X"""
    Y = X // 2
    prX, rX = r_all(X, primes)
    prY, rY = r_all(Y, primes)
    s = rX.copy()
    idx = {int(p): i for i, p in enumerate(prX)}
    for j, p in enumerate(prY):
        s[idx[int(p)]] -= rY[j]
    w = np.log(prX.astype(float)) * s
    suffix = np.cumsum(w[::-1])[::-1]          # T(z) at z = p_j
    B = max(0.0, suffix.max())
    return prX, s, suffix, B

# ---------- continuum profile ----------
SN_cache = [0.0]; AN_cache = [0.0]
def ensure_N(N):
    while len(SN_cache) <= N:
        k = len(SN_cache)
        SN_cache.append(SN_cache[-1] + k**-0.5)
        AN_cache.append(AN_cache[-1] + k**-0.5*math.log(k))

def E_profile(theta):
    """E(theta) = F(theta) - theta^{-1/2} log(1/theta), exact cell formula"""
    N = int(1/theta)
    if abs(theta*(N+1) - 1) < 1e-14: N = N+1 if False else N  # theta=1/(N+1) boundary: cell N+1... use limit continuity
    ensure_N(N)
    SN, AN = SN_cache[N], AN_cache[N]
    return theta**-0.5*(AN + (SN+1)*math.log(theta) + 4*SN) - 4*N

def cell_int_E(a, b, N):
    """exact integral of E over [a,b] within cell N (1/(N+1)<=a<=b<=1/N)"""
    ensure_N(N); SN, AN = SN_cache[N], AN_cache[N]
    # int theta^{-1/2} = 2 sqrt; int theta^{-1/2} log theta = 2 sqrt th (log th - 2)
    def I(t):
        return (AN+4*SN)*2*math.sqrt(t) + (SN+1)*(2*math.sqrt(t)*(math.log(t)-2)) - 4*N*t
    return I(b) - I(a)

def H_of(theta):
    """H(theta) = int_theta^1 E(u) du, exact per-cell"""
    N = int(1/theta)
    tot = 0.0
    # from theta to 1/N in cell N... iterate cells m=N down to 1
    parts = []
    a = theta
    for m in range(N, 0, -1):
        b = 1.0/m
        lo = max(a, 1.0/(m+1)) if m < N else a
        parts.append(cell_int_E(lo, b, m))
        a = b
    return fsum(parts)

def J_of(theta): return H_of(theta)/math.sqrt(theta)

# ---------- checks ----------
primes = sieve(300000)

print("== N1: B_X on sample ==")
for X in [50, 100, 500, 1000, 5000, 20000, 100000]:
    prX, s, suf, B = B_and_tail(X, primes)
    print(f"X={X:7d}  B_X={B:.6e}  max_tail={suf.max():+.4f}  tail_at_z2={suf[0]:+.4f}")

print("\n== N2: kappa = int_0^1 E, H sign, J monotone, H_c<=0 ==")
# kappa via H(theta) as theta->0
for th in [1e-2, 1e-3, 1e-4, 1e-5]:
    print(f"  H({th:g}) = {H_of(th):+.8f}   (kappa - int_0^th E; H(0+)=kappa)")
# J monotonicity spot check and H_c
cs = [1/3, 0.4, 1/2, 499999/1000000]
ths = np.geomspace(1e-4, 0.999, 400)
Hvals = [H_of(t) for t in ths]
print("  max H(theta) over grid:", max(Hvals))
for c in cs:
    worst = -1
    for t in ths:
        if t <= c:
            hc = H_of(t) - math.sqrt(c)*H_of(t/c)
        else:
            hc = H_of(t)
        worst = max(worst, hc)
    print(f"  c={c:.4f}: max H_c(theta) = {worst:+.3e}")
Jv = [H_of(t)/math.sqrt(t) for t in ths]
print("  J nondecreasing on grid:", all(Jv[i] <= Jv[i+1]+1e-12 for i in range(len(Jv)-1)), f" J(min)={Jv[0]:+.5f} J(max)={Jv[-1]:+.5f}")

print("\n== N3: A_X(2) vs Phi(X) = X^{-1/2} int_[2,X] E(t/X) dR(t) ==")
def Phi(X):
    pr = primes[primes <= X]
    S = fsum(math.log(p)*E_profile(p/X) for p in pr)          # int E dtheta
    # int_2^X E(t/X) dt = X * int_{2/X}^1 E(u) du = X*H(2/X)
    return (S - X*H_of(2/X))/math.sqrt(X)
for X in [100, 1000, 10000, 100000]:
    prX, rX = r_all(X, primes)
    A2 = fsum(math.log(p)*r for p, r in zip(prX, rX))
    ph = Phi(X)
    print(f"X={X:7d}  A_X(2)={A2:+.4f}  Phi(X)={ph:+.4f}  diff={A2-ph:+.4f}  log2X={math.log(2*X):.2f}")
