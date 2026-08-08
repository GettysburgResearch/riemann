#!/usr/bin/env python3
"""Directed finite mutation for R-24505.

For primes p in (X/3,X/2], the complete stopped-power boundary satisfies

  B_X(p) >= log(X)[(2p-1)^(-1/2)-(3p)^(-1/2)]
            -(2p-1)^(-1/2)log(X/(2p-1)).

Any complete divisor source supported at the next half endpoint has sigma_p=B_X(p).
The checker outward-rounds this lower bound and sums sqrt(p)B_X(p).
It proves no asymptotic prime theorem and no RH statement.
"""
from __future__ import annotations

from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
import hashlib
import json


PRECISION = 60
LOW = Context(prec=PRECISION, rounding=ROUND_FLOOR)
HIGH = Context(prec=PRECISION, rounding=ROUND_CEILING)


def prime_sieve(limit: int) -> bytearray:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return sieve


def reciprocal_sqrt_interval(n: int) -> tuple[Decimal, Decimal]:
    value = Decimal(n)
    sqrt_low = LOW.sqrt(value)
    sqrt_high = HIGH.sqrt(value)
    return (
        LOW.divide(Decimal(1), sqrt_high),
        HIGH.divide(Decimal(1), sqrt_low),
    )


def certify(endpoint: int) -> dict[str, object]:
    primes = prime_sieve(endpoint // 2)
    log_x_low = LOW.ln(Decimal(endpoint))

    prime_count = 0
    total_lower = Decimal(0)
    minimum_term_lower: Decimal | None = None

    for p in range(endpoint // 3 + 1, endpoint // 2 + 1):
        if not primes[p]:
            continue
        prime_count += 1

        inv_2p1_low, inv_2p1_high = reciprocal_sqrt_interval(2 * p - 1)
        _inv_3p_low, inv_3p_high = reciprocal_sqrt_interval(3 * p)

        analytic_pair_low = LOW.subtract(inv_2p1_low, inv_3p_high)
        analytic_term_low = LOW.multiply(log_x_low, analytic_pair_low)

        ratio_high = HIGH.divide(Decimal(endpoint), Decimal(2 * p - 1))
        finite_log_high = HIGH.ln(ratio_high)
        finite_term_high = HIGH.multiply(finite_log_high, inv_2p1_high)

        boundary_lower = LOW.subtract(analytic_term_low, finite_term_high)
        sqrt_p_low = LOW.sqrt(Decimal(p))
        weighted_lower = LOW.multiply(sqrt_p_low, boundary_lower)
        assert weighted_lower > 0

        total_lower = LOW.add(total_lower, weighted_lower)
        if minimum_term_lower is None or weighted_lower < minimum_term_lower:
            minimum_term_lower = weighted_lower

    assert minimum_term_lower is not None
    return {
        "endpoint": endpoint,
        "prime_band": "X/3 < p <= X/2",
        "prime_count": prime_count,
        "minimum_weighted_boundary_lower": str(minimum_term_lower),
        "atomic_norm_band_lower": str(total_lower),
        "precision": PRECISION,
    }


def main() -> None:
    controls = [certify(x) for x in (10_000, 100_000, 1_000_000)]
    payload = {
        "schema": "riemann.x24505.boundary-atomic-obstruction.v1",
        "verdict": "PASS_DIRECTED_MACROSCOPIC_BOUNDARY_ATOMIC_LOWER_BOUND",
        "controls": controls,
        "does_not_prove": [
            "the prime number theorem",
            "the asymptotic Omega(X) conclusion without the analytic proof",
            "the failure of every possible relative analytic-boundary repair",
            "RH",
        ],
    }
    payload["content_sha256"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
