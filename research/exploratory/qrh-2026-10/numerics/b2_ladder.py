"""
b2_ladder.py -- EMPIRICAL measurement of the low-side bilinear form of the 7/8 architecture
(BILINEAR_B2.md) against Cauchy-Schwarz, the large sieve, and random-phase controls.
binary64 throughout; nothing here is certified, and finite ladders prove nothing asymptotic.

Usage:  python3 -I b2_ladder.py OUT.json GEOM Z1 Z2 ...      (GEOM in {d0, dl})
        python3 -I b2_ladder.py --validate
GEOM d0: paper d = 0 exponents re-expressed in the primal theta length Z (= Z_paper^{7/6}):
         Q = Z^{5/7}, Y = Z^{23/56}  (P_a = Z^{3/28}).
GEOM dl: paper d = ell (fully rescaled, unmarked): Q = Z^{1/2}, Y = Z^{15/48} (P_a = Z^{1/8}).
"""
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import b2_common as C  # noqa: E402
from common import PrimeData  # noqa: E402  (moments/common.py)

E = C.E
NV = 16              # heights v = 9*j, j = 0..NV-1 (statistics over the fixed-height forms)
VSTEP = 9.0
NA_RAND = 8          # random-phase draws for gamma_1(s)


def log(*a):
    print(*a, flush=True)


def setup(Zmax, Qmax, Ymax):
    lib = C.load_kernel()
    spf = C.spf_sieve(int(2 * Zmax) + 10)
    g2 = C.gamma2_table(_g2_X(int(2 * Zmax) + 2), spf, lib, log=log)
    pr = C.Primes(int(2 * Zmax) + 2, spf)
    small = E.prime_ideals(int(max(2 * Qmax, 2 * Ymax, (2 * Zmax) ** (1 / 3))) + 2)
    gidx = {P.gen: i for i, P in enumerate(small)}
    pdat = PrimeData(small)
    return dict(lib=lib, spf=spf, g2=g2, pr=pr, small=small, gidx=gidx, pdat=pdat)


def _g2_X(X):
    best = None
    for f in os.listdir(C.SCR):
        if f.startswith("gamma2_") and f.endswith(".npz"):
            v = int(f[7:-4])
            if v >= X and (best is None or v < best):
                best = v
    return best if best else X


def compute_B(ctx, Z, R, T, K_weights):
    pd = ctx["pdat"]
    nc = C.ncodes(R, T["nlist"], ctx["small"], ctx["gidx"], ctx["spf"], ctx["pr"])
    Rt = ctx["Rtab"]
    wre = np.ascontiguousarray(K_weights.real)
    wim = np.ascontiguousarray(K_weights.imag)
    K = K_weights.shape[1]
    nm = len(R["a"])
    ore, oim = np.zeros(nm * K), np.zeros(nm * K)
    ctx["lib"].eval_B(pd.kind, pd.mod, pd.r, pd.off, pd.neg, pd.tables,
                      nm, R["u"], R["mcls"], R["rowptr"], R["ridx"], R["rexp"],
                      len(T["nlist"]), np.ascontiguousarray(nc), np.ascontiguousarray(Rt.ravel()),
                      len(T["cx"]), T["cx"], T["cy"], T["ucode"], T["ccls"], T["nidx"],
                      K, wre.ravel(), wim.ravel(), ore, oim)
    return (ore + 1j * oim).reshape(nm, K)


def B_direct(ctx, Z, R, T, i):
    """B_m for row i by exact symbols (a2/eis.py), validation only."""
    m = (int(R["a"][i]), int(R["b"][i]))
    tot = 0j
    for t in range(len(T["cx"])):
        c = (int(T["cx"][t]), int(T["cy"][t]))
        n = T["nlist"][T["nidx"][t]]
        fc = C.factor_element(c, E.norm(c), ctx["spf"], ctx["pr"])
        code = 0
        zero = False
        for g, e in fc:
            k = C.sym(m, g)
            if k is None:
                zero = True
                break
            code += e * k
        if zero:
            continue
        if n != (1, 0):
            for g, e in C.factor_element(n, E.norm(n), ctx["spf"], ctx["pr"]):
                k = C.sym(m, g)
                if k is None:
                    zero = True
                    break
                code += 3 * e * k
        if zero:
            continue
        tot += T["gamma2"][t] * T["weight"][t] * C.ZETA[code % 6]
    return tot


