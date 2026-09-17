"""Reviewer A: outward dyadic intervals; no Arb or floating transcendental calls."""
from fractions import Fraction
from math import isqrt, factorial
S=1<<128

def ceildiv(a,b): return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,x=0,radius=0):
        if isinstance(x,I): self.lo,self.hi=x.lo,x.hi
        else:
            q=Fraction(x); self.lo=q.numerator*S//q.denominator;self.hi=ceildiv(q.numerator*S,q.denominator)
        if radius:
            r=I(radius);self.lo-=r.hi;self.hi+=r.hi
    @classmethod
    def raw(cls,l,h):
        if l>h: raise ValueError('reversed interval')
        z=object.__new__(cls);z.lo,z.hi=l,h;return z
    def __add__(self,o):
        o=I(o);return I.raw(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I(o)
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=I(o);a=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi];return I.raw(min(a)//S,ceildiv(max(a),S))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I(o)
        if o.lo<=0<=o.hi:raise ZeroDivisionError
        if o.hi<0:return (-self)/(-o)
        a=[(self.lo*S)//o.lo,(self.lo*S)//o.hi,(self.hi*S)//o.lo,(self.hi*S)//o.hi]
        b=[ceildiv(self.lo*S,o.lo),ceildiv(self.lo*S,o.hi),ceildiv(self.hi*S,o.lo),ceildiv(self.hi*S,o.hi)]
        return I.raw(min(a),max(b))
    def __rtruediv__(self,o):return I(o)/self
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError
        ans=I(1);v=self
        while n:
            if n&1:ans=ans*v
            n//=2
            if n:v=v*v
        return ans
    def __lt__(self,o):return self.hi<I(o).lo
    def __gt__(self,o):return self.lo>I(o).hi
    def __ge__(self,o):return self.lo>=I(o).hi
    def __float__(self):return float(Fraction((self.lo+self.hi)//2,S))
    def lower(self):return I.raw(self.lo,self.lo)
    def upper(self):return I.raw(self.hi,self.hi)
    def abs_lower(self):
        a=0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi));return I.raw(a,a)
    def abs_upper(self):
        a=max(abs(self.lo),abs(self.hi));return I.raw(a,a)
    def sqrt(self):
        if self.lo<0:raise ValueError
        a=isqrt(self.lo*S);b=isqrt(self.hi*S);return I.raw(a,b+(b*b!=self.hi*S))
    def sincos(self):
        p=pi(); mid=(self.lo+self.hi)//2
        n=(4*mid+(p.lo+p.hi)//2)//(p.lo+p.hi)
        r=self-n*(p/2);m=(r.lo+r.hi)//2;rad=max(m-r.lo,r.hi-m)
        if abs(m)>S:raise ValueError('range reduction exceeded unit Taylor domain')
        z=I.raw(m,m);z2=z*z
        sn=I(Fraction((-1)**24,factorial(49)));cs=I(Fraction((-1)**24,factorial(48)))
        for k in range(23,-1,-1):
            sn=sn*z2+Fraction((-1)**k,factorial(2*k+1));cs=cs*z2+Fraction((-1)**k,factorial(2*k))
        sn=sn*z
        es=ceildiv(S,factorial(51))+rad;ec=ceildiv(S,factorial(50))+rad
        sn=I.raw(sn.lo-es,sn.hi+es);cs=I.raw(cs.lo-ec,cs.hi+ec)
        n%=4
        return [(sn,cs),(cs,-sn),(-sn,-cs),(-cs,sn)][n]
    def sin(self):return self.sincos()[0]
    def cos(self):return self.sincos()[1]
    def sinc(self):
        if max(abs(self.lo),abs(self.hi))<=S:
            z2=self*self;ans=I(Fraction(1,factorial(49)))
            for k in range(23,-1,-1):ans=ans*z2+Fraction((-1)**k,factorial(2*k+1))
            e=ceildiv(S,factorial(51));return I.raw(ans.lo-e,ans.hi+e)
        return self.sin()/self
_PI=None

def pi():
    global _PI
    if _PI is None:
        def atan(q,n):
            a=sum((Fraction((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),Fraction())
            e=Fraction(1,(2*n+1)*q**(2*n+1));return I(a,e)
        _PI=16*atan(5,64)-4*atan(239,20)
    return _PI
I.pi=staticmethod(pi)
