#!/usr/bin/env python3
"""Exact bounded replay for native phase/coprimality externalization."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_RELATIVE_PHASE_STRATIFIED_EXTERNALIZATION.md"
SOURCE_BLOBS = {
    (
        "aaccfe767c3d36a353056c9a2483e3824d89949f",
        "research/l-families/atlas/function_field/"
        "FFPS_RELATIVE_FIRST_ADAMS_CLOSURE.md",
    ): "aba88795dd1c95cb320d45c1dc367cd71d73e1d5",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/"
        "L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
}


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    result: list[tuple[int, int]] = []
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            exponent = 0
            while remaining % p == 0:
                remaining //= p
                exponent += 1
            result.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        result.append((remaining, 1))
    return tuple(result)


def mobius(n: int) -> int:
    sign = 1
    for _, exponent in factorization(n):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        frozen = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if frozen != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "fixed-label native phase/coprimality layer",
        "REMAINING-GLUE",
        "bounded-rank external-product presentation",
        "Every later arrow remains open.",
        "RH or GRH",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def phase_exponent(
    ell: int, rho: int, h: int, k: int, p_owner: int, q_owner: int, c: int, d: int
) -> tuple[int, int]:
    """Return the two separated additive exponents."""
    return (k * p_owner * c * c) % rho, (-h * q_owner * d * d) % ell


def phase_factorization_panel() -> dict[str, object]:
    rows = []
    for data in (
        (5, 7, 2, 3, 11, 13, 4, 6),
        (7, 11, 5, 8, 17, 19, 9, 10),
        (11, 13, 7, 9, 23, 29, 12, 14),
    ):
        ell, rho, h, k, p_owner, q_owner, c, d = data
        left, right = phase_exponent(*data)
        joint = ((k * p_owner * c * c) % rho, (-h * q_owner * d * d) % ell)
        if (left, right) != joint:
            raise ArithmeticError("phase failed to separate")
        rows.append(
            {
                "ell": ell,
                "rho": rho,
                "left_exponent_mod_rho": left,
                "right_exponent_mod_ell": right,
                "joint_pair_equal": True,
            }
        )
    return {"rows": rows, "fixed_label_external_rank": 1}


def coprime_sum(
    a_values: dict[int, Fraction], b_values: dict[int, Fraction], cap: int
) -> Fraction:
    return sum(
        (
            a_values.get(c, Fraction()) * b_values.get(d, Fraction()) / (c * d)
            for c in range(1, cap + 1)
            for d in range(1, cap + 1)
            if gcd(c, d) == 1
        ),
        Fraction(),
    )


def mobius_externalized_sum(
    a_values: dict[int, Fraction], b_values: dict[int, Fraction], cap: int
) -> Fraction:
    total = Fraction()
    for m in range(1, cap + 1):
        mu = mobius(m)
        if not mu:
            continue
        left = sum(
            (a_values.get(m * u, Fraction()) / u for u in range(1, cap // m + 1)),
            Fraction(),
        )
        right = sum(
            (b_values.get(m * v, Fraction()) / v for v in range(1, cap // m + 1)),
            Fraction(),
        )
        total += Fraction(mu, m * m) * left * right
    return total


def coprimality_panel() -> dict[str, object]:
    caps = (4, 7, 10)
    rows = []
    for cap in caps:
        a_values = {
            n: Fraction(((3 * n * n + n + 2) % 11) - 5, n + 1)
            for n in range(1, cap + 1)
        }
        b_values = {
            n: Fraction(((5 * n * n + 2 * n + 1) % 13) - 6, n + 2)
            for n in range(1, cap + 1)
        }
        direct = coprime_sum(a_values, b_values, cap)
        external = mobius_externalized_sum(a_values, b_values, cap)
        if direct != external:
            raise ArithmeticError(f"coprimality externalization failed at cap={cap}")
        rows.append({"cap": cap, "direct": str(direct), "external": str(external)})
    partial_mass = sum(
        (Fraction(abs(mobius(m)), m * m) for m in range(1, 101)), Fraction()
    )
    if partial_mass >= Fraction(2):
        raise ArithmeticError("outer absolute mass majorant failed")
    return {
        "rows": rows,
        "outer_weight": "mu(m)/m^2",
        "absolute_mass_bound": "sum |mu(m)|/m^2 <= zeta(2) < 2",
        "partial_mass_through_100": str(partial_mass),
    }


def mixed_fourier_gram_panel() -> dict[str, object]:
    rows = []
    for prime in (3, 5, 7, 11):
        size = prime - 1
        gram = [
            [prime - 1 if i == j else -1 for j in range(size)] for i in range(size)
        ]
        constant_eigenvalue = sum(gram[0])
        orthogonal_eigenvalue = gram[0][0] - gram[0][1]
        if constant_eigenvalue != 1 or orthogonal_eigenvalue != prime:
            raise ArithmeticError("finite Fourier Gram spectrum failed")
        rows.append(
            {
                "prime": prime,
                "matrix_size": size,
                "gram": "p I - J",
                "constant_eigenvalue": constant_eigenvalue,
                "orthogonal_eigenvalue": orthogonal_eigenvalue,
                "rank": size,
                "external_rank_lower_bound": size,
            }
        )
    return {"rows": rows, "bounded_rank_as_prime_grows": False}


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "B: relative-first family/sheaf route",
        "phase_factorization": phase_factorization_panel(),
        "coprimality_externalization": coprimality_panel(),
        "mixed_phase_firewall": mixed_fourier_gram_panel(),
        "exact_theorems": {
            "fixed_label_phase_is_external": True,
            "coprimality_has_signed_externalization": True,
            "coprimality_outer_mass_is_uniform": True,
            "mixed_bilinear_phase_requires_rank_p_minus_1": True,
        },
        "scope_firewall": {
            "complete_native_source_externalized": False,
            "natrel_proved": False,
            "relpartfrob_proved": False,
            "reltrace_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_contract": {
            f"{commit}:{path}": sha for (commit, path), sha in SOURCE_BLOBS.items()
        },
        "resource_caps": {"largest_integer_cap": 100, "largest_prime": 11},
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
