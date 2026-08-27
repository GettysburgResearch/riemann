"""Finite character algebra for the relative ternary projector."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction

from _ffps_relative_adams_arithmetic import validate_positive_integer

Character = tuple[int, int, int, int, int, int]
CharacterClass = dict[Character, Fraction]


def clean_class(value: CharacterClass) -> CharacterClass:
    return {key: coefficient for key, coefficient in value.items() if coefficient}


def add_classes(left: CharacterClass, right: CharacterClass) -> CharacterClass:
    result = dict(left)
    for character, coefficient in right.items():
        result[character] = result.get(character, Fraction()) + coefficient
    return clean_class(result)


def scale_class(value: CharacterClass, scalar: Fraction | int) -> CharacterClass:
    scalar = Fraction(scalar)
    return clean_class(
        {character: scalar * coefficient for character, coefficient in value.items()}
    )


def subtract_classes(left: CharacterClass, right: CharacterClass) -> CharacterClass:
    return add_classes(left, scale_class(right, -1))


def adams(value: CharacterClass, exponent_x: int, exponent_y: int) -> CharacterClass:
    validate_positive_integer(exponent_x)
    validate_positive_integer(exponent_y)
    result: CharacterClass = {}
    for character, coefficient in value.items():
        x1, x2, x3, y1, y2, y3 = character
        image = (
            exponent_x * x1 % 2,
            exponent_x * x2 % 2,
            exponent_x * x3 % 3,
            exponent_y * y1 % 2,
            exponent_y * y2 % 2,
            exponent_y * y3 % 3,
        )
        result[image] = result.get(image, Fraction()) + coefficient
    return clean_class(result)


def relative_class() -> CharacterClass:
    return {
        (x1, x2, 0, y1, y2, 0): Fraction(1)
        for x1 in (0, 1)
        for x2 in (0, 1)
        for y1 in (0, 1)
        for y2 in (0, 1)
    }


def selected_class(alignment: int) -> CharacterClass:
    if alignment not in (-1, 1):
        raise ValueError("alignment must be +1 or -1")
    return {
        (x1, x2, cubic, y1, y2, alignment * cubic % 3): Fraction(1, 4)
        for x1 in (0, 1)
        for x2 in (0, 1)
        for y1 in (0, 1)
        for y2 in (0, 1)
        for cubic in (1, 2)
    }


def hard_class(alignment: int) -> CharacterClass:
    return add_classes(relative_class(), selected_class(alignment))


def absolute_line_mass(value: CharacterClass) -> Fraction:
    return sum((abs(coefficient) for coefficient in value.values()), Fraction())


def class_digest(value: CharacterClass) -> str:
    payload = json.dumps(
        [
            {"character": list(character), "coefficient": str(coefficient)}
            for character, coefficient in sorted(value.items())
        ],
        separators=(",", ":"),
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def expected_relative_profile(exponent_x: int, exponent_y: int) -> CharacterClass:
    left = (
        {(x1, x2): Fraction(1) for x1 in (0, 1) for x2 in (0, 1)}
        if exponent_x % 2
        else {(0, 0): Fraction(4)}
    )
    right = (
        {(y1, y2): Fraction(1) for y1 in (0, 1) for y2 in (0, 1)}
        if exponent_y % 2
        else {(0, 0): Fraction(4)}
    )
    return {
        (x1, x2, 0, y1, y2, 0): left_coefficient * right_coefficient
        for (x1, x2), left_coefficient in left.items()
        for (y1, y2), right_coefficient in right.items()
    }


def character_algebra_replay(limit: int = 12) -> dict[str, object]:
    validate_positive_integer(limit)
    relative = relative_class()
    rows = []
    unique_profiles: dict[tuple[int, int], str] = {}
    for alignment in (-1, 1):
        selected = selected_class(alignment)
        hard = hard_class(alignment)
        if subtract_classes(hard, selected) != relative:
            raise ArithmeticError("hard-selected relative projector failed")
        checks = 0
        for exponent_x in range(1, limit + 1):
            for exponent_y in range(1, limit + 1):
                lhs = subtract_classes(
                    adams(hard, exponent_x, exponent_y),
                    adams(selected, exponent_x, exponent_y),
                )
                rhs = adams(relative, exponent_x, exponent_y)
                expected = expected_relative_profile(exponent_x, exponent_y)
                if lhs != rhs or rhs != expected:
                    raise ArithmeticError("subtract-before-Adams identity failed")
                if any(character[2] or character[5] for character in rhs):
                    raise ArithmeticError("cubic character survived relative projection")
                if absolute_line_mass(rhs) != 16:
                    raise ArithmeticError("relative Adams line mass changed")
                parity = (exponent_x % 2, exponent_y % 2)
                digest = class_digest(rhs)
                previous = unique_profiles.setdefault(parity, digest)
                if previous != digest:
                    raise ArithmeticError("relative profile depends on more than parity")
                checks += 1
        rows.append(
            {
                "alignment": alignment,
                "checks": checks,
                "hard_absolute_weighted_line_mass": str(absolute_line_mass(hard)),
                "hard_distinct_lines": len(hard),
                "relative_absolute_weighted_line_mass": str(
                    absolute_line_mass(relative)
                ),
                "relative_distinct_lines": len(relative),
                "selected_absolute_weighted_line_mass": str(
                    absolute_line_mass(selected)
                ),
                "selected_distinct_lines": len(selected),
            }
        )
    if len(unique_profiles) != 4:
        raise ArithmeticError("relative physical layer does not have four profiles")
    profile_rows = []
    for parity, digest in sorted(unique_profiles.items()):
        profile = expected_relative_profile(*parity)
        profile_rows.append(
            {
                "distinct_lines": len(profile),
                "line_mass": str(absolute_line_mass(profile)),
                "parity_x_y": list(parity),
                "profile_digest": digest,
            }
        )
    return {
        "adams_checks_per_alignment": limit * limit,
        "four_physical_parity_profiles": profile_rows,
        "hard_minus_selected_equals_relative": True,
        "partial_adams_preserves_difference": True,
        "rows": rows,
    }
