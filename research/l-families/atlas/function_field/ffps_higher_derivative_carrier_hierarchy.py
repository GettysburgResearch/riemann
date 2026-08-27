#!/usr/bin/env python3
"""Bounded exact replay for the higher-derivative beta carrier hierarchy."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_higher_derivative_carrier_hierarchy.json"

SOURCE_COMMIT = "866b082b7cecdfa03ebbeca369aa8f654a9bad00"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_BETA_CARRIER_LEGENDRE_MOMENT_TOWER.md": "d0c1fd90b990fe57ef52902b7d434572d870b2ba",
    "research/l-families/atlas/function_field/ffps_beta_carrier_legendre_moment_tower.py": "c81eb277f75becfae22ff3f7a23804c86b586aa9",
    "research/l-families/atlas/function_field/ffps_beta_carrier_legendre_moment_tower.json": "e37644360a071870e4cdbc4eb44e3e5e2e3ba328",
    "tests/test_ffps_beta_carrier_legendre_moment_tower.py": "6c8f2a084d83e772cd4eeecf37ca4874e10adde5",
}

MAX_RUNG = 6
MAX_EXTRA_MOMENT = 3
REPLAY_SUPPORT = Fraction(2)


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
    coefficients: tuple[Fraction, ...], order: int = 1
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


def polynomial_value(coefficients: tuple[Fraction, ...], point: Fraction) -> Fraction:
    output = Fraction(0)
    for coefficient in reversed(coefficients):
        output = output * point + coefficient
    return output


def polynomial_integral(
    coefficients: tuple[Fraction, ...], upper: Fraction
) -> Fraction:
    if upper < 0:
        raise ValueError("upper endpoint must be nonnegative")
    return sum(
        coefficient * upper ** (degree + 1) / (degree + 1)
        for degree, coefficient in enumerate(coefficients)
    )


def carrier_normalization(rung: int, support: Fraction) -> Fraction:
    validate_rung(rung)
    if support <= 0:
        raise ValueError("support must be positive")
    return Fraction(math.factorial(2 * rung + 1), math.factorial(rung) ** 2) / (
        support ** (2 * rung + 1)
    )


def carrier_polynomial(rung: int, support: Fraction) -> tuple[Fraction, ...]:
    normalization = carrier_normalization(rung, support)
    output = [Fraction(0) for _ in range(2 * rung + 1)]
    for added_degree in range(rung + 1):
        degree = rung + added_degree
        output[degree] = (
            normalization
            * (-1) ** added_degree
            * math.comb(rung, added_degree)
            * support ** (rung - added_degree)
        )
    return tuple(output)


def shifted_legendre_polynomial(rung: int, support: Fraction) -> tuple[Fraction, ...]:
    validate_rung(rung)
    if support <= 0:
        raise ValueError("support must be positive")
    return tuple(
        Fraction(
            (-1) ** (rung - degree)
            * math.comb(rung, degree)
            * math.comb(rung + degree, degree)
        )
        / support**degree
        for degree in range(rung + 1)
    )


def detector_polynomial(rung: int, support: Fraction) -> tuple[Fraction, ...]:
    return polynomial_derivative(carrier_polynomial(rung, support), rung)


def detector_legendre_factor(rung: int, support: Fraction) -> Fraction:
    validate_rung(rung)
    if support <= 0:
        raise ValueError("support must be positive")
    return Fraction(
        (-1) ** rung * math.factorial(2 * rung + 1), math.factorial(rung)
    ) / support ** (rung + 1)


def carrier_moment(rung: int, moment_order: int, support: Fraction) -> Fraction:
    validate_rung(rung)
    if moment_order < 0:
        raise ValueError("moment order must be nonnegative")
    if support <= 0:
        raise ValueError("support must be positive")
    return (
        Fraction(
            math.factorial(2 * rung + 1) * math.factorial(rung + moment_order),
            math.factorial(rung) * math.factorial(2 * rung + moment_order + 1),
        )
        * support**moment_order
    )


def detector_moment(rung: int, moment_order: int, support: Fraction) -> Fraction:
    validate_rung(rung)
    if moment_order < 0:
        raise ValueError("moment order must be nonnegative")
    if moment_order < rung:
        return Fraction(0)
    return Fraction(
        (-1) ** rung * math.factorial(moment_order),
        math.factorial(moment_order - rung),
    ) * carrier_moment(rung, moment_order - rung, support)


def sharp_energy_constant(rung: int) -> int:
    validate_rung(rung)
    return math.factorial(rung) ** 2 * (2 * rung + 1) * math.comb(2 * rung, rung) ** 2


def detector_norm_squared(rung: int, support: Fraction) -> Fraction:
    validate_rung(rung)
    if support <= 0:
        raise ValueError("support must be positive")
    return Fraction(sharp_energy_constant(rung)) / support ** (2 * rung + 1)


def higher_legendre_energy_constant(rung: int, extra_order: int) -> int:
    validate_rung(rung)
    if extra_order < 0:
        raise ValueError("extra order must be nonnegative")
    degree = rung + extra_order
    amplitude = (
        math.factorial(degree)
        * math.comb(2 * degree, degree)
        // math.factorial(extra_order)
    )
    return (2 * degree + 1) * amplitude**2


def moment_transform_coefficients(
    rung: int, extra_order: int, support: Fraction
) -> tuple[Fraction, ...]:
    validate_rung(rung)
    if extra_order < 0:
        raise ValueError("extra order must be nonnegative")
    if support <= 0:
        raise ValueError("support must be positive")
    common = Fraction(
        (-1) ** rung * math.factorial(rung) * math.comb(rung + extra_order, rung)
    )
    return tuple(
        common
        * math.comb(extra_order, extra_order - beta_order)
        * carrier_moment(rung, extra_order - beta_order, support)
        for beta_order in range(extra_order + 1)
    )


def autocorrelation_first_available_moment(
    rung: int, beta_prefix: Fraction
) -> Fraction:
    validate_rung(rung)
    return Fraction((-1) ** rung * math.factorial(2 * rung)) * beta_prefix**2


def spectral_first_available_derivative(rung: int, beta_prefix: Fraction) -> Fraction:
    validate_rung(rung)
    return Fraction(math.factorial(2 * rung)) * beta_prefix**2


def critical_width_power(rung: int) -> int:
    validate_rung(rung)
    return 2 * rung + 1


def forward_paid(rung: int, width_power: Fraction) -> bool:
    validate_rung(rung)
    if width_power < 0:
        raise ValueError("width power must be nonnegative")
    return width_power <= critical_width_power(rung)


def reverse_paid(rung: int, width_power: Fraction) -> bool:
    validate_rung(rung)
    if width_power < 0:
        raise ValueError("width power must be nonnegative")
    return width_power >= critical_width_power(rung)


def trivial_dilution_exponent(rung: int, width_power: Fraction) -> Fraction:
    validate_rung(rung)
    critical = Fraction(critical_width_power(rung))
    if not 0 <= width_power < critical:
        raise ValueError("width power must lie below the critical power")
    return Fraction(1, 1) / (critical - width_power)


def zero_exclusion_boundary(rung: int, support_exponent: Fraction) -> Fraction:
    validate_rung(rung)
    if support_exponent < 0:
        raise ValueError("support exponent must be nonnegative")
    return Fraction(1, 2) + Fraction(2 * rung + 1, 2) * support_exponent


def variation_scale_constant_bound(rung: int) -> int:
    """A safe K_m in ||J||_inf+Var(J) <= K_m*S^(-m-1)."""
    validate_rung(rung)
    detector_scale = math.factorial(2 * rung + 1) // math.factorial(rung)
    return detector_scale * (2 * rung + 3)


def support_condition_number(
    rung: int, field_length: Fraction, support: Fraction
) -> Fraction:
    validate_rung(rung)
    if field_length < support or support <= 0:
        raise ValueError("require field_length >= support > 0")
    return (field_length / support) ** critical_width_power(rung)


def normalized_forward_factor(
    rung: int, field_length: Fraction, support: Fraction
) -> Fraction:
    validate_rung(rung)
    if field_length < support or support <= 0:
        raise ValueError("require field_length >= support > 0")
    return (
        (2 * rung + 1)
        * (2 * rung + 3) ** 2
        * (field_length / support) ** (2 * rung + 2)
    )


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    rows = []
    for rung in range(1, MAX_RUNG + 1):
        carrier = carrier_polynomial(rung, REPLAY_SUPPORT)
        detector = detector_polynomial(rung, REPLAY_SUPPORT)
        legendre = shifted_legendre_polynomial(rung, REPLAY_SUPPORT)
        factor = detector_legendre_factor(rung, REPLAY_SUPPORT)
        expected_detector = tuple(factor * coefficient for coefficient in legendre)
        if detector != expected_detector:
            raise AssertionError("Rodrigues/Legendre identity failed")
        if polynomial_integral(carrier, REPLAY_SUPPORT) != 1:
            raise AssertionError("carrier mass failed")
        for derivative_order in range(rung):
            derivative = polynomial_derivative(carrier, derivative_order)
            if polynomial_value(derivative, Fraction(0)) != 0:
                raise AssertionError("left endpoint vanishing failed")
            if polynomial_value(derivative, REPLAY_SUPPORT) != 0:
                raise AssertionError("right endpoint vanishing failed")

        norm_from_polynomial = polynomial_integral(
            polynomial_product(detector, detector), REPLAY_SUPPORT
        )
        norm_from_formula = detector_norm_squared(rung, REPLAY_SUPPORT)
        if norm_from_polynomial != norm_from_formula:
            raise AssertionError("detector norm identity failed")

        carrier_moments = tuple(
            carrier_moment(rung, order, REPLAY_SUPPORT)
            for order in range(MAX_EXTRA_MOMENT + 1)
        )
        for order in range(rung + MAX_EXTRA_MOMENT + 1):
            weighted_detector = tuple((Fraction(0),) * order + detector)
            integrated = polynomial_integral(weighted_detector, REPLAY_SUPPORT)
            if integrated != detector_moment(rung, order, REPLAY_SUPPORT):
                raise AssertionError("detector moment identity failed")

        transform_rows = []
        sample_beta = tuple(Fraction(value) for value in (2, -3, 5, 7))
        for extra_order in range(MAX_EXTRA_MOMENT + 1):
            coefficients = moment_transform_coefficients(
                rung, extra_order, REPLAY_SUPPORT
            )
            leading = Fraction(
                (-1) ** rung
                * math.factorial(rung)
                * math.comb(rung + extra_order, rung)
            )
            if coefficients[-1] != leading:
                raise AssertionError("moment transform lost triangular diagonal")
            sample_value = sum(
                coefficient * sample_beta[index]
                for index, coefficient in enumerate(coefficients)
            )
            transform_rows.append(
                {
                    "extra_order": extra_order,
                    "field_order": rung + extra_order,
                    "coefficients_of_B_0_through_B_extra_order": [
                        fraction_text(value) for value in coefficients
                    ],
                    "sample_value": fraction_text(sample_value),
                    "legendre_energy_constant": higher_legendre_energy_constant(
                        rung, extra_order
                    ),
                }
            )

        critical = critical_width_power(rung)
        escape = trivial_dilution_exponent(rung, Fraction(0))
        boundary_at_escape = zero_exclusion_boundary(rung, escape)
        if boundary_at_escape != 1:
            raise AssertionError("trivial escape did not meet Re(rho)=1")
        beta_prefix = Fraction(3)
        autocorrelation = autocorrelation_first_available_moment(rung, beta_prefix)
        spectral = spectral_first_available_derivative(rung, beta_prefix)
        if spectral != (-1) ** rung * autocorrelation:
            raise AssertionError("spectral/autocorrelation sign failed")

        rows.append(
            {
                "rung": rung,
                "support": fraction_text(REPLAY_SUPPORT),
                "carrier_coefficients": [fraction_text(value) for value in carrier],
                "detector_coefficients": [fraction_text(value) for value in detector],
                "detector_legendre_factor": fraction_text(factor),
                "carrier_moments_q_0_through_q_3": [
                    fraction_text(value) for value in carrier_moments
                ],
                "detector_norm_squared": fraction_text(norm_from_formula),
                "sharp_energy_constant": sharp_energy_constant(rung),
                "variational_minimum_at_support_2": fraction_text(
                    detector_norm_squared(rung, REPLAY_SUPPORT)
                ),
                "critical_width_power": critical,
                "trivial_raw_dilution_exponent": fraction_text(escape),
                "zero_boundary_at_trivial_escape": fraction_text(boundary_at_escape),
                "variation_scale_constant_bound": variation_scale_constant_bound(rung),
                "support_condition_number_at_L_4_S_2": fraction_text(
                    support_condition_number(rung, Fraction(4), Fraction(2))
                ),
                "normalized_forward_factor_at_L_4_S_2": fraction_text(
                    normalized_forward_factor(rung, Fraction(4), Fraction(2))
                ),
                "autocorrelation_order_2m_for_B_0_3": fraction_text(autocorrelation),
                "spectral_derivative_order_2m_for_B_0_3": fraction_text(spectral),
                "moment_transform_rows": transform_rows,
                "phase_rows": [
                    {
                        "width_power": critical - 1,
                        "RH_forward_paid": forward_paid(rung, Fraction(critical - 1)),
                        "reverse_paid": reverse_paid(rung, Fraction(critical - 1)),
                    },
                    {
                        "width_power": critical,
                        "RH_forward_paid": forward_paid(rung, Fraction(critical)),
                        "reverse_paid": reverse_paid(rung, Fraction(critical)),
                    },
                    {
                        "width_power": critical + 1,
                        "RH_forward_paid": forward_paid(rung, Fraction(critical + 1)),
                        "reverse_paid": reverse_paid(rung, Fraction(critical + 1)),
                    },
                ],
            }
        )

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "hierarchy": {
            "rungs": rows,
            "carrier_formula": "Q_(m,S)=(2m+1)!*t^m*(S-t)^m/(m!^2*S^(2m+1))",
            "detector_formula": "D^m Q=(-1)^m*(2m+1)!*P_m(2t/S-1)/(m!*S^(m+1))",
            "moment_formula": "M_(m+r)=(-1)^m*m!*binom(m+r,m)*sum_h binom(r,h)*q_h*B_(r-h)",
            "generating_identity": "H_(m,S,X)(z)=(-z)^m*Q_(m,S)(z)*B_X(z)",
            "sharp_energy_formula": "L^(2m+1)*E>=C_m*|B_0|^2, C_m=(m!)^2*(2m+1)*binom(2m,m)^2",
            "higher_legendre_energy_formula": "(2m+2r+1)*[(m+r)!*binom(2m+2r,m+r)/r!]^2",
            "support_condition_number": "kappa_m=(L/S)^(2m+1)",
            "normalized_energy": "mathfrak_E=L^(2m+1)*E/C_m",
            "growing_rung_forward_factor": "(2m+1)*(2m+3)^2*(L/S)^(2m+2)",
            "spectral_formula": "P^(2m)(0)=(2m)!*|B_0|^2",
            "critical_width_formula": "p_c(m)=2m+1",
        },
        "proof_ledger": {
            "positive_unit_mass_beta_carrier": "PROVED",
            "Rodrigues_Legendre_detector_formula": "PROVED",
            "unique_signed_carrier_variational_optimum": "PROVED",
            "all_order_triangular_moment_transform": "PROVED",
            "sharp_support_energy_pythagorean_identity": "PROVED",
            "complete_higher_rung_Legendre_tower": "PROVED",
            "exact_support_condition_number": "PROVED",
            "first_available_autocorrelation_and_spectral_jet": "PROVED",
            "all_support_fixed_rung_renormalized_RH_equivalence": "PROVED",
            "normalized_safe_growing_rung_RH_equivalence": "PROVED",
            "critical_width_power_within_current_bounds": "PROVED",
            "subcritical_trivial_dilution_schedule": "PROVED",
            "supercritical_adaptive_schedule_obstruction": "PROVED",
            "raw_energy_zero_exclusion_wedge": "PROVED",
            "new_unconditional_subpower_beta_energy_estimate": "NOT PROVED",
            "unrestricted_growing_rung_forward_or_equivalence": "NOT PROVED",
            "arithmetic_improvement_beyond_support_geometry": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_rung": MAX_RUNG,
            "maximum_extra_moment": MAX_EXTRA_MOMENT,
            "beta_terms": 0,
            "primes": 0,
            "zeta_zeros": 0,
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
