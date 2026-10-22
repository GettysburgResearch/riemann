#!/usr/bin/env python3
"""Exact low-rank audit of reciprocal coefficient minors on USp(2g).

For a maximal-torus element with eigenvalue alphabet
``x_1,x_1^-1,...,x_g,x_g^-1``, let ``e_k`` be the elementary
symmetric character.  The reciprocal-centre Hankel minor is

    H_g = e_(g-1)*e_(g+1) - e_g^2 = e_(g-1)^2 - e_g^2.

Dual Jacobi--Trudi gives ``-H_g=s_(2^g)``, an honest Schur functor.
This script independently verifies the Laurent identity for ranks 1, 2,
and 3, decomposes the restricted Schur character into irreducible C_g
characters with Kostant's formula, and checks its first four Haar moments
by a separate Weyl constant-term calculation.

Everything uses capped Python integer arithmetic.  There is no finite-field
enumeration, random sampling, numerical integration, or external CAS.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass, field
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from time import perf_counter
from typing import Mapping, Sequence


Exponent = tuple[int, ...]
Laurent = dict[Exponent, int]

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "usp_coefficient_minor_rank_scan.json"
NOTE_PATH = HERE / "USP_COEFFICIENT_MINOR_RANK_SCAN.md"
MOMENT_PROOF_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"
MOMENT_CHECKER_PATH = HERE / "genus2_moment_identity.py"
CHECKER_PATH = HERE.parents[3] / "tests" / "test_usp_coefficient_minor_rank_scan.py"
FROZEN_RANKS = (1, 2, 3)
MAX_MOMENT = 4
MAX_WALL_SECONDS = 12.0
MAX_LAURENT_SUPPORT = 20_000
MAX_ABS_EXPONENT = 12

RESOURCE_LIMITS = {
    "laurent_pair_products": 2_000_000,
    "constant_term_lookups": 50_000,
    "kostant_weyl_summands": 100_000,
    "partition_states": 250_000,
    "character_weight_candidates": 5_000,
    "decomposition_updates": 100_000,
}


@dataclass
class ResourceGuard:
    limits: dict[str, int] = field(default_factory=lambda: dict(RESOURCE_LIMITS))
    counts: dict[str, int] = field(
        default_factory=lambda: {key: 0 for key in RESOURCE_LIMITS}
    )
    started: float = field(default_factory=perf_counter)

    def charge(self, category: str, amount: int = 1) -> None:
        if category not in self.limits or amount < 0:
            raise ValueError(f"invalid resource charge {category!r}: {amount}")
        self.counts[category] += amount
        if self.counts[category] > self.limits[category]:
            raise RuntimeError(
                f"resource cap exceeded for {category}: "
                f"{self.counts[category]} > {self.limits[category]}"
            )
        if perf_counter() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(
                f"rank scan exceeded {MAX_WALL_SECONDS:g} wall-clock seconds"
            )

    def snapshot(self) -> dict[str, int]:
        return dict(sorted(self.counts.items()))


def _check(polynomial: Mapping[Exponent, int]) -> None:
    if len(polynomial) > MAX_LAURENT_SUPPORT:
        raise RuntimeError("Laurent support cap exceeded")
    if polynomial and max(max(map(abs, exponent)) for exponent in polynomial) > MAX_ABS_EXPONENT:
        raise RuntimeError("Laurent exponent cap exceeded")


def add_scaled(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    scalar: int,
    guard: ResourceGuard,
) -> Laurent:
    guard.charge("decomposition_updates", len(right))
    result = dict(left)
    for exponent, coefficient in right.items():
        value = result.get(exponent, 0) + scalar * coefficient
        if value:
            result[exponent] = value
        else:
            result.pop(exponent, None)
    _check(result)
    return result


def multiply(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    guard: ResourceGuard,
) -> Laurent:
    guard.charge("laurent_pair_products", len(left) * len(right))
    result: Laurent = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exponent, right_exponent))
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
    result = {key: value for key, value in result.items() if value}
    _check(result)
    return result


def scale(polynomial: Mapping[Exponent, int], scalar: int) -> Laurent:
    result = {key: scalar * value for key, value in polynomial.items() if scalar * value}
    _check(result)
    return result


def elementary_character(rank: int, degree: int) -> Laurent:
    """Character of the indicated exterior power of the standard module."""

    if not 0 <= degree <= 2 * rank:
        raise ValueError("exterior degree outside 0..2*rank")
    weights: list[Exponent] = []
    for coordinate in range(rank):
        positive = [0] * rank
        positive[coordinate] = 1
        weights.extend((tuple(positive), tuple(-value for value in positive)))
    result: Laurent = {}
    for selection in itertools.combinations(weights, degree):
        exponent = tuple(sum(weight[index] for weight in selection) for index in range(rank))
        result[exponent] = result.get(exponent, 0) + 1
    return result


def reciprocal_centre_minor(rank: int, guard: ResourceGuard) -> Laurent:
    before = elementary_character(rank, rank - 1)
    centre = elementary_character(rank, rank)
    after = elementary_character(rank, rank + 1)
    if before != after:
        raise ArithmeticError("symplectic reciprocal exterior characters disagree")
    return add_scaled(multiply(before, after, guard), multiply(centre, centre, guard), -1, guard)


def fixed_depth_two_minor(rank: int, guard: ResourceGuard) -> Laurent:
    """Return the genus-two-inspired probe e_1^2-e_2^2 in any rank."""

    first = elementary_character(rank, 1)
    second = elementary_character(rank, 2)
    return add_scaled(multiply(first, first, guard), multiply(second, second, guard), -1, guard)


def dual_jacobi_trudi_rectangle(rank: int, guard: ResourceGuard) -> Laurent:
    """Return s_(2^rank)=e_rank^2-e_(rank-1)e_(rank+1)."""

    centre = elementary_character(rank, rank)
    before = elementary_character(rank, rank - 1)
    after = elementary_character(rank, rank + 1)
    return add_scaled(multiply(centre, centre, guard), multiply(before, after, guard), -1, guard)


def _permutation_sign(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def weyl_elements(rank: int) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    result = []
    for permutation in itertools.permutations(range(rank)):
        permutation_sign = _permutation_sign(permutation)
        for signs in itertools.product((-1, 1), repeat=rank):
            determinant = permutation_sign
            for sign in signs:
                determinant *= sign
            result.append((tuple(permutation), tuple(signs), determinant))
    return tuple(result)


def weyl_action(
    vector: Exponent,
    element: tuple[tuple[int, ...], tuple[int, ...], int],
) -> Exponent:
    permutation, signs, _determinant = element
    return tuple(signs[index] * vector[permutation[index]] for index in range(len(vector)))


def _e_to_simple(vector: Exponent) -> Exponent | None:
    prefixes = [sum(vector[: index + 1]) for index in range(len(vector) - 1)]
    total = sum(vector)
    if total % 2:
        return None
    result = (*prefixes, total // 2)
    return result if all(value >= 0 for value in result) else None


def _positive_roots_e(rank: int) -> tuple[Exponent, ...]:
    roots: list[Exponent] = []
    for left in range(rank):
        doubled = [0] * rank
        doubled[left] = 2
        roots.append(tuple(doubled))
        for right in range(left + 1, rank):
            difference = [0] * rank
            difference[left], difference[right] = 1, -1
            roots.append(tuple(difference))
            total = [0] * rank
            total[left] = total[right] = 1
            roots.append(tuple(total))
    return tuple(roots)


def weyl_dimension(highest: Exponent) -> int:
    rank = len(highest)
    rho = tuple(rank - index for index in range(rank))
    shifted = tuple(highest[index] + rho[index] for index in range(rank))
    value = Fraction(1)
    for root in _positive_roots_e(rank):
        # The coroot of 2e_i is e_i; the scaling cancels in each ratio.
        numerator = sum(shifted[index] * root[index] for index in range(rank))
        denominator = sum(rho[index] * root[index] for index in range(rank))
        value *= Fraction(numerator, denominator)
    if value.denominator != 1:
        raise ArithmeticError("nonintegral Weyl dimension")
    return value.numerator


class CnCharacterEngine:
    def __init__(self, rank: int, guard: ResourceGuard) -> None:
        self.rank = rank
        self.guard = guard
        self.rho = tuple(rank - index for index in range(rank))
        self.weyl = weyl_elements(rank)
        simple_roots = []
        for root in _positive_roots_e(rank):
            converted = _e_to_simple(root)
            if converted is None:
                raise ArithmeticError("positive root did not enter positive simple cone")
            simple_roots.append(converted)
        # Larger roots first keeps the tiny recursion tree shallow.
        self.simple_roots = tuple(sorted(simple_roots, key=lambda root: (sum(root), root), reverse=True))
        self._partition_cache: dict[tuple[int, Exponent], int] = {}
        self._character_cache: dict[Exponent, Laurent] = {}

    def _partition(self, root_index: int, target: Exponent) -> int:
        key = (root_index, target)
        if key in self._partition_cache:
            return self._partition_cache[key]
        self.guard.charge("partition_states")
        if not any(target):
            return 1
        if root_index == len(self.simple_roots):
            return 0
        root = self.simple_roots[root_index]
        bounds = [target[index] // value for index, value in enumerate(root) if value]
        maximum = min(bounds)
        value = 0
        for multiplicity in range(maximum + 1):
            remainder = tuple(
                target[index] - multiplicity * root[index]
                for index in range(self.rank)
            )
            value += self._partition(root_index + 1, remainder)
        self._partition_cache[key] = value
        return value

    def kostant_partition(self, vector: Exponent) -> int:
        simple = _e_to_simple(vector)
        return 0 if simple is None else self._partition(0, simple)

    def weight_multiplicity(self, highest: Exponent, weight: Exponent) -> int:
        shifted_highest = tuple(highest[index] + self.rho[index] for index in range(self.rank))
        shifted_weight = tuple(weight[index] + self.rho[index] for index in range(self.rank))
        self.guard.charge("kostant_weyl_summands", len(self.weyl))
        value = 0
        for element in self.weyl:
            image = weyl_action(shifted_highest, element)
            delta = tuple(image[index] - shifted_weight[index] for index in range(self.rank))
            value += element[2] * self.kostant_partition(delta)
        return value

    def character(self, highest: Exponent) -> Laurent:
        if highest in self._character_cache:
            return dict(self._character_cache[highest])
        if not all(highest[index] >= highest[index + 1] for index in range(self.rank - 1)) or highest[-1] < 0:
            raise ValueError("highest weight must be dominant")
        radius = highest[0]
        self.guard.charge("character_weight_candidates", (2 * radius + 1) ** self.rank)
        result: Laurent = {}
        for weight in itertools.product(range(-radius, radius + 1), repeat=self.rank):
            multiplicity = self.weight_multiplicity(highest, weight)
            if multiplicity < 0:
                raise ArithmeticError(f"negative Kostant multiplicity for {highest}, {weight}")
            if multiplicity:
                result[tuple(weight)] = multiplicity
        if result.get(highest) != 1:
            raise ArithmeticError(f"highest multiplicity is not one for {highest}")
        for weight, multiplicity in result.items():
            if any(result.get(weyl_action(weight, element), 0) != multiplicity for element in self.weyl):
                raise ArithmeticError(f"character is not Weyl-invariant for {highest}")
        if sum(result.values()) != weyl_dimension(highest):
            raise ArithmeticError(f"Weyl dimension mismatch for {highest}")
        self._character_cache[highest] = result
        return dict(result)


def decompose(polynomial: Mapping[Exponent, int], engine: CnCharacterEngine) -> dict[Exponent, int]:
    residual = dict(polynomial)
    result: dict[Exponent, int] = {}
    while residual:
        dominant = [
            weight
            for weight, coefficient in residual.items()
            if coefficient
            and all(weight[index] >= weight[index + 1] for index in range(engine.rank - 1))
            and weight[-1] >= 0
        ]
        if not dominant:
            raise ArithmeticError("residual has no dominant weight")
        highest = max(dominant)
        multiplicity = residual[highest]
        if multiplicity <= 0:
            raise ArithmeticError(
                f"virtual character has negative constituent {multiplicity} at {highest}"
            )
        result[highest] = multiplicity
        residual = add_scaled(residual, engine.character(highest), -multiplicity, engine.guard)
    return result


def fundamental_coordinates(highest: Exponent) -> tuple[int, ...]:
    return tuple(
        highest[index] - highest[index + 1]
        for index in range(len(highest) - 1)
    ) + (highest[-1],)


def weyl_density(rank: int, guard: ResourceGuard) -> Laurent:
    zero = (0,) * rank
    result: Laurent = {zero: 1}
    for root in _positive_roots_e(rank):
        negative = tuple(-value for value in root)
        result = multiply(result, {zero: 2, root: -1, negative: -1}, guard)
    expected = (2**rank) * factorial(rank)
    if result.get(zero, 0) != expected:
        raise ArithmeticError("unexpected Weyl density normalization")
    return result


def haar_constant_term(
    polynomial: Mapping[Exponent, int],
    density: Mapping[Exponent, int],
    rank: int,
    guard: ResourceGuard,
) -> int:
    guard.charge("constant_term_lookups", len(polynomial))
    numerator = sum(
        coefficient
        * density.get(tuple(-value for value in exponent), 0)
        for exponent, coefficient in polynomial.items()
    )
    order = (2**rank) * factorial(rank)
    if numerator % order:
        raise ArithmeticError("nonintegral Haar constant term")
    return numerator // order


def _source_sha256() -> str:
    source = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def _lf_normalized_file_sha256(path: Path) -> str:
    source = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def build_fixture() -> dict[str, object]:
    guard = ResourceGuard()
    ranks = []
    fixed_depth_audits = []
    for rank in FROZEN_RANKS:
        minor = reciprocal_centre_minor(rank, guard)
        schur = dual_jacobi_trudi_rectangle(rank, guard)
        if minor != scale(schur, -1):
            raise ArithmeticError(f"dual Jacobi--Trudi identity failed in rank {rank}")
        engine = CnCharacterEngine(rank, guard)
        decomposition = decompose(schur, engine)
        reconstruction: Laurent = {}
        for highest, multiplicity in decomposition.items():
            reconstruction = add_scaled(reconstruction, engine.character(highest), multiplicity, guard)
        if reconstruction != schur:
            raise ArithmeticError(f"C{rank} reconstruction failed")
        density = weyl_density(rank, guard)
        power: Laurent = {(0,) * rank: 1}
        moments = []
        invariant_multiplicities = []
        for moment in range(1, MAX_MOMENT + 1):
            power = multiply(power, schur, guard)
            invariant = haar_constant_term(power, density, rank, guard)
            invariant_multiplicities.append(invariant)
            moments.append(((-1) ** moment) * invariant)
        dimensions = sum(
            multiplicity * weyl_dimension(highest)
            for highest, multiplicity in decomposition.items()
        )
        if dimensions != sum(schur.values()):
            raise ArithmeticError(f"C{rank} decomposition dimension failed")
        ranks.append(
            {
                "rank": rank,
                "group": f"USp({2 * rank})",
                "rectangle_partition": [2] * rank,
                "schur_dimension": sum(schur.values()),
                "laurent_support_size": len(schur),
                "restricted_character_decomposition": [
                    {
                        "highest_weight_e_basis": list(highest),
                        "highest_weight_fundamental_basis": list(fundamental_coordinates(highest)),
                        "notation": "+".join(
                            f"{coefficient}*omega_{index + 1}"
                            for index, coefficient in enumerate(fundamental_coordinates(highest))
                            if coefficient
                        ) or "trivial",
                        "multiplicity": multiplicity,
                        "dimension": weyl_dimension(highest),
                    }
                    for highest, multiplicity in sorted(decomposition.items())
                ],
                "trivial_multiplicity_in_schur_character": decomposition.get((0,) * rank, 0),
                "invariant_multiplicities_in_powers_1_through_4": invariant_multiplicities,
                "hankel_minor_haar_moments_1_through_4": moments,
                "alternating_weak_sign_verified": all(
                    ((-1) ** (index + 1)) * value >= 0
                    for index, value in enumerate(moments)
                ),
                "even_moments_strictly_positive": all(moments[index - 1] > 0 for index in (2, 4)),
            }
        )

        fixed_minor = fixed_depth_two_minor(rank, guard)
        # The rank-one boundary has the opposite orientation.  From rank two
        # onward e_2^2-e_1^2 is the honest character described below.
        fixed_honest = fixed_minor if rank == 1 else scale(fixed_minor, -1)
        fixed_decomposition = decompose(fixed_honest, engine)
        fixed_power: Laurent = {(0,) * rank: 1}
        fixed_honest_moments = []
        for _moment in range(1, MAX_MOMENT + 1):
            fixed_power = multiply(fixed_power, fixed_honest, guard)
            fixed_honest_moments.append(
                haar_constant_term(fixed_power, density, rank, guard)
            )
        fixed_minor_moments = [
            value if rank == 1 else ((-1) ** moment) * value
            for moment, value in enumerate(fixed_honest_moments, start=1)
        ]
        fixed_depth_audits.append(
            {
                "rank": rank,
                "group": f"USp({2 * rank})",
                "honest_orientation": (
                    "e_1^2-e_2^2" if rank == 1 else "e_2^2-e_1^2"
                ),
                "honest_character_decomposition": [
                    {
                        "highest_weight_fundamental_basis": list(
                            fundamental_coordinates(highest)
                        ),
                        "notation": "+".join(
                            f"{coefficient}*omega_{index + 1}"
                            for index, coefficient in enumerate(
                                fundamental_coordinates(highest)
                            )
                            if coefficient
                        )
                        or "trivial",
                        "multiplicity": multiplicity,
                        "dimension": weyl_dimension(highest),
                    }
                    for highest, multiplicity in sorted(fixed_decomposition.items())
                ],
                "honest_character_moments_1_through_4": fixed_honest_moments,
                "original_probe_moments_1_through_4": fixed_minor_moments,
            }
        )

    # A virtual C2 line just outside the honest-character cone has a much
    # stronger cancellation: every odd Haar moment vanishes, while all even
    # moments have a closed Catalan/binomial form.
    rank = 2
    zero = (0, 0)
    first = elementary_character(rank, 1)
    second = elementary_character(rank, 2)
    balanced = add_scaled(
        scale(multiply(first, first, guard), 2),
        multiply(second, second, guard),
        -1,
        guard,
    )
    factor_one = {(2, 0): 1, (-2, 0): 1}
    factor_two = {(0, 2): 1, (0, -2): 1}
    factored = scale(multiply(factor_one, factor_two, guard), -1)
    if balanced != factored:
        raise ArithmeticError("balanced C2 torus factorization failed")
    c2_engine = CnCharacterEngine(rank, guard)
    expected_virtual = add_scaled(
        c2_engine.character((2, 0)), c2_engine.character((2, 2)), -1, guard
    )
    if balanced != expected_virtual:
        raise ArithmeticError("balanced C2 virtual-character identity failed")
    c2_density = weyl_density(rank, guard)
    for signs in itertools.product((-2, 2), repeat=2):
        if c2_density.get(signs, 0):
            raise ArithmeticError("C2 density unexpectedly has an (+-2,+-2) term")
    even_relevant_density = {
        exponent: coefficient
        for exponent, coefficient in c2_density.items()
        if all(value % 4 == 0 for value in exponent)
    }
    expected_even_relevant_density = {
        (-4, 0): -2,
        (0, -4): -2,
        (0, 0): 8,
        (0, 4): -2,
        (4, 0): -2,
    }
    if even_relevant_density != expected_even_relevant_density:
        raise ArithmeticError("unexpected even-power C2 Weyl-density support")
    balanced_power: Laurent = {zero: 1}
    balanced_moments = []
    for moment in range(1, 7):
        balanced_power = multiply(balanced_power, balanced, guard)
        balanced_moments.append(
            haar_constant_term(balanced_power, c2_density, rank, guard)
        )
    expected_balanced = [
        0 if moment % 2 else comb(moment, moment // 2) ** 2 // (moment // 2 + 1)
        for moment in range(1, 7)
    ]
    if balanced_moments != expected_balanced:
        raise ArithmeticError("balanced C2 all-order formula failed its frozen check")
    finite_balanced_means = []
    for q in (3, 5, 7):
        # Imported exact all-q channel means from GENUS2_MOMENT_IDENTITY.md:
        # <chi_(2,0)>=q^-3-q^-4 and <chi_(0,2)>=-q^-1-q^-5.
        mean = (
            Fraction(1, q)
            + Fraction(1, q**3)
            - Fraction(1, q**4)
            + Fraction(1, q**5)
        )
        finite_balanced_means.append(
            {"q": q, "exact_mean": [mean.numerator, mean.denominator]}
        )

    return {
        "schema": "riemann.function_field.usp_coefficient_minor_rank_scan.v1",
        "status": "PROVED_EXACT_LOW_RANK_AUDIT_PLUS_ALL_RANK_SCHUR_IDENTITY",
        "definition": {
            "e_k": "character of Exterior^k of the USp(2g) standard representation",
            "reciprocity": "e_(2g-k)=e_k on USp(2g)",
            "minor": "H_g=e_(g-1)*e_(g+1)-e_g^2=e_(g-1)^2-e_g^2",
        },
        "all_rank_identity": {
            "statement": "H_g=-s_(2^g) for every g>=1",
            "proof": "Dual Jacobi--Trudi gives s_(2^g)=e_g^2-e_(g-1)e_(g+1); symplectic reciprocity gives e_(g+1)=e_(g-1).",
            "consequence": "For every m>=0, (-1)^m*Haar(H_g^m) is the nonnegative integer dimension of invariants in S_(2^g)(V)^tensor_m.",
            "strictness": "Every positive even moment is strict because S_(2^g)(V) is a nonzero self-dual USp(2g) representation; odd moments may vanish.",
        },
        "rank_audits": ranks,
        "fixed_depth_two_probe": {
            "definition": "F_g=e_1^2-e_2^2",
            "all_rank_g_at_least_2_identity": (
                "-F_g=e_2^2-e_1^2=s_(2,2)+e_1*(e_3-e_1), where e_3-e_1 "
                "is the primitive third-exterior character; at g=2 the second term is zero"
            ),
            "strict_sign_consequence": (
                "For every g>=2 and m>=0, (-1)^m*Haar(F_g^m) is a positive "
                "integer: the honest character -F_g contains one trivial summand."
            ),
            "trivial_multiplicity_proof": (
                "e_1=chi_omega1 has Haar norm squared 1, while "
                "e_2=1+chi_omega2 has Haar norm squared 2; hence "
                "Haar(e_2^2-e_1^2)=1."
            ),
            "rank_one_counterexample": (
                "At g=1, F_1=e_1^2-1=s_(2) is positive honest rather than negative honest."
            ),
            "rank_audits": fixed_depth_audits,
        },
        "usp4_integer_pencil": {
            "definition": "Q_(alpha,beta)=alpha*e_1^2-beta*e_2^2",
            "irreducible_expansion_of_minus_Q": (
                "(2*beta-alpha)*(1+chi_omega2)+(beta-alpha)*chi_2omega1+"
                "beta*chi_2omega2"
            ),
            "honest_negative_cone": (
                "For nonnegative integers alpha,beta, -Q_(alpha,beta) is an "
                "honest character exactly when alpha<=beta."
            ),
            "interpretation": (
                "The original alpha=beta=1 probe is the boundary ray where the "
                "chi_2omega1 constituent cancels; a whole cone therefore has the "
                "same representation-forced alternating moment sign."
            ),
        },
        "usp4_balanced_virtual_probe": {
            "definition": "B=2*e_1^2-e_2^2",
            "character_identity": "B=chi_(2*omega1)-chi_(2*omega2)",
            "torus_factorization": (
                "B=-(x_1^2+x_1^-2)*(x_2^2+x_2^-2)"
            ),
            "all_odd_moments": 0,
            "weyl_density_relevant_coefficients": [
                {"exponent": list(exponent), "coefficient": coefficient}
                for exponent, coefficient in sorted(even_relevant_density.items())
            ],
            "even_moment_formula": (
                "Haar(B^(2r))=binomial(2r,r)^2/(r+1) for every r>=0"
            ),
            "compact_law_factorization": {
                "status": "PROVED_BY_COMPACT_MOMENT_DETERMINACY",
                "statement": (
                    "B has the same law as A*S for independent A and S, where A "
                    "has the arcsine law on [-2,2] and S has the Wigner semicircle "
                    "law on [-2,2]."
                ),
                "arcsine_density": "1/(pi*sqrt(4-x^2)) on (-2,2)",
                "semicircle_density": "sqrt(4-x^2)/(2*pi) on (-2,2)",
                "moment_match": (
                    "E[A^(2r)]=binomial(2r,r), E[S^(2r)]=binomial(2r,r)/(r+1), "
                    "and every odd moment vanishes."
                ),
                "support": [-4, 4],
                "sign_probabilities": {
                    "negative": [1, 2],
                    "zero": [0, 1],
                    "positive": [1, 2],
                },
                "proof": (
                    "The product law and Haar pushforward have identical moments at "
                    "every order and compact support [-4,4], so polynomial density "
                    "determines the measures. Both factors are continuous symmetric "
                    "laws, giving zero atom at zero and equal sign probabilities."
                ),
            },
            "proof": (
                "Odd powers have each exponent congruent to 2 mod 4, while the C2 "
                "Weyl density has zero coefficient at (+-2,+-2). For power 2r, "
                "only density exponents (0,0),(+-4,0),(0,+-4) contribute; their "
                "coefficients 8,-2,-2 reduce the constant term to "
                "C(2r,r)^2/(r+1)."
            ),
            "frozen_moments_1_through_6": balanced_moments,
            "finite_genus_two_family_bridge": {
                "status": "EXACT_CONSEQUENCE_OF_EXISTING_ALL_Q_CHARACTER_MEANS",
                "family": "all monic squarefree quintics over F_q, q an odd prime power",
                "normalization": "B_D=2*a_D^2/q-b_D^2/q^2",
                "formula": "mean(B_D)=1/q+1/q^3-1/q^4+1/q^5",
                "derivation": (
                    "B=chi_(2,0)-chi_(0,2), using the proved means "
                    "mean(chi_(2,0))=q^-3-q^-4 and "
                    "mean(chi_(0,2))=-q^-1-q^-5."
                ),
                "frozen_specializations": finite_balanced_means,
                "interpretation": (
                    "Haar(B)=0 but the exact finite-family mean is positive with "
                    "leading size q^-1; this is a directly isolated arithmetic bias."
                ),
                "dependency": "GENUS2_MOMENT_IDENTITY.md and its exact Q[q] checker",
            },
            "detector_use": (
                "This centered virtual line removes the built-in odd Haar bias and is "
                "a sharper control for testing arithmetic-family odd-moment deviations."
            ),
        },
        "detector_design_interpretation": {
            "result": "The alternating weak Haar-moment sign is built into Schur positivity of the reciprocal-centre minor, not evidence peculiar to genus two or to arithmetic families.",
            "genus_two_exception": "At g=2 the restricted Schur character contains the trivial representation, forcing strict alternating signs at every moment; this strictness does not persist at g=1 or g=3 at the first moment.",
            "control": "The sign-reversed Toeplitz/Newton minor e_g^2-e_(g-1)e_(g+1)=s_(2^g) is an honest-character positive control.",
        },
        "scope": "Compact-group representation theorem plus exact rank-1/2/3 audit only. No finite-family convergence, canonical L-function detector claim, or RH implication.",
        "verification": {
            "all_rank_proof": (
                "The note gives the two-by-two dual Jacobi--Trudi derivations; "
                "the all-rank quantifier is not inferred from the three checked ranks."
            ),
            "low_rank_character_check": (
                "Kostant multiplicities, Weyl dimensions, Weyl invariance, and exact "
                "Laurent reconstruction are all enforced for C1, C2, and C3."
            ),
            "haar_check": (
                "A separate Weyl-density constant-term path checks every frozen moment."
            ),
            "balanced_all_order_check": (
                "The checker independently rebuilds the sparse C2 density without the "
                "producer convolution and verifies the closed moment formula through "
                "order 40; the note proves the symbolic all-order reduction."
            ),
            "acceptance_rule": (
                "--check requires exact JSON equality, including source, checker, note, "
                "and finite-family dependency hashes."
            ),
        },
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _source_sha256(),
            "note": NOTE_PATH.name,
            "note_sha256_lf_normalized": _lf_normalized_file_sha256(NOTE_PATH),
            "checker": "tests/test_usp_coefficient_minor_rank_scan.py",
            "checker_sha256_lf_normalized": _lf_normalized_file_sha256(CHECKER_PATH),
            "arithmetic": "Python standard-library exact integer and rational arithmetic",
        },
        "dependency_locks": {
            "finite_family_mean_proof": {
                "path": MOMENT_PROOF_PATH.name,
                "sha256_lf_normalized": _lf_normalized_file_sha256(MOMENT_PROOF_PATH),
            },
            "finite_family_mean_checker": {
                "path": MOMENT_CHECKER_PATH.name,
                "sha256_lf_normalized": _lf_normalized_file_sha256(MOMENT_CHECKER_PATH),
            },
        },
        "resource_contract": {
            "ranks": list(FROZEN_RANKS),
            "maximum_rank_audit_moment": MAX_MOMENT,
            "maximum_balanced_virtual_check_moment": 6,
            "random_sampling": False,
            "numerical_integration": False,
            "finite_field_enumeration": False,
            "external_dependencies": False,
            "hard_caps": RESOURCE_LIMITS,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "maximum_laurent_support": MAX_LAURENT_SUPPORT,
            "maximum_abs_exponent": MAX_ABS_EXPONENT,
            "observed_counts": guard.snapshot(),
        },
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, nargs="?", const=DEFAULT_OUTPUT)
    parser.add_argument("--write", type=Path, nargs="?", const=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"rank-scan fixture mismatch: {args.check}")
        print(f"OK: exact USp coefficient-minor rank scan matches {args.check}")
        return 0
    if args.write:
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact rank-scan fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
