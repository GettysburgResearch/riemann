"""
moments.py -- EMPIRICAL (FLOATING_RECONNAISSANCE) evaluation of

    M_{2k}(D, H) = sum_{u in O, 0 < N(u) <= H} |A_u(D)|^{2k},   k = 1, 2, 3 (and 4),

for the sextic family A_u(D) = sum_n mu(n) chi_n(u) W(N(n)/D) of the OpenAI
Oct 5 2026 manuscript (nu = 1, S = {(2), (lambda)}, W the bump of common.py).

Row convention: u runs over ALL nonzero elements of O (units and non-primary
u included), as in "0 < N u <= H" and as in the w5copg mean-square numerics.
By A_{conj u} = conj(A_u) only rows with b >= 0 are evaluated; rows with
b > 0 are counted twice (b = 0 rows are self-conjugate).

Rows are split into disjoint classes:
    sixth   u = unit * v^6               (chi_n(u) = chi_n(unit) 1_{(n,v)=1})
    cube    u = unit * v^3, not sixth    (chi_n(u) = chi_n(unit) (v/n)_2: quadratic twists)
    square  u = unit * v^2, not sixth    (cubic twists)
    generic everything else
and, as an overlapping diagnostic, "rational" rows b = 0 (u in Z, A_u real).

Usage:
    python3 -I moments.py OUT_JSON --D 500 1000 ... [--thetas 0.05 0.1 0.25 0.5]
           [--theta-cap D:theta ...] [--d2-max DMAX] [--workers 2]

--theta-cap 32000:0.25 means: for D > 32000 only thetas <= 0.25 are run.
--d2-max: also run H = D^2 for D <= DMAX.
"""
import argparse
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402

CLASSES = ("sixth", "cube", "square", "generic", "rational")
KMAX = 4
OFF = 1 << 22


def key(a, b):
    return (np.asarray(a, dtype=np.int64) + OFF) * (2 * OFF) + (np.asarray(b, dtype=np.int64) + OFF)


def special_keys(Hmax):
    out = {}
    for e in (6, 3, 2):
        va, vb = E.nonzero_lattice(Hmax ** (1.0 / e) + 1e-9)
        # v^e by repeated multiplication (vectorised)
        pa, pb = va.copy(), vb.copy()
        for _ in range(e - 1):
            pa, pb = pa * va - pb * vb, pa * vb + pb * va - pb * vb
        ks = []
        for ea, eb in E.UNITS:
            ua, ub = ea * pa - eb * pb, ea * pb + eb * pa - eb * pb
            ks.append(key(ua, ub))
        out[e] = np.unique(np.concatenate(ks))
    return out


def classify(a, b, sk):
    k = key(a, b)
    is6 = np.isin(k, sk[6], assume_unique=False)
    is3 = np.isin(k, sk[3]) & ~is6
    is2 = np.isin(k, sk[2]) & ~is6
    gen = ~(is6 | is3 | is2)
    return {"sixth": is6, "cube": is3, "square": is2, "generic": gen, "rational": b == 0}


