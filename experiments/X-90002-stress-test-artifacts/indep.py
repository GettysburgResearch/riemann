#!/usr/bin/env python3
"""Independent re-implementation of L-30901 / T-30901 objects (from scratch).

Definitions implemented verbatim:
  Psi_X(x,c) = x^{-1/2} log(min(x,X)/c)                       (L-30901.3)
  b_X(q) = sum_{k>=1} [Psi_X(2kq-1, 2q-1) - Psi_X((2k+1)q, 2q-1)]   (L-30901.4)
  M = floor((X+1)/2), b_X(M+1) = 0
  V(b) = sum_{n=2}^{M} sqrt(n) |b(n)-b(n+1)|                  (L-30901.16)
  (T_M b)(q) = sum_{k>=1} [b(2kq-1) - b((2k+1)q)], zero ext. beyond M  (L-30901.18)
  chain: M_{g+1} = floor((M_g+1)/2)
"""
import numpy as np

SQ = np.sqrt

def zeta_half(A):
    """zeta(1/2, A) via Euler-Maclaurin asymptotics, valid A >= ~10 (float64)."""
    A = np.asarray(A, dtype=np.float64)
    out = -2.0 * np.sqrt(A) + 0.5 / np.sqrt(A)
    out += (1.0 / 24.0) * A ** -1.5                       # B2/2! * (1/2)
    out += -(1.875 / 720.0) * A ** -3.5                   # B4/4! * (1/2)(3/2)(5/2)
    out += (29.53125 / 30240.0) * A ** -5.5               # B6/6! * poch(1/2,5)
    out += -(1055.7421875 / 1209600.0) * A ** -7.5        # B8/8! * poch(1/2,7)
    return out

def boundary_bX(X, kmin=12):
    """b_X(q) for q=2..M as float64 array bfull with bfull[q]=b_X(q), len M+2 (b[M+1]=0)."""
    M = (X + 1) // 2
    q = np.arange(2, M + 1, dtype=np.int64)
    c = 2 * q - 1
    # explicit k range: K_q = max(kmin, ceil((X+1)/(2q))) so that a_k>X for k>K_q
    Kq = np.maximum(kmin, -((X + 1) // (-2 * q)))
    b = np.zeros(M - 1)
    # chunk over q to bound memory
    CH = 200_000
    for s in range(0, len(q), CH):
        qs = q[s:s + CH].astype(np.float64)
        cs = c[s:s + CH].astype(np.float64)
        Ks = Kq[s:s + CH]
        reps = Ks.astype(np.int64)
        qq = np.repeat(qs, reps)
        cc = np.repeat(cs, reps)
        # k index within each block
        kk = np.arange(1, reps.max() + 1)
        # build k values per pair
        idx = np.repeat(np.cumsum(reps) - reps, reps)
        kvals = (np.arange(reps.sum()) - idx + 1).astype(np.float64)
        a = 2.0 * kvals * qq - 1.0
        d = (2.0 * kvals + 1.0) * qq
        term = np.log(np.minimum(a, X) / cc) / np.sqrt(a) - np.log(np.minimum(d, X) / cc) / np.sqrt(d)
        segsum = np.add.reduceat(term, np.cumsum(reps) - reps)
        # analytic tail: k>K_q, all args > X:
        # tail = log(X/c) * (2q)^{-1/2} [zeta(1/2, K+1-1/(2q)) - zeta(1/2, K+3/2)]
        Kf = Ks.astype(np.float64)
        tail = np.log(X / cs) / np.sqrt(2.0 * qs) * (
            zeta_half(Kf + 1.0 - 1.0 / (2.0 * qs)) - zeta_half(Kf + 1.5))
        b[s:s + CH] = segsum + tail
    bfull = np.zeros(M + 2)
    bfull[2:M + 1] = b
    return bfull, M

def T_op(bfull, M):
    """(T_M b)(q) for q=2..Mn, Mn=floor((M+1)/2). bfull indexed 0..M+1, zero beyond M."""
    Mn = (M + 1) // 2
    out = np.zeros(Mn + 2)
    n = np.arange(0, M + 2)
    kmax = (M + 1) // 4 + 1
    for k in range(1, kmax + 1):
        qa = min(Mn, (M + 1) // (2 * k))          # 2kq-1 <= M
        qd = min(Mn, M // (2 * k + 1))            # (2k+1)q <= M
        if qa >= 2:
            qs = np.arange(2, qa + 1)
            out[2:qa + 1] += bfull[2 * k * qs - 1]
        if qd >= 2:
            qs = np.arange(2, qd + 1)
            out[2:qd + 1] -= bfull[(2 * k + 1) * qs]
        if qa < 2 and qd < 2:
            break
    return out, Mn

def debt_V(bfull, M):
    n = np.arange(2, M + 1)
    return float(np.sum(np.sqrt(n) * np.abs(bfull[2:M + 1] - bfull[3:M + 2])))

def chain(X, min_M=8):
    bfull, M = boundary_bX(X)
    res = []
    g = 1
    while M >= min_M:
        res.append((g, M, debt_V(bfull, M), float(np.max(np.abs(bfull)))))
        bfull, M = T_op(bfull, M)
        g += 1
    return res

if __name__ == "__main__":
    import sys, time
    for X in [int(a) for a in sys.argv[1:]]:
        t0 = time.time()
        rows = chain(X)
        print(f"X={X}  ({time.time()-t0:.1f}s)")
        for g, M, V, supb in rows:
            print(f"  g={g:2d}  M={M:7d}  V={V:.9f}  sup|b|={supb:.6f}")
