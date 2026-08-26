#!/usr/bin/env python3
"""Bounded exact marked ambient Sym-even trace ladder for genus two.

For r=2,4,6,8,10 this producer combines source-locked marked curve-open
traces with a directly rebuilt decomposable boundary

    A_(1,1)(w^1) = Y_0(2) x A_1,
    Sym^r(W_1 + W_1) = direct_sum_(i=0)^r W_i external_tensor W_(r-i).

All algebra is sparse exact integer arithmetic.  No field, curve, abelian
surface, cohomology group, or modular-symbol space is enumerated.  The exact
ladder closes before its frozen sources are read and validated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path

Monomial = tuple[int, int, int, int]
Polynomial = dict[Monomial, int]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "genus2_ambient_symmetric_power_ladder.json"
NOTE_PATH = HERE / "GENUS2_AMBIENT_SYMMETRIC_POWER_LADDER.md"
TEST_PATH = ROOT / "tests" / "test_genus2_ambient_symmetric_power_ladder.py"

NATIVE_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
SYM6_PATH = HERE / "genus2_sym6_marked_trace_average.json"
SYM8_PATH = HERE / "genus2_sym8_marked_trace_average.json"
SYM10_PATH = HERE / "genus2_sym10_marked_trace_average.json"
ADAPTER_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
DECOMPOSABLE_PATH = HERE / "genus2_chi04_stack_trace_reconciliation.json"
AMBIENT10_PATH = HERE / "genus2_sym10_ambient_stack_trace.json"

MAX_EXACT_OPERATIONS = 5_000
MAX_SOURCE_FILES = 7
MAX_SOURCE_BYTES_EACH = 32_768
MAX_SOURCE_BYTES_TOTAL = 131_072
MAX_PACKET_FILE_BYTES = 65_536
MAX_OUTPUT_BYTES = 65_536
MAX_WALL_SECONDS = 5.0
EVEN_RANKS = (2, 4, 6, 8, 10)

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "native_t2_t4": {
        "path": NATIVE_PATH,
        "commit": "aee73fda38a73bd792a4b69cd12ec7c4b7aaad1e",
        "git_blob": "9548aea141e1f5b48897850a91e9b6d76b7c0ae4",
        "lf_sha256": "aef506afa6b9b29f10528b634f45c7eab96abc36c6cd2de886262e834fcb2d43",
        "schema": "riemann.function_field.native_qadic_reciprocal_wavelet_spectroscopy.v1",
        "payload_sha256": "4e366316c6d55488b41e0104f6bee6c947220d7989ea7aa1381b5d72a099b882",
        "role": "all-q marked-open T_(2,0) and T_(4,0) traces",
    },
    "sym6": {
        "path": SYM6_PATH,
        "commit": "522bc6b454016a07a9c65aaa6177d0340d70f5dc",
        "git_blob": "b1d2c12ff8682db6cf60a8673574d93f2779010c",
        "lf_sha256": "4e6156e8ca4f8b652e02961d3aa5f3ea63c9b42243908d1ecab8b94c08d253a6",
        "schema": "riemann.function_field.genus2_sym6_marked_trace_average.v1",
        "payload_sha256": "7bf31859372bb2a292f8321794f9b05859d2def82b1dd59ad83ab992088a5e86",
        "role": "all-q marked-open T_(6,0) trace theorem",
    },
    "sym8": {
        "path": SYM8_PATH,
        "commit": "dc63f02d0897e10936ef0767a1c8e6f15ac49e06",
        "git_blob": "1dece87cbec2731f858e3dd38d2ceb0a96959d53",
        "lf_sha256": "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233",
        "schema": "riemann.function_field.genus2_sym8_marked_trace_average.v1",
        "payload_sha256": "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae",
        "role": "all-q marked-open T_(8,0) trace theorem",
    },
    "sym10": {
        "path": SYM10_PATH,
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "561caa7dc504dfb158908aef9229e91af0707a1e",
        "lf_sha256": "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce",
        "schema": "riemann.genus2_sym10_marked_trace_average.v1",
        "payload_sha256": "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77",
        "role": "all-q marked-open T_(10,0) trace theorem",
    },
    "marked_adapter": {
        "path": ADAPTER_PATH,
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        "git_blob": "79ad36346734bb41f21b570f380ad9d1af86f9ee",
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "role": "exact marked-stack measure and trace interpretation",
    },
    "decomposable_geometry": {
        "path": DECOMPOSABLE_PATH,
        "commit": "e0da0f790f96f6dc5c03b363a9a01b91621ee113",
        "git_blob": "9160b9a95efec4f0ed7a895b507d13d97158d714",
        "lf_sha256": "7338bb846308b685fc0124ba3f8da80e5fe368360aa79efff97754ad3c200c2b",
        "schema": "riemann.function_field.genus2_chi04_stack_trace_reconciliation.v1",
        "payload_sha256": "b87733cdf4f5532fcc0a74313d79f4d5ee3f056b55c9bab953ef40c3e01a5762",
        "role": "exact marked decomposable geometry Y_0(2) times A_1",
    },
    "ambient_sym10": {
        "path": AMBIENT10_PATH,
        "commit": "50cbe644c6fa9cc4e6a7f5f03683883ffea83d49",
        "git_blob": "c639b41275264ba2a05c51448da5c1cfdf472264",
        "lf_sha256": "abcdf414e237816dae407f6efcc3cd5bf6dc7ac24a1961decbd88e2dfe64d6d7",
        "schema": "riemann.function_field.genus2_sym10_ambient_stack_trace.v1",
        "payload_sha256": "867a49d1daa5dc41012119b6e7154e21d3b4281e9da24ce32014b7f6c371a1b7",
        "role": "independent committed Sym10 ambient endpoint",
    },
}


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    source_files: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if (
            not isinstance(label, str)
            or not label
            or isinstance(amount, bool)
            or not isinstance(amount, int)
            or amount < 0
        ):
            raise ValueError("invalid exact-operation increment")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def source(self, byte_count: int) -> None:
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
        ):
            raise ValueError("source byte count must be a nonnegative integer")
        if byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + byte_count > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source-byte cap exceeded")
        self.source_files += 1
        self.source_bytes += byte_count


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if not isinstance(label, str) or not label:
            raise ValueError("deadline label must be nonempty")
        elapsed = time.monotonic() - self.started
        if elapsed < 0:
            raise RuntimeError("monotonic clock moved backwards")
        if elapsed > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


ONE_MONOMIAL: Monomial = (0, 0, 0, 0)
L_MONOMIAL: Monomial = (1, 0, 0, 0)
DELTA_MONOMIAL: Monomial = (0, 1, 0, 0)
L_DELTA_MONOMIAL: Monomial = (1, 1, 0, 0)
F8_MONOMIAL: Monomial = (0, 0, 1, 0)
L_F8_MONOMIAL: Monomial = (1, 0, 1, 0)
F10_MONOMIAL: Monomial = (0, 0, 0, 1)
L_F10_MONOMIAL: Monomial = (1, 0, 0, 1)

CHANNEL_MONOMIALS: dict[str, Monomial] = {
    "1": ONE_MONOMIAL,
    "L": L_MONOMIAL,
    "Delta": DELTA_MONOMIAL,
    "L*Delta": L_DELTA_MONOMIAL,
    "f_(8,2)": F8_MONOMIAL,
    "L*f_(8,2)": L_F8_MONOMIAL,
    "g_(10,2)": F10_MONOMIAL,
    "L*g_(10,2)": L_F10_MONOMIAL,
}

OPEN_COEFFICIENTS: dict[int, dict[str, int]] = {
    2: {"1": -1, "L": 1},
    4: {"1": -3},
    6: {"1": -4},
    8: {"1": -6, "L": -1, "f_(8,2)": -1},
    10: {
        "1": -7,
        "L": -1,
        "Delta": -1,
        "L*Delta": 1,
        "f_(8,2)": -1,
        "g_(10,2)": -1,
    },
}

BOUNDARY_COEFFICIENTS: dict[int, dict[str, int]] = {
    2: {"1": 1, "L": -3},
    4: {"1": 3, "L": -3},
    6: {"1": 5, "L": -3, "L*f_(8,2)": -1},
    8: {"1": 7, "L": -3, "f_(8,2)": 1, "L*g_(10,2)": -1},
    10: {
        "1": 9,
        "L": -3,
        "Delta": 1,
        "L*Delta": -3,
        "f_(8,2)": 1,
        "g_(10,2)": 1,
    },
}

AMBIENT_COEFFICIENTS: dict[int, dict[str, int]] = {
    2: {"L": -2},
    4: {"L": -3},
    6: {"1": 1, "L": -3, "L*f_(8,2)": -1},
    8: {"1": 1, "L": -4, "L*g_(10,2)": -1},
    10: {"1": 2, "L": -4, "L*Delta": -2},
}

FORMULAS: dict[str, dict[int, str]] = {
    "open": {
        2: "L-1",
        4: "-3",
        6: "-4",
        8: "-f_(8,2)-L-6",
        10: "(L-1)*Delta-f_(8,2)-g_(10,2)-L-7",
    },
    "boundary": {
        2: "1-3*L",
        4: "3-3*L",
        6: "5-3*L-L*f_(8,2)",
        8: "7-3*L+f_(8,2)-L*g_(10,2)",
        10: "(1-3*L)*Delta+f_(8,2)+g_(10,2)-3*L+9",
    },
    "ambient": {
        2: "-2*L",
        4: "-3*L",
        6: "1-3*L-L*f_(8,2)",
        8: "1-4*L-L*g_(10,2)",
        10: "2-4*L-2*L*Delta",
    },
}

CONTROL_TRACES = {
    3: {"Delta": 252, "f_(8,2)": 12, "g_(10,2)": -156},
    5: {"Delta": 4_830, "f_(8,2)": -210, "g_(10,2)": 870},
    7: {"Delta": -16_744, "f_(8,2)": 1_016, "g_(10,2)": -952},
    9: {"Delta": -290_790, "f_(8,2)": -4_230, "g_(10,2)": -15_030},
}


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
        if isinstance(item, tuple):
            return [normalize(entry) for entry in item]
        if isinstance(item, list):
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


def _clean(polynomial: Mapping[Monomial, int]) -> Polynomial:
    result: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        if (
            len(monomial) != 4
            or any(
                isinstance(power, bool) or not isinstance(power, int) or power < 0
                for power in monomial
            )
            or isinstance(coefficient, bool)
            or not isinstance(coefficient, int)
        ):
            raise ValueError("invalid sparse polynomial term")
        if coefficient:
            result[tuple(monomial)] = coefficient
    return result


def poly_add(
    left: Mapping[Monomial, int],
    right: Mapping[Monomial, int],
    guard: ResourceGuard,
) -> Polynomial:
    result = dict(_clean(left))
    for monomial, coefficient in _clean(right).items():
        guard.operation("polynomial_add", 1)
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def poly_scale(
    polynomial: Mapping[Monomial, int], coefficient: int, guard: ResourceGuard
) -> Polynomial:
    if isinstance(coefficient, bool) or not isinstance(coefficient, int):
        raise TypeError("polynomial scale must be an integer")
    clean = _clean(polynomial)
    guard.operation("polynomial_scale", len(clean))
    return _clean({monomial: coefficient * value for monomial, value in clean.items()})


def poly_multiply(
    left: Mapping[Monomial, int],
    right: Mapping[Monomial, int],
    guard: ResourceGuard,
) -> Polynomial:
    left_clean = _clean(left)
    right_clean = _clean(right)
    result: Polynomial = {}
    for left_monomial, left_coefficient in left_clean.items():
        for right_monomial, right_coefficient in right_clean.items():
            guard.operation("polynomial_multiply", 1)
            monomial = tuple(
                left_power + right_power
                for left_power, right_power in zip(left_monomial, right_monomial)
            )
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
    return _clean(result)


def channel_polynomial(coefficients: Mapping[str, int]) -> Polynomial:
    result: Polynomial = {}
    for channel, coefficient in coefficients.items():
        monomial = CHANNEL_MONOMIALS.get(channel)
        if monomial is None:
            raise ValueError(f"unknown trace channel: {channel}")
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise TypeError("trace-channel coefficient must be an integer")
        if coefficient:
            result[monomial] = coefficient
    return result


def polynomial_channels(polynomial: Mapping[Monomial, int]) -> dict[str, int]:
    clean = _clean(polynomial)
    inverse = {monomial: label for label, monomial in CHANNEL_MONOMIALS.items()}
    if any(monomial not in inverse for monomial in clean):
        raise ArithmeticError("unexpected nonlinear trace channel survived")
    return {
        inverse[monomial]: clean[monomial]
        for monomial in CHANNEL_MONOMIALS.values()
        if monomial in clean
    }


def serialize_polynomial(polynomial: Mapping[Monomial, int]) -> list[dict[str, int]]:
    return [
        {
            "coefficient": coefficient,
            "L_power": monomial[0],
            "Delta_power": monomial[1],
            "f_(8,2)_power": monomial[2],
            "g_(10,2)_power": monomial[3],
        }
        for monomial, coefficient in sorted(_clean(polynomial).items())
    ]


def _one() -> Polynomial:
    return {ONE_MONOMIAL: 1}


def _generator(monomial: Monomial) -> Polynomial:
    return {monomial: 1}


def level_one_cusp(weight: int, guard: ResourceGuard) -> Polynomial:
    if weight not in (4, 6, 8, 10, 12):
        raise ValueError("level-one weight is outside the bounded ladder")
    guard.operation("cusp_lookup", 1)
    return _generator(DELTA_MONOMIAL) if weight == 12 else {}


def level_two_cusp(weight: int, guard: ResourceGuard) -> Polynomial:
    if weight not in (4, 6, 8, 10, 12):
        raise ValueError("level-two weight is outside the bounded ladder")
    guard.operation("cusp_lookup", 1)
    if weight == 8:
        return _generator(F8_MONOMIAL)
    if weight == 10:
        return _generator(F10_MONOMIAL)
    if weight == 12:
        return poly_scale(_generator(DELTA_MONOMIAL), 2, guard)
    return {}


def a1_euler(degree: int, guard: ResourceGuard) -> Polynomial:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("elliptic symmetric-power degree must be nonnegative")
    if degree == 0:
        return _generator(L_MONOMIAL)
    if degree % 2:
        return {}
    result = poly_scale(_one(), -1, guard)
    return poly_add(
        result, poly_scale(level_one_cusp(degree + 2, guard), -1, guard), guard
    )


def y0_euler(degree: int, guard: ResourceGuard) -> Polynomial:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("elliptic symmetric-power degree must be nonnegative")
    if degree == 0:
        return poly_add(_generator(L_MONOMIAL), poly_scale(_one(), -1, guard), guard)
    if degree % 2:
        return {}
    result = poly_scale(_one(), -2, guard)
    return poly_add(
        result, poly_scale(level_two_cusp(degree + 2, guard), -1, guard), guard
    )


def evaluate_polynomial(
    polynomial: Mapping[Monomial, int],
    q: int,
    traces: Mapping[str, int],
    guard: ResourceGuard | None = None,
) -> int:
    if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
        raise ValueError("q must be a positive integer")
    required = ("Delta", "f_(8,2)", "g_(10,2)")
    if any(
        name not in traces
        or isinstance(traces[name], bool)
        or not isinstance(traces[name], int)
        for name in required
    ):
        raise ValueError("incomplete exact modular trace row")
    clean = _clean(polynomial)
    resource = ResourceGuard() if guard is None else guard
    resource.operation("control_evaluation", len(clean))
    result = 0
    for monomial, coefficient in clean.items():
        result += (
            coefficient
            * q ** monomial[0]
            * traces["Delta"] ** monomial[1]
            * traces["f_(8,2)"] ** monomial[2]
            * traces["g_(10,2)"] ** monomial[3]
        )
    return result


def _boundary_for_rank(
    r: int, guard: ResourceGuard
) -> tuple[Polynomial, list[dict[str, object]]]:
    if r not in EVEN_RANKS:
        raise ValueError("rank is outside the declared even ladder")
    boundary: Polynomial = {}
    rows: list[dict[str, object]] = []
    dimension_sum = 0
    for index in range(r + 1):
        dimension = (index + 1) * (r - index + 1)
        dimension_sum += dimension
        left = y0_euler(index, guard)
        right = a1_euler(r - index, guard)
        contribution = poly_multiply(left, right, guard)
        boundary = poly_add(boundary, contribution, guard)
        if (index % 2 == 1) != (not contribution):
            raise ArithmeticError("odd-branch vanishing certificate failed")
        rows.append(
            {
                "i": index,
                "branch_dimension": dimension,
                "Y_0(2)_W_i": serialize_polynomial(left),
                "A_1_W_(r-i)": serialize_polynomial(right),
                "contribution": serialize_polynomial(contribution),
                "vanishes_by_unmarked_central_involution": not contribution,
            }
        )
    expected_dimension = (r + 1) * (r + 2) * (r + 3) // 6
    guard.operation("dimension_check", r + 1)
    if dimension_sum != expected_dimension:
        raise ArithmeticError("symmetric-power branch dimensions failed")
    return boundary, rows


def _channel_balance(
    open_polynomial: Mapping[Monomial, int],
    boundary: Mapping[Monomial, int],
    ambient: Mapping[Monomial, int],
) -> dict[str, object]:
    open_channels = polynomial_channels(open_polynomial)
    boundary_channels = polynomial_channels(boundary)
    ambient_channels = polynomial_channels(ambient)
    rows = []
    canceled = []
    for channel in CHANNEL_MONOMIALS:
        open_coefficient = open_channels.get(channel, 0)
        boundary_coefficient = boundary_channels.get(channel, 0)
        ambient_coefficient = ambient_channels.get(channel, 0)
        if open_coefficient or boundary_coefficient or ambient_coefficient:
            rows.append(
                {
                    "channel": channel,
                    "open": open_coefficient,
                    "boundary": boundary_coefficient,
                    "ambient": ambient_coefficient,
                }
            )
        if open_coefficient and boundary_coefficient and ambient_coefficient == 0:
            canceled.append(channel)
    return {"rows": rows, "exactly_canceled_channels": canceled}


def _build_exact_ladder(guard: ResourceGuard) -> dict[str, object]:
    ladder_rows = []
    ambient_polynomials: dict[int, Polynomial] = {}
    for r in EVEN_RANKS:
        open_polynomial = channel_polynomial(OPEN_COEFFICIENTS[r])
        boundary, branch_rows = _boundary_for_rank(r, guard)
        expected_boundary = channel_polynomial(BOUNDARY_COEFFICIENTS[r])
        if boundary != expected_boundary:
            raise ArithmeticError(f"rank-{r} decomposable boundary drifted")
        ambient = poly_add(open_polynomial, boundary, guard)
        expected_ambient = channel_polynomial(AMBIENT_COEFFICIENTS[r])
        if ambient != expected_ambient:
            raise ArithmeticError(f"rank-{r} ambient trace drifted")
        ambient_polynomials[r] = ambient
        ladder_rows.append(
            {
                "r": r,
                "branching_identity": (
                    f"Sym^{r}(W_1 direct_sum W_1)=direct_sum_(i=0)^{r} "
                    f"W_i external_tensor W_({r}-i)"
                ),
                "branch_dimension_sum": sum(
                    row["branch_dimension"] for row in branch_rows
                ),
                "symmetric_power_dimension": (r + 1) * (r + 2) * (r + 3) // 6,
                "branch_rows": branch_rows,
                "open_formula": FORMULAS["open"][r],
                "open_expression": serialize_polynomial(open_polynomial),
                "boundary_formula": FORMULAS["boundary"][r],
                "boundary_expression": serialize_polynomial(boundary),
                "ambient_formula": FORMULAS["ambient"][r],
                "ambient_expression": serialize_polynomial(ambient),
                "channel_balance": _channel_balance(open_polynomial, boundary, ambient),
            }
        )

    controls = []
    for q, traces in CONTROL_TRACES.items():
        controls.append(
            {
                "q": q,
                "Theta_Delta": traces["Delta"],
                "Theta_(8,2)": traces["f_(8,2)"],
                "Theta_(10,2)": traces["g_(10,2)"],
                "ambient_traces": {
                    str(r): evaluate_polynomial(
                        ambient_polynomials[r], q, traces, guard
                    )
                    for r in EVEN_RANKS
                },
            }
        )

    return {
        "formal_ring": "Z[L,Delta,f_(8,2),g_(10,2)]",
        "geometry": (
            "A_(1,1)(w^1)=Y_0(2) times A_1; the marked odd theta "
            "characteristic distinguishes the factors"
        ),
        "branching_rule": (
            "Sym^r(W_1 direct_sum W_1)=direct_sum_(i=0)^r W_i external_tensor W_(r-i)"
        ),
        "elliptic_inputs": {
            "A_1_W_0": "L",
            "Y_0(2)_W_0": "L-1",
            "A_1_even_positive": "-S[r+2]-1",
            "Y_0(2)_even_positive": "-S[Gamma_0(2),r+2]-2",
            "odd": "zero by the unmarked A_1 central involution",
            "level_1_nonzero": {"weight_12": "Delta"},
            "level_2_nonzero": {
                "weight_8": "f_(8,2)",
                "weight_10": "g_(10,2)",
                "weight_12": "2*Delta (oldspace; no newspace)",
            },
        },
        "ladder": ladder_rows,
        "channel_shift_ladder": [
            {
                "r": 2,
                "statement": "the open constant cancels and only -2*L remains",
            },
            {
                "r": 4,
                "statement": "the open constant cancels and only -3*L remains",
            },
            {
                "r": 6,
                "statement": "the boundary first injects -L*f_(8,2)",
            },
            {
                "r": 8,
                "statement": (
                    "the unshifted f_(8,2) channel cancels and the next "
                    "channel survives as -L*g_(10,2)"
                ),
            },
            {
                "r": 10,
                "statement": (
                    "unshifted f_(8,2), g_(10,2), and Delta cancel; "
                    "the two-copy level-two oldspace leaves -2*L*Delta"
                ),
            },
        ],
        "exact_controls": controls,
    }


def _read_locked_sources(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    parsed: dict[str, dict[str, object]] = {}
    manifest = []
    for name, lock in SOURCE_LOCKS.items():
        deadline.check(f"before source {name}")
        path = lock.get("path")
        if not isinstance(path, Path) or not path.is_file():
            raise RuntimeError(f"missing source lock: {name}")
        size = path.stat().st_size
        guard.source(size)
        raw = path.read_bytes()
        if len(raw) != size:
            raise RuntimeError(f"source changed while reading: {name}")
        if _lf_sha256_bytes(raw) != lock.get("lf_sha256"):
            raise RuntimeError(f"source LF hash mismatch: {name}")
        if _git_blob_sha1(raw) != lock.get("git_blob"):
            raise RuntimeError(f"source git-blob mismatch: {name}")
        value = json.loads(_lf_bytes(raw).decode("utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source JSON is not an object: {name}")
        if value.get("schema") != lock.get("schema"):
            raise RuntimeError(f"source schema mismatch: {name}")
        payload = dict(value)
        claimed_payload = payload.pop("payload_sha256", None)
        if (
            claimed_payload != lock.get("payload_sha256")
            or _canonical_sha256(payload) != claimed_payload
        ):
            raise RuntimeError(f"source canonical payload mismatch: {name}")
        parsed[name] = value
        manifest.append(
            {
                "id": name,
                "path": _relative(path),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "lf_sha256": lock["lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "schema": lock["schema"],
                "role": lock["role"],
                "bytes": size,
            }
        )
    return parsed, manifest


def _validate_source_semantics(sources: Mapping[str, dict[str, object]]) -> None:
    native = sources["native_t2_t4"]
    if native.get("proved_all_q_trace_inputs") != {
        "T_(2,0)": "q-1",
        "T_(4,0)": "-3",
        "source": "the exact low-weight character profile in the locked q-scan theorem",
    }:
        raise RuntimeError("T2/T4 marked-open source semantics changed")

    expected_marked = {
        "sym6": "T_(6,0)(q)=-4",
        "sym8": "T_(8,0)(q)=-Theta_(8,2)(q)-q-6",
        "sym10": (
            "T_(10,0)(q)=(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7"
        ),
    }
    for name, formula in expected_marked.items():
        theorem = sources[name].get("theorem")
        if (
            not isinstance(theorem, dict)
            or theorem.get("marked_stack_trace") != formula
        ):
            raise RuntimeError(f"{name} marked-open theorem changed")

    adapter = sources["marked_adapter"].get("trace_theorem")
    adapter_scope = sources["marked_adapter"].get("scope")
    if (
        not isinstance(adapter, dict)
        or adapter.get("generic_groupoid_formula")
        != "Tr_stack,q(V_lambda)=1/(q*(q-1))*sum_D Tr(Frob_D|V_lambda)"
        or not isinstance(adapter_scope, dict)
        or adapter_scope.get("base_fields")
        != "every finite field F_q of odd characteristic"
    ):
        raise RuntimeError("marked stack adapter semantics changed")

    decomposable = sources["decomposable_geometry"].get("exact_decomposable_boundary")
    if not isinstance(decomposable, dict) or decomposable.get("geometry") != (
        "A_(1,1)(w^1) is Y_0(2) times A_1"
    ):
        raise RuntimeError("marked decomposable geometry changed")

    ambient = sources["ambient_sym10"]
    theorem = ambient.get("theorem")
    exact_proof = ambient.get("exact_proof")
    if (
        not isinstance(theorem, dict)
        or theorem.get("formula")
        != "Tr(F_q,e_c(A_2(w^1),V_(10,0)))=2-4*q-2*q*Theta_Delta(q)"
        or not isinstance(exact_proof, dict)
    ):
        raise RuntimeError("committed ambient Sym10 endpoint changed")
    boundary = exact_proof.get("decomposable_boundary")
    dimensions = exact_proof.get("modular_dimension_certificate")
    standard_inputs = (
        boundary.get("standard_eichler_shimura_inputs")
        if isinstance(boundary, dict)
        else None
    )
    if (
        not isinstance(boundary, dict)
        or boundary.get("boundary_formula") != "(1-3*L)*Delta+f_(8,2)+g_(10,2)-3*L+9"
        or boundary.get("geometry")
        != (
            "A_(1,1)(w^1)=Y_0(2) times A_1; the marked odd theta "
            "characteristic distinguishes the factors, so there is no S_2 quotient"
        )
        or not isinstance(standard_inputs, dict)
        or standard_inputs.get("A_1_W_0") != "L"
        or standard_inputs.get("A_1_W_r_even_positive") != "-S[r+2]-1"
        or standard_inputs.get("Y_0(2)_W_0") != "L-1"
        or standard_inputs.get("Y_0(2)_W_r_even_positive") != "-S[Gamma_0(2),r+2]-2"
        or standard_inputs.get("odd_degree")
        != "zero because [-1] acts nontrivially on the unmarked A_1 fibre"
        or not isinstance(dimensions, dict)
    ):
        raise RuntimeError("ambient Sym10 boundary semantics changed")
    rows = dimensions.get("rows")
    expected_rows = [
        (4, 0, 0, 0, 0),
        (6, 0, 0, 0, 0),
        (8, 0, 1, 0, 1),
        (10, 0, 1, 0, 1),
        (12, 1, 2, 2, 0),
    ]
    if (
        not isinstance(rows, list)
        or [
            (
                row.get("weight"),
                row.get("dim_S_level_1"),
                row.get("dim_S_Gamma0_2"),
                row.get("dim_old_Gamma0_2"),
                row.get("dim_new_Gamma0_2"),
            )
            for row in rows
            if isinstance(row, dict)
        ]
        != expected_rows
    ):
        raise RuntimeError("elliptic cusp-space dimension ladder changed")


def _packet_manifest() -> list[dict[str, object]]:
    rows = []
    for path in (NOTE_PATH, SCRIPT_PATH, TEST_PATH):
        if not path.is_file():
            raise RuntimeError(f"missing packet file: {path}")
        size = path.stat().st_size
        if size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError(f"packet file exceeds byte cap: {path}")
        raw = path.read_bytes()
        if len(raw) != size:
            raise RuntimeError(f"packet file changed while reading: {path}")
        rows.append(
            {
                "path": _relative(path),
                "bytes": size,
                "lf_sha256": _lf_sha256_bytes(raw),
            }
        )
    return rows


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()

    exact_proof = _build_exact_ladder(guard)
    operations_after_exact_algebra = guard.exact_operations
    deadline.check("after exact ladder")

    sources, source_manifest = _read_locked_sources(guard, deadline)
    _validate_source_semantics(sources)
    deadline.check("after source validation")

    packet_manifest = _packet_manifest()
    deadline.check("after packet manifest")
    fixture: dict[str, object] = {
        "schema": "riemann.function_field.genus2_ambient_symmetric_power_ladder.v1",
        "status": "EXACT_MARKED_AMBIENT_SYM_EVEN_LADDER_R2_THROUGH_R10",
        "theorem": {
            "quantifier": "every odd prime power q",
            "ambient_space": "A_2(w^1)",
            "local_system": "V_(r,0)=Sym^r(V), r in {2,4,6,8,10}",
            "trace_meaning": (
                "alternating compactly supported geometric-Frobenius trace"
            ),
            "formulas": {
                "r=2": "-2*q",
                "r=4": "-3*q",
                "r=6": "1-3*q-q*Theta_(8,2)(q)",
                "r=8": "1-4*q-q*Theta_(10,2)(q)",
                "r=10": "2-4*q-2*q*Theta_Delta(q)",
            },
        },
        "exact_proof": exact_proof,
        "source_manifest": source_manifest,
        "packet_manifest": packet_manifest,
        "resource_contract": {
            "arithmetic": "exact sparse integer polynomial algebra only",
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operations_after_exact_algebra": operations_after_exact_algebra,
            "operation_counts": dict(sorted(guard.operation_counts.items())),
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
            "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_source_bytes": guard.source_bytes,
            "maximum_packet_file_bytes": MAX_PACKET_FILE_BYTES,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "abelian_surfaces_enumerated": 0,
            "cohomology_groups_enumerated": 0,
            "modular_symbols_enumerated": 0,
        },
        "scope": {
            "virtual_compact_support_trace": True,
            "individual_cohomology_group_decomposition": False,
            "motivic_isomorphism": False,
            "compatible_system_constructed": False,
            "memberwise_sign": False,
            "rh_or_grh_claim": False,
            "external_novelty_claimed": False,
        },
        "firewalls": [
            "The ladder concerns alternating compactly supported virtual traces, not individual cohomology groups.",
            "A trace-channel cancellation is not a motivic isomorphism or a proof that canceling cohomology objects are absent.",
            "The decomposable boundary is the ordered product Y_0(2) times A_1; no S_2 quotient is inserted.",
            "The r=10 endpoint is independently source-locked at commit 50cbe644c6fa9cc4e6a7f5f03683883ffea83d49.",
            "No finite-field enumeration, asymptotic inference, RH criterion, or external novelty claim is made.",
        ],
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    deadline.check("after payload")
    return fixture


def _serialized(value: Mapping[str, object]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _read_output_capped(path: Path) -> str:
    size = path.stat().st_size
    if size > MAX_OUTPUT_BYTES:
        raise RuntimeError(f"comparison fixture exceeds output byte cap: {path}")
    raw = path.read_bytes()
    if len(raw) != size:
        raise RuntimeError(f"comparison fixture changed while reading: {path}")
    return raw.decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    arguments = parser.parse_args()
    fixture = build_fixture()
    rendered = _serialized(fixture)
    if len(rendered.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise RuntimeError("serialized fixture exceeds output byte cap")
    if arguments.check:
        if not arguments.output.is_file():
            raise SystemExit(f"missing fixture: {arguments.output}")
        if _read_output_capped(arguments.output) != rendered:
            raise SystemExit(f"stale fixture: {arguments.output}")
        print(f"verified {arguments.output}")
        return 0
    arguments.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
