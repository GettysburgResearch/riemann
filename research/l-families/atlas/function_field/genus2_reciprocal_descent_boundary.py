#!/usr/bin/env python3
"""Prove the genus-two reciprocal-descent phase boundary.

For an even reciprocal endpoint d, the degree-five squarefree sieve contains
the coefficient C_5 of the quadratic L-polynomial attached to a squarefree
degree-d modulus.  The completed functional equation removes C_5 through
d=10.  Starting at d=12 it cannot do so: reciprocity turns the C_5 aggregate
into G_5, whose squarefree degree-five part is the target itself.

The replay uses only exact sparse-polynomial and formal coefficient algebra
for 2 <= d <= 20.  It enumerates no finite field, curve, or polynomial family.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_reciprocal_descent_boundary.json"
NOTE_PATH = HERE / "GENUS2_RECIPROCAL_DESCENT_BOUNDARY.md"
TEST_PATH = ROOT / "tests" / "test_genus2_reciprocal_descent_boundary.py"

SYM6_PATH = HERE / "genus2_sym6_marked_trace_average.json"
SYM8_PATH = HERE / "genus2_sym8_marked_trace_average.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "sym6": {
        "path": SYM6_PATH,
        "lf_sha256": (
            "4e6156e8ca4f8b652e02961d3aa5f3ea63c9b42243908d1ecab8b94c08d253a6"
        ),
        "payload_sha256": (
            "7bf31859372bb2a292f8321794f9b05859d2def82b1dd59ad83ab992088a5e86"
        ),
        "audited_commit": "522bc6b454016a07a9c65aaa6177d0340d70f5dc",
    },
    "sym8": {
        "path": SYM8_PATH,
        "lf_sha256": (
            "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233"
        ),
        "payload_sha256": (
            "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae"
        ),
        "audited_commit": "dc63f02d0897e10936ef0767a1c8e6f15ac49e06",
    },
}

MIN_ENDPOINT = 2
MAX_ENDPOINT = 20
MAX_SYMBOLIC_OPERATIONS = 2048
MAX_SOURCE_BYTES = 65_536
MAX_SOURCE_ATOMS = 32
MAX_WALL_SECONDS = 3.0

Monomial: TypeAlias = tuple[int, ...]
SparsePolynomial: TypeAlias = dict[Monomial, Fraction]


@dataclass
class ResourceGuard:
    """Bound every symbolic operation and every imported scalar."""

    symbolic_operations: int = 0
    source_atoms: int = 0
    source_bytes: int = 0

    def operation(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        self.symbolic_operations += amount
        if self.symbolic_operations > MAX_SYMBOLIC_OPERATIONS:
            raise RuntimeError("symbolic-operation cap exceeded")

    def atoms(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("source-atom increment must be nonnegative")
        self.source_atoms += amount
        if self.source_atoms > MAX_SOURCE_ATOMS:
            raise RuntimeError("source-atom cap exceeded")

    def source_size(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("source-byte increment must be nonnegative")
        self.source_bytes += amount
        if self.source_bytes > MAX_SOURCE_BYTES:
            raise RuntimeError("source-byte cap exceeded")


class PolynomialRing:
    """A tiny exact sparse-polynomial ring with an explicit operation meter."""

    def __init__(self, names: tuple[str, ...], guard: ResourceGuard) -> None:
        if not names or len(set(names)) != len(names):
            raise ValueError("ring variables must be nonempty and distinct")
        self.names = names
        self.guard = guard
        self.zero_monomial = (0,) * len(names)

    @staticmethod
    def _clean(poly: SparsePolynomial) -> SparsePolynomial:
        return {monomial: value for monomial, value in poly.items() if value}

    def constant(self, value: int | Fraction) -> SparsePolynomial:
        self.guard.operation()
        coefficient = Fraction(value)
        if not coefficient:
            return {}
        return {self.zero_monomial: coefficient}

    def variable(self, name: str) -> SparsePolynomial:
        self.guard.operation()
        try:
            index = self.names.index(name)
        except ValueError as exc:
            raise KeyError(name) from exc
        monomial = [0] * len(self.names)
        monomial[index] = 1
        return {tuple(monomial): Fraction(1)}

    def add(self, left: SparsePolynomial, right: SparsePolynomial) -> SparsePolynomial:
        self.guard.operation(len(left) + len(right) + 1)
        result = dict(left)
        for monomial, coefficient in right.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
        return self._clean(result)

    def neg(self, value: SparsePolynomial) -> SparsePolynomial:
        self.guard.operation(len(value) + 1)
        return {monomial: -coefficient for monomial, coefficient in value.items()}

    def sub(self, left: SparsePolynomial, right: SparsePolynomial) -> SparsePolynomial:
        return self.add(left, self.neg(right))

    def mul(self, left: SparsePolynomial, right: SparsePolynomial) -> SparsePolynomial:
        self.guard.operation(len(left) * len(right) + 1)
        result: SparsePolynomial = {}
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                monomial = tuple(
                    a + b for a, b in zip(left_monomial, right_monomial, strict=True)
                )
                result[monomial] = (
                    result.get(monomial, Fraction(0))
                    + left_coefficient * right_coefficient
                )
        return self._clean(result)

    def power(self, value: SparsePolynomial, exponent: int) -> SparsePolynomial:
        if exponent < 0:
            raise ValueError("polynomial exponent must be nonnegative")
        result = self.constant(1)
        base = value
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = self.mul(result, base)
            remaining //= 2
            if remaining:
                base = self.mul(base, base)
        return result

    def scale(
        self, value: SparsePolynomial, coefficient: int | Fraction
    ) -> SparsePolynomial:
        return self.mul(self.constant(coefficient), value)

    def support(self, value: SparsePolynomial) -> list[str]:
        indices = {
            index
            for monomial in value
            for index, exponent in enumerate(monomial)
            if exponent
        }
        return [self.names[index] for index in sorted(indices)]

    def coefficient_of_variable(
        self, value: SparsePolynomial, name: str
    ) -> SparsePolynomial:
        """Return the coefficient of a variable when it occurs only linearly."""

        try:
            index = self.names.index(name)
        except ValueError as exc:
            raise KeyError(name) from exc
        result: SparsePolynomial = {}
        for monomial, coefficient in value.items():
            exponent = monomial[index]
            if exponent > 1:
                raise ArithmeticError(f"{name} occurred nonlinearly")
            if exponent == 1:
                reduced = list(monomial)
                reduced[index] = 0
                result[tuple(reduced)] = coefficient
        self.guard.operation(len(value) + 1)
        return self._clean(result)

    def serialize(self, value: SparsePolynomial) -> list[dict[str, object]]:
        rows: list[dict[str, object]] = []
        for monomial, coefficient in sorted(value.items()):
            if coefficient.denominator == 1:
                serialized_coefficient: int | str = coefficient.numerator
            else:
                serialized_coefficient = (
                    f"{coefficient.numerator}/{coefficient.denominator}"
                )
            rows.append(
                {
                    "coefficient": serialized_coefficient,
                    "powers": {
                        name: exponent
                        for name, exponent in zip(self.names, monomial, strict=True)
                        if exponent
                    },
                }
            )
        return rows


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


def _lf_sha256(data: bytes) -> str:
    normalized = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _sum_polynomials(
    ring: PolynomialRing, values: list[SparsePolynomial]
) -> SparsePolynomial:
    result = ring.constant(0)
    for value in values:
        result = ring.add(result, value)
    return result


def _derive_squarefree_sieve(guard: ResourceGuard) -> dict[str, object]:
    ring = PolynomialRing(("q", "ell", "k"), guard)
    q = ring.variable("q")
    ell = ring.variable("ell")
    k = ring.variable("k")
    one = ring.constant(1)
    two = Fraction(1, 2)

    available_linears = ring.sub(q, ell)
    linear_pairs = ring.scale(
        ring.mul(available_linears, ring.sub(available_linears, one)), two
    )
    irreducible_quadratics = ring.scale(ring.mul(q, ring.sub(q, one)), two)
    available_irreducible_quadratics = ring.sub(irreducible_quadratics, k)
    signed_degree_two = ring.sub(linear_pairs, available_irreducible_quadratics)

    expected = ring.add(
        ring.sub(
            ring.scale(ring.mul(ell, ring.add(ell, one)), two),
            ring.mul(q, ell),
        ),
        k,
    )
    if signed_degree_two != expected:
        raise ArithmeticError("degree-two squarefree-sieve coefficient failed")

    return {
        "mobius_square_identity": "mu^2(D)=sum_(A^2|D) mu(A)",
        "degree_five_decomposition": "D=A^2*B with deg(A)=0,1,2",
        "degree_A_0_weight": "1",
        "degree_A_1_weight": "-(q-ell)",
        "degree_A_2_signed_count": ring.serialize(signed_degree_two),
        "degree_A_2_closed_form": "binom(ell+1,2)+k-q*ell",
        "identity": (
            "S_5(f)=C_5(f)-(q-ell(f))*C_3(f)+(binom(ell(f)+1,2)+k(f)-q*ell(f))*C_1(f)"
        ),
        "endpoint_dependence": "none: the same sieve holds for every modulus degree",
    }


def _completed_coefficient(
    ring: PolynomialRing,
    m: int,
    index: int,
    q: SparsePolynomial,
    cumulatives: dict[int, SparsePolynomial],
    x5: SparsePolynomial,
) -> SparsePolynomial:
    """Return Q_index after C_1,...,C_4 coordinate substitution."""

    if index < 0 or index > 2 * m:
        return ring.constant(0)
    if index == 0:
        return ring.constant(1)
    if index <= m:
        if index <= 4:
            return cumulatives[index]
        if index == 5:
            return x5
        raise ArithmeticError("the C5 boundary proof requested an unused Q coefficient")

    reflected = 2 * m - index
    if reflected == 0:
        low = ring.constant(1)
    elif reflected <= 4:
        low = cumulatives[reflected]
    elif reflected == 5:
        low = x5
    else:
        raise ArithmeticError("the C5 boundary proof requested an unused reflection")
    return ring.mul(ring.power(q, index - m), low)


def _expected_c5(
    ring: PolynomialRing,
    endpoint: int,
    q: SparsePolynomial,
    c: dict[int, SparsePolynomial],
    x5: SparsePolynomial,
) -> SparsePolynomial:
    one = ring.constant(1)
    if endpoint in (2, 4):
        return ring.constant(0)
    if endpoint == 6:
        return ring.neg(ring.power(q, 2))
    if endpoint == 8:
        return ring.sub(
            ring.mul(ring.mul(q, ring.sub(q, one)), ring.add(one, c[1])),
            ring.mul(q, c[2]),
        )
    if endpoint == 10:
        cumulative_three = _sum_polynomials(ring, [one, c[1], c[2], c[3]])
        return ring.sub(ring.mul(ring.sub(q, one), cumulative_three), c[4])
    cumulative_four = _sum_polynomials(ring, [one, c[1], c[2], c[3], c[4]])
    return ring.sub(x5, cumulative_four)


def _formula_for_endpoint(endpoint: int) -> str:
    if endpoint in (2, 4):
        return "C_5=0"
    if endpoint == 6:
        return "C_5=-q^2"
    if endpoint == 8:
        return "C_5=q*(q-1)*(1+C_1)-q*C_2"
    if endpoint == 10:
        return "C_5=(q-1)*(1+C_1+C_2+C_3)-C_4"
    if endpoint == 12:
        return "C_5=X_5-(1+C_1+C_2+C_3+C_4), with X_5=Q_5 central"
    return "C_5=X_5-(1+C_1+C_2+C_3+C_4), with X_5=Q_5 precentral"


def _status_for_endpoint(endpoint: int) -> str:
    if endpoint in (2, 4):
        return "ZERO_BEYOND_L_POLYNOMIAL_DEGREE"
    if endpoint == 6:
        return "ELIMINATED_TO_CONSTANT"
    if endpoint in (8, 10):
        return "ELIMINATED_TO_C0_THROUGH_C4"
    if endpoint == 12:
        return "FREE_CENTRAL_COMPLETED_COEFFICIENT"
    return "FREE_PRECENTRAL_COMPLETED_COEFFICIENT"


def _witness_pair(m: int, guard: ResourceGuard) -> dict[str, object]:
    if m < 5:
        raise ValueError("non-determination witness requires m >= 5")
    ring = PolynomialRing(("q",), guard)
    q = ring.variable("q")
    size = 2 * m + 1

    first = [ring.constant(0) for _ in range(size)]
    first[0] = ring.constant(1)
    first[2 * m] = ring.power(q, m)
    second = [dict(value) for value in first]
    second[5] = ring.add(second[5], ring.constant(1))
    if m > 5:
        second[2 * m - 5] = ring.add(second[2 * m - 5], ring.power(q, m - 5))

    for coefficients in (first, second):
        for index in range(m + 1):
            reflected = ring.mul(ring.power(q, m - index), coefficients[index])
            if coefficients[2 * m - index] != reflected:
                raise ArithmeticError("reciprocal witness failed functional equation")

    def l_prefix(coefficients: list[SparsePolynomial]) -> list[SparsePolynomial]:
        result = [coefficients[0]]
        for index in range(1, 6):
            result.append(ring.sub(coefficients[index], coefficients[index - 1]))
        return result

    first_l = l_prefix(first)
    second_l = l_prefix(second)
    if first_l[:5] != second_l[:5]:
        raise ArithmeticError("witness pair changed C_0,...,C_4")
    if first_l[5] == second_l[5]:
        raise ArithmeticError("witness pair did not change C_5")

    added_terms = [{"Q_index": 5, "coefficient": "1"}]
    if m > 5:
        added_terms.append({"Q_index": 2 * m - 5, "coefficient": f"q^{m - 5}"})
    return {
        "base_nonzero_terms": [
            {"Q_index": 0, "coefficient": "1"},
            {"Q_index": 2 * m, "coefficient": f"q^{m}"},
        ],
        "second_completion_added_terms": added_terms,
        "common_C_0_through_C_4": ["1", "-1", "0", "0", "0"],
        "first_C_5": "0",
        "second_C_5": "1",
        "both_completed_functional_equations_verified": True,
        "realizability_status": "FORMAL_FUNCTIONAL_EQUATION_WITNESS_ONLY",
    }


def _derive_phase_panel(guard: ResourceGuard) -> list[dict[str, object]]:
    ring = PolynomialRing(("q", "c1", "c2", "c3", "c4", "x5"), guard)
    q = ring.variable("q")
    c = {index: ring.variable(f"c{index}") for index in range(1, 5)}
    x5 = ring.variable("x5")
    one = ring.constant(1)
    cumulatives: dict[int, SparsePolynomial] = {}
    for index in range(1, 5):
        cumulatives[index] = _sum_polynomials(
            ring, [one] + [c[position] for position in range(1, index + 1)]
        )

    rows: list[dict[str, object]] = []
    for endpoint in range(MIN_ENDPOINT, MAX_ENDPOINT + 1, 2):
        m = endpoint // 2 - 1
        q4 = _completed_coefficient(ring, m, 4, q, cumulatives, x5)
        q5 = _completed_coefficient(ring, m, 5, q, cumulatives, x5)
        derived = ring.sub(q5, q4)
        expected = _expected_c5(ring, endpoint, q, c, x5)
        if derived != expected:
            raise ArithmeticError(f"C5 functional-equation row failed at d={endpoint}")

        x5_coefficient = ring.coefficient_of_variable(derived, "x5")
        eliminable = not x5_coefficient
        if eliminable != (endpoint <= 10):
            raise ArithmeticError("phase-boundary classification drifted")

        row: dict[str, object] = {
            "endpoint_d": endpoint,
            "m": m,
            "completed_degree": 2 * m,
            "L_polynomial_degree": endpoint - 1,
            "C5_formula": _formula_for_endpoint(endpoint),
            "C5_exact_sparse_polynomial": ring.serialize(derived),
            "C5_variable_support": ring.support(derived),
            "functional_equation_eliminates_C5": eliminable,
            "status": _status_for_endpoint(endpoint),
        }
        if endpoint >= 12:
            row["non_determination_witness"] = _witness_pair(m, guard)
        rows.append(row)
    return rows


def _derive_self_reference(guard: ResourceGuard) -> dict[str, object]:
    ring = PolynomialRing(("q", "T_d", "R5_d", "G3_d", "Lambda3_d", "Q1_d"), guard)
    q = ring.variable("q")
    target = ring.variable("T_d")
    remainder = ring.variable("R5_d")
    g3 = ring.variable("G3_d")
    lambda3 = ring.variable("Lambda3_d")
    q1 = ring.variable("Q1_d")

    g5 = ring.add(target, remainder)
    descent_rhs = _sum_polynomials(ring, [g5, ring.neg(ring.mul(q, g3)), lambda3, q1])
    residual = ring.sub(target, descent_rhs)
    target_coefficient = ring.coefficient_of_variable(residual, "T_d")
    if target_coefficient:
        raise ArithmeticError("target failed to cancel from reciprocal descent")

    expected_residual = _sum_polynomials(
        ring, [ring.neg(remainder), ring.mul(q, g3), ring.neg(lambda3), ring.neg(q1)]
    )
    if residual != expected_residual:
        raise ArithmeticError("self-reference residual identity drifted")

    return {
        "unreduced_descent": "T_d=G5_d-q*G3_d+Lambda3_d+Q1_d",
        "degree_five_split": "G5_d=T_d+R5_d",
        "squarefree_part_reason": (
            "for squarefree degree-five D, g_d(D)=r_D(d) by even-degree reciprocity"
        ),
        "nonsquarefree_remainder": ("R5_d=sum_(deg h=5, h nonsquarefree) g_d(h)"),
        "target_coefficient_after_substitution": 0,
        "exact_residual_sparse_polynomial": ring.serialize(residual),
        "consistency_identity": "R5_d-q*G3_d+Lambda3_d+Q1_d=0",
        "interpretation": (
            "the one-step sieve/reciprocity equation is self-referential and does not solve T_d"
        ),
    }


def _preboundary_aggregate_rows() -> list[dict[str, object]]:
    return [
        {
            "endpoint_d": 2,
            "C5_aggregate": "0",
            "one_step_descent": "T_2=-q*G3_2+Lambda3_2+Q1_2",
        },
        {
            "endpoint_d": 4,
            "C5_aggregate": "0",
            "one_step_descent": "T_4=-q*G3_4+Lambda3_4+Q1_4",
        },
        {
            "endpoint_d": 6,
            "C5_aggregate": "-q^2*M_6=0",
            "one_step_descent": "T_6=-q*G3_6+Lambda3_6+Q1_6",
        },
        {
            "endpoint_d": 8,
            "C5_aggregate": "q*(q-1)*(M_8+G1_8)-q*G2_8=0",
            "one_step_descent": "T_8=-q*G3_8+Lambda3_8+Q1_8",
        },
        {
            "endpoint_d": 10,
            "C5_aggregate": ("(q-1)*(M_10+G1_10+G2_10+G3_10)-G4_10"),
            "one_step_descent": (
                "T_10=(q-1)*(G1_10+G2_10)-G3_10-G4_10+Lambda3_10+Q1_10"
            ),
        },
    ]


def _load_sources(guard: ResourceGuard) -> dict[str, dict[str, object]]:
    loaded: dict[str, dict[str, object]] = {}
    for name in sorted(SOURCE_LOCKS):
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source-lock path must be a Path")
        remaining = MAX_SOURCE_BYTES - guard.source_bytes
        if remaining < 0:
            raise RuntimeError("source-byte cap already exceeded")
        with path.open("rb") as source_handle:
            data = source_handle.read(remaining + 1)
        if len(data) > remaining:
            raise RuntimeError("source-byte cap exceeded before full read")
        guard.source_size(len(data))
        if _lf_sha256(data) != lock["lf_sha256"]:
            raise RuntimeError(f"LF-normalized source hash mismatch: {name}")
        parsed = json.loads(data)
        if parsed.get("payload_sha256") != lock["payload_sha256"]:
            raise RuntimeError(f"payload source hash mismatch: {name}")
        hash_input = dict(parsed)
        claimed = hash_input.pop("payload_sha256")
        if _canonical_sha256(hash_input) != claimed:
            raise RuntimeError(f"canonical source payload mismatch: {name}")
        guard.atoms(4)
        loaded[name] = parsed
    return loaded


def _validate_source_cross_checks(
    sources: dict[str, dict[str, object]],
) -> dict[str, object]:
    sym6 = sources["sym6"]
    sym8 = sources["sym8"]
    if sym6.get("status") != "PROVED_EXACTLY_FOR_EVERY_ODD_PRIME_POWER":
        raise RuntimeError("Sym6 source status drifted")
    if sym8.get("status") != "PROVED_EXACTLY_FOR_EVERY_ODD_PRIME_POWER":
        raise RuntimeError("Sym8 source status drifted")

    sym6_reduction = sym6.get("mobius_euler_reduction")
    sym8_reduction = sym8.get("mobius_euler_reduction")
    if not isinstance(sym6_reduction, dict) or not isinstance(sym8_reduction, dict):
        raise TypeError("marked-trace source schema drifted")
    expected6 = "C_5(f)=-q^2 and sum_(deg f=6)mu(f)=0"
    expected8 = "C_5=q*(q-1)*C_1-q*C_2+q*(q-1)"
    if sym6_reduction.get("C5_cancellation") != expected6:
        raise RuntimeError("Sym6 C5 row drifted")
    if sym8_reduction.get("even_conductor_functional_equation") != expected8:
        raise RuntimeError("Sym8 C5 row drifted")
    return {
        "sym6": {
            "cross_checked_formula": "C_5=-q^2",
            "source_status": sym6["status"],
        },
        "sym8": {
            "cross_checked_formula": "C_5=q*(q-1)*(1+C_1)-q*C_2",
            "source_status": sym8["status"],
        },
        "sym10": {
            "cross_checked_formula": "C_5=(q-1)*(1+C_1+C_2+C_3)-C_4",
            "source_status": "DERIVED_INDEPENDENTLY_NOT_IMPORTED",
            "reason": (
                "the Sym10 packet was not a stable tracked source when this lock was made"
            ),
        },
    }


def _source_manifest() -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for name in sorted(SOURCE_LOCKS):
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source-lock path must be a Path")
        manifest.append(
            {
                "name": name,
                "path": path.relative_to(ROOT).as_posix(),
                "lf_sha256": lock["lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "audited_commit": lock["audited_commit"],
                "role": "post-proof formula and provenance cross-check only",
            }
        )
    return manifest


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    guard = ResourceGuard()

    sieve = _derive_squarefree_sieve(guard)
    panel = _derive_phase_panel(guard)
    self_reference = _derive_self_reference(guard)
    symbolic_before_sources = guard.symbolic_operations

    sources = _load_sources(guard)
    cross_checks = _validate_source_cross_checks(sources)

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_reciprocal_descent_boundary.v1",
        "status": "PROVED_EXACT_FORMAL_PHASE_BOUNDARY",
        "scope": {
            "q": "formal odd prime power parameter",
            "family": "monic squarefree quintics D over F_q[T]",
            "even_endpoint_panel": list(range(MIN_ENDPOINT, MAX_ENDPOINT + 1, 2)),
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "polynomial_families_enumerated": 0,
            "numeric_approximations": 0,
        },
        "definitions": {
            "sum_convention": "every polynomial sum is over monic polynomials",
            "target": "T_d=sum_(D in H_5(q)) r_D(d)",
            "reciprocal_coefficient": ("r_D(d)=sum_(deg f=d, f squarefree)mu(f)*(D/f)"),
            "quadratic_L_coefficients": ("L_f(u)=sum_j C_j(f)u^j=(1-u)Q_f(u)"),
            "completed_degree": "for d=2m+2, deg Q_f=2m",
            "completed_functional_equation": ("Q_(2m-j)=q^(m-j)*Q_j for 0<=j<=m"),
            "reciprocal_Euler_coefficient": (
                "G_h(z)=prod_P(1-(P/h)z^deg(P))=sum_n g_n(h)z^n"
            ),
            "linear_factor_mark": (
                "lambda_d(h)=sum_(deg f=d, f squarefree)mu(f)*ell(f)*(h/f)"
            ),
            "linear_pair_mark": (
                "lambda_d^[2](h)=sum_(deg f=d, f squarefree)mu(f)*binom(ell(f),2)*(h/f)"
            ),
            "quadratic_factor_mark": (
                "kappa_d(h)=sum_(deg f=d, f squarefree)mu(f)*k(f)*(h/f)"
            ),
            "degree_three_marked_row": ("Lambda3_d=sum_(deg h=3)lambda_d(h)"),
            "degree_one_combined_row": (
                "Q1_d=sum_(deg h=1)(lambda_d^[2]+lambda_d+kappa_d-q*lambda_d)(h)"
            ),
        },
        "theorem": {
            "universal_sieve_contains_C5": True,
            "functional_equation_eliminable_even_endpoints": [2, 4, 6, 8, 10],
            "first_self_referential_endpoint": 12,
            "last_non_self_referential_endpoint_for_this_method": 10,
            "boundary_statement": (
                "C_5 is eliminated by the completed functional equation through d=10; "
                "at d=12 it contains the central completed coefficient, and for every "
                "even d>=12 it is not determined by C_0,...,C_4 from that equation"
            ),
            "method_qualification": (
                "this is a boundary for the one-step squarefree-sieve/functional-equation/"
                "reciprocity descent, not an impossibility theorem for higher moments"
            ),
        },
        "squarefree_quintic_sieve": sieve,
        "functional_equation_panel": panel,
        "preboundary_aggregate_rows": _preboundary_aggregate_rows(),
        "universal_low_degree_cancellations": {
            "M_d": "sum_(deg f=d)mu(f)=0 for d>=2 from sum_f mu(f)u^deg(f)=1-q*u",
            "G1_d": "0 for d>=1 because the inverse L-series modulo a linear is 1",
            "G2_d": (
                "q*(q-1)*1+q*(1-q)=0 for d>=1, from squarefree quadratics and L^2"
            ),
        },
        "self_reference_certificate": self_reference,
        "source_cross_checks": cross_checks,
        "source_order_firewall": {
            "formal_boundary_closed_before_sources_loaded": True,
            "symbolic_operations_before_sources": symbolic_before_sources,
            "source_role": "post-proof exact cross-check only",
            "untracked_Sym10_used_as_input": False,
        },
        "firewalls": [
            "The witness polynomials prove non-determination by the functional equation; they are not asserted to be realized by quadratic characters or curves.",
            "The phase boundary is not an impossibility theorem: self-reference means only that this one-step descent does not solve T_d.",
            "Sym10 is the last non-self-referential even endpoint only for this exact sieve/functional-equation/reciprocity method.",
            "No memberwise sign, RH, GRH, motive, compatible system, or global Euler-product claim is made.",
            "No finite field, curve family, or polynomial family is enumerated by the replay.",
            "The d=6 and d=8 packets are source-locked only after the independent formal panel closes; an unstable Sym10 draft is not imported.",
        ],
        "resource_contract": {
            "maximum_even_endpoint": MAX_ENDPOINT,
            "maximum_symbolic_operations": MAX_SYMBOLIC_OPERATIONS,
            "actual_symbolic_operations": guard.symbolic_operations,
            "maximum_source_atoms": MAX_SOURCE_ATOMS,
            "actual_source_atoms": guard.source_atoms,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "actual_source_bytes": guard.source_bytes,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact Fraction sparse-polynomial and coefficient algebra",
        },
        "source_manifest": _source_manifest(),
        "replay": {
            "producer": OUTPUT_PATH.with_suffix(".py").relative_to(ROOT).as_posix(),
            "note": NOTE_PATH.relative_to(ROOT).as_posix(),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "write": (
                "python research/l-families/atlas/function_field/"
                "genus2_reciprocal_descent_boundary.py --write"
            ),
            "check": (
                "python research/l-families/atlas/function_field/"
                "genus2_reciprocal_descent_boundary.py --check"
            ),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    elapsed = time.perf_counter() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("reciprocal-descent boundary replay exceeded wall cap")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write canonical JSON")
    parser.add_argument("--check", action="store_true", help="check canonical JSON")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
        return
    if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
        raise SystemExit(f"fixture differs: {OUTPUT_PATH}")
    print(f"OK: reciprocal-descent boundary fixture matches {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
