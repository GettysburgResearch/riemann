#!/usr/bin/env python3
"""Exact finite checks for the invariant order-product and Toeplitz duality.

The script uses only Python's standard library and exact rational arithmetic.
It authenticates algebraic identities and finite controls only.  It does not
prove the analytic infinite products, the theta-mixture theorem, the
all-order E-Widder inequality, or the Riemann Hypothesis.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Iterable, Sequence


class QComplex:
    """Gaussian rational number."""

    __slots__ = ("re", "im")

    def __init__(self, re: object = 0, im: object = 0) -> None:
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, other: object) -> "QComplex":
        rhs = qcomplex(other)
        return QComplex(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "QComplex":
        return QComplex(-self.re, -self.im)

    def __sub__(self, other: object) -> "QComplex":
        return self + (-qcomplex(other))

    def __rsub__(self, other: object) -> "QComplex":
        return qcomplex(other) - self

    def __mul__(self, other: object) -> "QComplex":
        rhs = qcomplex(other)
        return QComplex(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "QComplex":
        return QComplex(self.re, -self.im)

    def norm_squared(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def inverse(self) -> "QComplex":
        norm = self.norm_squared()
        if norm == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return QComplex(self.re / norm, -self.im / norm)

    def __truediv__(self, other: object) -> "QComplex":
        return self * qcomplex(other).inverse()

    def __rtruediv__(self, other: object) -> "QComplex":
        return qcomplex(other) / self

    def __pow__(self, exponent: int) -> "QComplex":
        if not isinstance(exponent, int):
            raise TypeError("integer exponent required")
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = QComplex(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def __eq__(self, other: object) -> bool:
        rhs = qcomplex(other)
        return self.re == rhs.re and self.im == rhs.im

    def __repr__(self) -> str:
        return f"QComplex({self.re!r}, {self.im!r})"


def qcomplex(value: object) -> QComplex:
    return value if isinstance(value, QComplex) else QComplex(value)


def polynomial_value(coefficients: Sequence[object], z: QComplex) -> QComplex:
    result = QComplex(0)
    for coefficient in reversed(coefficients):
        result = result * z + coefficient
    return result


def finite_canonical_product(atoms: Iterable[QComplex], z: object) -> QComplex:
    value = QComplex(1)
    point = qcomplex(z)
    for atom in atoms:
        value *= 1 + point / atom
    return value


def determinant_fraction(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    """Bareiss fraction-free determinant over Q."""

    size = len(matrix)
    if size == 0:
        return Fraction(1)
    work = [[Fraction(entry) for entry in row] for row in matrix]
    sign = 1
    previous_pivot = Fraction(1)
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign *= -1
        pivot = work[column][column]
        for row in range(column + 1, size):
            for next_column in range(column + 1, size):
                work[row][next_column] = (
                    work[row][next_column] * pivot
                    - work[row][column] * work[column][next_column]
                ) / previous_pivot
        previous_pivot = pivot
        for row in range(column + 1, size):
            work[row][column] = Fraction(0)
    return sign * work[-1][-1]


def reciprocal_coefficients(
    coefficients: Sequence[Fraction], order: int
) -> list[Fraction]:
    """Coefficients of B(z)=1/A(-z), with A(0)=1."""

    signed = [Fraction(0) for _ in range(order + 1)]
    for index in range(min(len(coefficients), order + 1)):
        signed[index] = Fraction(coefficients[index]) * (-1 if index & 1 else 1)
    if signed[0] == 0:
        raise ValueError("nonzero constant coefficient required")
    reciprocal = [Fraction(0) for _ in range(order + 1)]
    reciprocal[0] = 1 / signed[0]
    for index in range(1, order + 1):
        reciprocal[index] = -sum(
            signed[j] * reciprocal[index - j] for j in range(1, index + 1)
        ) / signed[0]
    return reciprocal


def toeplitz_rectangle(
    coefficients: Sequence[Fraction], size: int, shift: int
) -> Fraction:
    def entry(index: int) -> Fraction:
        if index < 0 or index >= len(coefficients):
            return Fraction(0)
        return Fraction(coefficients[index])

    return determinant_fraction(
        [[entry(shift + j - i) for j in range(size)] for i in range(size)]
    )


def translated_coefficients(
    coefficients: Sequence[Fraction], scale: Fraction, shift: Fraction
) -> list[Fraction]:
    """Coefficients of G(shift+scale*u) for a finite polynomial G."""

    maximum = len(coefficients) - 1
    return [
        scale**n
        * sum(
            Fraction(coefficients[m]) * comb(m, n) * shift ** (m - n)
            for m in range(n, maximum + 1)
        )
        for n in range(maximum + 1)
    ]


def check_cross_ratio() -> int:
    checks = 0
    panels = [
        (
            Fraction(5, 3),
            QComplex(Fraction(3, 5), Fraction(4, 5)),
            QComplex(Fraction(3, 2), Fraction(2, 5)),
        ),
        (
            Fraction(7, 4),
            QComplex(Fraction(5, 13), Fraction(12, 13)),
            QComplex(Fraction(9, 7), Fraction(-3, 8)),
        ),
        (
            Fraction(11, 6),
            QComplex(Fraction(-7, 25), Fraction(24, 25)),
            QComplex(Fraction(4, 3), Fraction(5, 11)),
        ),
        (
            Fraction(13, 9),
            QComplex(Fraction(20, 29), Fraction(-21, 29)),
            QComplex(Fraction(17, 5), Fraction(1, 6)),
        ),
    ]
    for u, r, atom in panels:
        w = -(r - 1) ** 2 / (4 * r)
        transformed = 4 * u * atom / (u + atom) ** 2
        left = 1 - w * transformed
        right = (atom + u * r) * (atom + u / r) / (atom + u) ** 2
        if left != right:
            raise AssertionError(("cross_ratio", u, r, atom, left, right))
        checks += 1
    return checks


def check_finite_product() -> int:
    checks = 0
    atom_sets = [
        [
            QComplex(Fraction(3, 2), Fraction(2, 5)),
            QComplex(Fraction(3, 2), Fraction(-2, 5)),
            QComplex(7),
        ],
        [
            QComplex(Fraction(9, 7), Fraction(3, 11)),
            QComplex(Fraction(9, 7), Fraction(-3, 11)),
            QComplex(Fraction(5, 2)),
            QComplex(11),
        ],
        [QComplex(Fraction(4, 3)), QComplex(Fraction(13, 4)), QComplex(Fraction(17, 6))],
    ]
    panels = [
        (Fraction(5, 3), QComplex(Fraction(3, 5), Fraction(4, 5))),
        (Fraction(7, 5), QComplex(Fraction(5, 13), Fraction(12, 13))),
        (Fraction(11, 8), QComplex(Fraction(-7, 25), Fraction(24, 25))),
    ]
    for atoms in atom_sets:
        for u, r in panels:
            w = -(r - 1) ** 2 / (4 * r)
            left = QComplex(1)
            for atom in atoms:
                transformed = 4 * u * atom / (u + atom) ** 2
                left *= 1 - w * transformed
            right = (
                finite_canonical_product(atoms, u * r)
                * finite_canonical_product(atoms, u / r)
                / finite_canonical_product(atoms, u) ** 2
            )
            if left != right:
                raise AssertionError(("finite_product", atoms, u, r, left, right))
            checks += 1
    return checks


def check_matching_poles() -> int:
    checks = 0
    panels = [
        (QComplex(Fraction(3, 5), Fraction(4, 5)), Fraction(4, 5), Fraction(5, 4)),
        (QComplex(Fraction(5, 13), Fraction(12, 13)), Fraction(9, 13), Fraction(13, 9)),
        (QComplex(Fraction(7, 25), Fraction(24, 25)), Fraction(16, 25), Fraction(25, 16)),
    ]
    for atom, expected_w, expected_lambda in panels:
        u = Fraction(1)  # all selected atoms have modulus one
        transformed = 4 * u * atom / (u + atom) ** 2
        if transformed != expected_lambda:
            raise AssertionError(("matching_lambda", atom, transformed, expected_lambda))
        if 1 - expected_w * transformed != 0:
            raise AssertionError(("matching_zero", atom, expected_w, transformed))
        r = -atom
        w = -(r - 1) ** 2 / (4 * r)
        if w != expected_w:
            raise AssertionError(("matching_parameter", atom, w, expected_w))
        checks += 3
    return checks


def check_radial_modulus() -> int:
    checks = 0
    coefficient_sets = [
        [1, 2, 3, 5, 8, 13],
        [2, 1, 4, 1, 5, 9, 2],
        [3, 7, 11, 13, 17],
    ]
    unit_points = [
        QComplex(Fraction(3, 5), Fraction(4, 5)),
        QComplex(Fraction(5, 13), Fraction(12, 13)),
        QComplex(Fraction(-7, 25), Fraction(24, 25)),
    ]
    for coefficients in coefficient_sets:
        for u in [Fraction(1, 3), Fraction(4, 5), Fraction(7, 3)]:
            positive_axis = sum(
                Fraction(coefficient) * u**index
                for index, coefficient in enumerate(coefficients)
            )
            for point in unit_points:
                radial = polynomial_value(coefficients, u * point)
                if radial.norm_squared() > positive_axis * positive_axis:
                    raise AssertionError(
                        (
                            "radial_modulus",
                            coefficients,
                            u,
                            point,
                            radial.norm_squared(),
                            positive_axis * positive_axis,
                        )
                    )
                checks += 1
    return checks


def check_reciprocal_duality() -> int:
    checks = 0
    sequences = [
        [1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29],
        [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786],
        [
            1,
            Fraction(3, 2),
            Fraction(7, 3),
            Fraction(11, 4),
            Fraction(13, 5),
            Fraction(17, 6),
            Fraction(19, 7),
            Fraction(23, 8),
            Fraction(29, 9),
            Fraction(31, 10),
            Fraction(37, 11),
            Fraction(41, 12),
        ],
    ]
    for sequence in sequences:
        reciprocal = reciprocal_coefficients(sequence, 24)
        for size in range(1, 7):
            for shift in range(1, 7):
                left = toeplitz_rectangle(sequence, size, shift)
                right = toeplitz_rectangle(reciprocal, shift, size)
                if left != right:
                    raise AssertionError(
                        ("reciprocal_rectangle", size, shift, left, right)
                    )
                checks += 1
    return checks


def check_affine_translation() -> int:
    checks = 0
    coefficient_sets = [
        [1, 2, 3, 5, 7, 11],
        [
            Fraction(1, 8),
            Fraction(3, 5),
            Fraction(7, 9),
            Fraction(11, 13),
            Fraction(17, 19),
        ],
    ]
    for coefficients in coefficient_sets:
        translated = translated_coefficients(coefficients, Fraction(4), Fraction(1))
        for u in [Fraction(-1, 7), Fraction(2, 9), Fraction(5, 4)]:
            left = sum(translated[n] * u**n for n in range(len(translated)))
            right = sum(
                Fraction(coefficients[m]) * (1 + 4 * u) ** m
                for m in range(len(coefficients))
            )
            if left != right:
                raise AssertionError(("affine_translation", coefficients, u, left, right))
            checks += 1
        if not all(coefficient > 0 for coefficient in translated):
            raise AssertionError(("translated_positivity", coefficients, translated))
        checks += 1
    return checks


def check_bernoulli_string() -> int:
    checks = 0
    panels = [
        (Fraction(2, 3), [Fraction(1, 4), Fraction(5, 3), Fraction(17, 5)]),
        (
            Fraction(7, 5),
            [Fraction(3, 8), Fraction(11, 6), Fraction(23, 7), Fraction(31, 9)],
        ),
    ]
    for v, spectral_points in panels:
        probabilities = [v / (v + point) for point in spectral_points]
        for z in [Fraction(0), Fraction(1, 3), Fraction(1), Fraction(5, 4)]:
            normalized_product = Fraction(1)
            bernoulli_product = Fraction(1)
            for point, probability in zip(spectral_points, probabilities):
                normalized_product *= (1 + v * z / point) / (1 + v / point)
                bernoulli_product *= 1 - probability + probability * z
            if normalized_product != bernoulli_product:
                raise AssertionError(
                    (
                        "bernoulli_string",
                        v,
                        spectral_points,
                        z,
                        normalized_product,
                        bernoulli_product,
                    )
                )
            checks += 1
    return checks


def main() -> None:
    counts = {
        "cross_ratio": check_cross_ratio(),
        "finite_product": check_finite_product(),
        "matching_poles": check_matching_poles(),
        "radial_modulus": check_radial_modulus(),
        "reciprocal_duality": check_reciprocal_duality(),
        "affine_translation": check_affine_translation(),
        "bernoulli_string": check_bernoulli_string(),
    }
    print("PASS_ARCHITECTURE_E_ORDER_PRODUCT_AND_RECIPROCAL")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
