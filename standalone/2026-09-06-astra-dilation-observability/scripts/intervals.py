"""Tiny outward-rounded dyadic intervals; standard library only.

Every endpoint is an integer multiple of 2**-BITS. No machine float enters
any proof-producing operation. Analytic remainders are explicit rationals.
This is auditable research code, not a formally verified interval library.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb, isqrt

BITS = 224
SCALE = 1 << BITS
LOG_TERMS = 90
DIGAMMA_SHIFT = 128
EM_ORDER = 16


def ceil_div(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("zero divisor")
    return -((-a) // b)


def rational(value: int | Fraction) -> Fraction:
    if type(value) is int:
        return Fraction(value)
    if type(value) is Fraction:
        return value
    raise TypeError("only exact int or Fraction accepted (not bool/float)")


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if type(self.lo) is not int or type(self.hi) is not int:
            raise TypeError("dyadic endpoints must be exact integers")
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @classmethod
    def of(cls, x: int | Fraction | I) -> I:
        if isinstance(x, I):
            return x
        f = rational(x)
        return cls((f.numerator * SCALE) // f.denominator,
                   ceil_div(f.numerator * SCALE, f.denominator))

    @classmethod
    def bounds(cls, low: int | Fraction, high: int | Fraction) -> I:
        a, b = rational(low), rational(high)
        if a > b:
            raise ValueError("reversed rational bounds")
        return cls(cls.of(a).lo, cls.of(b).hi)

    def __add__(self, other: int | Fraction | I) -> I:
        b = I.of(other)
        return I(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self) -> I:
        return I(-self.hi, -self.lo)

    def __sub__(self, other: int | Fraction | I) -> I:
        return self + (-I.of(other))

    def __rsub__(self, other: int | Fraction | I) -> I:
        return I.of(other) - self

    def __mul__(self, other: int | Fraction | I) -> I:
        b = I.of(other)
        p = [a * c for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        return I(min(p) // SCALE, ceil_div(max(p), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other: int | Fraction | I) -> I:
        b = I.of(other)
        if b.lo <= 0 <= b.hi:
            raise ZeroDivisionError("divisor interval contains zero")
        p = [(a * SCALE, c) for a in (self.lo, self.hi)
             for c in (b.lo, b.hi)]
        return I(min(a // c for a, c in p), max(ceil_div(a, c) for a, c in p))

    def __rtruediv__(self, other: int | Fraction | I) -> I:
        return I.of(other) / self

    def __pow__(self, n: int) -> I:
        if type(n) is not int or n < 0:
            raise ValueError("nonnegative integer exponent required")
        ans, a = I.of(1), self
        while n:
            if n & 1:
                ans = ans * a
            a = a * a
            n //= 2
        return ans

    def square(self) -> I:
        if self.lo <= 0 <= self.hi:
            return I(0, ceil_div(max(self.lo**2, self.hi**2), SCALE))
        return self * self

    def sqrt(self) -> I:
        if self.lo < 0:
            raise ValueError("sqrt of interval with negative lower endpoint")
        a, b = isqrt(self.lo * SCALE), isqrt(self.hi * SCALE)
        return I(a, b + (b*b != self.hi*SCALE))

    def contains(self, x: int | Fraction) -> bool:
        f = rational(x)
        return self.lo * f.denominator <= f.numerator*SCALE <= self.hi*f.denominator

    def overlaps(self, b: I) -> bool:
        return max(self.lo, b.lo) <= min(self.hi, b.hi)

    def width(self) -> Fraction:
        return Fraction(self.hi-self.lo, SCALE)

    def decimal_bounds(self, digits: int = 12) -> list[str]:
        if type(digits) is not int or not 0 <= digits <= 80:
            raise ValueError("digits outside 0..80")
        unit = 10**digits
        vals = [self.lo*unit//SCALE, ceil_div(self.hi*unit, SCALE)]
        out = []
        for a in vals:
            sign = "-" if a < 0 else ""
            a = abs(a)
            out.append(f"{sign}{a//unit}.{a%unit:0{digits}d}" if digits else f"{sign}{a}")
        return out

    def record(self) -> dict[str, object]:
        return {"bits": BITS, "lo": str(self.lo), "hi": str(self.hi),
                "decimal_enclosure": self.decimal_bounds()}


def _atanh_log(z: Fraction) -> I:
    if not 0 <= z <= Fraction(1, 3):
        raise ValueError("log range reduction failed")
    x = I.of(z)
    step, power, out = x*x, x, I.of(0)
    for j in range(LOG_TERMS):
        out += power / (2*j+1)
        power *= step
    remainder = 2*z**(2*LOG_TERMS+1) / ((2*LOG_TERMS+1)*(1-z*z))
    return 2*out + I.bounds(0, remainder)


@lru_cache(maxsize=32768, typed=True)
def log_q(x: Fraction) -> I:
    x = rational(x)
    if x <= 0:
        raise ValueError("log requires a positive rational")
    y, e = x, 0
    while y >= 2:
        y /= 2
        e += 1
    while y < 1:
        y *= 2
        e -= 1
    return _atanh_log((y-1)/(y+1)) + e*_atanh_log(Fraction(1, 3))


@lru_cache(maxsize=1)
def bernoulli() -> tuple[Fraction, ...]:
    # Sum_{k=0}^{n} binom(n+1,k) B_k = 0, n>=1; B_1=-1/2.
    values = [Fraction(1)]
    for n in range(1, 2*EM_ORDER+1):
        values.append(-sum(Fraction(comb(n+1,k))*values[k] for k in range(n))/(n+1))
    return tuple(values)


@lru_cache(maxsize=32768, typed=True)
def psi_q(x: Fraction) -> I:
    """Rigorous digamma enclosure from shifted Euler--Maclaurin.

    The integral remainder after EM_ORDER terms is bounded by
    sup_{0<=u<=1}|B_{2m}(u)|/(2m*y**(2m)), y=x+DIGAMMA_SHIFT.
    Coefficient l1 norm bounds the polynomial supremum. See NUMERICS.md.
    """
    x = rational(x)
    if x <= 0:
        raise ValueError("digamma requires a positive rational")
    b = bernoulli()
    y = x + DIGAMMA_SHIFT
    ans = log_q(y) - I.of(1)/(2*y)
    for k in range(1, EM_ORDER+1):
        ans -= I.of(b[2*k] / (2*k*y**(2*k)))
    degree = 2*EM_ORDER
    polynomial_bound = sum(Fraction(comb(degree, k))*abs(b[k]) for k in range(degree+1))
    remainder = polynomial_bound / (degree*y**degree)
    ans += I.bounds(-remainder, remainder)
    for j in range(DIGAMMA_SHIFT):
        ans -= I.of(1/(x+j))
    return ans


def atan_inverse(q: int, terms: int = 100) -> I:
    if type(q) is not int or q < 2 or type(terms) is not int or terms < 1:
        raise ValueError("invalid arctan parameters")
    x = Fraction(1, q)
    total = sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms))
    err = x**(2*terms+1)/(2*terms+1)
    return I.bounds(total-err, total+err)


def pi_interval() -> I:
    # Machin's formula; elementary tangent addition fixes the branch in (3,4).
    return 16*atan_inverse(5)-4*atan_inverse(239)
