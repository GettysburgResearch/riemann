"""512-bit outward dyadic arithmetic. Elementary-series contracts: see PROOF.md §3.
All endpoints are integers divided by 2**BITS; no binary64 primitive is used.
"""
"""Outward fixed-point intervals: every stored endpoint is an integer / 2**BITS.
Elementary constants/functions use rational series and explicit remainder bounds.
"""
from math import isqrt, factorial
from fractions import Fraction
BITS = 512
S = 1 << BITS

class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, a=0, b=None, *, raw=False):
        if raw:
            self.lo, self.hi = (int(a), int(b))
            return
        if isinstance(a, I):
            self.lo, self.hi = (a.lo, a.hi)
            return
        a = Fraction(a)
        b = a if b is None else Fraction(b)
        self.lo = a.numerator * S // a.denominator
        self.hi = -(-b.numerator * S // b.denominator)
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    def __add__(a, b):
        b = I(b)
        return I(a.lo + b.lo, a.hi + b.hi, raw=True)
    __radd__ = __add__

    def __neg__(a):
        return I(-a.hi, -a.lo, raw=True)

    def __sub__(a, b):
        return a + -I(b)

    def __rsub__(a, b):
        return I(b) + -a

    def __mul__(a, b):
        b = I(b)
        v = (a.lo * b.lo, a.lo * b.hi, a.hi * b.lo, a.hi * b.hi)
        return I(min(v) // S, -(-max(v) // S), raw=True)
    __rmul__ = __mul__

    def __truediv__(a, b):
        b = I(b)
        if b.lo <= 0 <= b.hi:
            raise ValueError('division interval contains zero')
        if b.lo == b.hi and b.lo % S == 0:
            k = b.lo // S
            if k > 0:
                return I(a.lo // k, -((-a.hi) // k), raw=True)
            return I(a.hi // k, -((-a.lo) // k), raw=True)
        lows = [x * S // y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        highs = [-((-x * S) // y) for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return I(min(lows), max(highs), raw=True)

    def __rtruediv__(a, b):
        return I(b) / a

    def __pow__(a, n):
        if n < 0:
            return I(1) / a ** (-n)
        out = I(1)
        while n:
            if n & 1:
                out = out * a
            a = a * a
            n //= 2
        return out

    def absmax(a):
        return max(abs(a.lo), abs(a.hi))

    def sqrt(a):
        if a.lo < 0:
            raise ValueError('negative sqrt')
        low = isqrt(a.lo * S)
        up = isqrt(a.hi * S)
        if up * up < a.hi * S:
            up += 1
        return I(low, up, raw=True)

    def widen(a, e):
        e = I(e).absmax()
        return I(a.lo - e, a.hi + e, raw=True)

    def exp(a):
        shifts = max(0, a.absmax().bit_length() - BITS + 5)
        x = a / (1 << shifts)
        if x.absmax() > S // 16:
            raise ValueError('exp reduction')
        term = out = I(1)
        for k in range(1, 97):
            term = term * x / k
            out = out + term
        out = out.widen(Fraction(2, 16 ** 97 * factorial(97)))
        for j in range(shifts):
            out = out * out
        if out.hi < 0:
            raise ValueError('exp sign')
        return I(max(0, out.lo), out.hi, raw=True)

    def pair(a):
        return [str(a.lo), str(a.hi)]

def pi():

    def atan_inv(q):
        out = Fraction(0)
        for k in range(256):
            out += Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
        return I(out).widen(Fraction(1, 513 * q ** 513))
    return 16 * atan_inv(5) - 4 * atan_inv(239)
PI = pi()

def sincos(x):
    x = I(x)
    m = ((x.lo + x.hi) * 2 + (PI.lo + PI.hi) // 2) // (PI.lo + PI.hi)
    y = x - m * (PI / 2)
    if y.absmax() > S:
        raise ValueError('trig range reduction')
    y2 = y * y
    s = st = y
    c = ct = I(1)
    for k in range(1, 100):
        st = -st * y2 / (2 * k * (2 * k + 1))
        ct = -ct * y2 / ((2 * k - 1) * (2 * k))
        s = s + st
        c = c + ct
    e = Fraction(2, factorial(199))
    s = s.widen(e)
    c = c.widen(e)
    if m % 4 == 0:
        return (s, c)
    if m % 4 == 1:
        return (c, -s)
    if m % 4 == 2:
        return (-s, -c)
    return (-c, s)

class C:
    __slots__ = ('r', 'i')

    def __init__(self, r=0, i=0):
        if isinstance(r, C):
            self.r, self.i = (r.r, r.i)
        else:
            self.r, self.i = (I(r), I(i))

    def __add__(a, b):
        b = C(b)
        return C(a.r + b.r, a.i + b.i)
    __radd__ = __add__

    def __neg__(a):
        return C(-a.r, -a.i)

    def __sub__(a, b):
        return a + -C(b)

    def __rsub__(a, b):
        return C(b) + -a

    def __mul__(a, b):
        b = C(b)
        return C(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)
    __rmul__ = __mul__

    def __truediv__(a, b):
        if not isinstance(b, C):
            return C(a.r / b, a.i / b)
        den = b.r * b.r + b.i * b.i
        return C((a.r * b.r + a.i * b.i) / den, (a.i * b.r - a.r * b.i) / den)

    def widen(a, e):
        return C(a.r.widen(e), a.i.widen(e))

    def pair(a):
        return [a.r.pair(), a.i.pair()]

def cm_sincos(z):
    s, c = sincos(z.r)
    ep = z.i.exp()
    em = (-z.i).exp()
    ch = (ep + em) / 2
    sh = (ep - em) / 2
    return (C(s * ch, c * sh), C(c * ch, -s * sh))

def mul(a, b, n):
    out = []
    for k in range(n + 1):
        out.append(sum((a[j] * b[k - j] for j in range(k + 1)), I(0)))
    return out

def exp_series(a, n):
    out = [a[0].exp()]
    for k in range(1, n + 1):
        out.append(sum((j * a[j] * out[k - j] for j in range(1, k + 1)), I(0)) / k)
    return out

def sqrt_series(a, n):
    out = [a[0].sqrt()]
    if out[0].lo <= 0:
        raise ValueError('sqrt constant not proved positive')
    for k in range(1, n + 1):
        out.append((a[k] - sum((out[j] * out[k - j] for j in range(1, k)), I(0))) / (2 * out[0]))
    return out
