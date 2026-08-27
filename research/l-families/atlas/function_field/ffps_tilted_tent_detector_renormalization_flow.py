#!/usr/bin/env python3
"""Bounded replay for the tilted-tent detector renormalization flow."""

from __future__ import annotations

import argparse
import cmath
import json
import math
import subprocess
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_tilted_tent_detector_renormalization_flow.json"
SOURCE_COMMIT = "3658d4c31"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md": "bd4cbb842e78c1dad5d380c8d20ff14c39bba15e",
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py": "df80000192292cc5fc1cd08013f152fb257054f9",
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.json": "7e8889aa0dd1b01674e20158a52502cff0d8dffa",
    "tests/test_ffps_zero_free_beta_energy_ladder.py": "983a1320f89087028f6724fe36aaca5ca1309b15",
}
CUSP_SOURCE_COMMIT = "3dbf13f6d1c49e573a5b9cd8355d9c124273062b"
CUSP_SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md": "e7959b8788b8a374920aa53bcafd1fb28cda3b72",
    "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py": "52023bb4527a32a2c9983fdd25707da3361242e8",
    "research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.json": "0031e9ae114d7bf6c60d69789d5d52fe4cf04f6e",
    "tests/test_ffps_bandpass_assembled_perron_leakage.py": (
        "efc9cde7eef3e833aaa5ac40b5d37b1e34f76770"
    ),
}
LIVE_SOURCE = HERE / "ffps_zero_free_beta_energy_ladder.py"
LIVE_SOURCE_BLOB = SOURCE_BLOBS[
    "research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py"
]

REPLAY_ORDERS = (1, 2, 4, 8, 32, 128)
WEIGHT_FREQUENCIES = (0.25, 0.5, 1.0, 2.0, 3.0)
MAXIMUM_REPLAY_ORDER = max(REPLAY_ORDERS)

E_SYMBOL = sp.Symbol("E", positive=True)
T_SYMBOL = sp.Symbol("t")


