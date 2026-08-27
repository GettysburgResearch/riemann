#!/usr/bin/env python3
"""Bounded exact replay for the beta carrier Legendre moment tower."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_beta_carrier_legendre_moment_tower.json"

SOURCE_COMMIT = "fb5e545bcfceb8aeac1059d72e5cf94f99132d09"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_MOVING_SUPPORT_CARRIER_PHASE_DIAGRAM.md": "4a25a443e9f1e16528ba96a03657e1e66034563b",
    "research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.py": "772029c8c111265cd0809cb3190211d4acdbbc68",
    "research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.json": "59fde9c967d66265f6f68c2722b8b782f6b87dd8",
    "tests/test_ffps_moving_support_carrier_phase_diagram.py": "b0912d25bb256aae472002b51631993b97af1cd9",
}

MAX_ORDER = 6
MAX_AUTOCORRELATION_ORDER = 8


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


def parabolic_carrier_moments(
    max_order: int, support: Fraction = Fraction(1)
) -> tuple[Fraction, ...]:
    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    if support <= 0:
        raise ValueError("support must be positive")
    return tuple(
        Fraction(6, (j + 2) * (j + 3)) * support**j for j in range(max_order + 1)
    )


def field_moment_coefficients(
    order: int, carrier_moments: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    if order < 1:
        raise ValueError("order must be positive")
    if len(carrier_moments) < order:
        raise ValueError("insufficient carrier moments")
    if carrier_moments[0] != 1:
        raise ValueError("carrier mass must be one")
    coefficients: list[Fraction] = []
    for beta_order in range(order):
        carrier_order = order - 1 - beta_order
        coefficient = (
            -order
            * math.comb(order - 1, carrier_order)
            * carrier_moments[carrier_order]
        )
        coefficients.append(Fraction(coefficient))
    return tuple(coefficients)


def recover_beta_moments(
    field_moments: tuple[Fraction, ...],
    carrier_moments: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    if len(field_moments) < 2:
        raise ValueError("field moments must include M_0 and M_1")
    if field_moments[0] != 0:
        raise ValueError("M_0 must vanish")
    max_beta_order = len(field_moments) - 2
    if len(carrier_moments) <= max_beta_order:
        raise ValueError("insufficient carrier moments")
    beta_moments: list[Fraction] = []
    for r in range(max_beta_order + 1):
        lower = sum(
            Fraction(math.comb(r, j)) * carrier_moments[j] * beta_moments[r - j]
            for j in range(1, r + 1)
        )
        beta_moments.append(-field_moments[r + 1] / (r + 1) - lower)
    return tuple(beta_moments)


def shifted_legendre_coefficients(order: int) -> tuple[int, ...]:
    if order < 0:
        raise ValueError("order must be nonnegative")
    return tuple(
        (-1) ** (order - degree)
        * math.comb(order, degree)
        * math.comb(order + degree, degree)
        for degree in range(order + 1)
    )


def polynomial_inner_product(
    left: tuple[int | Fraction, ...],
    right: tuple[int | Fraction, ...],
) -> Fraction:
    return sum(
        Fraction(left_degree) * Fraction(right_degree) / (i + j + 1)
        for i, left_degree in enumerate(left)
        for j, right_degree in enumerate(right)
    )


def legendre_channel_beta_coefficients(
    order: int,
    carrier_moments: tuple[Fraction, ...],
    field_length: Fraction,
) -> tuple[Fraction, ...]:
    if order < 1:
        raise ValueError("order must be positive")
    if field_length <= 0:
        raise ValueError("field length must be positive")
    shifted = shifted_legendre_coefficients(order)
    output = [Fraction(0) for _ in range(order)]
    for moment_order in range(1, order + 1):
        multiplier = Fraction(shifted[moment_order], 1) / field_length**moment_order
        field_coefficients = field_moment_coefficients(moment_order, carrier_moments)
        for beta_order, coefficient in enumerate(field_coefficients):
            output[beta_order] += multiplier * coefficient
    return tuple(output)


def adjusted_beta_channel_coefficients(
    order: int,
    carrier_moments: tuple[Fraction, ...],
    field_length: Fraction,
) -> tuple[Fraction, ...]:
    channel = legendre_channel_beta_coefficients(order, carrier_moments, field_length)
    normalization = -(field_length**order) / (order * math.comb(2 * order, order))
    output = tuple(normalization * coefficient for coefficient in channel)
    if output[-1] != 1:
        raise AssertionError("adjusted beta channel is not monic")
    return output


def legendre_delta_coefficients(
    order: int, field_length: Fraction
) -> tuple[Fraction, ...]:
    """Coefficients of M_0,...,M_order in L^order*d_order."""
    if order < 0:
        raise ValueError("order must be nonnegative")
    if field_length <= 0:
        raise ValueError("field length must be positive")
    shifted = shifted_legendre_coefficients(order)
    return tuple(
        Fraction(shifted[moment_order]) * field_length ** (order - moment_order)
        for moment_order in range(order + 1)
    )


def legendre_energy_constant(order: int) -> int:
    if order < 1:
        raise ValueError("order must be positive")
    return (2 * order + 1) * order**2 * math.comb(2 * order, order) ** 2


def uniform_forward_multiplier(
    moment_order: int, field_length: Fraction, carrier_l1_norm: Fraction
) -> Fraction:
    """Coefficient in |M_k| <= multiplier * sup|B_0|."""
    if moment_order < 1:
        raise ValueError("moment order must be positive")
    if field_length <= 0:
        raise ValueError("field length must be positive")
    if carrier_l1_norm < 0:
        raise ValueError("carrier L1 norm must be nonnegative")
    return 2 * moment_order * carrier_l1_norm * field_length ** (moment_order - 1)


def autocorrelation_moment(field_moments: tuple[Fraction, ...], order: int) -> Fraction:
    if order < 0:
        raise ValueError("order must be nonnegative")
    if len(field_moments) <= order:
        raise ValueError("insufficient field moments")
    return sum(
        Fraction((-1) ** j * math.comb(order, j))
        * field_moments[j]
        * field_moments[order - j]
        for j in range(order + 1)
    )


def autocorrelation_term_coefficients(order: int) -> dict[str, int]:
    if order < 0:
        raise ValueError("order must be nonnegative")
    output: dict[str, int] = {}
    for j in range(order + 1):
        pair = tuple(sorted((j, order - j)))
        key = f"M_{pair[0]}*M_{pair[1]}"
        output[key] = output.get(key, 0) + (-1) ** j * math.comb(order, j)
    return {key: value for key, value in output.items() if value}


def spectral_even_derivative(
    field_moments: tuple[Fraction, ...], half_order: int
) -> Fraction:
    if half_order < 0:
        raise ValueError("half order must be nonnegative")
    return (-1) ** half_order * autocorrelation_moment(field_moments, 2 * half_order)


def pole_order_after_moment(zero_multiplicity: int, moment_order: int) -> int:
    if zero_multiplicity < 1:
        raise ValueError("zero multiplicity must be positive")
    if moment_order < 1:
        raise ValueError("moment order must be positive")
    return zero_multiplicity + moment_order - 1


def moving_carrier_cancellation_first_moment(
    beta_0: Fraction, beta_1: Fraction
) -> Fraction:
    """First carrier moment q_1 that forces M_2 to vanish."""
    if beta_0 == 0:
        raise ValueError("beta_0 must be nonzero")
    return -beta_1 / beta_0


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    carrier_moments = parabolic_carrier_moments(MAX_ORDER)
    field_rows = []
    for order in range(1, MAX_ORDER + 1):
        coefficients = field_moment_coefficients(order, carrier_moments)
        if coefficients[-1] != -order:
            raise AssertionError("field/source moment map lost triangular diagonal")
        field_rows.append(
            {
                "order": order,
                "coefficients_of_B_0_through_B_order_minus_1": [
                    fraction_text(value) for value in coefficients
                ],
                "leading_coefficient": fraction_text(coefficients[-1]),
            }
        )

    sample_beta = tuple(Fraction(value) for value in (2, -3, 5, 7, -11, 13))
    sample_field = [Fraction(0)]
    for order in range(1, MAX_ORDER + 1):
        coefficients = field_moment_coefficients(order, carrier_moments)
        sample_field.append(
            sum(coefficients[index] * sample_beta[index] for index in range(order))
        )
    recovered = recover_beta_moments(tuple(sample_field), carrier_moments)
    if recovered != sample_beta:
        raise AssertionError("triangular moment recovery failed")
    cancellation_q1 = moving_carrier_cancellation_first_moment(
        sample_beta[0], sample_beta[1]
    )
    cancellation_coefficients = field_moment_coefficients(
        2, (Fraction(1), cancellation_q1)
    )
    cancellation_value = sum(
        coefficient * sample_beta[index]
        for index, coefficient in enumerate(cancellation_coefficients)
    )
    if cancellation_value != 0:
        raise AssertionError("moving-carrier M_2 cancellation failed")

    orthogonality = []
    for left_order in range(MAX_ORDER + 1):
        row = []
        for right_order in range(MAX_ORDER + 1):
            value = polynomial_inner_product(
                shifted_legendre_coefficients(left_order),
                shifted_legendre_coefficients(right_order),
            )
            expected = (
                Fraction(1, 2 * left_order + 1)
                if left_order == right_order
                else Fraction(0)
            )
            if value != expected:
                raise AssertionError("shifted Legendre orthogonality failed")
            row.append(fraction_text(value))
        orthogonality.append(row)

    field_length = Fraction(2)
    legendre_rows = []
    for order in range(1, MAX_ORDER + 1):
        adjusted = adjusted_beta_channel_coefficients(
            order, carrier_moments, field_length
        )
        legendre_rows.append(
            {
                "order": order,
                "shifted_legendre_coefficients": list(
                    shifted_legendre_coefficients(order)
                ),
                "adjusted_coefficients_of_B_0_through_B_order_minus_1_at_L_2": [
                    fraction_text(value) for value in adjusted
                ],
                "energy_constant": legendre_energy_constant(order),
                "delta_coefficients_at_L_2": [
                    fraction_text(value)
                    for value in legendre_delta_coefficients(order, field_length)
                ],
                "uniform_forward_multiplier_at_L_2_Q_L1_1": fraction_text(
                    uniform_forward_multiplier(order, field_length, Fraction(1))
                ),
                "pole_order_for_double_zero": pole_order_after_moment(2, order),
            }
        )

    sample_moments = tuple(
        Fraction(value) for value in (0, -2, 3, 5, -7, 11, 13, -17, 19)
    )
    autocorrelation_rows = []
    for order in range(MAX_AUTOCORRELATION_ORDER + 1):
        value = autocorrelation_moment(sample_moments, order)
        if order % 2 == 1 and value != 0:
            raise AssertionError("odd autocorrelation moment did not vanish")
        autocorrelation_rows.append(
            {
                "order": order,
                "term_coefficients": autocorrelation_term_coefficients(order),
                "sample_value": fraction_text(value),
                "sample_spectral_derivative": (
                    fraction_text(spectral_even_derivative(sample_moments, order // 2))
                    if order % 2 == 0
                    else None
                ),
            }
        )

    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "moment_transform": {
            "generating_identity": "H_X(z)=-z*Q(z)*B_X(z)",
            "forward_formula": "M_k=-k*sum_(j=0)^(k-1) binom(k-1,j)*q_j*B_(k-1-j)",
            "inverse_formula": "B_r=-M_(r+1)/(r+1)-sum_(j=1)^r binom(r,j)*q_j*B_(r-j)",
            "parabolic_carrier_moments_support_1": [
                fraction_text(value) for value in carrier_moments
            ],
            "field_rows": field_rows,
            "sample_beta_moments": [fraction_text(value) for value in sample_beta],
            "sample_field_moments": [fraction_text(value) for value in sample_field],
            "recovered_beta_moments": [fraction_text(value) for value in recovered],
            "moving_carrier_M_2_cancellation": {
                "chosen_q_1": fraction_text(cancellation_q1),
                "resulting_M_2": fraction_text(cancellation_value),
            },
        },
        "fixed_moment_rh_criterion": {
            "statement": "for each fixed k>=1 and one fixed carrier Q, RH iff M_k(X)=X^o(1)",
            "power_exponent_firewall": "every fixed nonzero polynomial log-weight has the same infimal nonnegative power-growth exponent as B_0",
            "uniform_forward_bound": "|M_k|<=2*k*||Q||_1*L^(k-1)*sup_(t<=X)|B_0(t)|",
            "growing_order_forward_window": "RH implies M_k(X)=X^o(1) if log(k)+k*log(L)=o(log(X))",
            "operator": "G_k(s)=-k*R_(k-1)(-d/ds)F(s), with R monic",
            "off_line_zero_effect": "a zero of multiplicity m creates a pole of order m+k-1",
            "multiplicity_firewall": "critical-line multiplicity and the growing-k converse/equivalence are not controlled",
        },
        "legendre_tower": {
            "shifted_formula": "P_k(2x-1)=sum_m (-1)^(k-m)*binom(k,m)*binom(k+m,m)*x^m",
            "orthogonality_matrix_degrees_0_to_6": orthogonality,
            "energy_formula": "E=sum_(k=1)^R C_k*|A_(k-1)|^2/L^(2k+1)+orthogonal_remainder",
            "constant_formula": "C_k=(2k+1)*k^2*binom(2k,k)^2",
            "rows": legendre_rows,
        },
        "autocorrelation_tower": {
            "formula": "integral u^r*C_X(u) du=sum_j (-1)^j*binom(r,j)*M_j*M_(r-j)",
            "rows": autocorrelation_rows,
        },
        "proof_ledger": {
            "all_order_exponential_generating_identity": "PROVED",
            "triangular_field_source_moment_transform": "PROVED",
            "each_fixed_signed_field_moment_RH_equivalent": "PROVED",
            "fixed_polynomial_power_exponent_equivalence": "PROVED",
            "RH_forward_growing_order_window": "PROVED",
            "moving_carrier_M_2_tuning_no_go": "PROVED",
            "off_line_pole_order_magnification": "PROVED",
            "shifted_legendre_pythagorean_tower": "PROVED",
            "all_order_autocorrelation_moment_identity": "PROVED",
            "new_subpower_moment_estimate": "NOT PROVED",
            "growing_order_converse_or_equivalence": "NOT PROVED",
            "critical_line_zero_multiplicity_theorem": "NOT PROVED",
            "RH_or_GRH": "NOT PROVED",
        },
        "resource_caps": {
            "maximum_moment_order": MAX_ORDER,
            "maximum_autocorrelation_order": MAX_AUTOCORRELATION_ORDER,
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
