#!/usr/bin/env python3
"""Bounded exact proof replay for the marked genus-two Sym^10 trace.

For every odd prime power q, the packet proves

    T_(10,0)(q)
      = (q-1)*Theta_Delta(q) - Theta_f(q) - Theta_g(q) - q - 7,

where f and g are the unique weight-eight and weight-ten newforms on
Gamma_0(2).  The proof is a degree-ten Mobius/Euler reduction.  Its new
quartic row is derived by an elliptic-stack telescope and an exhaustive
six-stratum repeated-factor calculation.  No finite field is enumerated by
the proof replay; three frozen prime-field coefficient laws are loaded only
after the symbolic proof and the modular-form certificate have closed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

Poly = tuple[Fraction, ...]
SparseMonomial = tuple[int, int, int]  # q, s (or a), N
SparsePolynomial = dict[SparseMonomial, int]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "genus2_sym10_marked_trace_average.json"
NOTE_PATH = HERE / "GENUS2_SYM10_MARKED_TRACE_AVERAGE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym10_marked_trace_average.py"

GENUS1_JSON_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_NOTE_PATH = HERE / "GENUS1_CUBIC_FAMILY_LAWS.md"
SYM8_JSON_PATH = HERE / "genus2_sym8_marked_trace_average.json"
SYM8_NOTE_PATH = HERE / "GENUS2_SYM8_MARKED_TRACE_AVERAGE.md"
TOWER_JSON_PATH = HERE / "genus1_marked_2torsion_moment_tower.json"
TOWER_NOTE_PATH = HERE / "GENUS1_MARKED_2TORSION_MOMENT_TOWER.md"
BALANCED_JSON_PATH = HERE / "balanced_control_family_scan.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "genus1": {
        "commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
        "json_path": GENUS1_JSON_PATH,
        "json_git_blob": "49cde8d3a1881d0d626e4f288abc53f370a33244",
        "json_lf": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
        "payload": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
        "note_path": GENUS1_NOTE_PATH,
        "note_git_blob": "c6c9c24d941c25846a2252436e9cd3efd25295fd",
        "note_lf": "aad40573c6378c919ee6659bcd1c4b89a8981621c61feb0dcde9911d127c6b9f",
        "role": "all-q unmarked elliptic-stack moment theorem",
    },
    "sym8": {
        "commit": "dc63f02d0897e10936ef0767a1c8e6f15ac49e06",
        "json_path": SYM8_JSON_PATH,
        "json_git_blob": "1dece87cbec2731f858e3dd38d2ceb0a96959d53",
        "json_lf": "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233",
        "payload": "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae",
        "note_path": SYM8_NOTE_PATH,
        "note_git_blob": "f882ff91ba28421cf20bfe806a28912c9df71f40",
        "note_lf": "96a31bef0bd1f38764c8fb09edcd4585bffb6eea88e8141bcaac0ca808d01939",
        "role": "audited marked-model normalization and Y_0(2) bridge",
    },
    "tower": {
        "commit": "446c889795a05fd378fed93d443c8887b6e25794",
        "json_path": TOWER_JSON_PATH,
        "json_git_blob": "19c82e8af8aea133eb53c6843c7f45c6ca30b693",
        "json_lf": "8f254196d3aa73f440a18f22da0bfa3f54307db7c68e7fa3faf934de60cbbf3e",
        "payload": "d6861d94296bd37bba503f87cfa4b00b51a3a2d4f62ae01c707cc45a08588cde",
        "note_path": TOWER_NOTE_PATH,
        "note_git_blob": "92788c783ecf27ed85392a3fac64a217cd29b6bf",
        "note_lf": "bca19ccd65ded25a87d2a13e3347d313498f78bd5f61b7953c37734e0bee921b",
        "role": "all-q marked two-torsion moments through J_10",
    },
    "balanced": {
        "commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
        "json_path": BALANCED_JSON_PATH,
        "json_git_blob": "377c8c03d6a9ccf5a505a9b1a19acc360c59ff44",
        "json_lf": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
        "role": "held-out q=3,5,7 joint coefficient atoms only",
    },
}
THEOREM_SOURCE_NAMES = ("genus1", "sym8", "tower")
HELD_OUT_SOURCE_NAMES = ("balanced",)

MAX_EXACT_OPERATIONS = 32_768
MAX_HELD_OUT_ATOMS = 300
MAX_RECIPROCAL_UPDATES = 3_000
MAX_FOURIER_DEGREE = 9
MAX_WALL_SECONDS = 10.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    held_out_atoms: int = 0
    reciprocal_updates: int = 0

    def operation(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount

    def atom(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("atom increment must be nonnegative")
        if self.held_out_atoms + amount > MAX_HELD_OUT_ATOMS:
            raise RuntimeError("held-out atom cap exceeded")
        self.held_out_atoms += amount

    def reciprocal(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("reciprocal-update increment must be nonnegative")
        if self.reciprocal_updates + amount > MAX_RECIPROCAL_UPDATES:
            raise RuntimeError("reciprocal-update cap exceeded")
        self.reciprocal_updates += amount


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
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


def _lf_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _load_sources(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
    if not names or len(set(names)) != len(names):
        raise ValueError("source names must be nonempty and distinct")
    result: dict[str, dict[str, object]] = {}
    for name in names:
        lock = SOURCE_LOCKS.get(name)
        if lock is None:
            raise ValueError(f"unknown source: {name}")
        json_path = lock["json_path"]
        if not isinstance(json_path, Path) or _lf_sha256(json_path) != lock["json_lf"]:
            raise RuntimeError(f"source JSON lock failed: {name}")
        note_path = lock.get("note_path")
        if note_path is not None and (
            not isinstance(note_path, Path) or _lf_sha256(note_path) != lock["note_lf"]
        ):
            raise RuntimeError(f"source note lock failed: {name}")
        value = json.loads(json_path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not a JSON object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != lock["payload"] or claimed != _canonical_sha256(payload):
            raise ValueError(f"source payload lock failed: {name}")
        result[name] = value
    return result


def _trim(coefficients: list[Fraction]) -> Poly:
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients or [Fraction(0)])


def poly(*coefficients: int | Fraction) -> Poly:
    return _trim([Fraction(value) for value in coefficients])


def p_add(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    size = max(len(left), len(right))
    guard.operation(size)
    return _trim(
        [
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
            for index in range(size)
        ]
    )


def p_scale(value: Poly, scalar: int | Fraction, guard: ResourceGuard) -> Poly:
    guard.operation(len(value))
    factor = Fraction(scalar)
    return _trim([factor * coefficient for coefficient in value])


def p_mul(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    guard.operation(len(left) * len(right))
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return _trim(result)


def p_sub(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    return p_add(left, p_scale(right, -1, guard), guard)


def p_pow(value: Poly, exponent: int, guard: ResourceGuard) -> Poly:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    result = poly(1)
    for _ in range(exponent):
        result = p_mul(result, value, guard)
    return result


def p_eval(value: Poly, q_value: int) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(value):
        result = result * q_value + coefficient
    return result


def _pairs(value: Poly) -> list[list[int]]:
    return [[entry.numerator, entry.denominator] for entry in value]


def _assert_poly(actual: Poly, expected: Poly, label: str) -> None:
    if actual != expected:
        raise ArithmeticError(f"{label} failed: {actual!r} != {expected!r}")


@dataclass(frozen=True)
class TraceExpression:
    """A linear expression in Delta, f_(8,2), and g_(10,2)."""

    tate: Poly = (Fraction(0),)
    delta: Poly = (Fraction(0),)
    f8: Poly = (Fraction(0),)
    g10: Poly = (Fraction(0),)


def trace(
    *,
    tate: Poly | None = None,
    delta: Poly | None = None,
    f8: Poly | None = None,
    g10: Poly | None = None,
) -> TraceExpression:
    return TraceExpression(
        tate=poly(0) if tate is None else tate,
        delta=poly(0) if delta is None else delta,
        f8=poly(0) if f8 is None else f8,
        g10=poly(0) if g10 is None else g10,
    )


def t_add(
    left: TraceExpression, right: TraceExpression, guard: ResourceGuard
) -> TraceExpression:
    return TraceExpression(
        p_add(left.tate, right.tate, guard),
        p_add(left.delta, right.delta, guard),
        p_add(left.f8, right.f8, guard),
        p_add(left.g10, right.g10, guard),
    )


def t_scale_poly(
    value: TraceExpression, factor: Poly, guard: ResourceGuard
) -> TraceExpression:
    return TraceExpression(
        p_mul(value.tate, factor, guard),
        p_mul(value.delta, factor, guard),
        p_mul(value.f8, factor, guard),
        p_mul(value.g10, factor, guard),
    )


def t_scale(
    value: TraceExpression, factor: int | Fraction, guard: ResourceGuard
) -> TraceExpression:
    return TraceExpression(
        p_scale(value.tate, factor, guard),
        p_scale(value.delta, factor, guard),
        p_scale(value.f8, factor, guard),
        p_scale(value.g10, factor, guard),
    )


def _trace_object(value: TraceExpression) -> dict[str, list[list[int]]]:
    return {
        "tate": _pairs(value.tate),
        "Theta_Delta": _pairs(value.delta),
        "Theta_(8,2)": _pairs(value.f8),
        "Theta_(10,2)": _pairs(value.g10),
    }


def sp_add(
    left: SparsePolynomial, right: SparsePolynomial, guard: ResourceGuard
) -> SparsePolynomial:
    guard.operation(len(left) + len(right))
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def sp_shift(
    value: SparsePolynomial,
    guard: ResourceGuard,
    *,
    q_degree: int = 0,
    s_degree: int = 0,
    n_degree: int = 0,
    scale: int = 1,
) -> SparsePolynomial:
    if min(q_degree, s_degree, n_degree) < 0:
        raise ValueError("sparse exponent shift must be nonnegative")
    guard.operation(len(value))
    return {
        (q_exp + q_degree, s_exp + s_degree, n_exp + n_degree): coefficient * scale
        for (q_exp, s_exp, n_exp), coefficient in value.items()
        if coefficient * scale
    }


def _serialize_sparse(value: SparsePolynomial) -> list[dict[str, int]]:
    return [
        {
            "q_degree": monomial[0],
            "s_degree": monomial[1],
            "N_degree": monomial[2],
            "coefficient": value[monomial],
        }
        for monomial in sorted(value)
    ]


def _formal_euler_certificate(
    guard: ResourceGuard,
) -> tuple[dict[str, object], SparsePolynomial, SparsePolynomial]:
    one: SparsePolynomial = {(0, 0, 0): 1}
    g_rows = [one, {(0, 1, 0): -1}]
    for degree in range(2, 11):
        g_rows.append(
            sp_add(
                sp_shift(g_rows[degree - 1], guard, s_degree=1, scale=-1),
                sp_shift(g_rows[degree - 2], guard, q_degree=1, scale=-1),
                guard,
            )
        )
    expected_g10: SparsePolynomial = {
        (0, 10, 0): 1,
        (1, 8, 0): -9,
        (2, 6, 0): 28,
        (3, 4, 0): -35,
        (4, 2, 0): 15,
        (5, 0, 0): -1,
    }
    if g_rows[10] != expected_g10:
        raise ArithmeticError("formal g_10 recurrence failed")

    lambda10: SparsePolynomial = {}
    for marked_degree in range(1, 11):
        if marked_degree % 2:
            term = sp_shift(g_rows[10 - marked_degree], guard, s_degree=1, scale=-1)
        else:
            term = sp_shift(g_rows[10 - marked_degree], guard, n_degree=1, scale=-1)
        lambda10 = sp_add(lambda10, term, guard)
    expected_lambda10: SparsePolynomial = {
        (0, 10, 0): 1,
        (0, 8, 0): 1,
        (1, 8, 0): -8,
        (0, 8, 1): -1,
        (0, 6, 0): 1,
        (1, 6, 0): -6,
        (2, 6, 0): 21,
        (0, 6, 1): -1,
        (1, 6, 1): 7,
        (0, 4, 0): 1,
        (1, 4, 0): -4,
        (2, 4, 0): 10,
        (3, 4, 0): -20,
        (0, 4, 1): -1,
        (1, 4, 1): 5,
        (2, 4, 1): -15,
        (0, 2, 0): 1,
        (1, 2, 0): -2,
        (2, 2, 0): 3,
        (3, 2, 0): -4,
        (4, 2, 0): 5,
        (0, 2, 1): -1,
        (1, 2, 1): 3,
        (2, 2, 1): -6,
        (3, 2, 1): 10,
        (0, 0, 1): -1,
        (1, 0, 1): 1,
        (2, 0, 1): -1,
        (3, 0, 1): 1,
        (4, 0, 1): -1,
    }
    if lambda10 != expected_lambda10:
        raise ArithmeticError("formal lambda_10 recurrence failed")
    return (
        {
            "ring": "Z[q,s,N]",
            "recurrence": "g_0=1; g_1=-s; g_n=-s*g_(n-1)-q*g_(n-2)",
            "marked_recurrence": (
                "lambda_10=-sum_(1<=m<=10)p_m*g_(10-m), "
                "p_m=s for odd m and N for even m"
            ),
            "g_10": _serialize_sparse(g_rows[10]),
            "lambda_10": _serialize_sparse(lambda10),
        },
        g_rows[10],
        lambda10,
    )


def _validate_source_semantics(sources: Mapping[str, Mapping[str, object]]) -> None:
    genus1 = sources["genus1"].get("all_q_moment_theorem")
    if not isinstance(genus1, dict):
        raise TypeError("genus-one theorem block is missing")
    expected_unmarked = {
        "W_0": "q",
        "W_2": "q^2-1",
        "W_4": "2*q^3-3*q-1",
        "W_6": "5*q^4-9*q^2-5*q-1",
        "W_8": "14*q^5-28*q^3-20*q^2-7*q-1",
        "W_10": "42*q^6-90*q^4-75*q^3-35*q^2-9*q-1-Theta_12(q)",
    }
    rows = genus1.get("explicit_stack_sums")
    if not isinstance(rows, dict) or any(
        rows.get(name) != formula for name, formula in expected_unmarked.items()
    ):
        raise ValueError("source unmarked moment rows changed")

    sym8 = sources["sym8"].get("marked_cubic_sixth_moment")
    if not isinstance(sym8, dict) or sym8.get("model_stack_bridge") != (
        "J_6=q*(q-1)*sum_[(E,T)]a_E^6/|Aut_q(E,T)|, T in E[2](F_q)-{0}"
    ):
        raise ValueError("source marked-stack normalization changed")

    tower = sources["tower"].get("theorem")
    if not isinstance(tower, dict):
        raise TypeError("marked tower theorem block is missing")
    explicit = tower.get("explicit_rows_through_n_5")
    if not isinstance(explicit, list) or len(explicit) < 6:
        raise ValueError("marked tower explicit rows are missing")
    expected_j10 = (
        "J_10=q*(q-1)*(42*q^6-42*q^5-180*q^4-150*q^3-70*q^2-18*q-2"
        "-35*q^2*Theta_f(q)-9*q*Theta_g(q)-2*Theta_Delta(q))"
    )
    expected_j8 = (
        "J_8=q*(q-1)*(14*q^5-14*q^4-56*q^3-40*q^2-14*q-2-7*q*Theta_f(q)-Theta_g(q))"
    )
    if explicit[4].get("formula") != expected_j8:
        raise ValueError("source J_8 row changed")
    if explicit[5].get("formula") != expected_j10:
        raise ValueError("source J_10 row changed")
    if tower.get("trace_convention") != (
        "Theta_(k,Gamma0(2))(p^r) is the full cuspidal Frobenius-power "
        "trace, summed over underlying normalized newforms with oldform "
        "multiplicity; it is not generally a single Fourier coefficient"
    ):
        raise ValueError("source prime-power trace convention changed")


def _moment_rows() -> tuple[dict[int, TraceExpression], dict[int, TraceExpression]]:
    raw = {
        0: trace(tate=poly(0, 1)),
        2: trace(tate=poly(-1, 0, 1)),
        4: trace(tate=poly(-1, -3, 0, 2)),
        6: trace(tate=poly(-1, -5, -9, 0, 5)),
        8: trace(tate=poly(-1, -7, -20, -28, 0, 14)),
        10: trace(tate=poly(-1, -9, -35, -75, -90, 0, 42), delta=poly(-1)),
    }
    marked = {
        0: trace(tate=poly(-1, 1)),
        2: trace(tate=poly(-2, -1, 1)),
        4: trace(tate=poly(-2, -6, -2, 2)),
        6: trace(tate=poly(-2, -10, -18, -5, 5), f8=poly(-1)),
        8: trace(
            tate=poly(-2, -14, -40, -56, -14, 14),
            f8=poly(0, -7),
            g10=poly(-1),
        ),
        10: trace(
            tate=poly(-2, -18, -70, -150, -180, -42, 42),
            delta=poly(-2),
            f8=poly(0, 0, -35),
            g10=poly(0, -9),
        ),
    }
    return raw, marked


def _sum_sparse_over_squarefree_cubics(
    value: SparsePolynomial,
    raw: Mapping[int, TraceExpression],
    marked: Mapping[int, TraceExpression],
    guard: ResourceGuard,
) -> TraceExpression:
    result = trace()
    q_poly = poly(0, 1)
    for (q_degree, s_degree, n_degree), coefficient in value.items():
        if s_degree not in raw or n_degree not in (0, 1):
            raise ValueError("unsupported cubic moment in sparse summation")
        row = raw[s_degree]
        if n_degree == 1:
            row = t_add(
                t_scale_poly(row, q_poly, guard),
                t_scale(marked[s_degree], -1, guard),
                guard,
            )
        factor = p_scale(p_pow(q_poly, q_degree, guard), coefficient, guard)
        result = t_add(result, t_scale_poly(row, factor, guard), guard)
    return result


def _quartic_channel(guard: ResourceGuard) -> dict[str, object]:
    # Verify the character telescope in Z[q,a].
    p_rows: list[SparsePolynomial] = [{(0, 0, 0): 1}, {(0, 1, 0): 1}]
    for degree in range(2, 12):
        p_rows.append(
            sp_add(
                sp_shift(p_rows[degree - 1], guard, s_degree=1),
                sp_shift(p_rows[degree - 2], guard, q_degree=1, scale=-1),
                guard,
            )
        )
    sum_p: SparsePolynomial = {}
    for row in p_rows[:11]:
        sum_p = sp_add(sum_p, row, guard)
    left = sp_add(
        sp_shift(sum_p, guard, q_degree=1),
        sp_shift(sum_p, guard, s_degree=1, scale=-1),
        guard,
    )
    right = sp_shift(p_rows[10], guard, q_degree=1)
    for row in p_rows[1:12]:
        right = sp_add(right, sp_shift(row, guard, scale=-1), guard)
    if left != right:
        raise ArithmeticError("quartic SU(2) telescope failed")

    # On M_1: P_0 has stack sum q, odd P_k vanish, and positive even
    # P_k have sum -1-Theta_(k+2).  Only k=10 sees Delta here.
    p10_stack = trace(tate=poly(-1), delta=poly(-1))
    positive_1_through_11_stack = trace(tate=poly(-5), delta=poly(-1))
    squarefree_normalized = t_add(
        t_scale_poly(p10_stack, poly(0, 1), guard),
        t_scale(positive_1_through_11_stack, -1, guard),
        guard,
    )
    expected_squarefree = trace(tate=poly(5, -1), delta=poly(1, -1))
    if squarefree_normalized != expected_squarefree:
        raise ArithmeticError("squarefree quartic stack row failed")

    q = poly(0, 1)
    qm1 = poly(-1, 1)
    qm2 = poly(-2, 1)
    half = Fraction(1, 2)
    count_l4 = q
    count_l3m = p_mul(q, qm1, guard)
    count_l2m2 = p_scale(count_l3m, half, guard)
    count_q2 = p_scale(count_l3m, half, guard)
    count_l2mn = p_scale(p_mul(count_l3m, qm2, guard), half, guard)
    count_l2q = p_scale(p_mul(p_mul(q, q, guard), qm1, guard), half, guard)
    total_count = poly(0)
    for count in (
        count_l4,
        count_l3m,
        count_l2m2,
        count_q2,
        count_l2mn,
        count_l2q,
    ):
        total_count = p_add(total_count, count, guard)
    _assert_poly(total_count, poly(0, 0, 0, 1), "repeated quartic count")

    sign_sum_per_l = p_scale(qm1, -half, guard)
    contributions = {
        "L^4": p_mul(count_l4, poly(1, -1), guard),
        "L^3*M": count_l3m,
        "L^2*M^2": p_mul(count_l2m2, poly(11, -10), guard),
        "Q^2": count_q2,
        "L^2*M*N": p_mul(
            q,
            p_add(
                p_scale(p_scale(p_mul(qm1, qm2, guard), half, guard), 6, guard),
                p_scale(sign_sum_per_l, 5, guard),
                guard,
            ),
            guard,
        ),
        "L^2*Q": p_mul(
            q,
            p_add(
                p_scale(p_scale(p_mul(q, qm1, guard), half, guard), 6, guard),
                p_scale(sign_sum_per_l, 5, guard),
                guard,
            ),
            guard,
        ),
    }
    repeated_total = poly(0)
    for contribution in contributions.values():
        repeated_total = p_add(repeated_total, contribution, guard)
    expected_repeated = p_mul(p_mul(q, qm1, guard), poly(-5, 1), guard)
    _assert_poly(repeated_total, expected_repeated, "repeated quartic row")

    total_normalized = t_add(
        squarefree_normalized,
        trace(tate=poly(-5, 1)),
        guard,
    )
    expected_total = trace(delta=poly(1, -1))
    if total_normalized != expected_total:
        raise ArithmeticError("full quartic row failed")

    return {
        "affine_action": "(u,b).h(X)=u^(-4)*h(u*X+b)",
        "quotient_stack_equivalence": (
            "[H_4^sf/(G_m semidirect G_a)] is the stack of ordered "
            "triples (E,O,P) with P!=O"
        ),
        "ordered_points": "the two rational points at infinity are O and P",
        "elliptic_character_recurrence": "P_0=1; P_1=a; P_k=a*P_(k-1)-q*P_(k-2)",
        "g_10_identity": "g_10=sum_(k=0)^10 P_k(a,q)",
        "telescope": "(q-a)*sum_(k=0)^10 P_k=q*P_10-sum_(k=1)^11 P_k",
        "telescope_verified_in": "Z[q,a]",
        "squarefree_model_stack_bridge": (
            "sum_(h monic squarefree quartic)F(E_h)="
            "q*(q-1)*sum_E (#E(F_q)-1)*F(E)/|Aut_q(E)|"
        ),
        "squarefree_G4_over_q_q_minus_1": _trace_object(squarefree_normalized),
        "repeated_strata": [
            {
                "stratum": name,
                "count": _pairs(count),
                "aggregate_g10": _pairs(contributions[name]),
            }
            for name, count in (
                ("L^4", count_l4),
                ("L^3*M", count_l3m),
                ("L^2*M^2", count_l2m2),
                ("Q^2", count_q2),
                ("L^2*M*N", count_l2mn),
                ("L^2*Q", count_l2q),
            )
        ],
        "repeated_count": _pairs(total_count),
        "two_sign_sums_per_fixed_L": {
            "unordered_distinct_linear_pair": _pairs(sign_sum_per_l),
            "irreducible_quadratic": _pairs(sign_sum_per_l),
            "proof": (
                "the first is half of (sum_(x!=0)chi(x))^2-"
                "sum_(x!=0)chi(x)^2; the second is half the character "
                "sum on F_(q^2)\\F_q"
            ),
        },
        "repeated_G4": _pairs(repeated_total),
        "full_G4_over_q_q_minus_1": _trace_object(expected_total),
    }


def _linear_modulus_channel(guard: ResourceGuard) -> dict[str, object]:
    q = poly(0, 1)
    qm1 = poly(-1, 1)
    # p_m=sum_L chi_h(L)^m is 0 for odd m and q-1 for positive even m.
    lambda10 = p_scale(qm1, -1, guard)
    convolution = poly(0)
    for index in range(1, 10):
        left = poly(0) if index % 2 else qm1
        right = poly(0) if (10 - index) % 2 else qm1
        convolution = p_add(convolution, p_mul(left, right, guard), guard)
    diagonal = p_scale(qm1, 9, guard)
    choose_two = p_scale(p_sub(convolution, diagonal, guard), Fraction(1, 2), guard)
    expected_choose_two = p_scale(
        p_mul(qm1, poly(-13, 4), guard), Fraction(1, 2), guard
    )
    _assert_poly(choose_two, expected_choose_two, "two-linear marking")
    quadratic_mark = p_scale(qm1, Fraction(1, 2), guard)
    # binom(ell+1,2)=binom(ell,2)+ell.
    weighted_fixed = p_add(
        p_add(choose_two, lambda10, guard),
        p_add(quadratic_mark, p_scale(p_mul(q, lambda10, guard), -1, guard), guard),
        guard,
    )
    expected_fixed = p_mul(qm1, poly(-7, 3), guard)
    _assert_poly(weighted_fixed, expected_fixed, "linear-modulus weighted row")
    all_linear = p_mul(q, weighted_fixed, guard)
    return {
        "power_sums": "p_m=0 for odd m and p_m=q-1 for positive even m",
        "lambda_10": _pairs(lambda10),
        "binom_ell_2_lambda_10": _pairs(choose_two),
        "quadratic_factor_mark_kappa_10": _pairs(quadratic_mark),
        "binom_ell_plus_1_2_identity": "binom(ell+1,2)=binom(ell,2)+ell",
        "fixed_modulus_weighted_row": _pairs(weighted_fixed),
        "Q_1": _pairs(all_linear),
    }


def _build_symbolic_theorem(
    sources: Mapping[str, Mapping[str, object]], guard: ResourceGuard
) -> dict[str, object]:
    _validate_source_semantics(sources)
    formal_certificate, g10, lambda10 = _formal_euler_certificate(guard)
    raw, marked = _moment_rows()

    squarefree_g3 = _sum_sparse_over_squarefree_cubics(g10, raw, marked, guard)
    expected_squarefree_g3 = trace(tate=poly(-1), delta=poly(-1))
    if squarefree_g3 != expected_squarefree_g3:
        raise ArithmeticError("squarefree cubic g_10 row failed")
    full_g3 = t_add(squarefree_g3, trace(tate=poly(1)), guard)
    if full_g3 != trace(delta=poly(-1)):
        raise ArithmeticError("full cubic G_3 row failed")

    squarefree_lambda = _sum_sparse_over_squarefree_cubics(lambda10, raw, marked, guard)
    expected_squarefree_lambda = trace(
        tate=poly(-14, 1), delta=poly(-1), f8=poly(-1), g10=poly(-1)
    )
    if squarefree_lambda != expected_squarefree_lambda:
        raise ArithmeticError("squarefree cubic lambda_10 row failed")
    # L^3 contributes -(q-1) per L, while each ordered L^2*M contributes
    # 15-5q.  After division by q(q-1), the repeated row is 14-5q.
    repeated_lambda_normalized = trace(tate=poly(14, -5))
    full_lambda = t_add(squarefree_lambda, repeated_lambda_normalized, guard)
    expected_full_lambda = trace(
        tate=poly(0, -4), delta=poly(-1), f8=poly(-1), g10=poly(-1)
    )
    if full_lambda != expected_full_lambda:
        raise ArithmeticError("full cubic lambda_10 row failed")

    q = poly(0, 1)
    qm1 = poly(-1, 1)
    q_factor = p_mul(q, qm1, guard)
    degree_two_squarefree = q_factor
    degree_two_repeated = p_scale(q_factor, -1, guard)
    degree_two_total = p_add(degree_two_squarefree, degree_two_repeated, guard)
    _assert_poly(degree_two_total, poly(0), "G_2 cancellation")

    quartic = _quartic_channel(guard)
    quartic_total = trace(delta=poly(1, -1))
    linear = _linear_modulus_channel(guard)
    q1_normalized = trace(tate=poly(-7, 3))

    # (q-1)(G1+G2)-G3-G4+Lambda3+Q1, with G1=G2=0.
    final = trace()
    final = t_add(final, t_scale(full_g3, -1, guard), guard)
    final = t_add(final, t_scale(quartic_total, -1, guard), guard)
    final = t_add(final, full_lambda, guard)
    final = t_add(final, q1_normalized, guard)
    expected_final = trace(
        tate=poly(-7, -1), delta=poly(-1, 1), f8=poly(-1), g10=poly(-1)
    )
    if final != expected_final:
        raise ArithmeticError("final Sym10 marked trace failed")

    return {
        "formal_euler_recurrence_certificate": formal_certificate,
        "degree_ten_reciprocal_reduction": {
            "reciprocal_euler_coefficient": (
                "r_D(10)=sum_(f monic squarefree,deg f=10)mu(f)*(D/f)"
            ),
            "squarefree_quintic_sieve": (
                "S_5=C_5-(q-ell)*C_3+(binom(ell+1,2)+k-q*ell)*C_1"
            ),
            "even_functional_equation": ("C_5=(q-1)*(1+C_1+C_2+C_3)-C_4"),
            "constant_aggregate": (
                "sum_(deg f=10)mu(f)=0 from "
                "sum_f mu(f)z^deg(f)=prod_P(1-z^deg(P))=1-q*z"
            ),
            "aggregate_identity": (
                "sum_D r_D(10)=(q-1)*(G_1+G_2)-G_3-G_4+Lambda_3+Q_1"
            ),
            "Lambda_3_definition": (
                "sum_(deg h=3) sum_(deg f=10,squarefree) mu(f)*ell(f)*(h/f)"
            ),
            "Q_1_definition": (
                "sum_(deg h=1)(lambda^[2]_10+lambda_10+kappa_10-q*lambda_10)(h)"
            ),
            "G_1": "0 because G_h(z)=1 for every linear h",
            "G_2_squarefree": _pairs(degree_two_squarefree),
            "G_2_repeated": _pairs(degree_two_repeated),
            "G_2": _pairs(degree_two_total),
            "G_2_proof": (
                "(q^2-q) squarefree quadratics contribute 1 and q squares "
                "L^2 contribute 1-q"
            ),
        },
        "cubic_channel_over_q_q_minus_1": {
            "squarefree_G_3": _trace_object(squarefree_g3),
            "repeated_G_3": "1",
            "full_G_3": _trace_object(full_g3),
            "squarefree_Lambda_3": _trace_object(squarefree_lambda),
            "repeated_L3_per_modulus": "-(q-1)",
            "repeated_L2M_per_ordered_modulus": "15-5*q",
            "repeated_Lambda_3": _trace_object(repeated_lambda_normalized),
            "full_Lambda_3": _trace_object(full_lambda),
        },
        "quartic_channel": quartic,
        "linear_modulus_channel": linear,
        "final_normalized_trace_expression": _trace_object(final),
        "theorem": {
            "marked_stack_trace": (
                "T_(10,0)(q)=(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7"
            ),
            "reciprocal_total": ("sum_D r_D(10)=q*(q-1)*T_(10,0)(q)"),
            "reciprocal_mean": "E_D[r_D(10)]=T_(10,0)(q)/q^3",
            "character_mean": "E_D[chi_(10,0)(U_D)]=T_(10,0)(q)/q^8",
        },
    }


def _multiply_factor(
    coefficients: list[int], degree: int, multiplicity: int, guard: ResourceGuard
) -> None:
    maximum = len(coefficients) - 1
    for _ in range(multiplicity):
        for index in range(maximum, degree - 1, -1):
            coefficients[index] -= coefficients[index - degree]
            guard.operation()


def eta_level2_coefficients(maximum: int, guard: ResourceGuard) -> list[int]:
    if not 1 <= maximum <= MAX_FOURIER_DEGREE:
        raise ValueError("level-two eta-product degree exceeds cap")
    coefficients = [0] * (maximum + 1)
    coefficients[1] = 1
    for degree in range(1, maximum + 1):
        _multiply_factor(coefficients, degree, 8, guard)
        if 2 * degree <= maximum:
            _multiply_factor(coefficients, 2 * degree, 8, guard)
    return coefficients


def delta_coefficients(maximum: int, guard: ResourceGuard) -> list[int]:
    if not 1 <= maximum <= MAX_FOURIER_DEGREE:
        raise ValueError("Delta expansion degree exceeds cap")
    coefficients = [0] * (maximum + 1)
    coefficients[1] = 1
    for degree in range(1, maximum + 1):
        _multiply_factor(coefficients, degree, 24, guard)
    return coefficients


def weight2_level2_coefficients(maximum: int, guard: ResourceGuard) -> list[int]:
    if not 0 <= maximum <= MAX_FOURIER_DEGREE:
        raise ValueError("weight-two expansion degree exceeds cap")
    sigma_one = [0] * (maximum + 1)
    for divisor in range(1, maximum + 1):
        for multiple in range(divisor, maximum + 1, divisor):
            sigma_one[multiple] += divisor
            guard.operation()
    coefficients = [0] * (maximum + 1)
    coefficients[0] = 1
    for degree in range(1, maximum + 1):
        coefficients[degree] = 24 * sigma_one[degree]
        if degree % 2 == 0:
            coefficients[degree] -= 48 * sigma_one[degree // 2]
        guard.operation()
    return coefficients


def _convolve(
    left: list[int], right: list[int], maximum: int, guard: ResourceGuard
) -> list[int]:
    result = [0] * (maximum + 1)
    for left_index in range(maximum + 1):
        for right_index in range(maximum + 1 - left_index):
            result[left_index + right_index] += left[left_index] * right[right_index]
            guard.operation()
    return result


def prime_power_trace(
    coefficients: list[int], weight: int, prime: int, exponent: int
) -> int:
    if prime < 2 or exponent < 1:
        raise ValueError("invalid prime-power data")
    index = prime**exponent
    if index >= len(coefficients):
        raise ValueError("Fourier expansion is too short")
    previous = 0 if exponent < 2 else coefficients[prime ** (exponent - 2)]
    return coefficients[index] - prime ** (weight - 1) * previous


def _build_modular_certificate(
    tower: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    f8 = eta_level2_coefficients(MAX_FOURIER_DEGREE, guard)
    h2 = weight2_level2_coefficients(MAX_FOURIER_DEGREE, guard)
    g10 = _convolve(f8, h2, MAX_FOURIER_DEGREE, guard)
    delta = delta_coefficients(MAX_FOURIER_DEGREE, guard)
    expected_f8 = [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043]
    expected_g10 = [0, 1, 16, -156, 256, 870, -2496, -952, 4096, 4653]
    expected_delta = [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643]
    if (f8, g10, delta) != (expected_f8, expected_g10, expected_delta):
        raise ArithmeticError("independent modular-form expansion failed")
    source_certificate = tower.get("modular_form_certificate")
    if not isinstance(source_certificate, dict) or (
        source_certificate.get("f_coefficients_c_0_through_c_9") != f8
        or source_certificate.get("g_coefficients_d_0_through_d_9") != g10
        or source_certificate.get("delta_coefficients_tau_0_through_tau_9") != delta
    ):
        raise ValueError("source modular-form certificate changed")
    theta_delta_9 = prime_power_trace(delta, 12, 3, 2)
    theta_f8_9 = prime_power_trace(f8, 8, 3, 2)
    theta_g10_9 = prime_power_trace(g10, 10, 3, 2)
    if (theta_delta_9, theta_f8_9, theta_g10_9) != (-290790, -4230, -15030):
        raise ArithmeticError("q=9 Frobenius-power traces failed")
    t9 = 8 * theta_delta_9 - theta_f8_9 - theta_g10_9 - 9 - 7
    if t9 != -2_307_076:
        raise ArithmeticError("q=9 Sym10 consequence failed")
    return {
        "f_(8,2)_coefficients_0_through_9": f8,
        "g_(10,2)_coefficients_0_through_9": g10,
        "Delta_coefficients_0_through_9": delta,
        "construction": {
            "f_(8,2)": "eta(z)^8*eta(2z)^8",
            "g_(10,2)": "f_(8,2)*(2*E_2(2z)-E_2(z))",
            "Delta": "eta(z)^24",
        },
        "q_9": {
            "Theta_Delta(9)": theta_delta_9,
            "Theta_(8,2)(9)": theta_f8_9,
            "Theta_(10,2)(9)": theta_g10_9,
            "T_(10,0)(9)": t9,
            "status": "THEOREM_CONSEQUENCE_NOT_FIELD_ENUMERATION",
        },
    }


def reciprocal_coefficient_10(
    a_coefficient: int, b_coefficient: int, q: int, guard: ResourceGuard | None = None
) -> int:
    values = [1]
    for degree in range(1, 11):
        value = -a_coefficient * values[degree - 1]
        if degree >= 2:
            value -= b_coefficient * values[degree - 2]
        if degree >= 3:
            value -= q * a_coefficient * values[degree - 3]
        if degree >= 4:
            value -= q * q * values[degree - 4]
        values.append(value)
        if guard is not None:
            guard.reciprocal()
    return values[10]


def _held_out_controls(
    balanced: Mapping[str, object],
    modular: Mapping[str, object],
    guard: ResourceGuard,
) -> list[dict[str, object]]:
    frozen = balanced.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("balanced frozen-enumeration block is missing")
    families = frozen.get("families")
    if not isinstance(families, list) or len(families) != 3:
        raise ValueError("balanced held-out families changed")
    f8 = modular["f_(8,2)_coefficients_0_through_9"]
    g10 = modular["g_(10,2)_coefficients_0_through_9"]
    delta = modular["Delta_coefficients_0_through_9"]
    if not all(isinstance(row, list) for row in (f8, g10, delta)):
        raise TypeError("modular coefficient vectors are invalid")

    controls: list[dict[str, object]] = []
    for family in families:
        if not isinstance(family, dict):
            raise TypeError("held-out family row is invalid")
        q = int(family["q"])
        law = family.get("joint_a_D_b_D_law")
        if not isinstance(law, dict) or not isinstance(law.get("atoms"), list):
            raise TypeError("held-out joint law is invalid")
        observed = 0
        counted_members = 0
        for atom in law["atoms"]:
            if not isinstance(atom, dict):
                raise TypeError("held-out joint-law atom is invalid")
            guard.atom()
            count = int(atom["member_count"])
            observed += count * reciprocal_coefficient_10(
                int(atom["a_D"]), int(atom["b_D"]), q, guard
            )
            counted_members += count
        if (
            counted_members != q**4 * (q - 1)
            or counted_members != family["member_count"]
        ):
            raise ArithmeticError("held-out member count failed")
        theta_delta = int(delta[q])
        theta_f8 = int(f8[q])
        theta_g10 = int(g10[q])
        theorem_t = (q - 1) * theta_delta - theta_f8 - theta_g10 - q - 7
        theorem_sum = q * (q - 1) * theorem_t
        controls.append(
            {
                "q": q,
                "joint_law_atoms": len(law["atoms"]),
                "members": counted_members,
                "Theta_Delta": theta_delta,
                "Theta_(8,2)": theta_f8,
                "Theta_(10,2)": theta_g10,
                "observed_T_(10,0)": observed // (q * (q - 1)),
                "theorem_T_(10,0)": theorem_t,
                "observed_sum_r_D_10": observed,
                "theorem_sum_r_D_10": theorem_sum,
                "difference": observed - theorem_sum,
                "status": "HELD_OUT_FALSIFICATION_CONTROL_ONLY",
            }
        )
    expected = [(3, 638, 3828), (5, 18648, 372960), (7, -100542, -4222764)]
    if [
        (row["q"], row["theorem_T_(10,0)"], row["theorem_sum_r_D_10"])
        for row in controls
    ] != expected or any(row["difference"] for row in controls):
        raise ArithmeticError("held-out Sym10 controls failed")
    return controls


def _source_manifest() -> list[dict[str, object]]:
    result = []
    for name, lock in SOURCE_LOCKS.items():
        json_path = lock["json_path"]
        if not isinstance(json_path, Path):
            raise TypeError("invalid source manifest path")
        row: dict[str, object] = {
            "id": name,
            "commit": lock["commit"],
            "role": lock["role"],
            "json_path": _relative(json_path),
            "json_git_blob": lock["json_git_blob"],
            "json_sha256_lf_normalized": lock["json_lf"],
            "payload_sha256": lock["payload"],
        }
        note_path = lock.get("note_path")
        if note_path is not None:
            if not isinstance(note_path, Path):
                raise TypeError("invalid source note path")
            row.update(
                {
                    "note_path": _relative(note_path),
                    "note_git_blob": lock["note_git_blob"],
                    "note_sha256_lf_normalized": lock["note_lf"],
                }
            )
        result.append(row)
    return result


def _packet_manifest() -> list[dict[str, str]]:
    return [
        {"path": _relative(path), "sha256_lf_normalized": _lf_sha256(path)}
        for path in (NOTE_PATH, SCRIPT_PATH, TEST_PATH)
    ]


def build_fixture() -> dict[str, object]:
    start = time.monotonic()
    guard = ResourceGuard()
    theorem_sources = _load_sources(THEOREM_SOURCE_NAMES)
    symbolic = _build_symbolic_theorem(theorem_sources, guard)
    operations_after_symbolic = guard.exact_operations
    modular = _build_modular_certificate(theorem_sources["tower"], guard)
    operations_before_controls = guard.exact_operations

    held_out_sources = _load_sources(HELD_OUT_SOURCE_NAMES)
    controls = _held_out_controls(held_out_sources["balanced"], modular, guard)
    tower_ledger = theorem_sources["tower"].get("primary_source_ledger")
    if not isinstance(tower_ledger, list):
        raise TypeError("audited primary-source ledger is missing")

    fixture: dict[str, object] = {
        "schema": "riemann.genus2_sym10_marked_trace_average.v1",
        "status": "PROVED_ALL_ODD_PRIME_POWERS",
        "definitions": {
            "family": "H_5(q)=monic squarefree quintics over F_q",
            "family_size": "#H_5(q)=q^4*(q-1)",
            "reciprocal_series": (
                "1/(1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4)=sum_(n>=0)r_D(n)u^n"
            ),
            "central_normalization": "r_D(10)=q^5*chi_(10,0)(U_D)",
            "marked_stack_trace": ("T_(10,0)(q)=sum_D r_D(10)/(q*(q-1))"),
        },
        **symbolic,
        "modular_form_certificate": modular,
        "held_out_falsification_controls": controls,
        "source_manifest": _source_manifest(),
        "packet_manifest": _packet_manifest(),
        "primary_source_ledger": tower_ledger,
        "resource_contract": {
            "arithmetic": "exact integers/rationals and sparse polynomial algebra",
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "actual_operations_after_symbolic_theorem": operations_after_symbolic,
            "actual_operations_before_controls": operations_before_controls,
            "maximum_held_out_atoms": MAX_HELD_OUT_ATOMS,
            "actual_held_out_atoms": guard.held_out_atoms,
            "maximum_reciprocal_updates": MAX_RECIPROCAL_UPDATES,
            "actual_reciprocal_updates": guard.reciprocal_updates,
            "maximum_fourier_degree": MAX_FOURIER_DEGREE,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "new_finite_fields_enumerated": [],
            "q_9_field_enumerated": False,
        },
        "scope": {
            "proved_q": "every odd prime power",
            "sampled_q_values_used_as_theorem_input": [],
            "held_out_q_values": [3, 5, 7],
        },
        "firewalls": [
            "The q=3,5,7 coefficient atoms are loaded only after the symbolic proof and modular-form certificate close; they are not theorem inputs.",
            "The q=9 row uses Frobenius-power traces, not composite-index Fourier coefficients, and F_9 is not enumerated.",
            "The theorem is a marked family trace, not a memberwise sign theorem.",
            "No external novelty claim is made for the trace identity or its modular channels.",
            "This packet makes no RH, GRH, motive, compatible-system, global Euler-product, or average-to-principal-member claim.",
        ],
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    if time.monotonic() - start > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return fixture


def _serialized(fixture: Mapping[str, object]) -> str:
    return json.dumps(fixture, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    arguments = parser.parse_args()
    fixture = build_fixture()
    rendered = _serialized(fixture)
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
