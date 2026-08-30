#!/usr/bin/env python3
"""Exact Gate-0 replay for marked-place descent after signed cleanup.

The all-odd-q support theorem is proved in the companion note.  This replay
authenticates the frozen sources, exact q=3,5 rank panels, the Pi_0/Moebius/
Wick coefficient ledger, and quadratic-extension witnesses for the partial-
Frobenius support shift.  It enumerates no curve, closed place, L-function,
or zero.
"""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Self

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_MARKED_PLACE_SIGNED_DESCENT_GATE0.md"
FIXTURE_PATH = HERE / "ffps_marked_place_signed_descent_gate0.json"
SOURCE_LOCK_PATH = HERE / "ffps_marked_place_signed_descent_gate0.sources.json"

SOURCE_BLOBS = {
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/FFPS_MARKED_PLACE_BIFROBENIUS_GLUING_GATE.md",
    ): "a04eaa8a1fd5838f7bbe605dc9c8099e0f033511",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/FFPS_TERNARY_RELATIVE_CORRESPONDENCE_NORMAL_FORM.md",
    ): "4ee3c50f3cce3e7aa2dbd901b93fd50b713ea4bb",
    (
        "d79692ece0b7604ad309c459f565b24e9926f5c5",
        "research/l-families/atlas/function_field/FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md",
    ): "19939eb240ca6b2b6d5221954cec76fe0f5c4f9c",
    (
        "3a595dda92ef827a41e50d2395309692a93748ad",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_FIRST_ADAMS_CLOSURE.md",
    ): "aba88795dd1c95cb320d45c1dc367cd71d73e1d5",
    (
        "3a595dda92ef827a41e50d2395309692a93748ad",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_PHASE_STRATIFIED_EXTERNALIZATION.md",
    ): "68e99e25539de79955ef11534056b9e82b57cb60",
    (
        "3a595dda92ef827a41e50d2395309692a93748ad",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_TRACE_TENSOR_CLOSURE.md",
    ): "37647db8c43b983dc64bfc71a0c112539119a98a",
    (
        "3a595dda92ef827a41e50d2395309692a93748ad",
        "research/l-families/atlas/function_field/FFPS_RELATIVE_EXTERNAL_DIAGONAL_ADAMS.md",
    ): "884f2fc949bbd5b076df0c0c7afd4711f81ce37e",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md",
    ): "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md",
    ): "e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a",
}

Q_CONTROLS = (3, 5)
MAX_Q = 5
MAX_MATRIX_DIMENSION = 2 * MAX_Q * (MAX_Q - 1)
MAX_MATRIX_ENTRIES = MAX_MATRIX_DIMENSION**2

Matrix = tuple[tuple[Fraction, ...], ...]


def validate_q(q: int) -> None:
    if isinstance(q, bool) or not isinstance(q, int) or q not in Q_CONTROLS:
        raise ValueError("the bounded replay supports exactly q=3 and q=5")


def matrix_rank(matrix: Matrix) -> int:
    """Return exact row rank by Fraction Gaussian elimination."""

    if not matrix:
        return 0
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise ValueError("matrix must be nonempty and rectangular")
    work = [list(row) for row in matrix]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[pivot_row], strict=True)
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def ordered_distinct_pairs(q: int) -> tuple[tuple[int, int], ...]:
    validate_q(q)
    return tuple(
        (left, right) for left in range(q) for right in range(q) if left != right
    )


def fixed_label_coefficient_slice(q: int, ell: int, rho: int) -> Matrix:
    """The fixed-(ell,rho) (c)|(d) selector is one external product."""

    validate_q(q)
    if not 0 <= ell < q or not 0 <= rho < q or ell == rho:
        raise ValueError("fixed labels must be distinct field elements")
    return tuple(
        tuple(Fraction(c == ell and d == rho) for d in range(q)) for c in range(q)
    )


def marked_cross_matrix(q: int) -> Matrix:
    """Crossed selector on the source-faithful labelled allocation.

    Rows are (ell,d), columns are (rho,c), all ordered pairs being distinct.
    The entry is one exactly when c=ell and d=rho.  It is the swap
    permutation matrix and therefore has rank q(q-1).
    """

    pairs = ordered_distinct_pairs(q)
    return tuple(
        tuple(Fraction(c == ell and d == rho) for rho, c in pairs) for ell, d in pairs
    )


def wick_oriented_cross_matrix(q: int) -> Matrix:
    """Two off-atomic Wick orientations; same-label blocks are absent."""

    base = marked_cross_matrix(q)
    size = len(base)
    return tuple(
        tuple(
            base[row % size][column % size]
            if row // size == column // size
            else Fraction(0)
            for column in range(2 * size)
        )
        for row in range(2 * size)
    )


