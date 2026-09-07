#!/usr/bin/env python3
"""Exact ``Std tensor Sym^2`` / ``Sym^5`` local spectral intersection.

The three elliptic inputs use the geometric-trace convention

    P_t(T) = 1 - t*T + q*T^2.

``Std(E_A) tensor Sym^2(E_B)`` has weight three and degree six, while
``Sym^5(E_C)`` has weight five and degree six.  The typed raw comparison is
therefore

    P_{A tensor Sym2(B)}(q*T) = P_{Sym5(C)}(T).

The producer proves the complete rational classification by exact sparse
polynomial algebra over ``fractions.Fraction``.  It also certifies the finite
algebraic residuals at torus orders 7, 12, and 14, replays locked trace
histograms, and performs no field, curve, or model enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_tensor_sym2_sym5_spectral_intersection.json"
NOTE_PATH = HERE / "ELLIPTIC_TENSOR_SYM2_SYM5_SPECTRAL_INTERSECTION.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_tensor_sym2_sym5_spectral_intersection.py"

GENUS1_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_PRODUCER_PATH = HERE / "genus1_cubic_family_laws.py"
SYM5_PATH = HERE / "elliptic_sym5_coefficient_recovery.json"
SYM5_PRODUCER_PATH = HERE / "elliptic_sym5_coefficient_recovery.py"
FULL_FACTOR_PATH = HERE / "elliptic_symmetric_power_full_factor_sign_aliases.json"
FULL_FACTOR_PRODUCER_PATH = HERE / "elliptic_symmetric_power_full_factor_sign_aliases.py"
CYCLOTOMIC_PATH = HERE / "elliptic_symmetric_power_cyclotomic_spectral_aliases.json"
CYCLOTOMIC_PRODUCER_PATH = HERE / "elliptic_symmetric_power_cyclotomic_spectral_aliases.py"
PREDECESSOR_PATH = HERE / "elliptic_so4_sym3_spectral_intersection.json"
PREDECESSOR_PRODUCER_PATH = HERE / "elliptic_so4_sym3_spectral_intersection.py"

FROZEN_Q_VALUES = (3, 5, 7, 11, 13)
SYNTHETIC_Q = 9
LOCKED_TRIPLE_CAP_INCLUSIVE = 7_975
ACCOUNTED_WORK_CAP_EXCLUSIVE = 20_000
LADDER_REGRESSION_MAX_R = 12


SOURCE_LOCKS = {
    "genus1": {
        "path": GENUS1_PATH,
        "producer": GENUS1_PRODUCER_PATH,
        "schema": "riemann.function_field.genus1_cubic_family_laws.v1",
        "payload": "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
        "file": "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227",
        "producer_file": "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79",
    },
    "sym5": {
        "path": SYM5_PATH,
        "producer": SYM5_PRODUCER_PATH,
        "schema": "riemann.function_field.elliptic_sym5_coefficient_recovery.v1",
        "payload": "f7b1a484d2a8b3cc0b997dbf0f15a69893f279a32bc550b71f28b21a5a9d7467",
        "file": "649f682c0355a71eab618cd4fbd0507e96643b1fefacdd37e1eb9cd82dd36515",
        "producer_file": "53856b8c41ac5d10b0f3e4932e058e8fc806a611932af50a5d738f941998e0f6",
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
    "predecessor": {
        "path": PREDECESSOR_PATH,
        "producer": PREDECESSOR_PRODUCER_PATH,
        "schema": "riemann.function_field.elliptic_so4_sym3_spectral_intersection.v1",
        "payload": "c2657dceb8784e5581092cfd07500f7f39680ce4685516f0ce03e02c195b230c",
        "file": "1bb219a196d2fdb8302f6cf785daeda92312c846bbe294f3ac4fed7c5d3691c6",
        "producer_file": "c33d8b1fed8ed1295abf635821f6b6c6dbf46181b438c2b65e5142e0fea1ddcd",
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
    """Return ``(p,e)`` for an odd prime power and reject everything else."""

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
    """Fail closed on the locked-triple and declared-work budgets."""

    def __init__(
        self,
        triple_cap: int = LOCKED_TRIPLE_CAP_INCLUSIVE,
        work_cap: int = ACCOUNTED_WORK_CAP_EXCLUSIVE,
    ) -> None:
        if type(triple_cap) is not int or triple_cap < 0:
            raise ValueError("triple cap must be a nonnegative built-in integer")
        if type(work_cap) is not int or work_cap <= 0:
            raise ValueError("work cap must be a positive built-in integer")
        self.triple_cap = triple_cap
        self.work_cap = work_cap
        self.locked_triples = 0
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

    def charge_locked_triple(self) -> None:
        if self.locked_triples + 1 > self.triple_cap:
            raise RuntimeError(
                f"locked trace-triple cap exceeded: "
                f"{self.locked_triples + 1}>{self.triple_cap}"
            )
        self.locked_triples += 1
        self.charge("locked_trace_triples")


def _load_authenticated_source(lock: Mapping[str, object]) -> dict[str, object]:
    path = lock["path"]
    producer = lock["producer"]
    if not isinstance(path, Path) or not isinstance(producer, Path):
        raise RuntimeError("internal source lock path is malformed")
    if _lf_sha256(path) != lock["file"]:
        raise RuntimeError(f"locked source file changed: {path.name}")
    if _lf_sha256(producer) != lock["producer_file"]:
        raise RuntimeError(f"locked source producer changed: {producer.name}")
    source = json.loads(path.read_text(encoding="utf-8"))
    if source.get("schema") != lock["schema"]:
        raise RuntimeError(f"locked source schema changed: {path.name}")
    if source.get("payload_sha256") != lock["payload"]:
        raise RuntimeError(f"locked source payload changed: {path.name}")
    unhashed = dict(source)
    claimed = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
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

    sym5 = sources["sym5"]
    if sym5.get("normalization", {}).get("base_factor") != (
        "1-t*T+q*T^2=(1-alpha*T)*(1-beta*T)"
    ):
        raise RuntimeError("locked Sym5 sign convention changed")
    if sym5.get("coefficient_formulas", {}).get("self_reciprocal_coefficients") != (
        "[1,c1,c2,c3,q^5*c2,q^10*c1,q^15]"
    ):
        raise RuntimeError("locked Sym5 coefficient shape changed")

    theorem = sources["full_factor"].get(
        "complete_fixed_q_rational_collision_theorem", {}
    )
    if "first forces x^2=y^2" not in str(theorem.get("statement")):
        raise RuntimeError("locked full-factor rational theorem changed")
    orders = sources["cyclotomic"].get("orders_5_7_9_11")
    if not isinstance(orders, list) or orders[1].get(
        "minimal_polynomial_coefficients_low_to_high"
    ) != [-1, -2, 1, 1]:
        raise RuntimeError("locked order-seven trace polynomial changed")
    predecessor = sources["predecessor"].get(
        "exact_compact_intersection_theorem", {}
    )
    if predecessor.get("graphs") != [
        "u=+(v^2-2)",
        "u=-(v^2-2)",
        "v=+(u^2-2)",
        "v=-(u^2-2)",
    ]:
        raise RuntimeError("locked r=1 predecessor graph convention changed")
    return sources


def _source_lock_payload() -> dict[str, object]:
    output: dict[str, object] = {}
    for name, lock in SOURCE_LOCKS.items():
        path = lock["path"]
        producer = lock["producer"]
        if not isinstance(path, Path) or not isinstance(producer, Path):
            raise RuntimeError(f"internal source lock paths are malformed for {name}")
        output[name] = {
            "fixture_path": _relative(path),
            "fixture_schema": lock["schema"],
            "fixture_payload_sha256": lock["payload"],
            "fixture_sha256_lf_normalized": lock["file"],
            "producer_path": _relative(producer),
            "producer_sha256_lf_normalized": lock["producer_file"],
        }
    return output


def chebyshev_trace(n: object, t: object, q: object = 1) -> Fraction:
    """Return ``alpha^n+beta^n`` from ``alpha+beta=t, alpha*beta=q``."""

    n_int = _require_builtin_int(n, "n")
    if n_int < 0:
        raise ValueError("n must be nonnegative")
    t_q = Fraction(t)
    q_q = Fraction(q)
    if n_int == 0:
        return Fraction(2)
    previous, current = Fraction(2), t_q
    for _ in range(2, n_int + 1):
        previous, current = current, t_q * current - q_q * previous
    return current


def symmetric_character(m: object, t: object, q: object = 1) -> Fraction:
    """Return ``sum(alpha^(m-j)*beta^j, j=0..m)`` exactly."""

    m_int = _require_builtin_int(m, "m")
    if m_int < 0:
        raise ValueError("m must be nonnegative")
    t_q, q_q = Fraction(t), Fraction(q)
    if m_int == 0:
        return Fraction(1)
    previous, current = Fraction(1), t_q
    for _ in range(2, m_int + 1):
        previous, current = current, t_q * current - q_q * previous
    return current


def tensor_sym2_elementary(A: object, B: object, q: object) -> tuple[int, int, int]:
    """First three elementary coefficients of the unscaled weight-three tensor."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    q_int = _require_builtin_int(q, "q")
    if q_int == 0:
        raise ValueError("q must be nonzero")
    bracket = q_int * A_int * A_int + B_int**4 - 2 * q_int * B_int * B_int - 2 * q_int**2
    return (
        A_int * (B_int * B_int - q_int),
        q_int * (B_int * B_int - q_int) * (A_int * A_int + B_int * B_int - 3 * q_int),
        q_int**2 * A_int * bracket,
    )


