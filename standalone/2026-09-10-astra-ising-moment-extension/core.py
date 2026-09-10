#!/usr/bin/env python3
"""Outward dyadic theta primitives, adapted from IMR26 at pinned PR847.
No floating arithmetic, zeta oracle, zero list, or numerical quadrature library.
This checks the stated finite construction, not the open all-order realization.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

BITS=256
SCALE=1<<BITS
DEGREE=120
ROOT=Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceildiv(a,b):
    require(b>0, 'positive divisor required')
    return -((-a)//b)


class I:
    __slots__=('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo=int(lo); self.hi=int(lo if hi is None else hi)
        require(self.lo<=self.hi,'reversed interval')
    @staticmethod
    def rat(p,q=1):
        require(q>0,'positive rational denominator required')
        return I((p*SCALE)//q,ceildiv(p*SCALE,q))
    @staticmethod
    def coerce(x):
        if isinstance(x,I): return x
        if type(x) is int: return I(x*SCALE)
        if isinstance(x,F): return I.rat(x.numerator,x.denominator)
        raise TypeError('only exact numbers accepted')
    def __add__(self,x):
        x=I.coerce(x); return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,x): return self+(-I.coerce(x))
    def __rsub__(self,x): return I.coerce(x)+(-self)
    def __mul__(self,x):
        x=I.coerce(x)
        p=(self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi)
        return I(min(p)//SCALE,ceildiv(max(p),SCALE))
    __rmul__=__mul__
    def __truediv__(self,x):
        if type(x) is int:
            if x<0:return (-self)/(-x)
            require(x>0,'zero divisor');return I(self.lo//x,ceildiv(self.hi,x))
        x=I.coerce(x)
        require(x.lo>0 or x.hi<0,'division through zero')
        if x.hi<0:return (-self)/(-x)
        return self*I((SCALE*SCALE)//x.hi,ceildiv(SCALE*SCALE,x.lo))
    def __rtruediv__(self,x): return I.coerce(x)/self
    def __pow__(self,k):
        require(type(k) is int and k>=0,'nonnegative integer power required')
        out=I.coerce(1); base=self
        while k:
            if k&1: out=out*base
            k//=2
            if k:base=base*base
        return out
    def sqrt(self):
        require(self.lo>=0,'negative square root')
        lo=isqrt(self.lo*SCALE); h=self.hi*SCALE; hi=isqrt(h)
        return I(lo,hi if hi*hi==h else hi+1)
    def record(self): return [self.lo,self.hi]


def exp_endpoint(x):
    """Enclose exp(x/SCALE) for an integer x."""
    if x<0:return 1/exp_endpoint(-x)
    k=0
    while x> (SCALE//8)*(1<<k):k+=1
    y=I.rat(x,SCALE*(1<<k))
    term=I.coerce(1); total=term
    for j in range(1,97):
        term=term*y/j;total=total+term
    nxt=term*y/97
    rem=nxt/(1-y/98)
    total=I(total.lo,total.hi+rem.hi)
    for _ in range(k):total=total*total
    return total


def exp(x):
    x=I.coerce(x)
    return I(exp_endpoint(x.lo).lo,exp_endpoint(x.hi).hi)


def atan_recip(n):
    # Alternating series: 96 terms, first omitted term bounds remainder.
    total=F(0)
    for k in range(96):total+=F((-1)**k,(2*k+1)*n**(2*k+1))
    rem=F(1,193*n**193)
    return I.rat(total.numerator,total.denominator)+I(0,I.rat(rem.numerator,rem.denominator).hi)


def pi_interval():return 16*atan_recip(5)-4*atan_recip(239)


def series_exp_linear(a,center,h):
    out=[exp(a*center)]; v=a*h
    for k in range(1,DEGREE+1):out.append(out[-1]*v/k)
    return out


def mulpoly(a,b,limit=None):
    last=len(a)+len(b)-2
    if limit is not None:last=min(last,limit)
    c=[I.coerce(0) for _ in range(last+1)]
    for i,u in enumerate(a):
        for j in range(min(len(b),last-i+1)):
            c[i+j]=c[i+j]+u*b[j]
    return c


def cell_density(n,center,pi):
    h=I.rat(1,32); c=I.coerce(center);q=pi*n*n
    e2=series_exp_linear(I.coerce(2),c,h)
    g=[-q*v for v in e2]
    hh=[exp(g[0])]
    for j in range(1,DEGREE+1):
        hh.append(sum((k*g[k]*hh[j-k] for k in range(1,j+1)),I.coerce(0))/j)
    e9=series_exp_linear(I.rat(9,2),c,h)
    e5=series_exp_linear(I.rat(5,2),c,h)
    pref=[4*q*q*x-6*q*y for x,y in zip(e9,e5)]
    return mulpoly(pref,hh,DEGREE)


def integrate_moment(poly,center,j):
    h=I.rat(1,32); c=I.coerce(center)
    power=[comb(j,k)*(c**(j-k))*(h**k) for k in range(j+1)]
    out=mulpoly(poly,power)
    # Full-line moment: factor two times half-line cell integral.
    return 4*h*sum((out[k]/(k+1) for k in range(0,len(out),2)),I.coerce(0))



def sincos(x, pi):
    """Taylor enclosure after exact-identity pi/2 reduction. No float."""
    x=I.coerce(x)
    # Any integer multiple is valid; this one ensures a small remainder.
    k=(2*(x.lo+x.hi)+pi.lo)//(2*pi.lo)  # nearest to 2*x/pi
    y=x-k*pi/2
    require(max(abs(y.lo),abs(y.hi)) <= SCALE, 'trigonometric reduction')
    yy=y*y; st=y; ct=I.coerce(1); sn=st; cs=ct
    for j in range(1,101):
        st=-st*yy/((2*j)*(2*j+1));ct=-ct*yy/((2*j-1)*(2*j))
        sn=sn+st;cs=cs+ct
    # All |y|<=1: alternating remainder bounded by next factorial term.
    es=I.rat(1,factorial(203));ec=I.rat(1,factorial(202))
    sn=I(sn.lo-es.hi,sn.hi+es.hi);cs=I(cs.lo-ec.hi,cs.hi+ec.hi)
    q=k%4
    return ((sn,cs),(cs,-sn),(-sn,-cs),(-cs,sn))[q]


def integrate_fourier(poly,center,z,pi):
    """Full even density's real Fourier integral on this reflected cell."""
    h=I.rat(1,32); sn,cs=sincos(z*center,pi)
    cycle=(cs,-sn,-cs,sn);term=I.coerce(1);cp=[]
    for k in range(DEGREE+1):
        if k:term=term*(z*h)/k
        cp.append(cycle[k%4]*term)
    out=mulpoly(poly,cp,DEGREE)
    return 4*h*sum((out[k]/(k+1) for k in range(0,len(out),2)),I.coerce(0))


