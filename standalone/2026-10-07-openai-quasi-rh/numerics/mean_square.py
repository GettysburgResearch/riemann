"""
mean_square.py -- EMPIRICAL evaluation of the mean square in Proposition
thm:ms (eq. (ms); outline eq. intro-ms) of "The Quasi-Riemann Hypothesis"
(OpenAI, Oct 2026), with nu trivial and S = {(2), (lambda)}:

    A_u(D)   = sum_{n primary, squarefree, (n,6)=1} mu(n) chi_n(u) W(N(n)/D),
    S(D, H)  = sum_{u in O, 0 < N(u) <= H} |A_u(D)|^2,

W(y) = exp(4 - 1/((y-1)(2-y))) on (1,2), 0 elsewhere (a bump with max 1).
u runs over ALL nonzero elements of O (units and non-primary u included).

Usage:
    python3 -I mean_square.py OUT_JSON D_1 D_2 ... [--theta-max T] [--workers K]

For each D the values A_u(D) are computed once for 0 < N(u) <= D^(1+T)
(default T = 0.1) and S(D, H) is reported for H = D^(1+theta),
theta in {0, 0.05, 0.1} (those <= T).  Also reported:
  * diag(D,H) = sum_n W(N(n)/D)^2 #{u : 0<N(u)<=H, (u,n)=1}  (exact; this is
    S for perfectly orthogonal rows, i.e. the "diagonal" n1 = n2 terms);
  * the split of S into u = unit * v^6 (chi_n(u) = chi_n(unit) 1_{(n,v)=1}),
    u = unit * cube (not 6th power; quadratic twists), u = unit * square
    (not 6th power; cubic twists), and the rest;
  * A_1(D), A_unit(D), and A_{p^6}(D) - A_1(D) for small primes p
    (amplification step eq. A_u-vs-A_1), cross-checked against the direct
    formula A_{p^6} - A_1 = -sum_{p | n} mu(n) W(N(n)/D);
  * consistency checks: A_{conj u} = conj(A_u); A_{unit*lambda^6} = A_unit;
  * the normalised fourth moment E|A_u|^4/(E|A_u|^2)^2 over the "rest" rows
    (equal to 2 if the A_u were complex Gaussian).

Method: chi_p(u) for every prime ideal p and every u in a chunk is read off a
discrete-log-mod-6 table of the residue field (eisenstein.py; the tables are
validated against exact computation of u^{(N(p)-1)/6} mod p).  For n with
prime factors p_1..p_k the codes are added and mapped to complex values.
"""

import json
import math
import multiprocessing as mp
import os
import sys
import time

# one BLAS thread per worker process (the work is parallelised by processes)
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import eisenstein as E  # noqa: E402

CHUNK = 8192          # u's per work unit
NBLOCK = 32           # n's per block inside a work unit

# globals inherited by forked workers
G_PRIMES = None       # list of PrimeIdeal actually used (rows of the code matrix)
G_GROUPS = None       # list of (F (m,k) int32 row indices, w (m,) float64 = mu*W)
G_UA = G_UB = None    # u grid


def W(y):
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m = (y > 1) & (y < 2)
    out[m] = np.exp(4.0 - 1.0 / ((y[m] - 1) * (2 - y[m])))
    return out


def A_values(x, y):
    """A_u(D) for u = x + y*omega (int64 arrays), using the global n data."""
    codes = np.empty((len(G_PRIMES), len(x)), dtype=np.uint8)
    for i, P in enumerate(G_PRIMES):
        codes[i] = P.codes(x, y)
    A = np.zeros(len(x), dtype=np.complex128)
    for F, w in G_GROUPS:
        for b0 in range(0, len(w), NBLOCK):
            Fb = F[b0:b0 + NBLOCK]
            M = codes[Fb[:, 0]]
            for j in range(1, F.shape[1]):
                M += codes[Fb[:, j]]
            A += w[b0:b0 + NBLOCK].astype(np.complex128) @ E.VALUE[M]
    return A


def _work(bounds):
    lo, hi = bounds
    return lo, A_values(G_UA[lo:hi], G_UB[lo:hi])


def lattice_set(points):
    return {(int(a), int(b)) for a, b in points}


def special_sets(H):
    """u = unit*v^6, unit*v^3, unit*v^2 with N(u) <= H (as sets of pairs)."""
    out = {}
    for e in (6, 3, 2):
        vmax = H ** (1.0 / e)
        va, vb = E.nonzero_lattice(vmax)
        s = set()
        for v in zip(va.tolist(), vb.tolist()):
            ve = E.power(v, e)
            for eps in E.UNITS:
                s.add(E.mul(eps, ve))
        out[e] = s
    return out


