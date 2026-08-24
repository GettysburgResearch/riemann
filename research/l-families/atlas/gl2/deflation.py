"""Exact finite GL(2) central-zero deflation algebra.

This module is deliberately data-free.  It works over :class:`fractions.Fraction`
and supplies synthetic controls for the parity/rank bookkeeping requested by the
L-family detector atlas.  It does *not* evaluate an L-function.

Write the completed function in the centered variable as

    Lambda(z) = z**r G(z),       F_Lambda = Lambda'/Lambda = r/z + F_G.

For positive rational nodes ``x_i`` we keep two kernel conventions separate:

``loewner_difference``
    L_F(x,y) = (F(x)-F(y))/(x-y), with the derivative on the diagonal.
    The central atom is ``-r/(xy)``.

``pick_sum``
    H_F(x,y) = (F(x)+F(y))/(x+y).  This is the sum/Hankel convention used
    in the integrated actual-Xi Pick packet.  The central atom is ``+r/(xy)``.

Thus the two atoms have opposite signs, although both are rank one.  Calling
either one simply "the Pick matrix" without its convention is unsafe.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, NamedTuple, Sequence


LOEWNER_DIFFERENCE = "loewner_difference"
PICK_SUM = "pick_sum"
CONVENTIONS = (LOEWNER_DIFFERENCE, PICK_SUM)

Scalar = Fraction
Matrix = list[list[Scalar]]


class Inertia(NamedTuple):
    """Sylvester inertia ``(positive, negative, zero)``."""

    positive: int
    negative: int
    zero: int


@dataclass(frozen=True)
class DeflationPacket:
    """Raw, parity-deflated, and fully deflated exact matrices."""

    convention: str
    root_number: int
    central_order: int
    forced_order: int
    nodes: tuple[Scalar, ...]
    background: Matrix
    raw: Matrix
    parity_deflated: Matrix
    fully_deflated: Matrix

    @property
    def excess_order(self) -> int:
        return self.central_order - self.forced_order


def exact(value: int | str | Fraction) -> Fraction:
    """Convert an integer, rational string, or Fraction without float input."""

    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("booleans are not exact scalar inputs")
    if isinstance(value, (int, str)):
        return Fraction(value)
    raise TypeError("use int, rational string, or Fraction; floats are forbidden")


def exact_nodes(values: Iterable[int | str | Fraction]) -> tuple[Fraction, ...]:
    """Return a nonempty packet of positive off-center rational nodes."""

    nodes = tuple(exact(value) for value in values)
    if not nodes:
        raise ValueError("the node packet must be nonempty")
    if any(node <= 0 for node in nodes):
        raise ValueError("this pilot uses only positive centered nodes x_i > 0")
    return nodes


def _validate_convention(convention: str) -> None:
    if convention not in CONVENTIONS:
        raise ValueError(f"unknown kernel convention: {convention!r}")


def forced_order(root_number: int) -> int:
    """Return only the vanishing forced by the functional-equation sign."""

    if root_number not in (-1, 1):
        raise ValueError("root_number must be +1 or -1")
    return 0 if root_number == 1 else 1


def validate_parity(root_number: int, central_order: int) -> None:
    """Check ``(-1)**central_order == root_number`` and nonnegativity."""

    if not isinstance(central_order, int) or isinstance(central_order, bool):
        raise TypeError("central_order must be an integer")
    if central_order < 0:
        raise ValueError("central_order must be nonnegative")
    expected = 1 if central_order % 2 == 0 else -1
    if forced_order(root_number) != central_order % 2 or expected != root_number:
        raise ValueError(
            "central-order parity is incompatible with the root number"
        )


def zero_matrix(size: int) -> Matrix:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def identity_matrix(size: int) -> Matrix:
    return [
        [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]


def _coerce_square(matrix: Sequence[Sequence[int | str | Fraction]]) -> Matrix:
    result = [[exact(entry) for entry in row] for row in matrix]
    size = len(result)
    if any(len(row) != size for row in result):
        raise ValueError("matrix must be square")
    return result


def _assert_symmetric(matrix: Matrix) -> None:
    size = len(matrix)
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(i)):
        raise ValueError("inertia is defined here only for symmetric matrices")


def add(left: Sequence[Sequence[Scalar]], right: Sequence[Sequence[Scalar]]) -> Matrix:
    a = _coerce_square(left)
    b = _coerce_square(right)
    if len(a) != len(b):
        raise ValueError("matrix dimensions differ")
    return [
        [a[i][j] + b[i][j] for j in range(len(a))]
        for i in range(len(a))
    ]


def subtract(
    left: Sequence[Sequence[Scalar]], right: Sequence[Sequence[Scalar]]
) -> Matrix:
    a = _coerce_square(left)
    b = _coerce_square(right)
    if len(a) != len(b):
        raise ValueError("matrix dimensions differ")
    return [
        [a[i][j] - b[i][j] for j in range(len(a))]
        for i in range(len(a))
    ]


def central_atom(
    nodes: Iterable[int | str | Fraction], central_order: int, convention: str
) -> Matrix:
    """Return the exact rank-one matrix contributed by ``central_order/z``."""

    xs = exact_nodes(nodes)
    if not isinstance(central_order, int) or isinstance(central_order, bool):
        raise TypeError("central_order must be an integer")
    if central_order < 0:
        raise ValueError("central_order must be nonnegative")
    _validate_convention(convention)
    sign = -1 if convention == LOEWNER_DIFFERENCE else 1
    return [
        [Fraction(sign * central_order, 1) / (x * y) for y in xs]
        for x in xs
    ]


def synthetic_background(
    nodes: Iterable[int | str | Fraction],
    c: int | str | Fraction,
    d: int | str | Fraction,
    convention: str,
) -> Matrix:
    """Kernel of a labeled synthetic even entire nonzero factor.

    The control is

        G(z) = exp(c*z**2/2 + d*z**4/4),
        F_G(z) = c*z + d*z**3.

    Only the rational kernel formulas are evaluated; no transcendental values
    are needed.  This is an algebra control, not arithmetic L-function data.
    """

    xs = exact_nodes(nodes)
    c_q = exact(c)
    d_q = exact(d)
    _validate_convention(convention)
    if convention == LOEWNER_DIFFERENCE:
        return [
            [c_q + d_q * (x * x + x * y + y * y) for y in xs]
            for x in xs
        ]
    return [
        [c_q + d_q * (x * x - x * y + y * y) for y in xs]
        for x in xs
    ]


def make_packet(
    *,
    nodes: Iterable[int | str | Fraction],
    root_number: int,
    central_order: int,
    c: int | str | Fraction,
    d: int | str | Fraction,
    convention: str,
) -> DeflationPacket:
    """Build all three matrices for one exact synthetic parity/rank control."""

    xs = exact_nodes(nodes)
    validate_parity(root_number, central_order)
    background = synthetic_background(xs, c, d, convention)
    forced = forced_order(root_number)
    raw = add(background, central_atom(xs, central_order, convention))
    parity_deflated = subtract(raw, central_atom(xs, forced, convention))
    fully_deflated = subtract(raw, central_atom(xs, central_order, convention))
    return DeflationPacket(
        convention=convention,
        root_number=root_number,
        central_order=central_order,
        forced_order=forced,
        nodes=xs,
        background=background,
        raw=raw,
        parity_deflated=parity_deflated,
        fully_deflated=fully_deflated,
    )


def determinant(matrix: Sequence[Sequence[int | str | Fraction]]) -> Fraction:
    """Exact determinant by fraction-preserving Gaussian elimination."""

    work = _coerce_square(matrix)
    size = len(work)
    result = Fraction(1)
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            result = -result
        pivot = work[column][column]
        result *= pivot
        for row in range(column + 1, size):
            if not work[row][column]:
                continue
            factor = work[row][column] / pivot
            for entry in range(column + 1, size):
                work[row][entry] -= factor * work[column][entry]
            work[row][column] = Fraction(0)
    return result


def rank(matrix: Sequence[Sequence[int | str | Fraction]]) -> int:
    """Exact row rank over the rationals."""

    work = [[exact(entry) for entry in row] for row in matrix]
    if not work:
        return 0
    width = len(work[0])
    if any(len(row) != width for row in work):
        raise ValueError("matrix rows have unequal lengths")
    pivot_row = 0
    for column in range(width):
        candidate = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if candidate is None:
            continue
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [entry / pivot for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[pivot_row][entry]
                for entry in range(width)
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def _symmetric_permute(matrix: Matrix, order: Sequence[int]) -> Matrix:
    return [[matrix[i][j] for j in order] for i in order]


def inertia(matrix: Sequence[Sequence[int | str | Fraction]]) -> Inertia:
    """Compute exact symmetric inertia by rational congruence elimination.

    Nonzero diagonal pivots use a one-dimensional Schur complement.  If every
    remaining diagonal is zero but an off-diagonal entry is nonzero, a block
    ``[[0,b],[b,0]]`` supplies one positive and one negative direction.  This
    avoids floating-point eigenvalue thresholds.
    """

    work = _coerce_square(matrix)
    _assert_symmetric(work)
    positive = negative = zero = 0
    while work:
        size = len(work)
        diagonal = next((index for index in range(size) if work[index][index]), None)
        if diagonal is not None:
            order = [diagonal] + [index for index in range(size) if index != diagonal]
            work = _symmetric_permute(work, order)
            pivot = work[0][0]
            if pivot > 0:
                positive += 1
            else:
                negative += 1
            work = [
                [
                    work[i][j] - work[i][0] * work[0][j] / pivot
                    for j in range(1, size)
                ]
                for i in range(1, size)
            ]
            continue

        off_diagonal = next(
            (
                (i, j)
                for i in range(size)
                for j in range(i + 1, size)
                if work[i][j]
            ),
            None,
        )
        if off_diagonal is None:
            zero += size
            break
        first, second = off_diagonal
        order = [first, second] + [
            index for index in range(size) if index not in (first, second)
        ]
        work = _symmetric_permute(work, order)
        pivot = work[0][1]
        positive += 1
        negative += 1
        work = [
            [
                work[i][j]
                - (work[i][0] * work[1][j] + work[i][1] * work[0][j])
                / pivot
                for j in range(2, size)
            ]
            for i in range(2, size)
        ]
    return Inertia(positive, negative, zero)


def frobenius_norm_squared(
    matrix: Sequence[Sequence[int | str | Fraction]],
) -> Fraction:
    entries = [[exact(entry) for entry in row] for row in matrix]
    return sum((entry * entry for row in entries for entry in row), Fraction(0))


def correction_norm_squared(
    nodes: Iterable[int | str | Fraction], multiplicity: int
) -> Fraction:
    """Closed form ``m^2 (sum_i x_i^-2)^2`` for either atom convention."""

    xs = exact_nodes(nodes)
    if not isinstance(multiplicity, int) or isinstance(multiplicity, bool):
        raise TypeError("multiplicity must be an integer")
    if multiplicity < 0:
        raise ValueError("multiplicity must be nonnegative")
    reciprocal_square_sum = sum((1 / (x * x) for x in xs), Fraction(0))
    return multiplicity * multiplicity * reciprocal_square_sum**2


def determinant_affine_prediction(
    background: Sequence[Sequence[int | str | Fraction]],
    nodes: Iterable[int | str | Fraction],
    multiplicity: int,
    convention: str,
) -> Fraction:
    """Predict ``det(B + atom(m))`` from the rank-one affine determinant law."""

    base = _coerce_square(background)
    xs = exact_nodes(nodes)
    if len(base) != len(xs):
        raise ValueError("background dimension and node count differ")
    if not isinstance(multiplicity, int) or isinstance(multiplicity, bool):
        raise TypeError("multiplicity must be an integer")
    if multiplicity < 0:
        raise ValueError("multiplicity must be nonnegative")
    det_zero = determinant(base)
    det_one = determinant(add(base, central_atom(xs, 1, convention)))
    return det_zero + multiplicity * (det_one - det_zero)


def matrix_summary(matrix: Sequence[Sequence[int | str | Fraction]]) -> dict[str, object]:
    """Small JSON-friendly exact matrix summary."""

    exact_matrix = _coerce_square(matrix)
    signature = inertia(exact_matrix)
    return {
        "determinant": str(determinant(exact_matrix)),
        "rank": rank(exact_matrix),
        "inertia": {
            "positive": signature.positive,
            "negative": signature.negative,
            "zero": signature.zero,
        },
    }
