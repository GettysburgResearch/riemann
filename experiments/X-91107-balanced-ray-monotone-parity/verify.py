#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
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
        vals = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("interval contains zero")
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(value) -> I:
    if isinstance(value, I):
        return value
    if not isinstance(value, Fraction):
        value = Fraction(value)
    return I(value, value)


DEN = 10**70
ROOT_LO = Fraction(1844367547103, 10**14)
WINDOW_X_MAX = 1 / ROOT_LO


def sqrt_q(value: Fraction | int) -> I:
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


def mobius_sieve(limit: int) -> tuple[list[int], list[int]]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or p * n > limit:
                break
            least[p * n] = p
            if n % p == 0:
                mu[p * n] = 0
                break
            mu[p * n] = -mu[n]
    return mu, primes


MU, PRIMES = mobius_sieve(500)


def eta_zeta_half_interval(n_terms: int = 100) -> tuple[I, I]:
    if n_terms % 2:
        raise ValueError("need an even alternating partial sum")
    partial = I(Fraction(0), Fraction(0))
    for n in range(1, n_terms + 1):
        term = 1 / sqrt_q(n)
        partial = partial + term if n % 2 else partial - term
    eta = I(partial.lo, partial.hi + (1 / sqrt_q(n_terms + 1)).hi)
    zeta = eta / (I(Fraction(1), Fraction(1)) - sqrt_q(2))
    return eta, zeta


def atom_weight(a: int, x: Fraction, n: int) -> I:
    return a * sqrt_q(x) / n - 1 / sqrt_q(n)


def hall_margin(*, a: int, displacement: int, active_max: int, threshold: int, x: Fraction) -> I:
    value = I(Fraction(0), Fraction(0))
    for n in range(1, active_max + 1):
        wt = atom_weight(a, x, n)
        if MU[n] == 1 and n <= threshold + displacement:
            value += wt
        elif MU[n] == -1 and n <= threshold:
            value -= wt
    return value


def interval_seed(even_node: int, odd_node: int, mass: Fraction) -> dict[int, Fraction]:
    if even_node > odd_node:
        raise ValueError("monotone edge required")
    return {n: mass for n in range(even_node + 1, odd_node + 1)}


def delta(seed: dict[int, Fraction], n: int) -> Fraction:
    return seed.get(n, Fraction(0)) - seed.get(n + 1, Fraction(0))


def carry(seed: dict[int, Fraction], q: int) -> Fraction:
    if not seed:
        return Fraction(0)
    return sum(
        seed.get(k * q, Fraction(0)) - seed.get(k * q + 1, Fraction(0))
        for k in range(1, max(seed) // q + 2)
    )


def main() -> None:
    _, zeta_i = eta_zeta_half_interval(100)
    assert zeta_i.hi < Fraction(-4, 3), zeta_i
    assert zeta_i.lo > Fraction(-8, 5), zeta_i

    kappa_i = -2 * (I(Fraction(1), Fraction(1)) + zeta_i) / (
        I(Fraction(2), Fraction(2)) + zeta_i
    )
    assert kappa_i.lo > 1, kappa_i

    minimum_strict_equality = None
    minimum_balanced = None
    checks = 0

    for active_max in range(1, 55):
        right = Fraction(active_max + 1) if active_max < 54 else WINDOW_X_MAX
        odd_thresholds = [n for n in range(1, active_max + 1) if MU[n] == -1]
        for threshold in odd_thresholds:
            for x in (Fraction(active_max), right):
                reserve = hall_margin(
                    a=1,
                    displacement=0,
                    active_max=active_max,
                    threshold=threshold,
                    x=x,
                )
                equality_strict = hall_margin(
                    a=2,
                    displacement=0,
                    active_max=active_max,
                    threshold=threshold,
                    x=x,
                )
                assert reserve.lo > Fraction(39, 100)
                assert equality_strict.lo > Fraction(-9, 50)

                balanced = equality_strict + kappa_i * reserve
                assert balanced.lo > Fraction(1, 5), (
                    active_max,
                    threshold,
                    x,
                    balanced,
                )

                rec_e = (equality_strict.lo, active_max, threshold, x)
                rec_b = (balanced.lo, active_max, threshold, x)
                if minimum_strict_equality is None or rec_e[0] < minimum_strict_equality[0]:
                    minimum_strict_equality = rec_e
                if minimum_balanced is None or rec_b[0] < minimum_balanced[0]:
                    minimum_balanced = rec_b
                checks += 1

    edge_checks = 0
    carry_checks = 0
    for e in range(1, 55):
        for o in range(e, 55):
            mass = Fraction(e + o + 1, 113)
            seed = interval_seed(e, o, mass)
            for n in range(1, 56):
                expected = (
                    Fraction(0)
                    if e == o
                    else (mass if n == o else (-mass if n == e else Fraction(0)))
                )
                assert delta(seed, n) == expected, (e, o, n)
            edge_checks += 1

            for q in range(1, 55):
                expected = mass * (
                    (1 if o % q == 0 else 0) - (1 if e % q == 0 else 0)
                )
                assert carry(seed, q) == expected, (e, o, q)
                detail = carry(seed, q) - 2 * carry(seed, 4 * q)
                expected_detail = mass * (
                    (1 if o % q == 0 else 0)
                    - 2 * (1 if o % (4 * q) == 0 else 0)
                    - (1 if e % q == 0 else 0)
                    + 2 * (1 if e % (4 * q) == 0 else 0)
                )
                assert detail == expected_detail, (e, o, q)
                carry_checks += 1

    assert minimum_strict_equality is not None
    assert minimum_balanced is not None

    result = {
        "classification": "PASS_BALANCED_RAY_MONOTONE_PARITY_LIFT",
        "checks": checks + edge_checks + carry_checks,
        "zeta_half_interval": [float(zeta_i.lo), float(zeta_i.hi)],
        "kappa_interval": [float(kappa_i.lo), float(kappa_i.hi)],
        "strict_equality_hall_minimum": {
            "lower": float(minimum_strict_equality[0]),
            "cell_N": minimum_strict_equality[1],
            "threshold": minimum_strict_equality[2],
            "x": str(minimum_strict_equality[3]),
            "certified_above": "-9/50",
        },
        "balanced_hall_minimum": {
            "lower": float(minimum_balanced[0]),
            "cell_N": minimum_balanced[1],
            "threshold": minimum_balanced[2],
            "x": str(minimum_balanced[3]),
            "certified_above": "1/5",
            "support": "e <= o",
        },
        "interval_seed_edges_checked": edge_checks,
        "carry_and_detail_checks": carry_checks,
        "scope": (
            "The replay certifies the no-upward Hall margin and the exact "
            "nonnegative interval-seed/carry/detail identities. It does not "
            "certify nonnegative endpoint-row coefficients for the interval seed."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
