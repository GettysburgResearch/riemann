"""
anatomy_pairs.py -- EMPIRICAL (floating point, finite) pair anatomy of the sub-diagonal second moment

    M_2(D; H) = sum_{0 < N u <= H} |A_u|^2 = sum_{n, m} a_n a_m S_H(n, m),
    S_H(n, m) = sum_{0 < N u <= H} chi_n(u) conj(chi_m(u)),

for several real coefficient vectors a on the columns D < N n < 2D (all primary n prime to 6):
    mu    a_n = mu(n) W(N n / D)                 (the sextic Moebius family; zero off squarefree)
    lam   a_n = lambda(n) W(N n / D)             (Liouville, all n; equals mu on squarefree n)
    one   a_n = 1_sqf(n) W(N n / D)
    rand  a_n = eps_n 1_sqf(n) W,  eps_n iid +-1  (K samples)
    rmf   a_n = f(n) 1_sqf(n) W,   f random completely multiplicative +-1 on primes (K samples)

Outputs (per D and rho, H = D^rho): Diag (n = m), Off, the split of Off over pair classes
(shared prime / conjugate-shared prime / unit-aligned / generic) and over the log-size of the pair
conductor relative to H ("dual length"), sum |a a S| versus |sum a a S|, the row-class split of Off
(sixth / cube / square / generic rows), the mean of S over off-diagonal pairs, and a spectral
profile of a against the eigenvectors of S.

Usage: nice -n 10 python3 -I anatomy_pairs.py OUT.json --D 500 1000 2000 4000 --rhos 0.5 0.7 0.9 1.1
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

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402

ROWCLS = ("sixth", "cube", "square", "generic")
PAIRCLS = ("gcd", "conj", "unit", "generic")
DL_EDGES = [-np.inf, 0.0, 1.0, 2.0, 3.0, np.inf]       # log10(conductor / H) bins


def coef_vectors(cols, K, seed):
    rng = np.random.default_rng(seed)
    W, sqf = cols["W"], cols["sqf"]
    vec = {"mu": cols["mu"] * W, "lam": cols["lam"] * W, "one": sqf * W}
    rand = (rng.integers(0, 2, size=(len(W), K)) * 2 - 1) * (sqf * W)[:, None]
    used = sorted({i for f in cols["facs"] for i in f})
    pos = {g: k for k, g in enumerate(used)}
    fp = rng.integers(0, 2, size=(len(used), K)) * 2 - 1
    rmf = np.ones((len(W), K))
    for j, f in enumerate(cols["facs"]):
        for i in f:
            rmf[j] *= fp[pos[i]]
    rmf *= (sqf * W)[:, None]
    return vec, rand.astype(float), rmf


def stats_vec(a, ReS, masks, absS):
    """Off-diagonal anatomy for one real coefficient vector."""
    P = np.outer(a, a)
    tot = float(a @ ReS @ a)
    dg = float(np.sum(a * a * np.diag(ReS)))
    out = dict(M2=tot, diag=dg, off=tot - dg)
    offmask = masks["off"]
    out["sum_abs_off"] = float(np.sum(np.abs(P) * absS * offmask))
    out["by_pair"] = {c: float(np.sum(P * ReS * masks[c])) for c in PAIRCLS}
    out["by_pair_abs"] = {c: float(np.sum(np.abs(P) * absS * masks[c])) for c in PAIRCLS}
    out["conj_exact"] = float(np.sum(P * ReS * masks["conjexact"]))
    out["by_duallen"] = [float(np.sum(P * ReS * masks[f"dl{k}"])) for k in range(len(DL_EDGES) - 1)]
    out["by_duallen_abs"] = [float(np.sum(np.abs(P) * absS * masks[f"dl{k}"]))
                             for k in range(len(DL_EDGES) - 1)]
    return out


def summarize(x):
    x = np.asarray(x, dtype=float)
    return dict(mean=float(x.mean()), std=float(x.std(ddof=1)), q05=float(np.quantile(x, 0.05)),
                q50=float(np.quantile(x, 0.5)), q95=float(np.quantile(x, 0.95)))


def run_D(D, rhos, K, seed, primes, lib, pd, chunk=3000):
    t0 = time.time()
    cols = AC.columns(primes, D)
    nc = len(cols["norms"])
    used = sorted({i for f in cols["facs"] for i in f})
    Hs = [float(D) ** r for r in rhos]
    Hmax = max(Hs)
    a, b, N = AC.rows_sorted(Hmax)
    R = len(N)
    codes = AC.prime_codes(primes, used, a, b)
    rcls = AC.row_classes(a, b, Hmax)
    rclass_id = np.full(R, 3, dtype=np.int8)
    for k, c in enumerate(ROWCLS[:3]):
        rclass_id[rcls[c]] = k
    cut = [int(np.searchsorted(N, H, side="right")) for H in Hs]
    vec, rand, rmf = coef_vectors(cols, K, seed)
    names = list(vec)
    Amat_named = np.stack([vec[k] for k in names], axis=1)
    Aall = np.concatenate([Amat_named, rand, rmf], axis=1)          # nc x (3 + 2K)
    abs2 = Aall * Aall
    # unit code: chi_n(zeta), zeta = 1 + omega
    zcode = AC.chi_block(cols, AC.prime_codes(primes, used, np.array([1]), np.array([1])), slice(0, 1))[:, 0]
    S = np.zeros((nc, nc), dtype=np.complex128)
    # row accumulators: per row class, per coefficient: sum |A_u|^2 and sum diag_u
    racc_M = np.zeros((len(Hs), 4, Aall.shape[1]))
    racc_D = np.zeros((len(Hs), 4, Aall.shape[1]))
    nrows_cls = np.zeros((len(Hs), 4), dtype=np.int64)
    # kernel cross-check rows
    rng = np.random.default_rng(seed + 1)
    chk = np.sort(rng.choice(R, size=min(150, R), replace=False))
    A_mu_chk = np.zeros(len(chk), dtype=np.complex128)
    snaps = []
    start = 0
    for hi, stop in enumerate(cut):
        for s0 in range(start, stop, chunk):
            s1 = min(stop, s0 + chunk)
            X = AC.chi_block(cols, codes, slice(s0, s1))
            S += X @ X.conj().T
            Au = X.T @ Aall                                     # rows x coefs
            Du = (np.abs(X) ** 2).T @ abs2
            M = np.abs(Au) ** 2
            for k in range(4):
                m = rclass_id[s0:s1] == k
                if m.any():
                    racc_M[hi:, k] += M[m].sum(axis=0)
                    racc_D[hi:, k] += Du[m].sum(axis=0)
                    nrows_cls[hi:, k] += int(m.sum())
            inr = (chk >= s0) & (chk < s1)
            if inr.any():
                A_mu_chk[inr] = Au[chk[inr] - s0, 0]
        start = stop
        snaps.append(S.copy())
    # kernel cross-check of A_u for mu at chk rows (only rows covered, i.e. chk < cut[-1])
    sq_facs = [f for f, s in zip(cols["facs"], cols["sqf"]) if s]
    tree = C.Tree(sq_facs, list(vec["mu"][cols["sqf"]]))
    sb = np.ascontiguousarray(b[chk])
    sa0 = np.ascontiguousarray(a[chk])
    Ak = C.eval_rows(lib, pd, tree, (sb, sa0, np.ones(len(chk), dtype=np.int64)), workers=1, nchunks=1)
    kern_err = float(np.max(np.abs(Ak - A_mu_chk)))
    # masks
    share, conjshare = AC.prime_gcd_matrix(cols, primes)
    logQ = AC.pair_conductor(cols, primes)
    eye = np.eye(nc, dtype=bool)
    unit_al = np.isclose(zcode[:, None], zcode[None, :])
    masks = {"off": ~eye}
    masks["gcd"] = share & ~eye
    masks["conj"] = conjshare & ~eye
    masks["unit"] = unit_al & ~share & ~conjshare & ~eye
    masks["generic"] = ~unit_al & ~share & ~conjshare & ~eye
    gens = cols["gens"]
    conjidx = {g: k for k, g in enumerate(gens)}
    ce = np.zeros((nc, nc), dtype=bool)
    for j, g in enumerate(gens):
        k = conjidx.get(E.conj(g))
        if k is not None and k != j:
            ce[j, k] = True
    masks["conjexact"] = ce
    res = dict(D=D, n_cols=nc, n_sqf=int(cols["sqf"].sum()), kernel_check_maxdiff=kern_err,
               pair_counts={c: int(masks[c].sum()) for c in PAIRCLS}, per_rho=[])
    for hi, (rho, H) in enumerate(zip(rhos, Hs)):
        S_h = snaps[hi]
        ReS = S_h.real
        absS = np.abs(S_h)
        R_h = cut[hi]
        lq = (logQ - math.log(H)) / math.log(10)
        for k in range(len(DL_EDGES) - 1):
            masks[f"dl{k}"] = (lq > DL_EDGES[k]) & (lq <= DL_EDGES[k + 1]) & ~eye
        masks["absS_off"] = absS * ~eye
        # imaginary part check: S hermitian, real vectors -> only Re S matters
        herm = float(np.max(np.abs(S_h - S_h.conj().T)))
        per = dict(rho=rho, H=H, rows=R_h, hermitian_err=herm)
        # unweighted pair statistics of S
        Wv = cols["W"] * cols["sqf"]
        WW = np.outer(Wv, Wv)
        st = {}
        for c in PAIRCLS + ("off",):
            m = masks[c] & (WW > 0)
            if m.sum() == 0:
                continue
            st[c] = dict(npairs=int(m.sum()),
                         mean_ReS_W=float(np.sum(WW * ReS * m) / np.sum(WW * m)),
                         rms_S_over_sqrtR=float(np.sqrt(np.mean(absS[m] ** 2)) / math.sqrt(R_h)),
                         mean_abs_S_over_sqrtR=float(np.mean(absS[m]) / math.sqrt(R_h)))
        st["duallen"] = []
        for k in range(len(DL_EDGES) - 1):
            m = masks[f"dl{k}"] & (WW > 0)
            if m.sum() == 0:
                st["duallen"].append(None)
                continue
            st["duallen"].append(dict(npairs=int(m.sum()),
                                      rms_S_over_sqrtR=float(np.sqrt(np.mean(absS[m] ** 2)) / math.sqrt(R_h)),
                                      mean_ReS_W=float(np.sum(WW * ReS * m) / np.sum(WW * m))))
        per["S_stats"] = st
        per["named"] = {k: stats_vec(vec[k], ReS, masks, absS) for k in names}
        # row-class split of Off for named vectors
        for j, k in enumerate(names):
            per["named"][k]["by_rowclass_off"] = {c: float(racc_M[hi, ci, j] - racc_D[hi, ci, j])
                                                  for ci, c in enumerate(ROWCLS)}
            per["named"][k]["rowcheck_M2"] = float(racc_M[hi, :, j].sum())
        per["rows_by_class"] = {c: int(nrows_cls[hi, ci]) for ci, c in enumerate(ROWCLS)}
        # random controls
        for lab, Am, off0 in (("rand", rand, 3), ("rmf", rmf, 3 + K)):
            dgv = np.sum(Am * Am * np.diag(ReS)[:, None], axis=0)
            full = np.sum(Am * (ReS @ Am), axis=0)
            off = full - dgv
            sabs = np.sum(np.abs(Am) * (masks["absS_off"] @ np.abs(Am)), axis=0)
            byp = {c: summarize(np.sum(Am * ((ReS * masks[c]) @ Am), axis=0) / dgv) for c in PAIRCLS}
            rowoff = {c: summarize((racc_M[hi, ci, off0:off0 + K] - racc_D[hi, ci, off0:off0 + K]) / dgv)
                      for ci, c in enumerate(ROWCLS)}
            per[lab] = dict(off_over_diag=summarize(off / dgv), sumabs_over_diag=summarize(sabs / dgv),
                            sumabs_over_absoff=summarize(sabs / np.maximum(np.abs(off), 1e-300)),
                            by_pair_over_diag=byp, by_rowclass_off_over_diag=rowoff,
                            M2_over_diag=summarize(full / dgv))
        # z-scores of the named vectors against the rand distribution of Off/Diag
        rr = per["rand"]["off_over_diag"]
        for k in names:
            nk = per["named"][k]
            nk["off_over_diag"] = nk["off"] / nk["diag"]
            nk["z_vs_rand"] = (nk["off_over_diag"] - rr["mean"]) / rr["std"]
            nk["sumabs_over_absoff"] = nk["sum_abs_off"] / max(abs(nk["off"]), 1e-300)
        # positive mean of S over off-diagonal pairs and its share for each vector
        Sbar = st["off"]["mean_ReS_W"]
        for k in names:
            av = vec[k]
            per["named"][k]["mean_part"] = Sbar * float(av.sum() ** 2 - (av * av).sum())
            # with W-weights: a_n = s_n W_n; the "mean" model uses Sbar * sum_{n!=m} a_n a_m
        # spectral profile (eigenvectors of Re S on the squarefree columns)
        sq = cols["sqf"]
        Ssq = S_h[np.ix_(sq, sq)]
        lamS, V = np.linalg.eigh(Ssq)
        order = np.argsort(lamS)[::-1]
        lamS, V = lamS[order], V[:, order]
        nsq = len(lamS)
        ks = sorted({1, 10, max(1, nsq // 100), max(1, nsq // 10), nsq // 2})
        spec = dict(dim=nsq, rank_eff=int(np.sum(lamS > 1e-8 * lamS[0])),
                    top_eig_over_mean=float(lamS[0] / lamS.mean()), ks=ks)

        def prof(vv):
            c = V.conj().T @ vv.astype(complex)
            e = np.abs(c) ** 2
            e /= e.sum()
            cum = np.cumsum(e)
            contrib = lamS * np.abs(c) ** 2
            cc = np.cumsum(contrib) / contrib.sum()
            return [float(cum[k - 1]) for k in ks], [float(cc[k - 1]) for k in ks]

        spec["named"] = {}
        for k in ("mu", "one"):
            e, cmb = prof(vec[k][sq])
            spec["named"][k] = dict(energy_topk=e, M2share_topk=cmb)
        er, cr = [], []
        for t in range(min(K, 50)):
            e, cmb = prof(rand[sq, t])
            er.append(e)
            cr.append(cmb)
        spec["rand_mean"] = dict(energy_topk=list(np.mean(er, axis=0)), M2share_topk=list(np.mean(cr, axis=0)),
                                 energy_topk_std=list(np.std(er, axis=0)))
        per["spectral"] = spec
        res["per_rho"].append(per)
    res["seconds"] = time.time() - t0
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", required=True)
    ap.add_argument("--rhos", type=float, nargs="+", default=[0.5, 0.7, 0.9, 1.1])
    ap.add_argument("--K", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20261010)
    args = ap.parse_args()
    lib = AC.load_kernel_scratch()
    primes = E.prime_ideals(2 * max(args.D))
    nchk = E.self_test(primes, n_samples=20)
    pd = C.PrimeData(primes)
    print(f"setup: {len(primes)} primes, {nchk} exact symbol checks", flush=True)
    out = dict(convention="rows: all nonzero u in Z[omega], N u <= H = D^rho; columns: primary n prime to 6, "
                          "D < N n < 2D; W bump of common.py; real coefficient vectors; S_H(n,m) = "
                          "sum_u chi_n(u) conj chi_m(u)", results=[])
    for D in args.D:
        r = run_D(D, args.rhos, args.K, args.seed + D, primes, lib, pd)
        out["results"].append(r)
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=0)
        print(f"D={D} cols={r['n_cols']} sqf={r['n_sqf']} kernel_err={r['kernel_check_maxdiff']:.1e} "
              f"{r['seconds']:.1f}s", flush=True)
        for p in r["per_rho"]:
            mu = p["named"]["mu"]
            print(f"  rho={p['rho']} rows={p['rows']} M2/diag: mu={mu['M2']/mu['diag']:.3f} "
                  f"lam={p['named']['lam']['M2']/p['named']['lam']['diag']:.3f} "
                  f"one={p['named']['one']['M2']/p['named']['one']['diag']:.2f} "
                  f"rand={p['rand']['M2_over_diag']['mean']:.3f}+-{p['rand']['M2_over_diag']['std']:.3f} "
                  f"rmf={p['rmf']['M2_over_diag']['mean']:.3f}+-{p['rmf']['M2_over_diag']['std']:.3f} "
                  f"| mu sumabs/|off|={mu['sumabs_over_absoff']:.0f} sumabs/diag={mu['sum_abs_off']/mu['diag']:.1f} "
                  f"z={mu['z_vs_rand']:.2f}", flush=True)


if __name__ == "__main__":
    main()
