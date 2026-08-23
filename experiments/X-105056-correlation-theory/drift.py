uHome = "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/progA2/laneM"
import numpy as np, math, json
from mpmath import mp, hyp2f1, mpf
mp.dps = 25
h2 = math.log(2); s2 = math.sqrt(2)
def R(v):
    v = abs(v)
    if v <= h2: return 3*h2-(3+s2)*v
    if v <= 2*h2: return -s2*(2*h2-v)
    return 0.0
K = 40
gk = [mpf(1)]
for k in range(1, K): gk.append(gk[-1]*(k - mpf(3)/2)/k)
from functools import lru_cache
@lru_cache(maxsize=None)
def r_local(p, alpha):
    x = mpf(p)**(-1)
    return float(gk[alpha]*hyp2f1(alpha-0.5, -0.5, alpha+1, x)/hyp2f1(-0.5, -0.5, 1, x))

PMAX = 600
# varrho(n) multiplicative over p^alpha || n, via spf
spf = np.zeros(PMAX*PMAX+1, dtype=np.int64)  # need up to a*b <= ~4*PMAX^2? no: varrho(a)*varrho(b) separately
def varrho(n):
    out = 1.0
    while n > 1:
        p = 2
        while n % p: p += 1 if p == 2 else 2
        a = 0
        while n % p == 0: n //= p; a += 1
        out *= r_local(p, a)
    return out
vr = np.array([1.0]+[varrho(n) for n in range(1, PMAX+1)])

# gcd table via math.gcd; drift partial sums S(P) = sum_{max(a,b)<=P} R(log a/b)(ab)^{-1/2} vr(a)vr(b), (a,b)=1, a != b
import math as m
Ps = [2,3,4,6,8,12,16,24,32,48,64,96,128,192,256,384,512,600]
S = 0.0; Sabs = 0.0
out = []
pi = 0
for M in range(2, PMAX+1):  # M = max(a,b); add pairs with max = M (both orders)
    for c in range(max(1, M//4+1), M):
        if m.gcd(M, c) == 1:
            v = math.log(M/c)
            if v < 2*h2:
                t = R(v)/math.sqrt(M*c)*vr[M]*vr[c]
                S += 2*t; Sabs += 2*abs(t)
    if M in Ps:
        out.append((M, S, Sabs))
        print(f"P={M:4d}  Sdrift={S:+.5f}  Sabs={Sabs:.4f}  Sabs*log^2P/P={Sabs*math.log(M)**2/M:.4f}")
json.dump([[int(a), b, c] for a, b, c in out], open(uHome+"/drift_partial.json", "w"))
