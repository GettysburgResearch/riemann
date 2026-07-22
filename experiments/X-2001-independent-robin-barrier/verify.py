#!/usr/bin/env python3
"""Independent exact-rational verification of the Robin finite barrier.

This program deliberately does not import or call the Decimal implementation in
X-0201/X-0202. It uses direct trial-division factorization and a pure-integer
dyadic interval backend for log, Euler's constant, and exp.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Sequence

from rational_intervals import (
    DyadicInterval,
    euler_gamma_interval,
    exp_interval,
    log_fraction_interval,
    log_interval,
    parse_decimal_fraction,
)

FINITE_EXCEPTION = 5040
WINDOW_END = 5582
RECORD_THRESHOLD_START = 5583

# Exact finite decimal endpoints copied from the committed X-0202 certificate.
# They are parsed as Fractions, never as binary floats or Decimal values.
X0202_REFERENCE = {
    "5041": {
        "rhs_lower": "3.81691873568367079580846110342104611585507347583877999942192E+0",
        "rhs_upper": "3.81693782032506077787772575644211800138925559432966874963404E+0",
        "difference_lower": "3.7076488952982464196230725726719996200891962968493384557576E-1",
        "difference_upper": "3.7078397417121462403157191028827184754310174817582259578789E-1",
    },
    "5583": {
        "rhs_lower": "3.83812670368567483280437118228254259503981052272233075860800E+0",
        "rhs_upper": "3.83814589436716992493567908431626077827237556069052927725746E+0",
        "difference_lower": "3.146559043673756627594418730449980171528462709266336990E-5",
        "difference_upper": "5.065627193182969758384622102268303428032259529118201937E-5",
    },
}


@dataclass(frozen=True)
class ExactMaximum:
    start: int
    end: int
    maximizers: list[int]
    sigma_at_maximizer: int
    denominator_n: int
    reduced_numerator: int
    reduced_denominator: int


@dataclass(frozen=True)
class Comparison:
    n: int
    rational_numerator: int
    rational_denominator: int
    log_n: dict[str, object]
    log_log_n: dict[str, object]
    rhs: dict[str, object]
    rhs_minus_rational: dict[str, object]
    certified_strictly_positive: bool
    certified_strictly_negative: bool
    x0202_reference_available: bool
    contained_in_x0202_rhs_interval: bool | None
    contained_in_x0202_difference_interval: bool | None


def factorization_trial_division(n: int) -> list[tuple[int, int]]:
    """Factor n using direct trial division, independent of divisor-sum sieving."""
    if n < 1:
        raise ValueError("n must be positive")
    remaining = n
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def sigma_from_factorization(n: int) -> int:
    """Compute sigma(n) exactly from a freshly obtained factorization."""
    result = 1
    for prime, exponent in factorization_trial_division(n):
        result *= (prime ** (exponent + 1) - 1) // (prime - 1)
    return result


def exact_abundancy_maximum(start: int, end: int) -> ExactMaximum:
    """Maximize sigma(n)/n by exact integer cross multiplication."""
    if not (1 <= start <= end):
        raise ValueError("invalid range")
    best_n = start
    best_sigma = sigma_from_factorization(start)
    maximizers = [start]
    for n in range(start + 1, end + 1):
        sigma_n = sigma_from_factorization(n)
        comparison = sigma_n * best_n - best_sigma * n
        if comparison > 0:
            best_n = n
            best_sigma = sigma_n
            maximizers = [n]
        elif comparison == 0:
            maximizers.append(n)
    reduced = Fraction(best_sigma, best_n)
    return ExactMaximum(
        start=start,
        end=end,
        maximizers=maximizers,
        sigma_at_maximizer=best_sigma,
        denominator_n=best_n,
        reduced_numerator=reduced.numerator,
        reduced_denominator=reduced.denominator,
    )


def sigma_sequence_digest(end: int) -> str:
    """Hash the exact sequence n:sigma(n) for compact reproduction checks."""
    digest = hashlib.sha256()
    for n in range(1, end + 1):
        digest.update(f"{n}:{sigma_from_factorization(n)}\n".encode("ascii"))
    return digest.hexdigest()


def interval_subset_of_decimal_bounds(
    interval: DyadicInterval, lower_text: str, upper_text: str
) -> bool:
    """Check interval containment against exact finite-decimal endpoints."""
    lower_ref = parse_decimal_fraction(lower_text)
    upper_ref = parse_decimal_fraction(upper_text)
    scale = 1 << interval.bits
    return (
        interval.lower * lower_ref.denominator
        >= lower_ref.numerator * scale
        and interval.upper * upper_ref.denominator
        <= upper_ref.numerator * scale
    )


def compare_rhs_to_fraction(
    n: int,
    rational: Fraction,
    *,
    exp_gamma: DyadicInterval,
    bits: int,
    log_terms: int,
    decimal_digits: int,
) -> Comparison:
    """Enclose exp(gamma) log log(n) minus an exact rational."""
    log_n = log_fraction_interval(Fraction(n), bits=bits, terms=log_terms)
    log_log_n = log_interval(log_n, terms=log_terms)
    rhs = exp_gamma.multiply(log_log_n)
    rational_interval = DyadicInterval.from_fraction(rational, bits)
    difference = rhs.subtract(rational_interval)

    reference = X0202_REFERENCE.get(str(n))
    rhs_containment: bool | None = None
    difference_containment: bool | None = None
    if reference is not None:
        rhs_containment = interval_subset_of_decimal_bounds(
            rhs, reference["rhs_lower"], reference["rhs_upper"]
        )
        difference_containment = interval_subset_of_decimal_bounds(
            difference,
            reference["difference_lower"],
            reference["difference_upper"],
        )

    return Comparison(
        n=n,
        rational_numerator=rational.numerator,
        rational_denominator=rational.denominator,
        log_n=log_n.to_json(decimal_digits),
        log_log_n=log_log_n.to_json(decimal_digits),
        rhs=rhs.to_json(decimal_digits),
        rhs_minus_rational=difference.to_json(decimal_digits),
        certified_strictly_positive=difference.is_strictly_positive(),
        certified_strictly_negative=difference.is_strictly_negative(),
        x0202_reference_available=reference is not None,
        contained_in_x0202_rhs_interval=rhs_containment,
        contained_in_x0202_difference_interval=difference_containment,
    )


def build_certificate(
    *,
    bits: int = 320,
    log_terms: int = 96,
    exp_terms: int = 96,
    harmonic_cutoff: int = 1_000_000,
    decimal_digits: int = 70,
) -> dict[str, object]:
    """Build and internally validate the independent finite-barrier certificate."""
    below = exact_abundancy_maximum(1, FINITE_EXCEPTION)
    window = exact_abundancy_maximum(FINITE_EXCEPTION + 1, WINDOW_END)
    if below.maximizers != [5040] or Fraction(
        below.reduced_numerator, below.reduced_denominator
    ) != Fraction(403, 105):
        raise RuntimeError("independent maximum on [1,5040] disagrees")
    if window.maximizers != [5460] or Fraction(
        window.reduced_numerator, window.reduced_denominator
    ) != Fraction(224, 65):
        raise RuntimeError("independent maximum on [5041,5582] disagrees")

    gamma = euler_gamma_interval(
        harmonic_cutoff=harmonic_cutoff, bits=bits, log_terms=log_terms
    )
    exp_gamma = exp_interval(gamma, terms=exp_terms)

    comparison_5041 = compare_rhs_to_fraction(
        5041,
        Fraction(224, 65),
        exp_gamma=exp_gamma,
        bits=bits,
        log_terms=log_terms,
        decimal_digits=decimal_digits,
    )
    comparison_5582 = compare_rhs_to_fraction(
        5582,
        Fraction(403, 105),
        exp_gamma=exp_gamma,
        bits=bits,
        log_terms=log_terms,
        decimal_digits=decimal_digits,
    )
    comparison_5583 = compare_rhs_to_fraction(
        5583,
        Fraction(403, 105),
        exp_gamma=exp_gamma,
        bits=bits,
        log_terms=log_terms,
        decimal_digits=decimal_digits,
    )

    if not comparison_5041.certified_strictly_positive:
        raise RuntimeError("failed strict positive comparison at n=5041")
    if not comparison_5582.certified_strictly_negative:
        raise RuntimeError("failed strict negative comparison at n=5582")
    if not comparison_5583.certified_strictly_positive:
        raise RuntimeError("failed strict positive comparison at n=5583")

    for comparison in (comparison_5041, comparison_5583):
        if comparison.contained_in_x0202_rhs_interval is not True:
            raise RuntimeError(f"rhs enclosure at n={comparison.n} is not inside X-0202")
        if comparison.contained_in_x0202_difference_interval is not True:
            raise RuntimeError(
                f"difference enclosure at n={comparison.n} is not inside X-0202"
            )

    return {
        "schema": "riemann.robin.independent-finite-barrier.v2",
        "status": "INDEPENDENT_CERTIFIED_REPRODUCTION",
        "agent": "gpt56-03-b",
        "issue": 20,
        "base_claim": "T-0201",
        "backend": {
            "language": "Python standard library",
            "integer_factorization": "direct trial division for every n",
            "transcendentals": "pure-integer fixed-denominator dyadic intervals",
            "uses_binary_float": False,
            "uses_decimal_transcendentals": False,
            "imports_x0201_or_x0202_code": False,
            "bits": bits,
            "log_terms": log_terms,
            "exp_terms": exp_terms,
            "harmonic_cutoff": harmonic_cutoff,
        },
        "exact_maximum_1_through_5040": asdict(below),
        "exact_maximum_5041_through_5582": asdict(window),
        "sigma_sequence_sha256_1_through_5582": sigma_sequence_digest(WINDOW_END),
        "gamma": gamma.to_json(decimal_digits),
        "exp_gamma": exp_gamma.to_json(decimal_digits),
        "comparison_at_5041": asdict(comparison_5041),
        "comparison_at_5582": asdict(comparison_5582),
        "comparison_at_5583": asdict(comparison_5583),
        "sharp_integer_crossing": {
            "quantity": "exp(gamma) log log(n) - 403/105",
            "last_negative_integer": 5582,
            "first_positive_integer": 5583,
            "justification": (
                "The two adjacent signs are certified and exp(gamma) log log(x) "
                "is strictly increasing for x>1."
            ),
        },
        "boundary_audit": {
            "5040": "excluded endpoint of Robin's theorem; global finite maximum",
            "5041": "first in-domain integer; finite-window lower comparison point",
            "5582": "last finite-window integer and last integer below 403/105",
            "5583": "first integer above 403/105; record-maximizer threshold",
        },
        "deduction": (
            "No Robin counterexample lies in [5041,5582]. For any counterexample "
            "n>=5583, its least abundancy record-maximizer m<=n satisfies "
            "sigma(m)/m >= exp(gamma)loglog(n) >= exp(gamma)loglog(5583) "
            "> 403/105, while every k<=5040 has sigma(k)/k<=403/105. Hence "
            "m>5040; L-0201 makes m a superabundant Robin counterexample."
        ),
        "result": (
            "The exact finite maxima and both strict transcendental signs in "
            "T-0201/X-0202 are independently reproduced. The adjacent n=5582 "
            "negative sign strengthens the barrier to a sharp integer crossing. "
            "No discrepancy found."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bits", type=int, default=320)
    parser.add_argument("--log-terms", type=int, default=96)
    parser.add_argument("--exp-terms", type=int, default=96)
    parser.add_argument("--harmonic-cutoff", type=int, default=1_000_000)
    parser.add_argument("--decimal-digits", type=int, default=70)
    parser.add_argument("--output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        certificate = build_certificate(
            bits=args.bits,
            log_terms=args.log_terms,
            exp_terms=args.exp_terms,
            harmonic_cutoff=args.harmonic_cutoff,
            decimal_digits=args.decimal_digits,
        )
    except (ValueError, RuntimeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    text = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
