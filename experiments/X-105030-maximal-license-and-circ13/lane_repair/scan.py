#!/usr/bin/env python3
"""Large-x scan of the three feasibility functionals for ALL integer x <= 10^6:
F1: TB(x) = 4 sqrt(x) A_x - 3 B_x >= 0
F2: G_j(x) = sum_{k sqfree<=x} mu(k) Q_{x/k}(j)/sqrt(k)  (signed row) >= 0, j=2,3
F3(score): exact greedy margin at samples; crude proved lower bound -(3/4)B_x
   [M_score >= -TB_S + (5/4) TB = -(3/4) B_x  since s in [5/4, 2)]
G_j(x) via h_j(n) = sum_{d|n sqfree} mu(d) gamma_j(n/d):
G_j(x) = log(x) P_j(x) - L_j(x),  P_j = cumsum h_j(n)/sqrt(n), L_j = cumsum h_j log n/sqrt n.
"""
import numpy as np
from fast import sieve_mu_np, gamma_arrays, greedy_fast

N = 1_000_000

def build(N):
    mu = sieve_mu_np(N)
    n = np.arange(N+1, dtype=np.float64); n[0] = 1.0
    invs = 1.0/np.sqrt(n); lgn = np.log(n)
    muf = mu.astype(np.float64)
    A = np.cumsum(muf/n); B = np.cumsum(muf*invs)
    # h_j via convolution
    G = {}
    for j in (2, 3):
        g = np.full(N+1, 2.0/(j*(j-1))); g[:j] = 0.0
        g[j] = (j+1)/(j-1); g[j+1] = -((j+1)*(j-2))/(j*(j-1))
        h = np.zeros(N+1)
        for d in range(1, N+1):
            md = mu[d]
            if md == 0: continue
            L = N//d
            h[d::d] += md*g[1:L+1]
        P = np.cumsum(h*invs); Lc = np.cumsum(h*invs*lgn)
        G[j] = (P, Lc)
    return mu, A, B, G

def main():
    mu, A, B, G = build(N)
    x = np.arange(1, N+1, dtype=np.float64)
    sqx = np.sqrt(x)
    TB = 4*sqx*A[1:] - 3*B[1:]
    print("== F1: TB(x) over 1..1e6 ==")
    i = int(np.argmin(TB))
    print(f"min TB = {TB[i]:.6f} at x={i+1};  TB<0 count = {(TB<0).sum()}")
    print(f"max 4sqrt(x)A_x = {np.max(4*sqx*A[1:]):.4f}, min = {np.min(4*sqx*A[1:]):.4f}")
    print(f"B_x: max over x>=3 = {np.max(B[3:]):.6f} (at {int(np.argmax(B[3:])+3)}), "
          f"min = {np.min(B[3:]):.6f}; B_x<0 for all x>=3? {(B[3:]<0).all()}")
    print("\n== F2: G_j(x) ==")
    lgx = np.log(x)
    for j in (2, 3):
        P, Lc = G[j]
        Gx = lgx*P[1:] - Lc[1:]
        # ignore degenerate x < j+? (row empty): consider x >= 5
        sub = Gx[4:]
        i = int(np.argmin(sub)) + 4
        print(f"G_{j}: min over x in [5,1e6] = {Gx[i]:.6f} at x={i+1}; "
              f"negatives = {(sub<0).sum()};  G_{j}(1e6) = {Gx[-1]:.4f}; "
              f"G_{j}(1e6)/sqrt(1e6) = {Gx[-1]/1000:.6f}; G_{j}(1e6)/log(1e6)^2 = {Gx[-1]/np.log(1e6)**2:.4f}")
        for xx in (100, 1000, 10000, 100000, 1000000):
            print(f"   G_{j}({xx}) = {Gx[xx-1]:.6f}   /sqrt = {Gx[xx-1]/np.sqrt(xx):.6f}  /log^2 = {Gx[xx-1]/np.log(xx)**2:.6f}")
    print("\n== F3 crude proved bound: -(3/4) B_x ==")
    sub = -0.75*B[5:]
    i = int(np.argmin(sub)) + 5
    print(f"min over x>=5 of -(3/4)B_x = {sub.min():.6f} at x={i}")
    print("\n== exact greedy at samples (verify G_j = m_j, get exact m_sc) ==")
    ga = gamma_arrays(N)
    for xx in (10007, 31623, 100003, 316227, 999999):
        r = greedy_fast(float(xx) + 0.5, mu, ga)  # x=int+0.5 avoids boundary ties
        r2 = greedy_fast(float(xx), mu, ga)
        print(f"x={xx}: TB={r2['TB']:.6f} m2={r2['m2']:.6f} m3={r2['m3']:.6f} "
              f"m_sc={r2['m_sc']:.6f} G2={r2['G2']:.6f} G3={r2['G3']:.6f} feas={r2['feasible']}")
    # cross-validate convolution G against direct greedy G at two points
    for xx in (88, 1009):
        P, Lc = G[2]
        Gc = np.log(float(xx))*P[xx] - Lc[xx]
        r = greedy_fast(float(xx), mu, ga)
        print(f"convolution G_2({xx}) = {Gc:.9f} vs greedy G2 = {r['G2']:.9f}  diff={abs(Gc-r['G2']):.2e}")

if __name__ == "__main__":
    main()
