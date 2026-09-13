#!/usr/bin/env python3
"""Theta primitives adapted from ICR26, PR863 at 0640c9c59be0bf20c18258460a7517fb09728e82.
The moment list is extended from 16 to 18; the complete analytic remainders are
rederived in PROOF.md. Same interval backend, not independent arithmetic.
No input moment receipt or special-function oracle is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

BITS=320
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


def theta_moments():
    pi=pi_interval()
    require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    js=tuple(range(0,19,2));counts=(32,24,16,12)
    totals={j:I.coerce(0) for j in js}
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            center=F(2*k+1,32)
            d=cell_density(n,center,pi)
            for j in js:totals[j]+=integrate_moment(d,center,j)
    errs={}
    for j in js:
        # Cauchy circle radius1/8, half-cell1/32. Full source, not just a truncation.
        e=I.rat(16*10**11*2**j,4**(DEGREE+1))/F(3,4)
        tails=I.coerce(0)
        for n,cnt in enumerate(counts,1):
            U=F(cnt,16);q=pi*n*n;E=exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            tails+=8*q*q*exp(F(9,2)*I.coerce(U)-q*E)*sum(
                (comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*625*exp(-25*pi)*factorial(j)/(50*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi, totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    require(totals[0].lo>0,'normalization')
    mu={j:totals[j]/totals[0] for j in js[1:]}
    return totals,mu,errs


def cumulants(mom):
    k=[mom[0]*0 for _ in mom]
    for n in range(1,len(mom)):
        k[n]=mom[n]-sum((comb(n-1,j-1)*k[j]*mom[n-j] for j in range(1,n)),mom[0]*0)
    return k


def inverse(a):
    n=len(a);b=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for col in range(n):
        k=next(i for i in range(col,n) if b[i][col])
        b[k],b[col]=b[col],b[k];v=b[col][col];b[col]=[x/v for x in b[col]]
        for i in range(n):
            if i==col:continue
            v=b[i][col];b[i]=[x-v*y for x,y in zip(b[i],b[col])]
    return [row[n:] for row in b]


def absup(x):return max(abs(x.lo),abs(x.hi))