def tensor_sym2_factor(A: object, B: object, q: object) -> tuple[int, ...]:
    e1, e2, e3 = tensor_sym2_elementary(A, B, q)
    q_int = _require_builtin_int(q, "q")
    return (1, -e1, e2, -e3, q_int**3 * e2, -(q_int**6) * e1, q_int**9)


def dilate_polynomial(coefficients: Sequence[int], scalar: object) -> tuple[int, ...]:
    scalar_int = _require_builtin_int(scalar, "scalar")
    return tuple(coefficient * scalar_int**degree for degree, coefficient in enumerate(coefficients))


def sym5_elementary(C: object, q: object) -> tuple[int, int, int]:
    C_int = _require_builtin_int(C, "C")
    q_int = _require_builtin_int(q, "q")
    if q_int == 0:
        raise ValueError("q must be nonzero")
    e1 = C_int * (C_int * C_int - q_int) * (C_int * C_int - 3 * q_int)
    e2 = q_int * int(symmetric_character(8, C_int, q_int)) + q_int**3 * int(
        symmetric_character(4, C_int, q_int)
    ) + q_int**5
    e3 = q_int**3 * int(symmetric_character(9, C_int, q_int)) + q_int**5 * int(
        symmetric_character(5, C_int, q_int)
    ) + q_int**6 * int(symmetric_character(3, C_int, q_int))
    return e1, e2, e3


def sym5_factor(C: object, q: object) -> tuple[int, ...]:
    e1, e2, e3 = sym5_elementary(C, q)
    q_int = _require_builtin_int(q, "q")
    return (1, -e1, e2, -e3, q_int**5 * e2, -(q_int**10) * e1, q_int**15)


def dilated_tensor_factor(A: object, B: object, q: object) -> tuple[int, ...]:
    """Return the typed weight-five factor ``P_tensor(q*T)``."""

    q_int = _require_builtin_int(q, "q")
    return dilate_polynomial(tensor_sym2_factor(A, B, q_int), q_int)


def rational_graph_predicate(A: object, B: object, C: object, q: object) -> bool:
    """Invariant form of the two complete rational graph alternatives."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    C_int = _require_builtin_int(C, "C")
    q_int = _require_builtin_int(q, "q")
    if q_int == 0:
        raise ValueError("q must be nonzero")
    graph_one = B_int * B_int == C_int * C_int and (
        q_int * A_int == C_int * (C_int * C_int - 3 * q_int)
    )
    graph_two = A_int == C_int and (
        q_int * B_int * B_int == (C_int * C_int - 2 * q_int) ** 2
    )
    return graph_one or graph_two


def graph_branches(A: object, B: object, C: object, q: object) -> list[dict[str, object]]:
    """Return signed graph incidences for integral traces at an odd prime power."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    C_int = _require_builtin_int(C, "C")
    q_int = _require_builtin_int(q, "q")
    _, exponent = prime_power_data(q_int)
    output: list[dict[str, object]] = []
    for epsilon in (-1, 1):
        if B_int == epsilon * C_int and q_int * A_int == C_int * (
            C_int * C_int - 3 * q_int
        ):
            output.append(
                {
                    "graph": "T3_then_Sym2",
                    "epsilon": epsilon,
                    "normalized_relation": "x=T3(z), y=epsilon*z",
                }
            )
    if exponent % 2 == 0:
        s = math.isqrt(q_int)
        for epsilon in (-1, 1):
            if A_int == C_int and s * B_int == epsilon * (
                C_int * C_int - 2 * q_int
            ):
                output.append(
                    {
                        "graph": "Std_then_T2",
                        "epsilon": epsilon,
                        "normalized_relation": "x=z, y=epsilon*T2(z)",
                    }
                )
    return output


def branch_two_nonsquare_obstruction(A: object, B: object, C: object, q: object) -> bool:
    """Prove-by-predicate that branch two has no integral nonsquare odd-q point."""

    A_int = _require_builtin_int(A, "A")
    B_int = _require_builtin_int(B, "B")
    C_int = _require_builtin_int(C, "C")
    q_int = _require_builtin_int(q, "q")
    _, exponent = prime_power_data(q_int)
    on_invariant_branch = A_int == C_int and q_int * B_int * B_int == (
        C_int * C_int - 2 * q_int
    ) ** 2
    if exponent % 2 == 0:
        return False
    if on_invariant_branch:
        raise ArithmeticError("nonsquare odd-prime-power branch-two obstruction failed")
    return True


# Sparse exact polynomial algebra in Q[x,y,z].  Lexicographic order is
# x > y > z.  This deliberately small engine replaces any runtime CAS.
Monomial = tuple[int, int, int]
Poly = dict[Monomial, Fraction]
ZERO_MONOMIAL: Monomial = (0, 0, 0)


def _poly_clean(poly: Mapping[Monomial, Fraction | int]) -> Poly:
    return {
        monomial: Fraction(coefficient)
        for monomial, coefficient in poly.items()
        if coefficient
    }


def _poly_term(monomial: Monomial, coefficient: Fraction | int = 1) -> Poly:
    coefficient_q = Fraction(coefficient)
    return {} if not coefficient_q else {monomial: coefficient_q}


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


