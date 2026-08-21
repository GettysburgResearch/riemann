#!/usr/bin/env python3
"""Exact Q[C] verifier for the Volterra--virial identity L-9514.

C is a formal symbol for 1/zeta(2)=6/pi^2.  On each unit cell the
analytic totient part is a quadratic polynomial in x with coefficients
affine in C.  The checker integrates all squares exactly and compares
the two sides coefficient by coefficient in Q[C].
"""
from __future__ import annotations

from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "riemann.x9514-volterra-virial.v1"


def phi_sieve(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi


def p_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return [
        (a[i] if i < len(a) else Fraction(0))
        + (b[i] if i < len(b) else Fraction(0))
        for i in range(n)
    ]


def p_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def p_scale(a: list[Fraction], q: Fraction) -> list[Fraction]:
    return [q * x for x in a]


def p_integral(a: list[Fraction], left: int, right: int) -> Fraction:
    return sum(
        coefficient
        * Fraction(right ** (degree + 1) - left ** (degree + 1), degree + 1)
        for degree, coefficient in enumerate(a)
    )


def qpoly_json(values: tuple[Fraction, Fraction, Fraction]) -> list[dict[str, int]]:
    return [
        {"numerator": value.numerator, "denominator": value.denominator}
        for value in values
    ]


def square_at(
    x: int, phi: list[int]
) -> tuple[Fraction, Fraction, Fraction]:
    s0 = sum(Fraction(phi[n], n) for n in range(1, x + 1))
    s1 = sum(phi[n] for n in range(1, x + 1))
    q0 = Fraction(s1) - s0 * x
    q1 = Fraction(x * x, 2)
    return q0 * q0, 2 * q0 * q1, q1 * q1


def verify_endpoint(
    endpoint: int, phi: list[int]
) -> tuple[Fraction, Fraction, Fraction]:
    analytic_integral = [Fraction(0), Fraction(0), Fraction(0)]
    difference_integral = [Fraction(0), Fraction(0), Fraction(0)]

    s0 = Fraction(1)
    s1 = Fraction(1)

    for cell in range(1, endpoint):
        if cell > 1:
            s0 += Fraction(phi[cell], cell)
            s1 += phi[cell]

        # A(x) = q0(x) + C*q1(x),
        # q0 = s1 - s0*x, q1 = x^2/2.
        q0 = [s1, -s0]
        q1 = [Fraction(0), Fraction(0), Fraction(1, 2)]
        a_square = [
            p_mul(q0, q0),
            p_scale(p_mul(q0, q1), Fraction(2)),
            p_mul(q1, q1),
        ]
        for power in range(3):
            analytic_integral[power] += p_integral(
                a_square[power], cell, cell + 1
            )

        # E_phi = s1 - C*x^2/2 and f = s0 - C*x.
        e0 = [s1]
        e1 = [Fraction(0), Fraction(0), Fraction(-1, 2)]
        f0 = [s0]
        f1 = [Fraction(0), Fraction(-1)]
        x2 = [Fraction(0), Fraction(0), Fraction(1)]

        difference = [
            p_add(
                p_mul(e0, e0),
                p_scale(p_mul(x2, p_mul(f0, f0)), Fraction(-1)),
            ),
            p_add(
                p_scale(p_mul(e0, e1), Fraction(2)),
                p_scale(
                    p_mul(x2, p_scale(p_mul(f0, f1), Fraction(2))),
                    Fraction(-1),
                ),
            ),
            p_add(
                p_mul(e1, e1),
                p_scale(p_mul(x2, p_mul(f1, f1)), Fraction(-1)),
            ),
        ]
        for power in range(3):
            difference_integral[power] += p_integral(
                difference[power], cell, cell + 1
            )

    at_endpoint = square_at(endpoint, phi)
    at_one = square_at(1, phi)
    boundary = tuple(
        Fraction(endpoint) * at_endpoint[i] - at_one[i] for i in range(3)
    )
    left = tuple(2 * value for value in analytic_integral)
    right = tuple(
        difference_integral[i] + boundary[i] for i in range(3)
    )
    if left != right:
        raise AssertionError(
            f"virial identity failed at endpoint {endpoint}: {left} != {right}"
        )
    return left


def canonical_digest(body: dict[str, object]) -> str:
    raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(limit: int) -> dict[str, object]:
    if limit < 2:
        raise ValueError("limit must be at least two")
    phi = phi_sieve(limit)
    retained = {2, 3, 5, 10, 20, 32, 50, limit}
    rows = []
    for endpoint in range(2, limit + 1):
        value = verify_endpoint(endpoint, phi)
        if endpoint in retained:
            rows.append(
                {
                    "endpoint": endpoint,
                    "two_integral_analytic_square_QC": qpoly_json(value),
                }
            )
    body: dict[str, object] = {
        "schema": SCHEMA,
        "verdict": "PASS_EXACT_L9514_VOLTERRA_VIRIAL_IDENTITY",
        "formal_symbol": "C=1/zeta(2)=6/pi^2",
        "verified_endpoint_range": [2, limit],
        "rows": rows,
        "proof_boundary": (
            "Exact finite-cell algebra only.  The checker does not prove the "
            "critical X^(2+epsilon) joint remainder or RH."
        ),
    }
    body["proof_object_sha256"] = canonical_digest(body)
    return body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=64)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.limit)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
