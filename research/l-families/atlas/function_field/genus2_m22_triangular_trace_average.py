#!/usr/bin/env python3
"""Exact all-field proof of the genus-two M22 triangular trace average.

This packet applies the source-locked primitive sign-inventory engine from
the B3 theorem to the 20 exact signatures of

    sum_(D in H_5(q)) a_D^2*b_D^2.

It performs no finite-field or family-member enumeration and uses no sampled
q value as a theorem input.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections import Counter
from collections.abc import Mapping, Sequence
from pathlib import Path

import genus2_b3_primitive_trace_average as b3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_m22_triangular_trace_average.json"
NOTE_PATH = HERE / "GENUS2_M22_TRIANGULAR_TRACE_AVERAGE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_m22_triangular_trace_average.py"

SECOND_MOMENT_FIXTURE_PATH = HERE / "genus2_second_moment_reduction.json"
B3_FIXTURE_PATH = HERE / "genus2_b3_primitive_trace_average.json"
B3_PRODUCER_PATH = HERE / "genus2_b3_primitive_trace_average.py"
B3_NOTE_PATH = HERE / "GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md"
MOMENT_NOTE_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"

EXPECTED_PAYLOAD_SHA256 = {
    "second_moment_fixture": "55c5c9ef04a65ca46044ac1d76c76f33afc02b51c2d38a8ca196b99498ee16ec",
    "B3_fixture": "e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd",
}
EXPECTED_LF_SHA256 = {
    "second_moment_fixture": "0966565c0b29d7bf85f6ad20f8c6634365a8fff674e3c3b06589125fe0bdbaf0",
    "B3_fixture": "5ecc6006014a159a4030218977c89f58c63334461a568b7a67d36130bae1c50b",
    "B3_producer": "fd180499468a3672120fc1794109f12b4fb027530f881104181809ee5d6caa4c",
    "B3_note": "36e6aa856931e1171cea57243ea7e6a161c6ecd01833eb80b04e1ae57b296d83",
    "moment_note": "69272720e27f9630220be0fc083cd16bb22a94c73b57b466740aa4b77dcc6277",
}

MAX_SIGNATURES = 20
MAX_PRIMITIVE_TYPES = 7
MAX_SYMBOLIC_OPERATIONS = 4096
MAX_WALL_SECONDS = 5.0

EXPECTED_DEGREE_BLOCKS = {
    0: (0, -184, 504, -579, 407, -219, 97, -32, 6),
    2: (0, 1400, -2801, 1897, -559, 63),
    4: (0, -2577, 4132, -1463, -367, 354, -87, 8),
    6: (0, 1364, -1814, 147, 469, -184, 14, 5, -1),
}
EXPECTED_M22_TOTAL = (0, 3, 21, 2, -50, 14, 24, -19, 5)


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
        raise TypeError(f"expected object fixture at {path}")
    claimed = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload) or claimed != expected_payload:
        raise ValueError(f"source-locked payload mismatch at {path}")
    return fixture


def _verify_dependency_hashes() -> None:
    actual = {
        "second_moment_fixture": _lf_normalized_sha256(SECOND_MOMENT_FIXTURE_PATH),
        "B3_fixture": _lf_normalized_sha256(B3_FIXTURE_PATH),
        "B3_producer": _lf_normalized_sha256(B3_PRODUCER_PATH),
        "B3_note": _lf_normalized_sha256(B3_NOTE_PATH),
        "moment_note": _lf_normalized_sha256(MOMENT_NOTE_PATH),
    }
    if actual != EXPECTED_LF_SHA256:
        raise RuntimeError("an M22 source-locked dependency changed")


def _normalize_m22_rows(fixture: Mapping[str, object]) -> list[dict[str, object]]:
    blocks = fixture.get("signature_blocks")
    if not isinstance(blocks, dict):
        raise TypeError("second-moment fixture lost its signature blocks")
    block = blocks.get("M22")
    if not isinstance(block, dict):
        raise TypeError("second-moment fixture lost its M22 block")
    source_rows = block.get("signatures")
    if not isinstance(source_rows, list) or len(source_rows) != MAX_SIGNATURES:
        raise ValueError("M22 source is not the pinned 20-signature ledger")

    rows: list[dict[str, object]] = []
    for source in source_rows:
        if not isinstance(source, dict):
            raise TypeError("an M22 signature row is not an object")
        radical = source.get("odd_radical")
        type_count = source.get("type_count")
        if not isinstance(radical, dict) or not isinstance(type_count, dict):
            raise TypeError("an M22 signature row lost nested data")
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


def _serialize_polynomial(value: b3.Polynomial) -> list[list[int]]:
    return b3._polynomial_pairs(value)


def _a4_total(guard: b3.AlgebraGuard) -> b3.Polynomial:
    inner = b3._add(
        b3._add(
            b3._scale(b3._power(b3.Q, 4, guard), 3, guard),
            b3._scale(b3._power(b3.Q, 3, guard), -10, guard),
            guard,
        ),
        b3._add(
            b3._add(
                b3._scale(b3._power(b3.Q, 2, guard), 15, guard),
                b3._scale(b3.Q, -3, guard),
                guard,
            ),
            b3._constant(-11),
            guard,
        ),
        guard,
    )
    return b3._product(
        (
            b3.Q,
            b3._shift_constant(b3.Q, -1, guard),
            b3._shift_constant(b3.Q, 1, guard),
            inner,
        ),
        guard,
    )


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        SECOND_MOMENT_FIXTURE_PATH,
        B3_FIXTURE_PATH,
        B3_PRODUCER_PATH,
        B3_NOTE_PATH,
        MOMENT_NOTE_PATH,
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
    _verify_dependency_hashes()
    second = _load_locked_fixture(
        SECOND_MOMENT_FIXTURE_PATH,
        EXPECTED_PAYLOAD_SHA256["second_moment_fixture"],
        EXPECTED_LF_SHA256["second_moment_fixture"],
    )
    b3_fixture = _load_locked_fixture(
        B3_FIXTURE_PATH,
        EXPECTED_PAYLOAD_SHA256["B3_fixture"],
        EXPECTED_LF_SHA256["B3_fixture"],
    )
    rows = _normalize_m22_rows(second)

    guard = b3.AlgebraGuard(started + MAX_WALL_SECONDS)
    primitive_types = ((4, 0), (2, 1), (0, 2), (6, 0), (4, 1), (2, 2), (0, 3))
    primitive = {
        factor_type: b3._primitive_moments(*factor_type, guard)
        for factor_type in primitive_types
    }
    exact_rows = [b3._row_aggregates(row, primitive, guard) for row in rows]

    radical_census = Counter(int(row["radical_degree"]) for row in exact_rows)
    if radical_census != Counter({0: 4, 2: 8, 4: 5, 6: 3}):
        raise ArithmeticError("the M22 radical-degree census changed")

    weighted_tuple_count = b3.ZERO
    degree_blocks = {degree: b3.ZERO for degree in (0, 2, 4, 6)}
    for row in exact_rows:
        weighted_tuple_count = b3._add(
            weighted_tuple_count,
            b3._scale(
                b3._polynomial_from_pairs(row["type_count_low_to_high"]),
                int(row["tuple_weight"]),
                guard,
            ),
            guard,
        )
        degree = int(row["radical_degree"])
        degree_blocks[degree] = b3._add(
            degree_blocks[degree], row.pop("_contribution"), guard
        )
    if weighted_tuple_count != b3._power(b3.Q, 6, guard):
        raise ArithmeticError("the 20 M22 signatures do not exhaust q^6 tuples")
    for degree, expected in EXPECTED_DEGREE_BLOCKS.items():
        if degree_blocks[degree] != b3._clean(expected):
            raise ArithmeticError(f"M22 radical-degree {degree} block drifted")

    m22_total = b3.ZERO
    for value in degree_blocks.values():
        m22_total = b3._add(m22_total, value, guard)
    if m22_total != b3._clean(EXPECTED_M22_TOTAL):
        raise ArithmeticError("the 20 M22 rows did not close")

    target_inner = b3._add(
        b3._add(
            b3._add(
                b3._scale(b3._power(b3.Q, 5, guard), 5, guard),
                b3._scale(b3._power(b3.Q, 4, guard), -19, guard),
                guard,
            ),
            b3._add(
                b3._scale(b3._power(b3.Q, 3, guard), 29, guard),
                b3._scale(b3._power(b3.Q, 2, guard), -5, guard),
                guard,
            ),
            guard,
        ),
        b3._add(b3._scale(b3.Q, -21, guard), b3._constant(-3), guard),
        guard,
    )
    expected_total = b3._product(
        (
            b3.Q,
            b3._shift_constant(b3.Q, -1, guard),
            b3._shift_constant(b3.Q, 1, guard),
            target_inner,
        ),
        guard,
    )
    if m22_total != expected_total:
        raise ArithmeticError("factored M22 theorem target failed")

    known = b3._known_moment_totals(guard)
    a4_total = _a4_total(guard)
    family_size = b3._multiply(
        b3._power(b3.Q, 4, guard),
        b3._shift_constant(b3.Q, -1, guard),
        guard,
    )

    # Clear q^3 from R22=a^2*b^2/q^3-3*a^2*b/q^2-a^4/q^2+5*a^2/q-1.
    cleared_r22 = m22_total
    cleared_r22 = b3._subtract(
        cleared_r22,
        b3._scale(b3._multiply(b3.Q, known["sum_a2b"], guard), 3, guard),
        guard,
    )
    cleared_r22 = b3._subtract(cleared_r22, b3._multiply(b3.Q, a4_total, guard), guard)
    cleared_r22 = b3._add(
        cleared_r22,
        b3._scale(
            b3._multiply(b3._power(b3.Q, 2, guard), known["sum_a2"], guard),
            5,
            guard,
        ),
        guard,
    )
    cleared_r22 = b3._subtract(
        cleared_r22,
        b3._multiply(b3._power(b3.Q, 3, guard), family_size, guard),
        guard,
    )
    r22_numerator = b3._add(
        b3._add(
            b3._power(b3.Q, 4, guard),
            b3._scale(b3._power(b3.Q, 3, guard), 2, guard),
            guard,
        ),
        b3._add(
            b3._scale(b3._power(b3.Q, 2, guard), -1, guard),
            b3._add(b3._scale(b3.Q, -4, guard), b3._constant(-3), guard),
            guard,
        ),
        guard,
    )
    expected_cleared_r22 = b3._product(
        (b3.Q, b3._shift_constant(b3.Q, -1, guard), r22_numerator), guard
    )
    if cleared_r22 != expected_cleared_r22:
        raise ArithmeticError("R22 triangular lower-moment bridge failed")

    source_cleared_chi03 = b3._polynomial_from_pairs(
        b3_fixture["cleared_chi_sum_low_to_high"]
    )
    expected_source_chi03 = b3._product(
        (
            b3.Q,
            b3._shift_constant(b3.Q, -1, guard),
            b3._add(
                b3._subtract(
                    b3._power(b3.Q, 4, guard), b3._scale(b3.Q, 2, guard), guard
                ),
                b3._constant(-1),
                guard,
            ),
        ),
        guard,
    )
    if source_cleared_chi03 != expected_source_chi03:
        raise ArithmeticError("source-locked B3 chi_(0,3) theorem changed")
    cleared_chi22 = b3._subtract(cleared_r22, source_cleared_chi03, guard)
    chi22_numerator = b3._add(
        b3._add(
            b3._scale(b3._power(b3.Q, 3, guard), 2, guard),
            b3._scale(b3._power(b3.Q, 2, guard), -1, guard),
            guard,
        ),
        b3._add(b3._scale(b3.Q, -2, guard), b3._constant(-2), guard),
        guard,
    )
    expected_cleared_chi22 = b3._product(
        (b3.Q, b3._shift_constant(b3.Q, -1, guard), chi22_numerator), guard
    )
    if cleared_chi22 != expected_cleared_chi22:
        raise ArithmeticError("chi_(2,2) subtraction bridge failed")

    actual_atoms = guard.operations + len(rows) + len(primitive_types)
    if actual_atoms > MAX_SYMBOLIC_OPERATIONS:
        raise RuntimeError("M22 declared operation/signature atom cap exceeded")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("M22 proof replay exceeded its wall-time cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_m22_triangular_trace_average.v1",
        "status": "PROVED_EXACT_ALL_ODD_PRIME_POWERS",
        "scope": {
            "q": "every odd prime power",
            "family": "all monic squarefree quintics D in F_q[T]",
            "finite_fields_enumerated": 0,
            "family_members_consumed": 0,
            "sampled_q_values_used": 0,
            "numeric_approximations": 0,
        },
        "theorem": {
            "M22_total": (
                "sum_D a_D^2*b_D^2=q*(q-1)*(q+1)*(5*q^5-19*q^4+29*q^3-5*q^2-21*q-3)"
            ),
            "M22_mean": ("E[a_D^2*b_D^2]=(q+1)*(5*q^5-19*q^4+29*q^3-5*q^2-21*q-3)/q^3"),
            "R22_mean": "(q^4+2*q^3-q^2-4*q-3)/q^6",
            "chi_(2,2)_mean": "(2*q^3-q^2-2*q-2)/q^6",
            "marked_stack_trace_chi_(2,2)": "2*q^3-q^2-2*q-2",
        },
        "triangular_character_bridge": {
            "R22_identity": (
                "R22=chi_(0,3)+chi_(2,2)=a^2*b^2/q^3-3*a^2*b/q^2-a^4/q^2+5*a^2/q-1"
            ),
            "cleared_R22_sum_low_to_high": _serialize_polynomial(cleared_r22),
            "cleared_chi_(0,3)_sum_low_to_high": _serialize_polynomial(
                source_cleared_chi03
            ),
            "cleared_chi_(2,2)_sum_low_to_high": _serialize_polynomial(cleared_chi22),
            "clearing_convention": (
                "each cleared sum is q^3 times the corresponding family sum"
            ),
        },
        "ordered_tuple_signature_audit": {
            "signature_count": len(exact_rows),
            "radical_degree_census": {
                str(degree): radical_census[degree] for degree in (0, 2, 4, 6)
            },
            "weighted_type_count_low_to_high": _serialize_polynomial(
                weighted_tuple_count
            ),
            "weighted_type_count": "q^6",
            "slot_types": "two ordered monic-linear slots and two ordered monic-quadratic slots",
            "status": "EXACT_EXHAUSTIVE_20_SIGNATURE_PARTITION",
        },
        "signature_ledger": exact_rows,
        "radical_degree_blocks": {
            str(degree): _serialize_polynomial(value)
            for degree, value in degree_blocks.items()
        },
        "M22_total_low_to_high": _serialize_polynomial(m22_total),
        "reused_primitive_aggregate_lemma": {
            "source": "GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md equations (7)-(15)",
            "source_payload_sha256": b3_fixture["payload_sha256"],
            "meaning": (
                "the same exact conductor-type sums of s1, s1^2, s2, p1, p2 "
                "and marked deletion factors are reweighted by the M22 slot multiplicities"
            ),
            "new_fitted_or_sampled_primitive_average": False,
        },
        "source_manifest": _source_manifest(),
        "resource_contract": {
            "maximum_signatures": MAX_SIGNATURES,
            "actual_signatures": len(rows),
            "maximum_primitive_types": MAX_PRIMITIVE_TYPES,
            "actual_primitive_types": len(primitive_types),
            "maximum_symbolic_operations_and_input_atoms": MAX_SYMBOLIC_OPERATIONS,
            "actual_symbolic_operations": guard.operations,
            "actual_operations_and_input_atoms": actual_atoms,
            "symbolic_operation_semantics": (
                "one operation is one complete-polynomial add, scale, multiply, "
                "or power step; signature and primitive-type inputs are added as atoms"
            ),
            "maximum_wall_seconds": MAX_WALL_SECONDS,
        },
        "firewalls": [
            "The all-q theorem is not inferred from the q=3,5,7 aggregate controls.",
            "No finite field, quintic, curve, or family member is enumerated.",
            "Composite-denominator even-exponent primes remain deletion factors exactly as in the B3 theorem.",
            "The chi_(2,2) result depends on the separately source-locked chi_(0,3) theorem.",
            "No memberwise sign, novelty, RH, or GRH claim is made.",
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
            raise SystemExit(f"M22 triangular trace fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: M22 triangular trace fixture matches {OUTPUT_PATH}")
        return 0
    print(
        json.dumps(
            fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
