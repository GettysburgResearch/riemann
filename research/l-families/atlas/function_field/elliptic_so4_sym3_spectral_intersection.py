#!/usr/bin/env python3
"""Exact SO(4)-tensor / elliptic-Sym^3 compact spectral intersection.

This packet consumes two authenticated upstream artifacts and performs only
exact polynomial algebra and histogram-atom transforms.  It does not build a
finite field or enumerate a curve.  The five locked nonsquare-prime rows have
645 ordered histogram-atom pairs in total.

The load-bearing conventions are deliberately explicit.  Tensor inputs are

    P_A(T)=1+A*T+q*T^2,  P_B(T)=1+B*T+q*T^2,

with u=A/sqrt(q), v=B/sqrt(q).  An elliptic Sym^3 source input has coefficient
``a`` in 1+a*T+q*T^2 and geometric trace c=-a.  On
u=epsilon*(v^2-2), the matching Sym^3 geometric trace is c=epsilon*B,
so its source coefficient is a=-epsilon*B.  Raw factors have different
weights.  On square-q graph points there is an exact, typed dilation identity
``P_tensor(s*T)=P_Sym3,c(T)`` with ``s=sqrt(q)``; this is not equality in the
same unscaled variable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_so4_sym3_spectral_intersection.json"
NOTE_PATH = HERE / "ELLIPTIC_SO4_SYM3_SPECTRAL_INTERSECTION.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_so4_sym3_spectral_intersection.py"

SO4_FIXTURE_PATH = HERE / "elliptic_pair_rankin_so4_family.json"
SO4_PRODUCER_PATH = HERE / "elliptic_pair_rankin_so4_family.py"
SYM3_FIXTURE_PATH = HERE / "elliptic_symmetric_cube_family.json"
SYM3_PRODUCER_PATH = HERE / "elliptic_symmetric_cube_family.py"

EXPECTED_SO4_SCHEMA = "riemann.function_field.elliptic_pair_rankin_so4_family.v2"
EXPECTED_SO4_PAYLOAD_SHA256 = (
    "3634ab438de17596fa7a616130a318b85b579178b6d87f017523dae25c53e028"
)
EXPECTED_SO4_FIXTURE_SHA256_LF = (
    "6f10140f9ebcde3a85feadd3498c43214617cb62305cb8c610308c229d175a38"
)
EXPECTED_SO4_PRODUCER_SHA256_LF = (
    "2f3b0bab10135a626d0a05cde2a2fa75aa07e9bc62276411c1d0874bc2078545"
)

EXPECTED_SYM3_SCHEMA = "riemann.function_field.elliptic_symmetric_cube_family.v1"
EXPECTED_SYM3_PAYLOAD_SHA256 = (
    "7e30dd220b9c9e3a3873ffe8b168ad53af4899de1dd21a2d69e2498abc6ee5b9"
)
EXPECTED_SYM3_FIXTURE_SHA256_LF = (
    "2b8b7f206c4e4c24f4e1ac65d093ab976dd6483dceb6ea52f44e76a7004bb033"
)
EXPECTED_SYM3_PRODUCER_SHA256_LF = (
    "1a99107771a804f39c6d3b26b0b1e67ad385500ce6776f2e14cfe6bf7b810d26"
)

FROZEN_Q_VALUES = (3, 5, 7, 11, 13)
SYNTHETIC_SQUARE_Q_VALUES = (9, 25)
ATOM_PAIR_CAP_INCLUSIVE = 645
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 4_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _fraction(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _require_builtin_int(value: object, name: str) -> int:
    if type(value) is not int:
        raise TypeError(f"{name} must be a built-in integer")
    return value


def prime_power_data(q: object) -> tuple[int, int]:
    """Return ``(p,e)`` for an odd prime power, refusing all other inputs."""

    q_int = _require_builtin_int(q, "q")
    if q_int < 3 or q_int % 2 == 0:
        raise ValueError("q must be an odd prime power")
    for candidate in range(3, math.isqrt(q_int) + 1, 2):
        if q_int % candidate:
            continue
        residue = q_int
        exponent = 0
        while residue % candidate == 0:
            residue //= candidate
            exponent += 1
        if residue != 1:
            raise ValueError("q must be an odd prime power")
        return candidate, exponent
    return q_int, 1


class ResourceGuard:
    """Fail closed on both locked atom-pair and declared-work budgets."""

    def __init__(
        self,
        atom_pair_cap: int = ATOM_PAIR_CAP_INCLUSIVE,
        work_cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE,
    ) -> None:
        if type(atom_pair_cap) is not int or atom_pair_cap < 0:
            raise ValueError("atom-pair cap must be a nonnegative built-in integer")
        if type(work_cap) is not int or work_cap <= 0:
            raise ValueError("work cap must be a positive built-in integer")
        self.atom_pair_cap = atom_pair_cap
        self.work_cap = work_cap
        self.atom_pairs = 0
        self.ledger: Counter[str] = Counter()

    @property
    def total_work(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("resource name must be a nonempty string")
        if type(units) is not int or units < 0:
            raise ValueError("resource charge must be a nonnegative built-in integer")
        if self.total_work + units >= self.work_cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.work_cap}"
            )
        self.ledger[name] += units

    def charge_pair(self) -> None:
        if self.atom_pairs + 1 > self.atom_pair_cap:
            raise RuntimeError(
                f"histogram atom-pair cap exceeded: "
                f"{self.atom_pairs + 1}>{self.atom_pair_cap}"
            )
        self.atom_pairs += 1
        self.charge("locked_source_histogram_atom_pairs")


def _load_authenticated_fixture(
    path: Path,
    *,
    schema: str,
    payload_sha256: str,
    file_sha256_lf: str,
) -> dict[str, object]:
    if _lf_sha256(path) != file_sha256_lf:
        raise RuntimeError(f"locked fixture file changed: {path.name}")
    fixture = json.loads(path.read_text(encoding="utf-8"))
    if fixture.get("schema") != schema:
        raise RuntimeError(f"locked fixture schema changed: {path.name}")
    if fixture.get("payload_sha256") != payload_sha256:
        raise RuntimeError(f"locked fixture payload identity changed: {path.name}")
    unhashed = dict(fixture)
    claimed = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
        raise RuntimeError(f"locked fixture is internally inauthentic: {path.name}")
    return fixture


def load_locked_sources() -> tuple[dict[str, object], dict[str, object]]:
    """Authenticate both fixtures, both producers, and key conventions."""

    so4 = _load_authenticated_fixture(
        SO4_FIXTURE_PATH,
        schema=EXPECTED_SO4_SCHEMA,
        payload_sha256=EXPECTED_SO4_PAYLOAD_SHA256,
        file_sha256_lf=EXPECTED_SO4_FIXTURE_SHA256_LF,
    )
    sym3 = _load_authenticated_fixture(
        SYM3_FIXTURE_PATH,
        schema=EXPECTED_SYM3_SCHEMA,
        payload_sha256=EXPECTED_SYM3_PAYLOAD_SHA256,
        file_sha256_lf=EXPECTED_SYM3_FIXTURE_SHA256_LF,
    )
    if _lf_sha256(SO4_PRODUCER_PATH) != EXPECTED_SO4_PRODUCER_SHA256_LF:
        raise RuntimeError("locked SO(4) producer changed")
    if _lf_sha256(SYM3_PRODUCER_PATH) != EXPECTED_SYM3_PRODUCER_SHA256_LF:
        raise RuntimeError("locked Sym^3 producer changed")

    so4_rows = so4.get("frozen_histogram_cartesian_transforms")
    if not isinstance(so4_rows, list) or tuple(
        row.get("q") for row in so4_rows if isinstance(row, dict)
    ) != FROZEN_Q_VALUES:
        raise RuntimeError("locked SO(4) q rows changed")
    so4_coordinates = so4.get("compact_SO4_coefficient_image", {}).get(
        "coordinates"
    )
    if so4_coordinates != (
        "x=u*v=A*B/q and y=u^2+v^2-2=(A^2+B^2-2*q)/q"
    ):
        raise RuntimeError("locked SO(4) coordinate convention changed")

    sym3_rows = sym3.get("frozen_histogram_transforms")
    if not isinstance(sym3_rows, list) or tuple(
        row.get("q") for row in sym3_rows if isinstance(row, dict)
    ) != FROZEN_Q_VALUES:
        raise RuntimeError("locked Sym^3 q rows changed")
    normalization = sym3.get("normalization", {})
    if normalization.get("base_factor") != (
        "P_E(T)=1+A*T+q*T^2=(1-alpha*T)(1-beta*T)"
    ):
        raise RuntimeError("locked Sym^3 base-factor convention changed")
    if normalization.get("normalized_base_trace") != "t0=t/sqrt(q)=-A/sqrt(q)":
        raise RuntimeError("locked Sym^3 trace sign convention changed")
    if normalization.get("normalized_sym3_trace_x") != "x=t0^3-2t0":
        raise RuntimeError("locked Sym^3 trace normalization changed")
    if normalization.get("normalized_second_coefficient_y") != (
        "y=t0^4-3t0^2+2"
    ):
        raise RuntimeError("locked Sym^3 second coefficient changed")
    return so4, sym3


def _source_locks() -> dict[str, dict[str, object]]:
    return {
        "so4_fixture": {
            "path": _relative(SO4_FIXTURE_PATH),
            "schema": EXPECTED_SO4_SCHEMA,
            "payload_sha256": EXPECTED_SO4_PAYLOAD_SHA256,
            "sha256_lf_normalized": EXPECTED_SO4_FIXTURE_SHA256_LF,
        },
        "so4_producer": {
            "path": _relative(SO4_PRODUCER_PATH),
            "sha256_lf_normalized": EXPECTED_SO4_PRODUCER_SHA256_LF,
        },
        "sym3_fixture": {
            "path": _relative(SYM3_FIXTURE_PATH),
            "schema": EXPECTED_SYM3_SCHEMA,
            "payload_sha256": EXPECTED_SYM3_PAYLOAD_SHA256,
            "sha256_lf_normalized": EXPECTED_SYM3_FIXTURE_SHA256_LF,
        },
        "sym3_producer": {
            "path": _relative(SYM3_PRODUCER_PATH),
            "sha256_lf_normalized": EXPECTED_SYM3_PRODUCER_SHA256_LF,
        },
    }


def so4_coordinates(A: object, B: object, q: object) -> tuple[Fraction, Fraction]:
    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    return (
        Fraction(A_int * B_int, q_int),
        Fraction(A_int * A_int + B_int * B_int - 2 * q_int, q_int),
    )


def sym3_curve_value(
    x: Fraction | int, y: Fraction | int
) -> Fraction:
    if type(x) not in {int, Fraction} or type(y) not in {int, Fraction}:
        raise TypeError("curve coordinates must be exact integers or Fractions")
    xq, yq = Fraction(x), Fraction(y)
    return -(xq**4) + xq * xq * yq + xq * xq + yq**3 - 2 * yq * yq


def scaled_intersection_residual(A: object, B: object, q: object) -> int:
    """Return ``q^4 F_3(AB/q,(A^2+B^2-2q)/q)`` exactly."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    value = sym3_curve_value(*so4_coordinates(A_int, B_int, q_int)) * q_int**4
    if value.denominator != 1:
        raise ArithmeticError("scaled intersection residual lost integrality")
    return value.numerator


