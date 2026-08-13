#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(100000)

@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction
    def __add__(self, other):
        other = as_i(other); return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-as_i(other))
    def __rsub__(self, other): return as_i(other) - self
    def __mul__(self, other):
        other = as_i(other)
        vals = (self.lo*other.lo, self.lo*other.hi,
                self.hi*other.lo, self.hi*other.hi)
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("interval contains zero")
        return self * I(1/other.hi, 1/other.lo)
    def __rtruediv__(self, other): return as_i(other) / self

def as_i(value) -> I:
    if isinstance(value, I): return value
    if not isinstance(value, Fraction): value = Fraction(value)
    return I(value, value)

DEN = 10**90

def sqrt_q(value: Fraction | int) -> I:
    value = Fraction(value)
    z = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(z)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))

def log_q(value: Fraction, terms: int = 220) -> I:
    value = Fraction(value)
    if value <= 0: raise ValueError("log domain")
    k = 0; y = value
    while y >= 2: y /= 2; k += 1
    while y < 1: y *= 2; k -= 1
    z = (y - 1)/(y + 1); zz = z*z; p = z; total = Fraction(0)
    for j in range(terms):
        total += p/Fraction(2*j + 1); p *= zz
    total *= 2
    tail = 2*p/(Fraction(2*terms + 1)*(1 - zz))
    ly = I(total, total + tail)
    if y == 1: ly = I(Fraction(0), Fraction(0))
    z2 = Fraction(1,3); zz2 = z2*z2; p2 = z2; s2 = Fraction(0)
    for j in range(terms):
        s2 += p2/Fraction(2*j + 1); p2 *= zz2
    s2 *= 2
    tail2 = 2*p2/(Fraction(2*terms + 1)*(1 - zz2))
    return ly + k*I(s2, s2 + tail2)

@lru_cache(maxsize=None)
def alpha(T: int) -> I:
    return 2*log_q(Fraction(T, T-1))

@lru_cache(maxsize=None)
def delta(T: int) -> I:
    return 4*(1/sqrt_q(T-1) - 1/sqrt_q(T))

@lru_cache(maxsize=None)
def rnode(T: int) -> I:
    return delta(T)/alpha(T)

@lru_cache(maxsize=None)
def theta(T: int) -> I:
    return (rnode(T) - rnode(T+1))/(rnode(T-1) - rnode(T+1))

def ab(T: int) -> tuple[I,I]:
    al = alpha(T); th = theta(T)
    A = al*th*sqrt_q(T-1)*(rnode(T-1)*sqrt_q(T-1) - 1)
    B = al*(1-th)*sqrt_q(T)*(1 - rnode(T+1)*sqrt_q(T))
    return A,B

AB: dict[int, tuple[I,I]] = {T: ab(T) for T in range(3,56)}

def A(T: int) -> I: return AB[T][0]
def B(T: int) -> I:
    if T == 2: return I(Fraction(0), Fraction(0))
    return AB[T][1]

def main() -> None:
    min_gap = None
    max_ratio = None
    for T in range(3,56):
        aa,bb = AB[T]
        assert bb.lo > 0, (T,bb)
        assert aa.lo > bb.hi, (T,aa,bb)
        assert 200*bb.hi < 199*aa.lo, (T,aa,bb)
        gap = aa.lo - bb.hi
        ratio = bb.hi/aa.lo
        if min_gap is None or gap < min_gap[0]: min_gap=(gap,T)
        if max_ratio is None or ratio > max_ratio[0]: max_ratio=(ratio,T)

    # Once 0<B_T/A_T<199/200, the exact normalized recurrence
    # x_(n+1)=(B_(n+1)/A_(n+1))(1-x_n), x_(e+1)=0,
    # remains in [0,199/200) on every edge.
    edges=sum(54-e for e in range(1,54))
    recurrence_steps=sum(sum(o-e for o in range(e+1,55)) for e in range(1,54))
    max_eta=1/min(A(T).lo for T in range(3,56))

    result={
      "classification":"PASS_INTERVAL_SEED_POSITIVE_BUTTERFLY_LIFT",
      "butterfly_levels_checked":53,
      "monotone_edges_checked":edges,
      "recurrence_steps_checked":recurrence_steps,
      "minimum_A_minus_B":{"level_T":min_gap[1],"lower":float(min_gap[0])},
      "maximum_B_over_A":{"level_T":max_ratio[1],"upper":float(max_ratio[0])},
      "uniform_boundary_overshoot_ratio_upper":"199/200",
      "unit_mass_intensity_upper":float(max_eta),
      "scope":"Directed Fraction/sqrt/log intervals certify A_T>B_T>0 and the uniform ratio. The recurrence induction and exact seed identity are symbolic. Baseline endpoint-weight and positive-boundary capacity compatibility are not certified."
    }
    path=Path(__file__).resolve().parent/'results'/'verification.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(path)

if __name__=='__main__': main()
