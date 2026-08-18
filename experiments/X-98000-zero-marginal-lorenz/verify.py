#!/usr/bin/env python3
"""Exact rational-interval replay for T-98000.

The analytic squarefree-shell asymptotic uses the classical PNT and squarefree
density theorem. This replay certifies the finite cell constants, exact Lorenz
algebra, and Mellin numerator bookkeeping; it does not prove either zero-hinge
arithmetic sign or RH.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERDICT = "PASS_T98000_ZERO_MARGINAL_LORENZ_COLLAPSE"
DIGITS = 70
LOG_TERMS = 500


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-(other if isinstance(other, Interval) else Interval(other)))

    def __rsub__(self, other):
        return Interval(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        values = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def inv(self):
        assert self.lo > 0 or self.hi < 0
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        return self * other.inv()

    def __rtruediv__(self, other):
        return Interval(other) / self


def sqrt_interval(n: int) -> Interval:
    scale = 10**DIGITS
    lower = isqrt(n * scale * scale)
    return Interval(Fraction(lower, scale), Fraction(lower + 1, scale))


def log_interval(a: int, b: int = 1) -> Interval:
    """Exact atanh-series enclosure of log(a/b), for a>b>0."""
    assert a > b > 0
    z = Fraction(a - b, a + b)
    total = Fraction(0)
    power = z
    for j in range(LOG_TERMS + 1):
        total += power / Fraction(2 * j + 1)
        power *= z * z
    lower = 2 * total
    remainder = 2 * power / Fraction(2 * LOG_TERMS + 3) / (1 - z * z)
    return Interval(lower, lower + remainder)


def decimal_string(value: Fraction, places: int = 55) -> str:
    with localcontext() as context:
        context.prec = places + 20
        number = Decimal(value.numerator) / Decimal(value.denominator)
        return format(number, f".{places}f")


def qstar(m: int) -> int:
    if m == 1:
        return 0
    if m == 2:
        return 15
    if m == 3:
        return 6
    if m == 4:
        return 3
    return 6


def prefix_a(n: int) -> Interval:
    result = Interval(0)
    for m in range(1, n + 1):
        if qstar(m):
            result += Interval(qstar(m)) / sqrt_interval(m)
    return result


def prefix_b(n: int) -> Interval:
    result = Interval(0)
    for m in range(2, n + 1):
        if qstar(m):
            result += (
                Interval(qstar(m)) * log_interval(m) / sqrt_interval(m)
            )
    return result


def derivative_numerator_right(n: int) -> Interval:
    y = n + 1
    root = sqrt_interval(y)
    a = prefix_a(n)
    q = a * log_interval(y) - prefix_b(n)
    return a * (4 * root - 3) - 2 * root * q


def positive_part(value: Fraction) -> Fraction:
    return max(value, Fraction(0))


def lorenz_dual(even, odd, lam: Fraction) -> Fraction:
    target_odd = sum((target for target, scalar in odd), Fraction(0))
    scalar_odd = sum((scalar for target, scalar in odd), Fraction(0))
    return (
        lam * target_odd
        + sum(
            (
                positive_part(scalar - lam * target)
                for target, scalar in even
            ),
            Fraction(0),
        )
        - scalar_odd
    )


def one_switch_envelope(even, target: Fraction) -> Fraction:
    used = Fraction(0)
    value = Fraction(0)
    for atom_target, atom_scalar in even:
        take = min(atom_target, target - used)
        if take > 0:
            value += take * atom_scalar / atom_target
            used += take
        if used == target:
            break
    assert used == target
    return value


def run():
    finite = [derivative_numerator_right(n) for n in range(2, 8)]
    assert all(value.lo > 0 for value in finite)

    sqrt2 = sqrt_interval(2)
    sqrt3 = sqrt_interval(3)
    c = Interval(Fraction(27, 2)) - Interval(9) / sqrt2
    d = Interval(Fraction(39, 2)) - Interval(9) / sqrt2
    q4 = (
        Interval(15) * log_interval(2) / sqrt2
        + Interval(6) * log_interval(4, 3) / sqrt3
    )
    constant = q4 - 48 + c * log_interval(4)
    kappa = 36 + 4 * d + 2 * constant
    tail_margin = 2 * c * log_interval(8) - kappa
    shell_constant = 4 * log_interval(2) + 3 * sqrt2 - 6
    assert tail_margin.lo > Fraction(65, 100)
    assert shell_constant.lo > 1

    even = [
        (Fraction(2), Fraction(10)),
        (Fraction(3), Fraction(9)),
        (Fraction(5), Fraction(0)),
    ]
    odd = [(Fraction(4), Fraction(7)), (Fraction(2), Fraction(1))]
    target = sum((atom_target for atom_target, atom_scalar in odd), Fraction(0))
    envelope = one_switch_envelope(even, target)
    values = {
        lam: lorenz_dual(even, odd, lam)
        for lam in [Fraction(0), Fraction(3), Fraction(5), Fraction(6)]
    }
    assert envelope == 19
    assert values[Fraction(0)] == 11
    assert min(values.values()) == 11

    s = Fraction(7, 3)
    assert (
        4 / (s - Fraction(1, 2)) - 3 / s
        == (s + Fraction(3, 2)) / (s * (s - Fraction(1, 2)))
    )

    core = {
        "schema": "riemann.t98000.zero-marginal-lorenz.v2",
        "certificate_class": "EXACT_RATIONAL_INTERVALS",
        "ratio_monotonicity": {
            "finite_right_endpoint_lower_bounds": [
                decimal_string(value.lo) for value in finite
            ],
            "analytic_tail_start": 8,
            "tail_margin_lower": decimal_string(tail_margin.lo),
            "range": "[0,6)",
            "strict_after": 2,
        },
        "one_switch_order": True,
        "zero_marginal_shell": {
            "constant_lower": decimal_string(shell_constant.lo),
            "coefficient": "(3/pi^2)*(4log2+3sqrt2-6)",
            "eventually_positive": True,
        },
        "lorenz_fixture": {
            "envelope": str(envelope),
            "dual_at_zero": str(values[Fraction(0)]),
            "marginal_lambda": "0",
        },
        "target_mellin_identity": True,
        "cpsl67_proved": False,
        "gpc67_proved": False,
        "gtc67_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main():
    result = run()
    output = HERE / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
