"""
diag.py -- the diagonal ("orthogonal-rows") prediction for M_{2k}(D, H).

For k <= 5 the sextic principal condition prod n_i / prod m_j = sixth power
forces prod n_i = prod m_j as ideals (exponents lie in [-k, k]).  Hence the
diagonal part of M_{2k} is

    diag_{2k}(D, H) = sum_r c_k(r)^2 #{u : 0 < N u <= H, (u, r) = 1}
                    ~= L0(H) * E_k(D),
    E_k(D)          = sum_r c_k(r)^2 prod_{p | r} (1 - 1/Np),
    c_k(r)          = sum_{n_1 ... n_k = r (ordered)} prod |W(N n_i / D)|,

(all Moebius signs at fixed r agree), L0(H) = #{u : 0 < N u <= H}.
E_k(D) is also exactly the 2k-th moment of the random model
S = sum_n mu(n) W(Nn/D) X(n), X(n) = prod_{p|n} X_p, X_p independent,
X_p = 0 with probability 1/Np, else uniform on the sixth roots of unity.

Computed here:
  * E_1 exactly;
  * E_2 exactly (grouping ordered pairs by the product ideal) for D <= --exact2-max;
  * E_3 exactly (grouping triples) for D <= --exact3-max;
  * E_1..E_4 by Monte Carlo in the random model (C kernel) with standard errors.

Usage: python3 -I diag.py OUT_JSON --D ... [--exact2-max 16000] [--exact3-max 2000]
                          [--samples 1000000] [--workers 2]
"""
import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402

OFF = 1 << 22


def gens_arrays(ns, primes):
    ga = np.array([g[0] for g, _, _ in ns], dtype=np.int64)
    gb = np.array([g[1] for g, _, _ in ns], dtype=np.int64)
    kmax = max(len(f) for _, _, f in ns)
    F = np.full((len(ns), kmax), -1, dtype=np.int64)
    for i, (_, _, f) in enumerate(ns):
        F[i, :len(f)] = f
    gN = np.array([np.prod([1 - 1 / primes[p].N for p in f]) for _, _, f in ns])
    return ga, gb, F, gN


def corr_common(F_i, Frows, primes):
    """prod over primes p of n_i that also divide the row ideal of 1/(1-1/Np)."""
    c = np.ones(len(Frows))
    for p in F_i:
        if p < 0:
            continue
        hit = (Frows == p).any(axis=1)
        c[hit] /= (1 - 1 / primes[p].N)
    return c


def exact_E2(ns, w, primes):
    ga, gb, F, gN = gens_arrays(ns, primes)
    aw = np.abs(w)
    n = len(ns)
    keys, wts, gs = [], [], []
    for i in range(n):
        j = np.arange(i, n)
        pa = ga[i] * ga[j] - gb[i] * gb[j]
        pb = ga[i] * gb[j] + gb[i] * ga[j] - gb[i] * gb[j]
        keys.append((pa + OFF) * (2 * OFF) + (pb + OFF))
        m = np.where(j == i, 1.0, 2.0)
        wts.append(m * aw[i] * aw[j])
        gs.append(gN[i] * gN[j] * corr_common(F[i], F[j], primes))
    keys = np.concatenate(keys)
    wts = np.concatenate(wts)
    gs = np.concatenate(gs)
    uk, inv = np.unique(keys, return_inverse=True)
    c2 = np.bincount(inv, weights=wts)
    g = np.zeros(len(uk))
    g[inv] = gs
    return float(np.sum(c2 ** 2 * g)), int(len(uk))


