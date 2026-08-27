#!/usr/bin/env python3
"""Bounded exact replay for Boolean Frobenius tomography."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_BLOBS = {
    (
        "7a54822cb9b20f331edb6f40b2276618c496c1cb",
        (
            "research/l-families/atlas/function_field/"
            "FUNCTION_FIELD_BETA_BOOLEAN_EVALUATION_BANDPASS.md"
        ),
    ): "0306cfa06c68375dd62472073698aaae0ace0ff9",
    (
        "7a54822cb9b20f331edb6f40b2276618c496c1cb",
        (
            "research/l-families/atlas/function_field/"
            "function_field_beta_boolean_evaluation_bandpass.py"
        ),
    ): "5ab6b5845838495362bb37883386b640e6a8900d",
    (
        "8192514ed68f50b8e2a9cff9e1bedab2478bb5c1",
        (
            "research/l-families/atlas/function_field/"
            "FUNCTION_FIELD_FROBENIUS_CHANNEL_FILTER_CALCULUS.md"
        ),
    ): "182fee0619e3a78b9e8d9435d921293328c37668",
    (
        "8192514ed68f50b8e2a9cff9e1bedab2478bb5c1",
        (
            "research/l-families/atlas/function_field/"
            "function_field_frobenius_channel_filter_calculus.py"
        ),
    ): "f349df947adecf99dec4558a99741d1b26641934",
}

Polynomial = tuple[Fraction, ...]
Profile = dict[str, int]


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
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def _validate_profile(profile: Profile, name: str) -> None:
    for orbit, multiplicity in profile.items():
        if not isinstance(orbit, str) or not orbit:
            raise ValueError(f"{name} orbit names must be nonempty strings")
        if (
            isinstance(multiplicity, bool)
            or not isinstance(multiplicity, int)
            or multiplicity < 0
        ):
            raise ValueError(f"{name} multiplicities must be nonnegative integers")


def _validate_orbit_degrees(orbit_degrees: Profile) -> None:
    _validate_profile(orbit_degrees, "orbit degree")
    if any(degree == 0 for degree in orbit_degrees.values()):
        raise ValueError("orbit degrees must be positive integers")


def residual_profile(surviving: Profile, filter_orders: Profile) -> Profile:
    _validate_profile(surviving, "surviving")
    _validate_profile(filter_orders, "filter")
    return {
        orbit: max(multiplicity - filter_orders.get(orbit, 0), 0)
        for orbit, multiplicity in surviving.items()
        if max(multiplicity - filter_orders.get(orbit, 0), 0)
    }


def member_minimal_filter(
    surviving: Profile,
    retained: Profile,
    orbit_degrees: Profile,
) -> dict[str, object]:
    """Return the primitive additional filter selecting one retained profile."""

    _validate_profile(surviving, "surviving")
    _validate_profile(retained, "retained")
    _validate_orbit_degrees(orbit_degrees)
    retained = {orbit: value for orbit, value in retained.items() if value}
    if set(retained) - set(surviving):
        raise ValueError("a retained orbit must occur in the surviving denominator")
    filter_orders: Profile = {}
    for orbit, multiplicity in surviving.items():
        wanted = retained.get(orbit, 0)
        if wanted > multiplicity:
            raise ValueError("a polynomial filter cannot resurrect a deleted pole")
        order = multiplicity - wanted
        if order:
            filter_orders[orbit] = order
    missing_degrees = set(filter_orders) - set(orbit_degrees)
    if missing_degrees:
        raise ValueError(f"missing orbit degrees: {sorted(missing_degrees)}")
    degree = sum(orbit_degrees[orbit] * order for orbit, order in filter_orders.items())
    if residual_profile(surviving, filter_orders) != {
        orbit: value for orbit, value in retained.items() if value
    }:
        raise ArithmeticError("minimal member filter failed its retained profile")
    return {
        "filter_degree": degree,
        "filter_orders": filter_orders,
        "retained_profile": {
            orbit: value for orbit, value in retained.items() if value
        },
    }


def universal_filter_trilemma(
    surviving_rows: tuple[Profile, ...],
    retained_rows: tuple[Profile, ...],
    orbit_degrees: Profile,
) -> dict[str, object]:
    """Solve the exact orbitwise scalar-filter compatibility problem."""

    if not surviving_rows or len(surviving_rows) != len(retained_rows):
        raise ValueError(
            "surviving and retained families must have equal positive size"
        )
    _validate_orbit_degrees(orbit_degrees)
    for row in surviving_rows:
        _validate_profile(row, "surviving")
    for row in retained_rows:
        _validate_profile(row, "retained")
    retained_rows = tuple(
        {orbit: value for orbit, value in row.items() if value} for row in retained_rows
    )
    orbits = sorted(set().union(*(set(row) for row in surviving_rows)))
    if set().union(*(set(row) for row in retained_rows)) - set(orbits):
        raise ValueError("a retained orbit must occur in a family denominator")

    filter_orders: Profile = {}
    orbit_cases: dict[str, dict[str, object]] = {}
    conflicts: list[str] = []
    for orbit in orbits:
        positive_demands: list[int] = []
        deletion_lower_bound = 0
        for index, (surviving, retained) in enumerate(
            zip(surviving_rows, retained_rows, strict=True)
        ):
            multiplicity = surviving.get(orbit, 0)
            wanted = retained.get(orbit, 0)
            if wanted > multiplicity:
                conflicts.append(
                    f"{orbit}: member {index} asks to resurrect {wanted}>{multiplicity}"
                )
                continue
            if wanted:
                positive_demands.append(multiplicity - wanted)
            else:
                deletion_lower_bound = max(deletion_lower_bound, multiplicity)

        distinct_demands = sorted(set(positive_demands))
        if len(distinct_demands) > 1:
            conflicts.append(
                f"{orbit}: incompatible exact orders {distinct_demands} from retained modes"
            )
            orbit_cases[orbit] = {
                "case": "incompatible retained-mode orders",
                "deletion_lower_bound": deletion_lower_bound,
                "positive_exact_orders": distinct_demands,
            }
            continue
        if distinct_demands:
            exact_order = distinct_demands[0]
            if exact_order < deletion_lower_bound:
                conflicts.append(
                    f"{orbit}: exact retained order {exact_order} is below deletion bound "
                    f"{deletion_lower_bound}"
                )
                orbit_cases[orbit] = {
                    "case": "retention/deletion conflict",
                    "deletion_lower_bound": deletion_lower_bound,
                    "positive_exact_orders": distinct_demands,
                }
                continue
            order = exact_order
            case = "unique retained-mode order"
        else:
            order = deletion_lower_bound
            case = "lcm deletion order"
        if order:
            filter_orders[orbit] = order
        orbit_cases[orbit] = {
            "case": case,
            "deletion_lower_bound": deletion_lower_bound,
            "positive_exact_orders": distinct_demands,
            "selected_filter_order": order,
        }

    missing_degrees = set(filter_orders) - set(orbit_degrees)
    if missing_degrees:
        raise ValueError(f"missing orbit degrees: {sorted(missing_degrees)}")
    if conflicts:
        return {
            "conflicts": conflicts,
            "feasible": False,
            "orbit_cases": orbit_cases,
        }

    residual_rows = tuple(
        residual_profile(row, filter_orders) for row in surviving_rows
    )
    normalized_retained = tuple(
        {orbit: value for orbit, value in row.items() if value} for row in retained_rows
    )
    if residual_rows != normalized_retained:
        raise ArithmeticError("universal filter did not realize every retained profile")
    degree = sum(orbit_degrees[orbit] * order for orbit, order in filter_orders.items())
    return {
        "feasible": True,
        "filter_degree": degree,
        "filter_orders": filter_orders,
        "orbit_cases": orbit_cases,
        "residual_profiles": residual_rows,
    }


def galois_stable_selection(
    orbit_blocks: tuple[tuple[str, ...], ...], selected_roots: frozenset[str]
) -> bool:
    roots = {root for block in orbit_blocks for root in block}
    if not selected_roots <= roots:
        raise ValueError("selected roots must belong to a declared Galois orbit")
    return all(
        not (selected_roots & set(block)) or set(block) <= selected_roots
        for block in orbit_blocks
    )


def _trim(poly: Polynomial) -> Polynomial:
    values = list(poly)
    while len(values) > 1 and not values[-1]:
        values.pop()
    return tuple(values)


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            out[left_index + right_index] += left_value * right_value
    return _trim(tuple(out))


def polynomial_power(poly: Polynomial, exponent: int) -> Polynomial:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("polynomial exponent must be a nonnegative integer")
    out: Polynomial = (Fraction(1),)
    for _ in range(exponent):
        out = polynomial_multiply(out, poly)
    return out


def rational_series(
    numerator: Polynomial, denominator: Polynomial, horizon: int
) -> tuple[Fraction, ...]:
    if not denominator or denominator[0] != 1:
        raise ValueError("denominator must have constant coefficient one")
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a nonnegative integer")
    coefficients: list[Fraction] = []
    for degree in range(horizon + 1):
        value = numerator[degree] if degree < len(numerator) else Fraction(0)
        for offset in range(1, min(degree, len(denominator) - 1) + 1):
            value -= denominator[offset] * coefficients[degree - offset]
        coefficients.append(value)
    return tuple(coefficients)


def energy(values: tuple[Fraction, ...]) -> Fraction:
    return sum((value * value for value in values), start=Fraction(0))


def formal_energy_control(horizon: int = 40) -> dict[str, object]:
    """Replay a degree-five formal conductor with one retained double root."""

    linear: Polynomial = (Fraction(1), Fraction(1))
    quadratic: Polynomial = (Fraction(1), Fraction(0), Fraction(1))
    original_character_denominator = polynomial_multiply(
        polynomial_power(linear, 2), quadratic
    )
    adaptive_filter = quadratic
    retained_denominator = polynomial_power(linear, 2)
    beta_numerator: Polynomial = (Fraction(1), Fraction(1, 3))
    character = rational_series(beta_numerator, retained_denominator, horizon)

    expected_character = tuple(
        Fraction(1) if degree == 0 else (-1) ** degree * (Fraction(2 * degree, 3) + 1)
        for degree in range(horizon + 1)
    )
    if character != expected_character:
        raise ArithmeticError("retained double-root coefficient formula failed")
    character_energy = energy(character)
    exact_energy_polynomial = (
        Fraction(4, 27) * horizon**3
        + Fraction(8, 9) * horizon**2
        + Fraction(47, 27) * horizon
        + 1
    )
    if character_energy != exact_energy_polynomial:
        raise ArithmeticError("retained double-root energy polynomial failed")

    trivial_numerator = polynomial_multiply(
        adaptive_filter,
        polynomial_multiply(
            (Fraction(1), Fraction(-1, 3)),
            (Fraction(1), Fraction(-3)),
        ),
    )
    trivial_denominator: Polynomial = (
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(-1, 243),
    )
    trivial = rational_series(trivial_numerator, trivial_denominator, horizon)
    plus = tuple((t + c) / 2 for t, c in zip(trivial, character, strict=True))
    minus = tuple((t - c) / 2 for t, c in zip(trivial, character, strict=True))
    positive_energy = energy(plus) + energy(minus)
    separated_energy = (energy(trivial) + character_energy) / 2
    if positive_energy != separated_energy:
        raise ArithmeticError("Boolean positive-energy separation failed")
    if tuple(p + m for p, m in zip(plus, minus, strict=True)) != trivial:
        raise ArithmeticError("coherent Boolean symmetric channel failed")
    if tuple(p - m for p, m in zip(plus, minus, strict=True)) != character:
        raise ArithmeticError("coherent Boolean antisymmetric channel failed")

    return {
        "adaptive_filter": [str(value) for value in adaptive_filter],
        "beta_numerator": [str(value) for value in beta_numerator],
        "character_energy": str(character_energy),
        "character_energy_polynomial": "4*H^3/27 + 8*H^2/9 + 47*H/27 + 1",
        "character_leading_energy_coefficient": "4/27",
        "formal_conductor_degree": 5,
        "horizon": horizon,
        "normalized_character_denominator_before_filter": [
            str(value) for value in original_character_denominator
        ],
        "positive_boolean_leading_energy_coefficient": "2/27",
        "positive_energy_identity_verified": positive_energy == separated_energy,
        "retained_denominator": [str(value) for value in retained_denominator],
        "retained_principal_coefficient": "2/3",
        "scope": "formal Weil-circle polynomial; no modulus realization claim",
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    degrees = {"a": 1, "b": 2, "c": 2}
    surviving = (
        {"a": 2, "b": 1},
        {"a": 3, "c": 1},
    )
    retained = (
        {"a": 1},
        {"a": 2},
    )
    member_rows = tuple(
        member_minimal_filter(source, target, degrees)
        for source, target in zip(surviving, retained, strict=True)
    )
    compatible = universal_filter_trilemma(surviving, retained, degrees)
    full_deletion = universal_filter_trilemma(surviving, ({}, {}), degrees)
    retention_deletion_conflict = universal_filter_trilemma(
        surviving,
        ({"a": 1}, {}),
        degrees,
    )
    unequal_retention_conflict = universal_filter_trilemma(
        surviving,
        ({"a": 1}, {"a": 1}),
        degrees,
    )
    return {
        "source_contract": {
            "git_blobs": {
                f"{commit}:{path}": blob
                for (commit, path), blob in SOURCE_BLOBS.items()
            },
            "imported_nonvanishing": (
                "the literal beta numerator 1-chi(P)q^(-e/2)z^e has no zero on |z|=1"
            ),
        },
        "theorem": {
            "member_minimality": (
                "after any prefilter, an additional polynomial filter selects "
                "a retained Frobenius orbit profile r from the surviving "
                "profile s with the unique primitive orders s-r"
            ),
            "universal_trilemma": (
                "on each coefficient-field Galois orbit, either all members "
                "delete it and the lcm/max order is minimal; all positive "
                "retention requests impose one compatible exact order which "
                "dominates deletion requests; or no scalar universal filter exists"
            ),
            "positive_energy_firewall": (
                "coherent class sum/difference isolates trivial/character "
                "channels, while the sum of the two positive class energies "
                "retains one half of each channel energy"
            ),
        },
        "bounded_controls": {
            "compatible_family": compatible,
            "full_deletion_lcm": full_deletion,
            "galois_descent": {
                "conjugate_pair_selected_together": galois_stable_selection(
                    (("i", "-i"),), frozenset(("i", "-i"))
                ),
                "single_conjugate_selected_over_Q": galois_stable_selection(
                    (("i", "-i"),), frozenset(("i",))
                ),
            },
            "member_filters": member_rows,
            "retention_deletion_conflict": retention_deletion_conflict,
            "unequal_retention_conflict": unequal_retention_conflict,
        },
        "formal_energy_control": formal_energy_control(),
        "proof_ledger": {
            "all_curve_boolean_hadamard_split": "IMPORTED EXACT",
            "beta_unit_circle_numerator_nonvanishing": "IMPORTED EXACT",
            "member_adaptive_minimality": "PROVED EXACT BY ORBIT VALUATIONS",
            "finite_family_universal_trilemma": "PROVED EXACT BY ORBIT VALUATIONS",
            "full_deletion_lcm_corollary": "PROVED EXACT WITHOUT GENERICITY",
            "galois_descent_criterion": "PROVED BY COEFFICIENT-FIELD FACTORIZATION",
            "residue_and_energy_signature": "PROVED BY PARTIAL FRACTIONS",
            "formal_double_root_energy_control": "REPLAYED EXACT",
            "number_field_transfer": "NOT CLAIMED",
            "rh_or_grh": "NOT PROVED",
        },
        "scope": {
            "coefficient_field": (
                "factor normalized Frobenius polynomials over a field containing "
                "their coefficients and sqrt(q); over a smaller field the scaled "
                "filter polynomial itself must descend"
            ),
            "family": "finite family over one fixed q and coefficient field",
            "energy_analytic_gap": (
                "the global H^(2M-1) energy asymptotic assumes every "
                "non-weight-one inverse-L singularity lies outside some "
                "circle |z|=R_0>1; local orbit minimality needs only "
                "nonvanishing at the selected unit-circle roots"
            ),
            "function_field_rh": (
                "used only to place the relevant weight-one roots on |z|=1"
            ),
            "tomography_limit": (
                "a polynomial filter can delete surviving modes but cannot "
                "resurrect a mode already removed by the prefilter"
            ),
        },
        "resource_caps": {
            "curve_enumeration": 0,
            "finite_field_element_enumeration": 0,
            "formal_series_horizon": 40,
            "l_functions_enumerated": 0,
            "moduli_enumerated": 0,
            "point_counts": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    if not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
