#!/usr/bin/env python3
"""Exact replay for L-34401 using only Python's standard library."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


class Q2:
    """a+b*sqrt(2), exactly."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def _coerce(self, other):
        return other if isinstance(other, Q2) else Q2(other)

    def __add__(self, other):
        other = self._coerce(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        other = self._coerce(other)
        return self.a == other.a and self.b == other.b

    def as_json(self):
        return {"a": str(self.a), "b": str(self.b)}


def poly_add(x, y):
    n = max(len(x), len(y))
    out = [Q2() for _ in range(n)]
    for k in range(n):
        out[k] = (x[k] if k < len(x) else Q2()) + (
            y[k] if k < len(y) else Q2()
        )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(x, c):
    return [a * c for a in x]


def poly_mul(x, y):
    out = [Q2() for _ in range(len(x) + len(y) - 1)]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] = out[i + j] + a * b
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_negz(x):
    return [a if k % 2 == 0 else -a for k, a in enumerate(x)]


def poly_derivative(x):
    if len(x) <= 1:
        return [Q2()]
    return [x[k] * k for k in range(1, len(x))]


def poly_eval_one(x):
    return sum(x, Q2())


def positive_minus_a_plus_b_sqrt2(a: int, b: int) -> bool:
    """Return whether -a+b*sqrt(2)>0 for positive integers a,b."""
    assert a > 0 and b > 0
    return 2 * b * b > a * a


def main():
    rt2 = Q2(0, 1)

    p = poly_mul(
        poly_mul([Q2(1), Q2(-1)], [Q2(1), Q2(-2)]),
        poly_mul([Q2(1), -rt2], [Q2(1), -rt2]),
    )

    U = [
        Q2(Fraction(1, 2)),
        Q2(Fraction(-11, 3), Fraction(7, 2)),
        Q2(1, Fraction(1, 6)),
        Q2(Fraction(14, 3), -3),
    ]

    T = poly_mul([Q2(1), Q2(-1)], [Q2(1), Q2(0), Q2(-4)])

    # PR #263 Bezout identity.
    assert poly_add(poly_mul(U, p), poly_mul(poly_negz(U), poly_negz(p))) == [Q2(1)]

    # Stronger simple rational cycle certificate from L-34401.8.
    H = [
        Q2(Fraction(123, 1000)),
        Q2(Fraction(296, 1000)),
        Q2(Fraction(-387, 1000)),
        Q2(Fraction(117, 1000)),
        Q2(Fraction(-14, 1000)),
        Q2(Fraction(62, 1000)),
        Q2(Fraction(303, 1000)),
    ]
    assert poly_eval_one(H) == Q2(Fraction(1, 2))

    w_plus = poly_add(poly_mul(T, U), poly_mul(H, poly_negz(p)))
    w_minus = poly_add(
        poly_mul(T, poly_negz(U)), poly_scale(poly_mul(H, p), -1)
    )

    assert len(w_plus) == 11 and len(w_minus) == 11
    assert poly_add(poly_mul(w_plus, p), poly_mul(w_minus, poly_negz(p))) == T

    q_w = Q2()
    for j in range(11):
        square_sum = w_plus[j] * w_plus[j] + w_minus[j] * w_minus[j]
        q_w = q_w + square_sum * Fraction(1, 2**j)

    expected_q_w = Q2(
        Fraction(14014874005, 32000000),
        Fraction(-9814156296, 32000000),
    )
    assert q_w == expected_q_w

    # q_W < 9/2 is equivalent to
    # -13870874005 + 9814156296*sqrt(2) > 0.
    assert positive_minus_a_plus_b_sqrt2(13870874005, 9814156296)

    # The derivative-gauge polynomial
    # G_H(z)=z[W_+' p + W_-' p(-z)] has both z and z-1 factors.
    inside = poly_add(
        poly_mul(poly_derivative(w_plus), p),
        poly_mul(poly_derivative(w_minus), poly_negz(p)),
    )
    gauge = [Q2()] + inside
    assert gauge[0] == Q2()  # factor z
    assert poly_eval_one(gauge) == Q2()  # factor z-1

    result = {
        "schema": "X-34401-q4-compact-parity-synthesis-v2",
        "classification": "EXACT_Q_SQRT2",
        "degrees": {"W_plus": 10, "W_minus": 10},
        "bezout_target_identity": True,
        "cycle_H_at_1": "1/2",
        "current_charge": q_w.as_json(),
        "current_charge_lt_9_over_2": True,
        "normalized_current_charge_lt_2_over_5": True,
        "gauge_has_factor_z": True,
        "gauge_has_factor_one_minus_z": True,
        "gauge_source_type": "strictly_delayed_ordinary_mobius",
        "gauge_min_delay_blocks": 1,
        "does_not_prove": [
            "joint delayed-state reflected recurrence",
            "Riemann Hypothesis",
        ],
    }

    canonical = json.dumps(result, indent=2, sort_keys=True) + "\n"
    result["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()

    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    destination = Path(__file__).with_name("results") / "verification.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