def main():
    args = sys.argv[1:]
    out_json = args.pop(0)
    theta_max, workers = 0.1, os.cpu_count() or 1
    if "--theta-max" in args:
        i = args.index("--theta-max")
        theta_max = float(args[i + 1])
        del args[i:i + 2]
    if "--workers" in args:
        i = args.index("--workers")
        workers = int(args[i + 1])
        del args[i:i + 2]
    Ds = [int(a) for a in args]
    thetas = [t for t in (0.0, 0.05, 0.1) if t <= theta_max + 1e-12]

    global G_PRIMES, G_GROUPS, G_UA, G_UB
    t0 = time.time()
    Xmax = 2 * max(Ds)
    primes = E.prime_ideals(Xmax)
    nchk = E.self_test(primes, n_samples=100)
    sq = E.squarefree_primary(primes, Xmax)
    print(f"setup: {len(primes)} prime ideals, {len(sq)} squarefree n with N <= {Xmax}; "
          f"{nchk} exact table checks passed ({time.time()-t0:.1f}s)", flush=True)

    # integral of W^2 (for the heuristic normalisation printed below)
    yy = np.linspace(1, 2, 200001)
    intW2 = float(np.trapezoid(W(yy) ** 2, yy))
    results = []
    for D in Ds:
        t1 = time.time()
        ns = [(g, N, f) for g, N, f in sq if D < N < 2 * D]
        used = sorted({i for _, _, f in ns for i in f})
        row = {i: r for r, i in enumerate(used)}
        G_PRIMES = [primes[i] for i in used]
        wts = np.array([(-1) ** len(f) * W(N / D) for _, N, f in ns])
        groups = {}
        for (g, N, f), w in zip(ns, wts):
            groups.setdefault(len(f), ([], []))
            groups[len(f)][0].append([row[i] for i in f])
            groups[len(f)][1].append(w)
        G_GROUPS = [(np.array(F, dtype=np.int32), np.array(w)) for k, (F, w) in sorted(groups.items())]
        sumw2 = float(np.sum(wts ** 2))

        Hs = {th: D ** (1 + th) for th in thetas}
        Hmax = max(Hs.values())
        G_UA, G_UB = E.nonzero_lattice(Hmax)
        normu = G_UA * G_UA - G_UA * G_UB + G_UB * G_UB
        order = np.argsort(normu, kind="stable")
        G_UA, G_UB, normu = G_UA[order], G_UB[order], normu[order]
        nU = len(G_UA)

        jobs = [(lo, min(lo + CHUNK, nU)) for lo in range(0, nU, CHUNK)]
        A = np.empty(nU, dtype=np.complex128)
        ctx = mp.get_context("fork")
        with ctx.Pool(workers) as pool:
            for lo, vals in pool.imap_unordered(_work, jobs):
                A[lo:lo + len(vals)] = vals
        t2 = time.time()

        # ---- consistency checks -----------------------------------------
        key = G_UA * 10 ** 7 + G_UB
        sorter = np.argsort(key)
        ckey = (G_UA - G_UB) * 10 ** 7 + (-G_UB)
        cidx = sorter[np.searchsorted(key, ckey, sorter=sorter)]
        assert np.all(key[cidx] == ckey)
        conj_err = float(np.max(np.abs(A[cidx] - np.conj(A))))
        lookup = {(int(a), int(b)): i for i, (a, b) in enumerate(zip(G_UA.tolist(), G_UB.tolist()))
                  if normu[i] <= 4096}

        # ---- special u ---------------------------------------------------
        sp = special_sets(Hmax)
        is6 = np.array([(a, b) in sp[6] for a, b in zip(G_UA.tolist(), G_UB.tolist())])
        is3 = np.array([(a, b) in sp[3] for a, b in zip(G_UA.tolist(), G_UB.tolist())]) & ~is6
        is2 = np.array([(a, b) in sp[2] for a, b in zip(G_UA.tolist(), G_UB.tolist())]) & ~is6
        A_unit = {str(eps): A[lookup[eps]] for eps in E.UNITS}
        lam6 = E.power((1, 2), 6)                         # lambda^6 = -27
        lam6_err = max([abs(A[lookup[E.mul(eps, lam6)]] - A[lookup[eps]])
                        for eps in E.UNITS if E.norm(lam6) <= Hmax], default=float("nan"))
        A1 = A[lookup[(1, 0)]]

        # A_{p^6} for small primes (computed directly, also outside the grid)
        amp = []
        for P in primes[:8]:
            u6 = E.power(P.gen, 6)
            val = A_values(np.array([u6[0]], dtype=np.int64), np.array([u6[1]], dtype=np.int64))[0]
            # direct formula: A_{p^6} - A_1 = - sum_{p | n} mu(n) W(N(n)/D)
            pid = primes.index(P)
            direct = -sum(w for (g, N, f), w in zip(ns, wts) if pid in f)
            ntrivial = sum(abs(w) for (g, N, f), w in zip(ns, wts) if pid in f)
            amp.append(dict(p=list(P.gen), Np=P.N, A_p6=[val.real, val.imag],
                            diff=abs(val - A1), diff_direct=abs(direct),
                            check_err=abs((val - A1) - direct), trivial_bound=ntrivial))

        # ---- mean squares --------------------------------------------------
        absA2 = np.abs(A) ** 2
        Ls = np.sort(normu)

        def L(t):
            return int(np.searchsorted(Ls, t, side="right"))

        per_theta = []
        for th, H in Hs.items():
            m = normu <= H
            S = float(absA2[m].sum())
            diag = 0.0
            for (g, N, f), w in zip(ns, wts):
                tot = 0
                for mask in range(1 << len(f)):
                    Nd, sgn = 1, 1
                    for j in range(len(f)):
                        if mask >> j & 1:
                            Nd *= primes[f[j]].N
                            sgn = -sgn
                    tot += sgn * L(H / Nd)
                diag += w * w * tot
            rest = m & ~is6 & ~is3 & ~is2
            top = np.argsort(-absA2 * rest)[:5]
            per_theta.append(dict(
                theta=th, H=H, n_u=int(m.sum()), S=S, S_over_DH=S / (D * H),
                diag=diag, S_over_diag=S / diag,
                S_sixth=float(absA2[m & is6].sum()), n_sixth=int((m & is6).sum()),
                S_cube=float(absA2[m & is3].sum()), n_cube=int((m & is3).sum()),
                S_square=float(absA2[m & is2].sum()), n_square=int((m & is2).sum()),
                S_rest=float(absA2[rest].sum()), n_rest=int(rest.sum()),
                max_rest_over_sumw2=float(absA2[rest].max() / sumw2),
                top_rest_u=[[int(G_UA[i]), int(G_UB[i]), float(absA2[i] / sumw2)] for i in top],
                mean_cube_over_sumw2=float(absA2[m & is3].mean() / sumw2) if (m & is3).any() else None,
                mean_square_over_sumw2=float(absA2[m & is2].mean() / sumw2) if (m & is2).any() else None,
                mean_rest_over_sumw2=float(absA2[rest].mean() / sumw2),
                # E|A|^4 / (E|A|^2)^2 over the rest rows (= 2 for complex Gaussian A)
                fourth_moment_ratio_rest=float((absA2[rest] ** 2).mean() / absA2[rest].mean() ** 2),
                frac_S_sixth=float(absA2[m & is6].sum() / S),
            ))
        res = dict(D=D, n_count=len(ns), sum_w2=sumw2, sum_w2_over_D=sumw2 / D,
                   kmax=max(len(f) for _, _, f in ns), A1=[A1.real, A1.imag], absA1=abs(A1),
                   absA1_over_sqrt_sumw2=abs(A1) / math.sqrt(sumw2),
                   A_units={k: [v.real, v.imag, abs(v)] for k, v in A_unit.items()},
                   conj_symmetry_err=conj_err, lambda6_err=float(lam6_err),
                   amplification=amp, per_theta=per_theta,
                   seconds_A=t2 - t1, seconds_total=time.time() - t1)
        results.append(res)
        print(f"D={D}: #n={len(ns)}, #u={nU}, A computed in {t2-t1:.1f}s; |A_1|={abs(A1):.3f} "
              f"(sqrt(sum w^2)={math.sqrt(sumw2):.1f}); conj err {conj_err:.1e}, lambda^6 err {lam6_err:.1e}",
              flush=True)
        for r in per_theta:
            print(f"   theta={r['theta']:.2f} H={r['H']:.0f} #u={r['n_u']}: S/(DH)={r['S_over_DH']:.4f} "
                  f"S/diag={r['S_over_diag']:.4f} | sixth {r['S_sixth']:.3g} ({r['n_sixth']}), "
                  f"cube {r['S_cube']:.3g} ({r['n_cube']}), square {r['S_square']:.3g} ({r['n_square']}), "
                  f"rest {r['S_rest']:.4g}; max rest |A|^2/sum w^2 = {r['max_rest_over_sumw2']:.2f}; "
                  f"E|A|^4/(E|A|^2)^2 = {r['fourth_moment_ratio_rest']:.3f}",
                  flush=True)
        for a in amp[:4]:
            print(f"   N(p)={a['Np']}: |A_p6 - A_1| = {a['diff']:.3f} (direct {a['diff_direct']:.3f},"
                  f" err {a['check_err']:.1e}; sum_(p|n)|w| = {a['trivial_bound']:.2f})", flush=True)
        with open(out_json, "w") as fh:
            json.dump(dict(intW2=intW2, results=results), fh, indent=1)
    print(f"done in {time.time()-t0:.1f}s; wrote {out_json}")


if __name__ == "__main__":
    main()
