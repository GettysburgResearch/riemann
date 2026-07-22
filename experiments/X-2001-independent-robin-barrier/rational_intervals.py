#!/usr/bin/env python3
"""Pure-integer dyadic interval arithmetic for elementary constants.

No floating-point or decimal transcendental operation is used.  Every interval
endpoint is an integer divided by a fixed power of two.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Final


@dataclass(frozen=True)
class DyadicInterval:
    bits: int
    lower: int
    upper: int

    def __post_init__(self) -> None:
        if self.bits < 1:
            raise ValueError("bits must be positive")
        if self.lower > self.upper:
            raise ValueError("lower endpoint exceeds upper endpoint")

    @property
    def scale(self) -> int:
        return 1 << self.bits

    @classmethod
    def exact_integer(cls, value: int, bits: int) -> "DyadicInterval":
        scaled = value << bits
        return cls(bits, scaled, scaled)

    @classmethod
    def from_fraction(cls, value: Fraction, bits: int) -> "DyadicInterval":
        scale = 1 << bits
        p, q = value.numerator, value.denominator
        lower = (p * scale) // q
        upper = -((-p * scale) // q)
        return cls(bits, lower, upper)

    @classmethod
    def from_ratio(cls, numerator: int, denominator: int, bits: int) -> "DyadicInterval":
        if denominator <= 0:
            raise ValueError("denominator must be positive")
        return cls.from_fraction(Fraction(numerator, denominator), bits)

    def point_lower(self) -> "DyadicInterval":
        return DyadicInterval(self.bits, self.lower, self.lower)

    def point_upper(self) -> "DyadicInterval":
        return DyadicInterval(self.bits, self.upper, self.upper)

    def add(self, other: "DyadicInterval") -> "DyadicInterval":
        self._require_same_bits(other)
        return DyadicInterval(self.bits, self.lower + other.lower, self.upper + other.upper)

    def subtract(self, other: "DyadicInterval") -> "DyadicInterval":
        self._require_same_bits(other)
        return DyadicInterval(self.bits, self.lower - other.upper, self.upper - other.lower)

    def negate(self) -> "DyadicInterval":
        return DyadicInterval(self.bits, -self.upper, -self.lower)

    def multiply(self, other: "DyadicInterval") -> "DyadicInterval":
        self._require_same_bits(other)
        products = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        scale = self.scale
        low_product = min(products)
        high_product = max(products)
        lower = low_product // scale
        upper = -((-high_product) // scale)
        return DyadicInterval(self.bits, lower, upper)

    def multiply_integer(self, value: int) -> "DyadicInterval":
        if value >= 0:
            return DyadicInterval(self.bits, self.lower * value, self.upper * value)
        return DyadicInterval(self.bits, self.upper * value, self.lower * value)

    def divide_positive_integer(self, value: int) -> "DyadicInterval":
        if value <= 0:
            raise ValueError("positive divisor required")
        lower = self.lower // value
        upper = -((-self.upper) // value)
        return DyadicInterval(self.bits, lower, upper)

    def divide_positive(self, other: "DyadicInterval") -> "DyadicInterval":
        """Enclose self/other when both intervals are nonnegative and other>0."""
        self._require_same_bits(other)
        if self.lower < 0 or other.lower <= 0:
            raise ValueError("nonnegative numerator and positive denominator required")
        scale = self.scale
        lower = (self.lower * scale) // other.upper
        upper = -((-(self.upper * scale)) // other.lower)
        return DyadicInterval(self.bits, lower, upper)

    def intersect(self, other: "DyadicInterval") -> "DyadicInterval":
        self._require_same_bits(other)
        lower = max(self.lower, other.lower)
        upper = min(self.upper, other.upper)
        if lower > upper:
            raise ValueError("intervals are disjoint")
        return DyadicInterval(self.bits, lower, upper)

    def contains_fraction(self, value: Fraction) -> bool:
        scale = self.scale
        p, q = value.numerator, value.denominator
        return self.lower * q <= p * scale <= self.upper * q

    def is_strictly_positive(self) -> bool:
        return self.lower > 0

    def is_strictly_negative(self) -> bool:
        return self.upper < 0

    def width_numerator(self) -> int:
        return self.upper - self.lower

    def as_fraction_bounds(self) -> tuple[Fraction, Fraction]:
        scale = self.scale
        return Fraction(self.lower, scale), Fraction(self.upper, scale)

    def to_json(self, decimal_digits: int = 50) -> dict[str, object]:
        return {
            "bits": self.bits,
            "denominator_power_of_two": self.bits,
            "lower_numerator": str(self.lower),
            "upper_numerator": str(self.upper),
            "width_numerator": str(self.upper - self.lower),
            "lower_decimal_outward": format_dyadic_decimal(
                self.lower, self.bits, decimal_digits, upper=False
            ),
            "upper_decimal_outward": format_dyadic_decimal(
                self.upper, self.bits, decimal_digits, upper=True
            ),
        }

    def _require_same_bits(self, other: "DyadicInterval") -> None:
        if self.bits != other.bits:
            raise ValueError("dyadic precisions differ")


def _format_scaled_integer(value: int, digits: int) -> str:
    sign = "-" if value < 0 else ""
    magnitude = abs(value)
    if digits == 0:
        return sign + str(magnitude)
    text = str(magnitude).rjust(digits + 1, "0")
    return f"{sign}{text[:-digits]}.{text[-digits:]}"


def format_dyadic_decimal(
    numerator: int, bits: int, digits: int, *, upper: bool
) -> str:
    """Return an outward rounded fixed-point decimal for numerator/2**bits."""
    if digits < 0:
        raise ValueError("digits must be nonnegative")
    scale10 = 10**digits
    denominator = 1 << bits
    scaled_num = numerator * scale10
    if upper:
        rounded = -((-scaled_num) // denominator)
    else:
        rounded = scaled_num // denominator
    return _format_scaled_integer(rounded, digits)


def parse_decimal_fraction(text: str) -> Fraction:
    """Parse a finite decimal/scientific literal exactly as a Fraction."""
    text = text.strip()
    if not text:
        raise ValueError("empty decimal")
    sign = -1 if text.startswith("-") else 1
    if text[0] in "+-":
        text = text[1:]
    if "e" in text.lower():
        mantissa, exponent_text = text.lower().split("e", 1)
        exponent = int(exponent_text)
    else:
        mantissa, exponent = text, 0
    if "." in mantissa:
        whole, frac = mantissa.split(".", 1)
    else:
        whole, frac = mantissa, ""
    digits = (whole or "0") + frac
    numerator = sign * int(digits or "0")
    denominator = 10 ** len(frac)
    if exponent >= 0:
        numerator *= 10**exponent
    else:
        denominator *= 10 ** (-exponent)
    return Fraction(numerator, denominator)


def _range_reduce_fraction_to_one_two(value: Fraction) -> tuple[int, Fraction]:
    """Return k,y with value=2**k*y and 1<=y<2."""
    if value <= 0:
        raise ValueError("positive value required")
    p, q = value.numerator, value.denominator
    k = p.bit_length() - q.bit_length()
    if k >= 0:
        y = Fraction(p, q << k)
    else:
        y = Fraction(p << (-k), q)
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1
    return k, y


def atanh_log_reduced_interval(
    y: Fraction, *, bits: int, terms: int
) -> DyadicInterval:
    """Enclose log(y) for 1<=y<2 by the positive atanh series."""
    if not (1 <= y <= 2):
        raise ValueError("y must lie in [1,2]")
    if terms < 1:
        raise ValueError("terms must be positive")
    if y == 1:
        return DyadicInterval.exact_integer(0, bits)
    z = (y - 1) / (y + 1)
    z_interval = DyadicInterval.from_fraction(z, bits)
    z2 = z_interval.multiply(z_interval)
    power = z_interval
    total = DyadicInterval.exact_integer(0, bits)
    for j in range(terms):
        total = total.add(power.divide_positive_integer(2 * j + 1))
        power = power.multiply(z2)
    one = DyadicInterval.exact_integer(1, bits)
    denominator = one.subtract(z2)
    tail = power.divide_positive_integer(2 * terms + 1).divide_positive(denominator)
    doubled_partial = total.multiply_integer(2)
    return DyadicInterval(
        bits, doubled_partial.lower, doubled_partial.upper + 2 * tail.upper
    )


def log_fraction_interval(
    value: Fraction, *, bits: int = 320, terms: int = 96
) -> DyadicInterval:
    """Rigorous interval for the natural logarithm of a positive rational."""
    if value <= 0:
        raise ValueError("positive value required")
    if value == 1:
        return DyadicInterval.exact_integer(0, bits)
    k, y = _range_reduce_fraction_to_one_two(value)
    log_y = atanh_log_reduced_interval(y, bits=bits, terms=terms)
    log_two = atanh_log_reduced_interval(Fraction(2), bits=bits, terms=terms)
    return log_y.add(log_two.multiply_integer(k))


def log_interval(
    value: DyadicInterval, *, terms: int = 96
) -> DyadicInterval:
    """Monotone enclosure of log on a positive dyadic interval."""
    if value.lower <= 0:
        raise ValueError("positive interval required")
    scale = 1 << value.bits
    lower_eval = log_fraction_interval(
        Fraction(value.lower, scale), bits=value.bits, terms=terms
    )
    upper_eval = log_fraction_interval(
        Fraction(value.upper, scale), bits=value.bits, terms=terms
    )
    return DyadicInterval(value.bits, lower_eval.lower, upper_eval.upper)


def harmonic_dyadic_interval(n: int, *, bits: int = 320) -> DyadicInterval:
    """Enclose H_n using termwise directed dyadic rounding."""
    if n < 1:
        raise ValueError("n must be positive")
    scale = 1 << bits
    lower = 0
    upper = 0
    for k in range(1, n + 1):
        lower += scale // k
        upper += (scale + k - 1) // k
    return DyadicInterval(bits, lower, upper)


def euler_gamma_interval(
    *, harmonic_cutoff: int = 1_000_000, bits: int = 320, log_terms: int = 96
) -> DyadicInterval:
    """Enclose Euler's constant without a stored numerical constant.

    Uses the elementary two-sided bound

        1/(2(n+1)) < H_n-log(n)-gamma < 1/(2n).
    """
    harmonic = harmonic_dyadic_interval(harmonic_cutoff, bits=bits)
    log_n = log_fraction_interval(
        Fraction(harmonic_cutoff), bits=bits, terms=log_terms
    )
    correction_lower = DyadicInterval.from_ratio(
        1, 2 * (harmonic_cutoff + 1), bits
    )
    correction_upper = DyadicInterval.from_ratio(1, 2 * harmonic_cutoff, bits)
    correction = DyadicInterval(
        bits, correction_lower.lower, correction_upper.upper
    )
    return harmonic.subtract(log_n).subtract(correction)


def exp_point_interval(
    point_numerator: int, *, bits: int = 320, terms: int = 96
) -> DyadicInterval:
    """Enclose exp(x) at the dyadic point x=point_numerator/2**bits."""
    if point_numerator < 0:
        raise ValueError("this implementation requires x>=0")
    x = DyadicInterval(bits, point_numerator, point_numerator)
    one = DyadicInterval.exact_integer(1, bits)
    term = one
    total = one
    for j in range(1, terms + 1):
        term = term.multiply(x).divide_positive_integer(j)
        total = total.add(term)
    next_term = term.multiply(x).divide_positive_integer(terms + 1)
    ratio = x.divide_positive_integer(terms + 2)
    denominator = one.subtract(ratio)
    if denominator.lower <= 0:
        raise ValueError("too few terms for geometric tail bound")
    tail = next_term.divide_positive(denominator)
    return DyadicInterval(bits, total.lower, total.upper + tail.upper)


def exp_interval(value: DyadicInterval, *, terms: int = 96) -> DyadicInterval:
    """Monotone enclosure of exp on a nonnegative dyadic interval."""
    if value.lower < 0:
        raise ValueError("nonnegative interval required")
    lower = exp_point_interval(value.lower, bits=value.bits, terms=terms)
    upper = exp_point_interval(value.upper, bits=value.bits, terms=terms)
    return DyadicInterval(value.bits, lower.lower, upper.upper)
