#!/usr/bin/env python3
"""Bounded exact replay for the spectral-zero-free carrier tilt."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_spectral_zero_free_carrier_tilt.json"

SOURCE_COMMIT = "0123d1ecb097294fc132cf251aebeab9a6bda169"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_HIGHER_DERIVATIVE_CARRIER_HIERARCHY.md": "d9eda9b3abf512c93c6b0f5c8a84b06b658fe385",
    "research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.py": "83e7ed029c5613f392022c262e4e6bdb95627499",
    "research/l-families/atlas/function_field/ffps_higher_derivative_carrier_hierarchy.json": "8b2be0d6b3bc8a78c44f98269d7a139b7635c3f3",
    "tests/test_ffps_higher_derivative_carrier_hierarchy.py": "3eb7bde31a113603e2a28c50ef29483f0357c9d6",
}

DLMF_ZERO_URL = "https://dlmf.nist.gov/10.21#i"
MAX_RUNG = 6
MAX_PHI_HALF_ORDER = 4


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


def polynomial_derivative(
    coefficients: tuple[Fraction, ...], order: int
) -> tuple[Fraction, ...]:
    if order < 0:
        raise ValueError("derivative order must be nonnegative")
    output = coefficients
    for _ in range(order):
        if len(output) <= 1:
            return (Fraction(0),)
        output = tuple(
            Fraction(degree) * output[degree] for degree in range(1, len(output))
        )
    return output


def polynomial_product(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    output = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] += left_value * right_value
    return tuple(output)


def symmetric_polynomial_integral(coefficients: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (Fraction(2) * coefficient / (degree + 1) if degree % 2 == 0 else Fraction(0))
        for degree, coefficient in enumerate(coefficients)
    )


def centered_beta_polynomial(rung: int) -> tuple[Fraction, ...]:
    validate_rung(rung)
    output = [Fraction(0) for _ in range(2 * rung + 1)]
    for power in range(rung + 1):
        output[2 * power] = Fraction((-1) ** power * math.comb(rung, power))
    return tuple(output)


def multiply_by_x(coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return (Fraction(0),) + coefficients


def ordinary_legendre_polynomial(degree: int) -> tuple[Fraction, ...]:
    if degree < 0:
        raise ValueError("degree must be nonnegative")
    output = [Fraction(0) for _ in range(degree + 1)]
    for k in range(degree // 2 + 1):
        power = degree - 2 * k
        output[power] = Fraction(
            (-1) ** k * math.factorial(2 * degree - 2 * k),
            2**degree
            * math.factorial(k)
            * math.factorial(degree - k)
            * math.factorial(power),
        )
    return tuple(output)


def rodrigues_factor(rung: int) -> int:
    validate_rung(rung)
    return (-1) ** rung * 2**rung * math.factorial(rung)


def centered_beta_even_moment(rung: int, half_order: int) -> Fraction:
    validate_rung(rung)
    if half_order < 0:
        raise ValueError("half order must be nonnegative")
    numerator = Fraction(1)
    denominator = Fraction(1)
    for index in range(half_order):
        numerator *= 2 * index + 1
        denominator *= 2 * rung + 2 * index + 3
    return numerator / denominator


def phi_even_series_coefficients(
    rung: int, max_half_order: int
) -> tuple[Fraction, ...]:
    validate_rung(rung)
    if max_half_order < 0:
        raise ValueError("maximum half order must be nonnegative")
    return tuple(
        centered_beta_even_moment(rung, half_order) / math.factorial(2 * half_order)
        for half_order in range(max_half_order + 1)
    )


def curvature_ratio(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(2 * rung + 1, 2 * rung + 3)


def sharp_energy_constant(rung: int) -> int:
    validate_rung(rung)
    return math.factorial(rung) ** 2 * (2 * rung + 1) * math.comb(2 * rung, rung) ** 2


def centered_carrier_normalization_support_two(rung: int) -> Fraction:
    validate_rung(rung)
    return Fraction(
        math.factorial(2 * rung + 1),
        math.factorial(rung) ** 2 * 2 ** (2 * rung + 1),
    )


def optimal_energy_support_two_from_polynomial(rung: int) -> Fraction:
    carrier = centered_beta_polynomial(rung)
    detector = polynomial_derivative(carrier, rung)
    normalization = centered_carrier_normalization_support_two(rung)
    return normalization**2 * symmetric_polynomial_integral(
        polynomial_product(detector, detector)
    )


def zero_free_vertical_line_from_imaginary_zero_locus(tilt: Fraction) -> bool:
    return tilt != 0


def laplace_zero_line_real_part(tilt: Fraction, support: Fraction) -> Fraction:
    if support <= 0:
        raise ValueError("support must be positive")
    return -2 * tilt / support


def closed_right_half_plane_zero_free(tilt: Fraction) -> bool:
    return tilt > 0


def series_add(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    length = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(length)
    )


def series_scale(
    coefficients: tuple[Fraction, ...], scalar: Fraction
) -> tuple[Fraction, ...]:
    return tuple(scalar * coefficient for coefficient in coefficients)


def series_product(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
    max_degree: int,
) -> tuple[Fraction, ...]:
    if max_degree < 0:
        raise ValueError("maximum degree must be nonnegative")
    output = [Fraction(0) for _ in range(max_degree + 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            if i + j <= max_degree:
                output[i + j] += left_value * right_value
    return tuple(output)


def series_shift(
    coefficients: tuple[Fraction, ...], degree: int, max_degree: int
) -> tuple[Fraction, ...]:
    if degree < 0 or max_degree < 0:
        raise ValueError("degrees must be nonnegative")
    output = [Fraction(0) for _ in range(max_degree + 1)]
    for index, coefficient in enumerate(coefficients):
        if index + degree <= max_degree:
            output[index + degree] = coefficient
    return tuple(output)


def sinh_series(scale: int, max_degree: int) -> tuple[Fraction, ...]:
    if max_degree < 0:
        raise ValueError("maximum degree must be nonnegative")
    return tuple(
        (
            Fraction(scale**degree, math.factorial(degree))
            if degree % 2 == 1
            else Fraction(0)
        )
        for degree in range(max_degree + 1)
    )


def cosh_series(scale: int, max_degree: int) -> tuple[Fraction, ...]:
    if max_degree < 0:
        raise ValueError("maximum degree must be nonnegative")
    return tuple(
        (
            Fraction(scale**degree, math.factorial(degree))
            if degree % 2 == 0
            else Fraction(0)
        )
        for degree in range(max_degree + 1)
    )


def divide_series_after_common_zero(
    numerator: tuple[Fraction, ...],
    denominator: tuple[Fraction, ...],
    max_output_degree: int,
) -> tuple[Fraction, ...]:
    if max_output_degree < 0:
        raise ValueError("maximum output degree must be nonnegative")
    numerator_lead = next(
        (index for index, value in enumerate(numerator) if value), None
    )
    denominator_lead = next(
        (index for index, value in enumerate(denominator) if value), None
    )
    if numerator_lead is None or denominator_lead is None:
        raise ValueError("series must be nonzero")
    if numerator_lead != denominator_lead:
        raise ValueError("series do not have a common leading order")
    shifted_numerator = numerator[numerator_lead:]
    shifted_denominator = denominator[denominator_lead:]
    output: list[Fraction] = []
    for degree in range(max_output_degree + 1):
        numerator_value = (
            shifted_numerator[degree]
            if degree < len(shifted_numerator)
            else Fraction(0)
        )
        correction = sum(
            shifted_denominator[index] * output[degree - index]
            for index in range(1, degree + 1)
            if index < len(shifted_denominator)
        )
        output.append((numerator_value - correction) / shifted_denominator[0])
    return tuple(output)


def first_rung_scaled_energy_series(max_output_degree: int) -> tuple[Fraction, ...]:
    """Series of S^3*||D Q_(1,S,tau)||_2^2 at tau=0."""
    if max_output_degree < 0:
        raise ValueError("maximum output degree must be nonnegative")
    internal_degree = max_output_degree + 8
    sinh_two = sinh_series(2, internal_degree)
    cosh_two = cosh_series(2, internal_degree)
    one_plus_four_t2 = [Fraction(0) for _ in range(internal_degree + 1)]
    one_plus_four_t2[0] = 1
    one_plus_four_t2[2] = 4
    bracket = series_add(
        series_product(tuple(one_plus_four_t2), sinh_two, internal_degree),
        series_scale(series_shift(cosh_two, 1, internal_degree), Fraction(-2)),
    )
    numerator = series_shift(bracket, 3, internal_degree)

    tau_cosh = series_shift(cosh_series(1, internal_degree), 1, internal_degree)
    difference = series_add(
        tau_cosh, series_scale(sinh_series(1, internal_degree), Fraction(-1))
    )
    denominator = series_scale(
        series_product(difference, difference, internal_degree), Fraction(4)
    )
    return divide_series_after_common_zero(numerator, denominator, max_output_degree)


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    rows = []
    for rung in range(1, MAX_RUNG + 1):
        centered = centered_beta_polynomial(rung)
        detector = polynomial_derivative(centered, rung)
        first_variation = polynomial_derivative(multiply_by_x(centered), rung)
        factor = Fraction(rodrigues_factor(rung))
        expected_detector = tuple(
            factor * value for value in ordinary_legendre_polynomial(rung)
        )
        expected_variation = tuple(
            factor * value for value in ordinary_legendre_polynomial(rung + 1)
        )
        if detector != expected_detector:
            raise AssertionError("matched Rodrigues identity failed")
        if first_variation != expected_variation:
            raise AssertionError("tilt first-variation Legendre identity failed")

        detector_norm = symmetric_polynomial_integral(
            polynomial_product(detector, detector)
        )
        variation_norm = symmetric_polynomial_integral(
            polynomial_product(first_variation, first_variation)
        )
        ratio = variation_norm / detector_norm
        if ratio != curvature_ratio(rung):
            raise AssertionError("energy curvature ratio failed")

        optimal_energy = optimal_energy_support_two_from_polynomial(rung)
        expected_optimal = Fraction(sharp_energy_constant(rung), 2 ** (2 * rung + 1))
        if optimal_energy != expected_optimal:
            raise AssertionError("sharp support-two energy failed")

        phi_coefficients = phi_even_series_coefficients(rung, MAX_PHI_HALF_ORDER)
        if phi_coefficients[0] != 1:
            raise AssertionError("Phi normalization failed")
        if phi_coefficients[1] != Fraction(1, 2 * (2 * rung + 3)):
            raise AssertionError("Phi quadratic coefficient failed")

        rows.append(
            {
                "rung": rung,
                "centered_beta_coefficients": [
                    fraction_text(value) for value in centered
                ],
                "matched_detector_coefficients": [
                    fraction_text(value) for value in detector
                ],
                "tilt_first_variation_detector_coefficients": [
                    fraction_text(value) for value in first_variation
                ],
                "common_Legendre_factor": fraction_text(factor),
                "matched_detector_norm_centered_unnormalized": fraction_text(
                    detector_norm
                ),
                "first_variation_norm_centered_unnormalized": fraction_text(
                    variation_norm
                ),
                "energy_quadratic_ratio": fraction_text(ratio),
                "sharp_energy_support_2": fraction_text(optimal_energy),
                "Phi_even_series_coefficients_z_0_to_z_8": [
                    fraction_text(value) for value in phi_coefficients
                ],
                "sample_nonzero_tilts_miss_imaginary_zero_locus": {
                    fraction_text(
                        tilt
                    ): zero_free_vertical_line_from_imaginary_zero_locus(tilt)
                    for tilt in (
                        Fraction(-2),
                        Fraction(-1, 10),
                        Fraction(1, 10),
                        Fraction(2),
                    )
                },
            }
        )

    first_rung_energy_series = first_rung_scaled_energy_series(8)
    expected_first_rung_series = (
        Fraction(12),
        Fraction(0),
        Fraction(36, 5),
        Fraction(0),
        Fraction(72, 175),
        Fraction(0),
        Fraction(-4, 315),
        Fraction(0),
        Fraction(204, 336875),
    )
    if first_rung_energy_series != expected_first_rung_series:
        raise AssertionError("first-rung exact energy series failed")

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "classical_external_input": {
            "source": "NIST Digital Library of Mathematical Functions, section 10.21(i)",
            "url": DLMF_ZERO_URL,
            "statement_used": "all zeros of J_nu are real for real nu>=-1",
            "specialized_consequence": "all nonzero zeros of Phi_m are purely imaginary for integer m>=1",
            "computational_reproof_claimed": False,
        },
        "tilt_theorem": {
            "Phi_formula": "normalized integral from -1 to 1 of exp(z*x)*(1-x^2)^m",
            "Fourier_formula": "Qhat_tau(omega)=exp(-i*a)*Phi_m(tau-i*a)/Phi_m(tau), a=omega*S/2",
            "zero_free_conclusion": "for every real tau!=0, Qhat_tau has no real-frequency zero",
            "derivative_conclusion": "Fourier(D^m Q_tau) has exactly the forced order-m zero at omega=0",
            "Laplace_formula": "Qscr_tau(z)=exp(S*z/2)*Phi_m(tau+S*z/2)/Phi_m(tau)",
            "Laplace_zero_line": "Re(z)=-2*tau/S",
            "orientation_firewall": "tau>0 is closed-right-half-plane zero-free; tau<0 has a right-half-plane zero lattice",
            "variational_conclusion": "the positive real-Fourier-zero-free class has infimum C_m/S^(2m+1), not attained",
            "local_energy_formula": "E(tau)/E(0)=1+(2m+1)/(2m+3)*tau^2+O_m(tau^4)",
            "first_rung_exact_energy": "S^3*E=tau^3*((4tau^2+1)*sinh(2tau)-2tau*cosh(2tau))/(4*(tau*cosh(tau)-sinh(tau))^2)",
            "first_rung_scaled_energy_series_tau_0_through_tau_8": [
                fraction_text(value) for value in first_rung_energy_series
            ],
            "rows": rows,
        },
        "proof_ledger": {
            "positive_normalized_exponential_tilt": "PROVED",
            "exact_Fourier_shift": "PROVED",
            "all_nonzero_Phi_zeros_purely_imaginary": "CLASSICAL EXTERNAL THEOREM",
            "real_Fourier_zero_free_for_nonzero_tilt": "PROVED FROM CLASSICAL INPUT",
            "only_forced_derivative_zero_remains": "PROVED",
            "strict_energy_inequality_for_nonzero_tilt": "PROVED",
            "zero_free_class_same_infimum_not_attained": "PROVED",
            "exact_quadratic_energy_coefficient": "PROVED",
            "Laplace_zero_line_and_orientation": "PROVED",
            "new_beta_convolution_cancellation": "NOT PROVED",
            "uniform_condition_number_improvement_from_real_zero_freeness": "DISPROVED IN THIS ENERGY CLASS",
            "subpower_detector_estimate_RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_rung": MAX_RUNG,
            "maximum_Phi_half_order": MAX_PHI_HALF_ORDER,
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
