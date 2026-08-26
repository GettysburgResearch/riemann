#!/usr/bin/env python3
"""Bounded exact replay for primitive-ray localization of the beta Gram form."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "756660350"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md"
    ): "105837343b6b8ef148488f492c66da8feae0334a",
    (
        "research/l-families/atlas/function_field/"
        "ffps_boundary_field_near_correlation_criterion.py"
    ): "53b5a710cb2f6b918958ff7e96801d81e2a0a79c",
    (
        "research/l-families/atlas/function_field/"
        "ffps_boundary_field_near_correlation_criterion.json"
    ): "efc21abe6b87d16d49b272d0fd0dd65e1f059d57",
    "tests/test_ffps_boundary_field_near_correlation_criterion.py": (
        "006e1c41f34f4d1e9a8885fb160c7d9886a3a77d"
    ),
    (
        "research/l-families/atlas/function_field/"
        "FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md"
    ): "bf4d1baa231086ba7e8eafaecd39730d83c9201a",
}
EXCEPTIONAL_PRIME = 67
EXCEPTIONAL_COEFFICIENTS = (1, -2, 1)
RAY_SAMPLES = (
    (1, 1, 100),
    (2, 1, 80),
    (3, 5, 500),
    (67, 1, 4_690),
    (1, 67, 4_690),
    (4_489, 1, 22_445),
    (1, 4_489, 22_445),
    (134, 3, 9_380),
    (3, 335, 23_450),
)
LOCAL_FACTOR_CAP = 256


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
    correction = mobius(value // EXCEPTIONAL_PRIME) if value % 67 == 0 else 0
    return mobius(value) - correction


def valuation(value: int, prime: int) -> tuple[int, int]:
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or value < 1
        or isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 2
    ):
        raise ValueError("invalid valuation input")
    exponent = 0
    remaining = value
    while remaining % prime == 0:
        remaining //= prime
        exponent += 1
    return exponent, remaining


def ray_parts(left: int, right: int) -> tuple[int, int, int, int]:
    if (
        isinstance(left, bool)
        or not isinstance(left, int)
        or left < 1
        or isinstance(right, bool)
        or not isinstance(right, int)
        or right < 1
        or math.gcd(left, right) != 1
    ):
        raise ValueError("ray coordinates must be coprime positive integers")
    alpha, left_free = valuation(left, EXCEPTIONAL_PRIME)
    gamma, right_free = valuation(right, EXCEPTIONAL_PRIME)
    if (
        min(alpha, gamma) != 0
        or max(alpha, gamma) > 2
        or mobius(left_free) == 0
        or mobius(right_free) == 0
    ):
        raise ValueError("ray is not beta-admissible")
    return alpha, gamma, left_free, right_free


def squarefree_coprime_harmonic(limit: int, modulus: int) -> Fraction:
    if (
        isinstance(limit, bool)
        or not isinstance(limit, int)
        or limit < 0
        or isinstance(modulus, bool)
        or not isinstance(modulus, int)
        or modulus < 1
    ):
        raise ValueError("invalid harmonic-sum input")
    return sum(
        (
            Fraction(1, value)
            for value in range(1, limit + 1)
            if mobius(value) != 0 and math.gcd(value, modulus) == 1
        ),
        Fraction(0),
    )


def scaled_ray_weight_direct(left: int, right: int, prefix: int) -> Fraction:
    """Return sqrt(left*right) times the source weight on one reduced ray."""
    ray_parts(left, right)
    if isinstance(prefix, bool) or not isinstance(prefix, int) or prefix < 1:
        raise ValueError("prefix must be a positive integer")
    height = max(left, right)
    return sum(
        (
            Fraction(beta(radial * left) * beta(radial * right), radial)
            for radial in range(1, prefix // height + 1)
        ),
        Fraction(0),
    )


def exceptional_radial_sum(alpha: int, gamma: int) -> Fraction:
    if (
        isinstance(alpha, bool)
        or not isinstance(alpha, int)
        or isinstance(gamma, bool)
        or not isinstance(gamma, int)
        or min(alpha, gamma) != 0
        or max(alpha, gamma) > 2
    ):
        raise ValueError("invalid exceptional exponents")
    return sum(
        (
            Fraction(
                EXCEPTIONAL_COEFFICIENTS[radial + alpha]
                * EXCEPTIONAL_COEFFICIENTS[radial + gamma],
                EXCEPTIONAL_PRIME**radial,
            )
            for radial in range(3 - max(alpha, gamma))
        ),
        Fraction(0),
    )


def scaled_ray_weight_formula(left: int, right: int, prefix: int) -> Fraction:
    """Evaluate the exact right side after multiplying out sqrt(left*right)."""
    alpha, gamma, left_free, right_free = ray_parts(left, right)
    if isinstance(prefix, bool) or not isinstance(prefix, int) or prefix < 1:
        raise ValueError("prefix must be a positive integer")
    height = max(left, right)
    modulus = EXCEPTIONAL_PRIME * left_free * right_free
    sign = mobius(left_free) * mobius(right_free)
    return sign * sum(
        (
            Fraction(
                EXCEPTIONAL_COEFFICIENTS[radial + alpha]
                * EXCEPTIONAL_COEFFICIENTS[radial + gamma],
                EXCEPTIONAL_PRIME**radial,
            )
            * squarefree_coprime_harmonic(
                prefix // (EXCEPTIONAL_PRIME**radial * height), modulus
            )
            for radial in range(3 - max(alpha, gamma))
        ),
        Fraction(0),
    )


def exceptional_residue_ratio() -> Fraction:
    prime = EXCEPTIONAL_PRIME
    return Fraction(prime**2 + 4 * prime + 1, prime**2) / Fraction(prime + 1, prime)


def ordinary_local_identity() -> dict[tuple[int, int], int]:
    """Check (1+xy)-(x+y)=(1-x)(1-y) coefficientwise."""
    radial_minus_incidence = {(0, 0): 1, (1, 0): -1, (0, 1): -1, (1, 1): 1}
    direct = {
        (left_degree, right_degree): (-1) ** (left_degree + right_degree)
        for left_degree in range(2)
        for right_degree in range(2)
    }
    if radial_minus_incidence != direct:
        raise ArithmeticError("ordinary radial/projector identity failed")
    return direct


def exceptional_local_identity() -> dict[tuple[int, int], int]:
    """Check all nine exceptional local states and their gcd labels."""
    direct = {
        (left_degree, right_degree): EXCEPTIONAL_COEFFICIENTS[left_degree]
        * EXCEPTIONAL_COEFFICIENTS[right_degree]
        for left_degree in range(3)
        for right_degree in range(3)
    }
    reconstructed: dict[tuple[int, int], int] = {}
    for left_degree in range(3):
        for right_degree in range(3):
            radial = min(left_degree, right_degree)
            alpha = left_degree - radial
            gamma = right_degree - radial
            reconstructed[(radial + alpha, radial + gamma)] = (
                EXCEPTIONAL_COEFFICIENTS[radial + alpha]
                * EXCEPTIONAL_COEFFICIENTS[radial + gamma]
            )
    if reconstructed != direct:
        raise ArithmeticError("exceptional radial/projector identity failed")
    return direct


def run(check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()

    local_failures = []
    for value in range(1, LOCAL_FACTOR_CAP + 1):
        exponent, free_part = valuation(value, EXCEPTIONAL_PRIME)
        expected = (
            EXCEPTIONAL_COEFFICIENTS[exponent] * mobius(free_part)
            if exponent <= 2
            else 0
        )
        if beta(value) != expected:
            local_failures.append(value)
    if local_failures:
        raise ArithmeticError("beta local source model failed")

    ray_rows = []
    for left, right, prefix in RAY_SAMPLES:
        direct = scaled_ray_weight_direct(left, right, prefix)
        formula = scaled_ray_weight_formula(left, right, prefix)
        if direct != formula:
            raise ArithmeticError(f"ray formula failed on {left}/{right}")
        alpha, gamma, left_free, right_free = ray_parts(left, right)
        ray_rows.append(
            {
                "alpha": alpha,
                "gamma": gamma,
                "left": left,
                "left_free": left_free,
                "prefix": prefix,
                "right": right,
                "right_free": right_free,
                "scaled_weight_match": True,
            }
        )

    radial_cases = {
        "0,0": exceptional_radial_sum(0, 0),
        "1,0": exceptional_radial_sum(1, 0),
        "0,1": exceptional_radial_sum(0, 1),
        "2,0": exceptional_radial_sum(2, 0),
        "0,2": exceptional_radial_sum(0, 2),
    }
    expected_radial = {
        "0,0": Fraction(1) + Fraction(4, 67) + Fraction(1, 67**2),
        "1,0": -Fraction(2) - Fraction(2, 67),
        "0,1": -Fraction(2) - Fraction(2, 67),
        "2,0": Fraction(1),
        "0,2": Fraction(1),
    }
    if radial_cases != expected_radial or any(
        value == 0 for value in radial_cases.values()
    ):
        raise ArithmeticError("exceptional radial sums changed")

    ordinary = ordinary_local_identity()
    exceptional = exceptional_local_identity()
    ratio = exceptional_residue_ratio()
    if ratio != Fraction(2379, 2278):
        raise ArithmeticError("exceptional residue correction changed")

    return {
        "fixed_ray_theorem": {
            "asymptotic": "Q_(a,b)(X)=A_(a,b)*log(X)+O_(a,b,R)(1)",
            "exceptional_radial_sums": {
                key: str(value) for key, value in radial_cases.items()
            },
            "formula": (
                "sqrt(ab)*Q_(a,b)(X)/R(log(a/b))="
                "mu(a0)mu(b0)*sum_r c_(r+alpha)c_(r+gamma)67^-r"
                "*W_(67a0b0)(X/(67^r max(a,b)))"
            ),
            "harmonic_density": ("C(q)=zeta(2)^-1*product_(p|q)(1+1/p)^-1"),
            "ray_replays": ray_rows,
        },
        "localization": {
            "height": "h(m,n)=max(m/gcd(m,n),n/gcd(m,n))",
            "low_height_bound": "|Q_<=H(X)| <= 16||R||_infty H(X)(1+log X)",
            "quantifier": "every prescribed H(X)>=1 with H(X)=X^o(1)",
            "residual_geometry": (
                "both reduced coordinates > H(X)/16 and gcd(m,n) < X/H(X)"
            ),
            "rh_equivalence": "RH iff |Q_>H(X)(X)|=X^o(1)",
            "residual_estimate_proved": False,
            "rh_proved": False,
        },
        "radial_projector": {
            "domain": "separated Euler products converge absolutely only for Re(s)>1",
            "exceptional_local_cells": len(exceptional),
            "exceptional_residue_ratio": str(ratio),
            "ordinary_local_cells": len(ordinary),
            "radial_factor": (
                "zeta(2sigma)/zeta(4sigma)"
                "*(1+4*67^(-2sigma)+67^(-4sigma))/(1+67^(-2sigma))"
            ),
            "critical_line_convergence_claimed": False,
        },
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported_theorem": (
                "RH iff the signed off-diagonal compact-ratio beta Gram form is X^o(1)"
            ),
        },
        "resource_caps": {
            "largest_direct_radial_loop": max(
                prefix // max(left, right) for left, right, prefix in RAY_SAMPLES
            ),
            "local_beta_coefficients": LOCAL_FACTOR_CAP,
            "ray_samples": len(RAY_SAMPLES),
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
