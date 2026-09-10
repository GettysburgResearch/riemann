#!/usr/bin/env python3
"""Outward fixed-grid real/complex arithmetic, adapted from GTP26. Not an RH proof.

Only Python's standard library is trusted. Intervals have integer endpoints
in units of 2**(-BITS), and each operation rounds outward. No float enters
an acceptance test. See check.py and PROOF.md for the accepting contract.
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import platform

BITS = 288
S = 1 << BITS


def ceildiv(n: int, d: int) -> int:
    if d <= 0:
        raise ValueError('positive denominator required')
    return -((-n) // d)


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        need(self.lo <= self.hi, 'unordered interval')

    @staticmethod
    def point(x: int | F) -> 'I':
        x = F(x)
        return I(x.numerator * S // x.denominator,
                 ceildiv(x.numerator * S, x.denominator))

    def __add__(self, other: object) -> 'I':
        o = as_i(other)
        return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self) -> 'I':
        return I(-self.hi, -self.lo)

    def __sub__(self, other: object) -> 'I':
        return self + (-as_i(other))

    def __rsub__(self, other: object) -> 'I':
        return as_i(other) - self

    def __mul__(self, other: object) -> 'I':
        o = as_i(other)
        p = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return I(min(p)//S, ceildiv(max(p), S))
    __rmul__ = __mul__

    def inv(self) -> 'I':
        if self.lo > 0:
            return I(S*S//self.hi, ceildiv(S*S, self.lo))
        if self.hi < 0:
            return -(-self).inv()
        raise ZeroDivisionError('interval contains zero')

    def __truediv__(self, other: object) -> 'I':
        return self * as_i(other).inv()

    def __rtruediv__(self, other: object) -> 'I':
        return as_i(other) / self

    def __pow__(self, k: int) -> 'I':
        if not isinstance(k, int) or k < 0:
            raise ValueError('nonnegative integer exponent required')
        ans, v = I.point(1), self
        while k:
            if k & 1:
                ans = ans*v
            v = v*v
            k >>= 1
        return ans

    def abs_upper(self) -> F:
        return F(max(abs(self.lo), abs(self.hi)), S)

    def widen(self, radius: F) -> 'I':
        need(radius >= 0, 'negative radius')
        r = ceildiv(radius.numerator*S, radius.denominator)
        return I(self.lo-r, self.hi+r)

    def contains(self, x: int | F) -> bool:
        x = F(x)
        return F(self.lo, S) <= x <= F(self.hi, S)

    def record(self) -> dict[str, object]:
        # Decimal strings here are outward bounds, not nearest-rounding claims.
        T = 10**18
        def dec(n: int) -> str:
            sign = '-' if n < 0 else ''
            n = abs(n)
            return f'{sign}{n//T}.{n%T:018d}'
        return {'lo_integer': str(self.lo), 'hi_integer': str(self.hi),
                'denominator_power_of_two': BITS,
                'outward_decimal_18': [dec(self.lo*T//S), dec(ceildiv(self.hi*T,S))]}


def as_i(x: object) -> I:
    if isinstance(x, I):
        return x
    if isinstance(x, (int, F)):
        return I.point(x)
    raise TypeError('only integer, Fraction or interval allowed')


@dataclass(frozen=True)
class C:
    re: I
    im: I

    @staticmethod
    def point(re: int | F = 0, im: int | F = 0) -> 'C':
        return C(I.point(re), I.point(im))

    def __add__(self, o: 'C') -> 'C':
        return C(self.re+o.re, self.im+o.im)

    def __neg__(self) -> 'C':
        return C(-self.re, -self.im)

    def __sub__(self, o: 'C') -> 'C':
        return self + (-o)

    def __mul__(self, o: 'C') -> 'C':
        return C(self.re*o.re-self.im*o.im, self.re*o.im+self.im*o.re)

    def scale(self, x: I | int | F) -> 'C':
        return C(self.re*x, self.im*x)

    def __truediv__(self, o: 'C') -> 'C':
        den = o.re*o.re+o.im*o.im
        need(den.lo > 0, 'complex denominator not certified nonzero')
        return C((self.re*o.re+self.im*o.im)/den,
                 (self.im*o.re-self.re*o.im)/den)

    def norm_upper(self) -> F:
        return self.re.abs_upper()+self.im.abs_upper()

    def widen(self, radius: F) -> 'C':
        return C(self.re.widen(radius), self.im.widen(radius))

    def record(self) -> dict[str, object]:
        return {'real': self.re.record(), 'imaginary': self.im.record()}


def sqrt_i(x: I) -> I:
    need(x.lo >= 0, 'nonnegative sqrt required')
    lo = isqrt(x.lo*S)
    hi = isqrt(x.hi*S)
    if hi*hi < x.hi*S:
        hi += 1
    return I(lo, hi)


def atan_small(x: F, terms: int) -> I:
    need(0 < x < 1 and terms >= 1, 'invalid arctangent parameters')
    acc = sum(((-1)**j * x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    rem = x**(2*terms+1)/F(2*terms+1)
    return I.point(acc).widen(rem)


def pi_i() -> I:
    return 16*atan_small(F(1,5),130)-4*atan_small(F(1,239),45)


def log_core(x: I, terms: int = 120) -> I:
    need(x.lo >= S and x.hi <= 2*S, 'log_core needs [1,2]')
    y = (x-1)/(x+1)
    term, out = y, I.point(0)
    for j in range(terms):
        out = out + term/F(2*j+1)
        term = term*y*y
    yh = F(y.hi, S)
    tail = 2*yh**(2*terms+1)/(F(2*terms+1)*(1-yh*yh))
    return (2*out).widen(tail)


def log_i(x: I) -> I:
    need(x.lo > 0, 'positive logarithm required')
    k = 0
    while x.lo < S:
        x = x*2
        k -= 1
    while x.hi > 2*S:
        x = x/2
        k += 1
    # Our inputs are narrow and away from power-of-two boundaries.
    need(S <= x.lo <= x.hi <= 2*S, 'ambiguous logarithm scaling')
    return log_core(x)+k*log_core(I.point(2))



def hull(a: F, b: F) -> I:
    return I(I.point(a).lo, I.point(b).hi)

def exp_i(x: I) -> I:
    """Taylor on |x/2^n|<=1/8, full absolute tail, then squaring."""
    n=0
    while x.abs_upper()>F(1,8):
        x=x/2;n+=1
    term=I.point(1);ans=term
    N=64
    for j in range(1,N+1):
        term=term*x/j;ans=ans+term
    b=x.abs_upper()
    rem=2*b**(N+1)/factorial(N+1)
    ans=ans.widen(rem)
    for _ in range(n):ans=ans*ans
    return I(max(0,ans.lo),ans.hi)

def atan_i(x: I) -> I:
    n=0
    while x.abs_upper()>F(1,4):
        x=x/(1+sqrt_i(1+x*x));n+=1
    term=x;ans=I.point(0);N=100
    for j in range(N):
        ans=ans+term/F(2*j+1)
        term=-term*x*x
    b=x.abs_upper()
    ans=ans.widen(b**(2*N+1)/F(2*N+1))
    return ans*(2**n)

def log_c(z: C) -> C:
    need(z.re.lo>0,'complex logarithm requires positive real part')
    return C(log_i(z.re*z.re+z.im*z.im)/2,atan_i(z.im/z.re))

def exp_c(z: C) -> C:
    pi=pi_i_cached()
    # This integer only selects a reduction; enclosing pi pays its whole error.
    k=(z.im.lo+z.im.hi+2*pi.lo)//(4*pi.lo)
    y=z.im-2*k*pi
    need(y.abs_upper()<4,'complex exponential reduction failed')
    term=C.point(1);ans=term
    for j in range(1,161):
        term=(term*C(I.point(0),y)).scale(F(1,j));ans=ans+term
    # e^4 < 81, giving a simple complete Taylor tail.
    rem=81*F(4)**161/factorial(161)
    ans=ans.widen(rem)
    return ans.scale(exp_i(z.re))

from functools import lru_cache
pi_i_cached=lru_cache(maxsize=1)(pi_i)

def bernoulli_numbers(N: int) -> list[F]:
    from math import comb
    b=[F(1)]
    for n in range(1,N+1):
        b.append(-sum(F(comb(n+1,k))*b[k] for k in range(n))/F(n+1))
    return b

def gamma_prefactor(q: C) -> tuple[C,C]:
    """Return (c^q/Gamma(1-q), log(c)+psi(1-q))."""
    K=80;N=12;b=bernoulli_numbers(2*N)
    z=C.point(1)-q
    need(z.re.lo>0,'gamma argument not in right half-plane')
    w=z+C.point(K);lw=log_c(w);inv=C.point(1)/w
    logg=(w-C.point(F(1,2)))*lw-w+C(log_i(2*pi_i_cached())/2,I.point(0))
    psi=lw-inv.scale(F(1,2))
    for j in range(1,N):
        power=C.point(1)
        for _ in range(2*j-1):power=power*inv
        logg=logg+power.scale(b[2*j]/F(2*j*(2*j-1)))
        psi=psi-(power*inv).scale(b[2*j]/F(2*j))
    re=F(w.re.lo,S)
    need(w.im.abs_upper() <= re/F(4), 'gamma remainder sector')
    # DLMF 5.11(ii): sec(arg(w)/2)^25 < (128/127)^25 < 2
    # when |Im(w)| <= Re(w)/4. Replace |w| below by Re(w).
    logg=logg.widen(2*abs(b[2*N])/F(2*N*(2*N-1))/re**(2*N-1))
    psi=psi.widen(2*abs(b[2*N])/F(2*N)/re**(2*N))
    for j in range(K):
        v=z+C.point(j);logg=logg-log_c(v);psi=psi-C.point(1)/v
    lc=log_i(pi_i_cached()/6)
    return exp_c(q.scale(lc)-logg),psi+C(lc,I.point(0))