def orientation_forgotten_cross_matrix(q: int) -> Matrix:
    """Forget the two Wick orientations, so their labelled blocks add to 2*M_q."""

    return tuple(tuple(2 * entry for entry in row) for row in marked_cross_matrix(q))


def separable_control_matrix(q: int) -> Matrix:
    """A nonzero clean external product on the same finite index sets."""

    size = len(ordered_distinct_pairs(q))
    left = tuple(Fraction(index + 1) for index in range(size))
    right = tuple(Fraction((-1) ** index) for index in range(size))
    return tuple(tuple(a * b for b in right) for a in left)


def source_blind_phase_matrix(q: int) -> Matrix:
    """Counterfeit obtained by dropping both crossed source selectors."""

    size = len(ordered_distinct_pairs(q))
    return tuple(tuple(Fraction(1) for _ in range(size)) for _ in range(size))


def principal_projector(order: int) -> Matrix:
    if isinstance(order, bool) or not isinstance(order, int) or order < 2:
        raise ValueError("cyclic order must be at least two")
    return tuple(tuple(Fraction(1, order) for _ in range(order)) for _ in range(order))


def apply_matrix(matrix: Matrix, vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if not matrix or len(matrix[0]) != len(vector):
        raise ValueError("matrix and vector dimensions do not compose")
    return tuple(
        sum(
            (entry * value for entry, value in zip(row, vector, strict=True)),
            Fraction(),
        )
        for row in matrix
    )


def pi0_invariant_coefficient(order: int = 3) -> Fraction:
    projector = principal_projector(order)
    invariant = tuple(Fraction(1) for _ in range(order))
    if apply_matrix(projector, invariant) != invariant:
        raise ArithmeticError("Pi_0 failed to preserve the invariant deck line")
    return Fraction(1)


def linear_core_moebius_coprimality(left_root: int, right_root: int) -> int:
    """Sum mu(m) over common monic divisors of two monic linear cores."""

    return 1 if left_root != right_root else 0


def wick_label_coefficient(left_label: int, right_label: int) -> int:
    """Literal normal ordering deletes the same labelled atom only."""

    return int(left_label != right_label)


def post_cleanup_generic_coefficient(
    ell: int, rho: int, left_label: int, right_label: int
) -> Fraction:
    return (
        pi0_invariant_coefficient()
        * linear_core_moebius_coprimality(ell, rho)
        * wick_label_coefficient(left_label, right_label)
    )


@dataclass(frozen=True)
class Fq2:
    """Element a+b*t with t^2=nonsquare in the q=3,5 controls."""

    q: int
    nonsquare: int
    a: int
    b: int

    def __post_init__(self) -> None:
        validate_q(self.q)
        if self.nonsquare % self.q != 2:
            raise ValueError("the frozen controls use t^2=2")
        object.__setattr__(self, "a", self.a % self.q)
        object.__setattr__(self, "b", self.b % self.q)

    def _coerce(self, other: object) -> Self:
        if isinstance(other, int):
            return type(self)(self.q, self.nonsquare, other, 0)
        if not isinstance(other, Fq2):
            return NotImplemented
        if (self.q, self.nonsquare) != (other.q, other.nonsquare):
            raise ValueError("finite-field parameters differ")
        return other

    def __add__(self, other: object) -> Self:
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return type(self)(self.q, self.nonsquare, self.a + rhs.a, self.b + rhs.b)

    def __sub__(self, other: object) -> Self:
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return type(self)(self.q, self.nonsquare, self.a - rhs.a, self.b - rhs.b)

    def __mul__(self, other: object) -> Self:
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return type(self)(
            self.q,
            self.nonsquare,
            self.a * rhs.a + self.b * rhs.b * self.nonsquare,
            self.a * rhs.b + self.b * rhs.a,
        )

    def __pow__(self, exponent: int) -> Self:
        if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
            raise ValueError("exponent must be a nonnegative integer")
        result = type(self)(self.q, self.nonsquare, 1, 0)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def square(self) -> Self:
        return self * self

    def as_pair(self) -> list[int]:
        return [self.a, self.b]


@dataclass(frozen=True)
class CrossedPoint:
    lam: Fq2
    y: Fq2
    rho: Fq2
    x: Fq2


def clean_crossed_point(q: int) -> CrossedPoint:
    """Use lambda=t, rho=1 on t^2=2 over the quadratic extension of F_q."""

    validate_q(q)
    lam = Fq2(q, 2, 0, 1)
    rho = Fq2(q, 2, 1, 0)
    x = (rho - lam).square()
    y = (lam - rho).square()
    return CrossedPoint(lam=lam, y=y, rho=rho, x=x)


def crossed_support_holds(point: CrossedPoint) -> bool:
    return (
        point.lam != point.rho
        and point.x == (point.rho - point.lam).square()
        and point.y == (point.lam - point.rho).square()
    )


def left_partial_frobenius(point: CrossedPoint) -> CrossedPoint:
    q = point.lam.q
    return CrossedPoint(
        lam=point.lam**q,
        y=point.y**q,
        rho=point.rho,
        x=point.x,
    )


def right_partial_frobenius(point: CrossedPoint) -> CrossedPoint:
    q = point.lam.q
    return CrossedPoint(
        lam=point.lam,
        y=point.y,
        rho=point.rho**q,
        x=point.x**q,
    )


def total_frobenius(point: CrossedPoint) -> CrossedPoint:
    q = point.lam.q
    return CrossedPoint(
        lam=point.lam**q,
        y=point.y**q,
        rho=point.rho**q,
        x=point.x**q,
    )


def serialize_point(point: CrossedPoint) -> dict[str, list[int]]:
    return {
        "lambda": point.lam.as_pair(),
        "Y": point.y.as_pair(),
        "rho": point.rho.as_pair(),
        "X": point.x.as_pair(),
    }


def check_source_blobs() -> None:
    for (commit, path), expected_blob in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=4.0,
        )
        if completed.returncode:
            raise RuntimeError(
                "locked source object/path unavailable: "
                f"{commit}:{path}; fetch without merging via "
                f"`git fetch --no-tags origin {commit}`"
            )
        if completed.stdout.strip() != expected_blob:
            raise RuntimeError(f"source blob mismatch: {commit}:{path}")


