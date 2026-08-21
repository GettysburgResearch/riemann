"""E2g -- at large budget margin, is d_min limited by anything at all,
or only by the working precision?"""
import mpmath as mp
from mpmath import mpf
import core
S, B, K = mpf('5.11'), mpf('2.63'), 25
def sep(N, k0, d, tol=mpf('0.1'), dps_extra=0):
    d = mpf(d); m0 = B + S*k0
    ps, ws = [], []
    for k in range(K):
        m = B + S*k
        if k == k0: ps += [m-d/2, m+d/2]; ws += [mpf(1), mpf(1)]
        else: ps.append(m); ws.append(mpf(1))
    info = core.detect(N, ps, ws, extraprec=4000, dps_extra=dps_extra)
    r = info['pos_roots']
    near = sorted(r, key=lambda x: abs(x-m0))[:2]; near.sort()
    ok = abs(near[0]-(m0-d/2)) < tol*d and abs(near[1]-(m0+d/2)) < tol*d
    return ok, near, info['dps']
print("N=14, split pole #1 (margin m = N/2-k = 6), tiny gaps:")
for d in ('1e-10','1e-15','1e-20','1e-25','1e-30','1e-35','1e-40'):
    for xe in (0, 60):
        ok, near, dps = sep(14, 0, d, dps_extra=xe)
        print(f"   d={d:>7} dps={dps:>4}  d_rec={mp.nstr(near[1]-near[0],6):>12}  {'SEP' if ok else 'merged'}")
