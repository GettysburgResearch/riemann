# Our own re-implementation of the Lu-Zaman-Zhao computational predicate (arXiv:2602.03626v2, (2.5)):
#   for a fundamental discriminant d with q=|d| and c=1/5, find N with
#   sum_{p<=N} [ log p/(p^s-1) + chi_d(p) log p/(p^s-chi_d(p)) ]  >  c/(r(r log q + c)) + (r + c/log q)/R^2 + phi log q + E,
#   s = 1+r, r = lambda/log(1e10), R = r+7/8, (lambda, phi, E) from LZZ Table 1.
# Floating point (float64) with an explicit safety margin; NOT certified. Conditional on LZZ Theorem 2.1.
import sys, math, json, time
import numpy as np

ROWS = [(1.6, 0.22675, 1.1614, 60_000), (1.3, 0.23083, 1.1805, 5_000_000),
        (1.2, 0.23222, 1.1870, 50_000_000), (1.1, 0.23362, 1.1936, 130_000_000)]
C = 0.2
LOG1E10 = math.log(1e10)
SAFETY = 1e-6   # required excess over RHS; float64 summation error is far below this

def base_primes(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)

def prime_chunks(limit, seg=20_000_000):
    """Yield arrays of all primes <= limit, in increasing order, segment by segment."""
    bp = base_primes(int(math.isqrt(limit)) + 1)
    lo = 0
    while lo <= limit:
        hi = min(lo + seg, limit + 1)
        s = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            s[:2] = False
        for p in bp:
            if p * p >= hi: break
            start = max(p * p, ((lo + p - 1) // p) * p)
            s[start - lo::p] = False
        yield (np.nonzero(s)[0] + lo).astype(np.int64)
        lo = hi

def kron(d, p):
    """Kronecker symbol (d/p) for an int d and an int64 array of primes p (vectorized)."""
    out = np.zeros(p.shape, dtype=np.int64)
    two = p == 2
    if two.any():
        if d % 2 == 0:
            out[two] = 0
        else:
            out[two] = 1 if d % 8 in (1, 7) else -1
    odd = ~two
    po = p[odd]
    a = np.mod(d, po).astype(np.int64)
    e = (po - 1) // 2
    res = np.ones_like(po)
    b = a.copy()
    while True:
        m = (e & 1) == 1
        if m.any():
            res[m] = (res[m] * b[m]) % po[m]
        e >>= 1
        if not e.any(): break
        b = (b * b) % po
    v = np.where(a == 0, 0, np.where(res == 1, 1, -1))
    out[odd] = v
    return out

# cache primes so that repeated runs do not resieve
_PR = {}
def primes_upto_count(n):
    if n in _PR: return _PR[n]
    est = int(n * (math.log(n) + math.log(math.log(n)) + 2)) + 1000 if n > 10 else 100
    acc = []
    tot = 0
    for ch in prime_chunks(est):
        acc.append(ch); tot += len(ch)
        if tot >= n: break
    arr = np.concatenate(acc)[:n]
    assert len(arr) == n
    _PR[n] = arr
    return arr

def rhs(q, lam, phi, E):
    r = lam / LOG1E10
    R = r + 0.875
    L = math.log(q)
    return C / (r * (r * L + C)) + (r + C / L) / R ** 2 + phi * L + E

def test_d(d, rows=ROWS, chunk=5_000_000):
    q = abs(d)
    for lam, phi, E, N0 in rows:
        r = lam / LOG1E10
        s = 1.0 + r
        target = rhs(q, lam, phi, E) + SAFETY
        P = primes_upto_count(N0)
        acc = 0.0
        for i0 in range(0, N0, chunk):
            p = P[i0:i0 + chunk]
            chi = kron(d, p)
            lp = np.log(p.astype(np.float64))
            ps = np.exp(s * lp)
            term = lp / (ps - 1.0) + chi * lp / (ps - chi)
            cs = acc + np.cumsum(term)
            hit = np.nonzero(cs > target)[0]
            if hit.size:
                j = int(hit[0])
                return {"d": d, "row": lam, "n_primes": i0 + j + 1, "p": int(p[j]), "excess": float(cs[j] - target + SAFETY)}
            acc = float(cs[-1])
        last = {"d": d, "row": lam, "fail_at_N0": N0, "lhs": acc, "rhs": target - SAFETY}
    return last
