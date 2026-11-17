#!/usr/bin/env python3
"""C3-failure-anatomy: exact segmented sieve for Liouville lambda(n) and Moebius mu(n).

Computes, for 1 <= x <= N (default N = 1_000_000_000):
  L(x) = sum_{n<=x} lambda(n)   (Polya's conjecture: L(x) <= 0 for x >= 2; refuted)
  M(x) = sum_{n<=x} mu(n)       (Mertens' conjecture: |M(x)| < sqrt(x) for x > 1; refuted, non-constructively)
  T(x) = sum_{n<=x} lambda(n)/n (Turan's conjecture T(x) > 0; refuted)  -- float64 only

Integer quantities (L, M) are exact (int8/int64 arithmetic).  The only floating-point
decision is "does n have a prime factor > sqrt(N)?", decided by comparing log(n) with the
float32 sum of log p over the prime powers p^k <= N dividing n (p <= sqrt(N)).  The residual
cofactor is either 1 (difference ~ 0, |float error| < 1e-3) or a prime > sqrt(N) >= 30000
(difference >= log(sqrt(N)+1), > 10 for N = 1e9), so the threshold 1.0 decides exactly.  The script
counts differences in the ambiguous band [0.01, log(sqrt(N)+1) - 0.01] and the run is valid only if
that count is 0.

T(x) is accumulated in float64 with numpy cumsum (sequential add.accumulate) plus a carried
offset; a crude a-priori bound on its rounding error is |err| <= 2 * N * 2^-53 * H_N, which is
recorded in the output.  T is therefore labelled NUMERICAL-NONRIGOROUS (float64 + a-priori bound).

Usage: python3 liouville_mertens_sieve.py [N] [segment_log2] [outfile]
       python3 liouville_mertens_sieve.py --selftest
"""
import sys, json, math, time, hashlib, platform
import numpy as np


def small_primes(m):
    s = np.ones(m + 1, dtype=bool); s[:2] = False
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


