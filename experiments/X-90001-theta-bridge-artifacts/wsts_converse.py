import numpy as np, math
from math import log, sqrt

def sieve(n):
    s = np.ones(n+1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def bvals(m, X):
    # b_X(m) for integer array m; 0 outside [2, X]
    m = np.asarray(m, dtype=np.float64)
    out = 2.0*np.sqrt(m)*(np.log(X/m) - 2.0*(1.0 - np.sqrt(m/X)))
    out[(m < 2) | (m > X)] = 0.0
    return out

def v_q(q, X):
    K = X // q
    kq = np.arange(1, K+1, dtype=np.int64) * q
    return float(np.sum(bvals(kq, X) - bvals(kq+1, X)))

def prime_powers(X, primes):
    # (q=p^a, log p) for a>=2
    out = []
    for p in primes:
        if p*p > X: break
        q = p*p
        while q <= X:
            out.append((q, math.log(p)))
            q *= p
    return out

zeta_half   = -1.4603545088095868
zetap_half  = -3.9226461392091517

def analyze(X, primes, verbose=True):
    lp = np.log(primes.astype(np.float64))
    # ramp R(X) and per-prime w
    w = primes**-0.5 * np.log(X/primes.astype(np.float64))
    R = float(np.sum(lp*w))
    # v_p for all p
    v = np.array([v_q(int(p), X) for p in primes])
    V = float(np.sum(lp*v))                      # V_X(2)
    A = V - R                                    # sum log p * r_X(p)
    f = 4*math.sqrt(X) - R
    # bridge pieces
    n = np.arange(2, X+1, dtype=np.int64)
    V1 = float(np.sum(bvals(n, X)*np.log(n/(n-1.0))))
    V2 = float(sum(lgp*v_q(q, X) for q, lgp in prime_powers(X, primes)))
    if verbose:
        L2 = math.log(X)**2
        print(f"X={X}: 4sqrtX={4*math.sqrt(X):.3f} R={R:.3f} f=4sqrtX-R={f:.4f}")
        print(f"  V_X(2)={V:.4f}  V1-V2={V1-V2:.4f}  (identity gap {V-(V1-V2):.2e})")
        print(f"  V1-[4sqrtX-4sqrt2*log(X/2)]={V1-4*math.sqrt(X)+4*math.sqrt(2)*math.log(X/2):.4f}  V2={V2:.4f}  log^2X={L2:.2f}")
        print(f"  bridge: A_X - f(X) = V_X(2)-4sqrtX = {A-f:.4f}   (/log^2X = {(A-f)/L2:.4f})")
    return dict(R=R, V=V, A=A, f=f, V1=V1, V2=V2, v=v, w=w, lp=lp)

# ---- per-q expansion check ----
X = 10**6
primes6 = sieve(X)
print("== per-q lemma check, X=1e6:  v_q vs -zeta(1/2)q^{-1/2}log(X/q)+(4zeta(1/2)-zeta'(1/2))q^{-1/2}")
for q in [2, 4, 9, 25, 97, 343, 1009, 4096, 9973, 99991, 994009]:
    pred = (-zeta_half)*q**-0.5*math.log(X/q) + (4*zeta_half - zetap_half)*q**-0.5
    vq = v_q(q, X)
    print(f"  q={q:>7} v_q={vq:+.6f} pred={pred:+.6f} diff={vq-pred:+.2e}  bound~{q**-1.5*math.log(X)+X**-0.5*math.log(X):.2e}")

print("\n== bridge checks ==")
res = {}
for Xt in [10**4, 10**5, 3*10**5, 10**6]:
    pr = primes6[primes6 <= Xt]
    res[Xt] = analyze(Xt, pr)

# ---- A_X - A_{floor(X/2)} (z=2 tail of B) ----
print("\n== dyadic difference (z=2 term of B_X) ==")
for Xt in [10**5, 10**6]:
    Y = Xt//2
    print(f"X={Xt}: A_X-A_Y = {res[Xt]['A'] - analyze(Y, primes6[primes6<=Y], verbose=False)['A']:.4f}")

# ---- full B_X at X=1e5 ----
def B_of_X(X, primes):
    Y = X//2
    pX = primes[primes <= X]; pY = primes[primes <= Y]
    rX = np.array([v_q(int(p), X) for p in pX]) - pX**-0.5*np.log(X/pX.astype(float))
    rY = np.array([v_q(int(p), Y) for p in pY]) - pY**-0.5*np.log(Y/pY.astype(float))
    s = np.log(pX.astype(float))*rX.copy()
    s[:len(pY)] -= np.log(pY.astype(float))*rY
    tails = np.cumsum(s[::-1])[::-1]           # tail sum from each prime index = sum_{p'>=p}
    return max(0.0, float(tails.max()))
for Xt in [10**4, 10**5]:
    print(f"B_{Xt} = {B_of_X(Xt, primes6):.4f}   log^2 X = {math.log(Xt)**2:.1f}")
