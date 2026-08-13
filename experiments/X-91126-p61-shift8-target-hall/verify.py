#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(1_000_000)

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
DEN = 10**55
SHIFT = 8


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


def sqrt_i(value: Fraction | int) -> I:
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    if root * root * value.denominator == value.numerator * DEN * DEN:
        return I(Fraction(root, DEN), Fraction(root, DEN))
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


def invsqrt_i(n: int) -> I:
    return 1 / sqrt_i(n)


def divisors_with_mu() -> list[tuple[int, int]]:
    values = [(1, 1)]
    for prime in PRIMES:
        old = list(values)
        values.extend((d * prime, -mu) for d, mu in old)
    return sorted(values)


def mobius_sieve(limit: int) -> list[int]:
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


def w_target(x: Fraction, n: int) -> I:
    if n > x:
        return as_i(0)
    return 4 * sqrt_i(x) / n - 3 * invsqrt_i(n)


def certify() -> None:
    divisors = divisors_with_mu()
    assert len(divisors) == 2 ** len(PRIMES)

    # Prefix arrays indexed by divisor threshold.  The reciprocal prefix is exact;
    # the inverse-square-root prefix is directed.
    even_a = Fraction(0)
    odd_a = Fraction(0)
    even_b = as_i(0)
    odd_b = as_i(0)
    prefix_records: dict[int, tuple[Fraction, I, Fraction, I]] = {}
    odd_thresholds: list[int] = []
    for d, mu in divisors:
        if mu == 1:
            even_a += Fraction(1, d)
            even_b += invsqrt_i(d)
        else:
            odd_a += Fraction(1, d)
            odd_b += invsqrt_i(d)
            odd_thresholds.append(d)
        prefix_records[d] = (even_a, even_b, odd_a, odd_b)

    divisor_values = [d for d, _ in divisors]

    def prefix_at(limit: int) -> tuple[Fraction, I, Fraction, I]:
        lo = 0
        hi = len(divisor_values)
        while lo < hi:
            mid = (lo + hi) // 2
            if divisor_values[mid] <= limit:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0:
            return Fraction(0), as_i(0), Fraction(0), as_i(0)
        return prefix_records[divisor_values[lo - 1]]

    minimum_a8 = None
    minimum_parent_bound = None
    a7_witness = None
    odd_prefix_checks = 0

    for t in odd_thresholds:
        even_a8, even_b8, _, _ = prefix_at(t + SHIFT)
        _, _, odd_a_t, odd_b_t = prefix_at(t)
        a8 = even_a8 - odd_a_t
        b8 = even_b8 - odd_b_t
        assert a8 > Fraction(1, 67), (t, a8)

        if minimum_a8 is None or a8 < minimum_a8[0]:
            minimum_a8 = (a8, t)

        u = Fraction(t + SHIFT)
        if u <= 67 * 67:
            lower = (
                4 * sqrt_i(u) * (as_i(a8) - Fraction(3, 4 * 67))
                - 3 * b8
            )
        else:
            lower = 4 * as_i(a8) * sqrt_i(u) - 3 * b8 - 201 / sqrt_i(u)
        assert lower.lo > Fraction(9, 5), (t, lower)
        if minimum_parent_bound is None or lower.lo < minimum_parent_bound[0]:
            minimum_parent_bound = (lower.lo, t)

        if t == 47:
            even_a7, _, _, _ = prefix_at(t + 7)
            a7_witness = even_a7 - odd_a_t
            assert a7_witness < 0

        odd_prefix_checks += 1

    assert a7_witness is not None

    # Directed child-prefix envelope C_y^(8)(t) < 3 sqrt(y) over all cells.
    mu = mobius_sieve(67)
    maximum_child_ratio = None
    child_checks = 0
    for threshold in range(2, 68):
        if mu[threshold] != -1:
            continue
        for cell in range(1, 67):
            # On cell y in [cell,cell+1], active sets are fixed.  The Hall margin
            # is affine in sqrt(y), so its maximum after division by sqrt(y) is
            # attained at one endpoint.
            for endpoint in (Fraction(cell), Fraction(cell + 1)):
                y = endpoint
                even_limit = min(threshold + SHIFT, int(y))
                odd_limit = min(threshold, int(y))
                value = as_i(0)
                for n in range(1, even_limit + 1):
                    if mu[n] == 1:
                        value += w_target(y, n)
                for n in range(1, odd_limit + 1):
                    if mu[n] == -1:
                        value -= w_target(y, n)
                ratio = value / sqrt_i(y)
                assert ratio.hi < 3, (threshold, cell, endpoint, ratio)
                record = (ratio.hi, threshold, cell, endpoint)
                if maximum_child_ratio is None or record[0] > maximum_child_ratio[0]:
                    maximum_child_ratio = record
                child_checks += 1

    result = {
        "classification": "PASS_P61_SHIFT8_TARGET_HALL",
        "small_prime_block": PRIMES,
        "divisor_states": len(divisors),
        "odd_prefix_checks": odd_prefix_checks,
        "shift": SHIFT,
        "minimum_shifted_reciprocal_prefix": {
            "lower_decimal": float(minimum_a8[0]),
            "threshold": minimum_a8[1],
            "certified_above": "1/67",
        },
        "minimum_nonterminal_parent_minus_child_lower_bound": {
            "lower_decimal": float(minimum_parent_bound[0]),
            "threshold": minimum_parent_bound[1],
            "certified_above": "9/5",
        },
        "maximum_child_hall_over_sqrt_y": {
            "upper_decimal": float(maximum_child_ratio[0]),
            "threshold": maximum_child_ratio[1],
            "cell": maximum_child_ratio[2],
            "endpoint": str(maximum_child_ratio[3]),
            "certified_below": "3",
        },
        "child_envelope_checks": child_checks,
        "radius_seven_exact_witness": {
            "threshold": 47,
            "value": str(a7_witness),
            "negative": True,
        },
        "scope": (
            "Exact reciprocal prefixes and directed fixed-point square-root "
            "enclosures certify the displacement-eight Ferrers Hall inequalities "
            "for the P61 one-prime target.  The symbolic theorem separately uses "
            "the resident positive total target for terminal thresholds x<t+8. "
            "This does not certify score/row subordination or RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    certify()
