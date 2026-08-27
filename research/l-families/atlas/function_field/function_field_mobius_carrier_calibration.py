#!/usr/bin/env python3
"""Bounded replay for the curve-zeta Möbius carrier calibration."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "function_field_mobius_carrier_calibration.json"

SOURCE_COMMIT = "19f274c9335ecffb357e296b3fd5fefdeba5f3fd"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_VARIATIONAL_PROBABILITY_CARRIER_OPTIMUM.md": "d216e254e550c3f3cad49e3dac29da2b0b76e760",
    "research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py": "f7a8628858f2a23bc4b9f164ea0cde1601c03235",
    "research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.json": "a37d9b0bf1c43bed0df268a764427fa6c3870211",
    "tests/test_ffps_variational_probability_carrier_optimum.py": "6a8c9d45391014df212f4e2773be0d7a3e57e2e8",
}

FIELD_SIZE = 5
TRACE_ROWS = (
    (0, "Weil-compatible control"),
    (4, "Weil-compatible near-edge control"),
    (5, "formal off-circle control; not asserted to be a curve"),
)
DEGREE_CAP = 24


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_curve_row(field_size: int, trace: int, degree_cap: int) -> None:
    if not isinstance(field_size, int) or field_size < 2:
        raise ValueError("field size must be an integer at least two")
    if not isinstance(trace, int):
        raise TypeError("trace must be an integer")
    if not isinstance(degree_cap, int) or degree_cap < 0:
        raise ValueError("degree cap must be a nonnegative integer")


def reciprocal_roots(field_size: int, trace: int) -> tuple[complex, complex]:
    validate_curve_row(field_size, trace, 0)
    discriminant = complex(trace * trace - 4 * field_size)
    root = cmath.sqrt(discriminant)
    return ((trace + root) / 2.0, (trace - root) / 2.0)


def mobius_degree_coefficients(
    field_size: int, trace: int, degree_cap: int
) -> list[int]:
    """Coefficients of (1-u)(1-qu)/(1-a*u+q*u^2)."""
    validate_curve_row(field_size, trace, degree_cap)
    numerator = (1, -(field_size + 1), field_size)
    coefficients: list[int] = []
    for degree in range(degree_cap + 1):
        value = numerator[degree] if degree < len(numerator) else 0
        if degree >= 1:
            value += trace * coefficients[degree - 1]
        if degree >= 2:
            value -= field_size * coefficients[degree - 2]
        coefficients.append(value)
    return coefficients


def normalized_coefficients(
    field_size: int, trace: int, degree_cap: int
) -> list[float]:
    raw = mobius_degree_coefficients(field_size, trace, degree_cap)
    return [value / field_size ** (degree / 2.0) for degree, value in enumerate(raw)]


def support_length(field_size: int) -> float:
    if not isinstance(field_size, int) or field_size < 2:
        raise ValueError("field size must be an integer at least two")
    return 0.5 * math.log(field_size)


def detector_diagonal(field_size: int) -> float:
    support = support_length(field_size)
    return 12.0 / support**3


def orthogonal_energy(field_size: int, trace: int, degree_cap: int) -> float:
    normalized = normalized_coefficients(field_size, trace, degree_cap)
    return detector_diagonal(field_size) * sum(value * value for value in normalized)


def control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for trace, label in TRACE_ROWS:
        roots = reciprocal_roots(FIELD_SIZE, trace)
        radius = max(abs(root) for root in roots) / math.sqrt(FIELD_SIZE)
        energy = orthogonal_energy(FIELD_SIZE, trace, DEGREE_CAP)
        rows.append(
            {
                "field_size": FIELD_SIZE,
                "trace": trace,
                "label": label,
                "normalized_root_radius": radius,
                "energy_through_degree_cap": energy,
                "energy_root_estimator": energy ** (1.0 / (2.0 * DEGREE_CAP)),
                "last_normalized_coefficient": normalized_coefficients(
                    FIELD_SIZE, trace, DEGREE_CAP
                )[-1],
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    rows = control_rows()
    if any(row["normalized_root_radius"] > 1.0 + 1.0e-13 for row in rows[:2]):
        raise AssertionError("Weil-compatible controls left the unit circle")
    if rows[-1]["normalized_root_radius"] <= 1.0:
        raise AssertionError("formal off-circle control lost its expanding pole")
    if rows[-1]["energy_root_estimator"] <= rows[0]["energy_root_estimator"]:
        raise AssertionError("formal off-circle energy failed to separate")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "curve_theorem": {
            "zeta_shape": "Z_C(u)=P_C(u)/((1-u)(1-q*u))",
            "degree_mobius_sum": "M_n=[u^n](1-u)(1-q*u)/P_C(u)",
            "normalization": "b_n=q^(-n/2)*M_n",
            "carrier_support": "S=(log q)/2, strictly below one degree spacing",
            "orthogonal_energy": "E_N=(96/(log q)^3)*sum_{n<=N}|b_n|^2",
            "equivalence": "curve RH iff E_N=q^o(N)",
            "known_RH_consequence": "E_N=O_C((1+N)^max(0,4g-1))",
        },
        "mechanism": {
            "subexponential_energy": "equivalent to max_j |alpha_j|<=sqrt(q) after reduction",
            "functional_equation": "alpha_j pairs with q/alpha_j, forcing equality",
            "interpretation": "exact function-field calibration of the probability-carrier beta criterion",
        },
        "control_rows": rows,
        "proof_ledger": {
            "disjoint_degree_packet_energy": "PROVED EXACT",
            "energy_to_reciprocal_root_radius": "PROVED",
            "functional_equation_to_curve_RH": "PROVED",
            "Weil_RH_itself": "IMPORTED KNOWN THEOREM, NOT REPROVED",
            "number_field_beta_estimate": "NOT PROVED",
            "integer_RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "formal_genus_one_rows": len(TRACE_ROWS),
            "degree_cap": DEGREE_CAP,
            "curve_enumerations": 0,
            "field_element_enumerations": 0,
            "point_counts": 0,
            "zeta_zeros": 0,
            "random_samples": 0,
            "quadratures": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    payload = run(check_sources=not args.no_source_check)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json is not None:
        args.write_json.write_text(text, encoding="utf-8")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError(f"canonical fixture mismatch: {OUTPUT}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
