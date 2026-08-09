"""Rank-2 mechanism with FULL object weights; binding-family census + margin law at X=3000."""
import numpy as np
from math import log, sqrt
from rev_final import Model, children

# full-weight rank-2 audit at the deep points
def rank2(X, n, p):
    M = Model(X, n); E = M.E_table(); ip = p - M.Wlo
    G = np.zeros(X+2)
    for m in range(n, X+1): G[m] = m*E[m, ip]
    dW = np.zeros(X+2); dW[n] = G[n]/p
    for m in range(n+1, X+1): dW[m] = (G[m]-G[m-1])/p
    A, B = [], []
    for m in range(n, X+1):
        if abs(dW[m]) < 1e-12: continue
        for k in range(1, X//m + 1):
            if M.mu[k] == 0: continue
            (A if M.mu[k]*dW[m] > 0 else B).append((abs(dW[m])*M.w[m*k], m, k))
    A.sort(reverse=True); B.sort(reverse=True)
    w2p, w2p2 = M.w[2*p], M.w[2*p+2]
    nbig = sum(1 for wgt, _, _ in A if wgt >= w2p - 1e-14)
    print(f"({X},{n},{p}) FULL wts: B1,B2={[(m,k,round(wg,4)) for wg,m,k in B[:2]]} "
          f"A1,A2={[(m,k,round(wg,4)) for wg,m,k in A[:2]]} "
          f"#A with wt>=w(2p): {nbig}; A2 == w(2p+2)? {abs(A[1][0]-w2p2) < 1e-12}; "
          f"B2 == w(2p)? {abs(B[1][0]-w2p) < 1e-12}")
for args in [(1000, 23, 30), (1000, 29, 40), (1000, 50, 70)]:
    rank2(*args)

# binding-family census + margin law at X=3000 (forward g per n; g n-indep above 2n but recompute cheaply)
X = 3000
M = Model(X, 2)  # reuse S etc.
S = M.S
res = []
for n in range(8, 301):
    g = np.zeros(X+2); sink = np.zeros(X+2)
    for m in range(2*n, X+1): g[m] = S[m]
    for m in range(X, 2*n-1, -1):
        gm = g[m]
        if gm == 0.0: continue
        for c in children(m):
            q = c/(2*m)*gm
            if c >= 2*n: g[c] += q
            elif c >= n: sink[c] += q
    Sig = np.array([S[p] + sink[p] for p in range(n, 2*n)])
    i = int(np.argmin(Sig)); p = n + i
    res.append((n, p, Sig[i]))
cats = {"bottom(n)": 0, "2n-1": 0, "odd-int": 0, "even-int": 0}
neg = 0
for n, p, v in res:
    if v < 0: neg += 1
    if p == n: cats["bottom(n)"] += 1
    elif p == 2*n-1: cats["2n-1"] += 1
    elif p % 2 == 1: cats["odd-int"] += 1
    else: cats["even-int"] += 1
tot = len(res)
print(f"X=3000 scan n=8..300 ({tot} scales): negatives={neg}; " +
      "; ".join(f"{k}={100*v/tot:.0f}%" for k, v in cats.items()))
xs = np.array([log(X/n)+2 for n, p, v in res])
ys = np.array([sqrt(n)*v for n, p, v in res])
slope = float(np.sum(xs*ys)/np.sum(xs*xs))
resid = ys - slope*xs
r2 = 1 - float(np.sum(resid**2)/np.sum((ys-ys.mean())**2))
print(f"margin law: sqrt(n)*minSig ~ {slope:.3f}*(log(X/n)+2), R^2(through-origin fit)={r2:.3f}")
# even-interior exceptions?
exc = [(n, p) for n, p, v in res if p != n and p != 2*n-1 and p % 2 == 0]
print(f"even-interior binders: {exc[:8]}{'...' if len(exc) > 8 else ''} ({len(exc)} total)")
