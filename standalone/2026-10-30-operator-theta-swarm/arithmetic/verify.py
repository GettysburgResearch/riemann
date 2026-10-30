#!/usr/bin/env python3
"""Exact rational finite witness for the native log-kernel phase obstruction.

Standard library only. This verifies the displayed finite bound Q_16, not RH,
an infinite numerical sum, or the complete analytic proofs in the companion note.
The omitted infinite sum is negative by the proof in Section 8.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
import json


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = Interval(F(other), F(other))
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Interval) else -F(other))

    def __mul__(self, scalar):
        scalar = F(scalar)
        if scalar >= 0:
            return Interval(self.lo * scalar, self.hi * scalar)
        return Interval(self.hi * scalar, self.lo * scalar)

    __rmul__ = __mul__


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def atan_small(x: F, terms: int = 32) -> Interval:
    """Alternating Taylor series, including an exact signed next-term bound."""
    x = F(x)
    require(abs(x) <= F(1, 2), "atan argument not reduced")
    if x < 0:
        return -atan_small(-x, terms)
    partial = sum(((-1) ** j * x ** (2*j+1) / (2*j+1)
                   for j in range(terms)), F(0))
    remainder_bound = x ** (2*terms+1) / (2*terms+1)
    if terms % 2 == 0:
        return Interval(partial, partial + remainder_bound)
    return Interval(partial - remainder_bound, partial)


PI = 16 * atan_small(F(1, 5)) - 4 * atan_small(F(1, 239))


def atan(x: F) -> Interval:
    x = F(x)
    if x < 0:
        return -atan(-x)
    if x > 1:
        return PI * F(1, 2) - atan(1/x)
    if x > F(1, 2):
        return PI * F(1, 4) + atan_small((x-1)/(x+1))
    return atan_small(x)


def log_reduced(x: F, terms: int = 32) -> Interval:
    require(1 <= x <= 2, "log argument not reduced")
    z = (x-1)/(x+1)
    partial = 2 * sum((z ** (2*j+1) / (2*j+1)
                       for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return Interval(partial, partial + tail)


LOG2 = log_reduced(F(2))


def log(x: F) -> Interval:
    x = F(x)
    require(x > 0, "nonpositive logarithm")
    power = 0
    while x >= 2:
        x /= 2
        power += 1
    while x < 1:
        x *= 2
        power -= 1
    return power * LOG2 + log_reduced(x)


def coarse_interval(value: Interval, digits: int = 12):
    denominator = 10 ** digits
    lower = value.lo.numerator * denominator // value.lo.denominator
    upper = -((-value.hi.numerator * denominator) // value.hi.denominator)
    return {
        "lower_numerator": lower,
        "upper_numerator": upper,
        "denominator": denominator,
    }


def main():
    # Independent easy range checks expose wrong reciprocal/quadrant signs.
    require(F(3141592653589793238, 10**18) < PI.lo
            and PI.hi < F(3141592653589793239, 10**18), "pi enclosure")
    require(atan(F(0)).lo == 0 == atan(F(0)).hi, "atan zero")
    require(atan(F(1)).lo <= PI.hi/4
            and atan(F(1)).hi >= PI.lo/4, "atan unit")
    require(log(F(1)).lo == 0 == log(F(1)).hi, "log unit")

    a8 = (1+F(16, 3)**2)*(1+F(16)**2)
    a16 = (1+F(32, 3)**2)*(1+F(32)**2)
    require(a8 == F(68105, 9), "first exact modulus")
    require(a16 == F(1058825, 9), "second exact modulus")
    r8 = log(a8) * F(-1, 2)
    r16 = log(a16) * F(-1, 2)

    q16 = -8*r8 - F(5, 2)*r16
    q16 += 12*(atan(F(16, 3))+atan(F(16)))
    q16 -= 6*(atan(F(32, 3))+atan(F(32)))
    for n in range(16):
        b = F(n) + F(1, 4)
        term = atan(8/b) - 2*atan(4/b)
        require(term.hi < 0, "finite summand sign")
        q16 += 12*term

    require(F(-1435, 1000) < q16.lo, "lower Q16 enclosure")
    require(q16.hi < F(-1434, 1000), "strict negative Q16 upper enclosure")

    # Real and imaginary coefficient parts separately produce positive forms.
    q_real = -8*r8 + 2*r16
    q_imag = -F(9, 2)*r16
    require(q_real.lo > 0, "real coefficient control")
    require(q_imag.lo > 0, "imaginary coefficient control")

    # Exact modulus-squared law at alpha=3/2; the note derives this from Gamma recurrence.
    modulus_samples = []
    for t in [F(0), F(1, 3), F(1), F(8), F(16)]:
        value = F(9, 1)/(9+4*t*t)/(1+4*t*t)
        require(0 < value <= 1, "symmetrized modulus control")
        modulus_samples.append({"t": str(t), "modulus_squared": str(value)})

    print(json.dumps({
        "status": "PASS_EXACT_RATIONAL_FINITE_PHASE_WITNESS",
        "alpha": "3/2",
        "nodes": [0, 8, 16],
        "coefficients_real": [-1, 2, -1],
        "coefficients_imag": ["-3/2", "0", "3/2"],
        "q16_interval": coarse_interval(q16),
        "complete_q_strict_upper_bound": "-717/500",
        "tail_argument": "Every omitted atan(2x)-2 atan(x) term is strictly negative for x>0.",
        "real_part_control": coarse_interval(q_real),
        "imaginary_part_control": coarse_interval(q_imag),
        "symmetrized_modulus_samples": modulus_samples,
        "arithmetic": "fractions.Fraction; rational log/atan remainders; Machin pi",
        "scope": "Finite phase obstruction only; the analytic no-infinite-divisibility theorem uses the written proof.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
