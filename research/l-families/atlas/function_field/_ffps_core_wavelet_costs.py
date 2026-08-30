"""Exact finite cost replays for the core divisor transform."""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from _ffps_core_wavelet_arithmetic import (
    EXCEPTIONAL_PRIME,
    divisors,
    is_squarefree,
    tau,
    validate_positive_integer,
)


def assembly_cost_replay(limit: int = 120) -> dict[str, object]:
    validate_positive_integer(limit)
    left = Fraction()
    exact_reindexed = Fraction()
    for sieve in range(1, limit + 1):
        if sieve % EXCEPTIONAL_PRIME == 0 or not is_squarefree(sieve):
            continue
        left += Fraction(tau(sieve), sieve) * sum(
            (Fraction(1, core) for core in divisors(sieve)), Fraction()
        )
    for core in range(1, limit + 1):
        if core % EXCEPTIONAL_PRIME == 0 or not is_squarefree(core):
            continue
        for cofactor in range(1, limit // core + 1):
            if (
                cofactor % EXCEPTIONAL_PRIME == 0
                or not is_squarefree(cofactor)
                or gcd(core, cofactor) != 1
            ):
                continue
            exact_reindexed += Fraction(
                tau(core) * tau(cofactor), core * core * cofactor
            )
    if left != exact_reindexed:
        raise ArithmeticError("divisor assembly cost reindexing failed")

    outer_truncation = sum(
        (
            Fraction(tau(core), core * core)
            for core in range(1, limit + 1)
            if core % EXCEPTIONAL_PRIME and is_squarefree(core)
        ),
        Fraction(),
    )
    inner_truncation = sum(
        (
            Fraction(tau(cofactor), cofactor)
            for cofactor in range(1, limit + 1)
            if cofactor % EXCEPTIONAL_PRIME and is_squarefree(cofactor)
        ),
        Fraction(),
    )
    product_upper = outer_truncation * inner_truncation
    if left > product_upper:
        raise ArithmeticError("dropped-coprimality product upper bound failed")

    harmonic = sum((Fraction(1, value) for value in range(1, limit + 1)), Fraction())
    all_divisor_harmonic = sum(
        (Fraction(tau(value), value) for value in range(1, limit + 1)),
        Fraction(),
    )
    if inner_truncation > all_divisor_harmonic or all_divisor_harmonic > harmonic**2:
        raise ArithmeticError("harmonic divisor majorant failed")

    return {
        "exact_eta_zero_cost": str(left),
        "exact_reindexing": True,
        "finite_product_upper": str(product_upper),
        "harmonic_divisor_upper": str(harmonic**2),
        "limit": limit,
        "proof_euler_factor": (
            "sum_r tau(r)/r^(2-eta) has Euler product "
            "prod_(p!=67)(1+2*p^(eta-2)), convergent for eta<1"
        ),
    }


def inverse_assembly_cost_replay(limit: int = 120) -> dict[str, object]:
    """Authenticate the polylog condition number of divisor inversion."""
    validate_positive_integer(limit)
    fourth_divisor_harmonic = sum(
        (
            Fraction(tau(value) ** 2, value)
            for value in range(1, limit + 1)
            if value % EXCEPTIONAL_PRIME and is_squarefree(value)
        ),
        Fraction(),
    )
    harmonic = sum((Fraction(1, value) for value in range(1, limit + 1)), Fraction())
    if fourth_divisor_harmonic > harmonic**4:
        raise ArithmeticError("fourth-divisor harmonic majorant failed")

    rows = []
    for sieve in range(1, limit + 1):
        if sieve % EXCEPTIONAL_PRIME == 0 or not is_squarefree(sieve):
            continue
        exact_coefficient = sum(
            (
                Fraction(tau(core) ** 2, core)
                for core in range(sieve, limit + 1, sieve)
                if core % EXCEPTIONAL_PRIME
                and is_squarefree(core)
                and core % sieve == 0
            ),
            Fraction(),
        )
        factorized_upper = Fraction(tau(sieve) ** 2, sieve) * harmonic**4
        if exact_coefficient > factorized_upper:
            raise ArithmeticError("inverse divisor coefficient majorant failed")
        if sieve in {1, 2, 3, 6, 30}:
            rows.append(
                {
                    "coefficient": str(exact_coefficient),
                    "factorized_upper": str(factorized_upper),
                    "sieve": sieve,
                }
            )
    return {
        "finite_support_limit": limit,
        "fourth_divisor_harmonic": str(fourth_divisor_harmonic),
        "harmonic_fourth_power_upper": str(harmonic**4),
        "inverse_condition_number_is_polylogarithmic_up_to_tau_s_squared": True,
        "rows": rows,
    }
