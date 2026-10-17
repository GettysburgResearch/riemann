#!/usr/bin/env python3
"""Exact polynomial moments; five internal dimer correlations are variables.

z[:11] are positive observable amplitudes, z[11] is the hub factor,
z[12:17] are dimer alignment probabilities p=(1+tanh J)/2.
"""
from math import comb
from tree_core import Dual,cumulants,UNIT,COUNTS

def tree(z,degree=18,counts=COUNTS):
    zero=z[0]*0;one=zero+1;eta=z[11]
    total=[zero for _ in range(degree+1)]
    for i,a in enumerate(z[:11]):
        prob=one if i<6 else z[12+i-6]
        pattern=one*3 if i in (6,7) else one/100
        mu=[one]+[prob*a**n if n%2==0 else prob*pattern*eta*a**(n+1)
                  for n in range(1,degree+1)]
        kk=cumulants(mu)
        total=[old+counts[i]*x for old,x in zip(total,kk)]
    cond=[one]
    for n in range(1,degree+1):
        cond.append(sum((comb(n-1,j-1)*total[j]*cond[n-j] for j in range(1,n+1)),zero))
    mu=[x if n%2==0 else zero for n,x in enumerate(cond)]
    kap=cumulants(mu)
    return [kap[n]/UNIT[n] for n in range(2,degree+1,2)],mu

def jet(z,active=None,degree=18):
    if active is None:active=tuple(range(len(z)))
    zero=z[0]*0;one=zero+1
    values=[Dual(x,[one if i==j else zero for j in active])for i,x in enumerate(z)]
    s,mu=tree(values,degree)
    return [x.v for x in s],[list(x.d) for x in s],[x.v for x in mu]
