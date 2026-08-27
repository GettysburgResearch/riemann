#!/usr/bin/env python3
"""Bounded exact replay for band-pass assembly and Perron cusp leakage."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
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
    "research/l-families/atlas/function_field/FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md": (
        "105837343b6b8ef148488f492c66da8feae0334a"
    ),
    "research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.py": (
        "53b5a710cb2f6b918958ff7e96801d81e2a0a79c"
    ),
    "research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.json": (
        "efc21abe6b87d16d49b272d0fd0dd65e1f059d57"
    ),
    "tests/test_ffps_boundary_field_near_correlation_criterion.py": (
        "006e1c41f34f4d1e9a8885fb160c7d9886a3a77d"
    ),
}
PREDECESSOR_BLOBS = {
    "05aaabe69060c24c8db4ca33c350e109231960f1": {
        "research/l-families/atlas/function_field/FFPS_BANDPASS_BETA_ENERGY_LADDER.md": (
            "0ac23a6c384a896e50fed21ca7d8bf079c338ac0"
        ),
        "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py": (
            "9ca6db9ad6b0149936efbd0e99f799d89f3cc53a"
        ),
        "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.json": (
            "ff568b48100048f6ad963c7afa23c4ac04c3d291"
        ),
        "tests/test_ffps_bandpass_beta_energy_ladder.py": (
            "6b45ddd02148c437bba375d6dbaf753c938e3375"
        ),
    },
    "afd49590f1a7e70e68054b8932eb9cadfaa62c40": {
        "research/l-families/atlas/function_field/FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md": (
            "21ef8f5215ca349f0efffd52dca1543ef6d988d6"
        ),
        "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py": (
            "8e236e2d77ee047981bc5c14bfaadd1c1cb786c8"
        ),
        "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.json": (
            "1223ab8049492f58cf5e64a25f80d5799aa165f7"
        ),
        "tests/test_ffps_assembled_beta_perron_fourier_bridge.py": (
            "a3abb51a91e719487b85af4c8528898b6724d53d"
        ),
    },
}

EXCEPTIONAL_PRIME = 5
EXCEPTIONAL_COEFFICIENTS = (1, -2, 1)
PAIR_CAP = 40
TOY_BOUNDARY_KERNEL = (Fraction(3), Fraction(-1), Fraction(4), Fraction(2))
REPLAY_ORDER_CAP = 4


def check_source_contract() -> None:
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
    for commit, blobs in PREDECESSOR_BLOBS.items():
        for path, expected in blobs.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"predecessor blob mismatch: {commit}:{path}")


def validate_positive_integer(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")


def mobius(value: int) -> int:
    validate_positive_integer(value)
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


def beta(value: int, prime: int = EXCEPTIONAL_PRIME) -> int:
    validate_positive_integer(value)
    validate_positive_integer(prime)
    return mobius(value) - (mobius(value // prime) if value % prime == 0 else 0)


def convolve(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    if not left or not right:
        raise ValueError("convolution inputs must be nonempty")
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def finite_difference(cells: tuple[Fraction, ...], order: int) -> tuple[Fraction, ...]:
    if not cells:
        raise ValueError("cells must be nonempty")
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or not 1 <= order <= REPLAY_ORDER_CAP
    ):
        raise ValueError("order exceeds the bounded replay cap")
    result = cells
    difference = (Fraction(1), Fraction(-1))
    for _ in range(order):
        result = convolve(result, difference)
    return result


def box_smooth(
    cells: tuple[Fraction, ...], width: int, order: int
) -> tuple[Fraction, ...]:
    if not cells:
        raise ValueError("cells must be nonempty")
    validate_positive_integer(width)
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    box = (Fraction(1, width),) * width
    result = cells
    for _ in range(order):
        result = convolve(result, box)
    return result


def autocorrelation(cells: tuple[Fraction, ...]) -> dict[int, Fraction]:
    if not cells:
        raise ValueError("cells must be nonempty")
    radius = len(cells) - 1
    return {
        shift: sum(
            (
                cells[index] * cells[index + shift]
                for index in range(max(0, -shift), min(len(cells), len(cells) - shift))
            ),
            Fraction(0),
        )
        for shift in range(-radius, radius + 1)
    }


def signed_moment(correlation: dict[int, Fraction], exponent: int) -> Fraction:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    return sum(
        (value * shift**exponent for shift, value in correlation.items()),
        Fraction(0),
    )


def absolute_lag_moment(correlation: dict[int, Fraction], exponent: int) -> Fraction:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    return sum(
        (value * abs(shift) ** exponent for shift, value in correlation.items()),
        Fraction(0),
    )


def cumulative_cells(cells: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if not cells:
        raise ValueError("cells must be nonempty")
    running = Fraction(0)
    cumulative: list[Fraction] = []
    for value in cells[:-1]:
        running += value
        cumulative.append(running)
    if running + cells[-1] != 0:
        raise ValueError("cells must have mean zero")
    return tuple(cumulative)


def leakage_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in range(1, REPLAY_ORDER_CAP + 1):
        bandpass = box_smooth(
            finite_difference(TOY_BOUNDARY_KERNEL, order), width=3, order=1
        )
        correlation = autocorrelation(bandpass)
        zero_moments = [
            signed_moment(correlation, exponent) for exponent in range(2 * order)
        ]
        if any(zero_moments):
            raise ArithmeticError("translation-invariant notch lost order")
        cumulative = cumulative_cells(bandpass)
        primitive_energy = sum((value * value for value in cumulative), Fraction(0))
        absolute_first = absolute_lag_moment(correlation, 1)
        if absolute_first != -2 * primitive_energy or primitive_energy <= 0:
            raise ArithmeticError("absolute-lag primitive identity failed")
        rows.append(
            {
                "difference_order": order,
                "zero_moments": 2 * order,
                "primitive_energy": str(primitive_energy),
                "absolute_first_moment": str(absolute_first),
                "linear_leakage_coefficient": str(-absolute_first / 2),
                "linear_leakage_is_strict": True,
            }
        )
    return rows


def valuation(value: int, prime: int) -> int:
    validate_positive_integer(value)
    validate_positive_integer(prime)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def inverse_square_root_basis(value: int) -> tuple[int, Fraction]:
    validate_positive_integer(value)
    remaining = value
    square = 1
    squarefree = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        square *= prime ** (exponent // 2)
        if exponent % 2:
            squarefree *= prime
        prime += 1
    if remaining > 1:
        squarefree *= remaining
    return squarefree, Fraction(1, square)


def add_radical(
    output: dict[int, Fraction], radicand: int, coefficient: Fraction
) -> None:
    output[radicand] = output.get(radicand, Fraction(0)) + coefficient
    if output[radicand] == 0:
        del output[radicand]


def toy_bandpass_ratio_kernel(left: int, right: int) -> Fraction:
    correlation = autocorrelation(finite_difference(TOY_BOUNDARY_KERNEL, 2))
    shift = valuation(left, 2) - valuation(right, 2)
    return correlation.get(shift, Fraction(0))


def direct_energy() -> tuple[dict[int, Fraction], set[tuple[int, int]]]:
    output: dict[int, Fraction] = {}
    pairs: set[tuple[int, int]] = set()
    for left in range(1, PAIR_CAP + 1):
        left_beta = beta(left)
        if left_beta == 0:
            continue
        for right in range(1, PAIR_CAP + 1):
            right_beta = beta(right)
            if right_beta == 0:
                continue
            pairs.add((left, right))
            radicand, scale = inverse_square_root_basis(left * right)
            add_radical(
                output,
                radicand,
                Fraction(left_beta * right_beta)
                * scale
                * toy_bandpass_ratio_kernel(left, right),
            )
    return output, pairs


def squarefree_away(value: int) -> bool:
    return value % EXCEPTIONAL_PRIME != 0 and mobius(value) != 0


def assembled_energy() -> tuple[dict[int, Fraction], set[tuple[int, int]]]:
    output: dict[int, Fraction] = {}
    pairs: set[tuple[int, int]] = set()
    admissible = [value for value in range(1, PAIR_CAP + 1) if squarefree_away(value)]
    for left_exponent, left_coefficient in enumerate(EXCEPTIONAL_COEFFICIENTS):
        left_power = EXCEPTIONAL_PRIME**left_exponent
        for right_exponent, right_coefficient in enumerate(EXCEPTIONAL_COEFFICIENTS):
            right_power = EXCEPTIONAL_PRIME**right_exponent
            for common in admissible:
                for left_core in admissible:
                    if math.gcd(common, left_core) != 1:
                        continue
                    left = left_power * common * left_core
                    if left > PAIR_CAP:
                        continue
                    for right_core in admissible:
                        if (
                            math.gcd(common, right_core) != 1
                            or math.gcd(left_core, right_core) != 1
                        ):
                            continue
                        right = right_power * common * right_core
                        if right > PAIR_CAP:
                            continue
                        if (left, right) in pairs:
                            raise ArithmeticError(
                                "assembled coordinates were not unique"
                            )
                        pairs.add((left, right))
                        coefficient = (
                            left_coefficient
                            * right_coefficient
                            * mobius(left_core)
                            * mobius(right_core)
                        )
                        if coefficient != beta(left) * beta(right):
                            raise ArithmeticError(
                                "assembled source coefficient changed"
                            )
                        radicand, scale = inverse_square_root_basis(left * right)
                        add_radical(
                            output,
                            radicand,
                            Fraction(coefficient)
                            * scale
                            * toy_bandpass_ratio_kernel(left, right),
                        )
    return output, pairs


def assembled_reindex_panel() -> dict[str, object]:
    direct, direct_pairs = direct_energy()
    assembled, assembled_pairs = assembled_energy()
    if direct_pairs != assembled_pairs or direct != assembled:
        raise ArithmeticError("band-pass assembled reindex failed")
    payload = json.dumps(
        [(key, str(direct[key])) for key in sorted(direct)], separators=(",", ":")
    )
    return {
        "pair_cap": PAIR_CAP,
        "ordered_pairs": len(direct_pairs),
        "radical_dimension": len(direct),
        "radical_sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    }


def barnes_panel() -> dict[str, object]:
    # Exact partial fractions and residues for
    # 1 / ((z/2+v)(z/2-v)). Coefficients are recorded relative to 1/z.
    right_residue = Fraction(-1)
    right_closure_orientation = Fraction(-1)
    left_residue = Fraction(1)
    left_closure_orientation = Fraction(1)
    if right_residue * right_closure_orientation != 1:
        raise ArithmeticError("right Barnes residue normalization failed")
    if left_residue * left_closure_orientation != 1:
        raise ArithmeticError("left Barnes residue normalization failed")
    return {
        "change_of_variables": "z=z1+z2, v=(z1-z2)/2",
        "denominator": "z1*z2=(z/2+v)*(z/2-v)",
        "jacobian_absolute_value": 1,
        "relative_line": "-Re(z)/2 < Re(v) < Re(z)/2",
        "x_positive_pole": "v=z/2",
        "x_negative_pole": "v=-z/2",
        "identity": (
            "(1/(2pi i))*integral_v exp(-v*x)/((z/2+v)*(z/2-v)) dv=exp(-z*abs(x)/2)/z"
        ),
        "residue_coefficient": "1/z on both signs of x",
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blob_count": len(SOURCE_BLOBS),
            "predecessor_blobs": PREDECESSOR_BLOBS,
        },
        "bandpass_assembled_identity": {
            "wavelet": "replace R by R_(r,j) in the complete assembled divisor wavelet",
            "sharp_identity_survives_verbatim": True,
            "rh_equivalent": True,
            "estimate_proved": False,
        },
        "double_perron": {
            "formula": (
                "integral_z1 integral_z2 X^(z1+z2)/(z1*z2) integral_t "
                "Rhat_(r,j)(t) B_beta(1/2+z1-it) B_beta(1/2+z2+it)"
            ),
            "exact_t_zero_notch_retained": True,
            "absolute_region": "Re(z1)>1/2 and Re(z2)>1/2",
            "boundary_estimate_proved": False,
        },
        "barnes_collapse": barnes_panel(),
        "max_tilt_leakage": {
            "identity": "integral abs(x) R(x) dx=-2*||primitive(B)||_2^2",
            "expansion": ("Rhat_z(0)=z*||primitive(B)||_2^2+O_fixed(|z|^2)"),
            "uniform_bound": ("|Rhat_z(t)-Rhat(t)| <= |z|*S/2*exp(|z|S/2)*||B||_1^2"),
            "local_two_variable_shape": (
                "Rhat_z(t)=c_bd^2*t^(2r)+z*A_(r,j)+O_fixed(t^(2r+2)+|z|t^2+|z|^2)"
            ),
            "repeated_notch_improves_z_order": False,
            "crossover": "|t| is of order |z|^(1/(2r)) for positive real z",
            "rows": leakage_rows(),
        },
        "finite_assembled_replay": assembled_reindex_panel(),
        "scope": {
            "asymptotic_estimate": False,
            "perron_contour_shift": False,
            "rh_or_grh_proved": False,
        },
        "resource_caps": {
            "pair_cap": PAIR_CAP,
            "difference_order": REPLAY_ORDER_CAP,
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "l_functions": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    print(rendered, end="")


if __name__ == "__main__":
    main()
