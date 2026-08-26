#!/usr/bin/env python3
"""Exact F2 replay for the all-profile odd-notch parity sieve.

The replay enumerates only bounded integer degree profiles.  It enumerates no
finite fields, irreducibles, polynomials, curves, Frobenius classes, or zeros.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "QUADRATIC_FAMILY_NOTCH_PARITY_SIEVE.md"

FROZEN_BASE = "6e4609dfe1b073f1eb58445fdd1d7164dbc450d6"
SOURCE_PATH = (
    "research/l-families/atlas/function_field/"
    "QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md"
)
SOURCE_BLOB = "a1b8476ddd3cad6f63ff205392426ae9c2d0829c"

MAX_REPLAY_N = 9
MAX_PROFILES = 1_024
MAX_GENERAL_ROWS = 2_048
MAX_COEFFICIENT_STATES = 32_768
MAX_WALL_SECONDS = 4.0


def _strict_integer(value: object, name: str, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer at least {minimum}")
    return value


def _validate_degrees(degrees: object) -> tuple[int, ...]:
    if not isinstance(degrees, (list, tuple)) or not degrees:
        raise ValueError("degrees must be a nonempty list or tuple")
    values = tuple(_strict_integer(value, "factor degree", 1) for value in degrees)
    return tuple(sorted(values))


def integer_partitions(total: int, minimum: int = 1) -> list[tuple[int, ...]]:
    """Return nondecreasing positive integer partitions of a bounded total."""

    total = _strict_integer(total, "total", 1)
    minimum = _strict_integer(minimum, "minimum", 1)
    if minimum > total:
        return []
    result: list[tuple[int, ...]] = []

    def visit(remaining: int, lower: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            result.append(prefix)
            return
        for part in range(lower, remaining + 1):
            visit(remaining - part, part, (*prefix, part))

    visit(total, minimum, ())
    return result


def binary_atom_weights(degrees: object, target: int) -> list[int]:
    """Return the labelled binary weights 2^j*d that can reach target."""

    values = _validate_degrees(degrees)
    target = _strict_integer(target, "target", 0)
    weights: list[int] = []
    for degree in values:
        weight = degree
        while weight <= target:
            weights.append(weight)
            weight *= 2
    return weights


def subset_sum_parity(
    degrees: object, target: int, *, include_special_one: bool = False
) -> int:
    """Return the labelled binary-subset parity at one target."""

    target = _strict_integer(target, "target", 0)
    coefficients = [0] * (target + 1)
    coefficients[0] = 1
    weights = binary_atom_weights(degrees, target)
    if include_special_one and target >= 1:
        weights.append(1)
    for weight in weights:
        for degree in range(target, weight - 1, -1):
            coefficients[degree] ^= coefficients[degree - weight]
    return coefficients[target]


def profile_a_parities(degrees: object, max_degree: int) -> list[int]:
    """Return A(u)=prod(1+u^d)^-1 modulo two through max_degree."""

    values = _validate_degrees(degrees)
    max_degree = _strict_integer(max_degree, "max_degree", 0)
    coefficients = [0] * (max_degree + 1)
    coefficients[0] = 1
    for weight in binary_atom_weights(values, max_degree):
        for degree in range(max_degree, weight - 1, -1):
            coefficients[degree] ^= coefficients[degree - weight]
    return coefficients


def _multiply_mod2(left: list[int], right: list[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        if left_value == 0:
            continue
        for right_index, right_value in enumerate(right):
            if right_value:
                product[left_index + right_index] ^= 1
    return product


def p_polynomial_mod2(degrees: object) -> list[int]:
    """Return prod(1+u^d)/(1+u) over F2."""

    values = _validate_degrees(degrees)
    numerator = [1]
    for degree in values:
        factor = [0] * (degree + 1)
        factor[0] = 1
        factor[degree] = 1
        numerator = _multiply_mod2(numerator, factor)

    quotient = [0] * (sum(values))
    previous = 0
    for degree in range(len(quotient)):
        quotient[degree] = numerator[degree] ^ previous
        previous = quotient[degree]
    if numerator[-1] != quotient[-1]:
        raise RuntimeError("division by 1+u failed")
    return quotient


def d_polynomial_mod2(degrees: object) -> list[int]:
    """Return (1+u^2)P(u), the parity shadow of D(u)."""

    p_coefficients = p_polynomial_mod2(degrees)
    result = [0] * (len(p_coefficients) + 2)
    for degree, value in enumerate(p_coefficients):
        result[degree] ^= value
        result[degree + 2] ^= value
    return result


def general_parity_certificate(
    family_degree: int, degrees: object
) -> dict[str, object]:
    """Compare the three parity adapters for any odd conductor degree."""

    family_degree = _strict_integer(family_degree, "family_degree", 0)
    values = _validate_degrees(degrees)
    conductor_degree = sum(values)
    if conductor_degree % 2 == 0:
        raise ValueError("the general parity adapter requires odd conductor degree")

    a_coefficients = profile_a_parities(values, family_degree)
    d_coefficients = d_polynomial_mod2(values)
    source_parity = 0
    for index in range(family_degree // 2 + 1):
        d_index = family_degree - 2 * index
        if d_index < len(d_coefficients):
            source_parity ^= a_coefficients[index] & d_coefficients[d_index]
    previous_parity = a_coefficients[family_degree - 1] if family_degree else 0
    coefficient_parity = a_coefficients[family_degree] ^ previous_parity
    subset_parity = subset_sum_parity(values, family_degree, include_special_one=True)
    if len({source_parity, coefficient_parity, subset_parity}) != 1:
        raise RuntimeError("parity adapters disagree")
    return {
        "family_degree": family_degree,
        "M": conductor_degree,
        "degrees": list(values),
        "a_r_parity": a_coefficients[family_degree],
        "a_r_minus_1_parity": previous_parity,
        "S_parity": source_parity,
        "binary_subset_parity": subset_parity,
        "certified_nonzero": bool(source_parity),
        "binary_atom_count": len(binary_atom_weights(values, family_degree)) + 1,
    }


def profile_parity_certificate(n_value: int, degrees: object) -> dict[str, object]:
    """Specialize the general certificate to M=2n-1 and check the notch."""

    n_value = _strict_integer(n_value, "n", 2)
    values = _validate_degrees(degrees)
    expected_total = 2 * n_value - 1
    if sum(values) != expected_total:
        raise ValueError("factor degrees must sum to 2n-1")
    general = general_parity_certificate(n_value, values)
    d_coefficients = d_polynomial_mod2(values)
    if d_coefficients[n_value] != 0:
        raise RuntimeError("top notch D_n parity did not vanish")
    return {
        **general,
        "n": n_value,
        "a_n_parity": general["a_r_parity"],
        "a_n_minus_1_parity": general["a_r_minus_1_parity"],
    }


def shallow_layer_certificate(
    n_value: int, depth: int, degrees: object
) -> dict[str, object]:
    """Check the sufficient shallow condition S congruent m_h modulo two."""

    n_value = _strict_integer(n_value, "n", 2)
    depth = _strict_integer(depth, "depth", 0)
    values = _validate_degrees(degrees)
    if sum(values) != 2 * n_value - 1:
        raise ValueError("factor degrees must sum to 2n-1")
    h_value = n_value // 2
    d_value = h_value - depth
    if d_value < 1 or min(values) != d_value:
        raise ValueError("profile minimum must equal h-depth")
    epsilon = n_value % 2
    sufficient = h_value > 3 * depth + epsilon
    parity = profile_parity_certificate(n_value, values)["S_parity"]
    m_h = values.count(h_value)
    if sufficient and parity != m_h % 2:
        raise RuntimeError("shallow parity collapse failed")
    return {
        "n": n_value,
        "h": h_value,
        "epsilon": epsilon,
        "depth_j": depth,
        "minimum_degree_d": d_value,
        "condition_h_gt_3j_plus_epsilon": sufficient,
        "m_h": m_h,
        "m_h_parity": m_h % 2,
        "S_parity": parity,
        "certified_nonzero_from_m_h": bool(sufficient and m_h % 2),
    }


def split_profile_certificate(n_value: int) -> dict[str, object]:
    """Return the Lucas--Kummer parity control for 2n-1 linear factors."""

    n_value = _strict_integer(n_value, "n", 2)
    no_carry = (n_value & (2 * n_value - 3)) == 0
    replay = profile_parity_certificate(n_value, [1] * (2 * n_value - 1))
    if replay["S_parity"] != int(no_carry):
        raise RuntimeError("split-profile Lucas control failed")
    return {
        "n": n_value,
        "linear_factors": 2 * n_value - 1,
        "lucas_bit_test": f"{n_value} & {2 * n_value - 3} == 0",
        "no_binary_carry": no_carry,
        "S_parity": replay["S_parity"],
        "minimum_field_size_for_feasibility": 2 * n_value - 1,
    }


def _check_source_blob() -> None:
    completed = subprocess.run(
        ["git", "rev-parse", f"{FROZEN_BASE}:{SOURCE_PATH}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=2.0,
    )
    if completed.stdout.strip() != SOURCE_BLOB:
        raise RuntimeError("frozen notch source blob mismatch")


def build_report() -> dict[str, object]:
    started = time.monotonic()
    profile_count = 0
    coefficient_states = 0
    nonzero_certificates = 0
    parity_by_n: list[dict[str, int]] = []
    for n_value in range(2, MAX_REPLAY_N + 1):
        rows = integer_partitions(2 * n_value - 1)
        odd_rows = 0
        for degrees in rows:
            certificate = profile_parity_certificate(n_value, degrees)
            profile_count += 1
            coefficient_states += n_value + 1
            if certificate["certified_nonzero"]:
                odd_rows += 1
                nonzero_certificates += 1
        parity_by_n.append(
            {
                "n": n_value,
                "degree_profiles": len(rows),
                "parity_odd_profiles": odd_rows,
            }
        )
    if profile_count > MAX_PROFILES:
        raise RuntimeError("degree-profile cap exceeded")
    if coefficient_states > MAX_COEFFICIENT_STATES:
        raise RuntimeError("coefficient-state cap exceeded")

    general_rows = 0
    for conductor_degree in range(3, 12, 2):
        for degrees in integer_partitions(conductor_degree):
            for family_degree in range(13):
                general_parity_certificate(family_degree, degrees)
                general_rows += 1
    if general_rows > MAX_GENERAL_ROWS:
        raise RuntimeError("general-family-degree row cap exceeded")

    shallow_rows = []
    for n_value in range(4, MAX_REPLAY_N + 1):
        h_value = n_value // 2
        for depth in range(h_value):
            d_value = h_value - depth
            if 2 * n_value - 1 - d_value < d_value:
                continue
            profile = [d_value, 2 * n_value - 1 - d_value]
            row = shallow_layer_certificate(n_value, depth, profile)
            if row["condition_h_gt_3j_plus_epsilon"]:
                shallow_rows.append(row)

    report = {
        "schema": "riemann.function_field.quadratic_notch_parity_sieve.v1",
        "status": "EXACT_ALL_PROFILE_MOD_TWO_SIEVE",
        "source": {
            "commit": FROZEN_BASE,
            "path": SOURCE_PATH,
            "blob": SOURCE_BLOB,
        },
        "exact_theorem": {
            "all_family_degrees": (
                "for odd deg Q, S_(r,Q) == a_r+a_(r-1) (mod 2) for every r"
            ),
            "all_profile": "S_(n,Q) == a_n+a_(n-1) (mod 2)",
            "binary_certificate": (
                "S parity is the labelled binary-subset parity at weight n"
            ),
            "zero_necessary_condition": "a_n == a_(n-1) (mod 2)",
            "shallow_collapse": (
                "h>3j+epsilon and min degree h-j imply S == m_h (mod 2)"
            ),
            "split_profile": "S odd iff n & (2n-3) == 0",
        },
        "bounded_exact_replay": {
            "n_range": [2, MAX_REPLAY_N],
            "degree_profiles": profile_count,
            "general_family_degree_rows": general_rows,
            "parity_odd_profiles": nonzero_certificates,
            "rows_by_n": parity_by_n,
            "shallow_condition_rows": len(shallow_rows),
            "split_rows": [
                split_profile_certificate(n_value)
                for n_value in range(2, MAX_REPLAY_N + 1)
            ],
        },
        "resource_contract": {
            "integer_degree_profiles": profile_count,
            "maximum_profiles": MAX_PROFILES,
            "general_family_degree_rows": general_rows,
            "maximum_general_rows": MAX_GENERAL_ROWS,
            "coefficient_states": coefficient_states,
            "maximum_coefficient_states": MAX_COEFFICIENT_STATES,
            "finite_fields_enumerated": 0,
            "irreducibles_enumerated": 0,
            "polynomials_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
        "firewalls": [
            "Parity even is necessary but not sufficient for a raw zero.",
            "No density or equidistribution of the parity locus is claimed.",
            "The replay uses formal profiles and does not assert field feasibility.",
            "Raw family-sum zeros are not individual L-function zeros.",
            "No RH or GRH consequence is claimed.",
        ],
    }
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return report


def run_checks() -> dict[str, object]:
    _check_source_blob()
    report = build_report()
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "S_{r,Q}\\equiv a_r+a_{r-1}",
        "S_{n,Q}\\equiv a_n+a_{n-1}",
        "labelled binary atoms",
        "h>3j+\\varepsilon",
        "necessary condition, not a classification",
        "No numerical density follows",
        "known or folklore",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="run source and exact replay checks"
    )
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
