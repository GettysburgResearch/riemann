#!/usr/bin/env python3
"""Exact histogram-only packet for elliptic-pair tensor factors in SO(4).

The sole finite input is the locked marked-cubic trace histogram in
``genus1_cubic_family_laws.json`` for q=3,5,7,11,13.  The producer takes
ordered Cartesian products of those 55 histogram atoms; it does not build a
finite field, enumerate a curve, sample, or use floating point.

For

    P_A(T)=1+A*T+q*T^2,   P_B(T)=1+B*T+q*T^2,

the tensor roots give the degree-four polynomial

    1-A*B*T+q*(A^2+B^2-2*q)*T^2-q^2*A*B*T^3+q^4*T^4.

Closed coefficients and an independent Newton-power-sum construction are
compared at every frozen Cartesian atom pair.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_pair_rankin_so4_family.json"
NOTE_PATH = HERE / "ELLIPTIC_PAIR_RANKIN_SO4_FAMILY.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_pair_rankin_so4_family.py"

SOURCE_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
SOURCE_PRODUCER_PATH = HERE / "genus1_cubic_family_laws.py"
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
)
EXPECTED_SOURCE_FIXTURE_SHA256_LF = (
    "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
)
EXPECTED_SOURCE_PRODUCER_SHA256_LF = (
    "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79"
)

FROZEN_Q_VALUES = (3, 5, 7, 11, 13)
MAX_HAAR_MOMENT_ORDER = 12
ATOM_PAIR_CAP_INCLUSIVE = 55**2
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 4_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_builtin_int(value: object, name: str) -> int:
    if type(value) is not int:
        raise TypeError(f"{name} must be a built-in integer")
    return value


def _prime_power_data(q: object) -> tuple[int, int]:
    """Return (p,r), strictly refusing booleans and non-prime-power q."""

    q_int = _require_builtin_int(q, "q")
    if q_int < 3 or q_int % 2 == 0:
        raise ValueError("q must be an odd prime power")
    for candidate in range(3, math.isqrt(q_int) + 1, 2):
        if q_int % candidate:
            continue
        residue = q_int
        exponent = 0
        while residue % candidate == 0:
            residue //= candidate
            exponent += 1
        if residue != 1:
            raise ValueError("q must be an odd prime power")
        return candidate, exponent
    return q_int, 1


class ResourceGuard:
    """Fail closed on both histogram-pair and declared-work budgets."""

    def __init__(
        self,
        atom_pair_cap: int = ATOM_PAIR_CAP_INCLUSIVE,
        work_cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE,
    ) -> None:
        if type(atom_pair_cap) is not int or atom_pair_cap < 0:
            raise ValueError("atom-pair cap must be a nonnegative built-in integer")
        if type(work_cap) is not int or work_cap <= 0:
            raise ValueError("work cap must be a positive built-in integer")
        self.atom_pair_cap = atom_pair_cap
        self.work_cap = work_cap
        self.atom_pairs = 0
        self.ledger: Counter[str] = Counter()

    @property
    def total_work(self) -> int:
        return sum(self.ledger.values())

    def charge_pairs(self, units: int = 1) -> None:
        if type(units) is not int or units < 0:
            raise ValueError("atom-pair charge must be a nonnegative integer")
        if self.atom_pairs + units > self.atom_pair_cap:
            raise RuntimeError(
                f"histogram atom-pair cap exceeded: "
                f"{self.atom_pairs + units}>{self.atom_pair_cap}"
            )
        self.atom_pairs += units
        self.charge("source_histogram_atom_pairs", units)

    def charge(self, name: str, units: int = 1) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("resource charge name must be a nonempty string")
        if type(units) is not int or units < 0:
            raise ValueError("resource charge must be a nonnegative integer")
        if self.total_work + units >= self.work_cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.work_cap}"
            )
        self.ledger[name] += units


def multiply_polynomials(
    left: Sequence[int], right: Sequence[int]
) -> tuple[int, ...]:
    if not left or not right:
        raise ValueError("polynomial coefficient sequences must be nonempty")
    if any(type(coefficient) is not int for coefficient in (*left, *right)):
        raise TypeError("polynomial coefficients must be built-in integers")
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def add_scaled_polynomials(
    terms: Sequence[tuple[int, Sequence[int]]],
) -> tuple[int, ...]:
    """Exact coefficientwise sum of integer polynomials with scalar weights."""

    if not terms:
        raise ValueError("at least one polynomial term is required")
    if any(type(scale) is not int for scale, _ in terms):
        raise TypeError("polynomial scales must be built-in integers")
    if any(
        not coefficients
        or any(type(coefficient) is not int for coefficient in coefficients)
        for _, coefficients in terms
    ):
        raise TypeError("polynomial coefficients must be nonempty built-in integers")
    output = [0] * max(len(coefficients) for _, coefficients in terms)
    for scale, coefficients in terms:
        for degree, coefficient in enumerate(coefficients):
            output[degree] += scale * coefficient
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return tuple(output)


BivariatePolynomial = dict[tuple[int, int], int]


def _bivariate_add(
    *terms: tuple[int, Mapping[tuple[int, int], int]],
) -> BivariatePolynomial:
    output: Counter[tuple[int, int]] = Counter()
    for scale, polynomial in terms:
        if type(scale) is not int:
            raise TypeError("bivariate polynomial scales must be built-in integers")
        for exponent, coefficient in polynomial.items():
            if (
                not isinstance(exponent, tuple)
                or len(exponent) != 2
                or any(type(value) is not int or value < 0 for value in exponent)
                or type(coefficient) is not int
            ):
                raise TypeError("invalid exact bivariate polynomial term")
            output[exponent] += scale * coefficient
    return {
        exponent: coefficient
        for exponent, coefficient in output.items()
        if coefficient
    }


def _bivariate_multiply(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
) -> BivariatePolynomial:
    output: Counter[tuple[int, int]] = Counter()
    for (left_first, left_second), left_coefficient in left.items():
        for (right_first, right_second), right_coefficient in right.items():
            output[
                (left_first + right_first, left_second + right_second)
            ] += left_coefficient * right_coefficient
    return {
        exponent: coefficient
        for exponent, coefficient in output.items()
        if coefficient
    }


def _bivariate_square(
    polynomial: Mapping[tuple[int, int], int],
) -> BivariatePolynomial:
    return _bivariate_multiply(polynomial, polynomial)


def full_quartic_symbolic_certificates() -> dict[str, BivariatePolynomial]:
    """Return zero residuals certifying both factors of the full discriminant.

    The first variable is s (or p) and the second is t (or r), depending on
    the named certificate.
    """

    one = {(0, 0): 1}
    first = {(1, 0): 1}
    second = {(0, 1): 1}

    # Reciprocal quadratic traces: Q=(Z^2-s*Z+1)(Z^2-t*Z+1),
    # x=s+t and y=s*t+2.
    x = _bivariate_add((1, first), (1, second))
    y = _bivariate_add(
        (1, _bivariate_multiply(first, second)),
        (2, one),
    )
    y_plus_two = _bivariate_add((1, y), (2, one))
    y_minus_two = _bivariate_add((1, y), (-2, one))
    fold_from_xy = _bivariate_add(
        (1, _bivariate_square(y_plus_two)),
        (-4, _bivariate_square(x)),
    )
    internal_quadratic_discriminants = _bivariate_multiply(
        _bivariate_add((1, _bivariate_square(first)), (-4, one)),
        _bivariate_add((1, _bivariate_square(second)), (-4, one)),
    )
    endpoint_from_xy = _bivariate_add(
        (1, _bivariate_square(x)),
        (-4, y_minus_two),
    )
    trace_difference_squared = _bivariate_square(
        _bivariate_add((1, first), (-1, second))
    )
    full_from_xy = _bivariate_multiply(
        fold_from_xy, _bivariate_square(endpoint_from_xy)
    )
    full_from_factor_roots = _bivariate_multiply(
        internal_quadratic_discriminants,
        _bivariate_square(trace_difference_squared),
    )

    # Squared base traces: x^2=p*r and y=p+r-2.
    x_squared = _bivariate_multiply(first, second)
    y_pr = _bivariate_add((1, first), (1, second), (-2, one))
    fold_pr = _bivariate_add(
        (1, _bivariate_square(_bivariate_add((1, y_pr), (2, one)))),
        (-4, x_squared),
    )
    p_minus_r_squared = _bivariate_square(
        _bivariate_add((1, first), (-1, second))
    )
    endpoint_pr = _bivariate_add(
        (1, x_squared),
        (-4, _bivariate_add((1, y_pr), (-2, one))),
    )
    endpoint_expected = _bivariate_multiply(
        _bivariate_add((1, first), (-4, one)),
        _bivariate_add((1, second), (-4, one)),
    )
    full_pr = _bivariate_multiply(fold_pr, _bivariate_square(endpoint_pr))
    full_pr_expected = _bivariate_multiply(
        p_minus_r_squared, _bivariate_square(endpoint_expected)
    )
    return {
        "factor_trace_D_residual": _bivariate_add(
            (1, fold_from_xy), (-1, internal_quadratic_discriminants)
        ),
        "factor_trace_E_residual": _bivariate_add(
            (1, endpoint_from_xy), (-1, trace_difference_squared)
        ),
        "factor_trace_full_discriminant_residual": _bivariate_add(
            (1, full_from_xy), (-1, full_from_factor_roots)
        ),
        "squared_base_trace_D_residual": _bivariate_add(
            (1, fold_pr), (-1, p_minus_r_squared)
        ),
        "squared_base_trace_E_residual": _bivariate_add(
            (1, endpoint_pr), (-1, endpoint_expected)
        ),
        "squared_base_trace_full_discriminant_residual": _bivariate_add(
            (1, full_pr), (-1, full_pr_expected)
        ),
    }


def _fraction_determinant(matrix: Sequence[Sequence[Fraction | int]]) -> Fraction:
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("determinant requires a nonempty square matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    determinant = Fraction(1)
    dimension = len(work)
    for column in range(dimension):
        pivot_row = next(
            (row for row in range(column, dimension) if work[row][column]),
            None,
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            determinant = -determinant
        pivot = work[column][column]
        determinant *= pivot
        for row in range(column + 1, dimension):
            if not work[row][column]:
                continue
            factor = work[row][column] / pivot
            for index in range(column, dimension):
                work[row][index] -= factor * work[column][index]
    return determinant


def reciprocal_quartic_discriminant_via_resultant(
    x: Fraction | int, y: Fraction | int
) -> Fraction:
    """Direct Sylvester-resultant discriminant of Z^4-xZ^3+yZ^2-xZ+1."""

    if type(x) not in {int, Fraction} or type(y) not in {int, Fraction}:
        raise TypeError("quartic coordinates must be exact integers or Fractions")
    x_fraction = Fraction(x)
    y_fraction = Fraction(y)
    polynomial = [
        Fraction(1),
        -x_fraction,
        y_fraction,
        -x_fraction,
        Fraction(1),
    ]
    derivative = [
        Fraction(4),
        -3 * x_fraction,
        2 * y_fraction,
        -x_fraction,
    ]
    # For degrees 4 and 3, the Sylvester matrix has three shifted rows of Q
    # followed by four shifted rows of Q'.  Since (-1)^(4*3/2)=+1 and Q is
    # monic, this resultant is exactly Disc_Z(Q).
    matrix = [[Fraction(0) for _ in range(7)] for _ in range(7)]
    for row in range(3):
        matrix[row][row : row + 5] = polynomial
    for row in range(4):
        matrix[3 + row][row : row + 4] = derivative
    return _fraction_determinant(matrix)


def full_quartic_discriminant_certificate(
    A: object, B: object, q: object
) -> dict[str, Fraction | bool]:
    """Separate the coefficient-map fold from the full root discriminant."""

    certificate = coefficient_image_certificate(A, B, q)
    x = certificate["x"]
    y = certificate["y"]
    p = certificate["p"]
    r = certificate["r"]
    if not all(isinstance(value, Fraction) for value in (x, y, p, r)):
        raise ArithmeticError("coefficient certificate lost exact rational type")
    fold_discriminant = (y + 2) ** 2 - 4 * x * x
    endpoint_factor = x * x - 4 * (y - 2)
    full_discriminant = fold_discriminant * endpoint_factor**2
    resultant_discriminant = reciprocal_quartic_discriminant_via_resultant(x, y)
    if fold_discriminant != (p - r) ** 2:
        raise ArithmeticError("fold discriminant normalization failed")
    if endpoint_factor != (p - 4) * (r - 4):
        raise ArithmeticError("Hasse-endpoint factor normalization failed")
    if full_discriminant != resultant_discriminant:
        raise ArithmeticError("factorized and resultant quartic discriminants disagree")
    return {
        "x": x,
        "y": y,
        "p": p,
        "r": r,
        "coefficient_map_fold_D": fold_discriminant,
        "hasse_endpoint_factor_E": endpoint_factor,
        "full_quartic_root_discriminant": full_discriminant,
        "resultant_discriminant": resultant_discriminant,
        "on_fold_wall": fold_discriminant == 0,
        "on_hasse_endpoint_wall": endpoint_factor == 0,
        "has_repeated_quartic_root": full_discriminant == 0,
    }


def sym3_comparison_polynomial_certificates() -> dict[str, tuple[int, ...]]:
    """Symbolically certify the Sym^3 curve and its SO(4)-region discriminant."""

    # z=t^2, x^2=z*(z-2)^2, y=z^2-3*z+2.
    x_squared = multiply_polynomials((0, 1), multiply_polynomials((-2, 1), (-2, 1)))
    y = (2, -3, 1)
    x_fourth = multiply_polynomials(x_squared, x_squared)
    x_squared_y = multiply_polynomials(x_squared, y)
    y_squared = multiply_polynomials(y, y)
    y_cubed = multiply_polynomials(y_squared, y)
    curve_residual = add_scaled_polynomials(
        (
            (-1, x_fourth),
            (1, x_squared_y),
            (1, x_squared),
            (1, y_cubed),
            (-2, y_squared),
        )
    )
    y_plus_two = add_scaled_polynomials(((1, y), (1, (2,))))
    discriminant = add_scaled_polynomials(
        ((1, multiply_polynomials(y_plus_two, y_plus_two)), (-4, x_squared))
    )
    expected_discriminant = multiply_polynomials(
        multiply_polynomials((-1, 1), (-1, 1)),
        multiply_polynomials((-4, 1), (-4, 1)),
    )
    return {
        "curve_residual": curve_residual,
        "region_discriminant": discriminant,
        "expected_region_discriminant": expected_discriminant,
    }


def elliptic_power_sum(A: object, q: object, order: object) -> int:
    """Return alpha^n+beta^n when alpha+beta=-A and alpha*beta=q."""

    A_int = _require_builtin_int(A, "A")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    order_int = _require_builtin_int(order, "order")
    if order_int < 0:
        raise ValueError("power-sum order must be nonnegative")
    if order_int == 0:
        return 2
    if order_int == 1:
        return -A_int
    previous_previous, previous = 2, -A_int
    for _ in range(2, order_int + 1):
        previous_previous, previous = (
            previous,
            -A_int * previous - q_int * previous_previous,
        )
    return previous


def tensor_coefficients_closed(A: object, B: object, q: object) -> tuple[int, ...]:
    """Closed degree-four factor for the tensor of two quadratic factors."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    return (
        1,
        -A_int * B_int,
        q_int * (A_int * A_int + B_int * B_int - 2 * q_int),
        -(q_int**2) * A_int * B_int,
        q_int**4,
    )


