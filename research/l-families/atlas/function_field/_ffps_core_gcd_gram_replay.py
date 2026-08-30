"""Finite exact replays for the primitive shared-divisor Gram."""

from __future__ import annotations

from fractions import Fraction

from _ffps_core_gcd_gram_exact import (
    core_energy,
    finite_diagonal_majorant,
    gcd_off_diagonal,
    gram_parts,
    shared_divisor_kernel,
    shell_wavelets,
)
from _ffps_core_wavelet_arithmetic import divisors, tau


def exact_gram_replay() -> dict[str, object]:
    rows = []
    for alpha, blocks in (
        (0, ((8, 12), (12, 16))),
        (1, ((66, 100), (100, 134))),
    ):
        for lower, upper in blocks:
            direct = core_energy(alpha, lower, upper)
            gram, diagonal, off_diagonal = gram_parts(alpha, lower, upper)
            gcd_form = gcd_off_diagonal(alpha, lower, upper)
            if direct != gram:
                raise ArithmeticError("core energy/Gram identity failed")
            if gram != diagonal + off_diagonal:
                raise ArithmeticError("diagonal split failed")
            if off_diagonal != gcd_form:
                raise ArithmeticError("gcd form failed")
            rows.append(
                {
                    "alpha": alpha,
                    "core_energy_digest": direct.digest(),
                    "diagonal_digest": diagonal.digest(),
                    "height_block": [lower, upper],
                    "off_diagonal_digest": off_diagonal.digest(),
                    "product_shells": len(shell_wavelets(alpha, lower, upper)),
                }
            )
    return {
        "core_energy_equals_shared_divisor_gram": True,
        "diagonal_off_diagonal_split": True,
        "off_diagonal_equals_exact_gcd_form": True,
        "rows": rows,
    }


def feature_gram_replay() -> dict[str, object]:
    support = (1, 2, 3, 5, 6, 10, 15, 30)
    matrix = [
        [shared_divisor_kernel(left, right) for right in support]
        for left in support
    ]
    feature = [
        {core: Fraction(tau(core), core) for core in divisors(value)}
        for value in support
    ]
    rebuilt = [
        [
            sum(
                (
                    weight
                    for core, weight in feature[left].items()
                    if core in feature[right]
                ),
                Fraction(),
            )
            for right in range(len(support))
        ]
        for left in range(len(support))
    ]
    if matrix != rebuilt:
        raise ArithmeticError("feature Gram reconstruction failed")
    local_rows = []
    for prime in (2, 3, 5, 7, 11):
        determinant = Fraction(2, prime)
        trace = 2 + Fraction(2, prime)
        discriminant = trace * trace - 4 * determinant
        if discriminant != 4 + Fraction(4, prime * prime):
            raise ArithmeticError("local spectrum identity failed")
        local_rows.append(
            {
                "determinant": str(determinant),
                "discriminant": str(discriminant),
                "prime": prime,
                "trace": str(trace),
            }
        )
    return {
        "feature_gram_reconstruction": True,
        "kernel": "K_2(N,M)=sum_(r|gcd(N,M))tau(r)/r=prod_(p|gcd)(1+2/p)",
        "local_condition_number_asymptotic": "2p",
        "local_rows": local_rows,
        "support": list(support),
    }


def run_replays() -> dict[str, object]:
    return {
        "exact_gram_replay": exact_gram_replay(),
        "feature_gram_replay": feature_gram_replay(),
        "diagonal_majorant_replay": finite_diagonal_majorant(),
    }
