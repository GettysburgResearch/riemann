#!/usr/bin/env python3
"""Exact finite checks for the T-105210 low-order Levinson packet.

The replay authenticates finite Fourier-packet algebra only.  It does not
prove the analytic Xi Fourier representation, a fixed-height argument bound,
HLOC105210, or RH.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from pathlib import Path


@dataclass(frozen=True)
class GaussianFraction:
    real: Fraction
    imag: Fraction

    def __add__(self, other: object) -> "GaussianFraction":
        z = as_gaussian(other)
        return GaussianFraction(self.real + z.real, self.imag + z.imag)

    __radd__ = __add__

    def __neg__(self) -> "GaussianFraction":
        return GaussianFraction(-self.real, -self.imag)

    def __sub__(self, other: object) -> "GaussianFraction":
        return self + (-as_gaussian(other))

    def __rsub__(self, other: object) -> "GaussianFraction":
        return as_gaussian(other) - self

    def __mul__(self, other: object) -> "GaussianFraction":
        z = as_gaussian(other)
        return GaussianFraction(
            self.real * z.real - self.imag * z.imag,
            self.real * z.imag + self.imag * z.real,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "GaussianFraction":
        return GaussianFraction(self.real, -self.imag)

    def norm_squared(self) -> Fraction:
        return self.real * self.real + self.imag * self.imag

    def __truediv__(self, other: object) -> "GaussianFraction":
        z = as_gaussian(other)
        denominator = z.norm_squared()
        if denominator == 0:
            raise ZeroDivisionError("division by zero Gaussian fraction")
        return self * z.conjugate() * Fraction(1, denominator)


def as_gaussian(value: object) -> GaussianFraction:
    if isinstance(value, GaussianFraction):
        return value
    return GaussianFraction(Fraction(value), Fraction(0))


ZERO = GaussianFraction(Fraction(0), Fraction(0))
ONE = GaussianFraction(Fraction(1), Fraction(0))
I = GaussianFraction(Fraction(0), Fraction(1))


def i_power(exponent: int) -> GaussianFraction:
    return (ONE, I, -ONE, -I)[exponent % 4]


def phase(frequency: int, quarter_turns: int) -> GaussianFraction:
    """exp(i*pi*frequency*quarter_turns/2), exactly."""
    return i_power(frequency * quarter_turns)


def make_fixtures() -> list[tuple[list[int], dict[int, Fraction], dict[int, Fraction]]]:
    fixtures = []
    for radius in (2, 3, 4):
        frequencies = [u for u in range(-radius, radius + 1) if u != 0]
        # Perfect-square symmetric weights make wedge features rational.
        weights = {u: Fraction(abs(u) ** 2) for u in frequencies}
        square_roots = {u: Fraction(abs(u)) for u in frequencies}
        fixtures.append((frequencies, weights, square_roots))
    return fixtures


def check_exterior_square_gram() -> tuple[int, int, int]:
    entry_checks = 0
    quadratic_checks = 0
    schur_checks = 0

    for frequencies, weights, square_roots in make_fixtures():
        def derivative_value(order: int, quarter_turns: int) -> GaussianFraction:
            value = ZERO
            for u in frequencies:
                value += (
                    weights[u]
                    * i_power(order)
                    * (u ** order)
                    * phase(u, quarter_turns)
                )
            return value

        def laguerre(order: int, quarter_turns: int) -> GaussianFraction:
            f0 = derivative_value(order, quarter_turns)
            f1 = derivative_value(order + 1, quarter_turns)
            f2 = derivative_value(order + 2, quarter_turns)
            return f1 * f1 - f0 * f2

        pairs = list(combinations(frequencies, 2))

        def wedge_feature(
            index: int,
            quarter_turns: int,
            u: int,
            v: int,
        ) -> GaussianFraction:
            return (
                ((-1) ** index)
                * ((u * v) ** index)
                * (v - u)
                * square_roots[u]
                * square_roots[v]
                * phase(-(u + v), quarter_turns)
            )

        points = [(0, 0), (1, 1), (2, 2), (3, 3), (1, 0)]
        gram: list[list[GaussianFraction]] = []
        for a, t in points:
            row = []
            for b, s in points:
                direct = laguerre(a + b, (s - t) % 4)
                feature_inner = sum(
                    (
                        wedge_feature(a, t, u, v).conjugate()
                        * wedge_feature(b, s, u, v)
                        for u, v in pairs
                    ),
                    ZERO,
                )
                assert direct == feature_inner
                assert direct.imag == 0
                row.append(direct)
                entry_checks += 1
            gram.append(row)

        coefficient_vectors = (
            (1, 0, 0, 0, 0),
            (1, -1, 2, 0, 1),
            (2, 3, -1, 1, -2),
            (-1, 4, 2, -3, 1),
        )
        for coefficients in coefficient_vectors:
            quadratic = ZERO
            for i, left in enumerate(coefficients):
                for j, right in enumerate(coefficients):
                    quadratic += left * right * gram[i][j]

            feature_norm = ZERO
            for u, v in pairs:
                combined = sum(
                    (
                        coefficients[index]
                        * wedge_feature(*points[index], u, v)
                        for index in range(len(points))
                    ),
                    ZERO,
                )
                feature_norm += combined.conjugate() * combined

            assert quadratic == feature_norm
            assert quadratic.imag == 0 and quadratic.real >= 0
            quadratic_checks += 1

        for a, b, t in ((0, 1, 1), (1, 2, 2), (0, 3, 3), (2, 2, 1)):
            left = laguerre(a + b, t).norm_squared()
            right = laguerre(2 * a, 0).real * laguerre(2 * b, 0).real
            assert left <= right
            schur_checks += 1

    return entry_checks, quadratic_checks, schur_checks


def check_mean_orientation() -> int:
    checks = 0
    for frequencies, weights, _ in make_fixtures():
        for order in range(4):
            for tilt in (Fraction(3, 2), Fraction(2), Fraction(5, 2)):
                for lam in (Fraction(1, 7), Fraction(2, 5), Fraction(3, 4)):
                    strong = Fraction(0)
                    weak = Fraction(0)
                    a_value = Fraction(0)
                    b_value = Fraction(0)
                    c_value = Fraction(0)

                    for u in frequencies:
                        exponential_tilt = (
                            tilt ** (2 * u)
                            if u >= 0
                            else Fraction(1, 1) / (tilt ** (-2 * u))
                        )
                        base = (
                            Fraction(u ** (2 * order))
                            * weights[u] ** 2
                            * exponential_tilt
                        )
                        a_value += base
                        b_value += base * u * u
                        c_value += base * u
                        strong += base * (1 + lam * u) ** 2
                        weak += base * (1 - lam * u) ** 2

                    assert strong == a_value + 2 * lam * c_value + lam * lam * b_value
                    assert weak == a_value - 2 * lam * c_value + lam * lam * b_value
                    assert strong - weak == 4 * lam * c_value
                    assert c_value > 0
                    checks += 1
    return checks


def check_phase_sum_rule() -> int:
    checks = 0
    for frequencies, weights, _ in make_fixtures():
        for order in range(6):
            expected = 2 * sum(
                Fraction(u ** (2 * order + 2)) * weights[u] ** 2
                for u in frequencies
            )

            zero_mode = Fraction(0)
            for u in frequencies:
                v = -u
                if v in weights:
                    zero_mode += (
                        Fraction(1, 2)
                        * ((-1) ** order)
                        * (u - v) ** 2
                        * ((u * v) ** order)
                        * weights[u]
                        * weights[v]
                    )

            assert zero_mode == expected
            checks += 1
    return checks


def check_levinson_telescope() -> int:
    values = (
        GaussianFraction(Fraction(2), Fraction(1)),
        GaussianFraction(Fraction(3), Fraction(-2)),
        GaussianFraction(Fraction(5), Fraction(1)),
        GaussianFraction(Fraction(7), Fraction(3)),
        GaussianFraction(Fraction(11), Fraction(-1)),
        GaussianFraction(Fraction(13), Fraction(2)),
    )

    checks = 0
    for terminal in range(1, len(values)):
        product_value = ONE
        for index in range(terminal):
            product_value *= values[index] / values[index + 1]
        assert product_value == values[0] / values[terminal]
        checks += 1
    return checks


def check_crdb_correction() -> int:
    fixtures = (
        (4, 0, (3, 2), (Fraction(2, 3), Fraction(1, 2)), (1, 1)),
        (6, 2, (4, 5, 2), (Fraction(3, 4), Fraction(4, 5), Fraction(1, 2)), (1, 1, 1)),
        (2, 0, (1,), (Fraction(1),), (0,)),
    )

    checks = 0
    for o_zero, o_terminal, real_counts, coherences, wrong_counts in fixtures:
        slacks = [
            Fraction(real_count) * (1 - coherence) - wrong_count
            for real_count, coherence, wrong_count in zip(
                real_counts, coherences, wrong_counts
            )
        ]
        assert all(slack >= 0 for slack in slacks)

        boundary_sum = Fraction(o_zero - o_terminal - 2 * sum(wrong_counts))
        ledger = (
            Fraction(o_terminal)
            + 2
            * sum(
                Fraction(real_count) * (1 - coherence)
                for real_count, coherence in zip(real_counts, coherences)
            )
            + boundary_sum
        )
        assert ledger == Fraction(o_zero) + 2 * sum(slacks)
        checks += 1
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    entries, quadratic_forms, schur = check_exterior_square_gram()
    counts = {
        "crdb_identity_checks": check_crdb_correction(),
        "exterior_square_gram_entries": entries,
        "gram_quadratic_forms": quadratic_forms,
        "levinson_telescope_checks": check_levinson_telescope(),
        "mean_orientation_checks": check_mean_orientation(),
        "phase_sum_rule_checks": check_phase_sum_rule(),
        "pointwise_schur_checks": schur,
    }

    result = {
        "verdict": "PASS_X_105210_LOW_ORDER_LEVINSON_GRAM",
        "arithmetic_class": "EXACT_GAUSSIAN_RATIONAL_FINITE_FOURIER_PACKETS",
        "counts": counts,
        "total_checks": sum(counts.values()),
        "analytic_xi_fourier_theorem_machine_proved": False,
        "fixed_height_localization_proved": False,
        "hloc105210_proved": False,
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
