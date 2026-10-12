#!/usr/bin/env python3
"""Exact rational enclosure of the SHARP labelled-prime pairing threshold.

No floating-point values enter acceptance. See POWER_THRESHOLD.md for the
Euler--Maclaurin remainder and prime-zeta tail contracts. This finite checker
does not establish the critical power-one estimate or RH.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path

BITS = 180
DEN = 1 << BITS
LOG_TERMS = 64
EXP_TERMS = 64
ZETA_N = 64
ZETA_K = 14
PRIME_K = 80


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def lower_round(x: Q) -> Q:
    return Q(x.numerator * DEN // x.denominator, DEN)


def upper_round(x: Q) -> Q:
    return Q(-((-x.numerator * DEN) // x.denominator), DEN)


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __post_init__(self):
        require(self.lo <= self.hi, 'reversed enclosure')

    @staticmethod
    def point(x) -> 'Interval':
        return Interval(Q(x), Q(x))

    def round(self) -> 'Interval':
        return Interval(lower_round(self.lo), upper_round(self.hi))

    def __add__(self, other) -> 'Interval':
        b = other if isinstance(other, Interval) else Interval.point(other)
        return Interval(self.lo + b.lo, self.hi + b.hi).round()

    __radd__ = __add__

    def __neg__(self) -> 'Interval':
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other) -> 'Interval':
        return self + (-other if isinstance(other, Interval) else -Q(other))

    def __rsub__(self, other) -> 'Interval':
        return -self + other

    def __mul__(self, other) -> 'Interval':
        b = other if isinstance(other, Interval) else Interval.point(other)
        products = (self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi)
        return Interval(min(products), max(products)).round()

    __rmul__ = __mul__

    def __truediv__(self, other) -> 'Interval':
        b = other if isinstance(other, Interval) else Interval.point(other)
        require(b.lo > 0 or b.hi < 0, 'division through zero')
        return self * Interval(1/b.hi, 1/b.lo)

    def record(self) -> dict:
        return {'lower': str(self.lo), 'upper': str(self.hi)}


@lru_cache(None)
def log_point(x: Q) -> Interval:
    """Bound log(x) using its positive atanh series after binary reduction."""
    x = Q(x)
    require(x > 0, 'log domain')
    if x < 1:
        return -log_point(1/x)
    k = 0
    v = x
    while v >= 2:
        v /= 2
        k += 1

    def reduced(y: Q) -> Interval:
        z = (y-1)/(y+1)
        require(0 <= z <= Q(1, 3), 'log range reduction')
        term = z
        partial = Q(0)
        for j in range(LOG_TERMS):
            partial += term / (2*j+1)
            term *= z*z
        remainder = 2*term / ((2*LOG_TERMS+1)*(1-z*z))
        return Interval(2*partial, 2*partial+remainder).round()

    return reduced(v) + k*reduced(Q(2))


def log_interval(x: Interval) -> Interval:
    require(x.lo > 0, 'log interval domain')
    return Interval(log_point(x.lo).lo, log_point(x.hi).hi).round()


@lru_cache(None)
def exp_negative_point(x: Q) -> Interval:
    """Bound exp(-x), x>=0, by an alternating series and squaring."""
    x = Q(x)
    require(x >= 0, 'negative exponential domain')
    reductions = 0
    v = x
    while v > Q(1, 4):
        v /= 2
        reductions += 1
    term = Q(1)
    partial = Q(1)
    for j in range(1, EXP_TERMS+1):
        term *= -v/j
        partial += term
    # EXP_TERMS is even; the next, negative term gives a lower enclosure.
    require(EXP_TERMS % 2 == 0, 'exponential parity')
    next_term = term * (-v)/(EXP_TERMS+1)
    out = Interval(partial+next_term, partial).round()
    require(out.lo > 0, 'exponential lower bound')
    for _ in range(reductions):
        out = out*out
    return out


def negative_power(n: int, s: Q) -> Interval:
    require(type(n) is int and n >= 1 and s >= 0, 'negative-power domain')
    exponent = log_point(Q(n))*s
    return Interval(exp_negative_point(exponent.hi).lo,
                    exp_negative_point(exponent.lo).hi).round()


@lru_cache(None)
def bernoulli(n: int) -> Q:
    # B_1=+1/2 in this recurrence; only even indices are used.
    row = [Q(0)]*(n+1)
    for m in range(n+1):
        row[m] = Q(1, m+1)
        for j in range(m, 0, -1):
            row[j-1] = j*(row[j-1]-row[j])
    return row[0]


def rising(s: Q, count: int) -> Q:
    out = Q(1)
    for j in range(count):
        out *= s+j
    return out


def zeta_interval(s: Q) -> Interval:
    """Euler--Maclaurin with a proved periodic-Bernoulli remainder bound."""
    require(s > 1, 'zeta real domain')
    n = ZETA_N
    base_power = negative_power(n, s)
    total = sum((negative_power(j, s) for j in range(1, n)), Interval.point(0))
    total += base_power * (Q(n)/(s-1)+Q(1, 2))
    for k in range(1, ZETA_K+1):
        coefficient = bernoulli(2*k)/factorial(2*k)*rising(s, 2*k-1)
        total += base_power * (coefficient/Q(n**(2*k-1)))
    remainder_coefficient = abs(bernoulli(2*ZETA_K))/factorial(2*ZETA_K)
    remainder_coefficient *= rising(s, 2*ZETA_K-1)/n**(2*ZETA_K-1)
    error = (base_power*remainder_coefficient).hi
    out = Interval(total.lo-error, total.hi+error).round()
    require(out.lo > 1, 'zeta enclosure must be above one')
    return out


def mobius(n: int) -> int:
    sign = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def prime_zeta_interval(s: Q) -> Interval:
    require(s > 1, 'prime-zeta domain')
    out = Interval.point(0)
    for k in range(1, PRIME_K+1):
        mu = mobius(k)
        if mu:
            out += log_interval(zeta_interval(k*s)) * Q(mu, k)
    # log(zeta(t)) <= zeta(t)-1 <= 2^-t [1+2/(t-1)].
    # Bound 1/k and the bracket by their values at k=PRIME_K+1,
    # then sum the remaining powers of 2^-s geometrically.
    first = PRIME_K+1
    ratio = negative_power(2, s)
    tail = negative_power(2, first*s) * Q(1, first)
    tail *= 1+Q(2)/(first*s-1)
    tail /= 1-ratio
    return Interval(out.lo-tail.hi, out.hi+tail.hi).round()


def labelled_prime_mass(s: Q) -> Interval:
    return prime_zeta_interval(s)+negative_power(67, s)


def run() -> dict:
    lower = Q('1.40103426886')
    upper = Q('1.40103426887')
    lower_mass = labelled_prime_mass(lower)
    upper_mass = labelled_prime_mass(upper)
    require(lower_mass.lo > 1, 'lower threshold endpoint not proved above one')
    require(upper_mass.hi < 1, 'upper threshold endpoint not proved below one')
    require(bernoulli(2) == Q(1, 6), 'Bernoulli normalization')
    require(bernoulli(4) == -Q(1, 30), 'Bernoulli sign')
    require(mobius(1) == 1 and mobius(4) == 0 and mobius(6) == 1, 'Mobius controls')
    require(log_point(Q(1)) == Interval.point(0), 'log unit control')
    require(exp_negative_point(Q(0)) == Interval.point(1), 'exp unit control')
    # test_threshold.py checks this implementation independently using
    # Machin's pi identity, even-zeta formulas, and a direct prime-square sum.
    return {
        'status': 'PASS_EXACT_LABELLED_PRIME_THRESHOLD_BRACKET',
        'arithmetic': 'EXACT_RATIONAL_DIRECTED_DYADIC_ENCLOSURES',
        'alpha_bracket': [str(lower), str(upper)],
        'power_bracket': [str(2*lower-1), str(2*upper-1)],
        'lower_endpoint_mass': lower_mass.record(),
        'upper_endpoint_mass': upper_mass.record(),
        'valid_global_power_threshold': str(2*upper-1),
        'parameters': {'bits': BITS, 'log_terms': LOG_TERMS,
                       'exp_terms': EXP_TERMS, 'zeta_n': ZETA_N,
                       'zeta_remainder_order': ZETA_K, 'prime_series_cutoff': PRIME_K},
        'critical_power_one_proved': False,
        'rh_proved': False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    result['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    content = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding='utf-8')
    print(content, end='')


if __name__ == '__main__':
    main()
