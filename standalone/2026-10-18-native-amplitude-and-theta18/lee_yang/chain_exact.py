#!/usr/bin/env python3
"""Exact polynomial moments for the whole 281-spin chain-and-leaves tree.

Coordinates: two repeated leaf weights;14 core weights;13 chain edge
correlations. Hub/core-root correlation eta=1/1000. Leaf correlations
are eta times their observable weight. Scalars may be Fraction or intervals.
"""
from math import comb
from fractions import Fraction as F
from tree_core import Dual,cumulants,UNIT
ETA=F(1,1000)
COUNTS=(256,10)

def evaluate(z,degree=18,*,counts=COUNTS,ncore=14,eta=ETA):
    zero=z[0]*0;one=zero+1;eta=one*eta
    w=z[2:2+ncore];q=z[2+ncore:]
    if len(z)!=2*ncore+1:raise ValueError('two leaf weights, n core weights, n-1 edge correlations required')
    g=[one]+[w[-1]**n for n in range(1,degree+1)]
    for i in range(ncore-2,-1,-1):
        old=g;g=[]
        for n in range(degree+1):
            g.append(sum((comb(n,k)*w[i]**(n-k)*old[k]*(one if k%2==0 else q[i])for k in range(n+1)),zero))
    cm=[x*(one if n%2==0 else eta)for n,x in enumerate(g)]
    total=cumulants(cm)
    for i,count in enumerate(counts):
        a=z[i];cm=[one]+[a**n*(one if n%2==0 else eta*a)for n in range(1,degree+1)]
        kk=cumulants(cm);total=[x+count*y for x,y in zip(total,kk)]
    mu=[one]
    for n in range(1,degree+1):mu.append(sum((comb(n-1,j-1)*total[j]*mu[n-j]for j in range(1,n+1)),zero))
    mu=[x if n%2==0 else zero for n,x in enumerate(mu)]
    kap=cumulants(mu)
    return [kap[2*r]/UNIT[2*r]for r in range(1,degree//2+1)],mu

def jet(z,active=None,degree=18,**kwargs):
    if active is None:active=tuple(range(len(z)))
    zero=z[0]*0;one=zero+1
    dual=[Dual(x,[one if i==j else zero for j in active])for i,x in enumerate(z)]
    s,mu=evaluate(dual,degree,**kwargs)
    return [x.v for x in s],[list(x.d)for x in s],[x.v for x in mu]
