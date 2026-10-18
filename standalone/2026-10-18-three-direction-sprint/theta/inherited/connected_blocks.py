"""Exact complete moments of a hub, repeated signs and unequal Ising dimers.

Block 0 is a single-sign type, repeated 256 times. All other blocks are
two-spin components. Conditional on the hub each component root has the same
positive bias eta; its internal edge has bias2p-1. The first component's
passive entries are B=0,p=1. Every configuration is retained.
"""
from math import comb
from fractions import Fraction as F
from tree_core import Dual,cumulants,UNIT
COUNTS=(256,10)+(1,)*14
ETA=F(1,10**10)

def evaluate(z,degree=20,*,counts=COUNTS,eta=ETA):
    if len(z)!=3*len(counts):raise ValueError('full block data required')
    zero=z[0]*0;one=zero+1;eta=one*eta;total=[zero]*(degree+1)
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)*(one if n%2==0 else eta) for n in range(1,degree+1)]
        kk=cumulants(mu);total=[x+count*y for x,y in zip(total,kk)]
    mu=[one]
    for n in range(1,degree+1):mu.append(sum((comb(n-1,j-1)*total[j]*mu[n-j] for j in range(1,n+1)),zero))
    mu=[x if n%2==0 else zero for n,x in enumerate(mu)]
    kap=cumulants(mu)
    return [kap[2*r]/UNIT[2*r] for r in range(1,degree//2+1)],mu

def jet(z,active=None,degree=20,**kwargs):
    if active is None:active=tuple(range(len(z)))
    zero=z[0]*0;one=zero+1
    dual=[Dual(x,[one if i==j else zero for j in active]) for i,x in enumerate(z)]
    s,mu=evaluate(dual,degree,**kwargs)
    return [x.v for x in s],[list(x.d) for x in s],[x.v for x in mu]
