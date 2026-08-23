#!/usr/bin/env python3
"""Exact replay for T-105220 Bezoutian/residue decomposition.

This checker authenticates only finite rational polynomial identities and the
explicit ESDE scope counterexample. It does not prove the Xi entire-function
passage, BRP105220, PRES105220, or RH.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


Q = Fraction


def trim(p: list[Q]) -> list[Q]:
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def derivative(p: list[Q]) -> list[Q]:
    return trim([Q(i) * p[i] for i in range(1, len(p))] or [Q(0)])


def evaluate(p: list[Q], x: Q) -> Q:
    out = Q(0)
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


def multiply(p: list[Q], q: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def polynomial_from_roots(roots: list[int]) -> list[Q]:
    out = [Q(1)]
    for root in roots:
        out = multiply(out, [-Q(root), Q(1)])
    return out


def integrate_polynomial(q: list[Q], constant: Q) -> list[Q]:
    return trim([constant] + [q[i] / Q(i + 1) for i in range(len(q))])


def divide_with_remainder(a: list[Q], b: list[Q]) -> tuple[list[Q], list[Q]]:
    a = trim(a)
    b = trim(b)
    if len(a) < len(b):
        return [Q(0)], a
    quotient = [Q(0)] * (len(a) - len(b) + 1)
    remainder = list(a)
    while len(remainder) >= len(b) and not (
        len(remainder) == 1 and remainder[0] == 0
    ):
        shift = len(remainder) - len(b)
        coefficient = remainder[-1] / b[-1]
        quotient[shift] = coefficient
        for j, value in enumerate(b):
            remainder[j + shift] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def real_root_count(p: list[Q]) -> int:
    """Sturm count on the complete real line for a squarefree polynomial."""
    sequence = [trim(p), derivative(p)]
    while True:
        _, remainder = divide_with_remainder(sequence[-2], sequence[-1])
        if len(remainder) == 1 and remainder[0] == 0:
            break
        sequence.append([-value for value in remainder])

    def sign_at_infinity(poly: list[Q], positive: bool) -> int:
        sign = 1 if poly[-1] > 0 else -1
        if not positive and (len(poly) - 1) % 2:
            sign = -sign
        return sign

    def variations(signs: list[int]) -> int:
        return sum(left != right for left, right in zip(signs, signs[1:]))

    minus = variations([sign_at_infinity(poly, False) for poly in sequence])
    plus = variations([sign_at_infinity(poly, True) for poly in sequence])
    return minus - plus


def bezoutian_value(p: list[Q], x: Q, y: Q) -> Q:
    dp = derivative(p)
    if x == y:
        return evaluate(dp, x) ** 2 - evaluate(p, x) * evaluate(derivative(dp), x)
    return (
        evaluate(p, x) * evaluate(dp, y)
        - evaluate(dp, x) * evaluate(p, y)
    ) / (x - y)


def residue_decomposition_value(
    p: list[Q], critical_points: list[Q], x: Q, y: Q
) -> Q:
    degree = len(p) - 1
    dp = derivative(p)
    ddp = derivative(dp)
    out = evaluate(dp, x) * evaluate(dp, y) / Q(degree)

    for critical in critical_points:
        rho = evaluate(p, critical) / evaluate(ddp, critical)

        def critical_feature(z: Q) -> Q:
            if z == critical:
                return evaluate(ddp, critical)
            return evaluate(dp, z) / (z - critical)

        out -= rho * critical_feature(x) * critical_feature(y)
    return out


def check_bezoutian_factorizations() -> int:
    examples = [
        ([Q(-1), Q(0), Q(1)], [Q(0)]),
        ([Q(1), Q(0), Q(1)], [Q(0)]),
        ([Q(0), Q(-3), Q(0), Q(1)], [Q(-1), Q(1)]),
    ]

    q = polynomial_from_roots([-4, -1, 0, 5])
    examples.append(
        (integrate_polynomial(q, Q(8, 5)), [Q(-4), Q(-1), Q(0), Q(5)])
    )

    grid = [Q(-7, 2), Q(-2), Q(1, 2), Q(7, 2), Q(13, 2)]
    checks = 0
    for polynomial, critical_points in examples:
        for x in grid:
            for y in grid:
                assert bezoutian_value(polynomial, x, y) == residue_decomposition_value(
                    polynomial, critical_points, x, y
                )
                checks += 1

        dp = derivative(polynomial)
        ddp = derivative(dp)
        for i, left in enumerate(critical_points):
            for j, right in enumerate(critical_points):
                value = bezoutian_value(polynomial, left, right)
                if i != j:
                    assert value == 0
                else:
                    rho = evaluate(polynomial, left) / evaluate(ddp, left)
                    assert value == -rho * evaluate(ddp, left) ** 2
                checks += 1
    return checks


def check_scope_counterexample() -> int:
    q = polynomial_from_roots([-4, -1, 0, 5])
    p = integrate_polynomial(q, Q(8, 5))
    critical_points = [Q(-4), Q(-1), Q(0), Q(5)]
    expected_residues = [Q(-106, 135), Q(-4, 45), Q(-2, 25), Q(-1246, 675)]

    assert derivative(p) == q
    assert real_root_count(p) == 5

    ddp = derivative(q)
    residues = [evaluate(p, c) / evaluate(ddp, c) for c in critical_points]
    assert residues == expected_residues
    assert all(rho < 0 for rho in residues)

    count = len(residues)
    first_moment = -sum(residues, Q(0))
    second_moment = sum((rho * rho for rho in residues), Q(0))
    coherence = first_moment**2 / (Q(count) * second_moment)
    scaled_defect = Q(count) * (1 - coherence)

    assert first_moment == Q(14, 5)
    assert second_moment == Q(1839932, 455625)
    assert coherence == Q(893025, 1839932)
    assert scaled_defect == Q(946907, 459983)
    assert scaled_defect > 1

    pairwise_dispersion = sum(
        (residues[i] - residues[j]) ** 2
        for i in range(count)
        for j in range(i + 1, count)
    )
    assert pairwise_dispersion == Q(count) * second_moment - first_moment**2
    assert pairwise_dispersion > second_moment
    return 15


def check_chord_polarization_identity() -> int:
    examples = [
        [Q(-1), Q(0), Q(1)],
        [Q(0), Q(-3), Q(0), Q(1)],
        integrate_polynomial(polynomial_from_roots([-4, -1, 0, 5]), Q(8, 5)),
    ]
    points = [(Q(-3, 2), Q(5, 2)), (Q(-2), Q(1)), (Q(1, 3), Q(7, 3))]
    parameters = [Q(0), Q(1, 5), Q(1, 2), Q(4, 5), Q(1)]
    checks = 0

    for p in examples:
        dp = derivative(p)
        ddp = derivative(dp)
        for x, y in points:
            delta = y - x
            for t in parameters:
                alpha = x + t * delta
                beta = y - t * delta
                derivative_q = delta * (
                    2 * evaluate(dp, alpha) * evaluate(dp, beta)
                    - evaluate(p, alpha) * evaluate(ddp, beta)
                    - evaluate(ddp, alpha) * evaluate(p, beta)
                )
                polarized = (
                    evaluate(dp, alpha) * evaluate(dp, beta)
                    - (
                        evaluate(ddp, alpha) * evaluate(p, beta)
                        + evaluate(p, alpha) * evaluate(ddp, beta)
                    )
                    / 2
                )
                assert derivative_q == 2 * delta * polarized
                checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    counts = {
        "bezoutian_factorization_checks": check_bezoutian_factorizations(),
        "scope_counterexample_checks": check_scope_counterexample(),
        "chord_polarization_checks": check_chord_polarization_identity(),
    }
    result = {
        "verdict": "PASS_X_105220_BEZOUTIAN_BOUNDARY_DECOMPOSITION",
        "arithmetic_class": "EXACT_RATIONAL_STURM",
        "counts": counts,
        "esde105212_canonical": False,
        "pres105220_proved": False,
        "brp105220_proved": False,
        "rh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
