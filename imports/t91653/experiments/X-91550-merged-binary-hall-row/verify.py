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
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        other = as_i(other)
        values = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(value):
    if isinstance(value, I):
        return value
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return I(value, value)


DEN = 10**70
WINDOW_RIGHT = 55


@lru_cache(maxsize=None)
def sqrt_q(value):
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


@lru_cache(maxsize=None)
def invsqrt(n: int):
    return 1 / sqrt_q(Fraction(n))


@lru_cache(maxsize=None)
def log_q(value, terms: int = 160):
    value = Fraction(value)
    if value <= 0:
        raise ValueError("log argument must be positive")

    exponent = 0
    reduced = value
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1

    z = (reduced - 1) / (reduced + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / Fraction(2 * j + 1)
        power *= z2
    partial *= 2
    tail = 2 * power / (Fraction(2 * terms + 1) * (1 - z2))
    log_reduced = I(partial, partial + tail)
    if reduced == 1:
        log_reduced = I(Fraction(0), Fraction(0))

    z = Fraction(1, 3)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / Fraction(2 * j + 1)
        power *= z2
    partial *= 2
    tail = 2 * power / (Fraction(2 * terms + 1) * (1 - z2))
    log_two = I(partial, partial + tail)

    return log_reduced + exponent * log_two


def mobius_sieve(limit: int):
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            if prime > least[n] or prime * n > limit:
                break
            least[prime * n] = prime
            if n % prime == 0:
                mu[prime * n] = 0
                break
            mu[prime * n] = -mu[n]
    return mu


@lru_cache(maxsize=None)
def gamma_coeff(row: int, source: int):
    if source == row:
        return Fraction(row + 1, row - 1) * invsqrt(row)
    if source == row + 1:
        return -Fraction((row + 1) * (row - 2), row * (row - 1)) * invsqrt(row + 1)
    if source >= row + 2:
        return Fraction(2, row * (row - 1)) * invsqrt(source)
    return I(Fraction(0), Fraction(0))


def certify():
    mu = mobius_sieve(WINDOW_RIGHT - 1)

    # Conservative corridors containing all p>=67 binary-return parameters.
    corridors = {
        "survival_target": (Fraction(4, 3), Fraction(3, 2)),
        "survival_score": (Fraction(5, 3), Fraction(5, 3)),
        "hazard_target": (Fraction(1), Fraction(6, 5)),
        "hazard_score": (Fraction(1), Fraction(6, 5)),
    }

    hall_checks = 0
    hall_minimum = None
    hall_by_corridor = {}
    for name, (alpha_lo, alpha_hi) in corridors.items():
        local_minimum = None
        for threshold in range(1, WINDOW_RIGHT):
            if mu[threshold] != -1:
                continue

            a_prefix = Fraction(0)
            b_prefix = I(Fraction(0), Fraction(0))
            for n in range(1, threshold + 1):
                if mu[n] == 0:
                    continue
                a_prefix += Fraction(mu[n], n)
                b_prefix += mu[n] * invsqrt(n)

            if a_prefix >= 0:
                alpha = alpha_lo
                endpoint = Fraction(threshold)
            else:
                alpha = alpha_hi
                endpoint = Fraction(WINDOW_RIGHT)

            margin = alpha * a_prefix * sqrt_q(endpoint) - b_prefix
            assert margin.lo > Fraction(1, 250), (
                name,
                threshold,
                alpha,
                endpoint,
                a_prefix,
                margin,
            )
            record = (margin.lo, threshold, alpha, endpoint)
            if local_minimum is None or record[0] < local_minimum[0]:
                local_minimum = record
            if hall_minimum is None or record[0] < hall_minimum[0]:
                hall_minimum = (record[0], name, *record[1:])
            hall_checks += 1

        hall_by_corridor[name] = {
            "lower_decimal": float(local_minimum[0]),
            "threshold": local_minimum[1],
            "alpha_used": str(local_minimum[2]),
            "endpoint_used": str(local_minimum[3]),
            "certified_above": "1/250",
        }

    # For Q_Y(row)=c log Y-d on one activation cell, the derivative numerator
    # of Q_Y(row)/(alpha sqrt(Y)-1), after multiplying by 2Y, is
    # M_alpha(Y)=alpha sqrt(Y)(2c-Q_Y)-2c.
    # Its Y-derivative is -alpha Q_Y/(2sqrt(Y)) <=0, so the right cell endpoint
    # is worst.  Since sqrt(Y)(2c-Q_Y)>0, alpha=1 is worst over [1,5/3].
    component_checks = 0
    component_minimum = None
    for row in range(2, WINDOW_RIGHT):
        c_value = I(Fraction(0), Fraction(0))
        d_value = I(Fraction(0), Fraction(0))
        for cell in range(row, WINDOW_RIGHT):
            gamma = gamma_coeff(row, cell)
            c_value += gamma
            d_value += gamma * log_q(Fraction(cell))

            endpoint = Fraction(cell + 1)
            q_value = c_value * log_q(endpoint) - d_value
            assert q_value.lo >= 0, (row, cell, q_value)

            alpha_factor = sqrt_q(endpoint) * (2 * c_value - q_value)
            assert alpha_factor.lo > 0, (row, cell, alpha_factor)

            derivative_numerator = alpha_factor - 2 * c_value
            assert derivative_numerator.lo > Fraction(1, 25), (
                row,
                cell,
                derivative_numerator,
            )
            record = (derivative_numerator.lo, row, cell, endpoint)
            if component_minimum is None or record[0] < component_minimum[0]:
                component_minimum = record
            component_checks += 1

    result = {
        "classification": "PASS_MERGED_BINARY_HALL_ROW_CORRIDORS",
        "window": "1 <= x < 55",
        "rough_prime_floor": 67,
        "hall_checks": hall_checks,
        "hall_global_minimum": {
            "lower_decimal": float(hall_minimum[0]),
            "corridor": hall_minimum[1],
            "threshold": hall_minimum[2],
            "alpha_used": str(hall_minimum[3]),
            "endpoint_used": str(hall_minimum[4]),
            "certified_above": "1/250",
        },
        "hall_by_corridor": hall_by_corridor,
        "component_derivative_checks": component_checks,
        "component_derivative_minimum": {
            "lower_decimal": float(component_minimum[0]),
            "row": component_minimum[1],
            "cell": component_minimum[2],
            "right_endpoint": str(component_minimum[3]),
            "alpha_range": "1 <= alpha <= 5/3",
            "certified_above": "1/25",
        },
        "scope": (
            "Exact Fraction arithmetic with directed rational square-root and "
            "logarithm enclosures. The conservative parameter corridors contain "
            "all survival/hazard target and score channels for p>=67. This "
            "replay certifies the merged finite Hall/row inequalities, not the "
            "outer loss assembly or RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    certify()
