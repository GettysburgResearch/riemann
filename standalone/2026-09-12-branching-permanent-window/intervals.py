"""Fixed-point outward intervals. Exact rational inputs only; no float acceptance."""
from fractions import Fraction as Q
from math import factorial
BITS=256
S=1<<BITS

def ceildiv(a,b): return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi):
        if type(lo) is not int or type(hi) is not int or lo>hi: raise ValueError('invalid interval')
        self.lo,self.hi=lo,hi
    @staticmethod
    def of(x):
        if isinstance(x,I): return x
        if type(x) not in (int,Q): raise TypeError('exact input required')
        x=Q(x); return I(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
    def __add__(a,b):
        b=I.of(b);return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):return I(-a.hi,-a.lo)
    def __sub__(a,b):return a+-I.of(b)
    def __rsub__(a,b):return I.of(b)+-a
    def __mul__(a,b):
        b=I.of(b);v=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        return I(min(v)//S,ceildiv(max(v),S))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=I.of(b)
        if b.lo<=0<=b.hi:raise ZeroDivisionError('interval contains zero')
        v=[(x*S,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(x//y for x,y in v),max(ceildiv(x,y) for x,y in v))
    def __rtruediv__(a,b):return I.of(b)/a
    def abs_upper(a):return Q(max(abs(a.lo),abs(a.hi)),S)
    def inflate(a,e):
        k=I.of(e).hi
        if k<0:raise ValueError('negative radius')
        return I(a.lo-k,a.hi+k)
    def midpoint(a):return (a.lo+a.hi)//2
    def rec(a):return [hex(a.lo),hex(a.hi)]

class C:
    __slots__=('re','im')
    def __init__(self,re=0,im=0):self.re,self.im=I.of(re),I.of(im)
    @staticmethod
    def of(z):return z if isinstance(z,C) else C(z)
    def __add__(a,b):
        b=C.of(b);return C(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __neg__(a):return C(-a.re,-a.im)
    def __sub__(a,b):return a+-C.of(b)
    def __rsub__(a,b):return C.of(b)+-a
    def __mul__(a,b):
        b=C.of(b);return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def __truediv__(a,b):return C(a.re/b,a.im/b)
    def inflate(a,e):return C(a.re.inflate(e),a.im.inflate(e))
    def l1_upper(a):return a.re.abs_upper()+a.im.abs_upper()
    def midpoint(a):return (a.re.midpoint(),a.im.midpoint())

def exp_i(x):
    x=I.of(x);k=0
    while x.abs_upper()>Q(1,8):x=x/2;k+=1
    term=I.of(1);out=term
    for j in range(1,49):term=term*x/j;out+=term
    out=out.inflate(2*Q(1,8)**49/factorial(49))
    for _ in range(k):out=out*out
    return out

def pi_i():
    def at(x,n):
        x=Q(x)
        return I.of(sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(n)),Q())).inflate(x**(2*n+1)/(2*n+1))
    return 16*at(Q(1,5),64)-4*at(Q(1,239),20)
