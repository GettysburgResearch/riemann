#!/usr/bin/env python3
"""Exact bounded proof of the marked genus-two Sym^8 trace.

For every odd prime power q this producer proves

    T_(8,0)(q) = -Theta_(8,2)(q) - q - 6,

where Theta_(8,2) is the prime-power Frobenius trace of the unique normalized
weight-eight level-two newform eta(z)^8*eta(2z)^8.  The native part is a
Möbius/Euler-reciprocal reduction to one marked-cubic sixth moment.  The sole
external theorem is the standard Eichler--Shimura trace identity on Y_0(2).
No finite field or curve family is enumerated by the theorem replay.
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

Poly = tuple[Fraction, ...]
FormalMonomial = tuple[int, int, int]
FormalPolynomial = dict[FormalMonomial, int]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym8_marked_trace_average.json"
NOTE_PATH = HERE / "GENUS2_SYM8_MARKED_TRACE_AVERAGE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym8_marked_trace_average.py"

B4_JSON_PATH = HERE / "genus2_b4_triangular_trace_average.json"
B4_NOTE_PATH = HERE / "GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md"
GENUS1_JSON_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_NOTE_PATH = HERE / "GENUS1_CUBIC_FAMILY_LAWS.md"
ADAPTER_JSON_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
ADAPTER_NOTE_PATH = HERE / "GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md"
NATIVE_JSON_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
NATIVE_NOTE_PATH = HERE / "NATIVE_QADIC_RECIPROCAL_WAVELET_SPECTROSCOPY.md"
BALANCED_JSON_PATH = HERE / "balanced_control_family_scan.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "b4": {
        "path": B4_JSON_PATH,
        "lf": "31eec8f78bc81eb9d157f727c229efb16d112b94e7c27dbf0ea1f81f5005fde2",
        "payload": "d12099e24425badd5106f61caa151578ee04dd099a221eca7217b599783c5e5b",
    },
    "genus1": {
        "path": GENUS1_JSON_PATH,
        "lf": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
        "payload": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
    },
    "adapter": {
        "path": ADAPTER_JSON_PATH,
        "lf": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
    },
    "native": {
        "path": NATIVE_JSON_PATH,
        "lf": "aef506afa6b9b29f10528b634f45c7eab96abc36c6cd2de886262e834fcb2d43",
        "payload": "4e366316c6d55488b41e0104f6bee6c947220d7989ea7aa1381b5d72a099b882",
    },
    "balanced": {
        "path": BALANCED_JSON_PATH,
        "lf": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
    },
}
THEOREM_SOURCE_NAMES = ("b4", "genus1", "adapter")
HELD_OUT_SOURCE_NAMES = ("native", "balanced")

MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS = 4096
MAX_ETA_FOURIER_DEGREE = 9
MAX_WALL_SECONDS = 10.0


@dataclass
class ResourceGuard:
    symbolic_operations: int = 0
    input_atoms: int = 0

    def operation(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        self.symbolic_operations += amount
        self._check()

    def atoms(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("atom increment must be nonnegative")
        self.input_atoms += amount
        self._check()

    def _check(self) -> None:
        if (
            self.symbolic_operations + self.input_atoms
            > MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS
        ):
            raise RuntimeError("symbolic-operation/input-atom cap exceeded")


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


def _load_sources(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
    if not names or len(set(names)) != len(names):
        raise ValueError("source names must be nonempty and distinct")
    sources: dict[str, dict[str, object]] = {}
    for name in names:
        if name not in SOURCE_LOCKS:
            raise ValueError(f"unknown source lock: {name}")
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path) or _lf_sha256(path) != lock["lf"]:
            raise RuntimeError(f"source lock failed: {name}")
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not an object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != lock["payload"] or claimed != _canonical_sha256(payload):
            raise ValueError(f"source payload failed: {name}")
        sources[name] = value
    return sources


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
    for i, a_coefficient in enumerate(left):
        for j, b_coefficient in enumerate(right):
            result[i + j] += a_coefficient * b_coefficient
    return _trim(result)


def p_sub(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    return p_add(left, p_scale(right, -1, guard), guard)


def p_sum(values: list[Poly], guard: ResourceGuard) -> Poly:
    result = poly(0)
    for value in values:
        result = p_add(result, value, guard)
    return result


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


def _formal_add(
    left: FormalPolynomial, right: FormalPolynomial, guard: ResourceGuard
) -> FormalPolynomial:
    guard.operation(len(left) + len(right))
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def _formal_shift(
    value: FormalPolynomial,
    guard: ResourceGuard,
    *,
    q_degree: int = 0,
    s_degree: int = 0,
    n_degree: int = 0,
    scale: int = 1,
) -> FormalPolynomial:
    if min(q_degree, s_degree, n_degree) < 0:
        raise ValueError("formal exponent shift must be nonnegative")
    guard.operation(len(value))
    return {
        (q_exp + q_degree, s_exp + s_degree, n_exp + n_degree): (scale * coefficient)
        for (q_exp, s_exp, n_exp), coefficient in value.items()
        if scale * coefficient
    }


def _serialize_formal(value: FormalPolynomial) -> list[dict[str, int]]:
    return [
        {
            "q_degree": monomial[0],
            "s_degree": monomial[1],
            "N_degree": monomial[2],
            "coefficient": value[monomial],
        }
        for monomial in sorted(value)
    ]


def _euler_recurrence_certificate(guard: ResourceGuard) -> dict[str, object]:
    """Derive g_8 and lambda_8 in Q[q,s,N], rather than inserting them."""

    one: FormalPolynomial = {(0, 0, 0): 1}
    g_rows = [one, {(0, 1, 0): -1}]
    for degree in range(2, 9):
        next_row = _formal_add(
            _formal_shift(g_rows[degree - 1], guard, s_degree=1, scale=-1),
            _formal_shift(g_rows[degree - 2], guard, q_degree=1, scale=-1),
            guard,
        )
        g_rows.append(next_row)

    expected_g8: FormalPolynomial = {
        (0, 8, 0): 1,
        (1, 6, 0): -7,
        (2, 4, 0): 15,
        (3, 2, 0): -10,
        (4, 0, 0): 1,
    }
    if g_rows[8] != expected_g8:
        raise ArithmeticError("Euler recurrence failed at g8")

    lambda8: FormalPolynomial = {}
    for marked_degree in range(1, 9):
        if marked_degree % 2:
            term = _formal_shift(g_rows[8 - marked_degree], guard, s_degree=1, scale=-1)
        else:
            term = _formal_shift(g_rows[8 - marked_degree], guard, n_degree=1, scale=-1)
        lambda8 = _formal_add(lambda8, term, guard)

    expected_lambda8: FormalPolynomial = {
        (0, 8, 0): 1,
        (0, 6, 0): 1,
        (1, 6, 0): -6,
        (0, 6, 1): -1,
        (0, 4, 0): 1,
        (1, 4, 0): -4,
        (2, 4, 0): 10,
        (0, 4, 1): -1,
        (1, 4, 1): 5,
        (0, 2, 0): 1,
        (1, 2, 0): -2,
        (2, 2, 0): 3,
        (3, 2, 0): -4,
        (0, 2, 1): -1,
        (1, 2, 1): 3,
        (2, 2, 1): -6,
        (0, 0, 1): -1,
        (1, 0, 1): 1,
        (2, 0, 1): -1,
        (3, 0, 1): 1,
    }
    if lambda8 != expected_lambda8:
        raise ArithmeticError("distinguished-linear recurrence failed at lambda8")

    return {
        "ring": "Z[q,s,N]",
        "recurrence": "g_0=1; g_1=-s; g_n=-s*g_(n-1)-q*g_(n-2)",
        "marked_formula": (
            "lambda_8=-sum_(1<=m<=8)p_m*g_(8-m), p_m=s for odd m and N for even m"
        ),
        "g_8": _serialize_formal(g_rows[8]),
        "lambda_8": _serialize_formal(lambda8),
    }


def _validate_source_semantics(sources: dict[str, dict[str, object]]) -> None:
    genus1 = sources["genus1"].get("all_q_moment_theorem")
    if not isinstance(genus1, dict):
        raise TypeError("genus-one moment theorem missing")
    explicit = genus1.get("explicit_stack_sums")
    if not isinstance(explicit, dict):
        raise TypeError("genus-one explicit moment rows missing")
    expected_rows = {
        "W_2": "q^2-1",
        "W_4": "2*q^3-3*q-1",
        "W_6": "5*q^4-9*q^2-5*q-1",
        "W_8": "14*q^5-28*q^3-20*q^2-7*q-1",
    }
    if any(explicit.get(name) != value for name, value in expected_rows.items()):
        raise ValueError("genus-one cubic moment rows changed")

    b4 = sources["b4"].get("marked_root_cubic_lemma")
    if not isinstance(b4, dict):
        raise TypeError("B4 marked-root lemma missing")
    expected_b4 = {
        "M_111_2": [[0, 1], [1, 2], [-1, 6], [-1, 2], [1, 6]],
        "M_12_2": [[0, 1], [1, 2], [-1, 2], [-1, 2], [1, 2]],
        "three_M_111_4_plus_M_12_4": [
            [0, 1],
            [2, 1],
            [4, 1],
            [-4, 1],
            [-4, 1],
            [2, 1],
        ],
    }
    if any(b4.get(name) != value for name, value in expected_b4.items()):
        raise ValueError("B4 marked-root moments changed")

    adapter = sources["adapter"].get("trace_theorem")
    if not isinstance(adapter, dict):
        raise TypeError("marked-stack adapter theorem missing")
    if adapter.get("generic_groupoid_formula") != (
        "Tr_stack,q(V_lambda)=1/(q*(q-1))*sum_D Tr(Frob_D|V_lambda)"
    ):
        raise ValueError("marked-stack groupoid normalization changed")


def _symbolic_theorem(guard: ResourceGuard) -> dict[str, Poly]:
    q = poly(0, 1)
    q_minus_one = poly(-1, 1)
    q_minus_three = poly(-3, 1)
    q_plus_one = poly(1, 1)
    q_factor = p_mul(q, q_minus_one, guard)

    # Source-locked total even moments over squarefree monic cubics.
    total_0 = p_mul(q_factor, q, guard)
    total_2 = p_mul(q_factor, poly(-1, 0, 1), guard)
    total_4 = p_mul(q_factor, poly(-1, -3, 0, 2), guard)
    total_6 = p_mul(q_factor, poly(-1, -5, -9, 0, 5), guard)
    total_8 = p_mul(q_factor, poly(-1, -7, -20, -28, 0, 14), guard)

    # J_(2j)=sum_h m_1(h)*a_h^(2j).  J_6 is intentionally formal here.
    marked_0 = p_mul(q, p_pow(q_minus_one, 2, guard), guard)
    marked_2 = p_mul(
        p_mul(p_mul(q, q_minus_one, guard), q_plus_one, guard),
        poly(-2, 1),
        guard,
    )
    marked_4 = p_scale(
        p_mul(
            p_mul(p_mul(q, q_minus_one, guard), q_plus_one, guard),
            poly(-1, -2, 1),
            guard,
        ),
        2,
        guard,
    )

    # For squarefree cubic h, G_h=1/(1+s*z+q*z^2).  Its z^8 row is
    # s^8-7*q*s^6+15*q^2*s^4-10*q^3*s^2+q^4.
    squarefree_g8 = p_sum(
        [
            total_8,
            p_scale(p_mul(q, total_6, guard), -7, guard),
            p_scale(p_mul(p_pow(q, 2, guard), total_4, guard), 15, guard),
            p_scale(p_mul(p_pow(q, 3, guard), total_2, guard), -10, guard),
            p_mul(p_pow(q, 4, guard), total_0, guard),
        ],
        guard,
    )
    _assert_poly(squarefree_g8, p_scale(q_factor, -1, guard), "squarefree g8")

    def n_moment(total: Poly, marked: Poly) -> Poly:
        return p_sub(p_mul(q, total, guard), marked, guard)

    n0 = n_moment(total_0, marked_0)

    # lambda_8 = -sum_(m=1)^8 p_m*g_(8-m), with p_even=N=q-m_1
    # and p_odd=s.  Its J_6 coefficient is +1; this row stores the Tate
    # part only, leaving J_6 as the single formal residual.
    squarefree_lambda8_tate = p_sum(
        [
            total_8,
            p_mul(poly(1, -7), total_6, guard),
            p_mul(poly(1, -5, 15), total_4, guard),
            marked_4,
            p_scale(p_mul(q, marked_4, guard), -5, guard),
            p_mul(poly(1, -3, 6, -10), total_2, guard),
            p_mul(poly(1, -3, 6), marked_2, guard),
            p_mul(poly(-1, 1, -1, 1), n0, guard),
        ],
        guard,
    )
    expected_squarefree_lambda_tate = p_scale(
        p_mul(q_factor, poly(9, -11, -18, -5, 5), guard),
        -1,
        guard,
    )
    _assert_poly(
        squarefree_lambda8_tate,
        expected_squarefree_lambda_tate,
        "squarefree lambda8 Tate row",
    )

    # Repeated cubic moduli: h=L^3 and h=L^2*M.
    repeated_g8 = q_factor
    repeated_lambda_l3 = p_scale(q_factor, -1, guard)
    repeated_lambda_l2m = p_mul(q_factor, poly(12, -4), guard)
    all_cubic_g8 = p_add(squarefree_g8, repeated_g8, guard)
    all_cubic_lambda8_tate = p_sum(
        [
            squarefree_lambda8_tate,
            repeated_lambda_l3,
            repeated_lambda_l2m,
        ],
        guard,
    )
    _assert_poly(all_cubic_g8, poly(0), "all cubic g8")
    expected_all_cubic_lambda_tate = p_scale(
        p_mul(q_factor, poly(-2, -7, -18, -5, 5), guard),
        -1,
        guard,
    )
    _assert_poly(
        all_cubic_lambda8_tate,
        expected_all_cubic_lambda_tate,
        "all cubic lambda8 Tate row",
    )

    # Degree-one modulus row.  For n=8 the two-linear marked coefficient is
    # (q-1)(3q-10)/2 and the quadratic-marked coefficient is -q(q-1)/2.
    linear_lambda8 = p_scale(q_minus_one, -1, guard)
    linear_choose2_lambda8 = p_scale(
        p_mul(q_minus_one, poly(-10, 3), guard), Fraction(1, 2), guard
    )
    linear_kappa8 = p_scale(p_mul(q, q_minus_one, guard), Fraction(-1, 2), guard)
    linear_weighted = p_sum(
        [
            linear_choose2_lambda8,
            linear_kappa8,
            p_scale(p_mul(q_minus_one, linear_lambda8, guard), -1, guard),
        ],
        guard,
    )
    _assert_poly(
        linear_weighted,
        p_scale(p_mul(q_minus_one, q_minus_three, guard), 2, guard),
        "linear weighted row",
    )
    all_linear_weighted = p_mul(q, linear_weighted, guard)

    # The C5 functional-equation row is q(q-1)G1-qG2.  G1=G2=0:
    # squarefree quadratics contribute q(q-1), while h=L^2 contributes
    # q(1-q).  The C3 row is -q*G3+lambda3, and G3=0.
    degree_2_squarefree_g8 = q_factor
    degree_2_repeated_g8 = p_scale(q_factor, -1, guard)
    degree_2_g8 = p_add(degree_2_squarefree_g8, degree_2_repeated_g8, guard)
    _assert_poly(degree_2_g8, poly(0), "degree-two C5 row")

    reciprocal_reduction_tate = p_add(
        all_cubic_lambda8_tate, all_linear_weighted, guard
    )
    expected_reduction = p_scale(
        p_mul(q_factor, poly(4, -9, -18, -5, 5), guard), -1, guard
    )
    _assert_poly(
        reciprocal_reduction_tate,
        expected_reduction,
        "reciprocal reduction to J6",
    )

    # Eichler--Shimura on Y0(2): stack Sym6 trace is -Theta_(8,2)-2.
    # After a^6=P6+5qP4+9q^2P2+5q^3, this gives J6 below.
    j6_tate = p_mul(q_factor, poly(-2, -10, -18, -5, 5), guard)
    j6_theta_coefficient = p_scale(q_factor, -1, guard)
    reciprocal_total_tate = p_add(j6_tate, reciprocal_reduction_tate, guard)
    reciprocal_total_theta_coefficient = j6_theta_coefficient
    expected_total_tate = p_scale(p_mul(q_factor, poly(6, 1), guard), -1, guard)
    expected_theta_coefficient = p_scale(q_factor, -1, guard)
    _assert_poly(reciprocal_total_tate, expected_total_tate, "final Tate row")
    _assert_poly(
        reciprocal_total_theta_coefficient,
        expected_theta_coefficient,
        "final Theta row",
    )

    return {
        "total_0": total_0,
        "total_2": total_2,
        "total_4": total_4,
        "total_6": total_6,
        "total_8": total_8,
        "marked_0": marked_0,
        "marked_2": marked_2,
        "marked_4": marked_4,
        "squarefree_g8": squarefree_g8,
        "squarefree_lambda8_tate": squarefree_lambda8_tate,
        "repeated_g8": repeated_g8,
        "repeated_lambda_l3": repeated_lambda_l3,
        "repeated_lambda_l2m": repeated_lambda_l2m,
        "all_cubic_g8": all_cubic_g8,
        "all_cubic_lambda8_tate": all_cubic_lambda8_tate,
        "degree_2_squarefree_g8": degree_2_squarefree_g8,
        "degree_2_repeated_g8": degree_2_repeated_g8,
        "degree_2_g8": degree_2_g8,
        "linear_lambda8": linear_lambda8,
        "linear_choose2_lambda8": linear_choose2_lambda8,
        "linear_kappa8": linear_kappa8,
        "linear_weighted": linear_weighted,
        "all_linear_weighted": all_linear_weighted,
        "reciprocal_reduction_tate": reciprocal_reduction_tate,
        "j6_tate": j6_tate,
        "j6_theta_coefficient": j6_theta_coefficient,
        "reciprocal_total_tate": reciprocal_total_tate,
        "reciprocal_total_theta_coefficient": reciprocal_total_theta_coefficient,
    }


def eta_product_coefficients(max_degree: int, guard: ResourceGuard) -> list[int]:
    """Return c_0..c_max for eta(z)^8*eta(2z)^8=sum c_n Q^n."""

    if max_degree < 1 or max_degree > MAX_ETA_FOURIER_DEGREE:
        raise ValueError("eta expansion request outside the certified cap")
    # Remove the leading Q: multiply prod(1-Q^n)^8(1-Q^(2n))^8 only
    # through degree max_degree-1.
    truncation = max_degree - 1
    product = [1] + [0] * truncation
    for n in range(1, truncation + 1):
        for step in (n, 2 * n):
            if step > truncation:
                continue
            for _ in range(8):
                for degree in range(truncation, step - 1, -1):
                    product[degree] -= product[degree - step]
                    guard.operation()
    return [0, *product]


def theta_prime_power_from_fourier(
    prime: int, exponent: int, coefficients: list[int]
) -> int:
    """Use Theta(p^r)=c_(p^r)-p^7*c_(p^(r-2)), for r>=1."""

    if prime < 2 or exponent < 1:
        raise ValueError("prime and exponent must be positive")
    index = prime**exponent
    if index >= len(coefficients):
        raise ValueError("Fourier coefficient is outside the supplied expansion")
    previous = 0 if exponent < 2 else coefficients[prime ** (exponent - 2)]
    return coefficients[index] - prime**7 * previous


def reciprocal_coefficient_8(a_coefficient: int, b_coefficient: int, q: int) -> int:
    values = [1]
    for degree in range(1, 9):
        value = -a_coefficient * values[degree - 1]
        if degree >= 2:
            value -= b_coefficient * values[degree - 2]
        if degree >= 3:
            value -= q * a_coefficient * values[degree - 3]
        if degree >= 4:
            value -= q * q * values[degree - 4]
        values.append(value)
    return values[8]


def _held_out_controls(
    native: dict[str, object],
    balanced: dict[str, object],
    coefficients: list[int],
    guard: ResourceGuard,
) -> list[dict[str, object]]:
    panels = native.get("exact_finite_panels")
    if not isinstance(panels, list):
        raise TypeError("native spectroscopy panels missing")
    observed: dict[int, int] = {}
    for panel in panels:
        if not isinstance(panel, dict):
            raise TypeError("invalid native spectroscopy panel")
        q_value = panel.get("q")
        traces = panel.get("marked_symmetric_power_trace_values")
        if q_value in (3, 5, 7) and isinstance(traces, dict):
            trace = traces.get("T_(8,0)")
            if not isinstance(trace, int):
                raise TypeError("native T_(8,0) control missing")
            observed[q_value] = trace
    if set(observed) != {3, 5, 7}:
        raise ValueError("held-out native fields changed")
    guard.atoms(3)

    frozen = balanced.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("balanced control fixture lacks frozen facts")
    families = frozen.get("families")
    if not isinstance(families, list):
        raise TypeError("balanced control fixture lacks families")
    raw_sums: dict[int, tuple[int, int, int]] = {}
    for family in families:
        if not isinstance(family, dict):
            raise TypeError("invalid balanced family row")
        q_value = family.get("q")
        member_count = family.get("member_count")
        law = family.get("joint_a_D_b_D_law")
        if q_value not in (3, 5, 7) or not isinstance(member_count, int):
            raise ValueError("unexpected balanced held-out field")
        if not isinstance(law, dict) or not isinstance(law.get("atoms"), list):
            raise TypeError("balanced held-out joint law missing")
        atoms = law["atoms"]
        guard.atoms(len(atoms))
        raw_sum = 0
        counted = 0
        for atom in atoms:
            if not isinstance(atom, dict):
                raise TypeError("invalid balanced coefficient atom")
            a_value = atom.get("a_D")
            b_value = atom.get("b_D")
            count = atom.get("member_count")
            if not all(isinstance(value, int) for value in (a_value, b_value, count)):
                raise TypeError("nonintegral balanced coefficient atom")
            raw_sum += count * reciprocal_coefficient_8(a_value, b_value, q_value)
            counted += count
        if counted != member_count:
            raise ArithmeticError("balanced held-out family mass changed")
        raw_sums[q_value] = (raw_sum, len(atoms), member_count)
    if set(raw_sums) != {3, 5, 7}:
        raise ValueError("balanced held-out fields changed")

    rows: list[dict[str, object]] = []
    for q_value in (3, 5, 7):
        theta = theta_prime_power_from_fourier(q_value, 1, coefficients)
        predicted = -theta - q_value - 6
        if predicted != observed[q_value]:
            raise ArithmeticError(f"held-out q={q_value} control failed")
        raw_sum, atom_count, member_count = raw_sums[q_value]
        theorem_sum = q_value * (q_value - 1) * predicted
        if raw_sum != theorem_sum:
            raise ArithmeticError(f"held-out q={q_value} raw sum failed")
        rows.append(
            {
                "q": q_value,
                "eta_product_coefficient": theta,
                "joint_law_atoms": atom_count,
                "family_members": member_count,
                "observed_sum_r_D_8": raw_sum,
                "theorem_sum_r_D_8": theorem_sum,
                "observed_T_(8,0)": observed[q_value],
                "theorem_value": predicted,
                "difference": observed[q_value] - predicted,
                "status": "HELD_OUT_FALSIFICATION_CONTROL_ONLY",
            }
        )
    return rows


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        B4_JSON_PATH,
        B4_NOTE_PATH,
        GENUS1_JSON_PATH,
        GENUS1_NOTE_PATH,
        ADAPTER_JSON_PATH,
        ADAPTER_NOTE_PATH,
        NATIVE_JSON_PATH,
        NATIVE_NOTE_PATH,
        BALANCED_JSON_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    return [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_sha256(path),
        }
        for path in paths
    ]


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    theorem_sources = _load_sources(THEOREM_SOURCE_NAMES)
    _validate_source_semantics(theorem_sources)
    guard = ResourceGuard()
    recurrence_certificate = _euler_recurrence_certificate(guard)
    theorem = _symbolic_theorem(guard)
    symbolic_before_eta = guard.symbolic_operations
    eta_coefficients = eta_product_coefficients(MAX_ETA_FOURIER_DEGREE, guard)

    expected_eta = [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043]
    if eta_coefficients != expected_eta:
        raise ArithmeticError("eta-product expansion changed")
    if eta_coefficients[9] != eta_coefficients[3] ** 2 - 3**7:
        raise ArithmeticError("good-prime Hecke recurrence failed at 3^2")

    theta_9 = theta_prime_power_from_fourier(3, 2, eta_coefficients)
    if theta_9 != -4230:
        raise ArithmeticError("Theta_(8,2)(9) convention drifted")
    t80_9 = -theta_9 - 9 - 6
    if t80_9 != 4215:
        raise ArithmeticError("q=9 theorem consequence drifted")

    held_out_sources = _load_sources(HELD_OUT_SOURCE_NAMES)
    symbolic_before_controls = guard.symbolic_operations
    controls = _held_out_controls(
        held_out_sources["native"],
        held_out_sources["balanced"],
        eta_coefficients,
        guard,
    )

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym8_marked_trace_average.v1",
        "status": "PROVED_EXACTLY_FOR_EVERY_ODD_PRIME_POWER",
        "scope": {
            "q": "every odd prime power",
            "family": "all monic squarefree quintics D in F_q[T]",
            "theorem_replay_finite_fields_enumerated": 0,
            "theorem_replay_family_members_enumerated": 0,
            "sampled_q_values_used_as_theorem_input": [],
            "numeric_approximations": 0,
        },
        "definitions": {
            "curve_numerator": "P_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4",
            "reciprocal_series": "1/P_D(u)=sum_(n>=0) r_D(n)*u^n",
            "character_identity": "r_D(8)=q^4*chi_(8,0)(U_D)",
            "family_size": "#H_5(q)=q^4*(q-1)",
            "newform": "f(z)=eta(z)^8*eta(2z)^8=sum_(n>=1)c_n*Q^n",
            "prime_power_trace": (
                "Theta_(8,2)(p^r)=c_(p^r)-p^7*c_(p^(r-2)); "
                "the second term is zero for r<2"
            ),
        },
        "theorem": {
            "reciprocal_total": ("sum_D r_D(8)=q*(q-1)*(-Theta_(8,2)(q)-q-6)"),
            "reciprocal_mean": "E_D[r_D(8)]=(-Theta_(8,2)(q)-q-6)/q^3",
            "character_mean": ("E_D[chi_(8,0)(U_D)]=(-Theta_(8,2)(q)-q-6)/q^7"),
            "marked_stack_trace": "T_(8,0)(q)=-Theta_(8,2)(q)-q-6",
            "raw_coefficient_identity": (
                "r_D(8)=a_D^8-7*a_D^6*b_D+6*q*a_D^6+15*a_D^4*b_D^2"
                "-20*q*a_D^4*b_D+q^2*a_D^4-10*a_D^2*b_D^3"
                "+12*q*a_D^2*b_D^2+9*q^2*a_D^2*b_D-6*q^3*a_D^2"
                "+b_D^4-3*q^2*b_D^2+q^4"
            ),
        },
        "mobius_euler_reduction": {
            "reciprocal_euler_coefficient": ("r_D(8)=sum_(deg f=8)mu(f)*(D/f)"),
            "squarefree_sieve": (
                "S_5(f)=C_5(f)-(q-l(f))*C_3(f)+(binom(l(f)+1,2)+k(f)-q*l(f))*C_1(f)"
            ),
            "even_conductor_functional_equation": ("C_5=q*(q-1)*C_1-q*C_2+q*(q-1)"),
            "C5_aggregate": ("q*(q-1)*G_1-q*G_2=0 because G_1=G_2=0"),
            "all_cubic_G3": "sum_(deg h=3)g_8(h)=0",
            "direct_reduction": ("sum_D r_D(8)=J_6-q*(q-1)*(5*q^4-5*q^3-18*q^2-9*q+4)"),
            "only_non_tate_residual": "J_6=sum_h m_1(h)*a_h^6",
        },
        "formal_euler_recurrence_certificate": recurrence_certificate,
        "marked_cubic_sixth_moment": {
            "model_stack_bridge": (
                "J_6=q*(q-1)*sum_[(E,T)]a_E^6/|Aut_q(E,T)|, T in E[2](F_q)-{0}"
            ),
            "Y0(2)_character_traces": {
                "P_0": "q-1",
                "P_2": "-2",
                "P_4": "-2",
                "P_6": "-Theta_(8,2)(q)-2",
            },
            "SU2_decomposition": "a^6=P_6+5*q*P_4+9*q^2*P_2+5*q^3*P_0",
            "formula": ("J_6=q*(q-1)*(5*q^4-5*q^3-18*q^2-10*q-2-Theta_(8,2)(q))"),
            "imported_input": (
                "standard Eichler--Shimura/Grothendieck trace identity on Y_0(2)"
            ),
        },
        "eta_product_certificate": {
            "criterion": (
                "weight 8; level 2; exponent sums 24 and 24 modulo 24; "
                "trivial character; positive cusp orders"
            ),
            "dimension": (
                "M_8(Gamma_0(2)) has dimension 3 with basis "
                "E_8(z), E_8(2z), eta(z)^8*eta(2z)^8; hence S_8 is one-dimensional"
            ),
            "newspace": "S_8(SL_2(Z))=0, so the normalized cusp form is new",
            "independent_truncated_product_coefficients_c_0_through_c_9": eta_coefficients,
            "good_prime_checks": {"c_3": 12, "c_5": -210, "c_7": 1016},
            "Hecke_relation_at_9": "c_9=c_3^2-3^7=-2043",
        },
        "prime_power_consequence": {
            "q": 9,
            "c_9": eta_coefficients[9],
            "Theta_(8,2)(9)": theta_9,
            "calculation": "c_9-3^7*c_1=-2043-2187=-4230",
            "T_(8,0)(9)": t80_9,
            "status": "THEOREM_CONSEQUENCE_NOT_FIELD_ENUMERATION",
        },
        "polynomials_low_to_high": {
            name: _pairs(value) for name, value in theorem.items()
        },
        "held_out_falsification_controls": controls,
        "primary_source_ledger": [
            {
                "author": "Kai A. Behrend",
                "title": "The Lefschetz trace formula for algebraic stacks",
                "journal": "Inventiones Mathematicae 112 (1993), 127-149",
                "url": "https://personal.math.ubc.ca/~behrend/ladic.pdf",
                "audited_pdf_sha256": "7daefa84d961d59079c67b7efc3e1086b5e4294672d295694e6eff18aa733000",
                "role": "stack-weighted Grothendieck--Lefschetz trace formula, Theorem 1.0.1",
            },
            {
                "author": "A. J. Scholl",
                "title": "Motives for modular forms",
                "journal": "Inventiones Mathematicae 100 (1990), 419-430",
                "url": "https://www.dpmms.cam.ac.uk/~ajs1005/preprints/mf.pdf",
                "audited_pdf_sha256": "b3a28690b3ba4aff316ac52ea7003cca8da757bfa309b75a9aba9557a134def6",
                "role": (
                    "ell-adic Galois representation and good-prime Frobenius polynomial, "
                    "Theorem 1.2.4(i); Section 4.2 covers levels below three"
                ),
            },
            {
                "authors": (
                    "Nathan C. Ryan, Nicolas Sirolli, Jean Carlos "
                    "Villegas-Morales, and Qi-Yang Zheng"
                ),
                "title": "Explicit families of congruences for the overpartition function",
                "journal": "The Ramanujan Journal 65 (2024), 1631-1649",
                "url": "https://doi.org/10.1007/s11139-024-00953-z",
                "role": (
                    "Proposition 2.6 proves that Delta_2=eta(z)^8*eta(2z)^8 "
                    "has simple zeros at the two cusps and that multiplication by Delta_2 "
                    "identifies M_k(Gamma_0(2)) with S_(k+8)(Gamma_0(2))"
                ),
            },
            {
                "authors": "Nathan Kaplan and Ian Petrow",
                "title": "Elliptic curves over a finite field and the trace formula",
                "journal": "Proceedings of the London Mathematical Society 115 (2017), 1317-1372",
                "url": "https://arxiv.org/abs/1510.03980",
                "audited_pdf_sha256": "3dd6a2e984a7763f9d702c867ef9f90700f065e81f31fe995fa0cf2df97fb6ea",
                "role": (
                    "prime-power elliptic-curve/Chebyshev moments with prescribed torsion "
                    "and congruence-subgroup Hecke traces"
                ),
            },
            {
                "authors": "Nathan Kaplan and Ian Petrow",
                "title": (
                    "Traces of Hecke operators and refined weight enumerators of "
                    "Reed-Solomon codes"
                ),
                "journal": (
                    "Transactions of the American Mathematical Society 370 (2018), "
                    "2537-2561"
                ),
                "url": "https://arxiv.org/abs/1506.04440",
                "audited_pdf_sha256": "6a936be3e156822ac01e1f1b68c34a29fbd911552448e5300d978cfee13fdfeb",
                "role": (
                    "Theorems 8-9 give an independent all-prime-power prescribed-2-torsion "
                    "moment check; the marked combination cancels the Gamma_0(4) channel"
                ),
            },
            {
                "authors": "B. Ramakrishnan and Brundaban Sahu",
                "title": (
                    "On the number of representations of an integer by certain quadratic "
                    "forms in sixteen variables"
                ),
                "url": "https://www.niser.ac.in/~brundaban.sahu/convolution-16.pdf",
                "audited_pdf_sha256": "bfb3b23f27420cc89f531feb7381ca5663226dad429e62e9ef75bf57c189f13c",
                "role": (
                    "defines eta(z)^8*eta(2z)^8 and states that it is the unique "
                    "normalized weight-eight level-two newform; gives the M_8 basis"
                ),
            },
        ],
        "literature_firewall": {
            "BFG_status": (
                "the same curve-open answer follows from an S5 projection of BFG only "
                "after using their conjectural nonregular ambient/endoscopic formulas"
            ),
            "native_proof_status": (
                "the Möbius/Euler reduction here is independent of that conjectural ambient formula"
            ),
            "novelty_status": (
                "no global novelty claim; relative to the audited sources the exact marked all-q formula was not printed"
            ),
        },
        "firewalls": [
            "This is an exact family average and marked-stack trace, not a memberwise sign theorem.",
            "The proof makes no RH, GRH, motive, compatible-system, or Euler-product transfer claim.",
            "The q=3,5,7 values are held-out controls and do not enter the symbolic theorem.",
            "The theorem is not inferred from three-field interpolation.",
            "The q=9 value is derived from the good-prime Hecke recurrence and is not enumerated.",
        ],
        "resource_contract": {
            "maximum_symbolic_operations_and_input_atoms": MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS,
            "actual_symbolic_operations_before_eta_expansion": symbolic_before_eta,
            "actual_symbolic_operations_before_controls": symbolic_before_controls,
            "actual_symbolic_operations": guard.symbolic_operations,
            "actual_held_out_input_atoms": guard.input_atoms,
            "actual_operations_and_input_atoms": guard.symbolic_operations
            + guard.input_atoms,
            "maximum_eta_fourier_degree": MAX_ETA_FOURIER_DEGREE,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact Fraction/integer polynomial and truncated-product algebra",
        },
        "source_manifest": _source_manifest(),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    if time.perf_counter() - started > MAX_WALL_SECONDS:
        raise RuntimeError("Sym8 marked-trace replay exceeded wall cap")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the canonical JSON")
    parser.add_argument("--check", action="store_true", help="check the canonical JSON")
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
    print(f"OK: exact Sym8 marked-trace fixture matches {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
