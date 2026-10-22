"""E3 -- WEIGHT SENSITIVITY.  How small can a single pole's weight be before it is missed?

Background comb: K poles at spacing S, base BASE, all weights 1.
Extra probe pole inserted midway between comb elements k0 and k0+1, weight a.
Sweep a over many orders of magnitude; ask whether a recovered root tracks it,
and whether its presence disturbs the other recovered roots.
"""
import mpmath as mp
from mpmath import mpf
import core

S = mpf('5.11')
BASE = mpf('2.63')
K = 25


def run(N, k0, avals):
    m1 = BASE + S * k0 + S / 2
    # reference run WITHOUT the probe
    ps0 = [BASE + S * k for k in range(K)]
    w0 = [mpf(1)] * K
    ref = core.detect(N, ps0, w0, extraprec=4000)
    print(f"\n  N={N}  probe at m1={mp.nstr(m1,6)} (between comb #{k0+1} and #{k0+2}); "
          f"budget N/2={N/2}")
    print(f"  reference roots (no probe): {[mp.nstr(r,10) for r in ref['pos_roots'][:N//2+2]]}")
    print(f"  {'a':>10} {'root nearest m1':>22} {'rel.err':>12} {'detected?':>10} "
          f"{'max shift of other tracked roots':>34}")
    for a in avals:
        a = mpf(a)
        ps = ps0 + [m1]
        w = w0 + [a]
        info = core.detect(N, ps, w, extraprec=4000)
        r = info['pos_roots']
        near = min(r, key=lambda x: abs(x - m1))
        e = abs(near - m1) / m1
        det = "YES" if e < mpf('1e-3') else ("weak" if e < mpf('1e-1') else "no")
        # shift of the comb roots that were tracked in the reference run
        shifts = []
        for rr in ref['pos_roots'][:max(1, N // 2)]:
            p = min(ps0, key=lambda x: abs(x - rr))
            if abs(rr - p) / p < mpf('1e-6'):
                nn = min(r, key=lambda x: abs(x - p))
                shifts.append(abs(nn - p) / p)
        ms = max(shifts) if shifts else mpf(0)
        print(f"  {mp.nstr(a,3):>10} {mp.nstr(near,14):>22} {mp.nstr(e,4):>12} {det:>10} "
              f"{mp.nstr(ms,4):>34}")


if __name__ == '__main__':
    avals = ['1', '1e-1', '1e-2', '1e-3', '1e-4', '1e-6', '1e-8', '1e-10', '1e-12', '1e-16']
    print("=" * 110)
    print("E3  weight sensitivity")
    print("=" * 110)
    for N, k0 in [(14, 0), (14, 2), (14, 5), (10, 0), (10, 3)]:
        run(N, k0, avals)
