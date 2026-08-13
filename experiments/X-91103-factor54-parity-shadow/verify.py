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
        values = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return I(min(values), max(values))

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


def sqrt_q(value: Fraction) -> I:
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
        for prime in primes:
            if prime > least[n] or prime * n > limit:
                break
            least[prime * n] = prime
            if n % prime == 0:
                mu[prime * n] = 0
                break
            mu[prime * n] = -mu[n]
    return mu, primes


MU, PRIMES = mobius_sieve(500)
ROOT_LO = Fraction(1844367547103, 10**14)
ROOT_HI = Fraction(1844367547105, 10**14)
WINDOW_X_MAX = 1 / ROOT_LO


def atom_weight(a: int, x: Fraction, n: int) -> I:
    return a * sqrt_q(x) / n - 1 / sqrt_q(Fraction(n))


def hall_margin(
    *,
    a: int,
    displacement: int,
    active_max: int,
    threshold: int,
    x: Fraction,
) -> I:
    value = I(Fraction(0), Fraction(0))
    for n in range(1, active_max + 1):
        weight = atom_weight(a, x, n)
        if MU[n] == 1 and n <= threshold + displacement:
            value += weight
        elif MU[n] == -1 and n <= threshold:
            value -= weight
    return value


def least_prime_recursion_replay(limit: int = 500) -> dict:
    # Verify coefficient-wise that every squarefree n>1 has one unique least
    # prime p and a squarefree remainder with all prime factors greater than p.
    checked = 0
    parity_toggles = 0
    for n in range(2, limit + 1):
        if MU[n] == 0:
            continue
        factors = [p for p in PRIMES if p <= n and n % p == 0]
        least = factors[0]
        remainder = n // least
        if remainder > 1:
            remainder_factors = [p for p in PRIMES if p <= remainder and remainder % p == 0]
            assert remainder_factors[0] > least
        assert MU[n] == -MU[remainder]
        checked += 1
        parity_toggles += 1
    return {
        "squarefree_states_checked": checked,
        "unique_least_prime_toggles": parity_toggles,
        "limit": limit,
    }


def main() -> None:
    minimum_reserve = None
    minimum_equality = None

    # On each cell N <= x < N+1, active support is fixed and every Hall margin
    # is affine in sqrt(x). Therefore endpoint checks certify the whole cell.
    for active_max in range(1, 55):
        right = Fraction(active_max + 1) if active_max < 54 else WINDOW_X_MAX
        odd_thresholds = [
            n for n in range(1, active_max + 1) if MU[n] == -1
        ]
        for threshold in odd_thresholds:
            for x in (Fraction(active_max), right):
                reserve = hall_margin(
                    a=1,
                    displacement=0,
                    active_max=active_max,
                    threshold=threshold,
                    x=x,
                )
                equality = hall_margin(
                    a=2,
                    displacement=1,
                    active_max=active_max,
                    threshold=threshold,
                    x=x,
                )
                assert reserve.lo > Fraction(39, 100), (
                    active_max,
                    threshold,
                    x,
                    reserve,
                )
                assert equality.lo > Fraction(11, 100), (
                    active_max,
                    threshold,
                    x,
                    equality,
                )

                reserve_record = (
                    reserve.lo,
                    active_max,
                    threshold,
                    x,
                )
                equality_record = (
                    equality.lo,
                    active_max,
                    threshold,
                    x,
                )
                if minimum_reserve is None or reserve_record[0] < minimum_reserve[0]:
                    minimum_reserve = reserve_record
                if minimum_equality is None or equality_record[0] < minimum_equality[0]:
                    minimum_equality = equality_record

    even_squarefree = [n for n in range(1, 55) if MU[n] == 1]
    odd_squarefree = [n for n in range(1, 55) if MU[n] == -1]
    primes_through_53 = [p for p in PRIMES if p <= 53]
    assert len(primes_through_53) == 16
    assert PRIMES[len(primes_through_53)] == 59
    assert Fraction(1, 59) < ROOT_LO

    recursion = least_prime_recursion_replay()

    assert minimum_reserve is not None
    assert minimum_equality is not None
    result = {
        "classification": "PASS_FACTOR54_POSITIVE_PARITY_SHADOW",
        "reset_root_bracket": [str(ROOT_LO), str(ROOT_HI)],
        "next_prime_contraction": {
            "next_prime": 59,
            "one_over_59": float(Fraction(1, 59)),
            "root_lower": float(ROOT_LO),
            "strict": True,
        },
        "primes_through_53": primes_through_53,
        "even_squarefree_states": even_squarefree,
        "odd_squarefree_states": odd_squarefree,
        "reserve_hall_minimum": {
            "lower": float(minimum_reserve[0]),
            "cell_N": minimum_reserve[1],
            "threshold": minimum_reserve[2],
            "x": float(minimum_reserve[3]),
            "certified_above": 0.39,
            "support": "e <= o",
        },
        "equality_hall_minimum": {
            "lower": float(minimum_equality[0]),
            "cell_N": minimum_equality[1],
            "threshold": minimum_equality[2],
            "x": float(minimum_equality[3]),
            "certified_above": 0.11,
            "support": "e <= o+1",
        },
        "least_prime_recursion": recursion,
        "scope": (
            "All asserted Hall inequalities use exact Fraction arithmetic and "
            "directed rational square-root enclosures. Decimal fields are "
            "readable summaries only."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
