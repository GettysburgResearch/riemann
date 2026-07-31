"""E1b -- the error law.  Is log10(rel err of pole k) a function of the margin
        m = N - 2k alone (i.e. of the distance from the half-budget), for a
        comb source?  Test across N and across the comb spacing S.
"""
import mpmath as mp
from mpmath import mpf
import core


def errs(N, S, K):
    S = mpf(S)
    ps = [S / 2 + S * k for k in range(K)]
    info = core.detect(N, ps, [mpf(1)] * K, extraprec=4000)
    r = info['pos_roots']
    out = []
    for k in range(1, N + 1):
        if k - 1 >= len(ps):
            break
        p = ps[k - 1]
        rr = min(r, key=lambda x: abs(x - p)) if r else None
        out.append((k, p, rr, abs(rr - p) / p if rr is not None else None))
    return out, info


def table(S, Ns, K):
    print(f"\n### comb spacing S = {S}, K = {K}, weights 1")
    data = {}
    for N in Ns:
        e, info = errs(N, S, K)
        data[N] = e
    margins = sorted({N - 2 * k for N in Ns for (k, p, rr, er) in data[N]}, reverse=True)
    print("   log10(relative error) indexed by margin  m = N - 2k")
    hdr = f"   {'m':>4} |" + "".join(f"  N={N:<2}  |" for N in Ns)
    print(hdr)
    print("   " + "-" * (len(hdr) - 3))
    for m in margins:
        if m < -6 or m > 12:
            continue
        row = f"   {m:>4} |"
        for N in Ns:
            v = ""
            for (k, p, rr, er) in data[N]:
                if N - 2 * k == m:
                    v = mp.nstr(mp.log(er, 10), 4) if er and er > 0 else "-inf"
            row += f" {v:>6} |"
        print(row)
    return data


if __name__ == '__main__':
    print("=" * 90)
    print("E1b  error law vs margin m = N - 2k")
    print("=" * 90)
    Ns = [6, 8, 10, 12, 14]
    for S, K in [('1.85', 60), ('3.7', 40), ('7.4', 30), ('14.8', 30)]:
        table(S, Ns, K)
