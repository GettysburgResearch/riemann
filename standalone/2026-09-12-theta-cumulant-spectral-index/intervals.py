#!/usr/bin/env python3
"""Outward dyadic primitives adapted from frozen NMT26 certify.py.
New source calculation uses 768 bits, 64th-order midpoint Taylor control.
No numerical result from the parent is an input. See SOURCES.json.
"""
from fractions import Fraction as F
from math import factorial, comb, isqrt
import argparse, json, hashlib
from pathlib import Path

BITS=768
S=1<<BITS

def ceildiv(a,b):
    return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def point(x):
        x=F(x)
        return I(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
    @staticmethod
    def bounds(a,b):
        a=F(a);b=F(b)
        return I(a.numerator*S//a.denominator,ceildiv(b.numerator*S,b.denominator))
    def __add__(self,y):
        y=asI(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-asI(y)
    def __rsub__(self,y):return asI(y)+-self
    def __mul__(self,y):
        y=asI(y);v=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return I(min(v)//S,ceildiv(max(v),S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ValueError('division through zero')
        return I(S*S//self.hi,ceildiv(S*S,self.lo))
    def __truediv__(self,y):return self*asI(y).inv()
    def __pow__(self,n):
        if type(n) is not int or n<0:raise ValueError('nonnegative integer power required')
        r=I.point(1);a=self
        while n:
            if n&1:r=r*a
            n//=2
            if n:a=a*a
        return r
    def widened(self,r):
        r=F(r);n=ceildiv(r.numerator*S,r.denominator)
        return I(self.lo-n,self.hi+n)
    def sqrt(self):
        if self.lo<0:raise ValueError("sqrt of negative interval")
        lo=isqrt(self.lo*S);hi=isqrt(self.hi*S)
        if hi*hi<self.hi*S:hi+=1
        return I(lo,hi)
    def contains(self,x):
        x=F(x);return F(self.lo,S)<=x<=F(self.hi,S)
    def decimal(self,digits=15):
        k=10**digits
        def fmt(a):
            return ('-' if a<0 else '')+str(abs(a)//k)+'.'+str(abs(a)%k).zfill(digits)
        return [fmt(self.lo*k//S),fmt(ceildiv(self.hi*k,S))]
    def raw(self):return [str(self.lo),str(self.hi)]

def asI(x):return x if isinstance(x,I) else I.point(x)

def exp_at(x):
    # x is an exact dyadic endpoint, not a float.
    if x==0:return I.point(1)
    # e>2 gives exp(x)<=2^-BITS for x<=-BITS.
    if x<=-BITS*S:return I(0,1)
    r=max(0,(8*abs(x)).bit_length()-BITS)
    while 8*abs(x)>S*(1<<r):r+=1
    y=I(x//(1<<r),ceildiv(x,1<<r))
    if max(abs(y.lo),abs(y.hi))*8>S:raise ValueError('exp reduction failed')
    term=I.point(1);total=term
    for j in range(1,97):
        term=term*y/j;total=total+term
    # For |y|<=1/8 the omitted tail is <=2 |y|^97/97!.
    rem=F(2,8**97*factorial(97));total=total.widened(rem)
    if total.lo<=0:raise ValueError('nonpositive reduced exponential')
    for _ in range(r):total=total*total
    return total

def exp(x):
    x=asI(x)
    if x.hi<=-BITS*S:return I(0,1)
    if x.hi<=0:
        # exp is 1-Lipschitz on the negative half-line.
        a=exp_at(x.lo)
        return I(a.lo,min(S,a.hi+x.hi-x.lo))
    return I(exp_at(x.lo).lo,exp_at(x.hi).hi)

def atan_inv(k):
    x=F(1,k);a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(220)),F(0))
    rem=x**441/441
    return I.bounds(a,a+rem) # 220 terms: final sign negative; next positive.

def pi_interval():return 16*atan_inv(5)-4*atan_inv(239)


def need(ok, message):
    if not ok:
        raise ValueError(message)

def abs_upper(x):
    x=asI(x)
    return F(max(abs(x.lo),abs(x.hi)),S)

def pow_signed(x,k):
    return x**k if k>=0 else (x**(-k)).inv()

def poly_eval(poly,x):
    out=I.point(0)
    for k in range(max(poly),-1,-1):
        out=out*x+poly.get(k,F(0))
    return out

def derivative_polynomials(n):
    p={1:F(-6),2:F(4)};ans=[]
    for j in range(n+1):
        ans.append(p)
        q={}
        for k,c in p.items():
            q[k]=q.get(k,F(0))+(2*k+F(1,2))*c
            q[k+1]=q.get(k+1,F(0))-2*c
        p={k:c for k,c in q.items() if c}
    return ans

