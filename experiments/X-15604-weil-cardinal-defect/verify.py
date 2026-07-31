#!/usr/bin/env python3
"""Exact rational replay for Weil-cardinal zero-defect packets.

This checker performs only finite algebra. It does not evaluate Xi, certify zeros,
or prove that a listed zero configuration belongs to the Riemann zeta function.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15604-weil-cardinal-defect.v1"


class VerificationError(ValueError):
    pass


def require_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerificationError(f"{name} must be an integer")
    return value


def parse_fraction(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise VerificationError(f"{name} must be a rational object")
    numerator = require_int(value.get("numerator"), f"{name}.numerator")
    denominator = require_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise VerificationError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def dump_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def swap_rows_cols(matrix: list[list[Fraction]], i: int, j: int) -> None:
    matrix[i], matrix[j] = matrix[j], matrix[i]
    for row in matrix:
        row[i], row[j] = row[j], row[i]


def inertia_symmetric(matrix: list[list[Fraction]]) -> tuple[int, int, int]:
    """Exact inertia by symmetric congruence elimination."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise VerificationError("matrix is not square")
    a = [row[:] for row in matrix]
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise VerificationError("matrix is not symmetric")

    positive = negative = zero = 0
    k = 0
    while k < n:
        pivot = next((i for i in range(k, n) if a[i][i] != 0), None)
        if pivot is not None:
            swap_rows_cols(a, k, pivot)
            p = a[k][k]
            if p > 0:
                positive += 1
            else:
                negative += 1
            for i in range(k + 1, n):
                for j in range(i, n):
                    value = a[i][j] - a[i][k] * a[j][k] / p
                    a[i][j] = value
                    a[j][i] = value
            k += 1
            continue

        pair = None
        for i in range(k, n):
            for j in range(i + 1, n):
                if a[i][j] != 0:
                    pair = (i, j)
                    break
            if pair is not None:
                break

        if pair is None:
            zero += n - k
            break

        i, j = pair
        swap_rows_cols(a, k, i)
        if j == k:
            j = i
        swap_rows_cols(a, k + 1, j)
        b = a[k][k + 1]
        positive += 1
        negative += 1
        inv01 = Fraction(1, 1) / b
        for r in range(k + 2, n):
            for s in range(r, n):
                ur0, ur1 = a[r][k], a[r][k + 1]
                us0, us1 = a[s][k], a[s][k + 1]
                correction = ur0 * inv01 * us1 + ur1 * inv01 * us0
                value = a[r][s] - correction
                a[r][s] = value
                a[s][r] = value
        k += 2

    return positive, negative, zero


