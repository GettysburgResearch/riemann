#!/usr/bin/env python3
"""Exact definitions and small proof-oriented evaluators for X-17201.

The discovery scan uses FFT samples (see ``search.py``).  This module is the
independent, deliberately slow checker for a frozen rational support.  It uses
only Python integers and ``fractions.Fraction`` for:

* the finite box-convolution spline;
* logarithm and reciprocal-square-root enclosures;
* the von Mangoldt prime-power manifest; and
* outward interval accumulation.

The interval spline evaluator is practical only for small ledgers.  A profile
with ``d`` distinct boxes has ``3**d`` aggregated truncated-power terms after
the convolution square (each box occurs twice).
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, factorial, isqrt
from typing import Iterable, Iterator, Sequence


Q = Fraction
Interval = tuple[Q, Q]


def qtext(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def qparse(text: str) -> Q:
    a, b = text.split("/", 1)
    return Q(int(a), int(b))


def iadd(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def isub(a: Interval, b: Interval) -> Interval:
    return a[0] - b[1], a[1] - b[0]


def iscale(c: Q, a: Interval) -> Interval:
    if c >= 0:
        return c * a[0], c * a[1]
    return c * a[1], c * a[0]


def imul(a: Interval, b: Interval) -> Interval:
    values = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(values), max(values)


def log_rational_interval(x: Q, terms: int = 80) -> Interval:
    """Enclose log(x) for positive rational x by an exact atanh series.

    We first scale x into [1, 2), then use

        log(y) = 2 sum_{j>=0} q^(2j+1)/(2j+1), q=(y-1)/(y+1).

    The omitted positive tail is bounded geometrically.  ``log(2)`` is
    evaluated by the same series with q=1/3.  No floating operation enters the
    enclosure.
    """
    if x <= 0:
        raise ValueError("log argument must be positive")
    if terms < 1:
        raise ValueError("terms must be positive")

    # Exact binary scaling x = 2**k * y with 1 <= y < 2.
    k = x.numerator.bit_length() - x.denominator.bit_length()
    if k >= 0:
        y = x / (1 << k)
    else:
        y = x * (1 << (-k))
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1

    def log_unit_interval(y0: Q) -> Interval:
        q = (y0 - 1) / (y0 + 1)
        if q < 0 or q > Q(1, 3):
            raise AssertionError("binary reduction failed")
        total = Q(0)
        q2 = q * q
        power = q
        for j in range(terms):
            total += 2 * power / (2 * j + 1)
            power *= q2
        first_degree = 2 * terms + 1
        remainder = 2 * power / (first_degree * (1 - q2))
        return total, total + remainder

    log2 = log_unit_interval(Q(2))
    logy = log_unit_interval(y)
    return iadd(iscale(Q(k), log2), logy)


@lru_cache(maxsize=None)
def log_integer_interval(n: int, terms: int = 80) -> Interval:
    if n < 1:
        raise ValueError("integer log argument must be positive")
    return log_rational_interval(Q(n), terms)


@lru_cache(maxsize=None)
def reciprocal_sqrt_integer_interval(n: int, bits: int = 160) -> Interval:
    """Exact rational enclosure of 1/sqrt(n)."""
    if n < 1:
        raise ValueError("sqrt argument must be positive")
    scale = 1 << bits
    lo_scaled = isqrt(n * scale * scale)
    if lo_scaled == 0:
        raise AssertionError("unexpected zero square-root lower bound")
    if lo_scaled * lo_scaled == n * scale * scale:
        value = Q(scale, lo_scaled)
        return value, value
    # lo_scaled/scale < sqrt(n) < (lo_scaled+1)/scale.
    return Q(scale, lo_scaled + 1), Q(scale, lo_scaled)


def primes_through(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_power_events(limit: int) -> list[tuple[int, int, int]]:
    """Return sorted duplicate-free triples (p**k, p, k)."""
    events: list[tuple[int, int, int]] = []
    for p in primes_through(limit):
        value = p
        exponent = 1
        while value <= limit:
            events.append((value, p, exponent))
            if value > limit // p:
                break
            value *= p
            exponent += 1
    events.sort()
    return events


def manifest_digest(events: Iterable[tuple[int, int, int]]) -> str:
    h = sha256()
    for n, p, k in events:
        h.update(f"{n},{p},{k}\n".encode("ascii"))
    return h.hexdigest()


@dataclass(frozen=True)
class FilterSpec:
    """Finite exact directed filter.

    If ``mu`` is the convolution of normalized boxes of widths ``widths``,
    ``F(u)`` is the density of ``mu*mu`` shifted right by ``base_shift``.
    The final window is

        G = 2^-m (I-T_delta)^m (I-2 T_h) F,

    where h=log(4) is stored symbolically and ``m=highpass_order``.
    """

    widths: tuple[Q, ...]
    base_shift: Q = Q(2)
    highpass_delta: Q = Q(1, 64)
    highpass_order: int = 0

    def __post_init__(self) -> None:
        if not self.widths or any(w <= 0 for w in self.widths):
            raise ValueError("all box widths must be positive")
        if self.base_shift <= 0:
            raise ValueError("base shift must be positive")
        if self.highpass_delta <= 0 or self.highpass_order < 0:
            raise ValueError("invalid high-pass parameters")

    @property
    def profile_length(self) -> Q:
        return sum(self.widths, Q(0))

    def support_max_interval(self, log_terms: int = 80) -> Interval:
        log2 = log_rational_interval(Q(2), log_terms)
        h = iscale(Q(2), log2)
        rational = (
            self.base_shift
            + 2 * self.profile_length
            + self.highpass_order * self.highpass_delta
        )
        return rational + h[0], rational + h[1]

    @property
    def support_min(self) -> Q:
        return self.base_shift

    def physical_shift_ledger(self) -> list[tuple[int, Q, int]]:
        """Return (binomial coefficient, rational shift, pole branch).

        ``pole branch`` 0 means no h shift and 1 means one h shift with the
        additional coefficient -2.  The common 2^-m denominator is omitted
        from the integer coefficient and is applied by the evaluator.
        """
        out: list[tuple[int, Q, int]] = []
        m = self.highpass_order
        for j in range(m + 1):
            c = (-1 if j & 1 else 1) * comb(m, j)
            out.append((c, j * self.highpass_delta, 0))
            out.append((-2 * c, j * self.highpass_delta, 1))
        return out


@lru_cache(maxsize=None)
def _truncated_power_terms(widths: tuple[Q, ...]) -> tuple[int, Q, tuple[tuple[Q, int], ...]]:
    """Aggregate the exact generalized Irwin-Hall terms for mu*mu."""
    d = len(widths)
    degree = 2 * d - 1
    normalization = Q(1, factorial(degree))
    for w in widths:
        normalization /= w * w
    aggregate: dict[Q, int] = {}
    for choices in product((0, 1, 2), repeat=d):
        knot = sum((c * w for c, w in zip(choices, widths)), Q(0))
        coefficient = 1
        parity = 0
        for c in choices:
            coefficient *= comb(2, c)
            parity += c
        if parity & 1:
            coefficient = -coefficient
        aggregate[knot] = aggregate.get(knot, 0) + coefficient
    terms = tuple(sorted((k, c) for k, c in aggregate.items() if c))
    return degree, normalization, terms


def convolution_square_density_interval(y: Interval, widths: Sequence[Q]) -> Interval:
    """Exact outward range enclosure for the finite convolution square.

    The direct interval sum can overestimate badly across many knots.  We
    intersect it with positivity and the elementary L-infinity contraction
    ``density <= 1/max(widths)``.
    """
    widths_tuple = tuple(widths)
    total_support = 2 * sum(widths_tuple, Q(0))
    if y[1] <= 0 or y[0] >= total_support:
        # Endpoints have zero density for degree >= 1; all production ledgers
        # use at least two boxes.
        return Q(0), Q(0)
    lo = max(Q(0), y[0])
    hi = min(total_support, y[1])
    if lo > hi:
        return Q(0), Q(0)

    # Symmetry about total_support/2 can reduce large shifted powers.
    midpoint = total_support / 2
    if lo >= midpoint:
        lo, hi = total_support - hi, total_support - lo

    degree, normalization, terms = _truncated_power_terms(widths_tuple)
    lower = Q(0)
    upper = Q(0)
    for knot, coefficient in terms:
        a = max(Q(0), lo - knot) ** degree
        b = max(Q(0), hi - knot) ** degree
        if coefficient >= 0:
            lower += coefficient * a
            upper += coefficient * b
        else:
            lower += coefficient * b
            upper += coefficient * a
    lower *= normalization
    upper *= normalization
    density_cap = Q(1, max(widths_tuple))
    return max(Q(0), lower), min(density_cap, upper)


def fstar_interval(u: Interval, spec: FilterSpec) -> Interval:
    return convolution_square_density_interval(
        (u[0] - spec.base_shift, u[1] - spec.base_shift), spec.widths
    )


def g_interval(u: Interval, spec: FilterSpec, log_terms: int = 80) -> Interval:
    h = iscale(Q(2), log_rational_interval(Q(2), log_terms))
    total = (Q(0), Q(0))
    scale = Q(1, 1 << spec.highpass_order)
    for coefficient, rational_shift, pole_branch in spec.physical_shift_ledger():
        shifted = (u[0] - rational_shift, u[1] - rational_shift)
        if pole_branch:
            shifted = (shifted[0] - h[1], shifted[1] - h[0])
        value = fstar_interval(shifted, spec)
        total = iadd(total, iscale(scale * coefficient, value))
    return total


def von_mangoldt_weight_interval(
    n: int, p: int, *, log_terms: int = 80, sqrt_bits: int = 160
) -> Interval:
    logp = log_integer_interval(p, log_terms)
    invsqrt = reciprocal_sqrt_integer_interval(n, sqrt_bits)
    return imul(logp, invsqrt)


def directed_q_interval(
    x: Interval,
    spec: FilterSpec,
    events: Sequence[tuple[int, int, int]],
    *,
    log_terms: int = 80,
    sqrt_bits: int = 160,
) -> tuple[Interval, int]:
    """Outward-enclose Q_G throughout a rational x interval.

    ``events`` must be a complete manifest through a cutoff exceeding every
    possibly contributing n.  The function returns the Q interval and the
    number of manifest entries whose argument was not rejected by support.
    """
    total = (Q(0), Q(0))
    used = 0
    support_hi = spec.support_max_interval(log_terms)[1]
    for n, p, _k in events:
        logn = log_integer_interval(n, log_terms)
        u = (x[0] - logn[1], x[1] - logn[0])
        if u[1] < spec.support_min or u[0] > support_hi:
            continue
        window = g_interval(u, spec, log_terms)
        if window == (0, 0):
            continue
        weight = von_mangoldt_weight_interval(
            n, p, log_terms=log_terms, sqrt_bits=sqrt_bits
        )
        total = iadd(total, imul(weight, window))
        used += 1
    return total, used


def dyadic_widths(level: int) -> tuple[Q, ...]:
    if level < 1:
        raise ValueError("dyadic level must be positive")
    return tuple(Q(1, 1 << j) for j in range(1, level + 1))


# Rational nearest-10^-12 designs based on the mpmath midpoints used by X-15404.
# They define exact filters.  Their relation to actual zeros is EMPIRICAL until
# an independent certified zero backend encloses the ordinates.
NOTCH_WIDTHS_1E12: tuple[Q, ...] = (
    Q(444_521_223_029, 10**12),
    Q(298_885_617_911, 10**12),
    Q(251_218_307_371, 10**12),
    Q(206_514_737_519, 10**12),
    Q(190_774_967_596, 10**12),
)


def standard_spec(
    *, dyadic_level: int = 8, notch_count: int = 2, highpass_order: int = 0,
    highpass_delta: Q = Q(1, 64)
) -> FilterSpec:
    if notch_count < 0 or notch_count > len(NOTCH_WIDTHS_1E12):
        raise ValueError("unsupported notch count")
    widths = dyadic_widths(dyadic_level) + NOTCH_WIDTHS_1E12[:notch_count]
    return FilterSpec(widths, Q(2), highpass_delta, highpass_order)