def tensor_coefficients_via_newton(
    A: object, B: object, q: object
) -> tuple[int, ...]:
    """Independent construction from p_n(A tensor B)=p_n(A)*p_n(B)."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    power_sums = [0]
    for order in range(1, 5):
        power_sums.append(
            elliptic_power_sum(A_int, q_int, order)
            * elliptic_power_sum(B_int, q_int, order)
        )
    coefficients = [1]
    for degree in range(1, 5):
        numerator = -sum(
            coefficients[degree - order] * power_sums[order]
            for order in range(1, degree + 1)
        )
        if numerator % degree:
            raise ArithmeticError("tensor Newton recurrence lost integrality")
        coefficients.append(numerator // degree)
    return tuple(coefficients)


def normalized_coefficients(
    A: object, B: object, q: object
) -> tuple[Fraction, Fraction]:
    """Return (x,y) in 1-x*Z+y*Z^2-x*Z^3+Z^4, Z=q*T."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    return (
        Fraction(A_int * B_int, q_int),
        Fraction(A_int * A_int + B_int * B_int - 2 * q_int, q_int),
    )


def coefficient_image_certificate(
    A: object, B: object, q: object
) -> dict[str, Fraction | bool]:
    """Exact forward certificate for the SO(4) semialgebraic coefficient image."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    x, y = normalized_coefficients(A_int, B_int, q_int)
    p = Fraction(A_int * A_int, q_int)
    r = Fraction(B_int * B_int, q_int)
    discriminant = (y + 2) ** 2 - 4 * x * x
    if x * x != p * r:
        raise ArithmeticError("normalized trace product identity failed")
    if y != p + r - 2:
        raise ArithmeticError("normalized middle coefficient identity failed")
    if discriminant != (p - r) ** 2:
        raise ArithmeticError("coefficient-image discriminant identity failed")
    return {
        "x": x,
        "y": y,
        "p": p,
        "r": r,
        "coefficient_map_fold_D": discriminant,
        "hasse_box": 0 <= p <= 4 and 0 <= r <= 4,
    }


def wall_factorization(A: object, q: object, relation: object) -> tuple[int, ...]:
    """Factor on B=A or B=-A, with the relation selected explicitly."""

    A_int = _require_builtin_int(A, "A")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    if type(relation) is not str or relation not in {"equal", "opposite"}:
        raise ValueError("relation must be exactly 'equal' or 'opposite'")
    trace_square_part = A_int * A_int - 2 * q_int
    if relation == "equal":
        return multiply_polynomials(
            (1, -2 * q_int, q_int**2),
            (1, -trace_square_part, q_int**2),
        )
    return multiply_polynomials(
        (1, 2 * q_int, q_int**2),
        (1, trace_square_part, q_int**2),
    )


def catalan(index: object) -> int:
    index_int = _require_builtin_int(index, "Catalan index")
    if index_int < 0:
        raise ValueError("Catalan index must be nonnegative")
    return math.comb(2 * index_int, index_int) // (index_int + 1)


def so4_haar_trace_moment(order: object) -> int:
    """Haar moment of the SO(4) standard trace through the locked order cap."""

    order_int = _require_builtin_int(order, "moment order")
    if not 0 <= order_int <= MAX_HAAR_MOMENT_ORDER:
        raise ValueError(
            f"SO(4) Haar moment order is restricted to 0..{MAX_HAAR_MOMENT_ORDER}"
        )
    if order_int % 2:
        return 0
    return catalan(order_int // 2) ** 2


def su2_irrep_trace_moment(highest_weight: object, order: object) -> int:
    """Multiplicity of V_0 in V_highest_weight tensor power ``order``."""

    weight = _require_builtin_int(highest_weight, "highest weight")
    order_int = _require_builtin_int(order, "moment order")
    if weight < 0:
        raise ValueError("highest weight must be nonnegative")
    if not 0 <= order_int <= MAX_HAAR_MOMENT_ORDER:
        raise ValueError(
            f"SU(2) moment order is restricted to 0..{MAX_HAAR_MOMENT_ORDER}"
        )
    multiplicities: Counter[int] = Counter({0: 1})
    for _ in range(order_int):
        following: Counter[int] = Counter()
        for left_weight, multiplicity in multiplicities.items():
            for output_weight in range(
                abs(left_weight - weight), left_weight + weight + 1, 2
            ):
                following[output_weight] += multiplicity
        multiplicities = following
    return multiplicities[0]


def sym3_su2_haar_trace_moment(order: object) -> int:
    """Trace moment of the four-dimensional Sym^3(SU(2)) image."""

    return su2_irrep_trace_moment(3, order)


def generic_usp4_standard_trace_moment(order: object) -> int:
    """Exact generic USp(4) standard-trace moments through degree six.

    In degrees 0,2,4 the symplectic pair contractions are independent.  In
    degree 6 the 15 pair contractions have the unique rank-four Pfaffian
    relation, leaving 14 invariants.
    """

    order_int = _require_builtin_int(order, "moment order")
    if not 0 <= order_int <= 6:
        raise ValueError("generic USp(4) comparison is restricted to order 0..6")
    return {0: 1, 1: 0, 2: 1, 3: 0, 4: 3, 5: 0, 6: 14}[order_int]


def sym3_coefficient_curve_residual(
    x: Fraction | int, y: Fraction | int
) -> Fraction:
    """Independent residual for the normalized Sym^3(SU(2)) coefficient curve."""

    if type(x) not in {int, Fraction} or type(y) not in {int, Fraction}:
        raise TypeError("Sym^3 curve coordinates must be exact integers or Fractions")
    x_fraction = Fraction(x)
    y_fraction = Fraction(y)
    return (
        -(x_fraction**4)
        + x_fraction * x_fraction * y_fraction
        + x_fraction * x_fraction
        + y_fraction**3
        - 2 * y_fraction * y_fraction
    )


def base_normalized_trace_moment(order: object, q: object) -> Fraction:
    """Locked marked-cubic normalized moments needed by this packet."""

    order_int = _require_builtin_int(order, "moment order")
    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    if order_int not in {0, 1, 2, 3, 4}:
        raise ValueError("base moment order is restricted to 0..4")
    if order_int == 0:
        return Fraction(1)
    if order_int % 2:
        return Fraction(0)
    if order_int == 2:
        return 1 - Fraction(1, q_int**2)
    return 2 - Fraction(3, q_int**2) - Fraction(1, q_int**3)


def rankin_moments_via_base_moments(q: object) -> dict[str, Fraction]:
    """Derive tensor-coordinate laws from m2,m4 of two independent copies."""

    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    m2 = base_normalized_trace_moment(2, q_int)
    m4 = base_normalized_trace_moment(4, q_int)
    return {
        "mean_x_squared": m2**2,
        "mean_x_fourth": m4**2,
        "mean_y": 2 * m2 - 2,
        "mean_y_squared": 2 * m4 + 2 * m2**2 - 8 * m2 + 4,
        "mean_x_squared_times_y": 2 * m4 * m2 - 2 * m2**2,
        "mean_coefficient_map_fold_D": 2 * m4 - 2 * m2**2,
    }


def rankin_moment_formulas(q: object) -> dict[str, Fraction]:
    """Expanded all-odd-prime-power formulas, checked against the base route."""

    q_int = _require_builtin_int(q, "q")
    _prime_power_data(q_int)
    direct = {
        "mean_x_squared": (1 - Fraction(1, q_int**2)) ** 2,
        "mean_x_fourth": (
            2 - Fraction(3, q_int**2) - Fraction(1, q_int**3)
        )
        ** 2,
        "mean_y": -Fraction(2, q_int**2),
        "mean_y_squared": (
            2
            - Fraction(2, q_int**2)
            - Fraction(2, q_int**3)
            + Fraction(2, q_int**4)
        ),
        "mean_x_squared_times_y": (
            2
            - Fraction(6, q_int**2)
            - Fraction(2, q_int**3)
            + Fraction(4, q_int**4)
            + Fraction(2, q_int**5)
        ),
        "mean_coefficient_map_fold_D": (
            2
            - Fraction(2, q_int**2)
            - Fraction(2, q_int**3)
            - Fraction(2, q_int**4)
        ),
    }
    if direct != rankin_moments_via_base_moments(q_int):
        raise ArithmeticError("expanded Rankin moment laws disagree with base moments")
    return direct


def _load_locked_source() -> dict[str, object]:
    if _lf_sha256(SOURCE_FIXTURE_PATH) != EXPECTED_SOURCE_FIXTURE_SHA256_LF:
        raise RuntimeError("locked genus-one fixture file hash drifted")
    if _lf_sha256(SOURCE_PRODUCER_PATH) != EXPECTED_SOURCE_PRODUCER_SHA256_LF:
        raise RuntimeError("locked genus-one producer file hash drifted")
    payload = json.loads(SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
    if payload.get("payload_sha256") != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("locked genus-one payload identity drifted")
    unhashed = dict(payload)
    claimed = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
        raise RuntimeError("locked genus-one payload hash is internally stale")
    normalization = payload.get("normalization")
    if not isinstance(normalization, dict):
        raise RuntimeError("locked genus-one normalization is missing")
    if normalization.get("trace") != (
        "a_D=q+1-#E_D(F_q)=-sum_x quadratic_character(D(x))"
    ):
        raise RuntimeError("locked genus-one trace convention drifted")
    if normalization.get("l_polynomial") != "L_D(T)=1-a_D*T+q*T^2":
        raise RuntimeError("locked genus-one local-factor convention drifted")
    theorem = payload.get("all_q_moment_theorem")
    if not isinstance(theorem, dict):
        raise RuntimeError("locked genus-one moment theorem is missing")
    if theorem.get("scope") != "every odd prime power q and every integer n>=0":
        raise RuntimeError("locked genus-one theorem scope drifted")
    expected = {"W_2": "q^2-1", "W_4": "2*q^3-3*q-1"}
    explicit = theorem.get("explicit_stack_sums")
    if not isinstance(explicit, dict):
        raise RuntimeError("locked genus-one explicit moments are missing")
    for name, formula in expected.items():
        if explicit.get(name) != formula:
            raise RuntimeError(f"locked genus-one {name} formula drifted")
    if theorem.get("model_average") != "E_model[a_D^(2n)]=W_(2n)/q":
        raise RuntimeError("locked genus-one model measure drifted")
    return payload


def _lock(path: Path, **extra: object) -> dict[str, object]:
    return {
        "path": _relative(path),
        "sha256_lf_normalized": _lf_sha256(path),
        **extra,
    }


def _source_locks() -> dict[str, object]:
    locks = {
        "genus1_fixture": _lock(
            SOURCE_FIXTURE_PATH,
            payload_sha256=EXPECTED_SOURCE_PAYLOAD_SHA256,
        ),
        "genus1_producer": _lock(SOURCE_PRODUCER_PATH),
        "producer": _lock(Path(__file__).resolve()),
        "note": _lock(NOTE_PATH),
        "test": _lock(TEST_PATH),
    }
    expected = {
        "genus1_fixture": EXPECTED_SOURCE_FIXTURE_SHA256_LF,
        "genus1_producer": EXPECTED_SOURCE_PRODUCER_SHA256_LF,
    }
    for name, expected_hash in expected.items():
        if locks[name]["sha256_lf_normalized"] != expected_hash:
            raise RuntimeError(f"source lock drifted: {name}")
    return locks


def _law_moment(
    law: Mapping[tuple[Fraction, Fraction], int],
    member_count: int,
    x_power: int,
    y_power: int,
) -> Fraction:
    return Fraction(
        sum(
            count * x**x_power * y**y_power
            for (x, y), count in law.items()
        ),
        member_count,
    )


def _frozen_cartesian_transforms(
    source: Mapping[str, object], guard: ResourceGuard
) -> list[dict[str, object]]:
    rows = source.get("finite_regressions")
    if not isinstance(rows, list):
        raise RuntimeError("locked source has no finite regression rows")
    if tuple(row.get("q") for row in rows if isinstance(row, dict)) != FROZEN_Q_VALUES:
        raise RuntimeError("locked source q rows drifted")

    output: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError("locked source row is not an object")
        q = _require_builtin_int(row.get("q"), "source q")
        raw_histogram = row.get("model_trace_histogram")
        if not isinstance(raw_histogram, dict):
            raise RuntimeError("locked source histogram is missing")
        histogram = {
            int(trace): _require_builtin_int(count, "histogram count")
            for trace, count in raw_histogram.items()
        }
        if any(count <= 0 for count in histogram.values()):
            raise RuntimeError("locked source histogram has nonpositive mass")
        member_count = sum(histogram.values())
        if member_count != q * q * (q - 1):
            raise RuntimeError("locked source histogram has the wrong total mass")

        coefficient_law: Counter[tuple[int, ...]] = Counter()
        coordinate_law: Counter[tuple[Fraction, Fraction]] = Counter()
        trace_law: Counter[Fraction] = Counter()
        equal_wall_mass = 0
        opposite_wall_mass = 0
        wall_intersection_mass = 0
        hasse_endpoint_wall_mass = 0
        fold_and_endpoint_intersection_mass = 0
        full_repeated_root_mass = 0
        atom_pairs = 0
        for left_trace, left_count in sorted(histogram.items()):
            for right_trace, right_count in sorted(histogram.items()):
                guard.charge_pairs()
                atom_pairs += 1
                pair_count = left_count * right_count
                # The source uses 1-t*T+q*T^2; this packet uses A=-t.
                A = -left_trace
                B = -right_trace
                closed = tensor_coefficients_closed(A, B, q)
                newton = tensor_coefficients_via_newton(A, B, q)
                guard.charge("closed_vs_newton_factor_checks")
                if closed != newton:
                    raise ArithmeticError("closed and Newton tensor factors disagree")
                if closed[3] != q * q * closed[1] or closed[4] != q**4:
                    raise ArithmeticError("tensor reciprocal shape failed")
                certificate = coefficient_image_certificate(A, B, q)
                guard.charge("semialgebraic_forward_checks")
                if certificate["hasse_box"] is not True:
                    raise ArithmeticError("locked elliptic trace left the Hasse box")
                x = certificate["x"]
                y = certificate["y"]
                if not isinstance(x, Fraction) or not isinstance(y, Fraction):
                    raise ArithmeticError("normalized coefficient lost exact rational type")
                coefficient_law[closed] += pair_count
                coordinate_law[(x, y)] += pair_count
                trace_law[x] += pair_count

                full_discriminant = full_quartic_discriminant_certificate(A, B, q)
                guard.charge("full_quartic_resultant_checks")
                on_fold_wall = A * A == B * B
                on_endpoint_wall = A * A == 4 * q or B * B == 4 * q
                if full_discriminant["on_fold_wall"] is not on_fold_wall:
                    raise ArithmeticError("fold-wall classification disagrees")
                if (
                    full_discriminant["on_hasse_endpoint_wall"]
                    is not on_endpoint_wall
                ):
                    raise ArithmeticError("Hasse-endpoint classification disagrees")
                if (
                    full_discriminant["has_repeated_quartic_root"]
                    is not (on_fold_wall or on_endpoint_wall)
                ):
                    raise ArithmeticError("full repeated-root classification disagrees")
                if on_endpoint_wall:
                    hasse_endpoint_wall_mass += pair_count
                if on_fold_wall and on_endpoint_wall:
                    fold_and_endpoint_intersection_mass += pair_count
                if on_fold_wall or on_endpoint_wall:
                    full_repeated_root_mass += pair_count

                if A == B:
                    equal_wall_mass += pair_count
                    if wall_factorization(A, q, "equal") != closed:
                        raise ArithmeticError("equal-trace wall factorization failed")
                if A == -B:
                    opposite_wall_mass += pair_count
                    if wall_factorization(A, q, "opposite") != closed:
                        raise ArithmeticError("opposite-trace wall factorization failed")
                if A == B == 0:
                    wall_intersection_mass += pair_count

        pair_member_count = member_count**2
        if atom_pairs != len(histogram) ** 2:
            raise ArithmeticError("Cartesian histogram traversal was incomplete")
        if sum(coefficient_law.values()) != pair_member_count:
            raise ArithmeticError("coefficient law lost pair mass")
        if sum(coordinate_law.values()) != pair_member_count:
            raise ArithmeticError("coordinate law lost pair mass")
        if sum(trace_law.values()) != pair_member_count:
            raise ArithmeticError("trace law lost pair mass")

        finite_moments = {
            "mean_x_squared": _law_moment(coordinate_law, pair_member_count, 2, 0),
            "mean_x_fourth": _law_moment(coordinate_law, pair_member_count, 4, 0),
            "mean_y": _law_moment(coordinate_law, pair_member_count, 0, 1),
            "mean_y_squared": _law_moment(coordinate_law, pair_member_count, 0, 2),
            "mean_x_squared_times_y": _law_moment(
                coordinate_law, pair_member_count, 2, 1
            ),
            "mean_coefficient_map_fold_D": Fraction(
                sum(
                    count * ((y + 2) ** 2 - 4 * x * x)
                    for (x, y), count in coordinate_law.items()
                ),
                pair_member_count,
            ),
        }
        guard.charge("finite_moment_law_checks", len(finite_moments))
        theorem_moments = rankin_moment_formulas(q)
        if finite_moments != theorem_moments:
            raise ArithmeticError("frozen Cartesian law disagrees with all-q moments")

        output.append(
            {
                "q": q,
                "source_trace_histogram": {
                    str(trace): histogram[trace] for trace in sorted(histogram)
                },
                "source_histogram_sha256": _canonical_sha256(
                    {str(trace): histogram[trace] for trace in sorted(histogram)}
                ),
                "source_trace_atom_count": len(histogram),
                "source_members_represented": member_count,
                "ordered_cartesian_atom_pairs": atom_pairs,
                "ordered_model_pairs_represented": pair_member_count,
                "normalized_tensor_trace_histogram": {
                    "support_size": len(trace_law),
                    "atoms": [
                        {"x": _fraction(x), "pair_count": trace_law[x]}
                        for x in sorted(trace_law)
                    ],
                },
                "complete_normalized_coefficient_law": {
                    "support_size": len(coordinate_law),
                    "atoms": [
                        {
                            "x": _fraction(x),
                            "y": _fraction(y),
                            "coefficient_map_fold_D": _fraction(
                                (y + 2) ** 2 - 4 * x * x
                            ),
                            "hasse_endpoint_factor_E": _fraction(
                                x * x - 4 * (y - 2)
                            ),
                            "full_quartic_root_discriminant": _fraction(
                                ((y + 2) ** 2 - 4 * x * x)
                                * (x * x - 4 * (y - 2)) ** 2
                            ),
                            "pair_count": coordinate_law[(x, y)],
                        }
                        for x, y in sorted(coordinate_law)
                    ],
                },
                "complete_integral_local_factor_law": {
                    "support_size": len(coefficient_law),
                    "atoms": [
                        {
                            "coefficients_T0_through_T4": list(coefficients),
                            "pair_count": coefficient_law[coefficients],
                        }
                        for coefficients in sorted(coefficient_law)
                    ],
                },
                "coefficient_map_fold_wall_masses": {
                    "A_equals_B": equal_wall_mass,
                    "A_equals_minus_B": opposite_wall_mass,
                    "intersection_A_equals_B_equals_zero": wall_intersection_mass,
                    "fold_union_D_equals_zero_by_inclusion_exclusion": (
                        equal_wall_mass + opposite_wall_mass - wall_intersection_mass
                    ),
                },
                "full_quartic_repeated_root_masses": {
                    "fold_wall_D_equals_zero": (
                        equal_wall_mass + opposite_wall_mass - wall_intersection_mass
                    ),
                    "hasse_endpoint_wall_E_equals_zero": hasse_endpoint_wall_mass,
                    "fold_and_endpoint_intersection": (
                        fold_and_endpoint_intersection_mass
                    ),
                    "exhaustive_union_full_discriminant_equals_zero": (
                        full_repeated_root_mass
                    ),
                    "classification": "Disc_Z(Q)=D*E^2, so repeated roots occur exactly on the union D=0 or E=0",
                },
                "selected_exact_moments": {
                    name: _fraction(value) for name, value in finite_moments.items()
                },
            }
        )
    return output


def build_fixture(q_values: Iterable[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"frozen packet requires exactly q={FROZEN_Q_VALUES}")
    source = _load_locked_source()
    guard = ResourceGuard()
    frozen = _frozen_cartesian_transforms(source, guard)
    haar_moments = [
        so4_haar_trace_moment(order) for order in range(MAX_HAAR_MOMENT_ORDER + 1)
    ]
    guard.charge("compact_moment_formula_evaluations", len(haar_moments))
    expected_haar = [1, 0, 1, 0, 4, 0, 25, 0, 196, 0, 1764, 0, 17424]
    if haar_moments != expected_haar:
        raise ArithmeticError("SO(4) compact trace moments drifted")
    sym3_moments_through_six = [
        sym3_su2_haar_trace_moment(order) for order in range(7)
    ]
    generic_usp4_moments_through_six = [
        generic_usp4_standard_trace_moment(order) for order in range(7)
    ]
    if sym3_moments_through_six != [1, 0, 1, 0, 4, 0, 34]:
        raise ArithmeticError("Sym^3(SU(2)) compact comparison drifted")
    if generic_usp4_moments_through_six != [1, 0, 1, 0, 3, 0, 14]:
        raise ArithmeticError("generic USp(4) compact comparison drifted")
    guard.charge("compact_cross_family_moment_evaluations", 14)
    sym3_polynomial_certificates = sym3_comparison_polynomial_certificates()
    if sym3_polynomial_certificates["curve_residual"] != (0,):
        raise ArithmeticError("Sym^3 comparison curve did not vanish symbolically")
    if (
        sym3_polynomial_certificates["region_discriminant"]
        != sym3_polynomial_certificates["expected_region_discriminant"]
    ):
        raise ArithmeticError("Sym^3 compact-region discriminant factorization failed")
    guard.charge("sym3_symbolic_polynomial_certificates", 2)
    quartic_symbolic_certificates = full_quartic_symbolic_certificates()
    nonzero_quartic_residuals = {
        name: residual
        for name, residual in quartic_symbolic_certificates.items()
        if residual
    }
    if nonzero_quartic_residuals:
        raise ArithmeticError(
            f"full quartic discriminant symbolic residuals: "
            f"{sorted(nonzero_quartic_residuals)}"
        )
    guard.charge(
        "full_quartic_symbolic_discriminant_certificates",
        len(quartic_symbolic_certificates),
    )
    for parameter in (
        Fraction(-2),
        Fraction(-3, 2),
        Fraction(-1),
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
        Fraction(2),
    ):
        sym3_x = parameter**3 - 2 * parameter
        sym3_y = parameter**4 - 3 * parameter**2 + 2
        if sym3_coefficient_curve_residual(sym3_x, sym3_y):
            raise ArithmeticError("Sym^3 comparison curve parameterization failed")
        guard.charge("sym3_curve_comparison_checks")
    symbolic_cross_checks = {}
    for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
        symbolic_cross_checks[str(q)] = {
            name: _fraction(value) for name, value in rankin_moment_formulas(q).items()
        }
        guard.charge("symbolic_prime_power_moment_cross_checks")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_pair_rankin_so4_family.v2",
        "raw_fixture_id": "elliptic-pair-rankin-so4-q3-q5-q7-q11-q13-v2",
        "status": "EXACT_LOCAL_ALGEBRA_ALL_Q_LOW_MOMENTS_AND_SOURCE_LOCKED_FINITE_PUSHFORWARDS",
        "rigor_level": {
            "local_tensor_factor": "PROVED_POINTWISE_BY_ROOT_SYMMETRY_AND_INDEPENDENT_NEWTON_RECURRENCE",
            "coefficient_image": "EXACT_SEMIALGEBRAIC_PARAMETER_ELIMINATION_AT_COMPACT_REPRESENTATION_LEVEL",
            "wall_factorizations": "EXACT_POINTWISE_POLYNOMIAL_IDENTITIES",
            "full_quartic_discriminant": "PROVED_BY_SYMBOLIC_FACTOR_ELIMINATION_AND_INDEPENDENT_SYLVESTER_RESULTANTS",
            "compact_moments": "EXACT_PRODUCT_OF_TWO_SU2_HAAR_MOMENTS",
            "all_q_family_moments": "EXACT_FOR_EVERY_ODD_PRIME_POWER_FROM_THE_LOCKED_GENUS_ONE_W2_AND_W4_LAWS",
            "finite_pushforwards": "EXACT_FOR_Q_3_5_7_11_13_FROM_COMPLETE_LOCKED_HISTOGRAMS",
            "global_automorphy_monodromy_and_novelty": "NOT_INFERRED",
        },
        "input_family_and_measure": {
            "marked_models": "two independent monic squarefree cubics over F_q",
            "source_measure": "ordered product of uniform marked-model measures, equivalently the product normalized elliptic-stack measure for trace statistics",
            "source_factor": "L_E(T)=1-t*T+q*T^2",
            "packet_factor": "P_A(T)=1+A*T+q*T^2 with the load-bearing conversion A=-t, independently for both inputs",
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "new_field_curve_or_model_enumeration": False,
        },
        "local_tensor_polynomial_theorem": {
            "hypotheses": "q is an odd prime power; A and B are integers; each quadratic factor has determinant q",
            "input": "(1+A*T+q*T^2)*(1+B*T+q*T^2) as two separate rank-two Frobenius factors",
            "tensor_output": "1-A*B*T+q*(A^2+B^2-2*q)*T^2-q^2*A*B*T^3+q^4*T^4",
            "functional_equation_shape": "c_3=q^2*c_1 and c_4=q^4",
            "independent_derivations": [
                "elementary symmetric functions of alpha*gamma, alpha*delta, beta*gamma, beta*delta",
                "Newton recurrence p_n(A tensor B)=p_n(A)*p_n(B)",
            ],
        },
        "compact_SO4_coefficient_image": {
            "normalization": "u=A/sqrt(q), v=B/sqrt(q), Z=q*T; P=1-x*Z+y*Z^2-x*Z^3+Z^4",
            "coordinates": "x=u*v=A*B/q and y=u^2+v^2-2=(A^2+B^2-2*q)/q",
            "representation_image": "(SU(2) x SU(2))/{(1,1),(-1,-1)} isomorphic to SO(4) in its standard four-dimensional representation",
            "semialgebraic_image": {
                "coefficient_map_fold_discriminant": "D=(y+2)^2-4*x^2",
                "criterion": "D>=0 and p=((y+2)+sqrt(D))/2, r=((y+2)-sqrt(D))/2 both lie in [0,4]",
                "forward_certificate": "p=u^2, r=v^2, x^2=p*r, y=p+r-2, D=(p-r)^2",
                "sufficiency": "given the criterion, choose real u,v with squares p,r and signs whose product is x",
                "not_the_full_quartic_discriminant": "D is the discriminant for reconstructing the unordered squared base traces p,r and detects the p=r fold; it is only one factor of the reciprocal quartic root discriminant",
            },
            "rank_warning": "SO(4) has two compact torus parameters; this is a full rank-two compact image, not the rank-one slices studied elsewhere",
        },
        "coefficient_map_fold_walls": {
            "A_equals_B": "P_tensor(T)=(1-q*T)^2*(1-(A^2-2*q)*T+q^2*T^2)",
            "A_equals_minus_B": "P_tensor(T)=(1+q*T)^2*(1+(A^2-2*q)*T+q^2*T^2)",
            "coefficient_geometry": "the two walls are p=r, equivalently D=0; their normalized images are the two sign branches x=+p and x=-p with y=2*p-2",
            "scope": "these A=+/-B masses measure the coefficient-map fold D=0 only; they are not labeled as exhaustive reciprocal-quartic repeated-root masses",
            "local_global_firewall": "A=+/-B is equality/opposition of one local trace. It does not prove that the two curves are isomorphic, quadratic twists, related by a global correspondence, or members of the same global automorphic representation",
        },
        "full_reciprocal_quartic_root_discriminant": {
            "quartic": "Q(Z)=Z^4-x*Z^3+y*Z^2-x*Z+1",
            "reciprocal_quadratic_factorization": "Q=(Z^2-s*Z+1)*(Z^2-t*Z+1), with s+t=x and s*t=y-2",
            "coefficient_map_fold_factor": "D=(y+2)^2-4*x^2=(p-r)^2=(s^2-4)*(t^2-4)",
            "hasse_endpoint_factor": "E=x^2-4*(y-2)=(s-t)^2=(p-4)*(r-4)",
            "full_identity": "Disc_Z(Q)=D*E^2=(p-r)^2*(p-4)^2*(r-4)^2",
            "repeated_root_locus": "D=0 or E=0; the second component is the additional Hasse-endpoint union p=4 or r=4",
            "intersection": "D=E=0 exactly at p=r=4, where the repeated-root multiplicity increases",
            "proof_routes": [
                "symbolic bivariate elimination in both (s,t) and (p,r), with all six residual polynomials identically zero",
                "direct 7-by-7 Sylvester resultant of Q and Q' at every one of the 645 frozen histogram atom pairs",
            ],
            "symbolic_residuals": {
                name: [
                    [first_exponent, second_exponent, coefficient]
                    for (
                        first_exponent,
                        second_exponent,
                    ), coefficient in sorted(residual.items())
                ]
                for name, residual in quartic_symbolic_certificates.items()
            },
            "normalization_firewall": "D alone is not called the full or exhaustive quartic discriminant; E^2 is load-bearing even though E never vanishes in the five frozen prime-field rows",
        },
        "compact_haar_trace_moments": {
            "orders_0_through_12": list(range(13)),
            "SO4_standard_trace": haar_moments,
            "formula": "E[(u*v)^(2*n)]=Catalan(n)^2 and every odd moment is zero",
            "reason": "under Haar on Spin(4)=SU(2)xSU(2), the two standard SU(2) traces are independent and each has Catalan even moments",
        },
        "compact_image_discriminator": {
            "orders_0_through_6": list(range(7)),
            "SO4_standard": haar_moments[:7],
            "Sym3_SU2": sym3_moments_through_six,
            "generic_USp4_standard": generic_usp4_moments_through_six,
            "first_trace_moment_separations": {
                "SO4_vs_Sym3_SU2": "the sequences alias through order 4 and first separate at order 6: 25 versus 34",
                "SO4_vs_generic_USp4": "the sequences first separate at order 4: 4 versus 3",
                "Sym3_SU2_vs_generic_USp4": "the sequences first separate at order 4: 4 versus 3",
            },
            "exact_derivations": {
                "SO4": "Catalan squares from two independent SU(2) standard traces",
                "Sym3_SU2": "Clebsch--Gordan recursion for the multiplicity of V_0 in V_3 tensor power n",
                "generic_USp4": "symplectic pair contractions through degree 4; at degree 6 the 15 contractions have the unique rank-four Pfaffian relation, leaving 14",
            },
            "coefficient_support_geometry": {
                "SO4": "two-dimensional semialgebraic region D>=0 with both quadratic roots p,r in [0,4]",
                "Sym3_SU2": "one-dimensional nodal curve -x^4+x^2*y+x^2+y^3-2*y^2=0, independently checked from x=t^3-2*t and y=t^4-3*t^2+2",
                "relation": "the Sym3 curve lies inside the same reciprocal degree-four compact coefficient region but carries a different Haar pushforward",
            },
            "symbolic_polynomial_certificates_in_z_equals_t_squared": {
                "curve_residual_coefficients_low_to_high": list(
                    sym3_polynomial_certificates["curve_residual"]
                ),
                "SO4_region_discriminant_coefficients_low_to_high": list(
                    sym3_polynomial_certificates["region_discriminant"]
                ),
                "factorization": "(z-1)^2*(z-4)^2",
            },
            "upstream_consumption": "no Sym3 fixture or producer is consumed or source-locked here; the displayed curve and moments are independently rederived by this producer",
            "scope_firewall": "moment and support geometry distinguish compact representation-image laws; they do not prove finite-family convergence, actual monodromy, automorphy, or global descent",
        },
        "all_q_low_moment_theorem": {
            "scope": "every odd prime power q, for two independent uniform marked-cubic models / normalized elliptic-stack draws",
            "base_inputs": {
                "m2=E[u^2]": "1-q^(-2)",
                "m4=E[u^4]": "2-3*q^(-2)-q^(-3)",
                "source": "locked W_2=q^2-1, W_4=2*q^3-3*q-1 and E_model[t^(2*n)]=W_(2*n)/q",
            },
            "formulas": {
                "E[x^2]": "(1-q^(-2))^2",
                "E[x^4]": "(2-3*q^(-2)-q^(-3))^2",
                "E[y]": "-2*q^(-2)",
                "E[y^2]": "2-2*q^(-2)-2*q^(-3)+2*q^(-4)",
                "E[x^2*y]": "2-6*q^(-2)-2*q^(-3)+4*q^(-4)+2*q^(-5)",
                "E[D]": "2-2*q^(-2)-2*q^(-3)-2*q^(-4), where D=(u^2-v^2)^2 is the coefficient-map fold discriminant, not the full quartic root discriminant",
            },
            "two_symbolic_routes": [
                "expand each observable using independence and the locked m2,m4",
                "compare against the separately expanded rational functions in q",
            ],
            "exact_prime_power_cross_checks": symbolic_cross_checks,
        },
        "frozen_histogram_cartesian_transforms": frozen,
        "literature_boundary": {
            "classical_primary_context": "Dinakar Ramakrishnan, Modularity of the Rankin-Selberg L-series, and multiplicity one for SL(2), Annals of Mathematics 152 (2000), arXiv:math/0007203, https://arxiv.org/abs/math/0007203",
            "dependency_status": "the finite-field local polynomial, coefficient image, and histogram calculations do not invoke the global automorphic theorem or silently extend its hypotheses",
            "not_claimed_novel": [
                "the GL(2) x GL(2) tensor-product local factor",
                "the Spin(4)=SU(2)xSU(2) description",
                "classical Rankin-Selberg or automorphic tensor-product theory",
            ],
            "project_specific_record_without_priority_claim": "the exact semialgebraic coefficient-region packaging, source-locked marked-cubic Cartesian laws, separately typed fold and full repeated-root masses, and explicit finite-q defects from SO(4) Haar",
            "novelty_status": "NO_LITERATURE_PRIORITY_CLAIM; the project-specific packaging is a candidate tool for later comparison and recognition work",
        },
        "resource_contract": {
            "atom_pair_cap_inclusive": guard.atom_pair_cap,
            "actual_total_source_histogram_atom_pairs": guard.atom_pairs,
            "maximum_per_field_atom_pairs": max(
                row["ordered_cartesian_atom_pairs"] for row in frozen
            ),
            "total_locked_source_trace_atoms": sum(
                row["source_trace_atom_count"] for row in frozen
            ),
            "exclusive_accounted_work_unit_cap": guard.work_cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total_work,
            },
            "unit_definition": "declared histogram-atom pairs and high-level exact identity checks; not literal CPU instructions or a wall-clock complexity claim",
            "field_curve_or_model_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "maximum_local_polynomial_degree": 4,
            "maximum_compact_moment_order": MAX_HAAR_MOMENT_ORDER,
        },
        "producer_and_source_locks": {
            "input_method": "locked JSON trace histograms followed only by ordered Cartesian histogram transforms",
            "no_field_curve_or_model_enumeration": True,
            "locks": _source_locks(),
        },
        "scope_firewall": {
            "no_actual_monodromy_upgrade": "the compact representation image is SO(4), but this packet does not prove that the arithmetic or geometric monodromy of any supplied curve-pair family is the full group",
            "no_local_to_global_curve_relation": "equal or opposite traces at one q do not identify curves, twists, isogenies, motives, or global L-functions",
            "no_automorphy_claim": "the classical global GL(2) x GL(2) theory is cited as a boundary, not reproved or broadened here",
            "no_measure_substitution": "the ordered product marked-model / normalized-stack measure is not relabeled as uniform coarse curve-pair measure",
            "no_finite_to_asymptotic_claim": "five exact finite histogram laws test all-q formulas but do not establish an empirical rate, a number-field family law, or equidistribution",
            "no_fold_to_full_discriminant_conflation": "D=(p-r)^2 controls reconstruction of p,r and the A=+/-B fold; D is not the full reciprocal-quartic discriminant, which is D*[x^2-4*(y-2)]^2 and also vanishes at p=4 or r=4",
            "no_novelty_claim": "classical representation theory is separated from project-specific coefficient and finite-family packaging, whose literature priority remains unchecked",
            "no_RH_or_GRH_claim": "local factors, finite-field moments, and compact signatures imply no new analytic continuation, zero-free region, RH, or GRH result",
        },
        "next_targets": [
            {
                "name": "linked_pair_corrections",
                "known": "independent Cartesian sampling makes every mixed trace moment factor into two genus-one moments",
                "open": "replace independence by an isogeny, shared cover, or geometric correspondence and identify the first exact covariance correction",
            },
            {
                "name": "wall_arithmetic",
                "known": "the D=0 coefficient-map folds have exact repeated-factor decompositions and separately typed frozen masses; the full quartic repeated-root locus also contains the Hasse-endpoint wall E=0",
                "open": "separate accidental local trace coincidences from systematic global twist, isogeny, or endoscopic subfamilies across many primes",
            },
            {
                "name": "SO4_recognition",
                "known": "the semialgebraic region is necessary and sufficient at the compact coefficient level",
                "open": "add determinant, integrality, ramification, compatibility, and cross-prime conditions for an arithmetic or global recognition theorem",
            },
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def _write(path: Path) -> None:
    path.write_text(
        json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {path}")


def _check(path: Path) -> None:
    expected = build_fixture()
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit(f"fixture is stale: {path}")
    print(f"fixture is current: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    action.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    arguments = parser.parse_args()
    if arguments.write is not None:
        _write(arguments.write)
    elif arguments.check is not None:
        _check(arguments.check)
    else:
        print(json.dumps(build_fixture(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
