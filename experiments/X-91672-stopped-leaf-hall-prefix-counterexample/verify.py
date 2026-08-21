#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.pr455.stopped-leaf-hall-prefix-counterexample.v1"


class Interval:
    """Closed rational interval with exact outward arithmetic."""

    __slots__ = ("lo", "hi")

    def __init__(self, lo: Fraction | int, hi: Fraction | int | None = None) -> None:
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("invalid interval")

    @staticmethod
    def coerce(value: "Interval | Fraction | int") -> "Interval":
        return value if isinstance(value, Interval) else Interval(value)

    def __add__(self, other: "Interval | Fraction | int") -> "Interval":
        rhs = self.coerce(other)
        return Interval(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: "Interval | Fraction | int") -> "Interval":
        return self + (-self.coerce(other))

    def __rsub__(self, other: "Interval | Fraction | int") -> "Interval":
        return self.coerce(other) - self

    def __mul__(self, other: "Interval | Fraction | int") -> "Interval":
        rhs = self.coerce(other)
        products = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        values = (1 / self.lo, 1 / self.hi)
        return Interval(min(values), max(values))

    def __truediv__(self, other: "Interval | Fraction | int") -> "Interval":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: "Interval | Fraction | int") -> "Interval":
        return self.coerce(other) / self


def decimal(value: Fraction, digits: int = 30) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    whole, rem = divmod(value.numerator, value.denominator)
    out: list[str] = []
    for _ in range(digits):
        rem *= 10
        digit, rem = divmod(rem, value.denominator)
        out.append(str(digit))
    return f"{sign}{whole}." + "".join(out)


def interval_json(value: Interval) -> dict[str, str]:
    return {"lower": decimal(value.lo), "upper": decimal(value.hi)}


def sqrt_interval(n: int, digits: int = 72) -> Interval:
    if n < 0:
        raise ValueError("sqrt of negative integer")
    scale = 10**digits
    q = math.isqrt(n * scale * scale)
    lo = Fraction(q, scale)
    if q * q == n * scale * scale:
        return Interval(lo)
    return Interval(lo, Fraction(q + 1, scale))


def inv_sqrt_interval(n: int) -> Interval:
    return sqrt_interval(n).reciprocal()


def mobius_upto(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def log_unit_interval(y: Fraction, terms: int = 110) -> Interval:
    if not Fraction(1) <= y <= Fraction(2):
        raise ValueError("log unit reduction failed")
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lo = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lo, lo + tail)


LN2 = log_unit_interval(Fraction(2), 130)


def floor_log2_fraction(x: Fraction) -> int:
    if x < 1:
        raise ValueError("expected x >= 1")
    k = max(0, x.numerator.bit_length() - x.denominator.bit_length())
    while Fraction(1 << (k + 1)) <= x:
        k += 1
    while Fraction(1 << k) > x:
        k -= 1
    return k


def log_interval(x: Fraction) -> Interval:
    if x <= 0:
        raise ValueError("log requires positive input")
    if x == 1:
        return Interval(0)
    if x < 1:
        return -log_interval(1 / x)
    k = floor_log2_fraction(x)
    unit = x / Fraction(1 << k)
    return log_unit_interval(unit) + k * LN2


def h_interval(Y: int, m: int) -> Interval:
    if m > Y:
        return Interval(0)
    return log_interval(Fraction(Y, m)) * inv_sqrt_interval(m)


def component_log_coefficient(j: int, N: int) -> Interval:
    out = Fraction(j + 1, j - 1) * inv_sqrt_interval(j)
    if N >= j + 1:
        out += -Fraction((j + 1) * (j - 2), j * (j - 1)) * inv_sqrt_interval(j + 1)
    if N >= j + 2:
        for m in range(j + 2, N + 1):
            out += Fraction(2, j * (j - 1)) * inv_sqrt_interval(m)
    return out


