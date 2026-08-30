#!/usr/bin/env python3
"""Bounded prime-certificate acquisition for one m=3 masked gauge panel."""

from __future__ import annotations

import json
from math import gcd, isqrt, prod

MAX_CANDIDATES = 2000
PROTH_EXPONENT = 64


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def trial_prime(n: int) -> bool:
    require(type(n) is int and 2 <= n <= 1000300, "small-prime bound")
    return all(n % d for d in range(2, isqrt(n) + 1))


def proth_in_window(lower: int, upper: int):
    step = 1 << PROTH_EXPONENT
    k = (lower - 1) // step + 1
    k += 1 - k % 2
    for index in range(MAX_CANDIDATES):
        candidate = k * step + 1
        require(lower < candidate < upper, "bounded Proth window exhausted")
        require(0 < k < step, "Proth size condition")
        if all(candidate % p for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)):
            for base in range(2, 32):
                if (
                    gcd(base, candidate) == 1
                    and pow(base, (candidate - 1) // 2, candidate) == candidate - 1
                ):
                    return {
                        "prime": candidate,
                        "odd_multiplier": k,
                        "power_of_two": PROTH_EXPONENT,
                        "witness": base,
                        "candidates_examined": index + 1,
                    }
        k += 2
    raise ValueError("Proth candidate work cap reached")


def main():
    small = [n for n in range(100003, 100301) if trial_prime(n)][:6]
    require(
        len(small) == 6 and 300 * (max(small) - min(small)) < min(small),
        "six primes in relative-width 1/(100m) window",
    )
    t = prod(small)
    backgrounds = {}
    for label, lo, hi in (
        ("A", 1000, 1050),
        ("B", 1050, 1100),
        ("C", 1100, 1150),
        ("D", 1150, 1200),
    ):
        backgrounds[label] = proth_in_window(lo * t, hi * t)
    print(
        json.dumps(
            {
                "m": 3,
                "small_primes": small,
                "T": t,
                "backgrounds": backgrounds,
                "small_primality": "complete trial division",
                "large_primality": "Proth witness -1 at half exponent",
                "candidate_cap_per_window": MAX_CANDIDATES,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