def _poly_power(poly: Poly, exponent: int) -> Poly:
    if type(exponent) is not int or exponent < 0:
        raise ValueError("polynomial exponent must be a nonnegative built-in integer")
    output = _poly_term(ZERO_MONOMIAL)
    base = dict(poly)
    power = exponent
    while power:
        if power & 1:
            output = _poly_multiply(output, base)
        base = _poly_multiply(base, base)
        power //= 2
    return output


def _poly_leading(poly: Poly) -> tuple[Monomial, Fraction]:
    if not poly:
        raise ValueError("zero polynomial has no leading term")
    monomial = max(poly)
    return monomial, poly[monomial]


def _monomial_divides(divisor: Monomial, dividend: Monomial) -> bool:
    return all(left <= right for left, right in zip(divisor, dividend))


def _monomial_quotient(dividend: Monomial, divisor: Monomial) -> Monomial:
    if not _monomial_divides(divisor, dividend):
        raise ValueError("monomial division is not exact")
    return tuple(left - right for left, right in zip(dividend, divisor))


def _monomial_lcm(left: Monomial, right: Monomial) -> Monomial:
    return tuple(max(a, b) for a, b in zip(left, right))


def _poly_monic(poly: Poly) -> Poly:
    _, coefficient = _poly_leading(poly)
    return _poly_scale(poly, Fraction(1, 1) / coefficient)


def _poly_normal_form(
    poly: Poly,
    basis: Sequence[Poly],
    guard: ResourceGuard | None = None,
) -> Poly:
    working = dict(poly)
    remainder: Poly = {}
    while working:
        monomial, coefficient = _poly_leading(working)
        for divisor in basis:
            divisor_monomial, divisor_coefficient = _poly_leading(divisor)
            if _monomial_divides(divisor_monomial, monomial):
                quotient = _poly_term(
                    _monomial_quotient(monomial, divisor_monomial),
                    coefficient / divisor_coefficient,
                )
                working = _poly_add(
                    working, _poly_multiply(quotient, divisor), -1
                )
                if guard is not None:
                    guard.charge("exact_polynomial_leading_term_reductions")
                break
        else:
            leading_term = _poly_term(monomial, coefficient)
            remainder = _poly_add(remainder, leading_term)
            working = _poly_add(working, leading_term, -1)
    return remainder


def _s_polynomial(left: Poly, right: Poly) -> Poly:
    left_monomial, left_coefficient = _poly_leading(left)
    right_monomial, right_coefficient = _poly_leading(right)
    common = _monomial_lcm(left_monomial, right_monomial)
    left_multiplier = _poly_term(
        _monomial_quotient(common, left_monomial),
        Fraction(1, 1) / left_coefficient,
    )
    right_multiplier = _poly_term(
        _monomial_quotient(common, right_monomial),
        Fraction(1, 1) / right_coefficient,
    )
    return _poly_add(
        _poly_multiply(left_multiplier, left),
        _poly_multiply(right_multiplier, right),
        -1,
    )


def _reduced_groebner_basis(
    generators: Sequence[Poly], guard: ResourceGuard | None = None
) -> tuple[Poly, ...]:
    """Deterministic Buchberger replay followed by exact interreduction."""

    basis = [_poly_monic(generator) for generator in generators if generator]
    pairs = list(combinations(range(len(basis)), 2))
    while pairs:
        left_index, right_index = pairs.pop(0)
        if guard is not None:
            guard.charge("buchberger_s_pairs")
        remainder = _poly_normal_form(
            _s_polynomial(basis[left_index], basis[right_index]), basis, guard
        )
        if remainder:
            new_index = len(basis)
            basis.append(_poly_monic(remainder))
            pairs.extend((index, new_index) for index in range(new_index))

    minimal: list[Poly] = []
    for index, polynomial in enumerate(basis):
        leading, _ = _poly_leading(polynomial)
        redundant = False
        for other_index, other in enumerate(basis):
            if index == other_index:
                continue
            other_leading, _ = _poly_leading(other)
            if _monomial_divides(other_leading, leading) and (
                other_leading != leading or other_index < index
            ):
                redundant = True
                break
        if not redundant:
            minimal.append(polynomial)

    current = sorted(minimal, key=lambda item: _poly_leading(item)[0], reverse=True)
    for _ in range(4):
        reduced: list[Poly] = []
        for index, polynomial in enumerate(current):
            others = current[:index] + current[index + 1 :]
            remainder = _poly_normal_form(polynomial, others, guard)
            if not remainder:
                raise ArithmeticError("interreduction unexpectedly removed a minimal basis element")
            reduced.append(_poly_monic(remainder))
        reduced.sort(key=lambda item: _poly_leading(item)[0], reverse=True)
        if reduced == current:
            break
        current = reduced
    else:
        raise ArithmeticError("Groebner interreduction failed to stabilize")

    for left_index, right_index in combinations(range(len(current)), 2):
        remainder = _poly_normal_form(
            _s_polynomial(current[left_index], current[right_index]), current, guard
        )
        if remainder:
            raise ArithmeticError("Buchberger S-polynomial certificate failed")
    for generator in generators:
        if _poly_normal_form(generator, current, guard):
            raise ArithmeticError("an input ideal generator escaped the reduced basis")
    return tuple(current)


POLY_ONE = _poly_term(ZERO_MONOMIAL)
POLY_X = _poly_term((1, 0, 0))
POLY_Y = _poly_term((0, 1, 0))
POLY_Z = _poly_term((0, 0, 1))


def _poly_sum(*terms: tuple[int | Fraction, Poly]) -> Poly:
    output: Poly = {}
    for coefficient, polynomial in terms:
        output = _poly_add(output, polynomial, coefficient)
    return output


def coefficient_difference_generators() -> tuple[Poly, Poly, Poly]:
    """Return the normalized differences ``e_i(tensor)-e_i(Sym5)``."""

    x, y, z = POLY_X, POLY_Y, POLY_Z
    f1 = _poly_sum(
        (1, _poly_multiply(x, _poly_power(y, 2))),
        (-1, x),
        (-1, _poly_power(z, 5)),
        (4, _poly_power(z, 3)),
        (-3, z),
    )
    f2 = _poly_sum(
        (1, _poly_multiply(_poly_power(x, 2), _poly_power(y, 2))),
        (-1, _poly_power(x, 2)),
        (1, _poly_power(y, 4)),
        (-4, _poly_power(y, 2)),
        (-1, _poly_power(z, 8)),
        (7, _poly_power(z, 6)),
        (-16, _poly_power(z, 4)),
        (13, _poly_power(z, 2)),
    )
    f3 = _poly_sum(
        (1, _poly_power(x, 3)),
        (1, _poly_multiply(x, _poly_power(y, 4))),
        (-2, _poly_multiply(x, _poly_power(y, 2))),
        (-2, x),
        (-1, _poly_power(z, 9)),
        (8, _poly_power(z, 7)),
        (-22, _poly_power(z, 5)),
        (23, _poly_power(z, 3)),
        (-6, z),
    )
    return f1, f2, f3


def _p7_plus(variable: Poly) -> Poly:
    return _poly_sum(
        (1, _poly_power(variable, 3)),
        (1, _poly_power(variable, 2)),
        (-2, variable),
        (-1, POLY_ONE),
    )


def _p7_minus(variable: Poly) -> Poly:
    return _poly_sum(
        (1, _poly_power(variable, 3)),
        (-1, _poly_power(variable, 2)),
        (-2, variable),
        (1, POLY_ONE),
    )


def _c4(variable: Poly) -> Poly:
    return _poly_sum(
        (1, _poly_power(variable, 4)),
        (-4, _poly_power(variable, 2)),
        (2, POLY_ONE),
    )


