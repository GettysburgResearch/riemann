#!/usr/bin/env python3
"""Small exact checks of primary representatives, Gaussian Möbius, reciprocity."""
from experiment import primary,gauss_mu,spf_sieve,prime_sieve,sum_squares
spf=spf_sieve(1000)
assert gauss_mu(2,1,5,spf)==-1
assert gauss_mu(3,0,9,spf)==-1
assert gauss_mu(5,0,25,spf)==1
assert gauss_mu(3,4,25,spf)==0

def residue(z,pi,p):
    a,b=pi;r=(-a*pow(b,-1,p))%p
    v=(z[0]+z[1]*r)%p
    return {1:1,-1%p:-1,r:1j,-r%p:-1j,0:0}[pow(v,(p-1)//4,p)]

ps=[p for p in prime_sieve(500) if p%8==1]
for p in ps:
    a=primary(*sum_squares(p))
    for q in ps:
        if p!=q:
            b=primary(*sum_squares(q))
            assert residue(a,b,q)==residue(b,a,p),(p,q,a,b)
print('Gaussian Möbius examples and fixed-sector quartic reciprocity: passed')
