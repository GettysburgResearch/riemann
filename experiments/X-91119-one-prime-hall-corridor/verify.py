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
        other = as_i(other); return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-as_i(other))
    def __rsub__(self, other): return as_i(other) - self
    def __mul__(self, other):
        other = as_i(other)
        vals = [self.lo*other.lo, self.lo*other.hi,
                self.hi*other.lo, self.hi*other.hi]
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

DEN = 10**80

def sqrt_q(value: Fraction | int) -> I:
    value = Fraction(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    return I(Fraction(root, DEN), Fraction(root + 1, DEN))


def mobius_sieve(limit: int) -> list[int]:
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
            least[prime*n] = prime
            if n % prime == 0:
                mu[prime*n] = 0
                break
            mu[prime*n] = -mu[n]
    return mu

MU = mobius_sieve(54)
ROOT_LO = Fraction(1844367547103, 10**14)
WINDOW_X_MAX = 1 / ROOT_LO
R67 = 1 / sqrt_q(67)


def atom_weight(a: I, x: Fraction, n: int) -> I:
    return a * sqrt_q(x) / n - 1 / sqrt_q(n)


def hall_margin(*, a: I, displacement: int, active_max: int,
                threshold: int, x: Fraction) -> I:
    value = I(Fraction(0), Fraction(0))
    for n in range(1, active_max + 1):
        weight = atom_weight(a, x, n)
        if MU[n] == 1 and n <= threshold + displacement:
            value += weight
        elif MU[n] == -1 and n <= threshold:
            value -= weight
    return value


def scan(channel: str, a_values: list[I], displacement: int,
         certified: Fraction) -> dict:
    minimum = None
    checks = 0
    for active_max in range(1, 55):
        right = Fraction(active_max + 1) if active_max < 54 else WINDOW_X_MAX
        odd_thresholds = [n for n in range(1, active_max + 1) if MU[n] == -1]
        for threshold in odd_thresholds:
            for x in (Fraction(active_max), right):
                for endpoint, a in enumerate(a_values):
                    value = hall_margin(a=a, displacement=displacement,
                                        active_max=active_max,
                                        threshold=threshold, x=x)
                    checks += 1
                    assert value.lo > certified, (
                        channel, active_max, threshold, x, endpoint, value
                    )
                    record = (value.lo, active_max, threshold, x, endpoint)
                    if minimum is None or record[0] < minimum[0]:
                        minimum = record
    assert minimum is not None
    return {
        "checks": checks,
        "minimum_lower_decimal": float(minimum[0]),
        "cell_N": minimum[1],
        "threshold": minimum[2],
        "x": float(minimum[3]),
        "parameter_endpoint": minimum[4],
        "certified_above": str(certified),
    }


def main() -> None:
    reserve_parameters = [as_i(1), 1 + R67]
    equality_parameters = [as_i(2), 2 * (1 + R67)]

    reserve = scan("reserve", reserve_parameters, 0, Fraction(8, 25))
    equality = scan("equality", equality_parameters, 1, Fraction(1, 400))

    result = {
        "classification": "PASS_ONE_ROUGH_PRIME_HALL_CORRIDOR",
        "rough_prime_floor": 67,
        "reserve_parameter_interval": ["1", "1+1/sqrt(67)"],
        "equality_parameter_interval": ["2", "2(1+1/sqrt(67))"],
        "reserve_support": "e <= o",
        "equality_support": "e <= o+1",
        "reserve": reserve,
        "equality": equality,
        "scope": (
            "Directed Fraction/square-root intervals certify both parameter "
            "endpoints on every reset cell and threshold. Hall margins are "
            "affine in the parameter, so the complete intervals follow. This "
            "is a one-new-prime reset-boundary theorem, not multiprime scalar "
            "tensorization."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
