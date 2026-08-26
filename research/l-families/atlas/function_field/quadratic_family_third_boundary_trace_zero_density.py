#!/usr/bin/env python3
"""Exact symbolic replay for the odd-notch third factor-degree boundary."""

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
MIN_H = 12
MAX_H = 200
PROFILE_MAX_H = 60
LOCAL_Q_MAX = 3
WITNESS_Q_VALUES = (3, 5, 7, 9, 11, 13, 25, 27, 49)
FUNCTION_FIELD_PATH = "research/l-families/atlas/function_field"

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
        "97cdc4a5ea27bc1052dbad7eef19276da331388c",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_SECOND_BOUNDARY_TRACE_ZERO_REDUCTION.md",
    ): "80e6e3c5e3001011356df13381c9ad45b66d2245",
    (
        "f5aabadd65dd53cd9a69e3e3b38b9bc7693b3359",
        f"{FUNCTION_FIELD_PATH}/QUADRATIC_FAMILY_SECOND_BOUNDARY_ZERO_DENSITY_THIRD_ORDER.md",
    ): "12aa4be45fd970f843be6b2024547f7ab7594b21",
}

AffineLog2 = tuple[Fraction, Fraction]
H_MINUS_2: AffineLog2 = (Fraction(1, 3), Fraction(1, 3))
H_MINUS_3_GENERIC: AffineLog2 = (Fraction(7, 12), Fraction(1, 3))
H_MINUS_3_REPEATED_MINIMUM = Fraction(1, 4)
H_MINUS_3_MIXED = Fraction(1, 2)
H_MINUS_3_D5_TOTAL: AffineLog2 = (
    H_MINUS_3_GENERIC[0] + H_MINUS_3_REPEATED_MINIMUM,
    H_MINUS_3_GENERIC[1],
)


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


def _validate_h(h_value: int, maximum: int = MAX_H) -> None:
    if (
        isinstance(h_value, bool)
        or not isinstance(h_value, int)
        or h_value < MIN_H
        or h_value > maximum
    ):
        raise ValueError(f"h must be an integer in [{MIN_H},{maximum}]")


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


