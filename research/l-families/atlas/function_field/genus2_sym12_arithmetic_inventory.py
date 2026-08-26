#!/usr/bin/env python3
"""Prove the exact source-relative arithmetic inventory for marked Sym^12.

The degree-twelve reciprocal descent has one free completed coefficient.
This producer rebuilds every lower Euler/marking row from source-locked
all-weight genus-one laws, isolates that one coefficient, and derives the
decomposable ambient boundary.  It enumerates no field, polynomial, curve,
abelian surface, or cohomology group.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym12_arithmetic_inventory.json"
NOTE_PATH = HERE / "GENUS2_SYM12_ARITHMETIC_INVENTORY.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym12_arithmetic_inventory.py"

MAX_EXACT_OPERATIONS = 16_384
MAX_SOURCE_FILES = 8
MAX_SOURCE_BYTES_EACH = 65_536
MAX_SOURCE_BYTES_TOTAL = 225_000
MAX_OUTPUT_BYTES = 65_536
MAX_WALL_SECONDS = 4.0

SOURCE_LOCKS: tuple[dict[str, object], ...] = (
    {
        "name": "reciprocal_boundary",
        "path": HERE / "genus2_reciprocal_descent_boundary.json",
        "commit": "476f1f5e445a4f05e6ae8b8a54376bd78a2a1a20",
        "git_blob": "b66af64816f7cf5da13e07b25993377db2643fdf",
        "lf_sha256": "0a21ce9bd6340fcc9329ad343aeb354d7310ea0cf4dde6f128cbc11bc14a0c71",
        "schema": "riemann.function_field.genus2_reciprocal_descent_boundary.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "0b8cb0ac368d9923ce10644b5c5cd09f752d056ede8226e9e38d603b86aa1fbf",
        "role": "degree-twelve central-coefficient and method-boundary theorem",
    },
    {
        "name": "r6_reconnaissance",
        "path": HERE / "genus2_r6_proof_reconnaissance.json",
        "commit": "f83f80639fc821abc41d0bcb781972c65b85a548",
        "git_blob": "224f24b0ec3aa9ebc4cd98de7b505dbf5c30f53b",
        "lf_sha256": "8eac418b5d624b4524bdf5d63534100ec19e17bd85c787a590bed96e896e91a3",
        "schema": "riemann.function_field.genus2_r6_proof_reconnaissance.v1",
        "payload_key": "canonical_payload_sha256",
        "payload_sha256": "8e42ff92f764fd285ca2f68bba66c4831168f8b77bedb640256f27cdc7e9fcb7",
        "role": "character-span no-go and separate R6 arithmetic gap",
    },
    {
        "name": "sym6",
        "path": HERE / "genus2_sym6_marked_trace_average.json",
        "commit": "522bc6b454016a07a9c65aaa6177d0340d70f5dc",
        "git_blob": "b1d2c12ff8682db6cf60a8673574d93f2779010c",
        "lf_sha256": "4e6156e8ca4f8b652e02961d3aa5f3ea63c9b42243908d1ecab8b94c08d253a6",
        "schema": "riemann.function_field.genus2_sym6_marked_trace_average.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "7bf31859372bb2a292f8321794f9b05859d2def82b1dd59ad83ab992088a5e86",
        "role": "first exact marked symmetric-power ladder row",
    },
    {
        "name": "sym8",
        "path": HERE / "genus2_sym8_marked_trace_average.json",
        "commit": "dc63f02d0897e10936ef0767a1c8e6f15ac49e06",
        "git_blob": "1dece87cbec2731f858e3dd38d2ceb0a96959d53",
        "lf_sha256": "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233",
        "schema": "riemann.function_field.genus2_sym8_marked_trace_average.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae",
        "role": "second exact marked symmetric-power ladder row",
    },
    {
        "name": "sym10",
        "path": HERE / "genus2_sym10_marked_trace_average.json",
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "git_blob": "561caa7dc504dfb158908aef9229e91af0707a1e",
        "lf_sha256": "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce",
        "schema": "riemann.genus2_sym10_marked_trace_average.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77",
        "role": "last closed one-step marked row and quartic-stratum template",
    },
    {
        "name": "genus1",
        "path": HERE / "genus1_cubic_family_laws.json",
        "commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
        "git_blob": "49cde8d3a1881d0d626e4f288abc53f370a33244",
        "lf_sha256": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
        "schema": "riemann.function_field.genus1_cubic_family_laws.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
        "role": "all-weight unmarked elliptic moment and character law",
    },
    {
        "name": "marked_tower",
        "path": HERE / "genus1_marked_2torsion_moment_tower.json",
        "commit": "446c889795a05fd378fed93d443c8887b6e25794",
        "git_blob": "19c82e8af8aea133eb53c6843c7f45c6ca30b693",
        "lf_sha256": "8f254196d3aa73f440a18f22da0bfa3f54307db7c68e7fa3faf934de60cbbf3e",
        "schema": "riemann.genus1_marked_2torsion_moment_tower.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "d6861d94296bd37bba503f87cfa4b00b51a3a2d4f62ae01c707cc45a08588cde",
        "role": "all-weight marked Y_0(2) moment theorem",
    },
    {
        "name": "ambient_ladder",
        "path": HERE / "genus2_ambient_symmetric_power_ladder.json",
        "commit": "2871db30ec0a03b049a297675ac0d2081d706521",
        "git_blob": "89e17fd88697ae902a3f70c14c838a0c1038888a",
        "lf_sha256": "36f50aaf9f2c27130bd3f6ddc54f7eff9e9397faf1f1a0b9db82958b3f0daec6",
        "schema": "riemann.function_field.genus2_ambient_symmetric_power_ladder.v1",
        "payload_key": "payload_sha256",
        "payload_sha256": "c854c15f654edc97783537a814a20f5fd91fbdbf2b2929d34c8ba79c8eca2fb4",
        "role": "ordered decomposable geometry and elliptic boundary formulas",
    },
)

# q, Delta, f_(8,2), g_(10,2), Theta_(14,Gamma0(2)), Hhat_12.
Monomial = tuple[int, int, int, int, int, int]
Expression = dict[Monomial, Fraction]
SparseEuler = dict[tuple[int, int, int], int]
SparseSU2 = dict[tuple[int, int], int]
ZERO_MONOMIAL: Monomial = (0, 0, 0, 0, 0, 0)
VARIABLES = (
    "q",
    "Theta_Delta",
    "Theta_(8,2)",
    "Theta_(10,2)",
    "Theta_(14,2)",
    "Hhat_12",
)


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    source_files: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if (
            not label
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
        if byte_count < 0 or byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("source-file byte cap exceeded")
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
        if not label:
            raise ValueError("deadline label must be nonempty")
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _lf_bytes(raw: bytes) -> bytes:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return unicodedata.normalize("NFC", text).encode("utf-8")


def _lf_sha256(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    return hashlib.sha1(f"blob {len(normalized)}\0".encode() + normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _clean(expression: Mapping[Monomial, Fraction | int]) -> Expression:
    result: Expression = {}
    for monomial, coefficient in expression.items():
        if len(monomial) != len(VARIABLES) or any(power < 0 for power in monomial):
            raise ValueError("invalid expression monomial")
        value = Fraction(coefficient)
        if value:
            result[tuple(monomial)] = value
    return result


def e_add(
    left: Mapping[Monomial, Fraction | int],
    right: Mapping[Monomial, Fraction | int],
    guard: ResourceGuard,
) -> Expression:
    result = _clean(left)
    for monomial, coefficient in _clean(right).items():
        guard.operation("expression_add")
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def e_scale(
    expression: Mapping[Monomial, Fraction | int],
    coefficient: Fraction | int,
    guard: ResourceGuard,
) -> Expression:
    value = Fraction(coefficient)
    clean = _clean(expression)
    guard.operation("expression_scale", len(clean))
    return _clean({monomial: value * item for monomial, item in clean.items()})


def e_multiply(
    left: Mapping[Monomial, Fraction | int],
    right: Mapping[Monomial, Fraction | int],
    guard: ResourceGuard,
) -> Expression:
    result: Expression = {}
    for left_monomial, left_coefficient in _clean(left).items():
        for right_monomial, right_coefficient in _clean(right).items():
            guard.operation("expression_multiply")
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            result[monomial] = (
                result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
            )
    return _clean(result)


def term(
    coefficient: int = 1,
    *,
    q: int = 0,
    delta: int = 0,
    f8: int = 0,
    g10: int = 0,
    h14: int = 0,
    central: int = 0,
) -> Expression:
    return _clean({(q, delta, f8, g10, h14, central): coefficient})


def q_shift(
    expression: Mapping[Monomial, Fraction | int], degree: int, guard: ResourceGuard
) -> Expression:
    if degree < 0:
        raise ValueError("q shift must be nonnegative")
    return e_multiply(expression, term(q=degree), guard)


def _number(value: Fraction) -> int | list[int]:
    return (
        value.numerator
        if value.denominator == 1
        else [value.numerator, value.denominator]
    )


def serialize_expression(
    expression: Mapping[Monomial, Fraction | int],
) -> list[dict[str, object]]:
    return [
        {
            "coefficient": _number(coefficient),
            **{f"{name}_power": power for name, power in zip(VARIABLES, monomial)},
        }
        for monomial, coefficient in sorted(_clean(expression).items())
    ]


def sp_add(left: SparseEuler, right: SparseEuler, guard: ResourceGuard) -> SparseEuler:
    result = dict(left)
    for monomial, coefficient in right.items():
        guard.operation("euler_add")
        result[monomial] = result.get(monomial, 0) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def sp_shift(
    value: SparseEuler,
    guard: ResourceGuard,
    *,
    q: int = 0,
    s: int = 0,
    n: int = 0,
    scale: int = 1,
) -> SparseEuler:
    guard.operation("euler_shift", len(value))
    return {
        (a + q, b + s, c + n): scale * coefficient
        for (a, b, c), coefficient in value.items()
        if scale * coefficient
    }


def su2_add(left: SparseSU2, right: SparseSU2, guard: ResourceGuard) -> SparseSU2:
    result = dict(left)
    for monomial, coefficient in right.items():
        guard.operation("su2_add")
        result[monomial] = result.get(monomial, 0) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def su2_shift(
    value: SparseSU2, guard: ResourceGuard, *, q: int = 0, a: int = 0, scale: int = 1
) -> SparseSU2:
    guard.operation("su2_shift", len(value))
    return {
        (x + q, y + a): scale * coefficient
        for (x, y), coefficient in value.items()
        if scale * coefficient
    }


def catalan(index: int) -> int:
    return math.comb(2 * index, index) // (index + 1)


def ballot(half_degree: int, character_index: int) -> int:
    lower = half_degree - character_index
    second = math.comb(2 * half_degree, lower - 1) if lower else 0
    return math.comb(2 * half_degree, lower) - second


def level_one_cusp(weight: int) -> Expression:
    return term(delta=1) if weight == 12 else {}


def level_two_cusp(weight: int) -> Expression:
    if weight == 8:
        return term(f8=1)
    if weight == 10:
        return term(g10=1)
    if weight == 12:
        return term(2, delta=1)
    if weight == 14:
        return term(h14=1)
    return {}


def raw_moment(half_degree: int, guard: ResourceGuard) -> Expression:
    result = term(catalan(half_degree), q=half_degree + 1)
    for index in range(1, half_degree + 1):
        coefficient = ballot(half_degree, index)
        q_degree = half_degree - index
        result = e_add(result, term(-coefficient, q=q_degree), guard)
        result = e_add(
            result,
            e_scale(
                q_shift(level_one_cusp(2 * index + 2), q_degree, guard),
                -coefficient,
                guard,
            ),
            guard,
        )
    return result


def marked_moment(half_degree: int, guard: ResourceGuard) -> Expression:
    leading = e_add(
        term(-catalan(half_degree), q=half_degree),
        term(catalan(half_degree), q=half_degree + 1),
        guard,
    )
    result = leading
    for index in range(1, half_degree + 1):
        coefficient = ballot(half_degree, index)
        q_degree = half_degree - index
        result = e_add(result, term(-2 * coefficient, q=q_degree), guard)
        result = e_add(
            result,
            e_scale(
                q_shift(level_two_cusp(2 * index + 2), q_degree, guard),
                -coefficient,
                guard,
            ),
            guard,
        )
    return result


def _formal_euler(
    endpoint: int, guard: ResourceGuard
) -> tuple[list[SparseEuler], SparseEuler]:
    rows: list[SparseEuler] = [{(0, 0, 0): 1}, {(0, 1, 0): -1}]
    for _degree in range(2, endpoint + 1):
        rows.append(
            sp_add(
                sp_shift(rows[-1], guard, s=1, scale=-1),
                sp_shift(rows[-2], guard, q=1, scale=-1),
                guard,
            )
        )
    marked: SparseEuler = {}
    for degree in range(1, endpoint + 1):
        shift = {"s": 1} if degree % 2 else {"n": 1}
        marked = sp_add(
            marked, sp_shift(rows[endpoint - degree], guard, scale=-1, **shift), guard
        )
    return rows, marked


def _sum_squarefree_cubics(
    value: SparseEuler,
    raw: Mapping[int, Expression],
    marked: Mapping[int, Expression],
    guard: ResourceGuard,
) -> Expression:
    result: Expression = {}
    for (q_degree, s_degree, n_degree), coefficient in value.items():
        if s_degree not in raw or n_degree not in (0, 1):
            raise ArithmeticError("unsupported squarefree-cubic moment")
        row = raw[s_degree]
        if n_degree:
            row = e_add(
                q_shift(row, 1, guard), e_scale(marked[s_degree], -1, guard), guard
            )
        result = e_add(
            result, e_scale(q_shift(row, q_degree, guard), coefficient, guard), guard
        )
    return result


def _cubic_channel(guard: ResourceGuard) -> dict[str, object]:
    rows, lambda12 = _formal_euler(12, guard)
    expected_g12: SparseEuler = {
        (0, 12, 0): 1,
        (1, 10, 0): -11,
        (2, 8, 0): 45,
        (3, 6, 0): -84,
        (4, 4, 0): 70,
        (5, 2, 0): -21,
        (6, 0, 0): 1,
    }
    if rows[12] != expected_g12:
        raise ArithmeticError("formal g_12 recurrence failed")
    raw = {2 * n: raw_moment(n, guard) for n in range(7)}
    marked = {2 * n: marked_moment(n, guard) for n in range(6)}
    squarefree_g = _sum_squarefree_cubics(rows[12], raw, marked, guard)
    squarefree_lambda = _sum_squarefree_cubics(lambda12, raw, marked, guard)
    expected_g = term(-1)
    expected_lambda = e_add(
        e_add(term(-17), term(1, q=1), guard),
        e_add(e_add(term(-3, delta=1), term(-1, f8=1), guard), term(-1, g10=1), guard),
        guard,
    )
    if squarefree_g != expected_g or squarefree_lambda != expected_lambda:
        raise ArithmeticError("squarefree cubic row failed")
    repeated_g = term(1)
    repeated_lambda = e_add(term(17), term(-6, q=1), guard)
    full_g = e_add(squarefree_g, repeated_g, guard)
    full_lambda = e_add(squarefree_lambda, repeated_lambda, guard)
    expected_full_lambda = e_add(
        term(-5, q=1),
        e_add(e_add(term(-3, delta=1), term(-1, f8=1), guard), term(-1, g10=1), guard),
        guard,
    )
    if full_g or full_lambda != expected_full_lambda:
        raise ArithmeticError("full cubic row failed")
    return {
        "formal_g_12": [
            {"q_power": a, "s_power": b, "coefficient": c}
            for (a, b, _), c in sorted(rows[12].items())
        ],
        "formal_lambda_12_term_count": len(lambda12),
        "moment_inventory": {
            "unmarked_even_degrees": list(range(0, 13, 2)),
            "marked_even_degrees": list(range(0, 11, 2)),
            "highest_level_one_weight": 14,
            "highest_level_two_weight_actually_used": 12,
        },
        "squarefree_G3_over_q_q_minus_1": serialize_expression(squarefree_g),
        "repeated_G3_over_q_q_minus_1": serialize_expression(repeated_g),
        "full_G3_over_q_q_minus_1": serialize_expression(full_g),
        "squarefree_Lambda3_over_q_q_minus_1": serialize_expression(squarefree_lambda),
        "repeated_Lambda3_over_q_q_minus_1": serialize_expression(repeated_lambda),
        "full_Lambda3_over_q_q_minus_1": serialize_expression(full_lambda),
        "repeated_proof": {
            "L^3_per_modulus": "-(q-1)",
            "ordered_L^2*M_per_modulus": "18-6*q",
            "normalized_total": "17-6*q",
        },
        "full_G3_expression": full_g,
        "full_Lambda3_expression": full_lambda,
    }


def _quartic_channel(guard: ResourceGuard) -> dict[str, object]:
    rows: list[SparseSU2] = [{(0, 0): 1}, {(0, 1): 1}]
    for _degree in range(2, 14):
        rows.append(
            su2_add(
                su2_shift(rows[-1], guard, a=1),
                su2_shift(rows[-2], guard, q=1, scale=-1),
                guard,
            )
        )
    total: SparseSU2 = {}
    for row in rows[:13]:
        total = su2_add(total, row, guard)
    left = su2_add(
        su2_shift(total, guard, q=1), su2_shift(total, guard, a=1, scale=-1), guard
    )
    right = su2_shift(rows[12], guard, q=1)
    for row in rows[1:14]:
        right = su2_add(right, su2_shift(row, guard, scale=-1), guard)
    if left != right:
        raise ArithmeticError("quartic SU(2) telescope failed")
    p12_stack = e_add(term(-1), e_scale(level_one_cusp(14), -1, guard), guard)
    sum_p1_p13: Expression = {}
    for degree in range(1, 14):
        if degree % 2 == 0:
            row = e_add(term(-1), e_scale(level_one_cusp(degree + 2), -1, guard), guard)
            sum_p1_p13 = e_add(sum_p1_p13, row, guard)
    squarefree = e_add(
        q_shift(p12_stack, 1, guard), e_scale(sum_p1_p13, -1, guard), guard
    )
    expected_squarefree = e_add(
        e_add(term(6), term(-1, q=1), guard), term(1, delta=1), guard
    )
    if squarefree != expected_squarefree:
        raise ArithmeticError("squarefree quartic row failed")

    q = term(q=1)
    qm1 = e_add(q, term(-1), guard)
    qm2 = e_add(q, term(-2), guard)
    half = Fraction(1, 2)
    counts = {
        "L^4": q,
        "L^3*M": e_multiply(q, qm1, guard),
        "L^2*M^2": e_scale(e_multiply(q, qm1, guard), half, guard),
        "Q^2": e_scale(e_multiply(q, qm1, guard), half, guard),
        "L^2*M*N": e_scale(
            e_multiply(e_multiply(q, qm1, guard), qm2, guard), half, guard
        ),
        "L^2*Q": e_scale(e_multiply(e_multiply(q, q, guard), qm1, guard), half, guard),
    }
    sign_sum = e_scale(qm1, -half, guard)
    contributions = {
        "L^4": e_multiply(counts["L^4"], e_add(term(1), term(-1, q=1), guard), guard),
        "L^3*M": counts["L^3*M"],
        "L^2*M^2": e_multiply(
            counts["L^2*M^2"], e_add(term(13), term(-12, q=1), guard), guard
        ),
        "Q^2": counts["Q^2"],
        "L^2*M*N": e_multiply(
            q,
            e_add(
                e_scale(e_scale(e_multiply(qm1, qm2, guard), half, guard), 7, guard),
                e_scale(sign_sum, 6, guard),
                guard,
            ),
            guard,
        ),
        "L^2*Q": e_multiply(
            q,
            e_add(
                e_scale(e_scale(e_multiply(q, qm1, guard), half, guard), 7, guard),
                e_scale(sign_sum, 6, guard),
                guard,
            ),
            guard,
        ),
    }
    repeated: Expression = {}
    for contribution in contributions.values():
        repeated = e_add(repeated, contribution, guard)
    expected_repeated = e_multiply(
        e_multiply(q, qm1, guard), e_add(q, term(-6), guard), guard
    )
    if repeated != expected_repeated:
        raise ArithmeticError("repeated quartic row failed")
    repeated_normalized = e_add(q, term(-6), guard)
    full = e_add(squarefree, repeated_normalized, guard)
    if full != term(1, delta=1):
        raise ArithmeticError("full quartic row failed")
    return {
        "telescope": "(q-a)*sum_(k=0)^12 P_k=q*P_12-sum_(k=1)^13 P_k",
        "telescope_verified_in": "Z[q,a]",
        "squarefree_G4_over_q_q_minus_1": serialize_expression(squarefree),
        "repeated_strata": [
            {
                "stratum": name,
                "count": serialize_expression(counts[name]),
                "aggregate_g12": serialize_expression(contributions[name]),
            }
            for name in counts
        ],
        "two_sign_sums_per_fixed_L": serialize_expression(sign_sum),
        "repeated_G4": serialize_expression(repeated),
        "repeated_G4_over_q_q_minus_1": serialize_expression(repeated_normalized),
        "full_G4_over_q_q_minus_1": serialize_expression(full),
        "full_G4_expression": full,
    }


def _linear_channel(guard: ResourceGuard) -> dict[str, object]:
    q = term(q=1)
    qm1 = e_add(q, term(-1), guard)
    lambda12 = e_scale(qm1, -1, guard)
    convolution = e_scale(e_multiply(qm1, qm1, guard), 5, guard)
    diagonal = e_scale(qm1, 11, guard)
    choose_two = e_scale(
        e_add(convolution, e_scale(diagonal, -1, guard), guard), Fraction(1, 2), guard
    )
    quadratic_mark = e_scale(e_multiply(q, qm1, guard), Fraction(-1, 2), guard)
    weighted = e_add(
        e_add(choose_two, lambda12, guard),
        e_add(
            quadratic_mark, e_scale(e_multiply(q, lambda12, guard), -1, guard), guard
        ),
        guard,
    )
    expected = e_scale(e_multiply(qm1, e_add(q, term(-3), guard), guard), 3, guard)
    if weighted != expected:
        raise ArithmeticError("linear-modulus weighted row failed")
    normalized = e_add(term(-9), term(3, q=1), guard)
    return {
        "lambda_12_per_linear_modulus": serialize_expression(lambda12),
        "binom_ell_2_mark_per_linear_modulus": serialize_expression(choose_two),
        "quadratic_mark_per_linear_modulus": serialize_expression(quadratic_mark),
        "weighted_row_per_linear_modulus": serialize_expression(weighted),
        "Q1_over_q_q_minus_1": serialize_expression(normalized),
        "Q1_expression": normalized,
    }


def a1_euler(degree: int, guard: ResourceGuard) -> Expression:
    if degree == 0:
        return term(q=1)
    if degree % 2:
        return {}
    return e_add(term(-1), e_scale(level_one_cusp(degree + 2), -1, guard), guard)


def y0_euler(degree: int, guard: ResourceGuard) -> Expression:
    if degree == 0:
        return e_add(term(q=1), term(-1), guard)
    if degree % 2:
        return {}
    return e_add(term(-2), e_scale(level_two_cusp(degree + 2), -1, guard), guard)


def _ambient_boundary(guard: ResourceGuard) -> dict[str, object]:
    boundary: Expression = {}
    rows = []
    dimension_sum = 0
    for index in range(13):
        left = y0_euler(index, guard)
        right = a1_euler(12 - index, guard)
        contribution = e_multiply(left, right, guard)
        boundary = e_add(boundary, contribution, guard)
        dimension = (index + 1) * (13 - index)
        dimension_sum += dimension
        rows.append(
            {
                "i": index,
                "branch_dimension": dimension,
                "contribution": serialize_expression(contribution),
                "vanishes_by_unmarked_central_involution": not contribution,
            }
        )
    if dimension_sum != math.comb(15, 3):
        raise ArithmeticError("Sym^12 branch dimension failed")
    expected = {}
    for item in (
        term(11),
        term(-3, q=1),
        term(4, delta=1),
        term(1, f8=1),
        term(1, g10=1),
        term(-1, q=1, h14=1),
    ):
        expected = e_add(expected, item, guard)
    if boundary != expected:
        raise ArithmeticError("Sym^12 boundary row failed")
    return {
        "geometry": "A_(1,1)(w^1)=Y_0(2) times A_1",
        "branching": "Sym^12(W_1 direct_sum W_1)=direct_sum_(i=0)^12 W_i external_tensor W_(12-i)",
        "dimension_sum": dimension_sum,
        "branch_rows": rows,
        "boundary_expression": serialize_expression(boundary),
        "boundary_formula": "11-3*q+4*Theta_Delta+Theta_(8,2)+Theta_(10,2)-q*Theta_(14,Gamma0(2))",
        "expression": boundary,
    }


def _read_sources(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    values: dict[str, dict[str, object]] = {}
    manifest = []
    for lock in SOURCE_LOCKS:
        deadline.check(f"before {lock['name']} source")
        path = lock["path"]
        if not isinstance(path, Path) or not path.is_file():
            raise RuntimeError(f"missing source lock: {lock['name']}")
        raw = path.read_bytes()
        normalized = _lf_bytes(raw)
        guard.source(len(normalized))
        if _git_blob(raw) != lock["git_blob"] or _lf_sha256(raw) != lock["lf_sha256"]:
            raise RuntimeError(f"source content drift: {lock['name']}")
        value = json.loads(normalized.decode("utf-8"))
        if not isinstance(value, dict) or value.get("schema") != lock["schema"]:
            raise RuntimeError(f"source schema drift: {lock['name']}")
        payload = dict(value)
        claimed = payload.pop(str(lock["payload_key"]), None)
        if claimed != lock["payload_sha256"] or _canonical_sha256(payload) != claimed:
            raise RuntimeError(f"source payload drift: {lock['name']}")
        name = str(lock["name"])
        values[name] = value
        manifest.append(
            {
                key: (
                    _relative(item)
                    if key == "path" and isinstance(item, Path)
                    else item
                )
                for key, item in lock.items()
                if key != "name"
            }
            | {"name": name, "bytes": len(normalized)}
        )
    return values, manifest


def _validate_sources(sources: Mapping[str, Mapping[str, object]]) -> None:
    boundary = sources["reciprocal_boundary"]
    theorem = boundary.get("theorem")
    panel = boundary.get("functional_equation_panel")
    if (
        not isinstance(theorem, Mapping)
        or theorem.get("first_self_referential_endpoint") != 12
        or theorem.get("method_qualification")
        != "this is a boundary for the one-step squarefree-sieve/functional-equation/reciprocity descent, not an impossibility theorem for higher moments"
    ):
        raise RuntimeError("reciprocal-boundary semantics changed")
    row12 = (
        next(
            (
                row
                for row in panel
                if isinstance(row, Mapping) and row.get("endpoint_d") == 12
            ),
            None,
        )
        if isinstance(panel, list)
        else None
    )
    if (
        not isinstance(row12, Mapping)
        or row12.get("C5_formula")
        != "C_5=X_5-(1+C_1+C_2+C_3+C_4), with X_5=Q_5 central"
    ):
        raise RuntimeError("degree-twelve central row changed")
    expected_ladder = {
        "sym6": "T_(6,0)(q)=-4",
        "sym8": "T_(8,0)(q)=-Theta_(8,2)(q)-q-6",
        "sym10": "T_(10,0)(q)=(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7",
    }
    for name, formula in expected_ladder.items():
        row = sources[name].get("theorem")
        if not isinstance(row, Mapping) or row.get("marked_stack_trace") != formula:
            raise RuntimeError(f"{name} ladder theorem changed")
    genus1 = sources["genus1"].get("all_q_moment_theorem")
    explicit = (
        genus1.get("explicit_stack_sums") if isinstance(genus1, Mapping) else None
    )
    if (
        not isinstance(explicit, Mapping)
        or explicit.get("W_12")
        != "132*q^7-297*q^5-275*q^4-154*q^3-54*q^2-11*q-1-11*q*Theta_12(q)"
    ):
        raise RuntimeError("genus-one W_12 theorem changed")
    marked = sources["marked_tower"].get("theorem")
    if (
        not isinstance(marked, Mapping)
        or marked.get("theorem")
        != "J_(2n)/(q*(q-1))=C_n*q^n*(q-1)-sum_(j=1)^n c(n,j)*q^(n-j)*(2+Theta_(2j+2,Gamma0(2))(q))"
    ):
        raise RuntimeError("marked all-weight theorem changed")
    ambient = sources["ambient_ladder"].get("exact_proof")
    if (
        not isinstance(ambient, Mapping)
        or ambient.get("geometry")
        != "A_(1,1)(w^1)=Y_0(2) times A_1; the marked odd theta characteristic distinguishes the factors"
    ):
        raise RuntimeError("ambient geometry changed")
    r6 = sources["r6_reconnaissance"].get("low_moment_no_go")
    if (
        not isinstance(r6, Mapping)
        or "do not determine mean(R6)" not in str(r6.get("logical_boundary"))
        or "chi_(12,0)" in r6.get("R6_irreducible_coefficients", {})
    ):
        raise RuntimeError("R6 no-go semantics changed")


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()
    sources, manifest = _read_sources(guard, deadline)
    _validate_sources(sources)
    cubic = _cubic_channel(guard)
    quartic = _quartic_channel(guard)
    linear = _linear_channel(guard)
    lower: Expression = {}
    lower = e_add(lower, e_scale(cubic["full_G3_expression"], -1, guard), guard)
    lower = e_add(
        lower, e_scale(q_shift(cubic["full_G3_expression"], 1, guard), -1, guard), guard
    )
    lower = e_add(lower, e_scale(quartic["full_G4_expression"], -1, guard), guard)
    lower = e_add(lower, cubic["full_Lambda3_expression"], guard)
    lower = e_add(lower, linear["Q1_expression"], guard)
    expected_lower: Expression = {}
    for item in (
        term(-9),
        term(-2, q=1),
        term(-4, delta=1),
        term(-1, f8=1),
        term(-1, g10=1),
    ):
        expected_lower = e_add(expected_lower, item, guard)
    if lower != expected_lower:
        raise ArithmeticError("degree-twelve lower residual failed")
    marked_open = e_add(term(central=1), lower, guard)
    boundary = _ambient_boundary(guard)
    ambient = e_add(marked_open, boundary["expression"], guard)
    expected_ambient = e_add(
        e_add(term(central=1), term(2), guard),
        e_add(term(-5, q=1), term(-1, q=1, h14=1), guard),
        guard,
    )
    if ambient != expected_ambient:
        raise ArithmeticError("degree-twelve ambient inventory failed")
    deadline.check("before fixture assembly")
    for packet in (cubic, quartic, linear, boundary):
        packet.pop("full_G3_expression", None)
        packet.pop("full_Lambda3_expression", None)
        packet.pop("full_G4_expression", None)
        packet.pop("Q1_expression", None)
        packet.pop("expression", None)
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym12_arithmetic_inventory.v1",
        "status": "PROVED_EXACT_SOURCE_RELATIVE_ONE_SCALAR_CLOSURE",
        "scope": {
            "base_fields": "every finite field F_q of odd characteristic",
            "target": "marked curve-open and ambient V_(12,0)=Sym^12(V) virtual traces",
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "proof_mode": "bounded exact coefficient, Euler, marking, and boundary algebra",
        },
        "definitions": {
            "H_12": "sum_(deg f=12, f monic squarefree) mu(f)*Q_5(f), where Q_5(f) is the central coefficient of the completed even quadratic Dirichlet polynomial",
            "Hhat_12": "H_12/(q*(q-1))",
            "T_(12,0)": "sum_(D monic squarefree quintic) r_D(12)/(q*(q-1))",
            "normalization": "r_D(12)=q^6*chi_(12,0)(U_D)",
        },
        "degree_twelve_dependency": {
            "preclosure_identity": "T_(12,0)=Hhat_12-(q+1)*G3hat-G4hat+Lambda3hat+Q1hat",
            "lower_residual_expression": serialize_expression(lower),
            "marked_open_expression": serialize_expression(marked_open),
            "marked_open_formula": "T_(12,0)=Hhat_12-2*q-9-4*Theta_Delta-Theta_(8,2)-Theta_(10,2)",
            "necessary_and_sufficient_relative_input": "one scalar Hhat_12(q)",
            "minimality_certificate": {
                "coefficient_of_Hhat_12": 1,
                "remaining_unknown_dimension_over_the_locked_input_ring": 1,
                "meaning": "necessary and sufficient inside the locked one-step dependency graph; an additional arithmetic theorem could still evaluate or relate Hhat_12",
            },
        },
        "cubic_channel": cubic,
        "quartic_channel": quartic,
        "linear_modulus_channel": linear,
        "ambient_boundary": boundary,
        "ambient_inventory": {
            "expression": serialize_expression(ambient),
            "formula": "Tr(F_q,e_c(A_2(w^1),V_(12,0)))=Hhat_12+2-5*q-q*Theta_(14,Gamma0(2))(q)",
            "channel_cancellations": {
                "Theta_Delta": "-4+4=0",
                "Theta_(8,2)": "-1+1=0",
                "Theta_(10,2)": "-1+1=0",
            },
            "new_family_specific_input": "Hhat_12(q)",
            "standard_boundary_input": "the full weight-14 Gamma_0(2) cuspidal Frobenius trace",
        },
        "r6_and_ladder_boundary": {
            "exact_character_level_statement": "chi_(12,0) is absent from the irreducible support of R6 and from the Sym6/8/10 target characters, so their pointwise linear span does not contain chi_(12,0)",
            "arithmetic_firewall": "this character-basis fact does not rule out a separate family-specific relation among their means",
            "R6_role": "independent reconnaissance target; its locked mean gap neither evaluates nor enlarges the one-scalar Hhat_12 closure",
        },
        "theorem_target": {
            "paper_sized_statement": "The marked Sym^12 reciprocal trace is affinely equivalent to the normalized central Q_5 aggregate Hhat_12; all lower Euler rows are explicit, and after adding the decomposable boundary every inherited Delta, weight-8 level-2, and weight-10 level-2 channel cancels.",
            "next_exact_arithmetic_task": "evaluate Hhat_12(q), equivalently the central completed-coefficient average over squarefree degree-12 quadratic characters; then both marked and ambient Sym^12 traces close immediately",
        },
        "firewalls": [
            "This is a one-scalar dependency and obstruction theorem, not an evaluation of Hhat_12 or a closed Sym^12 trace formula.",
            "Minimality is relative to the source-locked one-step sieve/functional-equation/reciprocity graph, not a mathematical impossibility theorem.",
            "The weight-14 Gamma_0(2) trace is standard boundary arithmetic, but a numerical ambient value still requires that trace and Hhat_12.",
            "No external novelty, motivic isomorphism, individual cohomology decomposition, memberwise sign, RH/GRH criterion, or compatible system is claimed.",
        ],
        "source_manifest": manifest,
        "resource_contract": {
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operation_counts": dict(sorted(guard.operation_counts.items())),
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
            "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_source_bytes": guard.source_bytes,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "integers and exact rational intermediates only; no floating point in mathematical algebra",
        },
        "packet_manifest": {
            "producer": _relative(Path(__file__)),
            "note": _relative(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "producer_lf_sha256": _lf_sha256(Path(__file__).read_bytes()),
            "note_lf_sha256": _lf_sha256(NOTE_PATH.read_bytes()),
            "test_lf_sha256": _lf_sha256(TEST_PATH.read_bytes()),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def _encoded_fixture() -> bytes:
    return (
        json.dumps(build_fixture(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    ).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="verify the committed JSON"
    )
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    encoded = _encoded_fixture()
    if len(encoded) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output byte cap exceeded")
    if args.check:
        if not args.output.is_file() or args.output.read_bytes() != encoded:
            raise SystemExit("fixture drift")
        print(f"fixture OK: {args.output}")
        return
    args.output.write_bytes(encoded)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
