import sys, time
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, diff, nstr, pi, quad, cos
from core import Phi, dPhi, Xi, tail_cutoff, E_j, E_asym

mp.dps = 50
print("tail_cutoff =", nstr(tail_cutoff(), 8), " Phi(tail_cutoff) =", nstr(Phi(tail_cutoff()), 5))
print()
print("--- Phi values (repo normalization Phi = 4K) ---")
for t in ['0.0', '0.4545', '0.5', '0.7143', '1.0', '1.25', '2.0']:
    print(f"  Phi({t}) = {nstr(Phi(mpf(t)), 20)}")
print()
print("--- derivative check: closed form dPhi vs mpmath numeric diff ---")
for t in ['0.4545', '0.5', '0.7143', '1.0', '1.25']:
    tt = mpf(t)
    for k in (1, 2, 3):
        a = dPhi(tt, k)
        b = diff(lambda x: Phi(x), tt, k)
        rel = abs(a - b) / abs(b) if b != 0 else abs(a - b)
        print(f"  t={t:>7} k={k}: closed={nstr(a,18):>26}  numeric={nstr(b,18):>26}  rel={nstr(rel,3)}")
print()
print("--- is Phi'' > 0 on (T, inf) for T >= 0.45 ?  (needed for a clean rigorous O(j^-2) bound) ---")
tt = mpf('0.30')
prev = None
while tt < mpf('3.0'):
    v = dPhi(tt, 2)
    if prev is not None and (prev > 0) != (v > 0):
        print(f"    SIGN CHANGE of Phi'' between t={float(tt)-0.05:.2f} and {float(tt):.2f}")
    prev = v
    tt += mpf('0.05')
for t in ['0.30','0.35','0.40','0.45','0.50','0.60','0.80','1.00','1.25','1.5','2.0']:
    print(f"    Phi''({t}) = {nstr(dPhi(mpf(t),2), 8)}")
print()
print("--- Xi cross-check: Xi(z) = int_R Phi(t) e^{izt} dt = 2 int_0^inf Phi cos(zt) dt ---")
for z in ['0', '3.0', '6.2831853071795864769']:
    zz = mpf(z)
    lhs = Xi(zz)
    w = zz
    tend = tail_cutoff()
    if w == 0:
        rhs = 2*quad(lambda t: Phi(t), [0, tend])
    else:
        import math
        pts=[mpf(0)]
        k=0
        while True:
            tk=(pi/2+k*pi)/w
            if tk>=tend: break
            pts.append(tk); k+=1
        pts.append(tend)
        rhs = 2*sum(quad(lambda t: Phi(t)*cos(w*t), [a,b]) for a,b in zip(pts[:-1],pts[1:]))
    print(f"  z={z}: Xi={nstr(lhs,20)}  quad={nstr(rhs,20)}  rel diff={nstr(abs(lhs-rhs)/abs(lhs),3)}")
