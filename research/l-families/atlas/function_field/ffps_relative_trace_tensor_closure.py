#!/usr/bin/env python3
"""Exact bounded replay for relative trace tensor externalization."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_RELATIVE_TRACE_TENSOR_CLOSURE.md"
SOURCE_BLOBS = {
    (
        "680be76bd31acdd96925d0b73f1a469226a19c9f",
        "research/l-families/atlas/function_field/"
        "FFPS_RELATIVE_FIRST_ADAMS_CLOSURE.md",
    ): "aba88795dd1c95cb320d45c1dc367cd71d73e1d5",
    (
        "680be76bd31acdd96925d0b73f1a469226a19c9f",
        "research/l-families/atlas/function_field/"
        "FFPS_RELATIVE_PHASE_STRATIFIED_EXTERNALIZATION.md",
    ): "68e99e25539de79955ef11534056b9e82b57cb60",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/"
        "FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md",
    ): "9012f96b34a3ffe55b66282ba1e62bc02514b5c6",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/"
        "L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/"
        "L-106093-mellin-polarization-places-the-anchor-inside-one-amplified-family-moment.md",
    ): "cb8665b8cdbe2bc7e6eb223d6bc009e8e4f5a5df",
}

Eisenstein = tuple[Fraction, Fraction]
ZERO: Eisenstein = (Fraction(), Fraction())
ONE: Eisenstein = (Fraction(1), Fraction())
OMEGA: Eisenstein = (Fraction(), Fraction(1))


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    factors: list[tuple[int, int]] = []
    remaining = n
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def mobius(n: int) -> int:
    sign = 1
    for _, exponent in factorization(n):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        actual = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if actual != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "TRACE-NATREL",
        "COPRIME-WICK-EXT",
        "ONEPLACEWEIL",
        "finite signed tensor span",
        "not a uniform Betti theorem",
        "RH and GRH remain unproved",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def e_add(left: Eisenstein, right: Eisenstein) -> Eisenstein:
    return left[0] + right[0], left[1] + right[1]


def e_scale(scale: Fraction, value: Eisenstein) -> Eisenstein:
    return scale * value[0], scale * value[1]


def e_mul(left: Eisenstein, right: Eisenstein) -> Eisenstein:
    # omega^2 = -1 - omega
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c - b * d


def e_conj(value: Eisenstein) -> Eisenstein:
    a, b = value
    return a - b, -b


def e_abs2(value: Eisenstein) -> Fraction:
    result = e_mul(value, e_conj(value))
    if result[1]:
        raise ArithmeticError("Eisenstein norm did not land in Q")
    return result[0]


def e_pow_omega(exponent: int) -> Eisenstein:
    exponent %= 3
    if exponent == 0:
        return ONE
    if exponent == 1:
        return OMEGA
    return -Fraction(1), -Fraction(1)


def e_sum(values: list[Eisenstein] | tuple[Eisenstein, ...]) -> Eisenstein:
    result = ZERO
    for value in values:
        result = e_add(result, value)
    return result


def ternary_centered_identity(
    coefficients: tuple[Eisenstein, ...], labels: tuple[int, ...]
) -> tuple[Fraction, Fraction]:
    """Return both sides of the exact k=3, S={0,1} centered identity."""
    if len(coefficients) != len(labels) or not coefficients:
        raise ValueError("coefficients and labels must be nonempty and aligned")
    principal = e_sum(coefficients)
    diagonal = sum((e_abs2(value) for value in coefficients), Fraction())
    left = e_abs2(principal) - diagonal

    hard_centered: list[Fraction] = []
    for rotation in range(3):
        selected = {rotation, (rotation + 1) % 3}
        hard = e_scale(
            Fraction(3, 2),
            e_sum(
                [
                    value
                    for value, label in zip(coefficients, labels, strict=True)
                    if label in selected
                ]
            ),
        )
        hard_diagonal = Fraction(9, 4) * sum(
            (
                e_abs2(value)
                for value, label in zip(coefficients, labels, strict=True)
                if label in selected
            ),
            Fraction(),
        )
        hard_centered.append(e_abs2(hard) - hard_diagonal)

    selected_centered: list[Fraction] = []
    for power in (1, 2):
        member = e_sum(
            [
                e_mul(e_pow_omega(power * label), value)
                for value, label in zip(coefficients, labels, strict=True)
            ]
        )
        selected_centered.append(e_abs2(member) - diagonal)

    right = Fraction(1, 3) * sum(hard_centered, Fraction()) - Fraction(
        1, 4
    ) * sum(selected_centered, Fraction())
    return left, right


def centered_identity_panel() -> dict[str, object]:
    fixtures = (
        (
            (
                (Fraction(1), Fraction()),
                (Fraction(2), Fraction(1)),
                (Fraction(-1), Fraction(2)),
            ),
            (0, 1, 2),
        ),
        (
            (
                (Fraction(3, 2), Fraction(-1, 3)),
                (Fraction(-2, 5), Fraction(4, 3)),
                (Fraction(7, 4), Fraction(1, 2)),
                (Fraction(-5, 6), Fraction(-7, 5)),
                (Fraction(9, 7), Fraction(2, 9)),
            ),
            (0, 0, 1, 2, 2),
        ),
    )
    rows = []
    for index, (coefficients, labels) in enumerate(fixtures):
        left, right = ternary_centered_identity(coefficients, labels)
        if left != right:
            raise ArithmeticError("centered ternary identity failed")
        rows.append(
            {
                "fixture": index,
                "atoms": len(coefficients),
                "principal_centered": str(left),
                "hard_minus_selected": str(right),
            }
        )

    weights = (Fraction(3, 2), Fraction(-5, 7))
    restrictions = ((0, 2), (1, 3, 4))
    coefficients, labels = fixtures[1]
    total_left = Fraction()
    total_right = Fraction()
    for weight, subset in zip(weights, restrictions, strict=True):
        left, right = ternary_centered_identity(
            tuple(coefficients[index] for index in subset),
            tuple(labels[index] for index in subset),
        )
        total_left += weight * left
        total_right += weight * right
    if total_left != total_right:
        raise ArithmeticError("common restriction/recombination lost NATREL")
    return {
        "rows": rows,
        "common_restriction_preserved": True,
        "signed_outer_recombination_preserved": True,
        "signed_total": str(total_left),
    }


def coprime_direct(
    left: dict[int, Fraction], right: dict[int, Fraction], cap: int
) -> Fraction:
    return sum(
        (
            left.get(c, Fraction()) * right.get(d, Fraction()) / (c * d)
            for c in range(1, cap + 1)
            for d in range(1, cap + 1)
            if gcd(c, d) == 1
        ),
        Fraction(),
    )


def coprime_external(
    left: dict[int, Fraction], right: dict[int, Fraction], cap: int
) -> Fraction:
    total = Fraction()
    for m in range(1, cap + 1):
        mu = mobius(m)
        if not mu:
            continue
        left_sum = sum(
            (left.get(m * u, Fraction()) / u for u in range(1, cap // m + 1)),
            Fraction(),
        )
        right_sum = sum(
            (right.get(m * v, Fraction()) / v for v in range(1, cap // m + 1)),
            Fraction(),
        )
        total += Fraction(mu, m * m) * left_sum * right_sum
    return total


def square_external(
    left: dict[int, Fraction], right: dict[int, Fraction], cap: int
) -> Fraction:
    total = Fraction()
    for m in range(1, cap + 1):
        mu_m = mobius(m)
        if not mu_m:
            continue
        for n in range(1, cap + 1):
            mu_n = mobius(n)
            if not mu_n:
                continue
            left_cross = sum(
                (
                    left.get(m * u, Fraction())
                    * left.get(n * v, Fraction())
                    / (u * v)
                    for u in range(1, cap // m + 1)
                    for v in range(1, cap // n + 1)
                ),
                Fraction(),
            )
            right_cross = sum(
                (
                    right.get(m * u, Fraction())
                    * right.get(n * v, Fraction())
                    / (u * v)
                    for u in range(1, cap // m + 1)
                    for v in range(1, cap // n + 1)
                ),
                Fraction(),
            )
            total += Fraction(mu_m * mu_n, m * m * n * n) * left_cross * right_cross
    return total


def diagonal_direct(
    left: dict[int, Fraction], right: dict[int, Fraction], cap: int
) -> Fraction:
    return sum(
        (
            left.get(c, Fraction()) ** 2
            * right.get(d, Fraction()) ** 2
            / (c * c * d * d)
            for c in range(1, cap + 1)
            for d in range(1, cap + 1)
            if gcd(c, d) == 1
        ),
        Fraction(),
    )


def diagonal_external(
    left: dict[int, Fraction], right: dict[int, Fraction], cap: int
) -> Fraction:
    total = Fraction()
    for q in range(1, cap + 1):
        mu = mobius(q)
        if not mu:
            continue
        left_square = sum(
            (
                left.get(q * u, Fraction()) ** 2 / (u * u)
                for u in range(1, cap // q + 1)
            ),
            Fraction(),
        )
        right_square = sum(
            (
                right.get(q * v, Fraction()) ** 2 / (v * v)
                for v in range(1, cap // q + 1)
            ),
            Fraction(),
        )
        total += Fraction(mu, q**4) * left_square * right_square
    return total


def coprime_wick_panel() -> dict[str, object]:
    rows = []
    for cap in (4, 7, 10):
        left = {
            n: Fraction(((3 * n * n + 2 * n + 1) % 17) - 8, n + 2)
            for n in range(1, cap + 1)
        }
        right = {
            n: Fraction(((5 * n * n + n + 4) % 19) - 9, n + 3)
            for n in range(1, cap + 1)
        }
        direct = coprime_direct(left, right, cap)
        external = coprime_external(left, right, cap)
        square = direct * direct
        square_via_tensor = square_external(left, right, cap)
        diagonal = diagonal_direct(left, right, cap)
        diagonal_via_tensor = diagonal_external(left, right, cap)
        if direct != external or square != square_via_tensor:
            raise ArithmeticError("coprime tensor externalization failed")
        if diagonal != diagonal_via_tensor:
            raise ArithmeticError("atomic diagonal externalization failed")
        rows.append(
            {
                "cap": cap,
                "bilinear": str(direct),
                "square": str(square),
                "atomic_diagonal": str(diagonal),
                "centered": str(square - diagonal),
            }
        )

    mass_2 = sum(
        (Fraction(abs(mobius(m)), m * m) for m in range(1, 201)), Fraction()
    )
    mass_4 = sum(
        (Fraction(abs(mobius(m)), m**4) for m in range(1, 201)), Fraction()
    )
    if mass_2 >= 2 or mass_4 >= Fraction(11, 10):
        raise ArithmeticError("outer projective mass majorant failed")
    return {
        "rows": rows,
        "square_outer_mass": "(sum |mu(m)|/m^2)^2 <= zeta(2)^2",
        "diagonal_outer_mass": "sum |mu(q)|/q^4 <= zeta(4)",
        "partial_mass_2_through_200": str(mass_2),
        "partial_mass_4_through_200": str(mass_4),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "B: relative-first family/sheaf route",
        "centered_relative_identity": centered_identity_panel(),
        "coprime_wick_externalization": coprime_wick_panel(),
        "exact_theorems": {
            "trace_natrel_preserved_by_common_linear_cleanup": True,
            "coprime_square_has_finite_signed_tensor_expansion": True,
            "atomic_diagonal_has_finite_signed_tensor_expansion": True,
            "wick_centered_trace_has_bounded_projective_outer_cost": True,
        },
        "updated_gate": {
            "proved": ["TRACE-NATREL", "COPRIME-WICK-EXT"],
            "open": ["ONEPLACEWEIL", "ONEPLACETRACE", "PRINCIPAL-BINDING"],
        },
        "scope_firewall": {
            "constructible_one_place_descent_proved": False,
            "uniform_one_place_betti_bound_proved": False,
            "full_reltrace_proved": False,
            "principal_binding_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {
            f"{commit}:{path}": sha for (commit, path), sha in SOURCE_BLOBS.items()
        },
        "resource_caps": {
            "largest_integer_cap": 200,
            "centered_identity_fixtures": 2,
            "coprime_wick_caps": [4, 7, 10],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-lock", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(
        run(check_sources=not args.no_source_lock), indent=2, sort_keys=True
    ) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
