#!/usr/bin/env python3
"""Bounded exact replay for Frobenius-graph extension-tower aliasing."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_BLOBS = {
    (
        "e3903136912402a969abee7bfcf1ad5f9dfbd1a0",
        "research/l-families/atlas/function_field/FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md",
    ): "19939eb240ca6b2b6d5221954cec76fe0f5c4f9c",
    (
        "05da4d1705d994dd02d650f321196f8464034ba8",
        "research/l-families/atlas/function_field/FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md",
    ): "c79e52ebf0099fe416bc2c79dcb041cc21e025fb",
    (
        "98af0db6e",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
}

BASE_FIELD_SIZE = 2
MAX_MATRIX_EXTENSION_DEGREE = 5

Matrix = tuple[tuple[Fraction, ...], ...]


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{label} must be an integer")
    if value < 1:
        raise ValueError(f"{label} must be positive")


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value, "value")
    small: list[int] = []
    large: list[int] = []
    candidate = 1
    while candidate * candidate <= value:
        if value % candidate == 0:
            small.append(candidate)
            if candidate * candidate != value:
                large.append(value // candidate)
        candidate += 1
    return tuple(small + list(reversed(large)))


def mobius(value: int) -> int:
    validate_positive_integer(value, "value")
    remaining = value
    prime_count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_count += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def euler_phi(value: int) -> int:
    validate_positive_integer(value, "value")
    result = value
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result -= result // prime
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


def frobenius_cycle_counts(base_size: int, extension_degree: int) -> dict[int, int]:
    validate_positive_integer(base_size, "base size")
    validate_positive_integer(extension_degree, "extension degree")
    if base_size < 2:
        raise ValueError("base size must be at least two")
    counts: dict[int, int] = {}
    for degree in divisors(extension_degree):
        exact_elements = sum(
            mobius(degree // subdegree) * base_size**subdegree
            for subdegree in divisors(degree)
        )
        if exact_elements % degree:
            raise ArithmeticError(
                "exact-degree element count is not divisible by degree"
            )
        counts[degree] = exact_elements // degree
    if (
        sum(degree * count for degree, count in counts.items())
        != base_size**extension_degree
    ):
        raise ArithmeticError("Frobenius cycle counts do not fill the extension field")
    return counts


def frobenius_permutation(base_size: int, extension_degree: int) -> Matrix:
    counts = frobenius_cycle_counts(base_size, extension_degree)
    size = base_size**extension_degree
    image = [0] * size
    cursor = 0
    for cycle_length, cycle_count in counts.items():
        for _ in range(cycle_count):
            for offset in range(cycle_length):
                image[cursor + offset] = cursor + (offset + 1) % cycle_length
            cursor += cycle_length
    if cursor != size:
        raise ArithmeticError("abstract Frobenius permutation has the wrong size")
    return tuple(
        tuple(Fraction(int(row == image[column])) for column in range(size))
        for row in range(size)
    )


def identity(size: int) -> Matrix:
    validate_positive_integer(size, "matrix size")
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(
        len(left_row) != len(right_row)
        for left_row, right_row in zip(left, right, strict=True)
    ):
        raise ValueError("matrix shapes must agree")
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def matrix_scale(matrix: Matrix, scalar: Fraction | int) -> Matrix:
    scalar = Fraction(scalar)
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("matrix product has incompatible shapes")
    columns = tuple(zip(*right, strict=True))
    return tuple(
        tuple(
            sum((a * b for a, b in zip(row, column, strict=True)), Fraction(0))
            for column in columns
        )
        for row in left
    )


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("matrix exponent must be an integer")
    if exponent < 0:
        raise ValueError("matrix exponent must be nonnegative")
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix power requires a nonempty square matrix")
    result = identity(len(matrix))
    base = matrix
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = matrix_multiply(result, base)
        remaining //= 2
        if remaining:
            base = matrix_multiply(base, base)
    return result


def matrix_rank(matrix: Matrix) -> int:
    if not matrix or not matrix[0]:
        return 0
    column_count = len(matrix[0])
    working = [list(row) for row in matrix]
    rank = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, len(working)) if working[row][column]),
            None,
        )
        if pivot is None:
            continue
        working[rank], working[pivot] = working[pivot], working[rank]
        pivot_value = working[rank][column]
        working[rank] = [value / pivot_value for value in working[rank]]
        for row in range(len(working)):
            if row == rank or not working[row][column]:
                continue
            multiplier = working[row][column]
            working[row] = [
                current - multiplier * pivot_current
                for current, pivot_current in zip(
                    working[row], working[rank], strict=True
                )
            ]
        rank += 1
        if rank == len(working):
            break
    return rank


def matrix_trace(matrix: Matrix) -> Fraction:
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("trace requires a square matrix")
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def entry_sum(matrix: Matrix) -> Fraction:
    return sum((value for row in matrix for value in row), Fraction(0))


def centered_graph_kernel(
    base_size: int, extension_degree: int, frobenius_power: int
) -> Matrix:
    if isinstance(frobenius_power, bool) or not isinstance(frobenius_power, int):
        raise TypeError("Frobenius power must be an integer")
    if frobenius_power < 0:
        raise ValueError("Frobenius power must be nonnegative")
    permutation = frobenius_permutation(base_size, extension_degree)
    size = len(permutation)
    background = tuple(
        tuple(Fraction(1, size) for _ in range(size)) for _ in range(size)
    )
    return matrix_add(
        matrix_power(permutation, frobenius_power), matrix_scale(background, -1)
    )


def matrix_is_zero(matrix: Matrix) -> bool:
    return not any(value for row in matrix for value in row)


def frobenius_panel(base_size: int, extension_degree: int) -> dict[str, object]:
    permutation = frobenius_permutation(base_size, extension_degree)
    size = len(permutation)
    if matrix_power(permutation, extension_degree) != identity(size):
        raise ArithmeticError("Frobenius permutation does not have the declared period")
    if any(
        matrix_power(permutation, power) == identity(size)
        for power in range(1, extension_degree)
    ):
        raise ArithmeticError("Frobenius permutation period is unexpectedly short")
    rows = []
    for power in range(extension_degree + 2):
        kernel = centered_graph_kernel(base_size, extension_degree, power)
        expected_trace = base_size ** math.gcd(power, extension_degree) - 1
        if entry_sum(kernel) != 0:
            raise ArithmeticError("centered graph kernel has nonzero total mass")
        if matrix_trace(kernel) != expected_trace:
            raise ArithmeticError("centered graph operator trace formula failed")
        if matrix_rank(kernel) != size - 1:
            raise ArithmeticError("centered graph rank formula failed")
        rows.append(
            {
                "frobenius_power": power,
                "operator_trace": expected_trace,
                "pointwise_alias_class": power % extension_degree,
                "rank": size - 1,
                "total_centered_mass": 0,
                "total_graph_points": size,
            }
        )
    left = centered_graph_kernel(base_size, extension_degree, 2)
    right = centered_graph_kernel(base_size, extension_degree, 3)
    product_kernel = centered_graph_kernel(base_size, extension_degree, 5)
    if matrix_multiply(left, right) != product_kernel:
        raise ArithmeticError("centered graph multiplication law failed")
    return {
        "centered_algebra_dimension": extension_degree,
        "base_size": base_size,
        "centered_generator_minimal_polynomial": f"t*(t^{extension_degree}-1)",
        "extension_degree": extension_degree,
        "field_size": size,
        "permutation_minimal_polynomial": f"t^{extension_degree}-1",
        "rows": rows,
    }


def mobius_divisor_terms(value: int) -> tuple[tuple[int, int], ...]:
    """Return the nonzero terms of M_a(t)=sum_{e|a} mu(e)t^(a/e)."""

    return tuple(
        (value // divisor, coefficient)
        for divisor in divisors(value)
        if (coefficient := mobius(divisor))
    )


def reduced_mobius_coefficients(value: int, period: int) -> tuple[int, ...]:
    validate_positive_integer(period, "period")
    coefficients = [0] * period
    for exponent, coefficient in mobius_divisor_terms(value):
        coefficients[exponent % period] += coefficient
    return tuple(coefficients)


def permutation_polynomial_action(
    base_size: int, extension_degree: int, value: int
) -> Matrix:
    permutation = frobenius_permutation(base_size, extension_degree)
    output = matrix_scale(identity(len(permutation)), 0)
    for exponent, coefficient in mobius_divisor_terms(value):
        output = matrix_add(
            output, matrix_scale(matrix_power(permutation, exponent), coefficient)
        )
    return output


def centered_mobius_action(base_size: int, extension_degree: int, value: int) -> Matrix:
    size = base_size**extension_degree
    output = matrix_scale(identity(size), 0)
    for exponent, coefficient in mobius_divisor_terms(value):
        output = matrix_add(
            output,
            matrix_scale(
                centered_graph_kernel(base_size, extension_degree, exponent),
                coefficient,
            ),
        )
    return output


def prime_mobius_rank_formula(base_size: int, extension_degree: int, prime: int) -> int:
    if mobius(prime) != -1 or len(divisors(prime)) != 2:
        raise ValueError("prime parameter must be prime")
    kernel_dimension = sum(
        cycle_count * math.gcd(cycle_length, prime - 1)
        for cycle_length, cycle_count in frobenius_cycle_counts(
            base_size, extension_degree
        ).items()
    )
    return base_size**extension_degree - kernel_dimension


def mobius_action_panel() -> dict[str, object]:
    rows = []
    for value, extension_degree in ((5, 3), (7, 3), (7, 4), (11, 5)):
        action = permutation_polynomial_action(BASE_FIELD_SIZE, extension_degree, value)
        centered = centered_mobius_action(BASE_FIELD_SIZE, extension_degree, value)
        reduced = reduced_mobius_coefficients(value, extension_degree)
        if action != centered:
            raise ArithmeticError("a>1 Mobius action should already kill constants")
        if matrix_is_zero(action) != (not any(reduced)):
            raise ArithmeticError("reduced coefficient zero criterion failed")
        rank = matrix_rank(action)
        if len(divisors(value)) == 2 and rank != prime_mobius_rank_formula(
            BASE_FIELD_SIZE, extension_degree, value
        ):
            raise ArithmeticError("prime Mobius rank formula failed")
        rows.append(
            {
                "extension_degree": extension_degree,
                "field_size": BASE_FIELD_SIZE**extension_degree,
                "mobius_value": value,
                "operator_rank": rank,
                "operator_trace": int(matrix_trace(action)),
                "reduced_coefficients": list(reduced),
                "total_entry_sum": int(entry_sum(action)),
                "zero_operator": matrix_is_zero(action),
            }
        )
    return {
        "rows": rows,
        "definition": "M_a(t)=sum_(e|a) mu(e)t^(a/e)",
        "prime_formula": (
            "rank(P^p-P)=Q^r-sum_(d|r)c_d*gcd(d,p-1), where c_d is the "
            "number of Frobenius cycles of length d"
        ),
        "zero_criterion": (
            "M_a(P_r)=0 iff every residue coefficient "
            "sum_(e|a,a/e congruent j mod r) mu(e) is zero"
        ),
    }


def lcm_many(values: tuple[int, ...]) -> int:
    if not values:
        raise ValueError("tower must be nonempty")
    result = 1
    for value in values:
        validate_positive_integer(value, "tower level")
        result = math.lcm(result, value)
    return result


def tower_algebra_dimension(levels: tuple[int, ...]) -> int:
    cyclotomic_orders = {order for level in levels for order in divisors(level)}
    return sum(euler_phi(order) for order in cyclotomic_orders)


def joint_grid_matrix(exponents: tuple[int, ...], levels: tuple[int, ...]) -> Matrix:
    if not exponents:
        raise ValueError("exponent grid must be nonempty")
    if not levels:
        raise ValueError("tower must be nonempty")
    rows: list[tuple[Fraction, ...]] = []
    for level in levels:
        validate_positive_integer(level, "tower level")
        for residue in range(level):
            rows.append(
                tuple(
                    Fraction(int(exponent % level == residue)) for exponent in exponents
                )
            )
    return tuple(rows)


def tower_certificate(value: int, levels: tuple[int, ...]) -> dict[str, object]:
    exponents = tuple(exponent for exponent, _ in mobius_divisor_terms(value))
    labels = tuple(
        tuple(exponent % level for level in levels) for exponent in exponents
    )
    grid_rank = matrix_rank(joint_grid_matrix(exponents, levels))
    action_visible = any(
        any(reduced_mobius_coefficients(value, level)) for level in levels
    )
    return {
        "action_visible": action_visible,
        "centered_algebra_dimension": tower_algebra_dimension(levels),
        "divisor_grid_size": len(exponents),
        "joint_period": lcm_many(levels),
        "levels": list(levels),
        "linear_grid_faithful": grid_rank == len(exponents),
        "linear_grid_rank": grid_rank,
        "mobius_value": value,
        "pointwise_labels_distinct": len(set(labels)) == len(labels),
    }


def maximum_level_lower_bound(grid_size: int) -> int:
    validate_positive_integer(grid_size, "grid size")
    level = 1
    while level * (level + 1) // 2 < grid_size:
        level += 1
    return level


def fidelity_cost_panel(max_prime_count: int = 6) -> dict[str, object]:
    validate_positive_integer(max_prime_count, "maximum prime count")
    rows = []
    for prime_count in range(1, max_prime_count + 1):
        grid_size = 1 << prime_count
        tower_level = maximum_level_lower_bound(grid_size)
        rows.append(
            {
                "mobius_prime_count": prime_count,
                "divisor_grid_size": grid_size,
                "single_level_degree_lower_bound": grid_size,
                "single_level_matrix_dimension_lower_bound": BASE_FIELD_SIZE**grid_size,
                "arbitrary_tower_max_level_lower_bound": tower_level,
                "arbitrary_tower_largest_matrix_dimension_lower_bound": BASE_FIELD_SIZE
                ** tower_level,
            }
        )
    return {
        "base_size": BASE_FIELD_SIZE,
        "rows": rows,
        "scope": (
            "necessary costs for linear fidelity of every coefficient on the "
            "full nonzero-Mobius divisor grid; one particular Mobius vector "
            "can remain visible at lower cost"
        ),
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    frobenius_rows = [
        frobenius_panel(BASE_FIELD_SIZE, extension_degree)
        for extension_degree in range(1, MAX_MATRIX_EXTENSION_DEGREE + 1)
    ]
    tower_rows = [
        tower_certificate(30, (2, 3, 5)),
        tower_certificate(210, (2, 3, 5, 7)),
        tower_certificate(210, (2, 3, 5, 7, 11)),
    ]
    return {
        "source_contract": {
            "git_blobs": {
                f"{commit}:{path}": blob
                for (commit, path), blob in SOURCE_BLOBS.items()
            },
            "native_kernel": "H_n^(r)=P_r^n-Q^(-r)J on functions of F_(Q^r)",
        },
        "extension_field_theorem": {
            "total_graph_count": "Q^r for every n",
            "centered_total_mass": "zero for every n",
            "operator_trace": "Q^gcd(n,r)-1",
            "pointwise_alias": "H_n^(r)=H_m^(r) iff n is congruent to m mod r",
            "rank": "Q^r-1 for every n",
            "multiplication": "H_m H_n=H_(m+n), with indices mod r",
            "algebra": "span(H_n) is Q[C_r], with unit H_0 and dimension r",
            "minimal_polynomials": {
                "P_r": "t^r-1",
                "H_1_on_full_space": "t*(t^r-1)",
                "H_n_on_full_space": "t*(t^(r/gcd(n,r))-1)",
            },
            "finite_replay": frobenius_rows,
        },
        "mobius_divisor_polynomial": mobius_action_panel(),
        "tower_fidelity": {
            "exact_criterion": (
                "the coefficient grid is linearly faithful exactly when the "
                "stacked residue-incidence matrix [1_(e mod r=j)] has full "
                "column rank"
            ),
            "joint_centered_algebra_dimension": (
                "deg lcm_(r in T)(t^r-1)=sum phi(d) over d dividing some tower level"
            ),
            "label_period": "lcm of the tower levels",
            "finite_replay": tower_rows,
            "warning": (
                "distinct exponent labels modulo the joint period do not imply "
                "linear fidelity for arbitrary divisor coefficients"
            ),
        },
        "literal_matrix_cost": fidelity_cost_panel(),
        "categorical_scope": {
            "correspondence_support_rank_lower_bound": False,
            "betti_lower_bound": False,
            "statement": (
                "Q^r is the dimension of the literal point-function permutation "
                "model and Q^r-1 is its external separation rank. A graph "
                "correspondence can encode the same numerical kernel without "
                "presenting it as Q^r-1 external summands, so no sheaf-rank or "
                "Betti lower bound is inferred."
            ),
            "closed_point_adams_formula": "NOT CONSTRUCTED",
            "full_native_source_complex": "NOT CONSTRUCTED",
            "cysel_wcadd_wckum_rh_grh": "NOT PROVED",
        },
        "resource_caps": {
            "base_size": BASE_FIELD_SIZE,
            "largest_exact_matrix_dimension": BASE_FIELD_SIZE
            ** MAX_MATRIX_EXTENSION_DEGREE,
            "maximum_matrix_extension_degree": MAX_MATRIX_EXTENSION_DEGREE,
            "finite_field_element_enumeration": 0,
            "closed_place_enumeration": 0,
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
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    if not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
