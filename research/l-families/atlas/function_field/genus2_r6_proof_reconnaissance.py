#!/usr/bin/env python3
"""Exact lightweight reconnaissance for the unresolved genus-two R6 mean.

This producer performs no finite-field or family enumeration.  It uses the
existing capped C2 character engine to verify two statements:

1. after removing 2*chi_(0,3), R6 is the rank-two echo kernel

       R6 - 2*chi_(0,3) = -3*B1*B2 - 2*B3;

2. the five proved all-q low character means do not determine mean(R6), even
   after imposing positivity of a central probability law on USp(4).

All arithmetic is integer or Fraction arithmetic.  The character-candidate
source-atom count is capped at 4096, and no observed q=3,5,7 R6 value enters
the replay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from collections.abc import Mapping
from fractions import Fraction
from pathlib import Path

import usp_coefficient_minor_rank_scan as rank_scan

Exponent = tuple[int, int]
Laurent = dict[Exponent, int]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_r6_proof_reconnaissance.json"
NOTE_PATH = HERE / "GENUS2_R6_PROOF_RECONNAISSANCE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_r6_proof_reconnaissance.py"

BALANCED_NOTE_PATH = HERE / "BALANCED_CONTROL_FAMILY_SCAN.md"
BALANCED_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
MOMENT_NOTE_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"
HIGH_WEIGHT_NOTE_PATH = HERE / "GENUS2_HIGH_WEIGHT_CHANNEL_PROBE.md"
GUARDED_INFERENCE_PATH = HERE / "GUARDED_COHOMOLOGY_CONJECTURE_INFERENCE.md"
BOUNDARY_NOTE_PATH = HERE / "GENUS2_DETECTOR_BOUNDARY_QUOTIENT.md"
CHARACTER_ENGINE_PATH = HERE / "usp_coefficient_minor_rank_scan.py"

MAX_SOURCE_ATOMS = 4096
MAX_WALL_SECONDS = 5.0

LOW_WEIGHTS: tuple[tuple[str, Exponent], ...] = (
    ("chi_(0,1)", (1, 1)),
    ("chi_(2,0)", (2, 0)),
    ("chi_(0,2)", (2, 2)),
    ("chi_(2,1)", (3, 1)),
    ("chi_(4,0)", (4, 0)),
)

# Ascending negative-power coefficients: (degree, coefficient) represents
# coefficient*q^(-degree).  These are the five proved all-q mean formulas,
# stored once so both exact evaluation and the symbolic dimension budget are
# derived from the same primitive rows.
LOW_MEAN_LAURENT: dict[str, tuple[tuple[int, int], ...]] = {
    "chi_(0,1)": ((1, -1), (2, 1), (4, -1)),
    "chi_(2,0)": ((3, 1), (4, -1)),
    "chi_(0,2)": ((1, -1), (5, -1)),
    "chi_(2,1)": ((3, 2), (4, -1), (5, -2)),
    "chi_(4,0)": ((5, -3),),
}

# Each sign is proved below by shifting its signed numerator at q=3.
LOW_MEAN_SIGNS: dict[str, int] = {
    "chi_(0,1)": -1,
    "chi_(2,0)": 1,
    "chi_(0,2)": -1,
    "chi_(2,1)": 1,
    "chi_(4,0)": -1,
}

HIGH_R6_TERMS: tuple[tuple[str, Exponent, int], ...] = (
    ("chi_(2,3)", (5, 3), 2),
    ("chi_(6,0)", (6, 0), 3),
    ("chi_(4,2)", (6, 2), -3),
    ("chi_(2,4)", (6, 4), 1),
    ("chi_(0,6)", (6, 6), -1),
)


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _add_scaled(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    scalar: int,
    guard: rank_scan.ResourceGuard,
) -> Laurent:
    return rank_scan.add_scaled(left, right, scalar, guard)


def _linear_combination(
    terms: tuple[tuple[Mapping[Exponent, int], int], ...],
    guard: rank_scan.ResourceGuard,
) -> Laurent:
    result: Laurent = {}
    for polynomial, coefficient in terms:
        result = _add_scaled(result, polynomial, coefficient, guard)
    return result


def _adams(polynomial: Mapping[Exponent, int], power: int) -> Laurent:
    if power < 1:
        raise ValueError("Adams power must be positive")
    result = {
        (power * exponent[0], power * exponent[1]): coefficient
        for exponent, coefficient in polynomial.items()
    }
    if len(result) != len(polynomial):
        raise ArithmeticError("Adams scaling unexpectedly merged Laurent atoms")
    return result


def _haar_inner_product(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    density: Mapping[Exponent, int],
    guard: rank_scan.ResourceGuard,
) -> int:
    product = rank_scan.multiply(left, right, guard)
    return rank_scan.haar_constant_term(product, density, 2, guard)


def _low_means(q: int) -> dict[str, Fraction]:
    if q < 3:
        raise ValueError("q must be at least 3")
    return {
        name: sum(
            (Fraction(coefficient, q**degree) for degree, coefficient in row),
            Fraction(0),
        )
        for name, row in LOW_MEAN_LAURENT.items()
    }


def _weighted_dimension_budget(q: int, dimensions: Mapping[str, int]) -> Fraction:
    means = _low_means(q)
    return sum(
        (abs(means[name]) * dimensions[name] for name, _weight in LOW_WEIGHTS),
        Fraction(0),
    )


def _poly_shift(coefficients: tuple[int, ...], shift: int) -> tuple[int, ...]:
    """Return ascending coefficients of P(t+shift) from ascending P(q)."""

    result = [0] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for t_degree in range(degree + 1):
            result[t_degree] += (
                coefficient * math.comb(degree, t_degree) * shift ** (degree - t_degree)
            )
    return tuple(result)


def _signed_mean_numerator(name: str, denominator_degree: int = 5) -> tuple[int, ...]:
    """Return ascending coefficients of sign(name)*q^d*m_name(q)."""

    if name not in LOW_MEAN_LAURENT or denominator_degree < 5:
        raise ValueError("unknown low mean or insufficient denominator degree")
    coefficients = [0] * (denominator_degree + 1)
    sign = LOW_MEAN_SIGNS[name]
    for negative_degree, coefficient in LOW_MEAN_LAURENT[name]:
        coefficients[denominator_degree - negative_degree] += sign * coefficient
    return tuple(coefficients)


def _dimension_budget_coefficients(dimensions: Mapping[str, int]) -> dict[int, int]:
    """Derive S(q)=sum dim*abs(mean) after the symbolic sign proofs."""

    result: dict[int, int] = {}
    for name, _weight in LOW_WEIGHTS:
        sign = LOW_MEAN_SIGNS[name]
        for degree, coefficient in LOW_MEAN_LAURENT[name]:
            result[degree] = (
                result.get(degree, 0) + dimensions[name] * sign * coefficient
            )
    return {
        degree: coefficient
        for degree, coefficient in sorted(result.items())
        if coefficient
    }


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        BALANCED_NOTE_PATH,
        BALANCED_PRODUCER_PATH,
        MOMENT_NOTE_PATH,
        HIGH_WEIGHT_NOTE_PATH,
        GUARDED_INFERENCE_PATH,
        BOUNDARY_NOTE_PATH,
        CHARACTER_ENGINE_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    return [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_normalized_sha256(path),
        }
        for path in paths
    ]


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    guard = rank_scan.ResourceGuard()
    guard.limits["character_weight_candidates"] = MAX_SOURCE_ATOMS
    engine = rank_scan.CnCharacterEngine(2, guard)

    character_cache: dict[Exponent, Laurent] = {}

    def character(weight: Exponent) -> Laurent:
        if weight not in character_cache:
            character_cache[weight] = engine.character(weight)
        return dict(character_cache[weight])

    zero = (0, 0)
    one: Laurent = {zero: 1}
    chi_0_3 = character((3, 3))
    low_characters = {name: character(weight) for name, weight in LOW_WEIGHTS}

    balanced = _linear_combination(
        ((character((2, 0)), 1), (character((2, 2)), -1)), guard
    )
    expected_balanced = {
        (-2, -2): -1,
        (-2, 2): -1,
        (2, -2): -1,
        (2, 2): -1,
    }
    if balanced != expected_balanced:
        raise ArithmeticError("balanced torus factorization drifted")

    b_two = _adams(balanced, 2)
    b_three = _adams(balanced, 3)
    b_one_b_two = rank_scan.multiply(balanced, b_two, guard)

    r6: Laurent = {}
    high_dimensions: dict[str, int] = {}
    for name, weight, coefficient in HIGH_R6_TERMS:
        r6 = _add_scaled(r6, character(weight), coefficient, guard)
        high_dimensions[name] = rank_scan.weyl_dimension(weight)

    residual = _add_scaled(r6, chi_0_3, -2, guard)
    echo_residual = _linear_combination(((b_one_b_two, -3), (b_three, -2)), guard)
    if residual != echo_residual:
        raise ArithmeticError("R6 echo reduction failed")

    balanced_cubed = rank_scan.multiply(
        rank_scan.multiply(balanced, balanced, guard), balanced, guard
    )
    pointwise_rhs = _linear_combination(
        ((balanced_cubed, 1), (balanced, -6), (chi_0_3, 2)), guard
    )
    if r6 != pointwise_rhs:
        raise ArithmeticError("R6 polynomial identity failed")

    b_three_character_rhs = _linear_combination(
        (
            (character((3, 3)), 1),
            (character((5, 3)), -1),
            (character((6, 4)), 1),
            (character((6, 6)), -1),
        ),
        guard,
    )
    if b_three != b_three_character_rhs:
        raise ArithmeticError("B3 character decomposition failed")

    b_one_b_two_character_rhs = _linear_combination(
        (
            (character((6, 0)), -1),
            (character((6, 2)), 1),
            (character((6, 4)), -1),
            (character((6, 6)), 1),
        ),
        guard,
    )
    if b_one_b_two != b_one_b_two_character_rhs:
        raise ArithmeticError("B1*B2 character decomposition failed")

    # Extract, rather than prescribe, the separated coefficient matrix in the
    # basis (X_1, X_3) on each torus coordinate.  Every X_i(x)X_j(y) has four
    # sign variants with the same coefficient.  Exact support equality binds
    # the rank certificate to the computed Laurent residual.
    separated_frequencies = (1, 3)
    expected_residual_support = {
        (x_sign * 2 * x_frequency, y_sign * 2 * y_frequency)
        for x_frequency in separated_frequencies
        for y_frequency in separated_frequencies
        for x_sign in (-1, 1)
        for y_sign in (-1, 1)
    }
    if set(residual) != expected_residual_support:
        raise ArithmeticError("residual escaped the separated frequency basis")
    separated_matrix = tuple(
        tuple(
            residual[(2 * x_frequency, 2 * y_frequency)]
            for y_frequency in separated_frequencies
        )
        for x_frequency in separated_frequencies
    )
    for exponent, coefficient in residual.items():
        x_index = separated_frequencies.index(abs(exponent[0]) // 2)
        y_index = separated_frequencies.index(abs(exponent[1]) // 2)
        if coefficient != separated_matrix[x_index][y_index]:
            raise ArithmeticError("residual coefficient depends on a torus sign")
    separated_determinant = (
        separated_matrix[0][0] * separated_matrix[1][1]
        - separated_matrix[0][1] * separated_matrix[1][0]
    )
    if separated_determinant != -6:
        raise ArithmeticError("unexpected separated-kernel determinant")
    if len(residual) != 16 or len(b_three) != 4 or len(b_one_b_two) != 16:
        raise ArithmeticError("echo-support cardinality drifted")

    density = rank_scan.weyl_density(2, guard)
    gram_names = ("1", *(name for name, _weight in LOW_WEIGHTS), "chi_(0,3)", "R6")
    gram_polynomials = {
        "1": one,
        **low_characters,
        "chi_(0,3)": chi_0_3,
        "R6": r6,
    }
    gram = [
        [
            _haar_inner_product(
                gram_polynomials[left], gram_polynomials[right], density, guard
            )
            for right in gram_names
        ]
        for left in gram_names
    ]
    expected_diagonal = [1, 1, 1, 1, 1, 1, 1, 24]
    for row_index, row in enumerate(gram):
        for column_index, value in enumerate(row):
            expected = expected_diagonal[row_index] if row_index == column_index else 0
            if value != expected:
                raise ArithmeticError("Haar Gram matrix failed exact orthogonality")

    low_dimensions = {
        name: rank_scan.weyl_dimension(weight) for name, weight in LOW_WEIGHTS
    }
    r6_uniform_bound = sum(
        abs(coefficient) * high_dimensions[name]
        for name, _weight, coefficient in HIGH_R6_TERMS
    )
    if low_dimensions != {
        "chi_(0,1)": 5,
        "chi_(2,0)": 10,
        "chi_(0,2)": 14,
        "chi_(2,1)": 35,
        "chi_(4,0)": 35,
    }:
        raise ArithmeticError("low-character dimensions drifted")
    if r6_uniform_bound != 1620:
        raise ArithmeticError("R6 triangle-inequality bound drifted")

    # Prove the declared signs for every real q>=3: after multiplying by q^5
    # and shifting q=t+3, every signed numerator has nonnegative coefficients
    # and a positive constant.  The dimension budget is then derived
    # coefficientwise from the five primitive mean rows, with no q-sampling.
    low_sign_shift_certificates: dict[str, list[int]] = {}
    for name, _weight in LOW_WEIGHTS:
        shifted = _poly_shift(_signed_mean_numerator(name), 3)
        if shifted[0] <= 0 or any(coefficient < 0 for coefficient in shifted):
            raise ArithmeticError(f"low-mean sign proof failed for {name}")
        low_sign_shift_certificates[name] = list(shifted)
    budget_coefficients = _dimension_budget_coefficients(low_dimensions)
    if budget_coefficients != {1: 19, 2: -5, 3: 80, 4: -40, 5: 49}:
        raise ArithmeticError("derived weighted dimension budget drifted")

    # delta(q)=1-S(q)=P(q)/q^5.  Shifting q=t+19 gives strictly positive
    # coefficients, proving delta(q)>0 for every real q>=19 without sampling.
    delta_numerator_ascending = (-49, 40, -80, 5, -19, 1)
    shifted_delta = _poly_shift(delta_numerator_ascending, 19)
    expected_shifted_delta = (6126, 132736, 27641, 2171, 76, 1)
    if shifted_delta != expected_shifted_delta or any(
        value <= 0 for value in shifted_delta
    ):
        raise ArithmeticError("q=19 positivity shift failed")

    q_witness = 19
    budget_witness = _weighted_dimension_budget(q_witness, low_dimensions)
    delta_witness = 1 - budget_witness
    if delta_witness != Fraction(6126, 2476099):
        raise ArithmeticError("q=19 ambiguity margin drifted")
    ambiguity_mean = Fraction(24, 2 * r6_uniform_bound) * delta_witness
    if ambiguity_mean != Fraction(2042, 111424455):
        raise ArithmeticError("q=19 R6 ambiguity witness drifted")

    source_atoms = guard.snapshot()["character_weight_candidates"]
    if source_atoms > MAX_SOURCE_ATOMS:
        raise RuntimeError("source-atom cap exceeded")
    elapsed = time.perf_counter() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("R6 reconnaissance wall-clock cap exceeded")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_r6_proof_reconnaissance.v1",
        "status": "EXACT_REDUCTION_AND_LOW_MOMENT_NO_GO",
        "scope": {
            "finite_fields_enumerated": 0,
            "observed_R6_values_consumed": 0,
            "primitive_family_source_records_consumed": 0,
            "source_atom_accounting": (
                "conservatively count every C2 bounding-box character-weight "
                "candidate as one source atom"
            ),
            "maximum_source_atoms": MAX_SOURCE_ATOMS,
            "actual_source_atoms": source_atoms,
            "arithmetic": "Python integers and fractions only",
        },
        "echo_reduction": {
            "definition": "B_r=-(x^(2r)+x^(-2r))*(y^(2r)+y^(-2r))",
            "chebyshev_product": "X_1*X_2=X_3+X_1",
            "pointwise_identity": "R6-2*chi_(0,3)=-3*B_1*B_2-2*B_3",
            "mean_identity": "mean(R6)=2*mean(chi_(0,3))-3*mean(B_1*B_2)-2*mean(B_3)",
            "B3_character_decomposition": "chi_(0,3)-chi_(2,3)+chi_(2,4)-chi_(0,6)",
            "B1B2_character_decomposition": "-chi_(6,0)+chi_(4,2)-chi_(2,4)+chi_(0,6)",
            "torus_support": {
                "R6": len(r6),
                "chi_(0,3)": len(chi_0_3),
                "R6_minus_2_chi_(0,3)": len(residual),
                "B_1_B_2": len(b_one_b_two),
                "B_3": len(b_three),
            },
            "separated_basis": ["X_1", "X_3"],
            "separated_coefficient_matrix": [list(row) for row in separated_matrix],
            "separated_determinant": separated_determinant,
            "exact_separated_tensor_rank": 2,
            "one_product_factorization_no_go": (
                "The nonzero 2x2 determinant rules out a rank-one separated "
                "factorization of R6-2*chi_(0,3)."
            ),
        },
        "low_moment_no_go": {
            "proved_low_character_order": [name for name, _weight in LOW_WEIGHTS],
            "low_character_dimensions": low_dimensions,
            "R6_irreducible_coefficients": {
                name: coefficient for name, _weight, coefficient in HIGH_R6_TERMS
            },
            "R6_irreducible_dimensions": high_dimensions,
            "haar_gram_order": list(gram_names),
            "haar_gram_matrix": gram,
            "R6_squared_norm": 24,
            "R6_uniform_triangle_bound": r6_uniform_bound,
            "low_mean_sign_q_minus_3_coefficients_ascending": low_sign_shift_certificates,
            "derived_dimension_budget_coefficients": {
                str(degree): coefficient
                for degree, coefficient in budget_coefficients.items()
            },
            "dimension_budget": "S(q)=19/q-5/q^2+80/q^3-40/q^4+49/q^5",
            "ambiguity_margin": (
                "delta(q)=1-S(q)=(q^5-19*q^4+5*q^3-80*q^2+40*q-49)/q^5"
            ),
            "q_minus_19_positive_coefficients_ascending": list(shifted_delta),
            "probability_densities": (
                "f_(q,+/-)=1+sum_lambda m_lambda(q)*chi_lambda +/- delta(q)*R6/(2*1620)"
            ),
            "density_lower_bound": "delta(q)/2>0 for every real q>=19",
            "shared_low_means": "integral chi_lambda*f_(q,+/-)=m_lambda(q)",
            "opposite_R6_means": "integral R6*f_(q,+/-)=+/-delta(q)/135",
            "q_19_witness": {
                "S": _fraction_pair(budget_witness),
                "delta": _fraction_pair(delta_witness),
                "absolute_R6_mean": _fraction_pair(ambiguity_mean),
            },
            "logical_boundary": (
                "The five proved all-q low means and compact-group positivity alone "
                "do not determine mean(R6).  This does not rule out a separate "
                "squarefree-family arithmetic evaluation."
            ),
        },
        "resource_counts": guard.snapshot(),
        "source_manifest": _source_manifest(),
    }
    payload["canonical_payload_sha256"] = _canonical_sha256(payload)
    return payload


def _read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="compare with the frozen JSON"
    )
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    arguments = parser.parse_args()

    fixture = build_fixture()
    if arguments.check:
        if not arguments.output.is_file():
            raise FileNotFoundError(arguments.output)
        frozen = _read_json(arguments.output)
        if frozen != fixture:
            raise SystemExit("frozen R6 reconnaissance artifact does not match replay")
        print(
            "genus-two R6 proof reconnaissance check: ok "
            f"({fixture['scope']['actual_source_atoms']} source atoms)"
        )
        return

    arguments.output.write_text(
        json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(arguments.output)


if __name__ == "__main__":
    main()
