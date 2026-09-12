"""Outward fixed-dyadic intervals; no float arithmetic in accepting paths."""
from fractions import Fraction
from math import isqrt
BITS = 512
SCALE = 1 << BITS

def ceildiv(a, b):
    return -((-a)//b)

class I:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo=int(lo); self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def q(v):
        if isinstance(v,I): return v
        if isinstance(v,(float,bool)): raise TypeError('exact rational required')
        f=Fraction(v)
        return I(f.numerator*SCALE//f.denominator,ceildiv(f.numerator*SCALE,f.denominator))
    def __add__(self,other):
        o=I.q(other);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I.q(o)
    def __rsub__(self,o):return I.q(o)+-self
    def __mul__(self,other):
        o=I.q(other);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError('interval contains zero')
        return I((SCALE*SCALE)//self.hi,ceildiv(SCALE*SCALE,self.lo))
    def __truediv__(self,o):return self*I.q(o).inv()
    def __rtruediv__(self,o):return I.q(o)*self.inv()
    def __pow__(self,k):
        if not isinstance(k,int) or k<0: raise ValueError('nonnegative integer exponent required')
        if k==0:return I.q(1)
        # Squaring explicitly exploits the sign rather than dependency widening.
        if k==2:
            a,b=self.lo,self.hi
            if a<=0<=b:return I(0,ceildiv(max(a*a,b*b),SCALE))
            return I(min(a*a,b*b)//SCALE,ceildiv(max(a*a,b*b),SCALE))
        y=I.q(1);x=self
        while k:
            if k&1:y=y*x
            k//=2
            if k:x=x*x
        return y
    def sqrt(self):
        if self.lo<0:raise ValueError('negative square root')
        lo=isqrt(self.lo*SCALE);hi=isqrt(self.hi*SCALE)
        if hi*hi<self.hi*SCALE:hi+=1
        return I(lo,hi)
    def bounds(self):return [str(Fraction(self.lo,SCALE)),str(Fraction(self.hi,SCALE))]
    def inside(self,lo,hi):return Fraction(self.lo,SCALE)>Fraction(lo) and Fraction(self.hi,SCALE)<Fraction(hi)

def _exp_point(raw):
    if raw==0:return I.q(1)
    if raw<0:
        if -raw>=BITS*SCALE:return I(0,1)  # e>2.
        return _exp_point(-raw).inv()
    k=0
    while raw*8>SCALE*(1<<k):k+=1
    x=I.q(Fraction(raw,SCALE*(1<<k)))
    term=I.q(1);total=term
    for n in range(1,101):
        term=term*x/n;total=total+term
    nxt=term*x/101
    rem=nxt/(1-x/102)
    total=I(total.lo,total.hi+rem.hi)
    for _ in range(k):total=total**2
    return total

def exp(x):
    x=I.q(x)
    return I(_exp_point(x.lo).lo,_exp_point(x.hi).hi)

def pi():
    def atan_inv(q):
        v=sum((Fraction((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(128)),Fraction(0))
        # An even number of alternating terms ends below the positive limit.
        return I.q(v)+I(0,I.q(Fraction(1,257*q**257)).hi)
    return 16*atan_inv(5)-4*atan_inv(239)

from functools import lru_cache
@lru_cache(maxsize=8192)
def log_q(v):
    """Natural log of an exact positive rational by complete atanh series."""
    f=Fraction(v)
    if f<=0:raise ValueError('logarithm requires a positive argument')
    if f<1:return -log_q(1/f)
    k=0
    while f>=2:f/=2;k+=1
    def reduced(u):
        x=I.q((u-1)/(u+1));x2=x*x;term=x;total=I.q(0)
        for j in range(256):
            total=total+term/(2*j+1);term=term*x2
        remainder=2*term/513/(1-x2)
        out=2*total
        return I(out.lo,out.hi+remainder.hi)
    ans=reduced(f)
    if k:ans=ans+k*reduced(Fraction(2))
    return ans
