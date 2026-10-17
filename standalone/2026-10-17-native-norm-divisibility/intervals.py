"""Rigorous dyadic intervals using integers only. No floating rounding contract.

ln uses the atanh series with a rational geometric tail. exp uses a
Taylor remainder at |x| <= 1 followed by five exact interval squarings.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial

BITS = 112
SCALE = 1 << BITS

def ceildiv(a: int, b: int) -> int:
    return -((-a)//b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('reversed interval')
    @staticmethod
    def exact_fraction(x):
        x = Fraction(x)
        return I((x.numerator*SCALE)//x.denominator,
                 ceildiv(x.numerator*SCALE,x.denominator))
    def __add__(self, other):
        other = other if isinstance(other,I) else I.exact_fraction(other)
        return I(self.lo+other.lo,self.hi+other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi,-self.lo)
    def __sub__(self,other):
        other = other if isinstance(other,I) else I.exact_fraction(other)
        return self + (-other)
    def __rsub__(self,other):
        return I.exact_fraction(other) - self
    def __mul__(self,other):
        other = other if isinstance(other,I) else I.exact_fraction(other)
        ps = [self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return I(min(ps)//SCALE,ceildiv(max(ps),SCALE))
    __rmul__ = __mul__
    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError('interval includes zero')
        vals = [Fraction(SCALE*SCALE,self.lo),Fraction(SCALE*SCALE,self.hi)]
        low,high = min(vals),max(vals)
        return I(low.numerator//low.denominator,ceildiv(high.numerator,high.denominator))
    def __truediv__(self,other):
        other = other if isinstance(other,I) else I.exact_fraction(other)
        return self*other.reciprocal()
    def __rtruediv__(self,other):
        return I.exact_fraction(other)*self.reciprocal()
    def contains(self,x):
        x = Fraction(x)
        return self.lo*x.denominator <= x.numerator*SCALE <= self.hi*x.denominator
    def lower_gt(self,x):
        x=Fraction(x)
        return self.lo*x.denominator > x.numerator*SCALE
    def upper_lt(self,x):
        x=Fraction(x)
        return self.hi*x.denominator < x.numerator*SCALE
    def decimal_bounds(self,places=16):
        fac=10**places
        lo=(self.lo*fac)//SCALE
        hi=ceildiv(self.hi*fac,SCALE)
        def fmt(n):
            sign='-' if n<0 else ''
            n=abs(n)
            return f'{sign}{n//fac}.{n%fac:0{places}d}'
        return [fmt(lo),fmt(hi)]
    def record(self):
        return {'lower_numerator':str(self.lo),'upper_numerator':str(self.hi),
                'denominator_power_two':BITS,'decimal_outward':self.decimal_bounds()}


def log_ratio(a: int,b: int,terms=40) -> I:
    """ln(a/b), 1 <= a/b <= 2. Every series term has separate outward rounding."""
    if not b <= a <= 2*b:
        raise ValueError('log range reduction failed')
    if a == b:
        return I(0,0)
    u,v = a-b,a+b
    z2=Fraction(u*u,v*v)
    z=Fraction(u,v)
    power=z
    low=high=0
    for j in range(terms):
        term=2*power/Fraction(2*j+1)
        low += (term.numerator*SCALE)//term.denominator
        high += ceildiv(term.numerator*SCALE,term.denominator)
        power *= z2
    tail=2*power/Fraction(2*terms+1)/(1-z2)
    high += ceildiv(tail.numerator*SCALE,tail.denominator)
    return I(low,high)

@lru_cache(maxsize=None)
def log_int(n: int) -> I:
    if n<1:
        raise ValueError('log requires positive integer')
    k=n.bit_length()-1
    return k*log_ratio(2,1) + log_ratio(n,1<<k)


def exp_minus(u: I, terms=40) -> I:
    """e**(-u), 0 <= u <= 32; proof uses e < 3."""
    if u.lo < 0 or u.hi > 32*SCALE:
        raise ValueError('exponential range reduction failed')
    z=(-u)/32
    # Horner evaluation of sum z**j/j!, with absolute remainder <=3/(N+1)!.
    p=I.exact_fraction(Fraction(1,factorial(terms)))
    for j in range(terms-1,-1,-1):
        p=p*z + Fraction(1,factorial(j))
    rem=ceildiv(3*SCALE,factorial(terms+1))
    p=I(p.lo-rem,p.hi+rem)
    if p.lo <= 0:
        raise ArithmeticError('positive exponential interval lost')
    for _ in range(5):
        p=p*p
    return p


def gaussian_ratio_weight(n: int) -> tuple[I,I]:
    L=log_int(n)
    if n == 1:
        return I.exact_fraction(1),L
    return exp_minus(L/2 + L*L/8),L


def certified_tails(cap: int) -> tuple[I,I]:
    """Absolute tails from sum_{n<=x}|b(n)| <= 3x (THEOREMS, Section 6)."""
    L=log_int(cap)
    if not L.lower_gt(4):
        raise ValueError('tail bound needs log cap > 4')
    e=exp_minus(L*L/8-L/2)
    aa=(L-2)/4
    tail0=3*e*(1+1/aa)
    tail2=3*e*(L*L*(1+1/aa)+2*L/(aa*aa)+2/(aa*aa*aa))
    return tail0,tail2
