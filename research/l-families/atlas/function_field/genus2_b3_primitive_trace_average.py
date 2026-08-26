#!/usr/bin/env python3
"""Exact all-field proof of the genus-two B3 primitive trace average.

For every odd prime power q, this producer evaluates the 23 factor signatures
in the expansion of

    sum_(D in H_5(q)) b_D^3,

without enumerating a finite field or a family member.  Its only arithmetic
engine is exact polynomial algebra over Q.  The primitive conductor-degree
four and six coefficients are averaged by finite sign inventories and
Newton's identities.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import time
import unicodedata
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

Polynomial = tuple[Fraction, ...]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_b3_primitive_trace_average.json"
NOTE_PATH = HERE / "GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_b3_primitive_trace_average.py"

HIGH_WEIGHT_FIXTURE_PATH = HERE / "genus2_high_weight_channel_probe.json"
MOMENT_NOTE_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"
STACK_ADAPTER_PATH = HERE / "GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md"

EXPECTED_HIGH_WEIGHT_PAYLOAD_SHA256 = (
    "90820eded366af5c430df6712bb51f6ad7882faf7bd27c4665c411052c1dca0e"
)
EXPECTED_DEPENDENCY_LF_SHA256 = {
    "high_weight_fixture": "bfa4aaca81a755ee9d02d2ae3741b0c511f91899a75adf85ada00007612f9541",
    "moment_note": "69272720e27f9630220be0fc083cd16bb22a94c73b57b466740aa4b77dcc6277",
    "stack_adapter": "f6f3c5ff0d112bd3204b1843a6f13b286d642a9c6ee19329a63eb39e06165e1c",
}

MAX_SIGNATURES = 23
MAX_PRIMITIVE_TYPES = 7
MAX_SYMBOLIC_OPERATIONS = 4096
MAX_WALL_SECONDS = 5.0

Q: Polynomial = (Fraction(0), Fraction(1))
ONE: Polynomial = (Fraction(1),)
ZERO: Polynomial = (Fraction(0),)


@dataclass
class AlgebraGuard:
    """Cap complete-polynomial operations, not scalar coefficient products."""

    deadline: float
    operations: int = 0

    def tick(self, amount: int = 1) -> None:
        self.operations += amount
        if self.operations > MAX_SYMBOLIC_OPERATIONS:
            raise RuntimeError("exact symbolic-operation cap exceeded")
        if time.monotonic() > self.deadline:
            raise RuntimeError("exact symbolic wall-time cap exceeded")


def _clean(values: Sequence[Fraction | int]) -> Polynomial:
    result = [Fraction(value) for value in values]
    while len(result) > 1 and not result[-1]:
        result.pop()
    return tuple(result) if result else ZERO


def _constant(value: Fraction | int) -> Polynomial:
    return (Fraction(value),)


def _add(left: Polynomial, right: Polynomial, guard: AlgebraGuard) -> Polynomial:
    guard.tick()
    size = max(len(left), len(right))
    return _clean(
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    )


def _scale(
    value: Polynomial, scalar: Fraction | int, guard: AlgebraGuard
) -> Polynomial:
    guard.tick()
    return _clean(Fraction(scalar) * coefficient for coefficient in value)


def _subtract(left: Polynomial, right: Polynomial, guard: AlgebraGuard) -> Polynomial:
    return _add(left, _scale(right, -1, guard), guard)


def _multiply(left: Polynomial, right: Polynomial, guard: AlgebraGuard) -> Polynomial:
    guard.tick()
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] += left_coefficient * right_coefficient
    return _clean(result)


def _power(value: Polynomial, exponent: int, guard: AlgebraGuard) -> Polynomial:
    if exponent < 0 or exponent > 10:
        raise ValueError("polynomial exponent must lie in [0,10]")
    result = ONE
    for _ in range(exponent):
        result = _multiply(result, value, guard)
    return result


def _product(values: Sequence[Polynomial], guard: AlgebraGuard) -> Polynomial:
    result = ONE
    for value in values:
        result = _multiply(result, value, guard)
    return result


def _shift_constant(
    value: Polynomial, shift: Fraction | int, guard: AlgebraGuard
) -> Polynomial:
    return _add(value, _constant(shift), guard)


def _choose(value: Polynomial, size: int, guard: AlgebraGuard) -> Polynomial:
    if size < 0 or size > 8:
        raise ValueError("binomial size must lie in [0,8]")
    result = ONE
    for index in range(size):
        result = _multiply(result, _shift_constant(value, -index, guard), guard)
    return _scale(result, Fraction(1, math.factorial(size)), guard)


def _elementary_sign_sum(
    order: int,
    population: Polynomial,
    total_sign: Polynomial,
    guard: AlgebraGuard,
) -> Polynomial:
    """Return e_order for N signs in {+1,-1} with total sign S.

    Newton's identities use power sum S in odd degree and N in even degree.
    Both N and S may themselves be polynomials in q.
    """

    if order < 0 or order > 8:
        raise ValueError("elementary-sign order must lie in [0,8]")
    elementary = [ONE]
    for degree in range(1, order + 1):
        numerator = ZERO
        for power in range(1, degree + 1):
            power_sum = total_sign if power % 2 else population
            term = _multiply(elementary[degree - power], power_sum, guard)
            numerator = _add(
                numerator,
                _scale(term, 1 if power % 2 else -1, guard),
                guard,
            )
        elementary.append(_scale(numerator, Fraction(1, degree), guard))
    return elementary[order]


def _polynomial_pairs(value: Polynomial) -> list[list[int]]:
    return [[coefficient.numerator, coefficient.denominator] for coefficient in value]


def _polynomial_from_pairs(values: Sequence[Sequence[int]]) -> Polynomial:
    return _clean(Fraction(int(pair[0]), int(pair[1])) for pair in values)


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


def _lf_normalized_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _load_signature_rows() -> list[dict[str, object]]:
    actual_hashes = {
        "high_weight_fixture": _lf_normalized_sha256(HIGH_WEIGHT_FIXTURE_PATH),
        "moment_note": _lf_normalized_sha256(MOMENT_NOTE_PATH),
        "stack_adapter": _lf_normalized_sha256(STACK_ADAPTER_PATH),
    }
    if actual_hashes != EXPECTED_DEPENDENCY_LF_SHA256:
        raise RuntimeError("a source-locked B3 dependency changed")

    fixture = json.loads(HIGH_WEIGHT_FIXTURE_PATH.read_text(encoding="utf-8"))
    if not isinstance(fixture, dict):
        raise TypeError("high-weight fixture is not an object")
    claimed_hash = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed_hash != _canonical_sha256(payload):
        raise ValueError("high-weight fixture canonical payload hash is invalid")
    if claimed_hash != EXPECTED_HIGH_WEIGHT_PAYLOAD_SHA256:
        raise ValueError("high-weight fixture payload is not the pinned source")

    roadmap = fixture.get("b_cubed_signature_roadmap")
    if not isinstance(roadmap, dict):
        raise TypeError("high-weight fixture lost its B3 roadmap")
    rows = roadmap.get("signatures")
    if not isinstance(rows, list) or len(rows) != MAX_SIGNATURES:
        raise ValueError("the pinned B3 roadmap is not the 23-signature ledger")
    return rows


SIGNATURE_PATTERN = re.compile(r"^L\[([^]]+)\]\.Q\[([^]]+)\]$")


def _parse_exponents(value: str) -> tuple[int, ...]:
    if value == "-":
        return ()
    exponents = tuple(int(entry) for entry in value.split(","))
    if any(exponent < 1 or exponent > 6 for exponent in exponents):
        raise ValueError("signature exponent lies outside [1,6]")
    return exponents


def _parse_signature(signature: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    match = SIGNATURE_PATTERN.fullmatch(signature)
    if match is None:
        raise ValueError(f"malformed B3 signature: {signature}")
    return _parse_exponents(match.group(1)), _parse_exponents(match.group(2))


def _assignment_multiplier(exponents: Sequence[int]) -> int:
    result = 1
    for parity in (0, 1):
        counts = Counter(exponent for exponent in exponents if exponent % 2 == parity)
        size = sum(counts.values())
        result *= math.factorial(size)
        for multiplicity in counts.values():
            result //= math.factorial(multiplicity)
    return result


def _type_count(
    linear: Sequence[int], quadratic: Sequence[int], guard: AlgebraGuard
) -> Polynomial:
    linear_counts = Counter(linear)
    quadratic_counts = Counter(quadratic)
    linear_falling = _product(
        [_shift_constant(Q, -index, guard) for index in range(len(linear))], guard
    )
    i_value = _scale(
        _multiply(Q, _shift_constant(Q, -1, guard), guard), Fraction(1, 2), guard
    )
    quadratic_falling = _product(
        [_shift_constant(i_value, -index, guard) for index in range(len(quadratic))],
        guard,
    )
    denominator = math.prod(math.factorial(value) for value in linear_counts.values())
    denominator *= math.prod(
        math.factorial(value) for value in quadratic_counts.values()
    )
    return _scale(
        _multiply(linear_falling, quadratic_falling, guard),
        Fraction(1, denominator),
        guard,
    )


def _primitive_moments(
    linear_count: int, quadratic_count: int, guard: AlgebraGuard
) -> dict[str, Polynomial]:
    """Aggregate N, s1, s1^2, s2, p1, p2 over one conductor type."""

    q_minus_one = _shift_constant(Q, -1, guard)
    half_q_minus_one = _scale(q_minus_one, Fraction(1, 2), guard)
    i_value = _scale(_multiply(Q, q_minus_one, guard), Fraction(1, 2), guard)

    count = _multiply(
        _choose(Q, linear_count, guard),
        _choose(i_value, quadratic_count, guard),
        guard,
    )

    # For a fixed x in F_q: q-1 nonzero linear signs have sum 0, while
    # the I irreducible-quadratic signs have sum -(q-1)/2.
    s1 = _multiply(
        Q,
        _multiply(
            _elementary_sign_sum(linear_count, q_minus_one, ZERO, guard),
            _elementary_sign_sum(
                quadratic_count,
                i_value,
                _scale(half_q_minus_one, -1, guard),
                guard,
            ),
            guard,
        ),
        guard,
    )

    diagonal = _multiply(
        Q,
        _multiply(
            _choose(q_minus_one, linear_count, guard),
            _choose(i_value, quadratic_count, guard),
            guard,
        ),
        guard,
    )

    # For ordered x != y: q-2 nonzero linear signs have sum -1; the
    # irreducible-quadratic inventory still has sum -(q-1)/2.
    q_minus_two = _shift_constant(Q, -2, guard)
    off_diagonal = _multiply(
        _multiply(Q, q_minus_one, guard),
        _multiply(
            _elementary_sign_sum(linear_count, q_minus_two, _constant(-1), guard),
            _elementary_sign_sum(
                quadratic_count,
                i_value,
                _scale(half_q_minus_one, -1, guard),
                guard,
            ),
            guard,
        ),
        guard,
    )
    s1_squared = _add(diagonal, off_diagonal, guard)

    # For a fixed irreducible Q0 and z in its two roots: all q linear signs
    # have sum -1.  The I-1 other quadratic signs have sum -(q+1)/2.
    i_minus_one = _shift_constant(i_value, -1, guard)
    half_q_plus_one = _scale(_shift_constant(Q, 1, guard), Fraction(1, 2), guard)
    nonrational = _multiply(
        _scale(i_value, 2, guard),
        _multiply(
            _elementary_sign_sum(linear_count, Q, _constant(-1), guard),
            _elementary_sign_sum(
                quadratic_count,
                i_minus_one,
                _scale(half_q_plus_one, -1, guard),
                guard,
            ),
            guard,
        ),
        guard,
    )
    s2 = _add(diagonal, nonrational, guard)

    p1 = _add(count, s1, guard)
    p2 = _add(
        p1,
        _scale(_add(s1_squared, s2, guard), Fraction(1, 2), guard),
        guard,
    )
    return {
        "count": count,
        "sum_s1": s1,
        "sum_s1_squared": s1_squared,
        "sum_s2": s2,
        "sum_p1": p1,
        "sum_p2": p2,
    }


def _principal_coefficient(
    degree: int, linear_support: int, quadratic_support: int, guard: AlgebraGuard
) -> Polynomial:
    result = ZERO
    for linear_degree in range(linear_support + 1):
        for quadratic_degree in range(quadratic_support + 1):
            deletion_degree = linear_degree + 2 * quadratic_degree
            if deletion_degree > degree:
                continue
            coefficient = (
                (-1) ** (linear_degree + quadratic_degree)
                * math.comb(linear_support, linear_degree)
                * math.comb(quadratic_support, quadratic_degree)
            )
            term = _scale(
                _power(Q, degree - deletion_degree, guard), coefficient, guard
            )
            result = _add(result, term, guard)
    return result


def _row_aggregates(
    row: Mapping[str, object],
    primitive: Mapping[tuple[int, int], Mapping[str, Polynomial]],
    guard: AlgebraGuard,
) -> dict[str, object]:
    signature = row.get("signature")
    if not isinstance(signature, str):
        raise TypeError("B3 signature name is not a string")
    linear, quadratic = _parse_signature(signature)
    tuple_weight = int(row["tuple_weight"])
    if sum(linear) + 2 * sum(quadratic) != 6:
        raise ArithmeticError("a frozen B3 signature is not degree six")
    radical_degree = sum(exponent % 2 for exponent in linear) + 2 * sum(
        exponent % 2 for exponent in quadratic
    )
    if radical_degree != int(row["radical_degree"]):
        raise ArithmeticError("the frozen B3 radical degree changed")

    linear_odd = sum(exponent % 2 for exponent in linear)
    quadratic_odd = sum(exponent % 2 for exponent in quadratic)
    linear_even = sum(exponent % 2 == 0 for exponent in linear)
    quadratic_even = sum(exponent % 2 == 0 for exponent in quadratic)
    linear_support = linear_odd + linear_even
    quadratic_support = quadratic_odd + quadratic_even

    type_count = _type_count(linear, quadratic, guard)
    frozen_count = _polynomial_from_pairs(row["type_count_coefficients_low_to_high"])
    if type_count != frozen_count:
        raise ArithmeticError(f"type-count polynomial drifted for {signature}")

    assignment_multiplier = _assignment_multiplier(linear) * _assignment_multiplier(
        quadratic
    )
    q_minus_linear_odd = _shift_constant(Q, -linear_odd, guard)
    i_value = _scale(
        _multiply(Q, _shift_constant(Q, -1, guard), guard),
        Fraction(1, 2),
        guard,
    )
    conductor_count = _multiply(
        _choose(Q, linear_odd, guard),
        _choose(i_value, quadratic_odd, guard),
        guard,
    )
    base_count = _product(
        (
            conductor_count,
            _choose(q_minus_linear_odd, linear_even, guard),
            _choose(
                _shift_constant(i_value, -quadratic_odd, guard),
                quadratic_even,
                guard,
            ),
        ),
        guard,
    )
    if type_count != _scale(base_count, assignment_multiplier, guard):
        raise ArithmeticError(f"odd/even support count failed for {signature}")

    c1 = ZERO
    c3 = ZERO
    c5 = ZERO
    if radical_degree == 0:
        c1 = _multiply(
            type_count,
            _principal_coefficient(1, linear_even, quadratic_even, guard),
            guard,
        )
        c3 = _multiply(
            type_count,
            _principal_coefficient(3, linear_even, quadratic_even, guard),
            guard,
        )
        c5 = _multiply(
            type_count,
            _principal_coefficient(5, linear_even, quadratic_even, guard),
            guard,
        )
    elif radical_degree == 2:
        if (linear_even, quadratic_even) == (0, 0):
            c1 = _scale(conductor_count, -assignment_multiplier, guard)
        elif (linear_even, quadratic_even) == (1, 0):
            # Sum of the deletion signs over all external linears is -1
            # for each primitive degree-two conductor.
            sum_delta = _scale(conductor_count, -1, guard)
            c1 = _scale(
                _subtract(_scale(base_count, -1, guard), sum_delta, guard),
                assignment_multiplier,
                guard,
            )
        elif (linear_even, quadratic_even) == (2, 0):
            external_count = q_minus_linear_odd
            sum_singles = _multiply(
                conductor_count,
                _scale(_shift_constant(external_count, -1, guard), -1, guard),
                guard,
            )
            sum_pairs = _multiply(
                conductor_count,
                _elementary_sign_sum(2, external_count, _constant(-1), guard),
                guard,
            )
            c1 = _scale(
                _subtract(_scale(base_count, -1, guard), sum_singles, guard),
                assignment_multiplier,
                guard,
            )
            c3 = _scale(sum_pairs, -assignment_multiplier, guard)
        elif (linear_even, quadratic_even) == (0, 1):
            half_q_minus_one = _scale(
                _shift_constant(Q, -1, guard), Fraction(1, 2), guard
            )
            deletion_total = _scale(
                _add(half_q_minus_one, _constant(quadratic_odd), guard),
                -1,
                guard,
            )
            c1 = _scale(base_count, -assignment_multiplier, guard)
            c3 = _scale(
                _multiply(conductor_count, deletion_total, guard),
                assignment_multiplier,
                guard,
            )
        else:
            raise ArithmeticError(f"unhandled degree-two deletion type {signature}")
    elif radical_degree == 4:
        moments = primitive[(linear_odd, quadratic_odd)]
        if (linear_even, quadratic_even) == (0, 0):
            c1 = _scale(moments["sum_s1"], assignment_multiplier, guard)
            c3 = _scale(
                _multiply(Q, moments["count"], guard),
                -assignment_multiplier,
                guard,
            )
        elif (linear_even, quadratic_even) == (1, 0):
            external_count = q_minus_linear_odd
            c1 = _scale(
                _multiply(
                    _shift_constant(external_count, -1, guard),
                    moments["sum_s1"],
                    guard,
                ),
                assignment_multiplier,
                guard,
            )
            c3 = _add(
                _scale(
                    _product((Q, moments["count"], external_count), guard),
                    -1,
                    guard,
                ),
                _add(
                    _multiply(
                        _shift_constant(_scale(Q, -1, guard), 1, guard),
                        moments["sum_s1"],
                        guard,
                    ),
                    moments["sum_s1_squared"],
                    guard,
                ),
                guard,
            )
            c3 = _scale(c3, assignment_multiplier, guard)
        else:
            raise ArithmeticError(f"unhandled degree-four deletion type {signature}")
    elif radical_degree == 6:
        if linear_even or quadratic_even or assignment_multiplier != 1:
            raise ArithmeticError("a generic degree-six row gained deletion support")
        moments = primitive[(linear_odd, quadratic_odd)]
        c1 = _subtract(moments["sum_p1"], moments["count"], guard)
        c3 = _subtract(
            _multiply(Q, moments["sum_p1"], guard),
            moments["sum_p2"],
            guard,
        )
        c5 = _scale(_multiply(_power(Q, 2, guard), moments["count"], guard), -1, guard)
    else:
        raise ArithmeticError("B3 radical degree lies outside {0,2,4,6}")

    q_minus_l = _shift_constant(Q, -linear_support, guard)
    sieve_c1 = _shift_constant(
        _scale(Q, -linear_support, guard),
        math.comb(linear_support + 1, 2) + quadratic_support,
        guard,
    )
    s5 = _add(
        _subtract(c5, _multiply(q_minus_l, c3, guard), guard),
        _multiply(sieve_c1, c1, guard),
        guard,
    )
    contribution = _scale(s5, tuple_weight, guard)
    return {
        "signature": signature,
        "tuple_weight": tuple_weight,
        "radical_degree": radical_degree,
        "linear_odd_prime_count": linear_odd,
        "quadratic_odd_prime_count": quadratic_odd,
        "linear_deletion_prime_count": linear_even,
        "quadratic_deletion_prime_count": quadratic_even,
        "assignment_multiplier": assignment_multiplier,
        "type_count_low_to_high": _polynomial_pairs(type_count),
        "sum_C1_low_to_high": _polynomial_pairs(c1),
        "sum_C3_low_to_high": _polynomial_pairs(c3),
        "sum_C5_low_to_high": _polynomial_pairs(c5),
        "sum_S5_low_to_high": _polynomial_pairs(s5),
        "weighted_contribution_low_to_high": _polynomial_pairs(contribution),
        "_contribution": contribution,
    }


EXPECTED_DEGREE_BLOCKS = {
    0: (0, -112, 309, -357, 250, -134, 62, -23, 5),
    2: (0, 773, -1566, 1084, -330, 39),
    4: (0, -1365, 2214, -809, -196, 206, -56, 6),
    6: (0, 705, -949, 85, 256, -110, 10, 4, -1),
}
EXPECTED_B3_TOTAL = (0, 1, 8, 3, -20, 1, 16, -13, 4)


def _known_moment_totals(guard: AlgebraGuard) -> dict[str, Polynomial]:
    q_minus_one = _shift_constant(Q, -1, guard)
    q_plus_one = _shift_constant(Q, 1, guard)
    common = _multiply(Q, q_minus_one, guard)
    a2 = _multiply(
        common,
        _add(
            _multiply(_power(Q, 3, guard), q_minus_one, guard),
            _add(_power(Q, 2, guard), _shift_constant(Q, -2, guard), guard),
            guard,
        ),
        guard,
    )
    b1 = _multiply(
        common,
        _add(
            _subtract(_power(Q, 4, guard), _power(Q, 3, guard), guard),
            _shift_constant(_power(Q, 2, guard), -1, guard),
            guard,
        ),
        guard,
    )
    a2b = _product(
        (
            common,
            q_plus_one,
            _add(
                _subtract(_power(Q, 2, guard), _scale(Q, 2, guard), guard),
                _constant(3),
                guard,
            ),
            _add(
                _subtract(
                    _scale(_power(Q, 2, guard), 2, guard), _scale(Q, 2, guard), guard
                ),
                _constant(-1),
                guard,
            ),
        ),
        guard,
    )
    b2 = _multiply(
        common,
        _add(
            _multiply(
                _power(Q, 3, guard),
                _add(
                    _subtract(
                        _scale(_power(Q, 2, guard), 2, guard),
                        _scale(Q, 3, guard),
                        guard,
                    ),
                    _constant(2),
                    guard,
                ),
                guard,
            ),
            _add(
                _subtract(_power(Q, 2, guard), _scale(Q, 3, guard), guard),
                _constant(-1),
                guard,
            ),
            guard,
        ),
        guard,
    )
    return {"sum_a2": a2, "sum_b": b1, "sum_a2b": a2b, "sum_b2": b2}


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        HIGH_WEIGHT_FIXTURE_PATH,
        MOMENT_NOTE_PATH,
        STACK_ADAPTER_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    return [
        {
            "path": path.resolve().relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_normalized_sha256(path),
        }
        for path in paths
    ]


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    guard = AlgebraGuard(started + MAX_WALL_SECONDS)
    rows = _load_signature_rows()

    primitive_types = ((4, 0), (2, 1), (0, 2), (6, 0), (4, 1), (2, 2), (0, 3))
    primitive = {
        factor_type: _primitive_moments(*factor_type, guard)
        for factor_type in primitive_types
    }
    primitive_rows = []
    for linear_count, quadratic_count in primitive_types:
        moments = primitive[(linear_count, quadratic_count)]
        primitive_rows.append(
            {
                "conductor_degree": linear_count + 2 * quadratic_count,
                "linear_prime_count": linear_count,
                "quadratic_prime_count": quadratic_count,
                **{
                    f"{name}_low_to_high": _polynomial_pairs(value)
                    for name, value in moments.items()
                },
            }
        )

    exact_rows = [_row_aggregates(row, primitive, guard) for row in rows]
    radical_census = Counter(int(row["radical_degree"]) for row in exact_rows)
    if radical_census != Counter({0: 4, 2: 10, 4: 5, 6: 4}):
        raise ArithmeticError("the 23-signature radical-degree census changed")
    weighted_tuple_count = ZERO
    for row in exact_rows:
        weighted_tuple_count = _add(
            weighted_tuple_count,
            _scale(
                _polynomial_from_pairs(row["type_count_low_to_high"]),
                int(row["tuple_weight"]),
                guard,
            ),
            guard,
        )
    if weighted_tuple_count != _power(Q, 6, guard):
        raise ArithmeticError("the 23 signatures do not exhaust all q^6 triples")
    degree_blocks = {degree: ZERO for degree in (0, 2, 4, 6)}
    for row in exact_rows:
        degree = int(row["radical_degree"])
        degree_blocks[degree] = _add(
            degree_blocks[degree], row.pop("_contribution"), guard
        )
    for degree, expected in EXPECTED_DEGREE_BLOCKS.items():
        if degree_blocks[degree] != _clean(expected):
            raise ArithmeticError(f"radical-degree {degree} block polynomial drifted")

    b3_total = ZERO
    for value in degree_blocks.values():
        b3_total = _add(b3_total, value, guard)
    if b3_total != _clean(EXPECTED_B3_TOTAL):
        raise ArithmeticError("the 23 B3 rows did not close to the theorem polynomial")

    target_inner = _add(
        _add(
            _add(
                _scale(_power(Q, 6, guard), 4, guard),
                _scale(_power(Q, 5, guard), -9, guard),
                guard,
            ),
            _add(
                _scale(_power(Q, 4, guard), 7, guard),
                _scale(_power(Q, 3, guard), 8, guard),
                guard,
            ),
            guard,
        ),
        _add(
            _add(
                _scale(_power(Q, 2, guard), -12, guard),
                _scale(Q, -9, guard),
                guard,
            ),
            _constant(-1),
            guard,
        ),
        guard,
    )
    target_total = _product((Q, _shift_constant(Q, -1, guard), target_inner), guard)
    if b3_total != target_total:
        raise ArithmeticError("factored B3 theorem target failed")

    known = _known_moment_totals(guard)
    # Clear q^3 from the character identity
    # chi_03=b^3/q^3-b^2/q^2-2a^2b/q^2-b/q+3a^2/q.
    cleared_chi_sum = b3_total
    cleared_chi_sum = _subtract(
        cleared_chi_sum, _multiply(Q, known["sum_b2"], guard), guard
    )
    cleared_chi_sum = _subtract(
        cleared_chi_sum,
        _scale(_multiply(Q, known["sum_a2b"], guard), 2, guard),
        guard,
    )
    cleared_chi_sum = _subtract(
        cleared_chi_sum,
        _multiply(_power(Q, 2, guard), known["sum_b"], guard),
        guard,
    )
    cleared_chi_sum = _add(
        cleared_chi_sum,
        _scale(_multiply(_power(Q, 2, guard), known["sum_a2"], guard), 3, guard),
        guard,
    )
    expected_cleared_chi = _product(
        (
            Q,
            _shift_constant(Q, -1, guard),
            _add(
                _subtract(_power(Q, 4, guard), _scale(Q, 2, guard), guard),
                _constant(-1),
                guard,
            ),
        ),
        guard,
    )
    if cleared_chi_sum != expected_cleared_chi:
        raise ArithmeticError("chi_(0,3) lower-moment bridge failed")

    actual_atoms = guard.operations + len(rows) + len(primitive_types)
    if actual_atoms > MAX_SYMBOLIC_OPERATIONS:
        raise RuntimeError("declared exact operation/signature atom cap exceeded")
    elapsed = time.monotonic() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("B3 proof replay exceeded its wall-time cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_b3_primitive_trace_average.v1",
        "status": "PROVED_EXACT_ALL_ODD_PRIME_POWERS",
        "scope": {
            "q": "every odd prime power",
            "family": "all monic squarefree quintics D in F_q[T]",
            "finite_fields_enumerated": 0,
            "family_members_consumed": 0,
            "numeric_approximations": 0,
        },
        "theorem": {
            "b3_total": ("sum_D b_D^3=q*(q-1)*(4*q^6-9*q^5+7*q^4+8*q^3-12*q^2-9*q-1)"),
            "b3_mean": ("E[b_D^3]=(4*q^6-9*q^5+7*q^4+8*q^3-12*q^2-9*q-1)/q^3"),
            "chi_(0,3)_mean": "(q^4-2*q-1)/q^6",
            "marked_stack_trace": "T_(0,3)(q)=q^4-2*q-1",
            "marked_stack_normalization": (
                "T_(0,3)=q^3/[q*(q-1)]*sum_D chi_(0,3)(U_D)"
            ),
        },
        "primitive_sign_inventory_lemma": {
            "notation": (
                "E_j(N,S) is the j-th elementary symmetric sum of N signs "
                "with total S; Newton uses power sums S,N,S,N,..."
            ),
            "conductor_count": "N_lk=binom(q,l)*binom(I,k), I=q*(q-1)/2",
            "sum_s1": "q*E_l(q-1,0)*E_k(I,-(q-1)/2)",
            "sum_s1_squared": (
                "q*binom(q-1,l)*binom(I,k)+q*(q-1)*E_l(q-2,-1)*E_k(I,-(q-1)/2)"
            ),
            "sum_s2": ("q*binom(q-1,l)*binom(I,k)+2*I*E_l(q,-1)*E_k(I-1,-(q+1)/2)"),
            "primitive_coefficients": (
                "sum p1=N_lk+sum s1; sum p2=N_lk+sum s1+(sum s1^2+sum s2)/2"
            ),
            "status": "EXACT_BY_CHARACTER_ORTHOGONALITY_AND_NEWTON_IDENTITIES",
        },
        "primitive_type_aggregates": primitive_rows,
        "ordered_triple_signature_audit": {
            "signature_count": len(exact_rows),
            "radical_degree_census": {
                str(degree): radical_census[degree] for degree in (0, 2, 4, 6)
            },
            "weighted_type_count_low_to_high": _polynomial_pairs(weighted_tuple_count),
            "weighted_type_count": "q^6",
            "status": "EXACT_EXHAUSTIVE_23_SIGNATURE_PARTITION",
        },
        "signature_ledger": exact_rows,
        "radical_degree_blocks": {
            str(degree): _polynomial_pairs(value)
            for degree, value in degree_blocks.items()
        },
        "b3_total_low_to_high": _polynomial_pairs(b3_total),
        "cleared_chi_sum_low_to_high": _polynomial_pairs(cleared_chi_sum),
        "proof_dependencies": {
            "b_as_character_sum_and_squarefree_sieve": (
                "GENUS2_MOMENT_IDENTITY.md, equations (4) and (8)"
            ),
            "signature_source": (
                "the exact 23-row B3 ledger in genus2_high_weight_channel_probe.json"
            ),
            "known_lower_moments": (
                "the proved all-q a^2, b, a^2*b, b^2 totals in GENUS2_MOMENT_IDENTITY.md"
            ),
            "stack_normalization": "GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md",
        },
        "composite_denominator_convention": {
            "definition": (
                "(F/h)=product_P (F/P)^v_P(h), with every local symbol zero "
                "when P divides F"
            ),
            "even_exponent_warning": (
                "an even exponent makes the local value 1 only off P; it remains "
                "zero on multiples of P"
            ),
            "proof_effect": (
                "primes of positive even exponent are retained as deletion support "
                "E(h) in L_h=L_r*product_(P in E)(1-(P/r)u^deg(P))"
            ),
        },
        "source_manifest": _source_manifest(),
        "resource_contract": {
            "maximum_signatures": MAX_SIGNATURES,
            "actual_signatures": len(rows),
            "maximum_primitive_types": MAX_PRIMITIVE_TYPES,
            "actual_primitive_types": len(primitive_types),
            "symbolic_operation_semantics": (
                "one operation is one complete-polynomial add, scale, multiply, "
                "or power step; signature and primitive-type inputs are added as atoms"
            ),
            "maximum_symbolic_operations_and_input_atoms": MAX_SYMBOLIC_OPERATIONS,
            "actual_symbolic_operations": guard.operations,
            "actual_operations_and_input_atoms": actual_atoms,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "observed_wall_seconds_is_not_payload_data": True,
        },
        "firewalls": [
            "The proof quantifies over odd prime powers; it is not interpolation from q=3,5,7.",
            "No finite field, curve, quintic, or family member is enumerated.",
            "The result is an exact family moment and does not imply a memberwise sign.",
            "The marked-stack identity uses the separately proved normalization adapter; no motive or global Euler-product identity is inferred.",
            "No external novelty, RH, or GRH claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    fixture = build_fixture()
    if args.write:
        OUTPUT_PATH.write_text(
            json.dumps(
                fixture,
                allow_nan=False,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote {OUTPUT_PATH}")
        return 0
    if args.check:
        stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"B3 primitive trace fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: B3 primitive trace fixture matches {OUTPUT_PATH}")
        return 0
    print(
        json.dumps(
            fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
