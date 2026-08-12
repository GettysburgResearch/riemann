#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isqrt, prod
import json
from pathlib import Path


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
            raise ZeroDivisionError("interval division across zero")
        return self * I(Fraction(1, other.hi), Fraction(1, other.lo))

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(value):
    if isinstance(value, I):
        return value
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return I(value, value)


DEN = 10**70
TERMS = 180
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
P61 = prod(PRIMES)
M61 = Fraction(55036345385124606673, 3351096610268770599522)
DELTA61 = Fraction(336338530534578047569, 224523472888007630167974)


@lru_cache(maxsize=None)
def sqrt_q(value: Fraction | int) -> I:
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


@lru_cache(maxsize=None)
def invsqrt(n: int) -> I:
    return 1 / sqrt_q(n)


@lru_cache(maxsize=None)
def log_two() -> I:
    z = Fraction(1, 3)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(TERMS):
        partial += power / Fraction(2 * j + 1)
        power *= z2
    partial *= 2
    tail = 2 * power / (Fraction(2 * TERMS + 1) * (1 - z2))
    return I(partial, partial + tail)


@lru_cache(maxsize=None)
def log_q(value: Fraction | int) -> I:
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

    if reduced == 1:
        log_reduced = I(Fraction(0), Fraction(0))
    else:
        z = (reduced - 1) / (reduced + 1)
        z2 = z * z
        power = z
        partial = Fraction(0)
        for j in range(TERMS):
            partial += power / Fraction(2 * j + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / (Fraction(2 * TERMS + 1) * (1 - z2))
        log_reduced = I(partial, partial + tail)
    return log_reduced + exponent * log_two()


def squarefree_divisors_with_mu():
    values = [(1, 1)]
    for prime in PRIMES:
        values += [(d * prime, -mu) for d, mu in list(values)]
    return sorted(values)


def component_constants(j: int):
    A = Fraction(j + 1, j - 1)
    B = -Fraction((j + 1) * (j - 2), j * (j - 1))
    C = Fraction(2, j * (j - 1))
    alpha = A * invsqrt(j) + B * invsqrt(j + 1)
    beta = A * invsqrt(j) * log_q(j) + B * invsqrt(j + 1) * log_q(j + 1)
    kappa = 2 * C * sqrt_q(j + 1) - alpha
    return A, B, C, alpha, beta, kappa


def certify_profiles():
    threshold = Fraction(7, 1000)
    eta_min = None
    lower_min = None
    alpha_min = None
    kappa_min = None

    for j in range(2, 67):
        _, _, C, alpha, beta, kappa = component_constants(j)
        assert alpha.lo > 0, ("alpha", j, alpha)
        assert kappa.lo > 0, ("kappa", j, kappa)

        # Right endpoint of the second activation cell, Y=(j+2)^-.
        eta = alpha * (2 - log_q(j + 2)) + beta
        assert eta.lo > threshold, ("second-cell", j, eta)

        N = j + 2
        lower = (
            2 * alpha
            + beta
            + kappa * log_q(N + 1)
            - 2 * C * sqrt_q(j + 1) * log_q(j + 1)
            + 2 * C * sqrt_q(N) * log_q(Fraction(N, N + 1))
        )
        assert lower.lo > threshold, ("tail-lower", j, lower)

        candidates = [
            (alpha.lo, j, alpha),
            (kappa.lo, j, kappa),
            (eta.lo, j, eta),
            (lower.lo, j, lower),
        ]
        if alpha_min is None or candidates[0][0] < alpha_min[0]:
            alpha_min = candidates[0]
        if kappa_min is None or candidates[1][0] < kappa_min[0]:
            kappa_min = candidates[1]
        if eta_min is None or candidates[2][0] < eta_min[0]:
            eta_min = candidates[2]
        if lower_min is None or candidates[3][0] < lower_min[0]:
            lower_min = candidates[3]

    return {
        "rows_checked": 65,
        "j_range": "2 <= j <= 66",
        "alpha_minimum": {"row": alpha_min[1], "lower_decimal": float(alpha_min[0])},
        "kappa_minimum": {"row": kappa_min[1], "lower_decimal": float(kappa_min[0])},
        "second_cell_minimum": {
            "row": eta_min[1],
            "lower_decimal": float(eta_min[0]),
            "certified_above": "7/1000",
        },
        "unbounded_tail_lower_minimum": {
            "row": lower_min[1],
            "lower_decimal": float(lower_min[0]),
            "certified_above": "7/1000",
        },
    }


def certify_prefixes():
    divisors = squarefree_divisors_with_mu()
    assert len(divisors) == 2 ** len(PRIMES)

    prefix = Fraction(0)
    maximum = None
    minimum_ge_67 = None
    prefix_at_66 = None
    small = []

    for divisor, mu in divisors:
        prefix += Fraction(mu, divisor)
        if divisor < 67:
            small.append((divisor, mu, prefix))
        if divisor == 66:
            prefix_at_66 = prefix
        if maximum is None or prefix > maximum[0]:
            maximum = (prefix, divisor)
        if divisor >= 67 and (minimum_ge_67 is None or prefix < minimum_ge_67[0]):
            minimum_ge_67 = (prefix, divisor)

    assert maximum == (Fraction(1), 1)
    assert minimum_ge_67 == (M61, 70), minimum_ge_67
    assert len(small) == 41
    assert small[-1][0] == 66
    assert prefix_at_66 is not None and prefix_at_66 > DELTA61
    assert M61 - Fraction(1, 67) == DELTA61
    assert DELTA61 > Fraction(1498, 10**6)

    expected_small = [
        1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23,
        26, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47,
        51, 53, 55, 57, 58, 59, 61, 62, 65, 66,
    ]
    assert [d for d, _, _ in small] == expected_small

    # Abel-core coefficient dictionary:
    # sum_{i=1}^{40} B_i(f_i-f_{i+1}) + delta f_41.
    prefixes = [entry[2] for entry in small]
    direct = []
    direct.append(prefixes[0])
    for i in range(1, 40):
        direct.append(prefixes[i] - prefixes[i - 1])
    direct.append(DELTA61 - prefixes[39])

    for i in range(40):
        d, mu, _ = small[i]
        assert direct[i] == Fraction(mu, d)
    assert sum(direct, Fraction(0)) == DELTA61

    return {
        "divisor_states": len(divisors),
        "small_core_divisors": expected_small,
        "small_core_size": len(small),
        "global_prefix_maximum": {"value": "1", "activation_divisor": 1},
        "minimum_prefix_for_z_ge_67": {
            "fraction": str(M61),
            "activation_divisor": 70,
            "decimal": float(M61),
        },
        "prefix_at_66": {"fraction": str(prefix_at_66), "decimal": float(prefix_at_66)},
        "uniform_adjoined_prime_floor": {
            "fraction": str(DELTA61),
            "decimal": float(DELTA61),
            "certified_above": "1498/1000000",
        },
        "abel_core_total_coefficient": str(sum(direct, Fraction(0))),
    }


def main():
    result = {
        "classification": "PASS_P61_FORTY_ONE_DIVISOR_CORE_REDUCTION",
        "profile_certificate": certify_profiles(),
        "prefix_certificate": certify_prefixes(),
        "scope": (
            "Exact Fraction arithmetic and directed rational square-root/logarithm "
            "enclosures certify the global profile lower bounds for j=2,...,66, "
            "the complete P_61 prefix corridor, the forty-one small divisors, and "
            "the Abel-core coefficient dictionary. The checker does not certify "
            "the remaining one-variable core inequality C_j(X)>=0 and does not "
            "prove the Riemann Hypothesis."
        ),
    }

    root = Path(__file__).resolve().parent
    output = root / "results" / "verification.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
