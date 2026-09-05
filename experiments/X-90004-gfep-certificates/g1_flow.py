"""PRONG G1: flow/cut formalization of GFEP. Core toolkit.
Sigma_{X,n}(p) via forward first-entrance pass; harmonic pixels H_p^{(n)}(m) via
backward recursion; cross-checks against T-90005 certified values."""
import sys, math
import numpy as np
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r


def children(m):
    a2 = m // 2; b2 = m - a2; a3 = (m + 2) // 3; b3 = m - a3
    return (a2, b2, a3, b3)


def sigma_all(X, n, S):
    """Sigma_{X,n}(p), p in [n, min(2n,X+1)). Forward pass, O(X). S[m]=m*R_X(m)."""
    up = min(2 * n, X + 1)
    sig = np.array(S[n:up], dtype=np.float64)  # window self-source E_n = delta
    if X >= 2 * n:
        far = np.zeros(X + 1)
        far[2 * n: X + 1] = S[2 * n: X + 1]
        for m in range(X, 2 * n - 1, -1):
            g = far[m] / (2.0 * m)
            if g == 0.0:
                continue
            for c in children(m):
                if c >= 2 * n:
                    far[c] += g * c
                elif c >= n:
                    sig[c - n] += g * c
                # c < n: leak (overshoot), contributes 0
    return sig


def pixel_H(X, n, p):
    """H_p^{(n)}(m) = E_n(m,p) for all m in [n,X]. Backward recursion, O(X)."""
    H = np.zeros(X + 1)
    H[p] = 1.0
    for m in range(2 * n, X + 1):
        acc = 0.0
        for c in children(m):
            if c >= n:
                acc += (c / (2.0 * m)) * H[c]
        H[m] = acc
    return H


def hitting_h(X, n):
    """h_n(m) = P_m(hit n), harmonic at every m > n, absorbing below n."""
    h = np.zeros(X + 1)
    h[n] = 1.0
    for m in range(n + 1, X + 1):
        acc = 0.0
        for c in children(m):
            if c >= n:
                acc += (c / (2.0 * m)) * h[c]
        h[m] = acc
    return h


if __name__ == "__main__":
    # --- cross-check 1: T-90005 certified band-2 minimum (1960,196,391), sqrt(X)Sigma=4.826247
    X = 1960; n = 196
    mu = mobius_sieve(X); r = critical_r(X, mu)
    S = np.zeros(X + 2); m = np.arange(2, X + 1); S[2:X + 1] = m * r[2:X + 1]
    sig = sigma_all(X, n, S)
    j = int(np.argmin(sig)); p = n + j
    print(f"[check1] X={X} n={n}: argmin p={p}, sqrt(X)*Sigma={math.sqrt(X)*sig[j]:.6f}  (expect 391, 4.826247)")

    # --- cross-check 2: pairing identity <S,H_p> == Sigma(p) for several pixels
    for pp in (n, n + 60, 391):
        H = pixel_H(X, n, pp)
        v = float(np.dot(S[n:X + 1], H[n:X + 1]))
        print(f"[check2] p={pp}: <S,H_p>={v:.12e}  Sigma(p)={sig[pp - n]:.12e}  diff={abs(v - sig[pp - n]):.2e}")

    # --- cross-check 3: strong-Markov conic decomposition nA(n) = sum_p Sigma(p) h_n(p)
    h = hitting_h(X, n)
    lhs = float(np.dot(S[n:X + 1], h[n:X + 1]))
    rhs = float(np.dot(sig, h[n:min(2 * n, X + 1)]))
    print(f"[check3] <S,h_n>={lhs:.12e}  sum_p Sigma*h_n={rhs:.12e}  diff={abs(lhs - rhs):.2e}")
