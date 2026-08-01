#!/usr/bin/env python3
"""Exact Fraction-only regression for L-15610/L-15611/L-15612.

The synthetic packet checks three independent mechanisms:

1. an external exact corrector preserves the complete source-packet rank;
2. a weighted-deficit index cap and an unrelated equal-dimensional low packet
   force exact low-index saturation without a principal-angle hypothesis;
3. low compression for the same operator automatically supplies a rigorous
   weighted-deficit trace-tail and complement floor.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from typing import Sequence


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def transpose(a: Sequence[Sequence[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def add(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(a: Sequence[Sequence[F]], c: F) -> list[list[F]]:
    return [[c * x for x in row] for row in a]


def gram(columns: Sequence[Sequence[F]]) -> list[list[F]]:
    return matmul(transpose(columns), columns)


def quadratic_matrix(
    diagonal: Sequence[F], columns: Sequence[Sequence[F]]
) -> list[list[F]]:
    d_times_c = [
        [diagonal[i] * columns[i][j] for j in range(len(columns[0]))]
        for i in range(len(diagonal))
    ]
    return matmul(transpose(columns), d_times_c)


def ldl_pivots(a: Sequence[Sequence[F]]) -> list[F]:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("matrix must be square")
    lower = [[F(0) for _ in range(n)] for _ in range(n)]
    pivots = [F(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = F(1)
        pivots[i] = a[i][i] - sum(
            (lower[i][k] * lower[i][k] * pivots[k] for k in range(i)), F(0)
        )
        if pivots[i] <= 0:
            raise ValueError(f"nonpositive LDL pivot {i}: {pivots[i]}")
        for j in range(i + 1, n):
            numerator = a[j][i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)),
                F(0),
            )
            lower[j][i] = numerator / pivots[i]
    return pivots


def fj(value: F) -> dict[str, str]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def main() -> int:
    # L-15611: P=span(e1,e2), ell(x)=x1+2x2+x3, Q(c)=c e3.
    # Columns after R=(I-Q ell)|P: e1-e3, e2-2e3.
    repaired = [[F(1), F(0)], [F(0), F(1)], [F(-1), F(-2)]]
    repaired_gram = gram(repaired)
    repaired_pivots = ldl_pivots(repaired_gram)
    constraints = [
        repaired[0][j] + 2 * repaired[1][j] + repaired[2][j]
        for j in range(2)
    ]
    assert constraints == [0, 0]

    # L-15610: A >= G I-D exactly, here equality. D has two eigenvalues > kappa.
    G = F(2)
    Gamma = F(1)
    kappa = G - Gamma
    deficit_eigenvalues = [F(3, 2), F(6, 5), F(1, 2), F(1, 10)]
    operator_eigenvalues = [G - value for value in deficit_eigenvalues]
    weighted_index = sum(value > kappa for value in deficit_eigenvalues)
    exact_count_gamma = sum(value < Gamma for value in operator_eigenvalues)
    assert weighted_index == exact_count_gamma == 2

    # An unrelated two-dimensional packet, not equal to span(e1,e2).
    low_columns = [
        [F(1), F(0)],
        [F(0), F(1)],
        [F(1, 10), F(0)],
        [F(0), F(1, 10)],
    ]
    low_gram = gram(low_columns)
    low_form = quadratic_matrix(operator_eigenvalues, low_columns)

    alpha = F(17, 20)
    compression_moat = add(scale(low_gram, alpha), scale(low_form, F(-1)))
    compression_pivots = ldl_pivots(compression_moat)

    t = F(19, 20)
    threshold_moat = add(scale(low_gram, t), scale(low_form, F(-1)))
    threshold_pivots = ldl_pivots(threshold_moat)
    exact_count_t = sum(value < t for value in operator_eigenvalues)
    assert exact_count_t == exact_count_gamma == weighted_index

    # L-15612: low compression forces integrated deficit capture.
    trace_deficit = sum(deficit_eigenvalues, F(0))
    guaranteed_capture = weighted_index * (G - alpha)
    uncaptured_trace_upper = trace_deficit - guaranteed_capture
    assert uncaptured_trace_upper <= G - Gamma
    complement_floor = G - uncaptured_trace_upper
    assert complement_floor >= Gamma

    result = {
        "schema": "riemann.x15603-weighted-deficit-capacity.v2",
        "external_corrector": {
            "packet_dimension": 2,
            "repaired_dimension": 2,
            "constraints_after_repair": [str(value) for value in constraints],
            "repaired_gram": [
                [fj(value) for value in row] for row in repaired_gram
            ],
            "positive_ldl_pivots": [fj(value) for value in repaired_pivots],
            "classification": "EXACT_RANK_PRESERVING_SOURCE_REPAIR",
        },
        "weighted_deficit_saturation": {
            "G": fj(G),
            "Gamma": fj(Gamma),
            "kappa": fj(kappa),
            "deficit_eigenvalues": [fj(value) for value in deficit_eigenvalues],
            "operator_eigenvalues": [fj(value) for value in operator_eigenvalues],
            "weighted_deficit_index": weighted_index,
            "exact_count_below_t": exact_count_t,
            "exact_count_below_Gamma": exact_count_gamma,
            "low_packet_equals_deficit_packet": False,
            "low_packet_gram": [
                [fj(value) for value in row] for row in low_gram
            ],
            "alpha": fj(alpha),
            "alpha_gram_minus_low_form_ldl_pivots": [
                fj(value) for value in compression_pivots
            ],
            "t_gram_minus_low_form_ldl_pivots": [
                fj(value) for value in threshold_pivots
            ],
            "trace_capture": {
                "trace_deficit": fj(trace_deficit),
                "guaranteed_packet_capture": fj(guaranteed_capture),
                "uncaptured_trace_upper": fj(uncaptured_trace_upper),
                "required_upper": fj(G - Gamma),
                "certified_complement_floor": fj(complement_floor),
                "classification": "EXACT_L15612_TRACE_CAPTURE_COMPLEMENT_FLOOR",
            },
            "classification": (
                "EXACT_INDEX_AND_TRACE_SATURATION_WITHOUT_SUBSPACE_ALIGNMENT"
            ),
        },
        "verdict": "PASS_EXACT_L15610_L15611_L15612_REGRESSION",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
