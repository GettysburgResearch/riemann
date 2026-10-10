#!/usr/bin/env python3
"""Fixed rows j=2..JMAX for ALL T in [j+1, NMAX], vector over T.

c_T(j) = [ -2*U(j) + (j+2)(j-1) u_j - j(j-1) u_{j+1} + 2(1 - T^{-1/2}) ] / (j(j-1))
with U(j) = sum_{d=1}^{j-1} u_d,  u_d = d^{-1/2} S(floor(T/d)) - T^{-1/2} M(floor(T/d)).
Also records, per row, min over T > j (excluding the trivial diagonal zero T=j).
"""
import numpy as np, json, sys, time, os

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000_000
JMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 64
OUT = "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/sqhinge_results"
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:8.1f}s]", *a, flush=True)

def mobius_numpy(N):
    mu = np.ones(N + 1, dtype=np.int8)
    rem = np.arange(N + 1, dtype=np.int32 if N < 2**31 else np.int64)
    lim = int(N ** 0.5)
    sieve = np.ones(lim + 1, dtype=bool); sieve[:2] = False
    for p in range(2, int(lim ** 0.5) + 1):
        if sieve[p]: sieve[p*p::p] = False
    for p in np.nonzero(sieve)[0]:
        mu[p::p] *= -1
        rem[p::p] //= p
        mu[p*p::p*p] = 0
    mu[rem > 1] *= -1
    mu[0] = 0
    return mu

log("sieve to", NMAX)
mu = mobius_numpy(NMAX)
S = np.empty(NMAX + 1, dtype=np.float64); S[0] = 0.0
CH = 10_000_000; acc = 0.0
for lo in range(1, NMAX + 1, CH):
    hi = min(lo + CH, NMAX + 1)
    k = np.arange(lo, hi, dtype=np.float64)
    blk = mu[lo:hi].astype(np.float64) / np.sqrt(k)
    np.cumsum(blk, out=blk); blk += acc
    S[lo:hi] = blk; acc = blk[-1]
M = np.empty(NMAX + 1, dtype=np.int32); M[0] = 0
np.cumsum(mu[1:], dtype=np.int32, out=M[1:])
del mu
log("S,M ready. S(N)=%.6f M(N)=%d" % (S[NMAX], M[NMAX]))

rows = list(range(2, JMAX + 1))
res = {j: [np.inf, None] for j in rows}   # min over T>j, argmin
negs = {j: [] for j in rows}              # (T, value) first few
invsqd = 1.0 / np.sqrt(np.arange(1, JMAX + 3, dtype=np.float64))

CHT = 10_000_000
for lo in range(3, NMAX + 1, CHT):
    hi = min(lo + CHT, NMAX + 1)
    T = np.arange(lo, hi, dtype=np.int64)
    invsqT = 1.0 / np.sqrt(T.astype(np.float64))
    base = 2.0 * (1.0 - invsqT)
    U = S[T] - M[T] * invsqT       # = u_1 = prefix sum for j=2 (d<=j-1=1)
    idx2 = T // 2
    u_cur = S[idx2] * invsqd[1] - M[idx2] * invsqT  # u_2
    for j in rows:
        # need u_{j+1}
        d = j + 1
        idx = T // d
        u_next = S[idx] * invsqd[d - 1] - M[idx] * invsqT
        num = -2.0 * U + float((j + 2) * (j - 1)) * u_cur - float(j * (j - 1)) * u_next + base
        c = num / float(j * (j - 1))
        valid = T > j
        cv = np.where(valid, c, np.inf)
        i = int(np.argmin(cv))
        if cv[i] < res[j][0]:
            res[j][0] = float(cv[i]); res[j][1] = int(T[i])
        if cv[i] < 0:
            neg_idx = np.nonzero(cv < 0)[0]
            for t in neg_idx[:5]:
                negs[j].append((int(T[t]), float(cv[t])))
        # U is sum_{d<=j-1}; for next row j+1 need sum_{d<=j}
        U = U + u_cur
        u_cur = u_next
    log("chunk", lo, "done")

out = {str(j): {"min": res[j][0], "argmin": res[j][1], "negs": negs[j][:10],
                "neg_total": len(negs[j])} for j in rows}
with open(f"{OUT}/rows64.json", "w") as f:
    json.dump(out, f, indent=1)
for j in rows:
    if negs[j] or j <= 12 or j % 8 == 0:
        log(f"row {j}: min={res[j][0]:.6e} at T={res[j][1]}  negs={len(negs[j])}" +
            (f" first={negs[j][0]}" if negs[j] else ""))
log("DONE")