def third_boundary_profiles(h_value: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate degree multisets only on min degree h-2."""

    _validate_h(h_value, PROFILE_MAX_H)
    total = 4 * h_value + 1
    minimum = h_value - 2
    rows: list[tuple[int, ...]] = []
    for factor_count in range(2, total // minimum + 1):
        for tail in _fixed_partitions(total - minimum, factor_count - 1, minimum):
            rows.append((minimum, *tail))
    return tuple(rows)


def notch_coefficients(profile: tuple[int, ...], h_value: int) -> tuple[int, int, int]:
    """Return a_(h-2), a_(h-1), a_h from the locked Euler quotient."""

    coefficients = [0] * (h_value + 1)
    coefficients[0] = 1
    for degree in profile:
        for index in range(degree, h_value + 1):
            coefficients[index] += coefficients[index - degree]
    return coefficients[h_value - 2], coefficients[h_value - 1], coefficients[h_value]


def classify_profile(h_value: int, profile: tuple[int, ...]) -> dict[str, object]:
    _validate_h(h_value, PROFILE_MAX_H)
    minimum = h_value - 2
    if (
        not profile
        or tuple(sorted(profile)) != profile
        or profile[0] != minimum
        or sum(profile) != 4 * h_value + 1
    ):
        raise ValueError("profile is not on the stable third boundary")

    r_value = profile.count(h_value - 2)
    s_value = profile.count(h_value - 1)
    t_value = profile.count(h_value)
    coefficients = notch_coefficients(profile, h_value)
    if coefficients != (r_value, s_value, t_value):
        raise ArithmeticError("third-boundary coefficient collapse failed")

    if t_value % 2:
        branch = "nonzero_by_parity"
        zero_condition = "impossible because S is odd"
    elif t_value == 2:
        exceptional = (h_value - 2, h_value, h_value, h_value + 3)
        if profile != exceptional:
            raise ArithmeticError("positive even m_h escaped the unique profile")
        branch = "fourth_order_D5_plus_2D1"
        zero_condition = "D_5+2*D_1=0"
    elif t_value == 0:
        if s_value == 0:
            branch = "D5_zero"
            zero_condition = "D_5=0"
        else:
            branch = "mixed_D5_D3"
            zero_condition = f"{r_value}*D_5+{s_value}*D_3=0"
    else:
        raise ArithmeticError("degree budget admitted m_h>=4")

    return {
        "h": h_value,
        "M": 4 * h_value + 1,
        "profile": profile,
        "m_h_minus_2": r_value,
        "m_h_minus_1": s_value,
        "m_h": t_value,
        "residual": f"{r_value}*D_5+{s_value}*D_3+{t_value}*D_1",
        "branch": branch,
        "zero_condition": zero_condition,
    }


def claimed_parity_even_profiles(h_value: int) -> tuple[tuple[int, ...], ...]:
    """Closed list of every profile not eliminated by m_h parity."""

    _validate_h(h_value, PROFILE_MAX_H)
    d_value = h_value - 2
    rows: list[tuple[int, ...]] = [(d_value, 3 * h_value + 3)]
    rows.extend(
        (d_value, degree, 3 * h_value + 3 - degree)
        for degree in range(h_value + 1, (3 * h_value + 3) // 2 + 1)
    )
    rows.append((d_value, h_value + 1, h_value + 1, h_value + 1))
    rows.extend(
        (
            (d_value, d_value, 2 * h_value + 5),
            (d_value, d_value, h_value + 1, h_value + 4),
            (d_value, d_value, h_value + 2, h_value + 3),
            (d_value, h_value - 1, 2 * h_value + 4),
            (d_value, h_value - 1, h_value + 1, h_value + 3),
            (d_value, h_value - 1, h_value + 2, h_value + 2),
            (d_value, d_value, d_value, h_value + 7),
            (d_value, d_value, h_value - 1, h_value + 6),
            (d_value, h_value - 1, h_value - 1, h_value + 5),
            (d_value, h_value, h_value, h_value + 3),
        )
    )
    return tuple(sorted(rows))


def profile_principal_weight(profile: tuple[int, ...]) -> Fraction:
    multiplicities = Counter(profile)
    denominator = 1
    for degree, multiplicity in multiplicities.items():
        denominator *= degree**multiplicity * math.factorial(multiplicity)
    return Fraction(1, denominator)


def harmonic(number: int) -> Fraction:
    if isinstance(number, bool) or not isinstance(number, int) or number < 0:
        raise ValueError("harmonic index must be nonnegative")
    return sum((Fraction(1, index) for index in range(1, number + 1)), Fraction(0))


def generic_direct_weight(h_value: int) -> Fraction:
    """One minimum factor, no h-1/h factor, through three total factors."""

    _validate_h(h_value)
    minimum = h_value - 2
    complement = 3 * h_value + 3
    weight = Fraction(1, minimum * complement)
    for degree in range(h_value + 1, complement // 2 + 1):
        other = complement - degree
        if degree < other:
            weight += Fraction(1, minimum * degree * other)
        elif degree == other:
            weight += Fraction(1, 2 * minimum * degree * degree)
    return weight


def generic_harmonic_weight(h_value: int) -> Fraction:
    _validate_h(h_value)
    return Fraction(
        1 + harmonic(2 * h_value + 2) - harmonic(h_value),
        (h_value - 2) * (3 * h_value + 3),
    )


def repeated_minimum_weight(h_value: int) -> Fraction:
    _validate_h(h_value)
    return Fraction(1, 2 * (h_value - 2) ** 2 * (2 * h_value + 5))


def mixed_minimum_weight(h_value: int) -> Fraction:
    _validate_h(h_value)
    return Fraction(1, (h_value - 2) * (h_value - 1) * (2 * h_value + 4))


def _divisors(value: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def _mobius(value: int) -> int:
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def irreducible_count(q_value: int, degree: int) -> int:
    numerator = sum(
        _mobius(divisor) * q_value ** (degree // divisor)
        for divisor in _divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible-count formula lost integrality")
    return numerator // degree


def h2_rademacher(total: int, count: int) -> int:
    numerator = total * total + count
    if numerator % 2:
        raise ArithmeticError("h2 is not integral")
    return numerator // 2


def h3_rademacher(total: int, count: int) -> int:
    numerator = total**3 + (3 * count + 2) * total
    if numerator % 6:
        raise ArithmeticError("h3 is not integral")
    return numerator // 6


def h5_rademacher(total: int, count: int) -> int:
    numerator = (
        total**5
        + (10 * count + 20) * total**3
        + (15 * count * count + 50 * count + 24) * total
    )
    if numerator % 120:
        raise ArithmeticError("h5 is not integral")
    return numerator // 120


def local_d3(q_value: int, sums: tuple[int, int, int, int, int]) -> int:
    s1, s2, s3, _s4, _s5 = sums
    n1 = irreducible_count(q_value, 1)
    return s3 + s1 * s2 + h3_rademacher(s1, n1) - q_value * s1


def local_d5(q_value: int, sums: tuple[int, int, int, int, int]) -> int:
    s1, s2, s3, s4, s5 = sums
    n1 = irreducible_count(q_value, 1)
    n2 = irreducible_count(q_value, 2)
    a3 = s3 + s1 * s2 + h3_rademacher(s1, n1)
    a5 = (
        s5
        + s1 * s4
        + s2 * s3
        + h2_rademacher(s1, n1) * s3
        + h2_rademacher(s2, n2) * s1
        + h3_rademacher(s1, n1) * s2
        + h5_rademacher(s1, n1)
    )
    return a5 - q_value * a3


def rademacher_multiplicity(count: int, total: int) -> int:
    if abs(total) > count or (count + total) % 2:
        return 0
    return math.comb(count, (count + total) // 2)


def rademacher_attainable(count: int, total: int) -> bool:
    """Whether ``total`` is a possible sum of ``count`` signs."""

    return abs(total) <= count and (count + total) % 2 == 0


def local_probabilities(q_value: int) -> tuple[Fraction, Fraction]:
    """Exact tiny-q probabilities for D5=0 and D5+D3=0."""

    if (
        isinstance(q_value, bool)
        or not isinstance(q_value, int)
        or q_value < 3
        or q_value % 2 == 0
        or q_value > LOCAL_Q_MAX
    ):
        raise ValueError("local replay is intentionally restricted to q=3")
    counts = tuple(irreducible_count(q_value, degree) for degree in range(1, 6))
    favorable_d5 = 0
    favorable_d53 = 0
    for s1 in range(-counts[0], counts[0] + 1, 2):
        m1 = rademacher_multiplicity(counts[0], s1)
        for s2 in range(-counts[1], counts[1] + 1, 2):
            m2 = rademacher_multiplicity(counts[1], s2)
            for s3 in range(-counts[2], counts[2] + 1, 2):
                m3 = rademacher_multiplicity(counts[2], s3)
                for s4 in range(-counts[3], counts[3] + 1, 2):
                    multiplicity = m1 * m2 * m3 * rademacher_multiplicity(counts[3], s4)
                    lower_sums = (s1, s2, s3, s4, 0)
                    d3_value = local_d3(q_value, lower_sums)
                    d5_without_s5 = local_d5(q_value, lower_sums)
                    target_d5 = -d5_without_s5
                    target_d53 = -d5_without_s5 - d3_value
                    favorable_d5 += multiplicity * rademacher_multiplicity(
                        counts[4], target_d5
                    )
                    favorable_d53 += multiplicity * rademacher_multiplicity(
                        counts[4], target_d53
                    )
    total = 2 ** sum(counts)
    return Fraction(favorable_d5, total), Fraction(favorable_d53, total)


def positivity_witness(q_value: int) -> dict[str, int]:
    """Aggregate sign sums witnessing both local zero events."""

    if q_value < 3 or q_value % 2 == 0:
        raise ValueError("q must be odd and at least three")
    counts = tuple(irreducible_count(q_value, degree) for degree in range(1, 6))
    s2 = counts[1] % 2
    lower = (1, s2, 0, 0, 0)
    d3_value = local_d3(q_value, lower)
    d5_without_s5 = local_d5(q_value, lower)
    target_d5 = -d5_without_s5
    target_d53 = -d5_without_s5 - d3_value
    for target in (target_d5, target_d53):
        if not rademacher_attainable(counts[4], target):
            raise ArithmeticError("explicit local positivity witness failed")
    return {
        "q": q_value,
        "S1": 1,
        "S2": s2,
        "S3": 0,
        "S4": 0,
        "D3_before_S5": d3_value,
        "D5_before_S5": d5_without_s5,
        "S5_for_D5_zero": target_d5,
        "S5_for_D5_plus_D3_zero": target_d53,
        "N5": counts[4],
    }


def affine_render(value: AffineLog2) -> str:
    return f"{value[0]} + ({value[1]})*log(2)"


def run() -> dict[str, object]:
    profile_rows = []
    profiles_checked = 0
    for h_value in range(MIN_H, PROFILE_MAX_H + 1):
        profiles = third_boundary_profiles(h_value)
        profiles_checked += len(profiles)
        even_profiles = tuple(
            sorted(
                profile
                for profile in profiles
                if classify_profile(h_value, profile)["m_h"] % 2 == 0
            )
        )
        if even_profiles != claimed_parity_even_profiles(h_value):
            raise ArithmeticError("stable parity-even profile list is incomplete")
        for profile in profiles:
            classify_profile(h_value, profile)
        if h_value in (12, 20, 40, 60):
            branches = Counter(
                str(classify_profile(h_value, profile)["branch"])
                for profile in profiles
            )
            profile_rows.append(
                {
                    "h": h_value,
                    "M": 4 * h_value + 1,
                    "profiles": len(profiles),
                    "parity_even_profiles": len(even_profiles),
                    "branches": dict(sorted(branches.items())),
                }
            )

    for h_value in range(MIN_H, MAX_H + 1):
        if generic_direct_weight(h_value) != generic_harmonic_weight(h_value):
            raise ArithmeticError("generic harmonic compression failed")

    if H_MINUS_3_D5_TOTAL != (Fraction(5, 6), Fraction(1, 3)):
        raise ArithmeticError("D5 third-order coefficient changed")

    delta5_q3, delta53_q3 = local_probabilities(3)
    witnesses = [positivity_witness(q_value) for q_value in WITNESS_Q_VALUES]

    return {
        "schema": "riemann.function_field.quadratic_third_boundary_zero.v1",
        "status": (
            "exact h-2 residual/profile theorem and fixed-q density through "
            "M^-3, conditional only on fixed-modulus prime-polynomial progressions"
        ),
        "frozen_sources": {
            f"{commit}:{path}": blob for (commit, path), blob in SOURCE_BLOBS.items()
        },
        "exact_reduction": {
            "scope": "fixed odd prime power q; n=2h+1, M=4h+1, h>=12",
            "boundary": "minimum factor degree h-2",
            "residual": "S=m_(h-2)*D_5+m_(h-1)*D_3+m_h*D_1",
            "parity": "D_1 odd; D_3 and D_5 even; every zero has even m_h",
            "zero_dichotomy": (
                "m_h=0 and m_(h-2)D_5+m_(h-1)D_3=0; or profile "
                "(h-2,h,h,h+3) and D_5+2D_1=0"
            ),
            "positive_even_m_h_profile": "(h-2,h,h,h+3), order M^-4",
        },
        "order_separation": {
            "M^-1": "impossible: the whole fixed layer is O_q(M^-2)",
            "M^-2": "only m_(h-2)=1, m_(h-1)=m_h=0 and D_5=0",
            "M^-3": (
                "generic D_5 Euler correction, profile (h-2,h-2,2h+5) "
                "with D_5=0, and profile (h-2,h-1,2h+4) with D_5+D_3=0"
            ),
            "M^-4_or_lower": ("all other parity-even profiles, including D_5+2D_1"),
        },
        "local_law": {
            "independent_sign_counts": "N_r=I_q(r), 1<=r<=5",
            "D3": "S3+S1*S2+h3(S1;N1)-q*S1",
            "D5": (
                "S5+S1*S4+S2*S3+h2(S1;N1)S3+h2(S2;N2)S1+"
                "h3(S1;N1)S2+h5(S1;N1)-q*(S3+S1*S2+h3(S1;N1))"
            ),
            "delta_5_q": "Prob(D_5=0)",
            "delta_53_q": "Prob(D_5+D_3=0)",
            "both_probabilities_positive_for_every_odd_q": True,
            "q3": {
                "delta_5": str(delta5_q3),
                "delta_53": str(delta53_q3),
            },
        },
        "fixed_q_asymptotic": {
            "count_over_q^M": (
                "delta_5,q*(1+log(2))/(3h^2)+"
                "[delta_5,q*(5+2log(2))/6+delta_53,q/2]/h^3+O_q(h^-4)"
            ),
            "squarefree_density": (
                "[16*delta_5,q*(1+log(2))/(3M^2)+"
                "32*(delta_5,q*(2+log(2))+delta_53,q)/M^3+O_q(M^-4)]/"
                "(1-q^-1)"
            ),
            "h_minus_2_profile_coefficient": affine_render(H_MINUS_2),
            "h_minus_3_generic": affine_render(H_MINUS_3_GENERIC),
            "h_minus_3_repeated_minimum": str(H_MINUS_3_REPEATED_MINIMUM),
            "h_minus_3_mixed": str(H_MINUS_3_MIXED),
            "h_minus_3_D5_total": affine_render(H_MINUS_3_D5_TOTAL),
        },
        "profile_replay": {
            "h_min": MIN_H,
            "h_max": PROFILE_MAX_H,
            "profiles_checked": profiles_checked,
            "rows": profile_rows,
        },
        "positivity_witnesses": {
            "formula": ("S1=1, S2=N2 mod 2, S3=S4=0; choose S5 to cancel D5 or D5+D3"),
            "bounded_symbolic_checks": witnesses,
        },
        "claim_boundary": {
            "raw_detector_zero_asymptotic_proved": True,
            "input_theorem": "standard fixed-modulus prime-polynomial progression theorem",
            "individual_L_function_zero": False,
            "rh_or_grh": False,
            "external_priority_claim": False,
        },
        "resource_caps": {
            "maximum_profile_h": PROFILE_MAX_H,
            "profiles_checked": profiles_checked,
            "maximum_local_probability_q": LOCAL_Q_MAX,
            "maximum_positivity_witness_q": max(WITNESS_Q_VALUES),
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
