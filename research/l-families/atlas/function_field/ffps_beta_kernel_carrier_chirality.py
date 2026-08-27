#!/usr/bin/env python3
"""Bounded replay for the tilted beta-kernel carrier-chirality theorem."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_beta_kernel_carrier_chirality.json"

SOURCE_COMMIT = "3658d4c31cc866e15d48ab1fc9d8d119136da424"
FROZEN_SOURCES = {
    "research/l-families/atlas/function_field/FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md": (
        "bd4cbb842e78c1dad5d380c8d20ff14c39bba15e"
    ),
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py": (
        "df80000192292cc5fc1cd08013f152fb257054f9"
    ),
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.json": (
        "7e8889aa0dd1b01674e20158a52502cff0d8dffa"
    ),
    "tests/test_ffps_zero_free_beta_energy_ladder.py": (
        "983a1320f89087028f6724fe36aaca5ca1309b15"
    ),
}

MAXIMUM_ORDER = 6
TILT_SAMPLES = (
    Fraction(-1),
    Fraction(-1, 8),
    Fraction(0),
    Fraction(1, 8),
    Fraction(1, 2),
    Fraction(1),
)
FREQUENCY_SAMPLES = (
    Fraction(-10),
    Fraction(-3, 2),
    Fraction(-1, 100),
    Fraction(1, 100),
    Fraction(3, 2),
    Fraction(10),
)


def check_source_blobs() -> None:
    for path, expected in FROZEN_SOURCES.items():
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


def validate_order(order: int) -> None:
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or not 1 <= order <= MAXIMUM_ORDER
    ):
        raise ValueError(f"order must lie in [1,{MAXIMUM_ORDER}]")


def validate_real(value: float, name: str) -> None:
    if not isinstance(value, (float, int)) or isinstance(value, bool):
        raise TypeError(f"{name} must be real")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def squared_sinc(half_frequency: float) -> float:
    if half_frequency == 0.0:
        return 1.0
    return (math.sin(half_frequency) / half_frequency) ** 2


def atom_fourier_weight(tilt: float, frequency: float) -> float:
    """Return |f_tilt_hat(i frequency)|^2 for the normalized atom."""

    validate_real(tilt, "tilt")
    validate_real(frequency, "frequency")
    tilt = float(tilt)
    frequency = float(frequency)
    if tilt == 0.0:
        return squared_sinc(frequency / 2.0)
    sinh_half_squared = math.sinh(tilt / 2.0) ** 2
    numerator = tilt * tilt * (sinh_half_squared + math.sin(frequency / 2.0) ** 2)
    denominator = sinh_half_squared * (tilt * tilt + frequency * frequency)
    return numerator / denominator


def ladder_weight(tilt: float, order: int, frequency: float) -> float:
    validate_order(order)
    validate_real(frequency, "frequency")
    return float(frequency) ** 2 * atom_fourier_weight(
        tilt, float(frequency) / order
    ) ** (2 * order)


def carrier_real_part(tilt: float, order: int) -> float:
    validate_real(tilt, "tilt")
    validate_order(order)
    return order * float(tilt)


def direct_landau_zone(tilt: float, order: int) -> str:
    real_part = carrier_real_part(tilt, order)
    if real_part <= 0.0:
        return "DIRECTLY SAFE: nontrivial carrier zeros are on/left of Re(s)=0"
    if real_part >= 0.5:
        return "DIRECTLY SAFE: nontrivial carrier zeros are on/right of Re(s)=1/2"
    return "DIRECT CARRIER GAP: nontrivial zeros lie inside 0<Re(s)<1/2"


def nonzero_real_fourier_zeros(tilt: float, order: int) -> str:
    validate_real(tilt, "tilt")
    validate_order(order)
    if float(tilt) == 0.0:
        return "t=2pi*m*k for nonzero integers k"
    return "none"


def control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in range(1, MAXIMUM_ORDER + 1):
        for tilt_fraction in TILT_SAMPLES:
            tilt = float(tilt_fraction)
            samples = [
                ladder_weight(tilt, order, float(frequency))
                for frequency in FREQUENCY_SAMPLES
            ]
            mirror_samples = [
                ladder_weight(-tilt, order, float(frequency))
                for frequency in FREQUENCY_SAMPLES
            ]
            if any(
                not math.isclose(left, right, rel_tol=1e-13, abs_tol=1e-15)
                for left, right in zip(samples, mirror_samples, strict=True)
            ):
                raise ArithmeticError("mirror weights drifted")
            rows.append(
                {
                    "order": order,
                    "tilt": str(tilt_fraction),
                    "carrier_zero_real_part": str(order * tilt_fraction),
                    "direct_landau_zone": direct_landau_zone(tilt, order),
                    "nonzero_real_fourier_zeros": nonzero_real_fourier_zeros(
                        tilt, order
                    ),
                    "mirror_weight_maximum_error": max(
                        abs(left - right)
                        for left, right in zip(samples, mirror_samples, strict=True)
                    ),
                    "minimum_replayed_nonzero_weight": min(samples),
                }
            )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "frozen_blobs": FROZEN_SOURCES,
        },
        "tilted_atom": {
            "definition": "f_a(x)=a*exp(a*x)/(exp(a)-1) on [0,1], with f_0=1",
            "laplace_transform": ("f_a_hat(s)=a(exp(a-s)-1)/((exp(a)-1)(a-s))"),
            "reflection": "f_-a(x)=f_a(1-x)",
        },
        "compressed_ladder": {
            "definition": (
                "P_a=f_a*f_a, Q_(a,m)(x)=m P_a^(*m)(m*x), J_(a,m)=D Q_(a,m)"
            ),
            "support": "[0,2] for every a and m",
            "laplace_transform": "J_hat(s)=s[f_a_hat(s/m)]^(2m)",
            "nontrivial_carrier_zeros": (
                "s=m(a+2pi*i*k), nonzero integer k, each of order 2m"
            ),
            "reflection": "J_(-a,m)(x)=-J_(a,m)(2-x)",
            "laplace_reflection": "J_(-a,m)_hat(s)=-exp(-2s)J_(a,m)_hat(-s)",
            "fourier_weight": ("w_(a,m)(t)=t^2|f_a_hat(i*t/m)|^(4m)=w_(-a,m)(t)"),
            "rows": control_rows(),
        },
        "energy_conclusion": {
            "exact_isospectrality": (
                "E_(a,m)(X)=E_(-a,m)(X) for every finite coefficient vector"
            ),
            "all_tilt_fixed_order_criterion": (
                "for every fixed real a and m>=1, RH iff E_(a,m)(X)=X^o(1)"
            ),
            "reason": (
                "a<=0 is directly carrier-safe; a>0 transfers through the "
                "energy-identical -a mirror"
            ),
            "direct_one_sided_scope": (
                "the direct L1/Jordan Landau proof is certified only when "
                "m*a<=0 or m*a>=1/2"
            ),
        },
        "proof_ledger": {
            "tilted_atom_factorization_and_transform": "PROVED EXACT",
            "carrier_chirality_and_zero_set": "PROVED EXACT",
            "fourier_weight_mirror_identity": "PROVED EXACT",
            "finite_prefix_energy_isospectrality": "PROVED EXACT",
            "all_real_tilt_fixed_order_energy_rh_equivalence": (
                "PROVED FROM FROZEN LANDAU/ENERGY ARGUMENT"
            ),
            "direct_one_sided_criterion_inside_carrier_gap": "NOT CLAIMED",
            "any_beta_energy_estimate": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "largest_order": MAXIMUM_ORDER,
            "tilts": len(TILT_SAMPLES),
            "frequencies_per_row": len(FREQUENCY_SAMPLES),
            "zeta_zeros": 0,
            "primes": 0,
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
    text = canonical_text(run(check_sources=not args.no_source_check))
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
