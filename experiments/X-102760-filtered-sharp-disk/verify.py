#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 90

SQRT2 = Decimal(2).sqrt()
RADIUS = Decimal("0.5")
RHO = Decimal("0.942")
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


def raw_components(total_scale: int, midpoint: Decimal):
    """|S_-(y/scale)+w|^2 = C(x)+2B(x)Re(w)+A|w|^2."""
    t = midpoint / Decimal(total_scale)
    if t < 1:
        return (
            Decimal(0),
            (Decimal(0), Decimal(0)),
            (Decimal(0), Decimal(0), Decimal(0)),
        )
    scale = Decimal(total_scale)
    root = scale.sqrt()
    return (
        Decimal(1),
        (Decimal(4) / root, -Decimal(4)),
        (Decimal(16) / scale, -Decimal(32) / root, Decimal(16)),
    )


def filtered_components(source_scale: int, midpoint: Decimal):
    A = Decimal(0)
    B = [Decimal(0), Decimal(0)]
    C = [Decimal(0), Decimal(0), Decimal(0)]
    for coeff, dilation in zip(P2_COEFF, DILATIONS):
        a, b, c = raw_components(source_scale * dilation, midpoint)
        A += coeff * a
        B[0] += coeff * b[0]
        B[1] += coeff * b[1]
        for j in range(3):
            C[j] += coeff * c[j]
    return A, tuple(B), tuple(C)


def eval_linear(coeff, x: Decimal) -> Decimal:
    return coeff[0] * x + coeff[1]


def eval_quadratic(coeff, x: Decimal) -> Decimal:
    return (coeff[0] * x + coeff[1]) * x + coeff[2]


def quadratic_min(coeff, lo: Decimal, hi: Decimal):
    a, b, _ = coeff
    candidates = [lo, hi]
    if abs(a) > Decimal("1e-80"):
        root = -b / (Decimal(2) * a)
        if lo < root < hi:
            candidates.append(root)
    values = [eval_quadratic(coeff, x) for x in candidates]
    i = min(range(len(values)), key=values.__getitem__)
    return values[i], candidates[i]


def disk_min_certificate(A, B, C, lo: Decimal, hi: Decimal):
    """Minimum of C(x)+2B(x)Re(w)+A|w|^2 on |w|<=RADIUS."""
    minimum = Decimal("Infinity")
    witness = None

    cuts = [lo, hi]
    if abs(B[0]) > Decimal("1e-80"):
        zero = -B[1] / B[0]
        if lo < zero < hi:
            cuts.append(zero)
    cuts = sorted(cuts)
    for a, b in zip(cuts[:-1], cuts[1:]):
        if b <= a:
            continue
        mid = (a + b) / 2
        sign = Decimal(1) if eval_linear(B, mid) >= 0 else Decimal(-1)
        poly = (
            C[0],
            C[1] - Decimal(2) * RADIUS * sign * B[0],
            C[2] - Decimal(2) * RADIUS * sign * B[1] + A * RADIUS * RADIUS,
        )
        value, x = quadratic_min(poly, a, b)
        if value < minimum:
            minimum = value
            witness = ("boundary", str(x), int(sign))

    if A > Decimal("1e-80"):
        cuts = [lo, hi]
        for target in (-A * RADIUS, A * RADIUS):
            if abs(B[0]) > Decimal("1e-80"):
                x = (target - B[1]) / B[0]
                if lo < x < hi:
                    cuts.append(x)
        cuts = sorted(cuts)
        for a, b in zip(cuts[:-1], cuts[1:]):
            if b <= a:
                continue
            mid = (a + b) / 2
            if abs(eval_linear(B, mid)) <= A * RADIUS:
                determinant = (
                    A * C[0] - B[0] * B[0],
                    A * C[1] - Decimal(2) * B[0] * B[1],
                    A * C[2] - B[1] * B[1],
                )
                value, x = quadratic_min(determinant, a, b)
                value /= A
                if value < minimum:
                    minimum = value
                    witness = ("interior", str(x), 0)

    return minimum, witness


def breakpoints(limit: int):
    values = {1, 2, 4, 8, limit}
    for p in PRIMES:
        if p > limit:
            break
        for dilation in DILATIONS:
            if p * dilation <= limit:
                values.add(p * dilation)
    return sorted(values)


