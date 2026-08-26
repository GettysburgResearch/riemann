#!/usr/bin/env python3
"""Exact third-order primitive inventory for the genus-two B4 reduction.

For every odd prime power q, this producer reduces the conductor-type sums

    sum s1^3,  sum s1*s2,  sum s3

to eight explicitly named factorization-stratified genus-one trace moments.
It proves the affine-fibre multiplicities and consumes the source-locked
level-one cubic moment theorem only through degree eight.  It enumerates no
finite field, cubic, conductor, or genus-two family member.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import genus2_b3_primitive_trace_average as b3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_third_order_primitive_inventory.json"
NOTE_PATH = HERE / "GENUS2_THIRD_ORDER_PRIMITIVE_INVENTORY.md"
TEST_PATH = ROOT / "tests" / "test_genus2_third_order_primitive_inventory.py"

SECOND_MOMENT_FIXTURE_PATH = HERE / "genus2_second_moment_reduction.json"
B3_FIXTURE_PATH = HERE / "genus2_b3_primitive_trace_average.json"
B3_PRODUCER_PATH = HERE / "genus2_b3_primitive_trace_average.py"
B3_NOTE_PATH = HERE / "GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md"
GENUS1_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_PRODUCER_PATH = HERE / "genus1_cubic_family_laws.py"
GENUS1_NOTE_PATH = HERE / "GENUS1_CUBIC_FAMILY_LAWS.md"

EXPECTED_PAYLOAD_SHA256 = {
    "second_moment_fixture": (
        "55c5c9ef04a65ca46044ac1d76c76f33afc02b51c2d38a8ca196b99498ee16ec"
    ),
    "B3_fixture": ("e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd"),
    "genus1_fixture": (
        "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
    ),
}
EXPECTED_LF_SHA256 = {
    "second_moment_fixture": (
        "0966565c0b29d7bf85f6ad20f8c6634365a8fff674e3c3b06589125fe0bdbaf0"
    ),
    "B3_fixture": ("5ecc6006014a159a4030218977c89f58c63334461a568b7a67d36130bae1c50b"),
    "B3_producer": ("fd180499468a3672120fc1794109f12b4fb027530f881104181809ee5d6caa4c"),
    "B3_note": ("36e6aa856931e1171cea57243ea7e6a161c6ecd01833eb80b04e1ae57b296d83"),
    "genus1_fixture": (
        "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
    ),
    "genus1_producer": (
        "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79"
    ),
    "genus1_note": ("aad40573c6378c919ee6659bcd1c4b89a8981621c61feb0dcde9911d127c6b9f"),
}

MAX_SYMBOLIC_OPERATIONS_AND_ATOMS = 4096
MAX_WALL_SECONDS = 5.0
MAX_B4_SIGNATURES = 54

DEGREE_TYPES = {
    4: ((4, 0), (2, 1), (0, 2)),
    6: ((6, 0), (4, 1), (2, 2), (0, 3)),
    8: ((8, 0), (6, 1), (4, 2), (2, 3), (0, 4)),
}
ALL_TYPES = tuple(value for rows in DEGREE_TYPES.values() for value in rows)

RESIDUAL_KEYS = tuple(
    f"M_{factorization}_{degree}"
    for factorization in ("111", "12")
    for degree in (2, 4, 6, 8)
)

Bivariate = dict[tuple[int, int], Fraction]


@dataclass(frozen=True)
class ResidualExpression:
    """A q-polynomial plus q-polynomial coefficients of eight residuals."""

    constant: b3.Polynomial
    coefficients: Mapping[str, b3.Polynomial]


class _NestedPolynomialGuard:
    """Suppress coefficientwise ticks inside one residual-expression operation."""

    def __init__(self, parent: b3.AlgebraGuard) -> None:
        self.parent = parent

    def tick(self, amount: int = 1) -> None:
        del amount
        deadline = getattr(self.parent, "deadline", None)
        if deadline is not None and time.monotonic() > deadline:
            raise RuntimeError("exact symbolic wall-time cap exceeded")


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _load_locked_fixture(
    path: Path, expected_payload: str, expected_lf: str
) -> dict[str, object]:
    if _lf_normalized_sha256(path) != expected_lf:
        raise RuntimeError(f"source-locked file changed: {path}")
    fixture = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(fixture, dict):
        raise TypeError(f"expected object fixture at {path}")
    claimed = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload) or claimed != expected_payload:
        raise ValueError(f"source-locked payload mismatch at {path}")
    return fixture


def _verify_dependency_hashes() -> None:
    actual = {
        "second_moment_fixture": _lf_normalized_sha256(SECOND_MOMENT_FIXTURE_PATH),
        "B3_fixture": _lf_normalized_sha256(B3_FIXTURE_PATH),
        "B3_producer": _lf_normalized_sha256(B3_PRODUCER_PATH),
        "B3_note": _lf_normalized_sha256(B3_NOTE_PATH),
        "genus1_fixture": _lf_normalized_sha256(GENUS1_FIXTURE_PATH),
        "genus1_producer": _lf_normalized_sha256(GENUS1_PRODUCER_PATH),
        "genus1_note": _lf_normalized_sha256(GENUS1_NOTE_PATH),
    }
    if actual != EXPECTED_LF_SHA256:
        raise RuntimeError("a third-order source-locked dependency changed")


def _bi_clean(value: Mapping[tuple[int, int], Fraction | int]) -> Bivariate:
    return {
        key: Fraction(coefficient) for key, coefficient in value.items() if coefficient
    }


def _bi_constant(value: Fraction | int) -> Bivariate:
    return {} if not value else {(0, 0): Fraction(value)}


def _bi_monomial(
    q_degree: int, a_degree: int, coefficient: Fraction | int = 1
) -> Bivariate:
    return {} if not coefficient else {(q_degree, a_degree): Fraction(coefficient)}


def _bi_add(left: Bivariate, right: Bivariate, guard: b3.AlgebraGuard) -> Bivariate:
    guard.tick()
    result = dict(left)
    for key, coefficient in right.items():
        result[key] = result.get(key, Fraction(0)) + coefficient
    return _bi_clean(result)


def _bi_scale(
    value: Bivariate, scalar: Fraction | int, guard: b3.AlgebraGuard
) -> Bivariate:
    guard.tick()
    return _bi_clean({key: Fraction(scalar) * entry for key, entry in value.items()})


def _bi_multiply(
    left: Bivariate, right: Bivariate, guard: b3.AlgebraGuard
) -> Bivariate:
    guard.tick()
    result: dict[tuple[int, int], Fraction] = {}
    for (left_q, left_a), left_value in left.items():
        for (right_q, right_a), right_value in right.items():
            key = (left_q + right_q, left_a + right_a)
            result[key] = result.get(key, Fraction(0)) + left_value * right_value
    return _bi_clean(result)


def _bi_elementary(
    order: int,
    population: Bivariate,
    total_sign: Bivariate,
    guard: b3.AlgebraGuard,
) -> Bivariate:
    if order < 0 or order > 8:
        raise ValueError("bivariate elementary-sign order must lie in [0,8]")
    elementary = [_bi_constant(1)]
    for degree in range(1, order + 1):
        numerator: Bivariate = {}
        for power in range(1, degree + 1):
            power_sum = total_sign if power % 2 else population
            term = _bi_multiply(elementary[degree - power], power_sum, guard)
            numerator = _bi_add(
                numerator,
                _bi_scale(term, 1 if power % 2 else -1, guard),
                guard,
            )
        elementary.append(_bi_scale(numerator, Fraction(1, degree), guard))
    return elementary[order]


def _bi_elementary_table(
    maximum_order: int,
    population: Bivariate,
    total_sign: Bivariate,
    guard: b3.AlgebraGuard,
) -> list[Bivariate]:
    if maximum_order < 0 or maximum_order > 8:
        raise ValueError("bivariate elementary-sign maximum must lie in [0,8]")
    elementary = [_bi_constant(1)]
    for degree in range(1, maximum_order + 1):
        numerator: Bivariate = {}
        for power in range(1, degree + 1):
            power_sum = total_sign if power % 2 else population
            term = _bi_multiply(elementary[degree - power], power_sum, guard)
            numerator = _bi_add(
                numerator,
                _bi_scale(term, 1 if power % 2 else -1, guard),
                guard,
            )
        elementary.append(_bi_scale(numerator, Fraction(1, degree), guard))
    return elementary


def _elementary_table(
    maximum_order: int,
    population: b3.Polynomial,
    total_sign: b3.Polynomial,
    guard: b3.AlgebraGuard,
) -> list[b3.Polynomial]:
    if maximum_order < 0 or maximum_order > 8:
        raise ValueError("elementary-sign maximum must lie in [0,8]")
    elementary = [b3.ONE]
    for degree in range(1, maximum_order + 1):
        numerator = b3.ZERO
        for power in range(1, degree + 1):
            power_sum = total_sign if power % 2 else population
            term = b3._multiply(elementary[degree - power], power_sum, guard)
            numerator = b3._add(
                numerator,
                b3._scale(term, 1 if power % 2 else -1, guard),
                guard,
            )
        elementary.append(b3._scale(numerator, Fraction(1, degree), guard))
    return elementary


def _choose_table(
    maximum_order: int, population: b3.Polynomial, guard: b3.AlgebraGuard
) -> list[b3.Polynomial]:
    if maximum_order < 0 or maximum_order > 8:
        raise ValueError("binomial maximum must lie in [0,8]")
    values = [b3.ONE]
    for order in range(1, maximum_order + 1):
        values.append(
            b3._scale(
                b3._multiply(
                    values[-1],
                    b3._shift_constant(population, -(order - 1), guard),
                    guard,
                ),
                Fraction(1, order),
                guard,
            )
        )
    return values


def _expr(constant: b3.Polynomial = b3.ZERO) -> ResidualExpression:
    return ResidualExpression(constant, {})


def _expr_add(
    left: ResidualExpression,
    right: ResidualExpression,
    guard: b3.AlgebraGuard,
) -> ResidualExpression:
    guard.tick()
    nested = _NestedPolynomialGuard(guard)
    coefficients: dict[str, b3.Polynomial] = {}
    for key in set(left.coefficients) | set(right.coefficients):
        value = b3._add(
            left.coefficients.get(key, b3.ZERO),
            right.coefficients.get(key, b3.ZERO),
            nested,
        )
        if value != b3.ZERO:
            coefficients[key] = value
    return ResidualExpression(
        b3._add(left.constant, right.constant, nested), coefficients
    )


def _expr_scale_fraction(
    value: ResidualExpression,
    scalar: Fraction | int,
    guard: b3.AlgebraGuard,
) -> ResidualExpression:
    guard.tick()
    nested = _NestedPolynomialGuard(guard)
    return ResidualExpression(
        b3._scale(value.constant, scalar, nested),
        {
            key: b3._scale(coefficient, scalar, nested)
            for key, coefficient in value.coefficients.items()
        },
    )


def _expr_multiply_polynomial(
    value: ResidualExpression,
    polynomial: b3.Polynomial,
    guard: b3.AlgebraGuard,
) -> ResidualExpression:
    guard.tick()
    nested = _NestedPolynomialGuard(guard)
    return ResidualExpression(
        b3._multiply(value.constant, polynomial, nested),
        {
            key: b3._multiply(coefficient, polynomial, nested)
            for key, coefficient in value.coefficients.items()
        },
    )


def _expr_linear_combination(
    terms: Sequence[tuple[Fraction | int, ResidualExpression]],
    guard: b3.AlgebraGuard,
) -> ResidualExpression:
    result = _expr()
    for scalar, value in terms:
        result = _expr_add(result, _expr_scale_fraction(value, scalar, guard), guard)
    return result


def _serialize_expression(value: ResidualExpression) -> dict[str, object]:
    return {
        "constant_low_to_high": b3._polynomial_pairs(value.constant),
        "level2_residual_coefficients": {
            key: b3._polynomial_pairs(value.coefficients[key])
            for key in RESIDUAL_KEYS
            if key in value.coefficients
        },
    }


def _stack_moment_polynomials(guard: b3.AlgebraGuard) -> dict[int, b3.Polynomial]:
    rows = {
        0: (0, 1),
        2: (-1, 0, 1),
        4: (-1, -3, 0, 2),
        6: (-1, -5, -9, 0, 5),
        8: (-1, -7, -20, -28, 0, 14),
    }
    return {degree: b3._clean(values) for degree, values in rows.items()}


def _full_model_moments(guard: b3.AlgebraGuard) -> dict[int, b3.Polynomial]:
    factor = b3._multiply(b3.Q, b3._shift_constant(b3.Q, -1, guard), guard)
    return {
        degree: b3._multiply(factor, value, guard)
        for degree, value in _stack_moment_polynomials(guard).items()
    }


def _stratum_counts(guard: b3.AlgebraGuard) -> dict[str, b3.Polynomial]:
    i_value = b3._scale(
        b3._multiply(b3.Q, b3._shift_constant(b3.Q, -1, guard), guard),
        Fraction(1, 2),
        guard,
    )
    return {
        "111": b3._choose(b3.Q, 3, guard),
        "12": b3._multiply(b3.Q, i_value, guard),
        "3": b3._scale(
            b3._subtract(b3._power(b3.Q, 3, guard), b3.Q, guard),
            Fraction(1, 3),
            guard,
        ),
    }


def _inventory_polynomials(
    rational_roots: int,
    quadratic_factors: int,
    guard: b3.AlgebraGuard,
) -> dict[tuple[int, int], Bivariate]:
    q_value = _bi_monomial(1, 0)
    a_value = _bi_monomial(0, 1)
    a_squared = _bi_monomial(0, 2)
    q_squared = _bi_monomial(2, 0)
    i_value = _bi_scale(
        _bi_add(q_squared, _bi_scale(q_value, -1, guard), guard), Fraction(1, 2), guard
    )
    linear_population = _bi_add(q_value, _bi_constant(-rational_roots), guard)
    linear_total = _bi_scale(a_value, -1, guard)
    quadratic_population = _bi_add(i_value, _bi_constant(-quadratic_factors), guard)
    quadratic_total = _bi_scale(
        _bi_add(
            _bi_add(q_value, _bi_constant(rational_roots), guard),
            _bi_scale(a_squared, -1, guard),
            guard,
        ),
        Fraction(1, 2),
        guard,
    )
    linear_orders = sorted({linear for linear, _ in ALL_TYPES})
    quadratic_orders = sorted({quadratic for _, quadratic in ALL_TYPES})
    linear_table = _bi_elementary_table(
        max(linear_orders), linear_population, linear_total, guard
    )
    quadratic_table = _bi_elementary_table(
        max(quadratic_orders), quadratic_population, quadratic_total, guard
    )
    linear_inventory = {order: linear_table[order] for order in linear_orders}
    quadratic_inventory = {order: quadratic_table[order] for order in quadratic_orders}
    return {
        factor_type: _bi_multiply(
            linear_inventory[factor_type[0]],
            quadratic_inventory[factor_type[1]],
            guard,
        )
        for factor_type in ALL_TYPES
    }


def _trace_sum_expression(
    value: Bivariate,
    stratum: str,
    counts: Mapping[str, b3.Polynomial],
    full_moments: Mapping[int, b3.Polynomial],
    guard: b3.AlgebraGuard,
) -> ResidualExpression:
    if stratum not in ("111", "12", "3"):
        raise ValueError("unknown cubic factorization stratum")
    result = _expr()
    for (q_degree, a_degree), coefficient in value.items():
        if a_degree % 2:
            continue
        if a_degree > 8:
            raise ArithmeticError("trace inventory exceeded degree eight")
        q_monomial = b3._clean([Fraction(0)] * q_degree + [coefficient])
        if a_degree == 0:
            result = _expr_add(
                result,
                _expr(b3._multiply(q_monomial, counts[stratum], guard)),
                guard,
            )
            continue
        if stratum == "3":
            result = _expr_add(
                result,
                _expr(b3._multiply(q_monomial, full_moments[a_degree], guard)),
                guard,
            )
            for other in ("111", "12"):
                key = f"M_{other}_{a_degree}"
                result = _expr_add(
                    result,
                    ResidualExpression(
                        b3.ZERO,
                        {key: b3._scale(q_monomial, -1, guard)},
                    ),
                    guard,
                )
        else:
            key = f"M_{stratum}_{a_degree}"
            result = _expr_add(
                result,
                ResidualExpression(b3.ZERO, {key: q_monomial}),
                guard,
            )
    return result


def _lower_primitive_tables(
    guard: b3.AlgebraGuard,
) -> tuple[
    dict[tuple[int, int], dict[str, b3.Polynomial]],
    dict[tuple[int, int], b3.Polynomial],
]:
    q_minus_one = b3._shift_constant(b3.Q, -1, guard)
    q_minus_two = b3._shift_constant(b3.Q, -2, guard)
    i_value = b3._scale(b3._multiply(b3.Q, q_minus_one, guard), Fraction(1, 2), guard)
    minus_n = b3._scale(q_minus_one, Fraction(-1, 2), guard)
    i_minus_one = b3._shift_constant(i_value, -1, guard)
    minus_n_plus_one = b3._scale(
        b3._shift_constant(b3.Q, 1, guard), Fraction(-1, 2), guard
    )
    linear_orders = sorted({linear for linear, _ in ALL_TYPES})
    quadratic_orders = sorted({quadratic for _, quadratic in ALL_TYPES})
    maximum_linear = max(linear_orders)
    maximum_quadratic = max(quadratic_orders)

    choose_q = _choose_table(maximum_linear, b3.Q, guard)
    choose_q_minus_one = _choose_table(maximum_linear, q_minus_one, guard)
    choose_i = _choose_table(maximum_quadratic, i_value, guard)
    e_linear_one = _elementary_table(maximum_linear, q_minus_one, b3.ZERO, guard)
    e_linear_two_minus = _elementary_table(
        maximum_linear, q_minus_two, b3._constant(-1), guard
    )
    e_linear_two_plus = _elementary_table(
        maximum_linear, q_minus_two, b3._constant(1), guard
    )
    e_linear_q_minus = _elementary_table(maximum_linear, b3.Q, b3._constant(-1), guard)
    e_quadratic = _elementary_table(maximum_quadratic, i_value, minus_n, guard)
    e_quadratic_nonrational = _elementary_table(
        maximum_quadratic, i_minus_one, minus_n_plus_one, guard
    )

    primitive: dict[tuple[int, int], dict[str, b3.Polynomial]] = {}
    collisions: dict[tuple[int, int], b3.Polynomial] = {}
    for linear_count, quadratic_count in ALL_TYPES:
        count = b3._multiply(choose_q[linear_count], choose_i[quadratic_count], guard)
        sum_s1 = b3._product(
            (
                b3.Q,
                e_linear_one[linear_count],
                e_quadratic[quadratic_count],
            ),
            guard,
        )
        diagonal = b3._product(
            (
                b3.Q,
                choose_q_minus_one[linear_count],
                choose_i[quadratic_count],
            ),
            guard,
        )
        off_diagonal = b3._product(
            (
                b3.Q,
                q_minus_one,
                e_linear_two_minus[linear_count],
                e_quadratic[quadratic_count],
            ),
            guard,
        )
        sum_s1_squared = b3._add(diagonal, off_diagonal, guard)
        nonrational = b3._product(
            (
                b3._scale(i_value, 2, guard),
                e_linear_q_minus[linear_count],
                e_quadratic_nonrational[quadratic_count],
            ),
            guard,
        )
        sum_s2 = b3._add(diagonal, nonrational, guard)
        sum_p1 = b3._add(count, sum_s1, guard)
        sum_p2 = b3._add(
            sum_p1,
            b3._scale(
                b3._add(sum_s1_squared, sum_s2, guard),
                Fraction(1, 2),
                guard,
            ),
            guard,
        )
        primitive[(linear_count, quadratic_count)] = {
            "count": count,
            "sum_s1": sum_s1,
            "sum_s1_squared": sum_s1_squared,
            "sum_s2": sum_s2,
            "sum_p1": sum_p1,
            "sum_p2": sum_p2,
        }
        linear_even_part = b3._add(
            e_linear_two_minus[linear_count],
            e_linear_two_plus[linear_count],
            guard,
        )
        collisions[(linear_count, quadratic_count)] = b3._scale(
            b3._product(
                (
                    b3.Q,
                    q_minus_one,
                    linear_even_part,
                    e_quadratic[quadratic_count],
                ),
                guard,
            ),
            Fraction(3, 2),
            guard,
        )
    return primitive, collisions


def _primitive_third_order_rows(
    guard: b3.AlgebraGuard,
) -> tuple[list[dict[str, object]], dict[tuple[int, int], dict[str, object]]]:
    counts = _stratum_counts(guard)
    full_moments = _full_model_moments(guard)
    lower_tables, collision_tables = _lower_primitive_tables(guard)
    if (
        b3._add(b3._add(counts["111"], counts["12"], guard), counts["3"], guard)
        != full_moments[0]
    ):
        raise ArithmeticError("cubic factorization strata do not exhaust H_3(q)")

    strata = {"111": (3, 0), "12": (1, 1), "3": (0, 0)}
    trace_inventories: dict[tuple[str, int, int], ResidualExpression] = {}
    for stratum, (rational_roots, quadratic_factors) in strata.items():
        inventories = _inventory_polynomials(rational_roots, quadratic_factors, guard)
        for linear_count, quadratic_count in ALL_TYPES:
            inventory = inventories[(linear_count, quadratic_count)]
            trace_inventories[(stratum, linear_count, quadratic_count)] = (
                _trace_sum_expression(inventory, stratum, counts, full_moments, guard)
            )

    rows: list[dict[str, object]] = []
    raw: dict[tuple[int, int], dict[str, object]] = {}
    for degree, types in DEGREE_TYPES.items():
        for linear_count, quadratic_count in types:
            lower = lower_tables[(linear_count, quadratic_count)]
            equal_and_two = b3._add(
                lower["sum_s1"],
                collision_tables[(linear_count, quadratic_count)],
                guard,
            )
            sum_s1_cubed = _expr_add(
                _expr(equal_and_two),
                _expr_scale_fraction(
                    trace_inventories[("111", linear_count, quadratic_count)],
                    6,
                    guard,
                ),
                guard,
            )
            q_minus_l = b3._shift_constant(b3.Q, -linear_count, guard)
            sum_s1_s2 = _expr_add(
                _expr(b3._multiply(q_minus_l, lower["sum_s1"], guard)),
                _expr_scale_fraction(
                    trace_inventories[("12", linear_count, quadratic_count)],
                    2,
                    guard,
                ),
                guard,
            )
            sum_s3 = _expr_add(
                _expr(lower["sum_s1"]),
                _expr_scale_fraction(
                    trace_inventories[("3", linear_count, quadratic_count)],
                    3,
                    guard,
                ),
                guard,
            )
            cubic_coefficient = _expr_linear_combination(
                (
                    (Fraction(1, 6), sum_s1_cubed),
                    (Fraction(1, 2), sum_s1_s2),
                    (Fraction(1, 3), sum_s3),
                ),
                guard,
            )
            sum_p3 = _expr_add(_expr(lower["sum_p2"]), cubic_coefficient, guard)
            raw[(linear_count, quadratic_count)] = {
                "lower": lower,
                "sum_s1_cubed": sum_s1_cubed,
                "sum_s1_s2": sum_s1_s2,
                "sum_s3": sum_s3,
                "sum_p3": sum_p3,
            }
            rows.append(
                {
                    "conductor_degree": degree,
                    "linear_prime_count": linear_count,
                    "quadratic_prime_count": quadratic_count,
                    "count_low_to_high": b3._polynomial_pairs(lower["count"]),
                    "sum_s1_low_to_high": b3._polynomial_pairs(lower["sum_s1"]),
                    "sum_s1_squared_low_to_high": b3._polynomial_pairs(
                        lower["sum_s1_squared"]
                    ),
                    "sum_s2_low_to_high": b3._polynomial_pairs(lower["sum_s2"]),
                    "sum_p1_low_to_high": b3._polynomial_pairs(lower["sum_p1"]),
                    "sum_p2_low_to_high": b3._polynomial_pairs(lower["sum_p2"]),
                    "sum_s1_cubed": _serialize_expression(sum_s1_cubed),
                    "sum_s1_s2": _serialize_expression(sum_s1_s2),
                    "sum_s3": _serialize_expression(sum_s3),
                    "sum_p3": _serialize_expression(sum_p3),
                }
            )
    return rows, raw


def _marked_deletion_rows(
    raw: Mapping[tuple[int, int], Mapping[str, object]],
    guard: b3.AlgebraGuard,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    def add_row(
        degree: int,
        factor_type: tuple[int, int],
        kind: str,
        choice_count: b3.Polynomial,
        c1: ResidualExpression,
        c3: ResidualExpression,
        c5: ResidualExpression,
    ) -> None:
        rows.append(
            {
                "conductor_degree": degree,
                "linear_prime_count": factor_type[0],
                "quadratic_prime_count": factor_type[1],
                "deletion_kind": kind,
                "external_choices_per_conductor_low_to_high": (
                    b3._polynomial_pairs(choice_count)
                ),
                "sum_C1": _serialize_expression(c1),
                "sum_C3": _serialize_expression(c3),
                "sum_C5": _serialize_expression(c5),
            }
        )

    for factor_type in DEGREE_TYPES[6]:
        linear_count, _ = factor_type
        data = raw[factor_type]
        lower = data["lower"]
        if not isinstance(lower, dict):
            raise TypeError("lower primitive inventory is malformed")
        external = b3._shift_constant(b3.Q, -linear_count, guard)
        c1 = _expr(
            b3._multiply(
                b3._shift_constant(external, -1, guard),
                lower["sum_s1"],
                guard,
            )
        )
        base_c3 = b3._subtract(
            b3._multiply(b3.Q, lower["sum_p1"], guard),
            lower["sum_p2"],
            guard,
        )
        c3 = _expr_add(
            _expr(b3._multiply(external, base_c3, guard)),
            _expr_scale_fraction(
                _expr_add(data["sum_s1_cubed"], data["sum_s1_s2"], guard),
                Fraction(-1, 2),
                guard,
            ),
            guard,
        )
        p1s1 = b3._add(lower["sum_s1"], lower["sum_s1_squared"], guard)
        c5 = _expr(
            b3._add(
                b3._scale(
                    b3._product(
                        (
                            b3._power(b3.Q, 2, guard),
                            external,
                            lower["count"],
                        ),
                        guard,
                    ),
                    -1,
                    guard,
                ),
                b3._add(
                    b3._scale(
                        b3._multiply(
                            b3._power(b3.Q, 2, guard),
                            lower["sum_s1"],
                            guard,
                        ),
                        -1,
                        guard,
                    ),
                    b3._multiply(b3.Q, p1s1, guard),
                    guard,
                ),
                guard,
            )
        )
        add_row(6, factor_type, "one_external_linear", external, c1, c3, c5)

    i_value = b3._scale(
        b3._multiply(b3.Q, b3._shift_constant(b3.Q, -1, guard), guard),
        Fraction(1, 2),
        guard,
    )
    for factor_type in DEGREE_TYPES[4]:
        linear_count, quadratic_count = factor_type
        data = raw[factor_type]
        lower = data["lower"]
        if not isinstance(lower, dict):
            raise TypeError("lower primitive inventory is malformed")
        external_linear = b3._shift_constant(b3.Q, -linear_count, guard)

        one_linear_c1 = _expr(
            b3._multiply(
                b3._shift_constant(external_linear, -1, guard),
                lower["sum_s1"],
                guard,
            )
        )
        one_linear_c3 = _expr(
            b3._add(
                b3._scale(
                    b3._product((b3.Q, external_linear, lower["count"]), guard),
                    -1,
                    guard,
                ),
                b3._add(
                    b3._multiply(
                        b3._shift_constant(b3._scale(b3.Q, -1, guard), 1, guard),
                        lower["sum_s1"],
                        guard,
                    ),
                    lower["sum_s1_squared"],
                    guard,
                ),
                guard,
            )
        )
        add_row(
            4,
            factor_type,
            "one_external_linear",
            external_linear,
            one_linear_c1,
            one_linear_c3,
            _expr(),
        )

        external_quadratic = b3._shift_constant(i_value, -quadratic_count, guard)
        one_quadratic_c1 = _expr(
            b3._multiply(external_quadratic, lower["sum_s1"], guard)
        )
        epsilon_s1 = _expr_scale_fraction(
            _expr_add(
                data["sum_s1_s2"],
                _expr(
                    b3._scale(
                        b3._multiply(external_linear, lower["sum_s1"], guard),
                        -1,
                        guard,
                    )
                ),
                guard,
            ),
            Fraction(1, 2),
            guard,
        )
        one_quadratic_c3 = _expr_add(
            _expr(
                b3._scale(
                    b3._product((b3.Q, external_quadratic, lower["count"]), guard),
                    -1,
                    guard,
                )
            ),
            _expr_scale_fraction(epsilon_s1, -1, guard),
            guard,
        )
        epsilon_sum = b3._scale(
            b3._subtract(
                lower["sum_s2"],
                b3._multiply(external_linear, lower["count"], guard),
                guard,
            ),
            Fraction(1, 2),
            guard,
        )
        one_quadratic_c5 = _expr(b3._multiply(b3.Q, epsilon_sum, guard))
        add_row(
            4,
            factor_type,
            "one_external_quadratic",
            external_quadratic,
            one_quadratic_c1,
            one_quadratic_c3,
            one_quadratic_c5,
        )

        pair_choices = b3._choose(external_linear, 2, guard)
        pair_c1 = _expr(
            b3._scale(
                b3._product(
                    (
                        b3._shift_constant(external_linear, -1, guard),
                        b3._shift_constant(external_linear, -2, guard),
                        lower["sum_s1"],
                    ),
                    guard,
                ),
                Fraction(1, 2),
                guard,
            )
        )
        pair_c3_constant = b3._scale(
            b3._product((b3.Q, pair_choices, lower["count"]), guard),
            -1,
            guard,
        )
        pair_c3_constant = b3._add(
            pair_c3_constant,
            b3._scale(
                b3._product(
                    (
                        b3._shift_constant(external_linear, -1, guard),
                        b3._shift_constant(b3.Q, -1, guard),
                        lower["sum_s1"],
                    ),
                    guard,
                ),
                -1,
                guard,
            ),
            guard,
        )
        pair_c3_constant = b3._add(
            pair_c3_constant,
            b3._multiply(
                b3._shift_constant(external_linear, -1, guard),
                lower["sum_s1_squared"],
                guard,
            ),
            guard,
        )
        pair_c3 = _expr_add(
            _expr(pair_c3_constant),
            _expr_scale_fraction(
                _expr_add(
                    data["sum_s1_cubed"],
                    _expr(
                        b3._scale(
                            b3._multiply(external_linear, lower["sum_s1"], guard),
                            -1,
                            guard,
                        )
                    ),
                    guard,
                ),
                Fraction(1, 2),
                guard,
            ),
            guard,
        )
        pair_c5 = _expr(
            b3._scale(
                b3._multiply(
                    b3.Q,
                    b3._subtract(
                        lower["sum_s1_squared"],
                        b3._multiply(external_linear, lower["count"], guard),
                        guard,
                    ),
                    guard,
                ),
                Fraction(-1, 2),
                guard,
            )
        )
        add_row(
            4,
            factor_type,
            "two_external_linears",
            pair_choices,
            pair_c1,
            pair_c3,
            pair_c5,
        )
    return rows


def _evaluate_polynomial(value: b3.Polynomial, q_value: int) -> Fraction:
    return sum(
        coefficient * q_value**degree for degree, coefficient in enumerate(value)
    )


def _rank_certificate(
    raw: Mapping[tuple[int, int], Mapping[str, object]], q_value: int = 17
) -> dict[str, object]:
    selected = (
        ("sum_s1_cubed", (4, 0)),
        ("sum_s1_cubed", (0, 2)),
        ("sum_s1_cubed", (0, 3)),
        ("sum_s1_cubed", (0, 4)),
        ("sum_s1_s2", (4, 0)),
        ("sum_s1_s2", (0, 2)),
        ("sum_s1_s2", (0, 3)),
        ("sum_s1_s2", (0, 4)),
    )
    matrix: list[list[Fraction]] = []
    for moment_name, factor_type in selected:
        expression = raw[factor_type][moment_name]
        if not isinstance(expression, ResidualExpression):
            raise TypeError("rank-certificate expression is malformed")
        matrix.append(
            [
                _evaluate_polynomial(expression.coefficients.get(key, b3.ZERO), q_value)
                for key in RESIDUAL_KEYS
            ]
        )

    determinant = Fraction(1)
    for column in range(len(matrix)):
        pivot = next(
            (row for row in range(column, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            determinant = Fraction(0)
            break
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant *= -1
        pivot_value = matrix[column][column]
        determinant *= pivot_value
        for entry in range(column, len(matrix)):
            matrix[column][entry] /= pivot_value
        for row in range(column + 1, len(matrix)):
            scalar = matrix[row][column]
            if not scalar:
                continue
            for entry in range(column, len(matrix)):
                matrix[row][entry] -= scalar * matrix[column][entry]
    if not determinant:
        raise ArithmeticError("the selected residual coefficient minor vanished")
    return {
        "residual_count": len(RESIDUAL_KEYS),
        "rank_over_Q(q)": len(RESIDUAL_KEYS),
        "certificate_method": (
            "an 8x8 polynomial minor is nonzero because its exact q=17 "
            "specialization has the recorded nonzero determinant"
        ),
        "formal_specialization_q": q_value,
        "determinant_numerator": determinant.numerator,
        "determinant_denominator": determinant.denominator,
        "selected_rows": [
            {
                "moment": moment,
                "linear_prime_count": factor_type[0],
                "quadratic_prime_count": factor_type[1],
            }
            for moment, factor_type in selected
        ],
        "interpretation": (
            "under only the four source-locked level-one total-moment "
            "relations, all eight factorization-stratified residuals are needed"
        ),
    }


def _b4_structure_audit(fixture: Mapping[str, object]) -> dict[str, object]:
    blocks = fixture.get("signature_blocks")
    if not isinstance(blocks, dict):
        raise TypeError("second-moment fixture lost signature blocks")
    block = blocks.get("B4")
    if not isinstance(block, dict):
        raise TypeError("second-moment fixture lost B4 block")
    rows = block.get("signatures")
    if not isinstance(rows, list) or len(rows) != MAX_B4_SIGNATURES:
        raise ValueError("B4 source is not the frozen 54-signature ledger")
    census: Counter[tuple[int, int, int]] = Counter()
    primitive_types: set[tuple[int, int, int]] = set()
    for row in rows:
        if not isinstance(row, dict):
            raise TypeError("a B4 signature row is not an object")
        radical = row.get("odd_radical")
        even = row.get("even_exponent_support")
        if not isinstance(radical, dict) or not isinstance(even, dict):
            raise TypeError("a B4 row lost radical/deletion data")
        degree = int(radical["degree"])
        linear_even = int(even["linear_prime_count"])
        quadratic_even = int(even["quadratic_prime_count"])
        census[(degree, linear_even, quadratic_even)] += 1
        if degree in DEGREE_TYPES:
            primitive_types.add(
                (
                    degree,
                    int(radical["linear_prime_count"]),
                    int(radical["quadratic_prime_count"]),
                )
            )
    expected_types = {
        (degree, linear, quadratic)
        for degree, types in DEGREE_TYPES.items()
        for linear, quadratic in types
    }
    if primitive_types != expected_types:
        raise ArithmeticError("B4 primitive conductor-type support changed")
    return {
        "signature_count": len(rows),
        "primitive_conductor_types": [
            {
                "degree": degree,
                "linear_prime_count": linear,
                "quadratic_prime_count": quadratic,
            }
            for degree, linear, quadratic in sorted(primitive_types)
        ],
        "radical_degree_and_deletion_support_census": [
            {
                "radical_degree": key[0],
                "external_linear_count": key[1],
                "external_quadratic_count": key[2],
                "signature_count": count,
            }
            for key, count in sorted(census.items())
        ],
        "packet_A_interface": (
            "degree 8 uses p1,p2,p3; degree 6 plus one external linear "
            "uses s1^3+s1*s2; degree 4 plus one external quadratic uses "
            "s1*s2; degree 4 plus two external linears uses s1^3"
        ),
    }


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        SECOND_MOMENT_FIXTURE_PATH,
        B3_FIXTURE_PATH,
        B3_PRODUCER_PATH,
        B3_NOTE_PATH,
        GENUS1_FIXTURE_PATH,
        GENUS1_PRODUCER_PATH,
        GENUS1_NOTE_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    return [
        {
            "path": path.resolve().relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_normalized_sha256(path),
        }
        for path in paths
    ]


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    _verify_dependency_hashes()
    second = _load_locked_fixture(
        SECOND_MOMENT_FIXTURE_PATH,
        EXPECTED_PAYLOAD_SHA256["second_moment_fixture"],
        EXPECTED_LF_SHA256["second_moment_fixture"],
    )
    _load_locked_fixture(
        B3_FIXTURE_PATH,
        EXPECTED_PAYLOAD_SHA256["B3_fixture"],
        EXPECTED_LF_SHA256["B3_fixture"],
    )
    genus1 = _load_locked_fixture(
        GENUS1_FIXTURE_PATH,
        EXPECTED_PAYLOAD_SHA256["genus1_fixture"],
        EXPECTED_LF_SHA256["genus1_fixture"],
    )
    explicit = genus1["all_q_moment_theorem"]["explicit_stack_sums"]
    expected_explicit = {
        "W_0": "q",
        "W_2": "q^2-1",
        "W_4": "2*q^3-3*q-1",
        "W_6": "5*q^4-9*q^2-5*q-1",
        "W_8": "14*q^5-28*q^3-20*q^2-7*q-1",
    }
    if {key: explicit[key] for key in expected_explicit} != expected_explicit:
        raise ArithmeticError("source-locked genus-one moments through W8 changed")

    guard = b3.AlgebraGuard(started + MAX_WALL_SECONDS)
    primitive_rows, raw = _primitive_third_order_rows(guard)
    deletion_rows = _marked_deletion_rows(raw, guard)
    rank = _rank_certificate(raw)
    b4_audit = _b4_structure_audit(second)

    input_atoms = (
        len(ALL_TYPES) + len(deletion_rows) + len(RESIDUAL_KEYS) + MAX_B4_SIGNATURES
    )
    actual = guard.operations + input_atoms
    if actual > MAX_SYMBOLIC_OPERATIONS_AND_ATOMS:
        raise RuntimeError("third-order operation/input-atom cap exceeded")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("third-order proof replay exceeded its wall-time cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_third_order_primitive_inventory.v1",
        "status": "REDUCED_EXACTLY_TO_EIGHT_LEVEL2_MOMENT_CHANNELS",
        "scope": {
            "q": "every odd prime power",
            "conductor_types": (
                "squarefree products of l monic linears and k monic "
                "irreducible quadratics, for l+2*k in {4,6,8}"
            ),
            "finite_fields_enumerated": 0,
            "cubics_enumerated": 0,
            "conductors_enumerated": 0,
            "genus_two_family_members_consumed": 0,
            "sampled_q_values_used_as_theorem_input": 0,
            "numeric_approximations": 0,
        },
        "exact_reduction_theorem": {
            "primitive_rows": primitive_rows,
            "newton_bridge": ("sum p3=sum p2+(sum s1^3+3*sum s1*s2+2*sum s3)/6"),
            "factorization_strata": {
                "111": {
                    "count": "binom(q,3)",
                    "fibre_multiplicity_in_s1^3": 6,
                    "inventory": ("E_l(q-3,-eta*a_f)*E_k(I,(q+3-a_f^2)/2)"),
                },
                "12": {
                    "count": "q^2*(q-1)/2",
                    "fibre_multiplicity_in_s1*s2": 2,
                    "inventory": ("E_l(q-1,-eta*a_f)*E_k(I-1,(q+1-a_f^2)/2)"),
                },
                "3": {
                    "count": "(q^3-q)/3",
                    "fibre_multiplicity_in_s3": 3,
                    "inventory": ("E_l(q,-eta*a_f)*E_k(I,(q-a_f^2)/2)"),
                },
                "eta": "quadratic_character_Fq(-1)",
                "odd_trace_moments": (
                    "zero separately in each stratum by a nonsquare affine multiplier"
                ),
            },
            "level_one_relation": (
                "M_111_(2j)+M_12_(2j)+M_3_(2j)=q*(q-1)*W_(2j), for j=0,1,2,3,4"
            ),
            "source_locked_W_rows": expected_explicit,
            "unresolved_level2_residuals": list(RESIDUAL_KEYS),
            "rank_minimality_certificate": rank,
        },
        "marked_deletion_interface": deletion_rows,
        "B4_source_structure_audit": b4_audit,
        "downstream_cancellation_boundary": {
            "attribution": (
                "the parallel B4 reweight packet supplied the generic degree-8 "
                "weights (2520,360,72,24,24); this packet does not consume its result"
            ),
            "generic_degree8_weights_by_type": [
                {"linear_prime_count": 8, "quadratic_prime_count": 0, "weight": 2520},
                {"linear_prime_count": 6, "quadratic_prime_count": 1, "weight": 360},
                {"linear_prime_count": 4, "quadratic_prime_count": 2, "weight": 72},
                {"linear_prime_count": 2, "quadratic_prime_count": 3, "weight": 24},
                {"linear_prime_count": 0, "quadratic_prime_count": 4, "weight": 24},
            ],
            "firewall": (
                "Packet A leaves all eight level-2 channels explicit; only the "
                "source-locked 54-row Packet B may certify their weighted cancellation"
            ),
        },
        "source_manifest": _source_manifest(),
        "resource_contract": {
            "maximum_symbolic_operations_and_input_atoms": (
                MAX_SYMBOLIC_OPERATIONS_AND_ATOMS
            ),
            "actual_complete_polynomial_operations": guard.operations,
            "actual_input_atoms": input_atoms,
            "actual_operations_and_input_atoms": actual,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact Fraction coefficients; no floats",
            "rank_certificate_arithmetic": "exact Fraction Gaussian elimination",
        },
        "firewalls": [
            "The level-one cubic moment theorem does not determine a factorization stratum separately.",
            "No W2-through-W8 value is substituted for a Gamma(2) or rational-2-torsion moment.",
            "The formal q=17 rank specialization is a nonzero-minor certificate, not a sampled finite-field theorem input.",
            "Empty small-field conductor types remain literal zeros through binomial and elementary-symmetric polynomials.",
            "No polynomial interpolation, novelty, memberwise sign, RH, or GRH claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    fixture = build_fixture()
    if args.write:
        OUTPUT_PATH.write_text(
            json.dumps(
                fixture,
                allow_nan=False,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote {OUTPUT_PATH}")
        return 0
    if args.check:
        stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"third-order fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: third-order primitive fixture matches {OUTPUT_PATH}")
        return 0
    print(
        json.dumps(
            fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
