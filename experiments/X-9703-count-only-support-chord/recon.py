#!/usr/bin/env python3
"""Ordinary high-precision reconnaissance for L-9703 on configured slabs.

This is not a proof producer.  It uses an absolutely convergent Euler product
at support-scaled points in Re(s)>1 and records both the tempting raw chord and
the exact-count-adjusted chord.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp

CONFIG_SCHEMA = "riemann.x9703-certified-slab-configs.v1"


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    raise ValueError(f"{name} must be an integer")


def rational(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    numerator = integer(value.get("numerator"), f"{name}.numerator")
    denominator = integer(value.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise ValueError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def sieve_primes(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [value for value, flag in enumerate(flags) if flag]


def mp_fraction(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def euler_log_zeta(
    s: mp.mpc,
    primes: list[int],
    tolerance: mp.mpf,
) -> tuple[mp.mpc, mp.mpf]:
    total = mp.mpc(0)
    sigma = mp.re(s)
    for prime in primes:
        log_prime = mp.log(prime)
        z = mp.exp(-s * log_prime)
        power = z
        exponent = 1
        while True:
            term = power / exponent
            total += term
            if abs(term) < tolerance:
                break
            exponent += 1
            power *= z
            if exponent > 600:
                raise RuntimeError("Euler factor did not reach the tolerance")
    cutoff = mp.mpf(primes[-1])
    tail = cutoff ** (1 - sigma) / (
        (sigma - 1) * (1 - mp.power(2, -sigma))
    )
    return total, tail


def direct_log_h(
    u: mp.mpf,
    target: mp.mpf,
    primes: list[int],
    tolerance: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    x = mp.sqrt(u)
    s = mp.mpc(mp.mpf("0.5") + x, target)
    if mp.re(s) <= 1:
        raise ValueError("Euler-product reconnaissance requires Re(s)>1")
    log_zeta, tail = euler_log_zeta(s, primes, tolerance)
    value = 2 * (
        -mp.log(2)
        + mp.log(abs(s))
        + mp.log(abs(s - 1))
        - mp.re(s) * mp.log(mp.pi) / 2
        + mp.re(mp.loggamma(s / 2))
        + mp.re(log_zeta)
    )
    return value, tail


def decimal(value: mp.mpf, digits: int = 60) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def screen_slab(
    slab: dict[str, Any],
    alphas: list[Fraction],
    primes: list[int],
    tolerance: mp.mpf,
) -> dict[str, Any]:
    lower = rational(slab.get("lower"), "slab.lower")
    upper = rational(slab.get("upper"), "slab.upper")
    target_fraction = rational(slab.get("target"), "slab.target")
    count = integer(slab.get("total_count"), "slab.total_count")
    if not lower < target_fraction < upper or count < 0:
        raise ValueError("invalid configured slab")
    support_fraction = min(
        (target_fraction - lower) ** 2,
        (upper - target_fraction) ** 2,
    )
    target = mp_fraction(target_fraction)
    support = mp_fraction(support_fraction)
    nodes = [mp_fraction(alpha) * support for alpha in alphas]
    values: list[mp.mpf] = []
    tails: list[mp.mpf] = []
    for node in nodes:
        value, tail = direct_log_h(node, target, primes, tolerance)
        values.append(value)
        tails.append(tail)

    rows: list[dict[str, Any]] = []
    for first, middle, last in itertools.combinations(range(len(nodes)), 3):
        u0, u1, u2 = nodes[first], nodes[middle], nodes[last]
        l1 = mp.log((u1 + support) / (u0 + support))
        l2 = mp.log((u2 + support) / (u0 + support))
        raw = l1 * (values[last] - values[first]) - l2 * (
            values[middle] - values[first]
        )
        phi0 = l1 * mp.log(u2 / u0) - l2 * mp.log(u1 / u0)
        adjusted = raw - count * phi0
        geometry = l1 * l2 * (l2 - l1)
        rows.append(
            {
                "alpha_indices": [first, middle, last],
                "alphas": [str(alphas[index]) for index in (first, middle, last)],
                "raw_chord": decimal(raw),
                "phi0": decimal(phi0),
                "adjusted_chord": decimal(adjusted),
                "geometry_normalized_adjusted": decimal(adjusted / geometry),
            }
        )
    rows.sort(key=lambda row: mp.mpf(row["adjusted_chord"]))
    return {
        "id": slab.get("id"),
        "lower": str(lower),
        "upper": str(upper),
        "target": str(target_fraction),
        "total_count": count,
        "support_gap": str(support_fraction),
        "point_count": len(nodes),
        "row_count": len(rows),
        "minimum_row": rows[0],
        "smallest_rows": rows[:20],
        "raw_negative_rows": sum(mp.mpf(row["raw_chord"]) < 0 for row in rows),
        "adjusted_negative_rows": sum(
            mp.mpf(row["adjusted_chord"]) < 0 for row in rows
        ),
        "maximum_omitted_prime_logzeta_bound": decimal(max(tails), 20),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--prime-cutoff", type=int, default=10000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.dps < 50 or args.prime_cutoff < 100:
        raise SystemExit("use --dps>=50 and --prime-cutoff>=100")
    config = json.loads(args.config.read_text(encoding="utf-8"))
    if not isinstance(config, dict) or config.get("schema") != CONFIG_SCHEMA:
        raise SystemExit("configuration schema mismatch")
    raw_alphas = config.get("alphas")
    raw_slabs = config.get("slabs")
    if not isinstance(raw_alphas, list) or not isinstance(raw_slabs, list):
        raise SystemExit("configuration needs alphas and slabs arrays")
    alphas = sorted(
        {rational(raw, f"alphas[{index}]") for index, raw in enumerate(raw_alphas)}
    )
    if len(alphas) < 3 or any(alpha <= 0 for alpha in alphas):
        raise SystemExit("at least three positive distinct alpha values are required")

    started = time.time()
    mp.mp.dps = args.dps
    primes = sieve_primes(args.prime_cutoff)
    tolerance = mp.power(10, -(args.dps + 10))
    slabs = [
        screen_slab(raw, alphas, primes, tolerance) for raw in raw_slabs
    ]
    result = {
        "schema": "riemann.x9703-four-slab-reconnaissance.v1",
        "classification": "EMPIRICAL_HIGH_PRECISION_NOT_CERTIFIED",
        "environment": {
            "python": platform.python_version(),
            "mpmath": mp.__version__,
            "decimal_digits": args.dps,
        },
        "prime_cutoff": args.prime_cutoff,
        "prime_count": len(primes),
        "alpha_count": len(alphas),
        "slabs": slabs,
        "total_adjusted_negative_rows": sum(
            slab["adjusted_negative_rows"] for slab in slabs
        ),
        "counterexample_candidate": None,
        "elapsed_seconds": time.time() - started,
        "warning": (
            "Ordinary mpmath arithmetic.  The omitted-prime field is not a total "
            "rounding bound, and the configured counts are not recomputed here."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "slabs": [
                    {
                        "id": slab["id"],
                        "minimum_row": slab["minimum_row"],
                        "adjusted_negative_rows": slab[
                            "adjusted_negative_rows"
                        ],
                    }
                    for slab in slabs
                ],
                "elapsed_seconds": result["elapsed_seconds"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
