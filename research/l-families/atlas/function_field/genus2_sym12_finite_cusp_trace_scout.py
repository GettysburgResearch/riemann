#!/usr/bin/env python3
"""Replay a source-locked q=3,5,7 scout for the marked Sym^12 scalar.

This producer reads three committed JSON artifacts: the complete stored joint
(a_D,b_D) laws for q=3,5,7, the committed low-weight modular trace rows, and
the exact arithmetic inventory that converts the directly replayed T_(12,0)
rows into Hhat_12.  It never imports or invokes a finite-field or polynomial
enumerator.

The resulting match with one explicit weight-14 level-2 q-expansion is a
finite consequence at three primes of the raw T_(12,0) replay plus that
inventory theorem.  It is not an independent direct Q_5 average, an all-q
interpolation theorem, a prime-power identity, or a cohomological
identification.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym12_finite_cusp_trace_scout.json"
NOTE_PATH = HERE / "GENUS2_SYM12_FINITE_CUSP_TRACE_SCOUT.md"
SCRIPT_PATH = Path(__file__).resolve()
TEST_PATH = ROOT / "tests" / "test_genus2_sym12_finite_cusp_trace_scout.py"

FROZEN_PRIMES = (3, 5, 7)
RECIPROCAL_DEGREES = (6, 8, 10, 12)
Q_EXPANSION_DEGREE = 7

MAX_SOURCE_FILES = 3
MAX_SOURCE_BYTES_EACH = 160_000
MAX_SOURCE_BYTES_TOTAL = 225_000
MAX_JOINT_LAW_ATOMS = 251
MAX_RECIPROCAL_UPDATES = 3_012
MAX_RECIPROCAL_TERMS = 10_542
MAX_WEIGHTED_ACCUMULATIONS = 1_004
MAX_DIVISOR_TESTS = 56
MAX_DIVISOR_TERMS = 32
MAX_CONVOLUTION_TERMS = 72
MAX_LINEAR_COMBINATIONS = 8
MAX_FINITE_ROW_CHECKS = 3
MAX_OUTPUT_BYTES = 32_768
MAX_WALL_SECONDS = 4.0

SOURCE_LOCKS: tuple[dict[str, object], ...] = (
    {
        "id": "balanced_joint_laws",
        "path": HERE / "balanced_control_family_scan.json",
        "commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
        "git_blob": "377c8c03d6a9ccf5a505a9b1a19acc360c59ff44",
        "lf_sha256": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload_sha256": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
        "schema": "riemann.function_field.balanced_control_family_scan.v1",
        "role": "complete stored q=3,5,7 joint (a_D,b_D) laws",
    },
    {
        "id": "modular_trace_rows",
        "path": HERE / "genus2_sym10_marked_trace_average.json",
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "561caa7dc504dfb158908aef9229e91af0707a1e",
        "lf_sha256": "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce",
        "payload_sha256": "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77",
        "schema": "riemann.genus2_sym10_marked_trace_average.v1",
        "role": "committed Delta, f_(8,2), and g_(10,2) trace rows",
    },
    {
        "id": "sym12_arithmetic_inventory",
        "path": HERE / "genus2_sym12_arithmetic_inventory.json",
        "commit": "482e32c53f26517906143cd0d99c74d8b4edf3be",
        "git_blob": "68907aa3ee65ced500807c79123f116da05f0ece",
        "lf_sha256": "94f0647a91aff299c62f24019947846e6923863f3ecba3c2f9cf95008407d4f6",
        "payload_sha256": "fba1c85c8dc3d60b276635ae5e3ed84db3ded06f4960afeaa9b92b4055f9211f",
        "schema": "riemann.function_field.genus2_sym12_arithmetic_inventory.v1",
        "role": (
            "exact source-relative conversion from replayed T_(12,0) to "
            "Hhat_12; the scout does not directly average Q_5"
        ),
    },
)

EXPECTED_F_STAR = [0, 1, 64, 1_236, 4_096, -57_450, 79_104, 64_232]
EXPECTED_TOTALS = {
    3: {6: -24, 8: -126, 10: 3_828, 12: -27_522},
    5: {6: -80, 8: 3_980, 10: 372_960, 12: 5_345_020},
    7: {6: -168, 8: -43_218, 10: -4_222_764, 12: -16_074_870},
}
EXPECTED_T12 = {3: -4_587, 5: 267_251, 7: -382_735}
EXPECTED_HHAT12 = {3: -3_708, 5: 287_250, 7: -449_624}


@dataclass
class ResourceGuard:
    source_files: int = 0
    source_bytes: int = 0
    joint_law_atoms: int = 0
    reciprocal_updates: int = 0
    reciprocal_terms: int = 0
    weighted_accumulations: int = 0
    divisor_tests: int = 0
    divisor_terms: int = 0
    convolution_terms: int = 0
    linear_combinations: int = 0
    finite_row_checks: int = 0

    @staticmethod
    def _increment(current: int, amount: int, maximum: int, label: str) -> int:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError(f"invalid {label} increment")
        updated = current + amount
        if updated > maximum:
            raise RuntimeError(f"{label} cap exceeded")
        return updated

    def source(self, byte_count: int) -> None:
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
        ):
            raise ValueError("invalid source-byte count")
        if byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("source-file byte cap exceeded")
        self.source_files = self._increment(
            self.source_files, 1, MAX_SOURCE_FILES, "source-file"
        )
        self.source_bytes = self._increment(
            self.source_bytes,
            byte_count,
            MAX_SOURCE_BYTES_TOTAL,
            "total source-byte",
        )

    def atom(self) -> None:
        self.joint_law_atoms = self._increment(
            self.joint_law_atoms, 1, MAX_JOINT_LAW_ATOMS, "joint-law atom"
        )

    def recurrence(self, terms: int) -> None:
        self.reciprocal_updates = self._increment(
            self.reciprocal_updates,
            1,
            MAX_RECIPROCAL_UPDATES,
            "reciprocal update",
        )
        self.reciprocal_terms = self._increment(
            self.reciprocal_terms,
            terms,
            MAX_RECIPROCAL_TERMS,
            "reciprocal term",
        )

    def weighted(self) -> None:
        self.weighted_accumulations = self._increment(
            self.weighted_accumulations,
            1,
            MAX_WEIGHTED_ACCUMULATIONS,
            "weighted accumulation",
        )

    def divisor_test(self, is_divisor: bool) -> None:
        self.divisor_tests = self._increment(
            self.divisor_tests, 1, MAX_DIVISOR_TESTS, "divisor test"
        )
        if is_divisor:
            self.divisor_terms = self._increment(
                self.divisor_terms, 1, MAX_DIVISOR_TERMS, "divisor term"
            )

    def convolution(self) -> None:
        self.convolution_terms = self._increment(
            self.convolution_terms,
            1,
            MAX_CONVOLUTION_TERMS,
            "convolution term",
        )

    def linear_combination(self) -> None:
        self.linear_combinations = self._increment(
            self.linear_combinations,
            1,
            MAX_LINEAR_COMBINATIONS,
            "linear combination",
        )

    def finite_row(self) -> None:
        self.finite_row_checks = self._increment(
            self.finite_row_checks,
            1,
            MAX_FINITE_ROW_CHECKS,
            "finite-row check",
        )


@dataclass(frozen=True)
class Deadline:
    started: float

    @classmethod
    def start(cls) -> Deadline:
        return cls(time.monotonic())

    def check(self, label: str) -> None:
        if not label:
            raise ValueError("deadline label must be nonempty")
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
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
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_bytes(raw: bytes) -> bytes:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return unicodedata.normalize("NFC", text).encode("utf-8")


def _lf_sha256(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    prefix = f"blob {len(normalized)}\0".encode()
    return hashlib.sha1(prefix + normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _require_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{label} must be an integer")
    return value


def _verify_payload_hash(value: Mapping[str, object], label: str) -> None:
    payload = dict(value)
    claimed = payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload):
        raise ValueError(f"{label} payload hash mismatch")


def _load_locked_source(
    lock: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    path = lock.get("path")
    if not isinstance(path, Path):
        raise TypeError("source lock path is invalid")
    raw = path.read_bytes()
    guard.source(len(raw))
    if _lf_sha256(raw) != lock.get("lf_sha256"):
        raise ValueError(f"LF-normalized source hash mismatch: {path}")
    if _git_blob(raw) != lock.get("git_blob"):
        raise ValueError(f"git-blob source hash mismatch: {path}")
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"source fixture is not an object: {path}")
    if value.get("schema") != lock.get("schema"):
        raise ValueError(f"source schema mismatch: {path}")
    if value.get("payload_sha256") != lock.get("payload_sha256"):
        raise ValueError(f"source payload sentinel mismatch: {path}")
    _verify_payload_hash(value, str(path))
    return value


def _validate_inventory(value: Mapping[str, object]) -> None:
    definitions = value.get("definitions")
    dependency = value.get("degree_twelve_dependency")
    if not isinstance(definitions, Mapping) or not isinstance(dependency, Mapping):
        raise TypeError("Sym12 arithmetic inventory blocks are missing")
    if (
        definitions.get("Hhat_12") != "H_12/(q*(q-1))"
        or dependency.get("marked_open_formula")
        != "T_(12,0)=Hhat_12-2*q-9-4*Theta_Delta-Theta_(8,2)-Theta_(10,2)"
    ):
        raise ValueError("Sym12 arithmetic-inventory conversion changed")


def reciprocal_coefficients(
    q: int,
    a_coefficient: int,
    b_coefficient: int,
    degree: int = 12,
    guard: ResourceGuard | None = None,
) -> list[int]:
    """Return r_0,...,r_degree for 1/P_D by the exact reciprocal recurrence."""

    for value, label in (
        (q, "q"),
        (a_coefficient, "a_coefficient"),
        (b_coefficient, "b_coefficient"),
        (degree, "degree"),
    ):
        _require_int(value, label)
    if q <= 1 or degree < 0 or degree > 12:
        raise ValueError("invalid reciprocal-recurrence parameters")

    values = [1]
    for index in range(1, degree + 1):
        terms = 1
        value = -a_coefficient * values[index - 1]
        if index >= 2:
            value -= b_coefficient * values[index - 2]
            terms += 1
        if index >= 3:
            value -= q * a_coefficient * values[index - 3]
            terms += 1
        if index >= 4:
            value -= q * q * values[index - 4]
            terms += 1
        values.append(value)
        if guard is not None:
            guard.recurrence(terms)
    return values


def _sigma_power(n: int, power: int, guard: ResourceGuard) -> int:
    total = 0
    for divisor in range(1, n + 1):
        is_divisor = n % divisor == 0
        guard.divisor_test(is_divisor)
        if is_divisor:
            total += divisor**power
    return total


def _convolve_prefix(
    left: Sequence[int], right: Sequence[int], guard: ResourceGuard
) -> list[int]:
    result = []
    for degree in range(Q_EXPANSION_DEGREE + 1):
        coefficient = 0
        for left_degree in range(degree + 1):
            guard.convolution()
            coefficient += left[left_degree] * right[degree - left_degree]
        result.append(coefficient)
    return result


def _explicit_f_star(
    modular: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    certificate = modular.get("modular_form_certificate")
    if not isinstance(certificate, dict):
        raise TypeError("modular-form certificate is missing")
    f8_raw = certificate.get("f_(8,2)_coefficients_0_through_9")
    g10_raw = certificate.get("g_(10,2)_coefficients_0_through_9")
    if not isinstance(f8_raw, list) or not isinstance(g10_raw, list):
        raise TypeError("committed modular coefficient rows are missing")
    f8 = [_require_int(value, "f_(8,2) coefficient") for value in f8_raw[:8]]
    g10 = [_require_int(value, "g_(10,2) coefficient") for value in g10_raw[:8]]
    if len(f8) != 8 or len(g10) != 8:
        raise ValueError("committed modular coefficient rows are too short")

    e4 = [1] + [
        240 * _sigma_power(degree, 3, guard)
        for degree in range(1, Q_EXPANSION_DEGREE + 1)
    ]
    e6 = [1] + [
        -504 * _sigma_power(degree, 5, guard)
        for degree in range(1, Q_EXPANSION_DEGREE + 1)
    ]
    f8_e6 = _convolve_prefix(f8, e6, guard)
    g10_e4 = _convolve_prefix(g10, e4, guard)
    f_star = []
    for left, right in zip(f8_e6, g10_e4):
        guard.linear_combination()
        numerator = left + 3 * right
        if numerator % 4:
            raise ArithmeticError("f_star q-expansion is not integral")
        f_star.append(numerator // 4)
    if f_star != EXPECTED_F_STAR:
        raise ArithmeticError("explicit f_star q-expansion sentinel failed")
    return {
        "name": "f_minus_explicit_Fricke_negative_target",
        "construction": "f_-(Q)=(f_(8,2)(Q)*E_6(Q)+3*g_(10,2)(Q)*E_4(Q))/4",
        "normalization": "coefficient of Q is 1",
        "Fricke_sign": -1,
        "E_4_coefficients_Q0_through_Q7": e4,
        "E_6_coefficients_Q0_through_Q7": e6,
        "f_(8,2)_coefficients_Q0_through_Q7": f8,
        "g_(10,2)_coefficients_Q0_through_Q7": g10,
        "coefficients_Q0_through_Q7": f_star,
        "display": ("Q+64*Q^2+1236*Q^3+4096*Q^4-57450*Q^5+79104*Q^6+64232*Q^7+O(Q^8)"),
        "status": "EXACT_Q_EXPANSION_FROM_LOCKED_ROWS_THROUGH_Q7",
    }


def _trace_rows(modular: Mapping[str, object]) -> dict[int, dict[str, int]]:
    raw = modular.get("held_out_falsification_controls")
    if not isinstance(raw, list) or len(raw) != 3:
        raise ValueError("committed modular trace rows changed")
    rows: dict[int, dict[str, int]] = {}
    for source_row in raw:
        if not isinstance(source_row, dict):
            raise TypeError("modular trace row is invalid")
        q = _require_int(source_row.get("q"), "modular trace q")
        rows[q] = {
            "Theta_Delta": _require_int(source_row.get("Theta_Delta"), "Theta_Delta"),
            "Theta_(8,2)": _require_int(source_row.get("Theta_(8,2)"), "Theta_(8,2)"),
            "Theta_(10,2)": _require_int(
                source_row.get("Theta_(10,2)"), "Theta_(10,2)"
            ),
            "committed_sum_r_D_10": _require_int(
                source_row.get("observed_sum_r_D_10"), "observed_sum_r_D_10"
            ),
        }
    if tuple(sorted(rows)) != FROZEN_PRIMES:
        raise ValueError("committed modular q support changed")
    return rows


def _finite_rows(
    balanced: Mapping[str, object],
    modular: Mapping[str, object],
    f_star: Mapping[str, object],
    guard: ResourceGuard,
) -> list[dict[str, object]]:
    frozen = balanced.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("balanced frozen-enumeration facts are missing")
    families = frozen.get("families")
    if not isinstance(families, list) or len(families) != 3:
        raise ValueError("balanced family rows changed")
    traces = _trace_rows(modular)
    coefficients = f_star.get("coefficients_Q0_through_Q7")
    if not isinstance(coefficients, list):
        raise TypeError("explicit f_star coefficients are missing")

    rows = []
    for family in families:
        if not isinstance(family, dict):
            raise TypeError("balanced family row is invalid")
        q = _require_int(family.get("q"), "family q")
        if q not in FROZEN_PRIMES:
            raise ValueError("balanced family q support changed")
        candidate_count = _require_int(family.get("candidate_count"), "candidate count")
        member_count = _require_int(family.get("member_count"), "member count")
        expected_members = q**4 * (q - 1)
        if candidate_count != q**5 or member_count != expected_members:
            raise ArithmeticError("balanced coverage sentinel failed")
        law = family.get("joint_a_D_b_D_law")
        if not isinstance(law, dict) or not isinstance(law.get("atoms"), list):
            raise TypeError("joint (a_D,b_D) law is missing")
        atoms = law["atoms"]
        support_size = _require_int(law.get("support_size"), "support size")
        if len(atoms) != support_size:
            raise ArithmeticError("joint-law support size mismatch")

        totals = {degree: 0 for degree in RECIPROCAL_DEGREES}
        counted_members = 0
        seen_pairs: set[tuple[int, int]] = set()
        for atom in atoms:
            if not isinstance(atom, dict):
                raise TypeError("joint-law atom is invalid")
            guard.atom()
            a_value = _require_int(atom.get("a_D"), "a_D")
            b_value = _require_int(atom.get("b_D"), "b_D")
            multiplicity = _require_int(atom.get("member_count"), "atom member count")
            if multiplicity <= 0 or (a_value, b_value) in seen_pairs:
                raise ArithmeticError("invalid or repeated joint-law atom")
            seen_pairs.add((a_value, b_value))
            coefficients_r = reciprocal_coefficients(q, a_value, b_value, 12, guard)
            for degree in RECIPROCAL_DEGREES:
                guard.weighted()
                totals[degree] += multiplicity * coefficients_r[degree]
            counted_members += multiplicity
        if counted_members != member_count:
            raise ArithmeticError("joint-law multiplicities do not cover the family")
        if totals != EXPECTED_TOTALS[q]:
            raise ArithmeticError("reciprocal-total sentinel failed")

        trace = traces[q]
        expected_r6 = -4 * q * (q - 1)
        expected_r8 = q * (q - 1) * (-trace["Theta_(8,2)"] - q - 6)
        expected_t10 = (
            (q - 1) * trace["Theta_Delta"]
            - trace["Theta_(8,2)"]
            - trace["Theta_(10,2)"]
            - q
            - 7
        )
        expected_r10 = q * (q - 1) * expected_t10
        if (
            totals[6] != expected_r6
            or totals[8] != expected_r8
            or totals[10] != expected_r10
            or totals[10] != trace["committed_sum_r_D_10"]
        ):
            raise ArithmeticError("lower reciprocal regression failed")

        denominator = q * (q - 1)
        if totals[12] % denominator:
            raise ArithmeticError("T_(12,0) is not integral")
        t12 = totals[12] // denominator
        hhat12 = (
            t12
            + 2 * q
            + 9
            + 4 * trace["Theta_Delta"]
            + trace["Theta_(8,2)"]
            + trace["Theta_(10,2)"]
        )
        a_p = _require_int(coefficients[q], "f_star prime coefficient")
        guard.finite_row()
        if t12 != EXPECTED_T12[q] or hhat12 != EXPECTED_HHAT12[q]:
            raise ArithmeticError("Sym12 finite-value sentinel failed")
        if hhat12 != -q * a_p:
            raise ArithmeticError("finite cusp-trace match failed")

        rows.append(
            {
                "q": q,
                "historical_complete_scan_candidates": candidate_count,
                "squarefree_family_members": member_count,
                "joint_law_atoms_replayed": support_size,
                "member_coefficient_ledger_sha256": family.get(
                    "member_coefficient_ledger_sha256"
                ),
                "reciprocal_totals": {
                    "sum_D_r_D(6)": totals[6],
                    "sum_D_r_D(8)": totals[8],
                    "sum_D_r_D(10)": totals[10],
                    "sum_D_r_D(12)": totals[12],
                },
                "lower_recurrence_checks": {
                    "r6": {
                        "expected_formula": "-4*q*(q-1)",
                        "expected_total": expected_r6,
                        "match": True,
                    },
                    "r8": {
                        "expected_formula": ("q*(q-1)*(-Theta_(8,2)(q)-q-6)"),
                        "expected_total": expected_r8,
                        "match": True,
                    },
                    "r10": {
                        "expected_formula": (
                            "q*(q-1)*((q-1)*Theta_Delta(q)-Theta_(8,2)(q)-"
                            "Theta_(10,2)(q)-q-7)"
                        ),
                        "expected_total": expected_r10,
                        "committed_control_total": trace["committed_sum_r_D_10"],
                        "match": True,
                    },
                },
                "modular_traces": {
                    "Theta_Delta": trace["Theta_Delta"],
                    "Theta_(8,2)": trace["Theta_(8,2)"],
                    "Theta_(10,2)": trace["Theta_(10,2)"],
                },
                "T_(12,0)": t12,
                "Hhat_12": hhat12,
                "H_12": denominator * hhat12,
                "Hhat_12_provenance": (
                    "derived from replayed T_(12,0) by the source-locked "
                    "Sym12 arithmetic inventory; not a direct Q_5 average"
                ),
                "a_p(f_-)": a_p,
                "-p*a_p(f_-)": -q * a_p,
                "finite_match": True,
            }
        )
    if [row["q"] for row in rows] != list(FROZEN_PRIMES):
        raise ValueError("balanced family row order changed")
    return rows


def _source_manifest(guard: ResourceGuard) -> list[dict[str, object]]:
    result = []
    for lock in SOURCE_LOCKS:
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source manifest path is invalid")
        result.append(
            {
                "id": lock["id"],
                "path": _relative(path),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "sha256_lf_normalized": lock["lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "schema": lock["schema"],
                "role": lock["role"],
                "bytes_read": path.stat().st_size,
            }
        )
    if sum(row["bytes_read"] for row in result) != guard.source_bytes:
        raise ArithmeticError("source-byte ledger mismatch")
    return result


def _packet_manifest() -> list[dict[str, str]]:
    return [
        {
            "path": _relative(path),
            "sha256_lf_normalized": _lf_sha256(path.read_bytes()),
        }
        for path in (NOTE_PATH, SCRIPT_PATH, TEST_PATH)
    ]


def _resource_contract(guard: ResourceGuard) -> dict[str, object]:
    nonoverlapping_exact_step_total = (
        guard.reciprocal_terms
        + guard.weighted_accumulations
        + guard.divisor_tests
        + guard.convolution_terms
        + guard.linear_combinations
        + guard.finite_row_checks
    )
    return {
        "arithmetic": "exact Python integers only; no floats or numerical fitting",
        "field_or_polynomial_enumeration": "FORBIDDEN_AND_NOT_PERFORMED",
        "source_files": {"maximum": MAX_SOURCE_FILES, "actual": guard.source_files},
        "source_bytes": {
            "maximum_each": MAX_SOURCE_BYTES_EACH,
            "maximum_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_total": guard.source_bytes,
        },
        "joint_law_atoms": {
            "maximum": MAX_JOINT_LAW_ATOMS,
            "actual": guard.joint_law_atoms,
        },
        "reciprocal_updates": {
            "maximum": MAX_RECIPROCAL_UPDATES,
            "actual": guard.reciprocal_updates,
        },
        "reciprocal_scalar_terms": {
            "maximum": MAX_RECIPROCAL_TERMS,
            "actual": guard.reciprocal_terms,
        },
        "weighted_accumulations": {
            "maximum": MAX_WEIGHTED_ACCUMULATIONS,
            "actual": guard.weighted_accumulations,
        },
        "Eisenstein_divisor_tests": {
            "maximum": MAX_DIVISOR_TESTS,
            "actual": guard.divisor_tests,
        },
        "Eisenstein_divisor_terms": {
            "maximum": MAX_DIVISOR_TERMS,
            "actual": guard.divisor_terms,
        },
        "q_series_convolution_terms": {
            "maximum": MAX_CONVOLUTION_TERMS,
            "actual": guard.convolution_terms,
        },
        "q_series_linear_combinations": {
            "maximum": MAX_LINEAR_COMBINATIONS,
            "actual": guard.linear_combinations,
        },
        "finite_row_checks": {
            "maximum": MAX_FINITE_ROW_CHECKS,
            "actual": guard.finite_row_checks,
        },
        "nonoverlapping_exact_step_total": nonoverlapping_exact_step_total,
        "counter_nesting": (
            "reciprocal_updates contain reciprocal_scalar_terms; contributing "
            "Eisenstein_divisor_terms are a subset of Eisenstein_divisor_tests"
        ),
        "maximum_output_bytes": MAX_OUTPUT_BYTES,
        "maximum_wall_seconds": MAX_WALL_SECONDS,
        "new_q_values_enumerated": [],
        "historical_complete_scan_candidates_not_rerun": 20_175,
        "historical_squarefree_members_not_rerun": 17_068,
    }


def build_fixture() -> dict[str, object]:
    deadline = Deadline.start()
    guard = ResourceGuard()
    balanced = _load_locked_source(SOURCE_LOCKS[0], guard)
    modular = _load_locked_source(SOURCE_LOCKS[1], guard)
    inventory = _load_locked_source(SOURCE_LOCKS[2], guard)
    _validate_inventory(inventory)
    deadline.check("source locks")
    f_star = _explicit_f_star(modular, guard)
    rows = _finite_rows(balanced, modular, f_star, guard)
    deadline.check("finite rows")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym12_finite_cusp_trace_scout.v1",
        "status": "FINITE_EXACT_Q3_Q5_Q7_MATCH_ONLY",
        "scope": {
            "tested_q_values": list(FROZEN_PRIMES),
            "tested_q_type": "odd primes only",
            "all_q_statement": "NOT_PROVED",
            "prime_power_statement": "NOT_TESTED_AND_NOT_PROVED",
            "family_enumeration_in_this_producer": [],
        },
        "definitions": {
            "reciprocal_series": (
                "1/(1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4)=sum_(n>=0) r_D(n)*u^n"
            ),
            "T_(12,0)": "sum_D r_D(12)/(q*(q-1))",
            "Hhat_12": (
                "inventory-derived T_(12,0)+2*q+9+4*Theta_Delta+"
                "Theta_(8,2)+Theta_(10,2)"
            ),
            "H_12": (
                "inventory-derived q*(q-1)*Hhat_12; not directly enumerated "
                "as a central Q_5 coefficient sum"
            ),
        },
        "source_manifest": _source_manifest(guard),
        "explicit_weight_14_level_2_target": f_star,
        "finite_rows": rows,
        "finite_match": {
            "identity_on_tested_rows": "Hhat_12(p)=-p*a_p(f_-), p in {3,5,7}",
            "equivalent_T_identity_on_tested_rows": (
                "T_(12,0)(p)=-p*a_p(f_-)-2*p-9-4*Theta_Delta(p)-"
                "Theta_(8,2)(p)-Theta_(10,2)(p)"
            ),
            "status": (
                "EXACT_THREE_PRIME_CONSEQUENCE_OF_RAW_T12_PLUS_INVENTORY_"
                "NOT_AN_INDEPENDENT_INVENTORY_AUDIT"
            ),
        },
        "provenance_boundary": {
            "directly_replayed": (
                "sum_D r_D(12) and T_(12,0) from the stored complete joint laws"
            ),
            "imported_exact_theorem": (
                "the Sym12 arithmetic-inventory identity converting T_(12,0) "
                "to Hhat_12 and H_12"
            ),
            "not_performed": (
                "a direct enumeration of squarefree degree-twelve f and the "
                "central completed coefficients Q_5(f)"
            ),
            "logical_use": (
                "the p=3,5,7 Hhat_12 rows test the combined raw-T plus inventory "
                "branch; they are not an independent audit of the inventory"
            ),
        },
        "coefficient_provenance": {
            "primary_reference": (
                "Clery--van der Geer (2018), pp. 1139--1140, explicit f_- "
                "weight-14 level-2 expansion and Fricke sign"
            ),
            "url": "https://ems.press/content/serial-article-files/26421",
            "in_packet_reconstruction": (
                "The displayed coefficients through Q^7 are independently rebuilt "
                "from the committed f_(8,2), g_(10,2) rows and exact E_4,E_6 series."
            ),
            "database_orbit_label_used": False,
        },
        "resource_contract": _resource_contract(guard),
        "packet_manifest": _packet_manifest(),
        "firewalls": [
            "FINITE INTERPOLATION FIREWALL: equality at p=3,5,7 does not imply an identity at any fourth q; corrections divisible by (q-3)*(q-5)*(q-7) are invisible here.",
            "PRIME-POWER FIREWALL: for q=p^r, a Frobenius-power trace alpha_p^r+beta_p^r is not the naive composite-index Fourier coefficient a_(p^r); this packet tests no r>1 row.",
            "The explicit q-expansion, not an ambiguous database orbit label, defines f_- in this packet.",
            "No motive, compatible system, Yoshida/endoscopic summand, or cohomological identification is proved by the finite match.",
            "The producer reads stored joint-law atoms and committed modular rows; it does not enumerate a field, polynomial, curve, or family member.",
            "The r6, r8, and r10 identities are lower recurrence regressions; they authenticate normalization but do not strengthen the r12 match beyond q=3,5,7.",
            "PROVENANCE FIREWALL: only T_(12,0) is replayed directly from the stored family atoms; Hhat_12 and H_12 are exact consequences of the separately source-locked arithmetic inventory, not an independent central-coefficient enumeration.",
            "No RH, GRH, number-field transfer, sign theorem, or global Euler-product claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    rendered = _serialized(payload)
    if len(rendered.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output byte cap exceeded")
    deadline.check("payload serialization")
    return payload


def _serialized(value: Mapping[str, object]) -> str:
    return (
        json.dumps(value, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    arguments = parser.parse_args(argv)
    rendered = _serialized(build_fixture())
    if len(rendered.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise SystemExit("rendered output exceeds the byte cap")
    if arguments.check:
        if not arguments.output.exists():
            raise SystemExit(f"missing fixture: {arguments.output}")
        if arguments.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"stale fixture: {arguments.output}")
        print(f"verified {arguments.output}")
        return 0
    arguments.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
