#!/usr/bin/env python3
"""Exact rational enclosure of the calibrated block bound; no zeta oracle.

This checks finite constants and combinatorics, not BGST, the paper proof,
or the seven-point continuum inequality. Run the separate pressure verifier
for that last inequality. No assert is used for mathematical acceptance.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import argparse
import json
import sys


def need(ok: bool, text: str) -> None:
    if not ok:
        raise ValueError(text)


@dataclass(frozen=True)
class IV:
    lo: F
    hi: F

    def __post_init__(self):
        need(self.lo <= self.hi, 'reversed interval')

    @staticmethod
    def of(x):
        return x if isinstance(x, IV) else IV(F(x), F(x))

    def __add__(self, other):
        other = IV.of(other)
        return IV(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return IV(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -IV.of(other)

    def __rsub__(self, other):
        return IV.of(other) + -self

    def __mul__(self, other):
        other = IV.of(other)
        vals = [a*b for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return IV(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = IV.of(other)
        need(not other.lo <= 0 <= other.hi, 'zero-containing denominator')
        vals = [F(1)/other.lo, F(1)/other.hi]
        return self * IV(min(vals), max(vals))


def sqrt_q(x: F, bits: int = 192) -> IV:
    need(x >= 0, 'negative radical')
    scale = 1 << bits
    k = isqrt((x.numerator * scale * scale) // x.denominator)
    lo, hi = F(k, scale), F(k + 1, scale)
    need(lo * lo <= x <= hi * hi, 'sqrt enclosure')
    return IV(lo, hi)


def cosine_sinc(terms: int = 48):
    # At u^2=1/2, both alternating series have decreasing positive terms.
    c = sum((F((-1)**k, 2**k * factorial(2*k)) for k in range(terms)), F())
    s = sum((F((-1)**k, 2**k * factorial(2*k+1)) for k in range(terms)), F())
    dc = F((-1)**terms, 2**terms * factorial(2*terms))
    ds = F((-1)**terms, 2**terms * factorial(2*terms+1))
    return IV(min(c, c+dc), max(c, c+dc)), IV(min(s, s+ds), max(s, s+ds))


def decimal_endpoint(x: F, digits: int, up: bool) -> str:
    scale = 10**digits
    k = x.numerator * scale // x.denominator
    if up and F(k, scale) < x:
        k += 1
    sign = '-' if k < 0 else ''
    k = abs(k)
    return sign + str(k // scale) + '.' + str(k % scale).zfill(digits)


def encoded(iv: IV):
    return {'lo': str(iv.lo), 'hi': str(iv.hi),
            'decimal_lo': decimal_endpoint(iv.lo, 24, False),
            'decimal_hi': decimal_endpoint(iv.hi, 24, True)}


def reconstruct():
    C, S = cosine_sinc()
    need(S.lo > 0, 'sinc positive')
    H = F(3, 2) - C/S
    m = 322
    q = F(19*(m-6), 5000)
    need(F(m, m-1) < q < 2, 'fixed block range')
    rad = F(m-1, m)*q
    need(rad == F(481821, 402500), 'radical rational normalization')
    c = 2*sqrt_q(rad)-1+q/m
    slope = c/q
    alpha = c/m
    beta = c*F(m-1, 500*m)/q
    value = (H-beta)/(1-alpha)
    need(0 < c.lo and c.hi < q, 'strict calibrated span saving')
    need(value.lo > F(6730129, 10**7), 'advertised strict bound')
    need(beta.lo > 0 and alpha.hi < 1, 'count rearrangement')
    need(beta.lo == (c*F(1605,966644)).lo, 'beta identity')
    old_c = 2*sqrt_q(F(726237,700000))-1+F(2603,700000)
    old = (H-F(279,140000))/(1-old_c/280)
    gain = value-old
    need(gain.lo > 0, 'strict improvement over old 280 extraction')
    distinct = (1+value)/2
    # Source-independent bounded tests of the exact block counting.
    examples = 0
    for block in range(2,15):
        for count in range(0,3*block+2):
            starts = []
            loads = [0]*max(0,count-1)
            for offset in range(block):
                for first in range(offset, count-block+1, block):
                    starts.append(first)
                    for j in range(first, first+block-1):
                        loads[j] += 1
            need(sorted(starts) == list(range(max(0,count-block+1))), 'offset coverage')
            need(not loads or max(loads) <= block-1, 'gap multiplicity')
            examples += 1
    # Algebraic endpoint sharpness: trace/energy of equal-correlation spectrum.
    # a^2=(m-1)q/m; negative deviations are -a/(m-1).
    need(rad*(1+F(1,m-1)) == q, 'spectral energy identity')
    need(2*rad/(m-1) == 2*q/m, 'coefficient algebra control')
    return {
        'schema': 1,
        'status': 'PROPOSED_GLOBAL_SIMPLE_ZERO_BOUND_NOT_RH',
        'block_size': m,
        'q': str(q), 'radicand': str(rad),
        'H_MT': encoded(H), 'c': encoded(c), 'span_slope': encoded(slope),
        'alpha': encoded(alpha), 'beta': encoded(beta),
        'new_simple_global_bound': encoded(value),
        'old_280_bound': encoded(old), 'improvement_in_fraction': encoded(gain),
        'new_distinct_global_bound': encoded(distinct),
        'strict_rational_simple_bound': '6730129/10000000',
        'offset_cases_checked': examples,
        'all_spectral_or_analytic_theorems_machine_proved': False,
        'seven_point_pressure_replayed_by_this_program': False,
        'world_record_claim': False,
        'rh_proved': False,
    }


def strict_read(path):
    def pairs(items):
        result = {}
        for k,v in items:
            need(k not in result, 'duplicate JSON key')
            result[k]=v
        return result
    def no_float(x):
        raise ValueError('noninteger numeric literal')
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs,
                      parse_float=no_float, parse_constant=no_float)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit', action='store_true')
    group.add_argument('--check', type=Path)
    args=parser.parse_args()
    expected=reconstruct()
    if args.check:
        got = strict_read(args.check)
        # Serialized comparison deliberately distinguishes bool from integer.
        need(json.dumps(expected,sort_keys=True) == json.dumps(got,sort_keys=True),
             'receipt differs from exact reconstruction')
    print(json.dumps(expected, indent=2, sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError, ZeroDivisionError) as exc:
        print('REJECT: '+str(exc), file=sys.stderr)
        sys.exit(1)
