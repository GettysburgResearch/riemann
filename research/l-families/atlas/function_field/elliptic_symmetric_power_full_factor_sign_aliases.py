"""Exact fixed-q collisions of complete elliptic symmetric-power factors.

For ``1-t*T+q*T^2=(1-alpha*T)(1-beta*T)`` with ``q != 0``, this
packet first classifies equality for arbitrary rational traces and then gives
the sharper root-ratio theorem for the sign pair ``t,-t``.

The proof is a root-multiset argument with multiplicities.  The finite
regressions below use exact rational arithmetic, replay two locked packets,
and perform no field, curve, or trace-range enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_symmetric_power_full_factor_sign_aliases.json"
NOTE_PATH = HERE / "ELLIPTIC_SYMMETRIC_POWER_FULL_FACTOR_SIGN_ALIASES.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_symmetric_power_full_factor_sign_aliases.py"

TRACE_SOURCE_PATH = HERE / "elliptic_symmetric_power_trace_aliasing.json"
SYM5_SOURCE_PATH = HERE / "elliptic_sym5_coefficient_recovery.json"

SCHEMA = "riemann.function_field.elliptic_symmetric_power_full_factor_collisions.v1"
EXPECTED_TRACE_SOURCE_SCHEMA = (
    "riemann.function_field.elliptic_symmetric_power_trace_aliasing.v1"
)
EXPECTED_TRACE_SOURCE_PAYLOAD_SHA256 = (
    "046f76f43a2af3ac296f5c18c258e61f138e122bee38ec618af489e7e3a9e50e"
)
EXPECTED_TRACE_SOURCE_FILE_SHA256_LF = (
    "7a6e249fd696f9526154375f60bd97c2c40d251791f08eec6ecdc70b3177b941"
)
EXPECTED_SYM5_SOURCE_SCHEMA = (
    "riemann.function_field.elliptic_sym5_coefficient_recovery.v1"
)
EXPECTED_SYM5_SOURCE_PAYLOAD_SHA256 = (
    "f7b1a484d2a8b3cc0b997dbf0f15a69893f279a32bc550b71f28b21a5a9d7467"
)
EXPECTED_SYM5_SOURCE_FILE_SHA256_LF = (
    "649f682c0355a71eab618cd4fbd0507e96643b1fefacdd37e1eb9cd82dd36515"
)

MAX_REGRESSION_M = 36
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 5_000

Rational = int | Fraction
Polynomial = tuple[int, ...]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _as_fraction(name: str, value: Rational) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be an integer or Fraction")
    return Fraction(value)


def _json_rational(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return f"{value.numerator}/{value.denominator}"


class ResourceGuard:
    """Exclusive-cap ledger for the packet's small exact operations."""

    def __init__(self, cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        _require_integer("cap", cap)
        if cap <= 0:
            raise ValueError("cap must be positive")
        self.cap = cap
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        _require_integer("units", units)
        if units < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + units >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += units


def e_trace(order: int, t: Rational, q: Rational) -> Fraction:
    """Return sum(alpha^(order-j)*beta^j, j=0..order)."""

    _require_integer("order", order)
    if order < 0:
        raise ValueError("order must be nonnegative")
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    if order == 0:
        return Fraction(1)
    previous_previous, previous = Fraction(1), t_fraction
    for _ in range(2, order + 1):
        previous_previous, previous = (
            previous,
            t_fraction * previous - q_fraction * previous_previous,
        )
    return previous


def base_root_power_sum(order: int, t: Rational, q: Rational) -> Fraction:
    """Return alpha^order+beta^order from alpha+beta=t and alpha*beta=q."""

    _require_integer("order", order)
    if order < 0:
        raise ValueError("order must be nonnegative")
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    if order == 0:
        return Fraction(2)
    previous_previous, previous = Fraction(2), t_fraction
    for _ in range(2, order + 1):
        previous_previous, previous = (
            previous,
            t_fraction * previous - q_fraction * previous_previous,
        )
    return previous


def sym_power_local_factor(
    m: int,
    t: Rational,
    q: Rational,
    *,
    guard: ResourceGuard | None = None,
) -> tuple[Fraction, ...]:
    """Newton reconstruction of det(1-Sym^m(Frob)*T)."""

    _require_integer("m", m)
    if m < 0:
        raise ValueError("m must be nonnegative")
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    power_sums = [Fraction(0)] + [
        e_trace(
            m,
            base_root_power_sum(order, t_fraction, q_fraction),
            q_fraction**order,
        )
        for order in range(1, m + 2)
    ]
    coefficients = [Fraction(1)]
    for degree in range(1, m + 2):
        numerator = -sum(
            coefficients[degree - order] * power_sums[order]
            for order in range(1, degree + 1)
        )
        coefficient = numerator / degree
        coefficients.append(coefficient)
        if guard is not None:
            guard.charge("newton_coefficients_reconstructed")
    return tuple(coefficients)


def rational_root_ratio_order(t: Rational, q: Rational) -> int | None:
    """Exact root-of-unity order forced by rational t^2/q, if any."""

    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    square_ratio = t_fraction * t_fraction / q_fraction
    # r+r^(-1)=t^2/q-2.  These are exactly the rational cyclotomic cases.
    return {
        Fraction(0): 2,
        Fraction(1): 3,
        Fraction(2): 4,
        Fraction(3): 6,
        Fraction(4): 1,
    }.get(square_ratio)


def rational_sign_alias_prediction(m: int, t: Rational, q: Rational) -> bool:
    """Predict P_m(t,q)=P_m(-t,q) over Q from the exact theorem."""

    _require_integer("m", m)
    if m < 0:
        raise ValueError("m must be nonnegative")
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    if m % 2 == 0:
        return True
    order = rational_root_ratio_order(t, q_fraction)
    return order is not None and order % 2 == 0 and (m + 1) % order == 0


def rational_full_factor_collision_prediction(
    m: int, x: Rational, y: Rational, q: Rational
) -> bool:
    """Predict fixed-q equality for arbitrary rational traces, m>=1."""

    _require_integer("m", m)
    if m < 1:
        raise ValueError("full collision theorem requires m>=1")
    x_fraction = _as_fraction("x", x)
    y_fraction = _as_fraction("y", y)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    if x_fraction * x_fraction != y_fraction * y_fraction:
        return False
    if x_fraction == y_fraction:
        return True
    return rational_sign_alias_prediction(m, x_fraction, q_fraction)


def complete_cycle_alias_factor(
    m: int, q: Rational, even_order: int
) -> tuple[Fraction, ...]:
    """Closed factor when an even root-ratio order divides m+1 (m odd)."""

    _require_integer("m", m)
    _require_integer("even_order", even_order)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    if m < 1 or m % 2 == 0:
        raise ValueError("complete-cycle formula requires positive odd m")
    if even_order <= 0 or even_order % 2:
        raise ValueError("even_order must be a positive even integer")
    if (m + 1) % even_order:
        raise ValueError("even_order must divide m+1")
    repetitions = (m + 1) // even_order
    cycle_term = q_fraction ** (m * even_order // 2)
    coefficients = [Fraction(0)] * (m + 2)
    for power in range(repetitions + 1):
        coefficients[power * even_order] = (
            math.comb(repetitions, power) * cycle_term**power
        )
    return tuple(coefficients)


def consecutive_residue_counts(length: int, modulus: int) -> tuple[int, ...]:
    """Multiplicities of residues of 0,1,...,length-1 modulo modulus."""

    _require_integer("length", length)
    _require_integer("modulus", modulus)
    if length <= 0:
        raise ValueError("length must be positive")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    quotient, remainder = divmod(length, modulus)
    return tuple(
        quotient + (1 if residue < remainder else 0)
        for residue in range(modulus)
    )


def _shift_counts(counts: Sequence[int], shift: int) -> tuple[int, ...]:
    modulus = len(counts)
    if modulus == 0:
        raise ValueError("counts must be nonempty")
    return tuple(counts[(residue - shift) % modulus] for residue in range(modulus))


def consecutive_residue_shift_certificate(
    length: int, even_order: int
) -> dict[str, object]:
    """Certify half-period invariance iff even_order divides length."""

    _require_integer("even_order", even_order)
    if even_order <= 0 or even_order % 2:
        raise ValueError("even_order must be a positive even integer")
    counts = consecutive_residue_counts(length, even_order)
    half = even_order // 2
    shifted = _shift_counts(counts, half)
    quotient, remainder = divmod(length, even_order)
    invariant = counts == shifted
    predicted = remainder == 0
    if invariant != predicted:
        raise ArithmeticError("consecutive-residue lemma failed")

    witness: dict[str, int] | None = None
    if remainder:
        if remainder <= half:
            inside, outside = 0, half
        else:
            inside, outside = remainder - half, remainder
        if not (inside < remainder <= outside):
            raise ArithmeticError("residue contradiction witness is malformed")
        if (inside + half) % even_order != outside:
            raise ArithmeticError("residue contradiction does not use half-shift")
        if counts[inside] != quotient + 1 or counts[outside] != quotient:
            raise ArithmeticError("residue contradiction lost multiplicities")
        witness = {
            "inside_residue": inside,
            "half_shifted_outside_residue": outside,
            "inside_multiplicity": counts[inside],
            "outside_multiplicity": counts[outside],
        }
    return {
        "length": length,
        "even_order": even_order,
        "half_shift": half,
        "quotient": quotient,
        "remainder": remainder,
        "counts": list(counts),
        "half_shifted_counts": list(shifted),
        "invariant": invariant,
        "order_divides_length": predicted,
        "contradiction_witness": witness,
    }


def _trim_polynomial(polynomial: Sequence[int]) -> Polynomial:
    values = list(polynomial)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    product = [0] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product[left_degree + right_degree] += (
                left_coefficient * right_coefficient
            )
    return _trim_polynomial(product)


def _divide_monic_exact(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
    """Exact Z[x] division by a monic polynomial, coefficients low first."""

    dividend = _trim_polynomial(dividend)
    divisor = _trim_polynomial(divisor)
    if divisor == (0,):
        raise ValueError("polynomial divisor must be nonzero")
    if divisor[-1] != 1:
        raise ValueError("polynomial divisor must be monic")
    if len(dividend) < len(divisor):
        raise ArithmeticError("polynomial division is not exact")
    remainder = list(dividend)
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    for degree in range(len(dividend) - 1, len(divisor) - 2, -1):
        coefficient = remainder[degree]
        quotient_degree = degree - len(divisor) + 1
        quotient[quotient_degree] = coefficient
        for divisor_degree, divisor_coefficient in enumerate(divisor):
            remainder[quotient_degree + divisor_degree] -= (
                coefficient * divisor_coefficient
            )
    if any(remainder):
        raise ArithmeticError("polynomial division left a nonzero remainder")
    return _trim_polynomial(quotient)


def _divisors(value: int) -> list[int]:
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def cyclotomic_polynomials(max_order: int) -> dict[int, Polynomial]:
    """Generate Phi_n exactly from product_(d|n) Phi_d=x^n-1."""

    _require_integer("max_order", max_order)
    if max_order < 1:
        raise ValueError("max_order must be positive")
    output: dict[int, Polynomial] = {}
    for order in range(1, max_order + 1):
        polynomial: Polynomial = (-1,) + (0,) * (order - 1) + (1,)
        for divisor in _divisors(order):
            if divisor == order:
                continue
            polynomial = _divide_monic_exact(polynomial, output[divisor])
        output[order] = polynomial
    return output


def euler_phi(value: int) -> int:
    """Dependency-free Euler phi."""

    _require_integer("value", value)
    if value < 1:
        raise ValueError("value must be positive")
    remaining = value
    result = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            while remaining % prime == 0:
                remaining //= prime
            result -= result // prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


def _cyclotomic_certificate(guard: ResourceGuard) -> dict[str, object]:
    maximum = 36
    polynomials = cyclotomic_polynomials(maximum)
    for order, polynomial in polynomials.items():
        guard.charge("cyclotomic_orders_checked")
        if len(polynomial) - 1 != euler_phi(order):
            raise ArithmeticError("cyclotomic degree disagrees with Euler phi")
        product: Polynomial = (1,)
        for divisor in _divisors(order):
            product = _multiply_polynomials(product, polynomials[divisor])
        expected = (-1,) + (0,) * (order - 1) + (1,)
        if product != expected:
            raise ArithmeticError("cyclotomic divisor product failed")

    small_orders = [
        order for order in range(1, maximum + 1) if euler_phi(order) <= 2
    ]
    if small_orders != [1, 2, 3, 4, 6]:
        raise ArithmeticError("small cyclotomic degrees changed")
    expected_special = {
        1: (-1, 1),
        2: (1, 1),
        3: (1, 1, 1),
        4: (1, 0, 1),
        6: (1, -1, 1),
    }
    if {order: polynomials[order] for order in expected_special} != expected_special:
        raise ArithmeticError("special cyclotomic polynomials changed")

    ratio_quadratics = {
        1: (1, -2, 1),
        2: (1, 2, 1),
        3: (1, 1, 1),
        4: (1, 0, 1),
        6: (1, -1, 1),
    }
    if ratio_quadratics[1] != _multiply_polynomials(expected_special[1], expected_special[1]):
        raise ArithmeticError("order-one ratio quadratic failed")
    if ratio_quadratics[2] != _multiply_polynomials(expected_special[2], expected_special[2]):
        raise ArithmeticError("order-two ratio quadratic failed")
    for order in (3, 4, 6):
        if ratio_quadratics[order] != expected_special[order]:
            raise ArithmeticError("ratio quadratic lost its cyclotomic factor")

    return {
        "identity": "product_(d|n) Phi_d(X)=X^n-1",
        "coefficient_convention": "low degree to high degree",
        "exact_generation_checked_through_order": maximum,
        "all_degrees_equal_Euler_phi": True,
        "orders_with_phi_at_most_2_in_checked_range": small_orders,
        "global_phi_at_most_2_proof": {
            "prime_exclusion": (
                "a prime p>=5 dividing n forces p-1 to divide phi(n), so phi(n)>=4"
            ),
            "remaining_shape": "n=2^a*3^b",
            "pure_2_power": "phi(2^a)=2^(a-1), giving n=1,2,4",
            "pure_3_power": "phi(3^b)=2*3^(b-1), giving n=3",
            "mixed": "phi(2^a*3^b)=2^a*3^(b-1), giving n=6",
            "conclusion": "phi(n)<=2 iff n is one of 1,2,3,4,6",
        },
        "special_polynomials": {
            str(order): list(expected_special[order]) for order in expected_special
        },
        "square_ratio_t2_over_q_by_order": {
            "1": 4,
            "2": 0,
            "3": 1,
            "4": 2,
            "6": 3,
        },
        "even_orders_surviving": [2, 4, 6],
    }


def _load_locked_source(
    path: Path,
    expected_schema: str,
    expected_payload: str,
    expected_lf_hash: str,
) -> dict[str, object]:
    if _lf_sha256(path) != expected_lf_hash:
        raise RuntimeError(f"locked source LF hash mismatch: {_relative(path)}")
    source = json.loads(path.read_text(encoding="utf-8"))
    if source.get("schema") != expected_schema:
        raise RuntimeError(f"locked source schema mismatch: {_relative(path)}")
    if source.get("payload_sha256") != expected_payload:
        raise RuntimeError(f"locked source payload mismatch: {_relative(path)}")
    unhashed = dict(source)
    payload_hash = unhashed.pop("payload_sha256", None)
    if payload_hash != _canonical_sha256(unhashed):
        raise RuntimeError(f"locked source payload is inconsistent: {_relative(path)}")
    return source


def _source_replay(
    trace_source: Mapping[str, object],
    sym5_source: Mapping[str, object],
    guard: ResourceGuard,
) -> dict[str, object]:
    diagnostics = trace_source.get("full_factor_diagnostics")
    if not isinstance(diagnostics, dict):
        raise RuntimeError("trace source lost full-factor diagnostics")
    nuance = diagnostics.get("sign_nuance")
    if nuance != {
        "even_m": "t and -t always give the same full Sym^m factor",
        "odd_m_5_mod_6_at_t_squared_3q": (
            "the normalized spectrum is a union of complete six-cycles and is "
            "invariant under negation, so the t and -t full factors coincide"
        ),
    }:
        raise RuntimeError("trace source sign nuance changed")
    q3_row = diagnostics.get("q_3_m_5")
    if not isinstance(q3_row, dict):
        raise RuntimeError("trace source lost q=3,m=5 row")
    trace_replay: dict[str, list[int]] = {}
    for t, source_key in (
        (-3, "t_minus_3_full_factor"),
        (0, "t_0_full_factor"),
        (3, "t_3_full_factor"),
    ):
        factor = sym_power_local_factor(5, t, 3, guard=guard)
        integral_factor = [int(value) for value in factor]
        if any(value.denominator != 1 for value in factor):
            raise ArithmeticError("integral source replay produced a fraction")
        if integral_factor != q3_row.get(source_key):
            raise ArithmeticError("trace source q=3,m=5 factor failed replay")
        trace_replay[str(t)] = integral_factor

    recovery = sym5_source.get("exact_recovery_theorem_over_Q")
    if not isinstance(recovery, dict):
        raise RuntimeError("Sym^5 source lost recovery theorem")
    if recovery.get("full_factor_equal_iff") != (
        "x=y, or x=-y and x^2=3*q"
    ):
        raise RuntimeError("Sym^5 source full-factor theorem changed")
    locked_replay = sym5_source.get("locked_collision_replay")
    if not isinstance(locked_replay, dict):
        raise RuntimeError("Sym^5 source lost collision replay")
    aliases = locked_replay.get("full_factor_aliases")
    expected_aliases = [
        {"q": 3, "x": -3, "y": 3},
        {"q": 27, "x": -9, "y": 9},
        {"q": 243, "x": -27, "y": 27},
    ]
    if aliases != expected_aliases:
        raise RuntimeError("Sym^5 locked sign aliases changed")
    replayed_aliases: list[dict[str, int]] = []
    for row in expected_aliases:
        left = sym_power_local_factor(5, row["x"], row["q"], guard=guard)
        right = sym_power_local_factor(5, row["y"], row["q"], guard=guard)
        if left != right:
            raise ArithmeticError("locked Sym^5 sign alias failed replay")
        if row["x"] * row["x"] != 3 * row["q"]:
            raise ArithmeticError("locked Sym^5 alias left the order-six locus")
        replayed_aliases.append(dict(row))
    return {
        "trace_packet_q3_m5_factors": trace_replay,
        "sym5_packet_full_factor_aliases": replayed_aliases,
        "source_claims_replayed": 2,
        "new_curve_field_or_trace_range_enumerations": 0,
    }


def _bounded_residue_regression(max_m: int, guard: ResourceGuard) -> dict[str, object]:
    projection: list[dict[str, object]] = []
    for m in range(1, max_m + 1, 2):
        # If -1 occurs among 1,r,...,r^m, exact order n obeys n/2<=m.
        for even_order in range(2, 2 * m + 1, 2):
            certificate = consecutive_residue_shift_certificate(m + 1, even_order)
            guard.charge("bounded_residue_lemma_cases")
            projection.append(
                {
                    "m": m,
                    "even_order": even_order,
                    "remainder": certificate["remainder"],
                    "invariant": certificate["invariant"],
                    "witness": certificate["contradiction_witness"],
                }
            )
    return {
        "maximum_m": max_m,
        "odd_m_values_checked": (max_m + 1) // 2,
        "order_bound_reason": "-1=r^(n/2) occurs by exponent m, so n<=2m",
        "cases_checked": len(projection),
        "failures": 0,
        "projection_sha256": _canonical_sha256(projection),
    }


def _bounded_factor_regression(max_m: int, guard: ResourceGuard) -> dict[str, object]:
    cases = {
        "generic": (Fraction(1), Fraction(3)),
        "order_2_t_zero": (Fraction(0), Fraction(3)),
        "order_4_t2_eq_2q": (Fraction(2), Fraction(2)),
        "order_6_t2_eq_3q": (Fraction(3), Fraction(3)),
    }
    rows: list[dict[str, object]] = []
    comparisons = 0
    for m in range(1, max_m + 1):
        labels = ["generic"] if m % 2 == 0 else list(cases)
        aliases: list[str] = []
        for label in labels:
            t, q = cases[label]
            left = sym_power_local_factor(m, t, q, guard=guard)
            right = sym_power_local_factor(m, -t, q, guard=guard)
            actual = left == right
            predicted = rational_sign_alias_prediction(m, t, q)
            if actual != predicted:
                raise ArithmeticError("bounded full-factor regression failed")
            for degree, (left_coefficient, right_coefficient) in enumerate(
                zip(left, right)
            ):
                expected_right = ((-1) ** (m * degree)) * left_coefficient
                if right_coefficient != expected_right:
                    raise ArithmeticError("coefficient sign law failed")
            if actual:
                aliases.append(label)
            if actual and m % 2:
                order = rational_root_ratio_order(t, q)
                if order not in (2, 4, 6):
                    raise ArithmeticError("rational sign alias lost its even order")
                if left != complete_cycle_alias_factor(m, q, order):
                    raise ArithmeticError("complete-cycle closed factor failed")
            comparisons += 1
        rows.append(
            {
                "m": m,
                "tested_cases": labels,
                "alias_cases": aliases,
            }
        )
    return {
        "maximum_m": max_m,
        "exact_factor_comparisons": comparisons,
        "rows": rows,
        "arithmetic": "fractions.Fraction only",
    }


def _negative_controls(guard: ResourceGuard) -> dict[str, object]:
    rows = [
        {
            "label": "odd_order_3_even_though_3_divides_m_plus_1",
            "m": 5,
            "t": 3,
            "q": 9,
            "root_ratio_order": 3,
        },
        {
            "label": "odd_order_1_Hasse_endpoint",
            "m": 5,
            "t": 6,
            "q": 9,
            "root_ratio_order": 1,
        },
    ]
    for m in (1, 3, 7, 9):
        rows.append(
            {
                "label": "order_6_but_6_does_not_divide_m_plus_1",
                "m": m,
                "t": 3,
                "q": 3,
                "root_ratio_order": 6,
            }
        )
    projection: list[dict[str, object]] = []
    for row in rows:
        m, t, q = int(row["m"]), int(row["t"]), int(row["q"])
        order = rational_root_ratio_order(t, q)
        if order != row["root_ratio_order"]:
            raise ArithmeticError("negative control lost its cyclotomic order")
        left = sym_power_local_factor(m, t, q, guard=guard)
        right = sym_power_local_factor(m, -t, q, guard=guard)
        if left == right or rational_sign_alias_prediction(m, t, q):
            raise ArithmeticError("negative control unexpectedly aliased")
        projection.append(dict(row))
    return {
        "rows": projection,
        "all_factors_distinct_from_their_sign_partners": True,
    }


def _bounded_rational_collision_regression(
    guard: ResourceGuard,
) -> dict[str, object]:
    maximum_m = 8
    q_values = (Fraction(1), Fraction(3))
    traces = tuple(Fraction(value) for value in range(-2, 3))
    comparisons = 0
    collisions: list[dict[str, int]] = []
    for m in range(1, maximum_m + 1):
        for q in q_values:
            factors = {
                trace: sym_power_local_factor(m, trace, q, guard=guard)
                for trace in traces
            }
            for left_index, x in enumerate(traces):
                for y in traces[left_index:]:
                    actual = factors[x] == factors[y]
                    predicted = rational_full_factor_collision_prediction(
                        m, x, y, q
                    )
                    guard.charge("bounded_arbitrary_trace_pair_comparisons")
                    if actual != predicted:
                        raise ArithmeticError(
                            "bounded arbitrary-trace collision regression failed"
                        )
                    if actual:
                        collisions.append(
                            {
                                "m": m,
                                "q": int(q),
                                "x": int(x),
                                "y": int(y),
                            }
                        )
                    comparisons += 1
    return {
        "maximum_m": maximum_m,
        "q_values": [int(value) for value in q_values],
        "integer_traces": [int(value) for value in traces],
        "factor_comparisons": comparisons,
        "collision_projection_sha256": _canonical_sha256(collisions),
        "all_actual_equalities_match_complete_Q_theorem": True,
    }


def _nonrational_trace_counterexample() -> dict[str, object]:
    modulus, m = 5, 3
    first_exponents = sorted((m - 2 * index) % modulus for index in range(m + 1))
    second_exponents = sorted(
        (2 * (m - 2 * index)) % modulus for index in range(m + 1)
    )
    expected = [1, 2, 3, 4]
    if first_exponents != expected or second_exponents != expected:
        raise ArithmeticError("primitive-fifth-root counterexample spectra changed")
    phi5 = cyclotomic_polynomials(5)[5]
    if phi5 != (1, 1, 1, 1, 1):
        raise ArithmeticError("primitive-fifth-root counterexample factor changed")
    return {
        "q": 1,
        "m": m,
        "zeta": "a primitive fifth root of unity",
        "x": "zeta+zeta^(-1)",
        "y": "zeta^2+zeta^(-2)",
        "x_and_y_minimal_polynomial": "X^2+X-1",
        "x_not_equal_plus_or_minus_y": True,
        "first_spectrum_exponents_mod_5": first_exponents,
        "second_spectrum_exponents_mod_5": second_exponents,
        "common_factor": list(phi5),
        "meaning": "the rational-trace hypothesis in the complete collision theorem is essential",
    }


def build_fixture(
    *,
    max_m: int = MAX_REGRESSION_M,
    resource_cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE,
) -> dict[str, object]:
    """Build the canonical exact theorem/certificate fixture."""

    _require_integer("max_m", max_m)
    _require_integer("resource_cap", resource_cap)
    if max_m < 1:
        raise ValueError("max_m must be positive")
    if max_m > MAX_REGRESSION_M:
        raise ValueError(f"max_m must not exceed {MAX_REGRESSION_M}")
    guard = ResourceGuard(resource_cap)

    trace_source = _load_locked_source(
        TRACE_SOURCE_PATH,
        EXPECTED_TRACE_SOURCE_SCHEMA,
        EXPECTED_TRACE_SOURCE_PAYLOAD_SHA256,
        EXPECTED_TRACE_SOURCE_FILE_SHA256_LF,
    )
    sym5_source = _load_locked_source(
        SYM5_SOURCE_PATH,
        EXPECTED_SYM5_SOURCE_SCHEMA,
        EXPECTED_SYM5_SOURCE_PAYLOAD_SHA256,
        EXPECTED_SYM5_SOURCE_FILE_SHA256_LF,
    )
    guard.charge("locked_source_payloads_loaded", 2)

    cyclotomic = _cyclotomic_certificate(guard)
    residue_regression = _bounded_residue_regression(max_m, guard)
    factor_regression = _bounded_factor_regression(max_m, guard)
    source_replay = _source_replay(trace_source, sym5_source, guard)
    negative_controls = _negative_controls(guard)
    arbitrary_collision_regression = _bounded_rational_collision_regression(guard)
    nonrational_counterexample = _nonrational_trace_counterexample()

    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "normalization": {
            "base_factor": "1-t*T+q*T^2=(1-alpha*T)*(1-beta*T)",
            "relations": "alpha+beta=t; alpha*beta=q; q nonzero",
            "root_ratio": "r=alpha/beta; swapping alpha,beta replaces r by r^(-1)",
            "sym_m_factor": (
                "P_m(t,q;T)=product_(j=0)^m "
                "(1-alpha^(m-j)*beta^j*T)"
            ),
            "domain_of_sign_theorem": "characteristic zero, m>=0, q nonzero",
            "domain_of_complete_collision_theorem": (
                "fixed q in Q nonzero; x,y in Q; m>=1"
            ),
        },
        "complete_fixed_q_rational_collision_theorem": {
            "statement": (
                "for m>=1 and x,y,q in Q with q nonzero, equality of the "
                "complete Sym^m factors first forces x^2=y^2"
            ),
            "intrinsic_quotient_group": (
                "Gamma(A)=group generated by a/a' for spectrum elements a,a'"
            ),
            "nonzero_certificate": (
                "q nonzero makes alpha,beta and every symmetric-power weight nonzero, so all quotients are defined"
            ),
            "consecutive_weight_certificate": (
                "for A_x={alpha^(m-j)beta^j}, all quotients are powers of "
                "r=alpha/beta and consecutive weights have quotient r, so Gamma(A_x)=<r>"
            ),
            "infinite_case": (
                "equal infinite cyclic groups have r_x and r_y as generators, "
                "hence r_y=r_x or r_x^(-1)"
            ),
            "finite_case": (
                "each r is a generator of the common finite cyclic group; "
                "rational traces force exact order n in {1,2,3,4,6}, whose "
                "generators are inverse pairs and have one common r+r^(-1)"
            ),
            "square_recovery": "x^2/q-2=r_x+r_x^(-1), hence x^2=y^2",
            "complete_classification": {
                "even_m": "factor equality iff x=y or x=-y",
                "odd_m": (
                    "factor equality iff x=y, or y=-x with "
                    "[x^2=2q and 4 divides m+1], or y=-x with "
                    "[x^2=3q and 6 divides m+1]"
                ),
            },
            "m_zero_exception": "Sym^0 has factor 1-T for every trace and is excluded",
            "root_multisets_include_multiplicity": True,
        },
        "exact_sign_pair_theorem": {
            "even_m": "P_m(t,q;T)=P_m(-t,q;T) for every t and q",
            "odd_m_iff": (
                "P_m(t,q;T)=P_m(-t,q;T) iff r has exact even order n "
                "dividing m+1"
            ),
            "order_two_case": "n=2 iff t=0; the sign pair then collapses",
            "proof_steps": [
                "t->-t replaces (alpha,beta) by (-alpha,-beta)",
                "the Sym^m spectrum is fixed termwise for even m and negated for odd m",
                "after division by beta^m, the odd-m condition is multiset {1,r,...,r^m}=-{1,r,...,r^m}",
                "membership of -1 forces r to have even order n and -1=r^(n/2)",
                "multiplication by -1 shifts exponent residues by n/2",
                "the consecutive-residue multiplicity lemma gives invariance iff n divides m+1",
            ],
            "multiplicity_firewall": (
                "equality is equality of root multisets with multiplicity; no "
                "squarefreeness or distinct-root assumption is used"
            ),
        },
        "consecutive_residue_multiset_lemma": {
            "statement": (
                "for even n and L>=1, multiplicities of 0,...,L-1 mod n "
                "are invariant under shift n/2 iff n divides L"
            ),
            "division": "L=a*n+s, 0<=s<n",
            "counts": "a+1 on residues 0,...,s-1 and a elsewhere",
            "s_between_1_and_n_over_2": (
                "residue 0 is heavy but its half-shift n/2 is light"
            ),
            "s_between_n_over_2_and_n_minus_1": (
                "residue s-n/2 is heavy but its half-shift s is light"
            ),
            "s_zero": "all residues have multiplicity a, so invariance holds",
            "covers_repeated_torsion_roots": True,
        },
        "rational_corollary": {
            "identity": "t^2/q=r+r^(-1)+2",
            "cyclotomic_degree_argument": (
                "if t^2/q is rational and r has order n, then Phi_n divides "
                "a quadratic over Q, hence phi(n)<=2"
            ),
            "even_orders": [2, 4, 6],
            "square_ratio_by_order": {"2": 0, "4": 2, "6": 3},
            "odd_m_full_sign_alias_iff": (
                "t=0, or [t^2=2q and 4 divides m+1], or "
                "[t^2=3q and 6 divides m+1]"
            ),
        },
        "closed_alias_factors": {
            "general_even_order_n": (
                "if m is odd and n divides m+1, then "
                "P_m=(1+q^(m*n/2)*T^n)^((m+1)/n)"
            ),
            "order_2_t_zero": "(1+q^m*T^2)^((m+1)/2)",
            "order_4_t2_eq_2q": "(1+q^(2m)*T^4)^((m+1)/4)",
            "order_6_t2_eq_3q": "(1+q^(3m)*T^6)^((m+1)/6)",
            "sign_reason": (
                "beta^(m*n)=-q^(m*n/2) because r^(n/2)=-1 and m is odd"
            ),
        },
        "odd_prime_power_integral_corollary": {
            "scope": "q=p^a with p odd prime, a>=1; t is a nonzero integer; m is odd",
            "classification": (
                "P_m(t,q)=P_m(-t,q) iff m=5 mod 6, "
                "q=3^(2k+1), and t=+/-3^(k+1)"
            ),
            "equivalent_equation": "m=5 mod 6 and t^2=3q",
            "t2_eq_2q_impossible": (
                "v_2(2q)=1 for odd q, whereas a nonzero square has even v_2"
            ),
            "t2_eq_3q_prime_power_proof": (
                "prime valuations force p=3; then a+1 is even, so a=2k+1"
            ),
            "Hasse_check": "t^2=3q<4q",
            "curve_realization_claimed": False,
        },
        "cyclotomic_certificate": cyclotomic,
        "bounded_residue_regression": residue_regression,
        "bounded_full_factor_regression": factor_regression,
        "bounded_arbitrary_trace_collision_regression": arbitrary_collision_regression,
        "negative_controls": negative_controls,
        "nonrational_trace_counterexample": nonrational_counterexample,
        "source_replay": source_replay,
        "source_locks": [
            {
                "path": _relative(TRACE_SOURCE_PATH),
                "schema": EXPECTED_TRACE_SOURCE_SCHEMA,
                "payload_sha256": EXPECTED_TRACE_SOURCE_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_TRACE_SOURCE_FILE_SHA256_LF,
                "use": "replay the prior even-m and m=5 full-factor diagnostics",
            },
            {
                "path": _relative(SYM5_SOURCE_PATH),
                "schema": EXPECTED_SYM5_SOURCE_SCHEMA,
                "payload_sha256": EXPECTED_SYM5_SOURCE_PAYLOAD_SHA256,
                "file_sha256_lf_normalized": EXPECTED_SYM5_SOURCE_FILE_SHA256_LF,
                "use": "replay the three locked Sym^5 full-factor sign aliases",
            },
        ],
        "resource_contract": {
            "accounted_work_ledger": dict(sorted(guard.ledger.items())),
            "accounted_work_units": guard.total,
            "accounted_work_unit_cap_exclusive": guard.cap,
            "maximum_regression_m": max_m,
            "new_curve_field_or_trace_range_enumerations": 0,
            "random_samples": 0,
            "symbolic_engine_dependency": False,
            "arithmetic": "exact integers and fractions.Fraction only",
        },
        "scope_firewall": {
            "complete_fixed_q_rational_full_factor_classification": True,
            "does_not_classify_arbitrary_scalar_trace_collisions": True,
            "does_not_extend_complete_classification_to_nonrational_traces": True,
            "sign_pair_root_ratio_theorem_holds_in_characteristic_zero": True,
            "local_factor_identity_not_a_global_L_function_lift": True,
            "no_curve_or_isogeny_class_realization_claim": True,
            "no_automorphy_or_modularity_claim": True,
            "no_global_compatible_family_or_euler_product_constructed": True,
            "no_literature_priority_claim": True,
            "no_RH_GRH_or_zero_distribution_consequence_claim": True,
            "bounded_regression_is_not_the_proof": (
                "the proof is the exact root-multiset and consecutive-residue argument"
            ),
        },
        "producer": {
            "script": _relative(Path(__file__).resolve()),
            "script_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail unless the stored JSON equals a fresh exact build",
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored symmetric-power sign-alias fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
