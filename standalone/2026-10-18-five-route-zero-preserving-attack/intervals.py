"""Small outward rational intervals. No floating-point accepting arithmetic.

Log uses the atanh series; atan uses its alternating series and monotone
half-angle/reciprocal reductions; pi uses Machin's identity. Every operation
rounds outwards to a dyadic grid to keep rational sizes bounded. This is a
new implementation in this packet, not an independently authored backend.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt

BITS = 96
GRID = 1 << BITS

def down(x):
    x = Q(x)
    return Q((x.numerator * GRID) // x.denominator, GRID)

def up(x):
    return -down(-Q(x))

class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, lo, hi=None):
        lo, hi = Q(lo), Q(lo if hi is None else hi)
        if lo > hi:
            raise ValueError('reversed interval')
        self.lo, self.hi = down(lo), up(hi)
    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-as_i(other))
    def __rsub__(self, other):
        return as_i(other) - self
    def __mul__(self, other):
        other = as_i(other)
        xs = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(xs),max(xs))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError('interval contains zero')
        return self * I(1/other.hi,1/other.lo)
    def __rtruediv__(self, other):
        return as_i(other) / self
    def square(self):
        if self.lo <= 0 <= self.hi:
            return I(0,max(self.lo*self.lo,self.hi*self.hi))
        return I(min(self.lo*self.lo,self.hi*self.hi),
                 max(self.lo*self.lo,self.hi*self.hi))
    def text(self):
        return [str(self.lo),str(self.hi)]

def as_i(x):
    return x if isinstance(x,I) else I(x)

def sqrt_scalar(x):
    x = Q(x)
    if x < 0:
        raise ValueError('negative square root')
    k = isqrt((x.numerator * GRID * GRID) // x.denominator)
    lo = Q(k,GRID)
    return I(lo,lo if lo*lo == x else Q(k+1,GRID))

def sqrt_i(x):
    x = as_i(x)
    return I(sqrt_scalar(x.lo).lo,sqrt_scalar(x.hi).hi)

def _log_unit(x):
    # 1 <= x <= 2, r <= 1/3. All omitted terms are positive.
    r = (x-1)/(x+1)
    s = Q(0)
    for j in range(32):
        s += 2*r**(2*j+1)/(2*j+1)
    tail = 2*r**65/(65*(1-r*r))
    return I(s,s+tail)

@lru_cache(maxsize=4096)
def log_scalar(x):
    x = Q(x)
    if x <= 0:
        raise ValueError('nonpositive logarithm')
    k = 0
    while x < 1:
        x *= 2; k -= 1
    while x > 2:
        x /= 2; k += 1
    return _log_unit(x) + k*_log_unit(Q(2))

def log_i(x):
    x = as_i(x)
    return I(log_scalar(x.lo).lo,log_scalar(x.hi).hi)

def atan_small(x):
    x = Q(x)
    if not 0 <= x <= Q(1,2):
        raise ValueError('atan_small domain')
    s = sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(48)),Q(0))
    return I(s,s+x**97/97)

@lru_cache(maxsize=1)
def pi_i():
    return 16*atan_small(Q(1,5))-4*atan_small(Q(1,239))

def atan_scalar(x):
    x = Q(x)
    if x < 0:
        return -atan_scalar(-x)
    if x <= Q(1,2):
        return atan_small(x)
    if x > 1:
        return pi_i()/2-atan_scalar(1/x)
    v = I(x)/(1+sqrt_i(1+x*x))
    return 2*I(atan_small(v.lo).lo,atan_small(v.hi).hi)

def j_scalar(v):
    """Integral_0^1 (1-y) log(1+v^2 y^2)dy, with an entire tail."""
    v = Q(v)
    if v < 0:
        raise ValueError('negative v')
    if v <= Q(1,2):
        s = sum(((-1)**(j+1)*v**(2*j)/Q(j*(2*j+1)*(2*j+2))
                 for j in range(1,13)),Q(0))
        tail = v**26/Q(13*27*28)
        return I(s,s+tail)
    return (Q(1,2)-1/(2*v*v))*log_scalar(1+v*v)-Q(3,2)+2*atan_scalar(v)/v

def j_i(v):
    v = as_i(v)
    return I(j_scalar(v.lo).lo,j_scalar(v.hi).hi)

def phi_sieve(n):
    p = list(range(n+1))
    for q in range(2,n+1):
        if p[q] == q:
            for k in range(q,n+1,q):
                p[k] -= p[k]//q
    return p

def B_positive(b, cutoff=512):
    """Positive totient series, including its full a>cutoff tail."""
    b = as_i(b)
    if b.lo < 0 or cutoff < 1:
        raise ValueError('B domain')
    pi = pi_i()
    phi = phi_sieve(cutoff)
    ans = I(0)
    for a in range(1,cutoff+1):
        ans += Q(phi[a],a)*j_i(b/(2*pi*a))
    tail = b.hi*b.hi/(48*pi.lo*pi.lo*cutoff)
    return ans + I(0,tail)
