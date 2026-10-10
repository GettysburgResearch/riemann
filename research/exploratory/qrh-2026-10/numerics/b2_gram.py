"""
b2_gram.py -- EMPIRICAL test of the Gram excess P_a^{1/6} in sum_m |A_m|^2 ([OAI] Prop.
probe-gram, TeX l. 8340-8354; BILINEAR_B2.md Sec. 1.3, 2.4).  binary64, not certified.

A_m = Y^{-1} sum_{s sf, Y < q_s < 2Y} W(q_s/Y) (q_s/Y)^{-1/2 + i v} gamma_1(s) conj chi_s(-m), rows
Q < q_m < 2Q with (m, 6) = 1 and weight W(q_m/Q).  gramA = sum_m w |A_m|^2 / sum_m w sum_s |a_s|^2
1_{(m,s)=1} (= 1 + off-diagonal / diagonal), for the true sextic Gauss sums gamma_1(s) and for
iid uniform phases on the same support.  Averaged over heights v = 0..NV-1.

Usage: python3 -I b2_gram.py OUT.json Q1 [Q2 ...]
"""
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import b2_common as C  # noqa: E402

E = C.E
NV = 8
NR = 12


def run(Q, Ys, seed=5):
    spf = C.spf_sieve(int(2 * Q) + 10)
    small = E.prime_ideals(int(2 * max(max(Ys), Q)) + 2)
    gidx = {P.gen: i for i, P in enumerate(small)}
    pr = C.Primes(int(2 * Q) + 2, spf)
    R = C.rows(Q, spf, pr, gidx)
    w = C.W(R["N"] / Q)
    rng = np.random.default_rng(seed)
    out = []
    for Y in Ys:
        t0 = time.time()
        fam = C.s_family(Y, small, gidx)
        Ns = np.array([N for _, N, _, _ in fam], dtype=float)
        g1 = np.array([v for _, _, _, v in fam])
        codes = C.s_codes(fam, small, R)
        base = (1.0 / Y) * C.W(Ns / Y) * (Ns / Y) ** -0.5
        coefs = [g1] + [np.exp(2j * np.pi * rng.random(len(fam))) for _ in range(NR)]
        # ZETA with zero for code ZERO, conjugated (conj chi_s(-m))
        zt = np.zeros(256, dtype=np.complex128)
        zt[:32] = np.conj(C.ZETA[np.arange(32) % 6])
        diag = np.zeros(len(w))
        res = np.zeros((NV, len(coefs)))
        for v in range(NV):
            A = np.zeros((len(coefs), len(w)), dtype=np.complex128)
            ys = (Ns / Y) ** (1j * v)
            for i in range(len(fam)):
                row = zt[codes[i]]
                for k, cf in enumerate(coefs):
                    A[k] += (base[i] * ys[i] * cf[i]) * row
                if v == 0:
                    diag += base[i] ** 2 * (codes[i] < C.ZERO)
            D = float(np.sum(w * diag))
            res[v] = np.sum(w * np.abs(A) ** 2, axis=1) / D
        true = float(res[:, 0].mean())
        rnd = res[:, 1:].mean(axis=0)
        rec = dict(Q=Q, Y=Y, P_a=Y * Y / Q, n_s=len(fam), rows=len(w), gramA_true=true,
                   gramA_rand_mean=float(rnd.mean()), gramA_rand_sd=float(rnd.std(ddof=1)),
                   z_true=float((true - rnd.mean()) / rnd.std(ddof=1)),
                   P_a_sixth=(Y * Y / Q) ** (1 / 6), P_a2_over_Y=(Y * Y / Q) ** 2 / Y,
                   t=round(time.time() - t0, 1))
        print(json.dumps(rec), flush=True)
        out.append(rec)
    return out


def main():
    outfn = sys.argv[1]
    allr = []
    for q in sys.argv[2:]:
        Q = int(float(q))
        Ys = sorted({int(round(Q ** e)) for e in (0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7)})
        allr += run(Q, Ys)
        json.dump(dict(NV=NV, NR=NR, records=allr), open(outfn, "w"), indent=0)


if __name__ == "__main__":
    main()
