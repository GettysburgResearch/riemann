#!/usr/bin/env python3
"""Ordinary reconnaissance for T-20804.

The integer prime-power manifest is exact.  The transcendental evaluation is a
binary64 scan plus two mpmath replays; it is not a directed proof producer.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import mpmath as mp

SCHEMA = "riemann.x20808.prime-positive-square-diagonal-recon.v1"


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
        raise RuntimeError("prime powers are not strictly increasing")
    return rows


def manifest_sha(rows: Iterable[tuple[int, int, int]]) -> str:
    digest = hashlib.sha256()
    for q, p, exponent in rows:
        digest.update(f"{q},{p},{exponent}\n".encode("ascii"))
    return digest.hexdigest()


mp.mp.dps = 60
B_FLOAT = float(mp.mpf("0.5") * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi)))
C_FLOAT = float(mp.pi**2 + 8 * mp.catalan)


def a_float(t: float) -> float:
    y = math.exp(t / 2.0)
    tail = 0.0
    for m in range(1, 512):
        d = 4 * m + 1
        term = y ** (-d) / (d * d)
        tail += term
        if term < 1.0e-20:
            break
    return 4.0 * (y - 2.0) + B_FLOAT * t + C_FLOAT / 4.0 - 4.0 * tail


def a_mp(t: mp.mpf) -> mp.mpf:
    b = mp.mpf("0.5") * (mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
    c = mp.pi**2 + 8 * mp.catalan
    y = mp.e ** (t / 2)
    tail = mp.nsum(
        lambda m: y ** (-(4 * m + 1)) / (4 * m + 1) ** 2,
        [1, mp.inf],
    )
    return 4 * (y - 2) + b * t + c / 4 - 4 * tail


def exact_simple_dilation(n: int, a: mp.mpf) -> int:
    """Evaluate ceil(2 log(n)/a), preserving powers of two exactly at a=log(2)/2."""
    if n > 0 and (n & (n - 1)) == 0 and abs(a - mp.log(2) / 2) < mp.mpf("1e-40"):
        return 4 * (n.bit_length() - 1)
    return int(mp.ceil(2 * mp.log(n) / a))


def replay(
    rows: list[tuple[int, int, int]], n: int, a: mp.mpf, digits: int
) -> dict[str, object]:
    mp.mp.dps = digits
    r = exact_simple_dilation(n, a)
    t = 2 * mp.log(n) / r
    square_t = 2 * mp.log(n)
    p_sum = mp.mpf(0)
    q_sum = mp.mpf(0)
    for q, p, _exponent in rows:
        if q > n * n:
            break
        weight = mp.log(p) / mp.sqrt(q)
        p_sum += weight
        q_sum += weight * mp.log(q)
    ramp = square_t * p_sum - q_sum
    a_low = a_mp(t)
    a_square = a_mp(square_t)
    margin = r * r * a_low - a_square + ramp
    return {
        "n": n,
        "r": r,
        "t": mp.nstr(t, digits),
        "exp_t": mp.nstr(mp.e**t, digits),
        "P": mp.nstr(p_sum, digits),
        "Q": mp.nstr(q_sum, digits),
        "positive_prime_ramp": mp.nstr(ramp, digits),
        "A_low": mp.nstr(a_low, digits),
        "r2_A_low": mp.nstr(r * r * a_low, digits),
        "A_square": mp.nstr(a_square, digits),
        "Psi_square": mp.nstr(a_square - ramp, digits),
        "diagonal_margin": mp.nstr(margin, digits),
    }


def scan(limit: int, digits: int) -> dict[str, object]:
    rows = prime_powers(limit)
    if not rows:
        raise RuntimeError("empty prime-power manifest")

    ordinates = [q for q, _p, _exponent in rows]
    cumulative_p: list[float] = []
    cumulative_q: list[float] = []
    p_sum = 0.0
    q_sum = 0.0
    for q, p, _exponent in rows:
        weight = math.log(p) / math.sqrt(q)
        p_sum += weight
        q_sum += weight * math.log(q)
        cumulative_p.append(p_sum)
        cumulative_q.append(q_sum)

    a = math.log(2.0) / 2.0
    n_max = math.isqrt(limit)
    record: dict[str, object] | None = None
    maximum: dict[str, object] | None = None
    final: dict[str, object] | None = None
    all_positive = True
    maximum_base_cutoff = 0.0

    for n in range(2, n_max + 1):
        square_t = 2.0 * math.log(n)
        r = math.ceil(square_t / a)
        t = square_t / r
        maximum_base_cutoff = max(maximum_base_cutoff, math.exp(t))

        index = bisect.bisect_right(ordinates, n * n) - 1
        p_value = cumulative_p[index] if index >= 0 else 0.0
        q_value = cumulative_q[index] if index >= 0 else 0.0
        ramp = square_t * p_value - q_value
        psi_square = a_float(square_t) - ramp
        margin = r * r * a_float(t) - psi_square
        row: dict[str, object] = {
            "n": n,
            "r": r,
            "t": t,
            "margin": margin,
            "positive_prime_ramp": ramp,
            "A_square": a_float(square_t),
            "base_reserve": r * r * a_float(t),
            "Psi_square": psi_square,
        }
        all_positive = all_positive and margin > 0.0
        if record is None or margin < float(record["margin"]):
            record = row
        if maximum is None or margin > float(maximum["margin"]):
            maximum = row
        final = row

    assert record is not None and maximum is not None and final is not None

    def serialize(row: dict[str, object]) -> dict[str, object]:
        return {
            key: format(value, ".17g") if isinstance(value, float) else value
            for key, value in row.items()
        }

    exact_a = mp.log(2) / 2
    return {
        "schema": SCHEMA,
        "classification": "ORDINARY_HIGH_PRECISION_RECONNAISSANCE",
        "prime_power_limit": limit,
        "prime_power_count": len(rows),
        "manifest_sha256": manifest_sha(rows),
        "n_range": [2, n_max],
        "level_count": n_max - 1,
        "base_a": "log(2)/2",
        "all_binary64_margins_positive": all_positive,
        "maximum_base_cutoff_binary64": format(maximum_base_cutoff, ".17g"),
        "record_low_binary64": serialize(record),
        "maximum_binary64": serialize(maximum),
        "final_binary64": serialize(final),
        "record_low_high_precision": replay(rows, int(record["n"]), exact_a, digits),
        "final_high_precision": replay(rows, int(final["n"]), exact_a, digits),
        "proof_boundary": (
            "Exact integer prime-power enumeration plus ordinary binary64 scan "
            "and mpmath replays. No directed interval, no cofinal theorem, and "
            "no RH claim."
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
