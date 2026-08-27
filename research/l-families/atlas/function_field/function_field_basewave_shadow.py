#!/usr/bin/env python3
"""Exact bounded replay for the complete F_q[T] base-wavelet shadow."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from math import comb, gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md": (
        "31311893b8a7ba708ae7a2813b9c44b920b788a9"
    ),
    "research/l-families/atlas/function_field/FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md": (
        "105837343b6b8ef148488f492c66da8feae0334a"
    ),
    "research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.py": (
        "53b5a710cb2f6b918958ff7e96801d81e2a0a79c"
    ),
}

FIELD_SIZES = (3, 5, 7)
EXCEPTIONAL_DEGREE = 1
MAX_DEGREE = 35
PRODUCT_REPLAY_DEGREE = 8
CONTROL_WEIGHTS = {-2: 1, -1: 2, 0: 3, 1: 2, 2: 1}


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


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def is_prime_power(value: int) -> bool:
    validate_positive_integer(value, "field size")
    for prime in range(2, value + 1):
        if not is_prime(prime) or value % prime:
            continue
        remaining = value
        while remaining % prime == 0:
            remaining //= prime
        return remaining == 1
    return False


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value, "value")
    small: list[int] = []
    large: list[int] = []
    for divisor in range(1, math.isqrt(value) + 1):
        if value % divisor:
            continue
        small.append(divisor)
        if divisor * divisor != value:
            large.append(value // divisor)
    return tuple(small + list(reversed(large)))


def mobius(value: int) -> int:
    validate_positive_integer(value, "value")
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def irreducible_count(field_size: int, degree: int) -> int:
    if not is_prime_power(field_size):
        raise ValueError("field size must be a prime power")
    validate_positive_integer(degree, "degree")
    numerator = sum(
        mobius(divisor) * field_size ** (degree // divisor)
        for divisor in divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible-count numerator lost integrality")
    return numerator // degree


def available_irreducible_count(
    field_size: int, degree: int, exceptional_degree: int
) -> int:
    validate_positive_integer(exceptional_degree, "exceptional degree")
    result = irreducible_count(field_size, degree) - int(degree == exceptional_degree)
    if result < 0:
        raise ArithmeticError("exceptional prime cannot be removed")
    return result


def common_divisors(left_degree: int, right_degree: int) -> tuple[int, ...]:
    if left_degree < 0 or right_degree < 0 or left_degree + right_degree == 0:
        raise ValueError("degrees must be nonnegative and not both zero")
    common = gcd(left_degree, right_degree)
    if common == 0:
        common = max(left_degree, right_degree)
    return divisors(common)


def logarithm_coefficient(
    field_size: int,
    exceptional_degree: int,
    left_degree: int,
    right_degree: int,
) -> Fraction:
    """Coefficient of X^left Y^right in log product_P(1-X^d-Y^d)."""

    total_degree = left_degree + right_degree
    if total_degree == 0:
        return Fraction()
    result = Fraction()
    for degree in common_divisors(left_degree, right_degree):
        left_power = left_degree // degree
        right_power = right_degree // degree
        power = left_power + right_power
        multiplicity = available_irreducible_count(
            field_size, degree, exceptional_degree
        )
        result -= Fraction(multiplicity * comb(power, left_power), power)
    return result


def coefficient_table(
    field_size: int, exceptional_degree: int, degree_cap: int
) -> tuple[tuple[int, ...], ...]:
    """Coefficients of the unweighted bivariate orientation Euler product."""

    if not is_prime_power(field_size):
        raise ValueError("field size must be a prime power")
    validate_positive_integer(exceptional_degree, "exceptional degree")
    validate_positive_integer(degree_cap, "degree cap")
    logarithm = [
        [Fraction() for _ in range(degree_cap + 1)] for _ in range(degree_cap + 1)
    ]
    for left_degree in range(degree_cap + 1):
        for right_degree in range(degree_cap + 1):
            if left_degree + right_degree:
                logarithm[left_degree][right_degree] = logarithm_coefficient(
                    field_size,
                    exceptional_degree,
                    left_degree,
                    right_degree,
                )

    coefficients = [
        [Fraction() for _ in range(degree_cap + 1)] for _ in range(degree_cap + 1)
    ]
    coefficients[0][0] = Fraction(1)
    for total_degree in range(1, 2 * degree_cap + 1):
        left_minimum = max(0, total_degree - degree_cap)
        left_maximum = min(degree_cap, total_degree)
        for left_degree in range(left_minimum, left_maximum + 1):
            right_degree = total_degree - left_degree
            numerator = Fraction()
            for row_degree in range(left_degree + 1):
                for column_degree in range(right_degree + 1):
                    derivative_degree = row_degree + column_degree
                    if derivative_degree == 0:
                        continue
                    numerator += (
                        derivative_degree
                        * logarithm[row_degree][column_degree]
                        * coefficients[left_degree - row_degree][
                            right_degree - column_degree
                        ]
                    )
            coefficients[left_degree][right_degree] = numerator / total_degree

    if any(value.denominator != 1 for row in coefficients for value in row):
        raise ArithmeticError("Euler-product coefficient recurrence lost integrality")
    return tuple(tuple(int(value) for value in row) for row in coefficients)


def truncated_euler_product_table(
    field_size: int, exceptional_degree: int, degree_cap: int
) -> tuple[tuple[int, ...], ...]:
    """Independent finite product replay, truncated in both degree variables."""

    validate_positive_integer(degree_cap, "degree cap")
    table = [[0 for _ in range(degree_cap + 1)] for _ in range(degree_cap + 1)]
    table[0][0] = 1
    for prime_degree in range(1, degree_cap + 1):
        multiplicity = available_irreducible_count(
            field_size, prime_degree, exceptional_degree
        )
        local_terms: list[tuple[int, int, int]] = []
        power_cap = min(multiplicity, 2 * (degree_cap // prime_degree))
        for power in range(power_cap + 1):
            signed_binomial = (-1) ** power * comb(multiplicity, power)
            for left_power in range(power + 1):
                right_power = power - left_power
                left_degree = prime_degree * left_power
                right_degree = prime_degree * right_power
                if left_degree <= degree_cap and right_degree <= degree_cap:
                    local_terms.append(
                        (
                            left_degree,
                            right_degree,
                            signed_binomial * comb(power, left_power),
                        )
                    )
        updated = [[0 for _ in range(degree_cap + 1)] for _ in range(degree_cap + 1)]
        for left_degree in range(degree_cap + 1):
            for right_degree in range(degree_cap + 1):
                current = table[left_degree][right_degree]
                if current == 0:
                    continue
                for delta_left, delta_right, local_value in local_terms:
                    new_left = left_degree + delta_left
                    new_right = right_degree + delta_right
                    if new_left <= degree_cap and new_right <= degree_cap:
                        updated[new_left][new_right] += current * local_value
        table = updated
    return tuple(tuple(row) for row in table)


def axis_coefficient(field_size: int, exceptional_degree: int, degree: int) -> int:
    """Coefficient of (1-qX)/(1-X^e), the exact one-axis specialization."""

    if degree < 0:
        raise ValueError("degree must be nonnegative")
    return int(degree % exceptional_degree == 0) - field_size * int(
        degree >= 1 and (degree - 1) % exceptional_degree == 0
    )


def shell_pair(
    exceptional_degree: int, alpha: int, height: int, degree_difference: int
) -> tuple[int, int] | None:
    """Return (deg A,deg B) for max(alpha*e+deg A,deg B)=height."""

    validate_positive_integer(exceptional_degree, "exceptional degree")
    if isinstance(alpha, bool) or not isinstance(alpha, int) or alpha < 0:
        raise ValueError("alpha must be a nonnegative integer")
    if isinstance(height, bool) or not isinstance(height, int) or height < 0:
        raise ValueError("height must be a nonnegative integer")
    if isinstance(degree_difference, bool) or not isinstance(degree_difference, int):
        raise TypeError("degree difference must be an integer")
    shift = alpha * exceptional_degree
    if degree_difference >= 0:
        left_degree = height - shift
        right_degree = height - degree_difference
    else:
        left_degree = height + degree_difference - shift
        right_degree = height
    if left_degree < 0 or right_degree < 0:
        return None
    return left_degree, right_degree


def sqrt_power_pair(field_size: int, exponent: int) -> tuple[int, int]:
    """Represent q^(exponent/2) as rational + sqrt(q)*coefficient."""

    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    if exponent % 2:
        return 0, field_size ** ((exponent - 1) // 2)
    return field_size ** (exponent // 2), 0


def complete_shell_amplitude(
    coefficients: tuple[tuple[int, ...], ...],
    field_size: int,
    exceptional_degree: int,
    alpha: int,
    height: int,
    weights: dict[int, int],
    *,
    include_channels: bool = True,
) -> dict[str, object]:
    """Exact q^height-scaled amplitude in Q(sqrt(q))."""

    rational_part = 0
    radical_part = 0
    channels: list[dict[str, object]] = []
    cap = len(coefficients) - 1
    for degree_difference, weight in sorted(weights.items()):
        pair = shell_pair(exceptional_degree, alpha, height, degree_difference)
        if pair is None:
            continue
        left_degree, right_degree = pair
        if left_degree > cap or right_degree > cap:
            raise ValueError("coefficient table is too small for shell")
        coefficient = coefficients[left_degree][right_degree]
        half_power = alpha * exceptional_degree + abs(degree_difference)
        rational_multiplier, radical_multiplier = sqrt_power_pair(
            field_size, half_power
        )
        rational_part += weight * coefficient * rational_multiplier
        radical_part += weight * coefficient * radical_multiplier
        channels.append(
            {
                "degree_difference": degree_difference,
                "left_degree": left_degree,
                "right_degree": right_degree,
                "unweighted_coefficient": coefficient,
                "weight": weight,
            }
        )
    approximate = (
        rational_part + radical_part * math.sqrt(field_size)
    ) / field_size**height
    result: dict[str, object] = {
        "alpha": alpha,
        "height": height,
        "q_to_height_times_amplitude": {
            "rational_part": rational_part,
            "sqrt_q_part": radical_part,
        },
        "approximate_amplitude": approximate,
    }
    if include_channels:
        result["channels"] = channels
    return result


def local_factorization_certificate() -> dict[str, object]:
    checks = 0
    for left in (Fraction(1, 11), Fraction(2, 13), Fraction(-1, 17)):
        for right in (Fraction(1, 19), Fraction(-3, 23), Fraction(2, 29)):
            base = 1 - left - right
            factored_base = (1 - left) * (1 - right) * (1 - left * right)
            defect = left * right * (left + right - left * right)
            if factored_base - base != defect:
                raise ArithmeticError("local cubic factorization defect changed")
            checks += 1
    return {
        "exact_checks": checks,
        "identity": ("(1-a)(1-b)(1-ab)-(1-a-b)=ab(a+b-ab)"),
        "residual_starts_in_mixed_total_degree": 3,
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    factorization = local_factorization_certificate()
    field_rows: list[dict[str, object]] = []
    for field_size in FIELD_SIZES:
        coefficients = coefficient_table(field_size, EXCEPTIONAL_DEGREE, MAX_DEGREE)
        recurrence_control = coefficient_table(
            field_size, EXCEPTIONAL_DEGREE, PRODUCT_REPLAY_DEGREE
        )
        product_control = truncated_euler_product_table(
            field_size, EXCEPTIONAL_DEGREE, PRODUCT_REPLAY_DEGREE
        )
        if recurrence_control != product_control:
            raise ArithmeticError("recurrence and truncated Euler product disagree")
        for degree in range(MAX_DEGREE + 1):
            if coefficients[degree][0] != axis_coefficient(
                field_size, EXCEPTIONAL_DEGREE, degree
            ):
                raise ArithmeticError("one-axis zeta specialization failed")
            if coefficients[0][degree] != coefficients[degree][0]:
                raise ArithmeticError("orientation coefficients lost symmetry")

        sample_heights = (8, 20, 35)
        shell_rows = [
            complete_shell_amplitude(
                coefficients,
                field_size,
                EXCEPTIONAL_DEGREE,
                alpha,
                height,
                CONTROL_WEIGHTS,
                include_channels=False,
            )
            for alpha in (0, 1, 2)
            for height in sample_heights
        ]
        field_rows.append(
            {
                "field_size": field_size,
                "irreducible_counts_degrees_1_to_8": [
                    irreducible_count(field_size, degree) for degree in range(1, 9)
                ],
                "diagonal_coefficients_degrees_0_to_12": [
                    coefficients[degree][degree] for degree in range(13)
                ],
                "shell_rows": shell_rows,
            }
        )

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported_object": (
                "u=1 divisor wavelet sum over squarefree exceptional-prime-free "
                "products, with compact ratio autocorrelation"
            ),
        },
        "definition": {
            "orientation_series": (
                "F_q,e(X,Y)=prod_(P!=pi)(1-q^(-deg(P)/2)X^deg(P)-q^(-deg(P)/2)Y^deg(P))"
            ),
            "coefficient_interpretation": (
                "[X^iY^j]F=sum_(A,B monic squarefree coprime, pi not divide AB,"
                " deg A=i,deg B=j) mu(A)mu(B)/sqrt(|AB|)"
            ),
            "height_shell": (
                "max(alpha*deg(pi)+deg(A),deg(B))=h; a norm-factor-two shell "
                "contains at most one such h for q>=3"
            ),
        },
        "factorization": {
            "formula": (
                "F=((1-sqrt(q)X)(1-sqrt(q)Y)(1-XY))/"
                "((1-q^(-e/2)X^e)(1-q^(-e/2)Y^e)"
                "(1-q^(-e)(XY)^e))*J"
            ),
            "local_certificate": factorization,
            "J_absolute_convergence": (
                "on every closed bidisc |X|,|Y|<=r with r^3<sqrt(q)"
            ),
            "zero_frequency_channel": (
                "the diagonal Euler channel is the exact zero 1-XY, not a pole"
            ),
        },
        "theorem": {
            "statement": (
                "For fixed q,e,alpha and any finitely supported sampled ratio "
                "kernel, the complete degree-h base-wavelet shell is "
                "O_epsilon(q^(-(1/3-epsilon)h)) for every epsilon>0."
            ),
            "energy_consequence": (
                "the squared shell shadow is exponentially summable and hence "
                "satisfies every subpower complete-shell bound"
            ),
            "proof_grade": "PROVED BY EXACT EULER FACTORIZATION AND CAUCHY",
            "number_field_inference": False,
        },
        "finite_replay": {
            "control_kernel": CONTROL_WEIGHTS,
            "control_kernel_scope": (
                "rational positive-definite degree-lattice control only; theorem "
                "is uniform over the actual finite sampled autocorrelation values"
            ),
            "field_rows": field_rows,
            "recurrence_product_match_degree": PRODUCT_REPLAY_DEGREE,
        },
        "scope_firewall": {
            "degeneracy": (
                "polynomial norm ratios remember only degree, and the complete "
                "monic family has zeta polynomial 1-qu"
            ),
            "not_transferred": (
                "positive-genus Jacobian factors, incomplete owner/Boolean shells, "
                "nonzero PRIMCAR incidence modes, or number-field ratios"
            ),
            "rh_proved": False,
            "waveprimcar_proved": False,
        },
        "resource_caps": {
            "field_sizes": list(FIELD_SIZES),
            "maximum_degree": MAX_DEGREE,
            "polynomial_enumeration": 0,
            "point_counts": 0,
            "curves": 0,
            "l_functions": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    if args.check:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
