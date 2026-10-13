"""
amp_moments.py -- EMPIRICAL (floating point, finite) amplified mean squares of the
sextic Moebius family of the Oct 5 manuscript (external, unreviewed):

    A_u(D)   = sum_n mu(n) chi_n(u) W(N n / D)          (n squarefree primary, (n,6)=1)
    Amp_u    = sum_{l prime, N l <= L} x_l chi_l(u)      (row twists = Hecke values psi_u(l))
    M_amp    = sum_{0 < N u <= H} |Amp_u|^2 |A_u(D)|^2.

Reuses ../../moments/common.py, eisenstein.py and sextic_kernel.c unchanged
(read, not modified).  Single thread.  Nothing here proves anything.

Reported per (D, L, H, design):
  ratio_b   = M_amp / Diag_b,  Diag_b = n_u * sum_m |b_m|^2 prod_{p|m}(1 - 1/Np),
              b = x * (mu W) the amplified column vector (m = l n as ideals);
  decor     = M_amp * n_u / (sum|Amp|^2 * sum|A|^2)   (1 = amplifier uncorrelated with |A|^2);
  P_share   = share of M_amp from the principal rows u = v^6 (unit 1);
  P_pred    = n_P * |sum x|^2 * |A_1|^2 / M_amp (the "principal term" of the leverage count);
  sixth_share = share from all rows unit*v^6.
Designs: 'prime' (x_l = 1 on primes) and 'randphase' (x_l = e(theta_l), fixed seed): control.

Usage: python3 -I amp_moments.py OUT.json --D 1000 2000 --L 13 31 61 --Hfac 1 4
"""
import argparse
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MOM = os.path.normpath(os.path.join(HERE, "..", "..", "moments"))
sys.path.insert(0, MOM)
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402

OFF = 1 << 22


def key(a, b):
    return (np.asarray(a, dtype=np.int64) + OFF) * (2 * OFF) + (np.asarray(b, dtype=np.int64) + OFF)


def power_keys(Hmax, e, units):
    va, vb = E.nonzero_lattice(Hmax ** (1.0 / e) + 1e-9)
    pa, pb = va.copy(), vb.copy()
    for _ in range(e - 1):
        pa, pb = pa * va - pb * vb, pa * vb + pb * va - pb * vb
    ks = []
    for ea, eb in units:
        ua, ub = ea * pa - eb * pb, ea * pb + eb * pa - eb * pb
        ks.append(key(ua, ub))
    return np.unique(np.concatenate(ks))


def diag_b(primes, facs, w, amp_idx, x):
    """sum_m |b_m|^2 prod_{p|m}(1-1/Np) for b = x * w, m = l*n as a multiset of primes."""
    b = {}
    for li, xl in zip(amp_idx, x):
        for f, wn in zip(facs, w):
            m = tuple(sorted(f + (li,)))
            b[m] = b.get(m, 0.0) + xl * wn
    tot = 0.0
    for m, v in b.items():
        loc = 1.0
        for p in set(m):
            loc *= 1.0 - 1.0 / primes[p].N
        tot += abs(v) ** 2 * loc
    return tot, len(b)