def rung(ctx, Z, Q, Y, seed=1):
    t0 = time.time()
    R = C.rows(Q, ctx["spf"], ctx["pr"], ctx["gidx"])
    T = C.theta_terms(Z, ctx["spf"], ctx["pr"], ctx["g2"], log=log)
    nt = len(T["cx"])
    rng = np.random.default_rng(seed)
    # weight vectors: true, iid phase per c (two draws), random cube root per prime
    u1 = np.exp(2j * np.pi * rng.random(nt))
    u2 = np.exp(2j * np.pi * rng.random(nt))
    # iid per c must be shared across n: reindex by c
    keyc = {}
    cid = np.array([keyc.setdefault((x, y), len(keyc)) for x, y in zip(T["cx"].tolist(),
                                                                      T["cy"].tolist())])
    ph1 = np.exp(2j * np.pi * rng.random(len(keyc)))[cid]
    ph2 = np.exp(2j * np.pi * rng.random(len(keyc)))[cid]
    del u1, u2
    Wt = np.stack([T["gamma2"] * T["weight"],
                   ph1 * T["weight"],
                   ph2 * T["weight"],
                   T["gamma2"] * C.ZETA[T["cubecode"]] * T["weight"]], axis=1)
    labels_B = ["true", "rand_c1", "rand_c2", "rand_cuberoot"]
    t1 = time.time()
    Bm = compute_B(ctx, Z, R, T, Wt)
    t2 = time.time()
    # s side
    fam = C.s_family(Y, ctx["small"], ctx["gidx"])
    Ns = np.array([N for _, N, _, _ in fam], dtype=float)
    g1 = np.array([v for _, _, _, v in fam])
    Phi = C.code_val(C.s_codes(fam, ctx["small"], R))          # chi_s(-m), shape (#s, #m)
    Phi = np.conj(Phi)                                          # conj chi_s(-m)
    base_s = (1.0 / Y) * C.W(Ns / Y) * (Ns / Y) ** -0.5
    alphas = [base_s * g1] + [base_s * np.exp(2j * np.pi * rng.random(len(fam)))
                              for _ in range(NA_RAND)]
    labels_A = ["true"] + [f"rand{j}" for j in range(NA_RAND)]
    w = C.W(R["N"] / Q)
    xi = R["xi"]
    mask = (w > 0).astype(float)
    # large-sieve constant of this configuration (coefficient-blind, sharp): lambda_max(Phi Phi*)
    G = (Phi * mask) @ Phi.conj().T
    lam = float(np.linalg.eigvalsh(G).max())
    nrows = int(mask.sum())
    res = dict(Z=Z, Q=Q, Y=Y, P_a=Y * Y / Q, rows=nrows, n_s=len(fam), n_terms=nt,
               n_c=len(keyc), lam_max=lam, trG=float(np.trace(G).real),
               t_setup=round(t1 - t0, 1), t_kernel=round(t2 - t1, 1))
    out = {}
    for kb, lb in enumerate(labels_B):
        B = Bm[:, kb]
        normB2 = float(np.sum(w * np.abs(B) ** 2))
        cell = dict(normB2_per_row=normB2 / float(w.sum()))
        for ja, la in enumerate(labels_A):
            if lb != "true" and la not in ("true", "rand0", "rand1"):
                continue
            rec = []
            for jv in range(NV):
                v = VSTEP * jv
                ys = (Ns / Y) ** (1j * v)
                yq = (R["N"] / Q) ** (-1j * v)
                bvec = w * xi * yq * B                          # b_m
                Bs = Phi @ bvec                                 # cal-B(conj chi_s), all s
                al = alphas[ja] * ys
                S = complex(al @ Bs)
                A = al @ Phi                                    # A_m (rows)
                nA2 = float(np.sum(w * np.abs(xi) ** 2 * np.abs(A) ** 2))
                nB2 = float(np.sum(w * np.abs(xi) ** 2 * np.abs(B) ** 2))
                CS = math.sqrt(nA2 * nB2)
                U = math.sqrt(float(np.sum((w * np.abs(xi) * np.abs(A * B)) ** 2)))
                Ls = float(np.sum(np.abs(Bs) ** 2))
                b2 = float(np.sum(np.abs(bvec) ** 2))
                Ds = float(np.sum((np.abs(Phi) ** 2) @ (np.abs(bvec) ** 2)))
                diagA = float(np.sum(w * np.abs(xi) ** 2 * ((np.abs(al) ** 2) @ (np.abs(Phi) ** 2))))
                rec.append(dict(S_over_CS=abs(S) / CS, S_over_U=abs(S) / U,
                                Ls_over_lamb2=Ls / (lam * b2), Ls_over_Ds=Ls / Ds,
                                gramA=nA2 / diagA,
                                sroute_LS_over_CS=math.sqrt(float(np.sum(np.abs(al) ** 2)) * lam * b2) / CS))
            agg = {}
            for key in rec[0]:
                arr = np.array([r[key] for r in rec])
                if key == "S_over_CS" or key == "S_over_U":
                    agg[key + "_rms"] = float(np.sqrt(np.mean(arr ** 2)))
                    agg[key + "_v0"] = float(arr[0])
                else:
                    agg[key] = float(np.mean(arr))
            cell[la] = agg
        out[lb] = cell
    res["cells"] = out
    res["t_total"] = round(time.time() - t0, 1)
    return res


