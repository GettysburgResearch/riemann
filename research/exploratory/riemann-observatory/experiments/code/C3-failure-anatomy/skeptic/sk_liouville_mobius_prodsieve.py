#!/usr/bin/env python3
"""Skeptic: independent exact segmented sieve for lambda(n), mu(n), n <= N, by the integer
'product of small prime powers' method (no logarithms, no floats in any decision):
  prod(n) = product of p^k || n over p <= sqrt(N); the cofactor n // prod(n) is 1 or a single prime > sqrt(N).
Outputs L, M records, Polya positive region, and a rigorous lower bound for T(x)=sum lam(n)/n using
floor for lam=+1 and ceil for lam=-1 terms (scale 2^56), i.e. 2^56*T(x) >= sum_{lam=1} floor(2^56/n) - sum_{lam=-1} ceil(2^56/n).
Usage: python3 sk_liouville_mobius_prodsieve.py N out.json"""
import sys, json, math, time
import numpy as np

def primes_upto(m):
    s = np.ones(m + 1, dtype=bool); s[:2] = False
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def main():
    N = int(sys.argv[1]); out = sys.argv[2]
    t0 = time.time()
    R = math.isqrt(N)
    P = [int(p) for p in primes_upto(R)]
    SEG = 1 << 22
    SC = np.int64(1) << np.int64(56)
    Lc = Mc = 0; Tl = 0
    rec = dict(firstpos=None, lastpos=None, npos=0, maxL=-10**9, argmaxL=None, maxM=-10**9, argmaxM=None,
               minM=10**9, argminM=None, minTlow=None, argminTlow=None)
    ratio = {200: (0.0, None, None), 10**4: (0.0, None, None)}
    chk = {}
    want = {10**k for k in range(1, 10)} | {200, 179919749, 456877618, 903087703, 906150256, 906150257,
            906180359, 906316571, 906488079, 906488080, N}
    lo = 1
    while lo <= N:
        hi = min(lo + SEG, N + 1); m = hi - lo
        n = np.arange(lo, hi, dtype=np.int64)
        prod = np.ones(m, dtype=np.int64)
        par = np.zeros(m, dtype=np.int8)     # parity of Omega restricted to small primes
        dpar = np.zeros(m, dtype=np.int8)    # parity of omega restricted to small primes
        sqf = np.ones(m, dtype=bool)
        for p in P:
            st = (-lo) % p
            if st >= m: continue
            dpar[st::p] ^= 1
            pk = p; k = 1
            while pk < hi:
                st = (-lo) % pk
                if st < m:
                    prod[st::pk] *= p
                    par[st::pk] ^= 1
                    if k == 2: sqf[st::pk] = False
                pk *= p; k += 1
        cof = n // prod
        assert np.all(n == cof * prod)
        big = cof > 1
        # a cofactor > 1 must exceed sqrt(N) (all small primes removed) and hence be prime (cof < N/ sqrt(N)... )
        assert np.all(cof[big] > R)
        lam = np.where((par ^ big.astype(np.int8)) == 1, -1, 1).astype(np.int64)
        mu = np.where(sqf, np.where((dpar ^ big.astype(np.int8)) == 1, -1, 1), 0).astype(np.int64)
        L = Lc + np.cumsum(lam); M = Mc + np.cumsum(mu)
        q = SC // n; r = SC % n
        lowterm = np.where(lam == 1, q, -(q + (r != 0)))
        TL = Tl + np.cumsum(lowterm)
        pos = (L > 0) & (n >= 2)
        if pos.any():
            idx = np.nonzero(pos)[0]
            if rec["firstpos"] is None: rec["firstpos"] = int(n[idx[0]])
            rec["lastpos"] = int(n[idx[-1]]); rec["npos"] += int(len(idx))
        i = int(np.argmax(L))
        if L[i] > rec["maxL"]: rec["maxL"], rec["argmaxL"] = int(L[i]), int(n[i])
        i = int(np.argmax(M))
        if M[i] > rec["maxM"]: rec["maxM"], rec["argmaxM"] = int(M[i]), int(n[i])
        i = int(np.argmin(M))
        if M[i] < rec["minM"]: rec["minM"], rec["argminM"] = int(M[i]), int(n[i])
        i = int(np.argmin(TL))
        if rec["minTlow"] is None or TL[i] < rec["minTlow"]: rec["minTlow"], rec["argminTlow"] = int(TL[i]), int(n[i])
        rr = np.abs(M) / np.sqrt(n.astype(np.float64))
        for f in ratio:
            sel = n >= f
            if sel.any():
                j = int(np.argmax(np.where(sel, rr, -1.0)))
                if rr[j] > ratio[f][0]: ratio[f] = (float(rr[j]), int(n[j]), int(M[j]))
        for c in want:
            if lo <= c < hi: chk[str(c)] = {"L": int(L[c-lo]), "M": int(M[c-lo])}
        Lc, Mc, Tl = int(L[-1]), int(M[-1]), int(TL[-1])
        lo = hi
    rec["T_lower_bound_min"] = rec["minTlow"] / 2.0**56
    rec["ratio_records"] = {str(k): v for k, v in ratio.items()}
    rec["checkpoints"] = chk; rec["N"] = N; rec["runtime_s"] = round(time.time()-t0, 1)
    rec["numpy"] = np.__version__
    json.dump(rec, open(out, "w"), indent=1, sort_keys=True); print(json.dumps(rec, sort_keys=True))

main()
