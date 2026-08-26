#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, isqrt, log, sqrt

PRIME_BOUND = 1000
REGRESSION_X = 1_000_000


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def exact_finite_core_mass(primes: list[int]) -> Fraction:
    # Coefficients of prod_p (1 - theta/p^2).
    coeff = [Fraction(1)]
    for p in primes:
        a = Fraction(1, p * p)
        coeff.append(Fraction(0))
        for k in range(len(coeff) - 1, 0, -1):
            coeff[k] -= a * coeff[k - 1]
    return sum(
        coeff[k] * Fraction(1, comb(k + 2, 2))
        for k in range(2, len(coeff))
    )


def spf_sieve(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def live_coefficient(n: int, spf: list[int]) -> float:
    singles = 0
    square_core_depth = 0
    x = n
    while x > 1:
        p = spf[x]
        exponent = 0
        while x % p == 0:
            x //= p
            exponent += 1
        if exponent == 1:
            singles += 1
        elif exponent == 2:
            square_core_depth += 1
        else:
            return 0.0
    if singles == 2 and square_core_depth >= 2:
        return ((-1.0) ** square_core_depth) / comb(square_core_depth + 2, 2)
    return 0.0


def kernel(y: float) -> float:
    root2 = sqrt(2.0)
    if 1.0 <= y < 2.0:
        return 8.0 - 4.0 * sqrt(y)
    if 2.0 <= y < 4.0:
        return -8.0 * (1.0 + root2) + 4.0 * root2 * sqrt(y)
    if 4.0 <= y < 8.0:
        return 8.0 * root2 - 2.0 * sqrt(y)
    return 0.0


def finite_current(limit: int) -> tuple[int, float, float]:
    spf = spf_sieve(limit)
    lower = limit // 8 + 1
    current = 0.0
    active = 0
    for n in range(lower, limit + 1):
        coefficient = live_coefficient(n, spf)
        if coefficient:
            active += 1
            current += coefficient * kernel(limit / n) / sqrt(n)
    scale = sqrt(limit) * log(log(limit)) / log(limit)
    return active, current, current / scale


def main() -> None:
    primes = primes_upto(PRIME_BOUND)
    finite_mass = exact_finite_core_mass(primes)

    # Any omitted live core contains a prime > B and at least one other prime.
    # The elementary Euler-product majorant used in the proof gives an absolute
    # tail below 2/(B-1).  The resulting exact lower bound is already positive.
    tail_bound = Fraction(2, PRIME_BOUND - 1)
    mass_lower = finite_mass - tail_bound
    assert mass_lower > 0

    getcontext().prec = 60
    two = Decimal(2)
    detector_moment = -((two - two.sqrt()) ** 2) * two.ln()
    assert detector_moment < 0

    active, current, normalized = finite_current(REGRESSION_X)
    assert active > 0
    assert current < 0
    assert -0.003 < normalized < -0.002

    finite_mass_text = f"{finite_mass.numerator}/{finite_mass.denominator}"
    proof = {
        "schema": "riemann.t103130.qpti.semiprime_refutation.v1",
        "prime_bound": PRIME_BOUND,
        "finite_prime_count": len(primes),
        "finite_live_core_mass_decimal": f"{float(finite_mass):.16g}",
        "finite_live_core_mass_rational_sha256": sha256(
            finite_mass_text.encode("ascii")
        ).hexdigest(),
        "finite_live_core_mass_denominator_digits": len(str(finite_mass.denominator)),
        "declared_absolute_tail_bound": f"{tail_bound.numerator}/{tail_bound.denominator}",
        "certified_live_core_mass_lower_decimal": f"{float(mass_lower):.16g}",
        "live_core_mass_positive": True,
        "detector_semiprime_moment_formula": "-(2-sqrt(2))^2*log(2)",
        "detector_semiprime_moment_decimal": str(detector_moment),
        "detector_semiprime_moment_negative": True,
        "regression_x": REGRESSION_X,
        "regression_active_atoms": active,
        "regression_current": f"{current:.16g}",
        "regression_normalized_current": f"{normalized:.16g}",
        "regression_negative": True,
        "analytic_input": (
            "classical squarefree-semiprime asymptotic plus bounded-variation "
            "partial summation; proof is in L-103121/R-103121"
        ),
        "ebd103120": "REFUTED",
        "qpti103112_as_literal_euler_beta_gate": "REFUTED",
        "bci_hmo_equivalence_from_qpti": "WITHDRAWN_PENDING_SOURCE_REPAIR",
        "rh_established": False,
    }
    canonical = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
    proof["proof_object_sha256"] = sha256(canonical).hexdigest()
    proof["verdict"] = "PASS_T103130_QPTI_SEMIPRIME_MAIN_REFUTATION"
    print(json.dumps(proof, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
