#!/usr/bin/env python3
"""Large-scale scan of square-root hinge carry-inverse coefficients.

System: h_T(q) = sum_{n=q}^T c_T(n) beta_{nq}, beta_{nq}=floor(n/q)(q-1-(n mod q))/(n+1)
        h_T(q) = q^{-1/2} - T^{-1/2}   (T-32301.1, D-23801.1/.5)

Exact validated closed forms (see sqhinge_lib validation):
  u_m(T) = m^{-1/2} S(floor(T/m)) - T^{-1/2} M(floor(T/m)),
      S(x)=sum_{k<=x} mu(k)/sqrt(k),  M(x)=Mertens
  Fixed row:  c_T(j) = [ sum_{d=1}^{j+1} f_j(d) u_d(T) + 2(1 - T^{-1/2}) ] / (j(j-1))
  Full row:   c_T(j) = ((j+1)[j u_j - (j-2) u_{j+1}] + 2 sum_{m=j+2}^T u_m) / (j(j-1))
"""
import numpy as np
import json, sys, time

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000_000
OUT = "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/sqhinge_results"
import os
os.makedirs(OUT, exist_ok=True)
t0 = time.time()

def log(*a):
    print(f"[{time.time()-t0:8.1f}s]", *a, flush=True)

# ---------- Mobius sieve (numpy) ----------
def mobius_numpy(N):
    mu = np.ones(N + 1, dtype=np.int8)
    rem = np.arange(N + 1, dtype=np.int32 if N < 2**31 else np.int64)
    lim = int(N ** 0.5)
    # primes up to sqrt(N)
    sieve = np.ones(lim + 1, dtype=bool); sieve[:2] = False
    for p in range(2, int(lim ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    primes = np.nonzero(sieve)[0]
    for p in primes:
        mu[p::p] *= -1
        rem[p::p] //= p
        pp = p * p
        mu[pp::pp] = 0
    big = rem > 1
    mu[big] *= -1
    mu[0] = 0
    return mu

log("sieving mobius to", NMAX)
mu = mobius_numpy(NMAX)
log("mobius done. spot:", mu[1], mu[2], mu[4], mu[6], mu[30])

# validation vs reference sieve
sys.path.insert(0, os.path.dirname(OUT))
from sqhinge_lib import mobius_sieve as mob_ref
vn = min(NMAX, 100000)
ref = np.array(mob_ref(vn), dtype=np.int8)
assert np.array_equal(mu[:vn + 1], ref), "numpy mobius sieve mismatch"
log("numpy mobius validated to", vn)

# ---------- cumulative S (mu(k)/sqrt k) and M (Mertens) ----------
log("building S, M cumulatives")
S = np.empty(NMAX + 1, dtype=np.float64)
S[0] = 0.0
CH = 10_000_000
acc = 0.0
for lo in range(1, NMAX + 1, CH):
    hi = min(lo + CH, NMAX + 1)
    k = np.arange(lo, hi, dtype=np.float64)
    blk = mu[lo:hi].astype(np.float64) / np.sqrt(k)
    np.cumsum(blk, out=blk)
    blk += acc
    S[lo:hi] = blk
    acc = blk[-1]
del blk, k
M = np.empty(NMAX + 1, dtype=np.int32)
M[0] = 0
np.cumsum(mu[1:], dtype=np.int32, out=M[1:])
log("S,M done.  S(N)=%.6f  M(N)=%d  (1/zeta(1/2)=-0.684766)" % (S[NMAX], M[NMAX]))

def f_coeff(j, d):
    if d <= j - 1:
        return -2.0
    if d == j:
        return float((j + 2) * (j - 1))
    return float(-j * (j - 1))

# ---------- Phase A: fixed rows j=2..8 for ALL T in [3, NMAX] ----------
ROWS = [2, 3, 4, 5, 6, 7, 8]
stats = {j: {"min": np.inf, "argmin": None, "neg_count": 0, "first_neg": None,
             "min_early": np.inf, "argmin_early": None} for j in ROWS}
checkpoints = {}
cp_Ts = sorted(set(int(round(10 ** e)) for e in np.arange(1, 8.001, 0.25)) | {NMAX})
log("phase A: fixed rows", ROWS)
CHT = 5_000_000
for lo in range(3, NMAX + 1, CHT):
    hi = min(lo + CHT, NMAX + 1)
    T = np.arange(lo, hi, dtype=np.int64)
    invsqT = 1.0 / np.sqrt(T.astype(np.float64))
    Sd = {}
    Md = {}
    for d in range(1, 10):
        idx = T // d
        Sd[d] = S[idx]
        Md[d] = M[idx]
    for j in ROWS:
        tot = np.full(T.shape, 2.0)  # +2*1 from column-1 correction
        tot -= 2.0 * invsqT
        fsumM = 0.0
        for d in range(1, j + 2):
            f = f_coeff(j, d)
            tot += (f / np.sqrt(d)) * Sd[d]
            fsumM += 0.0  # placeholder
            tot -= f * invsqT * Md[d]
        c = tot / (j * (j - 1))
        # T must be >= j for row j to exist in the system; mask smaller T
        valid = T >= j
        cv = np.where(valid, c, np.inf)
        i = int(np.argmin(cv))
        if cv[i] < stats[j]["min"]:
            stats[j]["min"] = float(cv[i]); stats[j]["argmin"] = int(T[i])
        neg = (cv < 0)
        nn = int(neg.sum())
        if nn:
            stats[j]["neg_count"] += nn
            if stats[j]["first_neg"] is None:
                stats[j]["first_neg"] = int(T[np.argmax(neg)])
    for Tc in cp_Ts:
        if lo <= Tc < hi:
            row = {}
            for j in ROWS:
                if Tc < j: continue
                tot = 2.0 * (1.0 - 1.0 / np.sqrt(Tc))
                for d in range(1, j + 2):
                    f = f_coeff(j, d)
                    tot += f * (S[Tc // d] / np.sqrt(d) - M[Tc // d] / np.sqrt(Tc))
                row[j] = tot / (j * (j - 1))
            checkpoints[Tc] = row
    if (lo - 3) % (20 * CHT) == 0:
        log("  phase A progress T=", lo)
log("phase A done")
for j in ROWS:
    s = stats[j]
    log(f"row {j}: min={s['min']:.6e} at T={s['argmin']}  neg_count={s['neg_count']} first_neg={s['first_neg']}")
with open(f"{OUT}/fixed_rows.json", "w") as f:
    json.dump({"stats": {str(k): v for k, v in stats.items()},
               "checkpoints": {str(k): {str(j): v for j, v in r.items()} for k, r in checkpoints.items()}}, f, indent=1)

# ---------- Phase B: full vectors for selected endpoints ----------
def full_vector_stats(Tend):
    m = np.arange(1, Tend + 1, dtype=np.int64)
    idx = Tend // m
    u = S[idx] / np.sqrt(m.astype(np.float64)) - M[idx] / np.sqrt(float(Tend))
    # tail[m] = sum_{k=m}^{T} u_k ; build suffix sum
    tail = np.cumsum(u[::-1])[::-1]
    # c_j for j=2..Tend ; u array index offset: u[0] is m=1
    j = np.arange(2, Tend + 1, dtype=np.int64)
    uj = u[j - 1]
    uj1 = np.zeros_like(uj)
    uj1[:-1] = u[j[:-1]]  # u_{j+1} for j<=T-1
    tl = np.zeros_like(uj)
    tl[: max(0, Tend - 3)] = tail[j[: max(0, Tend - 3)] + 1]  # tail_{j+2} exists for j+2<=T
    jf = j.astype(np.float64)
    c = ((jf + 1) * (jf * uj - (jf - 2) * uj1) + 2.0 * tl) / (jf * (jf - 1))
    # stats over 2<=j<=T-1 (c_T(T)=0 exactly)
    cc = c[:-1]
    jj = j[:-1]
    i = int(np.argmin(cc))
    res = {"T": Tend, "min": float(cc[i]), "argmin": int(jj[i]),
           "neg": int((cc < 0).sum()), "cT": float(c[-1])}
    # interior minima
    for name, cap in (("half", Tend // 2), ("sqrt", int(Tend ** 0.5) + 1)):
        mask = jj <= cap
        if mask.any():
            ci = cc[mask]
            ii = int(np.argmin(ci))
            res[f"min_{name}"] = float(ci[ii])
            res[f"argmin_{name}"] = int(jj[mask][ii])
    if res["neg"]:
        negj = jj[cc < 0]
        res["neg_js"] = negj[:20].tolist()
    return res

log("phase B: full vectors, all T in [3,20000]")
worst = None
bstats = []
neg_endpoints = []
for Tend in range(3, min(20000, NMAX) + 1):
    r = full_vector_stats(Tend)
    if r["neg"]:
        neg_endpoints.append(r)
    if worst is None or r["min"] < worst["min"]:
        worst = r
    if Tend % 2000 == 0:
        log("  B progress", Tend, "worst so far:", worst["min"], "at T=", worst["T"], "j=", worst["argmin"])
log("dense sweep done. negatives:", len(neg_endpoints))

log("phase B2: log-spaced large endpoints")
bigTs = sorted(set(t for t in (int(round(10 ** e)) for e in np.arange(4.3, 8.0001, 0.1)) if t <= NMAX))
for Tend in bigTs:
    r = full_vector_stats(Tend)
    bstats.append(r)
    log("  T=%d  min=%.4e at j=%d  neg=%d  min_half=%.4e@%d  min_sqrt=%.4e@%d  c(T)=%.1e" %
        (Tend, r["min"], r["argmin"], r["neg"], r.get("min_half", 0), r.get("argmin_half", -1),
         r.get("min_sqrt", 0), r.get("argmin_sqrt", -1), r["cT"]))
    if r["neg"]:
        neg_endpoints.append(r)

with open(f"{OUT}/full_vectors.json", "w") as f:
    json.dump({"dense_worst": worst, "neg_endpoints": neg_endpoints[:200], "big": bstats}, f, indent=1)
log("ALL DONE")
