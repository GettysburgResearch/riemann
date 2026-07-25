#!/usr/bin/env python3
from __future__ import annotations

import json
import random
import mpmath as mp

SEGMENT_SIZE = 20_000_000
T = mp.mpf(94_184_072_727_073) / 20


def log_series(q: int, m: int, J: int = 3) -> mp.mpf:
    z = mp.mpf(q - m) / (q + m)
    return mp.log(m) + 2 * mp.fsum(z ** (2 * j + 1) / (2 * j + 1) for j in range(J + 1))


def invsqrt_series(q: int, m: int, J: int = 5) -> mp.mpf:
    y = mp.mpf(q - m) / m
    coefficient = mp.mpf(1)
    total = coefficient
    for k in range(1, J + 1):
        coefficient *= -mp.mpf(2 * k - 1) / (2 * k)
        total += coefficient * y**k
    return total / mp.sqrt(m)


def run() -> dict[str, object]:
    mp.mp.dps = 100
    rng = random.Random(2815)
    samples: list[tuple[int, int]] = []
    for segment in [2000, 2001, 2500, 3500, 4899]:
        low = 2 + segment * SEGMENT_SIZE
        midpoint = low + SEGMENT_SIZE // 2
        samples.extend([(low, midpoint), (midpoint, midpoint), (low + SEGMENT_SIZE - 1, midpoint)])
        for _ in range(40):
            samples.append((rng.randrange(low, low + SEGMENT_SIZE), midpoint))

    max_log = mp.mpf(0)
    max_phase = mp.mpf(0)
    max_inverse_sqrt = mp.mpf(0)
    for q, midpoint in samples:
        log_error = abs(mp.log(q) - log_series(q, midpoint))
        inverse_sqrt_error = abs(1 / mp.sqrt(q) - invsqrt_series(q, midpoint))
        max_log = max(max_log, log_error)
        max_phase = max(max_phase, T * log_error)
        max_inverse_sqrt = max(max_inverse_sqrt, inverse_sqrt_error)

    return {
        "status": "EMPIRICAL_HIGH_PRECISION_REGRESSION",
        "samples": len(samples),
        "max_log_error": mp.nstr(max_log, 50),
        "max_phase_error": mp.nstr(max_phase, 50),
        "max_reciprocal_sqrt_error": mp.nstr(max_inverse_sqrt, 50),
        "proof_boundary": (
            "mpmath comparison only; exact proof is verify_target_bounds.py and L-2815/L-2816"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
