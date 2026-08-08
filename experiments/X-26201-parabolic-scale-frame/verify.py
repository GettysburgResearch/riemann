#!/usr/bin/env python3
"""Proof-facing checks for the parabolic endpoint-scale frame.

Exact layer:
  * rational enclosures for K_16 < -1/2;
  * rational interval proof that H_N' > 7/25 on cells N=2,...,14.

Reconnaissance layer:
  * high-precision Decimal checks of actual endpoint atoms and scale greedy.

The reconnaissance output is not an asymptotic proof.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path

getcontext().prec = 70


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("invalid interval")

    @staticmethod
    def point(x: int | Fraction) -> "Interval":
        value = Fraction(x)
        return Interval(value, value)

    def __add__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        return Interval(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        return self + (-rhs)

    def __rsub__(self, other: object) -> "Interval":
        return Interval.point(Fraction(other)) - self

    def __mul__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        values = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return Interval(Fraction(1, 1) / self.hi, Fraction(1, 1) / self.lo)

    def __truediv__(self, other: object) -> "Interval":
        rhs = other if isinstance(other, Interval) else Interval.point(Fraction(other))
        return self * rhs.reciprocal()


SQRT_SCALE = 10**75


def sqrt_fraction_interval(value: Fraction) -> Interval:
    if value < 0:
        raise ValueError("negative square root")
    if value == 0:
        return Interval.point(0)
    scaled_floor = (value.numerator * SQRT_SCALE * SQRT_SCALE) // value.denominator
    k = isqrt(scaled_floor)
    while Fraction((k + 1) ** 2, SQRT_SCALE**2) <= value:
        k += 1
    while Fraction(k**2, SQRT_SCALE**2) > value:
        k -= 1
    return Interval(Fraction(k, SQRT_SCALE), Fraction(k + 1, SQRT_SCALE))


def log_unit_interval(value: Fraction, terms: int = 140) -> Interval:
    if not Fraction(1) <= value <= Fraction(2):
        raise ValueError("range reduction failure")
    z = (value - 1) / (value + 1)
    power = z
    partial = Fraction(0)
    for j in range(terms + 1):
        if j:
            power *= z * z
        partial += power / (2 * j + 1)
    lower = 2 * partial
    remainder = (
        2
        * z ** (2 * terms + 3)
        / (2 * terms + 3)
        / (1 - z * z)
    )
    return Interval(lower, lower + remainder)


LOG_TWO = log_unit_interval(Fraction(2))


def log_fraction_interval(value: Fraction) -> Interval:
    if value <= 0:
        raise ValueError("log argument must be positive")
    if value == 1:
        return Interval.point(0)
    if value < 1:
        return -log_fraction_interval(1 / value)
    reduced = value
    exponent = 0
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    return log_unit_interval(reduced) + exponent * LOG_TWO


def sa_intervals(n: int) -> tuple[Interval, Interval]:
    s = Interval.point(0)
    a = Interval.point(0)
    for k in range(1, n + 1):
        inverse_sqrt = sqrt_fraction_interval(Fraction(k)).reciprocal()
        s += inverse_sqrt
        a += inverse_sqrt * log_fraction_interval(Fraction(k))
    return s, a


def hprime_interval(n: int, left: Fraction, right: Fraction) -> Interval:
    s, a = sa_intervals(n)
    log_theta = Interval(
        log_fraction_interval(left).lo,
        log_fraction_interval(right).hi,
    )
    sqrt_theta = Interval(
        sqrt_fraction_interval(left).lo,
        sqrt_fraction_interval(right).hi,
    )
    q = a + 4 * s + (s + 1) * log_theta
    return Interval.point(4 * n) - q * sqrt_theta.reciprocal()


def exact_tail_gates() -> dict[str, object]:
    s16, a16 = sa_intervals(16)
    k16 = (s16 + 1) * log_fraction_interval(Fraction(16)) - a16 - 2 * s16 + 2
    if not k16.hi < Fraction(-1, 2):
        raise AssertionError("K_16 gate failed")

    lower_bounds: dict[str, str] = {}
    threshold = Fraction(7, 25)
    pieces = 64
    for n in range(2, 15):
        left = Fraction(1, n + 1)
        right = Fraction(1, n)
        best: Fraction | None = None
        for i in range(pieces):
            a = left + (right - left) * Fraction(i, pieces)
            b = left + (right - left) * Fraction(i + 1, pieces)
            interval = hprime_interval(n, a, b)
            if interval.lo <= threshold:
                raise AssertionError((n, i, interval.lo, threshold))
            if best is None or interval.lo < best:
                best = interval.lo
        assert best is not None
        lower_bounds[str(n)] = format(float(best), ".18g")

    return {
        "arithmetic": "EXACT_RATIONAL_INTERVAL",
        "K16_upper_decimal": format(float(k16.hi), ".18g"),
        "K16_less_than_minus_half": True,
        "cell_derivative_threshold": str(threshold),
        "cell_derivative_lower_bounds": lower_bounds,
    }


def dec(value: int | str | Decimal) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(value)


def b_seed(endpoint: int, m: int) -> Decimal:
    if m < 2 or m > endpoint:
        return Decimal(0)
    x = dec(m)
    y = dec(endpoint)
    return 2 * x.sqrt() * ((y / x).ln() - 2 * (1 - (x / y).sqrt()))


def d_seed(endpoint: int, max_endpoint: int) -> list[Decimal]:
    a = [Decimal(0)] * (max_endpoint + 3)
    for m in range(2, endpoint + 1):
        a[m] = b_seed(endpoint, m) / dec(m - 1)
    d = [Decimal(0)] * (max_endpoint + 1)
    for n in range(2, endpoint + 1):
        d[n] = dec(n + 1) * (a[n] - 2 * a[n + 1] + a[n + 2])
    return d


def beta(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    p = 2
    while p * p <= limit:
        if sieve[p]:
            start = p * p
            count = (limit - start) // p + 1
            sieve[start : limit + 1 : p] = b"\x00" * count
        p += 1
    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_power_lambda(limit: int) -> dict[int, Decimal]:
    result: dict[int, Decimal] = {}
    for p in primes_up_to(limit):
        q = p
        lp = dec(p).ln()
        while q <= limit:
            result[q] = lp
            if q > limit // p:
                break
            q *= p
    return result


def scale_greedy(endpoint: int) -> dict[str, object]:
    residual = [Decimal(0)] * (endpoint + 1)
    x = dec(endpoint)
    for q in range(2, endpoint + 1):
        residual[q] = (x / dec(q)).ln() / dec(q).sqrt()

    off_diagonal: list[dict[str, object]] = []
    maximum_loss = Decimal(0)
    minimum_atom = Decimal("Infinity")

    previous = [Decimal(0)] * (endpoint + 1)
    atoms: dict[int, list[Decimal]] = {}
    for t in range(2, endpoint + 1):
        current = d_seed(t, endpoint)
        if t >= 3:
            atom = [current[i] - previous[i] for i in range(endpoint + 1)]
            for n in range(2, t):
                minimum_atom = min(minimum_atom, atom[n])
                if atom[n] <= Decimal(0):
                    raise AssertionError((endpoint, t, n, atom[n]))
            atoms[t] = atom
        previous = current

    final_weights: dict[int, Decimal] = {}
    diagonal_losses: dict[int, Decimal] = {}
    for t in range(endpoint, 2, -1):
        atom = atoms[t]
        gamma = [Decimal(0)] * t
        for q in range(2, t):
            total = Decimal(0)
            for n in range(q, t):
                coefficient = beta(n, q)
                if coefficient:
                    total += atom[n] * dec(coefficient.numerator) / dec(coefficient.denominator)
            if total <= 0:
                raise AssertionError((endpoint, t, q, total))
            gamma[q] = total

        blocker = min(range(2, t), key=lambda q: residual[q] / gamma[q])
        weight = residual[blocker] / gamma[blocker]
        diagonal_candidate = residual[t - 1] / gamma[t - 1]
        loss = diagonal_candidate - weight
        if loss < Decimal(-1).scaleb(-55):
            raise AssertionError((endpoint, t, loss))
        if loss < 0:
            loss = Decimal(0)
        maximum_loss = max(maximum_loss, loss)
        final_weights[t] = weight
        diagonal_losses[t] = loss
        if blocker != t - 1 and weight > Decimal(1).scaleb(-50):
            off_diagonal.append(
                {
                    "T": t,
                    "blocker": blocker,
                    "weight": str(weight),
                    "loss": str(loss),
                }
            )
        for q in range(2, t):
            residual[q] -= weight * gamma[q]
            if residual[q] < 0 and residual[q] > -Decimal(1).scaleb(-50):
                residual[q] = Decimal(0)
            if residual[q] < 0:
                raise AssertionError((endpoint, t, q, residual[q]))

    total_slack = sum(residual[2:], Decimal(0))
    lambdas = prime_power_lambda(endpoint)
    weighted_gap = sum((weight * residual[q] for q, weight in lambdas.items()), Decimal(0))
    max_scaled_loss = max(
        (diagonal_losses[t] / dec(t).sqrt() for t in diagonal_losses),
        default=Decimal(0),
    )
    return {
        "X": endpoint,
        "minimum_positive_endpoint_atom": str(minimum_atom),
        "total_scale_slack": str(total_slack),
        "prime_power_weighted_gap": str(weighted_gap),
        "off_diagonal_blockers": off_diagonal,
        "off_diagonal_blocker_count": len(off_diagonal),
        "maximum_blocker_loss": str(maximum_loss),
        "maximum_loss_over_sqrt_T": str(max_scaled_loss),
        "maximum_scale_weight": str(max(final_weights.values(), default=Decimal(0))),
    }


def main() -> None:
    exact = exact_tail_gates()
    reconnaissance = [scale_greedy(x) for x in (64, 128, 256)]
    payload: dict[str, object] = {
        "schema": "riemann.x26201-parabolic-scale-frame.v1",
        "exact_tail_majorization_gates": exact,
        "scale_frame_reconnaissance": {
            "classification": "HIGH_PRECISION_DECIMAL_RECONNAISSANCE",
            "scope": "Finite endpoint atoms and scale-greedy behavior only; no asymptotic theorem.",
            "instances": reconnaissance,
        },
    }
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    output = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    result_path = Path(__file__).with_name("results") / "verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
