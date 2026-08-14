#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt, log, sqrt
from pathlib import Path
import hashlib
import json
import random

DEN = 10**55
TERMS = 180


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
        assert not (other.lo <= 0 <= other.hi)
        return self * I(1 / other.hi, 1 / other.lo)
    def __rtruediv__(self, other):
        return as_i(other) / self


def as_i(x) -> I:
    if isinstance(x, I):
        return x
    return I(Fraction(x), Fraction(x))


def sqrt_fraction_i(x: Fraction) -> I:
    assert x >= 0
    scaled_floor = (x.numerator * DEN * DEN) // x.denominator
    q = isqrt(scaled_floor)
    lo = Fraction(q, DEN)
    hi = lo if lo * lo == x else Fraction(q + 1, DEN)
    return I(lo, hi)


def invsqrt_i(n: int) -> I:
    return 1 / sqrt_fraction_i(Fraction(n))


def log_i(x: Fraction) -> I:
    assert x > 0
    exponent = 0
    y = x
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1

    def base(z: Fraction) -> I:
        z2 = z * z
        power = z
        partial = Fraction(0)
        for k in range(TERMS):
            partial += power / (2 * k + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / ((2 * TERMS + 1) * (1 - z2))
        return I(partial, partial + tail)

    return base((y - 1) / (y + 1)) + exponent * base(Fraction(1, 3))


def gamma_i(j: int, m: int) -> I:
    if m == j:
        return Fraction(j + 1, j - 1) * invsqrt_i(j)
    if m == j + 1:
        return -Fraction((j + 1) * (j - 2), j * (j - 1)) * invsqrt_i(j + 1)
    if m >= j + 2:
        return Fraction(2, j * (j - 1)) * invsqrt_i(m)
    return I(Fraction(0), Fraction(0))


def q_cell(j: int, N: int, Y: Fraction) -> tuple[I, I, I]:
    C = I(Fraction(0), Fraction(0))
    D = I(Fraction(0), Fraction(0))
    for m in range(j, N + 1):
        g = gamma_i(j, m)
        C += g
        D += g * log_i(Fraction(m))
    Q = C * log_i(Y) - D
    return Q, C, D


def shell_monotonicity_counterexample() -> dict:
    p = 67
    j = 5
    z = Fraction(201, 40)
    Yp = p * z
    Qp, Cp, _ = q_cell(j, int(Yp), Yp)
    Qc, Cc, _ = q_cell(j, int(z), z)
    numerator = (Cp - Cc) - Fraction(1, 2) * (Qp - Qc)
    denominator = 5 * (sqrt_fraction_i(Fraction(p)) - 1) * sqrt_fraction_i(z)
    derivative = numerator / denominator
    assert numerator.hi < Fraction(-3218, 100000)
    assert derivative.hi < Fraction(-1, 4000)
    return {
        "p": p,
        "j": j,
        "z": str(z),
        "numerator_upper": float(numerator.hi),
        "derivative_upper": float(derivative.hi),
        "certified_below": "-1/4000",
    }


def last_shell_weights(primes: list[int]) -> int:
    rs = [Fraction(1, p) for p in primes]  # algebra works for arbitrary r in (0,1)
    omega0 = Fraction(1)
    for r in rs:
        omega0 *= 1 - r
    weights = []
    for i, r in enumerate(rs):
        tail = Fraction(1)
        for rr in rs[i + 1:]:
            tail *= 1 - rr
        weights.append(r * tail)
    assert omega0 + sum(weights, Fraction(0)) == 1
    return len(weights) + 1


def shell_firewall_checks(limit: int = 400) -> int:
    # Verify the exact divisor-support statement behind R-91314.
    def sieve_mu(n: int) -> list[int]:
        mu = [0] * (n + 1)
        mu[1] = 1
        primes: list[int] = []
        lp = [0] * (n + 1)
        for i in range(2, n + 1):
            if lp[i] == 0:
                lp[i] = i
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if p > lp[i] or i * p > n:
                    break
                lp[i * p] = p
                mu[i * p] = 0 if p == lp[i] else -mu[i]
        return mu

    mu = sieve_mu(limit)
    primes = [p for p in range(2, 2000)
              if all(p % q for q in range(2, isqrt(p) + 1))]
    checks = 0
    rng = random.Random(91314)
    for _ in range(500):
        j = rng.randint(2, 40)
        X = rng.randint(j, limit * j)
        ratio = X // j
        p = next(q for q in primes if q > ratio)
        assert X / p < j
        for d in range(1, ratio + 1):
            if mu[d] == 0:
                continue
            # Every prime factor of squarefree d is below p.
            n = d
            f = 2
            while f * f <= n:
                if n % f == 0:
                    assert f < p
                    n //= f
                f += 1
            if n > 1:
                assert n < p
            checks += 1
    return checks


def positive_shell_density_checks() -> int:
    # Finite regression of the coefficientwise formulas in L-91382.
    primes = [2, 3, 5, 7, 11]
    checks = 0
    for p in [13, 17, 19]:
        for Z in range(1, 300):
            rough = [n for n in range(1, Z + 1)
                     if all(n % q for q in primes)]
            K = 0.0
            for n in rough:
                if n <= Z / p:
                    K += log(p) / sqrt(n)
                else:
                    K += log(Z / n) / sqrt(n)
            assert K >= -1e-14
            checks += 1
    return checks


def entropy_bound_checks() -> int:
    checks = 0
    for Y in range(1, 5000):
        E = sum(log(n) / sqrt(n) * log(Y / n) for n in range(2, Y + 1))
        T = 4 * sqrt(Y) - 3
        assert E <= 4 * T * log(3 * Y) + 1e-10
        checks += 1
    return checks


def main() -> None:
    result = {
        "classification": "PASS_EULER_SHELL_RECOVERY_AND_FIREWALL",
        "last_shell_weight_checks": sum(
            last_shell_weights(seq)
            for seq in ([2, 3], [2, 3, 5, 7], [67, 71, 73, 79, 83])
        ),
        "shell_firewall_factor_checks": shell_firewall_checks(),
        "positive_shell_density_checks": positive_shell_density_checks(),
        "entropy_bound_checks": entropy_bound_checks(),
        "normalized_shell_monotonicity_counterexample": shell_monotonicity_counterexample(),
        "scope": (
            "The replay certifies the algebraic convexification, last-shell "
            "weights, the native-row-hard shell firewall, representative "
            "positive shell-density formulas, the elementary entropy bound, "
            "and a directed monotonicity counterexample. It does not prove "
            "Hereditary Typed Entry, CFFP, or RH."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