def full_theta():
    """Every source index/time, via 84 cells and proved full tails."""
    pi=pi_interval();js=tuple(range(0,15,2));counts=(32,24,16,12)
    require(3*SCALE<pi.lo<pi.hi<4*SCALE,'pi enclosure')
    a=F('14.13472514173469');b=F('14.13472514173470')
    args=(a,b,3*(a+b)/2)
    raw={j:I.coerce(0) for j in js};four=[I.coerce(0) for _ in args]
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            cen=F(2*k+1,32);pol=cell_density(n,cen,pi)
            for j in js:raw[j]=raw[j]+integrate_moment(pol,cen,j)
            for j,z in enumerate(args):four[j]=four[j]+integrate_fourier(pol,cen,I.coerce(z),pi)
    ec0=I.rat(16*10**15,4**121)/I.rat(3,4)
    t0=16*(64*81**2+163)*exp(I.coerce(-150))
    es={}
    for j in js:
        ec=ec0*3**j;et=t0*factorial(j)
        ei=128*625*factorial(j)*exp(I.coerce(-75))/(2**j*I.rat(147,2)**(j+1))
        t=raw[j];raw[j]=I(t.lo-ec.hi,t.hi+ec.hi+et.hi+ei.hi)
        es[j]=[ec.record(),et.record(),ei.record()]
    require(raw[0].lo>I.rat(49,100).hi and raw[0].hi<I.rat(1,2).lo,'normalization')
    # Complex circles: |cos(z*t)|<=exp(43/8)<3^6.
    ecf=ec0*3**6
    ei0=128*625*exp(I.coerce(-75))/I.rat(147,2)
    ef=ecf+t0+ei0
    four=[I(t.lo-ef.hi,t.hi+ef.hi) for t in four]
    mu={0:I.coerce(1),**{j:raw[j]/raw[0] for j in js if j}}
    return raw,mu,four,{'cells':84,'theta_indices':4,'degree':DEGREE,'bits':BITS,
        'raw_errors':{str(j):x for j,x in es.items()},'fourier_error':ef.record(),
        'fourier_arguments':[str(z) for z in args]}

