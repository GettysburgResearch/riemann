#!/usr/bin/env python3
"""Independent directed replay of X-5606's previously omitted terminal cell."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import math
import platform
import time
from pathlib import Path

from flint import arb, ctx

SCHEMA = "riemann.x5606-terminal-cell-replay.v1"


def prime_powers(limit: int) -> list[tuple[int, int]]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            start = prime * prime
            flags[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    out: list[tuple[int, int]] = []
    for prime in range(2, limit + 1):
        if flags[prime]:
            value = prime
            while value <= limit:
                out.append((value, prime))
                value *= prime
    out.sort()
    return out


def exact_binary(value: arb) -> dict[str, str | int]:
    mantissa, exponent = value.man_exp()
    mantissa = int(mantissa)
    exponent = int(exponent)
    if exponent >= 0:
        numerator = mantissa << exponent
        denominator = 1
    else:
        numerator = mantissa
        denominator = 1 << (-exponent)
        while numerator and numerator % 2 == 0:
            numerator //= 2
            denominator //= 2
    return {
        "numerator": str(numerator),
        "denominator": str(denominator),
        "mantissa": str(mantissa),
        "exponent": exponent,
    }


class Smooth:
    def __init__(self) -> None:
        self.k1 = (arb(1) / 4).digamma() - arb.pi().log()
        self.constant = arb.pi() ** 2 + 8 * arb.const_catalan()

    def phi(self, t: arb, terms: int = 30) -> arb:
        z = (-2 * t).exp()
        acc, power = arb(0), arb(1)
        for index in range(terms):
            acc += power / ((arb(index) + arb(1) / 4) ** 2)
            power *= z
        tail = power / (((arb(terms) + arb(1) / 4) ** 2) * (1 - z))
        return acc + tail.union(arb(0))

    def value(self, t: arb) -> arb:
        return (
            4 * ((t / 2).exp() + (-t / 2).exp() - 2)
            + (t / 2) * self.k1
            + (self.constant - (-t / 2).exp() * self.phi(t)) / 4
        )

    def derivative(self, t: arb, terms: int = 30) -> arb:
        acc = arb(0)
        for index in range(terms):
            k = 4 * index + 1
            acc += 2 * (-(arb(k) * t) / 2).exp() / k
        k = 4 * terms + 1
        tail = (-(arb(k) * t) / 2).exp() / (2 * (1 - (-2 * t).exp()))
        return (
            2 * ((t / 2).exp() - (-t / 2).exp())
            + self.k1 / 2
            + acc
            + tail.union(arb(0))
        )


def replay(cutoff: int, precision: int) -> dict[str, object]:
    if cutoff < 2:
        raise ValueError("cutoff must be at least 2")
    ctx.prec = precision
    started = time.time()
    manifest = prime_powers(cutoff)
    if not manifest:
        raise ValueError("prime-power manifest is empty")
    last_n = manifest[-1][0]
    if last_n >= cutoff:
        raise ValueError("the requested cutoff has no omitted terminal cell")

    p0, p1 = arb(0), arb(0)
    for value, prime in manifest:
        knot = arb(value).log()
        weight = arb(prime).log() / arb(value).sqrt()
        p0 += weight
        p1 += weight * knot

    left = arb(last_n).log()
    right = arb(cutoff).log()
    midpoint = (left + right) / 2
    smooth = Smooth()
    psi_mid = smooth.value(midpoint) - p0 * midpoint + p1
    derivative_mid = smooth.derivative(midpoint) - p0
    tangent_lower = psi_mid + (
        derivative_mid * (left - midpoint)
    ).min(derivative_mid * (right - midpoint))

    result: dict[str, object] = {
        "schema": SCHEMA,
        "classification": (
            "DIRECTED_TERMINAL_CELL_CONTROL; same Arb library and analytic "
            "formula as X-5606, independently structured prime manifest and "
            "terminal-only accumulation"
        ),
        "environment": {
            "python": platform.python_version(),
            "python_flint": importlib.metadata.version("python-flint"),
            "precision_bits": precision,
        },
        "cutoff": cutoff,
        "prime_power_count": len(manifest),
        "last_prime_power": last_n,
        "terminal_cell": {
            "left": f"log({last_n})",
            "right": f"log({cutoff})",
            "left_ball": str(left),
            "right_ball": str(right),
            "width_ball": str(right - left),
        },
        "psi_mid_ball": str(psi_mid),
        "derivative_mid_ball": str(derivative_mid),
        "tangent_lower_ball": str(tangent_lower),
        "tangent_lower_exact_binary": {
            "lower": exact_binary(tangent_lower.lower()),
            "upper": exact_binary(tangent_lower.upper()),
        },
        "certified_positive": bool(tangent_lower > 0),
        "elapsed_seconds": time.time() - started,
        "proof_boundary": (
            "This closes only the terminal cell omitted by X-5606 v1. It does "
            "not independently reproduce the preceding cells, Suzuki's RH "
            "equivalence, D-9501 normalization, or the Arb library."
        ),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int, default=10**7)
    parser.add_argument("--prec", type=int, default=128)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = replay(args.cutoff, args.prec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["certified_positive"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
