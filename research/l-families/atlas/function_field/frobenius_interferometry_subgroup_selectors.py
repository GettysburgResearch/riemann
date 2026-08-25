#!/usr/bin/env python3
"""Exact low-frequency Frobenius-interferometry subgroup selectors.

For the standard torus of USp(4), put

    p_r(x,y) = x^r + x^-r + y^r + y^-r
    I_(r,s)  = p_r*p_s - p_(r+s).

This bounded, standard-library-only producer compares exact Haar constant
terms on USp(4), the block SU(2)xSU(2) subgroup, the doubled-standard and
Sym^3 one-parameter SU(2) subgroups, and their relevant uniform tori.  It
proves a three-observable subgroup-selector matrix and exhausts the raw
interferometers with r+s <= 10.  It constructs no finite field, curve, zero,
or random sample.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Iterable, Mapping, Sequence


MAX_TOTAL_FREQUENCY = 10
MAX_ROOT_LADDER_BASE = 12
ACCOUNTED_WORK_CAP_EXCLUSIVE = 100_000

GROUP_ORDER = (
    "USp4",
    "SU2xSU2_block",
    "SU2_doubled_standard",
    "SU2_Sym3",
    "T2_uniform",
    "T_doubled_uniform",
    "T_Sym3_uniform",
)

Exponent = tuple[int, ...]
Laurent = dict[Exponent, int]
Signature = tuple[Fraction, ...]


def _require_plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


@dataclass
class ResourceGuard:
    """Small logical-work guard for the exact Laurent calculations."""

    cap: int = ACCOUNTED_WORK_CAP_EXCLUSIVE
    ledger: Counter[str] = field(default_factory=Counter)

    def __post_init__(self) -> None:
        self.cap = _require_plain_int("work cap", self.cap)
        if self.cap < 1:
            raise ValueError("work cap must be positive")

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: object = 1) -> None:
        if not isinstance(name, str) or not name:
            raise TypeError("resource name must be a nonempty string")
        amount = _require_plain_int("resource units", units)
        if amount < 0:
            raise ValueError("resource units must be nonnegative")
        if self.total + amount >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += amount


def _clean(polynomial: Mapping[Exponent, int]) -> Laurent:
    return {
        exponent: coefficient
        for exponent, coefficient in polynomial.items()
        if coefficient
    }


def laurent_multiply(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    guard: ResourceGuard,
) -> Laurent:
    if not left or not right:
        return {}
    dimensions = len(next(iter(left)))
    if any(len(exponent) != dimensions for exponent in left):
        raise ValueError("left Laurent polynomial has mixed dimensions")
    if any(len(exponent) != dimensions for exponent in right):
        raise ValueError("Laurent polynomial dimensions do not match")
    guard.charge("laurent_pair_products", len(left) * len(right))
    result: dict[Exponent, int] = defaultdict(int)
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(
                left_value + right_value
                for left_value, right_value in zip(left_exponent, right_exponent)
            )
            result[exponent] += left_coefficient * right_coefficient
    return _clean(result)


def laurent_linear_combination(
    terms: Iterable[tuple[object, Mapping[Exponent, int]]],
    guard: ResourceGuard,
) -> Laurent:
    result: dict[Exponent, int] = defaultdict(int)
    for raw_coefficient, polynomial in terms:
        coefficient = _require_plain_int("linear-combination coefficient", raw_coefficient)
        guard.charge("linear_combination_terms", len(polynomial))
        for exponent, value in polynomial.items():
            result[exponent] += coefficient * value
    return _clean(result)


def trace_power(power: object) -> Laurent:
    r = _require_plain_int("trace power", power)
    if r < 1:
        raise ValueError("trace power must be positive")
    return {
        (r, 0): 1,
        (-r, 0): 1,
        (0, r): 1,
        (0, -r): 1,
    }


def interferometer(left: object, right: object, guard: ResourceGuard) -> Laurent:
    r = _require_plain_int("left frequency", left)
    s = _require_plain_int("right frequency", right)
    if r < 1 or s < r:
        raise ValueError("interferometer frequencies must satisfy 1 <= r <= s")
    product = laurent_multiply(trace_power(r), trace_power(s), guard)
    return laurent_linear_combination(
        ((1, product), (-1, trace_power(r + s))), guard
    )


def weyl_density(
    positive_roots: Sequence[Exponent],
    rank: object,
    guard: ResourceGuard,
) -> Laurent:
    dimensions = _require_plain_int("rank", rank)
    if dimensions < 1:
        raise ValueError("rank must be positive")
    density: Laurent = {(0,) * dimensions: 1}
    for root in positive_roots:
        if len(root) != dimensions:
            raise ValueError("root dimension does not match rank")
        factor = {
            (0,) * dimensions: 2,
            root: -1,
            tuple(-coordinate for coordinate in root): -1,
        }
        density = laurent_multiply(density, factor, guard)
    return density


def weyl_integral(
    polynomial: Mapping[Exponent, int],
    density: Mapping[Exponent, int],
    weyl_order: object,
    guard: ResourceGuard,
) -> Fraction:
    order = _require_plain_int("Weyl-group order", weyl_order)
    if order < 1:
        raise ValueError("Weyl-group order must be positive")
    guard.charge("weyl_density_lookups", len(polynomial))
    numerator = sum(
        coefficient
        * density.get(tuple(-coordinate for coordinate in exponent), 0)
        for exponent, coefficient in polynomial.items()
    )
    return Fraction(numerator, order)


def substitute_one_parameter(
    polynomial: Mapping[Exponent, int],
    first_weight: object,
    second_weight: object,
    guard: ResourceGuard,
) -> Laurent:
    a = _require_plain_int("first one-parameter weight", first_weight)
    b = _require_plain_int("second one-parameter weight", second_weight)
    if a < 1 or b < 1:
        raise ValueError("one-parameter weights must be positive")
    result: dict[Exponent, int] = defaultdict(int)
    guard.charge("one_parameter_substitutions", len(polynomial))
    for exponent, coefficient in polynomial.items():
        if len(exponent) != 2:
            raise ValueError("one-parameter substitution expects rank two")
        result[(a * exponent[0] + b * exponent[1],)] += coefficient
    return _clean(result)


@dataclass
class HaarContext:
    guard: ResourceGuard
    c2_density: Laurent = field(init=False)
    a1xa1_density: Laurent = field(init=False)
    a1_density: Laurent = field(init=False)

    def __post_init__(self) -> None:
        self.c2_density = weyl_density(
            ((2, 0), (0, 2), (1, 1), (1, -1)), 2, self.guard
        )
        self.a1xa1_density = weyl_density(((2, 0), (0, 2)), 2, self.guard)
        self.a1_density = weyl_density(((2,),), 1, self.guard)
        if self.c2_density.get((0, 0)) != 8:
            raise ArithmeticError("C2 Weyl density normalization drifted")
        if self.a1xa1_density.get((0, 0)) != 4:
            raise ArithmeticError("A1xA1 Weyl density normalization drifted")
        if self.a1_density.get((0,)) != 2:
            raise ArithmeticError("A1 Weyl density normalization drifted")

    def signature(self, polynomial: Mapping[Exponent, int]) -> Signature:
        doubled = substitute_one_parameter(polynomial, 1, 1, self.guard)
        sym3 = substitute_one_parameter(polynomial, 3, 1, self.guard)
        return (
            weyl_integral(polynomial, self.c2_density, 8, self.guard),
            weyl_integral(polynomial, self.a1xa1_density, 4, self.guard),
            weyl_integral(doubled, self.a1_density, 2, self.guard),
            weyl_integral(sym3, self.a1_density, 2, self.guard),
            Fraction(polynomial.get((0, 0), 0)),
            Fraction(doubled.get((0,), 0)),
            Fraction(sym3.get((0,), 0)),
        )


def su2_trace_mean(frequency: object) -> int:
    """Integral of z^n+z^-n against normalized SU(2) Haar."""

    n = _require_plain_int("SU(2) trace frequency", frequency)
    if n < 1:
        raise ValueError("SU(2) trace frequency must be positive")
    return -1 if n == 2 else 0


def su2_trace_pair_mean(left: object, right: object) -> int:
    """Integral of (z^m+z^-m)(z^n+z^-n) against SU(2) Haar."""

    m = _require_plain_int("left SU(2) frequency", left)
    n = _require_plain_int("right SU(2) frequency", right)
    if m < 1 or n < 1:
        raise ValueError("SU(2) frequencies must be positive")
    return (
        2 * int(m == n)
        - int(m + n == 2)
        - int(abs(m - n) == 2)
    )


def su2_embedding_interferometer_mean(
    first_weight: object,
    second_weight: object,
    left: object,
    right: object,
) -> int:
    """Closed Haar formula for the formal SU(2) pullback +/-a,+/-b.

    Arbitrary positive ``a,b`` define an exact class-function pullback, but
    need not be the weights of a four-dimensional symplectic representation.
    The actual named embeddings used here are ``(1,1)`` and ``(3,1)``.
    """

    a = _require_plain_int("first embedding weight", first_weight)
    b = _require_plain_int("second embedding weight", second_weight)
    r = _require_plain_int("left interferometer frequency", left)
    s = _require_plain_int("right interferometer frequency", right)
    if min(a, b, r, s) < 1:
        raise ValueError("embedding weights and frequencies must be positive")
    return (
        su2_trace_pair_mean(a * r, a * s)
        + su2_trace_pair_mean(a * r, b * s)
        + su2_trace_pair_mean(b * r, a * s)
        + su2_trace_pair_mean(b * r, b * s)
        - su2_trace_mean(a * (r + s))
        - su2_trace_mean(b * (r + s))
    )


def product_interferometer_mean(left: object, right: object) -> int:
    """Closed Haar formula for independent block SU(2)xSU(2)."""

    r = _require_plain_int("left product frequency", left)
    s = _require_plain_int("right product frequency", right)
    if r < 1 or s < 1:
        raise ValueError("product frequencies must be positive")
    return (
        4 * int(r == s)
        - 2 * int(abs(r - s) == 2)
        + 2 * int(r == s == 2)
    )


def sym3_root_resonance_pair(base: object, branch: str) -> tuple[int, int]:
    """Return an all-frequency pure Sym3 root-resonance pair.

    The outer branch is (r,3r+2) for r>=2.  The inner branch is
    (r,3r-2) for r>=4.  At these thresholds the other six Haar means
    vanish, while the Sym3 mean of I_(r,s) is -1.
    """

    r = _require_plain_int("root-resonance base", base)
    if branch == "outer":
        if r < 2:
            raise ValueError("outer Sym3 root ladder requires base at least two")
        return r, 3 * r + 2
    if branch == "inner":
        if r < 4:
            raise ValueError("inner Sym3 root ladder requires base at least four")
        return r, 3 * r - 2
    raise ValueError("root-resonance branch must be 'outer' or 'inner'")


def trace_power_sequence_from_coefficients(
    first_elementary: Fraction | int,
    second_elementary: Fraction | int,
    maximum: object = MAX_TOTAL_FREQUENCY,
) -> tuple[Fraction, ...]:
    """Return p_0,...,p_max from a normalized reciprocal quartic.

    The quartic convention is

        Z^4-e1*Z^3+e2*Z^2-e1*Z+1.

    No eigenvalues or numerical roots are constructed.
    """

    cap = _require_plain_int("maximum trace frequency", maximum)
    if cap < 0 or cap > MAX_TOTAL_FREQUENCY:
        raise ValueError(
            f"maximum trace frequency must lie in 0..{MAX_TOTAL_FREQUENCY}"
        )
    e1 = Fraction(first_elementary)
    e2 = Fraction(second_elementary)
    values = [Fraction(4)]
    if cap >= 1:
        values.append(e1)
    if cap >= 2:
        values.append(e1 * e1 - 2 * e2)
    if cap >= 3:
        values.append(e1**3 - 3 * e1 * e2 + 3 * e1)
    for frequency in range(4, cap + 1):
        values.append(
            e1 * values[frequency - 1]
            - e2 * values[frequency - 2]
            + e1 * values[frequency - 3]
            - values[frequency - 4]
        )
    return tuple(values)


def selector_values_from_coefficients(
    first_elementary: Fraction | int,
    second_elementary: Fraction | int,
) -> dict[str, Fraction]:
    """Evaluate the three selectors from reciprocal coefficients alone."""

    powers = trace_power_sequence_from_coefficients(
        first_elementary, second_elementary
    )

    def value(left: int, right: int) -> Fraction:
        return powers[left] * powers[right] - powers[left + right]

    return {
        "product_selector": value(2, 2) - value(4, 4),
        "doubled_selector": -value(1, 1) + 2 * value(1, 5) + value(4, 4),
        "sym3_selector": -2 * value(2, 8),
    }


def selector_values_from_squared_first_elementary(
    first_elementary_squared: Fraction | int,
    second_elementary: Fraction | int,
) -> dict[str, Fraction]:
    """Evaluate the even selectors from ``A=e1^2`` and ``e=e2``.

    This form is useful for finite-field reciprocal quartics, where ``e1``
    may contain ``sqrt(q)`` but ``e1^2`` is rational.
    """

    first_square = Fraction(first_elementary_squared)
    second = Fraction(second_elementary)
    a = first_square
    e = second
    product = -2 * (
        2 * a**2
        - 4 * a * e**2
        + 8 * a * e
        - 6 * a
        + e**4
        - 5 * e**2
        + 4
    )
    doubled = 2 * (
        a**2 * e
        + a**2
        - 8 * a * e**2
        + 15 * a * e
        - 10 * a
        + e**4
        + 2 * e**3
        - 4 * e**2
        - 7 * e
        + 6
    )
    sym3_residual = (
        2 * a**3
        - a**2 * e**2
        - 8 * a**2 * e
        + 11 * a**2
        + 4 * a * e**3
        - 4 * a * e**2
        + 4 * a * e
        - 14 * a
        - e**4
        + 3 * e**2
        + 1
    )
    return {
        "product_selector": product,
        "doubled_selector": doubled,
        "sym3_selector": 2 * (a - 2 * e) * sym3_residual,
    }


EXPECTED_NONZERO_RAW_SIGNATURES: dict[tuple[int, int], tuple[int, ...]] = {
    (1, 1): (2, 4, 6, 2, 4, 8, 4),
    (1, 3): (1, -2, -4, 1, 0, 0, 2),
    (2, 2): (4, 6, 8, 4, 4, 8, 4),
    (1, 5): (-1, 0, 0, -1, 0, 0, 0),
    (2, 4): (0, -2, -4, -2, 0, 0, 0),
    (3, 3): (2, 4, 8, 4, 4, 8, 4),
    (2, 6): (-1, 0, 0, 2, 0, 0, 2),
    (3, 5): (-1, -2, -4, -1, 0, 0, 0),
    (4, 4): (4, 4, 8, 4, 4, 8, 4),
    (2, 8): (0, 0, 0, -1, 0, 0, 0),
    (3, 7): (-1, 0, 0, -1, 0, 0, 0),
    (4, 6): (-1, -2, -4, -1, 0, 0, 0),
    (5, 5): (4, 4, 8, 4, 4, 8, 4),
}

SELECTOR_EXPECTATIONS: dict[str, tuple[int, ...]] = {
    "product_selector": (0, 2, 0, 0, 0, 0, 0),
    "doubled_selector": (0, 0, 2, 0, 0, 0, 0),
    "sym3_selector": (0, 0, 0, 2, 0, 0, 0),
}

EXPECTED_AMBIENT_GRAM = (
    (24, -20, 4),
    (-20, 48, 0),
    (4, 0, 40),
)


def _raw_polynomials(
    context: HaarContext,
) -> dict[tuple[int, int], Laurent]:
    result = {}
    for total in range(2, MAX_TOTAL_FREQUENCY + 1):
        for left in range(1, total // 2 + 1):
            result[left, total - left] = interferometer(
                left, total - left, context.guard
            )
    return result


def selector_polynomials(
    raw: Mapping[tuple[int, int], Mapping[Exponent, int]],
    guard: ResourceGuard,
) -> dict[str, Laurent]:
    return {
        "product_selector": laurent_linear_combination(
            ((1, raw[2, 2]), (-1, raw[4, 4])), guard
        ),
        "doubled_selector": laurent_linear_combination(
            ((-1, raw[1, 1]), (2, raw[1, 5]), (1, raw[4, 4])), guard
        ),
        "sym3_selector": laurent_linear_combination(
            ((-2, raw[2, 8]),), guard
        ),
    }


def _rational_rank(columns: Sequence[Signature]) -> int:
    if not columns:
        return 0
    row_count = len(columns[0])
    if any(len(column) != row_count for column in columns):
        raise ValueError("rank columns have inconsistent dimensions")
    matrix = [
        [Fraction(column[row]) for column in columns]
        for row in range(row_count)
    ]
    rank = 0
    column_count = len(columns)
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(row_count):
            if row == rank or not matrix[row][column]:
                continue
            multiplier = matrix[row][column]
            matrix[row] = [
                left - multiplier * right
                for left, right in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def _target_in_span(columns: Sequence[Signature], target: Signature) -> bool:
    return _rational_rank(columns) == _rational_rank((*columns, target))


def minimal_signature_support(
    raw_signatures: Mapping[tuple[int, int], Signature],
    target: Signature,
    guard: ResourceGuard,
    maximum_support: object = 3,
) -> tuple[int, list[tuple[tuple[int, int], ...]]]:
    cap = _require_plain_int("maximum signature support", maximum_support)
    if cap < 1:
        raise ValueError("maximum signature support must be positive")
    candidates = [
        pair
        for pair in sorted(raw_signatures, key=lambda item: (sum(item), item))
        if sum(pair) % 2 == 0 and any(raw_signatures[pair])
    ]
    for support in range(1, cap + 1):
        witnesses = []
        for indices in itertools.combinations(candidates, support):
            # Two exact rank calculations are made: the candidate columns and
            # the same matrix augmented by the target.  Charge their complete
            # entry counts rather than pretending Python row operations are a
            # literal instruction count.
            guard.charge(
                "signature_span_matrix_entries",
                len(target) * (2 * support + 1),
            )
            if _target_in_span(
                tuple(raw_signatures[index] for index in indices), target
            ):
                witnesses.append(indices)
        if witnesses:
            return support, witnesses
    raise ArithmeticError("target signature was not found within the support cap")


def _integer_signature(signature: Signature) -> tuple[int, ...]:
    if any(value.denominator != 1 for value in signature):
        raise ArithmeticError("expected integral subgroup signature")
    return tuple(value.numerator for value in signature)


def build_packet() -> dict[str, object]:
    guard = ResourceGuard()
    context = HaarContext(guard)
    raw = _raw_polynomials(context)
    raw_signatures = {pair: context.signature(poly) for pair, poly in raw.items()}

    zero_signature = (0,) * len(GROUP_ORDER)
    for pair, signature in raw_signatures.items():
        expected = EXPECTED_NONZERO_RAW_SIGNATURES.get(pair, zero_signature)
        if _integer_signature(signature) != expected:
            raise ArithmeticError(
                f"raw interferometer signature drifted at {pair}: "
                f"{signature} != {expected}"
            )

    raw_contrasts = [
        pair
        for pair, signature in raw_signatures.items()
        if signature[0] == 0 and any(signature[index] for index in (1, 2, 3))
    ]
    if raw_contrasts != [(2, 4), (2, 8)]:
        raise ArithmeticError("bounded raw contrast classification drifted")

    for pair, signature in raw_signatures.items():
        left, right = pair
        if signature[1] != product_interferometer_mean(left, right):
            raise ArithmeticError(f"product closed formula drifted at {pair}")
        if signature[2] != su2_embedding_interferometer_mean(1, 1, left, right):
            raise ArithmeticError(f"doubled closed formula drifted at {pair}")
        if signature[3] != su2_embedding_interferometer_mean(3, 1, left, right):
            raise ArithmeticError(f"Sym3 closed formula drifted at {pair}")

    selectors = selector_polynomials(raw, guard)
    selector_signatures = {
        name: context.signature(polynomial)
        for name, polynomial in selectors.items()
    }
    for name, expected in SELECTOR_EXPECTATIONS.items():
        if _integer_signature(selector_signatures[name]) != expected:
            raise ArithmeticError(f"{name} signature drifted")

    selector_names = tuple(SELECTOR_EXPECTATIONS)
    ambient_gram = tuple(
        tuple(
            context.signature(
                laurent_multiply(selectors[left], selectors[right], guard)
            )[0]
            for right in selector_names
        )
        for left in selector_names
    )
    if tuple(tuple(_integer_signature(row)) for row in ambient_gram) != EXPECTED_AMBIENT_GRAM:
        raise ArithmeticError("ambient selector Gram matrix drifted")

    support_records = {}
    for name, expected in SELECTOR_EXPECTATIONS.items():
        target = tuple(Fraction(value) for value in expected)
        minimum, witnesses = minimal_signature_support(
            raw_signatures, target, guard
        )
        support_records[name] = {
            "minimum_rational_support": minimum,
            "witnesses": [list(map(list, witness)) for witness in witnesses],
        }
    expected_minima = {
        "product_selector": 2,
        "doubled_selector": 3,
        "sym3_selector": 1,
    }
    if {
        name: record["minimum_rational_support"]
        for name, record in support_records.items()
    } != expected_minima:
        raise ArithmeticError("selector support minima drifted")

    root_ladder_rows: dict[str, list[dict[str, object]]] = {}
    root_target = SELECTOR_EXPECTATIONS["sym3_selector"]
    for branch, first_base in (("outer", 2), ("inner", 4)):
        rows = []
        for base in range(first_base, MAX_ROOT_LADDER_BASE + 1):
            pair = sym3_root_resonance_pair(base, branch)
            raw_polynomial = interferometer(*pair, guard)
            raw_signature = context.signature(raw_polynomial)
            selector_signature = tuple(-2 * value for value in raw_signature)
            if _integer_signature(selector_signature) != root_target:
                raise ArithmeticError(
                    f"{branch} Sym3 root ladder drifted at base {base}"
                )
            if raw_signature[1] != product_interferometer_mean(*pair):
                raise ArithmeticError("root ladder product formula drifted")
            if raw_signature[2] != su2_embedding_interferometer_mean(
                1, 1, *pair
            ):
                raise ArithmeticError("root ladder doubled formula drifted")
            if raw_signature[3] != su2_embedding_interferometer_mean(
                3, 1, *pair
            ):
                raise ArithmeticError("root ladder Sym3 formula drifted")
            rows.append(
                {
                    "base": base,
                    "frequencies": list(pair),
                    "raw_signature": list(_integer_signature(raw_signature)),
                    "selector_signature": list(
                        _integer_signature(selector_signature)
                    ),
                }
            )
        root_ladder_rows[branch] = rows

    return {
        "schema": "riemann.function_field.frobenius_interferometry_subgroup_selectors.v2",
        "status": "EXACT_COMPACT_GROUP_THEOREMS_AND_BOUNDED_CLASSIFICATION",
        "normalization": {
            "p_r": "Tr(U^r) in the four-dimensional standard representation",
            "I_r_s": "p_r*p_s-p_(r+s)",
            "haar_measures": "normalized probability",
            "projection_scope": (
                "constant/trivial-isotypic coefficient only, not pointwise "
                "vanishing"
            ),
        },
        "group_order": list(GROUP_ORDER),
        "raw_cap": {
            "maximum_total_frequency": MAX_TOTAL_FREQUENCY,
            "complete_pair_count": len(raw),
            "nonzero_signatures": [
                {
                    "frequencies": list(pair),
                    "signature": list(_integer_signature(raw_signatures[pair])),
                }
                for pair in sorted(
                    EXPECTED_NONZERO_RAW_SIGNATURES,
                    key=lambda item: (sum(item), item),
                )
            ],
            "ambient_zero_nontrivial_subgroup_contrasts": [
                list(pair) for pair in raw_contrasts
            ],
        },
        "sym3_root_resonance_ladders": {
            "theorem": (
                "-2*I_(r,3r+2) for every r>=2 and -2*I_(r,3r-2) "
                "for every r>=4 both have signature (0,0,0,2,0,0,0)"
            ),
            "mechanism": (
                "the frequency gap |3r-s|=2 hits the A1 root; all ambient, "
                "product, doubled, and uniform-torus constant terms vanish "
                "at the stated thresholds"
            ),
            "bounded_replay_maximum_base": MAX_ROOT_LADDER_BASE,
            "bounded_replay": root_ladder_rows,
        },
        "selectors": {
            "definitions": {
                "product_selector": "I_(2,2)-I_(4,4)",
                "doubled_selector": "-I_(1,1)+2*I_(1,5)+I_(4,4)",
                "sym3_selector": "-2*I_(2,8)",
            },
            "signatures": {
                name: list(_integer_signature(selector_signatures[name]))
                for name in selector_names
            },
            "ambient_gram": [
                list(_integer_signature(row)) for row in ambient_gram
            ],
            "bounded_support_minimality": support_records,
            "coefficient_adapter": {
                "quartic": "Z^4-e1*Z^3+e2*Z^2-e1*Z+1",
                "method": "exact order-four recurrence through p_10; no roots",
                "rational_even_form": (
                    "all selectors are also exported as polynomials in "
                    "A=e1^2 and e2"
                ),
            },
        },
        "resource_contract": {
            "finite_field_enumeration": False,
            "root_finding": False,
            "random_sampling": False,
            "external_data": False,
            "accounted_work_cap_exclusive": guard.cap,
            "accounted_work": dict(sorted(guard.ledger.items())),
            "accounted_work_total": guard.total,
        },
        "firewall": (
            "These are exact compact-group Haar signatures. They neither prove "
            "arithmetic monodromy/equidistribution nor identify a motive, compatible "
            "system, zero law, RH, or GRH consequence."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--show",
        action="store_true",
        help="print the complete exact packet as JSON",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="run all exact checks and print a concise success line",
    )
    arguments = parser.parse_args()
    packet = build_packet()
    if arguments.show:
        print(json.dumps(packet, indent=2, sort_keys=True))
    else:
        print(
            "frobenius interferometry subgroup selectors: ok "
            f"raw={packet['raw_cap']['complete_pair_count']} "
            f"work={packet['resource_contract']['accounted_work_total']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
