import numpy as np, math
from math import log, sqrt, fsum
from wsts_verify import (sieve, bX, v_p, r_all, B_and_tail, E_profile, H_of,
                         cell_int_E, ensure_N, SN_cache, AN_cache, primes)
import mpmath as mp

print("== N4: shell decomposition  sum (log p)s_X(p) = sqrtX*H_c(z/X) + E_{X,Y}(z) + floor ==")
def shell_check(X, zs):
    Y = X//2; c = Y/X
    prX, s, suffix, B = B_and_tail(X, primes)
    def E_c(th):
        v = E_profile(th)
        if th <= c: v -= c**-0.5 * E_profile(th/c)
        return v
    def H_c(th):
        if th >= c: return H_of(th)
        return H_of(th) - sqrt(c)*H_of(th/c)
    out=[]
    for z in zs:
        i = np.searchsorted(prX, z)
        lhs = suffix[i] if i < len(prX) else 0.0
        Esamp = fsum(log(int(p))*E_c(p/X) for p in prX[i:]) / sqrt(X)   # int E_c dtheta / sqrtX
        cont  = sqrt(X)*H_c(z/X)                                        # int E_c dt / sqrtX
        EXY   = Esamp - cont
        fl    = lhs - cont - EXY   # = lhs - Esamp
        bound = 1.31*z**-1.5*0 + 1.31*(2+log(X/z))*z**-0.5*0  # per-prime; aggregate bound:
        agg   = z**-0.5*(1+log(z))*(1+log(X))
        out.append((z, lhs, cont, EXY, fl, agg))
    return out
for X in [1000, 10000, 50000]:
    print(f" X={X}:")
    for z,lhs,cont,EXY,fl,agg in shell_check(X, [2, 10, 100, X**0.5, X/10, X/3]):
        print(f"   z={z:9.1f} lhs={lhs:+9.4f} moat={cont:+9.4f} E_XY={EXY:+9.4f} floor={fl:+8.4f} (|floor|<= {1.31*agg:.2f})")

print("\n== N4b: growth of sup_z |E_{X,Y}(z)| ==")
for X in [500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]:
    Y = X//2; c = Y/X
    prX = primes[primes<=X]
    def E_c(th):
        v = E_profile(th)
        if th <= c: v -= c**-0.5*E_profile(th/c)
        return v
    w = np.array([log(int(p))*E_c(p/X) for p in prX])
    sufE = np.cumsum(w[::-1])[::-1]/sqrt(X)   # sample part from z=p_j
    def H_c(th):
        if th >= c: return H_of(th)
        return H_of(th) - sqrt(c)*H_of(th/c)
    conts = np.array([sqrt(X)*H_c(p/X) for p in prX])
    EXY = sufE - conts
    print(f"  X={X:7d} sup_z|E_XY|={np.abs(EXY).max():8.4f}  log^2X={log(X)**2:7.2f} log^3X/10={log(X)**3/10:7.2f}")

print("\n== N5: Mellin dual  Ehat(s) = zeta(s+1/2)*ghat(s) - 1/s^2,  ghat=-1/s^2+4/(s(2s+1)) ==")
mp.mp.dps = 30
def Ehat_num(s, Ncells=4000):
    # int_0^1 E(u) u^{s-1/2} du, cellwise Gauss-Legendre
    tot = mp.mpf(0)
    for N in range(1, Ncells+1):
        a, b = mp.mpf(1)/(N+1), mp.mpf(1)/N
        ensure_N(N); SN, AN = SN_cache[N], AN_cache[N]
        f = lambda t: (mp.sqrt(1/t)*(AN + (SN+1)*mp.log(t) + 4*SN) - 4*N)*t**(s-mp.mpf(1)/2)
        tot += mp.quad(f, [a, b])
    # tail 0..1/(Ncells+1): use asymptotic E ~ u^{-1/2}((c12+1)log u + cA + 4c12) with c12=zeta(1/2), cA=-zeta'(1/2)
    c12 = mp.zeta(mp.mpf(1)/2); cA = -mp.diff(mp.zeta, mp.mpf(1)/2)
    eps = mp.mpf(1)/(Ncells+1)
    f2 = lambda t: (mp.sqrt(1/t)*((c12+1)*mp.log(t) + cA + 4*c12))*t**(s-mp.mpf(1)/2)
    tot += mp.quad(f2, [0, eps])
    return tot
def Ehat_formula(s):
    s = mp.mpf(s) if isinstance(s,(int,float)) else s
    g = -1/s**2 + 4/(s*(2*s+1))
    return mp.zeta(s+mp.mpf(1)/2)*g - 1/s**2
for s in [mp.mpf(2), mp.mpf('0.8'), mp.mpc('0.7','1.3')]:
    a, b = Ehat_num(s), Ehat_formula(s)
    print(f"  s={mp.nstr(s,4)}: numeric={mp.nstr(a,10)} formula={mp.nstr(b,10)} |diff|={mp.nstr(abs(a-b),3)}")
print("  Ehat(1/2) (should be 0, = kappa):", mp.nstr(mp.limit(lambda s: Ehat_formula(s), mp.mpf(1)/2), 8))
print("  ghat(1/2) =", mp.nstr(-4 + 4/(0.5*2),6), " ghat'(1/2)=", mp.nstr(mp.diff(lambda s: -1/s**2+4/(s*(2*s+1)), mp.mpf(1)/2),8))

print("\n== N6: profile constants  C_E=sup |E| th^{1/2}/(1+log(1/th)),  C_E'=sup |E'| th^{3/2}/(1+log(1/th)) ==")
sup1 = 0; sup2 = 0; arg1=None
for N in range(1, 20001):
    ensure_N(N); SN, AN = SN_cache[N], AN_cache[N]
    for t in np.linspace(1/(N+1)+1e-12, 1/N-1e-12, 7 if N<200 else 3):
        L = 1+log(1/t)
        e = abs(t**-0.5*(AN+(SN+1)*log(t)+4*SN) - 4*N)*t**0.5/L
        ep = abs(t**-1.5*((SN+1) - 0.5*(AN+(SN+1)*log(t)+4*SN)))*t**1.5/L
        if e>sup1: sup1, arg1 = e, (N,t)
        sup2 = max(sup2, ep)
print(f"  C_E  empirical = {sup1:.4f} at {arg1}")
print(f"  C_E' empirical = {sup2:.4f}")
print("  floor const: max over q,X of |r_X(q)-X^{-1/2}E(q/X)| q^{3/2}/(2+log(X/q)):")
worst=0
for X in [1000, 10000]:
    for q in range(2, min(X,3000)):
        r = v_p(q, X) - log(X/q)/sqrt(q)   # r for ALL integers q (v_q defined same way)
        err = abs(r - E_profile(q/X)/sqrt(X))*q**1.5/(2+log(X/q))
        worst = max(worst, err)
print(f"  C_f empirical = {worst:.4f}   (proved bound zeta(3/2)/2 = {0.5*float(mp.zeta(1.5)):.4f})")

print("\n== N7: A_3(2), A_2(2), telescope sanity ==")
for X in [2,3,4,5]:
    prX, rX = r_all(X, primes)
    print(f"  A_{X}(2) = {fsum(log(int(p))*r for p,r in zip(prX,rX)):+.6f}")