def check_source_lock_manifest() -> None:
    manifest = json.loads(SOURCE_LOCK_PATH.read_text(encoding="utf-8"))
    observed = {
        (entry["commit"], entry["path"]): entry["git_blob"]
        for entry in manifest["sources"]
    }
    if observed != SOURCE_BLOBS:
        raise RuntimeError("source-lock manifest does not match producer constants")
    if manifest["base_commit"] != "b870366141fe8d5f43d5b81f6e50a67d2a888070":
        raise RuntimeError("source-lock base commit changed")


def build_q_panel(q: int) -> dict[str, object]:
    validate_q(q)
    fixed_ranks = {
        matrix_rank(fixed_label_coefficient_slice(q, ell, rho))
        for ell, rho in ordered_distinct_pairs(q)
    }
    marked = marked_cross_matrix(q)
    wick = wick_oriented_cross_matrix(q)
    forgotten = orientation_forgotten_cross_matrix(q)
    separable = separable_control_matrix(q)
    source_blind = source_blind_phase_matrix(q)
    expected_size = q * (q - 1)
    if fixed_ranks != {1}:
        raise ArithmeticError("a fixed coefficient-partition slice lost rank one")
    if matrix_rank(marked) != expected_size:
        raise ArithmeticError("marked crossed-selector panel lost full rank")
    if matrix_rank(wick) != 2 * expected_size:
        raise ArithmeticError("off-atomic Wick orientations lost their rank ledger")
    if matrix_rank(forgotten) != expected_size:
        raise ArithmeticError("orientation-forgotten Wick panel lost rank q(q-1)")
    if matrix_rank(separable) != 1 or matrix_rank(source_blind) != 1:
        raise ArithmeticError("positive/counterfeit external controls lost rank one")

    point = clean_crossed_point(q)
    left = left_partial_frobenius(point)
    right = right_partial_frobenius(point)
    total = total_frobenius(point)
    support_truth = {
        "original": crossed_support_holds(point),
        "left_partial": crossed_support_holds(left),
        "right_partial": crossed_support_holds(right),
        "total": crossed_support_holds(total),
    }
    if support_truth != {
        "original": True,
        "left_partial": False,
        "right_partial": False,
        "total": True,
    }:
        raise ArithmeticError("quadratic-extension Frobenius witness changed")

    return {
        "q": q,
        "ordered_distinct_place_pairs": expected_size,
        "fixed_label_coefficient_partition_ranks": sorted(fixed_ranks),
        "separable_positive_control_rank": matrix_rank(separable),
        "source_blind_phase_only_rank": matrix_rank(source_blind),
        "source_faithful_marked_cross_rank": matrix_rank(marked),
        "post_wick_orientation_forgotten_rank": matrix_rank(forgotten),
        "post_wick_two_orientation_rank": matrix_rank(wick),
        "post_cleanup_generic_support_coefficient": str(
            post_cleanup_generic_coefficient(0, 1, 0, 1)
        ),
        "frobenius_support_truth": support_truth,
        "frobenius_witness": {
            "field": f"F_{q}[t]/(t^2-2)",
            "original": serialize_point(point),
            "left_partial": serialize_point(left),
            "right_partial": serialize_point(right),
            "total": serialize_point(total),
        },
    }


