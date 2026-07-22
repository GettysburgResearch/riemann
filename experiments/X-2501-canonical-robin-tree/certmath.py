#!/usr/bin/env python3
"""Exact dyadic interval arithmetic for Robin-certificate verification.

All interval endpoints are integers over a common denominator 2**bits.  The
transcendental routines use only integer arithmetic, rational series, and proved
remainder bounds.  They do not call floating-point, Decimal transcendental
functions, mpmath, or external numerical libraries.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Iterable


@dataclass(frozen=True)
class Dyadic:
    bits: int
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.bits < 8:
            raise ValueError("bits must be at least 8")
        if self.lo > self.hi:
            raise ValueError("invalid interval")

    @property
    def scale(self) -> int:
        return 1 << self.bits

    @classmethod
    def integer(cls, n: int, bits: int) -> "Dyadic":
        v = n << bits
        return cls(bits, v, v)

    @classmethod
    def fraction(cls, q: Fraction, bits: int) -> "Dyadic":
        scale = 1 << bits
        p, d = q.numerator, q.denominator
        lo = (p * scale) // d
        hi = -((-p * scale) // d)
        return cls(bits, lo, hi)

    def _same(self, other: "Dyadic") -> None:
        if self.bits != other.bits:
            raise ValueError("precision mismatch")

    def add(self, other: "Dyadic") -> "Dyadic":
        self._same(other)
        return Dyadic(self.bits, self.lo + other.lo, self.hi + other.hi)

    def sub(self, other: "Dyadic") -> "Dyadic":
        self._same(other)
        return Dyadic(self.bits, self.lo - other.hi, self.hi - other.lo)

    def neg(self) -> "Dyadic":
        return Dyadic(self.bits, -self.hi, -self.lo)

    def mul(self, other: "Dyadic") -> "Dyadic":
        self._same(other)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        scale = self.scale
        pmin, pmax = min(products), max(products)
        return Dyadic(
            self.bits,
            pmin // scale,
            -((-pmax) // scale),
        )

    def mul_int(self, n: int) -> "Dyadic":
        if n >= 0:
            return Dyadic(self.bits, self.lo * n, self.hi * n)
        return Dyadic(self.bits, self.hi * n, self.lo * n)

    def div_pos_int(self, n: int) -> "Dyadic":
        if n <= 0:
            raise ValueError("positive divisor required")
        return Dyadic(self.bits, self.lo // n, -((-self.hi) // n))

    def div_positive(self, other: "Dyadic") -> "Dyadic":
        """Enclose self/other when self>=0 and other>0."""
        self._same(other)
        if self.lo < 0 or other.lo <= 0:
            raise ValueError("requires nonnegative numerator and positive denominator")
        scale = self.scale
        return Dyadic(
            self.bits,
            (self.lo * scale) // other.hi,
            -((-(self.hi * scale)) // other.lo),
        )

    def contains_fraction(self, q: Fraction) -> bool:
        return self.lo * q.denominator <= q.numerator * self.scale <= self.hi * q.denominator

    def lower_gt_fraction(self, q: Fraction) -> bool:
        return self.lo * q.denominator > q.numerator * self.scale

    def upper_le_fraction(self, q: Fraction) -> bool:
        return self.hi * q.denominator <= q.numerator * self.scale

    def to_json(self, digits: int = 36) -> dict[str, object]:
        return {
            "bits": self.bits,
            "lower_numerator": str(self.lo),
            "upper_numerator": str(self.hi),
            "lower_decimal_outward": dyadic_decimal(self.lo, self.bits, digits, upper=False),
            "upper_decimal_outward": dyadic_decimal(self.hi, self.bits, digits, upper=True),
        }


def dyadic_decimal(numerator: int, bits: int, digits: int, *, upper: bool) -> str:
    if digits < 0:
        raise ValueError("digits must be nonnegative")
    ten = 10**digits
    den = 1 << bits
    scaled = numerator * ten
    rounded = -((-scaled) // den) if upper else scaled // den
    sign = "-" if rounded < 0 else ""
    raw = str(abs(rounded)).rjust(digits + 1, "0")
    if digits == 0:
        return sign + raw
    return f"{sign}{raw[:-digits]}.{raw[-digits:]}"


def range_reduce_power_two(x: Fraction) -> tuple[int, Fraction]:
    if x <= 0:
        raise ValueError("positive argument required")
    p, q = x.numerator, x.denominator
    k = p.bit_length() - q.bit_length()
    y = Fraction(p, q << k) if k >= 0 else Fraction(p << (-k), q)
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1
    return k, y


def atanh_log_unit(y: Fraction, *, bits: int, terms: int) -> Dyadic:
    """Enclose log(y), 1<=y<=2, by the positive atanh expansion."""
    if not (1 <= y <= 2):
        raise ValueError("reduced logarithm argument outside [1,2]")
    if terms < 1:
        raise ValueError("terms must be positive")
    if y == 1:
        return Dyadic.integer(0, bits)
    z = (y - 1) / (y + 1)
    z_i = Dyadic.fraction(z, bits)
    z2 = z_i.mul(z_i)
    power = z_i
    partial = Dyadic.integer(0, bits)
    for j in range(terms):
        partial = partial.add(power.div_pos_int(2 * j + 1))
        power = power.mul(z2)
    one = Dyadic.integer(1, bits)
    tail = power.div_pos_int(2 * terms + 1).div_positive(one.sub(z2))
    doubled = partial.mul_int(2)
    return Dyadic(bits, doubled.lo, doubled.hi + 2 * tail.hi)


@lru_cache(maxsize=32)
def log_two_interval(bits: int, terms: int) -> Dyadic:
    return atanh_log_unit(Fraction(2), bits=bits, terms=terms)


def log_fraction(x: Fraction, *, bits: int, terms: int) -> Dyadic:
    if x <= 0:
        raise ValueError("positive logarithm argument required")
    if x == 1:
        return Dyadic.integer(0, bits)
    k, y = range_reduce_power_two(x)
    return atanh_log_unit(y, bits=bits, terms=terms).add(
        log_two_interval(bits, terms).mul_int(k)
    )


def log_dyadic(x: Dyadic, *, terms: int) -> Dyadic:
    if x.lo <= 0:
        raise ValueError("positive logarithm interval required")
    den = 1 << x.bits
    lo = log_fraction(Fraction(x.lo, den), bits=x.bits, terms=terms)
    hi = log_fraction(Fraction(x.hi, den), bits=x.bits, terms=terms)
    return Dyadic(x.bits, lo.lo, hi.hi)


def harmonic_interval(n: int, *, bits: int) -> Dyadic:
    if n < 1:
        raise ValueError("positive harmonic cutoff required")
    scale = 1 << bits
    lo = 0
    hi = 0
    for k in range(1, n + 1):
        lo += scale // k
        hi += (scale + k - 1) // k
    return Dyadic(bits, lo, hi)


@lru_cache(maxsize=16)
def euler_gamma_interval(bits: int, log_terms: int, harmonic_cutoff: int) -> Dyadic:
    """Use 1/(2(n+1)) < H_n-log n-gamma < 1/(2n)."""
    h = harmonic_interval(harmonic_cutoff, bits=bits)
    logn = log_fraction(Fraction(harmonic_cutoff), bits=bits, terms=log_terms)
    correction = Dyadic(
        bits,
        Dyadic.fraction(Fraction(1, 2 * (harmonic_cutoff + 1)), bits).lo,
        Dyadic.fraction(Fraction(1, 2 * harmonic_cutoff), bits).hi,
    )
    return h.sub(logn).sub(correction)


def exp_point_nonnegative(point: int, *, bits: int, terms: int) -> Dyadic:
    if point < 0:
        raise ValueError("nonnegative point required")
    x = Dyadic(bits, point, point)
    one = Dyadic.integer(1, bits)
    term = one
    total = one
    for j in range(1, terms + 1):
        term = term.mul(x).div_pos_int(j)
        total = total.add(term)
    next_term = term.mul(x).div_pos_int(terms + 1)
    ratio = x.div_pos_int(terms + 2)
    denominator = one.sub(ratio)
    if denominator.lo <= 0:
        raise ValueError("exponential tail ratio is not below one")
    tail = next_term.div_positive(denominator)
    return Dyadic(bits, total.lo, total.hi + tail.hi)


def exp_nonnegative(x: Dyadic, *, terms: int) -> Dyadic:
    if x.lo < 0:
        raise ValueError("nonnegative exponential interval required")
    lo = exp_point_nonnegative(x.lo, bits=x.bits, terms=terms)
    hi = exp_point_nonnegative(x.hi, bits=x.bits, terms=terms)
    return Dyadic(x.bits, lo.lo, hi.hi)


@dataclass(frozen=True)
class RobinParameters:
    bits: int = 256
    log_terms: int = 88
    exp_terms: int = 88
    harmonic_cutoff: int = 250_000

    def validate(self) -> None:
        if self.bits < 8:
            raise ValueError("bits must be at least 8")
        if self.log_terms < 1 or self.exp_terms < 1:
            raise ValueError("series term counts must be positive")
        if self.harmonic_cutoff < 1:
            raise ValueError("harmonic cutoff must be positive")


@lru_cache(maxsize=16)
def exp_gamma(params: RobinParameters) -> Dyadic:
    params.validate()
    gamma = euler_gamma_interval(
        params.bits, params.log_terms, params.harmonic_cutoff
    )
    return exp_nonnegative(gamma, terms=params.exp_terms)


def robin_rhs(n: int, params: RobinParameters) -> Dyadic:
    """Enclose exp(gamma)*log(log(n)); requires n>=3."""
    params.validate()
    if n < 3:
        raise ValueError("Robin RHS implementation requires n>=3")
    logn = log_fraction(Fraction(n), bits=params.bits, terms=params.log_terms)
    loglogn = log_dyadic(logn, terms=params.log_terms)
    return exp_gamma(params).mul(loglogn)


def product_fraction(values: Iterable[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result
