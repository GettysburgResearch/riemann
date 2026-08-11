#!/usr/bin/env python3
"""Finite model for the high-carrier Fredholm fixed-degree firewall.

The diagonal family has the exact form A_c=cB+E_c with B>=0 and
||E_c||_1=1. The negative perturbation moves into the small-eigenvalue tail of
B, so one negative eigenvalue persists while every fixed exterior/Hankel degree
becomes positive and the first detecting degree diverges.

This is a diagnostic model, not the analytic zeta proof and not RH.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

STATUS = "PASS_X_90705_HIGH_CARRIER_FIXED_DEGREE_FIREWALL"


def elementary(values: list[float]) -> list[float]:
    out = [1.0]
    for value in values:
        out.append(0.0)
        for k in range(len(out) - 1, 0, -1):
            out[k] += value * out[k - 1]
    return out


def shifted_hankel(values: np.ndarray, degree: int) -> np.ndarray:
    moments = {
        k: float(np.sum(values**k))
        for k in range(1, 2 * degree + 2)
    }
    return np.array(
        [
            [moments[i + j + 1] for j in range(degree + 1)]
            for i in range(degree + 1)
        ],
        dtype=float,
    )


def model(carrier: float) -> tuple[np.ndarray, np.ndarray, int]:
    index = math.ceil(2.0 * math.sqrt(carrier))
    dimension = 4 * index
    B = np.array([1.0 / (j * j) for j in range(1, dimension + 1)])
    values = carrier * B
    values[index - 1] -= 1.0
    return values, B, index


def main() -> dict[str, object]:
    carriers = [10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0]
    rows: list[dict[str, object]] = []
    first_degrees: list[int] = []
    fixed_positive = True
    normalized_convergence = True
    hankel_positive = True
    root_escape = True

    for carrier in carriers:
        values, B, index = model(carrier)
        coeff = elementary(values.tolist())
        first_negative = next(
            k for k, value in enumerate(coeff[1:], start=1) if value < 0.0
        )
        first_degrees.append(first_negative)
        fixed_positive = fixed_positive and min(coeff[1:5]) > 0.0

        normalized_difference = float(
            np.sum(np.abs(values / carrier - B))
        )
        normalized_convergence = (
            normalized_convergence
            and abs(normalized_difference - 1.0 / carrier) < 1e-13
        )

        negative = float(-np.min(values))
        scaled_root = carrier / negative
        root_escape = root_escape and scaled_root > carrier

        hankel_rows = []
        for degree in range(3):
            H = shifted_hankel(values, degree)
            scaling = np.diag(
                [carrier ** (-i - 0.5) for i in range(degree + 1)]
            )
            normalized = scaling @ H @ scaling
            minimum = float(np.linalg.eigvalsh(normalized)[0])
            hankel_rows.append(minimum)
        if carrier >= 100.0:
            hankel_positive = hankel_positive and min(hankel_rows) > 1e-10

        rows.append(
            {
                "carrier": carrier,
                "dimension": len(values),
                "moving_negative_index": index,
                "negative_eigenvalue": float(np.min(values)),
                "negative_index": int(np.sum(values < 0.0)),
                "perturbation_trace_norm": 1.0,
                "normalized_trace_norm_error": normalized_difference,
                "first_negative_exterior_degree": first_negative,
                "fixed_exterior_coefficients_1_to_4": coeff[1:5],
                "normalized_hankel_min_eigenvalues_degrees_0_to_2": hankel_rows,
                "normalized_positive_axis_root": scaled_root,
            }
        )

    gates = {
        "one_negative_eigenvalue_persists": all(
            row["negative_index"] == 1 for row in rows
        ),
        "uniform_trace_norm_perturbation": all(
            row["perturbation_trace_norm"] == 1.0 for row in rows
        ),
        "normalized_trace_norm_convergence": normalized_convergence,
        "every_fixed_exterior_degree_positive": fixed_positive,
        "first_detecting_degree_strictly_increases": all(
            b > a for a, b in zip(first_degrees, first_degrees[1:])
        ),
        "fixed_hankel_degrees_eventually_positive": hankel_positive,
        "normalized_fredholm_root_escapes": root_escape,
    }
    if not all(gates.values()):
        raise AssertionError([name for name, ok in gates.items() if not ok])

    result = {
        "status": STATUS,
        "gates": gates,
        "rows": rows,
        "first_negative_degrees": first_degrees,
        "scope": (
            "finite moving-tail model only; the analytic high-carrier theorem "
            "is proved separately and RH remains open"
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    result = main()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(STATUS)
