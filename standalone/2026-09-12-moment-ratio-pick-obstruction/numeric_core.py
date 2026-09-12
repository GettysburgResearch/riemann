#!/usr/bin/env python3
"""Outward 288-bit scalar arithmetic, adapted from PR #851 intervals.py.

Only int and Fraction inputs; each operation rounds outwards. Python's
integer arithmetic, not a floating-point special-function library, is used.
Source: #851 @57726ef9b3bf90561df5a361e3b01169c892a62a, MIT license.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

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
        if not isinstance(x, (int, F)):
            raise TypeError('only integer or Fraction point allowed')
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


def atan_small(x: F, terms: int) -> I:
    need(0 < x < 1 and terms >= 1, 'invalid arctangent parameters')
    acc = sum(((-1)**j * x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    rem = x**(2*terms+1)/F(2*terms+1)
    return I.point(acc).widen(rem)


def pi_i() -> I:
    return 16*atan_small(F(1,5),130)-4*atan_small(F(1,239),45)


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
