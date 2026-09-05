#!/usr/bin/env python3
"""CBVR uniformity scan for PR 316 (branch research/gpt56-pro-309-coupled-boundary-variation).

Exact definitions implemented (quoted from the branch):

L-30901.3/.4 (paired representation of the first activated boundary):
    Psi_X(x,c) = x^{-1/2} log(min(x,X)/c)
    b_X(q) = sum_{k>=1} [ Psi_X(2kq-1, 2q-1) - Psi_X((2k+1)q, 2q-1) ]
  equivalently (L-30901.2):
    b_X(q) = log(X/(2q-1)) * Cp(q) - C w_X(q),  M = floor((X+1)/2), b_X(M+1)=0.

L-30901.16 (debt / weighted first-difference variation norm):
    V_X(b) = sum_{n=2}^{M} sqrt(n) |b(n) - b(n+1)|      (with b(M+1)=0)

L-30901.18 (residual operator exporting the next activated boundary):
    (T_M b)(q) = sum_{k>=1} [ b(2kq-1) - b((2k+1)q) ]   with zero extension beyond M.

L-30501.15/L-30403 (atomic divisor-source norm):
    b_X(q) = sum_{m<=M, q|m} sigma_X(m);   ||sigma||_at = sum_m sqrt(m)|sigma(m)|.
"""
import numpy as np

SQ2 = np.sqrt(2.0)


def _em_tail(K, eps):
    """sum_{k>=K} [(k-eps)^{-1/2} - (k+1/2)^{-1/2}] via Euler-Maclaurin.

    K, eps arrays (K >= 8 or so). f(t) = (t-eps)^{-1/2} - (t+1/2)^{-1/2}.
    sum_{k=K}^inf f(k) = int_K^inf f + f(K)/2 - f'(K)/12 + f'''(K)/720 - f^(5)(K)/30240
    int_K^inf f = 2[(K+1/2)^{1/2} - (K-eps)^{1/2}]
    """
    a = K - eps
    b = K + 0.5
    ra = 1.0 / np.sqrt(a)
    rb = 1.0 / np.sqrt(b)
    integral = 2.0 * (np.sqrt(b) - np.sqrt(a))
    f0 = ra - rb
    f1 = -0.5 * (ra / a - rb / b)                      # f'
    f3 = -(15.0 / 8.0) * (ra / a**3 - rb / b**3)       # f'''
    f5 = -(945.0 / 32.0) * (ra / a**5 - rb / b**5)     # f^(5)
    return integral + 0.5 * f0 - f1 / 12.0 + f3 / 720.0 - f5 / 30240.0