def validate():
    Z, Q, Y = 3000, 300, 60
    ctx = setup(Z, Q, Y)
    rep = {}
    # R table from small primes, then check on composite and non-squarefree pairs
    P = [p.gen for p in ctx["small"] if p.N < 3000]
    Rt, viol, filled = C.build_R_table(P, 6000)
    ctx["Rtab"] = (Rt * 1).astype(np.uint8)
    rep["R_table"] = dict(violations=viol, filled_classes=filled)
    rng = np.random.default_rng(3)
    bad = 0
    tests = 0
    a, b, N = C.primary_lattice(50, 6000)
    keep = N % 2 == 1
    a, b, N = a[keep], b[keep], N[keep]
    for _ in range(3000):
        i, j = rng.integers(0, len(a), 2)
        x, y = (int(a[i]), int(b[i])), (int(a[j]), int(b[j]))
        fx = C.factor_element(x, int(N[i]), ctx["spf"], ctx["pr"])
        fy = C.factor_element(y, int(N[j]), ctx["spf"], ctx["pr"])
        if {g for g, _ in fx} & {g for g, _ in fy}:
            continue
        k1 = sum(e * C.sym(x, g) for g, e in fy) % 6          # chi_y(x)
        k2 = sum(e * C.sym(y, g) for g, e in fx) % 6          # chi_x(y)
        tests += 1
        bad += int((k1 - k2 - int(Rt[C.cls4(*x), C.cls4(*y)])) % 6 != 0)
    rep["R_composite_check"] = dict(pairs=tests, failures=bad)
    # unit codes: chi_c(zeta) vs exact
    badu = 0
    for p in P[:200]:
        badu += int(C.sym((1, 1), p) != (E.norm(p) - 1) // 6 % 6)
    rep["unit_code_failures"] = badu
    # gamma_2 composite vs direct; gamma_1 vs direct
    T = C.theta_terms(Z, ctx["spf"], ctx["pr"], ctx["g2"])
    dev = 0
    for t in range(0, len(T["cx"]), max(1, len(T["cx"]) // 25)):
        c = (int(T["cx"][t]), int(T["cy"][t]))
        if E.norm(c) > 2500:
            continue
        fc = [g for g, _ in C.factor_element(c, E.norm(c), ctx["spf"], ctx["pr"])]
        dev = max(dev, abs(T["gamma2"][t] - C.eis.gamma(2, fc)))
    rep["gamma2_composite_maxdev"] = dev
    fam = C.s_family(Y, ctx["small"], ctx["gidx"])
    dev1 = 0
    for g, Nn, f, v in fam[:30]:
        dev1 = max(dev1, abs(v - C.eis.gamma(1, [ctx["small"][i].gen for i in f])))
    rep["gamma1_maxdev"] = dev1
    rep["n_s"] = len(fam)
    # kernel B_m vs exact direct evaluation
    R = C.rows(Q, ctx["spf"], ctx["pr"], ctx["gidx"])
    Wt = np.stack([T["gamma2"] * T["weight"]], axis=1)
    Bm = compute_B(ctx, Z, R, T, Wt)[:, 0]
    idx = rng.choice(len(R["a"]), 30, replace=False)
    devB = max(abs(Bm[i] - B_direct(ctx, Z, R, T, i)) for i in idx)
    rep["B_kernel_vs_direct_maxdev"] = devB
    rep["B_rms"] = float(np.sqrt(np.mean(np.abs(Bm) ** 2)))
    # A_m via Gauss sums directly: q_s^{-1/2} g_{chi_s}(s, -m) = gamma_1(s) conj chi_s(-m)
    Phi = np.conj(C.code_val(C.s_codes(fam, ctx["small"], R)))
    devA = 0
    for si in range(0, len(fam), max(1, len(fam) // 4)):
        g, Nn, f, v = fam[si]
        s = g
        res_, Ns = C.eis.residues(s)
        for mi in idx[:5]:
            m = (int(R["a"][mi]), int(R["b"][mi]))
            tot = 0
            for d in res_:
                k = C.eis.chi([ctx["small"][i].gen for i in f], d)
                if k is None:
                    continue
                tot += C.ZETA[k] * C.eis.e_of(C.E.mul((-m[0], -m[1]), d), s)
            devA = max(devA, abs(tot / math.sqrt(Ns) - v * Phi[si, mi]))
    rep["A_gauss_identity_maxdev"] = devA
    return rep


def main():
    if sys.argv[1] == "--validate":
        rep = validate()
        log(json.dumps(rep, indent=1, default=float))
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "b2_validate.json")
        json.dump(rep, open(out, "w"), indent=1, default=float)
        return
    outfn, geom = sys.argv[1], sys.argv[2]
    Zs = [float(z) for z in sys.argv[3:]]
    if geom == "d0":
        QY = [(z, z ** (5 / 7), z ** (23 / 56)) for z in Zs]
    elif geom == "dl":
        QY = [(z, z ** 0.5, z ** (15 / 48)) for z in Zs]
    else:
        raise SystemExit(geom)
    QY = [(int(round(z)), int(round(q)), int(round(y))) for z, q, y in QY]
    ctx = setup(max(z for z, _, _ in QY), max(q for _, q, _ in QY), max(y for _, _, y in QY))
    P = [p.gen for p in ctx["small"] if p.N < 3000]
    Rt, viol, filled = C.build_R_table(P, 6000)
    assert viol == 0, viol
    ctx["Rtab"] = Rt
    results = dict(geometry=geom, NV=NV, NA_RAND=NA_RAND, rungs=[])
    for Z, Q, Y in QY:
        log(f"rung Z={Z} Q={Q} Y={Y}")
        r = rung(ctx, Z, Q, Y)
        log(json.dumps({k: v for k, v in r.items() if k != "cells"}))
        for lb, cell in r["cells"].items():
            for la, agg in cell.items():
                if isinstance(agg, dict):
                    log(f"   B={lb:14s} A={la:6s} " + " ".join(f"{k}={v:.4g}" for k, v in agg.items()))
                else:
                    log(f"   B={lb:14s} {la}={agg:.4g}")
        results["rungs"].append(r)
        json.dump(results, open(outfn, "w"), indent=0, default=float)


if __name__ == "__main__":
    main()
