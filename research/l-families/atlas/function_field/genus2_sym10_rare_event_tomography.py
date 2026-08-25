#!/usr/bin/env python3
"""Build exact rare-event tomography for the genus-two Sym10 channel."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym10_rare_event_tomography.json"
NOTE_PATH = HERE / "GENUS2_SYM10_RARE_EVENT_TOMOGRAPHY.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym10_rare_event_tomography.py"

BALANCED_PATH = HERE / "balanced_control_family_scan.json"
SYM10_PATH = HERE / "genus2_sym10_marked_trace_average.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "balanced_joint_law": {
        "path": BALANCED_PATH,
        "lf_sha256": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload_sha256": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
        "audited_commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
    },
    "sym10_theorem": {
        "path": SYM10_PATH,
        "lf_sha256": "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce",
        "payload_sha256": "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77",
        "audited_commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
    },
}

MAX_SOURCE_BYTES = 200_000
MAX_SOURCE_ATOMS = 512
MAX_RECURRENCE_UPDATES = 4_096
MAX_SYMBOLIC_OPERATIONS = 16_384
MAX_WALL_SECONDS = 3.0
EXPECTED_Q_VALUES = (3, 5, 7)

Monomial: TypeAlias = tuple[int, int, int]  # powers of a, b, q
Polynomial: TypeAlias = dict[Monomial, int]


@dataclass
class ResourceGuard:
    source_bytes: int = 0
    source_atoms: int = 0
    recurrence_updates: int = 0
    symbolic_operations: int = 0

    def bytes(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("source-byte increment must be nonnegative")
        self.source_bytes += amount
        if self.source_bytes > MAX_SOURCE_BYTES:
            raise RuntimeError("source-byte cap exceeded")

    def atoms(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("source-atom increment must be nonnegative")
        self.source_atoms += amount
        if self.source_atoms > MAX_SOURCE_ATOMS:
            raise RuntimeError("source-atom cap exceeded")

    def updates(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("recurrence-update increment must be nonnegative")
        self.recurrence_updates += amount
        if self.recurrence_updates > MAX_RECURRENCE_UPDATES:
            raise RuntimeError("recurrence-update cap exceeded")

    def operations(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("symbolic-operation increment must be nonnegative")
        self.symbolic_operations += amount
        if self.symbolic_operations > MAX_SYMBOLIC_OPERATIONS:
            raise RuntimeError("symbolic-operation cap exceeded")


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(data: bytes) -> str:
    normalized = unicodedata.normalize(
        "NFC", data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _poly_add(left: Polynomial, right: Polynomial, guard: ResourceGuard) -> Polynomial:
    guard.operations(len(left) + len(right) + 1)
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def _poly_scale(value: Polynomial, scalar: int, guard: ResourceGuard) -> Polynomial:
    guard.operations(len(value) + 1)
    if scalar == 0:
        return {}
    return {monomial: scalar * coefficient for monomial, coefficient in value.items()}


def _poly_shift(
    value: Polynomial, shift: Monomial, scalar: int, guard: ResourceGuard
) -> Polynomial:
    guard.operations(len(value) + 1)
    if scalar == 0:
        return {}
    return {
        tuple(
            power + increment for power, increment in zip(monomial, shift, strict=True)
        ): (scalar * coefficient)
        for monomial, coefficient in value.items()
    }


def _derive_reciprocal_tower(guard: ResourceGuard) -> list[Polynomial]:
    tower: list[Polynomial] = [{(0, 0, 0): 1}]
    for endpoint in range(1, 11):
        value: Polynomial = {}
        value = _poly_add(
            value, _poly_shift(tower[endpoint - 1], (1, 0, 0), -1, guard), guard
        )
        if endpoint >= 2:
            value = _poly_add(
                value,
                _poly_shift(tower[endpoint - 2], (0, 1, 0), -1, guard),
                guard,
            )
        if endpoint >= 3:
            value = _poly_add(
                value,
                _poly_shift(tower[endpoint - 3], (1, 0, 1), -1, guard),
                guard,
            )
        if endpoint >= 4:
            value = _poly_add(
                value,
                _poly_shift(tower[endpoint - 4], (0, 0, 2), -1, guard),
                guard,
            )
        tower.append(value)
    return tower


def _evaluate_polynomial(
    value: Polynomial,
    a: int,
    b: int,
    q: int,
    guard: ResourceGuard | None = None,
) -> int:
    if guard is not None:
        guard.operations(len(value) + 1)
    return sum(
        coefficient * a**a_power * b**b_power * q**q_power
        for (a_power, b_power, q_power), coefficient in value.items()
    )


def _evaluate_reciprocal_recurrence(
    a: int, b: int, q: int, endpoint: int, guard: ResourceGuard
) -> int:
    if endpoint < 0:
        raise ValueError("reciprocal endpoint must be nonnegative")
    values = [1]
    for index in range(1, endpoint + 1):
        guard.updates()
        value = -a * values[index - 1]
        if index >= 2:
            value -= b * values[index - 2]
        if index >= 3:
            value -= q * a * values[index - 3]
        if index >= 4:
            value -= q * q * values[index - 4]
        values.append(value)
    return values[endpoint]


def _serialize_polynomial(value: Polynomial) -> list[dict[str, int]]:
    return [
        {
            "a_power": monomial[0],
            "b_power": monomial[1],
            "q_power": monomial[2],
            "coefficient": coefficient,
        }
        for monomial, coefficient in sorted(value.items())
    ]


def _specialize_even_coefficient(
    value: Polynomial, *, a_scale: int, b_scale: int
) -> dict[int, int]:
    """Substitute a=a_scale*s, b=b_scale*s^2, q=s^2."""

    result: dict[int, int] = {}
    for (a_power, b_power, q_power), coefficient in value.items():
        if a_scale == 0 and a_power:
            continue
        exponent = a_power + 2 * b_power + 2 * q_power
        scaled = coefficient * a_scale**a_power * b_scale**b_power
        result[exponent] = result.get(exponent, 0) + scaled
        if result[exponent] == 0:
            del result[exponent]
    return result


def _derive_compact_certificate(
    tower: list[Polynomial], guard: ResourceGuard
) -> dict[str, object]:
    resonance_rows: list[dict[str, object]] = []
    for n in range(6):
        endpoint = 2 * n
        plus = _specialize_even_coefficient(tower[endpoint], a_scale=0, b_scale=2)
        minus = _specialize_even_coefficient(tower[endpoint], a_scale=0, b_scale=-2)
        guard.operations(len(plus) + len(minus) + 2)
        expected_plus = {2 * n: (-1) ** n * (n + 1)}
        expected_minus = {2 * n: n + 1}
        if plus != expected_plus or minus != expected_minus:
            raise ArithmeticError("central quadratic-square resonance drifted")
        resonance_rows.append(
            {
                "n": n,
                "endpoint": endpoint,
                "P=(1+qT^2)^2": (-1) ** n * (n + 1),
                "P=(1-qT^2)^2": n + 1,
                "normalization": "listed coefficient times q^n",
            }
        )

    dimension = math.comb(13, 3)
    scalar_plus = _specialize_even_coefficient(tower[10], a_scale=-4, b_scale=6)
    scalar_minus = _specialize_even_coefficient(tower[10], a_scale=4, b_scale=6)
    if scalar_plus != {10: dimension} or scalar_minus != {10: dimension}:
        raise ArithmeticError("scalar compact ceiling specialization drifted")

    return {
        "central_quadratic_square_ladder": resonance_rows,
        "sym10_dimension": dimension,
        "compact_triangle_bound": "abs(chi_(10,0)(U))<=286",
        "equality_rigidity": {
            "monomial_comparison": (
                "equality in the 286-term triangle bound makes z_i^10 and "
                "z_i^9*z_j have the same phase, hence every z_j=z_i"
            ),
            "symplectic_consequence": (
                "the common eigenvalue equals its inverse, hence U=I or U=-I"
            ),
            "only_equality_classes": ["I", "-I"],
        },
        "scalar_coefficient_rows": [
            {
                "U": "I",
                "a": "-4*sqrt(q)",
                "b": "6*q",
                "P": "(1-sqrt(q)*T)^4",
                "r_10": "286*q^5",
            },
            {
                "U": "-I",
                "a": "4*sqrt(q)",
                "b": "6*q",
                "P": "(1+sqrt(q)*T)^4",
                "r_10": "286*q^5",
            },
        ],
        "integrality_boundary": (
            "the scalar coefficient rows are integral only when q is a square; "
            "geometric realization is not asserted"
        ),
    }


def _load_sources(guard: ResourceGuard) -> dict[str, dict[str, object]]:
    loaded: dict[str, dict[str, object]] = {}
    for name in sorted(SOURCE_LOCKS):
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source-lock path must be a Path")
        remaining = MAX_SOURCE_BYTES - guard.source_bytes
        if remaining < 0:
            raise RuntimeError("source-byte cap already exceeded")
        with path.open("rb") as source_handle:
            data = source_handle.read(remaining + 1)
        if len(data) > remaining:
            raise RuntimeError("source-byte cap exceeded before full read")
        guard.bytes(len(data))
        if _lf_sha256(data) != lock["lf_sha256"]:
            raise RuntimeError(f"LF-normalized source hash mismatch: {name}")
        parsed = json.loads(data)
        claimed = parsed.get("payload_sha256")
        if claimed != lock["payload_sha256"]:
            raise RuntimeError(f"payload source hash mismatch: {name}")
        payload = dict(parsed)
        payload.pop("payload_sha256")
        if _canonical_sha256(payload) != claimed:
            raise RuntimeError(f"canonical source payload mismatch: {name}")
        loaded[name] = parsed
    return loaded


def _is_integral_split(a: int, b: int, q: int) -> bool:
    discriminant = a * a - 4 * b + 8 * q
    if discriminant < 0:
        return False
    root = math.isqrt(discriminant)
    return root * root == discriminant and (-a + root) % 2 == 0


def _is_sym3_curve(a: int, b: int, q: int) -> bool:
    return -q * a**4 + q * a * a * b + q * q * a * a + b**3 - 2 * q * b * b == 0


def _locus_summary(
    rows: list[dict[str, object]],
    tail: list[dict[str, object]],
    predicate: str,
    total_l2: int,
) -> dict[str, object]:
    selected = [row for row in rows if row[predicate] is True]
    selected_tail = [row for row in tail if row[predicate] is True]
    members = sum(int(row["member_count"]) for row in selected)
    signed_sum = sum(int(row["r_10"]) * int(row["member_count"]) for row in selected)
    second = sum(int(row["r_10"]) ** 2 * int(row["member_count"]) for row in selected)
    return {
        "member_count": members,
        "tail_member_count": sum(int(row["member_count"]) for row in selected_tail),
        "signed_sum_r_10": signed_sum,
        "mean_r_10": _fraction_pair(Fraction(signed_sum, members))
        if members
        else [0, 1],
        "share_of_full_second_moment": _fraction_pair(Fraction(second, total_l2)),
    }


def _family_tomography(
    family: dict[str, object],
    expected: dict[str, object],
    r10_polynomial: Polynomial,
    guard: ResourceGuard,
) -> dict[str, object]:
    q = family.get("q")
    if not isinstance(q, int) or q not in EXPECTED_Q_VALUES:
        raise TypeError("unexpected finite-family q row")
    joint = family.get("joint_a_D_b_D_law")
    if not isinstance(joint, dict) or not isinstance(joint.get("atoms"), list):
        raise TypeError("balanced joint law schema drifted")
    atoms = joint["atoms"]
    guard.atoms(len(atoms))

    rows: list[dict[str, object]] = []
    for atom in atoms:
        if not isinstance(atom, dict):
            raise TypeError("joint-law atom must be a dictionary")
        a = atom.get("a_D")
        b = atom.get("b_D")
        member_count = atom.get("member_count")
        if not all(isinstance(value, int) for value in (a, b, member_count)):
            raise TypeError("joint-law atom lost integral coordinates")
        if member_count <= 0:
            raise ValueError("joint-law atom has nonpositive mass")
        r10 = _evaluate_reciprocal_recurrence(a, b, q, 10, guard)
        polynomial_oracle = _evaluate_polynomial(r10_polynomial, a, b, q, guard)
        if polynomial_oracle != r10:
            raise ArithmeticError("direct recurrence and sparse polynomial disagree")
        discriminant = a * a - 4 * b + 8 * q
        row = {
            "a_D": a,
            "b_D": b,
            "member_count": member_count,
            "r_10": r10,
            "absolute_r_10": abs(r10),
            "integral_split": _is_integral_split(a, b, q),
            "repeated_factor": discriminant == 0,
            "sym3_coefficient_curve": _is_sym3_curve(a, b, q),
            "central_plus": a == 0 and b == 2 * q,
            "central_minus": a == 0 and b == -2 * q,
        }
        rows.append(row)

    member_count = sum(int(row["member_count"]) for row in rows)
    expected_members = family.get("expected_squarefree_count")
    if member_count != expected_members or member_count != expected.get("members"):
        raise ArithmeticError("complete family member mass drifted")
    if len(rows) != expected.get("joint_law_atoms"):
        raise ArithmeticError("joint-law atom count drifted")

    total = sum(int(row["r_10"]) * int(row["member_count"]) for row in rows)
    if total != expected.get("theorem_sum_r_D_10"):
        raise ArithmeticError("Sym10 family total does not match theorem")
    total_l1 = sum(int(row["absolute_r_10"]) * int(row["member_count"]) for row in rows)
    total_l2 = sum(int(row["r_10"]) ** 2 * int(row["member_count"]) for row in rows)
    if total_l1 <= 0 or total_l2 <= 0:
        raise ArithmeticError("nontrivial Sym10 norm vanished")

    required_tail_mass = (member_count + 99) // 100
    accumulated = 0
    threshold: int | None = None
    for value in sorted({int(row["absolute_r_10"]) for row in rows}, reverse=True):
        accumulated += sum(
            int(row["member_count"])
            for row in rows
            if int(row["absolute_r_10"]) == value
        )
        if accumulated >= required_tail_mass:
            threshold = value
            break
    if threshold is None:
        raise ArithmeticError("failed to locate tied tail threshold")
    tail = [row for row in rows if int(row["absolute_r_10"]) >= threshold]
    tail_members = sum(int(row["member_count"]) for row in tail)
    bulk_members = member_count - tail_members
    if tail_members < required_tail_mass or bulk_members <= 0:
        raise ArithmeticError("invalid tied tail partition")
    tail_total = sum(int(row["r_10"]) * int(row["member_count"]) for row in tail)
    bulk_total = total - tail_total
    tail_l1 = sum(int(row["absolute_r_10"]) * int(row["member_count"]) for row in tail)
    tail_l2 = sum(int(row["r_10"]) ** 2 * int(row["member_count"]) for row in tail)

    sign_counts = {
        "negative": sum(
            int(row["member_count"]) for row in rows if int(row["r_10"]) < 0
        ),
        "zero": sum(int(row["member_count"]) for row in rows if int(row["r_10"]) == 0),
        "positive": sum(
            int(row["member_count"]) for row in rows if int(row["r_10"]) > 0
        ),
    }
    if sum(sign_counts.values()) != member_count:
        raise ArithmeticError("sign partition lost mass")

    loci = {
        name: _locus_summary(rows, tail, name, total_l2)
        for name in (
            "integral_split",
            "repeated_factor",
            "sym3_coefficient_curve",
            "central_plus",
            "central_minus",
        )
    }
    zero_atoms = [
        {
            "a_D": row["a_D"],
            "b_D": row["b_D"],
            "member_count": row["member_count"],
            "sym3_coefficient_curve": row["sym3_coefficient_curve"],
        }
        for row in rows
        if row["r_10"] == 0
    ]

    return {
        "q": q,
        "source_atom_count": len(rows),
        "member_count": member_count,
        "sign_member_counts": sign_counts,
        "sum_r_10": total,
        "mean_r_10": _fraction_pair(Fraction(total, member_count)),
        "sum_absolute_r_10": total_l1,
        "sum_r_10_squared": total_l2,
        "tied_outer_absolute_one_percent_tail": {
            "minimum_required_mass": required_tail_mass,
            "threshold": threshold,
            "member_count": tail_members,
            "member_fraction": _fraction_pair(Fraction(tail_members, member_count)),
            "signed_sum_r_10": tail_total,
            "mean_r_10": _fraction_pair(Fraction(tail_total, tail_members)),
            "share_of_signed_total": _fraction_pair(Fraction(tail_total, total)),
            "share_of_absolute_first_moment": _fraction_pair(
                Fraction(tail_l1, total_l1)
            ),
            "share_of_second_moment": _fraction_pair(Fraction(tail_l2, total_l2)),
            "atoms": sorted(
                tail,
                key=lambda row: (
                    -int(row["absolute_r_10"]),
                    int(row["a_D"]),
                    int(row["b_D"]),
                ),
            ),
        },
        "trimmed_bulk": {
            "member_count": bulk_members,
            "signed_sum_r_10": bulk_total,
            "mean_r_10": _fraction_pair(Fraction(bulk_total, bulk_members)),
        },
        "exceptional_loci": loci,
        "zero_atoms": zero_atoms,
    }


def _source_manifest() -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for name in sorted(SOURCE_LOCKS):
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source-lock path must be a Path")
        manifest.append(
            {
                "name": name,
                "path": path.relative_to(ROOT).as_posix(),
                "lf_sha256": lock["lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "audited_commit": lock["audited_commit"],
            }
        )
    return manifest


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    guard = ResourceGuard()

    tower = _derive_reciprocal_tower(guard)
    r10_polynomial = tower[10]
    compact = _derive_compact_certificate(tower, guard)
    symbolic_operations_before_sources = guard.symbolic_operations

    sources = _load_sources(guard)
    balanced = sources["balanced_joint_law"]
    sym10 = sources["sym10_theorem"]
    frozen = balanced.get("frozen_enumeration_facts")
    controls = sym10.get("held_out_falsification_controls")
    if not isinstance(frozen, dict) or not isinstance(frozen.get("families"), list):
        raise TypeError("balanced family source schema drifted")
    if frozen.get("q_values") != list(EXPECTED_Q_VALUES):
        raise RuntimeError("balanced source q ladder drifted")
    if not isinstance(controls, list):
        raise TypeError("Sym10 controls schema drifted")
    control_by_q = {row.get("q"): row for row in controls if isinstance(row, dict)}
    if tuple(sorted(control_by_q)) != EXPECTED_Q_VALUES:
        raise RuntimeError("Sym10 control q ladder drifted")

    families = [
        _family_tomography(family, control_by_q[family["q"]], r10_polynomial, guard)
        for family in frozen["families"]
    ]
    if tuple(row["q"] for row in families) != EXPECTED_Q_VALUES:
        raise RuntimeError("finite family order drifted")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym10_rare_event_tomography.v1",
        "status": "EXACT_COMPLETE_TOMOGRAPHY_ONLY_FOR_Q_3_5_7",
        "scope": {
            "family": "monic squarefree quintics over F_q[T]",
            "q_values": list(EXPECTED_Q_VALUES),
            "coverage": "complete member-uniform source laws for exactly q=3,5,7",
            "finite_fields_enumerated_by_this_replay": 0,
            "curves_enumerated_by_this_replay": 0,
            "polynomials_enumerated_by_this_replay": 0,
            "source_atoms_visited": sum(row["source_atom_count"] for row in families),
            "source_members_represented": sum(row["member_count"] for row in families),
        },
        "definition": {
            "local_factor": "P_D(T)=1+a_D*T+b_D*T^2+q*a_D*T^3+q^2*T^4",
            "reciprocal_series": "P_D(T)^(-1)=sum_n r_D(n)T^n",
            "channel": "r_D(10)=q^5*chi_(10,0)(U_D)",
            "tied_tail": (
                "include all atoms at the largest descending absolute threshold whose "
                "retained member mass is at least ceil(N/100)"
            ),
        },
        "formal_recurrence_certificate": {
            "recurrence": ("r_n=-a*r_(n-1)-b*r_(n-2)-q*a*r_(n-3)-q^2*r_(n-4)"),
            "initial_condition": "r_0=1 and r_n=0 for n<0",
            "r_10_sparse_polynomial": _serialize_polynomial(r10_polynomial),
            "derived_before_sources_loaded": True,
        },
        "compact_resonance_certificate": compact,
        "finite_tomography": {"families": families},
        "source_order_firewall": {
            "symbolic_recurrence_and_compact_certificate_closed_before_sources": True,
            "symbolic_operations_before_sources": symbolic_operations_before_sources,
        },
        "source_manifest": _source_manifest(),
        "firewalls": [
            "The q=3,5,7 rows are complete finite censuses, not an all-q distribution or tail theorem.",
            "A split, repeated, Sym3, or zero coefficient predicate is not a motive, monodromy, endomorphism, or compatible-system certificate.",
            "The square-field scalar equality row is only a compact/integrality consequence; geometric realization is not asserted.",
            "No zero-density, RH, GRH, memberwise sign, or average-to-individual conclusion is made.",
        ],
        "resource_contract": {
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "actual_source_bytes": guard.source_bytes,
            "maximum_source_atoms": MAX_SOURCE_ATOMS,
            "actual_source_atoms": guard.source_atoms,
            "maximum_recurrence_updates": MAX_RECURRENCE_UPDATES,
            "actual_recurrence_updates": guard.recurrence_updates,
            "maximum_symbolic_operations": MAX_SYMBOLIC_OPERATIONS,
            "actual_symbolic_operations": guard.symbolic_operations,
            "formal_symbolic_operations_before_sources": (
                symbolic_operations_before_sources
            ),
            "recurrence_steps_per_atom": 10,
            "sparse_oracle_terms_per_atom": len(r10_polynomial),
            "sparse_oracle_operation_units_per_atom": len(r10_polynomial) + 1,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact integers and Fraction ratios only",
        },
        "replay": {
            "producer": OUTPUT_PATH.with_suffix(".py").relative_to(ROOT).as_posix(),
            "note": NOTE_PATH.relative_to(ROOT).as_posix(),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "write": (
                "python research/l-families/atlas/function_field/"
                "genus2_sym10_rare_event_tomography.py --write"
            ),
            "check": (
                "python research/l-families/atlas/function_field/"
                "genus2_sym10_rare_event_tomography.py --check"
            ),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    elapsed = time.perf_counter() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("Sym10 rare-event replay exceeded wall cap")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write canonical JSON")
    parser.add_argument("--check", action="store_true", help="check canonical JSON")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
        return
    if not OUTPUT_PATH.exists():
        raise FileNotFoundError(f"missing canonical fixture: {OUTPUT_PATH}")
    if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
        raise RuntimeError(f"canonical fixture mismatch: {OUTPUT_PATH}")
    print(f"verified {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
