#!/usr/bin/env python3
"""Exact arithmetic for the NEW lossless-pressure lemmas, not the imported 6-D proof.

Python standard library only. This checks a polynomial majorant, Fourier-frame
and close-pair budgets, input capacities, and scalar constants. It does NOT check
RH, the analytic number-theory theorem, or the imported universal pressure search.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from fractions import Fraction as F
from dataclasses import dataclass
from typing import Any

ROOT = Path(__file__).resolve().parent
INPUT_SHA = "dcc31d50fa7cf116b1b58aa1b39bc8c734cdf6d3aeb8e35c282acca9206189d2"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self) -> None:
        require(self.lo <= self.hi, "Reversed interval")

    @staticmethod
    def point(x: Any) -> 'Interval':
        return x if isinstance(x, Interval) else Interval(F(x), F(x))

    def __add__(self, other: Any) -> 'Interval':
        o = self.point(other)
        return Interval(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self) -> 'Interval':
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: Any) -> 'Interval':
        return self + -self.point(other)

    def __rsub__(self, other: Any) -> 'Interval':
        return self.point(other) + -self

    def __mul__(self, other: Any) -> 'Interval':
        o = self.point(other)
        p = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return Interval(min(p), max(p))
    __rmul__ = __mul__

    def __truediv__(self, other: Any) -> 'Interval':
        o = self.point(other)
        require(o.lo > 0 or o.hi < 0, "Division interval contains zero")
        return self * Interval(1/o.hi, 1/o.lo)

    def __rtruediv__(self, other: Any) -> 'Interval':
        return self.point(other) / self


def alternating(terms: list[F]) -> Interval:
    """Adjacent truncations bracket the sum when the alternating tail decreases."""
    require(len(terms) >= 2, "Need adjacent truncations")
    partial = sum(terms[:-1], F(0))
    return Interval(min(partial, partial + terms[-1]),
                    max(partial, partial + terms[-1]))


def constants(n: int = 26) -> tuple[Interval, Interval, Interval]:
    require(n >= 4, "Insufficient series length")
    def atan_inv(k: int) -> Interval:
        return alternating([F((-1)**j, (2*j+1)*k**(2*j+1))
                            for j in range(3*n+1)])
    pi = 16*atan_inv(5) - 4*atan_inv(239)
    cosine = alternating([F((-1)**j, 2**j*math.factorial(2*j))
                          for j in range(n+1)])
    sinc = alternating([F((-1)**j, 2**j*math.factorial(2*j+1))
                        for j in range(n+1)])
    return pi, cosine, sinc


def poly_mul(a: list[F], b: list[F]) -> list[F]:
    p = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i+j] += x*y
    return p


def majorant(sum_abs: F, C: F = F(29,20)) -> list[F]:
    """Bernstein coefficients of C R(v)^2 - (1-v+v^2/6) - S on [0,1/4]."""
    b = F(88,35)**2  # pi < 22/7 and delta=4/5
    R = [F(1), -b/6, b*b/120, -b**3/5040]
    p = [C*x for x in poly_mul(R, R)]
    p[0] -= 1 + sum_abs
    p[1] += 1
    p[2] -= F(1,6)
    bern = [sum((p[j] * F(1,4)**j * F(math.comb(i,j),math.comb(6,j))
                 for j in range(i+1)), F(0)) for i in range(7)]
    require(min(bern) > F(1,1000), "Positive polynomial majorant failed")
    require(C/(F(4,5)*F(11,12)) < 2, "Separated Gram may reach clipping")
    return bern


def read_inputs() -> dict[str, Any]:
    raw = (ROOT/'inputs.json').read_bytes()
    require(hashlib.sha256(raw).hexdigest() == INPUT_SHA, "Input snapshot changed")
    return json.loads(raw)


def capacities(d: dict[str, Any]) -> tuple[F, F, list[F]]:
    require(len(d['cosine_numerators']) == 24, "Wrong cosine count")
    cs = [F(x,d['cosine_denominator']) for x in d['cosine_numerators']]
    require(len(d['pressure_numerators']) == 6, "Wrong pressure count")
    bs = [F(x,d['pressure_denominator']) for x in d['pressure_numerators']]
    require(all(b > 0 for b in bs), "Pressure must be positive")
    seen: set[tuple[int,int]] = set()
    cap = [F(0)]*7
    for i,j,x in d['pairs']:
        require(0 <= i < j <= 6 and (i,j) not in seen, "Invalid pair")
        require(x >= 0, "Negative pair weight")
        seen.add((i,j))
        cap[j-i] += F(x,d['pair_denominator'])
    require(len(seen) == 21 and cap[1:] == [F(2)]*6, "Span capacities failed")
    epsilon = F(d['epsilon'])
    require(0 < epsilon < F(9,400), "Close-pair budget cannot pay epsilon")
    B = sum(bs,F(0))
    require(B == F(1970462189,500000000000), "Incorrect total pressure")
    return epsilon, B, cs


def decimal_floor(x: F, digits: int = 35) -> str:
    scale = 10**digits
    q = (x.numerator*scale)//x.denominator
    sign = '-' if q < 0 else ''
    q = abs(q)
    return f'{sign}{q//scale}.{q%scale:0{digits}d}'


def enclosure(x: Interval, digits: int = 35) -> list[str]:
    unit = F(1,10**digits)
    return [decimal_floor(x.lo,digits), decimal_floor(x.hi+unit,digits)]


def partition(points: list[F], delta: F = F(4,5)) -> tuple[list[int], list[tuple[int,int]]]:
    """Disjoint close pairs and a separated remainder; indices refer to input."""
    require(all(x <= y for x,y in zip(points,points[1:])), "Points not ordered")
    require(delta > 0, "Nonpositive separation")
    remainder: list[int] = []
    pairs: list[tuple[int,int]] = []
    i = 0
    while i < len(points):
        if i+1 < len(points) and points[i+1]-points[i] < delta:
            pairs.append((i,i+1))
            i += 2
        else:
            remainder.append(i)
            i += 1
    # Every retained point was >=delta from its immediate next original point.
    # Removing later points can only increase that distance.
    return remainder, pairs


def run(n: int = 26) -> dict[str, Any]:
    d = read_inputs()
    epsilon, B, cs = capacities(d)
    S = sum(map(abs,cs),F(0))
    bern = majorant(S)
    require(F(3,4)-S > 0, "Window positivity failed")
    pair = F(7,30)-F(12,11)*S
    require(pair > F(3,20), "Close-pair kernel lower bound failed")
    pi, cosine, A = constants(n)
    require(F(3) < pi.lo and pi.hi < F(22,7), "Pi bounds failed")
    require(pi.hi*pi.hi < 10, "Pi-square bound failed")
    require(A.lo >= F(11,12), "Normalization lower bound failed")
    H0 = F(3,2)-cosine/A
    penalty = sum((c*c/2*(1-1/(2*j*j*pi*pi))
                   for j,c in enumerate(cs,1)),Interval.point(0))/(A*A)
    H = H0-penalty
    Hlo = F(d['baseline_lower'])
    require(H.lo > Hlo, "Analytic baseline lower bound failed")
    new = (Hlo-B)/(1-epsilon)
    require(new == F(104405554524189,155021134296875), "Target rational mismatch")
    old = F(d['comparison_bound'])
    require(new > old and new > F('0.6734923918'), "Improvement not established")
    inherited_mt = (H0-F(1,500))/(1-F(19,5000))
    return {
        'status': 'PASS: new exact finite checks only; analytic proof needs review',
        'input_sha256': INPUT_SHA,
        'six_dimensional_pressure_search_replayed': False,
        'rh_proved': False,
        'sum_absolute_coefficients': str(S),
        'majorant_bernstein_lower_bounds': [decimal_floor(x,20) for x in bern],
        'minimum_bernstein_coefficient': str(min(bern)),
        'separated_operator_norm_upper': str(F(29,20)/(F(4,5)*F(11,12))),
        'close_pair_kernel_lower': str(pair),
        'baseline_H_enclosure': enclosure(H),
        'new_bound_rational': str(new),
        'new_bound_enclosure': enclosure(Interval.point(new)),
        'comparison_bound_rational': str(old),
        'gain_over_comparison': enclosure(Interval.point(new-old)),
        'same_repo_pressure_improvement': enclosure(inherited_mt)
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check', type=Path, help='Reject unless saved result equals fresh reconstruction')
    args = p.parse_args()
    try:
        result = run()
        if args.check:
            require(json.loads(args.check.read_text()) == result, 'Saved result differs')
        print(json.dumps(result,indent=2,sort_keys=True))
    except (ValueError, OSError, KeyError, TypeError) as e:
        p.exit(1, f'FAIL: {e}\n')


if __name__ == '__main__':
    main()
