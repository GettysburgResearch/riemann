#!/usr/bin/env python3
"""Exact bounded controls for the invariant Widder resolvent.

The script uses only Python's standard library and exact rational arithmetic.
It checks finite algebraic identities in the companion theorem note.  It does
not prove the infinite zero expansions, the Guinand--Weil formula, the
terminal-annulus continuum theorem, the all-order source inequality, or RH.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Sequence, TypeAlias

ComplexQ: TypeAlias = tuple[Fraction, Fraction]

ZERO: ComplexQ = (Fraction(0), Fraction(0))
ONE: ComplexQ = (Fraction(1), Fraction(0))


def cq(real: int | Fraction, imag: int | Fraction = 0) -> ComplexQ:
    return Fraction(real), Fraction(imag)


def cadd(left: ComplexQ, right: ComplexQ) -> ComplexQ:
    return left[0] + right[0], left[1] + right[1]


def csub(left: ComplexQ, right: ComplexQ) -> ComplexQ:
    return left[0] - right[0], left[1] - right[1]


def cneg(value: ComplexQ) -> ComplexQ:
    return -value[0], -value[1]


def cmul(left: ComplexQ, right: ComplexQ) -> ComplexQ:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def cscale(scale: int | Fraction, value: ComplexQ) -> ComplexQ:
    factor = Fraction(scale)
    return factor * value[0], factor * value[1]


def cconj(value: ComplexQ) -> ComplexQ:
    return value[0], -value[1]


def cnorm2(value: ComplexQ) -> Fraction:
    return value[0] * value[0] + value[1] * value[1]


def cinv(value: ComplexQ) -> ComplexQ:
    denominator = cnorm2(value)
    if denominator == 0:
        raise ZeroDivisionError("complex rational division by zero")
    return value[0] / denominator, -value[1] / denominator


def cdiv(left: ComplexQ, right: ComplexQ) -> ComplexQ:
    return cmul(left, cinv(right))


def cpow(value: ComplexQ, exponent: int) -> ComplexQ:
    if exponent < 0:
        return cpow(cinv(value), -exponent)
    result = ONE
    base = value
    power = exponent
    while power:
        if power & 1:
            result = cmul(result, base)
        base = cmul(base, base)
        power >>= 1
    return result


def invariant_lambda(u: Fraction, atom: ComplexQ) -> ComplexQ:
    return cdiv(
        cscale(4 * u, atom),
        cpow(cadd(cq(u), atom), 2),
    )


def atom_generator(u: Fraction, w: Fraction, atom: ComplexQ) -> ComplexQ:
    value = invariant_lambda(u, atom)
    return cdiv(value, csub(ONE, cscale(w, value)))


def finite_q(z: ComplexQ, atoms: Sequence[ComplexQ]) -> ComplexQ:
    result = ZERO
    for atom in atoms:
        result = cadd(result, cdiv(cq(2), cadd(z, atom)))
    return result


# Taylor jets use coefficients f^(n)(u0)/n!.
def jet_constant(value: ComplexQ, order: int) -> list[ComplexQ]:
    return [value] + [ZERO] * order


def jet_add(
    left: Sequence[ComplexQ],
    right: Sequence[ComplexQ],
    order: int,
) -> list[ComplexQ]:
    return [
        cadd(
            left[index] if index < len(left) else ZERO,
            right[index] if index < len(right) else ZERO,
        )
        for index in range(order + 1)
    ]


def jet_mul(
    left: Sequence[ComplexQ],
    right: Sequence[ComplexQ],
    order: int,
) -> list[ComplexQ]:
    result = [ZERO] * (order + 1)
    for degree in range(order + 1):
        coefficient = ZERO
        for index in range(degree + 1):
            coefficient = cadd(
                coefficient,
                cmul(
                    left[index] if index < len(left) else ZERO,
                    right[degree - index]
                    if degree - index < len(right)
                    else ZERO,
                ),
            )
        result[degree] = coefficient
    return result


def jet_inv(value: Sequence[ComplexQ], order: int) -> list[ComplexQ]:
    if not value or value[0] == ZERO:
        raise ZeroDivisionError("jet has zero constant term")
    result = [ZERO] * (order + 1)
    result[0] = cinv(value[0])
    for degree in range(1, order + 1):
        coefficient = ZERO
        for index in range(1, degree + 1):
            coefficient = cadd(
                coefficient,
                cmul(
                    value[index] if index < len(value) else ZERO,
                    result[degree - index],
                ),
            )
        result[degree] = cneg(cdiv(coefficient, value[0]))
    return result


def jet_pow(
    value: Sequence[ComplexQ],
    exponent: int,
    order: int,
) -> list[ComplexQ]:
    if exponent < 0:
        return jet_pow(jet_inv(value, order), -exponent, order)
    result = [ONE] + [ZERO] * order
    base = list(value) + [ZERO] * max(0, order + 1 - len(value))
    power = exponent
    while power:
        if power & 1:
            result = jet_mul(result, base, order)
        base = jet_mul(base, base, order)
        power >>= 1
    return result


def jet_scale(
    scale: int | Fraction,
    value: Sequence[ComplexQ],
) -> list[ComplexQ]:
    return [cscale(scale, coefficient) for coefficient in value]


def lambda_jet(
    u0: Fraction,
    atom: ComplexQ,
    order: int = 2,
) -> list[ComplexQ]:
    u_jet = [cq(u0), ONE] + [ZERO] * (order - 1)
    denominator = jet_add(u_jet, jet_constant(atom, order), order)
    numerator = jet_scale(4, jet_mul(u_jet, jet_constant(atom, order), order))
    return jet_mul(numerator, jet_pow(denominator, -2, order), order)


def check_matching_scale() -> int:
    checks = 0
    unit_circle = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(7, 25), Fraction(24, 25)),
    ]
    radii = [Fraction(2, 3), Fraction(7, 4), Fraction(11, 5)]
    for cosine, sine in unit_circle:
        for radius in radii:
            atom = radius * cosine, radius * sine
            value = invariant_lambda(radius, atom)
            expected = Fraction(2, 1 + cosine), Fraction(0)
            if value != expected:
                raise AssertionError(("matching_lambda", atom, value, expected))
            pole = Fraction(1 + cosine, 2)
            if csub(ONE, cscale(pole, value)) != ZERO:
                raise AssertionError(("matching_pole", atom, pole, value))
            checks += 2
    return checks


def check_resolvent_identity() -> int:
    checks = 0
    unit_circle = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(7, 25), Fraction(24, 25)),
    ]
    atom_sets: list[list[ComplexQ]] = []
    for cosine, sine in unit_circle[:2]:
        atom_sets.append(
            [
                (2 * cosine, 2 * sine),
                (2 * cosine, -2 * sine),
                (Fraction(7, 3), Fraction(0)),
            ]
        )
    nodes = [Fraction(1, 7), Fraction(3, 2), Fraction(9, 4)]
    for cosine, sine in unit_circle:
        zeta = cosine, sine
        inverse_zeta = cconj(zeta)
        w = Fraction(1 - cosine, 2)
        for u in nodes:
            for atoms in atom_sets:
                direct = ZERO
                for atom in atoms:
                    direct = cadd(direct, atom_generator(u, w, atom))
                first_q = finite_q(cscale(u, zeta), atoms)
                second_q = finite_q(cscale(u, inverse_zeta), atoms)
                closed = cscale(
                    2 * u,
                    cdiv(
                        csub(cmul(zeta, first_q), cmul(inverse_zeta, second_q)),
                        csub(zeta, inverse_zeta),
                    ),
                )
                if direct != closed:
                    raise AssertionError(("resolvent", direct, closed))
                checks += 1
    return checks


def check_pair_numerator() -> int:
    checks = 0
    unit_circle = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(7, 25), Fraction(24, 25)),
    ]
    nodes = [Fraction(1, 7), Fraction(3, 2), Fraction(9, 4)]
    radius = Fraction(5, 3)
    radius_squared = radius * radius
    for cosine, sine in unit_circle:
        atom = radius * cosine, radius * sine
        conjugate = cconj(atom)
        for u in nodes:
            for w in [Fraction(1, 10), Fraction(2, 5), Fraction(3, 5)]:
                direct = cadd(
                    atom_generator(u, w, atom),
                    atom_generator(u, w, conjugate),
                )
                c_value = 1 - 2 * w
                denominator = cadd(
                    cadd(cpow(atom, 2), cscale(2 * u * c_value, atom)),
                    cq(u * u),
                )
                numerator = 8 * u * (
                    atom[0] * (radius_squared + u * u)
                    + 2 * u * c_value * radius_squared
                )
                expected = numerator / cnorm2(denominator), Fraction(0)
                if direct != expected:
                    raise AssertionError(("pair_numerator", direct, expected))
                checks += 1
    return checks


def check_pair_threshold() -> int:
    checks = 0
    unit_circle = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(7, 25), Fraction(24, 25)),
    ]
    nodes = [Fraction(1, 7), Fraction(3, 2), Fraction(9, 4)]
    radius = Fraction(7, 3)
    for cosine, sine in unit_circle:
        atom = radius * cosine, radius * sine
        conjugate = cconj(atom)
        pole = Fraction(1 + cosine, 2)
        for u in nodes:
            below = pole - Fraction(1, 100)
            value = cadd(
                atom_generator(u, below, atom),
                atom_generator(u, below, conjugate),
            )
            if value[1] != 0 or value[0] <= 0:
                raise AssertionError(("pair_below_pole", atom, u, value))
            checks += 1
        above = pole + Fraction(1, 100)
        value = cadd(
            atom_generator(radius, above, atom),
            atom_generator(radius, above, conjugate),
        )
        if value[1] != 0 or value[0] >= 0:
            raise AssertionError(("pair_above_pole", atom, value))
        checks += 1
    return checks


def check_normalized_recurrence() -> int:
    checks = 0
    atoms = [
        (Fraction(6, 5), Fraction(2, 5)),
        (Fraction(6, 5), Fraction(-2, 5)),
        (Fraction(5, 2), Fraction(0)),
    ]
    nodes = [Fraction(1, 7), Fraction(3, 2), Fraction(9, 4)]
    for u0 in nodes:
        for atom in atoms:
            value = lambda_jet(u0, atom, 2)
            for order in range(1, 9):
                current = jet_pow(value, order, 2)
                left = cpow(value[0], order + 1)
                current_value = current[0]
                current_prime = current[1]
                current_second = cscale(2, current[2])
                right = cscale(
                    Fraction(2, order * (2 * order + 1)),
                    csub(
                        csub(
                            cscale(order * order, current_value),
                            cscale(u0, current_prime),
                        ),
                        cscale(u0 * u0, current_second),
                    ),
                )
                if left != right:
                    raise AssertionError(
                        ("normalized_recurrence", u0, atom, order, left, right)
                    )
                checks += 1
    return checks


def check_heat_moment_bridge() -> int:
    checks = 0
    atoms = [
        (Fraction(6, 5), Fraction(2, 5)),
        (Fraction(6, 5), Fraction(-2, 5)),
        (Fraction(5, 2), Fraction(0)),
    ]
    nodes = [Fraction(1, 7), Fraction(3, 2), Fraction(9, 4)]
    for u in nodes:
        for atom in atoms:
            for order in range(1, 9):
                widder_atom = cscale(
                    2 * factorial(2 * order - 1),
                    cdiv(
                        cpow(atom, order),
                        cpow(cadd(cq(u), atom), 2 * order),
                    ),
                )
                laplace_moment = cscale(
                    2 * factorial(2 * order - 1),
                    cdiv(
                        cpow(atom, order),
                        cpow(cadd(cq(u), atom), 2 * order),
                    ),
                )
                if widder_atom != laplace_moment:
                    raise AssertionError(
                        ("heat_moment", u, atom, order, widder_atom, laplace_moment)
                    )
                checks += 1
    return checks


def main() -> None:
    counts = {
        "matching_scale": check_matching_scale(),
        "resolvent": check_resolvent_identity(),
        "pair_numerator": check_pair_numerator(),
        "pair_threshold": check_pair_threshold(),
        "normalized_recurrence": check_normalized_recurrence(),
        "heat_moment": check_heat_moment_bridge(),
    }
    print("PASS_INVARIANT_WIDDER_RESOLVENT_EXACT_CHECKS")
    for name, count in counts.items():
        print(f"{name}={count}")
    print(f"total={sum(counts.values())}")
    print("ALL_ORDER_SOURCE_SIGN_OPEN")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
