"""E4 -- BAND.  Is the recovery limit a fixed *height* (mu_max ~ C*N) or a
fixed *count* (~N/2 poles)?  Sweep the pole spacing S at fixed N.

If 'count' is the law, mu_max should scale with S.
If 'height' is the law, count should scale like 1/S.
"""
import mpmath as mp
from mpmath import mpf
import core

THR = [mpf('1e-6'), mpf('1e-3'), mpf('1e-1')]


def one(N, S, K, dps_extra=0):
    S = mpf(S)
    poles = [S / 2 + S * k for k in range(K)]
    w = [mpf(1)] * K
    info = core.detect(N, poles, w, extraprec=4000, dps_extra=dps_extra)
    m = core.match(info['pos_roots'], poles)
    out = {}
    for t in THR:
        good = [p for (r, p, e) in m if e < t]
        out[str(t)] = (len(good), max(good) if good else mpf(0))
    return info, m, out


if __name__ == '__main__':
    print("=" * 96)
    print("E4  band law: spacing sweep.  poles at mu_k = S/2 + S*k, a_k = 1, K chosen so max pole > 6N")
    print("=" * 96)
    rows = []
    for N in (6, 10, 14):
        for S in ('0.93', '1.85', '3.7', '7.4', '14.8'):
            Sm = mpf(S)
            K = int(mp.ceil(6 * N / Sm)) + 4
            K = max(K, N + 3)
            info, m, out = one(N, S, K)
            c6, mu6 = out[str(THR[0])]
            c3, mu3 = out[str(THR[1])]
            c1, mu1 = out[str(THR[2])]
            rows.append((N, Sm, K, c6, mu6, c3, mu3, c1, mu1, max(info['resid'])))
            print(f"N={N:>3} S={S:>6} K={K:>3} | err<1e-6: cnt={c6:>2} mu_max={mp.nstr(mu6,6):>8} "
                  f"mu_max/N={mp.nstr(mu6/N,4):>7} cnt/N={mp.nstr(mpf(c6)/N,4):>7} "
                  f"| err<1e-3: cnt={c3:>2} mu_max={mp.nstr(mu3,6):>8} mu_max/N={mp.nstr(mu3/N,4):>7} "
                  f"| err<0.1: cnt={c1:>2} mu_max={mp.nstr(mu1,6):>8}")
        print()

    print("=" * 96)
    print("E4b  dense limit: what happens when the pole spacing is below the node spacing 1?")
    print("=" * 96)
    for N in (10,):
        for S in ('0.25', '0.5', '0.93', '1.37'):
            Sm = mpf(S)
            K = int(mp.ceil(6 * N / Sm)) + 4
            info, m, out = one(N, S, K)
            c6, mu6 = out[str(THR[0])]
            c3, mu3 = out[str(THR[1])]
            print(f"N={N} S={S:>6} K={K:>4} | err<1e-6 cnt={c6:>2} mu_max={mp.nstr(mu6,6):>8}"
                  f" | err<1e-3 cnt={c3:>2} mu_max={mp.nstr(mu3,6):>8}"
                  f" | first 6 roots: {[mp.nstr(r,8) for r in info['pos_roots'][:6]]}")

    print()
    print("=" * 96)
    print("E4c  precision stability check (same case at dps+50)")
    print("=" * 96)
    for extra in (0, 50):
        info, m, out = one(10, '3.7', 30, dps_extra=extra)
        print(f"  dps={info['dps']}  roots: {[mp.nstr(r,16) for r in info['pos_roots'][:7]]}")
