#!/usr/bin/env python3
"""Exact C2 character decompositions for powers of the genus-two toy minor.

For a maximal-torus element of USp(4), write characters using highest weights
``a*omega1+b*omega2``.  The toy statistic from ``usp4_toy_minor_moments.py``
satisfies

    F = -(1 + chi_(0*omega1+1*omega2) + chi_(0*omega1+2*omega2)).

This module decomposes F^m for 1 <= m <= 6.  It uses Kostant's multiplicity
formula for C2 and exact integer Laurent polynomials.  A second Weyl
constant-term calculation checks the trivial multiplicity.  There is no
random sampling, numerical integration, or external computer-algebra system.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from time import perf_counter
from typing import Mapping


Exponent = tuple[int, int]
Laurent = dict[Exponent, int]
HighestWeight = tuple[int, int]  # e-basis coordinates lambda_1 >= lambda_2 >= 0

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "usp4_toy_minor_character_decomposition.json"
MAX_MOMENT = 6
MAX_HIGHEST_E_COORDINATE = 2 * MAX_MOMENT
MAX_WALL_SECONDS = 5.0
MAX_LAURENT_TERMS = 1_200
MAX_ABS_EXPONENT = 16
MAX_IRREDUCIBLES_PER_POWER = 64
FROZEN_HAAR_MOMENTS = (-1, 3, -11, 56, -374, 3117)

RESOURCE_LIMITS = {
    "character_weight_candidates": 25_000,
    "kostant_weyl_summands": 200_000,
    "laurent_pair_products": 150_000,
    "residual_term_updates": 50_000,
}


def _clean(polynomial: Mapping[Exponent, int]) -> Laurent:
    return {
        exponent: coefficient
        for exponent, coefficient in polynomial.items()
        if coefficient
    }


@dataclass
class ResourceGuard:
    """Deterministic operation caps plus a short wall-clock fail-safe."""

    limits: dict[str, int] = field(default_factory=lambda: dict(RESOURCE_LIMITS))
    counts: dict[str, int] = field(
        default_factory=lambda: {name: 0 for name in RESOURCE_LIMITS}
    )
    started: float = field(default_factory=perf_counter)

    def charge(self, category: str, amount: int = 1) -> None:
        if category not in self.limits:
            raise KeyError(f"unknown resource category {category!r}")
        if amount < 0:
            raise ValueError("resource charge must be nonnegative")
        self.counts[category] += amount
        if self.counts[category] > self.limits[category]:
            raise RuntimeError(
                f"resource cap exceeded for {category}: "
                f"{self.counts[category]} > {self.limits[category]}"
            )
        if perf_counter() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(
                f"exact character build exceeded {MAX_WALL_SECONDS:g} seconds"
            )

    def snapshot(self) -> dict[str, int]:
        return dict(sorted(self.counts.items()))


def _check_laurent_size(polynomial: Mapping[Exponent, int]) -> None:
    if len(polynomial) > MAX_LAURENT_TERMS:
        raise RuntimeError(
            f"Laurent support cap exceeded: {len(polynomial)} > {MAX_LAURENT_TERMS}"
        )
    if polynomial and max(max(abs(x), abs(y)) for x, y in polynomial) > MAX_ABS_EXPONENT:
        raise RuntimeError("Laurent exponent cap exceeded")


def add_scaled(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    scalar: int,
    guard: ResourceGuard,
) -> Laurent:
    guard.charge("residual_term_updates", len(right))
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + scalar * coefficient
        if result[exponent] == 0:
            del result[exponent]
    _check_laurent_size(result)
    return result


def multiply(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    guard: ResourceGuard,
) -> Laurent:
    guard.charge("laurent_pair_products", len(left) * len(right))
    result: Laurent = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            exponent = (left_x + right_x, left_y + right_y)
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
    cleaned = _clean(result)
    _check_laurent_size(cleaned)
    return cleaned


def scale(polynomial: Mapping[Exponent, int], scalar: int) -> Laurent:
    result = _clean(
        {exponent: scalar * coefficient for exponent, coefficient in polynomial.items()}
    )
    _check_laurent_size(result)
    return result


def evaluate_at_identity(polynomial: Mapping[Exponent, int]) -> int:
    return sum(polynomial.values())


def standard_trace_character() -> Laurent:
    return {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}


def standard_exterior_square_character() -> Laurent:
    return {
        (0, 0): 2,
        (1, 1): 1,
        (1, -1): 1,
        (-1, 1): 1,
        (-1, -1): 1,
    }


def statistic_from_defining_characters(guard: ResourceGuard) -> Laurent:
    """Return (Tr U)^2-e_2(U)^2 independently of irreducible characters."""

    trace_square = multiply(standard_trace_character(), standard_trace_character(), guard)
    exterior_square = standard_exterior_square_character()
    exterior_fourth = multiply(exterior_square, exterior_square, guard)
    return add_scaled(trace_square, exterior_fourth, -1, guard)


def weyl_dimension(a: int, b: int) -> int:
    """Weyl dimension for the C2 highest weight a*omega1+b*omega2."""

    if a < 0 or b < 0:
        raise ValueError("fundamental-weight coordinates must be nonnegative")
    numerator = (a + 1) * (b + 1) * (a + b + 2) * (a + 2 * b + 3)
    if numerator % 6:
        raise ArithmeticError("C2 dimension formula unexpectedly nonintegral")
    return numerator // 6


def _weyl_elements() -> tuple[tuple[bool, int, int, int], ...]:
    """Return signed permutations as (swap, sign_1, sign_2, determinant)."""

    return tuple(
        (swap, sign_1, sign_2, (-1 if swap else 1) * sign_1 * sign_2)
        for swap in (False, True)
        for sign_1 in (-1, 1)
        for sign_2 in (-1, 1)
    )


WEYL_ELEMENTS = _weyl_elements()
RHO = (2, 1)


def weyl_action(
    vector: Exponent, element: tuple[bool, int, int, int]
) -> Exponent:
    swap, sign_1, sign_2, _determinant = element
    first, second = vector
    if swap:
        first, second = second, first
    return sign_1 * first, sign_2 * second


class C2CharacterEngine:
    """Small exact C2 character engine using Kostant multiplicities."""

    def __init__(self, guard: ResourceGuard) -> None:
        self.guard = guard
        self._partition_cache: dict[Exponent, int] = {}
        self._character_cache: dict[HighestWeight, Laurent] = {}

    def kostant_partition(self, delta: Exponent) -> int:
        """Partition by the four positive C2 roots, in e-coordinates.

        With simple roots alpha_1=(1,-1), alpha_2=(0,2), write delta as
        p*alpha_1+q*alpha_2.  The remaining positive roots have simple-root
        coordinates (1,1) and (2,1), giving the finite sum below.
        """

        cached = self._partition_cache.get(delta)
        if cached is not None:
            return cached
        first, second = delta
        if first < 0 or (first + second) % 2:
            value = 0
        else:
            second_simple = (first + second) // 2
            if second_simple < 0:
                value = 0
            else:
                value = sum(
                    min(first - 2 * fourth, second_simple - fourth) + 1
                    for fourth in range(min(first // 2, second_simple) + 1)
                )
        self._partition_cache[delta] = value
        return value

    def weight_multiplicity(
        self, highest: HighestWeight, weight: Exponent
    ) -> int:
        self.guard.charge("kostant_weyl_summands", len(WEYL_ELEMENTS))
        shifted_highest = (highest[0] + RHO[0], highest[1] + RHO[1])
        shifted_weight = (weight[0] + RHO[0], weight[1] + RHO[1])
        value = 0
        for element in WEYL_ELEMENTS:
            image = weyl_action(shifted_highest, element)
            delta = (
                image[0] - shifted_weight[0],
                image[1] - shifted_weight[1],
            )
            value += element[3] * self.kostant_partition(delta)
        return value

    def character(self, highest: HighestWeight) -> Laurent:
        if highest in self._character_cache:
            return dict(self._character_cache[highest])
        first, second = highest
        if not 0 <= second <= first <= MAX_HIGHEST_E_COORDINATE:
            raise ValueError(
                "highest weight must satisfy 0 <= lambda_2 <= lambda_1 <= "
                f"{MAX_HIGHEST_E_COORDINATE}"
            )
        candidate_count = (2 * first + 1) ** 2
        self.guard.charge("character_weight_candidates", candidate_count)
        character: Laurent = {}
        for weight_first in range(-first, first + 1):
            for weight_second in range(-first, first + 1):
                weight = (weight_first, weight_second)
                multiplicity = self.weight_multiplicity(highest, weight)
                if multiplicity < 0:
                    raise ArithmeticError(
                        f"negative Kostant weight multiplicity {multiplicity} "
                        f"for highest={highest}, weight={weight}"
                    )
                if multiplicity:
                    character[weight] = multiplicity
        _check_laurent_size(character)
        if character.get(highest) != 1:
            raise ArithmeticError(f"highest-weight multiplicity is not one for {highest}")

        # Weyl invariance is an internal check separate from the dimension formula.
        for weight, multiplicity in character.items():
            for element in WEYL_ELEMENTS:
                if character.get(weyl_action(weight, element), 0) != multiplicity:
                    raise ArithmeticError(f"character is not Weyl-invariant for {highest}")

        a, b = first - second, second
        dimension = weyl_dimension(a, b)
        if evaluate_at_identity(character) != dimension:
            raise ArithmeticError(
                f"Kostant/Weyl dimension mismatch for {a}*omega1+{b}*omega2"
            )
        self._character_cache[highest] = character
        return dict(character)


def weyl_density(guard: ResourceGuard) -> Laurent:
    density: Laurent = {(0, 0): 1}
    for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
        factor = {(0, 0): 2, root: -1, (-root[0], -root[1]): -1}
        density = multiply(density, factor, guard)
    if density.get((0, 0), 0) != 8:
        raise ArithmeticError("unexpected C2 Weyl-density normalization")
    return density


def haar_constant_term(
    polynomial: Mapping[Exponent, int],
    density: Mapping[Exponent, int],
    guard: ResourceGuard,
) -> int:
    numerator = multiply(polynomial, density, guard).get((0, 0), 0)
    if numerator % 8:
        raise ArithmeticError("Haar constant term is not divisible by |W(C2)|=8")
    return numerator // 8


def decompose_character(
    polynomial: Mapping[Exponent, int],
    engine: C2CharacterEngine,
) -> dict[HighestWeight, int]:
    """Greedily decompose a Weyl-invariant character in dominance order."""

    residual = dict(polynomial)
    decomposition: dict[HighestWeight, int] = {}
    while residual:
        dominant_weights = [
            weight
            for weight, coefficient in residual.items()
            if coefficient and weight[0] >= weight[1] >= 0
        ]
        if not dominant_weights:
            raise ArithmeticError("nonzero residual has no dominant weight")
        highest = max(dominant_weights)
        multiplicity = residual[highest]
        if multiplicity <= 0:
            raise ArithmeticError(
                f"nonpositive tensor multiplicity {multiplicity} at {highest}"
            )
        decomposition[highest] = multiplicity
        if len(decomposition) > MAX_IRREDUCIBLES_PER_POWER:
            raise RuntimeError("irreducible-count cap exceeded")
        residual = add_scaled(
            residual, engine.character(highest), -multiplicity, engine.guard
        )
    return decomposition


def reconstruct_character(
    decomposition: Mapping[HighestWeight, int],
    engine: C2CharacterEngine,
) -> Laurent:
    result: Laurent = {}
    for highest, multiplicity in decomposition.items():
        result = add_scaled(result, engine.character(highest), multiplicity, engine.guard)
    return result


def _source_sha256() -> str:
    source = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def _weight_record(highest: HighestWeight, multiplicity: int, sign: int) -> dict:
    first, second = highest
    a, b = first - second, second
    dimension = weyl_dimension(a, b)
    return {
        "highest_weight": {
            "omega1_coefficient": a,
            "omega2_coefficient": b,
            "notation": f"{a}*omega1+{b}*omega2",
            "e_basis_coordinates": [first, second],
        },
        "dimension": dimension,
        "tensor_multiplicity_in_G_power": multiplicity,
        "coefficient_in_F_power": sign * multiplicity,
        "dimension_contribution_to_G_power": dimension * multiplicity,
    }


def build_fixture() -> dict:
    guard = ResourceGuard()
    engine = C2CharacterEngine(guard)

    trivial = engine.character((0, 0))
    omega2 = engine.character((1, 1))
    two_omega2 = engine.character((2, 2))
    positive_character = add_scaled(trivial, omega2, 1, guard)
    positive_character = add_scaled(positive_character, two_omega2, 1, guard)
    if evaluate_at_identity(positive_character) != 20:
        raise ArithmeticError("G=1+chi_omega2+chi_2omega2 must have dimension 20")
    statistic = scale(positive_character, -1)
    defining_statistic = statistic_from_defining_characters(guard)
    if defining_statistic != statistic:
        raise ArithmeticError(
            "F=(Tr U)^2-e_2(U)^2 does not match the irreducible-character identity"
        )
    density = weyl_density(guard)

    current: Laurent = {(0, 0): 1}
    powers: list[dict] = []
    all_reconstructions_exact = True
    all_dimensions_exact = True
    all_trivial_checks_exact = True
    for moment in range(1, MAX_MOMENT + 1):
        current = multiply(current, positive_character, guard)
        decomposition = decompose_character(current, engine)
        reconstruction = reconstruct_character(decomposition, engine)
        reconstruction_exact = reconstruction == current
        if not reconstruction_exact:
            raise ArithmeticError(f"character reconstruction failed at power {moment}")

        sign = -1 if moment % 2 else 1
        trivial_multiplicity = decomposition.get((0, 0), 0)
        signed_trivial = sign * trivial_multiplicity
        independent_haar = haar_constant_term(scale(current, sign), density, guard)
        if independent_haar != FROZEN_HAAR_MOMENTS[moment - 1]:
            raise ArithmeticError(f"independent Haar moment mismatch at power {moment}")
        if signed_trivial != independent_haar:
            raise ArithmeticError(f"trivial/Haar multiplicity mismatch at power {moment}")

        dimension_sum = sum(
            multiplicity
            * weyl_dimension(highest[0] - highest[1], highest[1])
            for highest, multiplicity in decomposition.items()
        )
        expected_dimension = 20**moment
        if dimension_sum != expected_dimension:
            raise ArithmeticError(f"dimension reconstruction failed at power {moment}")
        if not all(multiplicity > 0 for multiplicity in decomposition.values()):
            raise ArithmeticError("tensor multiplicities must all be positive")

        records = [
            _weight_record(highest, decomposition[highest], sign)
            for highest in sorted(decomposition)
        ]
        powers.append(
            {
                "power": moment,
                "global_sign_from_F_equals_minus_G": sign,
                "irreducible_count": len(records),
                "laurent_support_size": len(current),
                "tensor_dimension": expected_dimension,
                "dimension_sum_from_decomposition": dimension_sum,
                "trivial_tensor_multiplicity_in_G_power": trivial_multiplicity,
                "trivial_coefficient_in_F_power": signed_trivial,
                "independent_weyl_constant_term_haar_moment": independent_haar,
                "reconstruction_exact": reconstruction_exact,
                "decomposition": records,
            }
        )
        all_reconstructions_exact &= reconstruction_exact
        all_dimensions_exact &= dimension_sum == expected_dimension
        all_trivial_checks_exact &= signed_trivial == independent_haar

    return {
        "schema_version": "usp4-toy-minor-character-decomposition-v1",
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _source_sha256(),
            "language": "Python stdlib exact integer Laurent arithmetic",
        },
        "status": "PROVED_EXACT_C2_CHARACTER_DECOMPOSITION",
        "group": {
            "name": "USp(4)",
            "root_system": "C2",
            "highest_weight_convention": (
                "a*omega1+b*omega2 corresponds to e-basis coordinates "
                "(lambda1,lambda2)=(a+b,b)"
            ),
            "weyl_order": 8,
            "weyl_vector_e_basis": [2, 1],
            "positive_roots_e_basis": [[2, 0], [0, 2], [1, 1], [1, -1]],
            "dimension_formula": (
                "dim(a*omega1+b*omega2)="
                "(a+1)(b+1)(a+b+2)(a+2b+3)/6"
            ),
        },
        "character_identity": {
            "F": "-(1+chi_(0*omega1+1*omega2)+chi_(0*omega1+2*omega2))",
            "defining_formula": "F=(Tr U)^2-e_2(U)^2",
            "G": "1+chi_(0*omega1+1*omega2)+chi_(0*omega1+2*omega2)",
            "F_equals_minus_G": True,
            "laurent_identity_verified_exactly": True,
            "G_dimension": 20,
            "constituent_dimensions": [1, 5, 14],
        },
        "all_power_corollary": {
            "statement": (
                "For every integer m>=0, Haar(F^m)=(-1)^m times the "
                "multiplicity of the trivial representation in G^tensor_m."
            ),
            "strict_sign_rule": "(-1)^m*Haar(F^m)>0 for every m>=0",
            "integrality": True,
            "proof": (
                "G=1+chi_(0,1)+chi_(0,2) is the character of an honest "
                "self-dual representation containing the trivial summand; "
                "tensor-product multiplicities are nonnegative integers and "
                "the all-trivial tensor supplies at least one invariant."
            ),
            "scope": "compact-group Haar moments only; no finite-family convergence",
        },
        "method": {
            "character_generation": "Kostant multiplicity formula for C2",
            "decomposition": "exact dominant-weight triangular subtraction",
            "trivial_check": "independent C2 Weyl constant-term formula",
            "arithmetic": "integers only",
        },
        "powers": powers,
        "verification": {
            "all_kostant_character_dimensions_match_weyl_formula": True,
            "all_generated_characters_are_weyl_invariant": True,
            "all_power_reconstructions_exact": all_reconstructions_exact,
            "all_tensor_multiplicities_positive": True,
            "all_F_power_coefficients_have_uniform_sign_minus_one_to_m": True,
            "all_dimension_sums_equal_20_to_m": all_dimensions_exact,
            "all_trivial_multiplicities_match_independent_haar_constant_terms": (
                all_trivial_checks_exact
            ),
            "signed_trivial_multiplicities": [
                row["trivial_coefficient_in_F_power"] for row in powers
            ],
            "frozen_haar_moments": list(FROZEN_HAAR_MOMENTS),
        },
        "resource_contract": {
            "maximum_power": MAX_MOMENT,
            "maximum_highest_e_coordinate": MAX_HIGHEST_E_COORDINATE,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "operation_caps": dict(sorted(RESOURCE_LIMITS.items())),
            "observed_operations": guard.snapshot(),
            "random_sampling": False,
            "numerical_integration": False,
            "external_cas": False,
        },
        "scope_firewall": {
            "this_proves": (
                "the exact compact-group character decompositions and Haar moments "
                "listed here"
            ),
            "this_does_not_prove": [
                "finite genus-two family moment convergence",
                "USp(4) equidistribution for the scanned polynomial family",
                "a rate of convergence in q",
                "any number-field L-function statement",
            ],
        },
    }


def _serialized(payload: dict) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the frozen JSON fixture")
    parser.add_argument("--check", action="store_true", help="check the frozen JSON fixture")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    if arguments.write and arguments.check:
        parser.error("--write and --check are mutually exclusive")

    payload = build_fixture()
    rendered = _serialized(payload)
    if arguments.write:
        arguments.output.write_text(rendered, encoding="utf-8")
        return 0
    if arguments.check:
        if not arguments.output.exists():
            raise SystemExit(f"missing fixture: {arguments.output}")
        if arguments.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"fixture drift: regenerate {arguments.output}")
        return 0
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
