"""E2f -- is d_min a function of the 'budget margin' m = N/2 - k only?
        and does it scale with the comb spacing S?
Also pushes the bisection floor down to 1e-14 to see whether 'unlimited' is real.
"""
import mpmath as mp
from mpmath import mpf
import core


def make(K, k0, d, S, BASE):
    ps, ws = [], []
    for k in range(K):
        m = BASE + S * k
        if k == k0:
            ps += [m - d / 2, m + d / 2]
            ws += [mpf(1), mpf(1)]
        else:
            ps.append(m)
            ws.append(mpf(1))
    return ps, ws


def separated(N, k0, d, K, S, BASE, tol=mpf('0.1')):
    d = mpf(d)
    m0 = BASE + S * k0
    ps, ws = make(K, k0, d, S, BASE)
    info = core.detect(N, ps, ws, extraprec=4000)
    r = info['pos_roots']
    if len(r) < 2:
        return False
    near = sorted(r, key=lambda x: abs(x - m0))[:2]
    near.sort()
    return abs(near[0] - (m0 - d / 2)) < tol * d and abs(near[1] - (m0 + d / 2)) < tol * d


def dmin(N, k0, K, S, BASE, lo='1e-14', hi=None, iters=16):
    S = mpf(S); BASE = mpf(BASE)
    hi = mpf(hi) if hi is not None else S * mpf('0.6')
    lo = mpf(lo)
    if not separated(N, k0, hi, K, S, BASE):
        return None
    if separated(N, k0, lo, K, S, BASE):
        return mpf(0)          # below search floor
    for _ in range(iters):
        mid = mp.sqrt(lo * hi)
        if separated(N, k0, mid, K, S, BASE):
            hi = mid
        else:
            lo = mid
    return hi


if __name__ == '__main__':
    print("=" * 92)
    print("E2f-1  d_min vs budget margin m = N/2 - k   (k = 1-based index of the split pole)")
    print("       comb spacing S = 5.11, base 2.63, K = 25")
    print("=" * 92)
    print(f"{'N':>4} {'k':>3} {'m=N/2-k':>8} {'m0':>8} {'d_min':>14} {'d_min/S':>12}")
    S, B = mpf('5.11'), mpf('2.63')
    for N in (8, 10, 12, 14, 16):
        for k0 in range(0, N // 2 + 1):
            k = k0 + 1
            m = mpf(N) / 2 - k
            if m < -1:
                continue
            dm = dmin(N, k0, 25, S, B)
            s = ("<1e-14" if dm == 0 else mp.nstr(dm, 5)) if dm is not None else "NO SEP"
            r = ("" if dm in (None, 0) else mp.nstr(dm / S, 5))
            print(f"{N:>4} {k:>3} {mp.nstr(m,3):>8} {mp.nstr(B+S*k0,5):>8} {s:>14} {r:>12}")
        print()

    print("=" * 92)
    print("E2f-2  does d_min scale with the comb spacing S?  (margin m = 1, i.e. k = N/2 - 1)")
    print("=" * 92)
    for N in (10, 14):
        k0 = N // 2 - 2          # k = N/2 - 1  ->  margin 1
        for S in ('1.277', '2.555', '5.11', '10.22', '20.44'):
            Sm = mpf(S)
            dm = dmin(N, k0, 25, Sm, mpf('0.51') * Sm)
            s = ("<1e-14" if dm == 0 else mp.nstr(dm, 5)) if dm is not None else "NO SEP"
            r = ("" if dm in (None, 0) else mp.nstr(dm / Sm, 5))
            print(f"  N={N:>3} k={k0+1:>2} S={S:>7}  d_min={s:>12}  d_min/S={r:>10}")
        print()
