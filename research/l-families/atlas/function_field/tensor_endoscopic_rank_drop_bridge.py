#!/usr/bin/env python3
"""Exact bridge from tensor rank drop to the integral +q split locus.

This packet performs sparse monomial-ideal algebra and a deterministic
convolution of source-locked q=3,5,7 histograms.  It enumerates no field,
curve, variety, or family member.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "tensor_endoscopic_rank_drop_bridge.json"
NOTE_PATH = HERE / "TENSOR_ENDOSCOPIC_RANK_DROP_BRIDGE.md"
TEST_PATH = ROOT / "tests" / "test_tensor_endoscopic_rank_drop_bridge.py"

TENSOR_FIXTURE_PATH = HERE / "tensor_trace_zero_singular_strata.json"
TENSOR_SOURCE_PATH = HERE / "tensor_trace_zero_singular_strata.py"
ENDOSCOPIC_FIXTURE_PATH = HERE / "genus2_endoscopic_split_locus.json"
ENDOSCOPIC_SOURCE_PATH = HERE / "genus2_endoscopic_split_locus.py"
GENUS1_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_SOURCE_PATH = HERE / "genus1_cubic_family_laws.py"
BALANCED_FIXTURE_PATH = HERE / "balanced_control_family_scan.json"
BALANCED_SOURCE_PATH = HERE / "balanced_control_family_scan.py"

FROZEN_Q_VALUES = (3, 5, 7)
HISTOGRAM_WORK_CAP_EXCLUSIVE = 5_000
NO_SPLIT = "no_integral_q_elliptic_form_factorization"
SPLIT_KINDS = frozenset({"split_repeated", "split_distinct"})

EXPECTED_FIXTURES = {
    "tensor": {
        "path": TENSOR_FIXTURE_PATH,
        "schema": "riemann.product-tensor-trace-zero-singular-strata.v1",
        "payload": "f34aec41ee76a79715e2dc20b522c0dab19b87a507db951c17018b30a0d21592",
        "file": "570d334f883963003547f53857c452381ebb0540c2cb2177661062366d5f04e8",
    },
    "endoscopic": {
        "path": ENDOSCOPIC_FIXTURE_PATH,
        "schema": "riemann.function_field.genus2_endoscopic_split_locus.v1",
        "payload": "01ccb19f591f48682fa79dbef306880e924282184352cb992e3f66153ceae5c3",
        "file": "10edc162a37403c3c2af1bfa1051dfb07b1b75dbdea181dc673585dde70fd2f4",
    },
    "genus1": {
        "path": GENUS1_FIXTURE_PATH,
        "schema": "riemann.function_field.genus1_cubic_family_laws.v1",
        "payload": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
        "file": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
    },
    "balanced": {
        "path": BALANCED_FIXTURE_PATH,
        "schema": "riemann.function_field.balanced_control_family_scan.v1",
        "payload": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
        "file": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
    },
}

EXPECTED_UPSTREAM_SOURCE_HASHES = {
    "tensor_producer": (
        TENSOR_SOURCE_PATH,
        "878c44730eb62b3e6fb429630b599be0b8fded74da919792dbaa636a51f056ec",
    ),
    "endoscopic_producer": (
        ENDOSCOPIC_SOURCE_PATH,
        "4489c109f25f8e0ca3051dc9983a8738b7aaee941a351959c552aa19b001e4de",
    ),
    "genus1_producer": (
        GENUS1_SOURCE_PATH,
        "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79",
    ),
    "balanced_producer": (
        BALANCED_SOURCE_PATH,
        "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b",
    ),
}


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def _reject_floats(value: object) -> None:
    if isinstance(value, float):
        raise TypeError("floating-point value entered exact bridge fixture")
    if isinstance(value, dict):
        for item in value.values():
            _reject_floats(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _reject_floats(item)


def _load_locked_inputs() -> dict[str, dict[str, object]]:
    output: dict[str, dict[str, object]] = {}
    for name, lock in EXPECTED_FIXTURES.items():
        path = lock["path"]
        if _lf_sha256(path) != lock["file"]:
            raise ValueError(f"{name} fixture file lock changed")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("schema") != lock["schema"]:
            raise ValueError(f"{name} fixture schema changed")
        if payload.get("payload_sha256") != lock["payload"]:
            raise ValueError(f"{name} fixture payload lock changed")
        unhashed = dict(payload)
        claimed = unhashed.pop("payload_sha256")
        if _canonical_sha256(unhashed) != claimed:
            raise ValueError(f"{name} fixture payload is not internally authentic")
        output[name] = payload
    for name, (path, expected_hash) in EXPECTED_UPSTREAM_SOURCE_HASHES.items():
        if _lf_sha256(path) != expected_hash:
            raise ValueError(f"{name} source lock changed")
    _validate_upstream_semantics(output)
    return output


def _validate_upstream_semantics(inputs: Mapping[str, Mapping[str, object]]) -> None:
    tensor = inputs["tensor"]
    pullback = tensor["symbolic_geometry"]["coefficient_map_pullback"]  # type: ignore[index]
    scheme = pullback["scheme_pullback_after_clearing_q"]
    if scheme["R"] != "A^2+b-2*q":
        raise ValueError("tensor R convention changed")
    if scheme["rank_drop_line_ideal"] != "(A*a,R^2)":
        raise ValueError("tensor rank-drop ideal changed")
    if pullback["E_trace_zero_component"]["rank_drop_condition"] != "b=2*q":
        raise ValueError("tensor E-branch condition changed")
    if pullback["C_trace_zero_component"]["rank_drop_condition"] != "A^2+b=2*q":
        raise ValueError("tensor C-branch condition changed")

    endoscopic = inputs["endoscopic"]
    definition = endoscopic["definition_and_exact_identities"]  # type: ignore[index]
    if definition["discriminant"] != "Delta=a^2-4*b+8*q":
        raise ValueError("endoscopic discriminant changed")
    if not str(definition["split_criterion"]).startswith(
        "Delta is a nonnegative square d^2"
    ):
        raise ValueError("endoscopic split criterion changed")

    genus1 = inputs["genus1"]
    if genus1["normalization"]["l_polynomial"] != "L_D(T)=1-a_D*T+q*T^2":  # type: ignore[index]
        raise ValueError("genus-one trace convention changed")
    balanced = inputs["balanced"]
    frozen = balanced["frozen_enumeration_facts"]  # type: ignore[index]
    if frozen["status"] != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("balanced histogram coverage status changed")
    if not str(frozen["coverage"]).startswith("every one of q^5"):
        raise ValueError("balanced histogram is no longer member-complete")


@dataclass(frozen=True)
class SplitClassification:
    kind: str
    delta: int
    square_root_delta: int | None
    traces: tuple[int, int] | None

    @property
    def split(self) -> bool:
        return self.kind in SPLIT_KINDS


def classify_integral_q_split(q: int, a: int, b: int) -> SplitClassification:
    if not all(isinstance(value, int) for value in (q, a, b)):
        raise TypeError("q, a, and b must be integers")
    if q <= 1:
        raise ValueError("q must exceed one")
    delta = a * a - 4 * b + 8 * q
    if delta < 0:
        return SplitClassification(NO_SPLIT, delta, None, None)
    root = isqrt(delta)
    if root * root != delta or (root - a) % 2:
        return SplitClassification(
            NO_SPLIT, delta, root if root * root == delta else None, None
        )
    traces = tuple(sorted(((-a - root) // 2, (-a + root) // 2)))
    return SplitClassification(
        "split_repeated" if delta == 0 else "split_distinct",
        delta,
        root,
        traces,
    )


def multiply_coefficients(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def factorization_residual(q: int, a: int, b: int) -> tuple[int, ...] | None:
    classification = classify_integral_q_split(q, a, b)
    if classification.traces is None:
        return None
    left, right = classification.traces
    actual = multiply_coefficients((1, -left, q), (1, -right, q))
    expected = (1, a, b, q * a, q * q)
    return tuple(value - target for value, target in zip(actual, expected))


def rank_residual(A: int, b: int, q: int) -> int:
    return A * A + b - 2 * q


def transverse_detector_numerator(A: int, a: int, b: int, q: int) -> int:
    if q <= 0:
        raise ValueError("q must be positive")
    residual = rank_residual(A, b, q)
    return residual * residual + (A * a) ** 2


def rank_branch_labels(A: int, a: int, b: int, q: int) -> tuple[str, ...]:
    labels = []
    if A == 0 and b == 2 * q:
        labels.append("E_trace_zero_zero_factor_branch")
    if a == 0 and A * A + b == 2 * q:
        labels.append("C_trace_zero_matching_antidiagonal_branch")
    return tuple(labels)


def reduced_rank_drop(A: int, a: int, b: int, q: int) -> bool:
    return bool(rank_branch_labels(A, a, b, q))


Monomial = tuple[int, ...]


def _divides(first: Monomial, second: Monomial) -> bool:
    return all(left <= right for left, right in zip(first, second))


def _minimal_monomials(generators: Iterable[Monomial]) -> tuple[Monomial, ...]:
    unique = sorted(set(generators))
    return tuple(
        generator
        for generator in unique
        if not any(other != generator and _divides(other, generator) for other in unique)
    )


def _monomial_ideal_intersection(
    first: Iterable[Monomial], second: Iterable[Monomial]
) -> tuple[Monomial, ...]:
    return _minimal_monomials(
        tuple(max(left, right) for left, right in zip(a, b))
        for a in first
        for b in second
    )


def symbolic_bridge_certificate() -> dict[str, object]:
    # Variable order is (A,a,R).  R=A^2+b-2q after the triangular change.
    rank_ideal = _minimal_monomials(((1, 1, 0), (0, 0, 2)))
    e_primary = _minimal_monomials(((1, 0, 0), (0, 0, 2)))
    c_primary = _minimal_monomials(((0, 1, 0), (0, 0, 2)))
    intersection = _monomial_ideal_intersection(e_primary, c_primary)
    if intersection != rank_ideal:
        raise ArithmeticError("rank-branch primary decomposition drifted")

    for q in (3, 5, 7):
        for a in range(-2 * q, 2 * q + 1):
            e_factor = multiply_coefficients((1, 0, q), (1, a, q))
            if e_factor != (1, a, 2 * q, q * a, q * q):
                raise ArithmeticError("E branch factorization drifted")
        for A in range(-2 * q, 2 * q + 1):
            c_factor = multiply_coefficients((1, A, q), (1, -A, q))
            if c_factor != (1, 0, 2 * q - A * A, 0, q * q):
                raise ArithmeticError("C branch factorization drifted")

    return {
        "base_ring": "Q[A,a,R] for scheme statements; q is fixed and invertible",
        "parameters": {
            "R": "A^2+b-2*q",
            "Delta_after_b_substitution": "a^2+4*A^2-4*R",
            "detector_identity": "q^2*L=R^2+(A*a)^2",
        },
        "singular_plane_pullback": {
            "ideal": "I_sing=(A*a)=(A) intersect (a)",
            "scheme_status": "reduced union of the two trace-zero components",
        },
        "rank_line_pullback": {
            "ideal": "I_rank=(A*a,R^2)",
            "primary_decomposition": (
                "(A,R^2) intersect (a,R^2); each branch is doubled in R"
            ),
            "computed_monomial_generators_A_a_R": {
                "I_rank": [list(item) for item in rank_ideal],
                "E_primary": [list(item) for item in e_primary],
                "C_primary": [list(item) for item in c_primary],
                "intersection": [list(item) for item in intersection],
            },
            "radical": (
                "rad(I_rank)=(A*a,R)=(A,R) intersect (a,R), with no asserted "
                "containment of the nilpotent thickening in an arithmetic split scheme"
            ),
        },
        "reduced_branch_containment": {
            "E_branch": {
                "conditions": "A=0,b=2*q",
                "factorization": "(1+q*T^2)*(1+a*T+q*T^2)",
                "integral_factor_traces": "(0,-a)",
                "Delta": "a^2",
            },
            "C_branch": {
                "conditions": "a=0,b=2*q-A^2",
                "factorization": "(1+A*T+q*T^2)*(1-A*T+q*T^2)",
                "integral_factor_traces": "(-A,A)",
                "Delta": "4*A^2",
            },
            "combined_square_on_reduction": (
                "Delta=(a+2*A)^2=(a-2*A)^2 modulo (A*a,R)"
            ),
            "nonreduced_warning": (
                "Delta-(a+2*A)^2=-4*(R+A*a); R survives nilpotently modulo "
                "(A*a,R^2), so containment is a reduced-support statement"
            ),
        },
        "exact_converse": {
            "on_E_trace_zero_component": (
                "for split traces (r,s), rank drop iff b=2*q iff r*s=0"
            ),
            "on_C_trace_zero_component": (
                "split implies (r,s)=(-r,r); rank drop iff r^2=A^2, equivalently "
                "the factor traces are (-A,A) as an unordered pair"
            ),
            "outside_singular_preimage": "A*a!=0 implies no tensor rank drop",
            "repeated_rank_drop": "occurs exactly at A=a=0,b=2*q",
        },
        "real_integer_detector_scope": (
            "on real or integer product parameters, L=0 alone forces R=A*a=0 by "
            "the sum of squares; over complex points L=0 alone has extra cancellation"
        ),
    }


@dataclass
class WorkGuard:
    counts: Counter[str] = field(default_factory=Counter)

    def charge(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("work charge must be nonnegative")
        if sum(self.counts.values()) + amount >= HISTOGRAM_WORK_CAP_EXCLUSIVE:
            raise RuntimeError("strict bridge histogram-work cap would be reached")
        self.counts[name] += amount

    def snapshot(self) -> dict[str, int]:
        result = {name: self.counts[name] for name in sorted(self.counts)}
        result["total"] = sum(self.counts.values())
        return result


def _rows_by_q(rows: Iterable[Mapping[str, object]]) -> dict[int, Mapping[str, object]]:
    output = {int(row["q"]): row for row in rows}
    if not set(FROZEN_Q_VALUES) <= set(output):
        raise ValueError("locked source is missing q=3,5,7")
    return output


def _detector_failures_from_endoscopic(row: Mapping[str, object]) -> dict[str, object]:
    correlations = row["detector_correlations"]
    output = {}
    for label, key in (
        ("B", "B"),
        ("F", "F"),
        ("complete_balanced_echo", "complete_frobenius_echo"),
    ):
        fiber = correlations[key]["fiber_purity"]
        output[label] = {
            "fiber_count": fiber["fiber_count"],
            "mixed_split_status_fiber_count": fiber[
                "mixed_factorization_fiber_count"
            ],
            "genus2_member_count_in_mixed_fibers": fiber[
                "member_count_in_mixed_fibers"
            ],
        }
    return output


def analyze_frozen_family(
    q: int,
    genus1_row: Mapping[str, object],
    balanced_row: Mapping[str, object],
    tensor_row: Mapping[str, object],
    endoscopic_row: Mapping[str, object],
    guard: WorkGuard,
) -> dict[str, object]:
    elliptic_histogram = {
        int(trace): int(count)
        for trace, count in genus1_row["model_trace_histogram"].items()
    }
    genus2_atoms = balanced_row["joint_a_D_b_D_law"]["atoms"]
    split_source_rows = {
        (int(atom["a_D"]), int(atom["b_D"])): atom
        for atom in endoscopic_row["factorization_classification"][
            "split_signed_coefficient_atoms"
        ]
    }

    counts: Counter[str] = Counter()
    atom_counts: Counter[str] = Counter()
    rank_rows = []
    ledger = []
    for source_trace in sorted(elliptic_histogram):
        A = -source_trace
        elliptic_count = elliptic_histogram[source_trace]
        for atom in genus2_atoms:
            guard.charge("product_histogram_atom_pair")
            a = int(atom["a_D"])
            b = int(atom["b_D"])
            genus2_count = int(atom["member_count"])
            weight = elliptic_count * genus2_count
            classification = classify_integral_q_split(q, a, b)
            split = classification.split
            singular = A == 0 or a == 0
            residual = rank_residual(A, b, q)
            detector = transverse_detector_numerator(A, a, b, q)
            rank = reduced_rank_drop(A, a, b, q)
            if rank != (detector == 0):
                raise ArithmeticError("integer L=0 and reduced rank branches disagree")
            if rank and not split:
                raise ArithmeticError("rank-drop branch escaped integral +q split locus")
            if split and factorization_residual(q, a, b) != (0, 0, 0, 0, 0):
                raise ArithmeticError("split factorization residual is nonzero")
            if split != ((a, b) in split_source_rows):
                raise ArithmeticError("independent split classification disagrees with source")
            if split and int(split_source_rows[(a, b)]["member_count"]) != genus2_count:
                raise ArithmeticError("split source member count drifted")

            e_component = A == 0
            c_component = a == 0
            e_rank = A == 0 and b == 2 * q
            c_rank = a == 0 and residual == 0
            overlap = e_rank and c_rank
            repeated = classification.kind == "split_repeated"

            predicates = {
                "all_product_pairs": True,
                "integral_split": split,
                "split_repeated": repeated,
                "split_distinct": split and not repeated,
                "tensor_singular": singular,
                "rank_drop": rank,
                "split_and_tensor_singular": split and singular,
                "split_singular_not_rank": split and singular and not rank,
                "split_outside_tensor_singular": split and not singular,
                "split_and_L_positive": split and detector > 0,
                "non_split_and_L_zero": not split and detector == 0,
                "E_component": e_component,
                "E_component_split": e_component and split,
                "E_component_rank": e_rank,
                "E_component_split_not_rank": e_component and split and not e_rank,
                "C_component": c_component,
                "C_component_split": c_component and split,
                "C_component_rank": c_rank,
                "C_component_split_not_rank": c_component and split and not c_rank,
                "rank_branch_intersection": overlap,
                "rank_split_repeated": rank and repeated,
                "rank_split_distinct": rank and split and not repeated,
            }
            for name, enabled in predicates.items():
                if enabled:
                    counts[name] += weight
                    atom_counts[name] += 1

            labels = rank_branch_labels(A, a, b, q)
            if rank:
                if not labels:
                    raise ArithmeticError("rank row has no branch label")
                rank_rows.append(
                    {
                        "source_geometric_trace_t_E": source_trace,
                        "tensor_polynomial_coefficient_A": A,
                        "genus2_a": a,
                        "genus2_b": b,
                        "elliptic_histogram_count": elliptic_count,
                        "genus2_histogram_count": genus2_count,
                        "product_pair_count": weight,
                        "branches": list(labels),
                        "split_kind": classification.kind,
                        "integral_factor_traces_sorted": list(
                            classification.traces or ()
                        ),
                        "Delta": classification.delta,
                        "R": residual,
                        "q_squared_L_numerator": detector,
                    }
                )

            ledger.append(
                {
                    "A": A,
                    "a": a,
                    "b": b,
                    "weight": weight,
                    "split_kind": classification.kind,
                    "singular": singular,
                    "rank": rank,
                    "R": residual,
                    "L_num": detector,
                }
            )

    all_pairs = counts["all_product_pairs"]
    split_pairs = counts["integral_split"]
    rank_pairs = counts["rank_drop"]
    singular_pairs = counts["tensor_singular"]
    split_singular = counts["split_and_tensor_singular"]

    tensor_expected = tensor_row["trace_zero_partition_counts"]
    if all_pairs != int(tensor_row["product_model_pair_count"]):
        raise ArithmeticError("all product-pair count disagrees with tensor packet")
    if singular_pairs != int(tensor_expected["singular_trace_zero_total"]):
        raise ArithmeticError("singular count disagrees with tensor packet")
    if rank_pairs != int(tensor_expected["transverse_degenerate_union"]):
        raise ArithmeticError("rank count disagrees with tensor packet")
    components = tensor_row["component_incidence_census"]
    component_expectations = {
        "E_component": "E_trace_zero_component",
        "C_component": "C_trace_zero_component",
        "E_component_rank": "E_component_rank_drop",
        "C_component_rank": "C_component_rank_drop",
        "rank_branch_intersection": "rank_drop_intersection",
    }
    for observed, source_name in component_expectations.items():
        if counts[observed] != int(components[source_name]["pair_count"]):
            raise ArithmeticError(f"{observed} disagrees with tensor source")

    endoscopic_expected = endoscopic_row["factorization_classification"]
    genus2_split_members = int(endoscopic_expected["integral_split_locus"]["member_count"])
    if split_pairs != sum(elliptic_histogram.values()) * genus2_split_members:
        raise ArithmeticError("product split count disagrees with endoscopic source")

    incidence_counts = {
        name: {
            "product_pair_count": counts[name],
            "source_histogram_atom_pair_count": atom_counts[name],
        }
        for name in (
            "all_product_pairs",
            "integral_split",
            "split_repeated",
            "split_distinct",
            "tensor_singular",
            "rank_drop",
            "split_and_tensor_singular",
            "split_singular_not_rank",
            "split_outside_tensor_singular",
            "rank_split_repeated",
            "rank_split_distinct",
        )
    }

    return {
        "q": q,
        "source_histogram_sizes": {
            "elliptic_trace_atoms": len(elliptic_histogram),
            "genus2_coefficient_atoms": len(genus2_atoms),
            "product_atom_pairs": len(elliptic_histogram) * len(genus2_atoms),
        },
        "incidence_counts": incidence_counts,
        "incidence_fractions": {
            "rank_drop_of_all_product_pairs": _fraction(Fraction(rank_pairs, all_pairs)),
            "rank_drop_of_integral_split_pairs": _fraction(
                Fraction(rank_pairs, split_pairs)
            ),
            "split_singular_of_tensor_singular": _fraction(
                Fraction(split_singular, singular_pairs)
            ),
            "rank_drop_of_split_singular": _fraction(
                Fraction(rank_pairs, split_singular)
            ),
            "rank_drop_of_tensor_singular": _fraction(
                Fraction(rank_pairs, singular_pairs)
            ),
        },
        "inclusive_branch_converse_census": {
            "E_trace_zero_component": {
                "all_component_pairs": counts["E_component"],
                "integral_split_pairs": counts["E_component_split"],
                "rank_pairs_zero_factor": counts["E_component_rank"],
                "split_but_nonzero_factor_pairs": counts[
                    "E_component_split_not_rank"
                ],
            },
            "C_trace_zero_component": {
                "all_component_pairs": counts["C_component"],
                "integral_split_pairs": counts["C_component_split"],
                "rank_pairs_trace_match": counts["C_component_rank"],
                "split_but_trace_mismatch_pairs": counts[
                    "C_component_split_not_rank"
                ],
            },
            "rank_branch_intersection_pairs": counts["rank_branch_intersection"],
            "warning": "the two component rows are inclusive and share their intersection",
        },
        "detector_recognition": {
            "L_zero_contingency": {
                "split_and_L_zero": rank_pairs,
                "split_and_L_positive": counts["split_and_L_positive"],
                "non_split_and_L_zero": counts["non_split_and_L_zero"],
                "non_split_and_L_positive": all_pairs - split_pairs,
            },
            "rank_as_split_detector": {
                "precision_P_split_given_L_zero": [1, 1],
                "recall_P_L_zero_given_split": _fraction(
                    Fraction(rank_pairs, split_pairs)
                ),
                "interpretation": (
                    "L=0 recognizes exactly the rank-drop sublocus on integer product "
                    "parameters, not the whole integral split locus"
                ),
            },
            "locked_genus2_detector_failures": _detector_failures_from_endoscopic(
                endoscopic_row
            ),
        },
        "rank_drop_product_atoms": sorted(
            rank_rows, key=lambda row: (row["tensor_polynomial_coefficient_A"], row["genus2_a"], row["genus2_b"])
        ),
        "complete_product_atom_classification_ledger_sha256": _canonical_sha256(
            ledger
        ),
        "exact_cross_checks": {
            "rank_rows_all_integral_split": True,
            "factorization_residuals_zero": True,
            "integer_L_zero_equals_reduced_rank_union": True,
            "tensor_counts_replayed": True,
            "endoscopic_counts_replayed": True,
        },
    }


def _file_lock(path: Path, payload_sha256: str | None = None) -> dict[str, object]:
    result: dict[str, object] = {
        "path": _relative(path),
        "sha256_lf_normalized": _lf_sha256(path),
    }
    if payload_sha256 is not None:
        result["payload_sha256"] = payload_sha256
    return result


def build_fixture(q_values: tuple[int, ...] = FROZEN_Q_VALUES) -> dict[str, object]:
    if q_values != FROZEN_Q_VALUES:
        raise ValueError("bridge replay requires exactly q=(3,5,7)")
    inputs = _load_locked_inputs()
    genus1_rows = _rows_by_q(inputs["genus1"]["finite_regressions"])
    balanced_rows = _rows_by_q(
        inputs["balanced"]["frozen_enumeration_facts"]["families"]
    )
    tensor_rows = _rows_by_q(inputs["tensor"]["frozen_histogram_census"])
    endoscopic_rows = _rows_by_q(
        inputs["endoscopic"]["frozen_histogram_results"]["families"]
    )
    guard = WorkGuard()
    families = [
        analyze_frozen_family(
            q,
            genus1_rows[q],
            balanced_rows[q],
            tensor_rows[q],
            endoscopic_rows[q],
            guard,
        )
        for q in q_values
    ]

    source_locks = {
        name + "_fixture": _file_lock(lock["path"], lock["payload"])
        for name, lock in EXPECTED_FIXTURES.items()
    }
    source_locks.update(
        {
            name: _file_lock(path)
            for name, (path, _) in EXPECTED_UPSTREAM_SOURCE_HASHES.items()
        }
    )
    source_locks.update(
        {
            "producer": _file_lock(Path(__file__).resolve()),
            "note": _file_lock(NOTE_PATH),
            "test": _file_lock(TEST_PATH),
        }
    )

    payload: dict[str, object] = {
        "schema": "riemann.function_field.tensor_endoscopic_rank_drop_bridge.v1",
        "raw_fixture_id": "FUNCTION_FIELD.TENSOR.ENDOSCOPIC.RANK_DROP.BRIDGE.Q3_Q5_Q7.V1",
        "status": "EXACT_REDUCED_CONTAINMENT_SCHEME_MULTIPLICITY_AND_LOCKED_INCIDENCE",
        "rigor_level": "PROVED_ALGEBRA_PLUS_COMPLETE_SOURCE_HISTOGRAM_TRANSFORM",
        "scope": (
            "the pullback of the product-tensor coefficient-hypersurface rank-drop "
            "line and its relation to integral +q quadratic factorization of the "
            "genus-two Frobenius polynomial"
        ),
        "symbolic_bridge": symbolic_bridge_certificate(),
        "frozen_product_model_incidence": families,
        "producer_and_source_locks": {
            "input_method": (
                "source-locked JSON histogram convolution and sparse monomial algebra"
            ),
            "locks": source_locks,
        },
        "resource_contract": {
            "strict_histogram_work_cap_exclusive": HISTOGRAM_WORK_CAP_EXCLUSIVE,
            "guarded_work_units": guard.snapshot(),
            "strict_cap_satisfied": (
                guard.snapshot()["total"] < HISTOGRAM_WORK_CAP_EXCLUSIVE
            ),
            "field_curve_variety_or_member_enumerations": 0,
            "random_samples": 0,
            "floating_point_values": 0,
            "arithmetic": "integers, fractions, and sparse monomial ideals only",
        },
        "scope_firewall": {
            "reduced_support_not_nonreduced_scheme_containment": (
                "The integral +q split locus is an arithmetic square/parity predicate. "
                "Only the reduced integer rank-drop support is contained; the R^2 "
                "nilpotent thickening is not asserted to lie in an endoscopic scheme."
            ),
            "coefficient_geometry_not_variety_singularity": (
                "Rank drop concerns the transverse cone of an ambient coefficient "
                "hypersurface; it does not make E, C, E x C, or a Jacobian singular."
            ),
            "formal_factorization_not_isogeny_or_polarization": (
                "The displayed polynomial factorizations do not import Honda-Tate/Tate, "
                "prove a product isogeny, identify a principal polarization, split a "
                "genus-two curve, or exhibit elliptic quotient maps."
            ),
            "endoscopic_is_operational_label": (
                "Endoscopic means only integral factorization into two constant-+q "
                "elliptic-form quadratics in this packet."
            ),
            "real_integer_sum_of_squares_scope": (
                "L=0 alone recognizes rank drop on real/integer product parameters; "
                "over complex parameters the sum of squares can cancel."
            ),
            "product_model_measure_only": (
                "The q=3,5,7 weights are the ordered product of two locked uniform-model "
                "histograms, not a coarse moduli or product-variety measure."
            ),
            "no_causal_or_global_claim": (
                "The incidence tables imply no extra endomorphisms, monodromy component, "
                "all-q frequency, equidistribution, number-field transfer, RH, or GRH."
            ),
        },
    }
    _reject_floats(payload)
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    mode.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    args = parser.parse_args(argv)
    fixture = build_fixture()
    encoded = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    if args.write is not None:
        args.write.write_text(encoded, encoding="utf-8")
        print(f"wrote {args.write}")
    elif args.check is not None:
        if args.check.read_text(encoding="utf-8") != encoded:
            raise SystemExit(f"stale fixture: {args.check}")
        print(f"fixture current: {args.check}")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