def run(N, seglog=22, track=True):
    t0 = time.time()
    R = int(math.isqrt(N))
    primes = small_primes(R)
    logp = np.log(primes.astype(np.float64)).astype(np.float32)
    S = 1 << seglog
    Lc = 0; Mc = 0; Tc = 0.0; TFc = 0
    SCALE = np.int64(1) << np.int64(56)
    minTF_lower = None; argminTF = None
    res = {
        "N": N, "sqrtN": R, "num_small_primes": int(len(primes)), "segment": S,
        "first_x_ge2_L_pos": None, "L_at_first_pos": None,
        "count_x_le_N_L_pos": 0, "max_L": None, "argmax_L": None,
        "last_x_L_pos": None,
        "max_M": None, "argmax_M": None, "min_M": None, "argmin_M": None,
        "Mertens_ratio_records": {}, "min_T_x_ge1": None, "argmin_T": None,
        "checkpoints": {},
    }
    # ranges for the max |M(x)|/sqrt(x)
    ratio_floors = [2, 10, 100, 200, 1000, 10**4, 10**5, 10**6, 10**7, 10**8]
    best = {f: (-1.0, None, None) for f in ratio_floors}
    checkpoints = sorted(set([10**k for k in range(1, 10) if 10**k <= N] +
                             [x for x in (906150256, 906150257, 906180359, 906316571, 906488079,
                                          906488080, N) if x <= N]))
    maxL = None; argmaxL = None; maxM = None; argmaxM = None; minM = None; argminM = None
    minT = None; argminT = None
    first_pos = None; count_pos = 0; last_pos = None
    lo = 1
    ambiguous = 0
    while lo <= N:
        hi = min(lo + S, N + 1)
        n = np.arange(lo, hi, dtype=np.int64)
        m = hi - lo
        par = np.zeros(m, dtype=np.uint8)
        slog = np.zeros(m, dtype=np.float32)
        nsq = np.zeros(m, dtype=bool)
        for p, lp in zip(primes.tolist(), logp.tolist()):
            pk = p; k = 1
            lpf = np.float32(lp)
            while pk < hi:
                st = (-lo) % pk
                if st < m:
                    par[st::pk] ^= 1
                    slog[st::pk] += lpf
                    if k == 2:
                        nsq[st::pk] = True
                pk *= p; k += 1
        diff = np.log(n.astype(np.float64)) - slog.astype(np.float64)
        amb = np.count_nonzero((diff > 0.01) & (diff < math.log(R + 1) - 0.01))
        ambiguous += int(amb)
        big = diff > 1.0
        par ^= big.astype(np.uint8)
        lam = (1 - 2 * par.astype(np.int64))
        mu = np.where(nsq, 0, lam)
        L = Lc + np.cumsum(lam)
        M = Mc + np.cumsum(mu)
        T = Tc + np.cumsum(lam.astype(np.float64) / n.astype(np.float64))
        # exact fixed-point companion: TF(x) = sum lam(n)*floor(2^56/n), |TF - 2^56 T| < x
        TF = TFc + np.cumsum(lam * (SCALE // n))
        # Polya
        pos = (L > 0) & (n >= 2)
        cpos = int(np.count_nonzero(pos))
        if cpos:
            idx = np.nonzero(pos)[0]
            if first_pos is None:
                first_pos = int(n[idx[0]]); res["L_at_first_pos"] = int(L[idx[0]])
            last_pos = int(n[idx[-1]])
            count_pos += cpos
        i = int(np.argmax(L))
        if maxL is None or L[i] > maxL:
            maxL = int(L[i]); argmaxL = int(n[i])
        i = int(np.argmax(M))
        if maxM is None or M[i] > maxM:
            maxM = int(M[i]); argmaxM = int(n[i])
        i = int(np.argmin(M))
        if minM is None or M[i] < minM:
            minM = int(M[i]); argminM = int(n[i])
        lowerTF = TF - n          # 2^56 * T(x) >= TF(x) - x  (rigorous)
        i = int(np.argmin(lowerTF))
        if minTF_lower is None or lowerTF[i] < minTF_lower:
            minTF_lower = int(lowerTF[i]); argminTF = int(n[i])
        i = int(np.argmin(T))
        if minT is None or T[i] < minT:
            minT = float(T[i]); argminT = int(n[i])
        ratio = np.abs(M).astype(np.float64) / np.sqrt(n.astype(np.float64))
        for f in ratio_floors:
            if hi - 1 < f:
                continue
            sel = n >= f
            j = int(np.argmax(np.where(sel, ratio, -1.0)))
            if ratio[j] > best[f][0]:
                best[f] = (float(ratio[j]), int(n[j]), int(M[j]))
        for c in checkpoints:
            if lo <= c < hi:
                res["checkpoints"][str(c)] = {"L": int(L[c - lo]), "M": int(M[c - lo]),
                                              "T_float64": float(T[c - lo]),
                                              "T_fixed_lo": (int(TF[c - lo]) - c) / 2.0 ** 56,
                                              "T_fixed_hi": (int(TF[c - lo]) + c) / 2.0 ** 56}
        Lc = int(L[-1]); Mc = int(M[-1]); Tc = float(T[-1]); TFc = int(TF[-1])
        if track and (lo // S) % 20 == 0:
            print(f"lo={lo:,} L={Lc} M={Mc} elapsed={time.time()-t0:.1f}s", flush=True)
        lo = hi
    res.update({"first_x_ge2_L_pos": first_pos, "count_x_le_N_L_pos": count_pos,
                "last_x_L_pos": last_pos, "max_L": maxL, "argmax_L": argmaxL,
                "max_M": maxM, "argmax_M": argmaxM, "min_M": minM, "argmin_M": argminM,
                "min_T_x_ge1": minT, "argmin_T": argminT,
                "T_fixedpoint_rigorous_lower_bound_min": minTF_lower / 2.0 ** 56,
                "T_fixedpoint_argmin_of_lower_bound": argminTF,
                "T_fixedpoint_note": "T(x) >= (TF(x)-x)/2^56 with TF(x)=sum_{n<=x} lam(n)*floor(2^56/n) exact int64",
                "ambiguous_residual_decisions": ambiguous})
    res["Mertens_ratio_records"] = {str(f): {"max_|M(x)|/sqrt(x)": v[0], "x": v[1], "M(x)": v[2]}
                                    for f, v in best.items()}
    HN = math.log(N) + 0.5773 + 1.0 / N
    res["T_float64_apriori_error_bound"] = 2 * N * 2.0 ** -53 * HN
    res["runtime_s"] = time.time() - t0
    return res


def selftest():
    import sympy
    N = 200000
    r = run(N, seglog=12, track=False)
    lam = [0] + [(-1) ** sympy.primeomega(k) for k in range(1, N + 1)]
    mu = [0] + [int(sympy.mobius(k)) for k in range(1, N + 1)]
    L = np.cumsum(lam); M = np.cumsum(mu)
    for c, v in r["checkpoints"].items():
        c = int(c)
        assert v["L"] == L[c] and v["M"] == M[c], (c, v, L[c], M[c])
    assert r["max_M"] == int(M.max()) and r["min_M"] == int(M[1:].min())
    assert r["ambiguous_residual_decisions"] == 0
    print("selftest ok", {k: r["checkpoints"][k] for k in r["checkpoints"]})


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        selftest(); sys.exit(0)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
    seglog = int(sys.argv[2]) if len(sys.argv) > 2 else 22
    out = sys.argv[3] if len(sys.argv) > 3 else None
    res = run(N, seglog)
    res["versions"] = {"python": platform.python_version(), "numpy": np.__version__}
    s = json.dumps(res, indent=1, sort_keys=True)
    print(s)
    if out:
        with open(out, "w") as f:
            f.write(s + "\n")
        print("sha256", hashlib.sha256((s + "\n").encode()).hexdigest())
