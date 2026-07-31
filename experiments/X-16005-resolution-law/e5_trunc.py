"""E5 -- TRUNCATION.  What happens when the number of poles greatly exceeds N?
This is the regime the arithmetic computation is actually in.

(a) K = 50 poles, N = 6.  Which are found?  Are the found ones biased?
(b) Bias study: fix N, sweep K from N (exact case) upward; watch the SIGNED
    relative error of the low recovered roots.  Does it converge?  Which sign?
"""
import mpmath as mp
from mpmath import mpf
import core

S = mpf('3.7')
BASE = S / 2


def poles(K):
    return [BASE + S * k for k in range(K)]


def show(N, K):
    ps = poles(K)
    w = [mpf(1)] * K
    info = core.detect(N, ps, w, extraprec=4000)
    print(f"\n  N={N}, K={K} poles (comb {mp.nstr(BASE,4)}+{mp.nstr(S,4)}k, up to "
          f"{mp.nstr(ps[-1],6)}), dps={info['dps']}")
    print(f"    t* = {mp.nstr(info['tstar'],10)}   max root residual {mp.nstr(max(info['resid']),3)}"
          f"   all roots real: {info['max_imag_u'] == 0}")
    print(f"    {'#':>3} {'recovered root':>24} {'nearest pole':>13} {'signed rel.err':>16}")
    for i, r in enumerate(info['pos_roots']):
        p = min(ps, key=lambda m: abs(m - r))
        print(f"    {i+1:>3} {mp.nstr(r,18):>24} {mp.nstr(p,8):>13} {mp.nstr((r-p)/p,6):>16}")
    return info


if __name__ == '__main__':
    print("=" * 100)
    print("E5a  K = 50 poles, N = 6  (the task's stated regime)")
    print("=" * 100)
    show(6, 50)
    print("\n  ... compared with the untruncated / minimally truncated cases:")
    for K in (6, 7, 8, 10, 15, 25, 50, 100, 200):
        ps = poles(K)
        info = core.detect(6, ps, [mpf(1)] * K, extraprec=4000)
        r = info['pos_roots']
        errs = []
        for i in range(3):
            p = ps[i]
            rr = min(r, key=lambda x: abs(x - p))
            errs.append((rr - p) / p)
        print(f"    K={K:>4}: signed rel.err of poles 1,2,3 = "
              + ", ".join(mp.nstr(e, 6) for e in errs)
              + f"   | roots: {[mp.nstr(x,9) for x in r]}")

    print()
    print("=" * 100)
    print("E5b  same bias study at N = 10 and N = 14")
    print("=" * 100)
    for N in (10, 14):
        print(f"\n  N={N} (budget N/2 = {N//2})")
        for K in (N, N + 1, N + 2, 2 * N, 50, 100, 200):
            ps = poles(K)
            info = core.detect(N, ps, [mpf(1)] * K, extraprec=4000)
            r = info['pos_roots']
            errs = []
            for i in range(min(N // 2 + 1, K)):
                p = ps[i]
                rr = min(r, key=lambda x: abs(x - p))
                errs.append((rr - p) / p)
            print(f"    K={K:>4}: signed rel.err poles 1..{len(errs)} = "
                  + ", ".join(mp.nstr(e, 4) for e in errs))

    print()
    print("=" * 100)
    print("E5c  where do the ARTIFACT roots go?  (N=6, K=50)  and do they mean anything?")
    print("=" * 100)
    info = core.detect(6, poles(50), [mpf(1)] * 50, extraprec=4000)
    ps = poles(50)
    print("    recovered:", [mp.nstr(r, 10) for r in info['pos_roots']])
    print("    true poles 1..12:", [mp.nstr(p, 6) for p in ps[:12]])
    print("    highest true pole:", mp.nstr(ps[-1], 8))
