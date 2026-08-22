#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80

SQRT2 = Decimal(2).sqrt()
P2_COEFF = (
    Decimal(1),
    -(Decimal(2) + SQRT2),
    Decimal(1) + Decimal(2) * SQRT2,
    -SQRT2,
)
DILATIONS = (1, 2, 4, 8)


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


PRIMES = primes_upto(100_000)


def w_coeff(z: Decimal, total_scale: int, midpoint: Decimal):
    """W_z(y/total_scale) as A*x^2+B*x+C, x=sqrt(y), on one cell."""
    t = midpoint / Decimal(total_scale)
    if t < 1:
        return Decimal(0), Decimal(0), Decimal(0)
    scale = Decimal(total_scale)
    return (
        Decimal(16) / scale,
        Decimal(8) * (z - Decimal(3)) / scale.sqrt(),
        (z - Decimal(3)) ** 2,
    )


def k_coeff(z: Decimal, source_scale: int, midpoint: Decimal):
    """K_z(y/source_scale)=P2 W_z(y/source_scale), polynomial in sqrt(y)."""
    out = [Decimal(0), Decimal(0), Decimal(0)]
    for c, d in zip(P2_COEFF, DILATIONS):
        w = w_coeff(z, source_scale * d, midpoint)
        for j in range(3):
            out[j] += c * w[j]
    return tuple(out)


def peval(coeff, x: Decimal) -> Decimal:
    return (coeff[0] * x + coeff[1]) * x + coeff[2]


def finite_budget_certificate(z: Decimal, limit: int):
    ps = [p for p in PRIMES if p <= limit]
    breaks = {1, 2, 4, 8, limit}
    for p in ps:
        for d in DILATIONS:
            if p * d <= limit:
                breaks.add(p * d)
    breaks = sorted(breaks)

    max_value = Decimal(-1)
    max_cell = None
    stationary_points = 0

    for left, right in zip(breaks[:-1], breaks[1:]):
        midpoint = (Decimal(left) + Decimal(right)) / 2
        denominator = k_coeff(z, 1, midpoint)
        numerator = [Decimal(0), Decimal(0), Decimal(0)]

        for p in ps:
            if Decimal(p) > midpoint:
                break
            child = k_coeff(z, p, midpoint)
            rp = Decimal(p).sqrt()
            for j in range(3):
                numerator[j] += child[j] / rp

        # Second labelled copy of 67.
        if midpoint >= 67:
            child = k_coeff(z, 67, midpoint)
            rp = Decimal(67).sqrt()
            for j in range(3):
                numerator[j] += child[j] / rp

        A, B, C = numerator
        a, b, c = denominator

        # Derivative numerator of (Ax^2+Bx+C)/(ax^2+bx+c).
        qa = A * b - a * B
        qb = Decimal(2) * (A * c - a * C)
        qc = B * c - b * C

        lo = Decimal(left).sqrt()
        hi = Decimal(right).sqrt()
        candidates = [lo, hi]

        if abs(qa) > Decimal("1e-70"):
            disc = qb * qb - Decimal(4) * qa * qc
            if disc >= 0:
                sd = disc.sqrt()
                for root in (
                    (-qb - sd) / (Decimal(2) * qa),
                    (-qb + sd) / (Decimal(2) * qa),
                ):
                    if lo < root < hi:
                        candidates.append(root)
                        stationary_points += 1
        elif abs(qb) > Decimal("1e-70"):
            root = -qc / qb
            if lo < root < hi:
                candidates.append(root)
                stationary_points += 1

        for x in candidates:
            den = peval(denominator, x)
            if den <= Decimal("1e-50"):
                continue
            value = peval(tuple(numerator), x) / den
            if value > max_value:
                max_value = value
                max_cell = [left, right, str(x)]

    return {
        "cells": len(breaks) - 1,
        "stationary_points": stationary_points,
        "max_value": str(max_value),
        "max_cell": max_cell,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    cert1 = finite_budget_certificate(Decimal(-1), 1024)
    cert2 = finite_budget_certificate(Decimal("-0.5"), 2048)

    assert Decimal(cert1["max_value"]) < Decimal("0.874777")
    assert Decimal(cert2["max_value"]) < Decimal("0.941359")

    prime_partial = sum(
        Decimal(1) / (Decimal(p) * Decimal(p).sqrt()) for p in PRIMES
    )
    prime_upper = (
        prime_partial
        + Decimal(1) / (Decimal(67) * Decimal(67).sqrt())
        + Decimal(2) / Decimal(100_000).sqrt()
    )
    assert prime_upper < Decimal("0.858")

    tail1 = prime_upper + (Decimal(5) / 3 - 1) * Decimal(2) / Decimal(128).sqrt()
    tail2 = prime_upper + (Decimal(2) - 1) * Decimal(2) / Decimal(256).sqrt()
    assert tail1 < Decimal("0.976")
    assert tail2 < Decimal("0.983")

    # JP2 Q_z = Qf + (2z-3)G + (z^2-1)A.
    for z, expected in [
        (Decimal(-1), (Decimal(1), Decimal(-5), Decimal(0))),
        (Decimal("-0.5"), (Decimal(1), Decimal(-4), Decimal("-0.75"))),
    ]:
        coeff = (Decimal(1), Decimal(2) * z - 3, z * z - 1)
        assert coeff == expected

    # Scope firewall.
    A, G, Q = Decimal(1), Decimal(6), Decimal(30)
    assert Q - 5 * G >= 0
    assert Q - 4 * G - Decimal("0.75") * A >= 0
    assert 5 * A - G < 0

    payload = {
        "schema": "riemann.t102740.filtered-sharp-rays.v1",
        "ray_minus_one": cert1,
        "ray_minus_half": cert2,
        "prime_mass_upper": str(prime_upper),
        "analytic_tail_minus_one": str(tail1),
        "analytic_tail_minus_half": str(tail2),
        "filtered_current_identities": True,
        "full_lorentz_cone_closed": False,
        "flc102730_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102740_FILTERED_SHARP_RAYS",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
