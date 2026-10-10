"""
anatomy_galois.py -- EMPIRICAL (floating point, finite) test of the Galois-coherent secondary term.

For squarefree ideals, N(n) = N(m) iff m is a partial Galois conjugate of n (pi <-> conj(pi) at split
primes dividing n exactly once).  Then mu(m) = mu(n), W(N m/D) = W(N n/D), and

    chi_n(u) conj(chi_m(u)) = 1_{(u, n) = 1} prod_{pi in T} chi_pi(N u)      (T = conjugated primes),

since conj(chi_{conj pi}(u)) = chi_pi(conj u).  Summing over the 2^{s(n)} partial conjugates
(s(n) = number of split p with exactly one prime of n above p):

    sum_{m: N m = N n} chi_n(u) conj(chi_m(u)) = 1_{(u,n)=1} prod_{pi | n, conj pi not | n} (1 + chi_pi(N u)).

So the same-norm ("Galois") pairs give the exact piece
    Off_gal = sum_u sum_n a_n^2 1_{(u,n)=1} [prod (1 + chi_pi(N u)) - 1],
whose predictable part sits on the rows where chi_pi(N u) = 1 for every pi, i.e. N u = j^6:
    Pred_gal = sum_{u : N u = j^6 <= H} sum_n a_n^2 1_{(u,n)=1} (2^{s(n)} - 1).
mu and lambda have a_m = a_n on these pairs; random signs on ideals do not.  The script measures, for
mu and for controls (rand: iid on ideals; randc: iid on conjugation orbits; rmfc: random completely
multiplicative with f(pi) = f(conj pi)), the split Off = Off_gal + Off_rest, Pred_gal, and the row
split into "sixth-norm" rows (N u a sixth power) and the rest.

Usage: nice -n 10 python3 -I anatomy_galois.py OUT.json --D 500 1000 2000 2828 --rhos 0.5 0.7 0.9 1.1
"""
import argparse
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import anatomy_common as AC  # noqa: E402
import numpy as np  # noqa: E402

import eisenstein as E  # noqa: E402


def is_sixth_power_int(N):
    r = np.rint(np.asarray(N, dtype=float) ** (1 / 6)).astype(np.int64)
    return (r ** 6 == N) | ((r + 1) ** 6 == N) | ((r - 1) ** 6 == N)


