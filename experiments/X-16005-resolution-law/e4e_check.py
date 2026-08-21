import mpmath as mp
from mpmath import mpf
import core
OFF = mpf('0.037')
S = mpf('0.9')
print("check A: dps-independence of the dense-source failure (N=10, S=0.9, K=15)")
for xe in (0, 60, 120):
    ps = [S/2+OFF+S*k for k in range(15)]
    info = core.detect(10, ps, [mpf(1)]*15, extraprec=4000, dps_extra=xe)
    print("   dps=%4d  roots: %s" % (info['dps'], [mp.nstr(x,12) for x in info['pos_roots'][:5]]))

print()
print("check B: K = N exactly (no truncation) at the same dense spacing -> must be EXACT")
N = 10
ps = [S/2+OFF+S*k for k in range(N)]
allp = [p for p in ps] + [-p for p in ps]
core.set_dps(N)
lam = core.nodes(N)
Q = core.build_Q_rank1(N, ps, [mpf(1)]*N)
xi = []
for j in range(2*N+1):
    P = mpf(1)
    for m in allp: P *= (m - lam[j])
    D = mpf(1)
    for k in range(2*N+1):
        if k != j: D *= (lam[k]-lam[j])
    xi.append(P/D)
c = core.P_coeffs(N, xi); R,_ = core.even_reduce(c)
ur = core.poly_roots_increasing(R, extraprec=2000)
got = sorted([mp.sqrt(u).real for u in ur])
print("   true poles:", [mp.nstr(p,10) for p in ps[:5]])
print("   recovered :", [mp.nstr(g,10) for g in got[:5]])
print("   max rel err:", mp.nstr(max(abs(g-p)/p for g,p in zip(got, ps)), 4))

print()
print("check C: one excess pole only (K = N+1 = 11) at S=0.9 vs S=1.85")
for Sx in ('0.9','1.85'):
    Sx = mpf(Sx)
    ps = [Sx/2+OFF+Sx*k for k in range(11)]
    info = core.detect(10, ps, [mpf(1)]*11, extraprec=4000)
    errs = [min([abs(r-p)/p for r in info['pos_roots']]) for p in ps[:6]]
    print(f"   S={mp.nstr(Sx,4):>6}: rel errs poles 1..6 = " + ", ".join(mp.nstr(e,4) for e in errs))
