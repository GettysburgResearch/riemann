#!/usr/bin/env python3
"""Bounded exact replay for the function-field beta divisor-wavelet pilot."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "ffps_function_field_beta_divisor_wavelet_pilot.json"

SOURCE_COMMIT = "3658d4c31"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FUNCTION_FIELD_DIVISOR_WAVELET_WITT_FACTORIZATION.md": "ad1ec29ec5678c4dfe356c29f1077de8e2dc868e",
    "research/l-families/atlas/function_field/function_field_divisor_wavelet_witt_factorization.py": "af697bda209ef4e0f614a672d931e76bba94a83c",
    "research/l-families/atlas/function_field/function_field_divisor_wavelet_witt_factorization.json": "41c8ae54f6edd556055fcadee8b6ca72581cbed8",
    "tests/test_function_field_divisor_wavelet_witt_factorization.py": "5fa7501c6bea03a9325d5056ecdd603eed5694b9",
    "research/l-families/atlas/function_field/FUNCTION_FIELD_BETA_BOOLEAN_EVALUATION_BANDPASS.md": "0306cfa06c68375dd62472073698aaae0ace0ff9",
    "research/l-families/atlas/function_field/function_field_beta_boolean_evaluation_bandpass.py": "5ab6b5845838495362bb37883386b640e6a8900d",
    "research/l-families/atlas/function_field/function_field_beta_boolean_evaluation_bandpass.json": "b0131f481be7a052ea5df89e986cbb976c548d65",
    "tests/test_function_field_beta_boolean_evaluation_bandpass.py": "e6fe5181a820a27c995f1beea36b960bfe08edbe",
    "research/l-families/atlas/function_field/pilot.py": "cf1463fdb4f270c550e845874d497edcf41dea9c",
}

PILOT_PATH = HERE / "pilot.py"
PILOT_BLOB = SOURCE_BLOBS["research/l-families/atlas/function_field/pilot.py"]
SPEC = importlib.util.spec_from_file_location("ffps_small_field_pilot", PILOT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the frozen small-field pilot")
pilot = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pilot
SPEC.loader.exec_module(pilot)

Q = 5
CONDUCTOR = (1, 1, 0, 1)  # T^3+T+1
EXCEPTIONAL = (0, 1)  # T
MAXIMUM_DEGREE = 4
BETA_LOCAL = (1, -2, 1)

Series = dict[tuple[int, int], int]
UniSeries = dict[int, int]


def check_source_blobs() -> None:
    completed = subprocess.run(
        ["git", "hash-object", str(PILOT_PATH)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=3,
    )
    if completed.stdout.strip() != PILOT_BLOB:
        raise RuntimeError("working-tree finite-field pilot drifted")
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


def validate_degree(maximum_degree: int) -> None:
    if (
        isinstance(maximum_degree, bool)
        or not isinstance(maximum_degree, int)
        or not 0 <= maximum_degree <= MAXIMUM_DEGREE
    ):
        raise ValueError(f"maximum degree must lie in [0,{MAXIMUM_DEGREE}]")


def multiply_series(left: Series, right: Series, maximum_degree: int) -> Series:
    validate_degree(maximum_degree)
    output: Series = {}
    for (left_degree, left_phase), left_value in left.items():
        for (right_degree, right_phase), right_value in right.items():
            degree = left_degree + right_degree
            if degree > maximum_degree:
                continue
            key = (degree, left_phase + right_phase)
            output[key] = output.get(key, 0) + left_value * right_value
    return {key: value for key, value in output.items() if value}


def power_series(base: Series, exponent: int, maximum_degree: int) -> Series:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("series exponent must be a nonnegative integer")
    result: Series = {(0, 0): 1}
    factor = base
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply_series(result, factor, maximum_degree)
        factor = multiply_series(factor, factor, maximum_degree)
        remaining >>= 1
    return result


def multiply_univariate(
    left: UniSeries,
    right: UniSeries,
    maximum_degree: int,
) -> UniSeries:
    validate_degree(maximum_degree)
    output: UniSeries = {}
    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree
            if degree <= maximum_degree:
                output[degree] = output.get(degree, 0) + left_value * right_value
    return {degree: value for degree, value in output.items() if value}


def inverse_univariate(
    polynomial: Iterable[int],
    maximum_degree: int,
) -> UniSeries:
    validate_degree(maximum_degree)
    coefficients = tuple(polynomial)
    if not coefficients or coefficients[0] != 1:
        raise ValueError("polynomial must have constant coefficient one")
    result: UniSeries = {0: 1}
    for degree in range(1, maximum_degree + 1):
        value = -sum(
            coefficients[index] * result.get(degree - index, 0)
            for index in range(1, min(degree, len(coefficients) - 1) + 1)
        )
        if value:
            result[degree] = value
    return result


def power_univariate(
    base: UniSeries,
    exponent: int,
    maximum_degree: int,
) -> UniSeries:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("univariate exponent must be a nonnegative integer")
    result: UniSeries = {0: 1}
    factor = base
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply_univariate(result, factor, maximum_degree)
        factor = multiply_univariate(factor, factor, maximum_degree)
        remaining >>= 1
    return result


def integer_moebius(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("integer Moebius input must be positive")
    remaining = value
    prime = 2
    count = 0
    while prime * prime <= remaining:
        if remaining % prime:
            prime += 1
            continue
        remaining //= prime
        count += 1
        if remaining % prime == 0:
            return 0
        while remaining % prime == 0:
            remaining //= prime
        prime += 1
    if remaining > 1:
        count += 1
    return -1 if count % 2 else 1


def divisors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("divisor input must be positive")
    return tuple(
        candidate for candidate in range(1, value + 1) if value % candidate == 0
    )


def content_necklace(first: int, second: int) -> int:
    if (
        isinstance(first, bool)
        or isinstance(second, bool)
        or not isinstance(first, int)
        or not isinstance(second, int)
        or first < 0
        or second < 0
        or first + second == 0
    ):
        raise ValueError("necklace content must be nonnegative and nonzero")
    length = first + second
    common = math.gcd(first, second)
    numerator = sum(
        integer_moebius(divisor) * math.comb(length // divisor, first // divisor)
        for divisor in divisors(common)
    )
    if numerator % length:
        raise ArithmeticError("necklace multiplicity lost integrality")
    return numerator // length


def lyndon_count(length: int) -> int:
    if isinstance(length, bool) or not isinstance(length, int) or length < 1:
        raise ValueError("Lyndon length must be positive")
    return sum(content_necklace(first, length - first) for first in range(length + 1))


def irreducibles(maximum_degree: int) -> tuple[tuple[int, ...], ...]:
    validate_degree(maximum_degree)
    return tuple(
        polynomial
        for degree in range(1, maximum_degree + 1)
        for polynomial in pilot.monic_polynomials(Q, degree)
        if pilot.is_irreducible(polynomial, Q)
    )


def character(polynomial: tuple[int, ...]) -> int:
    return pilot.residue_symbol(polynomial, CONDUCTOR, Q)


def factor_subset_degrees(
    factors: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    degrees = tuple(pilot.degree(factor) for factor in factors)
    return tuple(
        sum(degrees[index] for index in range(len(degrees)) if mask >> index & 1)
        for mask in range(1 << len(degrees))
    )


def exceptional_factor(maximum_degree: int) -> Series:
    validate_degree(maximum_degree)
    exceptional_degree = pilot.degree(EXCEPTIONAL)
    exceptional_character = character(EXCEPTIONAL)
    return {
        (alpha * exceptional_degree, alpha * exceptional_degree): (
            BETA_LOCAL[alpha] * exceptional_character**alpha
        )
        for alpha in range(3)
        if alpha * exceptional_degree <= maximum_degree
    }


def core_enumeration(maximum_degree: int) -> Series:
    validate_degree(maximum_degree)
    exceptional_degree = pilot.degree(EXCEPTIONAL)
    exceptional_character = character(EXCEPTIONAL)
    output: Series = {}
    for core_degree in range(maximum_degree + 1):
        for core in pilot.monic_polynomials(Q, core_degree):
            if not pilot.divmod_poly(core, EXCEPTIONAL, Q)[1]:
                continue
            if not pilot.is_squarefree(core, Q):
                continue
            factors = pilot.factor_monic(core, Q)
            core_character = character(core)
            if core_character == 0:
                continue
            core_moebius = -1 if len(factors) % 2 else 1
            for alpha, beta_coefficient in enumerate(BETA_LOCAL):
                total_degree = core_degree + alpha * exceptional_degree
                if total_degree > maximum_degree:
                    continue
                coefficient = (
                    beta_coefficient
                    * exceptional_character**alpha
                    * core_moebius
                    * core_character
                )
                for divisor_degree in factor_subset_degrees(factors):
                    phase = (
                        alpha * exceptional_degree + 2 * divisor_degree - core_degree
                    )
                    key = (total_degree, phase)
                    output[key] = output.get(key, 0) + coefficient
    return {key: value for key, value in output.items() if value}


def literal_beta_enumeration(maximum_degree: int) -> Series:
    validate_degree(maximum_degree)
    exceptional_degree = pilot.degree(EXCEPTIONAL)
    output: Series = {}
    for total_degree in range(maximum_degree + 1):
        for polynomial in pilot.monic_polynomials(Q, total_degree):
            quotient, remainder = pilot.divmod_poly(polynomial, EXCEPTIONAL, Q)
            beta = pilot.moebius_polynomial(polynomial, Q)
            if not remainder:
                beta -= pilot.moebius_polynomial(quotient, Q)
            if beta == 0:
                continue
            alpha = 0
            core = polynomial
            while True:
                quotient, remainder = pilot.divmod_poly(core, EXCEPTIONAL, Q)
                if remainder:
                    break
                alpha += 1
                core = quotient
            if alpha > 2 or not pilot.is_squarefree(core, Q):
                raise ArithmeticError(
                    "literal beta support left the three-channel core"
                )
            factors = pilot.factor_monic(core, Q)
            coefficient = beta * character(polynomial)
            if coefficient == 0:
                continue
            for divisor_degree in factor_subset_degrees(factors):
                phase = (
                    alpha * exceptional_degree + 2 * divisor_degree - pilot.degree(core)
                )
                key = (total_degree, phase)
                output[key] = output.get(key, 0) + coefficient
    return {key: value for key, value in output.items() if value}


def euler_product(maximum_degree: int) -> Series:
    validate_degree(maximum_degree)
    result = exceptional_factor(maximum_degree)
    for prime in irreducibles(maximum_degree):
        if prime == EXCEPTIONAL:
            continue
        prime_character = character(prime)
        if prime_character == 0:
            continue
        prime_degree = pilot.degree(prime)
        local = {
            (0, 0): 1,
            (prime_degree, prime_degree): -prime_character,
            (prime_degree, -prime_degree): -prime_character,
        }
        result = multiply_series(result, local, maximum_degree)
    return result


def inverse_l_excluding_exceptional(
    character_power: int,
    maximum_degree: int,
    prime_list: tuple[tuple[int, ...], ...],
) -> UniSeries:
    validate_degree(maximum_degree)
    result: UniSeries = {0: 1}
    for prime in prime_list:
        if prime == EXCEPTIONAL:
            continue
        prime_character = character(prime)
        if prime_character == 0:
            continue
        prime_degree = pilot.degree(prime)
        if prime_degree > maximum_degree:
            continue
        local = {
            0: 1,
            prime_degree: -(prime_character**character_power),
        }
        result = multiply_univariate(result, local, maximum_degree)
    return result


def substitute_univariate(
    coefficients: UniSeries,
    length: int,
    phase: int,
    maximum_degree: int,
) -> Series:
    validate_degree(maximum_degree)
    return {
        (length * degree, phase * degree): value
        for degree, value in coefficients.items()
        if length * degree <= maximum_degree
    }


def witt_l_product(maximum_degree: int) -> Series:
    validate_degree(maximum_degree)
    prime_list = irreducibles(maximum_degree)
    result = exceptional_factor(maximum_degree)
    for length in range(1, maximum_degree + 1):
        inverse_l = inverse_l_excluding_exceptional(
            length,
            maximum_degree // length,
            prime_list,
        )
        for first in range(length + 1):
            second = length - first
            multiplicity = content_necklace(first, second)
            if multiplicity == 0:
                continue
            factor = substitute_univariate(
                inverse_l,
                length,
                first - second,
                maximum_degree,
            )
            result = multiply_series(
                result,
                power_series(factor, multiplicity, maximum_degree),
                maximum_degree,
            )
    return result


def collapse_zero_frequency(series: Series, maximum_degree: int) -> UniSeries:
    validate_degree(maximum_degree)
    result: UniSeries = {}
    for (degree, _phase), value in series.items():
        result[degree] = result.get(degree, 0) + value
    return {degree: value for degree, value in result.items() if value}


def evaluation_l_coefficients(maximum_degree: int) -> tuple[int, ...]:
    validate_degree(maximum_degree)
    return tuple(
        sum(character(polynomial) for polynomial in pilot.monic_polynomials(Q, degree))
        for degree in range(maximum_degree + 1)
    )


def principal_inverse_l(maximum_degree: int) -> UniSeries:
    validate_degree(maximum_degree)
    numerator = {0: 1, 1: -Q}
    denominator_inverse = inverse_univariate((1, 0, 0, -1), maximum_degree)
    return multiply_univariate(numerator, denominator_inverse, maximum_degree)


def full_inverse_l(character_power: int, maximum_degree: int) -> UniSeries:
    validate_degree(maximum_degree)
    if character_power % 2:
        l_polynomial = evaluation_l_coefficients(pilot.degree(CONDUCTOR) - 1)
        return inverse_univariate(l_polynomial, maximum_degree)
    return principal_inverse_l(maximum_degree)


def zero_frequency_full_l_product(maximum_degree: int) -> UniSeries:
    validate_degree(maximum_degree)
    exceptional_character = character(EXCEPTIONAL)
    numerator = {
        0: 1,
        1: -2 * exceptional_character,
        2: exceptional_character**2,
    }
    exceptional_denominator = inverse_univariate(
        (1, -2 * exceptional_character),
        maximum_degree,
    )
    result = multiply_univariate(numerator, exceptional_denominator, maximum_degree)
    for length in range(1, maximum_degree + 1):
        inverse_l = full_inverse_l(length, maximum_degree // length)
        substituted = {
            length * degree: value
            for degree, value in inverse_l.items()
            if length * degree <= maximum_degree
        }
        result = multiply_univariate(
            result,
            power_univariate(
                substituted,
                lyndon_count(length),
                maximum_degree,
            ),
            maximum_degree,
        )
    return result


def serialize_series(series: Series) -> list[dict[str, int]]:
    return [
        {"degree": degree, "phase": phase, "coefficient": value}
        for (degree, phase), value in sorted(series.items())
    ]


def serialize_univariate(
    series: UniSeries,
    maximum_degree: int,
) -> list[int]:
    return [series.get(degree, 0) for degree in range(maximum_degree + 1)]


def build_report(
    maximum_degree: int = MAXIMUM_DEGREE,
    *,
    check_sources: bool = True,
) -> dict[str, object]:
    validate_degree(maximum_degree)
    if check_sources:
        check_source_blobs()
    if not pilot.is_irreducible(CONDUCTOR, Q):
        raise ArithmeticError("frozen conductor is not irreducible")
    if not pilot.is_irreducible(EXCEPTIONAL, Q):
        raise ArithmeticError("frozen exceptional place is not irreducible")
    if character(EXCEPTIONAL) != 1:
        raise ArithmeticError("frozen exceptional character changed")

    core = core_enumeration(maximum_degree)
    literal = literal_beta_enumeration(maximum_degree)
    euler = euler_product(maximum_degree)
    witt = witt_l_product(maximum_degree)
    if not core == literal == euler == witt:
        raise ArithmeticError("beta/color/Euler/Witt coefficient identity failed")

    zero = collapse_zero_frequency(core, maximum_degree)
    full_l_zero = zero_frequency_full_l_product(maximum_degree)
    if zero != full_l_zero:
        raise ArithmeticError("zero-frequency full-L factorization failed")

    l_rows = evaluation_l_coefficients(maximum_degree)
    expected_l_rows = (1, 3, 5, 0, 0)[: maximum_degree + 1]
    if l_rows != expected_l_rows:
        raise ArithmeticError("frozen quadratic L-polynomial drifted")

    prime_list = irreducibles(maximum_degree)
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "live_pilot_blob": PILOT_BLOB,
        },
        "adapter": {
            "field": "F_5[T]",
            "conductor": "Q=T^3+T+1",
            "exceptional_place": "Pi=T",
            "exceptional_character": 1,
            "beta_local_vector": list(BETA_LOCAL),
            "definition": (
                "sum_(alpha=0)^2 c_alpha chi(Pi)^alpha (uz)^(alpha e) "
                "sum_(M sf,Pi not|M) mu(M)chi(M)u^deg(M)"
                "sum_(A|M)z^(2deg(A)-deg(M))"
            ),
            "euler_product": (
                "(1-chi(Pi)(uz)^e)^2 product_(R!=Pi)"
                "(1-chi(R)(uz)^deg(R)-chi(R)(u/z)^deg(R))"
            ),
            "witt_l_factorization": (
                "(1-chi(Pi)(uz)^e)^2/(1-chi(Pi)(uz)^e-"
                "chi(Pi)(u/z)^e) times product_(a,b)"
                "L_U(u^(a+b)z^(a-b),chi^(a+b))^(-M(a,b))"
            ),
        },
        "quadratic_selection_rule": {
            "odd_word_length": "inverse quadratic L_Q(v,chi)",
            "even_word_length": ("inverse deleted-principal L_U(v,1)=(1-5v)/(1-v^3)"),
            "zero_frequency": ("(1-u)^2/(1-2u) product_(k>=1)L_U(u^k,chi^k)^(-L_k(2))"),
            "first_two_lengths": ("(1+3u+5u^2)^(-2) times (1-5u^2)/(1-u^6)"),
        },
        "exact_example": {
            "quadratic_l_coefficients_through_degree_four": list(l_rows),
            "quadratic_l_polynomial": "1+3u+5u^2",
            "frobenius_eigenvalues": "alpha,beta=(-3+-sqrt(-11))/2",
            "frobenius_modulus": "sqrt(5)",
            "zero_frequency_coefficients": serialize_univariate(
                zero,
                maximum_degree,
            ),
            "laurent_coefficients": serialize_series(core),
            "identity_routes": [
                "literal beta enumeration",
                "three-channel squarefree-core enumeration",
                "two-color Euler product",
                "content-refined twisted Witt/L product",
            ],
        },
        "zero_mode_main_term": {
            "meromorphic_disk": "|u|<1/2",
            "pole_statement": (
                "double poles at u=alpha^-1,beta^-1; the k=2 principal "
                "zero 1-5u^2 does not cancel them"
            ),
            "principal_amplitudes": (
                "A_alpha=lim_(u->alpha^-1)(1-alpha*u)^2 B(u,1), "
                "A_beta=conjugate(A_alpha), both nonzero"
            ),
            "coefficient_law": ("b_n=n(A_alpha alpha^n+A_beta beta^n)+O(5^(n/2))"),
            "critical_energy": (
                "sum_(n<=H)|5^(-n/2)b_n|^2=(|A_alpha|^2+|A_beta|^2)H^3/3+O(H^2)"
            ),
            "interpretation": (
                "the complete zero Fourier mode retains a geometric "
                "quadratic-Frobenius constituent"
            ),
        },
        "proof_ledger": {
            "beta_three_channel_adapter": "PROVED EXACT",
            "literal_core_euler_identity": "PROVED EXACT",
            "twisted_witt_l_factorization": "PROVED FORMALLY",
            "quadratic_odd_even_selection_rule": "PROVED EXACT",
            "frozen_l_polynomial": "PROVED BY COMPLETE RESIDUE-CLASS SUMS",
            "zero_mode_meromorphic_continuation": (
                "PROVED BY NORMAL CONVERGENCE AFTER EXTRACTING LENGTHS 1 AND 2"
            ),
            "zero_mode_energy_main_term": "PROVED BY DOUBLE-POLE COEFFICIENTS",
            "near_square_or_maximal_wavelet_estimate": "NOT PROVED",
            "growing_sieve_or_core_uniformity": "NOT PROVED",
            "number_field_waveprimcar": "NOT PROVED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "q": Q,
            "maximum_monic_degree": maximum_degree,
            "monic_polynomials_per_complete_degree_scan": sum(
                Q**degree for degree in range(maximum_degree + 1)
            ),
            "irreducibles_replayed": len(prime_list),
            "maximum_primitive_word_length": maximum_degree,
            "zeta_zeros": 0,
            "numerical_l_zeros": 0,
            "curves_or_points": 0,
            "random_samples": 0,
            "floating_point_fits": 0,
        },
        "scope_firewall": {
            "complete_degree_shell_only": True,
            "zero_frequency_is_not_near_square_kernel": True,
            "finite_rows_imply_growing_cancellation": False,
            "function_field_rh_imported": False,
            "integer_rh_inferred": False,
        },
    }


def canonical_text(report: dict[str, object]) -> str:
    return json.dumps(report, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    args = parser.parse_args()
    text = canonical_text(build_report(check_sources=not args.no_source_check))
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            raise RuntimeError("canonical JSON drift")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