def quadratic(matrix: list[list[Fraction]], vector: list[Fraction]) -> Fraction:
    n = len(matrix)
    if len(vector) != n:
        raise VerificationError("vector dimension mismatch")
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(n)
        for j in range(n)
    )


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise VerificationError("schema mismatch")
    if data.get("classification") not in {
        "SYNTHETIC_ZERO_CONFIGURATION",
        "DIRECTED_ZETA_ZERO_CONFIGURATION",
    }:
        raise VerificationError("unsupported classification")

    radical_dimension = require_int(data.get("radical_dimension"), "radical_dimension")
    if radical_dimension < 0:
        raise VerificationError("radical_dimension must be nonnegative")

    raw_zeros = data.get("zeros")
    if not isinstance(raw_zeros, list) or not raw_zeros:
        raise VerificationError("zeros must be a nonempty list")

    zeros: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(raw_zeros):
        if not isinstance(row, dict):
            raise VerificationError(f"zeros[{index}] must be an object")
        zero_id = row.get("id")
        conjugate = row.get("conjugate")
        if not isinstance(zero_id, str) or not zero_id or zero_id in by_id:
            raise VerificationError("zero ids must be unique nonempty strings")
        if not isinstance(conjugate, str) or not conjugate:
            raise VerificationError(f"zeros[{index}].conjugate must be a string")
        multiplicity = require_int(row.get("multiplicity"), f"zeros[{index}].multiplicity")
        if multiplicity <= 0:
            raise VerificationError("zero multiplicities must be positive")
        deflated = row.get("deflated")
        if not isinstance(deflated, bool):
            raise VerificationError("deflated must be Boolean")
        parsed = {
            "id": zero_id,
            "conjugate": conjugate,
            "multiplicity": multiplicity,
            "deflated": deflated,
        }
        zeros.append(parsed)
        by_id[zero_id] = parsed

    for row in zeros:
        conjugate = by_id.get(row["conjugate"])
        if conjugate is None:
            raise VerificationError(f"missing conjugate for {row['id']}")
        if conjugate["conjugate"] != row["id"]:
            raise VerificationError("conjugation is not an involution")
        if conjugate["multiplicity"] != row["multiplicity"]:
            raise VerificationError("conjugate multiplicities differ")
        if row["deflated"] and row["conjugate"] != row["id"]:
            raise VerificationError("only certified critical-line zeros may be deflated")

    dimension = radical_dimension + len(zeros)
    index_by_id = {
        row["id"]: radical_dimension + index for index, row in enumerate(zeros)
    }

    gram = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
    for row in zeros:
        i = index_by_id[row["id"]]
        j = index_by_id[row["conjugate"]]
        gram[i][j] = Fraction(row["multiplicity"])

    positive, negative, zero = inertia_symmetric(gram)

    residual = [row[:] for row in gram]
    deflated_ids: list[str] = []
    for row in zeros:
        if row["deflated"]:
            i = index_by_id[row["id"]]
            residual[i][i] -= Fraction(row["multiplicity"])
            deflated_ids.append(row["id"])

    residual_positive, residual_negative, residual_zero = inertia_symmetric(residual)

    expected = data.get("expected")
    if not isinstance(expected, dict):
        raise VerificationError("expected object missing")
    claimed_inertia = expected.get("inertia")
    if not isinstance(claimed_inertia, dict):
        raise VerificationError("expected.inertia missing")
    claimed_tuple = (
        require_int(claimed_inertia.get("positive"), "expected.inertia.positive"),
        require_int(claimed_inertia.get("negative"), "expected.inertia.negative"),
        require_int(claimed_inertia.get("zero"), "expected.inertia.zero"),
    )
    if claimed_tuple != (positive, negative, zero):
        raise VerificationError("claimed inertia mismatch")

    claimed_residual = expected.get("residual_inertia")
    if not isinstance(claimed_residual, dict):
        raise VerificationError("expected.residual_inertia missing")
    claimed_residual_tuple = (
        require_int(claimed_residual.get("positive"), "expected.residual_inertia.positive"),
        require_int(claimed_residual.get("negative"), "expected.residual_inertia.negative"),
        require_int(claimed_residual.get("zero"), "expected.residual_inertia.zero"),
    )
    if claimed_residual_tuple != (
        residual_positive,
        residual_negative,
        residual_zero,
    ):
        raise VerificationError("claimed residual inertia mismatch")

    pair = expected.get("off_line_negative_pair")
    negative_witness = None
    if pair is not None:
        if (
            not isinstance(pair, list)
            or len(pair) != 2
            or not all(isinstance(item, str) for item in pair)
        ):
            raise VerificationError("off_line_negative_pair must contain two ids")
        left, right = pair
        if left not in by_id or right not in by_id:
            raise VerificationError("negative-pair id not found")
        if by_id[left]["conjugate"] != right or by_id[right]["conjugate"] != left:
            raise VerificationError("negative pair is not conjugate")
        if left == right:
            raise VerificationError("negative pair must be off the real axis")
        vector = [Fraction(0) for _ in range(dimension)]
        vector[index_by_id[left]] = Fraction(1)
        vector[index_by_id[right]] = Fraction(-1)
        value = quadratic(gram, vector)
        claimed_value = parse_fraction(
            expected.get("off_line_negative_quadratic"),
            "expected.off_line_negative_quadratic",
        )
        if value != claimed_value or value >= 0:
            raise VerificationError("off-line negative witness mismatch")
        negative_witness = {
            "pair": pair,
            "quadratic": dump_fraction(value),
            "coordinate_norm_squared": dump_fraction(Fraction(2)),
            "rayleigh": dump_fraction(value / 2),
        }

    schur = data.get("schur_control")
    schur_output = None
    if schur is not None:
        if not isinstance(schur, dict):
            raise VerificationError("schur_control must be an object")
        ideal_min = parse_fraction(schur.get("ideal_min"), "schur_control.ideal_min")
        block_error = parse_fraction(
            schur.get("block_error"), "schur_control.block_error"
        )
        cross_squared = parse_fraction(
            schur.get("cross_squared"), "schur_control.cross_squared"
        )
        complement_floor = parse_fraction(
            schur.get("complement_floor"), "schur_control.complement_floor"
        )
        if block_error < 0 or cross_squared < 0 or complement_floor <= 0:
            raise VerificationError("invalid Schur-control bounds")
        floor = ideal_min - block_error - cross_squared / complement_floor
        claimed_floor = parse_fraction(
            schur.get("claimed_floor"), "schur_control.claimed_floor"
        )
        if floor != claimed_floor:
            raise VerificationError("claimed Schur floor mismatch")
        schur_output = {
            "ideal_min": dump_fraction(ideal_min),
            "block_error": dump_fraction(block_error),
            "cross_squared": dump_fraction(cross_squared),
            "complement_floor": dump_fraction(complement_floor),
            "floor": dump_fraction(floor),
        }

    output: dict[str, Any] = {
        "schema": SCHEMA,
        "classification": data["classification"],
        "dimension": dimension,
        "radical_dimension": radical_dimension,
        "zero_ids": [row["id"] for row in zeros],
        "deflated_critical_line_ids": deflated_ids,
        "inertia": {"positive": positive, "negative": negative, "zero": zero},
        "residual_inertia": {
            "positive": residual_positive,
            "negative": residual_negative,
            "zero": residual_zero,
        },
        "negative_witness": negative_witness,
        "schur_control": schur_output,
    }
    output["proof_object_sha256"] = canonical_sha256(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.certificate.read_text())
        output = verify(data)
        status = 0
    except Exception as exc:
        output = {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}
        status = 2

    text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