def first_boundary(X):
    """b_X(n) for integer n in [2, M], per L-30901.4. Returns array b of len M+2,
    b[0]=b[1]=0 unused, b[M+1]=0."""
    M = (X + 1) // 2
    b = np.zeros(M + 2)
    q_all = np.arange(2, M + 1)
    logX = np.log(float(X))

    Q0 = min(M, 1024)
    # Part A: per-q loop, vectorized over k
    for q in range(2, Q0 + 1):
        Kexp = max((X + 1) // (2 * q) + 2, 32)
        k = np.arange(1, Kexp + 1, dtype=np.float64)
        c = 2.0 * q - 1.0
        aa = 2.0 * k * q - 1.0
        dd = (2.0 * k + 1.0) * q
        lc = np.log(c)
        term = (np.log(np.minimum(aa, X)) - lc) / np.sqrt(aa) \
             - (np.log(np.minimum(dd, X)) - lc) / np.sqrt(dd)
        b[q] = term.sum()

    # Part B: q in (Q0, M], per-k loop vectorized over q
    if M > Q0:
        qv = np.arange(Q0 + 1, M + 1, dtype=np.float64)
        cv = 2.0 * qv - 1.0
        lcv = np.log(cv)
        acc = np.zeros(len(qv))
        KmaxB = max((X + 1) // (2 * (Q0 + 1)) + 2, 32)
        for k in range(1, KmaxB + 1):
            if k <= 32:
                sl = slice(0, len(qv))
            else:
                qhi = (X + 1) // (2 * (k - 2))
                if qhi <= Q0:
                    break
                sl = slice(0, min(len(qv), qhi - Q0))
            qs = qv[sl]
            aa = 2.0 * k * qs - 1.0
            dd = (2.0 * k + 1.0) * qs
            acc[sl] += (np.log(np.minimum(aa, X)) - lcv[sl]) / np.sqrt(aa) \
                     - (np.log(np.minimum(dd, X)) - lcv[sl]) / np.sqrt(dd)
        b[Q0 + 1: M + 1] = acc

    # Analytic tail (all arguments > X): L * (2q)^{-1/2} * EM(K, 1/(2q))
    qf = q_all.astype(np.float64)
    Kexp_v = np.maximum((X + 1) // (2 * q_all) + 2, 32).astype(np.float64)
    K = Kexp_v + 1.0
    eps = 1.0 / (2.0 * qf)
    L = logX - np.log(2.0 * qf - 1.0)
    tail = L / np.sqrt(2.0 * qf) * _em_tail(K, eps)
    b[2: M + 1] += tail
    return b, M


def apply_T(b, M):
    """(T_M b)(q) = sum_k [b(2kq-1) - b((2k+1)q)], zero extension beyond M.
    b is array with b[m] valid for 2<=m<=M (and b[m]=0 tolerated elsewhere).
    Support of output: q <= M2 = floor((M+1)/2). Returns (b2 array len M2+2, M2)."""
    M2 = (M + 1) // 2
    out = np.zeros(M2 + 2)

    def bval(m):
        m = np.asarray(m)
        v = np.where((m >= 2) & (m <= M), b[np.clip(m, 0, M)], 0.0)
        return v

    Q0 = min(M2, 512)
    for q in range(2, Q0 + 1):
        kmax = (M + 1) // (2 * q) + 1
        k = np.arange(1, kmax + 1)
        out[q] = bval(2 * k * q - 1).sum() - bval((2 * k + 1) * q).sum()
    if M2 > Q0:
        qv = np.arange(Q0 + 1, M2 + 1)
        acc = np.zeros(len(qv))
        kmaxB = (M + 1) // (2 * (Q0 + 1)) + 1
        for k in range(1, kmaxB + 1):
            qhi = (M + 1) // (2 * k) + 1  # beyond this both args > M
            sl = slice(0, min(len(qv), max(0, qhi - Q0)))
            if sl.stop == 0:
                break
            qs = qv[sl]
            acc[sl] += bval(2 * k * qs - 1) - bval((2 * k + 1) * qs)
        out[Q0 + 1: M2 + 1] = acc
    return out, M2


def debt_norms(b, M):
    """V = sum_{n=2}^{M} sqrt(n)|b(n)-b(n+1)| with b(M+1)=0 (L-30901.16),
    and Npos = 2 * sum sqrt(n) [b(n+1)-b(n)]_+ (negative-capacity debt bound)."""
    n = np.arange(2, M + 1)
    d = b[2: M + 1] - b[3: M + 2]  # b[M+1] is 0
    w = np.sqrt(n)
    V = np.sum(w * np.abs(d))
    Npos = 2.0 * np.sum(w * np.maximum(-d, 0.0))
    return V, Npos


def atomic_norm(b, M):
    """sigma from b(q) = sum_{m<=M, q|m} sigma(m) via Moebius inversion over
    multiples: sigma(m) = sum_{j<=M, m|j} mu(j/m) b(j). Returns sum sqrt(m)|sigma(m)|."""
    # sieve mu up to M
    mu = np.ones(M + 1, dtype=np.int64)
    primes_mask = np.ones(M + 1, dtype=bool)
    primes_mask[:2] = False
    for p in range(2, int(M**0.5) + 1):
        if primes_mask[p]:
            primes_mask[p * p:: p] = False
    primes = np.nonzero(primes_mask)[0]
    for p in primes:
        mu[p:: p] *= -1
        p2 = p * p
        if p2 <= M:
            mu[p2:: p2] = 0
    total = 0.0
    for m in range(2, M + 1):
        j = np.arange(m, M + 1, m)
        s = np.sum(mu[j // m] * b[j])
        total += np.sqrt(m) * abs(s)
    return total
