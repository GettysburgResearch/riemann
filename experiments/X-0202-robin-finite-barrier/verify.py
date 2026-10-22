#!/usr/bin/env python3
"""Exact finite barrier supporting a complete superabundant Robin reduction.

The divisor-sum maxima are computed with exact integers. Two transcendental
comparisons are enclosed by the directed-decimal engine from X-0201.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from decimal import Decimal
from fractions import Fraction
import json
from pathlib import Path
import sys
from typing import Sequence

X0201 = Path(__file__).resolve().parents[1] / "X-0201-robin-ca-scan"
if str(X0201) not in sys.path:
    sys.path.insert(0, str(X0201))

from certify import DecimalIntervals, Interval, gamma_interval  # noqa: E402

FINITE_EXCEPTION = 5040
WINDOW_END = 5582
RECORD_THRESHOLD_START = 5583


@dataclass(frozen=True)
class ExactMaximum:
    start: int
    end: int
    maximizers: list[int]
    sigma: int
    denominator_n: int
    reduced_numerator: int
    reduced_denominator: int


@dataclass(frozen=True)
class CertifiedComparison:
    n: int
    rational_numerator: int
    rational_denominator: int
    rhs: dict[str, str]
    rhs_minus_rational: dict[str, str]
    certified_strictly_positive: bool


def divisor_sums(limit: int) -> list[int]:
    """Return sigma(n) for 0 <= n <= limit using exact integer additions."""
    if limit < 1:
        raise ValueError("limit must be positive")
    sigma = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            sigma[multiple] += divisor
    return sigma


def exact_abundancy_maximum(
    sigma: list[int], start: int, end: int
) -> ExactMaximum:
    if not (1 <= start <= end < len(sigma)):
        raise ValueError("invalid range")
    best_sigma = sigma[start]
    best_n = start
    maximizers = [start]
    for n in range(start + 1, end + 1):
        left = sigma[n] * best_n
        right = best_sigma * n
        if left > right:
            best_sigma = sigma[n]
            best_n = n
            maximizers = [n]
        elif left == right:
            maximizers.append(n)
    reduced = Fraction(best_sigma, best_n)
    return ExactMaximum(
        start=start,
        end=end,
        maximizers=maximizers,
        sigma=best_sigma,
        denominator_n=best_n,
        reduced_numerator=reduced.numerator,
        reduced_denominator=reduced.denominator,
    )


def robin_rhs_interval(
    n: int, *, precision: int, gamma_terms: int
) -> Interval:
    if n <= 1:
        raise ValueError("n must be greater than one")
    engine = DecimalIntervals(precision)
    gamma = gamma_interval(engine, gamma_terms)
    exp_gamma = engine.exponential(gamma)
    log_n = engine.logarithm(engine.exact(n))
    log_log_n = engine.logarithm(log_n)
    return engine.multiply_nonnegative(exp_gamma, log_log_n)


def compare_rhs_to_fraction(
    n: int,
    rational: Fraction,
    *,
    precision: int,
    gamma_terms: int,
) -> CertifiedComparison:
    engine = DecimalIntervals(precision)
    rhs = robin_rhs_interval(n, precision=precision, gamma_terms=gamma_terms)
    rational_interval = engine.divide_positive(
        engine.exact(rational.numerator), engine.exact(rational.denominator)
    )
    difference = engine.subtract(rhs, rational_interval)
    return CertifiedComparison(
        n=n,
        rational_numerator=rational.numerator,
        rational_denominator=rational.denominator,
        rhs=rhs.to_json(),
        rhs_minus_rational=difference.to_json(),
        certified_strictly_positive=difference.lower > Decimal(0),
    )


def build_certificate(
    *, precision: int = 60, gamma_terms: int = 100_000
) -> dict[str, object]:
    sigma = divisor_sums(WINDOW_END)
    below = exact_abundancy_maximum(sigma, 1, FINITE_EXCEPTION)
    window = exact_abundancy_maximum(
        sigma, FINITE_EXCEPTION + 1, WINDOW_END
    )
    below_ratio = Fraction(below.reduced_numerator, below.reduced_denominator)
    window_ratio = Fraction(window.reduced_numerator, window.reduced_denominator)
    first_comparison = compare_rhs_to_fraction(
        FINITE_EXCEPTION + 1,
        window_ratio,
        precision=precision,
        gamma_terms=gamma_terms,
    )
    barrier_comparison = compare_rhs_to_fraction(
        RECORD_THRESHOLD_START,
        below_ratio,
        precision=precision,
        gamma_terms=gamma_terms,
    )
    if below.maximizers != [5040] or below_ratio != Fraction(403, 105):
        raise RuntimeError("unexpected maximum on [1,5040]")
    if window.maximizers != [5460] or window_ratio != Fraction(224, 65):
        raise RuntimeError("unexpected maximum on [5041,5582]")
    if not first_comparison.certified_strictly_positive:
        raise RuntimeError("failed to certify the finite window")
    if not barrier_comparison.certified_strictly_positive:
        raise RuntimeError("failed to certify the record threshold")
    return {
        "schema": "riemann.robin.finite-barrier.v1",
        "status": "CERTIFIED_COMPUTATION_PENDING_INDEPENDENT_REPRODUCTION",
        "precision_decimal_digits": precision,
        "gamma_terms": gamma_terms,
        "exact_maximum_1_through_5040": asdict(below),
        "exact_maximum_5041_through_5582": asdict(window),
        "comparison_at_5041": asdict(first_comparison),
        "comparison_at_5583": asdict(barrier_comparison),
        "deduction": (
            "Every Robin counterexample n>5040 yields a superabundant Robin "
            "counterexample m>5040: n<=5582 is excluded by the finite window; "
            "for n>=5583, the record maximizer below n must exceed 5040."
        ),
        "proof_boundary": (
            "The divisor-sum maxima are exact. The two transcendental signs use "
            "the X-0201 directed-decimal engine and require independent backend "
            "reproduction before promotion beyond PROPOSED."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=60)
    parser.add_argument("--gamma-terms", type=int, default=100_000)
    parser.add_argument("--output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        certificate = build_certificate(
            precision=args.precision, gamma_terms=args.gamma_terms
        )
    except (ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    text = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
