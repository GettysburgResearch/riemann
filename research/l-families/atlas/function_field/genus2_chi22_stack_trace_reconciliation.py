#!/usr/bin/env python3
"""Bounded reconciliation of the marked genus-two chi_(2,2) trace.

This producer enumerates no finite field. It source-locks the exact
marked-stack adapter, the all-q B3 dependency, and the all-q M22 theorem;
imports one explicitly located published unmarked trace theorem; and derives
the marked/unmarked/mixed identities using exact integer polynomials.

The primary-literature text is a manually audited dependency. Its URLs,
locators, and downloaded artifact hashes are recorded, but this producer does
not access the network or machine-authenticate those documents.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_chi22_stack_trace_reconciliation.json"
NOTE_PATH = HERE.parent / "GENUS2_CHI22_STACK_TRACE_RECONCILIATION.md"
TEST_PATH = ROOT / "tests" / "test_genus2_chi22_stack_trace_reconciliation.py"

MARKED_ADAPTER_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
B3_THEOREM_PATH = HERE / "genus2_b3_primitive_trace_average.json"
M22_THEOREM_PATH = HERE / "genus2_m22_triangular_trace_average.json"

MAX_SOURCE_BYTES_EACH = 150_000
MAX_EXACT_OPERATIONS = 1_024
CHECK_Q_VALUES = (3, 5, 7)

SOURCE_LOCKS: dict[str, dict[str, str]] = {
    "genus2_marked_weierstrass_stack_adapter.json": {
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
    },
    "genus2_b3_primitive_trace_average.json": {
        "lf_sha256": "5ecc6006014a159a4030218977c89f58c63334461a568b7a67d36130bae1c50b",
        "payload_sha256": "e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd",
        "schema": "riemann.function_field.genus2_b3_primitive_trace_average.v1",
        "commit": "65eb68fe150998451799059aca80dce550a75b87",
    },
    "genus2_m22_triangular_trace_average.json": {
        "lf_sha256": "a93f288ddce023005989cc0a7ed543d859697e68fa378a24ae7619af35fc9633",
        "payload_sha256": "4d147295e3d2b7bc4b62eb8ba113c946f528606d82dd28d1a1ec002e2f93d60c",
        "schema": "riemann.function_field.genus2_m22_triangular_trace_average.v1",
        "commit": "65f4c7dc0c7340b561d0fb278cda75f1fb7944cd",
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
            (
                "Section 2, geometric Frobenius and arbitrary-point groupoid "
                "count (arXiv PDF pp. 3-4)"
            ),
            "Section 7.3, incomplete degree-six u_g inventory (arXiv PDF p. 17)",
            (
                "Section 11.1 (arXiv PDF p. 26) and Theorem 11.6 "
                "(arXiv PDF p. 29), e_c(M_2,V_(4,2))=L^3"
            ),
            (
                "Definition 12.1 (arXiv PDF p. 29), Lemma 12.8 "
                "(pp. 30-31), and Remark 12.9 (p. 31)"
            ),
        ],
        "claim_boundary": (
            "proves the unmarked V_(4,2) trace and supplies mixed "
            "ramification coordinates, but does not print or evaluate the "
            "marked V_(4,2) trace"
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
        "version": "arXiv v2, 20 April 2008",
        "pdf_sha256": (
            "f6294c69e2cafe16b4b0dc1ba1692a46813ba6e467e546aa548442d1a4f2a19e"
        ),
        "eprint_source_sha256": (
            "5780b581522ec17d4dfacc202b277f92e9b464fc54ef5f60dcc8ef56b660e5f0"
        ),
        "locators": [
            (
                "Sections 2-3, definitions of M_2(w^n), A_2(w^n), and "
                "V_(l,m) (arXiv PDF pp. 2-3)"
            ),
            "Section 5, finite-field computation for odd q<=37 (arXiv PDF pp. 6-8)",
            "Section 9, numerical A_2(w^1) dimension checks (arXiv PDF p. 12)",
            "Section 10, conjectural A_2[2], V_(4,2) example row (arXiv PDF p. 12)",
        ],
        "claim_boundary": (
            "right marked-Weierstrass geometry and finite point-count "
            "machinery, but no printed all-q M_2(w^1), V_(4,2) theorem"
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
            "p. 1: corrected A_2[2] example table, including the V_(4,2) row",
            "p. 2: corrected Example 7.10 in the pointed-hyperelliptic paper",
        ],
        "claim_boundary": (
            "prints the corrected ambient A_2[2], V_(4,2) row; that row is "
            "not an M_2(w^1) all-q theorem, and Theorem 11.6 is not listed "
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
    if claimed != lock["payload_sha256"]:
        raise ArithmeticError(f"pinned payload mismatch for {path.name}")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload):
        raise ArithmeticError(f"internal payload mismatch for {path.name}")
    return value


def _require_q(q: int) -> int:
    if isinstance(q, bool) or not isinstance(q, int) or q <= 1:
        raise ValueError("q must be an integer greater than one")
    return q


def unmarked_trace(q: int) -> int:
    q = _require_q(q)
    return q**3


def arbitrary_point_trace(q: int) -> int:
    q = _require_q(q)
    return (q + 1) * unmarked_trace(q)


def marked_trace(q: int) -> int:
    q = _require_q(q)
    return 2 * q**3 - q**2 - 2 * q - 2


def mixed_trace(q: int) -> int:
    q = _require_q(q)
    return (q + 1) * unmarked_trace(q) - marked_trace(q)


def marked_trace_from_mixed(q: int, mixed: int) -> int:
    q = _require_q(q)
    if isinstance(mixed, bool) or not isinstance(mixed, int):
        raise TypeError("mixed trace must be an integer")
    return (q + 1) * unmarked_trace(q) - mixed


def _poly_add(
    left: Sequence[int], right: Sequence[int], guard: OperationGuard
) -> tuple[int, ...]:
    values: list[int] = []
    for index in range(max(len(left), len(right))):
        guard.consume()
        values.append(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _poly_scale(
    value: Sequence[int], scalar: int, guard: OperationGuard
) -> tuple[int, ...]:
    guard.consume(len(value))
    return tuple(scalar * coefficient for coefficient in value)


def _poly_multiply(
    left: Sequence[int], right: Sequence[int], guard: OperationGuard
) -> tuple[int, ...]:
    values = [0] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            guard.consume(2)
            values[left_degree + right_degree] += left_coefficient * right_coefficient
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _poly_evaluate(value: Sequence[int], q: int, guard: OperationGuard) -> int:
    q = _require_q(q)
    result = 0
    for coefficient in reversed(value):
        guard.consume(2)
        result = result * q + coefficient
    return result


def _verify_adapter(adapter: Mapping[str, object]) -> dict[str, object]:
    theorem = adapter.get("trace_theorem")
    if not isinstance(theorem, dict):
        raise TypeError("marked adapter lost trace theorem")
    channels = theorem.get("even_channels_closed_by_adapter")
    if not isinstance(channels, dict):
        raise TypeError("marked adapter lost channel dictionary")
    channel = channels.get("chi_(2,2)")
    if not isinstance(channel, dict):
        raise TypeError("marked adapter lost chi_(2,2)")
    expected = {
        "fundamental_weight": [2, 2],
        "highest_weight_e_basis": [4, 2],
        "local_system_weight": 6,
        "central_character": 1,
        "dimension": 81,
        "exact_stack_trace_formula": ("q^3/(q*(q-1))*sum_(D in H5(q)) chi_(2,2)(U_D)"),
        "adapter_status": "PROVED_BY_THIS_PACKET",
    }
    for key, value in expected.items():
        if channel.get(key) != value:
            raise ArithmeticError(f"marked adapter chi_(2,2) drift at {key}")
    return {
        "project_character": "chi_(2,2)",
        "project_coordinate_system": "C2 fundamental-weight coordinates",
        "fundamental_weight": [2, 2],
        "highest_weight_e_basis": [4, 2],
        "literature_local_system": "V_(4,2)",
        "local_system_weight": 6,
        "central_character": 1,
        "status": "PROVED_BY_MARKED_STACK_ADAPTER",
    }


def _verify_branch_theorems(
    b3: Mapping[str, object], m22: Mapping[str, object]
) -> dict[str, object]:
    if b3.get("status") != "PROVED_EXACT_ALL_ODD_PRIME_POWERS":
        raise ArithmeticError("B3 dependency lost proved status")
    if m22.get("status") != "PROVED_EXACT_ALL_ODD_PRIME_POWERS":
        raise ArithmeticError("M22 theorem lost proved status")
    b3_theorem = b3.get("theorem")
    m22_theorem = m22.get("theorem")
    if not isinstance(b3_theorem, dict) or not isinstance(m22_theorem, dict):
        raise TypeError("branch theorem dictionary is malformed")
    if b3_theorem.get("chi_(0,3)_mean") != "(q^4-2*q-1)/q^6":
        raise ArithmeticError("B3 chi_(0,3) dependency drift")
    expected_m22 = {
        "M22_total": (
            "sum_D a_D^2*b_D^2=q*(q-1)*(q+1)*(5*q^5-19*q^4+29*q^3-5*q^2-21*q-3)"
        ),
        "R22_mean": "(q^4+2*q^3-q^2-4*q-3)/q^6",
        "chi_(2,2)_mean": "(2*q^3-q^2-2*q-2)/q^6",
        "marked_stack_trace_chi_(2,2)": "2*q^3-q^2-2*q-2",
    }
    for key, value in expected_m22.items():
        if m22_theorem.get(key) != value:
            raise ArithmeticError(f"M22 theorem drift at {key}")
    reused = m22.get("reused_primitive_aggregate_lemma")
    if not isinstance(reused, dict):
        raise TypeError("M22 theorem lost B3 source bridge")
    if reused.get("source_payload_sha256") != b3.get("payload_sha256"):
        raise ArithmeticError("M22/B3 payload bridge drift")
    audit = m22.get("ordered_tuple_signature_audit")
    if not isinstance(audit, dict) or audit.get("signature_count") != 20:
        raise ArithmeticError("M22 signature audit drift")
    return {
        "status": "PROVED_EXACT_ALL_ODD_PRIME_POWERS",
        "M22_total": expected_m22["M22_total"],
        "R22_mean": expected_m22["R22_mean"],
        "chi_(0,3)_mean": b3_theorem["chi_(0,3)_mean"],
        "chi_(2,2)_mean": expected_m22["chi_(2,2)_mean"],
        "marked_stack_trace": "T_(2,2)(q)=2*q^3-q^2-2*q-2",
        "M22_signature_count": 20,
        "B3_dependency_payload_sha256": b3["payload_sha256"],
    }


def build_certificate() -> dict[str, object]:
    guard = OperationGuard()
    adapter = _load_locked_json(
        MARKED_ADAPTER_PATH, SOURCE_LOCKS[MARKED_ADAPTER_PATH.name]
    )
    b3 = _load_locked_json(B3_THEOREM_PATH, SOURCE_LOCKS[B3_THEOREM_PATH.name])
    m22 = _load_locked_json(M22_THEOREM_PATH, SOURCE_LOCKS[M22_THEOREM_PATH.name])
    alias = _verify_adapter(adapter)
    branch_theorem = _verify_branch_theorems(b3, m22)

    # Coefficient order is increasing in q.
    q_plus_one = (1, 1)
    unmarked = (0, 0, 0, 1)
    arbitrary = _poly_multiply(q_plus_one, unmarked, guard)
    candidate_marked = (-2, -2, -1, 2)
    mixed = _poly_add(arbitrary, _poly_scale(candidate_marked, -1, guard), guard)
    expected_mixed = (2, 2, 1, -1, 1)
    if arbitrary != (0, 0, 0, 1, 1):
        raise ArithmeticError("arbitrary-point polynomial drift")
    if mixed != expected_mixed:
        raise ArithmeticError("marked/unmarked mixed polynomial reduction failed")

    checks: list[dict[str, object]] = []
    for q in CHECK_Q_VALUES:
        values = {
            "q": q,
            "unmarked_trace_U_42": _poly_evaluate(unmarked, q, guard),
            "arbitrary_point_trace_A_42": _poly_evaluate(arbitrary, q, guard),
            "marked_Weierstrass_trace_T_(2,2)": _poly_evaluate(
                candidate_marked, q, guard
            ),
            "mixed_ramification_trace_M_42": _poly_evaluate(mixed, q, guard),
            "status": "EXACT_SPECIALIZATION_NOT_AN_ALL_Q_PROOF_INPUT",
        }
        if values["unmarked_trace_U_42"] != unmarked_trace(q):
            raise ArithmeticError(f"q={q} unmarked specialization failed")
        if values["arbitrary_point_trace_A_42"] != arbitrary_point_trace(q):
            raise ArithmeticError(f"q={q} arbitrary specialization failed")
        if values["marked_Weierstrass_trace_T_(2,2)"] != marked_trace(q):
            raise ArithmeticError(f"q={q} marked specialization failed")
        if values["mixed_ramification_trace_M_42"] != mixed_trace(q):
            raise ArithmeticError(f"q={q} mixed specialization failed")
        if marked_trace_from_mixed(q, mixed_trace(q)) != marked_trace(q):
            raise ArithmeticError(f"q={q} forgetful-fibre equivalence failed")
        checks.append(values)

    payload: dict[str, object] = {
        "schema": ("riemann.function_field.genus2_chi22_stack_trace_reconciliation.v1"),
        "status": (
            "PROVED_ON_BRANCH_EXACT_M22_AND_MARKED_STACK_TRACE_"
            "PUBLISHED_MARKED_TABLE_IMPORT_NOT_FOUND"
        ),
        "scope": {
            "base_fields": "all finite fields F_q of odd characteristic",
            "unmarked_moduli_problem": "M_2",
            "arbitrary_point_moduli_problem": ("M_(2,1), one arbitrary rational point"),
            "marked_moduli_problem": ("M_2(w^1), one rational Weierstrass point"),
            "finite_field_or_curve_enumeration": False,
            "external_database_query": False,
            "rh_or_grh_claim": False,
        },
        "character_alias": alias,
        "branch_local_theorem": branch_theorem,
        "established_import": {
            "status": "IMPORTED_PRIMARY_LITERATURE_THEOREM_NOT_REPROVED_HERE",
            "formula": "U_42(q)=q^3",
            "definition": ("U_42(q)=sum_[C in M_2(F_q)] Tr(F_q|V_(4,2),C)/|Aut_q(C)|"),
            "source": (
                "Bergstrom, Section 2 geometric-Frobenius convention, "
                "Section 11.1 polynomial trace bridge, and Theorem 11.6, "
                "e_c(M_2,V_(4,2))=L^3"
            ),
            "characteristic": "odd",
            "erratum_boundary": (
                "the 2025 author erratum corrects Example 7.10 but does not "
                "list Theorem 11.6 as altered"
            ),
        },
        "arbitrary_point_distinction": {
            "stack": "M_(2,1)",
            "fibre_count": "#C(F_q)=q+1-a_1(C)",
            "odd_cross_trace": ("sum_[C] a_1(C)*Tr(F_q|V_(4,2),C)/|Aut_q(C)|=0"),
            "odd_cross_trace_reason": (
                "the central hyperelliptic mu_2-inertia acts nontrivially "
                "because a_1 has odd central weight and V_(4,2) has even "
                "central weight; equivalently, weighted twist descent cancels"
            ),
            "trace": "A_42(q)=q^4+q^3",
            "status": (
                "EXACT_CONSEQUENCE_OF_UNMARKED_TRACE_AND_CENTRAL_PARITY_"
                "NOT_THE_MARKED_WEIERSTRASS_TRACE"
            ),
        },
        "forgetful_fibre_identity": {
            "r_1_definition": (
                "Bergstrom r_1(C) counts rational base points with "
                "unramified hyperelliptic fibre"
            ),
            "rational_Weierstrass_count": "R_1(C)=q+1-r_1(C)",
            "mixed_trace_definition": (
                "M_42(q)=sum_[C in M_2(F_q)] r_1(C)*Tr(F_q|V_(4,2),C)/|Aut_q(C)|"
            ),
            "exact_identity": "T_(2,2)(q)=(q+1)*U_42(q)-M_42(q)",
            "after_unmarked_import": "T_(2,2)(q)=q^3*(q+1)-M_42(q)",
            "proof": (
                "groupoid cardinality of the forgetful fibre "
                "M_2(w^1)->M_2; automorphism weights are retained"
            ),
            "status": "PROVED_EXACTLY",
        },
        "mixed_trace_consequence": {
            "name": "CHI22-MIXED-RAMIFICATION-TRACE",
            "target": "M_42(q)=q^4-q^3+q^2+2*q+2",
            "proved_marked_trace": "T_(2,2)(q)=2*q^3-q^2-2*q-2",
            "exact_equivalence": (
                "T_(2,2)(q)=2*q^3-q^2-2*q-2 iff M_42(q)=q^4-q^3+q^2+2*q+2"
            ),
            "coefficient_vectors_in_increasing_q_power": {
                "unmarked_U_42": list(unmarked),
                "arbitrary_point_A_42": list(arbitrary),
                "marked_T_(2,2)": list(candidate_marked),
                "mixed_M_42": list(mixed),
            },
            "proof": (
                "the M22/B3 packets prove T_(2,2); the exact "
                "forgetful-fibre identity and published U_42=q^3 then "
                "prove M_42"
            ),
            "status": "PROVED_ON_BRANCH_AS_EXACT_CONSEQUENCE",
        },
        "exact_specializations": checks,
        "literature_verdict": {
            "published_unmarked_formula": "FOUND: U_42(q)=q^3",
            "published_marked_formula": "NOT_FOUND_IN_AUDITED_SOURCES_AND_NOT_CLAIMED",
            "published_mixed_formula": "NOT_FOUND_IN_AUDITED_SOURCES_AND_NOT_CLAIMED",
            "bergstrom_2009": (
                "prints the unmarked V_(4,2) class and exact mixed-coordinate "
                "language; Lemma 12.8/Remark 12.9 require all u_g values, "
                "while Section 7.3 explicitly lacks all degree-six u_g values"
            ),
            "level_two_2008": (
                "defines M_2(w^1) and exact finite trace machinery, but the "
                "fields are bounded, later identifications are conjectural, "
                "and Section 9 concerns ambient A_2(w^1)"
            ),
            "erratum_2025": (
                "prints the corrected A_2[2], V_(4,2) row; the row is "
                "ambient and not an all-q M_2(w^1) theorem"
            ),
            "novelty": "no novelty claim; later literature needs expert review",
        },
        "bounded_alternative_route": {
            "route": "Bergstrom u_g specialization",
            "next_step": (
                "decompose r_1*Tr(V_(4,2)) into u_g coordinates, isolate "
                "every degree-six or degree-seven term not already computed, "
                "including the genuinely new degree-seven general terms, "
                "supply genus-zero and genus-one bases, and apply Theorem 4.12"
            ),
            "status": "OUTLINED_NOT_EXECUTED",
        },
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
                "check_q_values": list(CHECK_Q_VALUES),
                "finite_fields_enumerated": 0,
                "curves_enumerated": 0,
                "random_samples": 0,
                "arithmetic": "integers only",
            },
        },
        "firewalls": [
            "M_(2,1) with an arbitrary marked point is not M_2(w^1).",
            "The published U_42=q^3 theorem is unmarked and does not itself evaluate T_(2,2).",
            "Lemma 12.8 and Remark 12.9 are coordinate equivalences, not an evaluation of M_42.",
            "The q=3,5,7 rows are exact specializations; the all-q proof is not interpolation.",
            "The corrected A_2[2] example row is not an all-q M_2(w^1) theorem.",
            "The Section 9 A_2(w^1) numerical Euler check is not an all-q M_2(w^1) Frobenius theorem.",
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
            raise SystemExit(f"chi22 reconciliation fixture mismatch: {args.check}")
        print(f"PASS_GENUS2_CHI22_STACK_TRACE_RECONCILIATION {args.check}")
        return 0
    if args.write:
        args.write.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {args.write}")
        return 0
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
