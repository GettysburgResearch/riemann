#!/usr/bin/env python3
"""Floating reconnaissance for the parabolic ordinary-prime tail queue.

Arithmetic class: FLOATING_RECONNAISSANCE_ONLY.
No output is a proof certificate or an asymptotic theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Any


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def parabolic_seed(limit: int) -> list[float]:
    values = [0.0] * (limit + 2)
    for m in range(2, limit + 1):
        values[m] = 2.0 * math.sqrt(m) * (
            math.log(limit / m)
            - 2.0 * (1.0 - math.sqrt(m / limit))
        )
    return values


def evaluate(limit: int) -> dict[str, Any]:
    primes = primes_up_to(limit)
    seed = parabolic_seed(limit)

    residuals: list[float] = []
    for p in primes:
        response = 0.0
        for multiple in range(p, limit + 1, p):
            response += seed[multiple] - seed[multiple + 1]
        target = math.log(limit / p) / math.sqrt(p)
        residuals.append(response - target)

    tail = 0.0
    queue = 0.0
    maximizing_start: int | None = None
    last_positive_start: int | None = None

    for index in range(len(primes) - 1, -1, -1):
        tail += residuals[index]
        if tail > 0.0:
            last_positive_start = primes[index]
        if tail > queue:
            queue = tail
            maximizing_start = primes[index]

    return {
        "X": limit,
        "prime_count": len(primes),
        "queue": max(queue, 0.0),
        "maximizing_start": maximizing_start,
        "total_tail": sum(residuals),
        "last_positive_start": last_positive_start,
        "max_point_residual": max(residuals),
        "min_point_residual": min(residuals),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("X", nargs="+", type=int)
    args = parser.parse_args()
    if any(limit < 2 for limit in args.X):
        raise SystemExit("all endpoints must be at least 2")

    result = {
        "classification": "FLOATING_RECONNAISSANCE_ONLY",
        "proof_boundary": (
            "Binary64 exploration of L-26704; no directed intervals, "
            "cofinal estimate, prime-tail theorem, or RH claim."
        ),
        "levels": [evaluate(limit) for limit in args.X],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