def scaled_intersection_factor_product(A: object, B: object, q: object) -> int:
    """The two rational-square factors after clearing ``q^4``."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    first = q_int * A_int * A_int - (B_int * B_int - 2 * q_int) ** 2
    second = (A_int * A_int - 2 * q_int) ** 2 - q_int * B_int * B_int
    return first * second


def graph_branches(A: object, B: object, q: object) -> list[dict[str, object]]:
    """Return square-q doubling branches through an integral pair.

    ``sym3_geometric_trace_c`` is the trace ``c`` for a source base factor
    ``1-c*T+q*T^2``.  The source packet calls its T coefficient ``a=-c``.
    """

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    _, exponent = prime_power_data(q_int)
    if exponent % 2:
        return []
    s = math.isqrt(q_int)
    if s * s != q_int:
        raise ArithmeticError("even prime-power exponent did not give a square")
    output: list[dict[str, object]] = []
    for epsilon in (-1, 1):
        if s * A_int == epsilon * (B_int * B_int - 2 * q_int):
            c = epsilon * B_int
            output.append(
                {
                    "orientation": "u_from_v",
                    "epsilon": epsilon,
                    "normalized_graph": "u=epsilon*(v^2-2)",
                    "sym3_geometric_trace_c": c,
                    "sym3_source_base_coefficient_a": -c,
                }
            )
        if s * B_int == epsilon * (A_int * A_int - 2 * q_int):
            c = epsilon * A_int
            output.append(
                {
                    "orientation": "v_from_u",
                    "epsilon": epsilon,
                    "normalized_graph": "v=epsilon*(u^2-2)",
                    "sym3_geometric_trace_c": c,
                    "sym3_source_base_coefficient_a": -c,
                }
            )
    return output


def tensor_coefficients(A: object, B: object, q: object) -> tuple[int, ...]:
    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    return (
        1,
        -A_int * B_int,
        q_int * (A_int * A_int + B_int * B_int - 2 * q_int),
        -(q_int**2) * A_int * B_int,
        q_int**4,
    )


def sym3_coefficients_from_geometric_trace(c: object, q: object) -> tuple[int, ...]:
    """Raw Sym^3 factor for base factor ``1-c*T+q*T^2``."""

    c_int = _require_builtin_int(c, "c")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    trace = c_int**3 - 2 * q_int * c_int
    second_reduced = c_int**4 - 3 * q_int * c_int * c_int + 2 * q_int**2
    return (1, -trace, q_int * second_reduced, -(q_int**3) * trace, q_int**6)


def normalize_polynomial(
    coefficients: Sequence[int], scale: object
) -> tuple[Fraction, ...]:
    scale_int = _require_builtin_int(scale, "scale")
    if scale_int <= 0:
        raise ValueError("scale must be positive")
    if not coefficients or any(type(value) is not int for value in coefficients):
        raise TypeError("coefficients must be a nonempty sequence of built-in integers")
    return tuple(
        Fraction(coefficient, scale_int**degree)
        for degree, coefficient in enumerate(coefficients)
    )


def dilate_polynomial(
    coefficients: Sequence[int], scale: object
) -> tuple[int, ...]:
    """Return coefficients of ``P(scale*T)`` for an integral polynomial P."""

    scale_int = _require_builtin_int(scale, "scale")
    if scale_int <= 0:
        raise ValueError("scale must be positive")
    if not coefficients or any(type(value) is not int for value in coefficients):
        raise TypeError("coefficients must be a nonempty sequence of built-in integers")
    return tuple(
        coefficient * scale_int**degree
        for degree, coefficient in enumerate(coefficients)
    )


def normalized_sym3_polynomial(c: object, q: object) -> tuple[Fraction, ...]:
    c_int = _require_builtin_int(c, "c")
    q_int = _require_builtin_int(q, "q")
    _, exponent = prime_power_data(q_int)
    if exponent % 2:
        raise ValueError("an integral normalization scale requires square q")
    s = math.isqrt(q_int)
    return normalize_polynomial(
        sym3_coefficients_from_geometric_trace(c_int, q_int), s**3
    )


def normalized_tensor_polynomial(A: object, B: object, q: object) -> tuple[Fraction, ...]:
    q_int = _require_builtin_int(q, "q")
    return normalize_polynomial(tensor_coefficients(A, B, q_int), q_int)


def waterhouse_intersection_classification(
    A: object, B: object, q: object
) -> dict[str, object]:
    """Classify simultaneous elliptic realization on a square-q graph.

    This is a direct specialization of Waterhouse, Theorem 4.1.  Tensor
    coefficients A,B correspond to geometric traces -A,-B; signs do not
    change the listed cases.
    """

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    p, exponent = prime_power_data(q_int)
    if exponent % 2:
        raise ValueError("Waterhouse intersection classification requires square q")
    s = math.isqrt(q_int)
    branches = graph_branches(A_int, B_int, q_int)
    if not branches:
        return {
            "on_integral_compact_intersection": False,
            "stratum": "off_intersection",
            "both_tensor_input_traces_realized": False,
            "waterhouse_cases": [],
        }
    abs_pair = (abs(A_int), abs(B_int))
    if abs_pair == (2 * s, 2 * s):
        return {
            "on_integral_compact_intersection": True,
            "stratum": "endpoint_endpoint",
            "normalized_absolute_pair": [2, 2],
            "both_tensor_input_traces_realized": True,
            "waterhouse_cases": ["Theorem 4.1 case (2) for traces +/-2*sqrt(q)"],
            "congruence_condition": "none",
        }
    if abs_pair == (s, s):
        realized = p % 3 != 1
        return {
            "on_integral_compact_intersection": True,
            "stratum": "unit_unit",
            "normalized_absolute_pair": [1, 1],
            "both_tensor_input_traces_realized": realized,
            "waterhouse_cases": ["Theorem 4.1 case (3) for traces +/-sqrt(q)"],
            "congruence_condition": "p is not congruent to 1 modulo 3",
        }
    if abs_pair in {(2 * s, 0), (0, 2 * s)}:
        realized = p % 4 != 1
        return {
            "on_integral_compact_intersection": True,
            "stratum": "endpoint_zero",
            "normalized_absolute_pair": [
                Fraction(abs(A_int), s).numerator,
                Fraction(abs(B_int), s).numerator,
            ],
            "both_tensor_input_traces_realized": realized,
            "waterhouse_cases": [
                "Theorem 4.1 case (2) for +/-2*sqrt(q)",
                "Theorem 4.1 case (5)(ii) for trace 0",
            ],
            "congruence_condition": "p is not congruent to 1 modulo 4",
        }
    return {
        "on_integral_compact_intersection": True,
        "stratum": "integral_hasse_lattice_ghost",
        "normalized_absolute_pair": [
            _fraction(Fraction(abs(A_int), s)),
            _fraction(Fraction(abs(B_int), s)),
        ],
        "both_tensor_input_traces_realized": False,
        "waterhouse_cases": [],
        "reason": "each graph free trace is divisible by p, so Waterhouse leaves only 0,+/-sqrt(q),+/-2sqrt(q); this pair is outside those simultaneous strata",
    }


def square_prime_power_intersection_counts(p: object, k: object) -> dict[str, object]:
    """All-q lattice and Waterhouse-realized counts for ``q=p^(2k)``."""

    p_int = _require_builtin_int(p, "p")
    k_int = _require_builtin_int(k, "k")
    prime, exponent = prime_power_data(p_int)
    if prime != p_int or exponent != 1:
        raise ValueError("p must be an odd prime")
    if k_int < 1:
        raise ValueError("k must be positive")
    M = p_int ** (k_int // 2)
    realized = 4
    if p_int % 3 != 1:
        realized += 4
    if p_int % 4 != 1:
        realized += 4
    ghost = (1 - 2 * p_int**2, p_int) if k_int == 2 else None
    return {
        "p": p_int,
        "k": k_int,
        "q": p_int ** (2 * k_int),
        "M=p^floor(k/2)": M,
        "integral_parameters_per_oriented_signed_graph": 4 * M + 1,
        "four_graph_branch_incidences": 16 * M + 4,
        "distinct_integral_hasse_lattice_points": 16 * M - 4,
        "pairwise_overlap_description": "the only integral (equivalently rational) overlaps are four endpoint pairs and four unit pairs, each incident to exactly two graphs; additional irrational real graph intersections do not affect the lattice count",
        "waterhouse_realized_distinct_points": realized,
        "waterhouse_realized_strata": {
            "endpoint_endpoint": 4,
            "unit_unit": 4 if p_int % 3 != 1 else 0,
            "endpoint_zero": 4 if p_int % 4 != 1 else 0,
        },
        "k_equals_2_explicit_ghost_A_B": None if ghost is None else list(ghost),
    }


def _fraction_determinant(matrix: Sequence[Sequence[Fraction | int]]) -> Fraction:
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("determinant requires a nonempty square matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    determinant = Fraction(1)
    for column in range(len(work)):
        pivot_row = next(
            (row for row in range(column, len(work)) if work[row][column]), None
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            determinant = -determinant
        pivot = work[column][column]
        determinant *= pivot
        for row in range(column + 1, len(work)):
            if not work[row][column]:
                continue
            ratio = work[row][column] / pivot
            for index in range(column, len(work)):
                work[row][index] -= ratio * work[column][index]
    return determinant


def reciprocal_quartic_discriminant_via_resultant(
    x: Fraction | int, y: Fraction | int
) -> Fraction:
    """Direct 7-by-7 Sylvester resultant of the reciprocal quartic and derivative."""

    if type(x) not in {int, Fraction} or type(y) not in {int, Fraction}:
        raise TypeError("quartic coordinates must be exact integers or Fractions")
    xq, yq = Fraction(x), Fraction(y)
    polynomial = [Fraction(1), -xq, yq, -xq, Fraction(1)]
    derivative = [Fraction(4), -3 * xq, 2 * yq, -xq]
    matrix = [[Fraction(0) for _ in range(7)] for _ in range(7)]
    for row in range(3):
        matrix[row][row : row + 5] = polynomial
    for row in range(4):
        matrix[3 + row][row : row + 4] = derivative
    return _fraction_determinant(matrix)


def discriminant_certificate_from_parameter(
    t: Fraction | int,
) -> dict[str, Fraction | bool]:
    if type(t) not in {int, Fraction}:
        raise TypeError("parameter must be an exact integer or Fraction")
    tq = Fraction(t)
    x = tq**3 - 2 * tq
    y = tq**4 - 3 * tq * tq + 2
    D = (y + 2) ** 2 - 4 * x * x
    E = x * x - 4 * (y - 2)
    expected_D = (tq * tq - 1) ** 2 * (tq * tq - 4) ** 2
    expected_E = tq * tq * (tq * tq - 4) ** 2
    full = D * E**2
    expected_full = (
        tq**4 * (tq * tq - 1) ** 2 * (tq * tq - 4) ** 6
    )
    resultant = reciprocal_quartic_discriminant_via_resultant(x, y)
    if D != expected_D or E != expected_E or full != expected_full:
        raise ArithmeticError("parameter discriminant factorization failed")
    if full != resultant:
        raise ArithmeticError("factorized and resultant discriminants disagree")
    return {
        "x": x,
        "y": y,
        "coefficient_map_fold_D": D,
        "hasse_endpoint_factor_E": E,
        "full_quartic_root_discriminant": full,
        "direct_sylvester_resultant": resultant,
        "on_fold_wall": D == 0,
        "on_hasse_endpoint_wall": E == 0,
        "has_repeated_root": full == 0,
    }


Polynomial = dict[int, int]
BivariatePolynomial = dict[tuple[int, int], int]


def _poly_add(*terms: tuple[int, Mapping[int, int]]) -> Polynomial:
    output: Counter[int] = Counter()
    for scale, polynomial in terms:
        for degree, coefficient in polynomial.items():
            output[degree] += scale * coefficient
    return {degree: coefficient for degree, coefficient in output.items() if coefficient}


def _poly_mul(left: Mapping[int, int], right: Mapping[int, int]) -> Polynomial:
    output: Counter[int] = Counter()
    for a, ca in left.items():
        for b, cb in right.items():
            output[a + b] += ca * cb
    return {degree: coefficient for degree, coefficient in output.items() if coefficient}


def _poly_pow(base: Mapping[int, int], exponent: int) -> Polynomial:
    if type(exponent) is not int or exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    output: Polynomial = {0: 1}
    for _ in range(exponent):
        output = _poly_mul(output, base)
    return output


def _bivar_add(
    *terms: tuple[int, Mapping[tuple[int, int], int]],
) -> BivariatePolynomial:
    output: Counter[tuple[int, int]] = Counter()
    for scale, polynomial in terms:
        for exponent, coefficient in polynomial.items():
            output[exponent] += scale * coefficient
    return {exponent: coefficient for exponent, coefficient in output.items() if coefficient}


def _bivar_mul(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
) -> BivariatePolynomial:
    output: Counter[tuple[int, int]] = Counter()
    for (a, b), ca in left.items():
        for (c, d), cb in right.items():
            output[(a + c, b + d)] += ca * cb
    return {exponent: coefficient for exponent, coefficient in output.items() if coefficient}


def _bivar_pow(
    base: Mapping[tuple[int, int], int], exponent: int
) -> BivariatePolynomial:
    if type(exponent) is not int or exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    output: BivariatePolynomial = {(0, 0): 1}
    for _ in range(exponent):
        output = _bivar_mul(output, base)
    return output


def symbolic_residuals() -> dict[str, Mapping[object, int]]:
    """Return exact zero residuals for factorization, graphs, and walls."""

    one = {(0, 0): 1}
    u = {(1, 0): 1}
    v = {(0, 1): 1}
    x = _bivar_mul(u, v)
    y = _bivar_add(
        (1, _bivar_pow(u, 2)), (1, _bivar_pow(v, 2)), (-2, one)
    )
    curve = _bivar_add(
        (-1, _bivar_pow(x, 4)),
        (1, _bivar_mul(_bivar_pow(x, 2), y)),
        (1, _bivar_pow(x, 2)),
        (1, _bivar_pow(y, 3)),
        (-2, _bivar_pow(y, 2)),
    )
    factors = (
        _bivar_add((1, u), (-1, _bivar_pow(v, 2)), (2, one)),
        _bivar_add((1, u), (1, _bivar_pow(v, 2)), (-2, one)),
        _bivar_add((1, _bivar_pow(u, 2)), (-1, v), (-2, one)),
        _bivar_add((1, _bivar_pow(u, 2)), (1, v), (-2, one)),
    )
    product = {(0, 0): 1}
    for factor in factors:
        product = _bivar_mul(product, factor)
    output: dict[str, Mapping[object, int]] = {
        "global_curve_factorization_residual": _bivar_add(
            (1, curve), (-1, product)
        )
    }

    t = {1: 1}
    one_t = {0: 1}
    chi2 = _poly_add((1, _poly_pow(t, 2)), (-2, one_t))
    for orientation in ("u_from_v", "v_from_u"):
        for epsilon in (-1, 1):
            doubled = {degree: epsilon * coefficient for degree, coefficient in chi2.items()}
            uu, vv = (doubled, t) if orientation == "u_from_v" else (t, doubled)
            parameter = {degree: epsilon * coefficient for degree, coefficient in t.items()}
            xx = _poly_mul(uu, vv)
            yy = _poly_add(
                (1, _poly_pow(uu, 2)),
                (1, _poly_pow(vv, 2)),
                (-2, one_t),
            )
            sym_x = _poly_add(
                (1, _poly_pow(parameter, 3)), (-2, parameter)
            )
            sym_y = _poly_add(
                (1, _poly_pow(parameter, 4)),
                (-3, _poly_pow(parameter, 2)),
                (2, one_t),
            )
            curve_on_graph = _poly_add(
                (-1, _poly_pow(xx, 4)),
                (1, _poly_mul(_poly_pow(xx, 2), yy)),
                (1, _poly_pow(xx, 2)),
                (1, _poly_pow(yy, 3)),
                (-2, _poly_pow(yy, 2)),
            )
            D = _poly_add(
                (1, _poly_pow(_poly_add((1, yy), (2, one_t)), 2)),
                (-4, _poly_pow(xx, 2)),
            )
            E = _poly_add(
                (1, _poly_pow(xx, 2)),
                (-4, _poly_add((1, yy), (-2, one_t))),
            )
            t2_minus_1 = _poly_add((1, _poly_pow(parameter, 2)), (-1, one_t))
            t2_minus_4 = _poly_add((1, _poly_pow(parameter, 2)), (-4, one_t))
            expected_D = _poly_mul(
                _poly_pow(t2_minus_1, 2), _poly_pow(t2_minus_4, 2)
            )
            expected_E = _poly_mul(
                _poly_pow(parameter, 2), _poly_pow(t2_minus_4, 2)
            )
            full = _poly_mul(D, _poly_pow(E, 2))
            expected_full = _poly_mul(
                _poly_pow(parameter, 4),
                _poly_mul(
                    _poly_pow(t2_minus_1, 2), _poly_pow(t2_minus_4, 6)
                ),
            )
            prefix = f"{orientation}_epsilon_{epsilon:+d}"
            output[f"{prefix}_sym3_trace_residual"] = _poly_add(
                (1, xx), (-1, sym_x)
            )
            output[f"{prefix}_sym3_second_coefficient_residual"] = _poly_add(
                (1, yy), (-1, sym_y)
            )
            output[f"{prefix}_curve_residual"] = curve_on_graph
            output[f"{prefix}_fold_discriminant_residual"] = _poly_add(
                (1, D), (-1, expected_D)
            )
            output[f"{prefix}_endpoint_factor_residual"] = _poly_add(
                (1, E), (-1, expected_E)
            )
            output[f"{prefix}_full_discriminant_residual"] = _poly_add(
                (1, full), (-1, expected_full)
            )
    return output


def _frozen_nonsquare_replay(
    so4: Mapping[str, object], guard: ResourceGuard
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    rows = so4["frozen_histogram_cartesian_transforms"]
    for row in rows:  # type: ignore[assignment]
        q = _require_builtin_int(row["q"], "source q")
        p, exponent = prime_power_data(q)
        if exponent % 2 == 0:
            raise RuntimeError("frozen obstruction row unexpectedly has square q")
        histogram = {
            int(trace): _require_builtin_int(count, "histogram count")
            for trace, count in row["source_trace_histogram"].items()
        }
        if len(histogram) != row["source_trace_atom_count"]:
            raise RuntimeError("locked source histogram atom count changed")
        pair_count = 0
        represented_mass = 0
        hits: list[dict[str, object]] = []
        for left_trace, left_mass in sorted(histogram.items()):
            for right_trace, right_mass in sorted(histogram.items()):
                guard.charge_pair()
                pair_count += 1
                represented_mass += left_mass * right_mass
                A, B = -left_trace, -right_trace
                direct = scaled_intersection_residual(A, B, q)
                factored = scaled_intersection_factor_product(A, B, q)
                guard.charge("direct_scaled_factorization_checks")
                if direct != factored:
                    raise ArithmeticError("scaled intersection factorization failed")
                normalized_from_raw = normalize_polynomial(
                    tensor_coefficients(A, B, q), q
                )
                x, y = so4_coordinates(A, B, q)
                if normalized_from_raw != (
                    Fraction(1), -x, y, -x, Fraction(1)
                ):
                    raise ArithmeticError("raw tensor factor normalization failed")
                guard.charge("direct_tensor_polynomial_normalization_checks")
                if direct == 0:
                    hits.append(
                        {
                            "source_trace_pair": [left_trace, right_trace],
                            "packet_coefficient_pair_A_B": [A, B],
                            "represented_pair_mass": left_mass * right_mass,
                        }
                    )
                guard.charge("nonsquare_valuation_obstruction_checks")
        if pair_count != row["ordered_cartesian_atom_pairs"]:
            raise ArithmeticError("locked Cartesian traversal was incomplete")
        if represented_mass != row["ordered_model_pairs_represented"]:
            raise ArithmeticError("locked Cartesian traversal lost represented mass")
        if hits:
            raise ArithmeticError("nonsquare prime-power obstruction has a counterexample")
        output.append(
            {
                "q": q,
                "prime_p": p,
                "prime_power_exponent": exponent,
                "source_trace_atom_count": len(histogram),
                "ordered_atom_pairs_checked": pair_count,
                "ordered_model_pairs_represented": represented_mass,
                "intersection_atom_hits": hits,
                "intersection_atom_hit_count": 0,
                "intersection_represented_mass": 0,
                "reason_for_zero": "q=p^e has odd e; either square equation would equate an odd p-adic valuation with an even one",
            }
        )
    return output


def _audit_sym3_frozen_factors(
    sym3: Mapping[str, object], guard: ResourceGuard
) -> list[dict[str, int]]:
    output: list[dict[str, int]] = []
    for row in sym3["frozen_histogram_transforms"]:  # type: ignore[index]
        q = _require_builtin_int(row["q"], "Sym3 q")
        atoms = row["transformed_atoms"]
        for atom in atoms:
            c = _require_builtin_int(atom["source_geometric_trace_t"], "trace")
            raw = sym3_coefficients_from_geometric_trace(c, q)
            if list(raw) != atom["polynomial_coefficients_T0_through_T4"]:
                raise ArithmeticError("locked Sym^3 raw factor convention changed")
            if raw[1] != -atom["sym3_trace_S"]:
                raise ArithmeticError("locked Sym^3 trace sign bridge changed")
            guard.charge("locked_sym3_raw_factor_checks")
        if len(atoms) != row["source_histogram_atom_count"]:
            raise ArithmeticError("locked Sym^3 atom traversal was incomplete")
        output.append({"q": q, "raw_factor_atoms_checked": len(atoms)})
    return output


def _synthetic_square_lattice_replay(guard: ResourceGuard) -> list[dict[str, object]]:
    """Complete tiny Hasse-lattice scans with typed Waterhouse classification."""

    output: list[dict[str, object]] = []
    for q in SYNTHETIC_SQUARE_Q_VALUES:
        s = math.isqrt(q)
        p, exponent = prime_power_data(q)
        k = exponent // 2
        count_theorem = square_prime_power_intersection_counts(p, k)
        bound = 2 * s
        hits: list[dict[str, object]] = []
        lattice_points = 0
        branch_incidence_count = 0
        realized_point_count = 0
        stratum_counts: Counter[str] = Counter()
        for A in range(-bound, bound + 1):
            for B in range(-bound, bound + 1):
                guard.charge("synthetic_square_hasse_lattice_points")
                lattice_points += 1
                direct = scaled_intersection_residual(A, B, q)
                factored = scaled_intersection_factor_product(A, B, q)
                if direct != factored:
                    raise ArithmeticError("square-q factorization check failed")
                branches = graph_branches(A, B, q)
                if (direct == 0) != bool(branches):
                    raise ArithmeticError("square-q graphs are not exhaustive")
                if not branches:
                    continue
                tensor_normalized = normalized_tensor_polynomial(A, B, q)
                branch_rows = []
                for branch in branches:
                    c = branch["sym3_geometric_trace_c"]
                    if type(c) is not int:
                        raise ArithmeticError("branch trace lost integer type")
                    sym3_normalized = normalized_sym3_polynomial(c, q)
                    if tensor_normalized != sym3_normalized:
                        raise ArithmeticError("normalized spectral polynomials disagree")
                    raw_sym3 = sym3_coefficients_from_geometric_trace(c, q)
                    dilated_tensor = dilate_polynomial(
                        tensor_coefficients(A, B, q), s
                    )
                    if dilated_tensor != raw_sym3:
                        raise ArithmeticError("exact raw dilation identity failed")
                    t = Fraction(c, s)
                    disc = discriminant_certificate_from_parameter(t)
                    x, y = so4_coordinates(A, B, q)
                    if (disc["x"], disc["y"]) != (x, y):
                        raise ArithmeticError("branch parameter gives wrong coefficients")
                    branch_rows.append(
                        {
                            **branch,
                            "normalized_sym3_parameter_t": _fraction(t),
                        }
                    )
                    branch_incidence_count += 1
                    guard.charge("synthetic_direct_spectral_and_resultant_checks")
                x, y = so4_coordinates(A, B, q)
                parameter = Fraction(branches[0]["sym3_geometric_trace_c"], s)
                disc = discriminant_certificate_from_parameter(parameter)
                waterhouse = waterhouse_intersection_classification(A, B, q)
                if not waterhouse["on_integral_compact_intersection"]:
                    raise ArithmeticError("Waterhouse classifier lost a graph point")
                stratum = waterhouse["stratum"]
                if not isinstance(stratum, str):
                    raise ArithmeticError("Waterhouse stratum lost string type")
                stratum_counts[stratum] += 1
                if waterhouse["both_tensor_input_traces_realized"]:
                    realized_point_count += 1
                guard.charge("synthetic_waterhouse_stratum_checks")
                hits.append(
                    {
                        "A": A,
                        "B": B,
                        "x": _fraction(x),
                        "y": _fraction(y),
                        "normalized_polynomial_Z0_through_Z4": [
                            _fraction(value) for value in tensor_normalized
                        ],
                        "branches": branch_rows,
                        "coefficient_map_fold_D": _fraction(
                            disc["coefficient_map_fold_D"]
                        ),
                        "hasse_endpoint_factor_E": _fraction(
                            disc["hasse_endpoint_factor_E"]
                        ),
                        "full_quartic_root_discriminant": _fraction(
                            disc["full_quartic_root_discriminant"]
                        ),
                        "waterhouse_classification": waterhouse,
                    }
                )
        if len(hits) != count_theorem["distinct_integral_hasse_lattice_points"]:
            raise ArithmeticError("square-q lattice union count theorem failed")
        if branch_incidence_count != count_theorem["four_graph_branch_incidences"]:
            raise ArithmeticError("square-q graph incidence count theorem failed")
        if realized_point_count != count_theorem["waterhouse_realized_distinct_points"]:
            raise ArithmeticError("square-q Waterhouse count theorem failed")
        output.append(
            {
                "q": q,
                "sqrt_q": s,
                "hasse_lattice_points_checked": lattice_points,
                "intersection_lattice_point_count": len(hits),
                "graph_branch_incidence_count": branch_incidence_count,
                "waterhouse_realized_intersection_point_count": realized_point_count,
                "intersection_stratum_counts": dict(sorted(stratum_counts.items())),
                "all_q_count_theorem_specialization": count_theorem,
                "intersection_lattice_points": hits,
                "realizability_status": "CLASSIFIED_TRACE_BY_TRACE_FROM_WATERHOUSE_THEOREM_4_1; separate local isogeny classes only",
            }
        )
    return output


def build_fixture(q_values: Iterable[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"frozen packet requires exactly q={FROZEN_Q_VALUES}")
    so4, sym3 = load_locked_sources()
    guard = ResourceGuard()

    residuals = symbolic_residuals()
    nonzero = {name: value for name, value in residuals.items() if value}
    if nonzero:
        raise ArithmeticError(f"nonzero symbolic residuals: {sorted(nonzero)}")
    guard.charge("symbolic_zero_residual_certificates", len(residuals))

    frozen = _frozen_nonsquare_replay(so4, guard)
    sym3_audit = _audit_sym3_frozen_factors(sym3, guard)
    square = _synthetic_square_lattice_replay(guard)

    payload: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_so4_sym3_spectral_intersection.v1",
        "raw_fixture_id": "elliptic-so4-sym3-spectral-intersection-v1",
        "status": "EXACT_COMPACT_INTERSECTION_NONSQUARE_OBSTRUCTION_SQUARE_LATTICE_COUNTS_AND_WATERHOUSE_STRATA",
        "rigor_level": {
            "compact_intersection": "PROVED_BY_EXACT_BIVARIATE_FACTORIZATION_AND_FOUR_GRAPH_PARAMETERIZATIONS",
            "nonsquare_prime_power_obstruction": "PROVED_FOR_ALL_ODD_PRIME_POWERS_BY_PARITY_OF_P_ADIC_VALUATIONS",
            "discriminant_restrictions": "PROVED_SYMBOLICALLY_AND_CHECKED_BY_DIRECT_SYLVESTER_RESULTANTS",
            "locked_finite_replay": "EXACT_FOR_ALL_645_SOURCE_HISTOGRAM_ATOM_PAIRS",
            "square_q_lattice_counts": "PROVED_FOR_EVERY_Q_POW_2K_BY_AN_EXPLICIT_INTEGRAL_PARAMETERIZATION_AND_GRAPH_OVERLAP_COUNT",
            "square_q_realizability": "CLASSIFIED_FROM_WATERHOUSE_THEOREM_4_1_INTO_THREE_REPEATED_ROOT_STRATA",
            "representation_homomorphism_global_correspondence_and_novelty": "NOT_INFERRED",
        },
        "conventions": {
            "tensor_inputs": "P_A(T)=1+A*T+q*T^2 and P_B(T)=1+B*T+q*T^2",
            "tensor_normalization": "u=A/sqrt(q), v=B/sqrt(q), T=Z/q",
            "tensor_normalized_factor": "1-x*Z+y*Z^2-x*Z^3+Z^4 with x=u*v and y=u^2+v^2-2",
            "sym3_source_input": "1+a*T+q*T^2=1-c*T+q*T^2, where c=-a is geometric trace",
            "sym3_normalization": "t=c/sqrt(q), T=Z/q^(3/2), x=t^3-2*t, y=t^4-3*t^2+2",
            "sign_bridge": "on u=epsilon*(v^2-2), c=epsilon*B and a=-epsilon*B; on v=epsilon*(u^2-2), c=epsilon*A and a=-epsilon*A",
            "weight_and_dilation": "the tensor factor has weight 2 and Sym3 has weight 3; at q=s^2 graph points P_tensor(s*T)=P_Sym3,c(T), equivalently the two factors agree after T=Z/q and T=Z/q^(3/2)",
        },
        "exact_compact_intersection_theorem": {
            "sym3_curve": "F3(x,y)=-x^4+x^2*y+x^2+y^3-2*y^2",
            "substitution": "x=u*v, y=u^2+v^2-2",
            "factorization": "F3=(u-v^2+2)*(u+v^2-2)*(u^2-v-2)*(u^2+v-2)",
            "graphs": [
                "u=+(v^2-2)",
                "u=-(v^2-2)",
                "v=+(u^2-2)",
                "v=-(u^2-2)",
            ],
            "doubling_interpretation": "t^2-2 is the SU(2) trace of the squared torus element; each orientation has an ordinary and central-sign-twisted branch",
            "spectral_identity": "on a graph the SO4 tensor torus weights {z*w,z/w,w/z,1/(z*w)} become {r^3,r,r^(-1),r^(-3)} after z=+/-w^2 (or the swapped relation)",
            "exact_square_q_dilation_identity": "if q=s^2, then P_tensor(s*T)=P_Sym3,c(T), with c=epsilon*B on u=epsilon*(v^2-2) and c=epsilon*A on the swapped graph",
            "coefficient_proof_of_dilation": "S_c=c^3-2q*c=s*A*B and D_c=c^4-3q*c^2+2q^2=q*(A^2+B^2-2q); the reciprocal coefficients then match automatically",
            "homomorphism_firewall": "this is an identity on one-dimensional maximal-torus spectral loci; the squaring relation does not define a claimed SU(2)->SU(2)xSU(2) representation homomorphism",
        },
        "integral_odd_prime_power_theorem": {
            "cleared_equation": "q^4*F3=[q*A^2-(B^2-2q)^2]*[(A^2-2q)^2-q*B^2]",
            "nonsquare_case": "if q=p^e with odd e, either zero factor equates an odd p-adic valuation e+2v_p(nonzero trace) with an even valuation; the zero-trace fallback would require a square to equal 2q and is impossible for odd p",
            "conclusion": "for nonsquare odd prime-power q there are no integral A,B on the compact spectral intersection, even before Hasse bounds",
            "square_case": "if q=s^2, the locus is exactly s*A=+/- (B^2-2q) or s*B=+/- (A^2-2q)",
            "divisibility_note": "on the first orientation integrality requires s|B^2, and on the second s|A^2",
            "parameterization": "for q=p^(2k), put M=p^floor(k/2); on s*A=epsilon*(B^2-2q), B=p^ceil(k/2)*m with |m|<=2M and A=epsilon*(p^(k mod 2)*m^2-2p^k), and swap A,B for the other orientation",
            "all_q_lattice_counts": "each oriented signed graph has 4M+1 parameters; four graphs have 16M+4 incidences; exactly four endpoint and four unit pairs are double incidences, so the union has 16M-4 points",
            "waterhouse_realized_strata": {
                "endpoint_endpoint": "(A/s,B/s) in {+/-2}x{+/-2}: 4 points, always realized",
                "unit_unit": "(A/s,B/s) in {+/-1}x{+/-1}: 4 points iff p is not 1 modulo 3",
                "endpoint_zero": "(+/-2,0) and (0,+/-2): 4 points iff p is not 1 modulo 4",
                "counts_by_odd_prime_residue": "4,8,8,12 for p congruent to 1,5,7,11 modulo 12; p=3 gives 12",
                "p_equals_3_boundary": "Waterhouse case (3) includes p=3; at q=3^(odd), case (4) cannot rescue an intersection because the nonsquare valuation theorem rules out every integral pair",
            },
            "universal_ghost": "at q=p^4, (A,B)=(1-2p^2,p) is an integral Hasse graph point; A is ordinary-realized while B is p-divisible and outside Waterhouse's special traces, so the pair is not simultaneously realized",
            "converse_scope": "Waterhouse classifies existence of separate local elliptic isogeny classes with the two traces; it does not construct a relation between curves or a compatible global family",
        },
        "discriminant_restriction_theorem": {
            "parameter": "on each graph choose normalized Sym3 geometric trace t=epsilon*v or epsilon*u",
            "SO4_fold_discriminant": "D=(y+2)^2-4*x^2=(t^2-1)^2*(t^2-4)^2",
            "SO4_hasse_endpoint_factor": "E=x^2-4*(y-2)=t^2*(t^2-4)^2",
            "full_quartic_root_discriminant": "Disc_Z=D*E^2=t^4*(t^2-1)^2*(t^2-4)^6",
            "unnormalized_square_q_form": "for c=s*t, D=(c^2-q)^2*(c^2-4q)^2/q^4, E=c^2*(c^2-4q)^2/q^3, Disc=c^4*(c^2-q)^2*(c^2-4q)^6/q^10",
            "wall_classification": {
                "coefficient_map_fold": "t^2 in {1,4}",
                "hasse_endpoint_wall": "t=0 or t^2=4",
                "full_repeated_root_locus": "t=0 or t^2 in {1,4}",
                "fold_endpoint_intersection": "t^2=4",
            },
            "direct_check": "the full formula is independently checked with the 7-by-7 Sylvester resultant at every synthetic square-q intersection point and every incident graph parameter",
        },
        "symbolic_certificates": {
            "residual_count": len(residuals),
            "all_residuals_are_zero": True,
            "residuals": {
                name: [
                    list(key) + [coefficient]
                    if isinstance(key, tuple)
                    else [key, coefficient]
                    for key, coefficient in sorted(value.items())
                ]
                for name, value in residuals.items()
            },
        },
        "locked_nonsquare_histogram_replay": {
            "families": frozen,
            "aggregate": {
                "q_values": list(FROZEN_Q_VALUES),
                "ordered_atom_pairs_checked": sum(
                    row["ordered_atom_pairs_checked"] for row in frozen
                ),
                "intersection_atom_hit_count": 0,
                "intersection_represented_mass": 0,
            },
        },
        "locked_sym3_factor_convention_audit": {
            "families": sym3_audit,
            "aggregate_raw_factor_atoms_checked": sum(
                row["raw_factor_atoms_checked"] for row in sym3_audit
            ),
        },
        "synthetic_square_q_hasse_lattice_replay": {
            "purpose": "nonvacuous exact checks of all four branches, sign bridges, raw dilation identities, discriminant restrictions, lattice counts, and Waterhouse strata",
            "families": square,
            "realizability_boundary": "Waterhouse classifies trace realization by separate elliptic isogeny classes; it supplies no shared curve, correspondence, or global compatible system",
        },
        "all_square_prime_power_count_examples": [
            square_prime_power_intersection_counts(3, 1),
            square_prime_power_intersection_counts(5, 1),
            square_prime_power_intersection_counts(3, 2),
            square_prime_power_intersection_counts(5, 2),
        ],
        "literature_boundary": {
            "primary_reference": "William C. Waterhouse, Abelian varieties over finite fields, Annales scientifiques de l'Ecole Normale Superieure 2 (1969), Theorem 4.1, https://numdam.org/articles/10.24033/asens.1183/",
            "use": "only the existence/nonexistence classification of individual elliptic Frobenius traces over F_q, specifically cases (2), (3), and (5)(ii)",
            "not_imported": "no curve-pair correspondence, representation homomorphism, automorphic transfer, cross-prime compatibility, or literature-priority claim",
        },
        "producer_and_source_locks": {
            "input_method": "two internally authenticated JSON artifacts plus LF-normalized fixture and producer file locks",
            "locks": _source_locks(),
        },
        "resource_contract": {
            "atom_pair_cap_inclusive": guard.atom_pair_cap,
            "actual_locked_source_histogram_atom_pairs": guard.atom_pairs,
            "exclusive_accounted_work_unit_cap": guard.work_cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total_work,
            },
            "unit_definition": "declared histogram pairs, Hasse-lattice points, and high-level exact identity checks; not CPU instructions",
            "field_curve_or_model_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "maximum_polynomial_degree": 24,
        },
        "scope_firewall": {
            "no_representation_homomorphism": "a torus-angle doubling graph and equality of normalized spectra do not supply an SU(2) representation homomorphism into the two tensor factors",
            "no_unscaled_raw_factor_identity": "there is an exact P_tensor(s*T)=P_Sym3,c(T) identity at square-q graph points, but different motivic weights prevent identifying P_tensor(T) and P_Sym3,c(T) in the same unscaled variable",
            "no_local_to_global_correspondence": "a coefficient coincidence at one q does not construct isogenies, motives, automorphic transfers, compatible systems, or a global Euler product",
            "no_realizability_to_correspondence_upgrade": "Waterhouse gives separate local isogeny classes for the classified traces; it does not link the two tensor inputs to the Sym3 source by a curve-level or global correspondence",
            "no_measure_or_asymptotic_claim": "zero hits in five locked nonsquare-prime rows follow from an all-q arithmetic obstruction, not a fitted probability or convergence law",
            "no_novelty_priority_claim": "the exact packaging is recorded for later comparison; no literature-priority claim is made",
            "no_RH_or_GRH_claim": "compact spectral intersections and finite-field local factors imply no zero-free region, RH, or GRH theorem",
        },
        "next_targets": [
            {
                "name": "cross_prime_doubling_correspondence",
                "known": "at one place the normalized Frobenius angles satisfy a doubling or sign-twisted doubling relation",
                "open": "decide whether any geometric family enforces one orientation coherently across primes and what global functorial object, if any, results",
            },
            {
                "name": "intersection_multiplicity_and_singularities",
                "known": "the restricted discriminant has special parameters t=0,+/-1,+/-2",
                "open": "compute scheme-theoretic graph intersections and relate multiplicities to compact centralizers and endoscopic degeneration",
            },
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def _write(path: Path) -> None:
    path.write_text(
        json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {path}")


def _check(path: Path) -> None:
    expected = build_fixture()
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit(f"fixture is stale: {path}")
    print(f"fixture is current: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    action.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    arguments = parser.parse_args()
    if arguments.write is not None:
        _write(arguments.write)
    elif arguments.check is not None:
        _check(arguments.check)
    else:
        print(json.dumps(build_fixture(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
