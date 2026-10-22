#!/usr/bin/env python3
"""Exact ``Std tensor Sym^3`` / ``Sym^7`` local spectral intersection.

All elliptic inputs use the geometric-trace convention

    P_t(T) = 1 - t*T + q*T^2.

The tensor factor has degree eight and weight four; the symmetric-seventh
factor has degree eight and weight seven.  After choosing ``s`` with
``s^2=q``, the typed comparison is therefore

    P_{Std(A) tensor Sym3(B)}(s^3*T) = P_{Sym7(C)}(T).

The producer uses only exact standard-library arithmetic.  Its elimination
certificate consists of explicit polynomial divisions, a two-line
ideal-membership identity, and univariate factorizations.  It performs no
runtime Groebner-basis calculation and no field, curve, or model enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_tensor_sym3_sym7_spectral_intersection.json"
NOTE_PATH = HERE / "ELLIPTIC_TENSOR_SYM3_SYM7_SPECTRAL_INTERSECTION.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_tensor_sym3_sym7_spectral_intersection.py"

GENUS1_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_PRODUCER_PATH = HERE / "genus1_cubic_family_laws.py"
FULL_FACTOR_PATH = HERE / "elliptic_symmetric_power_full_factor_sign_aliases.json"
FULL_FACTOR_PRODUCER_PATH = HERE / "elliptic_symmetric_power_full_factor_sign_aliases.py"
CYCLOTOMIC_PATH = HERE / "elliptic_symmetric_power_cyclotomic_spectral_aliases.json"
CYCLOTOMIC_PRODUCER_PATH = HERE / "elliptic_symmetric_power_cyclotomic_spectral_aliases.py"
LADDER_PATH = HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.json"
LADDER_PRODUCER_PATH = HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.py"

FROZEN_Q_VALUES = (3, 5, 7, 11, 13)
SYNTHETIC_Q_VALUES = (9, 25)
LOCKED_TRIPLE_CAP_INCLUSIVE = 7_975
SYNTHETIC_TRIPLE_CAP_INCLUSIVE = 11_458
ACCOUNTED_WORK_CAP_EXCLUSIVE = 25_000


SOURCE_LOCKS = {
    "genus1": {
        "path": GENUS1_PATH,
        "producer": GENUS1_PRODUCER_PATH,
        "schema": "riemann.function_field.genus1_cubic_family_laws.v1",
        "payload": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
        "file": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
        "producer_file": "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79",
    },
    "full_factor": {
        "path": FULL_FACTOR_PATH,
        "producer": FULL_FACTOR_PRODUCER_PATH,
        "schema": "riemann.function_field.elliptic_symmetric_power_full_factor_collisions.v1",
        "payload": "f1a7f183ee16c98c8f633e9b5ffa5f1bb76c0521cd596d5be71840a35711d983",
        "file": "5388e4e6819f2b48b08956ab810137054158424931e5e6ac1d516fc54d03c607",
        "producer_file": "b817406551fc9adc008fb6f24f9db6a1a84081cbcbd6aa3448344939bf74709a",
    },
    "cyclotomic": {
        "path": CYCLOTOMIC_PATH,
        "producer": CYCLOTOMIC_PRODUCER_PATH,
        "schema": "riemann.function_field.elliptic_symmetric_power_cyclotomic_spectral_aliases.v1",
        "payload": "b783dc120095c5256cacc2eaa79f3f152883f9b33b4074a18b123489f81bc6ff",
        "file": "4321113137615a88f43926c1e92df478160de5a00f0974c1472303de506aabdc",
        "producer_file": "7ffc5952d1e68ae2784f1ba292b54976a6d6953e3f5ea12216c1e92566a00d56",
    },
    "all_r_ladder": {
        "path": LADDER_PATH,
        "producer": LADDER_PRODUCER_PATH,
        "schema": "riemann.function_field.elliptic_tensor_sym2_sym5_spectral_intersection.v1",
        "payload": "e2c9c7ac3d1329b7b911a5214d36935d2694436cbe6d9cce551b94f8486b01ba",
        "file": "e583220e7df56765ef198d71a4a94887e8246992ba8fd9d127e8c1ce4e09cc32",
        "producer_file": "d414807d8c2bb41ee075c5526e22b243204f3e587e5988a55f91245a99f6d9e7",
    },
}


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_builtin_int(value: object, name: str) -> int:
    if type(value) is not int:
        raise TypeError(f"{name} must be a built-in integer")
    return value


def prime_power_data(q: object) -> tuple[int, int]:
    """Return ``(p,e)`` for an odd prime power and reject other inputs."""

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
    """Fail closed on all declared finite-replay budgets."""

    def __init__(
        self,
        locked_cap: int = LOCKED_TRIPLE_CAP_INCLUSIVE,
        synthetic_cap: int = SYNTHETIC_TRIPLE_CAP_INCLUSIVE,
        work_cap: int = ACCOUNTED_WORK_CAP_EXCLUSIVE,
    ) -> None:
        for value, name in (
            (locked_cap, "locked cap"),
            (synthetic_cap, "synthetic cap"),
            (work_cap, "work cap"),
        ):
            if type(value) is not int or value <= 0:
                raise ValueError(f"{name} must be a positive built-in integer")
        self.locked_cap = locked_cap
        self.synthetic_cap = synthetic_cap
        self.work_cap = work_cap
        self.locked_triples = 0
        self.synthetic_triples = 0
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

    def charge_triple(self, *, locked: bool) -> None:
        if locked:
            if self.locked_triples + 1 > self.locked_cap:
                raise RuntimeError("locked trace-triple cap exceeded")
            self.locked_triples += 1
            self.charge("locked_trace_triples")
        else:
            if self.synthetic_triples + 1 > self.synthetic_cap:
                raise RuntimeError("synthetic trace-triple cap exceeded")
            self.synthetic_triples += 1
            self.charge("synthetic_hasse_trace_triples")


def _load_authenticated_source(lock: Mapping[str, object]) -> dict[str, object]:
    path = lock.get("path")
    producer = lock.get("producer")
    if not isinstance(path, Path) or not isinstance(producer, Path):
        raise RuntimeError("internal source lock path is malformed")
    if _lf_sha256(path) != lock.get("file"):
        raise RuntimeError(f"locked source file changed: {path.name}")
    if _lf_sha256(producer) != lock.get("producer_file"):
        raise RuntimeError(f"locked source producer changed: {producer.name}")
    source = json.loads(path.read_text(encoding="utf-8"))
    if source.get("schema") != lock.get("schema"):
        raise RuntimeError(f"locked source schema changed: {path.name}")
    if source.get("payload_sha256") != lock.get("payload"):
        raise RuntimeError(f"locked source payload changed: {path.name}")
    unhashed = dict(source)
    claimed = unhashed.pop("payload_sha256", None)
    if not isinstance(claimed, str) or _canonical_sha256(unhashed) != claimed:
        raise RuntimeError(f"locked source is internally inauthentic: {path.name}")
    return source


def load_locked_sources() -> dict[str, dict[str, object]]:
    sources = {
        name: _load_authenticated_source(lock) for name, lock in SOURCE_LOCKS.items()
    }
    genus1 = sources["genus1"]
    if genus1.get("normalization", {}).get("l_polynomial") != "L_D(T)=1-a_D*T+q*T^2":
        raise RuntimeError("locked genus-one trace convention changed")
    rows = genus1.get("finite_regressions")
    if not isinstance(rows, list) or tuple(
        row.get("q") for row in rows if isinstance(row, dict)
    ) != FROZEN_Q_VALUES:
        raise RuntimeError("locked genus-one finite rows changed")

    full_factor = sources["full_factor"]
    normalization = full_factor.get("normalization", {})
    if normalization.get("base_factor") != "1-t*T+q*T^2=(1-alpha*T)*(1-beta*T)":
        raise RuntimeError("locked full-factor sign convention changed")

    cyclotomic = sources["cyclotomic"]
    orders = cyclotomic.get("orders_5_7_9_11")
    if not isinstance(orders, list) or not orders:
        raise RuntimeError("locked cyclotomic exact rows changed")

    ladder = sources["all_r_ladder"].get(
        "universal_tensor_symmetric_power_ladder", {}
    )
    if ladder.get("scope") != "every integer r>=1 on a normalized characteristic-zero torus":
        raise RuntimeError("locked all-r ladder scope changed")
    rows = ladder.get("bounded_regression", {}).get("rows")
    if not isinstance(rows, list) or len(rows) < 3 or rows[2].get("r") != 3:
        raise RuntimeError("locked all-r ladder r=3 row changed")
    return sources


def _source_lock_payload() -> dict[str, object]:
    output: dict[str, object] = {}
    for name, lock in SOURCE_LOCKS.items():
        path = lock.get("path")
        producer = lock.get("producer")
        if not isinstance(path, Path) or not isinstance(producer, Path):
            raise RuntimeError("internal source lock path is malformed")
        output[name] = {
            "fixture_path": _relative(path),
            "producer_path": _relative(producer),
            "schema": lock["schema"],
            "fixture_payload_sha256": lock["payload"],
            "fixture_sha256_lf_normalized": lock["file"],
            "producer_sha256_lf_normalized": lock["producer_file"],
        }
    return output


# Sparse exact polynomial arithmetic.  A monomial is an exponent tuple, and
# every coefficient is a Fraction.  The certificate only needs dimensions
# one, two, and three and exact division by displayed factors.
Monomial = tuple[int, ...]
Poly = dict[Monomial, Fraction]


def _poly_clean(poly: Mapping[Monomial, Fraction | int]) -> Poly:
    return {
        monomial: Fraction(coefficient)
        for monomial, coefficient in poly.items()
        if coefficient
    }


def _poly_constant(value: Fraction | int, dimension: int) -> Poly:
    if type(dimension) is not int or dimension <= 0:
        raise ValueError("polynomial dimension must be positive")
    coefficient = Fraction(value)
    return {} if not coefficient else {(0,) * dimension: coefficient}


def _poly_variable(index: int, dimension: int) -> Poly:
    if type(index) is not int or type(dimension) is not int:
        raise TypeError("polynomial indices must be built-in integers")
    if index < 0 or index >= dimension:
        raise ValueError("polynomial variable index is out of range")
    monomial = [0] * dimension
    monomial[index] = 1
    return {tuple(monomial): Fraction(1)}


def _poly_add(left: Poly, right: Poly, scale: Fraction | int = 1) -> Poly:
    output = dict(left)
    scale_q = Fraction(scale)
    for monomial, coefficient in right.items():
        output[monomial] = output.get(monomial, Fraction(0)) + scale_q * coefficient
    return _poly_clean(output)


def _poly_scale(poly: Poly, scale: Fraction | int) -> Poly:
    scale_q = Fraction(scale)
    return _poly_clean(
        {monomial: scale_q * coefficient for monomial, coefficient in poly.items()}
    )


def _poly_multiply(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return {}
    left_dimension = len(next(iter(left)))
    right_dimension = len(next(iter(right)))
    if left_dimension != right_dimension:
        raise ValueError("polynomial dimensions differ")
    output: dict[Monomial, Fraction] = defaultdict(Fraction)
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_exponent + right_exponent
                for left_exponent, right_exponent in zip(
                    left_monomial, right_monomial
                )
            )
            output[monomial] += left_coefficient * right_coefficient
    return _poly_clean(output)


def _poly_power(poly: Poly, exponent: int, dimension: int) -> Poly:
    if type(exponent) is not int or exponent < 0:
        raise ValueError("polynomial exponent must be a nonnegative integer")
    output = _poly_constant(1, dimension)
    base = dict(poly)
    power = exponent
    while power:
        if power & 1:
            output = _poly_multiply(output, base)
        power //= 2
        if power:
            base = _poly_multiply(base, base)
    return output


def _poly_sum(dimension: int, *terms: tuple[Fraction | int, Poly]) -> Poly:
    output = _poly_constant(0, dimension)
    for coefficient, polynomial in terms:
        output = _poly_add(output, polynomial, coefficient)
    return output


def _poly_exact_divide(dividend: Poly, divisor: Poly) -> Poly:
    """Exact lexicographic division by one polynomial, refusing a remainder."""

    if not divisor:
        raise ZeroDivisionError("cannot divide by the zero polynomial")
    working = dict(dividend)
    quotient: Poly = {}
    divisor_monomial = max(divisor)
    divisor_coefficient = divisor[divisor_monomial]
    while working:
        monomial = max(working)
        coefficient = working[monomial]
        if len(monomial) != len(divisor_monomial) or any(
            left < right for left, right in zip(monomial, divisor_monomial)
        ):
            raise ArithmeticError("displayed polynomial division has a remainder")
        quotient_monomial = tuple(
            left - right for left, right in zip(monomial, divisor_monomial)
        )
        quotient_term = {quotient_monomial: coefficient / divisor_coefficient}
        quotient = _poly_add(quotient, quotient_term)
        working = _poly_add(
            working, _poly_multiply(quotient_term, divisor), -1
        )
    return quotient


def _poly_remainder(dividend: Poly, divisor: Poly) -> Poly:
    """Return the exact lexicographic remainder on division by one polynomial."""

    if not divisor:
        raise ZeroDivisionError("cannot divide by the zero polynomial")
    working = dict(dividend)
    remainder: Poly = {}
    divisor_monomial = max(divisor)
    divisor_coefficient = divisor[divisor_monomial]
    while working:
        monomial = max(working)
        coefficient = working[monomial]
        if len(monomial) == len(divisor_monomial) and all(
            left >= right for left, right in zip(monomial, divisor_monomial)
        ):
            quotient_monomial = tuple(
                left - right for left, right in zip(monomial, divisor_monomial)
            )
            quotient_term = {quotient_monomial: coefficient / divisor_coefficient}
            working = _poly_add(
                working, _poly_multiply(quotient_term, divisor), -1
            )
        else:
            leading = {monomial: coefficient}
            remainder = _poly_add(remainder, leading)
            working = _poly_add(working, leading, -1)
    return remainder


def _poly_substitute(
    poly: Poly, replacements: Sequence[Poly], target_dimension: int
) -> Poly:
    if not replacements:
        raise ValueError("at least one polynomial replacement is required")
    output = _poly_constant(0, target_dimension)
    power_cache: dict[tuple[int, int], Poly] = {}
    for monomial, coefficient in poly.items():
        if len(monomial) != len(replacements):
            raise ValueError("replacement count does not match polynomial dimension")
        term = _poly_constant(coefficient, target_dimension)
        for index, exponent in enumerate(monomial):
            key = (index, exponent)
            if key not in power_cache:
                power_cache[key] = _poly_power(
                    replacements[index], exponent, target_dimension
                )
            term = _poly_multiply(term, power_cache[key])
        output = _poly_add(output, term)
    return output


def _poly_serialize(poly: Poly) -> list[list[object]]:
    rows: list[list[object]] = []
    for monomial in sorted(poly, reverse=True):
        coefficient = poly[monomial]
        rows.append(
            [
                list(monomial),
                coefficient.numerator,
                coefficient.denominator,
            ]
        )
    return rows


def _poly_hash(poly: Poly) -> str:
    return _canonical_sha256(_poly_serialize(poly))


def _poly_total_degree(poly: Poly) -> int:
    return max((sum(monomial) for monomial in poly), default=-1)


def _chebyshev_trace_polynomial(n: int, variable: Poly, dimension: int) -> Poly:
    if type(n) is not int or n < 0:
        raise ValueError("Chebyshev trace index must be nonnegative")
    previous = _poly_constant(2, dimension)
    if n == 0:
        return previous
    current = variable
    if n == 1:
        return current
    for _ in range(2, n + 1):
        previous, current = current, _poly_add(
            _poly_multiply(variable, current), previous, -1
        )
    return current


def _newton_elementaries(power_sums: Sequence[Poly], dimension: int) -> list[Poly]:
    elementaries = [_poly_constant(1, dimension)]
    for degree in range(1, len(power_sums) + 1):
        numerator = _poly_constant(0, dimension)
        for index in range(1, degree + 1):
            sign = 1 if index % 2 else -1
            numerator = _poly_add(
                numerator,
                _poly_multiply(elementaries[degree - index], power_sums[index - 1]),
                sign,
            )
        elementaries.append(_poly_scale(numerator, Fraction(1, degree)))
    return elementaries[1:]


def normalized_coefficient_generators() -> tuple[Poly, Poly, Poly, Poly]:
    """Return ``e_k(tensor)-e_k(Sym7)`` for ``1<=k<=4``."""

    dimension = 3
    u = _poly_variable(0, dimension)
    v = _poly_variable(1, dimension)
    z = _poly_variable(2, dimension)
    tensor_power_sums = []
    target_power_sums = []
    for n in range(1, 5):
        std = _chebyshev_trace_polynomial(n, u, dimension)
        sym3 = _poly_add(
            _chebyshev_trace_polynomial(3 * n, v, dimension),
            _chebyshev_trace_polynomial(n, v, dimension),
        )
        tensor_power_sums.append(_poly_multiply(std, sym3))
        target = _poly_constant(0, dimension)
        for weight in (1, 3, 5, 7):
            target = _poly_add(
                target, _chebyshev_trace_polynomial(weight * n, z, dimension)
            )
        target_power_sums.append(target)
    tensor_elementaries = _newton_elementaries(tensor_power_sums, dimension)
    target_elementaries = _newton_elementaries(target_power_sums, dimension)
    return tuple(
        _poly_add(left, right, -1)
        for left, right in zip(tensor_elementaries, target_elementaries)
    )


def _rational_u_substitution_numerator(generator: Poly, power: int) -> Poly:
    """Return ``g(v)^power*f(t(z)/g(v),v,z)`` in ``Q[v,z]``."""

    dimension = 2
    v = _poly_variable(0, dimension)
    z = _poly_variable(1, dimension)
    g = _poly_sum(
        dimension,
        (1, _poly_power(v, 3, dimension)),
        (-2, v),
    )
    t = _poly_sum(
        dimension,
        (1, _poly_power(z, 7, dimension)),
        (-6, _poly_power(z, 5, dimension)),
        (10, _poly_power(z, 3, dimension)),
        (-4, z),
    )
    output = _poly_constant(0, dimension)
    for (u_degree, v_degree, z_degree), coefficient in generator.items():
        if u_degree > power:
            raise ArithmeticError("u-degree exceeds the clearing power")
        term = _poly_constant(coefficient, dimension)
        for factor in (
            _poly_power(t, u_degree, dimension),
            _poly_power(g, power - u_degree, dimension),
            _poly_power(v, v_degree, dimension),
            _poly_power(z, z_degree, dimension),
        ):
            term = _poly_multiply(term, factor)
        output = _poly_add(output, term)
    return output


def _even_vz_to_VZ(poly: Poly) -> Poly:
    output: Poly = {}
    for (v_degree, z_degree), coefficient in poly.items():
        if v_degree % 2 or z_degree % 2:
            raise ArithmeticError("expected an even polynomial in v and z")
        monomial = (v_degree // 2, z_degree // 2)
        output[monomial] = output.get(monomial, Fraction(0)) + coefficient
    return _poly_clean(output)


def _lift_VZ_to_vz(poly: Poly) -> Poly:
    return {
        (2 * V_degree, 2 * Z_degree): coefficient
        for (V_degree, Z_degree), coefficient in poly.items()
    }


def elimination_certificate() -> dict[str, object]:
    """Recompute the small exact residual-support certificate."""

    generators = normalized_coefficient_generators()
    dimension3 = 3
    u3 = _poly_variable(0, dimension3)
    v3 = _poly_variable(1, dimension3)
    z3 = _poly_variable(2, dimension3)
    g3 = _poly_sum(
        dimension3,
        (1, _poly_power(v3, 3, dimension3)),
        (-2, v3),
    )
    t3 = _poly_sum(
        dimension3,
        (1, _poly_power(z3, 7, dimension3)),
        (-6, _poly_power(z3, 5, dimension3)),
        (10, _poly_power(z3, 3, dimension3)),
        (-4, z3),
    )
    if generators[0] != _poly_add(_poly_multiply(u3, g3), t3, -1):
        raise ArithmeticError("first coefficient elimination identity failed")

    N2 = _rational_u_substitution_numerator(generators[1], 2)
    N3 = _rational_u_substitution_numerator(generators[2], 3)
    N4 = _rational_u_substitution_numerator(generators[3], 4)

    dimension2 = 2
    v = _poly_variable(0, dimension2)
    z = _poly_variable(1, dimension2)
    V_lift = _poly_power(v, 2, dimension2)
    Z_lift = _poly_power(z, 2, dimension2)
    D = _poly_multiply(
        _poly_add(V_lift, Z_lift, -1),
        _poly_add(V_lift, _poly_power(_poly_add(Z_lift, _poly_constant(2, 2), -1), 2, 2), -1),
    )

    after_D_2 = _poly_exact_divide(N2, D)
    after_D_3 = _poly_exact_divide(N3, D)
    after_D_3_v = _poly_exact_divide(after_D_3, v)
    after_D_3_vz = _poly_exact_divide(after_D_3_v, z)
    after_D_4 = _poly_exact_divide(N4, D)

    quotient2 = _even_vz_to_VZ(after_D_2)
    quotient3 = _even_vz_to_VZ(after_D_3_vz)
    Cpoly = _even_vz_to_VZ(after_D_4)

    V = _poly_variable(0, dimension2)
    Z = _poly_variable(1, dimension2)
    V_minus_2 = _poly_add(V, _poly_constant(2, dimension2), -1)
    Z_minus_2 = _poly_add(Z, _poly_constant(2, dimension2), -1)
    Q16 = _poly_sum(
        dimension2,
        (1, _poly_power(Z, 2, dimension2)),
        (-4, Z),
        (2, _poly_constant(1, dimension2)),
    )
    A = _poly_exact_divide(quotient2, V_minus_2)
    B = _poly_exact_divide(
        quotient3,
        _poly_multiply(_poly_multiply(Z_minus_2, Q16), V_minus_2),
    )

    H = _poly_sum(
        dimension2,
        (1, _poly_power(Z, 4, dimension2)),
        (-8, _poly_power(Z, 3, dimension2)),
        (20, _poly_power(Z, 2, dimension2)),
        (-16, Z),
        (4, _poly_constant(1, dimension2)),
    )
    difference_identity = _poly_add(
        _poly_add(A, B, -1),
        _poly_multiply(V_minus_2, _poly_add(V, H, -1)),
    )
    if difference_identity:
        raise ArithmeticError("A-B ideal-membership identity failed")

    dimension1 = 1
    X = _poly_variable(0, dimension1)
    H1 = _poly_sum(
        dimension1,
        (1, _poly_power(X, 4, dimension1)),
        (-8, _poly_power(X, 3, dimension1)),
        (20, _poly_power(X, 2, dimension1)),
        (-16, X),
        (4, _poly_constant(1, dimension1)),
    )
    Q20 = _poly_sum(
        dimension1,
        (1, _poly_power(X, 2, dimension1)),
        (-5, X),
        (5, _poly_constant(1, dimension1)),
    )
    Q16_1 = _poly_sum(
        dimension1,
        (1, _poly_power(X, 2, dimension1)),
        (-4, X),
        (2, _poly_constant(1, dimension1)),
    )
    Q18 = _poly_sum(
        dimension1,
        (1, _poly_power(X, 3, dimension1)),
        (-6, _poly_power(X, 2, dimension1)),
        (9, X),
        (-1, _poly_constant(1, dimension1)),
    )
    Q7_14 = _poly_sum(
        dimension1,
        (1, _poly_power(X, 3, dimension1)),
        (-5, _poly_power(X, 2, dimension1)),
        (6, X),
        (-1, _poly_constant(1, dimension1)),
    )
    generic_support = _poly_constant(1, dimension1)
    for factor in (Q20, _poly_power(Q16_1, 2, 1), Q18, Q7_14):
        generic_support = _poly_multiply(generic_support, factor)
    A_at_H = _poly_substitute(A, (H1, X), dimension1)
    if A_at_H != generic_support:
        raise ArithmeticError("generic residual factorization failed")

    C_at_2 = _poly_substitute(
        Cpoly, (_poly_constant(2, dimension1), X), dimension1
    )
    special_support = _poly_multiply(
        _poly_power(X, 2, dimension1),
        _poly_multiply(
            _poly_power(_poly_add(X, _poly_constant(2, 1), -1), 3, 1),
            _poly_power(Q16_1, 3, 1),
        ),
    )
    if C_at_2 != special_support:
        raise ArithmeticError("V=2 residual factorization failed")

    t_factorization = _poly_multiply(
        X,
        _poly_multiply(
            _poly_add(_poly_power(X, 2, 1), _poly_constant(2, 1), -1),
            _poly_sum(
                1,
                (1, _poly_power(X, 4, 1)),
                (-4, _poly_power(X, 2, 1)),
                (2, _poly_constant(1, 1)),
            ),
        ),
    )
    target_trace = _poly_sum(
        1,
        (1, _poly_power(X, 7, 1)),
        (-6, _poly_power(X, 5, 1)),
        (10, _poly_power(X, 3, 1)),
        (-4, X),
    )
    if target_trace != t_factorization:
        raise ArithmeticError("g=0 target-trace factorization failed")

    squarefree_support = _poly_constant(1, dimension1)
    for factor in (
        X,
        _poly_add(X, _poly_constant(2, 1), -1),
        Q16_1,
        Q20,
        Q18,
        Q7_14,
    ):
        squarefree_support = _poly_multiply(squarefree_support, factor)

    return {
        "generator_term_counts": [len(generator) for generator in generators],
        "generator_total_degrees": [
            _poly_total_degree(generator) for generator in generators
        ],
        "generators_serialized": [_poly_serialize(item) for item in generators],
        "first_identity": "f1=u*g(v)-t(z), g=v*(v^2-2), t=z*(z^2-2)*(z^4-4*z^2+2)",
        "common_graph_divisor": "D=(v^2-z^2)*(v^2-(z^2-2)^2)",
        "cleared_factorizations": {
            "N2": "D*(V-2)*A(V,Z)",
            "N3": "D*v*z*(Z-2)*(Z^2-4Z+2)*(V-2)*B(V,Z)",
            "N4": "D*C(V,Z)",
            "A_serialized": _poly_serialize(A),
            "B_serialized": _poly_serialize(B),
            "C_serialized": _poly_serialize(Cpoly),
            "A_sha256": _poly_hash(A),
            "B_sha256": _poly_hash(B),
            "C_sha256": _poly_hash(Cpoly),
        },
        "small_ideal_membership_identity": "A-B=-(V-2)*(V-H(Z)), H=Z^4-8Z^3+20Z^2-16Z+4",
        "generic_substitution_factorization": "A(H(Z),Z)=(Z^2-5Z+5)*(Z^2-4Z+2)^2*(Z^3-6Z^2+9Z-1)*(Z^3-5Z^2+6Z-1)",
        "V_equals_2_factorization": "C(2,Z)=Z^2*(Z-2)^3*(Z^2-4Z+2)^3",
        "squarefree_residual_candidate_containment": "Z*(Z-2)*(Z^2-4Z+2)*(Z^2-5Z+5)*(Z^3-6Z^2+9Z-1)*(Z^3-5Z^2+6Z-1)",
        "squarefree_residual_candidate_serialized": _poly_serialize(
            squarefree_support
        ),
        "rational_root_exclusion": {
            "Z^2-4Z+2": "discriminant 8 is not a rational square",
            "Z^2-5Z+5": "discriminant 5 is not a rational square",
            "Z^3-6Z^2+9Z-1": "monic rational-root candidates +/-1 both fail",
            "Z^3-5Z^2+6Z-1": "monic rational-root candidates +/-1 both fail",
            "remaining_rational_Z": [0, 2],
        },
        "runtime_method": "exact sparse Fraction arithmetic, exact displayed-factor divisions, substitution, and multiplication; no Groebner basis or CAS",
    }


def _univariate_factor_in_z_from_Z(factor_in_Z: Poly) -> Poly:
    z = _poly_variable(0, 1)
    return _poly_substitute(factor_in_Z, (_poly_power(z, 2, 1),), 1)


def _verify_univariate_residual_locus(
    replacements: Sequence[Poly], minimal_in_z: Poly
) -> int:
    checks = 0
    for generator in normalized_coefficient_generators():
        specialized = _poly_substitute(generator, replacements, 1)
        if _poly_remainder(specialized, minimal_in_z):
            raise ArithmeticError("displayed cyclotomic residual witness failed")
        checks += 1
    return checks


def residual_witness_certificate() -> dict[str, object]:
    """Verify explicit residual strata without claiming they exhaust all points."""

    z = _poly_variable(0, 1)
    one = _poly_constant(1, 1)
    zero = _poly_constant(0, 1)
    C2 = _chebyshev_trace_polynomial(2, z, 1)
    C3 = _chebyshev_trace_polynomial(3, z, 1)
    C5 = _chebyshev_trace_polynomial(5, z, 1)
    C6 = _chebyshev_trace_polynomial(6, z, 1)

    X = _poly_variable(0, 1)
    factor_Z2 = _poly_add(X, _poly_constant(2, 1), -1)
    factor_N16 = _poly_sum(
        1,
        (1, _poly_power(X, 2, 1)),
        (-4, X),
        (2, one),
    )
    factor_N20 = _poly_sum(
        1,
        (1, _poly_power(X, 2, 1)),
        (-5, X),
        (5, one),
    )
    factor_N9_18 = _poly_sum(
        1,
        (1, _poly_power(X, 3, 1)),
        (-6, _poly_power(X, 2, 1)),
        (9, X),
        (-1, one),
    )
    factor_N14 = _poly_sum(
        1,
        (1, _poly_power(X, 3, 1)),
        (-5, _poly_power(X, 2, 1)),
        (6, X),
        (-1, one),
    )
    minima = {
        "N8": _univariate_factor_in_z_from_Z(factor_Z2),
        "N16": _univariate_factor_in_z_from_Z(factor_N16),
        "N20": _univariate_factor_in_z_from_Z(factor_N20),
        "N9_18": _univariate_factor_in_z_from_Z(factor_N9_18),
        "N14": _univariate_factor_in_z_from_Z(factor_N14),
    }

    checks: Counter[str] = Counter()
    for epsilon in (-1, 1):
        checks["N8"] += _verify_univariate_residual_locus(
            (zero, _poly_scale(z, epsilon), z), minima["N8"]
        )
        checks["N16_u_zero"] += _verify_univariate_residual_locus(
            (zero, _poly_scale(C3, epsilon), z), minima["N16"]
        )
        checks["N20"] += _verify_univariate_residual_locus(
            (_poly_scale(z, epsilon), _poly_scale(C6, epsilon), z),
            minima["N20"],
        )
        checks["N9_18"] += _verify_univariate_residual_locus(
            (_poly_scale(C2, epsilon), _poly_scale(C5, epsilon), z),
            minima["N9_18"],
        )
        checks["N14"] += _verify_univariate_residual_locus(
            (_poly_scale(C2, epsilon), _poly_scale(C3, epsilon), z),
            minima["N14"],
        )
        for delta in (-1, 1):
            checks["N16_v_squared_2"] += _verify_univariate_residual_locus(
                (_poly_scale(C3, epsilon), _poly_scale(C2, delta), z),
                minima["N16"],
            )

    return {
        "scope": "verified non-graph strata contained in the exact support; not an exhaustive algebraic point classification",
        "N8_Z_equals_2": "u=0, v=+/-z (hence v^2=2)",
        "N16_Z2_minus_4Z_plus_2": [
            "u=0, v=+/-C3(z), hence v^2=4-Z",
            "u=+/-C3(z), v=+/-C2(z), hence u^2=4-Z and v^2=2; the two signs are independent",
        ],
        "N20_Z2_minus_5Z_plus_5": "(u,v)=epsilon*(z,C6(z))",
        "N9_18_Z3_minus_6Z2_plus_9Z_minus_1": "(u,v)=epsilon*(C2(z),C5(z))",
        "N14_Z3_minus_5Z2_plus_6Z_minus_1": "(u,v)=epsilon*(C2(z),C3(z))",
        "zero_remainder_checks": dict(sorted(checks.items())),
        "all_zero_remainder_checks": sum(checks.values()),
    }


def Z_zero_stratification_certificate() -> dict[str, object]:
    """Prove that the original system at z=0 has four graph points only."""

    generators = normalized_coefficient_generators()
    u = _poly_variable(0, 2)
    v = _poly_variable(1, 2)
    zero2 = _poly_constant(0, 2)
    specialized = tuple(
        _poly_substitute(generator, (u, v, zero2), 2)
        for generator in generators
    )
    expected_f1 = _poly_multiply(
        _poly_multiply(u, v),
        _poly_add(_poly_power(v, 2, 2), _poly_constant(2, 2), -1),
    )
    if specialized[0] != expected_f1:
        raise ArithmeticError("z=0 first-equation stratification failed")
    f2_UV = _even_vz_to_VZ(specialized[1])
    f4_UV = _even_vz_to_VZ(specialized[3])

    dimension1 = 1
    X = _poly_variable(0, dimension1)
    zero1 = _poly_constant(0, dimension1)
    two1 = _poly_constant(2, dimension1)
    four1 = _poly_constant(4, dimension1)
    f2_v_zero = _poly_substitute(f2_UV, (X, zero1), 1)
    expected_v_zero = _poly_scale(_poly_add(X, four1, -1), 2)
    if f2_v_zero != expected_v_zero:
        raise ArithmeticError("z=v=0 stratum failed")
    f2_V_two = _poly_substitute(f2_UV, (X, two1), 1)
    if f2_V_two != _poly_constant(-4, 1):
        raise ArithmeticError("z=0, V=2 exclusion failed")

    V = X
    f2_u_zero = _poly_substitute(f2_UV, (zero1, V), 1)
    f4_u_zero = _poly_substitute(f4_UV, (zero1, V), 1)
    V_minus_4 = _poly_add(V, four1, -1)
    q2 = _poly_sum(
        1,
        (1, _poly_power(V, 2, 1)),
        (-2, V),
        (2, _poly_constant(1, 1)),
    )
    q4 = _poly_multiply(
        V,
        _poly_sum(
            1,
            (1, _poly_power(V, 2, 1)),
            (-4, V),
            (5, _poly_constant(1, 1)),
        ),
    )
    if f2_u_zero != _poly_multiply(V_minus_4, q2):
        raise ArithmeticError("z=u=0 second-equation factorization failed")
    if f4_u_zero != _poly_multiply(V_minus_4, q4):
        raise ArithmeticError("z=u=0 fourth-equation factorization failed")
    bezout_left = _poly_sum(
        1,
        (Fraction(1, 2), _poly_constant(1, 1)),
        (Fraction(-1, 10), _poly_power(V, 2, 1)),
    )
    bezout_right = _poly_sum(
        1,
        (Fraction(1, 10), V),
        (Fraction(1, 5), _poly_constant(1, 1)),
    )
    bezout = _poly_add(
        _poly_multiply(bezout_left, q2),
        _poly_multiply(bezout_right, q4),
    )
    if bezout != _poly_constant(1, 1):
        raise ArithmeticError("z=u=0 Bezout exclusion failed")
    return {
        "first_equation": "u*v*(v^2-2)=0",
        "v_equals_0": "f2=2*(u^2-4), hence (u,v)=(+/-2,0)",
        "u_equals_0": "f2=(V-4)*(V^2-2V+2), f4=V*(V-4)*(V^2-4V+5); the displayed Bezout identity makes V=4 necessary",
        "u_equals_0_Bezout": "(1/2-V^2/10)*(V^2-2V+2)+(V/10+1/5)*V*(V^2-4V+5)=1",
        "V_equals_2": "f2=-4, impossible",
        "solutions": [
            {"u": -2, "v": 0},
            {"u": 2, "v": 0},
            {"u": 0, "v": -2},
            {"u": 0, "v": 2},
        ],
        "all_solutions_are_graph_points": True,
    }


def _evaluate_poly(poly: Poly, values: Sequence[Fraction | int]) -> Fraction:
    total = Fraction(0)
    for monomial, coefficient in poly.items():
        if len(monomial) != len(values):
            raise ValueError("evaluation dimension mismatch")
        term = coefficient
        for value, exponent in zip(values, monomial):
            term *= Fraction(value) ** exponent
        total += term
    return total


def graph_weight_certificate() -> dict[str, object]:
    target = tuple(range(-7, 8, 2))
    first = tuple(sorted(sign * 4 + weight for sign in (-1, 1) for weight in (-3, -1, 1, 3)))
    second = tuple(sorted(sign + 2 * weight for sign in (-1, 1) for weight in (-3, -1, 1, 3)))
    if first != target or second != target:
        raise ArithmeticError("r=3 torus weight identity failed")

    generators = normalized_coefficient_generators()
    dimension1 = 1
    z = _poly_variable(0, dimension1)
    C2 = _poly_add(_poly_power(z, 2, 1), _poly_constant(2, 1), -1)
    C4 = _poly_sum(
        1,
        (1, _poly_power(z, 4, 1)),
        (-4, _poly_power(z, 2, 1)),
        (2, _poly_constant(1, 1)),
    )
    substitutions_checked = 0
    for epsilon in (-1, 1):
        for replacements in (
            (_poly_scale(C4, epsilon), _poly_scale(z, epsilon), z),
            (_poly_scale(z, epsilon), _poly_scale(C2, epsilon), z),
        ):
            for generator in generators:
                if _poly_substitute(generator, replacements, 1):
                    raise ArithmeticError("signed graph coefficient identity failed")
                substitutions_checked += 1
    return {
        "target_weights": list(target),
        "Std(w^4)_tensor_Sym3(w)_weights": list(first),
        "Std(w)_tensor_Sym3(w^2)_weights": list(second),
        "signed_graph_coefficient_zero_residuals": substitutions_checked,
        "same_epsilon_reason": "Std(-a) contributes -1 and Sym3(-b) contributes -1 because degree 3 is odd, so only their coupled central sign preserves every tensor root",
    }


def _su2_irreducible_trace_moments(highest_weight: int, maximum: int) -> list[int]:
    if type(highest_weight) is not int or highest_weight < 0:
        raise ValueError("highest weight must be a nonnegative integer")
    if type(maximum) is not int or maximum < 0:
        raise ValueError("moment maximum must be a nonnegative integer")
    character = {0: 1}
    moments = []
    for _ in range(maximum + 1):
        moments.append(character.get(0, 0))
        next_character: dict[int, int] = defaultdict(int)
        for left_weight, multiplicity in character.items():
            for output_weight in range(
                abs(left_weight - highest_weight),
                left_weight + highest_weight + 1,
                2,
            ):
                next_character[output_weight] += multiplicity
        character = dict(next_character)
    return moments


def compact_trace_moment_certificate(maximum: int = 8) -> dict[str, object]:
    std = _su2_irreducible_trace_moments(1, maximum)
    sym3 = _su2_irreducible_trace_moments(3, maximum)
    sym7 = _su2_irreducible_trace_moments(7, maximum)
    independent_product = [left * right for left, right in zip(std, sym3)]
    expected_product = [1, 0, 1, 0, 8, 0, 170, 0, 5096]
    expected_sym7 = [1, 0, 1, 0, 8, 0, 260, 0, 11096]
    if maximum != 8 or independent_product != expected_product or sym7 != expected_sym7:
        raise ArithmeticError("compact trace-moment certificate changed")
    return {
        "degrees": list(range(maximum + 1)),
        "Std_SU2_tensor_Sym3_SU2_independent_product": independent_product,
        "Sym7_SU2": sym7,
        "alias_through_degree": 4,
        "first_separation": "degree 6: 170 versus 260",
        "generic_USp8_standard_degree_4_moment": 3,
        "method": "exact Clebsch-Gordan multiplicity recursion; independent product moments multiply",
        "firewall": "compact Haar moments are contextual fingerprints, not arithmetic-origin recovery or a local-to-global theorem",
    }


def _base_power_sums(t: int, q: int, maximum: int) -> list[int]:
    values = [2, t]
    for _ in range(2, maximum + 1):
        values.append(t * values[-1] - q * values[-2])
    return values[: maximum + 1]


def _integer_newton_elementaries(power_sums: Sequence[int]) -> list[int]:
    elementaries = [1]
    for degree in range(1, len(power_sums) + 1):
        numerator = sum(
            (1 if index % 2 else -1)
            * elementaries[degree - index]
            * power_sums[index - 1]
            for index in range(1, degree + 1)
        )
        quotient, remainder = divmod(numerator, degree)
        if remainder:
            raise ArithmeticError("Newton recurrence lost integrality")
        elementaries.append(quotient)
    return elementaries[1:]


def tensor_sym3_factor(A: object, B: object, q: object) -> tuple[int, ...]:
    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    A_power = _base_power_sums(A_int, q_int, 8)
    B_power = _base_power_sums(B_int, q_int, 24)
    tensor_power_sums = [
        A_power[n] * (B_power[3 * n] + q_int**n * B_power[n])
        for n in range(1, 9)
    ]
    elementaries = _integer_newton_elementaries(tensor_power_sums)
    return tuple([1] + [(-1 if degree % 2 else 1) * value for degree, value in enumerate(elementaries, 1)])


def sym7_factor(C: object, q: object) -> tuple[int, ...]:
    C_int = _require_builtin_int(C, "C")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    powers = _base_power_sums(C_int, q_int, 56)
    target_power_sums = [
        powers[7 * n]
        + q_int**n * powers[5 * n]
        + q_int ** (2 * n) * powers[3 * n]
        + q_int ** (3 * n) * powers[n]
        for n in range(1, 9)
    ]
    elementaries = _integer_newton_elementaries(target_power_sums)
    return tuple([1] + [(-1 if degree % 2 else 1) * value for degree, value in enumerate(elementaries, 1)])


def typed_tensor_signature(A: object, B: object, q: object) -> tuple[tuple[int, int], ...]:
    q_int = _require_builtin_int(q, "q")
    factor = tensor_sym3_factor(A, B, q_int)
    s = math.isqrt(q_int)
    if s * s == q_int:
        return tuple((coefficient * s ** (3 * degree), 0) for degree, coefficient in enumerate(factor))
    signature = []
    for degree, coefficient in enumerate(factor):
        if degree % 2:
            signature.append((0, coefficient * q_int ** ((3 * degree - 1) // 2)))
        else:
            signature.append((coefficient * q_int ** (3 * degree // 2), 0))
    return tuple(signature)


def typed_sym7_signature(C: object, q: object) -> tuple[tuple[int, int], ...]:
    return tuple((coefficient, 0) for coefficient in sym7_factor(C, q))


def typed_factor_equal(A: object, B: object, C: object, q: object) -> bool:
    return typed_tensor_signature(A, B, q) == typed_sym7_signature(C, q)


def graph_branches(A: object, B: object, C: object, q: object) -> list[str]:
    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    C_int = _require_builtin_int(C, "C")
    q_int = _require_builtin_int(q, "q")
    prime_power_data(q_int)
    s = math.isqrt(q_int)
    if s * s != q_int:
        return []
    F = C_int**4 - 4 * q_int * C_int**2 + 2 * q_int**2
    G = C_int**2 - 2 * q_int
    branches = []
    for epsilon in (-1, 1):
        if B_int == epsilon * C_int and s**3 * A_int == epsilon * F:
            branches.append(f"I:e={epsilon:+d}")
        if A_int == epsilon * C_int and s * B_int == epsilon * G:
            branches.append(f"II:e={epsilon:+d}")
    return branches


def integral_graph_predicate(A: object, B: object, C: object, q: object) -> bool:
    return bool(graph_branches(A, B, C, q))


def hasse_lattice_count_theorem(p: object, exponent: object) -> dict[str, object]:
    p_int = _require_builtin_int(p, "p")
    exponent_int = _require_builtin_int(exponent, "exponent")
    if prime_power_data(p_int**exponent_int) != (p_int, exponent_int):
        raise ValueError("p^exponent must be an odd prime power")
    if exponent_int % 2:
        return {
            "p": p_int,
            "exponent": exponent_int,
            "q_is_square": False,
            "branch_I_distinct_triples": 0,
            "branch_II_distinct_triples": 0,
            "cross_branch_overlap": 0,
            "union_distinct_triples": 0,
        }
    k = exponent_int // 2
    first_scale = p_int ** (k // 4)
    second_scale = p_int ** (k // 2)
    branch_I = 8 * first_scale + 2
    branch_II = 8 * second_scale + 2
    overlap = 8
    return {
        "p": p_int,
        "exponent": exponent_int,
        "q_is_square": True,
        "k": k,
        "branch_I_C_divisor": p_int ** ((3 * k + 3) // 4),
        "branch_II_C_divisor": p_int ** ((k + 1) // 2),
        "branch_I_distinct_triples": branch_I,
        "branch_II_distinct_triples": branch_II,
        "cross_branch_overlap": overlap,
        "overlap_normalized_z": [-2, -1, 1, 2],
        "union_distinct_triples": branch_I + branch_II - overlap,
        "closed_formula": 8 * first_scale + 8 * second_scale - 4,
    }


def square_graph_triples(q: object) -> set[tuple[int, int, int]]:
    q_int = _require_builtin_int(q, "q")
    p, exponent = prime_power_data(q_int)
    if exponent % 2:
        return set()
    s = p ** (exponent // 2)
    triples = set()
    for C in range(-2 * s, 2 * s + 1):
        F = C**4 - 4 * q_int * C**2 + 2 * q_int**2
        G = C**2 - 2 * q_int
        for epsilon in (-1, 1):
            if F % s**3 == 0:
                triples.add((epsilon * (F // s**3), epsilon * C, C))
            if G % s == 0:
                triples.add((epsilon * C, epsilon * (G // s), C))
    return triples


def square_count_certificate(p: object, k: object) -> dict[str, object]:
    p_int = _require_builtin_int(p, "p")
    k_int = _require_builtin_int(k, "k")
    if k_int <= 0:
        raise ValueError("k must be positive")
    q = p_int ** (2 * k_int)
    theorem = hasse_lattice_count_theorem(p_int, 2 * k_int)
    triples = square_graph_triples(q)
    if len(triples) != theorem["union_distinct_triples"]:
        raise ArithmeticError("square graph enumeration disagrees with count theorem")
    overlap = [triple for triple in triples if len(graph_branches(*triple, q)) == 2]
    if len(overlap) != 8:
        raise ArithmeticError("eight-point graph overlap changed")
    return {
        **theorem,
        "enumerated_graph_triples": len(triples),
        "overlap_triples": [list(triple) for triple in sorted(overlap)],
    }


def _trace_histogram(row: Mapping[str, object]) -> dict[int, int]:
    raw = row.get("model_trace_histogram")
    if not isinstance(raw, dict):
        raise RuntimeError("locked trace histogram is malformed")
    histogram: dict[int, int] = {}
    for trace, count in raw.items():
        if not isinstance(trace, str) or type(count) is not int or count <= 0:
            raise RuntimeError("locked trace histogram entry is malformed")
        histogram[int(trace)] = count
    return histogram


def _enumerate_trace_triples(
    q: int,
    traces: Sequence[int],
    histogram: Mapping[int, int] | None,
    guard: ResourceGuard,
    *,
    locked: bool,
) -> dict[str, object]:
    tensor_signatures = {
        (A, B): typed_tensor_signature(A, B, q) for A in traces for B in traces
    }
    target_signatures = {C: typed_sym7_signature(C, q) for C in traces}
    hits = []
    triples_checked = 0
    for A in traces:
        for B in traces:
            tensor = tensor_signatures[(A, B)]
            for C in traces:
                triples_checked += 1
                guard.charge_triple(locked=locked)
                equal = tensor == target_signatures[C]
                predicted = integral_graph_predicate(A, B, C, q)
                if equal != predicted:
                    raise ArithmeticError(
                        f"integral classification replay failed at {(q, A, B, C)}"
                    )
                if equal:
                    weight = None
                    if histogram is not None:
                        weight = histogram[A] * histogram[B] * histogram[C]
                    hits.append(
                        {
                            "A": A,
                            "B": B,
                            "C": C,
                            "branches": graph_branches(A, B, C, q),
                            "member_weight": weight,
                        }
                    )
    return {
        "q": q,
        "trace_atom_count": len(traces),
        "ordered_trace_triples_checked": triples_checked,
        "factor_equal_trace_triple_count": len(hits),
        "factor_equal_member_weight": (
            sum(hit["member_weight"] for hit in hits) if histogram is not None else None
        ),
        "hits": hits,
    }


def frozen_and_synthetic_replay(
    genus1: Mapping[str, object], guard: ResourceGuard
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rows = genus1.get("finite_regressions")
    if not isinstance(rows, list):
        raise RuntimeError("locked finite rows are malformed")
    frozen = []
    for row in rows:
        if not isinstance(row, dict) or type(row.get("q")) is not int:
            raise RuntimeError("locked finite row is malformed")
        q = row["q"]
        histogram = _trace_histogram(row)
        replay = _enumerate_trace_triples(
            q, sorted(histogram), histogram, guard, locked=True
        )
        if replay["factor_equal_trace_triple_count"] != 0:
            raise ArithmeticError("nonsquare locked support unexpectedly intersects")
        frozen.append(replay)
    if tuple(row["q"] for row in frozen) != FROZEN_Q_VALUES:
        raise RuntimeError("frozen replay q sequence changed")
    if guard.locked_triples != guard.locked_cap:
        raise ArithmeticError("locked trace-triple total changed")

    synthetic = []
    for q in SYNTHETIC_Q_VALUES:
        s = math.isqrt(q)
        traces = list(range(-2 * s, 2 * s + 1))
        replay = _enumerate_trace_triples(q, traces, None, guard, locked=False)
        p, exponent = prime_power_data(q)
        theorem = hasse_lattice_count_theorem(p, exponent)
        if replay["factor_equal_trace_triple_count"] != theorem["union_distinct_triples"]:
            raise ArithmeticError("synthetic square-q count disagrees with theorem")
        replay["count_theorem"] = theorem
        synthetic.append(replay)
    if guard.synthetic_triples != guard.synthetic_cap:
        raise ArithmeticError("synthetic trace-triple total changed")
    return frozen, synthetic


def _owned_file_locks() -> dict[str, dict[str, str]]:
    output = {}
    for role, path in (
        ("producer", Path(__file__).resolve()),
        ("note", NOTE_PATH),
        ("test", TEST_PATH),
    ):
        if not path.is_file():
            raise RuntimeError(f"owned {role} file is missing: {path}")
        output[role] = {
            "path": _relative(path),
            "sha256_lf_normalized": _lf_sha256(path),
        }
    return output


def build_fixture(q_values: Iterable[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"frozen packet requires exactly q={FROZEN_Q_VALUES}")
    sources = load_locked_sources()
    guard = ResourceGuard()
    guard.charge("locked_source_pairs_verified", len(SOURCE_LOCKS))

    algebra = elimination_certificate()
    guard.charge("exact_elimination_certificate_identities", 9)
    residual_witnesses = residual_witness_certificate()
    guard.charge(
        "cyclotomic_residual_zero_remainders",
        residual_witnesses["all_zero_remainder_checks"],
    )
    z_zero = Z_zero_stratification_certificate()
    guard.charge("Z_zero_original_system_stratification", 7)
    weights = graph_weight_certificate()
    guard.charge("signed_graph_weight_and_coefficient_identities", 18)
    moments = compact_trace_moment_certificate()
    guard.charge("compact_representation_moments", 18)
    count_examples = [
        square_count_certificate(3, 1),
        square_count_certificate(5, 1),
        square_count_certificate(3, 2),
    ]
    guard.charge("p_adic_count_and_overlap_certificates", len(count_examples))
    frozen, synthetic = frozen_and_synthetic_replay(sources["genus1"], guard)

    payload: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_tensor_sym3_sym7_spectral_intersection.v1",
        "packet_id": "FUNCTION_FIELD.ELLIPTIC.TENSOR_SYM3.SYM7.SPECTRAL.INTERSECTION.V1",
        "status": "EXACT_INTEGRAL_RAW_INTERSECTION_AND_SQUARE_Q_HASSE_COUNT",
        "rigor_level": {
            "normalized_coefficients": "PROVED_BY_EXACT_CHEBYSHEV_POWER_SUMS_AND_NEWTON_RECURRENCES",
            "residual_support": "PROVED_BY_EXPLICIT_EXACT_DIVISIONS_IDEAL_MEMBERSHIP_UNIVARIATE_FACTORIZATIONS_AND_FACTOR_WITNESSES",
            "integral_raw_classification": "PROVED_FOR_ALL_ODD_PRIME_POWERS",
            "square_q_count": "PROVED_BY_P_ADIC_DIVISIBILITY_AND_EXACT_EIGHT_POINT_OVERLAP",
            "finite_replay": "EXACT_FOR_7975_LOCKED_AND_11458_SYNTHETIC_ORDERED_TRACE_TRIPLES",
            "algebraic_residual_points": "EXACT_Z_SUPPORT_WITH_WITNESS_STRATA; INDIVIDUAL POINT SET_NOT_COMPLETELY_CLASSIFIED",
            "global_correspondence_automorphy_and_novelty": "NOT_INFERRED",
        },
        "conventions": {
            "base_factor": "P_t(T)=1-t*T+q*T^2 for geometric traces t=A,B,C",
            "normalized_traces": "u=A/s, v=B/s, z=C/s after choosing s with s^2=q",
            "tensor": "Std(E_A) tensor Sym^3(E_B), degree 8 and weight 4",
            "target": "Sym^7(E_C), degree 8 and weight 7",
            "typed_raw_identity": "P_(Std(A) tensor Sym3(B))(q^(3/2)*T)=P_(Sym7(C))(T)",
            "square_q_identity": "when q=s^2 with chosen positive integer s, P_tensor(s^3*T)=P_Sym7(C)(T)",
            "same_epsilon": "both Std and Sym3 are odd under the central sign, so the graph signs must be coupled",
            "unscaled_firewall": "the unequal weights forbid comparison in the same unscaled variable",
        },
        "normalized_coefficient_system": {
            "tensor_power_sums": "p_n=C_n(u)*(C_(3n)(v)+C_n(v))",
            "target_power_sums": "p_n=C_n(z)+C_(3n)(z)+C_(5n)(z)+C_(7n)(z)",
            "coefficient_range": "Newton e_1 through e_4; reciprocal symmetry supplies degrees 5 through 8",
            "f1": "u*v^3-2*u*v-z^7+6*z^5-10*z^3+4*z",
            "generator_term_counts": algebra["generator_term_counts"],
            "generator_total_degrees": algebra["generator_total_degrees"],
        },
        "complete_integral_raw_intersection_theorem": {
            "scope": "q=p^e for odd prime p, e>=1, and integral A,B,C; Hasse bounds are needed only for the count",
            "statement": "typed factor equality holds iff q is a square, say q=s^2 with s a positive integer, and one of the two same-epsilon raw graph systems holds",
            "normalized_graph_I": "(u,v)=(epsilon*C4(z),epsilon*z), C4(z)=z^4-4z^2+2",
            "normalized_graph_II": "(u,v)=(epsilon*z,epsilon*C2(z)), C2(z)=z^2-2",
            "sign": "epsilon in {-1,+1} is the same in both coordinates",
            "nonsquare_q": "empty",
            "square_graph_I_raw": "B=epsilon*C and s^3*A=epsilon*(C^4-4q*C^2+2q^2)",
            "square_graph_II_raw": "A=epsilon*C and s*B=epsilon*(C^2-2q)",
            "proof_boundary": "the exact elimination leaves only the two graphs or the displayed residual support in Z=z^2=C^2/q; rationality of Z and odd-prime-power valuation exclude every residual",
            "Z_zero_case": "the exact original-system stratification gives only (u,v)=(+/-2,0) or (0,+/-2), all graph points",
            "Z_two_case": "C^2=2q is impossible for odd prime-power q by p-adic parity (and by the factor 2 when p is odd)",
            "no_search_dependency": "finite trace-triple replays are regressions, not the proof",
        },
        "exact_elimination_certificate": {
            **algebra,
            "Z_zero_original_system_stratification": z_zero,
            "verified_genuine_residual_strata": residual_witnesses,
            "exact_nongraph_Z_support": "(Z-2)*(Z^2-4Z+2)*(Z^2-5Z+5)*(Z^3-6Z^2+9Z-1)*(Z^3-5Z^2+6Z-1)",
            "support_logic": "the elimination certificate contains every candidate; the Z=0 stratification removes its nongraph possibility, and exact zero-remainder witnesses make every other irreducible factor genuine",
        },
        "graph_spectral_certificate": weights,
        "compact_trace_moment_context": moments,
        "odd_prime_power_arithmetic": {
            "nonsquare_graph_I_obstruction": "q^2*A=epsilon*s*(C^4-4q*C^2+2q^2); rational-versus-irrational separation would force A=0 and Z^2-4Z+2=0, impossible for rational Z",
            "nonsquare_graph_II_obstruction": "q*B=epsilon*s*(C^2-2q); separation would force B=0 and C^2=2q, impossible",
            "square_graph_I_integrality": "for q=p^(2k), s^3 divides C^4-4s^2*C^2+2s^4 iff p^ceil(3k/4) divides C",
            "square_graph_II_integrality": "s divides C^2-2s^2 iff p^ceil(k/2) divides C",
            "automatic_Hasse_bounds": "C4 and C2 map the normalized compact trace interval [-2,2] into itself",
            "branch_I_count": "8*p^floor(k/4)+2 across both epsilon signs",
            "branch_II_count": "8*p^floor(k/2)+2 across both epsilon signs",
            "eight_point_overlap": "z in {-2,-1,1,2}, with two epsilon choices for each z",
            "union_count": "8*p^floor(k/4)+8*p^floor(k/2)-4",
            "count_examples": count_examples,
            "lattice_firewall": "the count concerns integral Hasse trace triples, not existence of linked curves or a correspondence",
        },
        "locked_trace_support_replay": {
            "families": frozen,
            "aggregate": {
                "q_values": list(FROZEN_Q_VALUES),
                "ordered_trace_triples_checked": sum(
                    row["ordered_trace_triples_checked"] for row in frozen
                ),
                "factor_equal_trace_triple_count": sum(
                    row["factor_equal_trace_triple_count"] for row in frozen
                ),
                "factor_equal_member_weight": sum(
                    row["factor_equal_member_weight"] for row in frozen
                ),
            },
            "source_measure": "three ordered draws from each locked genus-one marked-cubic trace histogram",
        },
        "synthetic_square_q_replay": {
            "rows": synthetic,
            "aggregate": {
                "q_values": list(SYNTHETIC_Q_VALUES),
                "ordered_trace_triples_checked": sum(
                    row["ordered_trace_triples_checked"] for row in synthetic
                ),
                "factor_equal_trace_triple_count": sum(
                    row["factor_equal_trace_triple_count"] for row in synthetic
                ),
            },
            "purpose": "nonvacuous replay of both graph branches and the eight-point overlap",
            "realizability_status": "NOT_TESTED_OR_INFERRED",
        },
        "source_and_file_locks": {
            "source_locks": _source_lock_payload(),
            "owned_file_locks": _owned_file_locks(),
            "authentication": "every source JSON is schema-, payload-, canonical-payload-, and LF-file-locked; every source producer is LF-file-locked",
        },
        "resource_contract": {
            "locked_trace_triple_cap_inclusive": guard.locked_cap,
            "actual_locked_trace_triples": guard.locked_triples,
            "synthetic_trace_triple_cap_inclusive": guard.synthetic_cap,
            "actual_synthetic_trace_triples": guard.synthetic_triples,
            "exclusive_accounted_work_unit_cap": guard.work_cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total_work,
            },
            "unit_definition": "one replayed trace triple or one named exact certificate; not CPU instructions",
            "field_curve_or_model_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "runtime_symbolic_packages": 0,
            "runtime_Groebner_basis_runs": 0,
            "maximum_normalized_coefficient_degree": max(
                algebra["generator_total_degrees"]
            ),
        },
        "scope_firewall": {
            "no_complete_algebraic_residual_claim": "the exact squarefree nongraph Z-support and explicit witness strata are proved, but the individual non-graph point set over the algebraic closure is not claimed complete",
            "no_representation_homomorphism": "torus weight equalities on graph loci do not produce a homomorphism between the source groups",
            "no_local_to_global_upgrade": "one-place local factors supply no motive, compatible system, Euler product, or automorphic transfer",
            "no_realizability_claim": "integral Hasse triples are coefficient-lattice points, not asserted linked elliptic curves",
            "no_novelty_priority_claim": "the exact rigidity packet is recorded without a literature-priority assertion",
            "no_RH_or_GRH_claim": "finite local spectral identities imply no zero-free region, RH, or GRH theorem",
        },
        "next_targets": [
            "classify the individual algebraic residual points at the supported cyclotomic orders 7/14, 8, 16, 9/18, and 20",
            "test whether the same two graph loci are integrally complete for r=4 without a heavy elimination",
            "seek a geometric family that enforces one graph coherently across places without mistaking local trace identities for a correspondence",
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
