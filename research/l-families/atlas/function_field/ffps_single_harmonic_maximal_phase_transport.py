#!/usr/bin/env python3
"""Exact bounded replay for single-harmonic maximal phase transport."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "ece0694b29dfc6cd335a8f9da20fe141141d607b"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_CRITICAL_BETA_SPECTRAL_WITNESS_PRINCIPLE.md": (
        "2e3e0b395e3162e6b73bab5c06ea94e39a360a80"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.py": (
        "488f2fa28524ddf1fbb9c5d16053b6d4cd3cbb74"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_spectral_witness_principle.json": (
        "d48dd56093fb4782308bda622f0d5041f2256a16"
    ),
    "tests/test_ffps_critical_beta_spectral_witness_principle.py": (
        "71c7b5222b73cd2bd5d8649b3cacf208fa68c2a5"
    ),
    "research/l-families/atlas/function_field/FFPS_CRITICAL_LATTICE_FIRST_HARMONIC_FIREWALL.md": (
        "67b6bf8ec69a77b017dab21124bef117fc461f50"
    ),
    "research/l-families/atlas/function_field/ffps_critical_lattice_first_harmonic_firewall.py": (
        "114eb2a3d7d98e99a3cfb23788f519ea20f6698e"
    ),
    "research/l-families/atlas/function_field/ffps_critical_lattice_first_harmonic_firewall.json": (
        "63afdd65bc764b131cd0c6b17caef7585ef7c6bd"
    ),
    "tests/test_ffps_critical_lattice_first_harmonic_firewall.py": (
        "fc2c4992e2aa38ad125340b3c100c4e58708bac5"
    ),
}

TOY_PREFIX_CAP = 12
TOY_SCALE_DEPTH = 10
TOY_SCALE_MODULUS = Fraction(1, 5)

Gaussian = tuple[Fraction, Fraction]


def check_source_contract() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {path}")


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gsub(left: Gaussian, right: Gaussian) -> Gaussian:
    return gadd(left, gneg(right))


def gmul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gconjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def gpower(value: Gaussian, exponent: int) -> Gaussian:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    result = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        result = gmul(result, value)
    return result


def prefix_sums(values: tuple[Gaussian, ...]) -> tuple[Gaussian, ...]:
    total = (Fraction(0), Fraction(0))
    rows = []
    for value in values:
        total = gadd(total, value)
        rows.append(total)
    return tuple(rows)


def direct_twisted_sum(
    coefficients: tuple[Gaussian, ...],
    multipliers: tuple[Gaussian, ...],
    height: int,
) -> Gaussian:
    if (
        len(coefficients) != len(multipliers)
        or isinstance(height, bool)
        or not isinstance(height, int)
        or not 1 <= height <= len(coefficients)
    ):
        raise ValueError("coefficient, multiplier, and height shapes must agree")
    total = (Fraction(0), Fraction(0))
    for coefficient, multiplier in zip(
        coefficients[:height], multipliers[:height], strict=True
    ):
        total = gadd(total, gmul(coefficient, multiplier))
    return total


def abel_twisted_sum(
    coefficients: tuple[Gaussian, ...],
    multipliers: tuple[Gaussian, ...],
    height: int,
) -> Gaussian:
    if (
        len(coefficients) != len(multipliers)
        or isinstance(height, bool)
        or not isinstance(height, int)
        or not 1 <= height <= len(coefficients)
    ):
        raise ValueError("coefficient, multiplier, and height shapes must agree")
    prefixes = prefix_sums(coefficients)
    total = gmul(prefixes[height - 1], multipliers[height - 1])
    for index in range(height - 1):
        total = gadd(
            total,
            gmul(prefixes[index], gsub(multipliers[index], multipliers[index + 1])),
        )
    return total


def phase_transport_panel() -> dict[str, object]:
    coefficients = tuple(
        (
            Fraction(((-1) ** index) * (index + 2), index + 1),
            Fraction(index - 2, index + 3),
        )
        for index in range(TOY_PREFIX_CAP)
    )
    unit = (Fraction(3, 5), Fraction(4, 5))
    multipliers = tuple(gpower(unit, index + 1) for index in range(TOY_PREFIX_CAP))
    twisted_coefficients = tuple(
        gmul(coefficient, multiplier)
        for coefficient, multiplier in zip(coefficients, multipliers, strict=True)
    )
    inverse_multipliers = tuple(gconjugate(value) for value in multipliers)
    rows = []
    for height in range(1, TOY_PREFIX_CAP + 1):
        direct = direct_twisted_sum(coefficients, multipliers, height)
        if abel_twisted_sum(coefficients, multipliers, height) != direct:
            raise ArithmeticError("forward Abel phase identity changed")
        untwisted = direct_twisted_sum(
            twisted_coefficients, inverse_multipliers, height
        )
        if (
            abel_twisted_sum(twisted_coefficients, inverse_multipliers, height)
            != untwisted
        ):
            raise ArithmeticError("reverse Abel phase identity changed")
        if untwisted != prefix_sums(coefficients)[height - 1]:
            raise ArithmeticError("phase demodulation changed")
        rows.append(
            {
                "height": height,
                "forward_identity": True,
                "reverse_identity": True,
            }
        )
    return {
        "rows": rows,
        "unit_phase": [str(value) for value in unit],
        "theorem_bound": (
            "(1+|t|*log X)^(-1) max_Y|F_Y(0)|"
            "<=max_Y|F_Y(t)|<=(1+|t|*log X) max_Y|F_Y(0)|"
        ),
        "fixed_harmonic_cost": "1+2*pi*|h|",
    }


def scale_filter(values: tuple[Gaussian, ...], omega: Gaussian) -> tuple[Gaussian, ...]:
    if not values:
        raise ValueError("scale sequence must be nonempty")
    zero = (Fraction(0), Fraction(0))
    return tuple(
        gsub(
            value,
            gmul(omega, values[index + 1] if index + 1 < len(values) else zero),
        )
        for index, value in enumerate(values)
    )


def inverse_scale_filter(
    values: tuple[Gaussian, ...], omega: Gaussian
) -> tuple[Gaussian, ...]:
    if not values:
        raise ValueError("scale sequence must be nonempty")
    rows = []
    for index in range(len(values)):
        total = (Fraction(0), Fraction(0))
        power = (Fraction(1), Fraction(0))
        for offset in range(len(values) - index):
            total = gadd(total, gmul(power, values[index + offset]))
            power = gmul(power, omega)
        rows.append(total)
    return tuple(rows)


def beta_zero_scale_panel() -> dict[str, object]:
    ordinary = tuple(
        (
            Fraction((index + 1) * (index + 3), 2 * index + 1),
            Fraction(((-1) ** index) * (index + 2), index + 2),
        )
        for index in range(TOY_SCALE_DEPTH)
    )
    omega = (TOY_SCALE_MODULUS, Fraction(0))
    beta = scale_filter(ordinary, omega)
    if inverse_scale_filter(beta, omega) != ordinary:
        raise ArithmeticError("beta zero-frequency scale inverse changed")
    return {
        "depth": TOY_SCALE_DEPTH,
        "toy_modulus": str(TOY_SCALE_MODULUS),
        "reconstruction": True,
        "theorem_bounds": (
            "(1-67^(-1/2))*Msharp_max<=D_zero_max<=(1+67^(-1/2))*Msharp_max"
        ),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imports": (
                "common-period critical witness lattice, fixed-harmonic weight "
                "asymptotic, and duplicate-67 scale identity"
            ),
        },
        "classical_input": {
            "status": "IMPORTED CLASSICAL MERTENS CRITERION",
            "statement": ("RH iff sup_(1<=Y<=X)|sum_(n<=Y)mu(n)|=X^(1/2+o(1))"),
            "weighted_form": ("RH iff sup_(1<=Y<=X)|sum_(n<=Y)mu(n)/sqrt(n)|=X^o(1)"),
            "beta_form": ("RH iff sup_(1<=Y<=X)|D_Y(0)|=X^o(1)"),
        },
        "phase_transport": {
            "definition": "F_Y(t)=sum_(n<=Y)a_n*n^(-it)",
            "two_sided_maximal_bound": (
                "(1+|t|logX)^(-1)F_zero_max<=F_t_max<=(1+|t|logX)F_zero_max"
            ),
            "proof": (
                "discrete Abel summation and total variation "
                "sum_(n<Y)|n^(-it)-(n+1)^(-it)|<=|t|logY"
            ),
            "common_lattice_frequency": "t_(h,X)=2*pi*h/L_X",
            "fixed_harmonic_constant": ("|t_(h,X)|logX<2*pi*|h| for fixed nonzero h"),
        },
        "single_harmonic_equivalence": {
            "raw_target": ("sup_(1<=Y<=X)|D_Y(t_(h,X))|^2=X^o(1)"),
            "weighted_target": ("w_(h,X)*sup_(1<=Y<=X)|D_Y(t_(h,X))|^2=X^o(1)"),
            "weight": "w_(h,X)=|Bhat(t_(h,X))|^2/L_X",
            "weight_asymptotic": ("w_(h,X)~K_0^2*(2*pi*|h|)^(2r)*L_X^(-(2r+1))"),
            "theorem": (
                "for every fixed nonzero h and fixed kernel order r, "
                "RH iff either the raw or weighted maximal target holds"
            ),
            "minimal_window": (
                "inside the kernel-weighted retained lattice, one nonzero "
                "guarded lattice harmonic; k=0 has zero weight"
            ),
        },
        "load_bearing_scope": {
            "one_common_period_before_prefix_supremum": True,
            "maximal_prefix_assembly": True,
            "endpoint_only_first_harmonic_equivalence": False,
            "dyadic_endpoint_replacement_proved": False,
            "moving_kernel_order": False,
            "actual_signed_beta_source": True,
            "raw_central_beta_prefix_is_rh_equivalent": True,
            "rh_proved": False,
        },
        "bounded_replay": {
            "phase_transport": phase_transport_panel(),
            "beta_zero_scale": beta_zero_scale_panel(),
        },
        "resource_caps": {
            "toy_prefixes": TOY_PREFIX_CAP,
            "toy_scale_depth": TOY_SCALE_DEPTH,
            "floating_point_operations": 0,
            "zeta_zeros": 0,
            "large_matrices": 0,
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
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
