#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path

PRIMES_79 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79)
BASE_TERMS = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3), (11, 11), (13, 13))


def divisors_with_mu_below(limit: int) -> list[tuple[int, int]]:
    values = [(1, 1)]
    for prime in PRIMES_79:
        values += [(d * prime, -mu) for d, mu in values if d * prime <= limit]
    values.sort()
    return values


def exact_prefix_counterexample() -> tuple[Fraction, Fraction]:
    a_83 = sum((Fraction(mu, d) for d, mu in divisors_with_mu_below(83)), Fraction(0))
    expected = Fraction(
        -1401629533229069216211617003,
        107254825578022430263302818471,
    )
    assert a_83 == expected
    score_minus_target_coefficient = a_83 - Fraction(1, 83)
    expected_gap = Fraction(
        -223590076836035175208867029720,
        8902150522975861711854133933093,
    )
    assert score_minus_target_coefficient == expected_gap
    assert score_minus_target_coefficient < 0
    return a_83, score_minus_target_coefficient


def directed_base_gate() -> Decimal:
    # Decimal.ln and Decimal.sqrt are correctly rounded at the active precision.
    # We then enlarge every primitive by 10^-90, far above the 100-digit ulp.
    with localcontext() as ctx:
        ctx.prec = 100
        eps = Decimal(10) ** -90
        total_lower = Decimal(0)
        for n, base_prime in BASE_TERMS:
            log_prime_lower = ctx.ln(Decimal(base_prime)) - eps
            log_ratio_lower = ctx.ln(Decimal(83) / Decimal(n)) - eps
            sqrt_n_upper = ctx.sqrt(Decimal(n)) + eps
            assert log_prime_lower > 0 and log_ratio_lower > 0
            total_lower += log_prime_lower * log_ratio_lower / sqrt_n_upper

        assert total_lower > Decimal(649) / Decimal(50)
        # sqrt(83) < 228/25, hence (4/3)sqrt(83) < 304/25.
        assert 83 * 25 * 25 < 228 * 228
        assert Fraction(649, 50) - Fraction(304, 25) == Fraction(41, 50)
        return +total_lower


def rational_reductions() -> dict[str, str]:
    # Imported psi(x) >= 9x/10 for x >= 41 gives
    # A(x) > (1161/1000)sqrt(x) for x >= 83 because sqrt(41/83) < 71/100.
    assert 41 * 100 * 100 < 83 * 71 * 71
    derivative_margin = Fraction(1161, 1000) - Fraction(9, 83) - Fraction(2, 3)
    assert derivative_margin == Fraction(96089, 249000) > 0

    # Fully activated P_30 has reciprocal Euler product 4/15.
    reciprocal_product = Fraction(1, 2) * Fraction(2, 3) * Fraction(4, 5)
    assert reciprocal_product == Fraction(4, 15)
    target_slope = 3 * Fraction(4, 3) * reciprocal_product
    score_slope = 3 * Fraction(5, 3) * reciprocal_product
    assert target_slope == Fraction(16, 15)
    assert score_slope == Fraction(4, 3)
    physical_target_margin = score_slope - target_slope
    assert physical_target_margin == Fraction(4, 15) > 0

    return {
        "derivative_margin": str(derivative_margin),
        "target_upper_slope": str(target_slope),
        "score_upper_slope": str(score_slope),
        "physical_target_margin": str(physical_target_margin),
    }


def main() -> None:
    a_83, scalar_gap = exact_prefix_counterexample()
    base_lower = directed_base_gate()
    reductions = rational_reductions()
    result = {
        "classification": "PASS_DIRECT_EULER_SCORE_INTERFACE_AUDIT_AND_REPAIR",
        "A_P79_83": str(a_83),
        "scalar_score_minus_target_coefficient_at_p83_y1": str(scalar_gap),
        "nine_term_von_mangoldt_ramp_lower": str(base_lower),
        "base_physical_margin_lower": "41/50",
        **reductions,
        "scope": (
            "Exact rational refutation of the claimed P79 real-corridor first-moment surplus, "
            "directed verification of the x=83 von Mangoldt base gate, and exact rational "
            "reductions used by the physical component-entropy repair. The imported theorem "
            "psi(x) >= 0.9x for x >= 41 and the independent inherited-row positivity theorem "
            "are not replayed here. RH is not certified."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
