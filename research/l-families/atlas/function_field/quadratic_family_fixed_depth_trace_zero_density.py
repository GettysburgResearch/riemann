#!/usr/bin/env python3
"""Bounded symbolic replay for every fixed odd-notch depth through M^-3."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FUNCTION_FIELD_PATH = "research/l-families/atlas/function_field"
SECOND_BOUNDARY_NOTE = f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY_THIRD_ORDER.md"
SECOND_BOUNDARY_REPLAY = f"{FUNCTION_FIELD_PATH}/quadratic_family_second_boundary_zero_density_third_order.py"
THIRD_BOUNDARY_NOTE = (
    f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_THIRD_BOUNDARY_TRACE_ZERO_DENSITY.md"
)
THIRD_BOUNDARY_REPLAY = (
    f"{FUNCTION_FIELD_PATH}/quadratic_family_third_boundary_trace_zero_density.py"
)
MIN_J = 1
MAX_J = 8
PROFILE_H_SPAN = 12
MAX_H = 500

SOURCE_BLOBS = {
    (
        "9716d2261e9e7843a6c1ffffd67ee8d6756060aa",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md",
    ): "a1b8476ddd3cad6f63ff205392426ae9c2d0829c",
    (
        "4fc8930e14eaa3863d3f3edc151c056d7d5aedce",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_NOTCH_DEPTH_PHASE_DIAGRAM.md",
    ): "01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e",
    (
        "0b9f407f10ab8b12f22526af8a08b870baaef0e9",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_NOTCH_PARITY_SIEVE.md",
    ): "38f1b6e95f9a7eb6756450673ff067308886a0ff",
    (
        "f5aabadd65dd53cd9a69e3e3b38b9bc7693b3359",
        SECOND_BOUNDARY_NOTE,
    ): "12aa4be45fd970f843be6b2024547f7ab7594b21",
    (
        "f5aabadd65dd53cd9a69e3e3b38b9bc7693b3359",
        SECOND_BOUNDARY_REPLAY,
    ): "60dc980a4e8bccb2cdd607829d167909b3f4729c",
    (
        "d13dfcfcbb32733fc9b7925b82c4cf3dc9a9107a",
        THIRD_BOUNDARY_NOTE,
    ): "ba853379190d9f4de1172f576095ed29a068c0dd",
    (
        "d13dfcfcbb32733fc9b7925b82c4cf3dc9a9107a",
        THIRD_BOUNDARY_REPLAY,
    ): "8ca76f0286cf95537ba8f00081ba973e2940ed69",
}

AffineLog2 = tuple[Fraction, Fraction]
H_MINUS_2: AffineLog2 = (Fraction(1, 3), Fraction(1, 3))
REPEATED_MINIMUM_H_MINUS_3 = Fraction(1, 4)
NEAR_H_H_MINUS_3 = Fraction(1, 2)
NEAR_H_M_MINUS_3 = Fraction(32)


def check_source_blobs() -> None:
    for (commit, path), expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def stable_h(depth: int) -> int:
    _validate_depth(depth)
    return 5 * depth + 2


def _validate_depth(depth: int) -> None:
    if (
        isinstance(depth, bool)
        or not isinstance(depth, int)
        or not MIN_J <= depth <= MAX_J
    ):
        raise ValueError(f"depth must be an integer in [{MIN_J},{MAX_J}]")


def _validate_h(depth: int, h_value: int, maximum: int = MAX_H) -> None:
    _validate_depth(depth)
    if (
        isinstance(h_value, bool)
        or not isinstance(h_value, int)
        or not stable_h(depth) <= h_value <= maximum
    ):
        raise ValueError(f"h must be an integer in [{stable_h(depth)},{maximum}]")


def _fixed_partitions(
    total: int, length: int, minimum: int
) -> tuple[tuple[int, ...], ...]:
    if length < 1 or minimum < 1:
        raise ValueError("partition length and minimum must be positive")
    if length == 1:
        return ((total,),) if total >= minimum else ()
    rows: list[tuple[int, ...]] = []
    for first in range(minimum, total // length + 1):
        for tail in _fixed_partitions(total - first, length - 1, first):
            rows.append((first, *tail))
    return tuple(rows)


def fixed_depth_profiles(depth: int, h_value: int) -> tuple[tuple[int, ...], ...]:
    """All degree multisets with minimum degree exactly h-depth."""

    _validate_h(depth, h_value, stable_h(MAX_J) + PROFILE_H_SPAN)
    total = 4 * h_value + 1
    minimum = h_value - depth
    maximum_factors = total // minimum
    if maximum_factors != 4:
        raise ArithmeticError("stable range should admit exactly up to four factors")
    rows: list[tuple[int, ...]] = []
    for factor_count in range(2, maximum_factors + 1):
        for tail in _fixed_partitions(total - minimum, factor_count - 1, minimum):
            rows.append((minimum, *tail))
    return tuple(rows)


def channel_degrees(depth: int) -> tuple[int, ...]:
    _validate_depth(depth)
    return tuple(2 * depth + 1 - 2 * shift for shift in range(depth + 1))


def notch_coefficients(
    profile: tuple[int, ...], depth: int, h_value: int
) -> tuple[int, ...]:
    """Replay the reciprocal Euler quotient through degree h."""

    _validate_h(depth, h_value)
    coefficients = [0] * (h_value + 1)
    coefficients[0] = 1
    for degree in profile:
        for index in range(degree, h_value + 1):
            coefficients[index] += coefficients[index - degree]
    minimum = h_value - depth
    return tuple(coefficients[minimum + shift] for shift in range(depth + 1))


def residual_terms(
    profile: tuple[int, ...], depth: int, h_value: int
) -> tuple[tuple[int, int], ...]:
    coefficients = notch_coefficients(profile, depth, h_value)
    return tuple(
        (multiplicity, exterior_degree)
        for multiplicity, exterior_degree in zip(
            coefficients, channel_degrees(depth), strict=True
        )
        if multiplicity
    )


def classify_profile(
    depth: int, h_value: int, profile: tuple[int, ...]
) -> dict[str, object]:
    _validate_h(depth, h_value)
    minimum = h_value - depth
    if (
        not profile
        or tuple(sorted(profile)) != profile
        or profile[0] != minimum
        or sum(profile) != 4 * h_value + 1
    ):
        raise ValueError("profile is not on the stable fixed-depth boundary")

    coefficients = notch_coefficients(profile, depth, h_value)
    multiplicities = tuple(profile.count(minimum + shift) for shift in range(depth + 1))
    if coefficients != multiplicities:
        raise ArithmeticError("fixed-depth coefficient collapse failed")

    top_degree = 2 * depth + 1
    if coefficients[-1] % 2:
        branch = "parity_zero"
        channel_shift: int | None = depth
        zero_condition = "impossible: residual is odd"
    elif len(profile) == 2:
        branch = "generic_D_top"
        channel_shift = None
        zero_condition = f"D_{top_degree}=0"
    elif len(profile) == 3:
        second_shift = profile[1] - minimum
        if second_shift == 0:
            branch = "repeated_minimum_D_top"
            channel_shift = 0
            zero_condition = f"D_{top_degree}=0"
        elif 1 <= second_shift <= depth:
            lower_degree = top_degree - 2 * second_shift
            branch = "near_h_joint"
            channel_shift = second_shift
            zero_condition = f"D_{top_degree}+D_{lower_degree}=0"
        elif profile[1] >= h_value + 1:
            branch = "generic_D_top"
            channel_shift = None
            zero_condition = f"D_{top_degree}=0"
        else:
            raise ArithmeticError("three-factor profile escaped classification")
    elif len(profile) == 4:
        branch = "fourth_order_remainder"
        channel_shift = None
        zero_condition = "retained only in O_(q,j)(h^-4)"
    else:
        raise ArithmeticError("stable range admitted more than four factors")

    return {
        "depth": depth,
        "h": h_value,
        "M": 4 * h_value + 1,
        "profile": profile,
        "coefficients": coefficients,
        "residual_terms": residual_terms(profile, depth, h_value),
        "m_h": coefficients[-1],
        "branch": branch,
        "channel_shift": channel_shift,
        "zero_condition": zero_condition,
    }


def claimed_through_h_minus_3_profiles(
    depth: int, h_value: int
) -> tuple[tuple[int, ...], ...]:
    """Closed list of all two- and three-factor profiles."""

    _validate_h(depth, h_value)
    minimum = h_value - depth
    complement = 3 * h_value + depth + 1
    rows = [(minimum, complement)]
    rows.extend(
        (minimum, degree, complement - degree)
        for degree in range(minimum, complement // 2 + 1)
    )
    return tuple(rows)


def profile_principal_weight(profile: tuple[int, ...]) -> Fraction:
    multiplicities = Counter(profile)
    denominator = 1
    for degree, multiplicity in multiplicities.items():
        denominator *= degree**multiplicity * math.factorial(multiplicity)
    return Fraction(1, denominator)


def harmonic(number: int) -> Fraction:
    if isinstance(number, bool) or not isinstance(number, int) or number < 0:
        raise ValueError("harmonic index must be nonnegative")
    return sum((Fraction(1, index) for index in range(1, number + 1)), Fraction())


def generic_direct_weight(depth: int, h_value: int) -> Fraction:
    """Two-factor plus generic three-factor principal weight."""

    _validate_h(depth, h_value)
    minimum = h_value - depth
    complement = 3 * h_value + depth + 1
    weight = Fraction(1, minimum * complement)
    for degree in range(h_value + 1, complement // 2 + 1):
        other = complement - degree
        if degree < other:
            weight += Fraction(1, minimum * degree * other)
        elif degree == other:
            weight += Fraction(1, 2 * minimum * degree * degree)
    return weight


def generic_harmonic_weight(depth: int, h_value: int) -> Fraction:
    _validate_h(depth, h_value)
    return Fraction(
        1 + harmonic(2 * h_value + depth) - harmonic(h_value),
        (h_value - depth) * (3 * h_value + depth + 1),
    )


def repeated_minimum_weight(depth: int, h_value: int) -> Fraction:
    _validate_h(depth, h_value)
    return Fraction(
        1,
        2 * (h_value - depth) ** 2 * (2 * h_value + 2 * depth + 1),
    )


def near_h_weight(depth: int, shift: int, h_value: int) -> Fraction:
    _validate_h(depth, h_value)
    if isinstance(shift, bool) or not isinstance(shift, int) or not 1 <= shift <= depth:
        raise ValueError("shift must be an integer in [1,depth]")
    minimum = h_value - depth
    return Fraction(
        1,
        minimum * (minimum + shift) * (2 * h_value + 2 * depth + 1 - shift),
    )


def generic_h_minus_3(depth: int) -> AffineLog2:
    _validate_depth(depth)
    factor = 2 * depth - 1
    return Fraction(7 * factor, 36), Fraction(factor, 9)


def delta0_h_minus_3(depth: int) -> AffineLog2:
    generic = generic_h_minus_3(depth)
    return generic[0] + REPEATED_MINIMUM_H_MINUS_3, generic[1]


def delta0_m_minus_3(depth: int) -> AffineLog2:
    _validate_depth(depth)
    return (
        Fraction(32 * (7 * depth + 4), 9),
        Fraction(32 * (4 * depth + 1), 9),
    )


def delta_forced_zero(depth: int, shift: int) -> bool:
    _validate_depth(depth)
    if isinstance(shift, bool) or not isinstance(shift, int) or not 0 <= shift <= depth:
        raise ValueError("shift must be an integer in [0,depth]")
    return shift == depth


def affine_render(value: AffineLog2) -> str:
    return f"{value[0]} + ({value[1]})*log(2)"


def run() -> dict[str, object]:
    replay_rows = []
    profiles_checked = 0
    for depth in range(MIN_J, MAX_J + 1):
        for h_value in range(stable_h(depth), stable_h(depth) + PROFILE_H_SPAN + 1):
            profiles = fixed_depth_profiles(depth, h_value)
            profiles_checked += len(profiles)
            through_third = tuple(profile for profile in profiles if len(profile) <= 3)
            if through_third != claimed_through_h_minus_3_profiles(depth, h_value):
                raise ArithmeticError("two/three-factor profile list is incomplete")
            for profile in profiles:
                classify_profile(depth, h_value, profile)
            if generic_direct_weight(depth, h_value) != generic_harmonic_weight(
                depth, h_value
            ):
                raise ArithmeticError("generic harmonic compression failed")

        h_value = stable_h(depth)
        profiles = fixed_depth_profiles(depth, h_value)
        branches = Counter(
            str(classify_profile(depth, h_value, profile)["branch"])
            for profile in profiles
        )
        replay_rows.append(
            {
                "depth": depth,
                "h": h_value,
                "M": 4 * h_value + 1,
                "profiles": len(profiles),
                "branches": dict(sorted(branches.items())),
                "generic_h_minus_3": affine_render(generic_h_minus_3(depth)),
                "delta0_h_minus_3": affine_render(delta0_h_minus_3(depth)),
                "delta0_M_minus_3": affine_render(delta0_m_minus_3(depth)),
                "active_joint_shifts": list(range(1, depth)),
                "parity_zero_shift": depth,
            }
        )

    if delta0_h_minus_3(1) != (Fraction(4, 9), Fraction(1, 9)):
        raise ArithmeticError("depth-one specialization failed")
    if delta0_m_minus_3(1) != (Fraction(352, 9), Fraction(160, 9)):
        raise ArithmeticError("depth-one M-normalization failed")
    if delta0_h_minus_3(2) != (Fraction(5, 6), Fraction(1, 3)):
        raise ArithmeticError("depth-two specialization failed")
    if delta0_m_minus_3(2) != (Fraction(64), Fraction(32)):
        raise ArithmeticError("depth-two M-normalization failed")

    return {
        "schema": "riemann.function_field.quadratic_fixed_depth_zero.v1",
        "status": (
            "exact all-fixed-depth residual/profile theorem and fixed-q raw "
            "zero density through M^-3"
        ),
        "scope": {
            "q": "fixed odd prime power",
            "depth": "fixed integer j>=1",
            "stable_range": "h>=5j+2",
            "n": "2h+1",
            "M": "4h+1",
            "minimum_factor_degree": "h-j",
        },
        "frozen_sources": {
            f"{commit}:{path}": blob for (commit, path), blob in SOURCE_BLOBS.items()
        },
        "exact_reduction": {
            "residual": "sum_(s=0)^j m_(h-j+s)*D_(2j+1-2s)",
            "parity": "D_1 odd and every D_r with odd r>=3 even",
            "forced_zero_channel": "delta_(j,j,q)=Prob(D_(2j+1)+D_1=0)=0",
        },
        "profile_weights": {
            "generic_exact": ("[1+H_(2h+j)-H_h]/[(h-j)(3h+j+1)]"),
            "generic_h_minus_2": affine_render(H_MINUS_2),
            "generic_h_minus_3": "(2j-1)*(7+4log(2))/36",
            "repeated_minimum_h_minus_3": str(REPEATED_MINIMUM_H_MINUS_3),
            "each_near_h_h_minus_3": str(NEAR_H_H_MINUS_3),
        },
        "fixed_q_asymptotic": {
            "count_over_q^M": (
                "delta_(j,0,q)*(1+log(2))/(3h^2)+"
                "{delta_(j,0,q)*([(2j-1)(7+4log(2))+9]/36)+"
                "(1/2)*sum_(s=1)^j delta_(j,s,q)}/h^3+O_(q,j)(h^-4)"
            ),
            "squarefree_density": (
                "[16*delta_(j,0,q)*(1+log(2))/(3M^2)+"
                "32*{delta_(j,0,q)*[(7j+4)+(4j+1)log(2)]/9+"
                "sum_(s=1)^j delta_(j,s,q)}/M^3+O_(q,j)(M^-4)]/"
                "(1-q^-1)"
            ),
            "delta_definition": (
                "delta_(j,0,q)=Prob(D_(2j+1)=0); for s>=1, "
                "delta_(j,s,q)=Prob(D_(2j+1)+D_(2j+1-2s)=0)"
            ),
            "positivity_claimed": False,
        },
        "specializations": {
            "j=1": {
                "delta0_h_minus_3": affine_render(delta0_h_minus_3(1)),
                "delta0_M_minus_3": affine_render(delta0_m_minus_3(1)),
                "active_joint_channels": [],
                "recovers": "second-boundary M^-3 packet",
            },
            "j=2": {
                "delta0_h_minus_3": affine_render(delta0_h_minus_3(2)),
                "delta0_M_minus_3": affine_render(delta0_m_minus_3(2)),
                "active_joint_channels": ["delta_(2,1,q)"],
                "recovers": "third-boundary M^-3 packet",
            },
        },
        "aggregation_boundary": {
            "each_fixed_depth": "O_(q,j)(M^-2)",
            "necessary_for_M_minus_1": "a number of depths growing with M",
            "open_issue": (
                "decay or nondecay of the local delta tower, together with "
                "uniformity as j grows"
            ),
        },
        "bounded_replay": {
            "maximum_depth": MAX_J,
            "profile_h_span": PROFILE_H_SPAN,
            "profiles_checked": profiles_checked,
            "rows": replay_rows,
        },
        "claim_boundary": {
            "input_theorem": (
                "standard fixed-modulus prime-polynomial progression theorem"
            ),
            "individual_L_function_zero": False,
            "rh_or_grh": False,
            "uniform_growing_depth_theorem": False,
            "external_priority_claim": False,
        },
        "resource_caps": {
            "maximum_depth": MAX_J,
            "profiles_checked": profiles_checked,
            "polynomials_enumerated": 0,
            "irreducibles_enumerated": 0,
            "residue_classes_enumerated": 0,
            "finite_field_elements_enumerated": 0,
            "curves_enumerated": 0,
            "zeros_enumerated": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
