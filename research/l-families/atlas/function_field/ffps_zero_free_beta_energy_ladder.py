#!/usr/bin/env python3
"""Bounded replay for the zero-free beta energy ladder."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_zero_free_beta_energy_ladder.json"
KERNEL_COMMIT = "fc7ee1304746d3c5b50d02592ccb0d8cdf329c4f"
ENERGY_COMMIT = "05aaabe69060c24c8db4ca33c350e109231960f1"
FROZEN_SOURCES = (
    (
        KERNEL_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "FFPS_BETA_KERNEL_SPECTRAL_NONALIGNMENT.md"
        ),
        "9e280c6dfc6fdaa34690d3966851d6d5e1acebb2",
    ),
    (
        KERNEL_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "ffps_beta_kernel_spectral_nonalignment.py"
        ),
        "111e9b3f61ab7dd14c73e85e1a4501822ed3f26f",
    ),
    (
        KERNEL_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "ffps_beta_kernel_spectral_nonalignment.json"
        ),
        "e88ade4246f8003956d54fa3a09719285920cf0e",
    ),
    (
        KERNEL_COMMIT,
        "tests/test_ffps_beta_kernel_spectral_nonalignment.py",
        "4d86735b3970f92321e4801fea744cd5f34e6c94",
    ),
    (
        ENERGY_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "FFPS_BANDPASS_BETA_ENERGY_LADDER.md"
        ),
        "0ac23a6c384a896e50fed21ca7d8bf079c338ac0",
    ),
    (
        ENERGY_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "ffps_bandpass_beta_energy_ladder.py"
        ),
        "9ca6db9ad6b0149936efbd0e99f799d89f3cc53a",
    ),
    (
        ENERGY_COMMIT,
        (
            "research/l-families/atlas/function_field/"
            "ffps_bandpass_beta_energy_ladder.json"
        ),
        "ff568b48100048f6ad963c7afa23c4ac04c3d291",
    ),
    (
        ENERGY_COMMIT,
        "tests/test_ffps_bandpass_beta_energy_ladder.py",
        "6b45ddd02148c437bba375d6dbaf753c938e3375",
    ),
)

KERNEL_SOURCE = HERE / "ffps_beta_kernel_spectral_nonalignment.py"
KERNEL_SOURCE_BLOB = "111e9b3f61ab7dd14c73e85e1a4501822ed3f26f"
MAXIMUM_LADDER_ORDER = 6
WEIGHT_SAMPLES = (
    Fraction(-100),
    Fraction(-3, 2),
    Fraction(-1, 100),
    Fraction(1, 100),
    Fraction(3, 2),
    Fraction(100),
)


def check_imported_source_blob() -> None:
    completed = subprocess.run(
        ["git", "hash-object", str(KERNEL_SOURCE)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=3,
    )
    if completed.stdout.strip() != KERNEL_SOURCE_BLOB:
        raise RuntimeError("working-tree kernel producer differs from frozen blob")


check_imported_source_blob()
SPEC = importlib.util.spec_from_file_location("beta_kernel_source", KERNEL_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the frozen beta-kernel producer")
source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source)


def check_source_blobs() -> None:
    check_imported_source_blob()
    for commit, path, expected in FROZEN_SOURCES:
        completed = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def validate_order(order: int) -> None:
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or not 1 <= order <= MAXIMUM_LADDER_ORDER
    ):
        raise ValueError(f"bounded replay order must lie in [1,{MAXIMUM_LADDER_ORDER}]")


def phi_fourier_weight(t: float) -> float:
    if not math.isfinite(t):
        raise ValueError("frequency must be finite")
    spectral_floor = math.sinh(0.5) ** 2 + math.sin(t / 2.0) ** 2
    return 16.0 * spectral_floor**2 / (1.0 + t * t) ** 2


def normalized_phi_fourier_weight(t: float) -> float:
    if not math.isfinite(t):
        raise ValueError("frequency must be finite")
    mass_squared = 16.0 * math.sinh(0.5) ** 4
    return phi_fourier_weight(t) / mass_squared


def ladder_weight(order: int, t: float) -> float:
    validate_order(order)
    if not math.isfinite(t):
        raise ValueError("frequency must be finite")
    return t * t * normalized_phi_fourier_weight(t / order) ** order


def support_endpoint(order: int) -> int:
    validate_order(order)
    return 2


def decay_exponent(order: int) -> int:
    validate_order(order)
    return 2 - 4 * order


def control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in range(1, MAXIMUM_LADDER_ORDER + 1):
        samples = [ladder_weight(order, float(value)) for value in WEIGHT_SAMPLES]
        if any(value <= 0 for value in samples):
            raise ArithmeticError("zero-free ladder weight lost positivity")
        if order == 1:
            for sample, value in zip(WEIGHT_SAMPLES, samples, strict=True):
                mass_squared = 16.0 * math.sinh(0.5) ** 4
                expected = source.universal_weight(float(sample)) / mass_squared
                if not math.isclose(value, expected, rel_tol=1e-13, abs_tol=0):
                    raise ArithmeticError("order-one weight drifted from frozen source")
        rows.append(
            {
                "order": order,
                "kernel_support": [0, support_endpoint(order)],
                "autocorrelation_support": [
                    -support_endpoint(order),
                    support_endpoint(order),
                ],
                "ratio_band": [
                    f"exp(-{support_endpoint(order)})",
                    f"exp({support_endpoint(order)})",
                ],
                "weight_zero_set": ["0"],
                "weight_zero_order_at_zero": 2,
                "high_frequency_decay_exponent": decay_exponent(order),
                "positive_sample_minimum": min(samples),
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    rows = control_rows()
    return {
        "source_contract": {
            "frozen_sources": [
                {"commit": commit, "path": path, "blob": blob}
                for commit, path, blob in FROZEN_SOURCES
            ]
        },
        "kernel_ladder": {
            "definition": ("M=4sinh^2(1/2), P=Phi/M, Q_m(x)=m P^(*m)(m x), J_m=D Q_m"),
            "laplace_transform": (
                "J_m_hat(s)=s[Phi_hat(s/m)/M]^m, "
                "Phi_hat(z)=4e^(-z)sinh^2((z-1)/2)/(z-1)^2"
            ),
            "carrier_zeros": (
                "s=0 and s=m(1+2pi*i*k) for nonzero integers k; none in 0<Re(s)<1/2"
            ),
            "fourier_weight": (
                "t^2[((sinh^2(1/2)+sin^2(t/(2m)))^2)/(sinh^4(1/2)(1+(t/m)^2)^2)]^m"
            ),
            "real_weight_zeros": "t=0 only, always of order two",
            "fixed_support": "supp(J_m)=[0,2] for every m",
            "order_one_norm_squared": ("(1+sinh(2)/2)/(16sinh^4(1/2))"),
            "rows": rows,
        },
        "rh_equivalence": {
            "beta_source": "beta(n)=mu(n)-1_(67|n)mu(n/67)",
            "prefix_energy": (
                "E_m(X)=integral |sum_(n<=X) beta(n)n^(-1/2)J_m(t-log n)|^2 dt"
            ),
            "criterion": (
                "for every fixed m>=1, RH iff E_m(X)=X^o(1), "
                "iff complete L1 or negative mass is e^o(T)"
            ),
            "gram_ratio_band": "exp(-2)<=a/b<=exp(2), independent of m",
            "beta_diagonal": ("||J_m||_2^2 * 2379/(2278*zeta(2))*log X+O_m(1)"),
        },
        "proof_ledger": {
            "zero_free_kernel_ladder": "PROVED EXACT",
            "positive_nonzero_fourier_weight": "PROVED EXACT",
            "open_rh_strip_carrier_nonvanishing": "PROVED EXACT",
            "rh_equivalent_prefix_energy": "PROVED FROM FROZEN LANDAU ARGUMENT",
            "rh_equivalent_one_sided_negative_mass": (
                "PROVED FROM FROZEN LANDAU ARGUMENT"
            ),
            "compact_ratio_gram_identity": "PROVED EXACT",
            "any_energy_or_off_diagonal_estimate": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "largest_ladder_order": MAXIMUM_LADDER_ORDER,
            "weight_samples_per_order": len(WEIGHT_SAMPLES),
            "zeta_zeros": 0,
            "numerical_zeta_value_evaluations": 0,
            "primes": 0,
            "curves": 0,
            "random_samples": 0,
        },
    }


def canonical_text(result: dict[str, object]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    result = run(check_sources=not args.no_source_check)
    text = canonical_text(result)
    if args.write_json:
        args.write_json.write_text(text, encoding="utf-8", newline="\n")
    elif args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError("canonical JSON drift")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
