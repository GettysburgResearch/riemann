#!/usr/bin/env python3
"""U3 adjudication, independent pass: a second, independently written implementation of the
Lu-Zaman-Zhao test (2.5) (arXiv:2602.03626, Thm 2.1 + Table 1, c = 1/5), used ONLY to cross-check the
per-discriminant prime counts reported by the first adjudication pass (adj_U3_predicate_*.out).

Written separately from the first pass (no shared code): own segmented sieve, chi_d(p) by Euler's
criterion d^((p-1)/2) mod p (vectorised int64 modular exponentiation; the first pass also uses Euler's
criterion, so adj_U3_indep_chi_check.py checks it against a Jacobi-reciprocity routine), long-double
running sums. [Docstring corrected after the run; the code is byte-identical to the run copy.]
NOT certified: float64 terms / long double accumulation, no directed rounding. Conditional on LZZ Thm 2.1.

Test for row (lam, phi, E), r = lam/log(1e10), sigma = 1 + r, R = r + 7/8, q = |d|, c = 1/5:
  LHS(N) = sum_{p <= p_N} [ log p/(p^sigma - 1) + chi(p) log p/(p^sigma - chi(p)) ]
  RHS    = c/(r(r log q + c)) + (r + c/log q)/R^2 + phi log q + E
We report, per row, n_strict = least N with LHS(N) > RHS and n_margin = least N with LHS(N) >= RHS + 1e-6,
within LZZ's caps 6e4, 5e6, 5e7, 1.3e8 primes. Rows are tried in order, as in LZZ's four passes.
Usage: python3 -I adj_U3_indep_lzz_crosscheck.py OUT.json d1 d2 ...
"""
import sys, json, time, math
import numpy as np
import mpmath as mp

ROWS = [(1.6, 0.22675, 1.1614, 60_000), (1.3, 0.23083, 1.1805, 5_000_000),
        (1.2, 0.23222, 1.1870, 50_000_000), (1.1, 0.23362, 1.1936, 130_000_000)]
SEG = 50_000_000
MARGIN = 1e-6


def base_primes(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]


BP = base_primes(50_000)  # enough for limits up to 2.5e9


def primes_segments(seg=SEG):
    lo = 0
    while True:
        hi = lo + seg
        s = np.ones(seg, dtype=bool)
        if lo == 0:
            s[:2] = False
        for p in BP:
            p = int(p)
            if p * p >= hi:
                break
            start = max(p * p, ((lo + p - 1) // p) * p)
            s[start - lo::p] = False
        yield lo + np.nonzero(s)[0].astype(np.int64)
        lo = hi


def chi_vec(d, p):
    """chi_d(p) for a vector of primes p (int64), via Euler's criterion; p=2 by d mod 8."""
    out = np.empty(p.shape, dtype=np.int64)
    odd = p != 2
    po = p[odd]
    a = np.mod(np.int64(d), po)          # in [0, p)
    e = (po - 1) // 2
    res = np.ones_like(po)
    base = a.copy()
    while np.any(e > 0):
        m = (e & 1) == 1
        res = np.where(m, (res * base) % po, res)   # products < p^2 < 2^63 for p < 3.03e9
        base = (base * base) % po
        e >>= 1
    v = np.where(a == 0, 0, np.where(res == 1, 1, -1))
    out[odd] = v
    if np.any(~odd):
        if d % 2 == 0:
            out[~odd] = 0
        else:
            out[~odd] = 1 if d % 8 in (1, 7) else -1
    return out


def rhs(q, lam, phi, E, c=mp.mpf(1) / 5):
    mp.mp.dps = 40
    r = mp.mpf(lam) / mp.log(mp.mpf(10) ** 10)
    R = r + mp.mpf(7) / 8
    L = mp.log(q)
    return float(c / (r * (r * L + c)) + (r + c / L) / R ** 2 + mp.mpf(str(phi)) * L + mp.mpf(str(E)))


def run_row(d, lam, phi, E, cap):
    q = abs(d)
    r = lam / math.log(1e10)
    sig = 1.0 + r
    R0 = rhs(q, lam, phi, E)
    tot = np.longdouble(0)
    count = 0
    n_strict = n_margin = None
    p_margin = None
    for P in primes_segments():
        if count + len(P) > cap:
            P = P[:cap - count]
        if len(P) == 0:
            break
        chi = chi_vec(d, P)
        lp = np.log(P.astype(np.float64))
        ps = np.exp(sig * lp)
        t = lp / (ps - 1.0) + chi * lp / (ps - chi)
        cs = tot + np.cumsum(t.astype(np.longdouble))
        if n_strict is None:
            idx = np.nonzero(cs > R0)[0]
            if len(idx):
                n_strict = count + int(idx[0]) + 1
        idx = np.nonzero(cs >= R0 + MARGIN)[0]
        if len(idx):
            n_margin = count + int(idx[0]) + 1
            p_margin = int(P[idx[0]])
            break
        tot = cs[-1]
        count += len(P)
        if count >= cap:
            break
    return {"lam": lam, "rhs": R0, "n_strict": n_strict, "n_margin": n_margin, "p_margin": p_margin}


if __name__ == "__main__":
    out = sys.argv[1]
    ds = [int(x) for x in sys.argv[2:]]
    # self-checks of chi_vec against a direct Legendre computation
    P = np.array([2, 3, 5, 7, 11, 13, 101, 7919, 104729, 2147483647, 2147483629, 3000000019], dtype=np.int64)
    for d in (-3, -4, 5, 8, -8, 12, -2999, 9447241877, -433572483, -31508468):
        got = chi_vec(d, P)
        for pp, g in zip(P.tolist(), got.tolist()):
            if pp == 2:
                ref = 0 if d % 2 == 0 else (1 if d % 8 in (1, 7) else -1)
            elif d % pp == 0:
                ref = 0
            else:
                ref = 1 if pow(d % pp, (pp - 1) // 2, pp) == 1 else -1
            assert g == ref, (d, pp, g, ref)
    # sieve self-check
    first = next(primes_segments(10**6))
    assert len(first) == 78498 and first[-1] == 999983
    res = []
    for d in ds:
        t0 = time.time()
        rows = []
        for lam, phi, E, cap in ROWS:
            rr = run_row(d, lam, phi, E, cap)
            rows.append(rr)
            if rr["n_margin"] is not None:
                break
        rec = {"d": d, "rows": rows, "sec": round(time.time() - t0, 1)}
        res.append(rec)
        last = rows[-1]
        print(f"d={d}: row lam={last['lam']} n_strict={last['n_strict']} n_margin={last['n_margin']} "
              f"p={last['p_margin']} ({rec['sec']}s); earlier rows failed: {[r['lam'] for r in rows[:-1]]}",
              flush=True)
        json.dump(res, open(out, "w"), indent=1)
