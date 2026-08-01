#!/usr/bin/env python3
"""Exact rational control for the consecutive-triple radical frame."""
from __future__ import annotations

import json
from fractions import Fraction as F

SCHEMA = "riemann.x16202-local-triple-frame.v1"


class CertificateError(ValueError):
    pass


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def mat_mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def diagonal(values: list[F]) -> list[list[F]]:
    return [
        [values[i] if i == j else F(0) for j in range(len(values))]
        for i in range(len(values))
    ]


def ldl_pivots(a: list[list[F]]) -> list[F]:
    n = len(a)
    lower = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    pivots: list[F] = []
    for i in range(n):
        pivot = a[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        pivots.append(pivot)
        if pivot == 0:
            raise CertificateError("zero LDL pivot")
        for j in range(i + 1, n):
            lower[j][i] = (
                a[j][i]
                - sum(lower[j][k] * lower[i][k] * pivots[k] for k in range(i))
            ) / pivot
    return pivots


def require_pd(a: list[list[F]], name: str) -> list[F]:
    pivots = ldl_pivots(a)
    if not all(value > 0 for value in pivots):
        raise CertificateError(f"{name} is not positive definite")
    return pivots


def build_frame(defects: list[F], point_values: list[F]) -> tuple[list[list[F]], list[F]]:
    if len(defects) != len(point_values) or len(defects) < 3:
        raise CertificateError("invalid input dimensions")
    if any(defects[i] >= defects[i + 1] for i in range(len(defects) - 1)):
        raise CertificateError("defects must be strictly increasing")
    if any(value == 0 for value in point_values):
        raise CertificateError("point values must be nonzero")

    dimension = len(defects) - 2
    columns: list[list[F]] = []
    ratios: list[F] = []
    for j in range(dimension):
        ratio = (defects[j + 1] - defects[j]) / (defects[j + 2] - defects[j])
        ratios.append(ratio)
        x_vector = [F(0)] * len(defects)
        x_vector[j] = F(1) - ratio
        x_vector[j + 1] = F(-1)
        x_vector[j + 2] = ratio

        if sum(x_vector) != 0:
            raise CertificateError("zeroth constraint failed")
        if sum(defects[i] * x_vector[i] for i in range(len(defects))) != 0:
            raise CertificateError("defect constraint failed")

        columns.append([
            x_vector[i] / point_values[i] for i in range(len(defects))
        ])

    return transpose(columns), ratios


def verify() -> dict:
    defects = [F(1), F(10), F(1000), F(100000), F(10000000)]
    point_values = [F(1), F(2), F(1), F(2), F(1)]
    frame, ratios = build_frame(defects, point_values)
    gram = mat_mul(transpose(frame), frame)
    pivots = require_pd(gram, "radical frame Gram")

    lower = F(1, 100)
    shifted = [
        [gram[i][j] - (lower if i == j else F(0)) for j in range(len(gram))]
        for i in range(len(gram))
    ]
    shifted_pivots = require_pd(shifted, "declared frame lower bound")

    defect_gram = mat_mul(mat_mul(transpose(frame), diagonal(defects)), frame)
    defect_pivots = require_pd(defect_gram, "defect-energy Gram")

    maximum_ratio = max(ratios)
    if F(4) * maximum_ratio >= F(1):
        raise CertificateError("synthetic separation ratio is not small")

    return {
        "schema": SCHEMA,
        "classification": "EXACT_SYNTHETIC_LOCAL_TRIPLE_FRAME_CONTROL",
        "defects": [str(value) for value in defects],
        "point_values": [str(value) for value in point_values],
        "local_ratios": [str(value) for value in ratios],
        "maximum_ratio": str(maximum_ratio),
        "four_times_maximum_ratio": str(F(4) * maximum_ratio),
        "frame": [[str(value) for value in row] for row in frame],
        "frame_gram": [[str(value) for value in row] for row in gram],
        "frame_ldl_pivots": [str(value) for value in pivots],
        "certified_frame_lower_bound": str(lower),
        "shifted_ldl_pivots": [str(value) for value in shifted_pivots],
        "defect_gram": [[str(value) for value in row] for row in defect_gram],
        "defect_ldl_pivots": [str(value) for value in defect_pivots],
        "proof_boundary": (
            "Finite rational algebra only. This control does not certify any "
            "Riemann prolate defect, point value, arithmetic E-image, or Weil form."
        ),
    }


def main() -> int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
