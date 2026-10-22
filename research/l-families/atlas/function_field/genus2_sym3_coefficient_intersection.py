"""Exact intersection of a locked genus-two lattice with the Sym^3 curve.

This packet performs no curve or finite-field enumeration.  It transforms the
251 joint ``(a_D,b_D)`` atoms already frozen in
``balanced_control_family_scan.json`` and uses the independently frozen
elliptic trace witnesses in ``elliptic_symmetric_cube_family.json``.
Everything here is integer or rational algebra.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym3_coefficient_intersection.json"
NOTE_PATH = HERE / "GENUS2_SYM3_COEFFICIENT_INTERSECTION.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym3_coefficient_intersection.py"

BALANCED_FIXTURE = HERE / "balanced_control_family_scan.json"
BALANCED_SOURCE = HERE / "balanced_control_family_scan.py"
SYM3_FIXTURE = HERE / "elliptic_symmetric_cube_family.json"
SYM3_SOURCE = HERE / "elliptic_symmetric_cube_family.py"

EXPECTED_BALANCED_SCHEMA = "riemann.function_field.balanced_control_family_scan.v1"
EXPECTED_BALANCED_PAYLOAD_SHA256 = (
    "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c"
)
EXPECTED_BALANCED_FILE_SHA256_LF = (
    "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e"
)
EXPECTED_BALANCED_SOURCE_SHA256_LF = (
    "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b"
)

EXPECTED_SYM3_SCHEMA = "riemann.function_field.elliptic_symmetric_cube_family.v1"
EXPECTED_SYM3_PAYLOAD_SHA256 = (
    "7e30dd220b9c9e3a3873ffe8b168ad53af4899de1dd21a2d69e2498abc6ee5b9"
)
EXPECTED_SYM3_FILE_SHA256_LF = (
    "2b8b7f206c4e4c24f4e1ac65d093ab976dd6483dceb6ea52f44e76a7004bb033"
)
EXPECTED_SYM3_SOURCE_SHA256_LF = (
    "1a99107771a804f39c6d3b26b0b1e67ad385500ce6776f2e14cfe6bf7b810d26"
)

FROZEN_Q_VALUES = (3, 5, 7)
MAX_SOURCE_ATOMS = 300
MAX_SOURCE_MEMBERS = 20_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


def _fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _load_locked_fixture(
    path: Path,
    *,
    schema: str,
    payload_sha256: str,
    file_sha256_lf: str,
) -> dict[str, object]:
    if _lf_sha256(path) != file_sha256_lf:
        raise RuntimeError(f"locked fixture file changed: {path.name}")
    fixture = json.loads(path.read_text(encoding="utf-8"))
    if fixture.get("schema") != schema:
        raise RuntimeError(f"locked fixture schema changed: {path.name}")
    if fixture.get("payload_sha256") != payload_sha256:
        raise RuntimeError(f"locked fixture payload identity changed: {path.name}")
    unhashed = dict(fixture)
    claimed = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
        raise RuntimeError(f"locked fixture is internally inauthentic: {path.name}")
    return fixture


def load_sources() -> tuple[dict[str, object], dict[str, object]]:
    """Load both authenticated upstream artifacts and enforce their source locks."""

    balanced = _load_locked_fixture(
        BALANCED_FIXTURE,
        schema=EXPECTED_BALANCED_SCHEMA,
        payload_sha256=EXPECTED_BALANCED_PAYLOAD_SHA256,
        file_sha256_lf=EXPECTED_BALANCED_FILE_SHA256_LF,
    )
    sym3 = _load_locked_fixture(
        SYM3_FIXTURE,
        schema=EXPECTED_SYM3_SCHEMA,
        payload_sha256=EXPECTED_SYM3_PAYLOAD_SHA256,
        file_sha256_lf=EXPECTED_SYM3_FILE_SHA256_LF,
    )
    if _lf_sha256(BALANCED_SOURCE) != EXPECTED_BALANCED_SOURCE_SHA256_LF:
        raise RuntimeError("locked balanced-control producer changed")
    if _lf_sha256(SYM3_SOURCE) != EXPECTED_SYM3_SOURCE_SHA256_LF:
        raise RuntimeError("locked Sym^3 producer changed")

    definition = balanced.get("definition", {})
    if definition.get("coefficient_normalization") != (
        "L_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4"
    ):
        raise RuntimeError("balanced-control coefficient normalization changed")
    q_values = tuple(balanced["frozen_enumeration_facts"]["q_values"])  # type: ignore[index]
    if q_values != FROZEN_Q_VALUES:
        raise RuntimeError("balanced-control frozen q values changed")

    normalization = sym3.get("normalization", {})
    if normalization.get("normalized_sym3_trace_x") != "x=t0^3-2t0":
        raise RuntimeError("Sym^3 trace normalization changed")
    if normalization.get("normalized_second_coefficient_y") != (
        "y=t0^4-3t0^2+2"
    ):
        raise RuntimeError("Sym^3 second-coefficient normalization changed")
    return balanced, sym3


def scaled_curve_residual(a: int, b: int, q: int) -> int:
    """q^3 F(-a/sqrt(q), b/q) for the Sym^3 coefficient curve."""

    if q <= 0:
        raise ValueError("q must be positive")
    return -q * a**4 + q * a * a * b + q * q * a * a + b**3 - 2 * q * b * b


def generic_trace_parameter(a: int, b: int, q: int) -> Fraction:
    """Recover t=sqrt(q)t0 away from the nodal divisor a^2=b."""

    denominator = a * a - b
    if denominator == 0:
        raise ValueError("generic inverse is undefined on a^2=b")
    return Fraction(a * (q - b), denominator)


def shape_from_trace(t: int, q: int) -> tuple[Fraction, Fraction]:
    """Return the genus-two-scale coefficient shape induced by trace t."""

    if q <= 0:
        raise ValueError("q must be positive")
    return (
        Fraction(2 * q * t - t**3, q),
        Fraction(t**4 - 3 * q * t * t + 2 * q * q, q),
    )


def is_integral_hasse_parameter(t: Fraction, q: int) -> bool:
    """Necessary arithmetic test, exact and without square roots or floats."""

    return t.denominator == 1 and t.numerator * t.numerator <= 4 * q


def odd_prime_integral_shape_trace_candidates(p: int) -> tuple[int, ...]:
    """Prime-q classification after q | t^3 and the Hasse bound.

    The function validates primality only for its bounded research use.  The
    mathematical proof in the artifact is uniform in every odd prime.
    """

    if p < 3 or p % 2 == 0:
        raise ValueError("p must be an odd prime")
    if any(p % divisor == 0 for divisor in range(3, math.isqrt(p) + 1, 2)):
        raise ValueError("p must be an odd prime")
    return (-3, 0, 3) if p == 3 else (0,)


def _sym3_source_trace_witnesses(
    sym3: Mapping[str, object],
) -> dict[int, dict[int, int]]:
    """Positive-count elliptic witnesses, keyed first by q and then by trace."""

    output: dict[int, dict[int, int]] = {}
    for family in sym3["frozen_histogram_transforms"]:  # type: ignore[index]
        q = int(family["q"])
        output[q] = {
            int(atom["source_geometric_trace_t"]): int(atom["member_count"])
            for atom in family["transformed_atoms"]
            if int(atom["member_count"]) > 0
        }
    return output


def classify_atom(
    a: int,
    b: int,
    q: int,
    source_trace_witnesses: Mapping[int, int],
) -> dict[str, object]:
    """Classify one lattice atom with exact generic and nodal branches."""

    residual = scaled_curve_residual(a, b, q)
    divisor = a * a - b
    base: dict[str, object] = {
        "scaled_curve_residual": residual,
        "on_compact_sym3_curve": residual == 0,
        "nodal_divisor_a2_minus_b": divisor,
    }
    if residual:
        base["classification"] = "off_compact_sym3_coefficient_curve"
        return base

    if divisor == 0:
        if a == 0 and b == 0:
            base.update(
                {
                    "classification": "compact_curve_ghost_node_(0,0)",
                    "normalized_node": [0, 0],
                    "normalization_preimages": "t0^2=2",
                    "odd_q_arithmetic_obstruction": "t^2=2q has no integer solution when q is odd",
                    "source_witnessed_arithmetic_sym3_origin": False,
                }
            )
            return base
        if b == q and a * a == q:
            normalized_x = -1 if a > 0 else 1
            base.update(
                {
                    "classification": "compact_curve_ghost_side_node",
                    "normalized_node": [normalized_x, 1],
                    "normalization_preimages": (
                        "t0^2+t0-1=0" if normalized_x == -1 else "t0^2-t0-1=0"
                    ),
                    "arithmetic_obstruction": "integral a forces sqrt(q) integral, while both normalization preimages are irrational",
                    "source_witnessed_arithmetic_sym3_origin": False,
                }
            )
            return base
        raise ArithmeticError("curve point on a^2=b escaped the proved nodal classification")

    t = generic_trace_parameter(a, b, q)
    integral_hasse = is_integral_hasse_parameter(t, q)
    source_witness_count = (
        source_trace_witnesses.get(t.numerator, 0) if t.denominator == 1 else 0
    )
    source_witnessed = source_witness_count > 0
    if source_witnessed and not integral_hasse:
        raise ArithmeticError("source trace witness violates the exact Hasse test")

    a_from_t, b_from_t = (
        shape_from_trace(t.numerator, q)
        if t.denominator == 1
        else (None, None)
    )
    parameter_reconstructs = (
        t.denominator == 1 and a_from_t == a and b_from_t == b
    )
    if source_witnessed and not parameter_reconstructs:
        raise ArithmeticError("source-witnessed trace does not reconstruct the atom")

    if source_witnessed:
        classification = "source_witnessed_arithmetic_sym3_coefficient_shape"
    elif integral_hasse and parameter_reconstructs:
        classification = "integral_hasse_parameter_not_source_witnessed"
    else:
        classification = "generic_compact_curve_ghost"

    base.update(
        {
            "classification": classification,
            "generic_trace_parameter_t": _fraction(t),
            "integral_hasse_parameter": integral_hasse,
            "parameter_reconstructs_atom": parameter_reconstructs,
            "source_witnessed_arithmetic_sym3_origin": source_witnessed,
            "elliptic_source_trace_witness_member_count": source_witness_count,
        }
    )
    return base


def _source_family_rows(balanced: Mapping[str, object]) -> dict[int, Mapping[str, object]]:
    families = balanced["frozen_enumeration_facts"]["families"]  # type: ignore[index]
    return {int(family["q"]): family for family in families}


def _shape_record(t: int, q: int, atom_counts: Mapping[tuple[int, int], int]) -> dict[str, object]:
    a, b = shape_from_trace(t, q)
    if a.denominator != 1 or b.denominator != 1:
        raise ArithmeticError("prime candidate classification unexpectedly lost integrality")
    pair = (a.numerator, b.numerator)
    return {
        "elliptic_trace_t": t,
        "coefficient_shape_a_b": [pair[0], pair[1]],
        "present_in_locked_support": pair in atom_counts,
        "locked_member_count": atom_counts.get(pair, 0),
    }


def _transform_family(
    family: Mapping[str, object], source_trace_witnesses: Mapping[int, int]
) -> dict[str, object]:
    q = int(family["q"])
    source_atoms = family["joint_a_D_b_D_law"]["atoms"]  # type: ignore[index]
    if len(source_atoms) > MAX_SOURCE_ATOMS:
        raise RuntimeError("source atom cap exceeded")
    if int(family["member_count"]) > MAX_SOURCE_MEMBERS:
        raise RuntimeError("source member cap exceeded")

    transformed = []
    atom_counts: dict[tuple[int, int], int] = {}
    for atom in source_atoms:
        a = int(atom["a_D"])
        b = int(atom["b_D"])
        member_count = int(atom["member_count"])
        atom_counts[a, b] = member_count
        classification = classify_atom(a, b, q, source_trace_witnesses)
        transformed.append(
            {
                "a_D": a,
                "b_D": b,
                "member_count": member_count,
                "member_fraction": atom["member_fraction"],
                **classification,
            }
        )

    counts_by_class: Counter[str] = Counter()
    members_by_class: Counter[str] = Counter()
    for row in transformed:
        label = str(row["classification"])
        counts_by_class[label] += 1
        members_by_class[label] += int(row["member_count"])

    on_curve = [row for row in transformed if row["on_compact_sym3_curve"]]
    source_witnessed = [
        row
        for row in transformed
        if row.get("source_witnessed_arithmetic_sym3_origin") is True
    ]
    ghosts = [
        row
        for row in transformed
        if row["on_compact_sym3_curve"]
        and row.get("source_witnessed_arithmetic_sym3_origin") is not True
    ]
    source_member_count = int(family["member_count"])
    on_curve_members = sum(int(row["member_count"]) for row in on_curve)
    genuine_members = sum(int(row["member_count"]) for row in source_witnessed)
    ghost_members = sum(int(row["member_count"]) for row in ghosts)

    prime_candidates = [
        _shape_record(t, q, atom_counts)
        for t in odd_prime_integral_shape_trace_candidates(q)
    ]
    return {
        "q": q,
        "source_atom_count": len(source_atoms),
        "source_member_count": source_member_count,
        "transformed_atoms": transformed,
        "classification_summary": {
            "atom_counts": dict(sorted(counts_by_class.items())),
            "member_counts": dict(sorted(members_by_class.items())),
            "on_curve_atom_count": len(on_curve),
            "on_curve_member_count": on_curve_members,
            "on_curve_member_fraction": _fraction(
                Fraction(on_curve_members, source_member_count)
            ),
            "source_witnessed_atom_count": len(source_witnessed),
            "source_witnessed_member_count": genuine_members,
            "source_witnessed_member_fraction": _fraction(
                Fraction(genuine_members, source_member_count)
            ),
            "ghost_atom_count": len(ghosts),
            "ghost_member_count": ghost_members,
            "ghost_member_fraction": _fraction(
                Fraction(ghost_members, source_member_count)
            ),
        },
        "on_curve_atoms": [
            {
                key: row[key]
                for key in (
                    "a_D",
                    "b_D",
                    "member_count",
                    "classification",
                )
            }
            | (
                {"generic_trace_parameter_t": row["generic_trace_parameter_t"]}
                if "generic_trace_parameter_t" in row
                else {}
            )
            | (
                {
                    "elliptic_source_trace_witness_member_count": row[
                        "elliptic_source_trace_witness_member_count"
                    ]
                }
                if "elliptic_source_trace_witness_member_count" in row
                else {}
            )
            for row in on_curve
        ],
        "odd_prime_arithmetic_shape_candidates": prime_candidates,
    }


def _negative_controls(families: Iterable[Mapping[str, object]]) -> dict[str, object]:
    locked_witnesses = []
    for family in families:
        witness = next(
            row
            for row in family["transformed_atoms"]  # type: ignore[index]
            if not row["on_compact_sym3_curve"]
        )
        locked_witnesses.append(
            {
                "q": family["q"],
                "a_D": witness["a_D"],
                "b_D": witness["b_D"],
                "member_count": witness["member_count"],
                "scaled_curve_residual": witness["scaled_curve_residual"],
            }
        )
    return {
        "generic_usp4_boundary_point": {
            "normalized_point_x_y": [0, -2],
            "lattice_shape_a_b": "(0,-2q)",
            "scaled_curve_residual": "-16q^3",
            "purpose": "the compact Sym^3 curve is a proper subset of the USp(4) coefficient region",
        },
        "locked_off_curve_witnesses": locked_witnesses,
        "coefficient_curve_false_positive": {
            "shape_a_b": [0, 0],
            "scaled_curve_residual": 0,
            "why_negative": "for odd q its normalization preimages require t^2=2q, so it has no integral elliptic trace",
        },
    }


def build_fixture() -> dict[str, object]:
    balanced, sym3 = load_sources()
    source_witnesses = _sym3_source_trace_witnesses(sym3)
    source_families = _source_family_rows(balanced)
    if set(source_families) != set(FROZEN_Q_VALUES):
        raise RuntimeError("source family keys changed")
    if not set(FROZEN_Q_VALUES).issubset(source_witnesses):
        raise RuntimeError("Sym^3 fixture lacks a frozen trace support")

    families = [
        _transform_family(source_families[q], source_witnesses[q])
        for q in FROZEN_Q_VALUES
    ]
    total_atoms = sum(int(row["source_atom_count"]) for row in families)
    total_members = sum(int(row["source_member_count"]) for row in families)
    if total_atoms != 251:
        raise ArithmeticError("locked atom total changed")
    if total_members > MAX_SOURCE_MEMBERS:
        raise RuntimeError("combined member cap exceeded")

    aggregate_atoms: Counter[str] = Counter()
    aggregate_members: Counter[str] = Counter()
    for family in families:
        aggregate_atoms.update(family["classification_summary"]["atom_counts"])
        aggregate_members.update(family["classification_summary"]["member_counts"])

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym3_coefficient_intersection.v1",
        "status": "EXACT_SYMBOLIC_AND_SOURCE_LOCKED_Q_3_5_7_TRANSFORM",
        "coefficient_bridge": {
            "genus2_factor": "1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "genus2_normalized_factor": "1+(a/sqrt(q))*Z+(b/q)*Z^2+(a/sqrt(q))*Z^3+Z^4",
            "sym3_normalized_factor": "1-x*Z+y*Z^2-x*Z^3+Z^4",
            "coordinate_identification": "x=-a/sqrt(q), y=b/q",
            "sym3_curve": "F(x,y)=-x^4+x^2*y+x^2+y^3-2*y^2=0",
            "scaled_integer_equation": "G_q(a,b)=-q*a^4+q*a^2*b+q^2*a^2+b^3-2q*b^2=0",
            "clearing_denominators": "G_q(a,b)=q^3*F(-a/sqrt(q),b/q)",
            "weight_warning": "this matches independently normalized coefficient shapes; it is not an equality between the weight-1 genus-two factor and the weight-3 elliptic Sym^3 factor",
        },
        "generic_normalization_inverse": {
            "exceptional_divisor": "d=a^2-b=0",
            "numerator": "n=a(q-b)",
            "recovered_elliptic_trace": "t=n/d=a(q-b)/(a^2-b)",
            "source_normalization_inverse": "t0=x(y-1)/(x^2-y), with t=sqrt(q)t0",
            "cross_multiplied_identity_1": "n^3-2q*n*d^2+q*a*d^3=a(q-a^2)G_q(a,b)",
            "cross_multiplied_identity_2": "n^4-3q*n^2*d^2+(2q^2-qb)d^4=(a^4*b-2q*a^4+q*a^2*b+q^2*a^2-q*b^2)G_q(a,b)",
            "consequence_on_G_zero": [
                "q*a=2q*t-t^3",
                "q*b=t^4-3q*t^2+2q^2",
            ],
        },
        "singular_nodal_classification": {
            "restriction_to_exceptional_divisor": "G_q(a,a^2)=a^2(a^2-q)^2",
            "all_lattice_possibilities_on_G_zero_and_d_zero": [
                "(a,b)=(0,0)",
                "a^2=q and b=q",
            ],
            "zero_node": {
                "normalized_point": [0, 0],
                "preimages": "t0=+-sqrt(2)",
                "odd_q_theorem": "no integer t can satisfy t^2=2q because v_2(2q)=1",
            },
            "side_nodes": {
                "normalized_points": [[-1, 1], [1, 1]],
                "lattice_condition": "a^2=q,b=q",
                "arithmetic_obstruction": "integral a makes sqrt(q) integral, but t0 has one of the irreducible equations t0^2+-t0-1=0",
            },
            "interpretation": "all three are compact-image nodes, but none is an integral elliptic-trace shape under the stated lattice conditions",
        },
        "arithmetic_trace_conditions": {
            "all_positive_integer_q_integrality": "for integer t, both induced coefficients a,b are integral iff q divides t^3; q|t^3 automatically implies q|t^4",
            "necessary_hasse_bound": "t^2<=4q",
            "general_prime_power_caveat": "integrality plus the Hasse inequality is only an arithmetic candidate test here; actual elliptic realization is separately required",
            "frozen_acceptance_rule": "call a shape arithmetic only when its recovered integer Hasse trace occurs with positive count in the locked elliptic source fixture",
        },
        "odd_prime_classification": {
            "theorem": "if p is an odd prime and an elliptic trace t induces an integral genus-two-scale Sym^3 shape, then p|t; Hasse gives t=0 for p>=5 and t in {-3,0,3} for p=3",
            "proof": "p|t^3 implies p|t. Writing t=kp, k^2*p<=4. Thus k=0 for p>=5, while k in {-1,0,1} for p=3.",
            "coefficient_shapes": {
                "p_at_least_5": "t=0 gives (a,b)=(0,2p)",
                "p_equals_3": [
                    {"t": -3, "a_b": [3, 6]},
                    {"t": 0, "a_b": [0, 6]},
                    {"t": 3, "a_b": [-3, 6]},
                ],
            },
            "realization_scope": "the implication and candidate list are proved algebraically; the frozen q=3,5,7 traces called genuine below have independent positive-count elliptic witnesses",
        },
        "frozen_atom_transform": {
            "coverage": "every joint (a_D,b_D) atom and its exact member count from the locked q=3,5,7 balanced-control fixture",
            "families": families,
            "aggregate_audit_totals": {
                "source_atom_count": total_atoms,
                "source_member_count": total_members,
                "atom_counts_by_classification": dict(sorted(aggregate_atoms.items())),
                "member_counts_by_classification": dict(sorted(aggregate_members.items())),
                "pooling_warning": "summing across q is an audit total, not a common probability measure",
            },
        },
        "negative_controls": _negative_controls(families),
        "literature_boundary": {
            "classical_inherited": "the symmetric-cube representation and its automorphic theory are classical and are not novelty claims of this packet",
            "inherited_primary_references": [
                "https://arxiv.org/abs/math/9909198",
                "https://arxiv.org/abs/math/0409607",
            ],
            "project_specific_only": "the scaled bridge, nodal arithmetic filter, and exact intersection with these 251 locked atoms are atlas calculations",
            "priority_caveat": "project-specific does not mean absent from the literature; no novelty or priority claim is made without a dedicated search",
        },
        "scope_firewall": {
            "exact": [
                "the displayed polynomial identities and nodal classification",
                "the all-positive-integer-q divisibility criterion for an integer parameter",
                "the odd-prime candidate classification",
                "the complete transform of the 251 locked atoms",
            ],
            "frozen_only": [
                "all member counts and support intersections for q=3,5,7",
                "source-witnessed realization labels",
            ],
            "conjectural": [],
            "nonclaims": [
                "no equidistribution or density theorem",
                "no claim that a coefficient-curve point alone has arithmetic Sym^3 origin",
                "no identity of the differently weighted local factors",
                "no new curve, field, or L-function enumeration",
                "no RH or GRH implication",
            ],
        },
        "source_locks": {
            "balanced_control_fixture": {
                "path": str(BALANCED_FIXTURE.relative_to(ROOT)).replace("\\", "/"),
                "schema": EXPECTED_BALANCED_SCHEMA,
                "payload_sha256": EXPECTED_BALANCED_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_BALANCED_FILE_SHA256_LF,
                "producer_sha256_lf_normalized": EXPECTED_BALANCED_SOURCE_SHA256_LF,
            },
            "elliptic_sym3_fixture": {
                "path": str(SYM3_FIXTURE.relative_to(ROOT)).replace("\\", "/"),
                "schema": EXPECTED_SYM3_SCHEMA,
                "payload_sha256": EXPECTED_SYM3_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_SYM3_FILE_SHA256_LF,
                "producer_sha256_lf_normalized": EXPECTED_SYM3_SOURCE_SHA256_LF,
            },
        },
        "resource_contract": {
            "arithmetic": "exact Python integers and Fraction only",
            "new_curve_or_field_enumerations": 0,
            "source_atoms_transformed": total_atoms,
            "source_atom_cap": MAX_SOURCE_ATOMS,
            "source_members_represented": total_members,
            "source_member_cap": MAX_SOURCE_MEMBERS,
            "polynomial_residual_evaluations": total_atoms,
            "randomness": "not used",
            "floating_point": "not used",
        },
        "producer": {
            "script": Path(__file__).name,
            "script_sha256_lf_normalized": _lf_sha256(Path(__file__)),
            "note": NOTE_PATH.name,
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": str(TEST_PATH.relative_to(ROOT)).replace("\\", "/"),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _write(path: Path) -> None:
    fixture = build_fixture()
    path.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {path}")
    print(f"payload_sha256={fixture['payload_sha256']}")


def _check(path: Path) -> None:
    expected = build_fixture()
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit(f"stale fixture: {path}")
    print(f"fixture current: {path}")
    print(f"payload_sha256={expected['payload_sha256']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument(
        "--write",
        nargs="?",
        const=OUTPUT_PATH,
        type=Path,
        help="write the fixture (default: adjacent canonical JSON)",
    )
    action.add_argument(
        "--check",
        nargs="?",
        const=OUTPUT_PATH,
        type=Path,
        help="check the fixture (default: adjacent canonical JSON)",
    )
    args = parser.parse_args()
    if args.write is not None:
        _write(args.write)
    else:
        _check(args.check)


if __name__ == "__main__":
    main()
