"""
tm_twisted.py -- EMPIRICAL (floating point, finite) row-twisted mean squares

    T(l, l') = sum_{0 < N u <= H} chi_l(u) conj(chi_l'(u)) |A_u(D)|^2,   H = D^(1+theta),

for prime ideals l, l' (prime to 6) with N l, N l' <= Lmax, i.e. the Gram matrix G whose
quadratic form x^* G x is the amplified mean square M_amp(x).  Tests the hypothesis TM_eta of
README.md section 4 (power saving in the twist conductor N(l l')) and measures the empirical
kappa of the prime amplifier at H = D^(1+theta) (NOT H = D L).

Reuses ../../moments/{common,eisenstein}.py and sextic_kernel.c unchanged.  Single thread.
Usage: python3 -I tm_twisted.py OUT.json --D 2000 8000 --theta 0.1 --Lmax 211
"""
import argparse
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "moments")))
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402

OFF = 1 << 22


def key(a, b):
    return (np.asarray(a, dtype=np.int64) + OFF) * (2 * OFF) + (np.asarray(b, dtype=np.int64) + OFF)


def sixth_keys(Hmax):
    va, vb = E.nonzero_lattice(Hmax ** (1.0 / 6) + 1e-9)
    pa, pb = va.copy(), vb.copy()
    for _ in range(5):
        pa, pb = pa * va - pb * vb, pa * vb + pb * va - pb * vb
    return np.unique(key(pa, pb))


def run(lib, primes, pd, D, theta, Lmax):
    t0 = time.time()
    H = float(D) ** (1 + theta)
    ns, facs, norms, w = C.family(primes, D)
    treeA = C.Tree(facs, w)
    lidx = [i for i, P in enumerate(primes) if P.N <= Lmax]
    bmax = int(2 * math.sqrt(H / 3)) + 2
    segs, (a, b, N) = C.lattice_segments(H, bmin=-bmax)
    A = C.eval_rows(lib, pd, treeA, segs, workers=1, nchunks=1)
    wA = np.abs(A) ** 2
    V = np.empty((len(a), len(lidx)), dtype=complex)
    for j, i in enumerate(lidx):
        tr = C.Tree([(i,)], [1.0])
        V[:, j] = C.eval_rows(lib, pd, tr, segs, workers=1, nchunks=1)
    G = (V.conj().T * wA) @ V            # G[l,l'] = sum conj(chi_l) chi_l' |A|^2
    G = G.conj()                         # -> sum chi_l conj(chi_l') |A|^2
    isP = np.isin(key(a, b), sixth_keys(H))
    GP = (V[isP].conj().T * wA[isP]) @ V[isP]
    GP = GP.conj()
    L = len(lidx)
    d = np.real(np.diag(G))
    dm = d.mean()
    off = [(abs(G[i, j]) / math.sqrt(d[i] * d[j]), primes[lidx[i]].N * primes[lidx[j]].N)
           for i in range(L) for j in range(L) if i < j]
    offv = np.array([o for o, _ in off])
    offN = np.array([n for _, n in off], dtype=float)
    one = np.ones(L)
    Mamp = float(np.real(one @ G @ one))
    MampP = float(np.real(one @ GP @ one))
    evals = np.linalg.eigvalsh((G + G.conj().T) / 2)
    M1 = float(wA.sum())
    rand_scale = math.sqrt(float((wA ** 2).sum())) / M1      # |T|/M for random unimodular twists
    # slope of log(off) against log N(l l') (TM_eta would give slope -eta)
    sl = np.polyfit(np.log(offN), np.log(offv), 1)[0]
    # split by conductor-norm terciles
    qs = np.quantile(offN, [0, 1 / 3, 2 / 3, 1])
    terc = []
    for k in range(3):
        m = (offN >= qs[k]) & (offN <= qs[k + 1])
        terc.append(dict(Nr_lo=float(qs[k]), Nr_hi=float(qs[k + 1]),
                         median_off=float(np.median(offv[m])), rms_off=float(np.sqrt(np.mean(offv[m] ** 2)))))
    res = dict(D=D, theta=theta, H=H, n_u=len(a), n_l=L, Lmax=Lmax, M1=M1,
               diag_mean_over_M1=float(dm / M1),
               M_amp_over_L_diag=Mamp / (L * dm),
               kappa_emp=math.log(Mamp / (L * dm)) / math.log(L),
               principal_share=MampP / Mamp, n_principal=int(isP.sum()),
               lambda_max_over_diag=float(evals[-1] / dm),
               lambda_min_over_diag=float(evals[0] / dm),
               off_rms=float(np.sqrt(np.mean(offv ** 2))), off_max=float(offv.max()),
               random_twist_scale=rand_scale, slope_logoff_vs_logNr=float(sl),
               terciles=terc, A1_abs=float(abs(A[(a == 1) & (b == 0)][0])), seconds=time.time() - t0)
    print(f"D={D} th={theta} n_u={len(a)} #l={L} Mamp/(L diag)={res['M_amp_over_L_diag']:.4f} "
          f"kappa_emp={res['kappa_emp']:+.4f} lam_max/diag={res['lambda_max_over_diag']:.3f} "
          f"off_rms={res['off_rms']:.4f} rand={rand_scale:.4f} slope={sl:+.3f} P_share={res['principal_share']:.2e} "
          f"({res['seconds']:.1f}s)", flush=True)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--D", type=int, nargs="+", required=True)
    ap.add_argument("--theta", type=float, nargs="+", default=[0.1])
    ap.add_argument("--Lmax", type=int, default=211)
    args = ap.parse_args()
    lib = C.load_kernel()
    primes = E.prime_ideals(2 * max(max(args.D), args.Lmax))
    E.self_test(primes, n_samples=20)
    pd = C.PrimeData(primes)
    out = []
    for D in args.D:
        for th in args.theta:
            out.append(run(lib, primes, pd, D, th, args.Lmax))
            with open(args.out, "w") as fh:
                json.dump(dict(note="EMPIRICAL, floating point, finite; see tm_twisted.py", results=out), fh, indent=1)


if __name__ == "__main__":
    main()
