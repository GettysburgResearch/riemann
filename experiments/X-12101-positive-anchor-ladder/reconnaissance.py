#!/usr/bin/env python3
"""Ordinary-high-precision positive-anchor scout for the PR #103 table.

This is discovery code only. It reads directed old moments at their midpoints
and evaluates new completed-xi points with mpmath.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Iterable

import mpmath as mp
import sympy as sp

DEFAULT_BASIS = Path(
    "experiments/X-9306-real-log-portfolio-search/results/basis.json"
)
DEFAULT_PRIMITIVES = Path(
    "experiments/X-9302-total-count-zero-deflation/results/"
    "pr71-shift-fine/atomized-min-certificate-p512.json"
)
DEFAULT_ANCHORS = (
    Fraction(1, 8),
    Fraction(3, 16),
    Fraction(1, 4),
    Fraction(3, 8),
    Fraction(1, 2),
    Fraction(3, 4),
    Fraction(1, 1),
)


def midpoint(lower: str, upper: str) -> mp.mpf:
    return (mp.mpf(lower) + mp.mpf(upper)) / 2


def load_old_moments(path: Path) -> list[mp.mpf]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    rows = raw["basis_rows"]
    if [row["degree"] for row in rows] != list(range(15)):
        raise ValueError("basis rows are not degrees 0 through 14")
    return [
        midpoint(row["lower_exact_decimal"], row["upper_exact_decimal"])
        for row in rows
    ]


def load_primitives(
    path: Path,
) -> tuple[mp.mpf, list[sp.Rational], list[tuple[int, mp.mpf]]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    ordinate = raw["ordinate"]
    t = mp.mpf(ordinate["numerator"]) / mp.mpf(ordinate["denominator"])
    nodes = [
        sp.Rational(point["u"]["numerator"], point["u"]["denominator"])
        for point in raw["points"]
    ]
    counts = [window["count_lower"] for window in raw["count_windows"]]
    increments = [counts[0]] + [
        counts[index] - counts[index - 1]
        for index in range(1, len(counts))
    ]
    shells = []
    for increment, window in zip(increments, raw["count_windows"]):
        radius = Fraction(
            window["radius"]["numerator"],
            window["radius"]["denominator"],
        )
        shells.append(
            (
                increment,
                mp.mpf(radius.numerator**2) / radius.denominator**2,
            )
        )
    return t, nodes, shells


def logabs_xi_squared(u: mp.mpf, t: mp.mpf) -> mp.mpf:
    x = mp.sqrt(u)
    s = mp.mpf("0.5") + x + 1j * t
    zeta = mp.zeta(s, method="riemann-siegel")
    return 2 * (
        mp.log(mp.mpf("0.5"))
        + mp.log(abs(s))
        + mp.log(abs(s - 1))
        - mp.re(s) * mp.log(mp.pi) / 2
        + mp.re(mp.loggamma(s / 2))
        + mp.log(abs(zeta))
    )


def deflated_value(
    u: mp.mpf,
    t: mp.mpf,
    shells: list[tuple[int, mp.mpf]],
) -> mp.mpf:
    return logabs_xi_squared(u, t) - sum(
        count * mp.log(u + radius_square)
        for count, radius_square in shells
    )


def mpq(value: sp.Rational) -> mp.mpf:
    return mp.mpf(value.p) / mp.mpf(value.q)


def reduced_scalar(
    anchor: sp.Rational,
    anchor_value: mp.mpf,
    reference_value: mp.mpf,
    nodes: list[sp.Rational],
    old_moments: list[mp.mpf],
) -> mp.mpf:
    y = sp.symbols("y")
    denominator = sp.prod(y + node for node in nodes)
    at_negative_anchor = sp.expand(denominator.subs(y, -anchor))
    beta = -1 / at_negative_anchor
    old_polynomial = sp.cancel(
        (1 - denominator / at_negative_anchor) / (y + anchor)
        + denominator / (at_negative_anchor * (y + nodes[0]))
    )
    old_polynomial = sp.Poly(sp.expand(old_polynomial), y)
    coefficients = [old_polynomial.nth(index) for index in range(15)]
    return mpq(beta) * (anchor_value - reference_value) + sum(
        mpq(coefficients[index]) * old_moments[index]
        for index in range(15)
    )


def signed_divided_difference(
    anchors: list[mp.mpf], scalars: list[mp.mpf]
) -> mp.mpf:
    values = list(scalars)
    for level in range(1, len(anchors)):
        values = [
            (values[index + 1] - values[index])
            / (anchors[index + level] - anchors[index])
            for index in range(len(values) - 1)
        ]
    return (-1) ** (len(anchors) - 1) * values[0]


def transform(
    old: list[mp.mpf],
    anchors: list[mp.mpf],
    scalars: list[mp.mpf],
) -> list[mp.mpf]:
    previous = list(old)
    for index, anchor in enumerate(anchors):
        current = [
            signed_divided_difference(
                anchors[: index + 1], scalars[: index + 1]
            )
        ]
        for moment in previous:
            current.append(moment - anchor * current[-1])
        previous = current
    return previous


def correlation_minimum(matrix: mp.matrix) -> mp.mpf:
    size = matrix.rows
    correlation = mp.matrix(
        [
            [
                matrix[row, column]
                / mp.sqrt(matrix[row, row] * matrix[column, column])
                for column in range(size)
            ]
            for row in range(size)
        ]
    )
    return mp.eigsy(correlation, eigvals_only=True)[0]


def packet_summary(
    old: list[mp.mpf],
    anchors: list[mp.mpf],
    scalars: list[mp.mpf],
) -> dict[str, object]:
    moments = transform(old, anchors, scalars)
    degree = 14 + len(anchors)
    h0_size = degree // 2 + 1
    h1_size = (degree - 1) // 2 + 1
    h0 = mp.matrix(
        [
            [moments[row + column] for column in range(h0_size)]
            for row in range(h0_size)
        ]
    )
    h1 = mp.matrix(
        [
            [moments[row + column + 1] for column in range(h1_size)]
            for row in range(h1_size)
        ]
    )
    return {
        "anchor_count": len(anchors),
        "anchors": [mp.nstr(value, 30) for value in anchors],
        "final_degree": degree,
        "h0_size": h0_size,
        "h1_size": h1_size,
        "h0_min_eigenvalue": mp.nstr(
            mp.eigsy(h0, eigvals_only=True)[0], 45
        ),
        "h1_min_eigenvalue": mp.nstr(
            mp.eigsy(h1, eigvals_only=True)[0], 45
        ),
        "h0_correlation_min": mp.nstr(
            correlation_minimum(h0), 45
        ),
        "h1_correlation_min": mp.nstr(
            correlation_minimum(h1), 45
        ),
    }


def parse_anchors(values: Iterable[str]) -> list[Fraction]:
    anchors = [Fraction(value) for value in values]
    if not anchors:
        raise ValueError("at least one anchor is required")
    if any(value <= 0 for value in anchors):
        raise ValueError("anchors must be positive")
    if anchors != sorted(anchors) or len(set(anchors)) != len(anchors):
        raise ValueError("anchors must be strictly increasing")
    return anchors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--basis", type=Path, default=DEFAULT_BASIS)
    parser.add_argument(
        "--primitives", type=Path, default=DEFAULT_PRIMITIVES
    )
    parser.add_argument(
        "--anchors",
        nargs="*",
        default=[str(value) for value in DEFAULT_ANCHORS],
    )
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    rational_anchors = parse_anchors(args.anchors)
    old = load_old_moments(args.basis)
    t, nodes, shells = load_primitives(args.primitives)
    reference_u = mpq(nodes[0])
    reference_value = deflated_value(reference_u, t, shells)

    anchor_scalars = []
    point_values = []
    for rational_anchor in rational_anchors:
        anchor = mp.mpf(rational_anchor.numerator) / rational_anchor.denominator
        value = deflated_value(anchor, t, shells)
        scalar = reduced_scalar(
            sp.Rational(
                rational_anchor.numerator, rational_anchor.denominator
            ),
            value,
            reference_value,
            nodes,
            old,
        )
        point_values.append(value)
        anchor_scalars.append(scalar)

    numeric_anchors = [
        mp.mpf(value.numerator) / value.denominator
        for value in rational_anchors
    ]
    packets = [
        packet_summary(
            old,
            numeric_anchors[:count],
            anchor_scalars[:count],
        )
        for count in range(1, len(rational_anchors) + 1)
    ]
    result = {
        "schema": (
            "riemann.positive-anchor-ladder."
            "reconnaissance.regenerated.v1"
        ),
        "classification": "EMPIRICAL_ORDINARY_HIGH_PRECISION",
        "working_decimal_digits": args.dps,
        "ordinate": mp.nstr(t, 50),
        "anchors": [str(value) for value in rational_anchors],
        "deflated_point_values": [
            mp.nstr(value, 60) for value in point_values
        ],
        "one_anchor_scalars": [
            mp.nstr(value, 60) for value in anchor_scalars
        ],
        "prefix_packets": packets,
        "proof_boundary": (
            "Old interval moments are replaced by midpoints and new "
            "completed-xi values use ordinary mpmath arithmetic. "
            "This file is discovery only."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
