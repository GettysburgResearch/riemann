"""Closed-point Adams--Möbius finite replay."""

from __future__ import annotations

from fractions import Fraction

from _ffps_relative_adams_arithmetic import (
    divisors,
    mobius,
    omega,
    validate_positive_integer,
)

ClosedPointPacket = dict[int, tuple[Fraction, ...]]


def closed_point_sum(
    packet: ClosedPointPacket, degree: int, adams_exponent: int = 1
) -> Fraction:
    validate_positive_integer(degree)
    validate_positive_integer(adams_exponent)
    return sum(
        (eigenvalue**adams_exponent for eigenvalue in packet.get(degree, ())),
        Fraction(),
    )


def extension_field_sum(
    packet: ClosedPointPacket, extension_degree: int, adams_exponent: int = 1
) -> Fraction:
    validate_positive_integer(extension_degree)
    validate_positive_integer(adams_exponent)
    return sum(
        (
            closed_degree
            * sum(
                (
                    eigenvalue ** (adams_exponent * extension_degree // closed_degree)
                    for eigenvalue in packet.get(closed_degree, ())
                ),
                Fraction(),
            )
            for closed_degree in divisors(extension_degree)
        ),
        Fraction(),
    )


def one_place_adams_extract(packet: ClosedPointPacket, degree: int) -> Fraction:
    return sum(
        (
            mobius(exponent)
            * extension_field_sum(packet, degree // exponent, exponent)
            for exponent in divisors(degree)
        ),
        Fraction(),
    )


def two_place_adams_extract(
    packet_x: ClosedPointPacket,
    packet_y: ClosedPointPacket,
    degree_x: int,
    degree_y: int,
) -> Fraction:
    return sum(
        (
            mobius(exponent_x)
            * mobius(exponent_y)
            * extension_field_sum(packet_x, degree_x // exponent_x, exponent_x)
            * extension_field_sum(packet_y, degree_y // exponent_y, exponent_y)
            for exponent_x in divisors(degree_x)
            for exponent_y in divisors(degree_y)
        ),
        Fraction(),
    )


def closed_point_replay(limit: int = 12) -> dict[str, object]:
    packet_x: ClosedPointPacket = {
        1: (Fraction(2), Fraction(-1)),
        2: (Fraction(3, 2),),
        3: (Fraction(-2), Fraction(5, 3)),
        4: (Fraction(7, 2),),
        5: (Fraction(-3, 2), Fraction(2, 3)),
        6: (Fraction(4, 3),),
    }
    packet_y: ClosedPointPacket = {
        1: (Fraction(-2, 3), Fraction(5, 2)),
        2: (Fraction(4, 3), Fraction(-1, 2)),
        3: (Fraction(7, 3),),
        4: (Fraction(-5, 4), Fraction(3, 2)),
        5: (Fraction(2, 5),),
        6: (Fraction(-7, 5), Fraction(6, 5)),
    }
    one_place_checks = 0
    two_place_checks = 0
    term_count_checks = 0
    for degree in range(1, limit + 1):
        expected = degree * closed_point_sum(packet_x, degree)
        if one_place_adams_extract(packet_x, degree) != expected:
            raise ArithmeticError("one-place Adams extraction failed")
        nonzero_terms = sum(mobius(exponent) != 0 for exponent in divisors(degree))
        if nonzero_terms != 2 ** omega(degree):
            raise ArithmeticError("one-place nonzero Mobius term count failed")
        one_place_checks += 1
        term_count_checks += 1
    for degree_x in range(1, limit + 1):
        for degree_y in range(1, limit + 1):
            expected = (
                degree_x
                * degree_y
                * closed_point_sum(packet_x, degree_x)
                * closed_point_sum(packet_y, degree_y)
            )
            if (
                two_place_adams_extract(
                    packet_x, packet_y, degree_x, degree_y
                )
                != expected
            ):
                raise ArithmeticError("two-place Adams extraction failed")
            nonzero_terms = sum(
                mobius(exponent_x) != 0 and mobius(exponent_y) != 0
                for exponent_x in divisors(degree_x)
                for exponent_y in divisors(degree_y)
            )
            if nonzero_terms != 2 ** (omega(degree_x) + omega(degree_y)):
                raise ArithmeticError("two-place nonzero Mobius term count failed")
            two_place_checks += 1
            term_count_checks += 1

    paired = {
        1: ((Fraction(2), Fraction(3)), (Fraction(-1), Fraction(5))),
        2: ((Fraction(4), Fraction(-2)), (Fraction(3), Fraction(7))),
        3: ((Fraction(-3), Fraction(6)),),
    }
    diagonal_checks = 0
    for degree, rows in paired.items():
        product = sum((left for left, _ in rows), Fraction()) * sum(
            (right for _, right in rows), Fraction()
        )
        diagonal = sum((left * right for left, right in rows), Fraction())
        direct_distinct = sum(
            (
                left * other_right
                for left_index, (left, _) in enumerate(rows)
                for right_index, (_, other_right) in enumerate(rows)
                if left_index != right_index
            ),
            Fraction(),
        )
        if product - diagonal != direct_distinct:
            raise ArithmeticError("equal-degree distinct-place correction failed")
        diagonal_checks += 1

    return {
        "diagonal_correction_checks": diagonal_checks,
        "one_place_checks": one_place_checks,
        "term_count_checks": term_count_checks,
        "two_place_checks": two_place_checks,
        "theorems": {
            "one_place": "d P_d(V)=sum_(e|d) mu(e) A_(d/e)(psi^e V)",
            "two_place": (
                "ab P_(a,b)(K)=sum_(e|a,f|b) mu(e)mu(f) "
                "A_(a/e,b/f)^partial(psi_1^e psi_2^f K)"
            ),
        },
    }
