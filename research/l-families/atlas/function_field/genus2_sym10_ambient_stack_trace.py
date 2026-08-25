#!/usr/bin/env python3
"""Bounded exact replay for the marked genus-two Sym^10 ambient trace.

The proof combines the source-locked all-q curve-open theorem with an
independently rebuilt decomposable-boundary calculation in the exact ring
Z[L, Delta, f_(8,2), g_(10,2)].  The computation verifies the Sym^10
branching rule, elliptic compact-support formulas, level-two old/new
dimensions, modular q-expansions, and q=3,5,7,9 controls.  It performs no
finite-field, curve, abelian-surface, or cohomology enumeration.

Conjectural BFG formulas are recorded only as compatibility context.  They
are never passed to the exact proof builder.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "genus2_sym10_ambient_stack_trace.json"
NOTE_PATH = HERE / "GENUS2_SYM10_AMBIENT_STACK_TRACE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym10_ambient_stack_trace.py"

SYM10_JSON_PATH = HERE / "genus2_sym10_marked_trace_average.json"
SYM10_PRODUCER_PATH = HERE / "genus2_sym10_marked_trace_average.py"
SYM10_NOTE_PATH = HERE / "GENUS2_SYM10_MARKED_TRACE_AVERAGE.md"
SYM10_TEST_PATH = ROOT / "tests" / "test_genus2_sym10_marked_trace_average.py"

CHI04_JSON_PATH = HERE / "genus2_chi04_stack_trace_reconciliation.json"
CHI04_PRODUCER_PATH = HERE / "genus2_chi04_stack_trace_reconciliation.py"
CHI04_NOTE_PATH = HERE.parent / "GENUS2_CHI04_STACK_TRACE_RECONCILIATION.md"
CHI04_TEST_PATH = ROOT / "tests" / "test_genus2_chi04_stack_trace_reconciliation.py"

ADAPTER_JSON_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
ADAPTER_PRODUCER_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.py"
ADAPTER_NOTE_PATH = HERE / "GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md"
ADAPTER_TEST_PATH = ROOT / "tests" / "test_genus2_marked_weierstrass_stack_adapter.py"

MAX_EXACT_OPERATIONS = 20_000
MAX_SOURCE_FILES = 12
MAX_SOURCE_BYTES_EACH = 65_536
MAX_SOURCE_BYTES_TOTAL = 262_144
MAX_PACKET_FILE_BYTES = 65_536
MAX_WALL_SECONDS = 5.0
Q_SERIES_DEGREE = 9


SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "sym10_producer": {
        "path": SYM10_PRODUCER_PATH,
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "bcf8e4786609d196f88b2ce5fe8cd824b985f5fa",
        "lf_sha256": "f80efb55d16ff654b528d09d6f5c935c1640e1606d1aaa45f165280a05185e10",
        "role": "source-locked direct all-q proof producer",
    },
    "sym10_json": {
        "path": SYM10_JSON_PATH,
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "561caa7dc504dfb158908aef9229e91af0707a1e",
        "lf_sha256": "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce",
        "schema": "riemann.genus2_sym10_marked_trace_average.v1",
        "payload_sha256": "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77",
        "role": "source-locked direct all-q curve-open theorem",
    },
    "sym10_note": {
        "path": SYM10_NOTE_PATH,
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "96dffb56bb72ad4bf67094f2ce1f4d52875baab4",
        "lf_sha256": "f88200422627696710493b91fe0d8f22d9793f8f19d4d56fb47169756a8c39e7",
        "role": "source theorem statement and proof narrative",
    },
    "sym10_test": {
        "path": SYM10_TEST_PATH,
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "c11c83568b2eb47af76d4463eae9b1e26d9f4804",
        "lf_sha256": "31cea2f7a8a817b99c2a710b9355599ad5b3129e5803dd226deb283dfde52752",
        "role": "source theorem focused replay tests",
    },
    "chi04_producer": {
        "path": CHI04_PRODUCER_PATH,
        "commit": "e0da0f790f96f6dc5c03b363a9a01b91621ee113",
        "git_blob": "7f1f838bf0095eec15f771e377aa7739421096d1",
        "lf_sha256": "fd365f153ba7f2d9fef8c6f2f45dd5cd7c83c552f2934804c1843e0f4cbaed12",
        "role": "exact decomposable-geometry reconciliation producer",
    },
    "chi04_json": {
        "path": CHI04_JSON_PATH,
        "commit": "e0da0f790f96f6dc5c03b363a9a01b91621ee113",
        "git_blob": "9160b9a95efec4f0ed7a895b507d13d97158d714",
        "lf_sha256": "7338bb846308b685fc0124ba3f8da80e5fe368360aa79efff97754ad3c200c2b",
        "schema": "riemann.function_field.genus2_chi04_stack_trace_reconciliation.v1",
        "payload_sha256": "b87733cdf4f5532fcc0a74313d79f4d5ee3f056b55c9bab953ef40c3e01a5762",
        "role": "source-locked exact geometry and source ledger",
    },
    "chi04_note": {
        "path": CHI04_NOTE_PATH,
        "commit": "e0da0f790f96f6dc5c03b363a9a01b91621ee113",
        "git_blob": "fdb9349bab8ceed59362f4e983831c5f58f5ad6d",
        "lf_sha256": "89911841fda964987d44b9d3cc6189fa182b8f6946785a29b1217046b2b9012a",
        "role": "marked-boundary geometry and literature audit",
    },
    "chi04_test": {
        "path": CHI04_TEST_PATH,
        "commit": "e0da0f790f96f6dc5c03b363a9a01b91621ee113",
        "git_blob": "a554102d6b5ac6b89b3c573718deb89c2dddb2b0",
        "lf_sha256": "739a221be32f801d014d0c7183686d9db5e34d0cbf8cb8b0fbbcaf32210e6b4f",
        "role": "marked-boundary reconciliation tests",
    },
    "adapter_producer": {
        "path": ADAPTER_PRODUCER_PATH,
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        "git_blob": "db364b5300a09c81065ff96c874bf3d4adca3b46",
        "lf_sha256": "29c8084dafb15acdc4d1eb55ed21ac9ad4a8abfb7f1e0d208d93df2671142cc9",
        "role": "exact marked-Weierstrass stack adapter producer",
    },
    "adapter_json": {
        "path": ADAPTER_JSON_PATH,
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        "git_blob": "79ad36346734bb41f21b570f380ad9d1af86f9ee",
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "role": "exact marked stack measure and trace meaning",
    },
    "adapter_note": {
        "path": ADAPTER_NOTE_PATH,
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        "git_blob": "147c4e57b060e33115761b9685bc0b2ef8b1f5bc",
        "lf_sha256": "f6f3c5ff0d112bd3204b1843a6f13b286d642a9c6ee19329a63eb39e06165e1c",
        "role": "marked stack proof narrative",
    },
    "adapter_test": {
        "path": ADAPTER_TEST_PATH,
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        "git_blob": "45ac7cad100840202c53a8e15d39a3cd45f10d7f",
        "lf_sha256": "fd5be2c3d7dfc3cc427e6caa6a6a0c8db09a8da237e45c6b17cacc04267292d6",
        "role": "marked stack adapter tests",
    },
}


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    source_files: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def source(self, byte_count: int) -> None:
        if byte_count < 0:
            raise ValueError("source size must be nonnegative")
        if byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + byte_count > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += byte_count


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    header = f"blob {len(normalized)}\0".encode("ascii")
    return hashlib.sha1(header + normalized).hexdigest()


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, tuple):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _read_locked_sources(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    parsed: dict[str, dict[str, object]] = {}
    manifest: list[dict[str, object]] = []
    for name, lock in SOURCE_LOCKS.items():
        deadline.check(f"before source {name}")
        path = lock.get("path")
        if not isinstance(path, Path):
            raise TypeError(f"source path is not a Path: {name}")
        size = path.stat().st_size
        guard.source(size)
        raw = path.read_bytes()
        if len(raw) != size:
            raise RuntimeError(f"source size changed while reading: {name}")
        if _lf_sha256_bytes(raw) != lock.get("lf_sha256"):
            raise RuntimeError(f"source LF hash mismatch: {name}")
        if _git_blob_sha1(raw) != lock.get("git_blob"):
            raise RuntimeError(f"source git-blob mismatch: {name}")
        row = {
            "id": name,
            "path": _relative(path),
            "commit": lock["commit"],
            "git_blob": lock["git_blob"],
            "lf_sha256": lock["lf_sha256"],
            "bytes": size,
            "role": lock["role"],
        }
        if path.suffix == ".json":
            value = json.loads(raw.decode("utf-8"))
            if not isinstance(value, dict):
                raise TypeError(f"source JSON is not an object: {name}")
            if value.get("schema") != lock.get("schema"):
                raise RuntimeError(f"source schema mismatch: {name}")
            payload = dict(value)
            claimed = payload.pop("payload_sha256", None)
            if claimed != lock.get("payload_sha256"):
                raise RuntimeError(f"source pinned payload mismatch: {name}")
            if claimed != _canonical_sha256(payload):
                raise RuntimeError(f"source internal payload mismatch: {name}")
            parsed[name] = value
            row["schema"] = lock["schema"]
            row["payload_sha256"] = lock["payload_sha256"]
        manifest.append(row)
        deadline.check(f"after source {name}")
    if guard.source_files != len(SOURCE_LOCKS):
        raise RuntimeError("not every source lock was consumed")
    return parsed, manifest


@dataclass(frozen=True)
class ExactInputs:
    open_trace_formula: str
    geometry: str
    stack_trace_meaning: str
    sym10_controls: tuple[tuple[int, int], ...]
    q9_open_trace: int


def _validate_exact_inputs(sources: Mapping[str, Mapping[str, object]]) -> ExactInputs:
    sym10 = sources.get("sym10_json")
    chi04 = sources.get("chi04_json")
    adapter = sources.get("adapter_json")
    if not isinstance(sym10, Mapping) or not isinstance(chi04, Mapping):
        raise TypeError("source-locked theorem or boundary packet is missing")
    if not isinstance(adapter, Mapping):
        raise TypeError("source-locked marked-stack adapter is missing")
    if sym10.get("status") != "PROVED_ALL_ODD_PRIME_POWERS":
        raise RuntimeError("Sym10 source theorem status changed")
    theorem = sym10.get("theorem")
    if not isinstance(theorem, Mapping):
        raise TypeError("Sym10 theorem block is missing")
    formula = theorem.get("marked_stack_trace")
    expected_formula = (
        "T_(10,0)(q)=(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7"
    )
    if formula != expected_formula:
        raise RuntimeError("Sym10 open-trace formula changed")
    scope = sym10.get("scope")
    if not isinstance(scope, Mapping) or scope.get("proved_q") != (
        "every odd prime power"
    ):
        raise RuntimeError("Sym10 all-field scope changed")

    exact_boundary = chi04.get("exact_decomposable_boundary")
    if not isinstance(exact_boundary, Mapping):
        raise TypeError("exact decomposable-boundary block is missing")
    geometry = exact_boundary.get("geometry")
    if geometry != "A_(1,1)(w^1) is Y_0(2) times A_1":
        raise RuntimeError("marked decomposable geometry changed")
    moduli = chi04.get("moduli_firewall")
    if not isinstance(moduli, Mapping) or "decomposable locus" not in str(
        moduli.get("A_2(w^1)")
    ):
        raise RuntimeError("ambient marked-stack firewall changed")

    trace_theorem = adapter.get("trace_theorem")
    if not isinstance(trace_theorem, Mapping):
        raise TypeError("adapter trace theorem is missing")
    meaning = trace_theorem.get("meaning_of_stack_trace")
    if not isinstance(meaning, str) or "compactly-supported" not in meaning:
        raise RuntimeError("marked stack trace meaning changed")
    controls_raw = sym10.get("held_out_falsification_controls")
    modular = sym10.get("modular_form_certificate")
    if not isinstance(controls_raw, list) or not isinstance(modular, Mapping):
        raise TypeError("Sym10 controls are missing")
    controls: list[tuple[int, int]] = []
    for row in controls_raw:
        if not isinstance(row, Mapping):
            raise TypeError("Sym10 control row is malformed")
        controls.append((int(row["q"]), int(row["theorem_T_(10,0)"])))
    q9 = modular.get("q_9")
    if not isinstance(q9, Mapping):
        raise TypeError("Sym10 q=9 control is missing")
    return ExactInputs(
        open_trace_formula=expected_formula,
        geometry=str(geometry),
        stack_trace_meaning=meaning,
        sym10_controls=tuple(controls),
        q9_open_trace=int(q9["T_(10,0)(9)"]),
    )


Laurent = dict[tuple[int, int], int]


def _compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    if total < 0 or parts < 1:
        raise ValueError("invalid composition request")
    if parts == 1:
        return [(total,)]
    result: list[tuple[int, ...]] = []
    for first in range(total + 1):
        for tail in _compositions(total - first, parts - 1):
            result.append((first, *tail))
    return result


def _verify_sym10_branching(guard: ResourceGuard) -> dict[str, object]:
    direct: Laurent = {}
    for a, b, c, d in _compositions(10, 4):
        guard.operation("sym10_direct_monomials")
        exponent = (a - b, c - d)
        direct[exponent] = direct.get(exponent, 0) + 1
    branch: Laurent = {}
    dimensions: list[int] = []
    for degree in range(11):
        left_weights = range(degree, -degree - 1, -2)
        right_degree = 10 - degree
        right_weights = range(right_degree, -right_degree - 1, -2)
        dimensions.append((degree + 1) * (right_degree + 1))
        for left in left_weights:
            for right in right_weights:
                guard.operation("sym10_branch_monomials")
                exponent = (left, right)
                branch[exponent] = branch.get(exponent, 0) + 1
    if direct != branch:
        raise ArithmeticError("Sym10 Laurent-character branching failed")
    if sum(direct.values()) != math.comb(13, 10):
        raise ArithmeticError("direct Sym10 dimension failed")
    if sum(dimensions) != 286:
        raise ArithmeticError("branched Sym10 dimensions failed")
    return {
        "identity": (
            "Sym^10(W_1 direct_sum W_1)="
            "direct_sum_(i=0)^10 W_i external_tensor W_(10-i)"
        ),
        "verification_ring": "Z[x^+-1,y^+-1]",
        "direct_composition_monomials": math.comb(13, 10),
        "distinct_laurent_weights": len(direct),
        "summand_dimensions": dimensions,
        "total_dimension": 286,
    }


def _dim_m_level1(weight: int) -> int:
    if weight < 0 or weight % 2:
        return 0
    return sum(
        1
        for e4 in range(weight // 4 + 1)
        for e6 in range(weight // 6 + 1)
        if 4 * e4 + 6 * e6 == weight
    )


def _dim_s_level1(weight: int) -> int:
    return _dim_m_level1(weight - 12) if weight >= 12 else 0


def _dim_m_level2(weight: int) -> int:
    if weight < 0 or weight % 2:
        return 0
    return weight // 4 + 1


def _dim_s_level2(weight: int) -> int:
    if weight < 4 or weight % 2:
        return 0
    return _dim_m_level2(weight) - 2


def _verify_modular_dimensions(guard: ResourceGuard) -> dict[str, object]:
    rows: list[dict[str, int]] = []
    expected = {
        4: (0, 0, 0, 0),
        6: (0, 0, 0, 0),
        8: (0, 1, 0, 1),
        10: (0, 1, 0, 1),
        12: (1, 2, 2, 0),
    }
    for weight, wanted in expected.items():
        guard.operation("modular_dimension_rows", 4)
        level1 = _dim_s_level1(weight)
        level2 = _dim_s_level2(weight)
        old = 2 * level1
        new = level2 - old
        actual = (level1, level2, old, new)
        if actual != wanted:
            raise ArithmeticError(f"modular dimension mismatch at weight {weight}")
        rows.append(
            {
                "weight": weight,
                "dim_S_level_1": level1,
                "dim_S_Gamma0_2": level2,
                "dim_old_Gamma0_2": old,
                "dim_new_Gamma0_2": new,
            }
        )
    return {
        "level_1_ring": "M_*(SL_2(Z))=C[E_4,E_6]",
        "level_2_dimension_rule": ("dim M_k(Gamma_0(2))=floor(k/4)+1 for even k"),
        "two_rational_cusps": ["0", "infinity"],
        "oldspace_rule_at_level_2": (
            "two degeneracy images f(z),f(2z) for each level-one cusp form"
        ),
        "rows": rows,
        "identifications": {
            "weight_8_new": "f_(8,2)=eta(z)^8*eta(2z)^8",
            "weight_10_new": ("g_(10,2)=f_(8,2)*(2*E_2(2z)-E_2(z))"),
            "weight_12_old": "Delta(z) direct_sum Delta(2z)",
            "weight_12_new_dimension": 0,
        },
    }


Series = list[int]


def _series_mul(
    left: Sequence[int], right: Sequence[int], guard: ResourceGuard
) -> Series:
    result = [0] * (Q_SERIES_DEGREE + 1)
    for left_degree, left_value in enumerate(left):
        if not left_value:
            continue
        for right_degree, right_value in enumerate(right):
            if left_degree + right_degree > Q_SERIES_DEGREE:
                break
            if right_value:
                guard.operation("q_series_multiply")
                result[left_degree + right_degree] += left_value * right_value
    return result


def _one_minus_qn_power(n: int, exponent: int) -> Series:
    result = [0] * (Q_SERIES_DEGREE + 1)
    for power in range(exponent + 1):
        degree = n * power
        if degree > Q_SERIES_DEGREE:
            break
        result[degree] = (-1) ** power * math.comb(exponent, power)
    return result


def _eta_product(
    exponents: Mapping[int, int], shift: int, guard: ResourceGuard
) -> Series:
    product = [1] + [0] * Q_SERIES_DEGREE
    for multiplier, exponent in sorted(exponents.items()):
        for n in range(1, Q_SERIES_DEGREE + 1):
            degree = multiplier * n
            if degree > Q_SERIES_DEGREE:
                break
            product = _series_mul(product, _one_minus_qn_power(degree, exponent), guard)
    return [0] * shift + product[: Q_SERIES_DEGREE + 1 - shift]


def _sigma_one(n: int) -> int:
    return sum(divisor for divisor in range(1, n + 1) if n % divisor == 0)


def _verify_modular_q_series(guard: ResourceGuard) -> dict[str, object]:
    delta = _eta_product({1: 24}, 1, guard)
    f8 = _eta_product({1: 8, 2: 8}, 1, guard)
    e2 = [1] + [-24 * _sigma_one(n) for n in range(1, Q_SERIES_DEGREE + 1)]
    e2_at_2 = [e2[n // 2] if n % 2 == 0 else 0 for n in range(10)]
    weight2 = [2 * e2_at_2[n] - e2[n] for n in range(10)]
    g10 = _series_mul(f8, weight2, guard)
    expected = {
        "Delta": [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643],
        "f_(8,2)": [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043],
        "g_(10,2)": [0, 1, 16, -156, 256, 870, -2496, -952, 4096, 4653],
    }
    actual = {"Delta": delta, "f_(8,2)": f8, "g_(10,2)": g10}
    if actual != expected:
        raise ArithmeticError("modular q-expansion certificate failed")
    return {
        "degree_cap": Q_SERIES_DEGREE,
        "construction": {
            "Delta": "q*product_(n>=1)(1-q^n)^24",
            "f_(8,2)": "q*product_(n>=1)(1-q^n)^8*(1-q^(2n))^8",
            "g_(10,2)": "f_(8,2)*(2*E_2(2z)-E_2(z))",
        },
        "coefficients_0_through_9": actual,
    }


Monomial = tuple[int, int, int, int]  # L, Delta, f8, g10 exponents
Expression = dict[Monomial, int]


def _expr_term(
    coefficient: int,
    *,
    l_power: int = 0,
    delta_power: int = 0,
    f8_power: int = 0,
    g10_power: int = 0,
) -> Expression:
    if coefficient == 0:
        return {}
    if min(l_power, delta_power, f8_power, g10_power) < 0:
        raise ValueError("negative formal exponent")
    return {(l_power, delta_power, f8_power, g10_power): coefficient}


def _expr_add(
    left: Mapping[Monomial, int],
    right: Mapping[Monomial, int],
    guard: ResourceGuard,
) -> Expression:
    result = dict(left)
    for monomial, coefficient in right.items():
        guard.operation("formal_ring_add")
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def _expr_scale(
    value: Mapping[Monomial, int], coefficient: int, guard: ResourceGuard
) -> Expression:
    guard.operation("formal_ring_scale", len(value))
    return {
        monomial: coefficient * value_coefficient
        for monomial, value_coefficient in value.items()
        if coefficient * value_coefficient
    }


def _expr_mul(
    left: Mapping[Monomial, int],
    right: Mapping[Monomial, int],
    guard: ResourceGuard,
) -> Expression:
    result: Expression = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            guard.operation("formal_ring_multiply")
            monomial = tuple(
                left_monomial[index] + right_monomial[index] for index in range(4)
            )
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
            if result[monomial] == 0:
                del result[monomial]
    return result


def _expr_sum(values: Sequence[Expression], guard: ResourceGuard) -> Expression:
    result: Expression = {}
    for value in values:
        result = _expr_add(result, value, guard)
    return result


def _expr_json(value: Mapping[Monomial, int]) -> list[dict[str, int]]:
    return [
        {
            "L_power": monomial[0],
            "Delta_power": monomial[1],
            "f_(8,2)_power": monomial[2],
            "g_(10,2)_power": monomial[3],
            "coefficient": value[monomial],
        }
        for monomial in sorted(value)
    ]


ONE = _expr_term(1)
L = _expr_term(1, l_power=1)
DELTA = _expr_term(1, delta_power=1)
F8 = _expr_term(1, f8_power=1)
G10 = _expr_term(1, g10_power=1)


def _level1_cusp_class(weight: int) -> Expression:
    dimension = _dim_s_level1(weight)
    if weight == 12 and dimension == 1:
        return dict(DELTA)
    if dimension == 0:
        return {}
    raise ArithmeticError(f"unsupported level-one cusp class at weight {weight}")


def _level2_cusp_class(weight: int, guard: ResourceGuard) -> Expression:
    if weight == 8 and _dim_s_level2(weight) == 1:
        return dict(F8)
    if weight == 10 and _dim_s_level2(weight) == 1:
        return dict(G10)
    if weight == 12 and _dim_s_level2(weight) == 2:
        return _expr_scale(DELTA, 2, guard)
    if _dim_s_level2(weight) == 0:
        return {}
    raise ArithmeticError(f"unsupported level-two cusp class at weight {weight}")


def _a1_euler(degree: int, guard: ResourceGuard) -> Expression:
    if degree < 0:
        raise ValueError("negative local-system degree")
    if degree == 0:
        return dict(L)
    if degree % 2:
        return {}
    return _expr_add(
        _expr_scale(_level1_cusp_class(degree + 2), -1, guard),
        _expr_term(-1),
        guard,
    )


def _y02_euler(degree: int, guard: ResourceGuard) -> Expression:
    if degree < 0:
        raise ValueError("negative local-system degree")
    if degree == 0:
        return _expr_add(L, _expr_term(-1), guard)
    if degree % 2:
        return {}
    return _expr_add(
        _expr_scale(_level2_cusp_class(degree + 2, guard), -1, guard),
        _expr_term(-2),
        guard,
    )


def _build_boundary(guard: ResourceGuard) -> dict[str, object]:
    contributions: list[Expression] = []
    rows: list[dict[str, object]] = []
    for degree in range(11):
        y_value = _y02_euler(degree, guard)
        a_value = _a1_euler(10 - degree, guard)
        contribution = _expr_mul(y_value, a_value, guard)
        contributions.append(contribution)
        rows.append(
            {
                "i": degree,
                "Y_0(2)_W_i": _expr_json(y_value),
                "A_1_W_(10-i)": _expr_json(a_value),
                "contribution": _expr_json(contribution),
                "vanishes_by_unmarked_central_involution": bool(degree % 2),
            }
        )
    boundary = _expr_sum(contributions, guard)
    expected_boundary = _expr_sum(
        [
            _expr_term(1, delta_power=1),
            _expr_term(-3, l_power=1, delta_power=1),
            F8,
            G10,
            _expr_term(-3, l_power=1),
            _expr_term(9),
        ],
        guard,
    )
    if boundary != expected_boundary:
        raise ArithmeticError("exact decomposable-boundary sum failed")

    expected_even = {
        0: _expr_sum(
            [
                _expr_term(-1, l_power=1, delta_power=1),
                DELTA,
                _expr_term(-1, l_power=1),
                ONE,
            ],
            guard,
        ),
        2: _expr_term(2),
        4: _expr_term(2),
        6: _expr_add(F8, _expr_term(2), guard),
        8: _expr_add(G10, _expr_term(2), guard),
        10: _expr_sum(
            [
                _expr_term(-2, l_power=1, delta_power=1),
                _expr_term(-2, l_power=1),
            ],
            guard,
        ),
    }
    for degree, expected in expected_even.items():
        if contributions[degree] != expected:
            raise ArithmeticError(f"boundary row i={degree} failed")
    if any(contributions[degree] for degree in (1, 3, 5, 7, 9)):
        raise ArithmeticError("odd boundary row did not vanish")
    return {
        "geometry": (
            "A_(1,1)(w^1)=Y_0(2) times A_1; the marked odd theta "
            "characteristic distinguishes the factors, so there is no S_2 quotient"
        ),
        "standard_eichler_shimura_inputs": {
            "A_1_W_0": "L",
            "A_1_W_r_even_positive": "-S[r+2]-1",
            "Y_0(2)_W_0": "L-1",
            "Y_0(2)_W_r_even_positive": "-S[Gamma_0(2),r+2]-2",
            "odd_degree": (
                "zero because [-1] acts nontrivially on the unmarked A_1 fibre"
            ),
            "derivation": (
                "X(1) and X_0(2) have genus zero and respectively one and "
                "two rational cusps; the cuspidal H^1 term is Eichler-Shimura"
            ),
        },
        "rows": rows,
        "boundary_expression": _expr_json(boundary),
        "boundary_formula": ("(1-3*L)*Delta+f_(8,2)+g_(10,2)-3*L+9"),
    }


def _prime_power_trace(coefficients: Sequence[int], weight: int, q: int) -> int:
    if q < 2:
        raise ValueError("q must be at least two")
    prime = next((p for p in range(2, q + 1) if q % p == 0), q)
    if any(prime % divisor == 0 for divisor in range(2, math.isqrt(prime) + 1)):
        raise ValueError("q base is not prime")
    exponent = 0
    residue = q
    while residue % prime == 0:
        residue //= prime
        exponent += 1
    if residue != 1:
        raise ValueError("q is not a prime power")
    if prime >= len(coefficients):
        raise ValueError("q-series certificate does not reach the prime base")
    trace_p = coefficients[prime]
    if exponent == 1:
        return trace_p
    previous_previous = 2
    previous = trace_p
    determinant = prime ** (weight - 1)
    for _ in range(2, exponent + 1):
        current = trace_p * previous - determinant * previous_previous
        previous_previous, previous = previous, current
    return previous


def _expr_evaluate(
    value: Mapping[Monomial, int],
    q: int,
    delta: int,
    f8: int,
    g10: int,
    guard: ResourceGuard,
) -> int:
    result = 0
    for monomial, coefficient in value.items():
        guard.operation("formal_trace_evaluation")
        result += (
            coefficient
            * q ** monomial[0]
            * delta ** monomial[1]
            * f8 ** monomial[2]
            * g10 ** monomial[3]
        )
    return result


def _build_exact_proof(
    inputs: ExactInputs, guard: ResourceGuard, deadline: Deadline
) -> dict[str, object]:
    branching = _verify_sym10_branching(guard)
    dimensions = _verify_modular_dimensions(guard)
    modular = _verify_modular_q_series(guard)
    boundary = _build_boundary(guard)
    deadline.check("after exact boundary")

    open_expression = _expr_sum(
        [
            _expr_term(1, l_power=1, delta_power=1),
            _expr_term(-1, delta_power=1),
            _expr_term(-1, f8_power=1),
            _expr_term(-1, g10_power=1),
            _expr_term(-1, l_power=1),
            _expr_term(-7),
        ],
        guard,
    )
    boundary_expression = _expr_sum(
        [
            _expr_term(1, delta_power=1),
            _expr_term(-3, l_power=1, delta_power=1),
            F8,
            G10,
            _expr_term(-3, l_power=1),
            _expr_term(9),
        ],
        guard,
    )
    ambient = _expr_add(open_expression, boundary_expression, guard)
    expected_ambient = _expr_sum(
        [
            _expr_term(2),
            _expr_term(-4, l_power=1),
            _expr_term(-2, l_power=1, delta_power=1),
        ],
        guard,
    )
    if ambient != expected_ambient:
        raise ArithmeticError("open-plus-boundary cancellation failed")

    series = modular["coefficients_0_through_9"]
    if not isinstance(series, Mapping):
        raise TypeError("modular series certificate is malformed")
    controls: list[dict[str, int | str]] = []
    source_open = dict(inputs.sym10_controls)
    source_open[9] = inputs.q9_open_trace
    expected_ambient_controls = {3: -1522, 5: -48318, 7: 234390, 9: 5234186}
    for q in (3, 5, 7, 9):
        delta_trace = _prime_power_trace(series["Delta"], 12, q)
        f8_trace = _prime_power_trace(series["f_(8,2)"], 8, q)
        g10_trace = _prime_power_trace(series["g_(10,2)"], 10, q)
        open_trace = _expr_evaluate(
            open_expression, q, delta_trace, f8_trace, g10_trace, guard
        )
        boundary_trace = _expr_evaluate(
            boundary_expression, q, delta_trace, f8_trace, g10_trace, guard
        )
        ambient_trace = _expr_evaluate(
            ambient, q, delta_trace, f8_trace, g10_trace, guard
        )
        direct_ambient = 2 - 4 * q - 2 * q * delta_trace
        if open_trace != source_open[q]:
            raise ArithmeticError(f"source open control failed at q={q}")
        if ambient_trace != direct_ambient:
            raise ArithmeticError(f"ambient formula failed at q={q}")
        if ambient_trace != expected_ambient_controls[q]:
            raise ArithmeticError(f"ambient numeric control failed at q={q}")
        controls.append(
            {
                "q": q,
                "Theta_Delta": delta_trace,
                "Theta_(8,2)": f8_trace,
                "Theta_(10,2)": g10_trace,
                "open_trace": open_trace,
                "boundary_trace": boundary_trace,
                "ambient_trace": ambient_trace,
                "status": (
                    "THEOREM_CONSEQUENCE; USES FROBENIUS-ROOT POWER SUM"
                    if q == 9
                    else "SOURCE_LOCKED_PRIME_CONTROL"
                ),
            }
        )
    deadline.check("after exact controls")
    return {
        "branching_certificate": branching,
        "modular_dimension_certificate": dimensions,
        "modular_q_series_certificate": modular,
        "decomposable_boundary": boundary,
        "curve_open_expression": _expr_json(open_expression),
        "curve_open_formula": ("(L-1)*Delta-f_(8,2)-g_(10,2)-L-7"),
        "ambient_expression": _expr_json(ambient),
        "ambient_trace_formula": "2-4*q-2*q*Theta_Delta(q)",
        "channel_cancellation": {
            "Theta_Delta": "(q-1)+(1-3q)=-2q",
            "Theta_(8,2)": "-1+1=0",
            "Theta_(10,2)": "-1+1=0",
            "Tate": "(-q-7)+(-3q+9)=2-4q",
        },
        "controls": controls,
    }


def _build_compatibility_context(
    sources: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    chi04 = sources["chi04_json"]
    block = chi04.get("BFG_conjectural_reconciliation")
    if not isinstance(block, Mapping):
        raise TypeError("BFG compatibility ledger is missing")
    logical_status = block.get("logical_status")
    if logical_status != (
        "CONJECTURAL_AMBIENT_PREDICTION_PLUS_EXACT_BOUNDARY; "
        "NOT_A_SOURCE_PROOF_OF_THE_TARGET"
    ):
        raise RuntimeError("BFG conjectural status label changed")
    return {
        "status": "CONJECTURAL_COMPATIBILITY_ONLY_UNUSED_BY_EXACT_PROOF",
        "source_ledger_status": logical_status,
        "statement": (
            "The level-two cohomological framework is compatible with the trace "
            "pattern, but its nonregular/endoscopic formulas are not inputs to "
            "the exact open-plus-boundary proof."
        ),
    }


def _build_primary_source_ledger(
    sources: Mapping[str, Mapping[str, object]],
) -> list[dict[str, object]]:
    """Reuse the source-locked manual ledger without making a network replay."""

    sym10_ledger = sources["sym10_json"].get("primary_source_ledger")
    chi04_ledger = sources["chi04_json"].get("literature_artifacts")
    if not isinstance(sym10_ledger, list) or not isinstance(chi04_ledger, list):
        raise TypeError("source-locked primary-source ledger is missing")

    def by_title(rows: Sequence[object], needle: str) -> Mapping[str, object]:
        matches = [
            row
            for row in rows
            if isinstance(row, Mapping) and needle in str(row.get("title", ""))
        ]
        if len(matches) != 1:
            raise RuntimeError(f"expected one source-ledger match for {needle!r}")
        return matches[0]

    selected = [
        (
            by_title(sym10_ledger, "Lefschetz trace formula"),
            "STANDARD_STACK_TRACE_INPUT",
        ),
        (
            by_title(sym10_ledger, "Motives for modular forms"),
            "STANDARD_GOOD_PRIME_FROBENIUS_INPUT",
        ),
        (
            by_title(sym10_ledger, "overpartition function"),
            "LEVEL_TWO_DIMENSION_AND_ETA_PRODUCT_INPUT",
        ),
        (
            by_title(chi04_ledger, "Sur la cohomologie"),
            "LEVEL_ONE_ELLIPTIC_EICHLER_SHIMURA_INPUT_ONLY",
        ),
        (
            by_title(chi04_ledger, "Siegel modular forms of genus 2 and level 2"),
            "MODULI_DEFINITIONS_ONLY; CONJECTURAL_FORMULAS_UNUSED",
        ),
    ]
    return [
        {
            "title": source["title"],
            "url": source["url"],
            "audited_document_sha256": source.get(
                "audited_pdf_sha256", source.get("pdf_sha256")
            ),
            "role_in_this_packet": role,
            "replay_boundary": (
                "metadata is inherited from a source-locked manual audit; "
                "the local producer performs no network access"
            ),
        }
        for source, role in selected
    ]


def _packet_lf_sha256(path: Path) -> str:
    size = path.stat().st_size
    if size > MAX_PACKET_FILE_BYTES:
        raise RuntimeError(f"packet file exceeds byte cap: {path.name}")
    return _lf_sha256_bytes(path.read_bytes())


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()
    sources, manifest = _read_locked_sources(guard, deadline)
    exact_inputs = _validate_exact_inputs(sources)
    exact_proof = _build_exact_proof(exact_inputs, guard, deadline)
    # Deliberately appended after the exact proof has closed.  No value from
    # this block is accepted by _build_exact_proof.
    compatibility = _build_compatibility_context(sources)
    primary_source_ledger = _build_primary_source_ledger(sources)
    deadline.check("before fixture assembly")
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym10_ambient_stack_trace.v1",
        "status": "PROVED_EXACT_AMBIENT_TRACE_ALL_ODD_PRIME_POWERS",
        "scope": {
            "base_fields": "every finite field F_q of odd characteristic",
            "target": "A_2(w^1) with local system V_(10,0)=Sym^10(V)",
            "meaning": ("alternating compactly-supported geometric-Frobenius trace"),
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "abelian_surfaces_enumerated": 0,
            "cohomology_groups_enumerated": 0,
            "random_samples": 0,
        },
        "theorem": {
            "formula": ("Tr(F_q,e_c(A_2(w^1),V_(10,0)))=2-4*q-2*q*Theta_Delta(q)"),
            "quantifier": "every odd prime power q",
            "curve_open_input": exact_inputs.open_trace_formula,
            "stack_trace_meaning": exact_inputs.stack_trace_meaning,
        },
        "proof_dependency_graph": {
            "proof_inputs": [
                "source-locked direct Sym10 curve-open theorem at 42910253b",
                "exact marked geometry A_(1,1)(w^1)=Y_0(2) times A_1",
                "standard elliptic Eichler-Shimura compact-support identities",
            ],
            "rebuilt_exactly_here": [
                "Sym^10 branching and dimension 286",
                "level-one and level-two cusp-space dimensions and old/new split",
                "six even decomposable-boundary rows",
                "modular q-expansions and prime-power trace recurrence",
                "open-plus-boundary channel cancellation",
            ],
            "explicit_non_input": (
                "BFG nonregular, Eisenstein, endoscopic, and ambient formulas"
            ),
        },
        "exact_proof": exact_proof,
        "BFG_compatibility": compatibility,
        "primary_source_ledger": primary_source_ledger,
        "firewalls": [
            (
                "The formula is an equality of alternating compactly-supported "
                "Frobenius traces, not an isomorphism of motives or individual "
                "cohomology groups."
            ),
            (
                "The formal expression 2-4L-2L*S[12] records the proved trace "
                "pattern; it does not exclude canceling cohomological pieces."
            ),
            ("BFG compatibility is conjectural and unused by the proof."),
            (
                "The result gives no memberwise sign, RH/GRH criterion, zero-free "
                "region, principal-member amplifier, motive, or Euler product."
            ),
            "No external novelty claim is made.",
        ],
        "source_manifest": manifest,
        "provenance": {
            "hash_convention": "SHA-256 after CRLF/CR normalization to LF",
            "packet_lf_sha256": {
                "producer": _packet_lf_sha256(SCRIPT_PATH),
                "note": _packet_lf_sha256(NOTE_PATH),
                "test": _packet_lf_sha256(TEST_PATH),
            },
            "resource_contract": {
                "maximum_exact_operations": MAX_EXACT_OPERATIONS,
                "actual_exact_operations": guard.exact_operations,
                "operation_counts": dict(sorted(guard.operation_counts.items())),
                "maximum_source_files": MAX_SOURCE_FILES,
                "actual_source_files": guard.source_files,
                "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
                "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
                "actual_source_bytes": guard.source_bytes,
                "maximum_packet_file_bytes": MAX_PACKET_FILE_BYTES,
                "maximum_wall_seconds": MAX_WALL_SECONDS,
                "arithmetic": "integers only; no floats in mathematical algebra",
            },
        },
    }
    deadline.check("after fixture assembly")
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def _render(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="refuse unless the fixture is current"
    )
    arguments = parser.parse_args(argv)
    rendered = _render(build_fixture())
    if arguments.check:
        if not OUTPUT_PATH.exists():
            raise FileNotFoundError(f"missing fixture: {OUTPUT_PATH}")
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise RuntimeError(f"fixture is stale: {OUTPUT_PATH}")
        print("PASS_GENUS2_SYM10_AMBIENT_STACK_TRACE")
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
