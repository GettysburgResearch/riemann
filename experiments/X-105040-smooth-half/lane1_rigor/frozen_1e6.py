#!/usr/bin/env python3
"""Frozen 61-smooth greedy at x = 1e6 (NOT saturated — only divisors <= x active).
(1) Direct-Q margins vs L-105031(f) quoted m2=106.2, m3=39.4, m_sc=10.7.
(2) M_sc identity check (Corollary R.1 derivation).
(3) Expansion-Q variant (H -> 4 sqrt Y + zeta(1/2) log Y + zeta'(1/2) wherever
    floor(Y) >= j+1) — margin difference quantifies the E-neglect in-sample.
float64 with math.fsum (exact summation of rounded terms)."""
import math
import numpy as np

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
divs = [(1, 1)]
for p in P:
    divs = divs + [(d*p, -m) for (d, m) in divs if d*p <= 10**7]
divs = sorted(d for d in divs)
X = 1_000_000.0
act = [(d, m) for d, m in divs if d <= X]
print(f"active frozen divisors at x=1e6: {len(act)}")

# gamma cumsum arrays to N=1e6
N = 1_000_000
mm = np.arange(N+1, dtype=np.float64); mm[0] = 1.0
invs = 1.0/np.sqrt(mm); lg = np.log(mm)
ga = {}
for j in (2, 3):
    g = np.full(N+1, 2.0/(j*(j-1))); g[:j] = 0.0
    g[j] = (j+1)/(j-1); g[j+1] = -((j+1)*(j-2))/(j*(j-1))
    ga[j] = (np.cumsum(g*invs), np.cumsum(g*invs*lg))

ZH = -1.4603545088095868129
ZP = -3.9226461392091517275

def Qdir(Y, j):
    M = int(Y)
    Pg, Lg = ga[j]
    return math.log(Y)*Pg[M] - Lg[M]

def Qexp(Y, j):
    C = 2.0/(j*(j-1)); A = (j+1)/(j-1); B = (j+1)*(j-2)/(j*(j-1))
    if int(Y) < j+1:
        return Qdir(Y, j)   # knot form not fully active; use direct
    lam = A/math.sqrt(j) - B/math.sqrt(j+1) + C*(ZH - sum(1/math.sqrt(m) for m in range(1, j+2)))
    kapv = -A*math.log(j)/math.sqrt(j) + B*math.log(j+1)/math.sqrt(j+1) \
           + C*(ZP + sum(math.log(m)/math.sqrt(m) for m in range(1, j+2)))
    return 4*C*math.sqrt(Y) + lam*math.log(Y) + kapv

def greedy(Qfun):
    odds = [(d, m) for d, m in act if m == -1]
    evens = [(d, m) for d, m in act if m == +1]
    D = math.fsum((4*math.sqrt(X/d) - 3)/math.sqrt(d) for d, _ in odds)
    K = {j: math.fsum(Qfun(X/d, j)/math.sqrt(d) for d, _ in odds) for j in (2, 3)}
    Ksc = math.fsum((5*math.sqrt(X/d) - 3)/math.sqrt(d) for d, _ in odds)
    rem = D
    m2t = []; m3t = []; msct = []; sliv = []
    estar = None; theta = None
    B_E = math.fsum(1/math.sqrt(d) for d, _ in evens)
    B_O = math.fsum(1/math.sqrt(d) for d, _ in odds)
    for d, _ in evens:
        T = (4*math.sqrt(X/d) - 3)/math.sqrt(d)
        if rem > 0:
            take = min(T, rem)
            th = take/T
            if T > rem: estar, theta = d, th
            rem -= take
            m2t.append(th*Qfun(X/d, 2)/math.sqrt(d))
            m3t.append(th*Qfun(X/d, 3)/math.sqrt(d))
            msct.append(th*(5*math.sqrt(X/d) - 3)/math.sqrt(d))
            sliv.append((1-th)/math.sqrt(d))
        else:
            sliv.append(1/math.sqrt(d))
    m2 = math.fsum(m2t) - K[2]; m3 = math.fsum(m3t) - K[3]
    msc = Ksc - math.fsum(msct)
    Bs = B_E - B_O
    msc_id = 0.75*(math.fsum(sliv) - Bs)
    return m2, m3, msc, msc_id, estar, theta, Bs

m2, m3, msc, msc_id, estar, theta, Bs = greedy(Qdir)
print(f"DIRECT   : m2={m2:.6f}  m3={m3:.6f}  m_sc={msc:.6f}  [L-105031(f): 106.2 / 39.4 / 10.7]")
print(f"           e*={estar} theta*={theta:.9f}  B^s_x={Bs:.9f}")
print(f"           M_sc identity (3/4)[sliver - B^s] = {msc_id:.9f}  |diff|={abs(msc-msc_id):.2e}")
m2e, m3e, msce, _, _, _, _ = greedy(Qexp)
print(f"EXPANSION: m2={m2e:.6f}  m3={m3e:.6f}  m_sc={msce:.6f}")
print(f"           |dm2|={abs(m2-m2e):.3e}  |dm3|={abs(m3-m3e):.3e}  (E-neglect in-sample)")

# zero-row-mass odds audit: odds with x/o < j contribute demand but Q=0
for j in (2, 3):
    zr = [d for d, m in act if m == -1 and X/d < j]
    dm = math.fsum((4*math.sqrt(X/d)-3)/math.sqrt(d) for d in zr)
    print(f"j={j}: odds with x/o < j: {len(zr)} of {sum(1 for _,m in act if m==-1)}, "
          f"demand mass {dm:.4f} (row mass exactly 0 — capacity consumed, no row demand)")