def check_live_source_blob() -> None:
    completed = subprocess.run(
        ["git", "hash-object", str(LIVE_SOURCE)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=3,
    )
    if completed.stdout.strip() != LIVE_SOURCE_BLOB:
        raise RuntimeError("working-tree zero-free ladder producer drifted")


def check_source_blobs() -> None:
    check_live_source_blob()
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
    for path, expected in CUSP_SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{CUSP_SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen cusp-source blob mismatch: {path}")


def validate_order(order: int) -> None:
    if (
        isinstance(order, bool)
        or not isinstance(order, int)
        or not 1 <= order <= MAXIMUM_REPLAY_ORDER
    ):
        raise ValueError(f"order must lie in [1,{MAXIMUM_REPLAY_ORDER}]")


def symbolic_mgf() -> sp.Expr:
    return ((E_SYMBOL * sp.exp(T_SYMBOL) - 1) / ((E_SYMBOL - 1) * (1 + T_SYMBOL))) ** 2


def symbolic_cumulants(maximum_order: int = 4) -> tuple[sp.Expr, ...]:
    if (
        isinstance(maximum_order, bool)
        or not isinstance(maximum_order, int)
        or not 1 <= maximum_order <= 8
    ):
        raise ValueError("maximum cumulant order must lie in [1,8]")
    cumulant_generator = sp.log(symbolic_mgf())
    return tuple(
        sp.factor(sp.diff(cumulant_generator, T_SYMBOL, order).subs(T_SYMBOL, 0))
        for order in range(1, maximum_order + 1)
    )


def expected_first_four_cumulants() -> tuple[sp.Expr, ...]:
    e = E_SYMBOL
    return (
        2 / (e - 1),
        2 * (e**2 - 3 * e + 1) / (e - 1) ** 2,
        -2 * (2 * e**3 - 7 * e**2 + 5 * e - 2) / (e - 1) ** 3,
        2 * (6 * e**4 - 25 * e**3 + 32 * e**2 - 25 * e + 6) / (e - 1) ** 4,
    )


def exact_cumulant_strings() -> dict[str, str]:
    values = symbolic_cumulants(4)
    return {
        f"kappa_{index}": sp.sstr(value) for index, value in enumerate(values, start=1)
    }


def exact_gaussian_constants() -> dict[str, str]:
    return {
        "derivative_gaussian_energy": "1/(4*sqrt(pi))",
        "derivative_energy_first_correction": "5*lambda_4/(64*sqrt(pi)*m)",
        "gaussian_density_energy": "1/(2*sqrt(pi))",
        "cusp_refill_first_correction": "lambda_4/(32*sqrt(pi)*m)",
        "positive_and_negative_jordan_mass_limit": "1/sqrt(2*pi)",
        "total_variation_limit": "sqrt(2/pi)",
    }


def mean_and_variance() -> tuple[float, float]:
    e = math.e
    mean = 2.0 / (e - 1.0)
    variance = 2.0 * (1.0 - e / (e - 1.0) ** 2)
    return mean, variance


def normalized_p_fourier(frequency: float) -> complex:
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    denominator = (math.e - 1.0) * (1.0 - 1j * frequency)
    return ((cmath.exp(1.0 - 1j * frequency) - 1.0) / denominator) ** 2


def diffusive_weight(order: int, frequency: float) -> float:
    validate_order(order)
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    _, variance = mean_and_variance()
    scaled_frequency = frequency / math.sqrt(variance * order)
    modulus = abs(normalized_p_fourier(scaled_frequency))
    return frequency * frequency * modulus ** (2 * order)


def gaussian_derivative_weight(frequency: float) -> float:
    if not math.isfinite(frequency):
        raise ValueError("frequency must be finite")
    return frequency * frequency * math.exp(-(frequency**2))


def weight_control_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for order in REPLAY_ORDERS:
        errors = [
            abs(
                diffusive_weight(order, frequency)
                - gaussian_derivative_weight(frequency)
            )
            for frequency in WEIGHT_FREQUENCIES
        ]
        rows.append(
            {
                "order": order,
                "maximum_sample_error": max(errors),
                "support": [
                    "-(mu/sigma)*sqrt(m)",
                    "((2-mu)/sigma)*sqrt(m)",
                ],
                "real_weight_zero_set": [0],
                "carrier_zero_real_part": "sigma*sqrt(m)",
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    actual = symbolic_cumulants(4)
    expected = expected_first_four_cumulants()
    if any(sp.simplify(left - right) != 0 for left, right in zip(actual, expected)):
        raise AssertionError("symbolic cumulants drifted")
    rows = weight_control_rows()
    if rows[-1]["maximum_sample_error"] >= rows[0]["maximum_sample_error"]:
        raise AssertionError("bounded diffusive-weight control failed to improve")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "live_imported_source_blob": LIVE_SOURCE_BLOB,
            "cusp_commit": CUSP_SOURCE_COMMIT,
            "cusp_git_blobs": CUSP_SOURCE_BLOBS,
        },
        "probability_kernel": {
            "unnormalized_tent": "Phi(x)=exp(x-1)(1-|x-1|)_+",
            "mass": "Z=4sinh^2(1/2)=(e-1)^2/e",
            "density": "P(x)=exp(x)*min(x,2-x)/(e-1)^2 on [0,2]",
            "factorization": "P=f*f, f(v)=exp(v)/(e-1) on [0,1]",
            "mgf": "M_X(t)=((exp(1+t)-1)/((e-1)(1+t)))^2",
            "cumulants": exact_cumulant_strings(),
            "general_cumulant": ("for r>=2: 2[(-1)^(r-1)Li_(1-r)(e^-1)+(-1)^r(r-1)!]"),
            "mean": "mu=2/(e-1)",
            "variance": "sigma^2=2(e^2-3e+1)/(e-1)^2",
        },
        "diffusive_flow": {
            "unscaled_kernel": "K_m=D(P^(*m)), support [0,2m]",
            "normalized_density": ("f_m(y)=sigma*sqrt(m)P^(*m)(m*mu+sigma*sqrt(m)y)"),
            "normalized_detector": (
                "J_m(y)=m*sigma^2*K_m(m*mu+sigma*sqrt(m)y)=f_m'(y)"
            ),
            "support": ("[-(mu/sigma)sqrt(m),((2-mu)/sigma)sqrt(m)]"),
            "fourier_transform": "J_m_hat(t)=i*t*psi(t/sqrt(m))^m",
            "local_uniform_limit": "J_m_hat(t)->i*t*exp(-t^2/2)",
            "edgeworth": (
                "J_m(y)=-y*phi(y)-lambda_3*H_4(y)*phi(y)/(6sqrt(m))"
                "+O(m^-1) uniformly; proved by the stated Fourier-splitting lemma"
            ),
            "weight": "W_m(t)=t^2|psi(t/sqrt(m))|^(2m)",
            "weight_limit": "W_m(t)->t^2 exp(-t^2)",
            "weight_expansion": ("W_m=t^2 exp(-t^2)[1+lambda_4*t^4/(12m)+O_A(m^-2)]"),
            "weight_l1_error": "integral |W_m-t^2 exp(-t^2)| dt=O(m^-1)",
            "autocorrelation_limit": ("R_infinity(x)=(1-x^2/2)exp(-x^2/4)/(4sqrt(pi))"),
            "control_rows": rows,
        },
        "carrier": {
            "P_laplace": "((exp(1-s)-1)/((e-1)(1-s)))^2",
            "K_m_laplace": "s*P_laplace(s)^m",
            "K_m_zeros": ("s=0 simple; s=1+2pi*i*k, k!=0, order 2m"),
            "J_m_zeros": ("s=0 simple; s=sigma*sqrt(m)(1+2pi*i*k), k!=0, order 2m"),
            "open_rh_strip": (
                "causal K_m is zero-free for every finite m; centered J_m is "
                "zero-free only when sigma*sqrt(m)>=1/2"
            ),
            "real_fourier_zero_set": "{0}",
        },
        "norm_and_jordan_asymptotics": {
            **exact_gaussian_constants(),
            "J_m_energy": ("1/(4sqrt(pi))+5lambda_4/(64sqrt(pi)m)+O(m^-2)"),
            "K_m_energy": ("1/(4sqrt(pi)sigma^3*m^(3/2))*(1+O(m^-1))"),
            "K_m_each_jordan_side": ("1/(sigma*sqrt(2*pi*m))*(1+o(1))"),
            "cusp_refill": (
                "ell_m(0)=||f_m||_2^2=1/(2sqrt(pi))+lambda_4/(32sqrt(pi)m)+O(m^-2)"
            ),
            "exact_signed_moments": "integral J_m=0 and integral y*J_m(y)dy=-1",
        },
        "fixed_vs_growing_firewall": {
            "fixed_order": (
                "each finite m is compact and carrier-safe for the beta Mellin pole"
            ),
            "unscaled_fixed_frequency": (
                "t^2|P_hat(t)|^(2m) decays exponentially for every fixed t!=0"
            ),
            "diffusive_zoom": (
                "the Gaussian derivative appears only after centering and sqrt(m) scaling"
            ),
            "causality": (
                "centered J_m is noncausal; a right shift restores causality but adds a shrinking Laplace multiplier"
            ),
            "noncommuting_limits": (
                "m->infinity, Perron c->0, and height T->infinity are not interchanged"
            ),
            "arithmetic_estimate": "no beta energy, Jordan-mass, Perron, or RH estimate is proved",
        },
        "proof_ledger": {
            "probability_factorization_and_cumulants": "PROVED EXACT",
            "support_and_carrier_zeros": "PROVED EXACT",
            "local_uniform_fourier_and_weight_limits": "PROVED",
            "uniform_edgeworth_remainder": (
                "PROVED BY THE SELF-CONTAINED FOURIER-SPLITTING LEMMA IN THE MARKDOWN"
            ),
            "weight_l1_and_norm_asymptotics": ("PROVED BY THE SAME FOURIER SPLITTING"),
            "jordan_asymptotics": (
                "PROVED USING THE STATED CLASSICAL LOG-CONCAVITY CLOSURE LEMMA"
            ),
            "growing_order_beta_theorem": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "largest_replayed_order": MAXIMUM_REPLAY_ORDER,
            "weight_frequencies": len(WEIGHT_FREQUENCIES),
            "symbolic_cumulant_order": 4,
            "zeta_zeros": 0,
            "numerical_zeta_values": 0,
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
