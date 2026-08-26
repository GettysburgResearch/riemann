#!/usr/bin/env python3
"""Bounded reconciliation of the marked genus-two chi_(0,3) trace.

This producer does not enumerate a finite field.  It source-locks the exact
marked-stack adapter, the all-q B3 character-sum theorem, and the high-weight
controls; imports one explicitly located published unmarked trace theorem; and
derives the mixed ramification-trace identity as an exact consequence.

The primary-literature text is a manually audited dependency.  Its URLs,
locators, and downloaded artifact hashes are recorded, but the producer does
not access the network or claim to machine-authenticate those documents.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_chi03_stack_trace_reconciliation.json"
NOTE_PATH = HERE.parent / "GENUS2_CHI03_STACK_TRACE_RECONCILIATION.md"
TEST_PATH = ROOT / "tests" / "test_genus2_chi03_stack_trace_reconciliation.py"

HIGH_WEIGHT_PATH = HERE / "genus2_high_weight_channel_probe.json"
MARKED_ADAPTER_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
B3_THEOREM_PATH = HERE / "genus2_b3_primitive_trace_average.json"

MAX_SOURCE_BYTES_EACH = 150_000
MAX_EXACT_OPERATIONS = 1_024
FROZEN_Q_VALUES = (3, 5, 7)

SOURCE_LOCKS: dict[str, dict[str, str]] = {
    "genus2_high_weight_channel_probe.json": {
        "lf_sha256": "bfa4aaca81a755ee9d02d2ae3741b0c511f91899a75adf85ada00007612f9541",
        "payload_sha256": "90820eded366af5c430df6712bb51f6ad7882faf7bd27c4665c411052c1dca0e",
        "schema": "riemann.function_field.genus2_high_weight_channel_probe.v1",
    },
    "genus2_marked_weierstrass_stack_adapter.json": {
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
    },
    "genus2_b3_primitive_trace_average.json": {
        "lf_sha256": "5ecc6006014a159a4030218977c89f58c63334461a568b7a67d36130bae1c50b",
        "payload_sha256": "e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd",
        "schema": "riemann.function_field.genus2_b3_primitive_trace_average.v1",
    },
}

LITERATURE_ARTIFACTS: tuple[dict[str, object], ...] = (
    {
        "key": "bergstrom_pointed_hyperelliptic",
        "authors": "Jonas Bergstrom",
        "title": (
            "Equivariant counts of points of the moduli spaces of pointed "
            "hyperelliptic curves"
        ),
        "url": "https://arxiv.org/abs/math/0611813",
        "version": "arXiv v2, 30 November 2011",
        "pdf_sha256": (
            "12457527533aa0898375b5085c29cd0dec88e77ef4612a8810baac01ba92d5cd"
        ),
        "eprint_source_sha256": (
            "7a8c0cf50edb6de61694412e5b70e46f279587655582804d2011228a0f09973d"
        ),
        "locators": [
            "Section 7 opening and Section 7.3 (arXiv PDF pp. 16-17)",
            "Section 11.1 and Theorem 11.6 (arXiv PDF pp. 26 and 29)",
            "Definition 12.1 (arXiv PDF p. 29)",
            "Lemma 12.8 and Remark 12.9 (arXiv PDF pp. 30-31)",
        ],
        "claim_boundary": (
            "proves the unmarked V_(3,3) trace and supplies mixed "
            "ramification coordinates, but does not print or evaluate the "
            "marked V_(3,3) trace"
        ),
    },
    {
        "key": "bergstrom_faber_vandergeer_level_two",
        "authors": "Jonas Bergstrom, Carel Faber, Gerard van der Geer",
        "title": (
            "Siegel modular forms of genus 2 and level 2: cohomological "
            "computations and conjectures"
        ),
        "url": "https://arxiv.org/abs/0803.0917",
        "version": "arXiv:0803.0917",
        "pdf_sha256": (
            "f6294c69e2cafe16b4b0dc1ba1692a46813ba6e467e546aa548442d1a4f2a19e"
        ),
        "eprint_source_sha256": (
            "5780b581522ec17d4dfacc202b277f92e9b464fc54ef5f60dcc8ef56b660e5f0"
        ),
        "locators": [
            "Section 2, definition of M_2(w^n) (arXiv PDF p. 2)",
            "Equation (5.1) and Section 5.3 (arXiv PDF pp. 7-8)",
            "Section 9 A_2(w^1) dimension checks (arXiv PDF p. 12)",
            "Section 10 example table (arXiv PDF p. 12)",
        ],
        "claim_boundary": (
            "right marked-Weierstrass geometry and exact finite point-count "
            "formula, but bounded fields and conjectural non-Eisenstein "
            "identification; no printed all-q M_2(w^1), V_(3,3) theorem"
        ),
    },
    {
        "key": "bergstrom_2025_author_erratum",
        "authors": "Jonas Bergstrom",
        "title": "Erratum",
        "url": (
            "https://www.su.se/download/18.1f09f4df19a7bbe0dfd6a83e/"
            "1764771423396/Erratum.pdf"
        ),
        "version": "2 December 2025",
        "pdf_sha256": (
            "b064eef272d63a2a9b604647d25a346b825f48cba430399c14b144d477af16a3"
        ),
        "locators": [
            "p. 1: corrected A_2[2], V_(3,3) example row",
            "p. 2: corrected Example 7.10 in the pointed-hyperelliptic paper",
        ],
        "claim_boundary": (
            "the corrected level-two example row gains a constant -15; "
            "Theorem 11.6 of the pointed-hyperelliptic paper is not listed "
            "as altered"
        ),
    },
)


@dataclass
class OperationGuard:
    limit: int = MAX_EXACT_OPERATIONS
    used: int = 0

    def consume(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        self.used += amount
        if self.used > self.limit:
            raise RuntimeError(
                f"exact operation cap exceeded: {self.used}>{self.limit}"
            )


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, tuple):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        _normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _sha256_lf(path: Path) -> str:
    return hashlib.sha256(_lf_bytes(path.read_bytes())).hexdigest()


def _load_locked_json(path: Path, lock: Mapping[str, str]) -> dict[str, object]:
    raw = path.read_bytes()
    if not 0 < len(raw) <= MAX_SOURCE_BYTES_EACH:
        raise ValueError(f"{path.name} exceeds the declared source byte cap")
    actual_lf = hashlib.sha256(_lf_bytes(raw)).hexdigest()
    if actual_lf != lock["lf_sha256"]:
        raise ArithmeticError(f"LF source hash mismatch for {path.name}")
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"{path.name} is not a JSON object")
    if value.get("schema") != lock["schema"]:
        raise ArithmeticError(f"schema mismatch for {path.name}")
    claimed = value.get("payload_sha256")
    if "payload_sha256" in lock and claimed != lock["payload_sha256"]:
        raise ArithmeticError(f"pinned payload mismatch for {path.name}")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload):
        raise ArithmeticError(f"internal payload mismatch for {path.name}")
    return value


def _poly_add(
    left: Sequence[int], right: Sequence[int], guard: OperationGuard
) -> tuple[int, ...]:
    result: list[int] = []
    for index in range(max(len(left), len(right))):
        guard.consume()
        result.append(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def _poly_scale(
    value: Sequence[int], scalar: int, guard: OperationGuard
) -> tuple[int, ...]:
    guard.consume(len(value))
    result = [scalar * coefficient for coefficient in value]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def _poly_multiply(
    left: Sequence[int], right: Sequence[int], guard: OperationGuard
) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            guard.consume()
            result[left_index + right_index] += left_value * right_value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def _poly_evaluate(value: Sequence[int], q: int, guard: OperationGuard) -> int:
    result = 0
    for coefficient in reversed(value):
        guard.consume()
        result = q * result + coefficient
    return result


def unmarked_trace(q: int) -> int:
    if q <= 0:
        raise ValueError("q must be positive")
    return -q - 1


def candidate_marked_trace(q: int) -> int:
    if q <= 0:
        raise ValueError("q must be positive")
    return q**4 - 2 * q - 1


def mixed_trace_required_by_candidate(q: int) -> int:
    if q <= 0:
        raise ValueError("q must be positive")
    return (q + 1) * unmarked_trace(q) - candidate_marked_trace(q)


def marked_trace_from_mixed(q: int, mixed_trace: int) -> int:
    if q <= 0:
        raise ValueError("q must be positive")
    return (q + 1) * unmarked_trace(q) - mixed_trace


def _integer_polynomial_from_pairs(value: object, label: str) -> tuple[int, ...]:
    if not isinstance(value, list) or not value:
        raise TypeError(f"{label} is not a nonempty coefficient list")
    coefficients: list[int] = []
    for pair in value:
        if not isinstance(pair, list) or len(pair) != 2:
            raise TypeError(f"{label} contains a malformed rational pair")
        numerator, denominator = int(pair[0]), int(pair[1])
        if denominator != 1:
            raise ArithmeticError(f"{label} is not integral")
        coefficients.append(numerator)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def _verify_adapter(marked: Mapping[str, object]) -> dict[str, object]:
    theorem = marked.get("trace_theorem")
    if not isinstance(theorem, dict):
        raise TypeError("marked adapter lost trace_theorem")
    channels = theorem.get("even_channels_closed_by_adapter")
    if not isinstance(channels, dict):
        raise TypeError("marked adapter lost its even channel dictionary")
    channel = channels.get("chi_(0,3)")
    if not isinstance(channel, dict):
        raise TypeError("marked adapter lost chi_(0,3)")
    if tuple(channel.get("fundamental_weight", ())) != (0, 3):
        raise ArithmeticError("chi_(0,3) fundamental weight drifted")
    if tuple(channel.get("highest_weight_e_basis", ())) != (3, 3):
        raise ArithmeticError("chi_(0,3)/V_(3,3) alias drifted")
    if channel.get("local_system_weight") != 6:
        raise ArithmeticError("chi_(0,3) local-system weight drifted")
    if channel.get("candidate_value_status") != "NOT_PROVED_BY_THIS_PACKET":
        raise ArithmeticError("marked adapter silently promoted the candidate")
    return {
        "project_character": "chi_(0,3)",
        "literature_local_system": "V_(3,3)",
        "fundamental_weight": [0, 3],
        "highest_weight_e_basis": [3, 3],
        "local_system_weight": 6,
        "exact_model_trace_formula": channel["exact_stack_trace_formula"],
        "status": "PROVED_BY_MARKED_STACK_ADAPTER",
    }


def _verify_b3_theorem(
    b3: Mapping[str, object], guard: OperationGuard
) -> dict[str, object]:
    if b3.get("status") != "PROVED_EXACT_ALL_ODD_PRIME_POWERS":
        raise ArithmeticError("B3 packet no longer proves the all-q theorem")
    theorem = b3.get("theorem")
    if not isinstance(theorem, dict):
        raise TypeError("B3 packet lost its theorem dictionary")
    expected_strings = {
        "b3_total": ("sum_D b_D^3=q*(q-1)*(4*q^6-9*q^5+7*q^4+8*q^3-12*q^2-9*q-1)"),
        "chi_(0,3)_mean": "(q^4-2*q-1)/q^6",
        "marked_stack_trace": "T_(0,3)(q)=q^4-2*q-1",
    }
    for key, expected in expected_strings.items():
        if theorem.get(key) != expected:
            raise ArithmeticError(f"B3 theorem field {key} drifted")

    b3_total = _integer_polynomial_from_pairs(
        b3.get("b3_total_low_to_high"), "B3 total"
    )
    cleared_chi = _integer_polynomial_from_pairs(
        b3.get("cleared_chi_sum_low_to_high"), "cleared chi_(0,3) sum"
    )
    q_q_minus_one = (0, -1, 1)
    b3_inner = (-1, -9, -12, 8, 7, -9, 4)
    candidate_trace = (-1, -2, 0, 0, 1)
    if b3_total != _poly_multiply(q_q_minus_one, b3_inner, guard):
        raise ArithmeticError("B3 total lost its exact factorization")
    if cleared_chi != _poly_multiply(q_q_minus_one, candidate_trace, guard):
        raise ArithmeticError("B3 lower-moment bridge lost the chi_(0,3) theorem")

    signature_audit = b3.get("ordered_triple_signature_audit")
    if not isinstance(signature_audit, dict):
        raise TypeError("B3 packet lost its signature audit")
    if signature_audit.get("signature_count") != 23:
        raise ArithmeticError("B3 signature census drifted")
    if signature_audit.get("weighted_type_count") != "q^6":
        raise ArithmeticError("B3 signatures no longer exhaust q^6 triples")
    if signature_audit.get("status") != "EXACT_EXHAUSTIVE_23_SIGNATURE_PARTITION":
        raise ArithmeticError("B3 signature audit is no longer exact")

    return {
        "status": "PROVED_EXACT_ALL_ODD_PRIME_POWERS",
        "source_packet": "GENUS2_B3_PRIMITIVE_TRACE_AVERAGE",
        "b3_total": theorem["b3_total"],
        "chi_(0,3)_mean": theorem["chi_(0,3)_mean"],
        "marked_stack_trace": theorem["marked_stack_trace"],
        "signature_count": 23,
        "signature_partition": "q^6",
        "independent_audit": (
            "PASSED: Weyl character, sign inventories, seven primitive types, "
            "Möbius sieve, all 23 rows, factorization, and q=3,5,7 controls"
        ),
    }


def _finite_controls(
    high_weight: Mapping[str, object], guard: OperationGuard
) -> list[dict[str, object]]:
    rows = high_weight.get("finite_aggregate_controls")
    if not isinstance(rows, list):
        raise TypeError("high-weight packet lost finite controls")
    by_q = {int(row["q"]): row for row in rows}
    if tuple(sorted(by_q)) != FROZEN_Q_VALUES:
        raise ArithmeticError("high-weight controls lost q=3,5,7 coverage")
    result: list[dict[str, object]] = []
    for q in FROZEN_Q_VALUES:
        row = by_q[q]
        channel_means = row.get("channel_means")
        if not isinstance(channel_means, dict):
            raise TypeError(f"q={q} lost channel means")
        pair = channel_means.get("chi_(0,3)")
        if not isinstance(pair, list) or len(pair) != 2:
            raise TypeError(f"q={q} chi_(0,3) mean is malformed")
        mean = Fraction(int(pair[0]), int(pair[1]))
        guard.consume(4)
        marked = mean * q**6
        if marked.denominator != 1:
            raise ArithmeticError(f"q={q} marked stack trace is not integral")
        marked_value = marked.numerator
        expected_marked = candidate_marked_trace(q)
        if marked_value != expected_marked:
            raise ArithmeticError(f"q={q} marked control lost candidate agreement")
        mixed = (q + 1) * unmarked_trace(q) - marked_value
        if mixed != -(q**4) - q**2:
            raise ArithmeticError(f"q={q} mixed trace bridge failed")
        result.append(
            {
                "q": q,
                "source_mean_chi_(0,3)": [mean.numerator, mean.denominator],
                "marked_stack_trace": marked_value,
                "implied_mixed_ramification_trace": mixed,
                "status": "EXACT_FINITE_CONTROL_NOT_USED_AS_ALL_Q_PROOF",
            }
        )
    return result


def build_certificate() -> dict[str, object]:
    guard = OperationGuard()
    high_weight = _load_locked_json(
        HIGH_WEIGHT_PATH, SOURCE_LOCKS[HIGH_WEIGHT_PATH.name]
    )
    marked = _load_locked_json(
        MARKED_ADAPTER_PATH, SOURCE_LOCKS[MARKED_ADAPTER_PATH.name]
    )
    b3 = _load_locked_json(B3_THEOREM_PATH, SOURCE_LOCKS[B3_THEOREM_PATH.name])
    alias = _verify_adapter(marked)
    branch_theorem = _verify_b3_theorem(b3, guard)
    finite_controls = _finite_controls(high_weight, guard)

    # Polynomial coefficient order is increasing in q.
    q_plus_one = (1, 1)
    unmarked = (-1, -1)
    candidate = (-1, -2, 0, 0, 1)
    mixed = _poly_add(
        _poly_multiply(q_plus_one, unmarked, guard),
        _poly_scale(candidate, -1, guard),
        guard,
    )
    expected_mixed = (0, 0, -1, 0, -1)
    if mixed != expected_mixed:
        raise ArithmeticError("marked/unmarked polynomial reduction failed")
    for q in FROZEN_Q_VALUES:
        if _poly_evaluate(mixed, q, guard) != mixed_trace_required_by_candidate(q):
            raise ArithmeticError("mixed polynomial specialization failed")
        if marked_trace_from_mixed(q, -(q**4) - q**2) != candidate_marked_trace(q):
            raise ArithmeticError("candidate equivalence failed")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_chi03_stack_trace_reconciliation.v1",
        "status": (
            "PROVED_ON_BRANCH_EXACT_B3_AND_MARKED_STACK_TRACE_"
            "PUBLISHED_TABLE_IMPORT_NOT_FOUND"
        ),
        "scope": {
            "base_fields": "all finite fields F_q of odd characteristic",
            "marked_moduli_problem": "M_2(w^1), one rational Weierstrass point",
            "unmarked_moduli_problem": "M_2",
            "arbitrary_point_moduli_problem": (
                "M_(2,1), explicitly distinguished from M_2(w^1)"
            ),
            "finite_field_or_curve_enumeration": False,
            "external_database_query": False,
            "rh_or_grh_claim": False,
        },
        "character_alias": alias,
        "branch_local_theorem": branch_theorem,
        "established_import": {
            "status": "IMPORTED_PRIMARY_LITERATURE_THEOREM_NOT_REPROVED_HERE",
            "formula": "U_33(q)=-q-1",
            "definition": ("U_33(q)=sum_[C in M_2(F_q)] Tr(F_q|V_(3,3),C)/|Aut_q(C)|"),
            "source": (
                "Bergstrom, Section 11.1 finite-field Frobenius bridge and "
                "Theorem 11.6, e_c(M_2,V_(3,3))=-L-1"
            ),
            "characteristic": "odd",
            "erratum_boundary": (
                "the 2025 author erratum corrects Example 7.10 but does not "
                "list Theorem 11.6 as altered"
            ),
        },
        "forgetful_fibre_identity": {
            "r_1_definition": (
                "Bergstrom r_1(C) counts rational base points with unramified "
                "hyperelliptic fibre"
            ),
            "rational_Weierstrass_count": "R_1(C)=q+1-r_1(C)",
            "mixed_trace_definition": (
                "M_33(q)=sum_[C in M_2(F_q)] r_1(C)*Tr(F_q|V_(3,3),C)/|Aut_q(C)|"
            ),
            "exact_identity": "T_(0,3)(q)=(q+1)*U_33(q)-M_33(q)",
            "after_unmarked_import": "T_(0,3)(q)=-(q+1)^2-M_33(q)",
            "proof": (
                "groupoid cardinality of the forgetful fibre "
                "M_2(w^1)->M_2; automorphism weights are retained"
            ),
            "status": "PROVED_EXACTLY",
        },
        "mixed_trace_consequence": {
            "name": "CHI03-MIXED-RAMIFICATION-TRACE",
            "target": "M_33(q)=-q^4-q^2",
            "proved_marked_trace": "T_(0,3)(q)=q^4-2*q-1",
            "exact_equivalence": ("T_(0,3)(q)=q^4-2*q-1 iff M_33(q)=-q^4-q^2"),
            "coefficient_vectors_in_increasing_q_power": {
                "unmarked_U_33": list(unmarked),
                "candidate_marked_T_(0,3)": list(candidate),
                "required_mixed_M_33": list(mixed),
            },
            "proof": (
                "the B3 packet proves T_(0,3); the exact forgetful-fibre "
                "identity and U_33=-q-1 then prove M_33=-q^4-q^2"
            ),
            "status": "PROVED_ON_BRANCH_AS_EXACT_CONSEQUENCE",
        },
        "finite_controls": finite_controls,
        "literature_verdict": {
            "published_table_import": "NOT_FOUND_AND_NOT_CLAIMED",
            "branch_local_status": (
                "the marked trace is proved independently by the source-locked "
                "B3 character-sum packet; this does not change the literature verdict"
            ),
            "bergstrom_2009": (
                "prints the unmarked V_(3,3) class and exact mixed-coordinate "
                "language; Lemma 12.8/Remark 12.9 require all u_g values, "
                "while Section 7.3 explicitly lacks all degree-six u_g values"
            ),
            "level_two_2008": (
                "defines the correct marked cover and exact finite trace "
                "formula, but the non-Eisenstein identification is "
                "conjectural and the fields are bounded; Section 9 checks "
                "the ambient A_2(w^1), not an all-q M_2(w^1) trace theorem"
            ),
            "erratum_2025": (
                "corrects the A_2[2], V_(3,3) example row by adding -15; "
                "that row is not an M_2(w^1) all-q theorem"
            ),
            "novelty": ("no novelty claim; later literature needs expert review"),
        },
        "bounded_proof_routes": [
            {
                "route": "Bergstrom u_g specialization",
                "next_step": (
                    "decompose r_1*Tr(V_(3,3)) into u_g coordinates, isolate "
                    "the non-general degree-six terms, supply genus-zero and "
                    "genus-one bases, and apply Theorem 4.12"
                ),
                "status": "OUTLINED_NOT_EXECUTED",
            },
            {
                "route": "source-locked B3 signature proof",
                "result": (
                    "all p1, p2, deletion-character, and squarefree-sieve "
                    "averages close across the exhaustive 23 signatures"
                ),
                "status": "COMPLETED_AND_INDEPENDENTLY_AUDITED",
            },
        ],
        "primary_literature": list(LITERATURE_ARTIFACTS),
        "provenance": {
            "source_locks": SOURCE_LOCKS,
            "source_hashes_lf_sha256": {
                "producer": _sha256_lf(Path(__file__)),
                "note": _sha256_lf(NOTE_PATH),
                "test": _sha256_lf(TEST_PATH),
            },
            "literature_authentication": (
                "URLs, locators, and downloaded hashes were manually audited; "
                "the local checker performs no network replay"
            ),
            "resource_contract": {
                "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
                "exact_operation_cap": guard.limit,
                "exact_operations_used": guard.used,
                "frozen_q_values": list(FROZEN_Q_VALUES),
                "finite_fields_enumerated": 0,
                "curves_enumerated": 0,
                "random_samples": 0,
                "arithmetic": "integers and exact fractions only",
            },
        },
        "firewalls": [
            "M_(2,1) with an arbitrary marked point is not M_2(w^1).",
            "Lemma 12.8 and Remark 12.9 are coordinate equivalences, not the source of the branch-local proof.",
            "The q=3,5,7 rows are regression controls; the theorem comes from all-q character-sum algebra, not interpolation.",
            "The corrected A_2[2] example table is not an all-q M_2(w^1) theorem.",
            "The Section 9 A_2(w^1) numerical Euler check is not an all-q M_2(w^1) trace theorem.",
            "The internal proof makes no claim of external novelty or prior-literature absence beyond the audited sources.",
            "No cohomological decomposition, modular-form identification, number-field transfer, RH, or GRH conclusion is asserted.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    group.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    args = parser.parse_args(argv)

    certificate = build_certificate()
    rendered = (
        json.dumps(
            certificate,
            allow_nan=False,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    if args.check:
        stored = args.check.read_text(encoding="utf-8")
        if stored != rendered:
            raise SystemExit(f"chi03 reconciliation fixture mismatch: {args.check}")
        print(f"PASS_GENUS2_CHI03_STACK_TRACE_RECONCILIATION {args.check}")
        return 0
    if args.write:
        args.write.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {args.write}")
        return 0
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
