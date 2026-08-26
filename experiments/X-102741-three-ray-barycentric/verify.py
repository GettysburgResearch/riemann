#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80
SQRT2 = Decimal(2).sqrt()
P2 = (Decimal(1), -(Decimal(2) + SQRT2), Decimal(1) + 2 * SQRT2, -SQRT2)
DILATIONS = (1, 2, 4, 8)


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


PRIMES = primes_upto(100000)


def w_coeff(z, scale, midpoint):
    t = midpoint / Decimal(scale)
    if t < 1:
        return (Decimal(0),) * 3
    sc = Decimal(scale)
    return Decimal(16) / sc, Decimal(8) * (z - 3) / sc.sqrt(), (z - 3) ** 2


def k_coeff(z, scale, midpoint):
    out = [Decimal(0)] * 3
    for c, d in zip(P2, DILATIONS):
        term = w_coeff(z, scale * d, midpoint)
        for i in range(3):
            out[i] += c * term[i]
    return tuple(out)


def peval(coeff, x):
    return (coeff[0] * x + coeff[1]) * x + coeff[2]


def finite_certificate(z, limit):
    ps = [p for p in PRIMES if p <= limit]
    breaks = {1, 2, 4, 8, limit}
    for p in ps:
        for d in DILATIONS:
            if p * d <= limit:
                breaks.add(p * d)
    breaks = sorted(breaks)

    maximum = Decimal(-1)
    max_cell = None
    stationary = 0

    for left, right in zip(breaks[:-1], breaks[1:]):
        midpoint = (Decimal(left) + Decimal(right)) / 2
        denominator = k_coeff(z, 1, midpoint)
        numerator = [Decimal(0)] * 3
        for p in ps:
            if Decimal(p) > midpoint:
                break
            child = k_coeff(z, p, midpoint)
            rp = Decimal(p).sqrt()
            for i in range(3):
                numerator[i] += child[i] / rp
        if midpoint >= 67:
            child = k_coeff(z, 67, midpoint)
            rp = Decimal(67).sqrt()
            for i in range(3):
                numerator[i] += child[i] / rp

        A, B, C = numerator
        a, b, c = denominator
        qa = A * b - a * B
        qb = 2 * (A * c - a * C)
        qc = B * c - b * C

        lo = Decimal(left).sqrt()
        hi = Decimal(right).sqrt()
        candidates = [lo, hi]
        if abs(qa) > Decimal("1e-70"):
            disc = qb * qb - 4 * qa * qc
            if disc >= 0:
                sd = disc.sqrt()
                for root in ((-qb - sd) / (2 * qa), (-qb + sd) / (2 * qa)):
                    if lo < root < hi:
                        candidates.append(root)
                        stationary += 1
        elif abs(qb) > Decimal("1e-70"):
            root = -qc / qb
            if lo < root < hi:
                candidates.append(root)
                stationary += 1

        for x in candidates:
            den = peval(denominator, x)
            if den <= Decimal("1e-50"):
                continue
            value = peval(tuple(numerator), x) / den
            if value > maximum:
                maximum = value
                max_cell = [left, right, str(x)]

    return {
        "cells": len(breaks) - 1,
        "stationary_points": stationary,
        "max_value": str(maximum),
        "max_cell": max_cell,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    cert = finite_certificate(Decimal("-1.5"), 2048)
    assert Decimal(cert["max_value"]) < Decimal("0.920011")

    # Rows are coefficients of (Q,G,A).
    Pm = (Decimal(1), Decimal(-6), Decimal("1.25"))
    P0 = (Decimal(1), Decimal(-5), Decimal(0))
    Pp = (Decimal(1), Decimal(-4), Decimal("-0.75"))

    A = tuple(2 * (Pm[i] + Pp[i] - 2 * P0[i]) for i in range(3))
    assert A == (Decimal(0), Decimal(0), Decimal(1))

    G = tuple(A[i] + (Pp[i] - Pm[i]) / 2 for i in range(3))
    assert G == (Decimal(0), Decimal(1), Decimal(0))

    target = tuple(
        Decimal("8.5") * Pm[i] + Decimal("7.5") * Pp[i] - 16 * P0[i]
        for i in range(3)
    )
    assert target == (Decimal(0), Decimal(-1), Decimal(5))

    payload = {
        "schema": "riemann.t102741.three-ray-barycentric.v1",
        "ray_minus_three_halves": cert,
        "three_ray_coordinate_reconstruction": True,
        "common_linear_carrier_coefficient_sum": "0",
        "carrier_recombined_fluctuation_proved": False,
        "flc102740_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102741_THREE_RAY_BARYCENTRIC_RECONSTRUCTION",
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