def run(lib, primes, pd, D, Ls, Hfacs, designs, chunk_pts=2_000_000):
    t0 = time.time()
    ns, facs, norms, w = C.family(primes, D)
    treeA = C.Tree(facs, w)
    diagA_unit = float(sum(wn ** 2 * np.prod([1 - 1 / primes[p].N for p in f]) for f, wn in zip(facs, w)))
    out = []
    rng = np.random.default_rng(12345)
    Lmax = max(Ls)
    amp_all = [i for i, P in enumerate(primes) if P.N <= Lmax]
    phases = np.exp(2j * np.pi * rng.random(len(amp_all)))
    jobs = []
    for L in Ls:
        idx = [i for i in amp_all if primes[i].N <= L]
        for des in designs:
            if des == "prime":
                x = np.ones(len(idx), dtype=complex)
            else:
                x = phases[:len(idx)]
            jobs.append((L, des, idx, x))
    Hmax = max(D * L * hf for L in Ls for hf in Hfacs)
    sb, sa0, slen = C.lattice_segments(Hmax, points=False)
    k6 = power_keys(Hmax, 6, [(1, 0)])
    k6all = power_keys(Hmax, 6, E.UNITS)
    starts = np.concatenate([[0], np.cumsum(slen)])
    total = int(starts[-1])
    cuts = np.searchsorted(starts, np.arange(chunk_pts, total, chunk_pts))
    bounds = [0] + sorted(set(int(c) for c in cuts if 0 < c < len(slen))) + [len(slen)]
    # accumulators per job and H
    Hlist = sorted({D * L * hf for L in Ls for hf in Hfacs})
    acc = {}
    trees = []
    for (L, des, idx, x) in jobs:
        # Tree supports real weights only: split x into real and imaginary trees
        tr = C.Tree([(i,) for i in idx], list(x.real))
        ti = C.Tree([(i,) for i in idx], list(x.imag))
        trees.append((tr, ti))
    A1 = None
    for g0, g1 in zip(bounds[:-1], bounds[1:]):
        gs = (sb[g0:g1], sa0[g0:g1], slen[g0:g1])
        A = C.eval_rows(lib, pd, treeA, gs, workers=1, nchunks=1)
        a = np.concatenate([np.arange(s, s + n, dtype=np.int64) for s, n in zip(gs[1], gs[2])])
        bb = np.repeat(gs[0], gs[2])
        N = a * a - a * bb + bb * bb
        mult = np.where(bb == 0, 1.0, 2.0)
        kk = key(a, bb)
        isP = np.isin(kk, k6)
        is6 = np.isin(kk, k6all)
        hit = np.nonzero((a == 1) & (bb == 0))[0]
        if len(hit):
            A1 = complex(A[hit[0]])
        xA = np.abs(A) ** 2
        for j, (L, des, idx, x) in enumerate(jobs):
            tr, ti = trees[j]
            Amp = C.eval_rows(lib, pd, tr, gs, workers=1, nchunks=1) + 1j * C.eval_rows(lib, pd, ti, gs, workers=1, nchunks=1)
            xAmp = np.abs(Amp) ** 2
            prod = xAmp * xA
            for H in Hlist:
                if all(abs(H - D * L * hf) > 1e-6 for hf in Hfacs):
                    continue
                m = N <= H
                s = acc.setdefault((j, H), np.zeros(8))
                s[0] += (mult * m).sum()
                s[1] += (mult * xA * m).sum()
                s[2] += (mult * xAmp * m).sum()
                s[3] += (mult * prod * m).sum()
                s[4] += (mult * prod * (m & isP)).sum()
                s[5] += (mult * (m & isP)).sum()
                s[6] += (mult * prod * (m & is6)).sum()
                s[7] += (mult * xA * (m & isP)).sum()
    for j, (L, des, idx, x) in enumerate(jobs):
        db, nm = diag_b(primes, facs, w, idx, x)
        sumx2 = float(np.sum(np.abs(x) ** 2))
        sumx = complex(np.sum(x))
        for hf in Hfacs:
            H = D * L * hf
            s = acc[(j, H)]
            n_u, SA, SAmp, M, MP, nP, M6, SAP = s
            rec = dict(D=D, L=L, design=des, Hfac=hf, H=H, n_amp=len(idx), sum_x2=sumx2,
                       abs_sum_x2=abs(sumx) ** 2, n_u=n_u, n_m=nm,
                       M_amp=M, Diag_b=n_u * db, ratio_b=M / (n_u * db),
                       ratio_A=SA / (n_u * diagA_unit),
                       decor=M * n_u / (SAmp * SA), P_share=MP / M, n_P=nP,
                       P_pred=nP * abs(sumx) ** 2 * abs(A1) ** 2 / M if A1 is not None else None,
                       sixth_share=M6 / M, A1_abs=abs(A1) if A1 is not None else None,
                       meanA2_P=SAP / max(nP, 1), SA=SA, SAmp=SAmp, MP=MP,
                       enrich=(MP / M) / (nP * abs(A1) ** 2 / SA) if A1 is not None and nP > 0 else None)
            out.append(rec)
            print(f"D={D} L={L} {des:9s} H={hf:g}DL n_u={n_u:.0f} #l={len(idx)} ratio_b={rec['ratio_b']:.3f} "
                  f"ratio_A={rec['ratio_A']:.3f} decor={rec['decor']:.3f} P_share={rec['P_share']:.4f} "
                  f"P_pred={rec['P_pred']:.4f} 6share={rec['sixth_share']:.4f}", flush=True)
    print(f"  D={D} done in {time.time()-t0:.1f}s |A1|={abs(A1):.2f}", flush=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", required=True)
    ap.add_argument("--L", type=int, nargs="+", required=True)
    ap.add_argument("--Hfac", type=float, nargs="+", default=[1.0])
    ap.add_argument("--designs", nargs="+", default=["prime", "randphase"])
    args = ap.parse_args()
    lib = C.load_kernel()
    primes = E.prime_ideals(2 * max(max(args.D), max(args.L)))
    E.self_test(primes, n_samples=20)
    pd = C.PrimeData(primes)
    res = []
    for D in args.D:
        res += run(lib, primes, pd, D, args.L, args.Hfac, args.designs)
        with open(args.out, "w") as fh:
            json.dump(dict(note="EMPIRICAL, floating point, finite; see amp_moments.py docstring",
                           results=res), fh, indent=1)


if __name__ == "__main__":
    main()