def _generic_y_factor() -> Poly:
    y2_minus_z2 = _poly_add(_poly_power(POLY_Y, 2), _poly_power(POLY_Z, 2), -1)
    z2_minus_2 = _poly_add(_poly_power(POLY_Z, 2), _poly_scale(POLY_ONE, 2), -1)
    y2_minus_t2_squared = _poly_add(
        _poly_power(POLY_Y, 2), _poly_power(z2_minus_2, 2), -1
    )
    return _poly_multiply(y2_minus_z2, y2_minus_t2_squared)


def expected_main_groebner_basis() -> tuple[Poly, ...]:
    x, y, z = POLY_X, POLY_Y, POLY_Z
    g0 = _poly_sum(
        (1, _poly_power(x, 3)),
        (-3, x),
        (1, _poly_multiply(_poly_power(y, 2), _poly_power(z, 5))),
        (-4, _poly_multiply(_poly_power(y, 2), _poly_power(z, 3))),
        (3, _poly_multiply(_poly_power(y, 2), z)),
        (-1, _poly_power(z, 9)),
        (8, _poly_power(z, 7)),
        (-23, _poly_power(z, 5)),
        (27, _poly_power(z, 3)),
        (-9, z),
    )
    g1 = coefficient_difference_generators()[0]
    inner = _poly_sum(
        (1, _poly_multiply(x, _poly_power(z, 2))),
        (-1, x),
        (1, _poly_multiply(_poly_power(y, 4), _poly_power(z, 3))),
        (-2, _poly_multiply(_poly_power(y, 4), z)),
        (-1, _poly_multiply(_poly_power(y, 2), _poly_power(z, 7))),
        (5, _poly_multiply(_poly_power(y, 2), _poly_power(z, 5))),
        (-10, _poly_multiply(_poly_power(y, 2), _poly_power(z, 3))),
        (9, _poly_multiply(_poly_power(y, 2), z)),
        (1, _poly_power(z, 9)),
        (-6, _poly_power(z, 7)),
        (11, _poly_power(z, 5)),
        (-5, _poly_power(z, 3)),
        (-3, z),
    )
    g2 = _poly_multiply(
        _poly_add(_poly_power(z, 2), _poly_scale(POLY_ONE, 3), -1), inner
    )
    extra_y = _poly_sum(
        (1, _poly_power(y, 2)),
        (1, _poly_power(z, 4)),
        (-3, _poly_power(z, 2)),
        (-1, POLY_ONE),
    )
    generic = _generic_y_factor()
    g3 = _poly_multiply(generic, extra_y)
    g4 = _poly_multiply(
        generic, _poly_multiply(_p7_plus(z), _p7_minus(z))
    )
    return tuple(_poly_monic(item) for item in (g0, g1, g2, g3, g4))


def _poly_serialized(poly: Poly) -> list[list[int]]:
    return [
        [*monomial, coefficient.numerator, coefficient.denominator]
        for monomial, coefficient in sorted(poly.items(), reverse=True)
    ]


def _poly_substitute_y(poly: Poly, replacement: Poly) -> Poly:
    """Substitute a polynomial in ``z`` for ``y`` while retaining ``x,z``."""

    output: Poly = {}
    for (x_power, y_power, z_power), coefficient in poly.items():
        term = _poly_multiply(
            _poly_power(POLY_X, x_power),
            _poly_multiply(
                _poly_power(replacement, y_power), _poly_power(POLY_Z, z_power)
            ),
        )
        output = _poly_add(output, term, coefficient)
    return output


def _chebyshev_trace_poly(n: int) -> Poly:
    if type(n) is not int or n < 0:
        raise ValueError("trace-polynomial index must be nonnegative")
    if n == 0:
        return _poly_scale(POLY_ONE, 2)
    previous, current = _poly_scale(POLY_ONE, 2), POLY_Z
    for _ in range(2, n + 1):
        previous, current = current, _poly_add(
            _poly_multiply(POLY_Z, current), previous, -1
        )
    return current


def specialization_residuals() -> dict[str, Poly]:
    """Exact branch factorizations used in the rational case split."""

    f1, f2, f3 = coefficient_difference_generators()
    x, z = POLY_X, POLY_Z
    z2_minus_1 = _poly_add(_poly_power(z, 2), POLY_ONE, -1)
    z2_minus_3 = _poly_add(_poly_power(z, 2), _poly_scale(POLY_ONE, 3), -1)
    t3 = _poly_sum((1, _poly_power(z, 3)), (-3, z))
    t2 = _poly_sum((1, _poly_power(z, 2)), (-2, POLY_ONE))
    x_minus_t3 = _poly_add(x, t3, -1)
    x_plus_t3 = _poly_add(x, t3)
    x_minus_z = _poly_add(x, z, -1)
    x_plus_z = _poly_add(x, z)

    first_third_cofactor = _poly_sum(
        (1, _poly_power(x, 2)),
        (1, _poly_multiply(x, _poly_power(z, 3))),
        (-3, _poly_multiply(x, z)),
        (1, _poly_power(z, 6)),
        (-5, _poly_power(z, 4)),
        (7, _poly_power(z, 2)),
        (-2, POLY_ONE),
    )
    second_third_cofactor = _poly_sum(
        (1, _poly_power(x, 2)),
        (1, _poly_multiply(x, z)),
        (1, _poly_power(z, 8)),
        (-8, _poly_power(z, 6)),
        (22, _poly_power(z, 4)),
        (-23, _poly_power(z, 2)),
        (6, POLY_ONE),
    )
    first_expected = (
        _poly_multiply(z2_minus_1, x_minus_t3),
        _poly_multiply(
            z2_minus_1, _poly_multiply(x_minus_t3, x_plus_t3)
        ),
        _poly_multiply(x_minus_t3, first_third_cofactor),
    )
    second_expected = (
        _poly_multiply(
            x_minus_z, _poly_multiply(z2_minus_1, z2_minus_3)
        ),
        _poly_multiply(
            _poly_multiply(x_minus_z, x_plus_z),
            _poly_multiply(z2_minus_1, z2_minus_3),
        ),
        _poly_multiply(x_minus_z, second_third_cofactor),
    )
    residuals: dict[str, Poly] = {}
    for sign, replacement in (("plus", z), ("minus", _poly_scale(z, -1))):
        for index, (generator, expected) in enumerate(
            zip((f1, f2, f3), first_expected), 1
        ):
            residuals[f"y_{sign}_z_f{index}"] = _poly_add(
                _poly_substitute_y(generator, replacement), expected, -1
            )
    for sign, replacement in (("plus", t2), ("minus", _poly_scale(t2, -1))):
        for index, (generator, expected) in enumerate(
            zip((f1, f2, f3), second_expected), 1
        ):
            residuals[f"y_{sign}_T2_f{index}"] = _poly_add(
                _poly_substitute_y(generator, replacement), expected, -1
            )
    return residuals


