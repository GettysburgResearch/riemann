"""Exact model/stack/coarse-orbit comparison for the genus-two family.

This module consumes the frozen affine-orbit certificate only.  It does not
enumerate a finite field or rebuild a curve family.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Mapping


HERE = Path(__file__).resolve().parent
AFFINE_FIXTURE = HERE / "genus2_affine_orbits.json"
FROZEN_Q_VALUES = (3, 5, 7)
MAX_INPUT_BYTES = 200_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _integer_histogram(raw: Mapping[str, object]) -> dict[int, int]:
    histogram = {int(key): int(value) for key, value in raw.items()}
    if any(key <= 0 or value <= 0 for key, value in histogram.items()):
        raise ArithmeticError("orbit histograms must have positive keys and counts")
    return histogram


def _prime_characteristic(q: int) -> int:
    """Return p when q is a prime power p^r, and refuse other integers."""

    if q < 2:
        raise ValueError("q must be a prime power")
    for candidate in range(2, isqrt(q) + 1):
        if q % candidate:
            continue
        if any(candidate % divisor == 0 for divisor in range(2, isqrt(candidate) + 1)):
            continue
        residue = q
        while residue % candidate == 0:
            residue //= candidate
        if residue != 1:
            raise ValueError("q must be a prime power")
        return candidate
    return q


def burnside_census(q: int) -> dict[str, object]:
    """Return the all-q fixed-point contributions for the affine action."""

    characteristic = _prime_characteristic(q)
    if characteristic == 2:
        raise ValueError("the Burnside classification is proved only for odd q")
    group_order = q * (q - 1)
    contributions = {
        "identity": q**4 * (q - 1),
        "order_2_scalings": q * (q - 1) ** 2,
        "order_4_scalings": 2 * q * (q - 1) if (q - 1) % 4 == 0 else 0,
        "order_5_scalings": 4 * q * (q - 1) if (q - 1) % 5 == 0 else 0,
        "nonidentity_translations": q * (q - 1) if characteristic == 5 else 0,
    }
    numerator = sum(contributions.values())
    if numerator % group_order:
        raise ArithmeticError("Burnside numerator is not divisible by the group order")
    orbit_count = numerator // group_order
    closed_formula = (
        q**3
        + q
        - 1
        + 2 * int((q - 1) % 4 == 0)
        + 4 * int((q - 1) % 5 == 0)
        + int(characteristic == 5)
    )
    if orbit_count != closed_formula:
        raise ArithmeticError("Burnside census and closed orbit formula disagree")
    return {
        "characteristic": characteristic,
        "fixed_point_contribution_sums": contributions,
        "all_other_nonidentity_elements_contribute": 0,
        "burnside_numerator": numerator,
        "orbit_count": orbit_count,
        "closed_formula_value": closed_formula,
    }


def build_fixture(
    *,
    affine_fixture: Path = AFFINE_FIXTURE,
    maximum_input_bytes: int = MAX_INPUT_BYTES,
) -> dict[str, object]:
    """Build the exact measure-comparison certificate from frozen orbit totals."""

    if not 0 < maximum_input_bytes <= MAX_INPUT_BYTES:
        raise ValueError(f"input-byte cap must lie in (0,{MAX_INPUT_BYTES}]")
    raw = affine_fixture.read_bytes()
    if len(raw) > maximum_input_bytes:
        raise ValueError(
            f"affine fixture has {len(raw)} bytes, above cap {maximum_input_bytes}"
        )
    affine = json.loads(raw.decode("utf-8"))
    affine_without_hash = dict(affine)
    affine_payload_hash = affine_without_hash.pop("payload_sha256")
    if affine_payload_hash != _canonical_sha256(affine_without_hash):
        raise ArithmeticError("affine fixture payload hash mismatch")

    families: list[dict[str, object]] = []
    for family in affine["families"]:
        q = int(family["q"])
        member_count = int(family["member_count"])
        group_order = int(family["group"]["order"])
        orbit_partition = family["orbit_partition"]
        orbit_count = int(orbit_partition["orbit_count"])
        orbit_sizes = _integer_histogram(orbit_partition["orbit_size_histogram"])
        stabilizers = _integer_histogram(
            orbit_partition["stabilizer_order_histogram"]
        )

        if member_count != q**5 - q**4:
            raise ArithmeticError(f"q={q} member count is not q^5-q^4")
        if group_order != q * (q - 1):
            raise ArithmeticError(f"q={q} affine group order mismatch")
        if sum(orbit_sizes.values()) != orbit_count:
            raise ArithmeticError(f"q={q} orbit-size histogram count mismatch")
        if sum(size * count for size, count in orbit_sizes.items()) != member_count:
            raise ArithmeticError(f"q={q} orbit sizes do not recover the family")
        if sum(stabilizers.values()) != orbit_count:
            raise ArithmeticError(f"q={q} stabilizer histogram count mismatch")
        for stabilizer, count in stabilizers.items():
            if group_order % stabilizer:
                raise ArithmeticError(f"q={q} stabilizer does not divide group order")
            if orbit_sizes.get(group_order // stabilizer) != count:
                raise ArithmeticError(f"q={q} orbit/stabilizer histograms disagree")

        stack_cardinality = Fraction(member_count, group_order)
        if stack_cardinality != q**3:
            raise ArithmeticError(f"q={q} quotient stack mass is not q^3")
        burnside = burnside_census(q)
        if burnside["orbit_count"] != orbit_count:
            raise ArithmeticError(f"q={q} Burnside orbit formula mismatch")
        orbit_excess = orbit_count - q**3
        if orbit_excess <= 0:
            raise ArithmeticError(f"q={q} coarse orbit excess must be positive")

        total_variation = sum(
            count
            * abs(Fraction(1, orbit_count) - Fraction(size, member_count))
            for size, count in orbit_sizes.items()
        ) / 2
        free_orbit_count = stabilizers.get(1, 0)
        exact_tv_from_free_deficit = Fraction(
            free_orbit_count * orbit_excess,
            q**3 * orbit_count,
        )
        if total_variation != exact_tv_from_free_deficit:
            raise ArithmeticError(f"q={q} total-variation identity failed")
        universal_tv_upper_bound = Fraction(orbit_excess, q**3)
        if total_variation > universal_tv_upper_bound:
            raise ArithmeticError(f"q={q} total-variation upper bound failed")
        nonfree_orbit_count = sum(
            count for size, count in orbit_sizes.items() if size != group_order
        )
        nonfree_member_count = sum(
            size * count
            for size, count in orbit_sizes.items()
            if size != group_order
        )

        stabilizer_strata = []
        for stabilizer in sorted(stabilizers):
            orbit_size = group_order // stabilizer
            stabilizer_strata.append(
                {
                    "stabilizer_order": stabilizer,
                    "orbit_size": orbit_size,
                    "orbit_count": stabilizers[stabilizer],
                    "uniform_orbit_weight_each": _fraction(Fraction(1, orbit_count)),
                    "stack_weight_each": _fraction(Fraction(1, stabilizer * q**3)),
                    "coarse_to_stack_weight_ratio": _fraction(
                        Fraction(stabilizer * q**3, orbit_count)
                    ),
                }
            )

        sign_rows: dict[str, object] = {}
        for sign in ("negative", "zero", "positive"):
            row = family["sign_summaries"][sign]
            sign_orbits = int(row["orbit_count"])
            sign_members = int(row["member_count"])
            coarse = Fraction(sign_orbits, orbit_count)
            model_stack = Fraction(sign_members, member_count)
            sign_rows[sign] = {
                "orbit_count": sign_orbits,
                "member_count": sign_members,
                "uniform_coarse_orbit_fraction": _fraction(coarse),
                "uniform_model_equals_affine_stack_fraction": _fraction(model_stack),
                "coarse_minus_model_affine_stack": _fraction(coarse - model_stack),
            }
        if sum(row["orbit_count"] for row in sign_rows.values()) != orbit_count:
            raise ArithmeticError(f"q={q} sign orbits do not recover all orbits")
        if sum(row["member_count"] for row in sign_rows.values()) != member_count:
            raise ArithmeticError(f"q={q} sign members do not recover the family")

        families.append(
            {
                "q": q,
                "member_count": member_count,
                "group_order": group_order,
                "orbit_count": orbit_count,
                "quotient_stack_cardinality": _fraction(stack_cardinality),
                "burnside_census": burnside,
                "coarse_orbit_excess_over_stack_mass": orbit_excess,
                "total_variation_uniform_orbits_vs_model_affine_stack": _fraction(
                    total_variation
                ),
                "total_variation_from_free_orbit_deficit": _fraction(
                    exact_tv_from_free_deficit
                ),
                "universal_total_variation_upper_bound": _fraction(
                    universal_tv_upper_bound
                ),
                "nonfree_locus": {
                    "orbit_count": nonfree_orbit_count,
                    "member_count": nonfree_member_count,
                    "uniform_orbit_fraction": _fraction(
                        Fraction(nonfree_orbit_count, orbit_count)
                    ),
                    "uniform_model_equals_affine_stack_fraction": _fraction(
                        Fraction(nonfree_member_count, member_count)
                    ),
                },
                "stabilizer_strata": stabilizer_strata,
                "sign_measures": sign_rows,
            }
        )

    if tuple(row["q"] for row in families) != FROZEN_Q_VALUES:
        raise ArithmeticError(f"expected frozen q values {FROZEN_Q_VALUES}")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_family_measures.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.AFFINE_MODEL_MEASURES.Q3_Q5_Q7.V1",
        "rigor_level": "RIGOROUS_ALL_ODD_Q_LEMMA_WITH_FROZEN_FINITE_COMPARISONS",
        "status": "EXACT_STACK_IDENTITY_WITH_FROZEN_MEASURE_COMPARISONS",
        "theorem": {
            "family": "H_5(q), monic squarefree quintics over F_q",
            "group": "AGL(1,F_q) acting by D(T)->alpha^(-5)D(alpha*T+beta)",
            "all_q_scope": "every odd prime power q",
            "stack_cardinality": "sum_[D] 1/|Stab(D)|=q^3",
            "invariant_average": (
                "|H_5(q)|^(-1) sum_D f(D)="
                "q^(-3) sum_[D] f(D)/|Stab(D)|"
            ),
            "hypothesis_on_f": "f is invariant under the declared AGL(1,F_q) action",
            "proof": (
                "|H_5(q)|=q^4(q-1), |AGL(1,q)|=q(q-1), and "
                "orbit-stabilizer gives |Orbit(D)|=|G|/|Stab(D)|"
            ),
            "coarse_orbit_count": (
                "q^3+q-1+2*1_(4 divides q-1)+4*1_(5 divides q-1)"
                "+1_(characteristic(q)=5)"
            ),
            "burnside_fixed_shapes": {
                "order_2": "S^5+c3*S^3+c1*S, squarefree for (q-1)^2 pairs",
                "order_3": "S^5+c2*S^2, never squarefree",
                "order_4": "S^5+c1*S, squarefree for q-1 nonzero c1",
                "order_5": "S^5+c0, squarefree for q-1 nonzero c0",
                "translations": (
                    "none unless characteristic 5; then S^5-beta^4*S+c0 "
                    "gives q squarefree fixed polynomials per nonzero translation"
                ),
                "other_scaling_orders": "only S^5 is fixed, hence not squarefree",
            },
            "measure_comparison": {
                "orbit_excess": (
                    "delta_q=N_q-q^3=q-1+2*1_(4 divides q-1)"
                    "+4*1_(5 divides q-1)+1_(characteristic(q)=5)"
                ),
                "total_variation_bound": "TV(uniform coarse orbits, stack)<=delta_q/q^3",
                "asymptotic_rate": "O(q^(-2))",
                "bounded_invariant_consequence": (
                    "for |f|<=M, |E_coarse(f)-E_stack(f)|<=2*M*delta_q/q^3"
                ),
            },
        },
        "producer": {
            "script": "genus2_family_measures.py",
            "source_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "affine_fixture": affine_fixture.name,
            "affine_fixture_canonical_sha256": _canonical_sha256(affine),
            "affine_fixture_payload_sha256": affine_payload_hash,
        },
        "resource_contract": {
            "field_enumeration": False,
            "input_byte_cap": maximum_input_bytes,
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "arithmetic": "exact integers and fractions",
        },
        "families": families,
        "scope": {
            "not_the_full_curve_isomorphism_stack": True,
            "marked_infinity_affine_model_quotient_only": True,
            "frozen_measure_distortions_are_not_asymptotic_laws": True,
            "not_an_equidistribution_or_number_field_transfer": True,
            "interpretation": (
                "Uniform polynomial models already equal stabilizer-weighted stack "
                "averaging for this affine quotient; uniform orbit representatives "
                "define a different and generally biased family measure."
            ),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare with an exact JSON fixture")
    parser.add_argument("--write", type=Path, help="write the exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"genus-two family-measure fixture mismatch: {args.check}")
        print(f"OK: exact genus-two family measures match {args.check}")
    elif args.write:
        args.write.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE: {args.write}")
    else:
        print(json.dumps(fixture, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
