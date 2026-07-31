"""E2 -- RESOLUTION.  Two poles at distance d: smallest d still separated.

Background: comb of K poles at spacing 5 starting at 2.5, all weights 1
(K > N so the apparatus is in the truncated regime, like the arithmetic case).
The comb element with index k0 (height m0 = 2.5+5*k0) is REPLACED by a pair
m0 -+ d/2, each of weight 1.

Success criterion: the recovered root set contains r1<r2 with
    |r1 - (m0-d/2)| < tol*d   and   |r2 - (m0+d/2)| < tol*d,   tol = 0.1
i.e. the gap is reproduced to 10% of itself.
"""
import mpmath as mp
from mpmath import mpf
import core

SP = mpf('5.11')
BASE = mpf('2.63')   # offset chosen so poles never land on integer nodes


def poles_with_pair(K, k0, d):
    ps, ws = [], []
    for k in range(K):
        m = BASE + SP * k
        if k == k0:
            ps += [m - d / 2, m + d / 2]
            ws += [mpf(1), mpf(1)]
        else:
            ps.append(m)
            ws.append(mpf(1))
    return ps, ws


def separated(N, k0, d, K, tol=mpf('0.1'), dps_extra=0, verbose=False):
    d = mpf(d)
    m0 = BASE + SP * k0
    ps, ws = poles_with_pair(K, k0, d)
    info = core.detect(N, ps, ws, extraprec=4000, dps_extra=dps_extra)
    r = info['pos_roots']
    tgt1, tgt2 = m0 - d / 2, m0 + d / 2
    if len(r) < 2:
        return False, info, None
    near = sorted(r, key=lambda x: abs(x - m0))[:2]
    near.sort()
    ok = abs(near[0] - tgt1) < tol * d and abs(near[1] - tgt2) < tol * d
    if verbose:
        print(f"      d={mp.nstr(d,6):>10} pair=({mp.nstr(tgt1,10)},{mp.nstr(tgt2,10)}) "
              f"got=({mp.nstr(near[0],10)},{mp.nstr(near[1],10)}) "
              f"d_rec/d={mp.nstr((near[1]-near[0])/d,6)}  {'SEP' if ok else 'merged'}")
    return ok, info, near


def dmin(N, k0, K, lo='1e-5', hi='3.0', iters=26, tol=mpf('0.1')):
    lo, hi = mpf(lo), mpf(hi)
    ok_hi, _, _ = separated(N, k0, hi, K, tol)
    if not ok_hi:
        return None  # even the widest gap is not separated
    ok_lo, _, _ = separated(N, k0, lo, K, tol)
    if ok_lo:
        return lo  # no floor found within range
    for _ in range(iters):
        mid = mp.sqrt(lo * hi)
        ok, _, _ = separated(N, k0, mid, K, tol)
        if ok:
            hi = mid
        else:
            lo = mid
    return hi


if __name__ == '__main__':
    print("=" * 90)
    print("E2a  d_rec/d as d shrinks (illustrative), N=12, pair at m0=7.5, K=25 comb poles")
    print("=" * 90)
    for d in ('3', '2', '1.5', '1.2', '1.0', '0.8', '0.6', '0.4', '0.2', '0.1', '0.05'):
        separated(12, 1, d, 25, verbose=True)

    print()
    print("=" * 90)
    print("E2b  d_min vs N   (pair at m0 = 7.5, comb spacing 5, K = 25)")
    print("=" * 90)
    for N in (6, 8, 10, 12, 14, 16):
        dm = dmin(N, 1, 25)
        s = mp.nstr(dm, 6) if dm is not None else "not separated at any d<=3"
        print(f"   N={N:>3}   d_min = {s:>12}"
              + (f"   d_min*N = {mp.nstr(dm*N,5)}" if dm is not None else ""))

    print()
    print("=" * 90)
    print("E2c  d_min vs position in the band  (N = 14, comb spacing 5, K = 25)")
    print("     node band is [-14,14]; m0 = 2.5+5*k0")
    print("=" * 90)
    for k0 in range(0, 7):
        m0 = BASE + SP * k0
        dm = dmin(14, k0, 25)
        s = mp.nstr(dm, 6) if dm is not None else "NOT SEPARATED"
        print(f"   k0={k0}  m0={mp.nstr(m0,5):>6}  m0/N={mp.nstr(m0/14,4):>7}   d_min = {s:>12}")

    print()
    print("=" * 90)
    print("E2d  same at N = 10 (band [-10,10])")
    print("=" * 90)
    for k0 in range(0, 6):
        m0 = BASE + SP * k0
        dm = dmin(10, k0, 25)
        s = mp.nstr(dm, 6) if dm is not None else "NOT SEPARATED"
        print(f"   k0={k0}  m0={mp.nstr(m0,5):>6}  m0/N={mp.nstr(m0/10,4):>7}   d_min = {s:>12}")

    print()
    print("=" * 90)
    print("E2e  tolerance sensitivity of d_min (N=12, m0=7.5)")
    print("=" * 90)
    for tol in ('0.5', '0.2', '0.1', '0.01', '0.001'):
        dm = dmin(12, 1, 25, tol=mpf(tol))
        print(f"   tol={tol:>7}  d_min = {mp.nstr(dm,6) if dm is not None else 'none'}")
