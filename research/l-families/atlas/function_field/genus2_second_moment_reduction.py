#!/usr/bin/env python3
"""Bounded exact roadmap certificate for the genus-two second toy moment.

The certificate performs no finite-field or polynomial-family enumeration.  It
does four small exact tasks:

* enumerate the factor-exponent signatures in the ``a^2 b^2`` and ``b^4``
  character expansions;
* compute their ordered-tuple weights and exact type-count polynomials;
* replay the q=3,5,7 ``K`` histograms as checksums for the unresolved block;
* verify the relevant USp(4) character decompositions using the C2 Weyl
  alternant identity, without importing a character table.

The output is a proof roadmap, not an all-q second-moment formula.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "genus2_second_moment_reduction.json"
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
MOMENT_NOTE = HERE / "GENUS2_MOMENT_IDENTITY.md"
MOMENT_CERTIFICATE = HERE / "genus2_moment_identity.py"

MAX_SIGNATURES = 74
MAX_PARTITION_DEGREE = 8
MAX_OPERATIONS = 50_000
MAX_WALL_SECONDS = 2.0
CLOCK_CHECK_INTERVAL = 256
FROZEN_Q_VALUES = (3, 5, 7)


class ResourceLimitError(RuntimeError):
    """Raised before a frozen symbolic or time budget can be exceeded."""


@dataclass
class Budget:
    operation_limit: int
    deadline: float
    clock: Callable[[], float]
    operations: int = 0
    next_clock_check: int = 0

    def guard(self) -> None:
        if self.clock() >= self.deadline:
            raise TimeoutError("second-moment reduction exceeded its monotonic wall deadline")

    def tick(self, count: int = 1) -> None:
        if count < 0:
            raise ValueError("operation increment must be nonnegative")
        self.operations += count
        if self.operations > self.operation_limit:
            raise ResourceLimitError(
                f"second-moment reduction exceeded {self.operation_limit} exact operations"
            )
        if self.operations >= self.next_clock_check:
            self.guard()
            self.next_clock_check = self.operations + CLOCK_CHECK_INTERVAL


Polynomial = tuple[Fraction, ...]
Exponent = tuple[int, int]
Laurent = dict[Exponent, int]


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        _normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _trim_polynomial(coefficients: Iterable[Fraction]) -> Polynomial:
    values = [Fraction(value) for value in coefficients]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [Fraction(0)])


def _poly_add(left: Polynomial, right: Polynomial, budget: Budget) -> Polynomial:
    size = max(len(left), len(right))
    result: list[Fraction] = []
    for index in range(size):
        budget.tick()
        result.append(
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
        )
    return _trim_polynomial(result)


def _poly_scale(value: Polynomial, scalar: Fraction, budget: Budget) -> Polynomial:
    budget.tick(len(value))
    return _trim_polynomial(coefficient * scalar for coefficient in value)


def _poly_multiply(left: Polynomial, right: Polynomial, budget: Budget) -> Polynomial:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            budget.tick()
            result[left_index + right_index] += left_value * right_value
    if len(result) - 1 > MAX_PARTITION_DEGREE:
        raise ResourceLimitError("type-count polynomial exceeded degree eight")
    return _trim_polynomial(result)


def _poly_falling(value: Polynomial, length: int, budget: Budget) -> Polynomial:
    result: Polynomial = (Fraction(1),)
    for offset in range(length):
        result = _poly_multiply(
            result,
            _poly_add(value, (Fraction(-offset),), budget),
            budget,
        )
    return result


def _poly_evaluate(value: Polynomial, q: int, budget: Budget) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(value):
        budget.tick()
        result = result * q + coefficient
    return result


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _polynomial_pairs(value: Polynomial) -> list[list[int]]:
    return [_fraction_pair(coefficient) for coefficient in value]


def _partitions(total: int, maximum: int | None = None) -> Iterable[tuple[int, ...]]:
    if total < 0 or total > MAX_PARTITION_DEGREE:
        raise ValueError(f"partition total must lie in [0,{MAX_PARTITION_DEGREE}]")
    if total == 0:
        yield ()
        return
    upper = min(total, maximum if maximum is not None else total)
    for first in range(upper, 0, -1):
        for rest in _partitions(total - first, first):
            yield (first, *rest)


def _multiplicity_denominator(partition: tuple[int, ...]) -> int:
    return math.prod(math.factorial(count) for count in Counter(partition).values())


def _type_count_polynomial(
    linear: tuple[int, ...], quadratic: tuple[int, ...], budget: Budget
) -> Polynomial:
    q: Polynomial = (Fraction(0), Fraction(1))
    irreducible_quadratics: Polynomial = (
        Fraction(0),
        Fraction(-1, 2),
        Fraction(1, 2),
    )
    linear_count = _poly_scale(
        _poly_falling(q, len(linear), budget),
        Fraction(1, _multiplicity_denominator(linear)),
        budget,
    )
    quadratic_count = _poly_scale(
        _poly_falling(irreducible_quadratics, len(quadratic), budget),
        Fraction(1, _multiplicity_denominator(quadratic)),
        budget,
    )
    return _poly_multiply(linear_count, quadratic_count, budget)


def _linear_atoms(linear_count: int, quadratic_count: int) -> tuple[tuple[int, ...], ...]:
    atoms: list[tuple[int, ...]] = []
    width = linear_count + quadratic_count
    for index in range(linear_count):
        atom = [0] * width
        atom[index] = 1
        atoms.append(tuple(atom))
    return tuple(atoms)


def _quadratic_atoms(
    linear_count: int, quadratic_count: int
) -> tuple[tuple[int, ...], ...]:
    atoms: list[tuple[int, ...]] = []
    width = linear_count + quadratic_count
    for index in range(quadratic_count):
        atom = [0] * width
        atom[linear_count + index] = 1
        atoms.append(tuple(atom))
    for left in range(linear_count):
        for right in range(left, linear_count):
            atom = [0] * width
            atom[left] += 1
            atom[right] += 1
            atoms.append(tuple(atom))
    return tuple(atoms)


def _tuple_weight(
    linear: tuple[int, ...],
    quadratic: tuple[int, ...],
    slot_kinds: tuple[str, ...],
    budget: Budget,
) -> int:
    target = (*linear, *quadratic)
    atom_sets = {
        "L": _linear_atoms(len(linear), len(quadratic)),
        "Q": _quadratic_atoms(len(linear), len(quadratic)),
    }
    cache: dict[tuple[int, tuple[int, ...]], int] = {}

    def count(position: int, remaining: tuple[int, ...]) -> int:
        key = position, remaining
        cached = cache.get(key)
        if cached is not None:
            return cached
        if position == len(slot_kinds):
            result = int(not any(remaining))
            cache[key] = result
            return result
        result = 0
        for atom in atom_sets[slot_kinds[position]]:
            budget.tick()
            if all(atom[index] <= remaining[index] for index in range(len(remaining))):
                result += count(
                    position + 1,
                    tuple(remaining[index] - atom[index] for index in range(len(remaining))),
                )
        cache[key] = result
        return result

    weight = count(0, target)
    if weight <= 0:
        raise ArithmeticError(f"signature {(linear, quadratic)} has no tuple realization")
    return weight


def _signature_row(
    block: str,
    linear: tuple[int, ...],
    quadratic: tuple[int, ...],
    slot_kinds: tuple[str, ...],
    budget: Budget,
) -> tuple[dict[str, object], Polynomial]:
    count_polynomial = _type_count_polynomial(linear, quadratic, budget)
    specializations: dict[str, int] = {}
    for q in FROZEN_Q_VALUES:
        value = _poly_evaluate(count_polynomial, q, budget)
        if value.denominator != 1 or value < 0:
            raise ArithmeticError("type-count specialization is not a nonnegative integer")
        specializations[str(q)] = value.numerator
    weight = _tuple_weight(linear, quadratic, slot_kinds, budget)
    linear_multiplicities = Counter(linear)
    quadratic_multiplicities = Counter(quadratic)
    linear_denominator = _multiplicity_denominator(linear)
    quadratic_denominator = _multiplicity_denominator(quadratic)
    radical_degree = sum(exponent % 2 for exponent in linear) + 2 * sum(
        exponent % 2 for exponent in quadratic
    )
    if radical_degree % 2:
        raise ArithmeticError("an even-degree modulus produced an odd conductor degree")
    row: dict[str, object] = {
        "signature": (
            f"L[{','.join(map(str, linear)) or '-'}]."
            f"Q[{','.join(map(str, quadratic)) or '-'}]"
        ),
        "linear_exponents": list(linear),
        "quadratic_prime_exponents": list(quadratic),
        "linear_degree": sum(linear),
        "quadratic_prime_occurrences": sum(quadratic),
        "total_degree": sum(linear) + 2 * sum(quadratic),
        "linear_support": len(linear),
        "quadratic_support": len(quadratic),
        "odd_radical": {
            "linear_prime_count": sum(exponent % 2 for exponent in linear),
            "quadratic_prime_count": sum(exponent % 2 for exponent in quadratic),
            "degree": radical_degree,
        },
        "even_exponent_support": {
            "linear_prime_count": sum(exponent % 2 == 0 for exponent in linear),
            "quadratic_prime_count": sum(exponent % 2 == 0 for exponent in quadratic),
        },
        "tuple_weight": weight,
        "type_count": {
            "formula": (
                f"(q)_{len(linear)}/{linear_denominator} * "
                f"(I)_{len(quadratic)}/{quadratic_denominator}, I=q*(q-1)/2"
            ),
            "linear_exponent_multiplicities": {
                str(exponent): linear_multiplicities[exponent]
                for exponent in sorted(linear_multiplicities)
            },
            "quadratic_exponent_multiplicities": {
                str(exponent): quadratic_multiplicities[exponent]
                for exponent in sorted(quadratic_multiplicities)
            },
            "coefficients_low_to_high": _polynomial_pairs(count_polynomial),
            "specializations": specializations,
        },
        "block": block,
    }
    return row, count_polynomial


def _build_signature_block(
    block: str,
    quadratic_slots: int,
    slot_kinds: tuple[str, ...],
    expected_count: int,
    total_degree: int,
    budget: Budget,
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    weighted_total: Polynomial = (Fraction(0),)
    for quadratic_occurrences in range(quadratic_slots + 1):
        linear_degree = total_degree - 2 * quadratic_occurrences
        for linear in _partitions(linear_degree):
            for quadratic in _partitions(quadratic_occurrences):
                if len(rows) >= expected_count:
                    raise ResourceLimitError(
                        f"{block} signature enumeration exceeded its exact cap {expected_count}"
                    )
                row, count_polynomial = _signature_row(
                    block, linear, quadratic, slot_kinds, budget
                )
                rows.append(row)
                weighted_total = _poly_add(
                    weighted_total,
                    _poly_scale(count_polynomial, Fraction(row["tuple_weight"]), budget),
                    budget,
                )
    if len(rows) != expected_count:
        raise ArithmeticError(
            f"{block} produced {len(rows)} signatures instead of {expected_count}"
        )
    expected_total: Polynomial = tuple(
        Fraction(int(index == total_degree)) for index in range(total_degree + 1)
    )
    if weighted_total != expected_total:
        raise ArithmeticError(f"{block} tuple weights do not sum to q^{total_degree}")
    return {
        "block": block,
        "signature_count": len(rows),
        "signature_count_derivation": (
            "11+5+4=20" if block == "M22" else "22+11+10+6+5=54"
        ),
        "slot_generating_function": (
            "(sum_i x_i)^2*(sum_{i<=j}x_i*x_j+sum_s y_s)^2"
            if block == "M22"
            else "(sum_{i<=j}x_i*x_j+sum_s y_s)^4"
        ),
        "weighted_tuple_count_coefficients_low_to_high": _polynomial_pairs(weighted_total),
        "weighted_tuple_count_formula": f"q^{total_degree}",
        "maximum_tuple_weight": max(int(row["tuple_weight"]) for row in rows),
        "signatures": rows,
    }


def _laurent_clean(value: Mapping[Exponent, int]) -> Laurent:
    return {exponent: coefficient for exponent, coefficient in value.items() if coefficient}


def _laurent_add(values: Iterable[Mapping[Exponent, int]], budget: Budget) -> Laurent:
    result: Laurent = {}
    for value in values:
        for exponent, coefficient in value.items():
            budget.tick()
            result[exponent] = result.get(exponent, 0) + coefficient
    return _laurent_clean(result)


def _laurent_scale(value: Mapping[Exponent, int], scalar: int, budget: Budget) -> Laurent:
    budget.tick(len(value))
    return _laurent_clean(
        {exponent: coefficient * scalar for exponent, coefficient in value.items()}
    )


def _laurent_multiply(
    left: Mapping[Exponent, int], right: Mapping[Exponent, int], budget: Budget
) -> Laurent:
    result: Laurent = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            budget.tick()
            exponent = left_x + right_x, left_y + right_y
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
    return _laurent_clean(result)


def _laurent_power(value: Mapping[Exponent, int], exponent: int, budget: Budget) -> Laurent:
    if exponent < 0 or exponent > 4:
        raise ValueError("Laurent exponent must lie in [0,4]")
    result: Laurent = {(0, 0): 1}
    for _ in range(exponent):
        result = _laurent_multiply(result, value, budget)
    return result


def _weyl_alternant(weight: tuple[int, int], budget: Budget) -> Laurent:
    first, second = weight
    if not first > second > 0:
        raise ValueError("C2 alternant weight must be strictly dominant and positive")
    terms: Laurent = {}
    for swapped, permutation_sign in ((False, 1), (True, -1)):
        base = (second, first) if swapped else (first, second)
        for first_sign in (-1, 1):
            for second_sign in (-1, 1):
                budget.tick()
                exponent = first_sign * base[0], second_sign * base[1]
                coefficient = permutation_sign * first_sign * second_sign
                terms[exponent] = terms.get(exponent, 0) + coefficient
    return _laurent_clean(terms)


def _dimension(label: tuple[int, int]) -> int:
    a, b = label
    numerator = (a + 1) * (b + 1) * (a + b + 2) * (a + 2 * b + 3)
    if numerator % 6:
        raise ArithmeticError("C2 Weyl dimension formula was not integral")
    return numerator // 6


def _verify_character_decomposition(
    value: Mapping[Exponent, int],
    decomposition: tuple[tuple[tuple[int, int], int], ...],
    budget: Budget,
) -> None:
    rho = (2, 1)
    left = _laurent_multiply(value, _weyl_alternant(rho, budget), budget)
    right_terms: list[Laurent] = []
    for (a, b), multiplicity in decomposition:
        highest_weight = (a + b, b)
        alternant = _weyl_alternant(
            (highest_weight[0] + rho[0], highest_weight[1] + rho[1]), budget
        )
        right_terms.append(_laurent_scale(alternant, multiplicity, budget))
    right = _laurent_add(right_terms, budget)
    if left != right:
        raise ArithmeticError("C2 Weyl-alternant character decomposition failed")


def _decomposition_rows(
    decomposition: tuple[tuple[tuple[int, int], int], ...]
) -> list[dict[str, object]]:
    return [
        {
            "highest_weight_a_b": [label[0], label[1]],
            "multiplicity": multiplicity,
            "dimension": _dimension(label),
        }
        for label, multiplicity in decomposition
    ]


def _character_certificate(budget: Budget) -> dict[str, object]:
    trace: Laurent = {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}
    exterior_square: Laurent = {
        (0, 0): 2,
        (1, 1): 1,
        (1, -1): 1,
        (-1, 1): 1,
        (-1, -1): 1,
    }
    statistic = _laurent_add(
        (
            _laurent_power(trace, 2, budget),
            _laurent_scale(_laurent_power(exterior_square, 2, budget), -1, budget),
        ),
        budget,
    )
    statistic_squared = _laurent_power(statistic, 2, budget)
    trace_fourth = _laurent_power(trace, 4, budget)
    mixed_trace_middle = _laurent_multiply(
        _laurent_power(trace, 2, budget), exterior_square, budget
    )
    virtual_value = _laurent_add(
        (statistic_squared, _laurent_scale(trace_fourth, -1, budget)), budget
    )

    statistic_decomposition = (
        ((0, 0), -1),
        ((0, 1), -1),
        ((0, 2), -1),
    )
    trace_fourth_decomposition = (
        ((0, 0), 3),
        ((0, 1), 5),
        ((2, 0), 6),
        ((0, 2), 2),
        ((2, 1), 3),
        ((4, 0), 1),
    )
    mixed_trace_middle_decomposition = (
        ((0, 0), 2),
        ((0, 1), 3),
        ((2, 0), 3),
        ((0, 2), 1),
        ((2, 1), 1),
    )
    statistic_squared_decomposition = (
        ((0, 0), 3),
        ((0, 1), 4),
        ((2, 0), 2),
        ((0, 2), 4),
        ((2, 1), 2),
        ((4, 0), 1),
        ((0, 3), 2),
        ((2, 2), 1),
        ((0, 4), 1),
    )
    virtual_decomposition = (
        ((0, 1), -1),
        ((2, 0), -4),
        ((0, 2), 2),
        ((2, 1), -1),
        ((0, 3), 2),
        ((2, 2), 1),
        ((0, 4), 1),
    )
    high_weight_decomposition = (
        ((0, 3), 2),
        ((2, 2), 1),
        ((0, 4), 1),
    )

    _verify_character_decomposition(statistic, statistic_decomposition, budget)
    _verify_character_decomposition(
        trace_fourth, trace_fourth_decomposition, budget
    )
    _verify_character_decomposition(
        mixed_trace_middle, mixed_trace_middle_decomposition, budget
    )
    _verify_character_decomposition(
        statistic_squared, statistic_squared_decomposition, budget
    )
    _verify_character_decomposition(virtual_value, virtual_decomposition, budget)

    statistic_at_identity = sum(statistic.values())
    if statistic_at_identity != -20:
        raise ArithmeticError("F(identity) is not -20")
    trace_dimension = sum(
        multiplicity * _dimension(label)
        for label, multiplicity in trace_fourth_decomposition
    )
    mixed_trace_middle_dimension = sum(
        multiplicity * _dimension(label)
        for label, multiplicity in mixed_trace_middle_decomposition
    )
    statistic_square_dimension = sum(
        multiplicity * _dimension(label)
        for label, multiplicity in statistic_squared_decomposition
    )
    virtual_dimension = sum(
        multiplicity * _dimension(label)
        for label, multiplicity in virtual_decomposition
    )
    if trace_dimension != 4**4 or statistic_square_dimension != (-20) ** 2:
        raise ArithmeticError("character decomposition dimension checksum failed")
    if mixed_trace_middle_dimension != 4**2 * 6:
        raise ArithmeticError("mixed trace-middle character checksum failed")
    if virtual_dimension != statistic_square_dimension - trace_dimension:
        raise ArithmeticError("virtual obstruction dimension checksum failed")
    high_weight_dimension = sum(
        multiplicity * _dimension(label)
        for label, multiplicity in high_weight_decomposition
    )
    if high_weight_dimension != 196:
        raise ArithmeticError("honest high-weight packet dimension checksum failed")

    return {
        "method": (
            "coefficientwise C2 Weyl-alternant identity "
            "G*A_rho=sum multiplicity*A_(lambda+rho)"
        ),
        "weight_convention": "highest_weight=a*omega_1+b*omega_2",
        "statistic_identity": {
            "formula": "F=(Tr U)^2-e_2(U)^2=-(chi_00+chi_01+chi_02)",
            "F_at_identity": statistic_at_identity,
            "decomposition": _decomposition_rows(statistic_decomposition),
        },
        "trace_fourth": {
            "formula": (
                "(Tr U)^4=3*chi_00+5*chi_01+6*chi_20+2*chi_02+"
                "3*chi_21+chi_40"
            ),
            "dimension_checksum": trace_dimension,
            "decomposition": _decomposition_rows(trace_fourth_decomposition),
        },
        "mixed_trace_middle": {
            "formula": (
                "(Tr U)^2*e_2(U)=2*chi_00+3*chi_01+3*chi_20+"
                "chi_02+chi_21"
            ),
            "arithmetic_normalization": "a_D^2*b_D/q^2=(Tr U)^2*e_2(U)",
            "dimension_checksum": mixed_trace_middle_dimension,
            "decomposition": _decomposition_rows(mixed_trace_middle_decomposition),
        },
        "statistic_squared": {
            "formula": (
                "F^2=3*chi_00+4*chi_01+2*chi_20+4*chi_02+2*chi_21+"
                "chi_40+2*chi_03+chi_22+chi_04"
            ),
            "dimension_checksum": statistic_square_dimension,
            "haar_second_moment_target": 3,
            "decomposition": _decomposition_rows(statistic_squared_decomposition),
        },
        "single_virtual_character_obstruction": {
            "status": "EXACT_REDUCTION_UNRESOLVED_FOR_GENERAL_Q",
            "formula": (
                "F^2-(Tr U)^4=chi_04+chi_22+2*chi_03-chi_21+"
                "2*chi_02-4*chi_20-chi_01"
            ),
            "dimension_checksum": virtual_dimension,
            "decomposition": _decomposition_rows(virtual_decomposition),
            "proof_burden": (
                "Evaluate this one virtual-character average over H_5(q); the exact "
                "trace-fourth average is already supplied by the bound moment proof."
            ),
        },
        "refined_honest_high_weight_obstruction": {
            "status": "EXACT_REDUCTION_USING_PROVED_LOW_WEIGHT_MEANS",
            "formula": "H=chi_04+chi_22+2*chi_03",
            "dimension_checksum": high_weight_dimension,
            "decomposition": _decomposition_rows(high_weight_decomposition),
            "virtual_split": (
                "F^2-(Tr U)^4=H+L, "
                "L=-chi_21+2*chi_02-4*chi_20-chi_01"
            ),
            "exact_low_weight_average": (
                "mean(L)=-1/q-1/q^2-6/q^3+6/q^4"
            ),
            "limit_equivalence": (
                "Because the exact trace-fourth mean tends to 3 and mean(L) tends "
                "to 0, mean(F^2) tends to 3 if and only if mean(H) tends to 0."
            ),
            "proof_burden": (
                "Only the honest high-weight packet chi_04+chi_22+2*chi_03 remains; "
                "all five lower-weight channels are supplied by exact coefficient moments."
            ),
        },
    }


def _a_fourth_total(q: int) -> int:
    return q * (q - 1) * (q + 1) * (
        3 * q**4 - 10 * q**3 + 15 * q**2 - 3 * q - 11
    )


def _known_low_weight_correction(q: int) -> Fraction:
    """Exact mean of -chi_21+2 chi_02-4 chi_20-chi_01."""

    return -Fraction(1, q) - Fraction(1, q**2) - Fraction(6, q**3) + Fraction(6, q**4)


def _finite_histogram_checks(q_scan: Mapping[str, object], budget: Budget) -> list[dict[str, object]]:
    expected = {
        3: (162, 2_112, 14_448, Fraction(2_408, 3**7), -4_560, -760),
        5: (2_500, 116_880, 2_630_080, Fraction(131_504, 5**7), -291_920, -14_596),
        7: (14_406, 1_503_936, 69_108_480, Fraction(1_645_440, 7**7), -4_584_384, -109_152),
    }
    families = q_scan.get("families")
    if not isinstance(families, list) or [row.get("q") for row in families] != list(
        FROZEN_Q_VALUES
    ):
        raise ValueError("bound q-scan lost its exact q=3,5,7 family order")
    checks: list[dict[str, object]] = []
    for family in families:
        q = int(family["q"])
        member_count = int(family["member_count"])
        histogram = family["K_histogram"]
        if not isinstance(histogram, dict):
            raise TypeError("K histogram is not an object")
        histogram_count = 0
        sum_k = 0
        sum_k_squared = 0
        for key, count_value in histogram.items():
            budget.tick(3)
            k = int(key)
            count = int(count_value)
            histogram_count += count
            sum_k += count * k
            sum_k_squared += count * k * k
        if histogram_count != member_count:
            raise ArithmeticError("K histogram does not reconstruct the family")
        if sum_k != int(family["moments"]["K"]["sum"]):
            raise ArithmeticError("K histogram first moment drifted")
        sum_a_fourth = int(family["moments"]["a_fourth"]["sum"])
        if sum_a_fourth != _a_fourth_total(q):
            raise ArithmeticError("q-scan a^4 total differs from the all-q certificate")
        normalized_second = Fraction(sum_k_squared, member_count * q**4)
        residual = sum_k_squared - q**2 * sum_a_fourth
        residual_quotient = Fraction(residual, q * (q - 1))
        expected_row = expected[q]
        actual_row = (
            member_count,
            sum_a_fourth,
            sum_k_squared,
            normalized_second,
            residual,
            residual_quotient,
        )
        if actual_row != expected_row:
            raise ArithmeticError(f"q={q} second-moment checksum drifted")
        virtual_average = Fraction(residual, member_count * q**4)
        low_weight_correction = _known_low_weight_correction(q)
        high_weight_average = virtual_average - low_weight_correction
        checks.append(
            {
                "q": q,
                "member_count": member_count,
                "histogram_bin_count": len(histogram),
                "sum_K_squared": sum_k_squared,
                "normalized_second_moment_Z": _fraction_pair(normalized_second),
                "sum_a_fourth": sum_a_fourth,
                "q_squared_sum_a_fourth": q**2 * sum_a_fourth,
                "unresolved_B4_minus_2qM22": residual,
                "unresolved_residual_over_q_qminus_1": _fraction_pair(
                    residual_quotient
                ),
                "normalized_virtual_character_obstruction": _fraction_pair(
                    virtual_average
                ),
                "exact_low_weight_character_correction": _fraction_pair(
                    low_weight_correction
                ),
                "normalized_honest_high_weight_packet": _fraction_pair(
                    high_weight_average
                ),
            }
        )
    return checks


def _source_locks(q_scan: Mapping[str, object]) -> dict[str, object]:
    q_payload = dict(q_scan)
    claimed_payload_sha256 = q_payload.pop("payload_sha256", None)
    computed_payload_sha256 = _canonical_sha256(q_payload)
    if claimed_payload_sha256 != computed_payload_sha256:
        raise ValueError("bound q-scan payload hash mismatch")
    return {
        "q_scan": {
            "path": "research/l-families/atlas/function_field/genus2_q_scan.json",
            "canonical_sha256": _canonical_sha256(q_scan),
            "payload_sha256": claimed_payload_sha256,
        },
        "coefficient_moment_proof_note": {
            "path": "research/l-families/atlas/function_field/GENUS2_MOMENT_IDENTITY.md",
            "sha256_lf_normalized": _lf_normalized_sha256(MOMENT_NOTE),
        },
        "exact_polynomial_certificate": {
            "path": "research/l-families/atlas/function_field/genus2_moment_identity.py",
            "sha256_lf_normalized": _lf_normalized_sha256(MOMENT_CERTIFICATE),
        },
        "roadmap_generator": {
            "path": (
                "research/l-families/atlas/function_field/"
                "genus2_second_moment_reduction.py"
            ),
            "sha256_lf_normalized": _lf_normalized_sha256(Path(__file__).resolve()),
        },
    }


def build_fixture(
    *,
    operation_limit: int = MAX_OPERATIONS,
    maximum_wall_seconds: float = MAX_WALL_SECONDS,
    clock: Callable[[], float] = time.monotonic,
) -> dict[str, object]:
    if operation_limit <= 0 or operation_limit > MAX_OPERATIONS:
        raise ValueError(f"operation limit must lie in (0,{MAX_OPERATIONS}]")
    if maximum_wall_seconds <= 0 or maximum_wall_seconds > MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    start = clock()
    budget = Budget(operation_limit, start + maximum_wall_seconds, clock)
    budget.guard()

    q_scan = json.loads(Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
    source_locks = _source_locks(q_scan)
    m22 = _build_signature_block(
        "M22",
        quadratic_slots=2,
        slot_kinds=("L", "L", "Q", "Q"),
        expected_count=20,
        total_degree=6,
        budget=budget,
    )
    b4 = _build_signature_block(
        "B4",
        quadratic_slots=4,
        slot_kinds=("Q", "Q", "Q", "Q"),
        expected_count=54,
        total_degree=8,
        budget=budget,
    )
    if int(m22["signature_count"]) + int(b4["signature_count"]) != MAX_SIGNATURES:
        raise ArithmeticError("combined signature count is not exactly 74")
    character_certificate = _character_certificate(budget)
    finite_checks = _finite_histogram_checks(q_scan, budget)
    budget.guard()

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_second_moment_reduction.v1",
        "status": "DRAFT_EXACT_PROOF_ROADMAP_NOT_SECOND_MOMENT_FORMULA",
        "scope": (
            "symbolic reduction for monic squarefree quintics over every odd prime "
            "power q; histogram checks only at q=3,5,7"
        ),
        "definition": (
            "For K_D=q*a_D^2-b_D^2 and Z_D=K_D/q^2, reduce sum_D K_D^2 "
            "to exact factor-signature character correlations without enumerating a field."
        ),
        "source_locks": source_locks,
        "master_reduction": {
            "formula": "sum_D K_D^2=q^2*A4(q)-2*q*M22(q)+B4(q)",
            "definitions": {
                "A4": "sum_D a_D^4",
                "M22": "sum_D a_D^2*b_D^2",
                "B4": "sum_D b_D^4",
            },
            "squarefree_sieve": (
                "S5(h)=C5(h)-(q-l)C3(h)+(binom(l+1,2)+k-q*l)C1(h)"
            ),
            "sieve_scope": (
                "all h supported on monic linear and irreducible-quadratic primes; "
                "only Moebius degrees 0,1,2 occur because deg D=5"
            ),
            "proven_A4": {
                "total": (
                    "q*(q-1)*(q+1)*(3*q^4-10*q^3+15*q^2-3*q-11)"
                ),
                "mean": "3*q^2-7*q+5+12/q-14/q^2-11/q^3",
                "status": "PROVED_BY_REWEIGHTING_THE_BOUND_QUARTIC_TABLE",
            },
            "unresolved_block": "B4(q)-2*q*M22(q)",
        },
        "signature_blocks": {"M22": m22, "B4": b4},
        "primitive_character_reduction": {
            "odd_radical": "r(h)=product of primes having odd exponent in h",
            "even_support": "E(h)=primes having positive even exponent in h",
            "deletion_formula": (
                "C_n(h)=[u^n]L_r(u)*product_(P in E)(1-(P/r)*u^deg(P))"
            ),
            "new_marked_primitive_coefficients": {
                "degree_4": ["p1(r)"],
                "degree_6": ["p1(r)", "p2(r)"],
                "degree_8": ["p1(r)", "p2(r)", "p3(r)"],
            },
            "coefficient_as_character_sum": (
                "p_m(r)=sum_(j=0)^m sum_(F monic,deg F=j) (F/r)"
            ),
            "remaining_lemma": (
                "Evaluate the six marked primitive-coefficient families, including their "
                "deletion-character products, across the frozen 20+54 signatures."
            ),
        },
        "character_certificate": character_certificate,
        "finite_histogram_checks": finite_checks,
        "candidate_shape_firewall": {
            "elementary_expectation": (
                "Principal, collision, and type-count terms are polynomial in q; "
                "linear-linear reciprocity can introduce eta_q=chi_q(-1)."
            ),
            "unproved_possibility": (
                "Surviving p_i averages may be genuine Frobenius-trace terms, so neither "
                "a polynomial nor an eta_q two-branch quasipolynomial is asserted."
            ),
            "three_field_limitation": (
                "q=3,7 have eta_q=-1 and q=5 is the only eta_q=+1 sample; the "
                "three checks cannot identify an all-q formula or a prime-power law."
            ),
        },
        "resource_contract": {
            "maximum_signatures": MAX_SIGNATURES,
            "actual_signatures": int(m22["signature_count"])
            + int(b4["signature_count"]),
            "maximum_partition_degree": MAX_PARTITION_DEGREE,
            "maximum_exact_operations": MAX_OPERATIONS,
            "exact_operations_used": budget.operations,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "clock": "time.monotonic",
            "field_enumeration": "FORBIDDEN_AND_NOT_IMPORTED",
            "histogram_bins_read": sum(
                int(row["histogram_bin_count"]) for row in finite_checks
            ),
        },
        "firewalls": [
            "This packet is an exact proof roadmap, not an all-q second-moment formula.",
            "The 20+54 signature enumeration is combinatorial and performs no finite-field or family enumeration.",
            "The q=3,5,7 histogram identities are checksums and are not interpolation data for a theorem.",
            "The exact USp(4) character decomposition does not prove finite-family equidistribution or convergence.",
            "The mixed a_D^2*b_D^2 and b_D^4 character correlations remain unevaluated.",
            "No polynomial, quasipolynomial, rate, sign law, number-field transfer, RH, or GRH conclusion is asserted.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        stored = json.loads(args.check.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"second-moment reduction fixture mismatch: {args.check}")
        print(f"OK: second-moment reduction fixture matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote second-moment reduction fixture {args.write}")
        return 0
    print(json.dumps(fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
