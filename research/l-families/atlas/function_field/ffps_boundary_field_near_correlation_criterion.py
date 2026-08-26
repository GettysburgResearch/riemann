#!/usr/bin/env python3
"""Bounded exact replay for the compact boundary-field correlation criterion."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "9e19e27614e473b3b7d06cfc3d51f92eb39ff009"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md": (
        "bf4d1baa231086ba7e8eafaecd39730d83c9201a"
    ),
    "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py": (
        "2180038eef7ab639477879e806bb13fdbea0b1ec"
    ),
    "research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.json": (
        "c86a40d6a930603b3897ad12a28acc5f21e80dd6"
    ),
    "tests/test_ffps_mollified_beta_boundary_shell_identity.py": (
        "5e7de97284878c6f9b5a5ac43b83ccaf9528e242"
    ),
}
COEFFICIENT_CAP = 512
TOY_SOURCE_CAP = 24
TOY_KERNEL = (Fraction(2), Fraction(-1), Fraction(3), Fraction(-2))


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def mobius(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int) -> int:
    return mobius(value) - (mobius(value // 67) if value % 67 == 0 else 0)


def beta_square_local(prime: int, exponent: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 2
        or isinstance(exponent, bool)
        or not isinstance(exponent, int)
        or exponent < 0
    ):
        raise ValueError("invalid local-factor input")
    if exponent == 0:
        return 1
    if prime == 67:
        return {1: 4, 2: 1}.get(exponent, 0)
    return int(exponent == 1)


def factor_integer(value: int) -> dict[int, int]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    factors: dict[int, int] = {}
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
        prime += 1
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def beta_square_from_euler(value: int) -> int:
    result = 1
    for prime, exponent in factor_integer(value).items():
        result *= beta_square_local(prime, exponent)
    return result


def exceptional_residue_ratio() -> Fraction:
    return Fraction(1 + Fraction(4, 67) + Fraction(1, 67**2), 1 + Fraction(1, 67))


def autocorrelation(kernel: tuple[Fraction, ...]) -> dict[int, Fraction]:
    if not kernel:
        raise ValueError("kernel must be nonempty")
    radius = len(kernel) - 1
    return {
        shift: sum(
            (
                kernel[index] * kernel[index + shift]
                for index in range(
                    max(0, -shift), min(len(kernel), len(kernel) - shift)
                )
            ),
            Fraction(0),
        )
        for shift in range(-radius, radius + 1)
    }


def direct_toy_energy(
    source: tuple[Fraction, ...], kernel: tuple[Fraction, ...]
) -> Fraction:
    if not source or not kernel:
        raise ValueError("source and kernel must be nonempty")
    field = [Fraction(0)] * (len(source) + len(kernel) - 1)
    for source_index, coefficient in enumerate(source):
        for kernel_index, value in enumerate(kernel):
            field[source_index + kernel_index] += coefficient * value
    return sum((value * value for value in field), Fraction(0))


def gram_toy_energy(
    source: tuple[Fraction, ...], kernel: tuple[Fraction, ...]
) -> Fraction:
    if not source or not kernel:
        raise ValueError("source and kernel must be nonempty")
    gram = autocorrelation(kernel)
    return sum(
        (
            left * right * gram.get(right_index - left_index, Fraction(0))
            for left_index, left in enumerate(source)
            for right_index, right in enumerate(source)
        ),
        Fraction(0),
    )


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    coefficient_failures = [
        value
        for value in range(1, COEFFICIENT_CAP + 1)
        if beta(value) ** 2 != beta_square_from_euler(value)
    ]
    if coefficient_failures:
        raise ArithmeticError("beta-square Euler product failed")
    ratio = exceptional_residue_ratio()
    if ratio != Fraction(2379, 2278):
        raise ArithmeticError("exceptional Euler-factor residue changed")

    source = tuple(
        Fraction(beta(value), value) for value in range(1, TOY_SOURCE_CAP + 1)
    )
    direct_energy = direct_toy_energy(source, TOY_KERNEL)
    gram_energy = gram_toy_energy(source, TOY_KERNEL)
    if direct_energy != gram_energy or direct_energy < 0:
        raise ArithmeticError("finite exact Gram identity failed")
    gram = autocorrelation(TOY_KERNEL)
    if any(gram[shift] != gram[-shift] for shift in gram):
        raise ArithmeticError("autocorrelation lost evenness")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported_theorem": (
                "K_bd is nonzero compact BV on [0,4log2], and its L1 "
                "boundary field is RH-equivalent"
            ),
        },
        "criterion": {
            "prefix_field": "G_X(t)=sum_(n<=X) beta(n)/sqrt(n)*K_bd(t-log(n))",
            "energy": "E(X)=integral_R |G_X(t)|^2 dt",
            "gram_identity": ("E(X)=sum_(m,n<=X) beta(m)beta(n)/sqrt(mn)*R(log(m/n))"),
            "autocorrelation": "R(u)=integral K_bd(v)K_bd(v+u)dv",
            "ratio_support": "1/16 <= m/n <= 16",
            "equivalence": "RH iff E(X)=X^o(1)",
            "estimate_proved": False,
            "rh_proved": False,
        },
        "diagonal": {
            "dirichlet_series": ("zeta(s)/zeta(2s)*(1+4*67^-s+67^-2s)/(1+67^-s)"),
            "exceptional_residue_ratio": str(ratio),
            "harmonic_sum_constant": "2379/(2278*zeta(2))",
            "conclusion": "diagonal=R(0)*2379/(2278*zeta(2))*log(X)+O(1)",
            "off_diagonal_equivalence": "RH iff |O(X)|=X^o(1)",
        },
        "finite_gram_replay": {
            "source_length": len(source),
            "kernel": [str(value) for value in TOY_KERNEL],
            "autocorrelation": {str(key): str(value) for key, value in gram.items()},
            "direct_energy": str(direct_energy),
            "gram_energy": str(gram_energy),
        },
        "resource_caps": {
            "beta_square_coefficients": COEFFICIENT_CAP,
            "toy_source_terms": TOY_SOURCE_CAP,
            "toy_kernel_cells": len(TOY_KERNEL),
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "conductor_families": 0,
            "l_functions": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
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
