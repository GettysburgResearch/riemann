#!/usr/bin/env python3
"""Exact Sym^3 exterior-square / Sym^4 plethysm bridge.

This producer performs no finite-field or curve enumeration.  It checks two
formal polynomial identities and transforms the 251 signed coefficient atoms
already frozen by ``genus2_sym3_coefficient_intersection.json``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from collections.abc import Iterable, Mapping
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
OUTPUT_PATH = HERE / "sym3_exterior_sym4_plethysm_bridge.json"
NOTE_PATH = HERE / "SYM3_EXTERIOR_SYM4_PLETHYSM_BRIDGE.md"
TEST_PATH = ROOT / "tests" / "test_sym3_exterior_sym4_plethysm_bridge.py"

SOURCE_ATOM_CAP_INCLUSIVE = 251
SOURCE_MEMBER_CAP_INCLUSIVE = 17_068
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 512

SOURCE_PACKET_LOCKS = {
    "elliptic_sym3_packet": {
        "path": "research/l-families/atlas/function_field/elliptic_symmetric_cube_family.json",
        "schema": "riemann.function_field.elliptic_symmetric_cube_family.v1",
        "payload_sha256": "7e30dd220b9c9e3a3873ffe8b168ad53af4899de1dd21a2d69e2498abc6ee5b9",
        "file_sha256_lf_normalized": "2b8b7f206c4e4c24f4e1ac65d093ab976dd6483dceb6ea52f44e76a7004bb033",
    },
    "elliptic_sym4_packet": {
        "path": "research/l-families/atlas/function_field/elliptic_symmetric_fourth_so5_slice.json",
        "schema": "riemann.function_field.elliptic_symmetric_fourth_so5_slice.v1",
        "payload_sha256": "7cbf4e02e64fba82be120f3ad83d3448e86e6e93e0f05d180eae14c9f3a8320f",
        "file_sha256_lf_normalized": "fa26b5b34ac4b3effeeb3083981f7699a36a66997a0b5d3093604721e8122e7d",
    },
    "primitive_exterior_packet": {
        "path": "research/l-families/atlas/function_field/genus2_primitive_exterior_square.json",
        "schema": "riemann.function_field.genus2_primitive_exterior_square.v1",
        "payload_sha256": "235991e9e36a55ec8352a7c18fc2e0722546267daf51a17642ff767c3387ab1c",
        "file_sha256_lf_normalized": "2e39dd0f24dc38b1c03165d047f10858ac205edc780fbc8bff225717c507a976",
    },
    "genus2_sym3_intersection_packet": {
        "path": "research/l-families/atlas/function_field/genus2_sym3_coefficient_intersection.json",
        "schema": "riemann.function_field.genus2_sym3_coefficient_intersection.v1",
        "payload_sha256": "5d19dfeaa8aa2a142dd0c24f0f71d774e7f2d004e981e9fa5a30ac144c3d17e8",
        "file_sha256_lf_normalized": "6f10812a0a7473054f04820657ae8b679eaf5b4286566a049ef2fc3b4d04458c",
    },
}

INTERSECTION_FIXTURE_PATH = ROOT / SOURCE_PACKET_LOCKS[
    "genus2_sym3_intersection_packet"
]["path"]

# A sparse polynomial in two variables.  The exponent pair is interpreted as
# (degree in the first variable, degree in the second variable).
SparsePolynomial = dict[tuple[int, int], int]


class ResourceGuard:
    """Count declared high-level exact checks under a deliberately small cap."""

    def __init__(self) -> None:
        self._counts: Counter[str] = Counter()

    def charge(self, label: str, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("resource charge must be a nonnegative built-in int")
        proposed = sum(self._counts.values()) + amount
        if proposed >= ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE:
            raise RuntimeError(
                "accounted work would reach the exclusive cap "
                f"{ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE}"
            )
        self._counts[label] += amount

    def ledger(self) -> dict[str, object]:
        counts = dict(sorted(self._counts.items()))
        return {
            "counts": counts,
            "total_accounted_work_units": sum(counts.values()),
        }


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def validate_note_integrity(path: Path = NOTE_PATH) -> dict[str, object]:
    """Refuse control-byte damage and the escape-loss patterns seen in review."""

    raw = path.read_bytes()
    forbidden_controls = [
        offset
        for offset, byte in enumerate(raw)
        if byte < 32 and byte not in (9, 10, 13)
    ]
    if forbidden_controls:
        raise RuntimeError(
            f"note contains forbidden C0 controls at byte offsets {forbidden_controls}"
        )
    text = raw.decode("utf-8")
    malformed_literals = (",quad", ",qquad", "(operatorname", "(mathbb", "(bigwedge")
    present_malformed = [token for token in malformed_literals if token in text]
    bare_command_pattern = re.compile(
        r"(?<!\\)\b(?:operatorname|bigwedge|alpha|beta|qquad|mathbb|otimes|"
        r"oplus|simeq|boxed|xrightarrow|downarrow|substack|bigoplus)\b"
    )
    bare_commands = sorted(set(bare_command_pattern.findall(text)))
    if present_malformed or bare_commands:
        raise RuntimeError(
            "note contains malformed LaTeX escape remnants: "
            f"{present_malformed + bare_commands}"
        )

    display_tokens = re.findall(r"\\\[|\\\]", text)
    expected_display_tokens = [
        token
        for _ in range(len(display_tokens) // 2)
        for token in (r"\[", r"\]")
    ]
    if display_tokens != expected_display_tokens:
        raise RuntimeError("note has unmatched or misordered display-math delimiters")
    begin_environments = re.findall(r"\\begin\{([^}]+)\}", text)
    end_environments = re.findall(r"\\end\{([^}]+)\}", text)
    if begin_environments != end_environments:
        raise RuntimeError("note has unmatched LaTeX environments")
    odd_dollar_lines = [
        line_number
        for line_number, line in enumerate(text.splitlines(), start=1)
        if line.count("$") % 2
    ]
    if odd_dollar_lines:
        raise RuntimeError(
            f"note has unmatched inline-math delimiters on lines {odd_dollar_lines}"
        )
    return {
        "utf8_decoding": "strict_pass",
        "forbidden_C0_control_count": 0,
        "display_math_pair_count": len(display_tokens) // 2,
        "balanced_LaTeX_environments": begin_environments,
        "inline_math_lines_have_even_dollar_counts": True,
        "known_escape_loss_patterns_absent": True,
    }


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _fraction_pair(value: Fraction | int) -> list[int]:
    fraction = Fraction(value)
    return [fraction.numerator, fraction.denominator]


def _require_integral_local_data(t: int, q: int) -> None:
    if isinstance(t, bool) or not isinstance(t, int):
        raise TypeError("t must be a built-in int")
    if isinstance(q, bool) or not isinstance(q, int):
        raise TypeError("q must be a built-in int")
    if q <= 0:
        raise ValueError("q must be a positive built-in int")


def multiply_coefficients(
    left: Iterable[int], right: Iterable[int]
) -> tuple[int, ...]:
    left_tuple = tuple(left)
    right_tuple = tuple(right)
    if not left_tuple or not right_tuple:
        raise ValueError("coefficient lists must be nonempty")
    output = [0] * (len(left_tuple) + len(right_tuple) - 1)
    for left_degree, left_value in enumerate(left_tuple):
        for right_degree, right_value in enumerate(right_tuple):
            output[left_degree + right_degree] += left_value * right_value
    return tuple(output)


def sym3_local_coefficients(t: int, q: int) -> tuple[int, ...]:
    """Coefficients of Sym^3 for ``1-t*T+q*T^2``."""

    _require_integral_local_data(t, q)
    a3 = -t**3 + 2 * q * t
    b3 = q * (t**4 - 3 * q * t * t + 2 * q * q)
    Q = q**3
    return (1, a3, b3, Q * a3, Q * Q)


def primitive_exterior_coefficients(a: int, b: int, Q: int) -> tuple[int, ...]:
    """Generic primitive exterior polynomial for a reciprocal quartic."""

    if any(isinstance(value, bool) or not isinstance(value, int) for value in (a, b, Q)):
        raise TypeError("a, b, and Q must be built-in ints")
    if Q <= 0:
        raise ValueError("Q must be positive")
    difference = a * a - b
    return (
        1,
        Q - b,
        Q * difference,
        -(Q**2) * difference,
        Q**3 * (b - Q),
        -(Q**5),
    )


def sym4_invariants(t: int, q: int) -> tuple[int, int]:
    _require_integral_local_data(t, q)
    C = t**4 - 3 * q * t * t + q * q
    D = q * (t * t - 2 * q) * C
    return C, D


def sym4_local_coefficients(t: int, q: int) -> tuple[int, ...]:
    """Coefficients of the untwisted degree-five Sym^4 local factor."""

    C, D = sym4_invariants(t, q)
    return (1, -C, D, -(q**2) * D, q**6 * C, -(q**10))


def scale_local_variable(coefficients: Iterable[int], scale: int) -> tuple[int, ...]:
    if isinstance(scale, bool) or not isinstance(scale, int):
        raise TypeError("scale must be a built-in int")
    return tuple(coefficient * scale**degree for degree, coefficient in enumerate(coefficients))


def bridge_local_coefficients(t: int, q: int) -> tuple[int, ...]:
    """Compute R_Q after inserting the Sym^3 quartic."""

    sym3 = sym3_local_coefficients(t, q)
    return primitive_exterior_coefficients(sym3[1], sym3[2], q**3)


def sym3_curve_residual_from_x_squared(
    x_squared: Fraction | int, y: Fraction | int
) -> Fraction:
    x2 = Fraction(x_squared)
    y_fraction = Fraction(y)
    return (
        -(x2**2)
        + x2 * y_fraction
        + x2
        + y_fraction**3
        - 2 * y_fraction**2
    )


def primitive_coordinate_map(
    x_squared: Fraction | int, y: Fraction | int
) -> tuple[Fraction, Fraction]:
    x2 = Fraction(x_squared)
    y_fraction = Fraction(y)
    return y_fraction - 1, x2 - y_fraction


def sym4_curve_residual(s: Fraction | int, k: Fraction | int) -> Fraction:
    s_fraction = Fraction(s)
    k_fraction = Fraction(k)
    return (
        k_fraction**2
        + s_fraction * k_fraction
        - s_fraction**2
        - s_fraction**3
    )


def _poly_add(*polynomials: Mapping[tuple[int, int], int]) -> SparsePolynomial:
    output: Counter[tuple[int, int]] = Counter()
    for polynomial in polynomials:
        output.update(polynomial)
    return {exponents: coefficient for exponents, coefficient in output.items() if coefficient}


def _poly_scale(polynomial: Mapping[tuple[int, int], int], scalar: int) -> SparsePolynomial:
    return {
        exponents: scalar * coefficient
        for exponents, coefficient in polynomial.items()
        if scalar * coefficient
    }


def _poly_multiply(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
) -> SparsePolynomial:
    output: Counter[tuple[int, int]] = Counter()
    for (left_first, left_second), left_value in left.items():
        for (right_first, right_second), right_value in right.items():
            output[(left_first + right_first, left_second + right_second)] += (
                left_value * right_value
            )
    return {exponents: coefficient for exponents, coefficient in output.items() if coefficient}


def _poly_power(polynomial: Mapping[tuple[int, int], int], exponent: int) -> SparsePolynomial:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    output: SparsePolynomial = {(0, 0): 1}
    for _ in range(exponent):
        output = _poly_multiply(output, polynomial)
    return output


def _poly_subtract(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
) -> SparsePolynomial:
    return _poly_add(left, _poly_scale(right, -1))


def symbolic_local_factor_certificate() -> dict[str, object]:
    """Verify the bridge coefficientwise in Z[t,q]."""

    one: SparsePolynomial = {(0, 0): 1}
    t: SparsePolynomial = {(1, 0): 1}
    q: SparsePolynomial = {(0, 1): 1}
    t2 = _poly_power(t, 2)
    q2 = _poly_power(q, 2)
    a3 = _poly_add(_poly_scale(_poly_power(t, 3), -1), _poly_scale(_poly_multiply(q, t), 2))
    C = _poly_add(
        _poly_power(t, 4),
        _poly_scale(_poly_multiply(q, t2), -3),
        q2,
    )
    b3 = _poly_multiply(
        q,
        _poly_add(
            _poly_power(t, 4),
            _poly_scale(_poly_multiply(q, t2), -3),
            _poly_scale(q2, 2),
        ),
    )
    t2_minus_2q = _poly_add(t2, _poly_scale(q, -2))
    D = _poly_multiply(q, _poly_multiply(t2_minus_2q, C))
    Q = _poly_power(q, 3)
    difference = _poly_subtract(_poly_power(a3, 2), b3)

    intermediate_residuals = {
        "b3_minus_q_times_C_plus_q_squared": _poly_subtract(
            b3, _poly_multiply(q, _poly_add(C, q2))
        ),
        "a3_squared_minus_b3_minus_t_squared_minus_2q_times_C": _poly_subtract(
            difference, _poly_multiply(t2_minus_2q, C)
        ),
    }

    R = (
        one,
        _poly_subtract(Q, b3),
        _poly_multiply(Q, difference),
        _poly_scale(_poly_multiply(_poly_power(Q, 2), difference), -1),
        _poly_multiply(_poly_power(Q, 3), _poly_subtract(b3, Q)),
        _poly_scale(_poly_power(Q, 5), -1),
    )
    P_sym4 = (
        one,
        _poly_scale(C, -1),
        D,
        _poly_scale(_poly_multiply(q2, D), -1),
        _poly_multiply(_poly_power(q, 6), C),
        _poly_scale(_poly_power(q, 10), -1),
    )
    P_sym4_at_qT = tuple(
        _poly_multiply(coefficient, _poly_power(q, degree))
        for degree, coefficient in enumerate(P_sym4)
    )
    coefficient_residuals = tuple(
        _poly_subtract(left, right) for left, right in zip(R, P_sym4_at_qT)
    )

    failures = {
        name: residual
        for name, residual in intermediate_residuals.items()
        if residual
    }
    if failures or any(coefficient_residuals):
        raise RuntimeError("symbolic local-factor bridge failed")
    return {
        "coefficient_ring": "Z[t,q]",
        "intermediate_residual_term_counts": {
            name: len(residual) for name, residual in intermediate_residuals.items()
        },
        "R_Q_minus_P_Sym4_at_qT_residual_term_counts_T0_through_T5": [
            len(residual) for residual in coefficient_residuals
        ],
        "coefficients_compared": len(coefficient_residuals),
    }


def symbolic_curve_certificate() -> dict[str, object]:
    """Verify F4(y-1,x^2-y) + F3(x,y) = 0 in Z[x,y]."""

    one: SparsePolynomial = {(0, 0): 1}
    x: SparsePolynomial = {(1, 0): 1}
    y: SparsePolynomial = {(0, 1): 1}
    x2 = _poly_power(x, 2)
    s = _poly_subtract(y, one)
    k = _poly_subtract(x2, y)
    F3 = _poly_add(
        _poly_scale(_poly_power(x, 4), -1),
        _poly_multiply(x2, y),
        x2,
        _poly_power(y, 3),
        _poly_scale(_poly_power(y, 2), -2),
    )
    F4 = _poly_add(
        _poly_power(k, 2),
        _poly_multiply(s, k),
        _poly_scale(_poly_power(s, 2), -1),
        _poly_scale(_poly_power(s, 3), -1),
    )
    residual = _poly_add(F4, F3)
    if residual:
        raise RuntimeError("normalized coefficient-curve bridge failed")
    return {
        "coefficient_ring": "Z[x,y]",
        "substitution": {"s": "y-1", "k": "x^2-y"},
        "identity": "F4(y-1,x^2-y)=-F3(x,y)",
        "residual_term_count": 0,
    }


def plethysm_weight_certificate() -> dict[str, object]:
    """Compare diagonal-torus characters of both sides of the plethysm."""

    sym3_weights = ((3, 0), (2, 1), (1, 2), (0, 3))
    wedge_weights: Counter[tuple[int, int]] = Counter()
    for first_index, first in enumerate(sym3_weights):
        for second in sym3_weights[first_index + 1 :]:
            wedge_weights[(first[0] + second[0], first[1] + second[1])] += 1
    rhs_weights: Counter[tuple[int, int]] = Counter({(3, 3): 1})
    for alpha_degree in range(4, -1, -1):
        beta_degree = 4 - alpha_degree
        rhs_weights[(alpha_degree + 1, beta_degree + 1)] += 1
    if wedge_weights != rhs_weights:
        raise RuntimeError("rank-two plethysm weight multisets disagree")
    weight_rows = [
        [alpha_degree, beta_degree, multiplicity]
        for (alpha_degree, beta_degree), multiplicity in sorted(
            wedge_weights.items(), reverse=True
        )
    ]
    return {
        "assumptions": "V is two-dimensional over a characteristic-zero field",
        "identity": "wedge^2 Sym^3(V) = (det V)^3 direct_sum (Sym^4(V) tensor det V)",
        "Schur_functor_form": "S_(3,3)(V) direct_sum S_(5,1)(V)",
        "left_and_right_diagonal_torus_weight_multiset": weight_rows,
        "dimension": sum(row[2] for row in weight_rows),
        "why_character_equality_suffices": "finite-dimensional rational GL2 representations are semisimple in characteristic zero",
    }


def _load_and_verify_source_packets() -> tuple[dict[str, object], dict[str, object]]:
    verified: dict[str, object] = {}
    intersection: dict[str, object] | None = None
    for name, expected in SOURCE_PACKET_LOCKS.items():
        path = ROOT / expected["path"]
        actual_file_hash = _lf_normalized_sha256(path)
        if actual_file_hash != expected["file_sha256_lf_normalized"]:
            raise RuntimeError(f"source lock file hash mismatch for {name}")
        source = json.loads(path.read_text(encoding="utf-8"))
        if source.get("schema") != expected["schema"]:
            raise RuntimeError(f"source lock schema mismatch for {name}")
        if source.get("payload_sha256") != expected["payload_sha256"]:
            raise RuntimeError(f"source lock payload mismatch for {name}")
        unhashed = dict(source)
        claimed = unhashed.pop("payload_sha256", None)
        if claimed != _canonical_sha256(unhashed):
            raise RuntimeError(f"source packet has invalid canonical payload hash: {name}")
        verified[name] = {
            **expected,
            "canonical_payload_recomputed": True,
            "lock_scope": "the packet JSON payload; its embedded producer/note/test locks remain transitively frozen",
        }
        if name == "genus2_sym3_intersection_packet":
            intersection = source
    if intersection is None:
        raise RuntimeError("locked genus-two intersection packet was not loaded")
    return verified, intersection


def _atom_transcript_row(
    q: int,
    a: int,
    b: int,
    members: int,
    s: Fraction,
    k: Fraction,
    F3: Fraction,
    F4: Fraction,
    hit: bool,
) -> list[int]:
    return [
        q,
        a,
        b,
        members,
        s.numerator,
        s.denominator,
        k.numerator,
        k.denominator,
        F3.numerator,
        F3.denominator,
        F4.numerator,
        F4.denominator,
        int(hit),
    ]


def transform_locked_genus2_atoms(
    intersection: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    """Apply the commutative coefficient diagram to all 251 locked atoms."""

    frozen = intersection.get("frozen_atom_transform")
    if not isinstance(frozen, dict) or not isinstance(frozen.get("families"), list):
        raise TypeError("locked intersection packet has an unexpected family schema")
    expected = {
        3: (32, 162, 3, 18),
        5: (81, 2_500, 2, 55),
        7: (138, 14_406, 2, 378),
    }
    transcript: list[list[int]] = []
    output_families: list[dict[str, object]] = []
    aggregate_source_atoms = 0
    aggregate_source_members = 0
    aggregate_hit_atoms = 0
    aggregate_hit_members = 0

    for family_object in frozen["families"]:
        if not isinstance(family_object, dict):
            raise TypeError("locked family row must be an object")
        q = int(family_object["q"])
        rows = family_object.get("transformed_atoms")
        if q not in expected or not isinstance(rows, list):
            raise RuntimeError("locked intersection fields must be exactly q=3,5,7")
        signed_hits: list[dict[str, object]] = []
        compressed: dict[tuple[Fraction, Fraction], dict[str, object]] = {}
        source_members = 0

        for row_object in rows:
            if not isinstance(row_object, dict):
                raise TypeError("locked atom row must be an object")
            a = int(row_object["a_D"])
            b = int(row_object["b_D"])
            members = int(row_object["member_count"])
            source_members += members
            x_squared = Fraction(a * a, q)
            y = Fraction(b, q)
            s, k = primitive_coordinate_map(x_squared, y)
            F3 = sym3_curve_residual_from_x_squared(x_squared, y)
            F4 = sym4_curve_residual(s, k)
            if F4 != -F3:
                raise RuntimeError("atom violates F4=-F3")
            if F3 * q**3 != int(row_object["scaled_curve_residual"]):
                raise RuntimeError("atom disagrees with locked scaled Sym3 residual")
            hit = F3 == 0
            if hit != bool(row_object["on_compact_sym3_curve"]):
                raise RuntimeError("atom disagrees with locked Sym3 hit flag")
            transcript.append(_atom_transcript_row(q, a, b, members, s, k, F3, F4, hit))
            guard.charge("locked_signed_atom_transforms")

            if not hit:
                continue
            classification = str(row_object["classification"])
            signed_row = {
                "a_D": a,
                "b_D": b,
                "member_count": members,
                "source_classification": classification,
                "primitive_s": _fraction_pair(s),
                "primitive_k": _fraction_pair(k),
            }
            signed_hits.append(signed_row)
            key = (s, k)
            if key not in compressed:
                compressed[key] = {
                    "primitive_s": _fraction_pair(s),
                    "primitive_k": _fraction_pair(k),
                    "signed_preimage_atoms": [],
                    "member_count": 0,
                    "source_classifications": set(),
                }
            compressed_row = compressed[key]
            preimages = compressed_row["signed_preimage_atoms"]
            classifications = compressed_row["source_classifications"]
            if not isinstance(preimages, list) or not isinstance(classifications, set):
                raise TypeError("internal compression state corrupted")
            preimages.append([a, b, members])
            classifications.add(classification)
            compressed_row["member_count"] = int(compressed_row["member_count"]) + members

        compressed_rows: list[dict[str, object]] = []
        for key in sorted(compressed):
            row = compressed[key]
            classifications = row.pop("source_classifications")
            if not isinstance(classifications, set):
                raise TypeError("internal classification state corrupted")
            row["source_classifications"] = sorted(classifications)
            row["arithmetic_ghost_preserved"] = (
                "compact_curve_ghost_node_(0,0)" in classifications
            )
            compressed_rows.append(row)

        actual = (len(rows), source_members, len(signed_hits), sum(row["member_count"] for row in signed_hits))
        if actual != expected[q]:
            raise RuntimeError(f"locked incidence totals changed for q={q}: {actual}")
        if len(compressed_rows) != 2:
            raise RuntimeError(f"expected exactly two sign-compressed hits for q={q}")
        family_transcript = [row for row in transcript if row[0] == q]
        output_families.append(
            {
                "q": q,
                "source_signed_atom_count": len(rows),
                "source_member_count": source_members,
                "Sym3_curve_hit_signed_atom_count": len(signed_hits),
                "Sym4_pullback_hit_signed_atom_count": len(signed_hits),
                "common_hit_member_count": actual[3],
                "hit_sets_exactly_identical": True,
                "signed_hit_atoms": signed_hits,
                "sign_compressed_hit_count": len(compressed_rows),
                "sign_compressed_hits": compressed_rows,
                "transformed_atom_transcript_sha256": _canonical_sha256(family_transcript),
            }
        )
        aggregate_source_atoms += len(rows)
        aggregate_source_members += source_members
        aggregate_hit_atoms += len(signed_hits)
        aggregate_hit_members += actual[3]

    if [row["q"] for row in output_families] != [3, 5, 7]:
        raise RuntimeError("locked family order or field set changed")
    if aggregate_source_atoms != SOURCE_ATOM_CAP_INCLUSIVE:
        raise RuntimeError("source transform must contain exactly 251 signed atoms")
    if aggregate_source_members != SOURCE_MEMBER_CAP_INCLUSIVE:
        raise RuntimeError("source transform must represent exactly 17068 members")
    if (aggregate_hit_atoms, aggregate_hit_members) != (7, 451):
        raise RuntimeError("locked common incidence must be 7 atoms and 451 members")
    return {
        "source_semantics": "deterministic transform of pre-enumerated signed (a_D,b_D) atoms; no new curve or field enumeration",
        "coordinate_transform": {
            "x_squared": "a_D^2/q",
            "y": "b_D/q",
            "s": "y-1",
            "k": "x^2-y",
        },
        "all_251_atoms_satisfy_F4_equals_minus_F3": True,
        "families": output_families,
        "aggregate_audit_totals": {
            "source_signed_atom_count": aggregate_source_atoms,
            "source_member_count": aggregate_source_members,
            "common_hit_signed_atom_count": aggregate_hit_atoms,
            "common_hit_member_count": aggregate_hit_members,
            "sign_compressed_hit_count": sum(
                int(row["sign_compressed_hit_count"]) for row in output_families
            ),
            "pooling_warning": "cross-q sums are audit totals, not one probability space",
        },
        "all_atom_transform_transcript_format": [
            "q",
            "a_D",
            "b_D",
            "member_count",
            "s_numerator",
            "s_denominator",
            "k_numerator",
            "k_denominator",
            "F3_numerator",
            "F3_denominator",
            "F4_numerator",
            "F4_denominator",
            "common_hit_bit",
        ],
        "all_atom_transform_transcript_sha256": _canonical_sha256(transcript),
    }


def build_fixture() -> dict[str, object]:
    guard = ResourceGuard()
    note_integrity = validate_note_integrity()
    guard.charge("note_integrity_scan")
    source_locks, intersection = _load_and_verify_source_packets()
    plethysm = plethysm_weight_certificate()
    guard.charge("plethysm_weight_terms", int(plethysm["dimension"]))
    local_certificate = symbolic_local_factor_certificate()
    guard.charge("symbolic_local_factor_coefficients", int(local_certificate["coefficients_compared"]))
    curve_certificate = symbolic_curve_certificate()
    guard.charge("symbolic_curve_identity")
    incidence = transform_locked_genus2_atoms(intersection, guard)

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.sym3_exterior_sym4_plethysm_bridge.v1",
        "raw_fixture_id": "sym3-exterior-sym4-plethysm-bridge-exact-v1",
        "status": "exact characteristic-zero plethysm, exact coefficient algebra, and source-locked finite incidence transform",
        "rigor_level": "integer/rational/sparse-polynomial exact; no floats, samples, interpolation, or new enumeration",
        "artifact_integrity": {"note": note_integrity},
        "source_packet_locks": source_locks,
        "rank_two_representation_identity": plethysm,
        "local_factor_commutative_diagram": {
            "base_factor": "L_E(T)=1-t*T+q*T^2",
            "Sym3_quartic": {
                "Q": "q^3",
                "a3": "-t^3+2*q*t",
                "b3": "q*(t^4-3*q*t^2+2*q^2)",
                "shape": "1+a3*T+b3*T^2+Q*a3*T^3+Q^2*T^4",
            },
            "generic_primitive_exterior_polynomial": "R_Q(T)=1+(Q-b)T+Q(a^2-b)T^2-Q^2(a^2-b)T^3+Q^3(b-Q)T^4-Q^5T^5",
            "Sym4_invariants": {
                "C": "t^4-3*q*t^2+q^2",
                "D": "q*(t^2-2*q)*C",
            },
            "bridge_witnesses": [
                "b3=q*(C+q^2)",
                "a3^2-b3=(t^2-2*q)*C=D/q",
            ],
            "Sym4_factor": "P_Sym4(U)=1-CU+DU^2-q^2DU^3+q^6CU^4-q^10U^5",
            "exact_identity": "R_Q(T)=P_Sym4(q*T)",
            "common_coefficients_T0_through_T5": [
                "1",
                "-q*C",
                "q^2*D",
                "-q^5*D",
                "q^10*C",
                "-q^15",
            ],
            "symbolic_certificate": local_certificate,
        },
        "normalized_coefficient_diagram": {
            "Sym3_curve": "F3(x,y)=-x^4+x^2*y+x^2+y^3-2*y^2",
            "primitive_map": "(s,k)=(y-1,x^2-y)",
            "Sym4_curve": "F4(s,k)=k^2+s*k-s^2-s^3",
            "symbolic_certificate": curve_certificate,
            "normalization_parameter_bridge": "w=t0^2-2",
            "node_map": [
                {
                    "Sym3_node": [-1, 1],
                    "Sym4_image": [0, 0],
                    "Sym3_parameter_equation": "t0^2+t0-1=0",
                },
                {
                    "Sym3_node": [1, 1],
                    "Sym4_image": [0, 0],
                    "Sym3_parameter_equation": "t0^2-t0-1=0",
                },
                {
                    "Sym3_node": [0, 0],
                    "Sym4_image": [-1, 0],
                    "Sym3_parameter_equation": "t0^2=2",
                    "Sym4_parameter_w": 0,
                    "F4_gradient_at_image": [-1, -1],
                    "image_is_smooth": True,
                    "odd_q_arithmetic_status": "ghost remains: integral t would require t^2=2q, impossible for odd q",
                },
            ],
            "collapsed_Sym4_node": {
                "point": [0, 0],
                "normalization_preimage_equation": "w^2+w-1=0",
                "arithmetic_trace_exclusion": "w=t^2/q-2 is rational, but the two node parameters have discriminant 5",
            },
        },
        "frozen_genus2_incidence": incidence,
        "weight_and_Tate_twist_firewall": {
            "weights": "Sym^3 H^1 has weight 3; its exterior square and Sym^4 H^1 tensor det(H^1) have weight 6",
            "removed_line": "the direct summand (det V)^3 contributes the canonical factor 1-q^3*T removed in R_Q",
            "retained_middle_root": "Sym^4(V) tensor det(V) still has a pointwise q^3 eigenvalue, but irreducibility of Sym^4 gives no second common Tate line",
            "load_bearing_rescaling": "the surviving factor is P_Sym4(q*T), not P_Sym4(T); q is the determinant/Tate twist",
            "normalized_shapes_only": "the genus-two incidence compares coefficient shapes after normalization and does not identify weights, motives, local systems, families, or global L-functions",
            "arithmetic_ghost": "curve membership survives the map, so the Sym3 central ghost becomes a smooth Sym4-curve false positive rather than an arithmetic realization",
        },
        "literature_and_priority_boundary": {
            "classical_plethysm": "the rank-two representation decomposition is classical Clebsch-Gordan/plethysm and is not claimed as new",
            "classical_automorphy": [
                {
                    "result": "GL2 symmetric-cube transfer",
                    "authors": "Henry H. Kim and Freydoon Shahidi",
                    "url": "https://arxiv.org/abs/math/0409607",
                },
                {
                    "result": "GL2 symmetric-fourth transfer",
                    "author": "Henry H. Kim",
                    "url": "https://doi.org/10.1090/S0894-0347-02-00410-1",
                },
            ],
            "automorphy_dependency": "classical context only; no automorphy theorem is reproved or needed for the finite coefficient identities",
            "project_specific_contribution": "the commutative coefficient diagram and the frozen 251-atom incidence equality",
            "priority_claim": "none; no claim of literature priority for the diagram or packaging",
            "analytic_claim": "none; no RH, GRH, zero-free-region, or global functoriality consequence",
        },
        "next_family_target": {
            "name": "general_odd_symmetric_power_exterior_square_plethysm_ladder",
            "classical_representation_formula": "wedge^2 Sym^m(V)=direct_sum over odd i=1,3,...,m of Sym^(2m-2i)(V) tensor (det V)^i",
            "proposed_project_task": "derive the normalized coefficient maps and source-locked incidence pullbacks for successive odd m without fresh enumeration",
            "status": "nominated, not executed here",
        },
        "resource_contract": {
            "source_atom_cap_inclusive": SOURCE_ATOM_CAP_INCLUSIVE,
            "source_member_cap_inclusive": SOURCE_MEMBER_CAP_INCLUSIVE,
            "exclusive_accounted_work_unit_cap": ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE,
            "accounted_work_unit_ledger": guard.ledger(),
            "unit_definition": "declared high-level atom visits, torus weights, and symbolic coefficient comparisons; not literal arithmetic instructions or wall time",
            "field_or_curve_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "source_signed_atoms_transformed": SOURCE_ATOM_CAP_INCLUSIVE,
        },
        "scope_firewall": {
            "exact": [
                "characteristic-zero representation identity",
                "formal local-factor and normalized-curve identities",
                "deterministic transform of the four locked packet payloads",
            ],
            "imported": [
                "the completed Sym3, Sym4, primitive-exterior, and genus2-intersection packet payloads at the recorded hashes",
                "classical symmetric-cube and symmetric-fourth automorphy only as context",
            ],
            "nonclaims": [
                "no new finite-field or curve enumeration",
                "no arithmetic realization inferred from coefficient-curve membership",
                "no common Tate sub-local-system inferred from a pointwise middle root",
                "no family, motive, monodromy, Euler-product, priority, RH, or GRH claim",
            ],
        },
        "producer": {
            "script": _relative(Path(__file__)),
            "script_sha256_lf_normalized": _lf_normalized_sha256(Path(__file__)),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_normalized_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_normalized_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def write_fixture(path: Path = OUTPUT_PATH) -> None:
    fixture = build_fixture()
    path.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def check_fixture(path: Path = OUTPUT_PATH) -> None:
    stored = json.loads(path.read_text(encoding="utf-8"))
    expected = build_fixture()
    if stored != expected:
        raise RuntimeError(f"stored fixture does not match exact replay: {path}")
    unhashed = dict(stored)
    claimed = unhashed.pop("payload_sha256", None)
    if claimed != _canonical_sha256(unhashed):
        raise RuntimeError("stored fixture payload hash is invalid")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true", help="regenerate the adjacent JSON fixture")
    group.add_argument(
        "--check",
        nargs="?",
        const=str(OUTPUT_PATH),
        metavar="JSON",
        help="replay and compare with the adjacent or supplied fixture",
    )
    args = parser.parse_args()
    if args.write:
        write_fixture()
        print(f"wrote {OUTPUT_PATH}")
        return
    check_fixture(Path(args.check))
    print(f"verified {args.check}")


if __name__ == "__main__":
    main()