def groebner_and_torsion_certificate(
    guard: ResourceGuard | None = None,
) -> dict[str, object]:
    """Recompute the exact ideals and finite cyclotomic residuals."""

    generators = coefficient_difference_generators()
    main_basis = _reduced_groebner_basis(generators, guard)
    expected_main = expected_main_groebner_basis()
    if main_basis != expected_main:
        raise ArithmeticError("main reduced Groebner basis changed")

    y_trace_product = _poly_multiply(_p7_plus(POLY_Y), _p7_minus(POLY_Y))
    plus_expected = (
        _poly_add(POLY_X, _c4(POLY_Y), -1),
        y_trace_product,
        _p7_plus(POLY_Z),
    )
    minus_expected = (
        _poly_add(POLY_X, _c4(POLY_Y)),
        y_trace_product,
        _p7_minus(POLY_Z),
    )
    z2_minus_3 = _poly_add(
        _poly_power(POLY_Z, 2), _poly_scale(POLY_ONE, 3), -1
    )
    order12_expected = (
        _poly_sum((1, _poly_power(POLY_X, 3)), (-3, POLY_X)),
        _poly_sum(
            (1, _poly_multiply(POLY_X, _poly_power(POLY_Y, 2))),
            (-1, POLY_X),
        ),
        _poly_sum(
            (1, _poly_power(POLY_Y, 4)),
            (-4, _poly_power(POLY_Y, 2)),
            (3, POLY_ONE),
        ),
        z2_minus_3,
    )
    restricted = {
        "order_7_target": _reduced_groebner_basis(
            (*generators, _p7_plus(POLY_Z)), guard
        ),
        "order_14_target": _reduced_groebner_basis(
            (*generators, _p7_minus(POLY_Z)), guard
        ),
        "order_12_target": _reduced_groebner_basis(
            (*generators, z2_minus_3), guard
        ),
    }
    expected_restricted = {
        "order_7_target": plus_expected,
        "order_14_target": minus_expected,
        "order_12_target": order12_expected,
    }
    for name, basis in restricted.items():
        expected = tuple(_poly_monic(item) for item in expected_restricted[name])
        if basis != expected:
            raise ArithmeticError(f"{name} reduced Groebner basis changed")

    trace7 = _chebyshev_trace_poly(7)
    order7_factor_residual = _poly_add(
        _poly_add(trace7, _poly_scale(POLY_ONE, 2), -1),
        _poly_multiply(
            _poly_add(POLY_Z, _poly_scale(POLY_ONE, 2), -1),
            _poly_power(_p7_plus(POLY_Z), 2),
        ),
        -1,
    )
    order14_factor_residual = _poly_add(
        _poly_add(trace7, _poly_scale(POLY_ONE, 2)),
        _poly_multiply(
            _poly_add(POLY_Z, _poly_scale(POLY_ONE, 2)),
            _poly_power(_p7_minus(POLY_Z), 2),
        ),
        -1,
    )
    specializations = specialization_residuals()
    if order7_factor_residual or order14_factor_residual or any(specializations.values()):
        raise ArithmeticError("torsion or branch factor certificate failed")

    if any(
        value == 0
        for value in (
            1**3 + 1**2 - 2 * 1 - 1,
            (-1) ** 3 + (-1) ** 2 - 2 * (-1) - 1,
            1**3 - 1**2 - 2 * 1 + 1,
            (-1) ** 3 - (-1) ** 2 - 2 * (-1) + 1,
        )
    ):
        raise ArithmeticError("rational-root exclusion for trace cubics failed")

    return {
        "variable_order": "lexicographic x>y>z",
        "input_generators": [_poly_serialized(poly) for poly in generators],
        "main_reduced_basis": [_poly_serialized(poly) for poly in main_basis],
        "main_leading_monomials": [list(_poly_leading(poly)[0]) for poly in main_basis],
        "elimination_factors": {
            "generic_y_factor": "(y^2-z^2)*(y^2-(z^2-2)^2)",
            "order_7_trace_polynomial": "p7+(z)=z^3+z^2-2z-1",
            "order_14_trace_polynomial": "p7-(z)=z^3-z^2-2z+1",
            "basis_product": "generic_y_factor*p7+(z)*p7-(z)",
        },
        "restricted_reduced_bases": {
            name: [_poly_serialized(poly) for poly in basis]
            for name, basis in restricted.items()
        },
        "order_7_trace_identity": "C7(z)-2=(z-2)*p7+(z)^2",
        "order_14_trace_identity": "C7(z)+2=(z+2)*p7-(z)^2",
        "branch_specialization_zero_residual_count": len(specializations),
        "all_branch_specialization_residuals_zero": True,
        "algebraic_residuals": {
            "order_12": {
                "target": "z^2=3",
                "complete_solution_over_algebraic_closure": "y^2=3,x=0 (graph 1), or y^2=1,x in {z,0,-z}; x=z is graph 2 and x=0,-z are the extra points",
                "extra_points": "z^2=3, y^2=1, x=0 or x=-z",
            },
            "order_7": {
                "target": "p7+(z)=0",
                "complete_restricted_ideal": "p7+(z)=0, p7+(y)*p7-(y)=0, x=C4(y)",
            },
            "order_14": {
                "target": "p7-(z)=0",
                "complete_restricted_ideal": "p7-(z)=0, p7+(y)*p7-(y)=0, x=-C4(y)",
            },
        },
        "no_rational_raw_trace_certificate": {
            "orders_7_14": "z=C/s lies in Q(s), of degree at most 2 over Q, but each p7+/- is an irreducible cubic by the rational-root test; impossible",
            "order_12": "z^2=3 and y^2=1 imply C^2=3q and B^2=q, hence (C/B)^2=3 with nonzero rational C/B; impossible",
        },
        "runtime_symbolic_packages": 0,
        "method": "custom sparse Fraction polynomial arithmetic, deterministic Buchberger replay, interreduction, exact S-polynomial checks, and zero reduction of every input generator",
    }


def _trace_poly(variable: Poly, n: int) -> Poly:
    if type(n) is not int or n < 0:
        raise ValueError("trace-polynomial index must be nonnegative")
    if n == 0:
        return _poly_scale(POLY_ONE, 2)
    previous, current = _poly_scale(POLY_ONE, 2), variable
    for _ in range(2, n + 1):
        previous, current = current, _poly_add(
            _poly_multiply(variable, current), previous, -1
        )
    return current


def _newton_elementaries(power_sums: Sequence[Poly]) -> tuple[Poly, ...]:
    elementaries = [POLY_ONE]
    for degree in range(1, len(power_sums) + 1):
        numerator: Poly = {}
        for index in range(1, degree + 1):
            numerator = _poly_add(
                numerator,
                _poly_multiply(elementaries[degree - index], power_sums[index - 1]),
                1 if index % 2 else -1,
            )
        elementaries.append(_poly_scale(numerator, Fraction(1, degree)))
    return tuple(elementaries[1:])


