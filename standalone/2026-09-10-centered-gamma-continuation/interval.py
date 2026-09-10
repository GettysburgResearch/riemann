"""Outward dyadic arithmetic. No numerical package or floating arithmetic.
All endpoints are integers in units 2**-512. See CERTIFICATE.md for remainders.
"""
from math import isqrt, factorial
from fractions import Fraction
BITS = 512
S = 1 << BITS

class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, a=0, b=None, *, raw=False):
        if raw:
            self.lo, self.hi = int(a), int(b)
        elif isinstance(a, I):
            self.lo, self.hi = a.lo, a.hi
        else:
            a = Fraction(a); b = a if b is None else Fraction(b)
            self.lo = a.numerator*S//a.denominator
            self.hi = -((-b.numerator*S)//b.denominator)
        if self.lo > self.hi:
            raise ValueError('reversed interval')
    def __add__(a, b):
        b = I(b); return I(a.lo+b.lo, a.hi+b.hi, raw=True)
    __radd__ = __add__
    def __neg__(a):
        return I(-a.hi, -a.lo, raw=True)
    def __sub__(a, b):
        return a+-I(b)
    def __rsub__(a, b):
        return I(b)+-a
    def __mul__(a, b):
        b = I(b)
        v = (a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi)
        return I(min(v)//S, -((-max(v))//S), raw=True)
    __rmul__ = __mul__
    def __truediv__(a, b):
        b = I(b)
        if b.lo <= 0 <= b.hi:
            raise ValueError('division interval contains zero')
        v = [Fraction(x*S, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        lo, hi = min(v), max(v)
        return I(lo.numerator//lo.denominator, -((-hi.numerator)//hi.denominator), raw=True)
    def __rtruediv__(a, b):
        return I(b)/a
    def __pow__(a, n):
        if type(n) is not int:
            raise TypeError('integer exponent required')
        if n < 0:
            return I(1)/(a**(-n))
        out = I(1)
        while n:
            if n & 1: out = out*a
            a = a*a; n //= 2
        return out
    def absmax(a):
        return max(abs(a.lo), abs(a.hi))
    def sqrt(a):
        if a.lo < 0:
            raise ValueError('negative sqrt')
        lo = isqrt(a.lo*S); hi = isqrt(a.hi*S)
        if hi*hi < a.hi*S: hi += 1
        return I(lo, hi, raw=True)
    def widen(a, e):
        e = I(e).absmax(); return I(a.lo-e, a.hi+e, raw=True)
    def exp(a):
        shifts = max(0, a.absmax().bit_length()-BITS+5)
        x = a/(1 << shifts)
        if x.absmax() > S//16:
            raise ValueError('exp reduction failed')
        term = out = I(1)
        for k in range(1, 97):
            term = term*x/k; out = out+term
        out = out.widen(Fraction(2, 16**97*factorial(97)))
        for _ in range(shifts):
            out = out*out
        return I(max(0, out.lo), out.hi, raw=True)
    def pair(a):
        return [str(a.lo), str(a.hi)]

def pi():
    def atan_inv(q):
        out = sum((Fraction((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(256)), Fraction(0))
        return I(out).widen(Fraction(1, 513*q**513))
    return 16*atan_inv(5)-4*atan_inv(239)
PI = pi()

def sincos(x):
    x = I(x)
    m = (4*(x.lo+x.hi)+PI.lo+PI.hi)//(2*(PI.lo+PI.hi))
    y = x-m*(PI/2)
    if y.absmax() > S:
        raise ValueError('trig reduction failed')
    y2 = y*y; s = st = y; c = ct = I(1)
    for k in range(1, 100):
        st = -st*y2/((2*k)*(2*k+1))
        ct = -ct*y2/((2*k-1)*(2*k))
        s = s+st; c = c+ct
    e = Fraction(2, factorial(199)); s = s.widen(e); c = c.widen(e)
    return ((s, c), (c, -s), (-s, -c), (-c, s))[m % 4]

class C:
    __slots__ = ('r', 'i')
    def __init__(self, r=0, i=0):
        if isinstance(r, C): self.r, self.i = r.r, r.i
        else: self.r, self.i = I(r), I(i)
    def __add__(a, b):
        b = C(b); return C(a.r+b.r, a.i+b.i)
    __radd__ = __add__
    def __neg__(a): return C(-a.r, -a.i)
    def __sub__(a, b): return a+-C(b)
    def __rsub__(a, b): return C(b)+-a
    def __mul__(a, b):
        b = C(b); return C(a.r*b.r-a.i*b.i, a.r*b.i+a.i*b.r)
    __rmul__ = __mul__
    def __truediv__(a, b):
        if not isinstance(b, C): return C(a.r/b, a.i/b)
        den = b.r*b.r+b.i*b.i
        return C((a.r*b.r+a.i*b.i)/den, (a.i*b.r-a.r*b.i)/den)
    def widen(a, e): return C(a.r.widen(e), a.i.widen(e))
    def pair(a): return [a.r.pair(), a.i.pair()]

def cm_sincos(z):
    s, c = sincos(z.r); ep = z.i.exp(); em = (-z.i).exp()
    ch, sh = (ep+em)/2, (ep-em)/2
    return C(s*ch, c*sh), C(c*ch, -s*sh)

def mul(a, b, n):
    return [sum((a[j]*b[k-j] for j in range(k+1)), I(0)) for k in range(n+1)]

def exp_series(a, n):
    out = [a[0].exp()]
    for k in range(1, n+1):
        out.append(sum((j*a[j]*out[k-j] for j in range(1, k+1)), I(0))/k)
    return out

def sqrt_series(a, n):
    out = [a[0].sqrt()]
    if out[0].lo <= 0:
        raise ValueError('sqrt constant not proved positive')
    for k in range(1, n+1):
        out.append((a[k]-sum((out[j]*out[k-j] for j in range(1, k)), I(0)))/(2*out[0]))
    return out
