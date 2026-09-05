#!/usr/bin/env python3
"""Independent literal greedy at saturation (x=1e26, mp dps 30): no reduction
algebra — enumerate all 2^18 divisors, compute T, expansion-Q, s; sort evens
ascending; prefix-fill to demand; margins summed term by term. Compare against
the closed form of lattice_sat.py and the orchestrator's values.
Also: M_sc three ways (direct greedy sum; (3/4)[sum_e(1-theta)/sqrt e - B^s];
-(3/4)Delta_B closed form)."""
import time
from mpmath import mp, mpf, sqrt, log

mp.dps = 30
t0 = time.time()
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
divs = [(1, 1)]
for p in P:
    divs = divs + [(d*p, -m) for (d, m) in divs]
divs.sort()

z = mp.zeta(mpf(1)/2); zp = mp.zeta(mpf(1)/2, 1, 1)
lam = {}; kap = {}; Cc = {}
for j in (2, 3):
    A = mpf(j+1)/(j-1); B = mpf((j+1)*(j-2))/(j*(j-1)); C = mpf(2)/(j*(j-1))
    Cc[j] = C
    lam[j] = A/sqrt(mpf(j)) - B/sqrt(mpf(j+1)) + C*(z - sum(1/sqrt(mpf(m)) for m in range(1, j+2)))
    kap[j] = -A*log(mpf(j))/sqrt(mpf(j)) + B*log(mpf(j+1))/sqrt(mpf(j+1)) \
             + C*(zp + sum(log(mpf(m))/sqrt(mpf(m)) for m in range(1, j+2)))

def run(x):
    x = mpf(x)
    sqx = sqrt(x); lgx = log(x)
    # pass 1: odds — demand and row/score demand sums
    D = mpf(0); K2 = mpf(0); K3 = mpf(0); Ksc = mpf(0); B_O = mpf(0)
    evs = []
    for d, m in divs:
        sd = sqrt(mpf(d)); sY = sqx/sd; lY = lgx - log(mpf(d))
        T = (4*sY - 3)/sd
        if m == -1:
            D += T
            K2 += (4*Cc[2]*sY + lam[2]*lY + kap[2])/sd
            K3 += (4*Cc[3]*sY + lam[3]*lY + kap[3])/sd
            Ksc += T*(5*sY - 3)/(4*sY - 3)
            B_O += 1/sd
        else:
            evs.append((d, T, sd, sY, lY))
    # pass 2: greedy fill evens (already ascending)
    m2 = -K2; m3 = -K3; msc = Ksc; rem = D
    sliv_recip = mpf(0)      # sum_e (1-theta)/sqrt(e)
    B_E = mpf(0)
    estar = None; theta_star = None
    for d, T, sd, sY, lY in evs:
        B_E += 1/sd
        if rem > 0:
            take = T if T <= rem else rem
            th = take/T
            if take == rem and T > rem:
                estar = d; theta_star = th
            rem -= take
            m2 += th*(4*Cc[2]*sY + lam[2]*lY + kap[2])/sd
            m3 += th*(4*Cc[3]*sY + lam[3]*lY + kap[3])/sd
            msc -= th*T*(5*sY - 3)/(4*sY - 3)
            sliv_recip += (1 - th)/sd
        else:
            sliv_recip += 1/sd
    Bs = B_E - B_O
    msc_ident = mpf(3)/4*(sliv_recip - Bs)
    return dict(D=D, m2=m2, m3=m3, msc=msc, msc_ident=msc_ident,
                estar=estar, theta=theta_star, Bs=Bs)

for xs in ("1e26",):
    r = run(xs)
    print(f"x={xs}  ({time.time()-t0:.0f}s)")
    print(f"  e* = {r['estar']}   theta* = {mp.nstr(r['theta'], 20)}")
    print(f"  M2  = {mp.nstr(r['m2'], 15)}")
    print(f"  M3  = {mp.nstr(r['m3'], 15)}")
    print(f"  Msc greedy sum      = {mp.nstr(r['msc'], 15)}")
    print(f"  Msc identity R.1    = {mp.nstr(r['msc_ident'], 15)}")
    print(f"  |Msc diff| = {mp.nstr(abs(r['msc']-r['msc_ident']), 3)}")
    print(f"  B^s = {mp.nstr(r['Bs'], 12)}")
