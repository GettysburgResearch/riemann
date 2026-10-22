import mpmath as mp
from mpmath import mpf
import core, e6_zeta as E6
G = E6.gammas(90)
Delta = mp.log(2000)/(2*mp.pi)
print("odd/even N, zeta-positioned source, c=2000, K=90:  rel err of gamma_k")
print(f"{'N':>3} " + " ".join(f"{'k='+str(k):>10}" for k in range(1,10)))
for N in (5,6,7,8,9,10,11,12,13):
    ps = [g*Delta for g in G[:90]]
    info = core.detect(N, ps, [mpf(1)]*90, extraprec=4000)
    rec = [r/Delta for r in info['pos_roots']]
    row = f"{N:>3} "
    for k in range(9):
        g = G[k]; rr = min(rec, key=lambda x: abs(x-g)); e = abs(rr-g)/g
        row += f" {mp.nstr(e,3):>10}"
    print(row + f"   (floor(N/2)={N//2})")
