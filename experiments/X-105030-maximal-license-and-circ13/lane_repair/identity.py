#!/usr/bin/env python3
"""(1) Exact identity G_j(x) = C_j log x + sum_{q<=j+1} delta_j(q) q^{-1/2} W(x/q),
   W(y) = sum_{m<=y} mu(m) log(y/m)/sqrt(m).
(2) min TB over [2,1e6]; effective slopes.
(3) sliver lemma: cap_j(x) - TB(x) > 0 for x >= 30 (cap_j = even capacity in (x/j, x]).
(4) exact minima of m2,m3,m_sc,TB over integer x in [3,10007], plus m_j == G_j check."""
import numpy as np
from math import sqrt, log
from fast import sieve_mu_np, gamma_arrays, greedy_fast

N = 1_000_000
mu = sieve_mu_np(N)
n = np.arange(N+1, dtype=np.float64); n[0] = 1.0
invs = 1.0/np.sqrt(n); lgn = np.log(n)
muf = mu.astype(np.float64)
A = np.cumsum(muf/n); B = np.cumsum(muf*invs); Blog = np.cumsum(muf*invs*lgn)

def W(y):
    m = int(np.floor(y))
    return log(y)*B[m] - Blog[m]

def G_direct(x, j):
    ga = gamma_arrays(int(x)+2, js=(j,))
    r = greedy_fast(float(x), mu, ga, js=(j,))
    return r[f"G{j}"]

print("== (1) identity check ==")
for j in (2, 3):
    Cj = 2.0/(j*(j-1))
    gam = {}
    for q in range(1, j+2):
        if q < j: g = 0.0
        elif q == j: g = (j+1)/(j-1)
        else: g = -((j+1)*(j-2))/(j*(j-1))
        gam[q] = g
    delta = {q: gam[q] - Cj for q in range(1, j+2)}
    Lam = sum(delta[q]/sqrt(q) for q in delta)
    print(f"j={j}: delta={ {q: round(delta[q],6) for q in delta} }  Lambda_j={Lam:.6f}  "
          f"slope C_j + Lambda_j/zeta(1/2) = {Cj + Lam/(-1.4603545088):.6f}")
    for x in (88.0, 1009.0, 100003.0):
        lhs = G_direct(x, j)
        rhs = Cj*log(x) + sum(delta[q]/sqrt(q)*W(x/q) for q in delta)
        print(f"   x={x:>9}: G_{j} greedy = {lhs:.9f}   identity = {rhs:.9f}   diff = {abs(lhs-rhs):.2e}")

print("\n== (2) TB minima ==")
x = np.arange(1, N+1, dtype=np.float64)
TB = 4*np.sqrt(x)*A[1:] - 3*B[1:]
for lo in (2, 5, 100):
    sub = TB[lo-1:]
    i = int(np.argmin(sub)) + lo
    print(f"min TB over [{lo},1e6] = {TB[i-1]:.6f} at x={i}")

print("\n== (3) sliver lemma: cap_j(x) - TB(x) ==")
ev = (mu == 1)
alpha = np.cumsum(np.where(ev, 1.0/n, 0.0)); beta = np.cumsum(np.where(ev, invs, 0.0))
for j in (2, 3):
    xf = np.arange(30, N+1)
    lo = (xf // j).astype(np.int64)   # evens e <= x/j excluded; cap over (x/j, x]
    capj = 4*np.sqrt(xf.astype(float))*(alpha[xf]-alpha[lo]) - 3*(beta[xf]-beta[lo])
    diff = capj - TB[xf-1]
    i = int(np.argmin(diff))
    print(f"j={j}: min over [30,1e6] of cap_j - TB = {diff[i]:.6f} at x={xf[i]} "
          f"(cap_j={capj[i]:.4f}); cap_j(1e6)/sqrt = {capj[-1]/1000:.4f}")

print("\n== (4) exact minima over integer x in [3,10007] ==")
ga = gamma_arrays(10008)
mins = {k: (1e18, None) for k in ("m2","m3","m_sc","TB")}
maxdev = 0.0; slivbad = []
for xi in range(3, 10008):
    r = greedy_fast(float(xi), mu, ga)
    for k in mins:
        if r[k] < mins[k][0]: mins[k] = (r[k], xi)
    dev = max(abs(r["m2"]-r["G2"]), abs(r["m3"]-r["G3"]))
    if dev > 1e-9: slivbad.append((xi, dev))
    maxdev = max(maxdev, dev)
for k in mins:
    print(f"min {k} over [3,10007] = {mins[k][0]:.9f} at x={mins[k][1]}")
print(f"max |m_j - G_j| = {maxdev:.2e}; fibres where sliver touches rows: {slivbad[:10]}")
