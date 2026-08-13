#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(1_000_000)

SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
SCALE = 10**35
MAX_J = 66
MAX_K = 67 * MAX_J


def floor_scaled(x: Fraction) -> int:
    return (x.numerator * SCALE) // x.denominator


def ceil_scaled(x: Fraction) -> int:
    return -((-x.numerator * SCALE) // x.denominator)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __add__(self, other: object) -> "I":
        o = as_i(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self) -> "I":
        return I(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "I":
        return self + (-as_i(other))

    def __rsub__(self, other: object) -> "I":
        return as_i(other) - self

    def __mul__(self, other: object) -> "I":
        o = as_i(other)
        values = (
            self.lo * o.lo,
            self.lo * o.hi,
            self.hi * o.lo,
            self.hi * o.hi,
        )
        lower = min(values) // SCALE
        upper = -((-max(values)) // SCALE)
        return I(lower, upper)

    __rmul__ = __mul__

    def lower_float(self) -> float:
        return self.lo / SCALE

    def upper_float(self) -> float:
        return self.hi / SCALE


def as_i(x: object) -> I:
    if isinstance(x, I):
        return x
    if isinstance(x, int):
        return I(x * SCALE, x * SCALE)
    if isinstance(x, Fraction):
        return I(floor_scaled(x), ceil_scaled(x))
    raise TypeError(type(x))


def abs_upper(x: I) -> int:
    return max(abs(x.lo), abs(x.hi))


def mul_upper(a: int, b: int) -> int:
    assert a >= 0 and b >= 0
    return -((-(a * b)) // SCALE)


def invsqrt_i(n: int) -> I:
    q = (SCALE * SCALE) // n
    m = isqrt(q)
    if m * m * n == SCALE * SCALE:
        return I(m, m)
    return I(m, m + 1)


def log_bounds(x: Fraction, terms: int = 120) -> I:
    assert x > 0
    power = 0
    y = x
    while y >= 2:
        y /= 2
        power += 1
    while y < 1:
        y *= 2
        power -= 1

    z = (y - 1) / (y + 1)
    z2 = z * z
    term = z
    total = Fraction(0)
    for k in range(terms):
        total += term / Fraction(2 * k + 1)
        term *= z2
    total *= 2
    tail = 2 * abs(term) / (Fraction(2 * terms + 1) * (1 - z2))
    low_y = total
    high_y = total + tail

    z = Fraction(1, 3)
    z2 = z * z
    term = z
    total2 = Fraction(0)
    for k in range(terms):
        total2 += term / Fraction(2 * k + 1)
        term *= z2
    total2 *= 2
    tail2 = 2 * term / (Fraction(2 * terms + 1) * (1 - z2))
    low2 = total2
    high2 = total2 + tail2

    if power >= 0:
        low = low_y + power * low2
        high = high_y + power * high2
    else:
        low = low_y + power * high2
        high = high_y + power * low2
    return I(floor_scaled(low), ceil_scaled(high))


def sieve(limit: int) -> tuple[list[int], list[int]]:
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    primes = [n for n in range(2, limit + 1) if spf[n] == n]
    return spf, primes


def build_divisors(prime_logs: dict[int, I]) -> list[tuple[int, int, I]]:
    values: list[tuple[int, int, I]] = [(1, 1, as_i(0))]
    for p in SMALL_PRIMES:
        old = list(values)
        values.extend((d * p, -mu, ld + prime_logs[p]) for d, mu, ld in old)
    values.sort(key=lambda row: row[0])
    return values


def weights_for_row(j: int) -> dict[int, I]:
    c = as_i(Fraction(2, j * (j - 1)))
    weights: dict[int, I] = {}
    for m in range(1, j):
        weights[m] = -(c * invsqrt_i(m))
    weights[j] = as_i(Fraction(j + 2, j)) * invsqrt_i(j)
    weights[j + 1] = -invsqrt_i(j + 1)
    return weights


def kr_upper(weights: dict[int, I], total: I, log_n: list[I], j: int) -> tuple[int, int]:
    best: int | None = None
    best_anchor = -1
    for anchor in range(1, j + 2):
        adjusted = dict(weights)
        adjusted[anchor] = adjusted[anchor] - total
        nodes = sorted(adjusted, reverse=True)
        cumulative = as_i(0)
        value = 0
        for left, right in zip(nodes[:-1], nodes[1:]):
            cumulative = cumulative + adjusted[left]
            length = log_n[left] - log_n[right]
            assert length.lo >= 0
            value += mul_upper(abs_upper(cumulative), length.hi)
        if best is None or value < best:
            best = value
            best_anchor = anchor
    assert best is not None
    return best, best_anchor


def main() -> None:
    spf, primes = sieve(MAX_K)
    prime_logs = {p: log_bounds(Fraction(p)) for p in primes}

    log_n = [as_i(0) for _ in range(MAX_K + 1)]
    for n in range(2, MAX_K + 1):
        p = spf[n]
        log_n[n] = log_n[n // p] + prime_logs[p]

    divisors = build_divisors(prime_logs)
    assert len(divisors) == 2 ** len(SMALL_PRIMES)

    one = as_i(1)
    beta = as_i(1)
    for p in SMALL_PRIMES:
        beta = beta * (one - invsqrt_i(p))
    assert beta.hi < as_i(Fraction(1, 400)).lo

    c_bound = as_i(Fraction(7, 6))
    l_bound = as_i(Fraction(27, 20))
    prefix_m = as_i(0)
    prefix_log = as_i(0)
    maximum_e = 0
    maximum_l = 0
    maximum_e_location: tuple[str, int] | None = None
    maximum_l_location = -1

    for index, (d, mu, log_d) in enumerate(divisors):
        inv = invsqrt_i(d)
        weighted_log = inv * log_d
        if mu == 1:
            prefix_m = prefix_m + inv
            prefix_log = prefix_log + weighted_log
        else:
            prefix_m = prefix_m - inv
            prefix_log = prefix_log - weighted_log

        slope = prefix_m - beta
        slope_abs = abs_upper(slope)
        assert slope_abs < l_bound.lo
        if slope_abs > maximum_l:
            maximum_l = slope_abs
            maximum_l_location = d

        e_left = slope * log_d - prefix_log
        e_abs = abs_upper(e_left)
        assert e_abs < c_bound.lo
        if e_abs > maximum_e:
            maximum_e = e_abs
            maximum_e_location = ("left", d)

        if index + 1 < len(divisors):
            next_d, _, next_log = divisors[index + 1]
            e_right = slope * next_log - prefix_log
            e_abs = abs_upper(e_right)
            assert e_abs < c_bound.lo
            if e_abs > maximum_e:
                maximum_e = e_abs
                maximum_e_location = ("right", next_d)

    # On (0,1), the causal extension E(u)=-beta log u.  The only relevant
    # range is u>=2/3, and this is far inside the same 7/6 corridor.
    log_three_halves = log_bounds(Fraction(3, 2))
    assert (beta * log_three_halves).hi < c_bound.lo

    rough = [True] * (MAX_K + 1)
    rough[0] = False
    for p in SMALL_PRIMES:
        for n in range(p, MAX_K + 1, p):
            rough[n] = False
    rough[1] = True

    beta_majorant = as_i(Fraction(1, 400))
    r0 = invsqrt_i(67)
    log67 = log_n[67]
    margin_target = as_i(Fraction(1, 500))

    minimum_margin: tuple[int, int, int] | None = None
    minimum_coefficient: tuple[int, int] | None = None
    row_records = []

    for j in range(2, MAX_J + 1):
        a_sum = as_i(0)
        b_sum = as_i(0)
        for k in range(1, 67 * j + 1):
            if rough[k]:
                inv = invsqrt_i(k)
                a_sum = a_sum + inv
                b_sum = b_sum + inv * log_n[k]

        weights = weights_for_row(j)
        total = as_i(0)
        weighted_log = as_i(0)
        for m, weight in weights.items():
            total = total + weight
            weighted_log = weighted_log + weight * log_n[m]

        total_abs = abs_upper(total)
        weighted_log_abs = abs_upper(weighted_log)
        wasserstein, anchor = kr_upper(weights, total, log_n, j)

        c = as_i(Fraction(2, j * (j - 1)))
        total_abs_i = I(total_abs, total_abs)
        weighted_log_abs_i = I(weighted_log_abs, weighted_log_abs)
        wasserstein_i = I(wasserstein, wasserstein)

        log_coefficient = c * a_sum - beta_majorant * total_abs_i
        assert log_coefficient.lo > 0

        margin = (
            log_coefficient * log67
            + c * ((a_sum - r0) * log_n[j] - b_sum)
            - (one + r0)
            * (c_bound * total_abs_i + l_bound * wasserstein_i)
            - beta_majorant
            * (total_abs_i * log67 + weighted_log_abs_i)
        )
        assert margin.lo > margin_target.hi, (j, margin.lower_float())

        if minimum_margin is None or margin.lo < minimum_margin[0]:
            minimum_margin = (margin.lo, j, anchor)
        if minimum_coefficient is None or log_coefficient.lo < minimum_coefficient[0]:
            minimum_coefficient = (log_coefficient.lo, j)

        row_records.append(
            {
                "j": j,
                "margin_lower": margin.lower_float(),
                "log_p_coefficient_lower": log_coefficient.lower_float(),
                "kr_upper": wasserstein / SCALE,
                "kr_anchor": anchor,
            }
        )

    assert minimum_margin is not None and minimum_coefficient is not None

    result = {
        "classification": "PASS_P61_ONE_PRIME_GREEN_BOUNDARY_DOMINATION",
        "small_prime_block": SMALL_PRIMES,
        "divisor_cells_checked": len(divisors),
        "beta_interval": [beta.lower_float(), beta.upper_float()],
        "beta_upper_gate": "1/400",
        "E_uniform_abs_upper": maximum_e / SCALE,
        "E_uniform_gate": "7/6",
        "E_extremal_location": maximum_e_location,
        "E_log_lipschitz_upper": maximum_l / SCALE,
        "E_log_lipschitz_gate": "27/20",
        "E_slope_extremal_divisor": maximum_l_location,
        "rows_checked": [2, MAX_J],
        "minimum_row_margin": {
            "lower": minimum_margin[0] / SCALE,
            "row_j": minimum_margin[1],
            "kr_anchor": minimum_margin[2],
            "certified_above": "1/500",
        },
        "minimum_log_p_coefficient": {
            "lower": minimum_coefficient[0] / SCALE,
            "row_j": minimum_coefficient[1],
        },
        "row_records": row_records,
        "scope": (
            "Fixed-point directed intervals certify the global P_61 Green-error "
            "corridor, its logarithmic Lipschitz constant, the bounded-Lipschitz "
            "boundary norm, and a >1/500 lower bound for every inherited one-prime "
            "row.  The symbolic theorem converts these gates into the statement "
            "for all real p>=67 and j<=y<=67.  This checker does not by itself "
            "audit the remaining factor-54 composition or prove RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(json.dumps(result["minimum_row_margin"], sort_keys=True))
    print(output)


if __name__ == "__main__":
    main()
