#!/usr/bin/env python3
"""Bounded exact replay for the assembled beta Perron--Fourier bridge."""

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
    "research/l-families/atlas/function_field/FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md": (
        "31311893b8a7ba708ae7a2813b9c44b920b788a9"
    ),
}

EXCEPTIONAL_PRIME = 67
EXCEPTIONAL_COEFFICIENTS = (1, -2, 1)
REPLAY_EXCEPTIONAL_PRIME = 5
REPLAY_SOURCE_CAP = 72
TOY_BOUNDARY_KERNEL = (Fraction(1), Fraction(2), Fraction(1))


def check_source_blobs() -> None:
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
            raise RuntimeError(f"frozen source blob mismatch: {path}")


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


def exceptional_valuation(value: int, prime: int) -> tuple[int, int]:
    validate_positive_integer(value)
    validate_positive_integer(prime)
    exponent = 0
    residue = value
    while residue % prime == 0:
        exponent += 1
        residue //= prime
    return exponent, residue


def beta(value: int, prime: int = EXCEPTIONAL_PRIME) -> int:
    validate_positive_integer(value)
    return mobius(value) - (mobius(value // prime) if value % prime == 0 else 0)


def is_squarefree_away(value: int, prime: int) -> bool:
    return value % prime != 0 and mobius(value) != 0


def inverse_square_root_basis(value: int) -> tuple[int, Fraction]:
    """Return k,q with 1/sqrt(value)=q/sqrt(k) and k squarefree."""
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


def ratio_kernel(left: int, right: int) -> Fraction:
    """A symmetric exact compact-ratio toy kernel."""
    validate_positive_integer(left)
    validate_positive_integer(right)
    common = math.gcd(left, right)
    reduced_left = left // common
    reduced_right = right // common
    if reduced_left > 4 * reduced_right or reduced_right > 4 * reduced_left:
        return Fraction(0)
    return Fraction(1, reduced_left + reduced_right)


def add_radical_term(
    accumulator: dict[int, Fraction], radicand: int, coefficient: Fraction
) -> None:
    accumulator[radicand] = accumulator.get(radicand, Fraction(0)) + coefficient
    if accumulator[radicand] == 0:
        del accumulator[radicand]


def direct_prefix_energy(
    cap: int = REPLAY_SOURCE_CAP, prime: int = REPLAY_EXCEPTIONAL_PRIME
) -> tuple[dict[int, Fraction], set[tuple[int, int]]]:
    validate_positive_integer(cap)
    pairs: set[tuple[int, int]] = set()
    result: dict[int, Fraction] = {}
    for left in range(1, cap + 1):
        left_beta = beta(left, prime)
        if left_beta == 0:
            continue
        for right in range(1, cap + 1):
            right_beta = beta(right, prime)
            if right_beta == 0:
                continue
            pairs.add((left, right))
            radicand, scale = inverse_square_root_basis(left * right)
            add_radical_term(
                result,
                radicand,
                Fraction(left_beta * right_beta) * scale * ratio_kernel(left, right),
            )
    return result, pairs


def assembled_prefix_energy(
    cap: int = REPLAY_SOURCE_CAP, prime: int = REPLAY_EXCEPTIONAL_PRIME
) -> tuple[dict[int, Fraction], set[tuple[int, int]], int]:
    """Rebuild the prefix through (i,j,g,a,b) primitive coordinates."""
    validate_positive_integer(cap)
    pairs: set[tuple[int, int]] = set()
    result: dict[int, Fraction] = {}
    coefficient_checks = 0
    admissible = [
        value for value in range(1, cap + 1) if is_squarefree_away(value, prime)
    ]
    for left_exponent, left_exceptional in enumerate(EXCEPTIONAL_COEFFICIENTS):
        left_power = prime**left_exponent
        for right_exponent, right_exceptional in enumerate(EXCEPTIONAL_COEFFICIENTS):
            right_power = prime**right_exponent
            for common in admissible:
                if left_power * common > cap or right_power * common > cap:
                    continue
                left_cores = [
                    value
                    for value in admissible
                    if left_power * common * value <= cap
                    and math.gcd(value, common) == 1
                ]
                right_cores = [
                    value
                    for value in admissible
                    if right_power * common * value <= cap
                    and math.gcd(value, common) == 1
                ]
                for left_core in left_cores:
                    for right_core in right_cores:
                        if math.gcd(left_core, right_core) != 1:
                            continue
                        left = left_power * common * left_core
                        right = right_power * common * right_core
                        if (left, right) in pairs:
                            raise ArithmeticError(
                                "primitive coordinates were not unique"
                            )
                        pairs.add((left, right))
                        source_product = (
                            left_exceptional
                            * right_exceptional
                            * mobius(left_core)
                            * mobius(right_core)
                        )
                        if source_product != beta(left, prime) * beta(right, prime):
                            raise ArithmeticError("assembled beta coefficient mismatch")
                        coefficient_checks += 1
                        radicand, scale = inverse_square_root_basis(left * right)
                        add_radical_term(
                            result,
                            radicand,
                            Fraction(source_product)
                            * scale
                            * ratio_kernel(left, right),
                        )
    return result, pairs, coefficient_checks


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value)
    return tuple(
        candidate for candidate in range(1, value + 1) if value % candidate == 0
    )


def harmonic_common_factor(bound: int, primitive_product: int, prime: int) -> Fraction:
    """The literal finite H_N(bound) from the displayed assembled wavelet."""
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("bound must be a nonnegative integer")
    validate_positive_integer(primitive_product)
    validate_positive_integer(prime)
    return sum(
        (
            Fraction(1, common)
            for common in range(1, bound + 1)
            if is_squarefree_away(common, prime)
            and math.gcd(common, primitive_product) == 1
        ),
        Fraction(0),
    )


def collapsed_wavelet_prefix_energy(
    cap: int = REPLAY_SOURCE_CAP, prime: int = REPLAY_EXCEPTIONAL_PRIME
) -> tuple[dict[int, Fraction], int, int]:
    """Replay the displayed N/divisor/H_N wavelet without source-pair loops."""
    validate_positive_integer(cap)
    validate_positive_integer(prime)
    result: dict[int, Fraction] = {}
    nonzero_orientations = 0
    primitive_products = 0
    for primitive_product in range(1, cap * cap + 1):
        if not is_squarefree_away(primitive_product, prime):
            continue
        used_product = False
        primitive_sign = mobius(primitive_product)
        for left_exponent, left_exceptional in enumerate(EXCEPTIONAL_COEFFICIENTS):
            left_power = prime**left_exponent
            for right_exponent, right_exceptional in enumerate(
                EXCEPTIONAL_COEFFICIENTS
            ):
                right_power = prime**right_exponent
                exceptional_product = left_exceptional * right_exceptional
                radicand, scale = inverse_square_root_basis(
                    (prime ** (left_exponent + right_exponent)) * primitive_product
                )
                for left_core in divisors(primitive_product):
                    right_core = primitive_product // left_core
                    endpoint = max(left_power * left_core, right_power * right_core)
                    common_bound = cap // endpoint
                    if common_bound < 1:
                        continue
                    kernel = ratio_kernel(
                        left_power * left_core, right_power * right_core
                    )
                    if kernel == 0:
                        continue
                    harmonic = harmonic_common_factor(
                        common_bound, primitive_product, prime
                    )
                    if harmonic == 0:
                        continue
                    used_product = True
                    nonzero_orientations += 1
                    add_radical_term(
                        result,
                        radicand,
                        Fraction(primitive_sign * exceptional_product)
                        * scale
                        * kernel
                        * harmonic,
                    )
        if used_product:
            primitive_products += 1
    return result, primitive_products, nonzero_orientations


def serialize_radical_sum(values: dict[int, Fraction]) -> list[tuple[int, str]]:
    return [(key, str(values[key])) for key in sorted(values)]


def radical_digest(values: dict[int, Fraction]) -> str:
    payload = json.dumps(serialize_radical_sum(values), separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


Polynomial = dict[tuple[int, int], int]


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    product: Polynomial = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            exponent = (left_x + right_x, left_y + right_y)
            product[exponent] = product.get(exponent, 0) + (
                left_coefficient * right_coefficient
            )
    return {
        exponent: coefficient
        for exponent, coefficient in product.items()
        if coefficient
    }


def local_factor_panel() -> dict[str, object]:
    primitive_states: Polynomial = {
        (0, 0): 1,
        (1, 1): 1,
        (1, 0): -1,
        (0, 1): -1,
    }
    factored = polynomial_multiply({(0, 0): 1, (1, 0): -1}, {(0, 0): 1, (0, 1): -1})
    if primitive_states != factored:
        raise ArithmeticError("generic local state factorization failed")

    exceptional_one_variable = {0: 1, 1: -2, 2: 1}
    expected_one_variable = {0: 1, 1: -2, 2: 1}
    if exceptional_one_variable != expected_one_variable:
        raise ArithmeticError("exceptional source polynomial changed")
    exceptional_pair: Polynomial = {
        (left, right): left_coefficient * right_coefficient
        for left, left_coefficient in exceptional_one_variable.items()
        for right, right_coefficient in exceptional_one_variable.items()
    }
    exceptional_factored = polynomial_multiply(
        polynomial_multiply({(0, 0): 1, (1, 0): -1}, {(0, 0): 1, (1, 0): -1}),
        polynomial_multiply({(0, 0): 1, (0, 1): -1}, {(0, 0): 1, (0, 1): -1}),
    )
    if exceptional_pair != exceptional_factored:
        raise ArithmeticError("exceptional local square factorization failed")
    return {
        "generic_states": {
            f"x^{left}y^{right}": coefficient
            for (left, right), coefficient in sorted(primitive_states.items())
        },
        "generic_factorization": "1+xy-x-y=(1-x)(1-y)",
        "exceptional_coefficients": list(EXCEPTIONAL_COEFFICIENTS),
        "exceptional_factorization": "1-2x+x^2=(1-x)^2",
        "pair_factorization": "(1-x)^2(1-y)^2",
    }


def finite_difference(cells: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if not cells:
        raise ValueError("cells must be nonempty")
    result = [Fraction(0)] * (len(cells) + 1)
    for index, value in enumerate(cells):
        result[index] += value
        result[index + 1] -= value
    return tuple(result)


def repeated_difference(
    cells: tuple[Fraction, ...], order: int
) -> tuple[Fraction, ...]:
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    result = cells
    for _ in range(order):
        result = finite_difference(result)
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


def correlation_moment(correlation: dict[int, Fraction], exponent: int) -> Fraction:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    return sum(
        (Fraction(shift**exponent) * value for shift, value in correlation.items()),
        Fraction(0),
    )


def notch_tilt_panel() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for order in (1, 2, 3):
        kernel = repeated_difference(TOY_BOUNDARY_KERNEL, order)
        correlation = autocorrelation(kernel)
        vanishing = [
            correlation_moment(correlation, exponent) for exponent in range(2 * order)
        ]
        if any(vanishing):
            raise ArithmeticError("finite-difference autocorrelation notch lost order")
        tilted = sum(
            (
                value * Fraction(1, 2) ** abs(shift)
                for shift, value in correlation.items()
            ),
            Fraction(0),
        )
        rows.append(
            {
                "difference_order": order,
                "kernel": [str(value) for value in kernel],
                "zero_moments": 2 * order,
                "absolute_tilt_at_one_half": str(tilted),
                "tilt_refills_zero_mode": tilted != 0,
            }
        )
    return {
        "rows": rows,
        "scope": (
            "the exact t=0 notch survives translation-invariant Fourier analysis; "
            "a nonconstant max/Perron tilt can refill it and must be controlled"
        ),
    }


def finite_reindex_panel() -> dict[str, object]:
    direct, direct_pairs = direct_prefix_energy()
    assembled, assembled_pairs, coefficient_checks = assembled_prefix_energy()
    if direct_pairs != assembled_pairs:
        missing = sorted(direct_pairs.symmetric_difference(assembled_pairs))[:5]
        raise ArithmeticError(f"assembled pair bijection failed: {missing}")
    if direct != assembled:
        raise ArithmeticError("assembled radical energy differs from direct energy")
    collapsed, primitive_products, nonzero_orientations = (
        collapsed_wavelet_prefix_energy()
    )
    if direct != collapsed:
        raise ArithmeticError(
            "collapsed N/divisor/H_N wavelet differs from direct energy"
        )
    return {
        "exceptional_prime": REPLAY_EXCEPTIONAL_PRIME,
        "source_cap": REPLAY_SOURCE_CAP,
        "ordered_source_pairs": len(direct_pairs),
        "coefficient_checks": coefficient_checks,
        "radical_basis_dimension": len(direct),
        "radical_sum_sha256": radical_digest(direct),
        "collapsed_wavelet_primitive_products": primitive_products,
        "collapsed_wavelet_nonzero_orientations": nonzero_orientations,
        "collapsed_wavelet_sha256": radical_digest(collapsed),
        "sample_radical_rows": [
            {"radicand": radicand, "coefficient": coefficient}
            for radicand, coefficient in serialize_radical_sum(direct)[:8]
        ],
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    return {
        "source_provenance": {
            "commit": SOURCE_COMMIT,
            "blob_count": len(SOURCE_BLOBS),
        },
        "assembled_identity": {
            "beta_series": "B_beta(w)=(1-67^(-w))/zeta(w)",
            "primitive_coordinates": "m=67^i*g*a, n=67^j*g*b",
            "one_variable_coordinate": "N=a*b with mu(a)mu(b)=mu(N)",
            "rh_equivalent": True,
            "estimate_proved": False,
        },
        "perron_fourier": {
            "s": "s=(1+z)/2",
            "tilted_kernel": "R_z(x)=R(x)exp(-z|x|/2)",
            "dirichlet_product": "B_beta(s-it)B_beta(s+it)",
            "absolute_convergence": "Re(z)>1",
            "boundary_contour_estimate_proved": False,
        },
        "local_factor": local_factor_panel(),
        "finite_reindex": finite_reindex_panel(),
        "notch_tilt_firewall": notch_tilt_panel(),
        "open_gate": {
            "name": "ASMPERRON",
            "target": (
                "control the signed Perron--Fourier integral near Re(z)=0 "
                "without taking absolute values across t, channels, or common-factor states"
            ),
            "rh_proved": False,
            "grh_proved": False,
        },
        "resource_caps": {
            "finite_source_cap": REPLAY_SOURCE_CAP,
            "finite_exceptional_prime": REPLAY_EXCEPTIONAL_PRIME,
            "zeta_zeros": 0,
            "prime_ranges": 0,
            "curve_or_point_enumeration": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
