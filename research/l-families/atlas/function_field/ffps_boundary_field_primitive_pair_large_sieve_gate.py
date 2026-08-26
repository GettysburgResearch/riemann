#!/usr/bin/env python3
"""Bounded replay for the primitive-pair large-sieve decomposition."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "2582feec6"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md"
    ): "4ab7c602991b0dc319e72d3c805e202b2302b46e",
    (
        "research/l-families/atlas/function_field/"
        "ffps_boundary_field_primitive_ray_localization.py"
    ): "c16cc534afce645412d2cfd5d93a2b6a34d92860",
    (
        "research/l-families/atlas/function_field/"
        "ffps_boundary_field_primitive_ray_localization.json"
    ): "66773e4d9a0ea243191c28d71e66c7f2b8bac8f9",
    "tests/test_ffps_boundary_field_primitive_ray_localization.py": (
        "7bc9ff4f6d5ea056a7ee9dca55419fafde466275"
    ),
}
EXCEPTIONAL_PRIME = 67
EXCEPTIONAL_COEFFICIENTS = (1, -2, 1)
CHANNELS = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2))
INDEPENDENT_CHANNELS = ((0, 0), (1, 0), (2, 0))
TOY_PREFIX = 96
RECIPROCITY_ROWS = (
    (1, 0, 1, 64, 128),
    (2, 0, 1, 4_096, 8_192),
)
GRAM_ROWS = (
    (0, 0, 1, 8, 16),
    (1, 0, 1, 64, 96),
)
BOOLEAN_ROW = (0, 0, 30, 8, 16)


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def mobius(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    parity = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            parity += 1
            if remaining % prime == 0:
                return 0
        prime += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    correction = (
        mobius(value // EXCEPTIONAL_PRIME) if value % EXCEPTIONAL_PRIME == 0 else 0
    )
    return mobius(value) - correction


def toy_correlation(left: int, right: int) -> Fraction:
    if (
        isinstance(left, bool)
        or not isinstance(left, int)
        or left < 1
        or isinstance(right, bool)
        or not isinstance(right, int)
        or right < 1
    ):
        raise ValueError("invalid correlation coordinates")
    if max(left, right) > 16 * min(left, right):
        return Fraction(0)
    return Fraction(min(left, right), max(left, right))


def square_decomposition(value: int) -> tuple[int, int]:
    """Return square_part, squarefree_part with value=square_part^2*part."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    square_part = 1
    squarefree_part = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        square_part *= prime ** (exponent // 2)
        if exponent % 2:
            squarefree_part *= prime
        prime += 1
    if remaining > 1:
        squarefree_part *= remaining
    return square_part, squarefree_part


RadicalForm = dict[int, Fraction]


def add_radical_term(form: RadicalForm, under_root: int, coefficient: Fraction) -> None:
    square_part, squarefree_part = square_decomposition(under_root)
    form[squarefree_part] = form.get(squarefree_part, Fraction(0)) + (
        coefficient / square_part
    )
    if form[squarefree_part] == 0:
        del form[squarefree_part]


def add_forms(left: RadicalForm, right: RadicalForm) -> RadicalForm:
    result = dict(left)
    for radicand, coefficient in right.items():
        result[radicand] = result.get(radicand, Fraction(0)) + coefficient
        if result[radicand] == 0:
            del result[radicand]
    return result


def scale_form(form: RadicalForm, scalar: Fraction) -> RadicalForm:
    return {
        radicand: scalar * coefficient
        for radicand, coefficient in form.items()
        if scalar * coefficient
    }


def subtract_forms(left: RadicalForm, right: RadicalForm) -> RadicalForm:
    return add_forms(left, scale_form(right, Fraction(-1)))


def multiply_forms(left: RadicalForm, right: RadicalForm) -> RadicalForm:
    result: RadicalForm = {}
    for left_radicand, left_coefficient in left.items():
        for right_radicand, right_coefficient in right.items():
            add_radical_term(
                result,
                left_radicand * right_radicand,
                left_coefficient * right_coefficient,
            )
    return result


def prime_factors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    factors = []
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            factors.append(prime)
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def divisors(value: int) -> tuple[int, ...]:
    result = [1]
    for prime in prime_factors(value):
        result += [prime * divisor for divisor in result]
    return tuple(sorted(result))


def direct_shell(prefix: int, height: int) -> RadicalForm:
    if (
        isinstance(prefix, bool)
        or not isinstance(prefix, int)
        or prefix < 2
        or isinstance(height, bool)
        or not isinstance(height, int)
        or height < 1
    ):
        raise ValueError("invalid direct-shell input")
    form: RadicalForm = {}
    for left in range(1, prefix + 1):
        left_beta = beta(left)
        if left_beta == 0:
            continue
        for right in range(1, prefix + 1):
            right_beta = beta(right)
            if right_beta == 0 or left == right:
                continue
            common = math.gcd(left, right)
            reduced_left = left // common
            reduced_right = right // common
            primitive_height = max(reduced_left, reduced_right)
            if not height < primitive_height <= 2 * height:
                continue
            correlation = toy_correlation(reduced_left, reduced_right)
            if correlation == 0:
                continue
            add_radical_term(
                form,
                reduced_left * reduced_right,
                Fraction(left_beta * right_beta, common) * correlation,
            )
    return form


def formula_shell(prefix: int, height: int) -> RadicalForm:
    if (
        isinstance(prefix, bool)
        or not isinstance(prefix, int)
        or prefix < 2
        or isinstance(height, bool)
        or not isinstance(height, int)
        or height < 1
    ):
        raise ValueError("invalid formula-shell input")
    form: RadicalForm = {}
    for alpha, gamma in CHANNELS:
        left_scale = EXCEPTIONAL_PRIME**alpha
        right_scale = EXCEPTIONAL_PRIME**gamma
        for radial in range(3 - max(alpha, gamma)):
            common_scale = EXCEPTIONAL_PRIME**radial
            exceptional_weight = (
                EXCEPTIONAL_COEFFICIENTS[radial + alpha]
                * EXCEPTIONAL_COEFFICIENTS[radial + gamma]
            )
            radial_limit = prefix // (common_scale * height)
            for common_free in range(1, radial_limit + 1):
                if mobius(common_free) == 0 or common_free % EXCEPTIONAL_PRIME == 0:
                    continue
                upper = min(2 * height, prefix // (common_scale * common_free))
                for left_free in range(1, upper // left_scale + 1):
                    left_mu = mobius(left_free)
                    if (
                        left_mu == 0
                        or left_free % EXCEPTIONAL_PRIME == 0
                        or math.gcd(left_free, common_free) != 1
                    ):
                        continue
                    physical_left = left_scale * left_free
                    for right_free in range(1, upper // right_scale + 1):
                        right_mu = mobius(right_free)
                        if (
                            right_mu == 0
                            or right_free % EXCEPTIONAL_PRIME == 0
                            or math.gcd(right_free, common_free) != 1
                            or math.gcd(left_free, right_free) != 1
                        ):
                            continue
                        physical_right = right_scale * right_free
                        primitive_height = max(physical_left, physical_right)
                        if not height < primitive_height <= upper:
                            continue
                        correlation = toy_correlation(physical_left, physical_right)
                        if correlation == 0:
                            continue
                        add_radical_term(
                            form,
                            (EXCEPTIONAL_PRIME ** (alpha + gamma))
                            * left_free
                            * right_free,
                            Fraction(
                                exceptional_weight * left_mu * right_mu,
                                common_scale * common_free,
                            )
                            * correlation,
                        )
    return form


def direct_off_diagonal(prefix: int) -> RadicalForm:
    if isinstance(prefix, bool) or not isinstance(prefix, int) or prefix < 2:
        raise ValueError("prefix must be an integer at least two")
    form: RadicalForm = {}
    for left in range(1, prefix + 1):
        left_beta = beta(left)
        if left_beta == 0:
            continue
        for right in range(1, prefix + 1):
            right_beta = beta(right)
            if right_beta == 0 or left == right:
                continue
            common = math.gcd(left, right)
            reduced_left = left // common
            reduced_right = right // common
            correlation = toy_correlation(reduced_left, reduced_right)
            if correlation == 0:
                continue
            add_radical_term(
                form,
                reduced_left * reduced_right,
                Fraction(left_beta * right_beta, common) * correlation,
            )
    return form


def panel_form(
    alpha: int, gamma: int, sieve: int, height: int, upper: int
) -> RadicalForm:
    if (
        (alpha, gamma) not in CHANNELS
        or isinstance(sieve, bool)
        or not isinstance(sieve, int)
        or sieve < 1
        or mobius(sieve) == 0
        or sieve % EXCEPTIONAL_PRIME == 0
        or isinstance(height, bool)
        or not isinstance(height, int)
        or height < 1
        or isinstance(upper, bool)
        or not isinstance(upper, int)
        or not height <= upper <= 2 * height
    ):
        raise ValueError("invalid panel input")
    left_scale = EXCEPTIONAL_PRIME**alpha
    right_scale = EXCEPTIONAL_PRIME**gamma
    form: RadicalForm = {}
    for left in range(1, upper // left_scale + 1):
        left_mu = mobius(left)
        if left_mu == 0 or left % EXCEPTIONAL_PRIME == 0 or math.gcd(left, sieve) != 1:
            continue
        physical_left = left_scale * left
        for right in range(1, upper // right_scale + 1):
            right_mu = mobius(right)
            if (
                right_mu == 0
                or right % EXCEPTIONAL_PRIME == 0
                or math.gcd(right, sieve) != 1
                or math.gcd(left, right) != 1
            ):
                continue
            physical_right = right_scale * right
            primitive_height = max(physical_left, physical_right)
            if not height < primitive_height <= upper:
                continue
            correlation = toy_correlation(physical_left, physical_right)
            if correlation == 0:
                continue
            add_radical_term(
                form,
                left * right,
                Fraction(left_mu * right_mu) * correlation,
            )
    return form


def primitive_rectangle(alpha: int, gamma: int, sieve: int, upper: int) -> RadicalForm:
    if (
        (alpha, gamma) not in CHANNELS
        or isinstance(sieve, bool)
        or not isinstance(sieve, int)
        or sieve < 1
        or mobius(sieve) == 0
        or sieve % EXCEPTIONAL_PRIME == 0
        or isinstance(upper, bool)
        or not isinstance(upper, int)
        or upper < 0
    ):
        raise ValueError("invalid primitive-rectangle input")
    left_scale = EXCEPTIONAL_PRIME**alpha
    right_scale = EXCEPTIONAL_PRIME**gamma
    form: RadicalForm = {}
    for left in range(1, upper // left_scale + 1):
        left_mu = mobius(left)
        if left_mu == 0 or math.gcd(left, EXCEPTIONAL_PRIME * sieve) != 1:
            continue
        physical_left = left_scale * left
        for right in range(1, upper // right_scale + 1):
            right_mu = mobius(right)
            if (
                right_mu == 0
                or math.gcd(right, EXCEPTIONAL_PRIME * sieve) != 1
                or math.gcd(left, right) != 1
            ):
                continue
            physical_right = right_scale * right
            correlation = toy_correlation(physical_left, physical_right)
            if correlation == 0:
                continue
            add_radical_term(
                form,
                left * right,
                Fraction(left_mu * right_mu) * correlation,
            )
    return form


def mobius_lifted_rectangle(
    alpha: int, gamma: int, sieve: int, upper: int
) -> RadicalForm:
    if (
        (alpha, gamma) not in CHANNELS
        or isinstance(sieve, bool)
        or not isinstance(sieve, int)
        or sieve < 1
        or mobius(sieve) == 0
        or sieve % EXCEPTIONAL_PRIME == 0
        or isinstance(upper, bool)
        or not isinstance(upper, int)
        or upper < 0
    ):
        raise ValueError("invalid lifted-rectangle input")
    left_scale = EXCEPTIONAL_PRIME**alpha
    right_scale = EXCEPTIONAL_PRIME**gamma
    common_limit = upper // max(left_scale, right_scale)
    form: RadicalForm = {}
    for common in range(1, common_limit + 1):
        common_mu = mobius(common)
        if common_mu == 0 or math.gcd(common, EXCEPTIONAL_PRIME * sieve) != 1:
            continue
        local_sieve = EXCEPTIONAL_PRIME * sieve * common
        for left in range(1, upper // (left_scale * common) + 1):
            left_mu = mobius(left)
            if left_mu == 0 or math.gcd(left, local_sieve) != 1:
                continue
            physical_left = left_scale * left
            for right in range(1, upper // (right_scale * common) + 1):
                right_mu = mobius(right)
                if right_mu == 0 or math.gcd(right, local_sieve) != 1:
                    continue
                physical_right = right_scale * right
                correlation = toy_correlation(physical_left, physical_right)
                if correlation == 0:
                    continue
                add_radical_term(
                    form,
                    left * right,
                    Fraction(common_mu * left_mu * right_mu, common) * correlation,
                )
    return form


def incidence_strata(
    alpha: int, gamma: int, modulus: int, height: int, upper: int
) -> dict[int, RadicalForm]:
    if (
        (alpha, gamma) not in CHANNELS
        or isinstance(modulus, bool)
        or not isinstance(modulus, int)
        or modulus < 1
        or mobius(modulus) == 0
        or modulus % EXCEPTIONAL_PRIME == 0
        or isinstance(height, bool)
        or not isinstance(height, int)
        or height < 1
        or isinstance(upper, bool)
        or not isinstance(upper, int)
        or not height <= upper <= 2 * height
    ):
        raise ValueError("invalid incidence-strata input")
    strata = {divisor: {} for divisor in divisors(modulus)}
    left_scale = EXCEPTIONAL_PRIME**alpha
    right_scale = EXCEPTIONAL_PRIME**gamma
    for left in range(1, upper // left_scale + 1):
        left_mu = mobius(left)
        if left_mu == 0 or left % EXCEPTIONAL_PRIME == 0:
            continue
        physical_left = left_scale * left
        for right in range(1, upper // right_scale + 1):
            right_mu = mobius(right)
            if (
                right_mu == 0
                or right % EXCEPTIONAL_PRIME == 0
                or math.gcd(left, right) != 1
            ):
                continue
            physical_right = right_scale * right
            primitive_height = max(physical_left, physical_right)
            if not height < primitive_height <= upper:
                continue
            correlation = toy_correlation(physical_left, physical_right)
            if correlation == 0:
                continue
            incidence = math.gcd(left * right, modulus)
            add_radical_term(
                strata[incidence],
                left * right,
                Fraction(left_mu * right_mu) * correlation,
            )
    return strata


def sieve_from_strata(strata: dict[int, RadicalForm], sieve: int) -> RadicalForm:
    if isinstance(sieve, bool) or not isinstance(sieve, int) or sieve < 1:
        raise ValueError("sieve must be a positive integer")
    result: RadicalForm = {}
    for incidence, form in strata.items():
        if math.gcd(incidence, sieve) == 1:
            result = add_forms(result, form)
    return result


def boolean_parseval_certificate(
    alpha: int, gamma: int, modulus: int, height: int, upper: int
) -> dict[str, object]:
    strata = incidence_strata(alpha, gamma, modulus, height, upper)
    modulus_divisors = divisors(modulus)
    panel_rows = {sieve: sieve_from_strata(strata, sieve) for sieve in modulus_divisors}
    for sieve, form in panel_rows.items():
        if form != panel_form(alpha, gamma, sieve, height, upper):
            raise ArithmeticError("incidence disjointness transform failed")

    inversion_rows: dict[int, RadicalForm] = {}
    for incidence in modulus_divisors:
        recovered: RadicalForm = {}
        for inner in divisors(incidence):
            recovered = add_forms(
                recovered,
                scale_form(
                    panel_rows[(modulus // incidence) * inner],
                    Fraction((-1) ** len(prime_factors(inner))),
                ),
            )
        if recovered != strata[incidence]:
            raise ArithmeticError("incidence transform inversion failed")
        inversion_rows[incidence] = recovered

    normalizer = sum((Fraction(1, sieve) for sieve in modulus_divisors), Fraction(0))
    left_energy: RadicalForm = {}
    for sieve, form in panel_rows.items():
        left_energy = add_forms(
            left_energy,
            scale_form(multiply_forms(form, form), Fraction(1, sieve) / normalizer),
        )

    right_energy: RadicalForm = {}
    zero_frequency: RadicalForm = {}
    for frequency in modulus_divisors:
        frequency_primes = prime_factors(frequency)
        frequency_weight = Fraction((-1) ** len(frequency_primes))
        frequency_norm = Fraction(1)
        for prime in frequency_primes:
            frequency_weight *= Fraction(prime, (prime + 1) ** 2)
            frequency_norm *= Fraction(prime, (prime + 1) ** 2)
        coefficient: RadicalForm = {}
        for incidence, form in strata.items():
            if incidence % frequency:
                continue
            tail_weight = Fraction(1)
            for prime in prime_factors(incidence // frequency):
                tail_weight *= Fraction(prime, prime + 1)
            coefficient = add_forms(
                coefficient, scale_form(form, frequency_weight * tail_weight)
            )
        if frequency == 1:
            zero_frequency = coefficient
        right_energy = add_forms(
            right_energy,
            scale_form(
                multiply_forms(coefficient, coefficient), Fraction(1, frequency_norm)
            ),
        )
    if left_energy != right_energy:
        raise ArithmeticError("harmonic Boolean Parseval identity failed")

    return {
        "energy_digest": radical_digest(left_energy),
        "incidence_digests": {
            str(incidence): radical_digest(strata[incidence])
            for incidence in modulus_divisors
        },
        "inversion_match": all(
            inversion_rows[incidence] == strata[incidence]
            for incidence in modulus_divisors
        ),
        "parseval_match": True,
        "sieve_digests": {
            str(sieve): radical_digest(panel_rows[sieve]) for sieve in modulus_divisors
        },
        "zero_frequency_digest": radical_digest(zero_frequency),
    }


def radical_digest(form: RadicalForm) -> str:
    payload = "|".join(
        f"{radicand}:{coefficient.numerator}/{coefficient.denominator}"
        for radicand, coefficient in sorted(form.items())
    )
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    shell_rows = []
    reconstructed: RadicalForm = {}
    height = 1
    while height < TOY_PREFIX:
        direct = direct_shell(TOY_PREFIX, height)
        formula = formula_shell(TOY_PREFIX, height)
        if direct != formula:
            raise ArithmeticError(f"common-factor swap failed at height {height}")
        reconstructed = add_forms(reconstructed, formula)
        shell_rows.append(
            {
                "basis_terms": len(direct),
                "digest": radical_digest(direct),
                "height": height,
                "match": True,
            }
        )
        height *= 2

    complete = direct_off_diagonal(TOY_PREFIX)
    if reconstructed != complete:
        raise ArithmeticError("dyadic shell reconstruction failed")

    reciprocity_rows = []
    for alpha, gamma, sieve, height, upper in RECIPROCITY_ROWS:
        forward = panel_form(alpha, gamma, sieve, height, upper)
        reverse = panel_form(gamma, alpha, sieve, height, upper)
        if forward != reverse:
            raise ArithmeticError(f"channel reciprocity failed for {alpha},{gamma}")
        reciprocity_rows.append(
            {
                "basis_terms": len(forward),
                "forward": [alpha, gamma],
                "height": height,
                "match": True,
                "reverse": [gamma, alpha],
                "sieve": sieve,
                "upper": upper,
            }
        )

    gram_rows = []
    for alpha, gamma, sieve, height, upper in GRAM_ROWS:
        primitive_upper = primitive_rectangle(alpha, gamma, sieve, upper)
        lifted_upper = mobius_lifted_rectangle(alpha, gamma, sieve, upper)
        primitive_lower = primitive_rectangle(alpha, gamma, sieve, height)
        lifted_lower = mobius_lifted_rectangle(alpha, gamma, sieve, height)
        shell = subtract_forms(primitive_upper, primitive_lower)
        if primitive_upper != lifted_upper or primitive_lower != lifted_lower:
            raise ArithmeticError("Möbius-lifted rectangle identity failed")
        if shell != panel_form(alpha, gamma, sieve, height, upper):
            raise ArithmeticError("rectangle-increment identity failed")
        gram_rows.append(
            {
                "channel": [alpha, gamma],
                "height": height,
                "lifted_match": True,
                "shell_digest": radical_digest(shell),
                "sieve": sieve,
                "upper": upper,
            }
        )

    boolean_alpha, boolean_gamma, modulus, boolean_height, boolean_upper = BOOLEAN_ROW
    boolean_certificate = boolean_parseval_certificate(
        boolean_alpha,
        boolean_gamma,
        modulus,
        boolean_height,
        boolean_upper,
    )
    frozen_prime = 19
    if frozen_prime <= boolean_upper:
        raise ArithmeticError("frozen-prime replay row is not beyond the panel")
    if panel_form(
        boolean_alpha,
        boolean_gamma,
        frozen_prime,
        boolean_height,
        boolean_upper,
    ) != panel_form(
        boolean_alpha,
        boolean_gamma,
        1,
        boolean_height,
        boolean_upper,
    ):
        raise ArithmeticError("large-prime sieve coordinate was not frozen")

    return {
        "conditional_gate": {
            "name": "PRIMLS",
            "estimate": (
                "sum_(d<=D,sf,67-free) d^-1 "
                "sup_(H<=U<=2H)|P_(alpha,gamma)(d;H,U)|^2 "
                "<<_epsilon (2DH)^epsilon"
            ),
            "channels_required": [list(row) for row in INDEPENDENT_CHANNELS],
            "estimate_proved": False,
            "conditional_implication_to_rh_proved": True,
            "rh_implies_gate_claimed": False,
            "rh_proved": False,
        },
        "decomposition": {
            "channels": [list(row) for row in CHANNELS],
            "common_factor_identity": (
                "S_H(X)=sum_(alpha,gamma,r) kappa * sum_d d^-1 "
                "P_(alpha,gamma)(d;H,min(2H,X/(67^r d)))"
            ),
            "dyadic_reconstruction": "O(X)=sum_(0<=j<ceil(log2 X)) S_(2^j)(X)",
            "exceptional_coefficients": list(EXCEPTIONAL_COEFFICIENTS),
            "identity_proved": True,
            "reciprocity": "P_10=P_01 and P_20=P_02",
            "reciprocity_rows": reciprocity_rows,
        },
        "exact_normal_forms": {
            "boolean_sieve": {
                "channel": [boolean_alpha, boolean_gamma],
                "frozen_prime": frozen_prime,
                "height": boolean_height,
                "harmonic_parseval": (
                    "Z_Q^-1 sum_(d|Q) d^-1 |P(d)|^2 =sum_(S|Q)|b_S|^2/N_S"
                ),
                "modulus": modulus,
                "replay": boolean_certificate,
                "upper": boolean_upper,
                "zero_frequency_obstruction": (
                    "the harmonic mean b_1 survives Parseval; sieve averaging "
                    "alone cannot force cancellation"
                ),
            },
            "mobius_gram": {
                "identity": (
                    "P_(alpha,gamma)(d;H,U)=G_(alpha,gamma)(d;U)"
                    "-G_(alpha,gamma)(d;H), with G a signed k^-1 "
                    "Mobius sum of one-dimensional Gram inner products"
                ),
                "rows": gram_rows,
            },
        },
        "finite_exact_replay": {
            "complete_basis_terms": len(complete),
            "complete_digest": radical_digest(complete),
            "dyadic_match": True,
            "prefix": TOY_PREFIX,
            "shells": shell_rows,
            "toy_correlation": (
                "min(a,b)/max(a,b) on the closed ratio-sixteen band, zero outside"
            ),
        },
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported_theorem": (
                "exact primitive-ray formula and RH localization to "
                "subpower-complement primitive height"
            ),
        },
        "resource_caps": {
            "boolean_modulus": modulus,
            "direct_pair_cells": TOY_PREFIX**2,
            "largest_reciprocity_upper": max(row[4] for row in RECIPROCITY_ROWS),
            "zeta_zeros": 0,
            "finite_fields": 0,
            "curves": 0,
            "conductor_families": 0,
            "l_functions": 0,
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
    print(rendered, end="")


if __name__ == "__main__":
    main()
