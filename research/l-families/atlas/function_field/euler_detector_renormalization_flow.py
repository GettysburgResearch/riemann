#!/usr/bin/env python3
"""Exact bounded probes for a finite-dimensional Euler-detector flow.

This module deliberately separates three operations which are easy to blur:

* a local Euler logarithm is expanded in an ``SU(2)`` character basis;
* independent local increments are aggregated in a cumulant jet, where
  addition is exact modulo the declared jet order;
* normalization by the accumulated variance produces a renormalization
  cocycle, not an autonomous prime-by-prime dynamical system.

All arithmetic is ``Fraction`` arithmetic.  There is no finite-field, curve,
zero, prime-range, numerical-integration, or random-sampling computation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Iterable, Mapping


MAX_CHARACTER_WEIGHT = 96
MAX_MOMENT_ORDER = 10
MAX_LOCAL_FACTORS = 64

CharacterPolynomial = dict[int, Fraction]


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _serialize_character_polynomial(
    polynomial: Mapping[int, Fraction],
) -> dict[str, list[int]]:
    return {
        str(weight): _fraction_pair(coefficient)
        for weight, coefficient in sorted(polynomial.items())
        if coefficient
    }


def _clean_character_polynomial(
    polynomial: Mapping[int, Fraction | int],
) -> CharacterPolynomial:
    result = {
        int(weight): Fraction(coefficient)
        for weight, coefficient in polynomial.items()
        if coefficient
    }
    if any(weight < 0 for weight in result):
        raise ValueError("SU(2) highest weights must be nonnegative")
    if result and max(result) > MAX_CHARACTER_WEIGHT:
        raise RuntimeError(
            f"character weight exceeds the cap {MAX_CHARACTER_WEIGHT}"
        )
    return result


def add_character_polynomials(
    left: Mapping[int, Fraction | int],
    right: Mapping[int, Fraction | int],
) -> CharacterPolynomial:
    result = _clean_character_polynomial(left)
    for weight, coefficient in _clean_character_polynomial(right).items():
        result[weight] = result.get(weight, Fraction(0)) + coefficient
        if not result[weight]:
            del result[weight]
    return result


def scale_character_polynomial(
    polynomial: Mapping[int, Fraction | int], coefficient: Fraction | int
) -> CharacterPolynomial:
    scalar = Fraction(coefficient)
    return _clean_character_polynomial(
        {weight: scalar * value for weight, value in polynomial.items()}
    )


def su2_irrep_product(left_weight: int, right_weight: int) -> tuple[int, ...]:
    """Clebsch--Gordan: chi_a chi_b=sum chi_c in steps of two."""

    if left_weight < 0 or right_weight < 0:
        raise ValueError("SU(2) highest weights must be nonnegative")
    maximum = left_weight + right_weight
    if maximum > MAX_CHARACTER_WEIGHT:
        raise RuntimeError(
            f"character product exceeds the cap {MAX_CHARACTER_WEIGHT}"
        )
    return tuple(range(abs(left_weight - right_weight), maximum + 1, 2))


def multiply_character_polynomials(
    left: Mapping[int, Fraction | int],
    right: Mapping[int, Fraction | int],
) -> CharacterPolynomial:
    left_clean = _clean_character_polynomial(left)
    right_clean = _clean_character_polynomial(right)
    result: CharacterPolynomial = {}
    for left_weight, left_coefficient in left_clean.items():
        for right_weight, right_coefficient in right_clean.items():
            coefficient = left_coefficient * right_coefficient
            for output_weight in su2_irrep_product(left_weight, right_weight):
                result[output_weight] = result.get(output_weight, Fraction(0)) + coefficient
    return _clean_character_polynomial(result)


def character_power(
    polynomial: Mapping[int, Fraction | int], order: int
) -> CharacterPolynomial:
    if order < 0 or order > MAX_MOMENT_ORDER:
        raise ValueError(f"character power must lie in [0,{MAX_MOMENT_ORDER}]")
    result: CharacterPolynomial = {0: Fraction(1)}
    for _ in range(order):
        result = multiply_character_polynomials(result, polynomial)
    return result


def project_character_span(
    polynomial: Mapping[int, Fraction | int], cutoff: int
) -> tuple[CharacterPolynomial, CharacterPolynomial]:
    """Return the retained and discarded parts of a declared finite span."""

    if cutoff < 0 or cutoff > MAX_CHARACTER_WEIGHT:
        raise ValueError("invalid character cutoff")
    clean = _clean_character_polynomial(polynomial)
    return (
        {weight: value for weight, value in clean.items() if weight <= cutoff},
        {weight: value for weight, value in clean.items() if weight > cutoff},
    )


def haar_mean(polynomial: Mapping[int, Fraction | int]) -> Fraction:
    """The SU(2) Haar mean is the multiplicity of the trivial character."""

    return _clean_character_polynomial(polynomial).get(0, Fraction(0))


def projected_power_haar_mean(
    polynomial: Mapping[int, Fraction | int], order: int, cutoff: int
) -> Fraction:
    """Multiply with projection after every step; this is intentionally lossy."""

    if order < 0 or order > MAX_MOMENT_ORDER:
        raise ValueError(f"order must lie in [0,{MAX_MOMENT_ORDER}]")
    result: CharacterPolynomial = {0: Fraction(1)}
    for _ in range(order):
        result, _ = project_character_span(
            multiply_character_polynomials(result, polynomial), cutoff
        )
    return haar_mean(result)


def trace_power_character(power: int) -> CharacterPolynomial:
    """Return Tr(U^power)=chi_power-chi_(power-2) for U in SU(2)."""

    if power < 1 or power > MAX_CHARACTER_WEIGHT:
        raise ValueError("trace power is outside the declared range")
    result: CharacterPolynomial = {power: Fraction(1)}
    if power >= 2:
        result[power - 2] = Fraction(-1)
    return result


def centered_trace_power_character(power: int) -> CharacterPolynomial:
    return center_character_polynomial(trace_power_character(power))


def trace_power_variance(power: int) -> Fraction:
    centered = centered_trace_power_character(power)
    return character_raw_moments(centered, 2)[2]


def trace_channel_critical_sigma(power: int) -> Fraction:
    """Variance-budget boundary for a p^(-power*sigma) trace channel."""

    if power < 1 or power > MAX_MOMENT_ORDER:
        raise ValueError("trace power is outside the declared range")
    return Fraction(1, 2 * power)


def truncated_euler_log_character(z: Fraction | int, rank: int) -> CharacterPolynomial:
    r"""Return sum_{r<=rank} z^r Tr(U^r)/r in the character basis."""

    if rank < 1 or rank > MAX_MOMENT_ORDER:
        raise ValueError(f"rank must lie in [1,{MAX_MOMENT_ORDER}]")
    z = Fraction(z)
    result: CharacterPolynomial = {}
    for power in range(1, rank + 1):
        result = add_character_polynomials(
            result,
            scale_character_polynomial(
                trace_power_character(power), Fraction(z**power, power)
            ),
        )
    return result


def center_character_polynomial(
    polynomial: Mapping[int, Fraction | int],
) -> CharacterPolynomial:
    clean = _clean_character_polynomial(polynomial)
    mean = clean.get(0, Fraction(0))
    if not mean:
        return clean
    return add_character_polynomials(clean, {0: -mean})


def character_raw_moments(
    polynomial: Mapping[int, Fraction | int], maximum_order: int
) -> tuple[Fraction, ...]:
    if maximum_order < 0 or maximum_order > MAX_MOMENT_ORDER:
        raise ValueError(f"maximum order must lie in [0,{MAX_MOMENT_ORDER}]")
    return tuple(
        haar_mean(character_power(polynomial, order))
        for order in range(maximum_order + 1)
    )


def cumulants_from_raw_moments(
    raw_moments: Iterable[Fraction | int],
) -> tuple[Fraction, ...]:
    """Use kappa_n=mu_n-sum C(n-1,j-1) kappa_j mu_(n-j)."""

    moments = tuple(Fraction(value) for value in raw_moments)
    if not moments or moments[0] != 1:
        raise ValueError("raw moment sequence must start with mu_0=1")
    if len(moments) - 1 > MAX_MOMENT_ORDER:
        raise ValueError("moment sequence exceeds the declared cap")
    cumulants = [Fraction(0)] * len(moments)
    for order in range(1, len(moments)):
        cumulants[order] = moments[order] - sum(
            Fraction(comb(order - 1, index - 1))
            * cumulants[index]
            * moments[order - index]
            for index in range(1, order)
        )
    return tuple(cumulants)


def character_cumulants(
    polynomial: Mapping[int, Fraction | int], maximum_order: int
) -> tuple[Fraction, ...]:
    return cumulants_from_raw_moments(
        character_raw_moments(polynomial, maximum_order)
    )


@dataclass(frozen=True)
class DiscreteLaw:
    """A tiny exact probability law used only for finite-jet counterexamples."""

    atoms: tuple[tuple[Fraction, Fraction], ...]

    @classmethod
    def from_mapping(
        cls, atoms: Mapping[Fraction | int, Fraction | int]
    ) -> "DiscreteLaw":
        cleaned = tuple(
            sorted(
                (
                    (Fraction(value), Fraction(probability))
                    for value, probability in atoms.items()
                    if probability
                ),
                key=lambda item: item[0],
            )
        )
        if not cleaned or any(probability < 0 for _, probability in cleaned):
            raise ValueError("probabilities must be nonnegative and nonempty")
        if sum(probability for _, probability in cleaned) != 1:
            raise ValueError("probabilities must sum exactly to one")
        if len(cleaned) > MAX_LOCAL_FACTORS:
            raise RuntimeError("discrete support exceeds the declared cap")
        return cls(cleaned)

    def raw_moments(self, maximum_order: int) -> tuple[Fraction, ...]:
        if maximum_order < 0 or maximum_order > MAX_MOMENT_ORDER:
            raise ValueError("moment order exceeds the declared cap")
        return tuple(
            sum(probability * value**order for value, probability in self.atoms)
            for order in range(maximum_order + 1)
        )

    def cumulants(self, maximum_order: int) -> tuple[Fraction, ...]:
        return cumulants_from_raw_moments(self.raw_moments(maximum_order))

    def translate(self, shift: Fraction | int) -> "DiscreteLaw":
        shift = Fraction(shift)
        return DiscreteLaw.from_mapping(
            {value + shift: probability for value, probability in self.atoms}
        )

    def convolve(self, other: "DiscreteLaw") -> "DiscreteLaw":
        atoms: dict[Fraction, Fraction] = {}
        if len(self.atoms) * len(other.atoms) > MAX_LOCAL_FACTORS**2:
            raise RuntimeError("discrete convolution exceeds the declared cap")
        for left_value, left_probability in self.atoms:
            for right_value, right_probability in other.atoms:
                value = left_value + right_value
                atoms[value] = atoms.get(value, Fraction(0)) + (
                    left_probability * right_probability
                )
        return DiscreteLaw.from_mapping(atoms)

    def positive_probability_after_centering(self) -> Fraction:
        mean = self.raw_moments(1)[1]
        return sum(
            probability for value, probability in self.atoms if value > mean
        )


def finite_difference_twin(jet_order: int = 4) -> tuple[DiscreteLaw, DiscreteLaw]:
    """Two laws with identical moments through ``jet_order``.

    Splitting the alternating (jet_order+1)-st binomial difference into its
    even and odd supports annihilates every polynomial of degree at most the
    requested order.
    """

    if jet_order < 1 or jet_order + 1 > MAX_MOMENT_ORDER:
        raise ValueError("jet order is outside the declared range")
    difference_order = jet_order + 1
    normalizer = 2**jet_order
    even = {
        value: Fraction(comb(difference_order, value), normalizer)
        for value in range(0, difference_order + 1, 2)
    }
    odd = {
        value: Fraction(comb(difference_order, value), normalizer)
        for value in range(1, difference_order + 1, 2)
    }
    return DiscreteLaw.from_mapping(even), DiscreteLaw.from_mapping(odd)


def add_cumulant_jets(*jets: Iterable[Fraction | int]) -> tuple[Fraction, ...]:
    """The exact independent-convolution law in Q[[t]]/(t^(m+1))."""

    materialized = [tuple(Fraction(value) for value in jet) for jet in jets]
    if not materialized:
        raise ValueError("at least one cumulant jet is required")
    length = len(materialized[0])
    if any(len(jet) != length for jet in materialized):
        raise ValueError("cumulant jets must have equal lengths")
    if length - 1 > MAX_MOMENT_ORDER:
        raise ValueError("cumulant jet exceeds the declared cap")
    return tuple(sum(jet[index] for jet in materialized) for index in range(length))


def four_block_eigenvalue(order: int) -> Fraction:
    """Eigenvalue of kappa_order under (X1+...+X4)/2."""

    if order < 2 or order > MAX_MOMENT_ORDER:
        raise ValueError("order is outside the declared standardized jet")
    return Fraction(1, 2 ** (order - 2))


def four_block_standardized_flow(
    standardized_cumulants: Mapping[int, Fraction | int]
) -> dict[int, Fraction]:
    """Exact diagonal four-copy RG map on centered variance-one jets."""

    result: dict[int, Fraction] = {}
    for order, value in standardized_cumulants.items():
        if order < 3 or order > MAX_MOMENT_ORDER:
            raise ValueError("only standardized orders 3 through the cap are stored")
        result[order] = Fraction(value) * four_block_eigenvalue(order)
    return result


def weighted_su2_even_flow(
    variance_weights: Iterable[Fraction | int], maximum_order: int = 8
) -> dict[int, Fraction]:
    r"""Standardized cumulants of sum sqrt(a_p)*chi_1(U_p).

    Only even cumulants are returned, so rational variance weights ``a_p``
    suffice even when their square roots are irrational.
    """

    weights = tuple(Fraction(value) for value in variance_weights)
    if not weights:
        raise ValueError("variance-weight list is empty")
    if len(weights) > MAX_LOCAL_FACTORS:
        raise RuntimeError("variance-weight list exceeds the declared cap")
    if any(weight <= 0 for weight in weights):
        raise ValueError("variance weights must be positive")
    if maximum_order < 4 or maximum_order > MAX_MOMENT_ORDER or maximum_order % 2:
        raise ValueError("maximum order must be even and lie between 4 and the cap")
    base = character_cumulants({1: Fraction(1)}, maximum_order)
    total_variance = sum(weights)
    return {
        order: base[order]
        * sum(weight ** (order // 2) for weight in weights)
        / total_variance ** (order // 2)
        for order in range(4, maximum_order + 1, 2)
    }


def leverage_bound(
    variance_weights: Iterable[Fraction | int], half_order: int
) -> Fraction:
    """Return rho^(half_order-1), the exact power-sum upper bound."""

    weights = tuple(Fraction(value) for value in variance_weights)
    if not weights or any(weight <= 0 for weight in weights):
        raise ValueError("variance weights must be positive and nonempty")
    if half_order < 2:
        raise ValueError("half order must be at least two")
    total = sum(weights)
    rho = max(weights) / total
    return rho ** (half_order - 1)


def two_place_chi1_coupling_packet(maximum_order: int = 8) -> dict[str, object]:
    """Exact coupling defects for equal Haar marginals at two formal places.

    The three couplings are: independent copies, the diagonal copy ``Y=X``,
    and the central-antidiagonal copy ``Y=-X``.  Because the Haar ``chi_1`` law
    is symmetric, every individual marginal is identical in all three cases.
    """

    if maximum_order < 2 or maximum_order > MAX_MOMENT_ORDER:
        raise ValueError("maximum order is outside the declared cap")
    base = character_cumulants({1: Fraction(1)}, maximum_order)
    modes: dict[str, object] = {}
    for name in ("independent", "diagonal", "central_antidiagonal"):
        aggregate: dict[str, list[int]] = {}
        defect: dict[str, list[int]] = {}
        for order in range(1, maximum_order + 1):
            local_sum = 2 * base[order]
            if name == "independent":
                aggregate_value = local_sum
            elif name == "diagonal":
                aggregate_value = 2**order * base[order]
            else:
                aggregate_value = Fraction(0)
            aggregate[str(order)] = _fraction_pair(aggregate_value)
            defect[str(order)] = _fraction_pair(aggregate_value - local_sum)
        modes[name] = {
            "aggregate_cumulants": aggregate,
            "mixed_cumulant_defect": defect,
        }
    return {
        "individual_marginal": "Haar_SU2_chi_1_in_every_mode",
        "modes": modes,
    }


def build_probe() -> dict[str, object]:
    """Build the small exact examples quoted in the companion note."""

    chi_one = {1: Fraction(1)}
    chi_one_moments = character_raw_moments(chi_one, 8)
    chi_one_cumulants = cumulants_from_raw_moments(chi_one_moments)

    local_raw = truncated_euler_log_character(Fraction(1, 2), 2)
    local_centered = center_character_polynomial(local_raw)
    local_moments = character_raw_moments(local_centered, 6)
    local_cumulants = cumulants_from_raw_moments(local_moments)

    exact_fourth = character_raw_moments(chi_one, 4)[4]
    projected_fourth = projected_power_haar_mean(chi_one, 4, cutoff=1)
    _, first_product_defect = project_character_span(
        multiply_character_polynomials(chi_one, chi_one), cutoff=1
    )

    even_law, odd_law = finite_difference_twin(4)
    even_cumulants = even_law.cumulants(5)
    odd_cumulants = odd_law.cumulants(5)

    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    critical_weights = tuple(Fraction(1, prime) for prime in primes)
    convergent_weights = tuple(Fraction(1, prime * prime) for prime in primes)

    return {
        "status": "EXACT_COMPACT_MODEL_AND_FORMAL_JET_PROBE",
        "scope": {
            "compact_group": "SU(2)",
            "arithmetic_family": False,
            "global_euler_product": False,
            "rh_or_grh_consequence": False,
        },
        "local_euler_log_example": {
            "z": [1, 2],
            "trace_power_cutoff": 2,
            "raw_character_coordinates": _serialize_character_polynomial(local_raw),
            "centered_character_coordinates": _serialize_character_polynomial(
                local_centered
            ),
            "centered_moments_0_through_6": [
                _fraction_pair(value) for value in local_moments
            ],
            "centered_cumulants_0_through_6": [
                _fraction_pair(value) for value in local_cumulants
            ],
        },
        "trace_channel_variance_hierarchy": {
            str(power): {
                "centered_character_coordinates": _serialize_character_polynomial(
                    centered_trace_power_character(power)
                ),
                "haar_variance": _fraction_pair(trace_power_variance(power)),
                "critical_sigma": _fraction_pair(
                    trace_channel_critical_sigma(power)
                ),
            }
            for power in range(1, 7)
        },
        "finite_character_projection_obstruction": {
            "declared_span": [0, 1],
            "first_product_discarded": _serialize_character_polynomial(
                first_product_defect
            ),
            "exact_chi1_fourth_moment": _fraction_pair(exact_fourth),
            "project_after_each_product_fourth_moment": _fraction_pair(
                projected_fourth
            ),
        },
        "chi1_reference": {
            "moments_0_through_8": [
                _fraction_pair(value) for value in chi_one_moments
            ],
            "cumulants_0_through_8": [
                _fraction_pair(value) for value in chi_one_cumulants
            ],
            "four_block_eigenvalues_orders_3_through_8": {
                str(order): _fraction_pair(four_block_eigenvalue(order))
                for order in range(3, 9)
            },
        },
        "weighted_prime_prefix_probe": {
            "primes": list(primes),
            "critical_variance_weights_1_over_p": {
                str(order): _fraction_pair(value)
                for order, value in weighted_su2_even_flow(
                    critical_weights
                ).items()
            },
            "summable_variance_weights_1_over_p_squared": {
                str(order): _fraction_pair(value)
                for order, value in weighted_su2_even_flow(
                    convergent_weights
                ).items()
            },
            "critical_maximum_variance_leverage": _fraction_pair(
                max(critical_weights) / sum(critical_weights)
            ),
            "summable_maximum_variance_leverage": _fraction_pair(
                max(convergent_weights) / sum(convergent_weights)
            ),
        },
        "four_jet_nonidentifiability": {
            "even_support_law": [
                [_fraction_pair(value), _fraction_pair(probability)]
                for value, probability in even_law.atoms
            ],
            "odd_support_law": [
                [_fraction_pair(value), _fraction_pair(probability)]
                for value, probability in odd_law.atoms
            ],
            "shared_cumulants_0_through_4": [
                _fraction_pair(value) for value in even_cumulants[:5]
            ],
            "even_fifth_cumulant": _fraction_pair(even_cumulants[5]),
            "odd_fifth_cumulant": _fraction_pair(odd_cumulants[5]),
            "even_probability_above_mean": _fraction_pair(
                even_law.positive_probability_after_centering()
            ),
            "odd_probability_above_mean": _fraction_pair(
                odd_law.positive_probability_after_centering()
            ),
        },
        "two_place_local_marginal_nonidentifiability": (
            two_place_chi1_coupling_packet(8)
        ),
        "resource_contract": {
            "exact_rational_arithmetic": True,
            "random_sampling": False,
            "finite_field_or_curve_enumeration": False,
            "zero_computation": False,
            "maximum_character_weight": MAX_CHARACTER_WEIGHT,
            "maximum_moment_order": MAX_MOMENT_ORDER,
            "maximum_local_factors": MAX_LOCAL_FACTORS,
            "actual_local_factors": len(primes),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--compact",
        action="store_true",
        help="emit compact rather than indented JSON",
    )
    arguments = parser.parse_args()
    print(
        json.dumps(
            build_probe(),
            sort_keys=True,
            indent=None if arguments.compact else 2,
        )
    )


if __name__ == "__main__":
    main()