def component_row_interval(Y: int, j: int) -> Interval:
    h_j = h_interval(Y, j)
    h_j1 = h_interval(Y, j + 1)
    tail = Interval(0)
    for m in range(j + 2, Y + 1):
        tail += h_interval(Y, m)
    return (
        Fraction(j + 1, j - 1) * (h_j - h_j1)
        + Fraction(2 * (j + 1), j * (j - 1)) * h_j1
        + Fraction(2, j * (j - 1)) * tail
    )


def verify() -> dict[str, Any]:
    mu = mobius_upto(13)

    # Admissible stopped leaf in L-91621/L-91560.
    p = 67
    y = 13
    X = p * y
    threshold = 13

    A13 = sum((Fraction(mu[n], n) for n in range(1, threshold + 1)), Fraction(0))
    assert A13 == Fraction(-2323, 30030)

    B13 = Interval(0)
    for n in range(1, threshold + 1):
        if mu[n]:
            B13 += mu[n] * inv_sqrt_interval(n)

    r = inv_sqrt_interval(p)
    alpha_s = 2 * (r + 2) / (r + 3)
    g_s = (1 - r) * (r + 3)
    assert g_s.lo > 0

    # Necessary no-upward Hall prefix in the survival target channel.
    H_s = alpha_s * sqrt_interval(X) * A13 - B13
    assert H_s.hi < -2
    physical_H_s = g_s * H_s
    assert physical_H_s.hi < 0

    # Since alpha_s > 4/3, A13 < 0, and sqrt(13p) is increasing, this
    # conservative p=67 bound proves failure for every prime p >= 67 at y=13.
    family_upper_bound = Fraction(4, 3) * sqrt_interval(X) * A13 - B13
    assert family_upper_bound.hi < -2

    # L-91670 promotes the finite-window M_1 > 1/20 certificate to all cells.
    # The following right endpoint disproves that numerical promotion, while
    # remaining positive and therefore not refuting monotonicity itself.
    N = 71
    j = 70
    Y = N + 1
    C = component_log_coefficient(j, N)
    Q = component_row_interval(Y, j)
    M1 = sqrt_interval(Y) * (2 * C - Q) - 2 * C
    assert M1.lo > 0
    assert M1.hi < Fraction(1, 20)

    core = {
        "frozen_target": {
            "proposal_pr": 455,
            "proposal_head": "1b502acbe511776178da3dc916e3cd3464cd5e77",
            "normative_content_commit": "c696d2a356eeacb3097d4ea6cc727b84548d7a03",
        },
        "stopped_leaf": {
            "p": p,
            "y": y,
            "parent_endpoint_X_equals_p_times_y": X,
            "active_prefix_threshold": threshold,
            "A13": str(A13),
            "B13": interval_json(B13),
            "survival_alpha": interval_json(alpha_s),
            "unscaled_survival_prefix_margin": interval_json(H_s),
            "physical_survival_prefix_margin": interval_json(physical_H_s),
            "conservative_all_p_ge_67_upper_bound": interval_json(family_upper_bound),
            "unscaled_margin_lt_minus_2": True,
            "failure_for_every_prime_p_ge_67_at_y_13": True,
            "no_upward_survival_target_hall_transport_exists": False,
        },
        "promoted_row_margin": {
            "cell_N": N,
            "row_j": j,
            "right_endpoint_Y": Y,
            "M1": interval_json(M1),
            "M1_positive": True,
            "M1_lt_1_over_20": True,
            "note": "This refutes the promoted global 1/20 margin, not global monotonicity itself.",
        },
        "scope": {
            "single_sharp_atom_identity_refuted": False,
            "finite_seed_fubini_identity_refuted": False,
            "stopped_leaf_hall_entry_refuted_as_stated": True,
            "T91656_conclusion_survives_this_reconstruction": False,
            "riemann_hypothesis_established": False,
        },
    }
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "schema": SCHEMA,
        "classification": "PASS_PR455_STOPPED_LEAF_HALL_PREFIX_COUNTEREXAMPLE",
        "proof_object_sha256": digest,
        "core": core,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