def coefficient_identity_residuals() -> dict[str, Poly]:
    """Independent Newton derivations of all normalized load-bearing formulas."""

    tensor_power_sums = [
        _poly_multiply(
            _trace_poly(POLY_X, n),
            _poly_add(_trace_poly(POLY_Y, 2 * n), POLY_ONE),
        )
        for n in range(1, 4)
    ]
    target_power_sums = [
        _poly_sum(
            (1, _trace_poly(POLY_Z, 5 * n)),
            (1, _trace_poly(POLY_Z, 3 * n)),
            (1, _trace_poly(POLY_Z, n)),
        )
        for n in range(1, 4)
    ]
    tensor_newton = _newton_elementaries(tensor_power_sums)
    target_newton = _newton_elementaries(target_power_sums)
    tensor_closed = (
        _poly_sum(
            (1, _poly_multiply(POLY_X, _poly_power(POLY_Y, 2))),
            (-1, POLY_X),
        ),
        _poly_sum(
            (1, _poly_multiply(_poly_power(POLY_X, 2), _poly_power(POLY_Y, 2))),
            (-1, _poly_power(POLY_X, 2)),
            (1, _poly_power(POLY_Y, 4)),
            (-4, _poly_power(POLY_Y, 2)),
            (3, POLY_ONE),
        ),
        _poly_sum(
            (1, _poly_power(POLY_X, 3)),
            (1, _poly_multiply(POLY_X, _poly_power(POLY_Y, 4))),
            (-2, _poly_multiply(POLY_X, _poly_power(POLY_Y, 2))),
            (-2, POLY_X),
        ),
    )
    target_closed = (
        _poly_sum(
            (1, _poly_power(POLY_Z, 5)),
            (-4, _poly_power(POLY_Z, 3)),
            (3, POLY_Z),
        ),
        _poly_sum(
            (1, _poly_power(POLY_Z, 8)),
            (-7, _poly_power(POLY_Z, 6)),
            (16, _poly_power(POLY_Z, 4)),
            (-13, _poly_power(POLY_Z, 2)),
            (3, POLY_ONE),
        ),
        _poly_sum(
            (1, _poly_power(POLY_Z, 9)),
            (-8, _poly_power(POLY_Z, 7)),
            (22, _poly_power(POLY_Z, 5)),
            (-23, _poly_power(POLY_Z, 3)),
            (6, POLY_Z),
        ),
    )
    residuals = {}
    for index, (derived, closed) in enumerate(zip(tensor_newton, tensor_closed), 1):
        residuals[f"tensor_e{index}_newton_minus_closed"] = _poly_add(
            derived, closed, -1
        )
    for index, (derived, closed) in enumerate(zip(target_newton, target_closed), 1):
        residuals[f"sym5_e{index}_newton_minus_closed"] = _poly_add(
            derived, closed, -1
        )
    return residuals


def ladder_weight_certificate(r: object) -> dict[str, object]:
    """Exact all-r normalized torus weight-union identity."""

    r_int = _require_builtin_int(r, "r")
    if r_int < 1:
        raise ValueError("r must be positive")
    target = sorted(range(-(2 * r_int + 1), 2 * r_int + 2, 2))
    first = sorted(
        epsilon * (r_int + 1) + r_int - 2 * j
        for epsilon in (-1, 1)
        for j in range(r_int + 1)
    )
    second = sorted(
        epsilon + 2 * (r_int - 2 * j)
        for epsilon in (-1, 1)
        for j in range(r_int + 1)
    )
    if first != target or second != target:
        raise ArithmeticError("universal tensor/symmetric-power ladder identity failed")
    return {
        "r": r_int,
        "target_weights": target,
        "Std(w^(r+1))_tensor_Symr(w)_weights": first,
        "Std(w)_tensor_Symr(w^2)_weights": second,
    }


def _su2_invariant_moment(highest_weight: int, tensor_power: int) -> int:
    if type(highest_weight) is not int or highest_weight < 0:
        raise ValueError("highest weight must be nonnegative")
    if type(tensor_power) is not int or tensor_power < 0:
        raise ValueError("tensor power must be nonnegative")
    multiplicities = {0: 1}
    for _ in range(tensor_power):
        next_multiplicities: dict[int, int] = defaultdict(int)
        for existing, multiplicity in multiplicities.items():
            for output in range(
                abs(existing - highest_weight), existing + highest_weight + 1, 2
            ):
                next_multiplicities[output] += multiplicity
        multiplicities = dict(next_multiplicities)
    return multiplicities.get(0, 0)


def compact_trace_moments(max_degree: object = 8) -> dict[str, list[int]]:
    max_degree_int = _require_builtin_int(max_degree, "max_degree")
    if max_degree_int < 0 or max_degree_int > 12:
        raise ValueError("max_degree must lie between 0 and 12")
    std = [_su2_invariant_moment(1, n) for n in range(max_degree_int + 1)]
    sym2 = [_su2_invariant_moment(2, n) for n in range(max_degree_int + 1)]
    product = [left * right for left, right in zip(std, sym2)]
    sym5 = [_su2_invariant_moment(5, n) for n in range(max_degree_int + 1)]
    output = {
        "degrees": list(range(max_degree_int + 1)),
        "Std_SU2_tensor_Sym2_SU2_independent_product": product,
        "Sym5_SU2": sym5,
    }
    if max_degree_int >= 6:
        if product[:5] != sym5[:5] or (product[6], sym5[6]) != (75, 111):
            raise ArithmeticError("compact moment separation certificate failed")
    return output


def _is_odd_prime(p: int) -> bool:
    if type(p) is not int or p < 3 or p % 2 == 0:
        return False
    return all(p % divisor for divisor in range(3, math.isqrt(p) + 1, 2))