def build_report() -> dict[str, object]:
    panels = [build_q_panel(q) for q in Q_CONTROLS]
    return {
        "schema": "riemann.function_field.ffps_marked_place_signed_descent_gate0.v1",
        "status": "EXACT_SCOPED_NO_GO_AND_PARTITION_RECONCILIATION",
        "arithmetic_class": "EXACT_RATIONAL_AND_FINITE_FIELD_EXTENSION_CONTROL",
        "theorem_ledger": {
            "MPD-G0.1": "FIXED_LABEL_TRACE_EXTERNALITY_IMPORTED_AND_REDERIVED",
            "MPD-G0.2": "CLEAN_MARKED_SUPPORT_SHIFT_PROVED_ALL_ODD_Q_IN_NOTE",
            "MPD-G0.3": "POST_CLEANUP_GENERIC_SUPPORT_SURVIVAL_PROVED_ON_CLEAN_STRATUM",
            "MPD-G0.4": "PARTITION_RANK_TAX_PROVED_ALL_FINITE_INDEX_SETS_IN_NOTE",
            "MPD-G0.5": "COMPLETE_SIGNED_PUSHFORWARD_AND_RELTRACE_REMAIN_OPEN",
        },
        "cleanup_ledger": {
            "Pi_0_invariant_line_coefficient": str(pi0_invariant_coefficient()),
            "linear_core_Moebius_coprimality_on_distinct_open": linear_core_moebius_coprimality(
                0, 1
            ),
            "literal_Wick_ordered_off_atomic_coefficient": wick_label_coefficient(0, 1),
            "combined_generic_support_coefficient": str(
                post_cleanup_generic_coefficient(0, 1, 0, 1)
            ),
        },
        "finite_controls": panels,
        "reconciliation": {
            "coefficient_partition": "fixed (ell,rho): (P,c)|(Q,d)",
            "marked_place_partition": "(ell,h,Y,Y')|(rho,k,X,X')",
            "verdict": (
                "trace externality in the coefficient partition does not imply "
                "partial-Frobenius descent in the marked-place partition"
            ),
        },
        "not_proved": [
            "noncancellation after the complete signed source pushforward",
            "ONEPLACEWEIL for the complete native amplitudes",
            "commuting partial Frobenii for the complete relative object",
            "uniform ONEPLACETRACE or RELTRACE",
            "principal binding to the frozen RH consumer",
            "RH or GRH",
        ],
        "resource_ledger": {
            "q_controls": list(Q_CONTROLS),
            "maximum_matrix_dimension": MAX_MATRIX_DIMENSION,
            "maximum_matrix_entries": MAX_MATRIX_ENTRIES,
            "base_field_labels_enumerated": sum(Q_CONTROLS),
            "ordered_distinct_pairs_materialized": sum(q * (q - 1) for q in Q_CONTROLS),
            "quadratic_extension_point_transforms_checked": 4 * len(Q_CONTROLS),
            "source_blobs_authenticated": len(SOURCE_BLOBS),
            "polynomial_or_closed_place_families_enumerated": 0,
            "curves_or_pushforwards_computed": 0,
            "floating_point_operations": 0,
        },
    }


def rendered_report() -> str:
    return json.dumps(build_report(), indent=2, sort_keys=True) + "\n"


def check_note_contract() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "MPD-G0.3 — post-cleanup generic-support survival",
        "coefficient partition",
        "marked-place partition",
        "universal coefficient space",
        "base-field trace",
        "place at infinity is outside",
        "complete signed pushforward remains undecided",
        "ONEPLACEWEIL",
        "RH and GRH remain unproved",
    ):
        if marker not in note:
            raise RuntimeError(f"note contract marker missing: {marker}")


def check_no_assert_statements() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    if any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
        raise RuntimeError("producer must not use optimization-sensitive assert")


def run_checks() -> dict[str, object]:
    check_source_blobs()
    check_source_lock_manifest()
    check_note_contract()
    check_no_assert_statements()
    report = build_report()
    if (
        FIXTURE_PATH.read_text(encoding="utf-8")
        != json.dumps(report, indent=2, sort_keys=True) + "\n"
    ):
        raise RuntimeError("canonical JSON fixture is stale")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = run_checks() if args.check else build_report()
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
