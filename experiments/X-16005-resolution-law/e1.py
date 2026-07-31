"""E1 -- how many poles are recovered accurately, as a function of N.

Fixed source (K=30 positive poles, comb of spacing S starting at S/2), growing model N.
This is the analogue of the arithmetic case: the source is fixed and effectively
infinite relative to the model.
"""
import mpmath as mp
from mpmath import mpf
import core


def run(S, K, Ns, label, weights=None):
    S = mpf(S)
    poles = [S / 2 + S * k for k in range(K)]
    w = weights if weights is not None else [mpf(1)] * K
    print()
    print("#" * 78)
    print(f"# {label}:  K={K} positive poles at mu_k = {mp.nstr(S/2,4)} + {mp.nstr(S,4)}*k, all a_k=1")
    print("#" * 78)
    res = {}
    for N in Ns:
        info = core.detect(N, poles, w, extraprec=4000)
        m = core.match(info['pos_roots'], poles)
        res[N] = (info, m)
        print(f"\nN={N}  dps={info['dps']}  t*={mp.nstr(info['tstar'],8)}  "
              f"max root residual={mp.nstr(max(info['resid']),3)}  "
              f"max|Im u|/(1+|u|)={mp.nstr(info['max_imag_u'],3)}")
        for i, (r, p, e) in enumerate(m):
            tag = "OK " if e < mpf('1e-6') else ("~  " if e < mpf('1e-2') else "ART")
            print(f"    root {i+1:>2}: {mp.nstr(r,14):>22}   nearest pole {mp.nstr(p,10):>10}"
                  f"   rel.err {mp.nstr(e,4):>12}  {tag}")
    return poles, res


def summary_table(poles, res, Ns, thresh=('1e-6', '1e-3')):
    print("\n--- relative error of recovered root vs true pole, by pole index (blank = pole not recovered) ---")
    hdr = "  pole idx |   mu     | " + " | ".join(f"  N={N}   " for N in Ns)
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    maxidx = max(len(res[N][1]) for N in Ns)
    for k in range(min(maxidx + 3, len(poles))):
        row = f"  {k+1:>8} | {mp.nstr(poles[k],6):>8} |"
        for N in Ns:
            info, m = res[N]
            hits = [e for (r, p, e) in m if abs(p - poles[k]) < mpf('1e-20')]
            if hits:
                row += f" {mp.nstr(min(hits),3):>9} |"
            else:
                row += "         - |"
        print(row)
    print()
    for t in thresh:
        t = mpf(t)
        print(f"  # poles recovered with rel.err < {mp.nstr(t,2)}:")
        for N in Ns:
            info, m = res[N]
            cnt = sum(1 for (r, p, e) in m if e < t)
            best = max([p for (r, p, e) in m if e < t], default=mpf(0))
            print(f"     N={N:>3}:  count={cnt:>3}   highest pole recovered = {mp.nstr(best,6):>9}"
                  f"   ratio mu_max/N = {mp.nstr(best/N,4)}")


if __name__ == '__main__':
    Ns = [4, 6, 8, 10, 12, 14]
    poles, res = run('3.7', 30, Ns, "E1-A  spacing 3.7")
    summary_table(poles, res, Ns)
