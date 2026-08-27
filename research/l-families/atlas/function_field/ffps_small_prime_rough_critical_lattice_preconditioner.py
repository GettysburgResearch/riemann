#!/usr/bin/env python3
"""Bounded exact replay for small-prime rough critical-lattice conditioning."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "8192514ed68f50b8e2a9cff9e1bedab2478bb5c1"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/FFPS_DUPLICATE67_CRITICAL_SCALE_FILTER_FIREWALL.md": (
        "3a66ff2c438945ba3c25193fa6c36734e59bc09f"
    ),
    "research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.py": (
        "4a67f44518dad3116aed2b23716cbfbeccea131d"
    ),
    "research/l-families/atlas/function_field/ffps_duplicate67_critical_scale_filter_firewall.json": (
        "60d20a60b378fc22632195a4c9f1c6d6eff916dc"
    ),
    "tests/test_ffps_duplicate67_critical_scale_filter_firewall.py": (
        "b63c96d25d5c4829ed6854785464c528959d885b"
    ),
    "research/l-families/atlas/function_field/FFPS_CRITICAL_BETA_FOURIER_LATTICE_COMPRESSION.md": (
        "2334c471d37456acd974765d15c21122f65d01b1"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_fourier_lattice_compression.py": (
        "ad0fe111e1cd4be4a56f0da8171fe5cc6cec4d14"
    ),
    "research/l-families/atlas/function_field/ffps_critical_beta_fourier_lattice_compression.json": (
        "9cc5d8cf91a00fb18a5a416c0c1a4c8963ff4986"
    ),
    "tests/test_ffps_critical_beta_fourier_lattice_compression.py": (
        "3c71d664649a9cfd3f5840f5ccfa0b6487bb7b67"
    ),
}

EXCEPTIONAL_PRIME = 67
TOY_PRIMES = (2, 3, 5, 7)
COEFFICIENT_CAP = 420
PREFIX_CAP = 96


def check_source_contract() -> None:
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
            raise RuntimeError(f"source blob mismatch: {path}")


def validate_positive_integer(value: int, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")


def primes_up_to(limit: int) -> tuple[int, ...]:
    validate_positive_integer(limit, "limit")
    if limit < 2:
        return ()
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                sieve[multiple] = False
    return tuple(index for index, is_prime in enumerate(sieve) if is_prime)


def mobius(value: int) -> int:
    validate_positive_integer(value, "value")
    remaining = value
    parity = 0
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            remaining //= candidate
            parity += 1
            if remaining % candidate == 0:
                return 0
        candidate += 1
    if remaining > 1:
        parity += 1
    return -1 if parity % 2 else 1


def beta(value: int, prime: int = EXCEPTIONAL_PRIME) -> int:
    validate_positive_integer(value, "value")
    validate_positive_integer(prime, "prime")
    return mobius(value) - (mobius(value // prime) if value % prime == 0 else 0)


def is_smooth(value: int, primes: tuple[int, ...]) -> bool:
    validate_positive_integer(value, "value")
    remaining = value
    for prime in primes:
        while remaining % prime == 0:
            remaining //= prime
    return remaining == 1


def rough_mobius(value: int, primes: tuple[int, ...]) -> int:
    validate_positive_integer(value, "value")
    if any(value % prime == 0 for prime in primes):
        return 0
    return mobius(value)


def divisors(value: int) -> tuple[int, ...]:
    validate_positive_integer(value, "value")
    return tuple(divisor for divisor in range(1, value + 1) if value % divisor == 0)


def forward_coefficient(value: int, primes: tuple[int, ...]) -> int:
    return sum(
        mobius(divisor) * rough_mobius(value // divisor, primes)
        for divisor in divisors(value)
        if is_smooth(divisor, primes)
    )


def inverse_coefficient(value: int, primes: tuple[int, ...]) -> int:
    return sum(
        mobius(value // divisor)
        for divisor in divisors(value)
        if is_smooth(divisor, primes)
    )


def coefficient_panel() -> dict[str, object]:
    rows: list[tuple[int, int, int]] = []
    rough_nonzero = 0
    for value in range(1, COEFFICIENT_CAP + 1):
        ordinary = mobius(value)
        rough = rough_mobius(value, TOY_PRIMES)
        if forward_coefficient(value, TOY_PRIMES) != ordinary:
            raise ArithmeticError("forward rough-source coefficient identity changed")
        if inverse_coefficient(value, TOY_PRIMES) != rough:
            raise ArithmeticError("terminating smooth inverse identity changed")
        rough_nonzero += int(rough != 0)
        rows.append((value, ordinary, rough))
    digest = hashlib.sha256(
        json.dumps(rows, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "primes": list(TOY_PRIMES),
        "coefficient_cap": COEFFICIENT_CAP,
        "rough_nonzero": rough_nonzero,
        "sha256": digest,
        "forward_identity": "mu=(product over p<=y of (1-delta_p))*mu_y_rough",
        "inverse_identity": "mu_y_rough=(sum over y-smooth d) mu(n/d)",
    }


def scale_filter(
    values: tuple[Fraction, ...], prime: int, omega: Fraction
) -> tuple[Fraction, ...]:
    if len(values) < 2 or values[0] != 0:
        raise ValueError("prefix values must be nonempty after a zero sentinel")
    validate_positive_integer(prime, "prime")
    return tuple(
        Fraction(0) if height == 0 else values[height] - omega * values[height // prime]
        for height in range(len(values))
    )


def inverse_scale_filter(
    values: tuple[Fraction, ...], prime: int, omega: Fraction
) -> tuple[Fraction, ...]:
    if len(values) < 2 or values[0] != 0:
        raise ValueError("prefix values must be nonempty after a zero sentinel")
    validate_positive_integer(prime, "prime")
    reconstructed = [Fraction(0)]
    for height in range(1, len(values)):
        subtotal = Fraction(0)
        reduced = height
        power = Fraction(1)
        while reduced >= 1:
            subtotal += power * values[reduced]
            reduced //= prime
            power *= omega
        reconstructed.append(subtotal)
    return tuple(reconstructed)


def apply_filters(
    values: tuple[Fraction, ...],
    ordered_primes: tuple[int, ...],
    omegas: dict[int, Fraction],
) -> tuple[Fraction, ...]:
    result = values
    for prime in ordered_primes:
        result = scale_filter(result, prime, omegas[prime])
    return result


def apply_inverse_filters(
    values: tuple[Fraction, ...],
    ordered_primes: tuple[int, ...],
    omegas: dict[int, Fraction],
) -> tuple[Fraction, ...]:
    result = values
    for prime in ordered_primes:
        result = inverse_scale_filter(result, prime, omegas[prime])
    return result


def commuting_scale_panel() -> dict[str, object]:
    values = (Fraction(0),) + tuple(
        Fraction(((-1) ** height) * (height + 2), height + 1)
        for height in range(1, PREFIX_CAP + 1)
    )
    omegas = {prime: Fraction(1, prime + 1) for prime in TOY_PRIMES}
    forward = apply_filters(values, TOY_PRIMES, omegas)
    reverse = apply_filters(values, tuple(reversed(TOY_PRIMES)), omegas)
    if forward != reverse:
        raise ArithmeticError("commuting prefix-scale filters changed")
    reconstructed = apply_inverse_filters(forward, tuple(reversed(TOY_PRIMES)), omegas)
    if reconstructed != values:
        raise ArithmeticError("terminating prefix-scale inverse changed")
    return {
        "prefix_cap": PREFIX_CAP,
        "toy_omegas": {str(prime): str(omegas[prime]) for prime in TOY_PRIMES},
        "commuting_orders_agree": True,
        "terminating_inverse_reconstructs": True,
        "operator": "T_p=I-omega_p*S_p, (S_p F)_X=F_(X/p)",
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "imported": (
                "critical retained beta lattice RH criterion and duplicate-67 "
                "maximal positive-measure scale isomorphism"
            ),
        },
        "exact_operator": {
            "rough_prefix": ("A_(y,X)(t)=sum_(n<=X, gcd(n,P(y))=1) mu(n)*n^(-1/2-it)"),
            "ordinary_factorization": ("M=product_(p<=y)(I-omega_p*S_p) A_y"),
            "beta_factorization": (
                "D=(I-omega_67*S_67)*product_(p<=y)(I-omega_p*S_p) A_y"
            ),
            "commuting": True,
            "single_inverse": (
                "(I-omega_p*S_p)^(-1)=sum_(j>=0)omega_p^j*S_p^j, "
                "terminating at every prefix"
            ),
            "product_inverse": ("A_(y,X)=sum_(d<=X, d y-smooth)d^(-1/2-it)M_(X/d)"),
            "beta_inverse": (
                "A_(y,X)=sum_(j>=0)omega_67^j sum_(d y-smooth)d^(-1/2-it)D_(X/(67^j*d))"
            ),
        },
        "maximal_conditioning": {
            "measure_scope": "every positive Fourier measure nu",
            "forward_cost": "C_+(y)=product_(p<=y)(1+p^(-1/2))",
            "inverse_cost": "C_-(y)=product_(p<=y)(1-p^(-1/2))^(-1)",
            "mobius_bounds": "C_-(y)^(-1) A_nu<=M_nu<=C_+(y) A_nu",
            "beta_bounds": (
                "(1-67^(-1/2))*C_-(y)^(-1) A_nu<=D_nu<=(1+67^(-1/2))*C_+(y) A_nu"
            ),
            "condition_number": "C_+(y)*C_-(y)",
        },
        "pnt_import": {
            "status": "CLASSICAL EXTERNAL INPUT, NOT REPROVED BY THE REPLAY",
            "statement": ("sum_(p<=y)p^(-1/2)=(2+o(1))*sqrt(y)/log(y)"),
            "derivation": "prime number theorem plus partial summation",
            "quadratic_error": "sum_(p<=y)1/p=O(log log y)",
            "consequences": {
                "log_C_plus": "(2+o(1))*sqrt(y)/log(y)",
                "log_C_minus": "(2+o(1))*sqrt(y)/log(y)",
                "log_condition_number": "(4+o(1))*sqrt(y)/log(y)",
            },
        },
        "absolute_neumann_frontier": {
            "subpower_scale": ("y=(log X)^2*(log log X)^(2-delta), fixed delta>0"),
            "subpower_cost": (
                "log C_+(y), log C_-(y)=(1+o(1))*log(X)/(log log X)^(delta/2)=o(log X)"
            ),
            "critical_scale": ("y=c*(log X)^2*(log log X)^2, fixed c>0"),
            "critical_cost": (
                "C_+(y)=C_-(y)=X^(sqrt(c)+o(1)); C_+(y)C_-(y)=X^(2*sqrt(c)+o(1))"
            ),
            "critical_energy_one_way_cost": "X^(2*sqrt(c)+o(1)) after squaring",
        },
        "moving_y_lattice_equivalence": {
            "retained_measure": (
                "lambda_X=(1/L_X)*sum_(|k|<=K_*)|Bhat(t_k)|^2*delta_(t_k)"
            ),
            "maximal_rough_target": (
                "sup_(1<=Y<=X)||A_(y(X),Y)||_(L2(lambda_X))^2=X^o(1)"
            ),
            "general_cost_condition": ("sqrt(y(X))/log(y(X))=o(log X)"),
            "theorem": (
                "under the general cost condition, RH iff the maximal "
                "y(X)-rough retained-lattice target is X^o(1)"
            ),
            "subfrontier_is_admissible": True,
            "critical_scale_transfers_subpower": False,
        },
        "structural_burden": {
            "remaining_source": (
                "squarefree y-rough Mobius prefixes sampled jointly on the "
                "critical retained Fourier lattice"
            ),
            "cancellation_produced_by_preconditioner": False,
            "why_maximal": (
                "terminating inverses call all smaller y-smooth dilates X/d"
            ),
            "beyond_frontier": (
                "absolute Neumann inversion loses a fixed power; signed scale "
                "cancellation or a different norm could still improve it"
            ),
        },
        "bounded_replay": {
            "coefficients": coefficient_panel(),
            "commuting_scales": commuting_scale_panel(),
        },
        "scope": {
            "exact_prefix_coordinate_theorem": True,
            "pnt_asymptotic_imported": True,
            "rough_prefix_estimate_proved": False,
            "critical_retained_estimate_proved": False,
            "cancellation_or_rh_proved": False,
            "operator_norm_claim_for_discarded_lattice_tail": False,
        },
        "resource_caps": {
            "coefficient_cap": COEFFICIENT_CAP,
            "prefix_cap": PREFIX_CAP,
            "toy_primes": list(TOY_PRIMES),
            "floating_point_operations": 0,
            "zeta_zeros": 0,
            "large_matrices": 0,
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
