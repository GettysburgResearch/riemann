"""
balanced.py -- EMPIRICAL test of PR 910 FOURTH_MOMENT_REDUCTION.md (3.5) on the
actual sextic symbols (PR 910 itself only tested +-1 surrogate phases).

    B_{c,u}(X) = sum_{(a,b)=1, (ab, cS)=1} mu(a) mu(b) chi_{ab}(u) W(Na/X) W(Nb/X)
               = sum_{r squarefree, (r, cS)=1} mu(r) chi_r(u) WW_X(r),            (3.1)-(3.2)
    WW_X(r)    = sum_{d | r} W(Nd/X) W(Nr/(X Nd)),                                 (3.3)

    target (3.5):  sum_{0 < N u <= H} |B_{c,u}(X)|^2  <<  D^eps H X^2,  H = D^{1+theta}.

nu = 1, S = {(2), (lambda)}, W the bump of common.py, u over all nonzero
elements (conjugation symmetry B_{conj u} = conj B_u is used, as in moments.py).

Reported: the mean square, its ratio to H X^2, and its ratio to the exact
diagonal  sum_r WW_X(r)^2 #{u : (u, r) = 1} ~= L0(H) sum_r WW_X(r)^2 prod_{p|r}(1-1/Np).

Usage: python3 -I balanced.py OUT_JSON --D 1000 2000 4000 [--thetas 0.05 0.1 0.25] [--workers 2]
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402


def columns(primes, X, cset):
    """Squarefree r = ab with (a,b)=1, X < Na, Nb < 2X, (ab, c) = 1: dict r-tuple -> mu(r) WW_X(r)."""
    sq = E.squarefree_primary(primes, 2 * X)
    fam = [(N, f) for g, N, f in sq if X < N < 2 * X and not (set(f) & cset)]
    n = len(fam)
    kmax = max(len(f) for _, f in fam)
    F = np.full((n, kmax), -1, dtype=np.int64)
    for i, (_, f) in enumerate(fam):
        F[i, :len(f)] = f
    w = np.array([(-1) ** len(f) for _, f in fam]) * C.W(np.array([N for N, _ in fam]) / X)
    cols = {}
    for i in range(n):
        j = np.arange(i + 1, n)
        clash = np.zeros(len(j), dtype=bool)
        for p in F[i]:
            if p >= 0:
                clash |= (F[j] == p).any(axis=1)
        fi = fam[i][1]
        for jj in j[~clash].tolist():
            r = tuple(sorted(fi + fam[jj][1]))
            cols[r] = cols.get(r, 0.0) + 2.0 * w[i] * w[jj]    # ordered (a,b) and (b,a)
    return cols, n


def run_case(lib, primes, pd, D, X, cfacs, thetas, workers):
    t0 = time.time()
    cols, nfam = columns(primes, X, set(cfacs))
    keys = list(cols.keys())
    wts = np.array([cols[k] for k in keys])
    g = np.array([np.prod([1 - 1 / primes[p].N for p in k]) for k in keys])
    diag_density = float(np.sum(wts ** 2 * g))
    tree = C.Tree(keys, wts)
    Hlist = [(t, float(D) ** (1 + t)) for t in thetas]
    Hmax = max(H for _, H in Hlist)
    segs = C.lattice_segments(Hmax, points=False)
    B = C.eval_rows(lib, pd, tree, segs, workers=workers)
    sb, sa0, slen = segs
    a = np.concatenate([np.arange(x, x + m, dtype=np.int64) for x, m in zip(sa0, slen)])
    b = np.repeat(sb, slen)
    N = a * a - a * b + b * b
    mult = np.where(b == 0, 1.0, 2.0)
    x = np.abs(B) ** 2
    out = []
    for t, H in Hlist:
        m = N <= H
        L0 = float(mult[m].sum())
        ms = float((mult * x)[m].sum())
        out.append(dict(theta=t, H=H, L0=L0, ms=ms, ms_over_HX2=ms / (H * X * X),
                        ms_over_diag=ms / (L0 * diag_density),
                        m4_over_m2sq=float((mult * x * x)[m].sum() / L0 / (ms / L0) ** 2)))
    return dict(D=D, X=X, c=[list(primes[p].gen) for p in cfacs], Nc=int(np.prod([primes[p].N for p in cfacs])),
                n_family=nfam, n_columns=len(keys), tree_nodes=tree.nn,
                sum_WW2_g=diag_density, sum_WW2=float(np.sum(wts ** 2)),
                per_H=out, seconds=time.time() - t0)


def brute_check(lib, primes, pd, X, cfacs):
    """B_{c,u}(X) from the column tree vs a direct double sum over (a, b), a few u."""
    sq = E.squarefree_primary(primes, 2 * X)
    fam = [(N, f) for g, N, f in sq if X < N < 2 * X and not (set(f) & set(cfacs))]
    cols, _ = columns(primes, X, set(cfacs))
    keys = list(cols.keys())
    tree = C.Tree(keys, np.array([cols[k] for k in keys]))
    pts = [(5, 17), (-31, 4), (123, -77), (2, 1)]
    sb = np.array([p[1] for p in pts], dtype=np.int64)
    sa0 = np.array([p[0] for p in pts], dtype=np.int64)
    Bk = C.eval_rows(lib, pd, tree, (sb, sa0, np.ones(len(pts), dtype=np.int64)), workers=1, nchunks=1)
    err = 0.0
    for u, bk in zip(pts, Bk):
        sym = {}
        tot = 0j
        for Na, fa in fam:
            for Nb, fb in fam:
                if set(fa) & set(fb):
                    continue
                val = 1 + 0j
                for p in fa + fb:
                    if p not in sym:
                        cc = E.sextic_symbol_exact(u, primes[p].gen)
                        sym[p] = 0 if cc == E.ZERO else E.ZETA[cc]
                    val *= sym[p]
                tot += (-1) ** (len(fa) + len(fb)) * val * C.W(np.array([Na / X]))[0] * C.W(np.array([Nb / X]))[0]
        err = max(err, abs(tot - bk))
    return err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", required=True)
    ap.add_argument("--thetas", type=float, nargs="+", default=[0.05, 0.1, 0.25])
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    lib = C.load_kernel()
    primes = E.prime_ideals(2 * max(args.D))
    pd = C.PrimeData(primes)
    i7 = next(i for i, P in enumerate(primes) if P.N == 7)
    i13 = next(i for i, P in enumerate(primes) if P.N == 13)
    err = brute_check(lib, primes, pd, 60.0, [])
    err7 = brute_check(lib, primes, pd, 60.0, [i7])
    print(f"brute-force check of B_(c,u)(60): max err {err:.1e} (c=1), {err7:.1e} (c=p7)", flush=True)
    out = dict(brute_check_err=max(err, err7), results=[])
    if os.path.exists(args.out):
        with open(args.out) as fh:
            prev = json.load(fh)
        out["results"] = [r for r in prev["results"] if r["D"] not in args.D]
        out["brute_check_err"] = max(out["brute_check_err"], prev.get("brute_check_err", 0.0))
    for D in args.D:
        cases = [(D, []), (D / 2, []), (D / 4, []), (D / 16, []), (D / 7, [i7]), (D / 91, [i7, i13])]
        for X, cf in cases:
            if X < 8:
                continue
            r = run_case(lib, primes, pd, D, X, cf, args.thetas, args.workers)
            out["results"].append(r)
            with open(args.out, "w") as fh:
                json.dump(out, fh, indent=1)
            s = "; ".join(f"th={q['theta']:g}: ms/HX^2={q['ms_over_HX2']:.4f} ms/diag={q['ms_over_diag']:.4f} "
                          f"m4/m2^2={q['m4_over_m2sq']:.2f}" for q in r["per_H"])
            print(f"D={D} X={X:.0f} Nc={r['Nc']} #fam={r['n_family']} #cols={r['n_columns']} "
                  f"nodes={r['tree_nodes']} [{r['seconds']:.1f}s]: {s}", flush=True)


if __name__ == "__main__":
    main()
