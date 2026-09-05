#!/usr/bin/env python3
"""High-precision (mpmath mp.dps=60) spot checks of marginal quantities +
cap_2 crossover + L-105021 continuity (C* closed form)."""
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, log as mlog
mp.dps = 60
from fast import sieve_mu_np, gamma_arrays, greedy_fast

Nsieve = 1_000_000
mu = sieve_mu_np(Nsieve)

def hp_greedy(x, js=(2,3)):
    xm = mpf(x)
    n = int(x)
    ks = [k for k in range(1, n+1) if mu[k] != 0]
    T, s, rho = {}, {}, {j: {} for j in js}
    for k in ks:
        Y = xm/k; sY = msqrt(Y); den = 4*sY - 3
        T[k] = den/msqrt(k)
        s[k] = (5*sY-3)/den
        for j in js:
            M = int(Y)
            q = mpf(0)
            for m in range(j, M+1):
                if m == j: g = mpf(j+1)/(j-1)
                elif m == j+1: g = -mpf((j+1)*(j-2))/(j*(j-1))
                else: g = mpf(2)/(j*(j-1))
                q += g/msqrt(m)*mlog(Y/m)
            rho[j][k] = q/den
    E = [k for k in ks if mu[k] == 1]; O = [k for k in ks if mu[k] == -1]
    D = sum(T[o] for o in O); TB = sum(T[e] for e in E) - D
    c = {}; rem = D
    for e in E:
        t = min(T[e], rem); c[e] = t; rem -= t
    out = dict(TB=TB)
    for j in js:
        out[f"m{j}"] = sum(c[e]*rho[j][e] for e in E) - sum(T[o]*rho[j][o] for o in O)
    out["m_sc"] = sum(T[o]*s[o] for o in O) - sum(c[e]*s[e] for e in E)
    return out

print("== x=88 margins at 60 digits vs float64 ==")
r = hp_greedy(88)
ga = gamma_arrays(10008)
f = greedy_fast(88.0, mu, ga)
for k in ("TB", "m2", "m3", "m_sc"):
    print(f"  {k}: hp={mp.nstr(r[k], 20)}   f64={f[k]!r}   |diff|={mp.nstr(abs(r[k]-mpf(f[k])), 3)}")

print("\n== TB(200) (global minimum over [2,1e6]) at 60 digits ==")
from fractions import Fraction
Afr = Fraction(0); Bmp = mpf(0)
for nn in range(1, 201):
    if mu[nn] != 0:
        Afr += Fraction(int(mu[nn]), nn); Bmp += mpf(int(mu[nn]))/msqrt(nn)
TB200 = 4*msqrt(200)*mpf(Afr.numerator)/Afr.denominator - 3*Bmp
print(f"  A_200 = {Afr} = {mp.nstr(mpf(Afr.numerator)/Afr.denominator, 12)}")
print(f"  TB(200) = {mp.nstr(TB200, 25)}   (f64 scan: 1.603621180)")

print("\n== B_221 (max of B_x for x>=3) at 60 digits ==")
B221 = mpf(0)
for nn in range(1, 222):
    if mu[nn] != 0: B221 += mpf(int(mu[nn]))/msqrt(nn)
print(f"  B_221 = {mp.nstr(B221, 25)}  -> crude score floor -(3/4)B = {mp.nstr(-0.75*B221, 20)}")

print("\n== L-105021 continuity: C* = (45045 |B_13|/4646)^2 ==")
B13 = 1 - 1/msqrt(2) - 1/msqrt(3) - 1/msqrt(5) + 1/msqrt(6) - 1/msqrt(7) + 1/msqrt(10) - 1/msqrt(11) - 1/msqrt(13)
Cstar = (45045*abs(B13)/4646)**2
print(f"  B_13 = {mp.nstr(B13, 25)}  C* = {mp.nstr(Cstar, 25)}  (claimed 87.35893176924588158)")

print("\n== cap_2(x) - TB(x): crossover and min beyond ==")
n = np.arange(Nsieve+1, dtype=np.float64); n[0] = 1.0
muf = mu.astype(np.float64); invs = 1.0/np.sqrt(n)
A = np.cumsum(muf/n); B = np.cumsum(muf*invs)
ev = (mu == 1)
alpha = np.cumsum(np.where(ev, 1.0/n, 0.0)); beta = np.cumsum(np.where(ev, invs, 0.0))
xf = np.arange(2, Nsieve+1)
xd = xf.astype(np.float64)
TB = 4*np.sqrt(xd)*A[xf] - 3*B[xf]
lo = xf//2
cap2 = 4*np.sqrt(xd)*(alpha[xf]-alpha[lo]) - 3*(beta[xf]-beta[lo])
bad = xf[cap2 - TB <= 0]
print(f"  largest x with cap_2 <= TB: {bad.max() if len(bad) else None}; count={len(bad)}")
m47 = (cap2 - TB)[xf >= 47]
print(f"  min over [47,1e6] of cap_2-TB = {m47.min():.6f} at x={xf[xf>=47][np.argmin(m47)]}")

print("\n== kappa_j sup check: left-edge values decreasing ==")
for j, kbar in ((2, 3/np.sqrt(2)), (3, 2/np.sqrt(3))):
    Cj = 2.0/(j*(j-1))
    gam = lambda m: (0.0 if m < j else ((j+1)/(j-1) if m == j else (-((j+1)*(j-2))/(j*(j-1)) if m == j+1 else Cj)))
    G = 0.0; H = 0.0; worst = 0.0
    for Nc in range(j, 20001):
        G += Nc*gam(Nc); H += gam(Nc)/np.sqrt(Nc)
        v = (4*G/Nc**1.5 - H)/3.0
        worst = max(worst, v)
    print(f"  j={j}: sup over cells (left edges, N<=2e4) = {worst:.9f}; claimed kappa_bar = A_j/sqrt(j) = {kbar:.9f}")