def run(D, rhos, K, seed, primes):
    t0 = time.time()
    rng = np.random.default_rng(seed)
    cols = AC.columns(primes, D)
    keep = cols["sqf"]
    for k in ("norms", "W", "mu"):
        cols[k] = cols[k][keep]
    for k in ("facs", "exps", "gens"):
        cols[k] = [x for x, s in zip(cols[k], keep) if s]
    nc = len(cols["norms"])
    W = cols["W"]
    used = sorted({i for f in cols["facs"] for i in f})
    gidx = {g: k for k, g in enumerate(cols["gens"])}
    orb = np.array([min(k, gidx.get(E.conj(g), k)) for k, g in enumerate(cols["gens"])])
    # s(n): split primes of n whose conjugate does not divide n
    fs = [set(f) for f in cols["facs"]]
    gen2i = {primes[i].gen: i for i in used}
    s_n = np.array([sum(1 for i in f if primes[i].kind == "split" and gen2i.get(E.conj(primes[i].gen)) not in f)
                    for f in fs])
    rand = (rng.integers(0, 2, size=(nc, K)) * 2 - 1) * W[:, None]
    randc = (rng.integers(0, 2, size=(nc, K)) * 2 - 1)[orb] * W[:, None]
    rp = sorted({primes[i].p for i in used})
    rpos = {q: k for k, q in enumerate(rp)}
    fq = rng.integers(0, 2, size=(len(rp), K)) * 2 - 1
    rmfc = np.ones((nc, K))
    for j, f in enumerate(cols["facs"]):
        for i in f:
            rmfc[j] *= fq[rpos[primes[i].p]]
    rmfc *= W[:, None]
    vecs = np.concatenate([cols["mu"][:, None] * W[:, None], rand, randc, rmfc], axis=1)
    Hs = [float(D) ** r for r in rhos]
    a, b, N = AC.rows_sorted(max(Hs))
    six = is_sixth_power_int(N)
    codes = AC.prime_codes(primes, used, a, b)
    same = (cols["norms"][:, None] == cols["norms"][None, :]) & ~np.eye(nc, dtype=bool)
    res = dict(D=D, n_cols=nc, mean_2pow_s=float(np.sum(W ** 2 * 2.0 ** s_n) / np.sum(W ** 2)),
               n_samenorm_pairs=int(same.sum()), per_rho=[])
    S = np.zeros((nc, nc), dtype=np.complex128)
    S6 = np.zeros((nc, nc), dtype=np.complex128)        # rows with N u a sixth power only
    start = 0
    for rho, H in zip(rhos, Hs):
        stop = int(np.searchsorted(N, H, side="right"))
        for s0 in range(start, stop, 3000):
            s1 = min(stop, s0 + 3000)
            X = AC.chi_block(cols, codes, slice(s0, s1))
            S += X @ X.conj().T
            m6 = six[s0:s1]
            if m6.any():
                S6 += X[:, m6] @ X[:, m6].conj().T
        start = stop
        ReS, ReS6 = S.real, S6.real
        d = np.diag(ReS)
        quad = lambda M: np.sum(vecs * (M @ vecs), axis=0)     # noqa: E731
        dg = np.sum(vecs * vecs * d[:, None], axis=0)
        off = quad(ReS) - dg
        off_gal = quad(ReS * same)
        off_rest = off - off_gal
        d6 = np.sum(vecs * vecs * np.diag(ReS6)[:, None], axis=0)
        off6 = quad(ReS6) - d6                                # off-diagonal on sixth-norm rows
        off6_gal = quad(ReS6 * same)
        # prediction of the Galois piece on sixth-norm rows (exact on those rows by construction)
        pred6 = float(np.sum(np.diag(ReS6) * W ** 2 * (2.0 ** s_n - 1)))
        n6 = int(six[:stop].sum())
        per = dict(rho=rho, H=H, rows=stop, rows_sixthnorm=n6, pred_gal_sixthnorm_over_diag=pred6 / dg[0])

        def pack(sl):
            dd = dg[sl]
            out = {}
            for nm, v in (("off", off), ("off_gal", off_gal), ("off_rest", off_rest), ("off_sixthnorm_rows", off6),
                          ("off_gal_sixthnorm_rows", off6_gal), ("off_nonsix_rows", off - off6)):
                x = v[sl] / dd
                out[nm] = float(x[0]) if np.ndim(x) == 1 and len(x) == 1 else dict(mean=float(np.mean(x)),
                                                                                      std=float(np.std(x, ddof=1)))
            return out
        per["mu"] = pack(slice(0, 1))
        per["rand"] = pack(slice(1, 1 + K))
        per["randc"] = pack(slice(1 + K, 1 + 2 * K))
        per["rmfc"] = pack(slice(1 + 2 * K, 1 + 3 * K))
        # correlation (across rmfc samples) between off_gal and off_rest
        x, y = off_gal[1 + 2 * K:] / dg[1 + 2 * K:], off_rest[1 + 2 * K:] / dg[1 + 2 * K:]
        per["rmfc_corr_gal_rest"] = float(np.corrcoef(x, y)[0, 1])
        res["per_rho"].append(per)
        mu = per["mu"]
        print(f"D={D} rho={rho} rows={stop} six-norm rows={n6} mean2^s={res['mean_2pow_s']:.2f} | mu: off={mu['off']:+.4f} "
              f"gal={mu['off_gal']:+.4f} rest={mu['off_rest']:+.4f} six-rows={mu['off_sixthnorm_rows']:+.4f} "
              f"(gal part {mu['off_gal_sixthnorm_rows']:+.4f}, pred {per['pred_gal_sixthnorm_over_diag']:+.4f}) | "
              + " ".join(f"{c}: off={per[c]['off']['mean']:+.4f}({per[c]['off']['std']:.4f}) gal={per[c]['off_gal']['mean']:+.4f} "
                         f"six={per[c]['off_sixthnorm_rows']['mean']:+.4f}" for c in ("rand", "randc", "rmfc"))
              + f" corr(rmfc gal,rest)={per['rmfc_corr_gal_rest']:+.2f} ({time.time()-t0:.0f}s)", flush=True)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", default=[500, 1000, 2000, 2828])
    ap.add_argument("--rhos", type=float, nargs="+", default=[0.5, 0.7, 0.9, 1.1])
    ap.add_argument("--K", type=int, default=200)
    ap.add_argument("--seed", type=int, default=11)
    args = ap.parse_args()
    primes = E.prime_ideals(2 * max(args.D))
    E.self_test(primes, n_samples=20)
    out = dict(convention="as anatomy_pairs.py, squarefree columns only", results=[])
    for D in args.D:
        out["results"].append(run(D, args.rhos, args.K, args.seed + D, primes))
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=0)


if __name__ == "__main__":
    main()
