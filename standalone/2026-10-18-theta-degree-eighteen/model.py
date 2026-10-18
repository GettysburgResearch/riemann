#!/usr/bin/env python3
"""Exact rational polynomial for the complete 282-spin conditional tree law."""
from fractions import Fraction as F
from math import factorial
from interval_source import I
N=18
MULT=(256,10,1,1,1,1,1,1,1,1,1)
KS=(F(1,100),)*6+(F(3),F(3))+(F(1,100),)*3
FACTORIAL=tuple(factorial(j) for j in range(N+1))
class AD:
    __slots__=('value','gradient')
    def __init__(self,value,gradient):self.value=value;self.gradient=gradient
    def cast(self,x):
        if isinstance(x,AD):return x
        return AD(x,[self.value*0 for _ in self.gradient])
    def __add__(self,x):
        x=self.cast(x);return AD(self.value+x.value,[u+v for u,v in zip(self.gradient,x.gradient)])
    __radd__=__add__
    def __neg__(self):return AD(-self.value,[-v for v in self.gradient])
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);return AD(self.value*x.value,[u*x.value+self.value*v for u,v in zip(self.gradient,x.gradient)])
    __rmul__=__mul__
    def __truediv__(self,x):
        if isinstance(x,AD):raise TypeError('only scalar division is used')
        return AD(self.value/x,[v/x for v in self.gradient])
    def __pow__(self,n):
        if type(n)is not int or n<0:raise ValueError('nonnegative integer power')
        out=self.cast(1);b=self
        while n:
            if n&1:out=out*b
            n//=2
            if n:b=b*b
        return out

def conv(a,b):
    zero=a[0]*0
    return [sum((a[j]*b[i-j] for j in range(i+1)),zero) for i in range(N+1)]
def ppow(p,m):
    r=[p[0]*0 for _ in p];r[0]=r[0]+1
    while m:
        if m&1:r=conv(r,p)
        m//=2
        if m:p=conv(p,p)
    return r

def fair_cumulants():
    from interval_source import cumulants
    return cumulants([F(int(j%2==0)) for j in range(N+1)])
CK=fair_cumulants()

def evaluate(z,return_moments=False,multiplicities=MULT):
    """z=(a0..a10, eta, p0..p4, p_new); old sign #5 is now a dimer.
    Moment generating coefficients condition on hub +1. Every component and
    all its multiplicities are included. Symmetrization averages both hub states.
    """
    if len(z)!=18:raise ValueError('18 parameters required')
    zero=z[0]*0;one=zero+1;tot=[one]+[zero]*N
    for i in range(11):
        alignment=one if i<5 else z[17] if i==5 else z[12+i-6]
        bias=z[11]*KS[i]*z[i]
        c=[one]+[alignment*z[i]**j*(bias if j%2 else one)/FACTORIAL[j] for j in range(1,N+1)]
        tot=conv(tot,ppow(c,multiplicities[i]))
    for j in range(1,N+1,2):tot[j]=zero
    log=[zero]*(N+1)
    for n in range(2,N+1,2):
        log[n]=tot[n]-sum((j*log[j]*tot[n-j] for j in range(2,n,2)),zero)/n
    ratios=[log[2*r]*FACTORIAL[2*r]/CK[2*r] for r in range(1,10)]
    return (ratios,[tot[j]*FACTORIAL[j] for j in range(N+1)]) if return_moments else ratios

def values_and_jacobian(z,active):
    zero=z[0]*0;one=zero+1;index={j:i for i,j in enumerate(active)}
    args=[]
    for j,x in enumerate(z):
        g=[zero]*len(active)
        if j in index:g[index[j]]=one
        args.append(AD(x,g))
    out=evaluate(args)
    return [v.value for v in out],[v.gradient for v in out]
