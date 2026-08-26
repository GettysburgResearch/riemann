#!/usr/bin/env python3
"""Build the exact Sym12 stable-channel closure and Eisenstein reduction.

The producer verifies finite symmetric-group branching, specializes an
explicitly conjectural BFG endoscopic/Eisenstein ledger, and compares it with
the committed project ambient formula.  A locked corrected marked-valuation
fixture closes the form-attached stable/general channel exactly; the
nonregular Eisenstein value remains open.  This is not an all-q trace formula.
No web service, database, finite field, polynomial, curve, or modular-form
space is queried at runtime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym12_conditional_endoscopic_closure.json"
NOTE_PATH = HERE / "GENUS2_SYM12_CONDITIONAL_ENDOSCOPIC_CLOSURE.md"
ADAPTER_NOTE_PATH = HERE / "GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md"
SCRIPT_PATH = Path(__file__).resolve()
TEST_PATH = ROOT / "tests" / "test_genus2_sym12_conditional_endoscopic_closure.py"

MAX_SOURCE_FILES = 9
MAX_SOURCE_BYTES_EACH = 45_000
MAX_SOURCE_BYTES_TOTAL = 180_000
MAX_BRANCHING_PARTITIONS = 11
MAX_BRANCHING_ROW_TESTS = 35
MAX_REMOVABLE_CORNERS = 19
MAX_ENDOSCOPIC_PROJECTION_TERMS = 11
MAX_HOOK_BOXES = 30
MAX_SYMBOLIC_COMPONENT_OPERATIONS = 70
MAX_FINITE_CORROBORATION_ROWS = 3
MAX_OUTPUT_BYTES = 32_768
MAX_WALL_SECONDS = 4.0

SOURCE_LOCKS: tuple[dict[str, object], ...] = (
    {
        "id": "sym12_inventory",
        "path": HERE / "genus2_sym12_arithmetic_inventory.json",
        "commit": "70dd4a130e702a2d6df4b0fb96a0182a560009a4",
        "git_blob": "b48963d7b9bc6459046024507a2f2cb8ccbbcd40",
        "lf_sha256": "e966b54fe909570eaac7d9253f635c8067c5f874ed47c9daf485c8fd88bfbd85",
        "payload_sha256": "557ab6465a16bb6080caa2a249c3d0935f8d36fb49bdf54898a0fe72b372496f",
        "schema": "riemann.function_field.genus2_sym12_arithmetic_inventory.v1",
        "role": "exact project ambient formula with one scalar Hhat_12",
    },
    {
        "id": "sym12_finite_scout",
        "path": HERE / "genus2_sym12_finite_cusp_trace_scout.json",
        "commit": "4a27bc2f96d9995f5657c23624ed731150f3630c",
        "git_blob": "9ee1d3cb82bf896e9479cf096faa0835a31a531c",
        "lf_sha256": "21540da03e0595b119120bf957a6ebaab136a0291525b87335c852a3c5c356b4",
        "payload_sha256": "9fdc8907f9b9c61de5d4e573b04fa6e78024b4c84117db5c4831d552e51086dc",
        "schema": "riemann.function_field.genus2_sym12_finite_cusp_trace_scout.v1",
        "role": (
            "finite q=3,5,7 raw T_(12,0) replay, inventory-derived Hhat_12, "
            "and explicit Fricke-negative f_minus"
        ),
    },
)

MARKED_ZERO_LOCK: dict[str, object] = {
    "id": "sym12_marked_valuation_kernel",
    "path": HERE / "genus2_sym12_marked_valuation_kernel.json",
    "commit": "a0871416abb4ac58132b53dd4ae30faeed9719bd",
    "git_blob": "6e9fcc3d42f1a7acf74759dd408259fd507c79f0",
    "raw_worktree_blob": "5a6449e035ced7fcf666ca29be0fe80b0075bb06",
    "lf_sha256": "9e833cb7778c6613d0f4c7ef22a72319864c05ce41c50addc9dee778d5446076",
    "role": (
        "exact corrected two-orientation rank-66/nullity-zero certificate for "
        "the marked (j,k)=(12,3) modular space"
    ),
}

PARTITIONS_OF_6: tuple[tuple[int, ...], ...] = (
    (6,),
    (5, 1),
    (4, 2),
    (4, 1, 1),
    (3, 3),
    (3, 2, 1),
    (3, 1, 1, 1),
    (2, 2, 2),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
)

BASIS = (
    "one",
    "L",
    "L_f_plus",
    "L_f_minus",
    "Hhat_12",
    "Epsilon_Eis",
    "Genuine",
)
Vector = tuple[int, int, int, int, int, int, int]
ZERO: Vector = (0, 0, 0, 0, 0, 0, 0)


@dataclass
class ResourceGuard:
    source_files: int = 0
    source_bytes: int = 0
    branching_partitions: int = 0
    branching_row_tests: int = 0
    removable_corners: int = 0
    endoscopic_projection_terms: int = 0
    hook_boxes: int = 0
    symbolic_component_operations: int = 0
    finite_corroboration_rows: int = 0

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
            self.source_files, 1, MAX_SOURCE_FILES, "source file"
        )
        self.source_bytes = self._increment(
            self.source_bytes,
            byte_count,
            MAX_SOURCE_BYTES_TOTAL,
            "source byte",
        )

    def partition(self) -> None:
        self.branching_partitions = self._increment(
            self.branching_partitions,
            1,
            MAX_BRANCHING_PARTITIONS,
            "branching partition",
        )

    def branching_row(self, is_corner: bool) -> None:
        self.branching_row_tests = self._increment(
            self.branching_row_tests,
            1,
            MAX_BRANCHING_ROW_TESTS,
            "branching row test",
        )
        if is_corner:
            self.removable_corners = self._increment(
                self.removable_corners,
                1,
                MAX_REMOVABLE_CORNERS,
                "removable corner",
            )

    def endoscopic_term(self) -> None:
        self.endoscopic_projection_terms = self._increment(
            self.endoscopic_projection_terms,
            1,
            MAX_ENDOSCOPIC_PROJECTION_TERMS,
            "endoscopic projection term",
        )

    def hook_box(self) -> None:
        self.hook_boxes = self._increment(
            self.hook_boxes, 1, MAX_HOOK_BOXES, "hook box"
        )

    def symbolic(self, amount: int) -> None:
        self.symbolic_component_operations = self._increment(
            self.symbolic_component_operations,
            amount,
            MAX_SYMBOLIC_COMPONENT_OPERATIONS,
            "symbolic component operation",
        )

    def finite_row(self) -> None:
        self.finite_corroboration_rows = self._increment(
            self.finite_corroboration_rows,
            1,
            MAX_FINITE_CORROBORATION_ROWS,
            "finite corroboration row",
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


def _raw_git_blob(raw: bytes) -> str:
    prefix = f"blob {len(raw)}\0".encode()
    return hashlib.sha1(prefix + raw).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _verify_payload_hash(value: Mapping[str, object], label: str) -> None:
    payload = dict(value)
    claimed = payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload):
        raise ValueError(f"{label} payload hash mismatch")


def _read_counted(path: Path, guard: ResourceGuard) -> bytes:
    raw = path.read_bytes()
    guard.source(len(raw))
    return raw


def _packet_manifest_rows(value: Mapping[str, object]) -> list[dict[str, str]]:
    manifest = value.get("packet_manifest")
    if isinstance(manifest, list):
        rows = []
        for row in manifest:
            if not isinstance(row, dict):
                raise TypeError("packet-manifest row is invalid")
            path = row.get("path")
            digest = row.get("sha256_lf_normalized")
            if not isinstance(path, str) or not isinstance(digest, str):
                raise TypeError("packet-manifest fields are invalid")
            rows.append({"path": path, "sha256_lf_normalized": digest})
        return rows
    if isinstance(manifest, dict):
        rows = []
        for label in ("note", "producer", "test"):
            path = manifest.get(label)
            digest = manifest.get(f"{label}_lf_sha256")
            if not isinstance(path, str) or not isinstance(digest, str):
                raise TypeError("legacy packet-manifest fields are invalid")
            rows.append({"path": path, "sha256_lf_normalized": digest})
        return rows
    raise TypeError("packet manifest is missing")


def _load_locked_packet(
    lock: Mapping[str, object], guard: ResourceGuard
) -> tuple[dict[str, object], list[dict[str, object]]]:
    path = lock.get("path")
    if not isinstance(path, Path):
        raise TypeError("source lock path is invalid")
    raw = _read_counted(path, guard)
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

    transitive = []
    for row in _packet_manifest_rows(value):
        packet_path = ROOT / row["path"]
        packet_raw = _read_counted(packet_path, guard)
        actual = _lf_sha256(packet_raw)
        if actual != row["sha256_lf_normalized"]:
            raise ValueError(f"transitive packet hash mismatch: {packet_path}")
        transitive.append(
            {
                "path": row["path"],
                "bytes_read": len(packet_raw),
                "sha256_lf_normalized": actual,
            }
        )
    return value, transitive


def _load_marked_zero(guard: ResourceGuard) -> dict[str, object]:
    path = MARKED_ZERO_LOCK.get("path")
    if not isinstance(path, Path):
        raise TypeError("marked-zero lock path is invalid")
    raw = _read_counted(path, guard)
    if _lf_sha256(raw) != MARKED_ZERO_LOCK.get("lf_sha256"):
        raise ValueError("LF-normalized marked-zero source hash mismatch")
    if _raw_git_blob(raw) != MARKED_ZERO_LOCK.get("raw_worktree_blob"):
        raise ValueError("raw-worktree marked-zero source hash mismatch")
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        raise TypeError("marked-zero fixture is not an object")

    parameters = value.get("parameters")
    highest = value.get("highest_weight_model")
    boundary = value.get("representative_boundary_valuation")
    controls = value.get("calibration_controls")
    if not all(isinstance(block, dict) for block in (parameters, highest, boundary)):
        raise TypeError("marked-zero fixture blocks are missing")
    if not isinstance(controls, list):
        raise TypeError("marked-zero calibration controls are missing")
    combined = boundary.get("combined_matrix")
    if not isinstance(combined, dict):
        raise TypeError("marked-zero combined matrix is missing")

    if parameters != {
        "b": 12,
        "d": 9,
        "holomorphy_t_degree_cap": 18,
        "selected_total_degree": 27,
    }:
        raise ValueError("marked-zero parameters changed")
    if highest.get("nullity") != 66:
        raise ValueError("marked-zero highest-weight dimension changed")
    if (
        combined.get("columns"),
        combined.get("rank_over_Q"),
        combined.get("nullity"),
        combined.get("rank_mod_1000003"),
        combined.get("rank_mod_1000033"),
    ) != (66, 66, 0, 66, 66):
        raise ValueError("marked-zero corrected rank certificate changed")
    if boundary.get("oriented_blocks_computed") != ["{1,2,6}", "{3,4,5}"]:
        raise ValueError("marked-zero orientation certificate changed")

    control_rows = {
        (row.get("d"), row.get("b")): row for row in controls if isinstance(row, dict)
    }
    expected_controls = {
        (4, 6): (6, 0),
        (7, 4): (18, 0),
        (12, 2): (36, 2),
    }
    if set(control_rows) != set(expected_controls):
        raise ValueError("marked-zero calibration controls changed")
    for key, (rank, nullity) in expected_controls.items():
        row = control_rows[key]
        if (row.get("corrected_rank"), row.get("corrected_nullity")) != (
            rank,
            nullity,
        ):
            raise ValueError("marked-zero calibration result changed")
    return value


def _partition_label(partition: Sequence[int]) -> str:
    return "[" + ",".join(str(part) for part in partition) + "]"


def _removable_shapes(
    partition: tuple[int, ...], guard: ResourceGuard
) -> tuple[tuple[int, ...], ...]:
    shapes = []
    for index, row_length in enumerate(partition):
        next_length = partition[index + 1] if index + 1 < len(partition) else 0
        is_corner = row_length > next_length
        guard.branching_row(is_corner)
        if not is_corner:
            continue
        updated = list(partition)
        updated[index] -= 1
        if updated[index] == 0:
            del updated[index]
        shape = tuple(updated)
        if sum(shape) != 5 or any(
            shape[i] < shape[i + 1] for i in range(len(shape) - 1)
        ):
            raise ArithmeticError("invalid S6-to-S5 branching shape")
        shapes.append(shape)
    return tuple(shapes)


def _branching_certificate(guard: ResourceGuard) -> dict[str, object]:
    rows = []
    invariant_labels = []
    for partition in PARTITIONS_OF_6:
        guard.partition()
        shapes = _removable_shapes(partition, guard)
        multiplicity = shapes.count((5,))
        if multiplicity not in (0, 1):
            raise ArithmeticError("unexpected S5-invariant multiplicity")
        label = _partition_label(partition)
        if multiplicity:
            invariant_labels.append(label)
        rows.append(
            {
                "S6_partition": label,
                "S5_shapes_after_removing_one_corner": [
                    _partition_label(shape) for shape in shapes
                ],
                "S5_invariant_multiplicity": multiplicity,
            }
        )
    if invariant_labels != ["[6]", "[5,1]"]:
        raise ArithmeticError("S6-to-S5 invariant branching changed")
    return {
        "rule": (
            "Res^(S6)_(S5) s[lambda] is the sum over partitions obtained by "
            "removing one corner; S5 invariants are copies of s[5]"
        ),
        "rows": rows,
        "partitions_with_invariants": invariant_labels,
        "invariant_multiplicity": 1,
        "status": "EXACT_STANDARD_BRANCHING_RULE_REPLAY",
    }


def _invariant_multiplicity(label: str, branching: Mapping[str, object]) -> int:
    rows = branching.get("rows")
    if not isinstance(rows, list):
        raise TypeError("branching rows are missing")
    for row in rows:
        if isinstance(row, dict) and row.get("S6_partition") == label:
            value = row.get("S5_invariant_multiplicity")
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("invalid branching multiplicity")
            return value
    raise KeyError(f"unknown S6 partition label: {label}")


def _project_terms(
    terms: Sequence[tuple[str, int | None]],
    branching: Mapping[str, object],
    guard: ResourceGuard,
) -> tuple[int, list[dict[str, object]]]:
    projected = 0
    rows = []
    for partition, coefficient in terms:
        guard.endoscopic_term()
        multiplicity = _invariant_multiplicity(partition, branching)
        if coefficient is None:
            if multiplicity:
                raise ArithmeticError("unknown coefficient survived S5 projection")
            contribution = 0
            coefficient_display: int | str = "irrelevant_tau_coefficient"
        else:
            contribution = coefficient * multiplicity
            coefficient_display = coefficient
        projected += contribution
        rows.append(
            {
                "partition": partition,
                "coefficient_after_k16_specialization": coefficient_display,
                "S5_invariant_multiplicity": multiplicity,
                "projected_coefficient": contribution,
            }
        )
    return projected, rows


def _level_one_cusp_dimension(weight: int) -> int:
    if weight < 4 or weight % 2:
        return 0
    quotient, remainder = divmod(weight, 12)
    modular_dimension = quotient if remainder == 2 else quotient + 1
    return modular_dimension - 1


def _level_two_cusp_dimension(weight: int) -> int:
    if weight < 4 or weight % 2:
        return 0
    return weight // 4 - 1


def _endoscopic_specialization(
    branching: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    tau = {
        "tau_(1,16)": 1,
        "tau_(2,16)": 1,
        "tau_16_plus": 1,
        "tau_16_minus": 0,
    }
    gamma04_terms = (
        ("[3,1,1,1]", None),
        ("[3,3]", tau["tau_(1,16)"]),
        ("[4,1,1]", tau["tau_(1,16)"] + tau["tau_(2,16)"]),
    )
    gamma02_terms = (
        ("[3,2,1]", tau["tau_(1,16)"] + tau["tau_(2,16)"]),
        ("[4,1,1]", None),
        ("[4,2]", tau["tau_(1,16)"]),
        ("[5,1]", tau["tau_(1,16)"]),
    )
    plus_terms = (
        ("[4,2]", tau["tau_16_plus"]),
        ("[5,1]", tau["tau_16_minus"]),
    )
    minus_terms = (
        ("[4,2]", tau["tau_16_minus"]),
        ("[5,1]", tau["tau_16_plus"]),
    )
    gamma04, gamma04_rows = _project_terms(gamma04_terms, branching, guard)
    gamma02, gamma02_rows = _project_terms(gamma02_terms, branching, guard)
    plus, plus_rows = _project_terms(plus_terms, branching, guard)
    minus, minus_rows = _project_terms(minus_terms, branching, guard)
    level_one_dimension = _level_one_cusp_dimension(14)
    if (gamma04, gamma02, plus, minus, level_one_dimension) != (0, 1, 0, 1, 0):
        raise ArithmeticError("BFG endoscopic S5 projection failed")
    return {
        "source_formula": "BFG_2008_Conjecture_8.1",
        "parameters": {"l": 12, "m": 0, "k": 16, "k_prime": 14},
        "tau_specialization": tau,
        "projected_channels": {
            "S14_Gamma0(4)_new": {
                "term_rows": gamma04_rows,
                "projected_multiplicity": gamma04,
                "result": "0 by S6-to-S5 branching",
            },
            "S14_Gamma0(2)_new": {
                "term_rows": gamma02_rows,
                "projected_multiplicity": gamma02,
                "motive": "f_plus+f_minus",
            },
            "S14_Gamma0(2)_new_plus": {
                "term_rows": plus_rows,
                "projected_multiplicity": plus,
                "motive": "f_plus",
            },
            "S14_Gamma0(2)_new_minus": {
                "term_rows": minus_rows,
                "projected_multiplicity": minus,
                "motive": "f_minus",
            },
            "S14_SL2Z": {
                "dimension": level_one_dimension,
                "result": "0 independently of its S6 coefficient ledger",
            },
        },
        "S5_invariant_inside_parentheses": "f_plus+2*f_minus",
        "expanded_endoscopy": "-L*(f_plus+2*f_minus)",
        "BFG_status": "CONJECTURAL_IN_BFG_2008",
        "later_theorem_support": (
            "Roesner Theorem 5.13 and Shmakov Theorem 4.6.4 support the "
            "semisimplified inner/endoscopic mechanism for nonregular weights"
        ),
    }


def _eisenstein_specialization() -> dict[str, object]:
    dim_s14_level2 = _level_two_cusp_dimension(14)
    dim_s16_level2 = _level_two_cusp_dimension(16)
    dim_s14_level1 = _level_one_cusp_dimension(14)
    s2_formal: tuple[int, int] = (-1, -1)  # -1-L in basis (one,L).
    even_tail = (2 * (s2_formal[0] + 1), 2 * s2_formal[1])
    result = (dim_s14_level2 + even_tail[0], -dim_s16_level2 + even_tail[1])
    if (
        (dim_s14_level2, dim_s16_level2, dim_s14_level1) != (2, 3, 0)
        or even_tail != (0, -2)
        or result != (2, -5)
    ):
        raise ArithmeticError("formal nonregular Eisenstein specialization failed")
    return {
        "formula_specialized": ("dim S14(Gamma0(2))-dim S16(Gamma0(2))*L+2*(S[2]+1)"),
        "dimensions": {
            "dim_S14_Gamma0(2)": dim_s14_level2,
            "dim_S16_Gamma0(2)": dim_s16_level2,
            "dim_S14_SL2Z": dim_s14_level1,
        },
        "nonregular_convention": "S[2]=-L-1",
        "even_tail": "2*(S[2]+1)=-2*L",
        "formal_result": "2-5*L",
        "BFG_status": (
            "CONJECTURAL_NONREGULAR_CONTINUATION; BFG proves the displayed "
            "Eisenstein formula only in the regular range"
        ),
        "later_source_discrepancy": {
            "Shmakov_Siegel_Eisenstein": "2-2*L",
            "Shmakov_Klingen": "0",
            "Shmakov_Borel": "-2*L",
            "Shmakov_printed_specialization": "2-4*L",
            "difference_BFG_minus_Shmakov": "-L",
            "missing_channel": (
                "one [5,1] tensor L copy tied to the unique Fricke-positive "
                "weight-16 level-2 newform"
            ),
            "outer_automorphism_excluded": (
                "Roesner constructs the natural S6 action from six Weierstrass points"
            ),
            "normalization_check": (
                "the project and both cited specializations concern the same ambient "
                "A_2(w^1)=A_2[2]/S5; no open/ambient reconciliation is identified"
            ),
            "connecting_and_Galois_caveat": (
                "connecting assumptions do not change Euler characteristic; a "
                "Galois-action caveat remains"
            ),
            "status": "UNRESOLVED_ONE_TATE_DISCREPANCY",
        },
    }


def _hook_dimension(partition: Sequence[int], guard: ResourceGuard) -> int:
    hook_product = 1
    for row_index, row_length in enumerate(partition):
        for column_index in range(row_length):
            guard.hook_box()
            boxes_below = sum(
                lower_length > column_index
                for lower_length in partition[row_index + 1 :]
            )
            hook_product *= row_length - column_index + boxes_below
    return math.factorial(sum(partition)) // hook_product


def _stable_vanishing_certificate(
    branching: Mapping[str, object],
    marked: Mapping[str, object],
    guard: ResourceGuard,
) -> dict[str, object]:
    api_partitions = (
        (3, 1, 1, 1),
        (2, 2, 2),
        (2, 2, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1),
    )
    rows = []
    total_dimension = 0
    invariant_dimension = 0
    for partition in api_partitions:
        label = _partition_label(partition)
        dimension = _hook_dimension(partition, guard)
        multiplicity = _invariant_multiplicity(label, branching)
        total_dimension += dimension
        invariant_dimension += multiplicity
        rows.append(
            {
                "S6_partition": label,
                "Specht_dimension": dimension,
                "S5_invariant_multiplicity": multiplicity,
            }
        )
    if total_dimension != 30 or invariant_dimension != 0:
        raise ArithmeticError("stable-space data projection failed")
    highest = marked.get("highest_weight_model")
    boundary = marked.get("representative_boundary_valuation")
    if not isinstance(highest, dict) or not isinstance(boundary, dict):
        raise TypeError("marked-zero certificate blocks are missing")
    combined = boundary.get("combined_matrix")
    if not isinstance(combined, dict):
        raise TypeError("marked-zero combined matrix is missing")

    return {
        "project_notation": "S_(12,3)(Gamma_2(w^1))",
        "source_notation_warning": (
            "Bergstrom--Clery order is scalar first, S_(3,12); the project and "
            "official query use (j,k)=(12,3)"
        ),
        "exact_marked_modular_zero": {
            "preholomorphic_highest_weight_dimension": highest["nullity"],
            "corrected_two_orientation_matrix": {
                "rows": combined["rows"],
                "columns": combined["columns"],
                "rank_over_Q": combined["rank_over_Q"],
                "rank_mod_1000003": combined["rank_mod_1000003"],
                "rank_mod_1000033": combined["rank_mod_1000033"],
                "nullity": combined["nullity"],
            },
            "quotient_identification": (
                "A_2(w^1)=A_2[2]/S5 in the natural point-stabilizer convention"
            ),
            "odd_scalar_weight": (
                "M_(12,3)=S_(12,3), because the global Phi target vanishes"
            ),
            "conclusion": "S_(12,3)(Gamma_2(w^1))=0",
            "source_grade": "EXACT_LOCKED_CORRECTED_VALUATION_CERTIFICATE",
        },
        "form_to_stable_channel_adapter": {
            "BFG_definition": (
                "S[Gamma_2[2],(j,k)] is the form-attached rank-4-per-eigenform "
                "inner-cohomology channel"
            ),
            "Bergstrom_Clery_decomposition": (
                "S_(k,j)=S^(G)_(k,j) direct_sum S^(Y)_(k,j) for j>0; "
                "S^(G) is the general-type summand"
            ),
            "Roesner_theorem": (
                "for every l>=m>=0 the level-two inner cohomology is the direct "
                "sum of endoscopic, Saito-Kurokawa, and stable parts; the stable "
                "part consists of four-dimensional irreducible Galois "
                "representations and contributes equally to all four Hodge types"
            ),
            "holomorphic_component": (
                "H_!^(3,0)(A_2[2],V_(l,m)) is Hecke-isomorphic to "
                "S_(l-m,m+3)(Gamma[2]), including m=0"
            ),
            "invariant_exactness": (
                "over characteristic zero, S5 invariants are exact and commute "
                "with the stable direct-summand decomposition"
            ),
            "no_leakage": (
                "Yoshida/endoscopic and Eisenstein/boundary terms are separate "
                "summands; the level-two Soudry contribution is zero"
            ),
            "conclusion": (
                "Genuine=(S_gen,Gamma(2)[12,3])^S5=0 as a semisimple "
                "Gal(Qbar/Q)-representation"
            ),
            "source_grade": "THEOREM_GRADE_FORM_ATTACHED_ADAPTER",
        },
        "exact_conclusion": "Genuine=0",
        "official_conditional_corroboration": {
            "isotypical_rows": rows,
            "total_dimension_checksum": total_dimension,
            "S5_invariant_dimension_from_these_rows": invariant_dimension,
            "endpoint": ("https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0"),
            "runtime_access": "NONE; rows are a frozen source-audit transcription",
            "source_grade": ("CONDITIONAL_K3_ISOTYPICAL_FORMULA; CORROBORATION_ONLY"),
            "why_conditional": (
                "Bergstrom--Clery Theorem 5.3 covers k>=4; Remark 5.4 extends "
                "its cohomology-derived isotypical formula to k=3 only under the "
                "BFG nonregular Eisenstein conjecture"
            ),
        },
        "firewall": (
            "the conclusion is for the positive semisimplified stable/general "
            "channel G; it does not identify the nonregular compact-support "
            "Eisenstein Galois class or nonsemisimple boundary extensions"
        ),
    }


def _v_add(left: Vector, right: Vector, guard: ResourceGuard) -> Vector:
    guard.symbolic(len(BASIS))
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def _v_sub(left: Vector, right: Vector, guard: ResourceGuard) -> Vector:
    guard.symbolic(len(BASIS))
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def _serialize_vector(vector: Vector) -> dict[str, int]:
    return {
        name: coefficient for name, coefficient in zip(BASIS, vector) if coefficient
    }


def _conditional_algebra(guard: ResourceGuard) -> dict[str, object]:
    eisenstein_general: Vector = (2, -5, 0, 0, 0, 1, 0)
    eisenstein_bfg: Vector = (2, -5, 0, 0, 0, 0, 0)
    eisenstein_shmakov: Vector = (2, -4, 0, 0, 0, 0, 0)
    endoscopy: Vector = (0, 0, -1, -2, 0, 0, 0)
    minus_genuine: Vector = (0, 0, 0, 0, 0, 0, -1)
    project: Vector = (2, -5, -1, -1, 1, 0, 0)

    master_target = _v_add(
        _v_add(eisenstein_general, endoscopy, guard), minus_genuine, guard
    )
    master_difference = _v_sub(project, master_target, guard)
    bfg_closed_target = _v_add(eisenstein_bfg, endoscopy, guard)
    bfg_closed_difference = _v_sub(project, bfg_closed_target, guard)
    shmakov_general_target = _v_add(
        _v_add(eisenstein_shmakov, endoscopy, guard), minus_genuine, guard
    )
    shmakov_general_difference = _v_sub(project, shmakov_general_target, guard)
    shmakov_closed_target = _v_add(eisenstein_shmakov, endoscopy, guard)
    shmakov_closed_difference = _v_sub(project, shmakov_closed_target, guard)

    if master_difference != (0, 0, 0, 1, 1, -1, 1):
        raise ArithmeticError("master conditional ambient difference failed")
    if bfg_closed_difference != (0, 0, 0, 1, 1, 0, 0):
        raise ArithmeticError("vanishing-specialized ambient difference failed")
    if shmakov_general_difference != (0, -1, 0, 1, 1, 0, 1):
        raise ArithmeticError("Shmakov general ambient difference failed")
    if shmakov_closed_difference != (0, -1, 0, 1, 1, 0, 0):
        raise ArithmeticError("Shmakov closed ambient difference failed")
    return {
        "basis": list(BASIS),
        "interpretation": (
            "free trace-channel module; this algebra does not assert a motivic isomorphism"
        ),
        "project_ambient": {
            "formula": "Hhat_12+2-5*L-L*(f_plus+f_minus)",
            "vector": _serialize_vector(project),
        },
        "master_target_before_exact_stable_specialization": {
            "definitions": {
                "Epsilon_Eis": "e_Eis-(2-5*L)",
                "Genuine": "positive stable/general S5-invariant channel whose e_c contribution is -Genuine",
            },
            "formula": ("2-5*L+Epsilon_Eis-L*(f_plus+2*f_minus)-Genuine"),
            "vector": _serialize_vector(master_target),
            "project_minus_target": _serialize_vector(master_difference),
            "equality_iff": ("Hhat_12=-L*f_minus+Epsilon_Eis-Genuine"),
        },
        "target_after_exact_stable_vanishing": {
            "formula": "2-5*L-L*(f_plus+2*f_minus)",
            "vector": _serialize_vector(bfg_closed_target),
            "project_minus_target": _serialize_vector(bfg_closed_difference),
            "equality_iff": "Hhat_12=-L*f_minus",
            "status": (
                "EXACT_STABLE_SPECIALIZATION; EQUALITY_TO_MINUS_L_F_MINUS "
                "STILL_REQUIRES_EPSILON_EIS_ZERO"
            ),
        },
        "one_Tate_discrepancy_effect": {
            "if_Eisenstein_is_2_minus_4L_before_stable_vanishing": {
                "target": _serialize_vector(shmakov_general_target),
                "project_minus_target": _serialize_vector(shmakov_general_difference),
                "equality_iff": "Hhat_12=L-L*f_minus-Genuine",
            },
            "if_Eisenstein_is_2_minus_4L_and_Genuine_is_zero": {
                "target": _serialize_vector(shmakov_closed_target),
                "project_minus_target": _serialize_vector(shmakov_closed_difference),
                "equality_iff": "Hhat_12=L-L*f_minus",
            },
            "meaning": (
                "the unresolved Eisenstein discrepancy changes the closure relation; "
                "it cannot be ignored"
            ),
        },
    }


def _finite_corroboration(
    scout: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    match = scout.get("finite_match")
    provenance = scout.get("provenance_boundary")
    target = scout.get("explicit_weight_14_level_2_target")
    rows = scout.get("finite_rows")
    if (
        not isinstance(match, dict)
        or not isinstance(provenance, dict)
        or not isinstance(target, dict)
        or not isinstance(rows, list)
    ):
        raise TypeError("finite scout structure changed")
    if (
        match.get("status")
        != "EXACT_THREE_PRIME_CONSEQUENCE_OF_RAW_T12_PLUS_INVENTORY_"
        "NOT_AN_INDEPENDENT_INVENTORY_AUDIT"
    ):
        raise ValueError("finite scout status weakened")
    if "not an independent audit" not in str(
        provenance.get("logical_use")
    ) or "T_(12,0)" not in str(provenance.get("directly_replayed")):
        raise ValueError("finite scout provenance boundary changed")
    if target.get("Fricke_sign") != -1:
        raise ValueError("finite scout f_minus sign changed")
    corroboration = []
    for row in rows:
        if not isinstance(row, dict):
            raise TypeError("finite scout row is invalid")
        q = row.get("q")
        t12 = row.get("T_(12,0)")
        hhat = row.get("Hhat_12")
        coefficient = row.get("a_p(f_-)")
        traces = row.get("modular_traces")
        if (
            isinstance(q, bool)
            or not isinstance(q, int)
            or isinstance(t12, bool)
            or not isinstance(t12, int)
            or isinstance(hhat, bool)
            or not isinstance(hhat, int)
            or isinstance(coefficient, bool)
            or not isinstance(coefficient, int)
            or not isinstance(traces, Mapping)
            or "not a direct Q_5 average" not in str(row.get("Hhat_12_provenance"))
        ):
            raise TypeError("finite scout values are invalid")
        delta = traces.get("Theta_Delta")
        f8 = traces.get("Theta_(8,2)")
        g10 = traces.get("Theta_(10,2)")
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in (delta, f8, g10)
        ):
            raise TypeError("finite scout modular traces are invalid")
        guard.finite_row()
        if hhat != -q * coefficient:
            raise ArithmeticError("finite scout corroboration failed")
        alternate_required = q - q * coefficient
        if alternate_required - hhat != q:
            raise ArithmeticError("one-Tate finite shift failed")
        raw_t_project_minus_shmakov = (
            t12 + 9 + q + 4 * delta + f8 + g10 + q * coefficient
        )
        if raw_t_project_minus_shmakov != -q:
            raise ArithmeticError("raw-T one-Tate contradiction failed")
        corroboration.append(
            {
                "p": q,
                "direct_T_(12,0)": t12,
                "Hhat_12": hhat,
                "Hhat_12_is_inventory_derived": True,
                "a_p(f_minus)": coefficient,
                "BFG_required_Hhat": -q * coefficient,
                "Shmakov_2_minus_4L_required_Hhat_if_Genuine_zero": (
                    alternate_required
                ),
                "Shmakov_required_minus_observed": q,
                "Shmakov_required_Genuine_trace_to_match_observed": q,
                "raw_T_plus_inventory_project_minus_Shmakov_target": (
                    raw_t_project_minus_shmakov
                ),
                "BFG_match": True,
                "match": True,
            }
        )
    if [row["p"] for row in corroboration] != [3, 5, 7]:
        raise ValueError("finite scout support changed")
    return {
        "rows": corroboration,
        "role": (
            "EXACT_RAW_T_PLUS_INVENTORY_CONSEQUENCE_NOT_AN_INDEPENDENT_"
            "INVENTORY_AUDIT_OR_INTERPOLATION"
        ),
        "firewall": (
            "only T_(12,0) is replayed directly; Hhat_12 is inventory-derived, so "
            "the three primes test the combined arithmetic branch, are not an "
            "independent audit of the inventory, do not prove an all-q or prime-power "
            "identity, and do not realize the nonregular Eisenstein Galois class"
        ),
        "one_Tate_check": (
            "with Genuine=0, the 2-4*L branch requires Hhat_12=L-L*f_minus and "
            "therefore misses each stored row by +p; without that vanishing, the "
            "same rows instead require Tr(F_p,Genuine)=p"
        ),
        "raw_T_check": (
            "after substituting the inventory conversion but without treating Hhat_12 "
            "as direct data, E_project-E_Shmakov equals -p at p=3,5,7"
        ),
    }


def _verify_inventory(inventory: Mapping[str, object]) -> None:
    ambient = inventory.get("ambient_inventory")
    if not isinstance(ambient, dict):
        raise TypeError("Sym12 ambient inventory is missing")
    expected = "Tr(F_q,e_c(A_2(w^1),V_(12,0)))=Hhat_12+2-5*q-q*Theta_(14,Gamma0(2))(q)"
    if ambient.get("formula") != expected:
        raise ValueError("locked Sym12 ambient formula changed")


def _source_manifest(
    transitive: Mapping[str, list[dict[str, object]]], guard: ResourceGuard
) -> list[dict[str, object]]:
    rows = []
    for lock in SOURCE_LOCKS:
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source manifest path is invalid")
        source_id = lock["id"]
        if not isinstance(source_id, str):
            raise TypeError("source manifest id is invalid")
        rows.append(
            {
                "id": source_id,
                "path": _relative(path),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "sha256_lf_normalized": lock["lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "schema": lock["schema"],
                "role": lock["role"],
                "bytes_read": path.stat().st_size,
                "transitive_packet_files": transitive[source_id],
            }
        )
    marked_path = MARKED_ZERO_LOCK["path"]
    if not isinstance(marked_path, Path):
        raise TypeError("marked-zero source manifest path is invalid")
    rows.append(
        {
            "id": MARKED_ZERO_LOCK["id"],
            "path": _relative(marked_path),
            "commit": MARKED_ZERO_LOCK["commit"],
            "git_blob": MARKED_ZERO_LOCK["git_blob"],
            "raw_worktree_blob": MARKED_ZERO_LOCK["raw_worktree_blob"],
            "sha256_lf_normalized": MARKED_ZERO_LOCK["lf_sha256"],
            "role": MARKED_ZERO_LOCK["role"],
            "bytes_read": marked_path.stat().st_size,
            "content_kind": "EXACT_RAW_FIXTURE_WITH_COMMIT_AND_DUAL_HASH_LOCK",
            "transitive_packet_files": [],
        }
    )
    total = sum(
        row["bytes_read"]
        + sum(item["bytes_read"] for item in row["transitive_packet_files"])
        for row in rows
    )
    if total != guard.source_bytes:
        raise ArithmeticError("source-byte ledger mismatch")
    return rows


def _packet_manifest() -> list[dict[str, str]]:
    return [
        {
            "path": _relative(path),
            "sha256_lf_normalized": _lf_sha256(path.read_bytes()),
        }
        for path in (NOTE_PATH, ADAPTER_NOTE_PATH, SCRIPT_PATH, TEST_PATH)
    ]


def _resource_contract(guard: ResourceGuard) -> dict[str, object]:
    fields = (
        ("source_files", MAX_SOURCE_FILES),
        ("branching_partitions", MAX_BRANCHING_PARTITIONS),
        ("branching_row_tests", MAX_BRANCHING_ROW_TESTS),
        ("removable_corners", MAX_REMOVABLE_CORNERS),
        ("endoscopic_projection_terms", MAX_ENDOSCOPIC_PROJECTION_TERMS),
        ("hook_boxes", MAX_HOOK_BOXES),
        ("symbolic_component_operations", MAX_SYMBOLIC_COMPONENT_OPERATIONS),
        ("finite_corroboration_rows", MAX_FINITE_CORROBORATION_ROWS),
    )
    result: dict[str, object] = {
        name: {"maximum": maximum, "actual": getattr(guard, name)}
        for name, maximum in fields
    }
    result.update(
        {
            "source_bytes": {
                "maximum_each": MAX_SOURCE_BYTES_EACH,
                "maximum_total": MAX_SOURCE_BYTES_TOTAL,
                "actual_total": guard.source_bytes,
            },
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact finite integer and free-module algebra",
            "runtime_web_or_database_calls": "FORBIDDEN_AND_NOT_PERFORMED",
            "field_polynomial_curve_enumeration": "FORBIDDEN_AND_NOT_PERFORMED",
            "numeric_fitting": "NONE",
        }
    )
    return result


def build_fixture() -> dict[str, object]:
    deadline = Deadline.start()
    guard = ResourceGuard()
    inventory, inventory_transitive = _load_locked_packet(SOURCE_LOCKS[0], guard)
    scout, scout_transitive = _load_locked_packet(SOURCE_LOCKS[1], guard)
    marked = _load_marked_zero(guard)
    _verify_inventory(inventory)
    deadline.check("locked packets")

    branching = _branching_certificate(guard)
    endoscopy = _endoscopic_specialization(branching, guard)
    eisenstein = _eisenstein_specialization()
    stable = _stable_vanishing_certificate(branching, marked, guard)
    algebra = _conditional_algebra(guard)
    finite = _finite_corroboration(scout, guard)
    deadline.check("conditional reduction")

    transitive = {
        "sym12_inventory": inventory_transitive,
        "sym12_finite_scout": scout_transitive,
    }
    payload: dict[str, object] = {
        "schema": (
            "riemann.function_field.genus2_sym12_conditional_endoscopic_closure.v2"
        ),
        "status": "EXACT_STABLE_CHANNEL_CLOSURE_ONE_EISENSTEIN_GATE_NOT_ALL_Q",
        "conditional_statement": {
            "master_reduction": (
                "Hhat_12=-L*f_minus+Epsilon_Eis-Genuine, where "
                "Epsilon_Eis=e_Eis-(2-5*L) and the stable/general Euler "
                "contribution is -Genuine"
            ),
            "premises": [
                "Use the semisimplified inner/endoscopic specialization -L*(f_plus+2*f_minus).",
                (
                    "Use the exact marked modular zero and the theorem-grade "
                    "form-to-stable adapter, which give Genuine=0."
                ),
                "Adopt the conjectural nonregular compact-support Eisenstein continuation 2-5*L.",
            ],
            "unresolved_premises": [
                "Epsilon_Eis=0 (the BFG nonregular Eisenstein continuation).",
            ],
            "exact_stable_closure": (
                "Genuine=(S_gen,Gamma(2)[12,3])^S5=0; hence the master "
                "reduction simplifies to Hhat_12=-L*f_minus+Epsilon_Eis."
            ),
            "exact_conclusion": (
                "After the exact stable closure, the project ambient formula equals "
                "the theorem-supported cohomological target if and only if "
                "Hhat_12=-L*f_minus+Epsilon_Eis; imposing the one remaining BFG "
                "Eisenstein premise gives Hhat_12=-L*f_minus."
            ),
            "unconditional_conclusion": (
                "The positive semisimplified S5-fixed stable/general channel Genuine "
                "vanishes; no conclusion is made here about Epsilon_Eis."
            ),
        },
        "prime_power_trace_convention": (
            "For q=p^r, -L*f_minus means -p^r*(alpha_{-,p}^r+beta_{-,p}^r) "
            "at the level of Frobenius-root power sums, not -p^r times a naive "
            "composite-index Fourier coefficient. Epsilon_Eis and Genuine are "
            "likewise evaluated by Tr(F_p^r,-)."
        ),
        "source_manifest": _source_manifest(transitive, guard),
        "S6_to_S5_branching": branching,
        "BFG_endoscopic_specialization": endoscopy,
        "nonregular_Eisenstein_specialization": eisenstein,
        "stable_invariant_vanishing_certificate": stable,
        "exact_internal_algebra": algebra,
        "finite_scout_corroboration": finite,
        "source_grade_ledger": [
            {
                "claim": "S6-to-S5 invariant branching and formal channel algebra",
                "grade": "EXACT_INTERNAL",
            },
            {
                "claim": "semisimplified inner/endoscopic mechanism",
                "grade": "THEOREM_SUPPORTED_BY_ROESNER_AND_SHMAKOV",
                "boundary": (
                    "this does not prove the nonregular compact-support Eisenstein term"
                ),
            },
            {
                "claim": "BFG specialization of Conjecture 8.1",
                "grade": "CONJECTURAL_IN_BFG_BUT_ENDOSCOPICALLY_THEOREM_SUPPORTED",
            },
            {
                "claim": "nonregular Eisenstein value 2-5*L",
                "grade": "CONJECTURAL_CONTINUATION_WITH_UNRESOLVED_ONE_TATE_DISCREPANCY",
            },
            {
                "claim": "S_(12,3)(Gamma_2(w^1)) S5-invariant vanishing",
                "grade": "EXACT_CORRECTED_MARKED_VALUATION_CERTIFICATE",
            },
            {
                "claim": "Genuine=(S_gen,Gamma(2)[12,3])^S5=0",
                "grade": "THEOREM_GRADE_FORM_ATTACHED_STABLE_ADAPTER",
                "boundary": (
                    "semisimplified stable/general channel only; Eisenstein and "
                    "nonsemisimple boundary extensions are separate"
                ),
            },
            {
                "claim": "Hhat_12=-L*f_minus+Epsilon_Eis-Genuine",
                "grade": "EXACT_MASTER_REDUCTION_GIVEN_THE_THEOREM_SUPPORTED_ENDOSCOPIC_CHANNEL",
            },
            {
                "claim": "Hhat_12=-L*f_minus",
                "grade": "EXACT_IFF_UNDER_ALL_LISTED_PREMISES_ONLY",
            },
            {
                "claim": "the p=3,5,7 Hhat_12 rows",
                "grade": "EXACT_CONSEQUENCES_OF_DIRECT_RAW_T12_PLUS_THE_LOCKED_INVENTORY",
                "boundary": (
                    "not a direct central-Q_5 enumeration and not an independent "
                    "audit of the arithmetic inventory"
                ),
            },
        ],
        "literature_ledger": [
            {
                "source": "Bergstrom--Faber--van der Geer 2008",
                "url": "https://arxiv.org/abs/0803.0917",
                "use": (
                    "Conjecture 8.1 endoscopy and explicitly expected, not proved, "
                    "nonregular Eisenstein continuation"
                ),
            },
            {
                "source": "Roesner dissertation, Theorem 5.13, pp. 97-98",
                "url": (
                    "https://sites.math.unt.edu/~schmidt/dimension_formulas/"
                    "papers/2016_Dissertation_Roesner_final.pdf"
                ),
                "use": (
                    "semisimplified endoscopy and, via pp. 95-99 and Corollary "
                    "5.20, the arbitrary-weight stable direct sum and its "
                    "holomorphic companion"
                ),
            },
            {
                "source": "Shmakov dissertation, Theorem 4.6.4, p. 366",
                "url": "https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf",
                "use": (
                    "inner/endoscopic theorem support; later printed Eisenstein formulas "
                    "also expose the unresolved 2-4*L versus 2-5*L discrepancy"
                ),
            },
            {
                "source": "Bergstrom--Clery, arXiv:2309.04388v2",
                "url": "https://arxiv.org/abs/2309.04388",
                "use": (
                    "Arthur decomposition S=S^(G) direct_sum S^(Y), exact odd-k "
                    "cuspidality, and the boundary between structural form-attached "
                    "channels and the conditional k=3 isotypical formula"
                ),
            },
            {
                "source": "Clery--van der Geer, arXiv:2605.13300",
                "url": "https://arxiv.org/abs/2605.13300",
                "use": (
                    "structural identification A2[w]=A2[2]/S5 and the "
                    "covariant/valuation criterion used by the locked corrected "
                    "(j,k)=(12,3) rank certificate"
                ),
            },
        ],
        "firewalls": [
            "CONDITIONAL-REDUCTION FIREWALL: Genuine=0 is closed exactly, but the final Hhat_12=-L*f_minus identity still requires the displayed nonregular Eisenstein premise; it is not an all-q theorem.",
            "NONREGULAR FIREWALL: BFG proves the Eisenstein formula in the regular range and only expects the m=0 continuation used here.",
            "ONE-TATE FIREWALL: Shmakov's printed 2-4*L specialization differs from BFG's formal 2-5*L by one Tate term and changes the master relation to Hhat_12=L-L*f_minus-Genuine; only after Genuine=0 does this become Hhat_12=L-L*f_minus.",
            "AMBIENT-NORMALIZATION FIREWALL: the project and both cited specializations use the same ambient A_2(w^1)=A_2[2]/S5; no open/ambient correction resolving the discrepancy has been identified.",
            "STABLE-SPACE CLOSURE: the locked corrected two-orientation valuation kernel proves the full marked modular space zero, and the form-attached stable adapter therefore gives Genuine=0 without the conditional k=3 isotypical rows.",
            "DIMENSION FIREWALL: the full-level dimension 30 alone does not imply absence of S5 invariants; the conclusion instead uses the exact marked rank-66/nullity-zero kernel.",
            "COHOMOLOGY FIREWALL: Genuine is the positive semisimplified stable/general form-attached channel, not an arbitrary residual Euler class; boundary, Eisenstein, endoscopic, and nonsemisimple extension data cannot be absorbed into it.",
            "FINITE-SCOUT PROVENANCE FIREWALL: p=3,5,7 directly replay T_(12,0); Hhat_12 is then derived with the separately locked arithmetic inventory. The rows give an exact -p raw-T residual against the Shmakov branch, but they are not an independent audit of the inventory and do not prove any fourth q or prime-power row.",
            "No motivic isomorphism, compatible system, novelty, RH, GRH, number-field transfer, or global Euler-product claim is made.",
            "The producer performs no runtime web/database call and no field, polynomial, curve, or family enumeration.",
        ],
        "resource_contract": _resource_contract(guard),
        "packet_manifest": _packet_manifest(),
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
