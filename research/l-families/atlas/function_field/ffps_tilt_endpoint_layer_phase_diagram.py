#!/usr/bin/env python3
"""Bounded exact replay for the carrier-tilt endpoint-layer phase diagram."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_tilt_endpoint_layer_phase_diagram.json"

SOURCE_COMMIT = "805ab873cb051c739f19978ebb772b2625adcffb"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_SPECTRAL_ZERO_FREE_CARRIER_TILT.md": "a23f6f57dc87ef698fd06e9fe2680119e032e37b",
    "research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.py": "f8f7c7596c368293cf5005c25e8f156ebcf0b94c",
    "research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.json": "3d7e74420af1b85c7ab35a11166c54e3218434d2",
    "tests/test_ffps_spectral_zero_free_carrier_tilt.py": "2c2215c3810089b46b7f3d83d5ed7b5aa77f3e85",
}

MAX_RUNG = 6
NUMERICAL_TILTS = (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(4))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


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


def validate_rung(rung: int) -> None:
    if rung < 1:
        raise ValueError("rung must be positive")


def phi_leading_constant(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(
        math.factorial(2 * rung + 1),
        2 ** (rung + 1) * math.factorial(rung),
    )


def phi_first_relative_correction(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(-rung * (rung + 1), 2)


def energy_leading_constant(rung: int) -> int:
    validate_rung(rung)
    return math.comb(2 * rung, rung)


def energy_first_relative_correction(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(rung * (2 * rung + 1), 2)


def effective_width_energy_constant(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(math.comb(2 * rung, rung), 2 ** (2 * rung + 1))


def laguerre_polynomial(degree: int) -> tuple[Fraction, ...]:
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    return tuple(
        Fraction((-1) ** power * math.comb(degree, power), math.factorial(power))
        for power in range(degree + 1)
    )


def exponential_two_inner(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> Fraction:
    """Integral_0^infinity exp(-2u)*left(u)*right(u) du."""
    output = Fraction(0)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output += (
                left_value
                * right_value
                * Fraction(math.factorial(i + j), 2 ** (i + j + 1))
            )
    return output


def gamma_layer_norm(rung: int) -> Fraction:
    validate_rung(rung)
    laguerre = laguerre_polynomial(rung)
    return exponential_two_inner(laguerre, laguerre)


def gamma_layer_cross_next(rung: int) -> Fraction:
    validate_rung(rung)
    return exponential_two_inner(
        laguerre_polynomial(rung), laguerre_polynomial(rung + 1)
    )


def correction_from_gamma_layer(rung: int) -> Fraction:
    validate_rung(rung)
    coefficient = Fraction(rung * (rung + 1), 2)
    return 2 * coefficient * gamma_layer_cross_next(rung) / gamma_layer_norm(rung)


def first_rung_algebraic_asymptotic_coefficients() -> tuple[Fraction, ...]:
    """Coefficients of T^3,T^2,T,1 in S^3 E_1(T)."""
    return Fraction(2), Fraction(3), Fraction(9, 2), Fraction(6)


def first_rung_phi(tilt: float) -> float:
    if tilt < 0:
        raise ValueError("tilt magnitude must be nonnegative")
    if tilt == 0:
        return 1.0
    return 3 * (tilt * math.cosh(tilt) - math.sinh(tilt)) / tilt**3


def first_rung_sup_detector(tilt: float, support: float = 1.0) -> float:
    if support <= 0:
        raise ValueError("support must be positive")
    return 6 * math.exp(tilt) / (support**2 * first_rung_phi(tilt))


def first_rung_detector_variation(tilt: float, support: float = 1.0) -> float:
    if tilt < 0:
        raise ValueError("tilt magnitude must be nonnegative")
    if support <= 0:
        raise ValueError("support must be positive")
    phi = first_rung_phi(tilt)
    if tilt <= 0.5:
        return 24 * math.cosh(tilt) / (support**2 * phi)
    root = math.sqrt(tilt**2 + 2)
    bracket = math.exp(tilt) + (root - 1) * math.exp(root - 2) / tilt
    return 12 * bracket / (support**2 * phi)


def renormalized_safe_log_cost(
    rung: int,
    theta_log: Fraction,
    one_plus_eta_log: Fraction,
) -> Fraction:
    """Log_X of the sufficient normalized forward factor."""
    validate_rung(rung)
    theta_log = Fraction(theta_log)
    one_plus_eta_log = Fraction(one_plus_eta_log)
    if theta_log < 0 or one_plus_eta_log < 0:
        raise ValueError("log costs must be nonnegative")
    return (2 * rung + 1) * theta_log + one_plus_eta_log


def raw_power_exponents(
    rung: int, support_power: Fraction, tilt_power: Fraction
) -> tuple[Fraction, Fraction]:
    """Two power exponents in the RH-forward raw-energy bound."""
    validate_rung(rung)
    sigma = Fraction(support_power)
    alpha = Fraction(tilt_power)
    if sigma < 0 or alpha < 0:
        raise ValueError("powers must be nonnegative")
    difference = alpha - sigma
    return (2 * rung + 1) * difference, (2 * rung + 2) * difference


def raw_power_schedule_certified(
    rung: int, support_power: Fraction, tilt_power: Fraction
) -> bool:
    return max(raw_power_exponents(rung, support_power, tilt_power)) <= 0


def critical_power_exponents(
    rung: int, support_power: Fraction, tilt_power: Fraction
) -> tuple[Fraction, Fraction]:
    """Power exponents after multiplying raw energy by L^(2m+1)."""
    validate_rung(rung)
    sigma = Fraction(support_power)
    alpha = Fraction(tilt_power)
    if sigma <= 0 or alpha < 0:
        raise ValueError("critical power chart requires positive support power")
    return (2 * rung + 1) * alpha, (2 * rung + 2) * alpha - sigma


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    rows = []
    for rung in range(1, MAX_RUNG + 1):
        norm = gamma_layer_norm(rung)
        expected_norm = effective_width_energy_constant(rung)
        if norm != expected_norm:
            raise AssertionError("Gamma-layer Laguerre norm failed")
        correction = correction_from_gamma_layer(rung)
        if correction != energy_first_relative_correction(rung):
            raise AssertionError("Gamma-layer first correction failed")
        rows.append(
            {
                "rung": rung,
                "Phi_leading_constant": fraction_text(phi_leading_constant(rung)),
                "Phi_first_relative_correction": fraction_text(
                    phi_first_relative_correction(rung)
                ),
                "energy_leading_constant": energy_leading_constant(rung),
                "energy_first_relative_correction": fraction_text(correction),
                "effective_width_energy_constant": fraction_text(
                    effective_width_energy_constant(rung)
                ),
                "Laguerre_norm": fraction_text(norm),
                "Laguerre_cross_next": fraction_text(gamma_layer_cross_next(rung)),
                "raw_power_chart_sigma_1_alpha_0_1_2": [
                    {
                        "tilt_power": fraction_text(alpha),
                        "exponents": [
                            fraction_text(value)
                            for value in raw_power_exponents(rung, Fraction(1), alpha)
                        ],
                        "certified": raw_power_schedule_certified(
                            rung, Fraction(1), alpha
                        ),
                    }
                    for alpha in (Fraction(0), Fraction(1), Fraction(2))
                ],
            }
        )

    numerical_bv = []
    for tilt in NUMERICAL_TILTS:
        value = float(tilt)
        numerical_bv.append(
            {
                "tilt_magnitude": fraction_text(tilt),
                "Phi_1": f"{first_rung_phi(value):.12f}",
                "detector_sup_support_1": f"{first_rung_sup_detector(value):.12f}",
                "detector_variation_support_1": f"{first_rung_detector_variation(value):.12f}",
            }
        )

    return {
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "endpoint_layer_theorem": {
            "Phi_asymptotic": "Phi_m(T)=A_m*exp(T)*T^(-m-1)*(1-m*(m+1)/(2T)+O_m(T^-2))",
            "Phi_leading_constant": "A_m=(2m+1)!/(2^(m+1)*m!)",
            "Gamma_layer": "u=T*(1-sign(tau)*x), g_m(u)=u^m*exp(-u)/m!",
            "Gamma_derivative": "g_m^(m)(u)=exp(-u)*L_m(u)",
            "energy_asymptotic": "E_m=binom(2m,m)*T^(2m+1)/S^(2m+1)*(1+m*(2m+1)/(2T)+O_m(T^-2))",
            "effective_width": "w=S/(2T), E_m~[binom(2m,m)/2^(2m+1)]*w^(-2m-1)",
            "first_rung_exact_algebraic_coefficients_T3_T2_T1_T0": [
                fraction_text(value)
                for value in first_rung_algebraic_asymptotic_coefficients()
            ],
            "first_rung_BV": "||J||_infty=6*exp(T)/(S^2*Phi_1(T)); Var(J) is piecewise at T=1/2",
            "moving_tilt_RH_forward": "E<=X^o(1)*[(Lambda/S)^(2m+1)+log(X)*(Lambda/S)^(2m+2)], Lambda=1+|tau|",
            "critical_safe_window": "(2m+1)*log(Theta)+log(1+H)=o(log X), Theta=Lambda*L/S, H=Lambda*log(X)/S",
            "uniform_simple_window": "(1+|tau_X|)*L_X/S_X=X^o(1); in particular |tau_X|=X^o(1) is safe for every S_X>=1",
            "raw_power_chart": "for S=X^(sigma+o(1)), T=X^(alpha+o(1)), sigma>0 and alpha>=0, raw energy is certified subpower when alpha<=sigma",
            "rows": rows,
            "bounded_first_rung_BV_certificates": numerical_bv,
        },
        "proof_ledger": {
            "fixed_rung_endpoint_Gamma_layer": "PROVED",
            "energy_leading_constant_and_first_correction": "PROVED EXACT",
            "first_rung_exact_BV_formula": "PROVED EXACT",
            "moving_tilt_RH_forward_bound": "PROVED",
            "safe_critical_normalization_window": "PROVED SUFFICIENT",
            "raw_power_schedule_phase_chart": "PROVED SUFFICIENT UNDER RH",
            "polynomial_tilt_safe_for_critical_normalization": "NOT PROVED",
            "converse_failure_outside_safe_window": "NOT PROVED",
            "new_unconditional_beta_estimate": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_rung": MAX_RUNG,
            "numerical_tilt_values": len(NUMERICAL_TILTS),
            "beta_terms": 0,
            "primes": 0,
            "zeta_zeros": 0,
            "Bessel_root_searches": 0,
            "random_samples": 0,
            "quadratures": 0,
            "curve_computations": 0,
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
