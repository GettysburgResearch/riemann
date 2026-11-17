#!/usr/bin/env python3
"""SKEPTIC replay of C2-05 (DH right edge) and C2-11 (Epstein x^2+5y^2 right edge).

Independent implementation: segmented numpy sieve, float64 partial sums with an explicit rounding-error
allowance (relative 1e-12 of the sum, far above the true float64 error), Rosser-Schoenfeld
pi(x) < 1.25506 x/log x tail exactly as in the claims.  Also recomputes the targets
pi - 2 arctan(kappa) (DH) and pi (Epstein), and the PNT-heuristic edge.
Usage: python3 sk_edges.py OUTDIR [P]
"""
import sys, os, json, time, math
import numpy as np
import mpmath as mp


def sieve_segmented(P, seg=10_000_000):
    small = np.ones(int(P ** 0.5) + 2, dtype=bool); small[:2] = False
    for i in range(2, int(len(small) ** 0.5) + 1):
        if small[i]:
            small[i * i::i] = False
    sp = np.nonzero(small)[0]
    out = []
    for lo in range(0, P + 1, seg):
        hi = min(lo + seg, P + 1)
        a = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            a[:2] = False
        for p in sp:
            if p * p >= hi:
                break
            st = max(p * p, ((lo + p - 1) // p) * p)
            a[st - lo::p] = False
        out.append(np.nonzero(a)[0] + lo)
    return np.concatenate(out)


def main():
    P = int(sys.argv[2]) if len(sys.argv) > 2 else 100_000_000
    t0 = time.time()
    pr = sieve_segmented(P)
    res = dict(P=P, n_primes=int(pr.size))
    # ---- DH ----
    mp.mp.dps = 30
    k = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    target = float(mp.pi - 2 * mp.atan(k))
    p23 = pr[(pr % 5 == 2) | (pr % 5 == 3)].astype(float)
    def S_dh(sig):
        return float(np.sum(2 * np.arctan(p23 ** (-sig))))
    def tail(sig, c):
        return c * 1.25506 * sig * P ** (1 - sig) / ((sig - 1) * math.log(P))
    dh = {}
    for sig in [1.13514, 1.13513504, 1.11464, 1.1146350377]:
        part = S_dh(sig)
        dh[str(sig)] = dict(partial=part, upper=part * (1 + 1e-12) + tail(sig, 2), lower=part * (1 - 1e-12))
    # bisection of the partial-sum root and of partial+PNT tail
    def root(fun):
        lo, hi = 1.0001, 3.0
        for _ in range(60):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if fun(m) > target else (lo, m)
        return (lo + hi) / 2
    dh['root_partial'] = root(S_dh)
    dh['root_partial_plus_PNT_tail'] = root(lambda s: S_dh(s) + float(mp.e1((s - 1) * math.log(P))))
    dh['root_rigorous_upper_bound_for_edge'] = root(lambda s: S_dh(s) * (1 + 1e-12) + tail(s, 2))
    dh['target_pi_minus_2atan_kappa'] = target
    res['DH'] = dh
    # ---- Epstein x^2+5y^2 ----
    p37 = pr[(pr % 20 == 3) | (pr % 20 == 7)].astype(float)
    def S_ep(sig):
        return 2 * math.atan(2 ** (-sig)) + float(np.sum(4 * np.arctan(p37 ** (-sig))))
    ep = {}
    for sig in [1.17816, 1.12806]:
        part = S_ep(sig)
        ep[str(sig)] = dict(partial=part, upper=part * (1 + 1e-12) + tail(sig, 4), lower=part * (1 - 1e-12))
    targ = math.pi
    def root2(fun):
        lo, hi = 1.0001, 4.0
        for _ in range(60):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if fun(m) > targ else (lo, m)
        return (lo + hi) / 2
    ep['root_partial'] = root2(S_ep)
    # heuristic tail: primes = 3,7 mod 20 have density 2/8 = 1/4: sum_{p>P} 4 p^-s ~ E1((s-1)log P)
    ep['root_partial_plus_PNT_tail'] = root2(lambda s: S_ep(s) + float(mp.e1((s - 1) * math.log(P))))
    ep['root_rigorous_upper_bound_for_edge'] = root2(lambda s: S_ep(s) * (1 + 1e-12) + tail(s, 4))
    res['Epstein_x2+5y2'] = ep
    res['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(res, open(os.path.join(sys.argv[1], 'sk_edges.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
