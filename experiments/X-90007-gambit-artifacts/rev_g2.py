"""G2 audit: chain objects, cardinality kill, rank-2 mechanism, doubling identity."""
import numpy as np
from rev_final import Model, children

def audit(X, n, p):
    M = Model(X, n)
    E = M.E_table()
    ip = p - M.Wlo
    G = np.zeros(X+2)
    for m in range(n, X+1):
        G[m] = m*E[m, ip]
    dG = np.zeros(X+2)
    dG[n] = G[n]
    for m in range(n+1, X+1):
        dG[m] = G[m] - G[m-1]
    # doubling identity W(2m)=W(m)+(1/2)(W(ceil(2m/3))+W(floor(4m/3))), m>=n, 2m<=X
    Wf = G/p
    worst = 0.0
    for m in range(n, X//2 + 1):
        a3 = -(-2*m//3); b3 = (4*m)//3
        rhs = Wf[m] + 0.5*(Wf[a3]*(a3 >= n) + Wf[b3]*(b3 >= n))
        worst = max(worst, abs(Wf[2*m]-rhs))
    print(f"({X},{n},{p}): doubling identity worst |diff| = {worst:.2e}")
    # chain objects (m,k): k sf, mk<=X, m>=n, dG(m)!=0
    A, B = [], []
    for m in range(n, X+1):
        if abs(dG[m]) < 1e-12: continue
        for k in range(1, X//m + 1):
            if M.mu[k] == 0: continue
            s = M.mu[k]*dG[m]
            (A if s > 0 else B).append((M.w[m*k]*abs(dG[m]), m, k, M.w[m*k]))
    A.sort(reverse=True); B.sort(reverse=True)
    print(f"   #A={len(A)} #B={len(B)}  (#B>#A? {len(B) > len(A)})")
    # top objects by BARE weight w(mk) (G2's mechanism narrative uses w-weights)
    Aw = sorted(A, key=lambda t: -t[3]); Bw = sorted(B, key=lambda t: -t[3])
    print(f"   top-3 B by w: {[(m,k,round(w4,5)) for _,m,k,w4 in Bw[:3]]}")
    print(f"   top-3 A by w: {[(m,k,round(w4,5)) for _,m,k,w4 in Aw[:3]]}")
    w2p = M.w[2*p]
    Abig = [(m, k) for _, m, k, w4 in Aw if w4 >= w2p - 1e-15]
    print(f"   A-chains with w(mk) >= w(2p): {Abig}  [G2 claims only (p,1)]")
    # sorted-domination (Hall-type necessary cond) on FULL weights |dG|*w
    r = None
    for i in range(min(len(A), len(B))):
        if B[i][0] > A[i][0] + 1e-12:
            r = i+1; break
    print(f"   sorted-domination on |dG|w fails at rank {r}" if r else "   sorted-domination on |dG|w passes (injection not excluded by ranks)")
    return M, dG

audit(100, 13, 13)
audit(1000, 23, 30)
audit(1000, 29, 40)
audit(1000, 50, 70)
