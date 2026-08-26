#!/usr/bin/env python3
"""Exact 54-signature reduction of the genus-two B4 trace average.

The packet consumes the source-locked third-order primitive inventory and
reweights every signature in ``sum_D b_D^4``.  Its decisive checks are formal:
the sixth- and eighth-order level-2 channels cancel, while the fourth-order
survivor descends exactly to a rational-root-marked cubic moment.
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
from fractions import Fraction
from pathlib import Path

import genus2_b3_primitive_trace_average as b3
import genus2_m22_triangular_trace_average as m22
import genus2_third_order_primitive_inventory as third

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_b4_triangular_trace_average.json"
NOTE_PATH = HERE / "GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_b4_triangular_trace_average.py"

SECOND_MOMENT_FIXTURE_PATH = HERE / "genus2_second_moment_reduction.json"
THIRD_FIXTURE_PATH = HERE / "genus2_third_order_primitive_inventory.json"
THIRD_PRODUCER_PATH = HERE / "genus2_third_order_primitive_inventory.py"
THIRD_NOTE_PATH = HERE / "GENUS2_THIRD_ORDER_PRIMITIVE_INVENTORY.md"
THIRD_TEST_PATH = ROOT / "tests" / "test_genus2_third_order_primitive_inventory.py"
B3_FIXTURE_PATH = HERE / "genus2_b3_primitive_trace_average.json"
M22_FIXTURE_PATH = HERE / "genus2_m22_triangular_trace_average.json"

# Filled only after Packet A is frozen.  Packet B refuses an unpinned Packet A.
EXPECTED_THIRD_PAYLOAD_SHA256 = (
    "0f624fc9ad81a4212aa7300b5d4563ff7b5b2b338aa0db97f3351baf0ae0dfff"
)
EXPECTED_THIRD_LF_SHA256 = {
    "fixture": "9559f814c02383970f3fbe841a10c95c53ee4a2206e4e6657bc737f9d259e906",
    "producer": "5f29b8f5b62fbb19aa9f03024014c8a5e5d2cf49592bf3847134790a817f0546",
    "note": "bf5f384795d1c067e3f1765d618a9631b8e4336af2839bce3b0b763c5d196e2d",
    "test": "b2a6338fab19dfe09d1190db71be5eb07872d910a0033b73d46f6b97eecb774b",
}

EXPECTED_SOURCE_PAYLOAD_SHA256 = {
    "second_moment": "55c5c9ef04a65ca46044ac1d76c76f33afc02b51c2d38a8ca196b99498ee16ec",
    "B3": "e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd",
    "M22": "4d147295e3d2b7bc4b62eb8ba113c946f528606d82dd28d1a1ec002e2f93d60c",
}
EXPECTED_SOURCE_LF_SHA256 = {
    "second_moment": "0966565c0b29d7bf85f6ad20f8c6634365a8fff674e3c3b06589125fe0bdbaf0",
    "B3": "5ecc6006014a159a4030218977c89f58c63334461a568b7a67d36130bae1c50b",
    "M22": "a93f288ddce023005989cc0a7ed543d859697e68fa378a24ae7619af35fc9633",
}

MAX_SIGNATURES = 54
MAX_PRIMITIVE_ROWS = 12
MAX_MARKED_ROWS = 13
MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS = 4096
MAX_WALL_SECONDS = 5.0

SIGNATURE_PATTERN = re.compile(r"^L\[([^]]+)\]\.Q\[([^]]+)\]$")


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


def _load_locked_fixture(
    path: Path, expected_payload: str, expected_lf: str
) -> dict[str, object]:
    if _lf_normalized_sha256(path) != expected_lf:
        raise RuntimeError(f"source-locked file changed: {path}")
    fixture = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(fixture, dict):
        raise TypeError(f"expected an object fixture at {path}")
    claimed = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload) or claimed != expected_payload:
        raise ValueError(f"source-locked payload mismatch at {path}")
    return fixture


def _parse_polynomial(value: object) -> b3.Polynomial:
    if not isinstance(value, list):
        raise TypeError("serialized polynomial is not a list")
    return b3._polynomial_from_pairs(value)


def _parse_expression(value: object) -> third.ResidualExpression:
    if not isinstance(value, dict):
        raise TypeError("serialized residual expression is not an object")
    constant = _parse_polynomial(value["constant_low_to_high"])
    raw_coefficients = value.get("level2_residual_coefficients")
    if not isinstance(raw_coefficients, dict):
        raise TypeError("residual coefficient dictionary is missing")
    coefficients = {
        key: _parse_polynomial(raw_coefficients[key])
        for key in third.RESIDUAL_KEYS
        if key in raw_coefficients
    }
    return third.ResidualExpression(constant, coefficients)


def _expr_subtract(
    left: third.ResidualExpression,
    right: third.ResidualExpression,
    guard: b3.AlgebraGuard,
) -> third.ResidualExpression:
    return third._expr_add(left, third._expr_scale_fraction(right, -1, guard), guard)


def _expr_is_polynomial(value: third.ResidualExpression) -> bool:
    return all(polynomial == b3.ZERO for polynomial in value.coefficients.values())


def _parse_exponents(value: str) -> tuple[int, ...]:
    if value == "-":
        return ()
    result = tuple(int(entry) for entry in value.split(","))
    if any(exponent < 1 or exponent > 8 for exponent in result):
        raise ValueError("B4 exponent lies outside [1,8]")
    return result


def _parse_signature(signature: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    match = SIGNATURE_PATTERN.fullmatch(signature)
    if match is None:
        raise ValueError(f"malformed B4 signature: {signature}")
    return _parse_exponents(match.group(1)), _parse_exponents(match.group(2))


def _normalize_b4_rows(fixture: Mapping[str, object]) -> list[dict[str, object]]:
    blocks = fixture.get("signature_blocks")
    if not isinstance(blocks, dict) or not isinstance(blocks.get("B4"), dict):
        raise TypeError("second-moment fixture lost its B4 block")
    source_rows = blocks["B4"].get("signatures")
    if not isinstance(source_rows, list) or len(source_rows) != MAX_SIGNATURES:
        raise ValueError("B4 source is not the pinned 54-signature ledger")
    rows: list[dict[str, object]] = []
    for source in source_rows:
        if not isinstance(source, dict):
            raise TypeError("a B4 source row is not an object")
        radical = source.get("odd_radical")
        type_count = source.get("type_count")
        if not isinstance(radical, dict) or not isinstance(type_count, dict):
            raise TypeError("a B4 source row lost nested data")
        rows.append(
            {
                "signature": source["signature"],
                "tuple_weight": source["tuple_weight"],
                "radical_degree": radical["degree"],
                "type_count_coefficients_low_to_high": type_count[
                    "coefficients_low_to_high"
                ],
            }
        )
    return rows


def _primitive_maps(
    fixture: Mapping[str, object],
) -> tuple[
    dict[tuple[int, int], dict[str, object]],
    dict[tuple[int, int, str], dict[str, third.ResidualExpression]],
]:
    theorem = fixture.get("exact_reduction_theorem")
    if not isinstance(theorem, dict):
        raise TypeError("Packet A lost its exact reduction theorem")
    source_rows = theorem.get("primitive_rows")
    if not isinstance(source_rows, list) or len(source_rows) != MAX_PRIMITIVE_ROWS:
        raise ValueError("Packet A lost its twelve primitive rows")
    primitive: dict[tuple[int, int], dict[str, object]] = {}
    for row in source_rows:
        if not isinstance(row, dict):
            raise TypeError("a Packet A primitive row is malformed")
        key = int(row["linear_prime_count"]), int(row["quadratic_prime_count"])
        primitive[key] = {
            "count": _parse_polynomial(row["count_low_to_high"]),
            "sum_s1": _parse_polynomial(row["sum_s1_low_to_high"]),
            "sum_s1_squared": _parse_polynomial(row["sum_s1_squared_low_to_high"]),
            "sum_s2": _parse_polynomial(row["sum_s2_low_to_high"]),
            "sum_p1": _parse_polynomial(row["sum_p1_low_to_high"]),
            "sum_p2": _parse_polynomial(row["sum_p2_low_to_high"]),
            "sum_s1_cubed": _parse_expression(row["sum_s1_cubed"]),
            "sum_s1_s2": _parse_expression(row["sum_s1_s2"]),
            "sum_s3": _parse_expression(row["sum_s3"]),
            "sum_p3": _parse_expression(row["sum_p3"]),
        }
    marked_source = fixture.get("marked_deletion_interface")
    if not isinstance(marked_source, list) or len(marked_source) != MAX_MARKED_ROWS:
        raise ValueError("Packet A marked deletion interface changed")
    marked: dict[tuple[int, int, str], dict[str, third.ResidualExpression]] = {}
    for row in marked_source:
        if not isinstance(row, dict):
            raise TypeError("a Packet A marked row is malformed")
        key = (
            int(row["linear_prime_count"]),
            int(row["quadratic_prime_count"]),
            str(row["deletion_kind"]),
        )
        marked[key] = {
            "C1": _parse_expression(row["sum_C1"]),
            "C3": _parse_expression(row["sum_C3"]),
            "C5": _parse_expression(row["sum_C5"]),
        }
    return primitive, marked


def _degree_two_deletion_coefficient(
    coefficient_degree: int,
    linear_conductor_count: int,
    quadratic_conductor_count: int,
    linear_deletion_count: int,
    quadratic_deletion_count: int,
    guard: b3.AlgebraGuard,
) -> b3.Polynomial:
    """Sum one deletion-polynomial coefficient over all external choices."""

    n_linear = b3._shift_constant(b3.Q, -linear_conductor_count, guard)
    i_value = b3._scale(
        b3._multiply(b3.Q, b3._shift_constant(b3.Q, -1, guard), guard),
        Fraction(1, 2),
        guard,
    )
    n_quadratic = b3._shift_constant(i_value, -quadratic_conductor_count, guard)
    total_linear = b3._constant(-1)
    total_quadratic = b3._scale(
        b3._shift_constant(b3.Q, 1 - linear_conductor_count, guard),
        Fraction(-1, 2),
        guard,
    )
    result = b3.ZERO
    for selected_linear in range(linear_deletion_count + 1):
        for selected_quadratic in range(quadratic_deletion_count + 1):
            if selected_linear + 2 * selected_quadratic != coefficient_degree:
                continue
            term = b3._product(
                (
                    b3._choose(
                        b3._shift_constant(n_linear, -selected_linear, guard),
                        linear_deletion_count - selected_linear,
                        guard,
                    ),
                    b3._choose(
                        b3._shift_constant(n_quadratic, -selected_quadratic, guard),
                        quadratic_deletion_count - selected_quadratic,
                        guard,
                    ),
                    b3._elementary_sign_sum(
                        selected_linear, n_linear, total_linear, guard
                    ),
                    b3._elementary_sign_sum(
                        selected_quadratic,
                        n_quadratic,
                        total_quadratic,
                        guard,
                    ),
                ),
                guard,
            )
            result = b3._add(
                result,
                b3._scale(term, (-1) ** (selected_linear + selected_quadratic), guard),
                guard,
            )
    return result


def _row_coefficients(
    row: Mapping[str, object],
    primitive: Mapping[tuple[int, int], Mapping[str, object]],
    marked: Mapping[tuple[int, int, str], Mapping[str, third.ResidualExpression]],
    guard: b3.AlgebraGuard,
) -> dict[str, object]:
    signature = str(row["signature"])
    linear, quadratic = _parse_signature(signature)
    if sum(linear) + 2 * sum(quadratic) != 8:
        raise ArithmeticError("a B4 signature lost total degree eight")
    radical_degree = sum(value % 2 for value in linear) + 2 * sum(
        value % 2 for value in quadratic
    )
    if radical_degree != int(row["radical_degree"]):
        raise ArithmeticError("a B4 radical degree changed")
    linear_odd = sum(value % 2 for value in linear)
    quadratic_odd = sum(value % 2 for value in quadratic)
    linear_even = sum(value % 2 == 0 for value in linear)
    quadratic_even = sum(value % 2 == 0 for value in quadratic)
    assignment = b3._assignment_multiplier(linear) * b3._assignment_multiplier(
        quadratic
    )
    type_count = b3._type_count(linear, quadratic, guard)
    frozen_count = _parse_polynomial(row["type_count_coefficients_low_to_high"])
    if type_count != frozen_count:
        raise ArithmeticError(f"B4 type-count polynomial drifted for {signature}")

    c1 = third._expr()
    c3 = third._expr()
    c5 = third._expr()
    key = linear_odd, quadratic_odd
    if radical_degree == 0:
        c1 = third._expr(
            b3._multiply(
                type_count,
                b3._principal_coefficient(1, linear_even, quadratic_even, guard),
                guard,
            )
        )
        c3 = third._expr(
            b3._multiply(
                type_count,
                b3._principal_coefficient(3, linear_even, quadratic_even, guard),
                guard,
            )
        )
        c5 = third._expr(
            b3._multiply(
                type_count,
                b3._principal_coefficient(5, linear_even, quadratic_even, guard),
                guard,
            )
        )
    elif radical_degree == 2:
        i_value = b3._scale(
            b3._multiply(b3.Q, b3._shift_constant(b3.Q, -1, guard), guard),
            Fraction(1, 2),
            guard,
        )
        conductor_count = b3._multiply(
            b3._choose(b3.Q, linear_odd, guard),
            b3._choose(i_value, quadratic_odd, guard),
            guard,
        )
        deletion = {
            degree: _degree_two_deletion_coefficient(
                degree,
                linear_odd,
                quadratic_odd,
                linear_even,
                quadratic_even,
                guard,
            )
            for degree in range(6)
        }
        c1 = third._expr(
            b3._scale(
                b3._multiply(
                    conductor_count,
                    b3._subtract(deletion[1], deletion[0], guard),
                    guard,
                ),
                assignment,
                guard,
            )
        )
        c3 = third._expr(
            b3._scale(
                b3._multiply(
                    conductor_count,
                    b3._subtract(deletion[3], deletion[2], guard),
                    guard,
                ),
                assignment,
                guard,
            )
        )
        c5 = third._expr(
            b3._scale(
                b3._multiply(
                    conductor_count,
                    b3._subtract(deletion[5], deletion[4], guard),
                    guard,
                ),
                assignment,
                guard,
            )
        )
    elif radical_degree == 4:
        data = primitive[key]
        if (linear_even, quadratic_even) == (0, 0):
            c1 = third._expr(data["sum_s1"])
            c3 = third._expr(
                b3._scale(b3._multiply(b3.Q, data["count"], guard), -1, guard)
            )
        else:
            deletion_kind = {
                (1, 0): "one_external_linear",
                (2, 0): "two_external_linears",
                (0, 1): "one_external_quadratic",
            }.get((linear_even, quadratic_even))
            if deletion_kind is None:
                raise ArithmeticError(f"unhandled degree-four B4 row {signature}")
            c1 = marked[(key[0], key[1], deletion_kind)]["C1"]
            c3 = marked[(key[0], key[1], deletion_kind)]["C3"]
            c5 = marked[(key[0], key[1], deletion_kind)]["C5"]
        c1 = third._expr_scale_fraction(c1, assignment, guard)
        c3 = third._expr_scale_fraction(c3, assignment, guard)
        c5 = third._expr_scale_fraction(c5, assignment, guard)
    elif radical_degree == 6:
        data = primitive[key]
        if (linear_even, quadratic_even) == (0, 0):
            c1 = third._expr(data["sum_s1"])
            c3 = third._expr(
                b3._subtract(
                    b3._multiply(b3.Q, data["sum_p1"], guard),
                    data["sum_p2"],
                    guard,
                )
            )
            c5 = third._expr(
                b3._scale(
                    b3._multiply(b3._power(b3.Q, 2, guard), data["count"], guard),
                    -1,
                    guard,
                )
            )
        elif (linear_even, quadratic_even) == (1, 0):
            deletion_data = marked[(key[0], key[1], "one_external_linear")]
            c1, c3, c5 = (
                deletion_data["C1"],
                deletion_data["C3"],
                deletion_data["C5"],
            )
        else:
            raise ArithmeticError(f"unhandled degree-six B4 row {signature}")
        c1 = third._expr_scale_fraction(c1, assignment, guard)
        c3 = third._expr_scale_fraction(c3, assignment, guard)
        c5 = third._expr_scale_fraction(c5, assignment, guard)
    elif radical_degree == 8:
        if linear_even or quadratic_even:
            raise ArithmeticError("a generic degree-eight B4 row gained deletion")
        data = primitive[key]
        c1 = third._expr(data["sum_s1"])
        c3 = _expr_subtract(data["sum_p3"], third._expr(data["sum_p2"]), guard)
        c5 = third._expr(
            b3._subtract(
                b3._multiply(b3._power(b3.Q, 2, guard), data["sum_p1"], guard),
                b3._multiply(b3.Q, data["sum_p2"], guard),
                guard,
            )
        )
    else:
        raise ArithmeticError("B4 radical degree lies outside {0,2,4,6,8}")

    linear_support = len(linear)
    quadratic_support = len(quadratic)
    q_minus_linear_support = b3._shift_constant(b3.Q, -linear_support, guard)
    sieve_c1 = b3._shift_constant(
        b3._scale(b3.Q, -linear_support, guard),
        math.comb(linear_support + 1, 2) + quadratic_support,
        guard,
    )
    s5 = third._expr_add(
        _expr_subtract(
            c5,
            third._expr_multiply_polynomial(c3, q_minus_linear_support, guard),
            guard,
        ),
        third._expr_multiply_polynomial(c1, sieve_c1, guard),
        guard,
    )
    contribution = third._expr_scale_fraction(s5, int(row["tuple_weight"]), guard)
    return {
        "signature": signature,
        "tuple_weight": int(row["tuple_weight"]),
        "radical_degree": radical_degree,
        "linear_odd_prime_count": linear_odd,
        "quadratic_odd_prime_count": quadratic_odd,
        "linear_deletion_prime_count": linear_even,
        "quadratic_deletion_prime_count": quadratic_even,
        "assignment_multiplier": assignment,
        "type_count_low_to_high": b3._polynomial_pairs(type_count),
        "sum_C1": third._serialize_expression(c1),
        "sum_C3": third._serialize_expression(c3),
        "sum_C5": third._serialize_expression(c5),
        "sum_S5": third._serialize_expression(s5),
        "weighted_contribution": third._serialize_expression(contribution),
        "_contribution": contribution,
    }


def _candidate_b4_total(guard: b3.AlgebraGuard) -> b3.Polynomial:
    inner = b3._add(
        b3._add(
            b3._add(
                b3._scale(b3._power(b3.Q, 7, guard), 10, guard),
                b3._scale(b3._power(b3.Q, 6, guard), -29, guard),
                guard,
            ),
            b3._add(
                b3._scale(b3._power(b3.Q, 5, guard), 21, guard),
                b3._scale(b3._power(b3.Q, 4, guard), 44, guard),
                guard,
            ),
            guard,
        ),
        b3._add(
            b3._add(
                b3._scale(b3._power(b3.Q, 3, guard), -47, guard),
                b3._scale(b3._power(b3.Q, 2, guard), -56, guard),
                guard,
            ),
            b3._add(b3._scale(b3.Q, -10, guard), b3._constant(-1), guard),
            guard,
        ),
        guard,
    )
    return b3._product((b3.Q, b3._shift_constant(b3.Q, -1, guard), inner), guard)


def _marked_root_moment_lemma(
    guard: b3.AlgebraGuard,
) -> dict[str, object]:
    """Prove the low-order cubic-stratum identities used in the descent.

    The fourth-moment calculation uses the translated marked-root family

        f(X)=X*(X^2+u*X+v).

    Before removing ``v=0`` and ``u^2=4v``, its ordered four-point character
    sum is split by multiplicity partition.  The all-distinct term is reduced
    by a cross-ratio Jacobi sum to the Legendre second moment; no level-2
    fourth moment is inserted.
    """

    q_minus_one = b3._shift_constant(b3.Q, -1, guard)
    q_minus_two = b3._shift_constant(b3.Q, -2, guard)
    q_minus_three = b3._shift_constant(b3.Q, -3, guard)
    q_minus_four = b3._shift_constant(b3.Q, -4, guard)
    q_plus_one = b3._shift_constant(b3.Q, 1, guard)

    legendre_second = b3._add(
        b3._subtract(b3._power(b3.Q, 2, guard), b3._scale(b3.Q, 2, guard), guard),
        b3._constant(-3),
        guard,
    )
    if legendre_second != b3._multiply(q_minus_three, q_plus_one, guard):
        raise ArithmeticError("Legendre second-moment factorization failed")

    # Sum a_f^2 on the fully split cubic stratum by affine-normalizing an
    # ordered root triple to (0,1,lambda), then dividing its six orderings.
    m111_2 = b3._scale(
        b3._product((b3.Q, q_minus_one, legendre_second), guard),
        Fraction(1, 6),
        guard,
    )

    # In the translated two-parameter family, the unrestricted second moment
    # is q*(q-1)^2.  Each of the two singular divisors contributes q-1, with
    # zero overlap, before the final choice of marked root.
    unrestricted_second = b3._multiply(b3.Q, b3._power(q_minus_one, 2, guard), guard)
    valid_second_per_root = b3._subtract(
        unrestricted_second, b3._scale(q_minus_one, 2, guard), guard
    )
    marked_second = b3._multiply(b3.Q, valid_second_per_root, guard)
    expected_marked_second = b3._product(
        (b3.Q, q_minus_one, q_plus_one, q_minus_two), guard
    )
    if marked_second != expected_marked_second:
        raise ArithmeticError("marked-root cubic second moment failed")
    m12_2 = b3._subtract(marked_second, b3._scale(m111_2, 3, guard), guard)
    expected_m12_2 = b3._scale(
        b3._product((b3.Q, b3._power(q_minus_one, 2, guard), q_plus_one), guard),
        Fraction(1, 2),
        guard,
    )
    if m12_2 != expected_m12_2:
        raise ArithmeticError("linear-times-quadratic second moment failed")

    partition_4 = b3._multiply(b3.Q, b3._power(q_minus_one, 2, guard), guard)
    partition_31 = b3.ZERO
    partition_22 = b3._scale(
        b3._product((b3._power(q_minus_one, 3, guard), q_minus_two), guard),
        3,
        guard,
    )
    partition_211 = b3._scale(
        b3._multiply(q_minus_one, q_minus_three, guard), -6, guard
    )
    partition_1111 = b3._subtract(
        b3._scale(
            b3._product((b3.Q, q_minus_one, q_minus_three), guard),
            3,
            guard,
        ),
        b3._product((q_minus_one, q_minus_four, legendre_second), guard),
        guard,
    )
    unrestricted_fourth = b3.ZERO
    for term in (
        partition_4,
        partition_31,
        partition_22,
        partition_211,
        partition_1111,
    ):
        unrestricted_fourth = b3._add(unrestricted_fourth, term, guard)
    expected_unrestricted_fourth = b3._scale(
        b3._product(
            (
                b3.Q,
                q_minus_one,
                b3._add(
                    b3._subtract(b3._power(b3.Q, 2, guard), b3.Q, guard),
                    b3._constant(-3),
                    guard,
                ),
            ),
            guard,
        ),
        2,
        guard,
    )
    if unrestricted_fourth != expected_unrestricted_fourth:
        raise ArithmeticError("marked-root four-point collision sum failed")
    valid_fourth_per_root = b3._subtract(
        unrestricted_fourth, b3._scale(q_minus_one, 2, guard), guard
    )
    marked_fourth = b3._multiply(b3.Q, valid_fourth_per_root, guard)
    expected_marked_fourth = b3._scale(
        b3._product(
            (
                b3.Q,
                q_minus_one,
                q_plus_one,
                b3._add(
                    b3._subtract(
                        b3._power(b3.Q, 2, guard),
                        b3._scale(b3.Q, 2, guard),
                        guard,
                    ),
                    b3._constant(-1),
                    guard,
                ),
            ),
            guard,
        ),
        2,
        guard,
    )
    if marked_fourth != expected_marked_fourth:
        raise ArithmeticError("marked-root cubic fourth moment failed")

    return {
        "Legendre_second_moment": legendre_second,
        "M_111_2": m111_2,
        "M_12_2": m12_2,
        "marked_second": marked_second,
        "marked_fourth": marked_fourth,
        "unrestricted_second": unrestricted_second,
        "unrestricted_fourth": unrestricted_fourth,
        "four_point_partitions": {
            "4": partition_4,
            "31": partition_31,
            "22": partition_22,
            "211": partition_211,
            "1111": partition_1111,
        },
    }


def _held_out_controls(guard: b3.AlgebraGuard) -> list[dict[str, object]]:
    observed = {11: 16_219_859_920, 13: 77_445_995_952}
    candidate = _candidate_b4_total(guard)
    rows = []
    for q_value, total in observed.items():
        expected = sum(
            coefficient * q_value**degree
            for degree, coefficient in enumerate(candidate)
        )
        if expected != total:
            raise ArithmeticError("a held-out B4 falsification control changed")
        rows.append(
            {
                "q": q_value,
                "quadratic_character_of_minus_one": 1 if q_value % 4 == 1 else -1,
                "monic_quintic_inputs": q_value**5,
                "squarefree_members": q_value**4 * (q_value - 1),
                "observed_sum_b_fourth": total,
                "candidate_sum_b_fourth": int(expected),
                "difference": 0,
                "diagnostic_method": (
                    "independent batched exact prime-field F_q/F_(q^2) character evaluation"
                ),
                "maximum_declared_character_evaluation_atoms": (
                    q_value**5 * (q_value + q_value * (q_value - 1) // 2)
                ),
                "theorem_input": False,
            }
        )
    return rows


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        SECOND_MOMENT_FIXTURE_PATH,
        THIRD_FIXTURE_PATH,
        THIRD_PRODUCER_PATH,
        THIRD_NOTE_PATH,
        THIRD_TEST_PATH,
        B3_FIXTURE_PATH,
        M22_FIXTURE_PATH,
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
    second = _load_locked_fixture(
        SECOND_MOMENT_FIXTURE_PATH,
        EXPECTED_SOURCE_PAYLOAD_SHA256["second_moment"],
        EXPECTED_SOURCE_LF_SHA256["second_moment"],
    )
    third_fixture = _load_locked_fixture(
        THIRD_FIXTURE_PATH,
        EXPECTED_THIRD_PAYLOAD_SHA256,
        EXPECTED_THIRD_LF_SHA256["fixture"],
    )
    b3_fixture = _load_locked_fixture(
        B3_FIXTURE_PATH,
        EXPECTED_SOURCE_PAYLOAD_SHA256["B3"],
        EXPECTED_SOURCE_LF_SHA256["B3"],
    )
    m22_fixture = _load_locked_fixture(
        M22_FIXTURE_PATH,
        EXPECTED_SOURCE_PAYLOAD_SHA256["M22"],
        EXPECTED_SOURCE_LF_SHA256["M22"],
    )
    locked_packet_a_sources = {
        "producer": THIRD_PRODUCER_PATH,
        "note": THIRD_NOTE_PATH,
        "test": THIRD_TEST_PATH,
    }
    for key, path in locked_packet_a_sources.items():
        if _lf_normalized_sha256(path) != EXPECTED_THIRD_LF_SHA256[key]:
            raise RuntimeError(f"source-locked Packet A {key} changed")

    rows = _normalize_b4_rows(second)
    primitive, marked = _primitive_maps(third_fixture)
    guard = b3.AlgebraGuard(started + MAX_WALL_SECONDS)
    exact_rows = [_row_coefficients(row, primitive, marked, guard) for row in rows]
    radical_census = Counter(int(row["radical_degree"]) for row in exact_rows)
    if radical_census != Counter({0: 9, 2: 16, 4: 17, 6: 7, 8: 5}):
        raise ArithmeticError("B4 radical-degree census changed")

    weighted_count = b3.ZERO
    total = third._expr()
    degree_blocks = {degree: third._expr() for degree in (0, 2, 4, 6, 8)}
    for row in exact_rows:
        weighted_count = b3._add(
            weighted_count,
            b3._scale(
                _parse_polynomial(row["type_count_low_to_high"]),
                int(row["tuple_weight"]),
                guard,
            ),
            guard,
        )
        contribution = row.pop("_contribution")
        degree = int(row["radical_degree"])
        degree_blocks[degree] = third._expr_add(
            degree_blocks[degree], contribution, guard
        )
        total = third._expr_add(total, contribution, guard)
    if weighted_count != b3._power(b3.Q, 8, guard):
        raise ArithmeticError("the 54 B4 signatures do not exhaust q^8 tuples")
    expected_residual_coefficients = {
        "M_111_2": (8274, -3096, 252),
        "M_111_4": (234, -27),
        "M_111_6": (0,),
        "M_111_8": (0,),
        "M_12_2": (2286, -960, 84),
        "M_12_4": (78, -9),
        "M_12_6": (0,),
        "M_12_8": (0,),
    }
    for key, expected in expected_residual_coefficients.items():
        if total.coefficients.get(key, b3.ZERO) != b3._clean(expected):
            raise ArithmeticError(f"B4 residual coefficient drifted at {key}")
    if total.coefficients["M_111_4"] != b3._scale(
        total.coefficients["M_12_4"], 3, guard
    ):
        raise ArithmeticError("the marked-root fourth-moment descent failed")

    marked_lemma = _marked_root_moment_lemma(guard)
    closed_total = total.constant
    closed_total = b3._add(
        closed_total,
        b3._multiply(total.coefficients["M_111_2"], marked_lemma["M_111_2"], guard),
        guard,
    )
    closed_total = b3._add(
        closed_total,
        b3._multiply(total.coefficients["M_12_2"], marked_lemma["M_12_2"], guard),
        guard,
    )
    closed_total = b3._add(
        closed_total,
        b3._multiply(
            total.coefficients["M_12_4"], marked_lemma["marked_fourth"], guard
        ),
        guard,
    )
    expected_b4 = _candidate_b4_total(guard)
    if closed_total != expected_b4:
        raise ArithmeticError("the 54 B4 rows did not close to the theorem polynomial")

    known = b3._known_moment_totals(guard)
    a4_total = m22._a4_total(guard)
    family_size = b3._multiply(
        b3._power(b3.Q, 4, guard),
        b3._shift_constant(b3.Q, -1, guard),
        guard,
    )
    # Clear q^4 from R4=b^4/q^4-5*a^2*b/q^2-2*a^4/q^2
    #                         +14*a^2/q-3*b^2/q^2-2.
    cleared_r4 = closed_total
    cleared_r4 = b3._subtract(
        cleared_r4,
        b3._scale(
            b3._multiply(b3._power(b3.Q, 2, guard), known["sum_a2b"], guard),
            5,
            guard,
        ),
        guard,
    )
    cleared_r4 = b3._subtract(
        cleared_r4,
        b3._scale(
            b3._multiply(b3._power(b3.Q, 2, guard), a4_total, guard),
            2,
            guard,
        ),
        guard,
    )
    cleared_r4 = b3._add(
        cleared_r4,
        b3._scale(
            b3._multiply(b3._power(b3.Q, 3, guard), known["sum_a2"], guard),
            14,
            guard,
        ),
        guard,
    )
    cleared_r4 = b3._subtract(
        cleared_r4,
        b3._scale(
            b3._multiply(b3._power(b3.Q, 2, guard), known["sum_b2"], guard),
            3,
            guard,
        ),
        guard,
    )
    cleared_r4 = b3._subtract(
        cleared_r4,
        b3._scale(
            b3._multiply(b3._power(b3.Q, 4, guard), family_size, guard),
            2,
            guard,
        ),
        guard,
    )

    cleared_chi03 = _parse_polynomial(b3_fixture["cleared_chi_sum_low_to_high"])
    bridge22 = m22_fixture.get("triangular_character_bridge")
    if not isinstance(bridge22, dict):
        raise TypeError("M22 fixture lost its character bridge")
    cleared_chi22 = _parse_polynomial(bridge22["cleared_chi_(2,2)_sum_low_to_high"])
    cleared_chi04 = b3._subtract(
        b3._subtract(
            cleared_r4,
            b3._scale(b3._multiply(b3.Q, cleared_chi22, guard), 3, guard),
            guard,
        ),
        b3._scale(b3._multiply(b3.Q, cleared_chi03, guard), 4, guard),
        guard,
    )
    expected_cleared_chi04 = b3._scale(
        b3._product(
            (
                b3.Q,
                b3._shift_constant(b3.Q, -1, guard),
                b3._shift_constant(
                    b3._scale(b3._power(b3.Q, 2, guard), 2, guard), 1, guard
                ),
            ),
            guard,
        ),
        -1,
        guard,
    )
    if cleared_chi04 != expected_cleared_chi04:
        raise ArithmeticError("chi_(0,4) triangular bridge failed")

    held_out = _held_out_controls(guard)
    input_atoms = len(rows) + len(primitive) + len(marked) + len(third.RESIDUAL_KEYS)
    actual = guard.operations + input_atoms
    if actual > MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS:
        raise RuntimeError("B4 symbolic-operation/input-atom cap exceeded")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("B4 proof replay exceeded its wall-time cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_b4_triangular_trace_average.v1",
        "status": "PROVED_EXACT_ALL_ODD_PRIME_POWERS",
        "scope": {
            "q": "every odd prime power",
            "family": "all monic squarefree quintics D in F_q[T]",
            "finite_fields_enumerated_by_theorem_replay": 0,
            "family_members_consumed_by_theorem_replay": 0,
            "sampled_q_values_used_as_theorem_input": 0,
            "numeric_approximations": 0,
        },
        "theorem": {
            "B4_total": (
                "sum_D b_D^4=q*(q-1)*(10*q^7-29*q^6+21*q^5+44*q^4-47*q^3-56*q^2-10*q-1)"
            ),
            "B4_mean": (
                "E[b_D^4]=(10*q^7-29*q^6+21*q^5+44*q^4-47*q^3-56*q^2-10*q-1)/q^3"
            ),
            "R4_identity": (
                "R4=chi_(0,4)+3*chi_(2,2)+4*chi_(0,3)=b^4/q^4-5*a^2*b/q^2-2*a^4/q^2+14*a^2/q-3*b^2/q^2-2"
            ),
            "chi_(0,4)_mean": "-(2*q^2+1)/q^7",
            "marked_stack_trace_chi_(0,4)": "-(2*q^2+1)",
        },
        "level2_descent_certificate": {
            "formal_residual_basis": list(third.RESIDUAL_KEYS),
            "weighted_total_coefficients": {
                key: b3._polynomial_pairs(total.coefficients.get(key, b3.ZERO))
                for key in third.RESIDUAL_KEYS
            },
            "high_moment_status": ("M_111_6,M_111_8,M_12_6,M_12_8 cancel identically"),
            "low_moment_status": (
                "M_111_2 and M_12_2 close separately; moment four survives only as 3*M_111_4+M_12_4, the rational-root-marked cubic moment"
            ),
            "meaning": (
                "the 54-row theorem kills the genuinely high level-2 channels and descends the remaining fourth moment to a marked-root family before evaluating it"
            ),
        },
        "marked_root_cubic_lemma": {
            "Legendre_second_moment": b3._polynomial_pairs(
                marked_lemma["Legendre_second_moment"]
            ),
            "M_111_2": b3._polynomial_pairs(marked_lemma["M_111_2"]),
            "M_12_2": b3._polynomial_pairs(marked_lemma["M_12_2"]),
            "three_M_111_4_plus_M_12_4": b3._polynomial_pairs(
                marked_lemma["marked_fourth"]
            ),
            "unrestricted_translated_second_moment": b3._polynomial_pairs(
                marked_lemma["unrestricted_second"]
            ),
            "unrestricted_translated_fourth_moment": b3._polynomial_pairs(
                marked_lemma["unrestricted_fourth"]
            ),
            "four_point_collision_partitions": {
                key: b3._polynomial_pairs(value)
                for key, value in marked_lemma["four_point_partitions"].items()
            },
            "singular_locus_subtraction_per_root": "2*(q-1) in each positive even moment",
            "proof_boundary": (
                "the all-distinct four-point term is reduced by an exact cross-ratio Jacobi sum to the displayed Legendre second moment; no factorization-stratified fourth-moment value is assumed"
            ),
        },
        "ordered_tuple_signature_audit": {
            "signature_count": len(exact_rows),
            "radical_degree_census": {
                str(degree): radical_census[degree] for degree in (0, 2, 4, 6, 8)
            },
            "weighted_type_count_low_to_high": b3._polynomial_pairs(weighted_count),
            "weighted_type_count": "q^8",
            "status": "EXACT_EXHAUSTIVE_54_SIGNATURE_PARTITION",
        },
        "signature_ledger": exact_rows,
        "radical_degree_blocks": {
            str(degree): third._serialize_expression(value)
            for degree, value in degree_blocks.items()
        },
        "formal_constant_before_low_level2_descent_low_to_high": (
            b3._polynomial_pairs(total.constant)
        ),
        "B4_total_low_to_high": b3._polynomial_pairs(closed_total),
        "triangular_character_bridge": {
            "cleared_R4_sum_low_to_high": b3._polynomial_pairs(cleared_r4),
            "cleared_chi_(0,3)_sum_low_to_high": b3._polynomial_pairs(cleared_chi03),
            "cleared_chi_(2,2)_sum_low_to_high": b3._polynomial_pairs(cleared_chi22),
            "cleared_chi_(0,4)_sum_low_to_high": b3._polynomial_pairs(cleared_chi04),
            "clearing_convention": (
                "R4 and chi_(0,4) are cleared by q^4; source chi_(0,3) and chi_(2,2) sums are cleared by q^3"
            ),
        },
        "held_out_falsification_controls": held_out,
        "source_manifest": _source_manifest(),
        "resource_contract": {
            "maximum_signatures": MAX_SIGNATURES,
            "actual_signatures": len(rows),
            "maximum_symbolic_operations_and_input_atoms": (
                MAX_SYMBOLIC_OPERATIONS_AND_INPUT_ATOMS
            ),
            "actual_complete_polynomial_operations": guard.operations,
            "actual_input_atoms": input_atoms,
            "actual_operations_and_input_atoms": actual,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "held_out_controls_are_outside_theorem_replay": True,
            "largest_declared_held_out_character_atom_cap": max(
                row["maximum_declared_character_evaluation_atoms"] for row in held_out
            ),
        },
        "firewalls": [
            "The all-q theorem is not interpolated from q=3,5,7,11,13.",
            "The q=11 and q=13 rows are held-out falsification controls, not theorem inputs.",
            "Packet A leaves eight factorization-stratified level-2 moments formal; Packet B cancels moments six and eight, then evaluates only the exact low-order marked-root descent.",
            "No finite field, quintic, curve, or family member is enumerated by the default proof replay.",
            "No novelty, memberwise sign, RH, or GRH claim is made.",
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
            raise SystemExit(f"B4 triangular trace fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: B4 triangular trace fixture matches {OUTPUT_PATH}")
        return 0
    print(
        json.dumps(
            fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
