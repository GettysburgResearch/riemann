#!/usr/bin/env python3
"""Exact/directed replay for the factor-54 adversarial repair packet.

Checks:
1. exact exponent-vector proof that K_m = log(m), 2 <= m <= 201;
2. directed interval proof H(67) > 5*sqrt(67)-3;
3. analytic inequalities used in the residual-entropy theorem;
4. exact affine-vs-same-index counterexample at p=67, Y=201;
5. target-minus-score countermodel;
6. monotonicity of the radix-four detail target on a finite rational grid.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Dict, List

getcontext().prec = 90
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def primes_upto(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for k in range(p * p, n + 1, p):
                sieve[k] = False
    return [p for p in range(2, n + 1) if sieve[p]]


PRIMES = primes_upto(300)


def factor_vector(n: int) -> Dict[int, Fraction]:
    out: Dict[int, Fraction] = {}
    x = n
    for p in PRIMES:
        if p * p > x:
            break
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e:
            out[p] = Fraction(e)
    if x > 1:
        out[x] = out.get(x, Fraction(0)) + 1
    return out


def add_scaled(dst: Dict[int, Fraction], src: Dict[int, Fraction], a: Fraction) -> None:
    for p, e in src.items():
        dst[p] = dst.get(p, Fraction(0)) + a * e
        if dst[p] == 0:
            del dst[p]


def g_vector(j: int) -> Dict[int, Fraction]:
    out: Dict[int, Fraction] = {}
    for r in range(j + 1):
        c = math.comb(j, r)
        add_scaled(out, factor_vector(c), Fraction(1, j + 1))
    return out


def k_vector(m: int, gs: Dict[int, Dict[int, Fraction]]) -> Dict[int, Fraction]:
    out: Dict[int, Fraction] = {}
    add_scaled(out, gs[m], Fraction(m + 1, m - 1))
    if m >= 3:
        add_scaled(out, gs[m - 1], -Fraction(m * (m - 3), (m - 1) * (m - 2)))
    for j in range(2, m - 1):
        add_scaled(out, gs[j], Fraction(2, j * (j - 1)))
    return out


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def scale(self, a: Fraction) -> "Interval":
        return Interval(a * self.lo, a * self.hi) if a >= 0 else Interval(a * self.hi, a * self.lo)


def atanh_log_ratio_interval(num: int, den: int, terms: int = 700) -> Interval:
    assert num > den > 0
    x = Fraction(num - den, num + den)
    s = Fraction(0)
    power = x
    for k in range(terms):
        s += power / (2 * k + 1)
        power *= x * x
    lo = 2 * s
    tail = 2 * power / ((2 * terms + 1) * (1 - x * x))
    return Interval(lo, lo + tail)


def sqrt_interval(n: int, scale: int = 10**70) -> Interval:
    a = math.isqrt(n * scale * scale)
    return Interval(Fraction(a, scale), Fraction(a + 1, scale))


def frac_decimal(x: Fraction, digits: int = 45) -> str:
    getcontext().prec = digits + 10
    return format(Decimal(x.numerator) / Decimal(x.denominator), f".{digits}g")


def h67_interval() -> Interval:
    total = Interval(Fraction(0), Fraction(0))
    for m in range(2, 68):
        lm = atanh_log_ratio_interval(m, 1)
        l67m = atanh_log_ratio_interval(67, m) if m < 67 else Interval(Fraction(0), Fraction(0))
        prod = Interval(lm.lo * l67m.lo, lm.hi * l67m.hi)
        sm = sqrt_interval(m)
        inv = Interval(1 / sm.hi, 1 / sm.lo)
        term = Interval(prod.lo * inv.lo, prod.hi * inv.hi)
        total = total + term
    return total


def omega(X: float, q: int) -> float:
    if X < q:
        return 0.0
    if X < 4 * q:
        return math.log(X / q) / math.sqrt(q)
    return math.log(4.0) / math.sqrt(q)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    checks = 0

    gs = {j: g_vector(j) for j in range(2, 202)}
    for m in range(2, 202):
        assert k_vector(m, gs) == factor_vector(m), m
        checks += 1

    h67 = h67_interval()
    s67 = sqrt_interval(67)
    rhs67 = Interval(5 * s67.lo - 3, 5 * s67.hi - 3)
    margin_lo = h67.lo - rhs67.hi
    assert margin_lo > Fraction(12764, 10000)
    checks += 1

    for N in range(67, 10001):
        assert Fraction(8, 3) ** 2 * N > Fraction(5, 2) ** 2 * (N + 1)
        checks += 1
    for p in [q for q in PRIMES if q >= 67]:
        r = 1 / math.sqrt(p)
        assert 5 * math.sqrt(p) - 3 > 5 * (1 - 1 / p) * (1 - r) * math.sqrt(p)
        assert r * (1 + 4 * r) < 5 * (1 - 1 / p)
        checks += 2

    lp = atanh_log_ratio_interval(201, 200)
    sp = sqrt_interval(200)
    q_parent = Interval(
        Fraction(201, 199) * lp.lo / sp.hi,
        Fraction(201, 199) * lp.hi / sp.lo,
    )
    lc = atanh_log_ratio_interval(3, 2)
    sc = sqrt_interval(134)
    q_child = Interval(3 * lc.lo / sc.hi, 3 * lc.hi / sc.lo)
    assert q_parent.hi < Fraction(1, 2000)
    assert q_child.lo > Fraction(1, 10)
    checks += 2

    T = Fraction(1)
    S = Fraction(1)
    Hrow = Fraction(0)
    assert max(T - S, 0) == 0
    assert max(S - Hrow, 0) == 1
    assert max(S - Hrow, 0) <= 2 * T
    checks += 3

    for q in range(2, 250):
        vals = [omega(X / 8, q) for X in range(8, 8 * 1200 + 1)]
        assert all(a <= b + 1e-14 for a, b in zip(vals, vals[1:]))
        checks += 1

    result = {
        "verdict": "PASS_FACTOR54_ACTUAL_ENTROPY_AND_CHILD_LIFT_REPAIR",
        "checks": checks,
        "exact_Km_range": [2, 201],
        "H67_lower": frac_decimal(h67.lo),
        "H67_upper": frac_decimal(h67.hi),
        "rhs67_upper": frac_decimal(rhs67.hi),
        "certified_margin_lower": frac_decimal(margin_lo),
        "affine_counterexample": {
            "p": 67,
            "parent_Y": 201,
            "child_Y": 3,
            "child_row": 2,
            "affine_parent_row": 200,
            "parent_upper": frac_decimal(q_parent.hi),
            "affine_child_lower": frac_decimal(q_child.lo),
            "certified_comparison": "parent < 1/2000 < 1/10 < affine child"
        },
        "actual_debt_countermodel": {
            "T": 1,
            "S": 1,
            "row_entropy": 0,
            "old_T_minus_S_debt": 0,
            "actual_S_minus_H_debt": 1
        }
    }

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n")


if __name__ == "__main__":
    main()