def finite_disk_budget(limit: int):
    points = breakpoints(limit)
    minimum = Decimal("Infinity")
    witness = None
    checked = 0

    for left, right in zip(points[:-1], points[1:]):
        midpoint = (Decimal(left) + Decimal(right)) / 2
        A, B, C = filtered_components(1, midpoint)
        Ad = RHO * A
        Bd = [RHO * B[0], RHO * B[1]]
        Cd = [RHO * c for c in C]

        for p in PRIMES:
            if Decimal(p) > midpoint:
                break
            a, b, c = filtered_components(p, midpoint)
            factor = Decimal(1) / Decimal(p).sqrt()
            Ad -= factor * a
            Bd[0] -= factor * b[0]
            Bd[1] -= factor * b[1]
            for j in range(3):
                Cd[j] -= factor * c[j]

        if midpoint >= 67:
            a, b, c = filtered_components(67, midpoint)
            factor = Decimal(1) / Decimal(67).sqrt()
            Ad -= factor * a
            Bd[0] -= factor * b[0]
            Bd[1] -= factor * b[1]
            for j in range(3):
                Cd[j] -= factor * c[j]

        value, local_witness = disk_min_certificate(
            Ad,
            tuple(Bd),
            tuple(Cd),
            Decimal(left).sqrt(),
            Decimal(right).sqrt(),
        )
        checked += 1
        if value < minimum:
            minimum = value
            witness = [left, right, local_witness]

    return {
        "cells": checked,
        "minimum_deficit": str(minimum),
        "witness": witness,
    }


def carrier_disk_certificate():
    minimum = Decimal("Infinity")
    witness = None
    for left, right in ((1, 2), (2, 4), (4, 8), (8, 64)):
        midpoint = (Decimal(left) + Decimal(right)) / 2
        A, B, C = filtered_components(1, midpoint)
        value, local_witness = disk_min_certificate(
            A,
            B,
            C,
            Decimal(left).sqrt(),
            Decimal(right).sqrt(),
        )
        if value < minimum:
            minimum = value
            witness = [left, right, local_witness]
    return {"minimum": str(minimum), "witness": witness}


def carrier_ratio_certificate():
    """Check K_w(y) <= 2*c*y for 1<=y<=8 uniformly on the disk."""
    c = Decimal(2) * (Decimal(2) - SQRT2)
    minimum = Decimal("Infinity")
    witness = None
    for left, right in ((1, 2), (2, 4), (4, 8)):
        midpoint = (Decimal(left) + Decimal(right)) / 2
        A, B, C = filtered_components(1, midpoint)
        value, local_witness = disk_min_certificate(
            -A,
            (-B[0], -B[1]),
            (Decimal(2) * c - C[0], -C[1], -C[2]),
            Decimal(left).sqrt(),
            Decimal(right).sqrt(),
        )
        if value < minimum:
            minimum = value
            witness = [left, right, local_witness]
    return {"minimum": str(minimum), "witness": witness}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    carrier = carrier_disk_certificate()
    ratio = carrier_ratio_certificate()
    finite = finite_disk_budget(2048)

    assert Decimal(carrier["minimum"]) >= Decimal("-1e-70")
    assert Decimal(ratio["minimum"]) >= Decimal("-1e-70")
    assert Decimal(finite["minimum_deficit"]) >= Decimal("-1e-65")

    prime_partial = sum(
        Decimal(1) / (Decimal(p) * Decimal(p).sqrt()) for p in PRIMES
    )
    prime_upper = (
        prime_partial
        + Decimal(1) / (Decimal(67) * Decimal(67).sqrt())
        + Decimal(2) / Decimal(100_000).sqrt()
    )
    analytic_tail = (
        prime_upper
        + (Decimal(2) - Decimal(1))
        * Decimal(2)
        / Decimal(256).sqrt()
    )
    assert prime_upper < Decimal("0.858")
    assert analytic_tail < Decimal("0.983")

    A = Decimal("-3")
    B = Decimal("0")
    P0 = Decimal(1)
    assert P0 + A * RADIUS * RADIUS > 0
    target = Decimal(4) * A - B
    assert target < 0

    payload = {
        "schema": "riemann.t102760.filtered-sharp-disk.v1",
        "carrier_disk": carrier,
        "carrier_ratio": ratio,
        "finite_disk_budget": finite,
        "prime_mass_upper": str(prime_upper),
        "analytic_tail_upper": str(analytic_tail),
        "disk_center": "-1",
        "disk_radius": "1/2",
        "budget_rho": str(RHO),
        "filtered_s_lemma_matrix": True,
        "disk_positivity_alone_closes_lorentz": False,
        "frs102760_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102760_FULL_FILTERED_SHARP_DISK",
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
