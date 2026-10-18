#!/usr/bin/env python3
"""Exact polynomial moments for the full connected hidden-hub tree.

Generic scalars may be Fractions, Decimals, or outward intervals. No graph
configuration is omitted: conditioning on the hidden hub gives independent
single-sign and two-spin components, encoded by their complete moments.
"""
from math import comb
COUNTS=(256,10,1,1,1,1,1,1,1,1,1)
ACTIVE=(0,1,2,3,4,5,7,9,11)

def unit_cumulants(n=20):
    mu=[int(j%2==0) for j in range(n+1)];kap=[0]*(n+1)
    for j in range(1,n+1):
        kap[j]=mu[j]-sum(comb(j-1,k-1)*kap[k]*mu[j-k] for k in range(1,j))
    return kap

UNIT=unit_cumulants()

class Dual:
    __slots__=('v','d')
    def __init__(self,v,d):self.v=v;self.d=tuple(d)
    def __add__(self,o):
        if isinstance(o,Dual):return Dual(self.v+o.v,[a+b for a,b in zip(self.d,o.d)])
        return Dual(self.v+o,self.d)
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,[-a for a in self.d])
    def __sub__(self,o):return self+-o
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if isinstance(o,Dual):return Dual(self.v*o.v,[a*o.v+self.v*b for a,b in zip(self.d,o.d)])
        return Dual(self.v*o,[a*o for a in self.d])
    __rmul__=__mul__
    def __truediv__(self,o):return Dual(self.v/o,[a/o for a in self.d])
    def __pow__(self,n):
        if not n:return Dual(self.v*0+1,[x*0 for x in self.d])
        vn=self.v**(n-1)
        return Dual(vn*self.v,[n*vn*x for x in self.d])

def cumulants(mu):
    zero=mu[0]*0;k=[zero for _ in mu]
    for n in range(1,len(mu)):
        k[n]=mu[n]-sum((comb(n-1,j-1)*k[j]*mu[n-j] for j in range(1,n)),zero)
    return k

def tree(z,degree=18):
    zero=z[0]*0;one=zero+1;eta=z[-1]
    total=[zero for _ in range(degree+1)]
    for i,a in enumerate(z[:-1]):
        prob=one if i<6 else (one*3)/5
        pattern=one*3 if i in (6,7) else one/100
        mu=[one]+[prob*a**n if n%2==0 else prob*pattern*eta*a**(n+1)
                  for n in range(1,degree+1)]
        kk=cumulants(mu)
        total=[old+COUNTS[i]*x for old,x in zip(total,kk)]
    cond=[one]
    for n in range(1,degree+1):
        cond.append(sum((comb(n-1,j-1)*total[j]*cond[n-j] for j in range(1,n+1)),zero))
    mu=[x if n%2==0 else zero for n,x in enumerate(cond)]
    kap=cumulants(mu)
    return [kap[n]/UNIT[n] for n in range(2,degree+1,2)],mu

def jet(z,active=ACTIVE,degree=18):
    zero=z[0]*0;one=zero+1;values=[]
    for i,x in enumerate(z):
        values.append(Dual(x,[one if i==j else zero for j in active]))
    s,mu=tree(values,degree)
    return [x.v for x in s],[list(x.d) for x in s],[x.v for x in mu]

def linear_solve(A,b):
    n=len(b);a=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(a[i][k]))
        if a[pivot][k]==0:raise ArithmeticError('singular Jacobian')
        a[k],a[pivot]=a[pivot],a[k];v=a[k][k]
        a[k]=[x/v for x in a[k]]
        for i in range(n):
            if i!=k:
                v=a[i][k];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
    return [row[-1] for row in a]
