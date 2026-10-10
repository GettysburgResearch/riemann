"""Cross-examiner check of Derivation-2 Step 4 (Mellin + Landau ingredients).

(a) P(w) = -zeta'/zeta(w) - h(w) numerically (sign conventions + h correctness).
(b) End-to-end F(s) = int_1^inf f(X)X^{-s-1}dX  vs  M(s) = 4/(s-1/2)
    + (zeta'/zeta)(s+1/2)/s^2 + h(s+1/2)/s^2, with F computed by EXACT
    piecewise closed-form integration of f(X)=4 sqrt X - R(X) between
    consecutive primes up to T=1e6 plus a tail estimate.
(c) Removability of s=1/2: M(1/2+t) bounded as t->0.
"""
import numpy as np, math
from mpmath import mp, mpf, zeta, diff

mp.dps = 30

def sieve(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

T = 10**6
pr = sieve(T).astype(float)
lp = np.log(pr)

def zpz(w):          # zeta'/zeta(w)
    return diff(zeta, w) / zeta(w)

def hval(w, pmax=200000):
    p = pr[pr <= pmax]
    l = lp[pr <= pmax]
    return float(np.sum(l * p**(-2.0*w) / (1.0 - p**(-w))))

# (a) P(w) + zeta'/zeta(w) + h(w) ~ 0
print("== (a) P(w) = -zeta'/zeta - h ==")
for w in (2.5, 1.75):
    P = float(np.sum(lp * pr**(-w)))
    # tail bound: int_T^inf log t * t^-w dt
    tail = (math.log(T)/(w-1) + 1.0/(w-1)**2) * T**(1-w)
    rhs = float(-zpz(w)) - hval(w)
    print(f"  w={w}: P_T={P:.10f}  -z'/z-h={rhs:.10f}  diff={P-rhs:+.2e}  tailbound={tail:.1e}")

# (b) end-to-end F(s)=M(s) at s=2, 1.25 via exact piecewise integration
# R(X) = a_i log X - b_i on [p_i, p_{i+1}),  a_i=sum_{p<=p_i} logp/sqrt p, b_i=sum logp^2/sqrt p
a = np.cumsum(lp / np.sqrt(pr))
bb = np.cumsum(lp**2 / np.sqrt(pr))
edges = np.concatenate([pr, [float(T) + 1e-9]])

def F_direct(s):
    lo = edges[:-1]; hi = edges[1:]
    # int_lo^hi 4 sqrt X * X^{-s-1} dX = 4/(s-1/2) (lo^{1/2-s}-hi^{1/2-s})
    I1 = 4.0/(s-0.5) * (lo**(0.5-s) - hi**(0.5-s))
    # int X^{-s-1} dX = (lo^-s - hi^-s)/s ; int log X X^{-s-1} = (lo^-s(s loglo+1)-hi^-s(s loghi+1))/s^2
    Ilog = (lo**(-s)*(s*np.log(lo)+1) - hi**(-s)*(s*np.log(hi)+1))/s**2
    Icst = (lo**(-s) - hi**(-s))/s
    total = float(np.sum(I1 - a*Ilog + bb*Icst))
    # segment [1,2): f = 4 sqrt X  (R=0)
    total += 4.0/(s-0.5)*(1.0 - 2.0**(0.5-s))
    # tail estimate X>T: |f| <~ f(T)+ drift; use f(T)*int_T^inf X^{-s-1}
    fT = 4*math.sqrt(T) - float(a[-1]*math.log(T) - bb[-1])
    tail = abs(fT) * T**(-s)/s * 3
    return total, tail

print("== (b) end-to-end Mellin identity ==")
for s in (2.0, 1.25):
    Fd, tl = F_direct(s)
    M = 4.0/(s-0.5) + float(zpz(s+0.5))/s**2 + hval(s+0.5)/s**2
    print(f"  s={s}: F_direct={Fd:.10f}  M(s)={M:.10f}  diff={Fd-M:+.2e}  tail~{tl:.1e}")

# (c) removability at s=1/2
print("== (c) s=1/2 removability: M(1/2+t) ==")
for t in (1e-2, 1e-4, 1e-6):
    s = 0.5 + t
    M = 4.0/(s-0.5) + float(zpz(s+0.5))/s**2 + hval(s+0.5)/s**2
    print(f"  t={t:.0e}: M={M:.6f}")
