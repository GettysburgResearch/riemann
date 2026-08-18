#!/usr/bin/env python3
"""Reproduce the quadrature-error reconnaissance retained from the pass."""
import mpmath as mp
mp.mp.dps = 80
zeta_half = mp.zeta(mp.mpf('0.5'))

def H(x, n):
    if n > x:
        return mp.mpf(0)
    return min(mp.log(4), mp.log(x/n))

def K_direct(x):
    return mp.fsum(H(x,n)/mp.sqrt(n) for n in range(1, int(mp.floor(x))+1))

def error(x):
    x=mp.mpf(x)
    return K_direct(x)-2*mp.sqrt(x)-zeta_half*mp.log(4)

for x in [1,2,3,4,10,67,184,1000,5000]:
    e=error(x); b=1/(6*mp.sqrt(x))
    print(x, mp.nstr(e,30), 'bound', mp.nstr(b,30), 'ratio', mp.nstr(abs(e)/b,20))
