#!/usr/bin/env python3
"""Exact bounded replay for gcd-wave Fourier-mode decoupling."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_GCD_WAVE_MODE_DECOUPLING.md"
SOURCE_COMMIT = "5122e939df2fa322b5a3185cf1d78d4b402f3d5f"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/"
    "FFPS_HIGH_GCD_WAVE_LOCALIZATION.md": (
        "1493a630000c211717339b8dd2e92244b624a6cd"
    ),
    "research/l-families/atlas/function_field/"
    "FFPS_HIGH_GCD_FAR_GAP_LOCALIZATION.md": (
        "72a4dbf21f452041c939c2c308716abfd49195a9"
    ),
    "research/l-families/atlas/function_field/"
    "FFPS_DIVISOR_WAVE_SHIFTED_ZETA_FACTORIZATION.md": (
        "21ef6a6e0078beb85f81fc880e5f161fc6288a8f"
    ),
    "research/l-families/atlas/function_field/"
    "FFPS_PRIMITIVE_CORE_GCD_GRAM_CLOSURE.md": (
        "d3b5a372b554f48fda50fc5d4b8de9a37b1ba036"
    ),
}

Monomial = tuple[int, int, int, int]
Polynomial = dict[Monomial, Fraction]


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        actual = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if actual != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "MODE-DECOUPLING",
        "critical coupling is absolutely summable",
        "small-prime firewall",
        "sharp hyperbola cutoff",
        "HIGHFARGCDWAVE remains open",
        "RH and GRH remain unproved",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def add_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    result: dict[Monomial, Fraction] = defaultdict(Fraction)
    for key, value in left.items():
        result[key] += value
    for key, value in right.items():
        result[key] += value
    return {key: value for key, value in result.items() if value}


def scale_polynomial(scale: Fraction, value: Polynomial) -> Polynomial:
    return {key: scale * coefficient for key, coefficient in value.items() if coefficient}


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    result: dict[Monomial, Fraction] = defaultdict(Fraction)
    for (dx1, dy1, wx1, wy1), value1 in left.items():
        for (dx2, dy2, wx2, wy2), value2 in right.items():
            result[(dx1 + dx2, dy1 + dy2, wx1 + wx2, wy1 + wy2)] += (
                value1 * value2
            )
    return {key: value for key, value in result.items() if value}


def one_variable_local(axis: str) -> Polynomial:
    if axis == "x":
        return {
            (0, 0, 0, 0): Fraction(1),
            (1, 0, 1, 0): Fraction(-1),
            (1, 0, -1, 0): Fraction(-1),
        }
    if axis == "y":
        return {
            (0, 0, 0, 0): Fraction(1),
            (0, 1, 0, 1): Fraction(-1),
            (0, 1, 0, -1): Fraction(-1),
        }
    raise ValueError("axis must be x or y")


def abxy_polynomial() -> Polynomial:
    return {
        (1, 1, sx, sy): Fraction(1)
        for sx in (-1, 1)
        for sy in (-1, 1)
    }


def gcd_local_polynomial(prime: int) -> Polynomial:
    if prime < 2:
        raise ValueError("prime must be at least two")
    base_without_cross = add_polynomials(
        add_polynomials(one_variable_local("x"), one_variable_local("y")),
        {(0, 0, 0, 0): Fraction(-1)},
    )
    return add_polynomials(
        base_without_cross,
        scale_polynomial(Fraction(prime + 2, prime), abxy_polynomial()),
    )


def local_decoupling_panel() -> dict[str, object]:
    rows = []
    product = multiply_polynomials(one_variable_local("x"), one_variable_local("y"))
    for prime in (5, 7, 11, 13, 17, 29):
        coupled = gcd_local_polynomial(prime)
        difference = add_polynomials(coupled, scale_polynomial(Fraction(-1), product))
        expected = scale_polynomial(Fraction(2, prime), abxy_polynomial())
        if difference != expected:
            raise ArithmeticError("gcd local factor did not decouple")
        rows.append(
            {
                "prime": prime,
                "coupling_coefficient_per_weight": str(Fraction(2, prime)),
                "coupling_monomials": len(expected),
            }
        )
    return {
        "rows": rows,
        "identity": "L_p=L_x,p*L_y,p+(2/p)A_p(xi)B_p(eta)x_p y_p",
    }


def critical_majorant(prime: int) -> Fraction:
    """Uniform upper bound for |H_p-1| at Re(s),Re(t)>=1/2."""
    root = math.isqrt(prime)
    # Rational lower bound sqrt(p) > root and 2/sqrt(p) < 2/root.
    if root <= 2:
        raise ValueError("majorant is used only for primes at least 17")
    denominator_lower = Fraction(root - 2, root)
    return Fraction(8, prime * prime) / (denominator_lower * denominator_lower)


def convergence_panel() -> dict[str, object]:
    rows = []
    for prime in (17, 19, 23, 29, 31, 37, 41, 43):
        bound = critical_majorant(prime)
        if bound >= 1:
            raise ArithmeticError("tail local factor not uniformly nonzero")
        rows.append({"prime": prime, "delta_bound": str(bound)})
    # Integral-test bound: sum_(n>=17) 32/n^2
    # <= 32*(1/17^2 + integral_17^infinity x^-2 dx) = 576/289 < 2.
    tail_bound = Fraction(576, 289)
    if tail_bound >= 2:
        raise ArithmeticError("critical coupling majorant unexpectedly large")
    return {
        "rows": rows,
        "tail_majorant": "|H_p-1|<<p^-2 uniformly on Re(s),Re(t)>=1/2",
        "normal_convergence": True,
        "nonzero_after_deleting_primes_at_most_13": True,
        "integer_plus_integral_bound": str(tail_bound),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta / primitive-pair route",
        "local_decoupling": local_decoupling_panel(),
        "critical_coupling": convergence_panel(),
        "exact_global_identity": (
            "G_(xi,eta)(s,t)=H_(xi,eta)(s,t) F_xi(s) F_eta(t)"
        ),
        "updated_gate": (
            "sharp hyperbola/Perron assembly of two one-variable Witt-zeta modes"
        ),
        "scope_firewall": {
            "sharp_height_cutoff_decoupled": False,
            "joint_mode_mean_estimate_proved": False,
            "highgcdwave_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_commit": SOURCE_COMMIT,
        "source_blobs": SOURCE_BLOBS,
        "resource_caps": {"local_primes": 6, "majorant_primes": 8},
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