def hasse_lattice_count_theorem(p: object, exponent: object) -> dict[str, object]:
    """Exact count of integral Hasse triples on the two rational branches."""

    p_int = _require_builtin_int(p, "p")
    exponent_int = _require_builtin_int(exponent, "exponent")
    if not _is_odd_prime(p_int):
        raise ValueError("p must be an odd prime")
    if exponent_int < 1:
        raise ValueError("exponent must be positive")
    q = p_int**exponent_int
    hasse_bound = math.isqrt(4 * q)
    divisor_exponent = (exponent_int + 2) // 3
    positive_parameters = hasse_bound // (p_int**divisor_exponent)
    branch_one = 4 * positive_parameters + 1
    if exponent_int % 2:
        branch_two = 0
        overlap = 0
        union = branch_one
        square_closed_form = None
    else:
        k = exponent_int // 2
        branch_two = 8 * p_int ** (k // 2) + 2
        overlap = 4
        union = branch_one + branch_two - overlap
        square_closed_form = (
            8 * p_int ** (k // 3) + 8 * p_int ** (k // 2) - 1
        )
        if union != square_closed_form:
            raise ArithmeticError("square-q closed lattice count failed")
    return {
        "p": p_int,
        "exponent": exponent_int,
        "q": q,
        "H=floor(2*sqrt(q))": hasse_bound,
        "d=ceil(exponent/3)": divisor_exponent,
        "h=floor(H/p^d)": positive_parameters,
        "branch_one_distinct_triples": branch_one,
        "branch_two_distinct_triples": branch_two,
        "branch_overlap_distinct_triples": overlap,
        "union_distinct_triples": union,
        "square_q_closed_form": square_closed_form,
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
    hits = []
    triples_checked = 0
    for A in traces:
        for B in traces:
            for C in traces:
                triples_checked += 1
                if locked:
                    guard.charge_locked_triple()
                else:
                    guard.charge("synthetic_hasse_trace_triples")
                factor_equal = dilated_tensor_factor(A, B, q) == sym5_factor(C, q)
                predicted = rational_graph_predicate(A, B, C, q)
                if factor_equal != predicted:
                    raise ArithmeticError(
                        f"rational classification replay failed at {(q, A, B, C)}"
                    )
                if factor_equal:
                    member_weight = None
                    if histogram is not None:
                        member_weight = histogram[A] * histogram[B] * histogram[C]
                    hits.append(
                        {
                            "A": A,
                            "B": B,
                            "C": C,
                            "member_weight": member_weight,
                            "branches": graph_branches(A, B, C, q),
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
) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = genus1.get("finite_regressions")
    if not isinstance(rows, list):
        raise RuntimeError("locked finite rows are malformed")
    frozen = []
    for row in rows:
        if not isinstance(row, dict):
            raise RuntimeError("locked finite row is malformed")
        q = row.get("q")
        if type(q) is not int:
            raise RuntimeError("locked q is malformed")
        histogram = _trace_histogram(row)
        traces = sorted(histogram)
        replay = _enumerate_trace_triples(
            q, traces, histogram, guard, locked=True
        )
        p, exponent = prime_power_data(q)
        count_theorem = hasse_lattice_count_theorem(p, exponent)
        if replay["factor_equal_trace_triple_count"] != count_theorem[
            "union_distinct_triples"
        ]:
            raise ArithmeticError("locked Hasse support count disagrees with theorem")
        replay["all_q_lattice_count_specialization"] = count_theorem
        frozen.append(replay)
    if tuple(row["q"] for row in frozen) != FROZEN_Q_VALUES:
        raise RuntimeError("frozen replay q sequence changed")
    if guard.locked_triples != LOCKED_TRIPLE_CAP_INCLUSIVE:
        raise ArithmeticError("locked triple total changed")

    s = math.isqrt(SYNTHETIC_Q)
    synthetic_traces = list(range(-2 * s, 2 * s + 1))
    synthetic = _enumerate_trace_triples(
        SYNTHETIC_Q, synthetic_traces, None, guard, locked=False
    )
    theorem = hasse_lattice_count_theorem(3, 2)
    if synthetic["factor_equal_trace_triple_count"] != theorem[
        "union_distinct_triples"
    ]:
        raise ArithmeticError("synthetic q=9 count disagrees with theorem")
    synthetic["all_q_lattice_count_specialization"] = theorem
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

    coefficient_residuals = coefficient_identity_residuals()
    if any(coefficient_residuals.values()):
        raise ArithmeticError("normalized Newton coefficient identity failed")
    guard.charge("normalized_Newton_coefficient_certificates", len(coefficient_residuals))

    algebra = groebner_and_torsion_certificate(guard)
    ladder_rows = [
        ladder_weight_certificate(r) for r in range(1, LADDER_REGRESSION_MAX_R + 1)
    ]
    guard.charge("universal_ladder_bounded_weight_unions", len(ladder_rows))
    moments = compact_trace_moments(8)
    guard.charge("compact_representation_moments", len(moments["degrees"]) * 2)
    frozen, synthetic = frozen_and_synthetic_replay(sources["genus1"], guard)

    expected_counts = {3: 5, 5: 1, 7: 1, 11: 1, 13: 1}
    expected_weights = {
        3: 80,
        5: 8_000,
        7: 74_088,
        11: 10_648_000,
        13: 3_796_416,
    }
    for row in frozen:
        q = row["q"]
        if row["factor_equal_trace_triple_count"] != expected_counts[q]:
            raise ArithmeticError("locked intersection support count changed")
        if row["factor_equal_member_weight"] != expected_weights[q]:
            raise ArithmeticError("locked intersection member weight changed")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_tensor_sym2_sym5_spectral_intersection.v1",
        "packet_id": "FUNCTION_FIELD.ELLIPTIC.TENSOR_SYM2.SYM5.SPECTRAL_INTERSECTION.V1",
        "status": "EXACT_RATIONAL_COMPLETE_FACTOR_INTERSECTION_ALL_M_TORUS_LADDER_AND_CYCLOTOMIC_RESIDUALS",
        "rigor_level": {
            "raw_coefficient_formulas": "PROVED_BY_INDEPENDENT_EXACT_NEWTON_POWER_SUM_DERIVATIONS",
            "rational_complete_intersection": "PROVED_BY_AN_EXACT_REDUCED_GROEBNER_BASIS_AND_RATIONAL_CASE_SPLIT",
            "algebraic_residuals": "PROVED_BY_RESTRICTED_REDUCED_GROEBNER_BASES_AND_CYCLOTOMIC_TRACE_IDENTITIES",
            "odd_prime_power_lattice_counts": "PROVED_BY_P_ADIC_DIVISIBILITY_PARAMETERIZATIONS_AND_EXACT_OVERLAP_COUNT",
            "all_m_ladder": "PROVED_FOR_EVERY_R_BY_TWO_EXPLICIT_WEIGHT_UNIONS; BOUNDED ROWS ARE REGRESSION_ONLY",
            "compact_moments": "PROVED_BY_CLEBSCH_GORDAN_MULTIPLICITIES",
            "locked_replay": "EXACT_FOR_ALL_7975_ORDERED_TRACE_TRIPLES_IN_THE_FIVE_LOCKED_SUPPORTS",
            "global_correspondence_automorphy_and_novelty": "NOT_INFERRED",
        },
        "conventions": {
            "three_base_factors": "P_t(T)=1-t*T+q*T^2 for geometric traces t=A,B,C",
            "normalized_traces": "x=A/s, y=B/s, z=C/s after choosing s with s^2=q",
            "tensor_construction": "Std(E_A) tensor Sym^2(E_B), degree 6 and weight 3",
            "target_construction": "Sym^5(E_C), degree 6 and weight 5",
            "typed_raw_identity": "P_(A tensor Sym2(B))(q*T)=P_(Sym5(C))(T)",
            "sign_rule": "B -> -B does not change Sym^2(E_B), producing the +/- y branches; A and C retain their geometric trace signs",
            "unscaled_firewall": "P_tensor(T) and P_Sym5(T) have different weights and are not compared without the displayed q dilation",
        },
        "exact_coefficient_identities": {
            "normalized_tensor": {
                "e1": "x*(y^2-1)",
                "e2": "(y^2-1)*(x^2+y^2-3)",
                "e3": "x*(x^2+y^4-2*y^2-2)",
            },
            "normalized_sym5": {
                "e1": "z*(z^2-1)*(z^2-3)",
                "e2": "(z^2-1)*(z^2-3)*(z^2-z-1)*(z^2+z-1)",
                "e3": "z*(z^2-3)*(z^2-2)*(z^2-z-1)*(z^2+z-1)",
            },
            "raw_tensor_before_dilation": {
                "e1": "A*(B^2-q)",
                "e2": "q*(B^2-q)*(A^2+B^2-3q)",
                "e3": "q^2*A*(q*A^2+B^4-2q*B^2-2q^2)",
                "factor": "[1,-e1,e2,-e3,q^3*e2,-q^6*e1,q^9]",
            },
            "raw_tensor_after_q_dilation": {
                "d1": "q*A*(B^2-q)",
                "d2": "q^3*(B^2-q)*(A^2+B^2-3q)",
                "d3": "q^5*A*(q*A^2+B^4-2q*B^2-2q^2)",
                "factor": "[1,-d1,d2,-d3,q^5*d2,-q^10*d1,q^15]",
            },
            "sym5_plethystic_cross_check": {
                "e1": "E5(C,q)",
                "e2": "q*E8(C,q)+q^3*E4(C,q)+q^5",
                "e3": "q^3*E9(C,q)+q^5*E5(C,q)+q^6*E3(C,q)",
            },
            "Newton_zero_residual_count": len(coefficient_residuals),
            "all_Newton_residuals_zero": True,
        },
        "complete_rational_intersection_theorem": {
            "scope": "A,B,C,q in Q with q nonzero; equivalently the formal factors defined by the displayed trace formulas",
            "normalized_statement": "factor equality iff [x=T3(z)=z^3-3z and y=+/-z] or [x=z and y=+/-T2(z)=+/-(z^2-2)]",
            "raw_invariant_statement": "factor equality iff [B^2=C^2 and q*A=C*(C^2-3q)] or [A=C and q*B^2=(C^2-2q)^2]",
            "graph_one_spectral_weights": "u=w^3, v=+/-w gives {u^+/-1*v^(2,0,-2)}={w^+/-1,w^+/-3,w^+/-5}",
            "graph_two_spectral_weights": "u=w, v^2=w^4 gives {u^+/-1*v^(2,0,-2)}={w^+/-1,w^+/-3,w^+/-5}",
            "proof": [
                "the three coefficient differences generate the certified ideal I",
                "the reduced lex basis contains generic_y_factor*p7+(z)*p7-(z)",
                "z=C/s lies in Q(s) of degree at most two, so the irreducible cubic trace equations p7+/-(z)=0 exclude the non-generic alternative for rational raw data",
                "on y^2=z^2, the exact specializations leave x=T3(z), with z^2=1 overlap absorbed by graph two",
                "on y^2=(z^2-2)^2, the exact specializations leave x=z; z^2=1 is graph-one overlap and z^2=3 is irrational",
                "the order-12 restricted ideal supplies the only remaining x values, and its extra points cannot have rational raw traces",
            ],
            "no_search_dependency": "the 7975-triple and q=9 replays are regressions; the theorem is the exact ideal and rational exclusion argument",
        },
        "exact_algebraic_certificate": algebra,
        "odd_prime_power_integral_theorem": {
            "scope": "q=p^e for odd prime p, e>=1, and integral A,B,C in the Hasse interval",
            "same_two_branches": "the rational theorem applies; the algebraic order 7,12,14 residuals have no rational raw traces",
            "branch_one_integrality": "q*A=C*(C^2-3q) is integral iff q divides C^3, equivalently p^ceil(e/3) divides C",
            "branch_one_hasse_reason": "A/s=T3(C/s), and T3 maps the compact SU(2) trace interval [-2,2] to itself",
            "branch_one_count": "with H=floor(2sqrt(q)), d=ceil(e/3), h=floor(H/p^d), the distinct (A,B,C) count is 4h+1",
            "branch_two_nonsquare_obstruction": "if e is odd, v_p(q*B^2) is odd while v_p((C^2-2q)^2) is even; the zero fallback C^2=2q is impossible for odd q",
            "branch_two_square_parameterization": "for e=2k, C=p^ceil(k/2)*m with |m|<=2p^floor(k/2), A=C, and p^k*B=+/-(C^2-2q); the branch count is 8p^floor(k/2)+2",
            "square_branch_overlap": "exactly C=A=+/-2p^k and B=+/-2p^k, giving four triples",
            "square_q_union_count": "8p^floor(k/3)+8p^floor(k/2)-1 for q=p^(2k)",
            "count_examples": [
                hasse_lattice_count_theorem(3, 1),
                hasse_lattice_count_theorem(5, 1),
                hasse_lattice_count_theorem(3, 2),
                hasse_lattice_count_theorem(3, 4),
                hasse_lattice_count_theorem(5, 6),
            ],
            "realizability_firewall": "integral Hasse triples are coefficient-lattice points; no Waterhouse, curve existence, or relation among three curves is inferred",
        },
        "universal_tensor_symmetric_power_ladder": {
            "scope": "every integer r>=1 on a normalized characteristic-zero torus",
            "first_identity": "Std(w^(r+1)) tensor Sym^r(w) has the Sym^(2r+1)(w) weight multiset",
            "first_weight_union": "+(r+1)+{r,r-2,...,-r}={2r+1,...,1}; -(r+1)+{r,r-2,...,-r}={-1,...,-(2r+1)}",
            "second_identity": "Std(w) tensor Sym^r(w^2) has the Sym^(2r+1)(w) weight multiset",
            "second_weight_union": "+1+2{r,r-2,...,-r} and -1+2{r,r-2,...,-r} interlace to every odd weight from -(2r+1) to 2r+1",
            "raw_dilation": "the tensor side has weight r+1 and the target weight 2r+1, so T -> q^(r/2)*T; for odd r this requires a chosen sqrt(q), while r=2 gives the clean q*T identity",
            "classification_boundary": "these are universal sufficient spectral loci; only r=2 is completely classified in this packet",
            "bounded_regression": {
                "maximum_r": LADDER_REGRESSION_MAX_R,
                "rows": ladder_rows,
            },
        },
        "compact_trace_moment_fingerprint": {
            **moments,
            "first_product_vs_Sym5_separation": "degree 6: 75 versus 111",
            "generic_USp6_standard_degrees_0_through_6": [1, 0, 1, 0, 3, 0, 15],
            "generic_separation": "both thin constructions have fourth moment 6, versus 3 for generic USp(6)",
            "interpretation": "full coefficient support sees the explicit graph intersection; trace moments alone do not distinguish the two thin compact images before degree six",
        },
        "locked_trace_triple_replay": {
            "families": frozen,
            "aggregate": {
                "q_values": list(FROZEN_Q_VALUES),
                "ordered_trace_triples_checked": sum(
                    row["ordered_trace_triples_checked"] for row in frozen
                ),
                "factor_equal_trace_triple_count": sum(
                    row["factor_equal_trace_triple_count"] for row in frozen
                ),
            },
            "source_measure": "three independent ordered draws from the same uniform marked-cubic model trace histogram",
        },
        "synthetic_q9_hasse_replay": {
            **synthetic,
            "purpose": "nonvacuous exact replay of both rational branches and their four-point overlap",
            "realizability_status": "NOT_TESTED_OR_INFERRED",
        },
        "source_and_file_locks": {
            "source_locks": _source_lock_payload(),
            "owned_file_locks": _owned_file_locks(),
            "authentication": "each source JSON is schema-, payload-, canonical-payload-, and LF-file-locked; each source producer is LF-file-locked",
        },
        "resource_contract": {
            "locked_trace_triple_cap_inclusive": guard.triple_cap,
            "actual_locked_trace_triples": guard.locked_triples,
            "exclusive_accounted_work_unit_cap": guard.work_cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total_work,
            },
            "unit_definition": "one replayed trace triple, one exact leading-term reduction, one Buchberger S-pair, or one named small certificate; not CPU instructions",
            "field_curve_or_model_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "runtime_symbolic_packages": 0,
            "maximum_polynomial_total_degree": 12,
        },
        "scope_firewall": {
            "no_unscaled_identity": "different weights require the displayed q dilation for r=2; the unscaled Euler factors are not equal",
            "no_representation_homomorphism": "a maximal-torus weight coincidence on two graph loci does not define a homomorphism identifying the two source representations",
            "no_local_to_global_upgrade": "one-place complete-factor equality supplies no motive, correspondence, compatible system, Euler product, or automorphic transfer",
            "no_realizability_claim": "Hasse-lattice points are not renamed elliptic curves or linked triples of curves",
            "no_moment_origin_recovery": "matching finitely many trace moments does not recover arithmetic origin or monodromy",
            "no_novelty_priority_claim": "Chebyshev identities may be classical; the exact rigidity and residual packaging are recorded without a literature-priority claim",
            "no_RH_or_GRH_claim": "finite local spectral intersections imply no analytic continuation, zero-free region, RH, or GRH statement",
        },
        "next_targets": [
            "prove or refute generic completeness of the two torus graphs for every r and classify their cyclotomic residuals",
            "determine whether a geometric family can enforce either r=2 graph coherently across primes",
            "classify Waterhouse realization of the exact Hasse triples without confusing separate local isogeny classes with a correspondence",
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
