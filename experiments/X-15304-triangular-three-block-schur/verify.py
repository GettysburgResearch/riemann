#!/usr/bin/env python3
"""Exact rational verifier for the triangular three-block Schur floor.

The checker verifies the strict finite version of L-15306. It uses only
integers and fractions.Fraction. All analytic/source-normalization claims are
external gates.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.x15304-triangular-three-block-schur.v1"
OUTPUT_SCHEMA = "riemann.x15304-triangular-three-block-schur.verification.v1"


class CertificateError(ValueError):
    pass


def parse_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def parse_fraction(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an integer or rational object")
    numerator = parse_int(value.get("numerator"), f"{name}.numerator")
    denominator = parse_int(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def fraction_json(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def parse_matrix(value: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty matrix")
    rows: list[list[Fraction]] = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        rows.append([parse_fraction(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)])
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise CertificateError(f"{name} is ragged")
    return rows


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def require_symmetric(a: list[list[Fraction]], name: str) -> None:
    n, m = shape(a)
    if n != m or a != transpose(a):
        raise CertificateError(f"{name} must be symmetric")


def zeros(n: int, m: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def add(
    a: list[list[Fraction]],
    b: list[list[Fraction]],
    scalar_a: Fraction = Fraction(1),
    scalar_b: Fraction = Fraction(1),
) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise CertificateError("matrix addition dimension mismatch")
    return [
        [scalar_a * x + scalar_b * y for x, y in zip(row_a, row_b)]
        for row_a, row_b in zip(a, b)
    ]


def scale(a: list[list[Fraction]], scalar: Fraction) -> list[list[Fraction]]:
    return [[scalar * x for x in row] for row in a]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if shape(a)[1] != shape(b)[0]:
        raise CertificateError("matrix multiplication dimension mismatch")
    bt = transpose(b)
    return [
        [sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in bt]
        for row in a
    ]


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    require_symmetric(a, "matrix to invert")
    n = len(a)
    aug = [a[i][:] + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot_row = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot_row is None:
            raise CertificateError("singular matrix")
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        pivot = aug[col][col]
        aug[col] = [x / pivot for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            multiplier = aug[row][col]
            if multiplier != 0:
                aug[row] = [
                    x - multiplier * y for x, y in zip(aug[row], aug[col])
                ]
    return [row[n:] for row in aug]


def ldl_positive_pivots(a: list[list[Fraction]], name: str) -> list[Fraction]:
    """Exact no-pivot LDL for a strictly positive-definite rational matrix."""
    require_symmetric(a, name)
    n = len(a)
    lower = zeros(n, n)
    pivots: list[Fraction] = []
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivot = a[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        if pivot <= 0:
            raise CertificateError(f"{name} has nonpositive LDL pivot {i}: {pivot}")
        pivots.append(pivot)
        for j in range(i + 1, n):
            numerator = a[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k] for k in range(i)
            )
            lower[j][i] = numerator / pivot
    return pivots


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def matrix_json(a: list[list[Fraction]]) -> list[list[dict[str, str]]]:
    return [[fraction_json(x) for x in row] for row in a]


def parse_and_check_dimensions(data: dict[str, Any]):
    matrices = {
        name: parse_matrix(data.get(name), name)
        for name in ("G_R", "G_V", "M", "B_R", "B_V", "C", "X", "Y", "Z")
    }
    g_r, g_v, metric = matrices["G_R"], matrices["G_V"], matrices["M"]
    n_r, m_r = shape(g_r)
    n_v, m_v = shape(g_v)
    n_e, m_e = shape(metric)
    if n_r != m_r or n_v != m_v or n_e != m_e:
        raise CertificateError("metric matrices must be square")
    for name, n in (
        ("G_R", n_r),
        ("B_R", n_r),
        ("G_V", n_v),
        ("B_V", n_v),
        ("M", n_e),
        ("C", n_e),
    ):
        if shape(matrices[name]) != (n, n):
            raise CertificateError(f"{name} has the wrong square dimension")
        require_symmetric(matrices[name], name)
    if shape(matrices["X"]) != (n_v, n_r):
        raise CertificateError("X must map R to V")
    if shape(matrices["Y"]) != (n_e, n_r):
        raise CertificateError("Y must map R to E")
    if shape(matrices["Z"]) != (n_e, n_v):
        raise CertificateError("Z must map V to E")
    return matrices


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("status") != "DECLARED_THREE_BLOCK_PACKET":
        raise CertificateError("status must preserve the theorem's proof boundary")

    a = parse_and_check_dimensions(data)
    g_r, g_v, metric = a["G_R"], a["G_V"], a["M"]
    b_r, b_v, c = a["B_R"], a["B_V"], a["C"]
    x, y, z = a["X"], a["Y"], a["Z"]

    e = parse_fraction(data.get("radical_lower_loss"), "radical_lower_loss")
    h = parse_fraction(data.get("complement_floor"), "complement_floor")
    beta = parse_fraction(data.get("visible_schur_floor"), "visible_schur_floor")
    kappa = parse_fraction(
        data.get("radical_correction_bound"), "radical_correction_bound"
    )
    delta = parse_fraction(data.get("assembly_radius"), "assembly_radius")
    if e < 0 or kappa < 0 or delta < 0 or h <= 0 or beta <= 0:
        raise CertificateError("losses must be nonnegative and floors strictly positive")

    metric_pivots = {
        "G_R": ldl_positive_pivots(g_r, "G_R"),
        "G_V": ldl_positive_pivots(g_v, "G_V"),
        "M": ldl_positive_pivots(metric, "M"),
    }
    metric_inv = inverse(metric)
    g_v_inv = inverse(g_v)

    complement_slack = add(c, scale(metric, h), scalar_b=Fraction(-1))
    complement_pivots = ldl_positive_pivots(complement_slack, "C - h M")

    z_metric_z = matmul(transpose(z), matmul(metric_inv, z))
    visible_schur = add(
        b_v, scale(z_metric_z, Fraction(1, h)), scalar_b=Fraction(-1)
    )
    visible_slack = add(
        visible_schur, scale(g_v, beta), scalar_b=Fraction(-1)
    )
    visible_pivots = ldl_positive_pivots(visible_slack, "visible Schur slack")

    z_metric_y = matmul(transpose(z), matmul(metric_inv, y))
    corrected_x = add(
        x, scale(z_metric_y, Fraction(1, h)), scalar_b=Fraction(-1)
    )

    y_correction = scale(
        matmul(transpose(y), matmul(metric_inv, y)), Fraction(1, h)
    )
    x_correction = scale(
        matmul(transpose(corrected_x), matmul(g_v_inv, corrected_x)),
        Fraction(1, beta),
    )
    total_correction = add(y_correction, x_correction)
    correction_slack = add(
        scale(g_r, kappa), total_correction, scalar_b=Fraction(-1)
    )
    correction_pivots = ldl_positive_pivots(
        correction_slack, "radical correction slack"
    )

    radical_slack = add(b_r, scale(g_r, e))
    radical_pivots = ldl_positive_pivots(radical_slack, "B_R + e G_R")

    epsilon = e + kappa + delta
    result: dict[str, Any] = {
        "schema": OUTPUT_SCHEMA,
        "verified": True,
        "status": "CERTIFIED_THREE_BLOCK_LOWER_FLOOR",
        "dimensions": {
            "radical": len(g_r),
            "visible": len(g_v),
            "complement": len(metric),
        },
        "floors_and_losses": {
            "radical_lower_loss": fraction_json(e),
            "complement_floor": fraction_json(h),
            "visible_schur_floor": fraction_json(beta),
            "radical_correction_bound": fraction_json(kappa),
            "assembly_radius": fraction_json(delta),
            "final_negative_floor": fraction_json(epsilon),
        },
        "corrected_radical_visible_cross": matrix_json(corrected_x),
        "radical_correction_matrix": matrix_json(total_correction),
        "ldl_pivots": {
            **{
                name: [fraction_json(v) for v in pivots]
                for name, pivots in metric_pivots.items()
            },
            "complement_slack": [fraction_json(v) for v in complement_pivots],
            "visible_schur_slack": [fraction_json(v) for v in visible_pivots],
            "radical_correction_slack": [
                fraction_json(v) for v in correction_pivots
            ],
            "radical_diagonal_slack": [
                fraction_json(v) for v in radical_pivots
            ],
        },
        "theorem_identity": (
            "epsilon = e + kappa + delta, with kappa bounding "
            "h^-1 Y^T M^-1 Y + beta^-1 X_tilde^T G_V^-1 X_tilde and "
            "X_tilde = X - h^-1 Z^T M^-1 Y"
        ),
        "proof_boundary": (
            "Exact finite rational algebra only. Source radicality, zero-Gram and "
            "symbol floors, metric provenance, cofinal rates, and the RH implication "
            "are external gates."
        ),
        "proof_object_sha256": canonical_sha256(data),
    }
    result["verification_sha256"] = canonical_sha256(result)
    return result


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"{path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify(load(args.certificate))
        code = 0
    except (CertificateError, ZeroDivisionError) as exc:
        result = {
            "schema": OUTPUT_SCHEMA,
            "verified": False,
            "status": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
