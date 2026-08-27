#!/usr/bin/env python3
"""Exact replay for the beta source under a Boolean evaluation restriction."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "070be728e"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FUNCTION_FIELD_BASEWAVE_SHADOW.md": (
        "e66606a8e06977b4ed54734942adf6c74cf82286"
    ),
    "research/l-families/atlas/function_field/function_field_basewave_shadow.py": (
        "e4896b7c8e59ba2f3a264d4e846e9ba821ec8116"
    ),
    "research/l-families/atlas/function_field/FUNCTION_FIELD_BASEWAVE_CURVE_EXTENSION.md": (
        "fd8f0c7659b5d5d3e00ff7b1d6b720b77cce2afc"
    ),
    "research/l-families/atlas/function_field/function_field_basewave_curve_extension.py": (
        "d2db36d21823d5a28dd4dd3207469e9c9d9edbc7"
    ),
    "research/l-families/atlas/function_field/FFPS_BANDPASS_BETA_ENERGY_LADDER.md": (
        "0ac23a6c384a896e50fed21ca7d8bf079c338ac0"
    ),
    "research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py": (
        "e5091a72b15dc6a5c73d0e0c828ceeb8eb9baef6"
    ),
    "research/l-families/atlas/function_field/FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md": (
        "21ef8f5215ca349f0efffd52dca1543ef6d988d6"
    ),
    "research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py": (
        "2dbe93508eadcc9ba9ed15a5f64d02f13c728ef3"
    ),
}
REPLAY_FIELD_SIZES = (3, 5, 7)
REPLAY_CONDUCTOR_DEGREES = (9, 10)
REPLAY_SERIES_CAP = 40

Polynomial = tuple[Fraction, ...]


def check_source_blobs() -> None:
    """Authenticate the exact source and function-field predecessors."""
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


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def trim(polynomial: Polynomial) -> Polynomial:
    if not polynomial:
        return (Fraction(0),)
    end = len(polynomial)
    while end > 1 and polynomial[end - 1] == 0:
        end -= 1
    return polynomial[:end]


def polynomial_add(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    result = [Fraction(0)] * size
    for index in range(size):
        if index < len(left):
            result[index] += left[index]
        if index < len(right):
            result[index] += right[index]
    return trim(tuple(result))


def polynomial_scale(polynomial: Polynomial, scalar: Fraction) -> Polynomial:
    return trim(tuple(scalar * coefficient for coefficient in polynomial))


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            result[left_degree + right_degree] += left_value * right_value
    return trim(tuple(result))


def polynomial_power(polynomial: Polynomial, exponent: int) -> Polynomial:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("polynomial exponent must be a nonnegative integer")
    result: Polynomial = (Fraction(1),)
    base = trim(polynomial)
    power = exponent
    while power:
        if power & 1:
            result = polynomial_multiply(result, base)
        base = polynomial_multiply(base, base)
        power //= 2
    return result


def monomial_factor(degree: int, coefficient: Fraction) -> Polynomial:
    validate_positive_integer(degree, "monomial degree")
    result = [Fraction(0)] * (degree + 1)
    result[0] = Fraction(1)
    result[degree] = coefficient
    return tuple(result)


def rational_series(
    numerator: Polynomial, denominator: Polynomial, coefficient_cap: int
) -> Polynomial:
    """Return coefficients through cap of numerator/denominator."""
    if isinstance(coefficient_cap, bool) or not isinstance(coefficient_cap, int):
        raise TypeError("coefficient cap must be an integer")
    if coefficient_cap < 0:
        raise ValueError("coefficient cap must be nonnegative")
    denominator = trim(denominator)
    if denominator[0] == 0:
        raise ValueError("denominator must have nonzero constant coefficient")
    result = [Fraction(0)] * (coefficient_cap + 1)
    for degree in range(coefficient_cap + 1):
        target = numerator[degree] if degree < len(numerator) else Fraction(0)
        target -= sum(
            (
                denominator[index] * result[degree - index]
                for index in range(1, min(degree, len(denominator) - 1) + 1)
            ),
            Fraction(0),
        )
        result[degree] = target / denominator[0]
    return tuple(result)


def bandpass_polynomial(
    seed: Polynomial,
    step: int,
    order: int,
    box_length: int = 1,
    box_order: int = 0,
) -> Polynomial:
    """Exact degree-lattice analogue of boxes followed by fixed differences."""
    validate_positive_integer(step, "difference step")
    validate_positive_integer(order, "difference order")
    validate_positive_integer(box_length, "box length")
    if isinstance(box_order, bool) or not isinstance(box_order, int) or box_order < 0:
        raise ValueError("box order must be a nonnegative integer")
    seed = trim(tuple(Fraction(value) for value in seed))
    if all(value == 0 for value in seed):
        raise ValueError("seed polynomial must be nonzero")
    difference = monomial_factor(step, Fraction(-1))
    difference = polynomial_scale(difference, Fraction(1, step))
    box = tuple(Fraction(1, box_length) for _ in range(box_length))
    return polynomial_multiply(
        seed,
        polynomial_multiply(
            polynomial_power(difference, order), polynomial_power(box, box_order)
        ),
    )


def vanishing_order_at_one(polynomial: Polynomial) -> int:
    """Multiplicity of z=1 as a root, by exact formal derivatives."""
    polynomial = trim(polynomial)
    for derivative_order in range(len(polynomial)):
        value = Fraction(0)
        for degree in range(derivative_order, len(polynomial)):
            falling = factorial(degree) // factorial(degree - derivative_order)
            value += polynomial[degree] * falling
        if value != 0:
            return derivative_order
    raise ArithmeticError("zero polynomial has no finite vanishing order")


def beta_local_coefficients(character_value: int) -> tuple[int, int, int]:
    if character_value not in (-1, 1):
        raise ValueError("quadratic character value must be -1 or 1")
    return (1, -2 * character_value, 1)


def beta_local_panel() -> dict[str, object]:
    rows = []
    for value in (-1, 1):
        local = tuple(Fraction(entry) for entry in beta_local_coefficients(value))
        squared = polynomial_power((Fraction(1), Fraction(-value)), 2)
        if local != squared:
            raise ArithmeticError("literal beta local factor is not a square")
        rows.append(
            {
                "character_value_at_exceptional_place": value,
                "coefficients": [int(entry) for entry in local],
                "factorization": f"(1-({value})u^e)^2",
            }
        )
    return {
        "rows": rows,
        "global_weighted_identity": (
            "sum_D beta_P(D)psi(D)u^deg(D)=(1-psi(P)u^e)/L_U(u,psi)"
        ),
    }


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value, "integer")
    return tuple(
        candidate for candidate in range(1, value + 1) if value % candidate == 0
    )


def mobius_integer(value: int) -> int:
    validate_positive_integer(value, "integer")
    remaining = value
    prime_count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            if remaining % prime == 0:
                return 0
            prime_count += 1
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def irreducible_count(field_size: int, degree: int) -> int:
    validate_positive_integer(field_size, "field size")
    validate_positive_integer(degree, "degree")
    if field_size < 2:
        raise ValueError("field size must be at least two")
    numerator = sum(
        mobius_integer(divisor) * field_size ** (degree // divisor)
        for divisor in divisors(degree)
    )
    if numerator % degree:
        raise ArithmeticError("irreducible-degree count lost integrality")
    return numerator // degree


def quadratic_completed_degree(conductor_degree: int) -> int:
    validate_positive_integer(conductor_degree, "conductor degree")
    even_correction = 1 if conductor_degree % 2 == 0 else 0
    return conductor_degree - 1 - even_correction


def degree_obstruction_panel(filter_polynomial: Polynomial) -> dict[str, object]:
    filter_degree = len(trim(filter_polynomial)) - 1
    rows: list[dict[str, object]] = []
    for field_size in REPLAY_FIELD_SIZES:
        for conductor_degree in REPLAY_CONDUCTOR_DEGREES:
            completed_degree = quadratic_completed_degree(conductor_degree)
            if completed_degree <= filter_degree:
                raise ArithmeticError("replay conductor does not cross the degree gate")
            count = irreducible_count(field_size, conductor_degree)
            if count <= 0:
                raise ArithmeticError(
                    "replay conductor degree has no irreducible modulus"
                )
            rows.append(
                {
                    "field_size": field_size,
                    "conductor_degree": conductor_degree,
                    "quadratic_completed_l_degree": completed_degree,
                    "filter_degree": filter_degree,
                    "irreducible_modulus_count": count,
                    "all_frobenius_modes_can_be_cancelled": False,
                }
            )
    return {
        "criterion": (
            "if d-1-1_(2|d)>deg(B), the completed quadratic L polynomial "
            "cannot divide B"
        ),
        "rows": rows,
    }


def a1_boolean_series(
    square_root_q: int,
    exceptional_degree: int,
    conductor_degree: int,
    character_at_exceptional: int,
    boolean_sign: int,
    filter_polynomial: Polynomial,
    completed_l_polynomial: Polynomial,
    coefficient_cap: int,
) -> dict[str, Polynomial]:
    """Exact normalized A1 trivial/character/Boolean coefficient series."""
    validate_positive_integer(square_root_q, "square root of field size")
    validate_positive_integer(exceptional_degree, "exceptional degree")
    validate_positive_integer(conductor_degree, "conductor degree")
    if character_at_exceptional not in (-1, 1):
        raise ValueError("character at exceptional place must be -1 or 1")
    if boolean_sign not in (-1, 1):
        raise ValueError("Boolean sign must be -1 or 1")
    completed_l_polynomial = trim(completed_l_polynomial)
    if completed_l_polynomial[0] != 1:
        raise ValueError("completed L polynomial must have constant coefficient one")

    exceptional_scale = Fraction(1, square_root_q**exceptional_degree)
    trivial_numerator = polynomial_multiply(
        filter_polynomial,
        polynomial_multiply(
            monomial_factor(exceptional_degree, -exceptional_scale),
            (Fraction(1), Fraction(-square_root_q)),
        ),
    )
    trivial_denominator = monomial_factor(
        conductor_degree, Fraction(-1, square_root_q**conductor_degree)
    )
    character_numerator = polynomial_multiply(
        filter_polynomial,
        monomial_factor(
            exceptional_degree, -character_at_exceptional * exceptional_scale
        ),
    )
    character_denominator = completed_l_polynomial
    if conductor_degree % 2 == 0:
        character_denominator = polynomial_multiply(
            (Fraction(1), Fraction(-1, square_root_q)), character_denominator
        )

    trivial = rational_series(trivial_numerator, trivial_denominator, coefficient_cap)
    character = rational_series(
        character_numerator, character_denominator, coefficient_cap
    )
    boolean = tuple(
        (trivial[index] + boolean_sign * character[index]) / 2
        for index in range(coefficient_cap + 1)
    )
    return {
        "trivial": trivial,
        "character": character,
        "boolean": boolean,
        "trivial_numerator": trivial_numerator,
        "trivial_denominator": trivial_denominator,
        "character_numerator": character_numerator,
        "character_denominator": character_denominator,
    }


def periodic_control_panel() -> dict[str, object]:
    """A bounded exact residue control; no arithmetic realization is asserted."""
    filter_polynomial = bandpass_polynomial(
        (Fraction(1),), step=1, order=1, box_length=1, box_order=0
    )
    series = a1_boolean_series(
        square_root_q=3,
        exceptional_degree=1,
        conductor_degree=3,
        character_at_exceptional=-1,
        boolean_sign=1,
        filter_polynomial=filter_polynomial,
        completed_l_polynomial=(Fraction(1), Fraction(0), Fraction(1)),
        coefficient_cap=REPLAY_SERIES_CAP,
    )
    character = series["character"]
    start = len(series["character_numerator"])
    for degree in range(start, REPLAY_SERIES_CAP - 3):
        if character[degree + 4] != character[degree]:
            raise ArithmeticError("formal unit-root control lost period four")
    block = character[start : start + 4]
    character_mean_square = sum((value * value for value in block), Fraction(0)) / 4
    boolean_energy_leading_coefficient = character_mean_square / 4
    if boolean_energy_leading_coefficient != Fraction(5, 18):
        raise ArithmeticError("formal Boolean energy coefficient changed")
    boolean = series["boolean"]
    if any(
        boolean[index] != (series["trivial"][index] + series["character"][index]) / 2
        for index in range(REPLAY_SERIES_CAP + 1)
    ):
        raise ArithmeticError("Boolean Fourier projector changed")
    return {
        "field_size": 9,
        "conductor_degree": 3,
        "completed_l_control": "P(z)=1+z^2 (Weil-admissible formal control only)",
        "filter": [str(value) for value in filter_polynomial],
        "eventual_character_period": [str(value) for value in block],
        "character_mean_square": str(character_mean_square),
        "boolean_energy_leading_coefficient": str(boolean_energy_leading_coefficient),
        "boolean_coefficients_through_12": [str(value) for value in boolean[:13]],
        "arithmetic_modulus_realization_claimed": False,
    }


def boolean_parallelogram_panel() -> dict[str, object]:
    """Exact amplitude-versus-positive-energy firewall for the two classes."""
    filter_polynomial = bandpass_polynomial(
        (Fraction(1),), step=1, order=1, box_length=1, box_order=0
    )
    common = {
        "square_root_q": 3,
        "exceptional_degree": 1,
        "conductor_degree": 3,
        "character_at_exceptional": -1,
        "filter_polynomial": filter_polynomial,
        "completed_l_polynomial": (Fraction(1), Fraction(0), Fraction(1)),
        "coefficient_cap": 20,
    }
    plus = a1_boolean_series(boolean_sign=1, **common)
    minus = a1_boolean_series(boolean_sign=-1, **common)
    checks = 0
    for degree in range(21):
        left = plus["boolean"][degree]
        right = minus["boolean"][degree]
        trivial = plus["trivial"][degree]
        character = plus["character"][degree]
        if left + right != trivial or left - right != character:
            raise ArithmeticError("Boolean coherent recombination changed")
        if (
            left * left + right * right
            != (trivial * trivial + character * character) / 2
        ):
            raise ArithmeticError("Boolean positive-energy parallelogram changed")
        checks += 1
    return {
        "coefficient_checks": checks,
        "coherent_amplitude_identity": "h_+(n)+h_-(n)=h_triv(n)",
        "difference_identity": "h_+(n)-h_-(n)=h_chi(n)",
        "positive_energy_identity": (
            "|h_+(n)|^2+|h_-(n)|^2=(|h_triv(n)|^2+|h_chi(n)|^2)/2"
        ),
        "verdict": (
            "positive class averaging retains half the inverse-L energy; "
            "coherent amplitude recombination removes it"
        ),
    }


def main_term_formula() -> dict[str, str]:
    return {
        "surviving_order": "M_lambda=max(m_lambda-ord_(z=lambda^-1)B(z),0)",
        "coefficient_expansion": (
            "h_n=sum_(M_lambda>0)Q_lambda(n)lambda^n+O(R^-n), deg(Q_lambda)=M_lambda-1"
        ),
        "coefficient_recurrence": (
            "if L_norm(z)=1+sum_(k=1)^N ell_k z^k and C(z)=N(z)/L_norm(z), "
            "then c_n=N_n-sum_(k=1)^N ell_k c_(n-k)"
        ),
        "principal_coefficient": ("A_lambda=lim_(z->lambda^-1)(1-lambda*z)^M H(z)"),
        "simple_principal_coefficient": (
            "A_lambda=sigma*B(lambda^-1)(1-chi(P)q^(-e/2)lambda^-e)"
            "/[2(1-lambda^-1/sqrt(q))^epsilon*"
            "prod_(mu!=lambda)(1-mu/lambda)^m_mu]"
        ),
        "energy_asymptotic": (
            "sum_(n<=H)|h_n|^2=H^(2M-1)/[(2M-1)((M-1)!)^2] "
            "*sum_(M_lambda=M)|A_lambda|^2+O(H^(2M-2))"
        ),
        "simple_root_case": ("sum_(n<=H)|h_n|^2=H*sum_lambda|A_lambda|^2+O(1)"),
    }


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    release_filter = bandpass_polynomial(
        (Fraction(1), Fraction(2), Fraction(1)),
        step=1,
        order=2,
        box_length=3,
        box_order=1,
    )
    if vanishing_order_at_one(release_filter) != 2:
        raise ArithmeticError("degree band-pass lost its exact notch order")
    return {
        "source_contract": {
            "source_commit": SOURCE_COMMIT,
            "source_blobs": SOURCE_BLOBS,
            "literal_source": "beta_P(D)=mu(D)-1_(P<=D)mu(D-P)",
            "normalization": "u=z/sqrt(q), so degree n carries q^(-n/2)",
        },
        "literal_beta": beta_local_panel(),
        "degree_bandpass": {
            "formula": ("B(z)=K(z)((1-z^s)/s)^r((1+...+z^(ell-1))/ell)^j"),
            "release_control_coefficients": [str(value) for value in release_filter],
            "release_control_degree": len(release_filter) - 1,
            "zero_order_at_z_1": vanishing_order_at_one(release_filter),
            "fixed_parameters": True,
        },
        "evaluation_boolean": {
            "selector": ("delta_sigma(D)=1_(Q not<=D)(1+sigma*chi_Q(D))/2"),
            "complete_a1_identity": (
                "H_complete(z)=B(z)(1-q^(-e/2)z^e)(1-sqrt(q)z), a polynomial"
            ),
            "deletion_only_identity": (
                "H_Qfree(z)=B(z)(1-q^(-e/2)z^e)(1-sqrt(q)z)"
                "/(1-q^(-d/2)z^d), exponentially decaying"
            ),
            "all_curve_identity": (
                "A_sigma(z)=B(z)/2*[(1-q^(-e/2)z^e)/Z_U(z/sqrt(q))"
                "+sigma(1-chi(P)q^(-e/2)z^e)/L_U(z/sqrt(q),chi)]"
            ),
            "a1_identity": (
                "A_sigma(z)=B(z)/2*[(1-q^(-e/2)z^e)(1-sqrt(q)z)"
                "/(1-q^(-d/2)z^d)+sigma(1-chi(P)q^(-e/2)z^e)"
                "/L_Q(z/sqrt(q),chi)]"
            ),
            "incomplete": True,
            "evaluation_character": (
                "chi_Q(f) is the quadratic character of f mod Q in F_(q^d); "
                "Q-divisible f are excluded"
            ),
            "positive_energy_firewall": boolean_parallelogram_panel(),
        },
        "frobenius_truth_serum": {
            "completed_quadratic_degree": "N_Q=d-1-1_(2|d)",
            "normalized_roots": (
                "P_Q(z/sqrt(q))=prod_lambda(1-lambda*z)^m_lambda, |lambda|=1"
            ),
            "beta_numerator_unit_circle_zeros": 0,
            "cancellation_criterion": (
                "all evaluation Frobenius modes disappear iff the completed "
                "P_Q(z/sqrt(q)) divides B(z) with multiplicity"
            ),
            "fixed_filter_no_go": (
                "if N_Q>deg(B), at least one unit-circle mode survives for every "
                "irreducible evaluation modulus Q of degree d"
            ),
            "degree_rows": degree_obstruction_panel(release_filter),
            "main_terms": main_term_formula(),
            "formal_periodic_control": periodic_control_panel(),
        },
        "all_curve_extension": {
            "scope": (
                "every fixed smooth projective geometrically connected curve, "
                "open U, exceptional P in U, and quadratic divisor character chi"
            ),
            "exact_identity_proved": True,
            "main_term_algorithm": (
                "factor the trivial inverse-zeta and inverse-L denominators on "
                "the normalized unit circle and add their exact principal parts"
            ),
            "possible_cross_channel_cancellation": True,
            "a1_clean_separation": (
                "the trivial deleted channel is analytic on |z|<sqrt(q), so it "
                "cannot cancel an evaluation Frobenius pole"
            ),
        },
        "scope_firewalls": {
            "complete_family_result": False,
            "genuine_incomplete_boolean_restriction": True,
            "owner_restriction_included": False,
            "all_curve_euler_identity": True,
            "a1_uniform_nonannihilation_for_large_conductor": True,
            "incomplete_waveprimcar_proved": False,
            "number_field_inference": False,
            "rh_proved": False,
            "grh_proved": False,
            "external_novelty_claim": False,
        },
        "resource_caps": {
            "field_sizes": list(REPLAY_FIELD_SIZES),
            "conductor_degrees": list(REPLAY_CONDUCTOR_DEGREES),
            "series_coefficient_cap": REPLAY_SERIES_CAP,
            "polynomials_enumerated": 0,
            "curves_enumerated": 0,
            "points_enumerated": 0,
            "l_functions_enumerated": 0,
            "floating_point_operations": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    if not args.check and not args.write_json:
        print(rendered, end="")


if __name__ == "__main__":
    main()
