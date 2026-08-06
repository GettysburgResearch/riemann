#!/usr/bin/env python3
"""Ordinary-high-precision reconnaissance for T-20802/L-20808.

This script is deliberately NOT a directed proof producer.  It enumerates every
prime power through a finite integer cutoff exactly, streams the two cumulative
moments P,Q, solves the smooth Fenchel stationarity equation in binary64 for
ranking, and replays the record-low prefix with mpmath.

A finite positive result is reconnaissance only.  A production theorem needs
outward intervals for the prime moments and archimedean/Fenchel evaluation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import mpmath as mp


SCHEMA = "riemann.x20806.prime-prefix-transport-recon.v1"


def primes_through(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n in range(2, limit + 1) if flags[n]]


def prime_powers(limit: int) -> list[tuple[int, int, int]]:
    rows: list[tuple[int, int, int]] = []
    for p in primes_through(limit):
        q = p
        exponent = 1
        while q <= limit:
            rows.append((q, p, exponent))
            if q > limit // p:
                break
            q *= p
            exponent += 1
    rows.sort()
    if any(rows[i][0] >= rows[i + 1][0] for i in range(len(rows) - 1)):
        raise RuntimeError("prime-power ordinates are not strictly increasing")
    return rows


def manifest_sha(rows: Iterable[tuple[int, int, int]]) -> str:
    digest = hashlib.sha256()
    for q, p, exponent in rows:
        digest.update(f"{q},{p},{exponent}\n".encode("ascii"))
    return digest.hexdigest()


def constants_float() -> tuple[float, float]:
    mp.mp.dps = 50
    b = mp.mpf("0.5") * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
    c = mp.pi**2 + 8 * mp.catalan
    return float(b), float(c)


B_FLOAT, C_FLOAT = constants_float()
TAU_ONE = math.log(2.0)


def a_float(t: float) -> float:
    y = math.exp(t / 2.0)
    total = 0.0
    for m in range(1, 256):
        d = 4 * m + 1
        term = y ** (-d) / (d * d)
        total += term
        if term < 1.0e-19:
            break
    return 4.0 * (y - 2.0) + B_FLOAT * t + C_FLOAT / 4.0 - 4.0 * total


def a_prime_float(t: float) -> float:
    x = math.exp(-t / 2.0)
    return (
        2.0 * math.exp(t / 2.0)
        + B_FLOAT
        + math.atanh(x)
        + math.atan(x)
        - 2.0 * x
    )


def a_second_float(t: float) -> float:
    return math.exp(t / 2.0) - math.exp(-5.0 * t / 2.0) / (
        1.0 - math.exp(-2.0 * t)
    )


def solve_stationary_float(p_value: float, previous: float) -> float:
    if p_value <= a_prime_float(TAU_ONE):
        return TAU_ONE
    t = max(previous, TAU_ONE)
    for _ in range(8):
        residual = a_prime_float(t) - p_value
        curvature = a_second_float(t)
        candidate = t - residual / curvature
        if not math.isfinite(candidate) or candidate < TAU_ONE:
            candidate = (t + TAU_ONE) / 2.0
        if abs(candidate - t) < 2.0e-15:
            return candidate
        t = candidate
    return t


def high_precision_replay(
    rows: list[tuple[int, int, int]], prefix_length: int, digits: int
) -> dict[str, str]:
    mp.mp.dps = digits
    b = mp.mpf("0.5") * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
    c = mp.pi**2 + 8 * mp.catalan

    def a_mp(t: mp.mpf) -> mp.mpf:
        y = mp.e ** (t / 2)
        tail = mp.nsum(
            lambda m: y ** (-(4 * m + 1)) / (4 * m + 1) ** 2,
            [1, mp.inf],
        )
        return 4 * (y - 2) + b * t + c / 4 - 4 * tail

    def a_prime_mp(t: mp.mpf) -> mp.mpf:
        x = mp.e ** (-t / 2)
        return 2 * mp.e ** (t / 2) + b + mp.atanh(x) + mp.atan(x) - 2 * x

    p_sum = mp.mpf(0)
    q_sum = mp.mpf(0)
    for q, p, _exponent in rows[:prefix_length]:
        weight = mp.log(p) / mp.sqrt(q)
        tau = mp.log(q)
        p_sum += weight
        q_sum += weight * tau

    q_last = rows[prefix_length - 1][0]
    guess = mp.log(q_last)
    t_star = mp.findroot(lambda t: a_prime_mp(t) - p_sum, guess)
    margin = q_sum - (p_sum * t_star - a_mp(t_star))
    next_tau = (
        mp.log(rows[prefix_length][0])
        if prefix_length < len(rows)
        else mp.nan
    )
    return {
        "P": mp.nstr(p_sum, digits),
        "Q": mp.nstr(q_sum, digits),
        "t_star": mp.nstr(t_star, digits),
        "margin": mp.nstr(margin, digits),
        "left_tau": mp.nstr(mp.log(q_last), digits),
        "right_tau": mp.nstr(next_tau, digits),
    }


def scan(limit: int, digits: int) -> dict[str, object]:
    rows = prime_powers(limit)
    if not rows:
        raise RuntimeError("empty prime-power manifest")

    p_sum = 0.0
    q_sum = 0.0
    stationary = TAU_ONE
    minimum = math.inf
    maximum = -math.inf
    minimum_index = -1
    final_margin = math.nan

    for index, (q, p, _exponent) in enumerate(rows):
        weight = math.log(p) / math.sqrt(q)
        tau = math.log(q)
        p_sum += weight
        q_sum += weight * tau
        stationary = solve_stationary_float(p_sum, stationary)
        conjugate = p_sum * stationary - a_float(stationary)
        margin = q_sum - conjugate
        if margin < minimum:
            minimum = margin
            minimum_index = index
        maximum = max(maximum, margin)
        final_margin = margin

    replay = high_precision_replay(rows, minimum_index + 1, digits)
    q_last, p_last, exponent_last = rows[minimum_index]
    next_q = rows[minimum_index + 1][0] if minimum_index + 1 < len(rows) else None

    return {
        "schema": SCHEMA,
        "classification": "ORDINARY_HIGH_PRECISION_RECONNAISSANCE",
        "limit": limit,
        "prime_power_count": len(rows),
        "manifest_sha256": manifest_sha(rows),
        "all_binary64_prefix_margins_positive": minimum > 0.0,
        "record_low": {
            "prefix_index_zero_based": minimum_index,
            "prefix_length": minimum_index + 1,
            "q": q_last,
            "p": p_last,
            "exponent": exponent_last,
            "next_q": next_q,
            "binary64_margin": format(minimum, ".17g"),
            "high_precision_replay": replay,
        },
        "final_prefix": {
            "q": rows[-1][0],
            "margin_binary64": format(final_margin, ".17g"),
        },
        "maximum_margin_binary64": format(maximum, ".17g"),
        "proof_boundary": (
            "Exact integer prime-power enumeration plus ordinary binary64 ranking "
            "and one same-formula mpmath replay. This is not directed arithmetic, "
            "does not certify all prefixes, and supplies no cofinal theorem."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10_000_000)
    parser.add_argument("--digits", type=int, default=80)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = scan(args.limit, args.digits)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