# IMR26 original four-group root brackets, rerun against fresh moments.
def fit_seed(mu):
    v=mu[2]; r4=mu[4]/v**2; r6=mu[6]/v**3; r8=mu[8]/v**4
    k4=r4-3; k6=r6-15*r4+30
    k8=r8-28*r6-35*r4*r4+420*r4-630
    s2=-k4/2; s3=k6/16; s4=-k8/272
    def data(a):
        r1=1-25*a; r2=s2-25*a*a; r3=s3-25*a**3
        e2=(r1*r1-r2)/2; e3=(r1**3-3*r1*r2+2*r3)/6
        return r1,e2,e3,r2,r3
    def g(a):
        e1,e2,e3,r2,r3=data(a)
        return 25*a**4+e1*r3-e2*r2+e3*e1-s4
    lo=F(220907,10**7); hi=F(220909,10**7)
    require(g(I.coerce(lo)).lo>0 and g(I.coerce(hi)).hi<0,'quartic IVT bracket')
    # Interval brackets for the three roots at EVERY a in this initial interval.
    def root_brackets(a, refine):
        e1,e2,e3,_,_=data(a)
        def f(x):return x**3-e1*x*x+e2*x-e3
        brackets=[(F(404,10000),F(406,10000),1),
                  (F(1415,10000),F(1418,10000),-1),
                  (F(2655,10000),F(2658,10000),1)]
        out=[]
        for l,h,sgn in brackets:
            fl=f(I.coerce(l))*sgn;fh=f(I.coerce(h))*sgn
            require(fl.hi<0 and fh.lo>0,'three positive cubic roots')
            if refine:
                for _ in range(65):
                    mid=(l+h)/2;fm=f(I.coerce(mid))*sgn
                    if fm.hi<0:l=mid
                    elif fm.lo>0:h=mid
                    else:break
            out.append(I(I.coerce(l).lo,I.coerce(h).hi))
        return out
    roots0=root_brackets(I(I.coerce(lo).lo,I.coerce(hi).hi),False)
    require(all(r.lo>I.coerce(hi).hi for r in roots0),'quartic derivative sign')
    for _ in range(65):
        mid=(lo+hi)/2;gm=g(I.coerce(mid))
        if gm.lo>0:lo=mid
        elif gm.hi<0:hi=mid
        else:break
    a=I(I.coerce(lo).lo,I.coerce(hi).hi)
    b,c,d=root_brackets(a,True)
    weights=[(v*x).sqrt() for x in (a,b,c,d)]
    k10=7936*(25*a**5+b**5+c**5+d**5)
    model10=k10+45*k8+210*k6*k4+630*k6+1575*k4*k4+3150*k4+945
    diff=model10-mu[10]/v**5
    require(diff.lo>I.rat(-123,1000).hi and diff.hi<I.rat(-122,1000).lo,
            'unmatched tenth moment')
    return {'s2':s2.record(),'s3':s3.record(),'s4':s4.record(),
        'a':a.record(),'b':b.record(),'c':c.record(),'d':d.record(),
        'weights':[x.record() for x in weights], 'multiplicities':[25,1,1,1],
        'standardized_tenth_difference':diff.record(),
        'left_sign_lower':g(I.coerce(lo)).lo,'right_sign_upper':g(I.coerce(hi)).hi}