def run_D(lib, primes, pd, D, Hlist, workers, chunk_pts=3_000_000):
    t0 = time.time()
    ns, facs, norms, w = C.family(primes, D)
    tree = C.Tree(facs, w)
    sumw2 = float(np.sum(w ** 2))
    Hmax = max(H for _, H in Hlist)
    sb, sa0, slen = C.lattice_segments(Hmax, points=False)
    sk = special_keys(Hmax)
    Hs = np.array([H for _, H in Hlist])
    nH = len(Hs)
    S = {c: np.zeros((nH, KMAX + 1)) for c in CLASSES}     # S[c][h, k] = sum mult*|A|^{2k}, k=0 is count
    mx = {c: np.zeros(nH) for c in CLASSES}
    starts = np.concatenate([[0], np.cumsum(slen)])
    total = int(starts[-1])
    # group segments into chunks of ~chunk_pts points
    cuts = np.searchsorted(starts, np.arange(chunk_pts, total, chunk_pts))
    bounds = [0] + sorted(set(int(c) for c in cuts if 0 < c < len(slen))) + [len(slen)]
    A1 = None
    for g0, g1 in zip(bounds[:-1], bounds[1:]):
        gs = (sb[g0:g1], sa0[g0:g1], slen[g0:g1])
        A = C.eval_rows(lib, pd, tree, gs, workers=workers)
        a = np.concatenate([np.arange(x, x + n, dtype=np.int64) for x, n in zip(gs[1], gs[2])])
        b = np.repeat(gs[0], gs[2])
        N = a * a - a * b + b * b
        mult = np.where(b == 0, 1.0, 2.0)
        x = np.abs(A) ** 2
        cls = classify(a, b, sk)
        hit = np.nonzero((a == 1) & (b == 0))[0]
        if len(hit):
            A1 = complex(A[hit[0]])
        pw = [mult * x ** k for k in range(KMAX + 1)]
        for hi, H in enumerate(Hs):
            inH = N <= H
            for c in CLASSES:
                m = inH & cls[c]
                if m.any():
                    for k in range(KMAX + 1):
                        S[c][hi, k] += float(pw[k][m].sum())
                    mx[c][hi] = max(mx[c][hi], float(x[m].max()))
    secs = time.time() - t0
    per_H = []
    for hi, (lab, H) in enumerate(Hlist):
        tot = sum(S[c][hi] for c in ("sixth", "cube", "square", "generic"))
        row = dict(label=lab, H=H, n_u=int(round(tot[0])),
                   M={str(k): float(tot[k]) for k in range(1, KMAX + 1)},
                   by_class={c: dict(n_u=int(round(S[c][hi, 0])),
                                     M={str(k): float(S[c][hi, k]) for k in range(1, KMAX + 1)},
                                     max_abs2=float(mx[c][hi])) for c in CLASSES})
        per_H.append(row)
    res = dict(D=D, n_count=len(ns), tree_nodes=tree.nn, sum_w2=sumw2,
               A1=[A1.real, A1.imag] if A1 is not None else None,
               per_H=per_H, seconds=secs, n_u_evaluated=total)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", required=True)
    ap.add_argument("--thetas", type=float, nargs="+", default=[0.05, 0.1, 0.25, 0.5])
    ap.add_argument("--theta-cap", nargs="*", default=[])
    ap.add_argument("--d2-max", type=int, default=0)
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    caps = sorted((int(s.split(":")[0]), float(s.split(":")[1])) for s in args.theta_cap)
    lib = C.load_kernel()
    t0 = time.time()
    primes = E.prime_ideals(2 * max(args.D))
    nchk = E.self_test(primes, n_samples=40)
    pd = C.PrimeData(primes)
    print(f"setup: {len(primes)} prime ideals up to {2*max(args.D)}, tables {pd.tables.nbytes/1e6:.0f} MB, "
          f"{nchk} exact symbol checks passed ({time.time()-t0:.1f}s)", flush=True)
    out = dict(convention="u over all nonzero elements of Z[omega], 0<N(u)<=H; nu=1; "
                          "W(y)=exp(4-1/((y-1)(2-y))) on (1,2); n squarefree primary prime to 6",
               results=[])
    if os.path.exists(args.out):
        with open(args.out) as fh:
            out = json.load(fh)
    for D in args.D:
        tmax = max(args.thetas)
        for Dc, tc in caps:
            if D > Dc:
                tmax = min(tmax, tc)
        Hlist = [(f"theta={t:g}", float(D) ** (1 + t)) for t in args.thetas if t <= tmax + 1e-12]
        if D <= args.d2_max:
            Hlist.append(("H=D^2", float(D) ** 2))
        res = run_D(lib, primes, pd, D, Hlist, args.workers)
        out["results"] = [r for r in out["results"] if r["D"] != D] + [res]
        out["results"].sort(key=lambda r: r["D"])
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=1)
        s2 = res["sum_w2"]
        line = []
        for r in res["per_H"]:
            mean = {k: r["M"][k] / r["n_u"] for k in r["M"]}
            line.append(f"{r['label']}: #u={r['n_u']} m2/sw2={mean['1']/s2:.3f} "
                        f"m4/m2^2={mean['2']/mean['1']**2:.3f} m6/m2^3={mean['3']/mean['1']**3:.3f}")
        print(f"D={D} #n={res['n_count']} nodes={res['tree_nodes']} |A1|={abs(complex(*res['A1'])):.2f} "
              f"{res['seconds']:.1f}s\n   " + "\n   ".join(line), flush=True)
    print(f"total {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
