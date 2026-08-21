"""E6 -- apply the calibrated law back to the zeta case.

Synthetic source whose poles sit exactly where O-16004 says the arithmetic poles sit:
    mu_k = gamma_k * Delta,   Delta = log(c)/(2 pi)
Then run the SAME detector and see how many gammas come back, at which accuracy.
This is a MODEL of the arithmetic run (the true Weil matrix is not a pure pole source),
so agreement tests the *resolution law*, not the arithmetic.
"""
import json, os
import mpmath as mp
from mpmath import mpf
import core

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zeros.json')


def gammas(n=90, dps=60):
    if os.path.exists(CACHE):
        d = json.load(open(CACHE))
        if len(d) >= n:
            old = mp.mp.dps
            mp.mp.dps = dps
            out = [mpf(s) for s in d[:n]]
            mp.mp.dps = old
            return out
    old = mp.mp.dps
    mp.mp.dps = dps
    out = [mp.im(mp.zetazero(k)) for k in range(1, n + 1)]
    mp.mp.dps = old
    json.dump([mp.nstr(g, 55) for g in out], open(CACHE, 'w'))
    return out


def run(c, N, G, K, weight_mode='flat', label=''):
    L = mp.log(c)
    Delta = L / (2 * mp.pi)
    ps = [g * Delta for g in G[:K]]
    if weight_mode == 'flat':
        w = [mpf(1)] * K
    elif weight_mode == 'inv':
        w = [1 / g for g in G[:K]]
    elif weight_mode == 'inv2':
        w = [1 / g ** 2 for g in G[:K]]
    info = core.detect(N, ps, w, extraprec=4000)
    rec_gamma = [r / Delta for r in info['pos_roots']]
    print(f"\n  c={c}  L={mp.nstr(L,6)}  Delta={mp.nstr(Delta,6)}  N={N}  K={K}  "
          f"weights={weight_mode}  budget N/2={N/2}  {label}")
    print(f"    mu_1={mp.nstr(ps[0],6)}  (node band is [-{N},{N}])   "
          f"mu_1/N={mp.nstr(ps[0]/N,4)}   max root residual {mp.nstr(max(info['resid']),3)}")
    print(f"    {'k':>3} {'gamma_k (true)':>20} {'recovered':>20} {'rel.err':>12} {'margin N-2k':>12}")
    for k in range(min(len(rec_gamma), 12)):
        if k < len(G):
            g = G[k]
            rr = min(rec_gamma, key=lambda x: abs(x - g))
            e = abs(rr - g) / g
            print(f"    {k+1:>3} {mp.nstr(g,16):>20} {mp.nstr(rr,16):>20} "
                  f"{mp.nstr(e,4):>12} {N-2*(k+1):>12}")
    print(f"    all recovered roots (gamma units): {[mp.nstr(x,9) for x in rec_gamma]}")
    return info, rec_gamma


if __name__ == '__main__':
    G = gammas(90)
    print("=" * 100)
    print("E6  zeta-positioned synthetic source")
    print("=" * 100)
    print("  first 8 gammas:", [mp.nstr(g, 12) for g in G[:8]])

    print("\n### the O-16004 run: c = 2000, N = 6, 8, 10")
    for N in (6, 8, 10):
        run(2000, N, G, 90)

    print("\n### does the count law survive a change of cutoff? (N=10)")
    for c in (50, 100, 500, 5000):
        run(c, 10, G, 90)

    print("\n### is the count law weight-robust?  (c=2000, N=10)")
    for wm in ('inv', 'inv2'):
        run(2000, 10, G, 90, weight_mode=wm)

    print("\n### how many zeros would larger N buy?  (c=2000)")
    for N in (12, 14, 16):
        run(2000, N, G, 90)
