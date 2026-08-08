#!/usr/bin/env python3
"""Exact finite replay for the critical-mode-null source package.

Uses only the Python standard library and exact Fraction arithmetic in Q(sqrt(2)).
The checker authenticates finite algebra. It does not prove a cofinal source
estimate or RH.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Q2) else Q2(Fraction(x), Fraction(0))

    def __add__(self, other):
        other = self.coerce(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Q2(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def text(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"({self.b})*sqrt(2)"
        return f"{self.a}+({self.b})*sqrt(2)"


ONE = Q2(1)
SQRT2 = Q2(0, 1)


def poly_mul(p, q):
    out = [Q2() for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = out[i + j] + a * b
    return out


def poly_eval(p, x):
    out = Q2()
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def product_poly(constants):
    p = [ONE]
    for c in constants:
        p = poly_mul(p, [ONE, -c])
    return p


def mobius_sieve(limit):
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for prime in primes:
            value = n * prime
            if value > limit:
                break
            composite[value] = True
            if n % prime == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]
    return mu


MU = mobius_sieve(512)


def source(n, polynomial):
    out = Q2()
    for j, coefficient in enumerate(polynomial):
        scale = 1 << j
        if n % scale == 0:
            out = out + coefficient * MU[n // scale]
    return out


def beta(n, q):
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def carry_image(n, polynomial):
    out = Q2()
    for q in range(2, n + 1):
        out = out + source(q, polynomial) * beta(n, q)
    return out


def check_polynomials():
    p_omega = product_poly([Q2(1), Q2(Fraction(1, 2))])
    p_dagger = product_poly([Q2(1), Q2(Fraction(1, 2)), SQRT2])
    p_box = product_poly(
        [Q2(1), Q2(Fraction(1, 2)), Q2(2), SQRT2, SQRT2]
    )

    assert p_dagger == poly_mul(p_omega, [ONE, -SQRT2])
    assert poly_eval(p_dagger, Q2(1)).is_zero()
    assert poly_eval(p_dagger, Q2(2)).is_zero()
    assert poly_eval(p_dagger, Q2(0, Fraction(1, 2))).is_zero()

    assert poly_eval(p_box, Q2(1)).is_zero()
    assert poly_eval(p_box, Q2(2)).is_zero()
    assert poly_eval(p_box, Q2(Fraction(1, 2))).is_zero()
    critical = Q2(0, Fraction(1, 2))
    assert poly_eval(p_box, critical).is_zero()

    expected_box = [
        Q2(1),
        Q2(Fraction(-7, 2), -2),
        Q2(Fraction(11, 2), 7),
        Q2(-8, -7),
        Q2(7, 2),
        Q2(-2),
    ]
    assert p_box == expected_box

    return p_omega, p_dagger, p_box


def check_dagger_rows(p_dagger):
    expected = {
        2: Q2(Fraction(-5, 6), Fraction(-1, 3)),
        3: Q2(Fraction(-1, 2)),
        4: Q2(0, Fraction(11, 10)),
        5: Q2(0, Fraction(5, 6)),
        6: Q2(0, Fraction(9, 14)),
        7: Q2(0, Fraction(1, 2)),
    }
    for n, value in expected.items():
        assert carry_image(n, p_dagger) == value
    for n in range(8, 129):
        assert carry_image(n, p_dagger).is_zero()
    return {str(n): v.text() for n, v in expected.items()}


def sign_q2(value):
    # Exact sign for the values occurring in this replay.  If a and b have
    # opposite signs compare a^2 with 2b^2; otherwise their common sign decides.
    if value.a == 0:
        return 1 if value.b > 0 else -1 if value.b < 0 else 0
    if value.b == 0:
        return 1 if value.a > 0 else -1
    if value.a > 0 and value.b > 0:
        return 1
    if value.a < 0 and value.b < 0:
        return -1
    left = value.a * value.a
    right = 2 * value.b * value.b
    if value.a > 0:
        return 1 if left > right else -1
    return -1 if left > right else 1


def check_box_rows(p_box):
    signs = {n: sign_q2(carry_image(n, p_box)) for n in range(2, 32)}
    assert all(signs[n] == -1 for n in range(2, 4))
    assert all(signs[n] == +1 for n in range(4, 8))
    assert all(signs[n] == -1 for n in range(8, 16))
    assert all(signs[n] == +1 for n in range(16, 32))
    for n in range(32, 129):
        assert carry_image(n, p_box).is_zero()
    return {
        "2_to_3": "negative",
        "4_to_7": "positive",
        "8_to_15": "negative",
        "16_to_31": "positive",
        "32_plus_through_128": "zero",
    }


def check_inverse_positivity():
    coefficients = []
    for r in range(33):
        value = Q2()
        for i in range(r + 1):
            for j in range(r - i + 1):
                k = r - i - j
                value = value + (Fraction(1, 2) ** j) * (SQRT2 ** k)
        assert value.a >= 0 and value.b >= 0
        coefficients.append(value.text())
    return {"checked_power_two_coefficients": len(coefficients)}


def check_five_adic_witness():
    assert Fraction(1, 5) > Fraction(16, 81)
    assert Fraction(2, 15) > Fraction(1, 9)
    assert Fraction(1, 15) > Fraction(1, 16)
    assert Fraction(4, 9) + Fraction(1, 3) + Fraction(1, 4) == Fraction(37, 36)
    assert Fraction(37, 36) > 1
    return {"rational_lower_sum": "37/36"}


def main():
    p_omega, p_dagger, p_box = check_polynomials()
    results = {
        "schema": "X-32301-critical-null-source-v1",
        "classification": "EXACT_Q_SQRT2_AND_RATIONAL",
        "polynomials": {
            "omega_degree": len(p_omega) - 1,
            "dagger_degree": len(p_dagger) - 1,
            "box_degree": len(p_box) - 1,
            "box_coefficients": [x.text() for x in p_box],
        },
        "dagger_carry_rows": check_dagger_rows(p_dagger),
        "box_carry_sign_blocks": check_box_rows(p_box),
        "positive_inverse": check_inverse_positivity(),
        "five_adic_firewall": check_five_adic_witness(),
        "does_not_prove": [
            "CNSB",
            "eventual one-sign of the six-row scalar",
            "the five-state Cycle-Debt recurrence",
            "the physical-block upper estimate",
            "RH",
        ],
    }
    canonical = json.dumps(results, indent=2, sort_keys=True) + "\n"
    results["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    output = json.dumps(results, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
