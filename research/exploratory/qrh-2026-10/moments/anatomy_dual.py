"""
anatomy_dual.py -- EMPIRICAL (floating point, finite) explicit Poisson dual of the pair sums, small D.

Rows carry the Gaussian weight g(u) = exp(-pi N(u) / Y) over all u in O = Z[omega].  For squarefree
primary n, m (prime to 6) with lcm c (product of the primary prime generators of the primes of nm),
Q = N(c), Poisson summation over the lattice O (covolume sqrt(3)/2, dual lattice (c sqrt(-3))^{-1} O)
gives the exact identity

    S_Y(n, m) := sum_u chi_n(u) conj(chi_m(u)) g(u)
               = (2Y / (sqrt(3) Q)) sum_{h in O} exp(-4 pi Y N(h) / (3Q)) G_{n,m}(h),

    G_{n,m}(h) = sum_{x mod c} chi_n(x) conj(chi_m(x)) e(h x / c),   e(z) = exp(4 pi i Im(z)/sqrt 3),

and, by CRT, G = prod_{p | c} G_p with
    p | n only:  G_p = chi_p(c/p) conj(chi_p(h)) tau_p,      tau_p  = sum_x chi_p(x) e(x/p)
    p | m only:  G_p = conj(chi_p(c/p)) chi_p(h) tau_p^-,    tau_p^- = sum_x conj(chi_p(x)) e(x/p)
    p | (n, m):  G_p = Ramanujan sum = N p - 1 if p | h, else -1.
(G_p = 0 in the first two cases when p | h.)

The script (i) checks the identity against direct lattice sums, (ii) writes the off-diagonal
Off = sum_{n != m} a_n a_m S_Y(n, m) as sum_{h != 0} T(h), (iii) splits sum T(h) by the class of the
dual frequency h (unit*sixth power / cube / square / generic) and by N(h) relative to the dual
length, and compares with the "dual diagonal"
    DD = (2Y/sqrt3) sum_n a_n^2 N(n)^{-1} sum_{h != 0, (h, n) = 1} exp(-4 pi Y N h / (3 N n^2)),
for mu and for the controls of anatomy_pairs.py.

Usage: nice -n 10 python3 -I anatomy_dual.py OUT.json --D 150 300 --rhos 0.5 0.7 0.9
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

ZETA = E.ZETA
SQ3 = math.sqrt(3.0)
HCLS = ("sixth", "cube", "square", "generic")


def e_frac(hx, c):
    """e(hx / c) for an element hx = (A, B) (arrays) and modulus element c: exp(2 pi i B'/N c),
    with hx * conj(c) = A' + B' omega."""
    cc = E.conj(c)
    A = hx[0] * cc[0] - hx[1] * cc[1]
    B = hx[0] * cc[1] + hx[1] * cc[0] - hx[1] * cc[1]
    return np.exp(2j * np.pi * (B % E.norm(c)) / E.norm(c))


def gauss_tau(P):
    """tau_p = sum_{x mod p} chi_p(x) e(x/p) and tau_p^- (conjugate character)."""
    if P.kind == "split":
        x = np.arange(P.p, dtype=np.int64)
        y = np.zeros_like(x)
    else:
        q = P.p
        g = np.arange(q * q, dtype=np.int64)
        x, y = g // q, g % q
    codes = P.codes(x, y)
    val = np.where(codes == E.ZERO, 0, ZETA[np.minimum(codes, 5)])
    ev = e_frac((x, y), P.gen)
    tau = np.sum(val * ev)
    taum = np.sum(np.conj(val) * ev)
    return tau, taum


def chi_val(P, x, y):
    c = P.codes(np.asarray(x, dtype=np.int64), np.asarray(y, dtype=np.int64))
    return np.where(c == E.ZERO, 0, ZETA[np.minimum(c, 5)])


def lattice_all(Nmax):
    a, b = E.nonzero_lattice(Nmax)
    N = a * a - a * b + b * b
    return a, b, N


def h_classes(a, b, Nmax):
    import moments as Mo
    sk = Mo.special_keys(Nmax)
    cl = Mo.classify(a, b, sk)
    out = np.full(len(a), 3, dtype=np.int8)
    for k, c in enumerate(HCLS[:3]):
        out[cl[c]] = k
    return out


def run(D, rhos, K, seed, primes, check_pairs=12):
    t0 = time.time()
    rng = np.random.default_rng(seed)
    sq = [t for t in E.squarefree_primary(primes, 2 * D) if D < t[1] < 2 * D]
    sq.sort(key=lambda t: (t[1], t[0]))
    gens = [t[0] for t in sq]
    norms = np.array([t[1] for t in sq], dtype=float)
    facs = [t[2] for t in sq]
    nc = len(sq)
    Wv = C.W(norms / D)
    mu = np.array([(-1.0) ** len(f) for f in facs]) * Wv
    used = sorted({i for f in facs for i in f})
    taus = {i: gauss_tau(primes[i]) for i in used}
    # controls
    gidx = {g: k for k, g in enumerate(gens)}
    orb = np.array([min(k, gidx.get(E.conj(g), k)) for k, g in enumerate(gens)])
    rand = (rng.integers(0, 2, size=(nc, K)) * 2 - 1) * Wv[:, None]
    randc = (rng.integers(0, 2, size=(nc, K)) * 2 - 1)[orb] * Wv[:, None]
    vecs = np.concatenate([mu[:, None], Wv[:, None], rand, randc], axis=1)     # mu, one, rand K, randc K
    res = dict(D=D, n_cols=nc, per_rho=[])
    for rho in rhos:
        Y = float(D) ** rho
        # ---------- direct side ----------
        Umax = Y * 14.0
        ua, ub, uN = lattice_all(Umax)
        gu = np.exp(-np.pi * uN / Y)
        codes = AC.prime_codes(primes, used, ua, ub)
        cols = dict(facs=facs, exps=[tuple(1 for _ in f) for f in facs])
        X = AC.chi_block(cols, codes, slice(0, len(ua)))
        S = (X * gu[None, :]) @ X.conj().T
        ReS = S.real
        dS = np.diag(ReS)
        full = np.sum(vecs * (ReS @ vecs), axis=0)
        diag = np.sum(vecs * vecs * dS[:, None], axis=0)
        off_direct = full - diag
        # ---------- dual side ----------
        Qmax = (2 * D) ** 2
        CUT = 20.0                                                 # exp(-20) truncation
        Hmax = 3 * Qmax * CUT / (4 * np.pi * Y)
        ha, hb, hN = lattice_all(Hmax)
        o = np.argsort(hN, kind="stable")
        ha, hb, hN = ha[o], hb[o], hN[o]
        hcls = h_classes(ha, hb, Hmax)
        Hd = 3 * (1.5 * D) ** 2 / (4 * np.pi * Y)                 # dual length at N n = N m = 1.5 D
        nb_edges = [0, 0.1, 0.3, 1.0, 3.0, np.inf]
        nbin = np.searchsorted(np.array(nb_edges[1:-1]), hN / Hd, side="left").astype(np.int64)
        chih = {i: chi_val(primes[i], ha, hb) for i in used}
        divh = {i: (chih[i] == 0) for i in used}
        Kc = np.zeros((4, nc, nc))
        Kb = np.zeros((len(nb_edges) - 1, nc, nc))
        T_mu = np.zeros(len(ha))
        Tabs = 0.0
        dual_err = []
        chk = set(map(tuple, rng.integers(0, nc, size=(check_pairs, 2)).tolist()))
        for j in range(nc):
            for k in range(nc):
                if j == k:
                    continue
                fj, fk = set(facs[j]), set(facs[k])
                allp = sorted(fj | fk)
                c = (1, 0)
                for i in allp:
                    c = E.mul(c, primes[i].gen)
                Q = float(E.norm(c))
                hi = int(np.searchsorted(hN, 3 * Q * CUT / (4 * np.pi * Y), side="right"))
                G = np.ones(hi, dtype=np.complex128)
                for i in allp:
                    P = primes[i]
                    cp = (1, 0)
                    for i2 in allp:
                        if i2 != i:
                            cp = E.mul(cp, primes[i2].gen)
                    if i in fj and i in fk:
                        G *= np.where(divh[i][:hi], P.N - 1.0, -1.0)
                    elif i in fj:
                        G *= chi_val(P, [cp[0]], [cp[1]])[0] * np.conj(chih[i][:hi]) * taus[i][0]
                    else:
                        G *= np.conj(chi_val(P, [cp[0]], [cp[1]])[0]) * chih[i][:hi] * taus[i][1]
                wG = (2 * Y / (SQ3 * Q)) * np.exp(-4 * np.pi * Y * hN[:hi] / (3 * Q)) * G
                K_h = wG.real
                Kc[:, j, k] = np.bincount(hcls[:hi], weights=K_h, minlength=4)
                Kb[:, j, k] = np.bincount(nbin[:hi], weights=K_h, minlength=len(nb_edges) - 1)
                T_mu[:hi] += K_h * (mu[j] * mu[k])
                Tabs += float(np.sum(np.abs(wG))) * abs(mu[j] * mu[k])
                if (j, k) in chk:
                    dual_err.append(abs(np.sum(wG) - S[j, k]) / max(1.0, abs(S[j, k])))
        quad = lambda M: np.sum(vecs * (M @ vecs), axis=0)            # noqa: E731
        offc = np.array([quad(Kc[q]) for q in range(4)])               # 4 x nvec
        offb = np.array([quad(Kb[q]) for q in range(len(nb_edges) - 1)])
        off_dual = offc.sum(axis=0)
        # dual diagonal (n = m term of the bilinearized dual)
        DD = np.zeros(vecs.shape[1])
        for j in range(nc):
            cop = np.ones(len(ha), dtype=bool)
            for i in facs[j]:
                cop &= ~divh[i]
            s = np.sum(np.exp(-4 * np.pi * Y * hN[cop] / (3 * norms[j] ** 2)))
            DD += vecs[j] ** 2 * (2 * Y / SQ3) / norms[j] * s
        per = dict(rho=rho, Y=Y, dual_length=Hd, n_h=int(len(ha)),
                   identity_maxrelerr=float(max(dual_err) if dual_err else 0.0),
                   offdirect_vs_dual_maxdiff=float(np.max(np.abs(off_direct - off_dual) / diag)))
        names = ["mu", "one"]
        for idx, nm in enumerate(names):
            per[nm] = dict(diag=float(diag[idx]), off=float(off_dual[idx]), DD=float(DD[idx]),
                           off_over_diag=float(off_dual[idx] / diag[idx]),
                           DD_over_diag=float(DD[idx] / diag[idx]),
                           by_hclass_over_diag={c: float(offc[ci, idx] / diag[idx]) for ci, c in enumerate(HCLS)},
                           by_Nh_over_diag=[float(offb[q, idx] / diag[idx]) for q in range(len(nb_edges) - 1)])
        per["mu"]["sum_abs_T_over_diag"] = float(np.sum(np.abs(T_mu)) / diag[0])
        per["mu"]["sum_abs_pairterms_over_diag"] = float(Tabs / diag[0])
        # fraction of |T| mass and of the signed sum carried by the largest |T(h)|
        oT = np.argsort(-np.abs(T_mu))
        cs = np.cumsum(T_mu[oT])
        per["mu"]["signed_partial_sums_by_rank_over_diag"] = {str(r): float(cs[min(r, len(cs)) - 1] / diag[0])
                                                              for r in (10, 100, 1000, 10000, len(cs))}
        # the special dual rows individually: units and small sixth powers
        sel = np.nonzero(hcls == 0)[0]
        sel = sel[np.argsort(hN[sel])][:12]
        per["mu"]["T_at_sixth_rows_over_DDrow"] = [
            dict(h=[int(ha[s]), int(hb[s])], Nh=int(hN[s]), T_over_diag=float(T_mu[s] / diag[0])) for s in sel]
        for lab, sl in (("rand", slice(2, 2 + K)), ("randc", slice(2 + K, 2 + 2 * K))):
            dg = diag[sl]
            per[lab] = dict(off_over_diag_mean=float(np.mean(off_dual[sl] / dg)),
                            off_over_diag_std=float(np.std(off_dual[sl] / dg, ddof=1)),
                            DD_over_diag_mean=float(np.mean(DD[sl] / dg)),
                            by_hclass_over_diag={c: dict(mean=float(np.mean(offc[ci, sl] / dg)),
                                                         std=float(np.std(offc[ci, sl] / dg, ddof=1)))
                                                 for ci, c in enumerate(HCLS)},
                            by_Nh_over_diag=[dict(mean=float(np.mean(offb[q, sl] / dg)),
                                                  std=float(np.std(offb[q, sl] / dg, ddof=1)))
                                             for q in range(len(nb_edges) - 1)])
        per["n_h_by_class"] = {c: int(np.sum(hcls == ci)) for ci, c in enumerate(HCLS)}
        per["Nh_bins_over_dual_length"] = nb_edges[:-1] + ["inf"]
        res["per_rho"].append(per)
        print(f"D={D} rho={rho} Y={Y:.1f} #n={nc} #h={len(ha)} identity err={per['identity_maxrelerr']:.1e} "
              f"off direct-dual={per['offdirect_vs_dual_maxdiff']:.1e} | mu off/diag={per['mu']['off_over_diag']:+.4f} "
              f"DD/diag={per['mu']['DD_over_diag']:.1f} sum|T|/diag={per['mu']['sum_abs_T_over_diag']:.1f} "
              f"classes={ {c: round(v, 4) for c, v in per['mu']['by_hclass_over_diag'].items()} } "
              f"rand={per['rand']['off_over_diag_mean']:+.4f}+-{per['rand']['off_over_diag_std']:.4f} "
              f"randc={per['randc']['off_over_diag_mean']:+.4f}+-{per['randc']['off_over_diag_std']:.4f} "
              f"({time.time()-t0:.0f}s)", flush=True)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", default=[150, 300])
    ap.add_argument("--rhos", type=float, nargs="+", default=[0.5, 0.7, 0.9])
    ap.add_argument("--K", type=int, default=100)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    primes = E.prime_ideals(2 * max(args.D))
    E.self_test(primes, n_samples=20)
    out = dict(convention="Gaussian row weight exp(-pi N u / Y) over all u in Z[omega]; squarefree primary n "
                          "prime to 6, D < N n < 2D; e(z) = exp(4 pi i Im z / sqrt 3)", results=[])
    for D in args.D:
        out["results"].append(run(D, args.rhos, args.K, args.seed + D, primes))
        with open(args.out, "w") as fh:
            json.dump(out, fh, indent=0)


if __name__ == "__main__":
    main()
