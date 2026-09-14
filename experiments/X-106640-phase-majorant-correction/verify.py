#!/usr/bin/env python3
"""Exact replay for the L-106514 / T-106540 phase-angle correction.

The replay uses Gaussian rational arithmetic only.  It checks the one-pole
firewall, several finite Cauchy-Gram fixtures, and the exact inequality

    Re Delta <= |Delta| <= canonical model overlap.

It does not evaluate Xi or prove the open phase or Cauchy-transport gates.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path


@dataclass(frozen=True)
class GQ:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    @staticmethod
    def of(value: int | Fraction) -> "GQ":
        return GQ(Fraction(value), Fraction(0))

    def __add__(self, other: "GQ") -> "GQ":
        return GQ(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "GQ") -> "GQ":
        return GQ(self.re - other.re, self.im - other.im)

    def __neg__(self) -> "GQ":
        return GQ(-self.re, -self.im)

    def __mul__(self, other: "GQ") -> "GQ":
        return GQ(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conjugate(self) -> "GQ":
        return GQ(self.re, -self.im)

    def abs2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def inverse(self) -> "GQ":
        denominator = self.abs2()
        assert denominator != 0
        return GQ(self.re / denominator, -self.im / denominator)

    def __truediv__(self, other: "GQ") -> "GQ":
        return self * other.inverse()


ZERO = GQ()
ONE = GQ.of(1)
TWO = GQ.of(2)


def point(a: int | Fraction, y: int = 1) -> GQ:
    return GQ(Fraction(a), Fraction(y))


def eye(n: int) -> list[list[GQ]]:
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def matmul(a: list[list[GQ]], b: list[list[GQ]]) -> list[list[GQ]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    assert len(a[0]) == inner
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(inner)), ZERO)
            for j in range(cols)
        ]
        for i in range(rows)
    ]


def adjoint(a: list[list[GQ]]) -> list[list[GQ]]:
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]


def inverse(a: list[list[GQ]]) -> list[list[GQ]]:
    n = len(a)
    aug = [row[:] + ident[:] for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = next(index for index in range(col, n) if aug[index][col] != ZERO)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col].inverse()
        aug[col] = [entry * scale for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor == ZERO:
                continue
            aug[row] = [
                left - factor * right
                for left, right in zip(aug[row], aug[col])
            ]
    return [row[n:] for row in aug]


def trace(a: list[list[GQ]]) -> GQ:
    return sum((a[i][i] for i in range(len(a))), ZERO)


def blaschke_value(z: GQ, roots: list[GQ]) -> GQ:
    value = ONE
    for root in roots:
        value = value * ((z - root) / (z - root.conjugate()))
    return value


def blaschke_derivative(z: GQ, roots: list[GQ]) -> GQ:
    total = ZERO
    for index, root in enumerate(roots):
        factor_derivative = (root - root.conjugate()) / (
            (z - root.conjugate()) * (z - root.conjugate())
        )
        product = ONE
        for other_index, other in enumerate(roots):
            if other_index == index:
                continue
            product = product * ((z - other) / (z - other.conjugate()))
        total = total + factor_derivative * product
    return total


def gram(left: list[GQ], right: list[GQ]) -> list[list[GQ]]:
    # Fixtures use unit heights, so the normalized numerator is exactly 2.
    assert all(root.im == 1 for root in left + right)
    return [
        [
            TWO
            / GQ(
                left_root.im + right_root.im,
                left_root.re - right_root.re,
            )
            for right_root in right
        ]
        for left_root in left
    ]


def canonical_overlap(denominator: list[GQ], numerator: list[GQ]) -> Fraction:
    g_minus = gram(denominator, denominator)
    g_plus = gram(numerator, numerator)
    cross = gram(denominator, numerator)
    product = matmul(
        matmul(
            matmul(inverse(g_minus), cross),
            inverse(g_plus),
        ),
        adjoint(cross),
    )
    result = trace(product)
    assert result.im == 0
    return result.re


def cross_delta(denominator: list[GQ], numerator: list[GQ]) -> GQ:
    return sum(
        (
            blaschke_derivative(root, numerator)
            / blaschke_derivative(root, denominator)
            for root in denominator
        ),
        ZERO,
    )


def check_fixture(denominator: list[GQ], numerator: list[GQ]) -> dict[str, str]:
    overlap = canonical_overlap(denominator, numerator)
    delta = cross_delta(denominator, numerator)
    assert delta.re <= overlap
    assert delta.abs2() <= overlap * overlap
    charge = Fraction(len(denominator)) - overlap
    phase = Fraction(len(denominator)) - delta.re
    assert charge <= phase
    return {
        "degree_minus": str(len(denominator)),
        "degree_plus": str(len(numerator)),
        "overlap": str(overlap),
        "delta_re": str(delta.re),
        "delta_im": str(delta.im),
        "canonical_charge": str(charge),
        "phase_majorant": str(phase),
        "slack": str(phase - charge),
    }


def main() -> dict[str, object]:
    fixtures = [
        ([point(0)], [point(1)]),
        ([point(-2), point(2)], [point(-1), point(1)]),
        ([point(-3), point(0), point(4)], [point(-2), point(1), point(5)]),
        ([point(-5), point(-1), point(3)], [point(-4), point(2)]),
    ]
    results = [check_fixture(denominator, numerator) for denominator, numerator in fixtures]

    first = results[0]
    assert first["overlap"] == "4/5"
    assert first["delta_re"] == "12/25"
    assert first["delta_im"] == "-16/25"
    assert first["canonical_charge"] == "1/5"
    assert first["phase_majorant"] == "13/25"
    assert first["slack"] == "8/25"

    payload: dict[str, object] = {
        "schema": "riemann.x106640.phase-majorant-correction.v1",
        "classification": "PASS_T106640_PHASE_MAJORANT_CORRECTION",
        "fixtures": results,
        "cross_trace_norm_inequality_checked": True,
        "one_pole_equality_refuted": True,
        "canonical_charge": "1/5",
        "phase_majorant": "13/25",
        "phase_slack": "8/25",
        "mesotrans106630_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
