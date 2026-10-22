#!/usr/bin/env python3
"""Tiny exact symbolic certificate for squarefree-quintic moment identities.

This module does not enumerate finite fields or polynomial families.  It works
in ``Q[q]`` with degree at most twelve, encodes the three quadratic types for
the first moment of ``b_D`` and the nine factorization types of a product of
two monic quadratics, and reweights the five linear-only quartic types for the
exact fourth moment of the trace coefficient.  It checks the identities proved
in ``GENUS2_MOMENT_IDENTITY.md``.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from math import comb


HARD_DEGREE_LIMIT = 12
HARD_OPERATION_LIMIT = 10_000
HARD_ROW_LIMIT = 9
HARD_QUADRATIC_ROW_LIMIT = 3
HARD_SERIES_LIMIT = 5


class ResourceLimitError(RuntimeError):
    """Raised before a symbolic resource limit can be exceeded."""


def _normalize(coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    values = list(coefficients)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    if len(values) - 1 > HARD_DEGREE_LIMIT:
        raise ResourceLimitError(
            f"polynomial degree exceeds hard limit {HARD_DEGREE_LIMIT}"
        )
    return tuple(values) if values else (Fraction(0),)


@dataclass(frozen=True)
class Polynomial:
    """An exact polynomial in q, with coefficients ordered low to high."""

    coefficients: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        normalized = _normalize(tuple(Fraction(value) for value in self.coefficients))
        if normalized != self.coefficients:
            object.__setattr__(self, "coefficients", normalized)

    @property
    def degree(self) -> int:
        return len(self.coefficients) - 1

    def evaluate(self, q: int) -> Fraction:
        value = Fraction(0)
        for coefficient in reversed(self.coefficients):
            value = value * q + coefficient
        return value


def polynomial(*coefficients: int | Fraction) -> Polynomial:
    return Polynomial(tuple(Fraction(value) for value in coefficients))


class ExactAlgebra:
    """Budgeted arithmetic in Q[q]; no operation count depends on q."""

    def __init__(self, operation_limit: int = HARD_OPERATION_LIMIT) -> None:
        if operation_limit < 1:
            raise ValueError("operation_limit must be positive")
        if operation_limit > HARD_OPERATION_LIMIT:
            raise ResourceLimitError(
                f"operation limit exceeds hard cap {HARD_OPERATION_LIMIT}"
            )
        self.operation_limit = operation_limit
        self.operations = 0

    def _spend(self, amount: int) -> None:
        self.operations += amount
        if self.operations > self.operation_limit:
            raise ResourceLimitError(
                f"symbolic operation budget {self.operation_limit} exceeded"
            )

    def add(self, left: Polynomial, right: Polynomial) -> Polynomial:
        size = max(len(left.coefficients), len(right.coefficients))
        self._spend(size)
        values = [Fraction(0)] * size
        for index in range(size):
            if index < len(left.coefficients):
                values[index] += left.coefficients[index]
            if index < len(right.coefficients):
                values[index] += right.coefficients[index]
        return Polynomial(tuple(values))

    def negate(self, value: Polynomial) -> Polynomial:
        self._spend(len(value.coefficients))
        return Polynomial(tuple(-coefficient for coefficient in value.coefficients))

    def subtract(self, left: Polynomial, right: Polynomial) -> Polynomial:
        return self.add(left, self.negate(right))

    def scale(self, value: Polynomial, scalar: int | Fraction) -> Polynomial:
        self._spend(len(value.coefficients))
        factor = Fraction(scalar)
        return Polynomial(tuple(factor * coefficient for coefficient in value.coefficients))

    def multiply(self, left: Polynomial, right: Polynomial) -> Polynomial:
        if left.degree + right.degree > HARD_DEGREE_LIMIT:
            raise ResourceLimitError(
                f"product degree exceeds hard limit {HARD_DEGREE_LIMIT}"
            )
        self._spend(len(left.coefficients) * len(right.coefficients))
        values = [Fraction(0)] * (len(left.coefficients) + len(right.coefficients) - 1)
        for left_index, left_value in enumerate(left.coefficients):
            for right_index, right_value in enumerate(right.coefficients):
                values[left_index + right_index] += left_value * right_value
        return Polynomial(tuple(values))

    def product(self, *values: Polynomial) -> Polynomial:
        result = polynomial(1)
        for value in values:
            result = self.multiply(result, value)
        return result

    def power(self, value: Polynomial, exponent: int) -> Polynomial:
        if exponent < 0 or exponent > HARD_DEGREE_LIMIT:
            raise ResourceLimitError("refusing an exponent outside the hard degree limit")
        result = polynomial(1)
        for _ in range(exponent):
            result = self.multiply(result, value)
        return result

    def sum(self, values: tuple[Polynomial, ...]) -> Polynomial:
        result = polynomial(0)
        for value in values:
            result = self.add(result, value)
        return result


@dataclass(frozen=True)
class QuarticType:
    """One factorization type for h=fg with f,g monic quadratics.

    ``c3_each`` is C_3(h) for every h in the type.  ``c1_total`` is
    the aggregate sum of C_1(h) over the whole type, not a per-h value.
    """

    label: str
    count: Polynomial
    weight: int
    linear_support: int
    quadratic_support: int
    c3_each: Polynomial
    c1_total: Polynomial
    c5_each: Polynomial
    correction: Polynomial = Polynomial((Fraction(0),))


@dataclass(frozen=True)
class QuadraticType:
    """One factorization type for the monic quadratic f in sum_D b_D.

    Unlike ``QuarticType.c1_total``, all three character coefficients here
    are per polynomial ``f``.  ``sieve_value`` reconstructs
    ``sum_{D in H_5} (D/f)`` and ``contribution`` multiplies it by the number
    of polynomials of this type.
    """

    label: str
    count: Polynomial
    linear_support: int
    quadratic_support: int
    c1_each: Polynomial
    c3_each: Polynomial
    c5_each: Polynomial
    sieve_value: Polynomial = Polynomial((Fraction(0),))
    contribution: Polynomial = Polynomial((Fraction(0),))


@dataclass(frozen=True)
class MomentCertificate:
    rows: tuple[QuarticType, ...]
    quadratic_rows: tuple[QuadraticType, ...]
    squarefree_count: Polynomial
    a_diagonal_coefficient: Polynomial
    a_off_diagonal_coefficient: Polynomial
    sum_a_squared: Polynomial
    a_fourth_t0: Polynomial
    a_fourth_delta: Polynomial
    sum_a_fourth: Polynomial
    a_squared_b_t0: Polynomial
    a_squared_b_delta: Polynomial
    sum_a_squared_b: Polynomial
    sum_b: Polynomial
    t0: Polynomial
    delta: Polynomial
    sum_b_squared: Polynomial
    sum_k: Polynomial
    operations_used: int

    def totals_at(self, q: int) -> dict[str, int | Fraction]:
        """Specialize formally at odd q; family semantics require a prime power."""

        if q < 3 or q % 2 == 0:
            raise ValueError("the theorem and certificate require an odd q >= 3")

        def exact_integer(value: Polynomial) -> int:
            evaluated = value.evaluate(q)
            if evaluated.denominator != 1:
                raise ArithmeticError("certified total did not specialize to an integer")
            return evaluated.numerator

        members = exact_integer(self.squarefree_count)
        sum_a_squared = exact_integer(self.sum_a_squared)
        sum_a_fourth = exact_integer(self.sum_a_fourth)
        sum_a_squared_b = exact_integer(self.sum_a_squared_b)
        sum_b = exact_integer(self.sum_b)
        sum_b_squared = exact_integer(self.sum_b_squared)
        sum_k = exact_integer(self.sum_k)
        return {
            "member_count": members,
            "sum_a_squared": sum_a_squared,
            "sum_a_fourth": sum_a_fourth,
            "sum_a_squared_b": sum_a_squared_b,
            "sum_b": sum_b,
            "sum_b_squared": sum_b_squared,
            "sum_K": sum_k,
            "mean_a_squared": Fraction(sum_a_squared, members),
            "mean_a_fourth": Fraction(sum_a_fourth, members),
            "mean_a_squared_b": Fraction(sum_a_squared_b, members),
            "mean_b": Fraction(sum_b, members),
            "mean_b_squared": Fraction(sum_b_squared, members),
            "mean_K": Fraction(sum_k, members),
        }


@dataclass(frozen=True)
class SignDensityCertificate:
    """Exact algebra behind the negative-sign proportion corollary."""

    mean_deficit_numerator: Polynomial
    shifted_positive_polynomial: Polynomial
    range_lower_bound: int
    proportion_denominator: int

    def lower_bound_at(self, q: int) -> Fraction:
        """Specialize formally at odd q; family semantics require a prime power."""

        if q < 3 or q % 2 == 0:
            raise ValueError(
                "formal density-bound specialization requires an odd q >= 3; "
                "family semantics require an odd prime power"
            )
        numerator = self.mean_deficit_numerator.evaluate(q)
        if numerator.denominator != 1 or numerator <= 0:
            raise ArithmeticError("negative-sign density numerator is not a positive integer")
        return numerator / (self.proportion_denominator * q**5)


def _translate(value: Polynomial, shift: int) -> Polynomial:
    """Return value(q+shift), exactly and within the fixed degree limit."""

    coefficients = [Fraction(0)] * (value.degree + 1)
    for degree, coefficient in enumerate(value.coefficients):
        for power in range(degree + 1):
            coefficients[power] += (
                coefficient * comb(degree, power) * Fraction(shift ** (degree - power))
            )
    return Polynomial(tuple(coefficients))


def build_sign_density_certificate(
    moment_certificate: MomentCertificate | None = None,
) -> SignDensityCertificate:
    """Certify P(q)>0 for q>=3 and the resulting 1/20 density floor."""

    if moment_certificate is None:
        moment_certificate = build_certificate()
    numerator = polynomial(-1, -1, 0, 1, -2, 1)
    shifted = polynomial(104, 215, 171, 67, 13, 1)
    bridge_algebra = ExactAlgebra(operation_limit=100)
    moment_deficit_total = bridge_algebra.negate(moment_certificate.sum_k)
    density_deficit_total = bridge_algebra.multiply(
        polynomial(0, -1, 1), numerator
    )
    if moment_deficit_total != density_deficit_total:
        raise ArithmeticError(
            "density numerator is not tied to the certified identity "
            "-sum_D K_D=q*(q-1)*P(q)"
        )
    if _translate(shifted, -3) != numerator:
        raise ArithmeticError("shifted positivity identity failed")
    if any(coefficient <= 0 for coefficient in shifted.coefficients):
        raise ArithmeticError("shifted positivity polynomial lost a positive coefficient")
    return SignDensityCertificate(
        mean_deficit_numerator=numerator,
        shifted_positive_polynomial=shifted,
        range_lower_bound=-20,
        proportion_denominator=20,
    )


def _coefficient_of_product(
    algebra: ExactAlgebra,
    left: tuple[Polynomial, ...],
    right: tuple[Polynomial, ...],
    degree: int,
) -> Polynomial:
    if degree < 0 or degree > HARD_SERIES_LIMIT:
        raise ResourceLimitError(
            f"formal-series degree exceeds hard limit {HARD_SERIES_LIMIT}"
        )
    return algebra.sum(
        tuple(
            algebra.multiply(left[index], right[degree - index])
            for index in range(degree + 1)
        )
    )


def _a2_euler_product_coefficients(
    algebra: ExactAlgebra, q: Polynomial
) -> tuple[Polynomial, Polynomial]:
    """Return the u^5 coefficients for the diagonal and off-diagonal sums."""

    q_powers = tuple(algebra.power(q, exponent) for exponent in range(6))
    alternating = tuple(polynomial(1 if exponent % 2 == 0 else -1) for exponent in range(6))
    inverse_one_minus_u2_squared = tuple(
        polynomial(exponent // 2 + 1 if exponent % 2 == 0 else 0)
        for exponent in range(6)
    )

    # [u^5] (1-q*u^2) / ((1-q*u)(1+u)).
    base_degree_5 = _coefficient_of_product(algebra, q_powers, alternating, 5)
    base_degree_3 = _coefficient_of_product(algebra, q_powers, alternating, 3)
    diagonal = algebra.subtract(base_degree_5, algebra.multiply(q, base_degree_3))

    # [u^5] (1-u)(1-q*u^2)/(1-u^2)^2.
    numerator = (
        polynomial(1),
        polynomial(-1),
        algebra.negate(q),
        q,
        polynomial(0),
        polynomial(0),
    )
    off_diagonal = _coefficient_of_product(
        algebra, numerator, inverse_one_minus_u2_squared, 5
    )
    return diagonal, off_diagonal


def _row_correction(
    algebra: ExactAlgebra, q: Polynomial, row: QuarticType
) -> Polynomial:
    q_minus_l = algebra.subtract(q, polynomial(row.linear_support))
    c3_total = algebra.product(row.count, row.c3_each)
    first = algebra.negate(algebra.product(q_minus_l, c3_total))
    moebius_degree_two = algebra.subtract(
        polynomial(
            row.linear_support * (row.linear_support + 1) // 2
            + row.quadratic_support
        ),
        algebra.scale(q, row.linear_support),
    )
    second = algebra.multiply(moebius_degree_two, row.c1_total)
    return algebra.scale(algebra.add(first, second), row.weight)


def _quadratic_sieve_value(
    algebra: ExactAlgebra, q: Polynomial, row: QuadraticType
) -> Polynomial:
    """Return C5-(q-l)C3+(binom(l+1,2)+k-ql)C1 for one f."""

    q_minus_l = algebra.subtract(q, polynomial(row.linear_support))
    c3_correction = algebra.negate(
        algebra.multiply(q_minus_l, row.c3_each)
    )
    moebius_degree_two = algebra.subtract(
        polynomial(
            row.linear_support * (row.linear_support + 1) // 2
            + row.quadratic_support
        ),
        algebra.scale(q, row.linear_support),
    )
    c1_correction = algebra.multiply(moebius_degree_two, row.c1_each)
    return algebra.sum((row.c5_each, c3_correction, c1_correction))


def _a_fourth_from_quartic_rows(
    algebra: ExactAlgebra, q: Polynomial, rows: tuple[QuarticType, ...]
) -> tuple[Polynomial, Polynomial, Polynomial]:
    """Reuse the linear-only quartic rows for sum_D a_D^4.

    The original row weight counts ordered factorizations h=f*g by monic
    quadratics.  For a_D^4, the relevant weight instead counts ordered
    quadruples of monic linears with the displayed multiplicity pattern.
    """

    ordered_linear_weights = {
        "L^4": 1,
        "L^3 M": 4,
        "L^2 M^2": 6,
        "L M N^2": 12,
        "L M N R": 24,
    }
    selected = tuple(row for row in rows if row.label in ordered_linear_weights)
    if {row.label for row in selected} != set(ordered_linear_weights):
        raise ArithmeticError("a^4 certificate lost a linear quartic factorization type")
    principal = algebra.sum(
        tuple(
            algebra.scale(
                algebra.multiply(row.count, row.c5_each),
                ordered_linear_weights[row.label],
            )
            for row in selected
        )
    )
    correction = algebra.sum(
        tuple(
            _row_correction(
                algebra,
                q,
                replace(row, weight=ordered_linear_weights[row.label]),
            )
            for row in selected
        )
    )
    return principal, correction, algebra.add(principal, correction)


def _a_squared_b_from_quartic_rows(
    algebra: ExactAlgebra, q: Polynomial, rows: tuple[QuarticType, ...]
) -> tuple[Polynomial, Polynomial, Polynomial]:
    """Reuse the quartic rows for sum_D a_D^2*b_D.

    The weight counts two ordered linear slots and one monic-quadratic slot.
    The two purely quadratic quartic types cannot occur.
    """

    tuple_weights = {
        "L^4": 1,
        "L^2 M^2": 4,
        "L^3 M": 3,
        "Q L^2": 1,
        "L M N^2": 7,
        "Q L M": 2,
        "L M N R": 12,
    }
    selected = tuple(row for row in rows if row.label in tuple_weights)
    if {row.label for row in selected} != set(tuple_weights):
        raise ArithmeticError("a^2*b certificate lost a quartic factorization type")
    principal = algebra.sum(
        tuple(
            algebra.scale(
                algebra.multiply(row.count, row.c5_each),
                tuple_weights[row.label],
            )
            for row in selected
        )
    )
    correction = algebra.sum(
        tuple(
            _row_correction(
                algebra,
                q,
                replace(row, weight=tuple_weights[row.label]),
            )
            for row in selected
        )
    )
    return principal, correction, algebra.add(principal, correction)


def build_certificate(
    *, operation_limit: int = HARD_OPERATION_LIMIT
) -> MomentCertificate:
    """Construct and internally verify the exact polynomial certificate."""

    algebra = ExactAlgebra(operation_limit)
    q = polynomial(0, 1)
    one = polynomial(1)
    q_minus_1 = algebra.subtract(q, one)
    q_minus_2 = algebra.subtract(q, polynomial(2))
    q_minus_3 = algebra.subtract(q, polynomial(3))
    q2 = algebra.power(q, 2)
    q3 = algebra.power(q, 3)
    q4 = algebra.power(q, 4)
    q5 = algebra.power(q, 5)
    irreducible_quadratics = algebra.scale(algebra.product(q, q_minus_1), Fraction(1, 2))
    choose_q_2 = irreducible_quadratics
    choose_i_2 = algebra.scale(
        algebra.product(
            irreducible_quadratics,
            algebra.subtract(irreducible_quadratics, one),
        ),
        Fraction(1, 2),
    )
    choose_q_4 = algebra.scale(
        algebra.product(q, q_minus_1, q_minus_2, q_minus_3),
        Fraction(1, 24),
    )

    zero = polynomial(0)
    quadratic_rows = (
        QuadraticType(
            "L^2",
            q,
            1,
            0,
            q_minus_1,
            algebra.product(q2, q_minus_1),
            algebra.product(q4, q_minus_1),
        ),
        QuadraticType(
            "L M",
            choose_q_2,
            2,
            0,
            polynomial(-1),
            zero,
            zero,
        ),
        QuadraticType(
            "Q",
            irreducible_quadratics,
            0,
            1,
            polynomial(-1),
            zero,
            zero,
        ),
    )
    if len(quadratic_rows) != HARD_QUADRATIC_ROW_LIMIT:
        raise ResourceLimitError(
            "b first-moment certificate must have exactly "
            f"{HARD_QUADRATIC_ROW_LIMIT} rows"
        )
    quadratic_rows = tuple(
        replace(row, sieve_value=_quadratic_sieve_value(algebra, q, row))
        for row in quadratic_rows
    )
    quadratic_rows = tuple(
        replace(
            row,
            contribution=algebra.multiply(row.count, row.sieve_value),
        )
        for row in quadratic_rows
    )
    sum_b = algebra.sum(tuple(row.contribution for row in quadratic_rows))

    rows = (
        QuarticType(
            "L^4",
            q,
            1,
            1,
            0,
            algebra.product(q2, q_minus_1),
            algebra.product(q, q_minus_1),
            algebra.product(q4, q_minus_1),
        ),
        QuarticType(
            "L^2 M^2",
            choose_q_2,
            3,
            2,
            0,
            algebra.product(q, algebra.power(q_minus_1, 2)),
            algebra.product(choose_q_2, q_minus_2),
            algebra.product(q3, algebra.power(q_minus_1, 2)),
        ),
        QuarticType(
            "Q^2",
            irreducible_quadratics,
            1,
            0,
            1,
            algebra.subtract(q3, q),
            algebra.product(irreducible_quadratics, q),
            algebra.product(q3, algebra.subtract(q2, one)),
        ),
        QuarticType(
            "L^3 M",
            algebra.product(q, q_minus_1),
            2,
            2,
            0,
            zero,
            algebra.negate(algebra.product(q, q_minus_1)),
            zero,
        ),
        QuarticType(
            "Q L^2",
            algebra.product(q, irreducible_quadratics),
            2,
            1,
            1,
            zero,
            algebra.scale(
                algebra.negate(algebra.product(q, algebra.power(q_minus_1, 2))),
                Fraction(1, 2),
            ),
            zero,
        ),
        QuarticType(
            "L M N^2",
            algebra.product(choose_q_2, q_minus_2),
            4,
            3,
            0,
            zero,
            algebra.scale(
                algebra.negate(algebra.product(q, q_minus_1, q_minus_3)),
                Fraction(1, 2),
            ),
            zero,
        ),
        QuarticType(
            "Q_1 Q_2",
            choose_i_2,
            2,
            0,
            2,
            algebra.negate(q),
            algebra.scale(
                algebra.negate(algebra.product(q, algebra.subtract(q2, one))),
                Fraction(1, 8),
            ),
            zero,
        ),
        QuarticType(
            "Q L M",
            algebra.product(irreducible_quadratics, choose_q_2),
            2,
            2,
            1,
            algebra.negate(q),
            algebra.scale(
                algebra.product(q, algebra.power(q_minus_1, 2)), Fraction(1, 4)
            ),
            zero,
        ),
        QuarticType(
            "L M N R",
            choose_q_4,
            6,
            4,
            0,
            algebra.negate(q),
            algebra.scale(
                algebra.product(q, q_minus_1, q_minus_3), Fraction(1, 8)
            ),
            zero,
        ),
    )
    if len(rows) != HARD_ROW_LIMIT:
        raise ResourceLimitError(f"certificate must have exactly {HARD_ROW_LIMIT} rows")
    rows = tuple(
        replace(row, correction=_row_correction(algebra, q, row)) for row in rows
    )

    t0 = algebra.sum(
        tuple(
            algebra.scale(algebra.product(row.count, row.c5_each), row.weight)
            for row in rows
        )
    )
    delta = algebra.sum(tuple(row.correction for row in rows))
    sum_b_squared = algebra.add(t0, delta)
    a_fourth_t0, a_fourth_delta, sum_a_fourth = _a_fourth_from_quartic_rows(
        algebra, q, rows
    )
    a_squared_b_t0, a_squared_b_delta, sum_a_squared_b = (
        _a_squared_b_from_quartic_rows(algebra, q, rows)
    )

    diagonal, off_diagonal = _a2_euler_product_coefficients(algebra, q)
    sum_a_squared = algebra.add(
        algebra.multiply(q, diagonal),
        algebra.product(q, q_minus_1, off_diagonal),
    )
    squarefree_count = algebra.product(q4, q_minus_1)
    sum_k = algebra.subtract(algebra.multiply(q, sum_a_squared), sum_b_squared)

    expected_diagonal = algebra.sum(
        (
            q5,
            algebra.scale(q4, -2),
            algebra.scale(q3, 2),
            algebra.scale(q2, -2),
            algebra.scale(q, 2),
            polynomial(-1),
        )
    )
    expected_off_diagonal = algebra.subtract(algebra.scale(q, 2), polynomial(3))
    expected_t0 = algebra.product(
        q4,
        q_minus_1,
        algebra.add(
            algebra.add(algebra.scale(q2, 2), algebra.scale(q, -2)), one
        ),
    )
    expected_delta = algebra.negate(
        algebra.product(
            q,
            q_minus_1,
            algebra.sum(
                (
                    q4,
                    algebra.negate(q3),
                    algebra.negate(q2),
                    algebra.scale(q, 3),
                    one,
                )
            ),
        )
    )
    expected_sum_a_squared = algebra.add(
        algebra.product(q4, algebra.power(q_minus_1, 2)),
        algebra.product(
            q,
            q_minus_1,
            algebra.add(algebra.add(q2, q), polynomial(-2)),
        ),
    )
    expected_a_fourth_t0 = polynomial(0, 0, 0, 0, -3, 8, -8, 3)
    expected_a_fourth_delta = polynomial(0, 11, 3, -26, 10, 4, -2)
    expected_sum_a_fourth = polynomial(0, 11, 3, -26, 7, 12, -10, 3)
    expected_a_squared_b_t0 = polynomial(0, 0, 0, 0, -2, 5, -5, 2)
    expected_a_squared_b_delta = polynomial(0, 3, 4, -12, 4, 2, -1)
    expected_sum_a_squared_b = polynomial(0, 3, 4, -12, 2, 7, -6, 2)
    expected_sum_b = algebra.product(
        q,
        q_minus_1,
        algebra.sum((q4, algebra.negate(q3), q2, polynomial(-1))),
    )
    expected_sum_b_squared = algebra.add(
        algebra.product(
            q4,
            q_minus_1,
            algebra.add(
                algebra.add(algebra.scale(q2, 2), algebra.scale(q, -3)),
                polynomial(2),
            ),
        ),
        algebra.product(
            q,
            q_minus_1,
            algebra.add(
                algebra.add(q2, algebra.scale(q, -3)), polynomial(-1)
            ),
        ),
    )
    expected_sum_k = algebra.add(
        algebra.negate(algebra.product(q4, algebra.power(q_minus_1, 3))),
        algebra.product(q, q_minus_1, algebra.add(q, one)),
    )
    identities = {
        "diagonal Euler coefficient": (diagonal, expected_diagonal),
        "off-diagonal Euler coefficient": (off_diagonal, expected_off_diagonal),
        "a^2 total": (sum_a_squared, expected_sum_a_squared),
        "a^4 principal total": (a_fourth_t0, expected_a_fourth_t0),
        "a^4 correction total": (a_fourth_delta, expected_a_fourth_delta),
        "a^4 total": (sum_a_fourth, expected_sum_a_fourth),
        "a^2*b principal total": (a_squared_b_t0, expected_a_squared_b_t0),
        "a^2*b correction total": (a_squared_b_delta, expected_a_squared_b_delta),
        "a^2*b total": (sum_a_squared_b, expected_sum_a_squared_b),
        "b first-moment L^2 sieve": (
            quadratic_rows[0].sieve_value,
            expected_diagonal,
        ),
        "b first-moment L M sieve": (
            quadratic_rows[1].sieve_value,
            expected_off_diagonal,
        ),
        "b first-moment Q sieve": (
            quadratic_rows[2].sieve_value,
            polynomial(-1),
        ),
        "b first-moment L^2 contribution": (
            quadratic_rows[0].contribution,
            algebra.multiply(q, expected_diagonal),
        ),
        "b first-moment L M contribution": (
            quadratic_rows[1].contribution,
            algebra.multiply(choose_q_2, expected_off_diagonal),
        ),
        "b first-moment Q contribution": (
            quadratic_rows[2].contribution,
            algebra.negate(irreducible_quadratics),
        ),
        "b first-moment total": (sum_b, expected_sum_b),
        "T0": (t0, expected_t0),
        "Delta": (delta, expected_delta),
        "b^2 total": (sum_b_squared, expected_sum_b_squared),
        "K total": (sum_k, expected_sum_k),
    }
    for label, (actual, expected) in identities.items():
        if actual != expected:
            raise ArithmeticError(f"symbolic identity failed: {label}")

    return MomentCertificate(
        rows=rows,
        quadratic_rows=quadratic_rows,
        squarefree_count=squarefree_count,
        a_diagonal_coefficient=diagonal,
        a_off_diagonal_coefficient=off_diagonal,
        sum_a_squared=sum_a_squared,
        a_fourth_t0=a_fourth_t0,
        a_fourth_delta=a_fourth_delta,
        sum_a_fourth=sum_a_fourth,
        a_squared_b_t0=a_squared_b_t0,
        a_squared_b_delta=a_squared_b_delta,
        sum_a_squared_b=sum_a_squared_b,
        sum_b=sum_b,
        t0=t0,
        delta=delta,
        sum_b_squared=sum_b_squared,
        sum_k=sum_k,
        operations_used=algebra.operations,
    )


def main() -> int:
    certificate = build_certificate()
    sign_density = build_sign_density_certificate(certificate)
    print(
        "OK: exact genus-two moment identities, including E[b], E[a^4], and E[a^2*b]; "
        f"{certificate.operations_used}/{HARD_OPERATION_LIMIT} symbolic operations; "
        f"negative-sign liminf >= 1/{sign_density.proportion_denominator}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
