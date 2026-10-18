#!/usr/bin/env python3
"""Directed theta-source replay. Adapted explicitly from PR974/PR886 primitives.
Standard library, integer endpoints / 2**320. Not a second independent backend.
The six-index tail proof is reproduced in PROOF.md. No stored moments are inputs.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt
import json
from pathlib import Path
BITS=320; SCALE=1<<BITS; DEGREE=120

def require(ok,message):
    if not ok: raise ValueError(message)
def ceildiv(a,b):
    require(b>0,'positive divisor');return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        require(self.lo<=self.hi,'reversed interval')
    @staticmethod
    def rat(p,q=1):
        require(q>0,'positive denominator');return I(p*SCALE//q,ceildiv(p*SCALE,q))
    @staticmethod
    def coerce(x):
        if isinstance(x,I):return x
        if type(x) is int:return I(x*SCALE)
        if isinstance(x,F):return I.rat(x.numerator,x.denominator)
        raise TypeError('exact numbers required')
    def __add__(self,x):
        if hasattr(x,'gradient'):return NotImplemented
        x=I.coerce(x);return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,x):return self+(-I.coerce(x))
    def __rsub__(self,x):return I.coerce(x)+(-self)
    def __mul__(self,x):
        if hasattr(x,'gradient'):return NotImplemented
        x=I.coerce(x);p=(self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi)
        return I(min(p)//SCALE,ceildiv(max(p),SCALE))
    __rmul__=__mul__
    def __truediv__(self,x):
        if type(x) is int:
            if x<0:return -self/-x
            require(x>0,'zero divisor');return I(self.lo//x,ceildiv(self.hi,x))
        x=I.coerce(x);require(x.lo>0 or x.hi<0,'division through zero')
        if x.hi<0:return -self/-x
        return self*I(SCALE*SCALE//x.hi,ceildiv(SCALE*SCALE,x.lo))
    def __rtruediv__(self,x):return I.coerce(x)/self
    def __pow__(self,k):
        require(type(k) is int and k>=0,'nonnegative integer power')
        a=I.coerce(1);b=self
        while k:
            if k&1:a=a*b
            k//=2
            if k:b=b*b
        return a
    def record(self):return [self.lo,self.hi]
    def absup(self):return max(abs(self.lo),abs(self.hi))

def exp_endpoint(x):
    if x<0:return 1/exp_endpoint(-x)
    k=0
    while x>(SCALE//8)*(1<<k):k+=1
    y=I.rat(x,SCALE*(1<<k));term=I.coerce(1);total=term
    for j in range(1,97):term=term*y/j;total=total+term
    nxt=term*y/97;rem=nxt/(1-y/98);total=I(total.lo,total.hi+rem.hi)
    for _ in range(k):total=total*total
    return total
def exp(x):
    x=I.coerce(x);return I(exp_endpoint(x.lo).lo,exp_endpoint(x.hi).hi)
def atan_recip(n):
    total=sum((F((-1)**k,(2*k+1)*n**(2*k+1)) for k in range(96)),F(0))
    rem=F(1,193*n**193)
    return I.coerce(total)+I(0,I.coerce(rem).hi)
def pi_interval():return 16*atan_recip(5)-4*atan_recip(239)
def series_exp_linear(a,center,h):
    out=[exp(a*center)];v=a*h
    for k in range(1,DEGREE+1):out.append(out[-1]*v/k)
    return out
def mulpoly(a,b,limit=None):
    last=len(a)+len(b)-2
    if limit is not None:last=min(last,limit)
    c=[I.coerce(0) for _ in range(last+1)]
    for i,u in enumerate(a):
        for j in range(min(len(b),last-i+1)):c[i+j]=c[i+j]+u*b[j]
    return c
def cell_density(n,center,pi):
    h=I.rat(1,32);c=I.coerce(center);q=pi*n*n
    e2=series_exp_linear(I.coerce(2),c,h);g=[-q*v for v in e2];hh=[exp(g[0])]
    for j in range(1,DEGREE+1):hh.append(sum((k*g[k]*hh[j-k] for k in range(1,j+1)),I.coerce(0))/j)
    e9=series_exp_linear(I.rat(9,2),c,h);e5=series_exp_linear(I.rat(5,2),c,h)
    return mulpoly([4*q*q*x-6*q*y for x,y in zip(e9,e5)],hh,DEGREE)
def integrate_moment(poly,center,j):
    h=I.rat(1,32);c=I.coerce(center)
    out=mulpoly(poly,[comb(j,k)*c**(j-k)*h**k for k in range(j+1)])
    return 4*h*sum((out[k]/(k+1) for k in range(0,len(out),2)),I.coerce(0))
def cumulants(mom):
    k=[mom[0]*0 for _ in mom]
    for n in range(1,len(mom)):
        k[n]=mom[n]-sum((comb(n-1,j-1)*k[j]*mom[n-j] for j in range(1,n)),mom[0]*0)
    return k
def reconstruct():
    pi=pi_interval();require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    counts=(32,24,16,12,8,6);js=range(0,19,2);totals={j:I.coerce(0) for j in js}
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            center=F(2*k+1,32);d=cell_density(n,center,pi)
            for j in js:totals[j]+=integrate_moment(d,center,j)
    errs={}
    for j in js:
        e=I.rat(16*10**11*2**j,4**(DEGREE+1))/F(3,4);tails=I.coerce(0)
        for n,cnt in enumerate(counts,1):
            U=F(cnt,16);q=pi*n*n;E=exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            require(lam.lo>0,'tail exponent')
            tails+=8*q*q*exp(F(9,2)*I.coerce(U)-q*E)*sum((comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*7**4*exp(-49*pi)*factorial(j)/(98*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi,totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    require(totals[0].lo>0,'normalization');mu={j:totals[j]/totals[0] for j in js if j};v=mu[2]
    require(v.lo>SCALE//25 and v.hi<SCALE//20,'variance')
    mom=[I.coerce(0) for _ in range(19)];mom[0]=I.coerce(1)
    for r in range(1,10):mom[2*r]=mu[2*r]/v**r
    kap=cumulants(mom);unit=cumulants([F(int(n%2==0)) for n in range(19)])
    ss=[kap[2*r]/unit[2*r] for r in range(1,10)]
    return {'status':'DIRECTED_FULL_SOURCE','bits':BITS,'degree':DEGREE,'cells':sum(counts),'explicit_indices':6,
            'raw':{str(j):x.record() for j,x in totals.items()},'variance':v.record(),
            'standardized_moments':[x.record() for x in mom], 's':[x.record() for x in ss], 'tails':errs}
if __name__=='__main__':
    print(json.dumps(reconstruct(),sort_keys=True,indent=2))