def exact_E3(ns, w, primes):
    ga, gb, F, gN = gens_arrays(ns, primes)
    aw = np.abs(w)
    n = len(ns)
    # pairs (j, l), j <= l, sorted by j
    J, L = np.triu_indices(n)
    pa = ga[J] * ga[L] - gb[J] * gb[L]
    pb = ga[J] * gb[L] + gb[J] * ga[L] - gb[J] * gb[L]
    FJL = np.concatenate([F[J], F[L]], axis=1)
    g2 = gN[J] * gN[L]
    common = np.ones(len(J))
    for c in range(F.shape[1]):
        p = F[J, c]
        hit = (p[:, None] == F[L]).any(axis=1) & (p >= 0)
        Np = np.array([primes[q].N if q >= 0 else 1 for q in p], dtype=float)
        common[hit] /= (1 - 1 / Np[hit])
    g2 = g2 * common
    startj = np.searchsorted(J, np.arange(n))
    keys, wts, gs = [], [], []
    for i in range(n):
        s = startj[i]
        jj, ll = J[s:], L[s:]
        qa = ga[i] * pa[s:] - gb[i] * pb[s:]
        qb = ga[i] * pb[s:] + gb[i] * pa[s:] - gb[i] * pb[s:]
        keys.append((qa + OFF) * (2 * OFF) + (qb + OFF))
        # multiplicity of the unordered triple i <= j <= l
        neq = (jj != i).astype(int) + (ll != jj).astype(int)
        mult = np.where(neq == 2, 6.0, np.where(neq == 1, 3.0, 1.0))
        wts.append(mult * aw[i] * aw[jj] * aw[ll])
        gs.append(gN[i] * g2[s:] * corr_common(F[i], FJL[s:], primes))
    keys = np.concatenate(keys)
    wts = np.concatenate(wts)
    gs = np.concatenate(gs)
    uk, inv = np.unique(keys, return_inverse=True)
    c3 = np.bincount(inv, weights=wts)
    g = np.zeros(len(uk))
    g[inv] = gs
    return float(np.sum(c3 ** 2 * g)), int(len(uk))


def mc(lib, primes, tree, nsamp, workers, seed):
    pz = np.array([1.0 / primes[i].N for i in tree.used])
    per = nsamp // workers
    outs = [np.empty(per) for _ in range(workers)]

    def job(t):
        lib.sample_model(len(pz), pz, tree.nn, tree.parent, tree.pidx, tree.w,
                         per, np.uint64(seed * 1000 + t), outs[t])

    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(job, range(workers)))
    x = np.concatenate(outs)
    res = {}
    for k in range(1, 5):
        v = x ** k
        res[str(k)] = [float(v.mean()), float(v.std() / np.sqrt(len(v)))]
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", required=True)
    ap.add_argument("--exact2-max", type=int, default=16000)
    ap.add_argument("--exact3-max", type=int, default=2000)
    ap.add_argument("--samples", type=int, default=1_000_000)
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    lib = C.load_kernel()
    primes = E.prime_ideals(2 * max(args.D))
    out = {"results": []}
    if os.path.exists(args.out):
        with open(args.out) as fh:
            out = json.load(fh)
    for D in args.D:
        t0 = time.time()
        ns, facs, norms, w = C.family(primes, D)
        tree = C.Tree(facs, w)
        gN = np.array([np.prod([1 - 1 / primes[p].N for p in f]) for f in facs])
        r = dict(D=D, n_count=len(ns), sum_w2=float(np.sum(w ** 2)),
                 E1=float(np.sum(w ** 2 * gN)))
        if D <= args.exact2_max:
            r["E2_exact"], r["E2_ncols"] = exact_E2(ns, w, primes)
        if D <= args.exact3_max:
            r["E3_exact"], r["E3_ncols"] = exact_E3(ns, w, primes)
        r["mc"] = mc(lib, primes, tree, args.samples, args.workers, seed=D)
        r["mc_samples"] = args.samples
        r["seconds"] = time.time() - t0
        out["results"] = [x for x in out["results"] if x["D"] != D] + [r]
        out["results"].sort(key=lambda x: x["D"])
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=1)
        msg = f"D={D}: E1={r['E1']:.4g} (mc {r['mc']['1'][0]:.4g})"
        if "E2_exact" in r:
            msg += f"; E2={r['E2_exact']:.4g} (mc {r['mc']['2'][0]:.4g}+-{r['mc']['2'][1]:.2g}); E2/2E1^2={r['E2_exact']/(2*r['E1']**2):.4f}"
        if "E3_exact" in r:
            msg += f"; E3={r['E3_exact']:.4g} (mc {r['mc']['3'][0]:.4g}+-{r['mc']['3'][1]:.2g}); E3/6E1^3={r['E3_exact']/(6*r['E1']**3):.4f}"
        else:
            msg += f"; mc E3/6E1^3={r['mc']['3'][0]/(6*r['E1']**3):.4f}"
        print(msg + f" [{r['seconds']:.1f}s]", flush=True)


if __name__ == "__main__":
    main()
