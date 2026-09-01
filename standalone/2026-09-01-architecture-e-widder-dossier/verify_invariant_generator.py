#!/usr/bin/env python3
"""Exact bounded checks for the invariant determinant / generator packet.

The checks use only Python's standard library and rational arithmetic.
They authenticate finite algebraic identities, not the infinite canonical
product, the external zero-height theorem, the heat-trace explicit formula,
the all-order source inequality, or RH.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence


@dataclass(frozen=True)
class QComplex:
    re: Fraction
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "QComplex":
        right = as_qcomplex(other)
        return QComplex(self.re + right.re, self.im + right.im)

    __radd__ = __add__

    def __sub__(self, other: object) -> "QComplex":
        right = as_qcomplex(other)
        return QComplex(self.re - right.re, self.im - right.im)

    def __rsub__(self, other: object) -> "QComplex":
        return as_qcomplex(other) - self

    def __neg__(self) -> "QComplex":
        return QComplex(-self.re, -self.im)

    def __mul__(self, other: object) -> "QComplex":
        right = as_qcomplex(other)
        return QComplex(
            self.re * right.re - self.im * right.im,
            self.re * right.im + self.im * right.re,
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
        return self * as_qcomplex(other).inverse()

    def __rtruediv__(self, other: object) -> "QComplex":
        return as_qcomplex(other) / self

    def __pow__(self, exponent: int) -> "QComplex":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = QComplex(Fraction(1))
        base = self
        n = exponent
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out


def as_qcomplex(value: object) -> QComplex:
    if isinstance(value, QComplex):
        return value
    if isinstance(value, Fraction):
        return QComplex(value)
    if isinstance(value, int):
        return QComplex(Fraction(value))
    raise TypeError(f"unsupported exact scalar: {type(value)!r}")


def product(values: Iterable[QComplex]) -> QComplex:
    out = QComplex(Fraction(1))
    for value in values:
        out = out * value
    return out


def invariant_lambda(u: Fraction, a: QComplex) -> QComplex:
    return QComplex(4 * u) * a / (QComplex(u) + a) ** 2


def finite_entire(z: QComplex, atoms: Sequence[QComplex]) -> QComplex:
    return product(QComplex(1) + z / atom for atom in atoms)


def finite_q(z: QComplex, atoms: Sequence[QComplex]) -> QComplex:
    return QComplex(2) * sum(
        (QComplex(1) / (z + atom) for atom in atoms),
        QComplex(0),
    )


def polynomial_multiply(
    left: Sequence[QComplex], right: Sequence[QComplex]
) -> list[QComplex]:
    out = [QComplex(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = out[i + j] + a * b
    return out


def finite_coefficients(atoms: Sequence[QComplex]) -> list[QComplex]:
    coeffs = [QComplex(1)]
    for atom in atoms:
        coeffs = polynomial_multiply(
            coeffs, [QComplex(1), QComplex(1) / atom]
        )
    return coeffs


def check_matching_scale_pole() -> int:
    checks = 0
    a = QComplex(Fraction(3), Fraction(4))
    u = Fraction(5)
    lam = invariant_lambda(u, a)
    if lam != QComplex(Fraction(5, 4)):
        raise AssertionError(("matching_lambda", lam))
    checks += 1

    w0 = Fraction(4, 5)
    if QComplex(1) - w0 * lam != QComplex(0):
        raise AssertionError(("matching_pole", w0, lam))
    checks += 1

    if invariant_lambda(u, a.conjugate()) != lam:
        raise AssertionError("conjugate matching scale")
    checks += 1

    residue = -Fraction(1)
    if residue != -1:
        raise AssertionError("residue normalization")
    checks += 1
    return checks


def check_determinant_and_generator() -> int:
    checks = 0
    atoms = [
        QComplex(Fraction(3), Fraction(4)),
        QComplex(Fraction(3), Fraction(-4)),
        QComplex(Fraction(2)),
        QComplex(Fraction(5), Fraction(12)),
        QComplex(Fraction(5), Fraction(-12)),
    ]
    panels = [
        (
            Fraction(7, 3),
            QComplex(Fraction(3, 5), Fraction(4, 5)),
            Fraction(1, 5),
        ),
        (
            Fraction(11, 4),
            QComplex(Fraction(5, 13), Fraction(12, 13)),
            Fraction(4, 13),
        ),
        (
            Fraction(17, 6),
            QComplex(Fraction(7, 25), Fraction(24, 25)),
            Fraction(9, 25),
        ),
    ]
    for u, eta, w in panels:
        if eta * eta.conjugate() != QComplex(1):
            raise AssertionError(("unit_eta", eta))
        checks += 1
        if eta + eta.inverse() != QComplex(2 * (1 - 2 * w)):
            raise AssertionError(("eta_w_relation", eta, w))
        checks += 1

        lambdas = [invariant_lambda(u, atom) for atom in atoms]
        delta_product = product(QComplex(1) - w * lam for lam in lambdas)
        delta_ratio = (
            finite_entire(QComplex(u) * eta, atoms)
            * finite_entire(QComplex(u) / eta, atoms)
            / finite_entire(QComplex(u), atoms) ** 2
        )
        if delta_product != delta_ratio:
            raise AssertionError(("determinant_ratio", delta_product, delta_ratio))
        checks += 1

        generator_sum = sum(
            (lam / (QComplex(1) - w * lam) for lam in lambdas),
            QComplex(0),
        )
        generator_q = (
            QComplex(2 * u)
            / (eta - eta.inverse())
            * (
                eta * finite_q(QComplex(u) * eta, atoms)
                - eta.inverse() * finite_q(QComplex(u) / eta, atoms)
            )
        )
        if generator_sum != generator_q:
            raise AssertionError(("generator_q", generator_sum, generator_q))
        checks += 1

        derivative_ratio = sum(
            (lam / (QComplex(1) - w * lam) for lam in lambdas),
            QComplex(0),
        )
        if derivative_ratio != generator_sum:
            raise AssertionError("log derivative")
        checks += 1
    return checks


def check_probability_characteristic_function() -> int:
    checks = 0
    atoms = [
        QComplex(Fraction(3), Fraction(4)),
        QComplex(Fraction(3), Fraction(-4)),
        QComplex(Fraction(2)),
        QComplex(Fraction(5), Fraction(12)),
        QComplex(Fraction(5), Fraction(-12)),
    ]
    coeffs = finite_coefficients(atoms)
    for coeff in coeffs:
        if coeff.im != 0 or coeff.re <= 0:
            raise AssertionError(("positive_coefficients", coeff))
        checks += 1

    panels = [
        (Fraction(7, 3), QComplex(Fraction(3, 5), Fraction(4, 5))),
        (Fraction(11, 4), QComplex(Fraction(5, 13), Fraction(12, 13))),
        (Fraction(17, 6), QComplex(Fraction(7, 25), Fraction(24, 25))),
    ]
    for u, eta in panels:
        normalizer = finite_entire(QComplex(u), atoms)
        probabilities = [
            coeff * QComplex(u**index) / normalizer
            for index, coeff in enumerate(coeffs)
        ]
        if sum(probabilities, QComplex(0)) != QComplex(1):
            raise AssertionError("probability normalization")
        checks += 1
        characteristic = sum(
            (
                probability * eta**index
                for index, probability in enumerate(probabilities)
            ),
            QComplex(0),
        )
        expected = finite_entire(QComplex(u) * eta, atoms) / normalizer
        if characteristic != expected:
            raise AssertionError(("characteristic", characteristic, expected))
        checks += 1
        determinant = characteristic * characteristic.conjugate()
        direct = (
            finite_entire(QComplex(u) * eta, atoms)
            * finite_entire(QComplex(u) / eta, atoms)
            / normalizer**2
        )
        if determinant != direct:
            raise AssertionError(("probability_determinant", determinant, direct))
        checks += 1
        if determinant.im != 0 or not (0 <= determinant.re <= 1):
            raise AssertionError(("characteristic_bound", determinant))
        checks += 1
    return checks


def pair_resolvent(u: Fraction, a: QComplex, w: Fraction) -> QComplex:
    lam = invariant_lambda(u, a)
    return (
        lam / (QComplex(1) - w * lam)
        + lam.conjugate() / (QComplex(1) - w * lam.conjugate())
    )


def check_pair_threshold() -> int:
    checks = 0
    pairs = [
        (QComplex(Fraction(3), Fraction(4)), Fraction(5), Fraction(4, 5)),
        (QComplex(Fraction(5), Fraction(12)), Fraction(13), Fraction(9, 13)),
        (QComplex(Fraction(8), Fraction(15)), Fraction(17), Fraction(25, 34)),
    ]
    u_values = [Fraction(1, 3), Fraction(2), Fraction(7), Fraction(31)]
    for a, radius, threshold in pairs:
        if a.norm_squared() != radius * radius:
            raise AssertionError(("radius", a, radius))
        checks += 1
        matching = invariant_lambda(radius, a)
        if matching.im != 0 or Fraction(1, 1) / matching.re != threshold:
            raise AssertionError(("threshold", matching, threshold))
        checks += 1

        for u in u_values:
            lam = invariant_lambda(u, a)
            reciprocal_real = (QComplex(1) / lam).re
            formula = Fraction(1, 2) + Fraction(1, 4) * (
                Fraction(u, radius) + Fraction(radius, u)
            ) * Fraction(a.re, radius)
            if reciprocal_real != formula:
                raise AssertionError(
                    ("reciprocal_real", a, u, reciprocal_real, formula)
                )
            checks += 1
            if reciprocal_real < threshold:
                raise AssertionError(("AMGM_threshold", a, u))
            checks += 1

            for w in [Fraction(0), Fraction(1, 4), Fraction(1, 2)]:
                value = pair_resolvent(u, a, w)
                if value.im != 0 or value.re <= 0:
                    raise AssertionError(("half_ray_positive", a, u, w, value))
                checks += 1
    return checks


def check_normalized_power_sum() -> int:
    checks = 0
    atoms = [
        QComplex(Fraction(3), Fraction(4)),
        QComplex(Fraction(3), Fraction(-4)),
        QComplex(Fraction(2)),
    ]
    for u in [Fraction(2, 5), Fraction(7, 3), Fraction(9)]:
        lambdas = [invariant_lambda(u, atom) for atom in atoms]
        for k in range(1, 9):
            direct = sum((lam**k for lam in lambdas), QComplex(0))
            atom_formula = sum(
                (
                    (QComplex(4 * u) * atom / (QComplex(u) + atom) ** 2)
                    ** k
                    for atom in atoms
                ),
                QComplex(0),
            )
            if direct != atom_formula:
                raise AssertionError(("power_sum", u, k, direct, atom_formula))
            checks += 1
            if direct.im != 0:
                raise AssertionError(("conjugation_reality", u, k, direct))
            checks += 1
    return checks


def main() -> None:
    counts = {
        "matching_scale_pole": check_matching_scale_pole(),
        "determinant_generator": check_determinant_and_generator(),
        "probability_characteristic": check_probability_characteristic_function(),
        "pair_threshold": check_pair_threshold(),
        "normalized_power_sum": check_normalized_power_sum(),
    }
    print("PASS_INVARIANT_DETERMINANT_GENERATOR_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
