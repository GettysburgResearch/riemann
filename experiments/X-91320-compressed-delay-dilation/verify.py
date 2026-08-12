#!/usr/bin/env python3
"""Exact regression for the compressed Hardy-delay dilation.

The infinite-dimensional theorem is analytic.  This script verifies its exact
finite model for the model space K_{z^m}: raw Laurent delay ze{-k} splits
orthogonally into the compressed backward shift and the escaped negative-power
prefix.  All arithmetic is over Gaussian integers; no floating point is used.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Tuple

Gaussian = Tuple[int, int]
Vector = Dict[int, Gaussian]


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] + b[0], a[1] + b[1])


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a: Gaussian) -> Gaussian:
    return (a[0], -a[1])


def is_zero(a: Gaussian) -> bool:
    return a == (0, 0)


def clean(v: Vector) -> Vector:
    return {e: z for e, z in v.items() if not is_zero(z)}


def vadd(*vectors: Vector) -> Vector:
    out: Vector = {}
    for v in vectors:
        for e, z in v.items():
            out[e] = gadd(out.get(e, (0, 0)), z)
    return clean(out)


def vscale(c: Gaussian, v: Vector) -> Vector:
    return clean({e: gmul(c, z) for e, z in v.items()})


def shift_raw(v: Vector, delay: int) -> Vector:
    if delay < 0:
        raise ValueError("delay must be nonnegative")
    return {e - delay: z for e, z in v.items()}


def resident(v: Vector) -> Vector:
    return {e: z for e, z in v.items() if e >= 0}


def leakage(v: Vector) -> Vector:
    return {e: z for e, z in v.items() if e < 0}


def compressed_delay(v: Vector, delay: int) -> Vector:
    return resident(shift_raw(v, delay))


def escaped_prefix(v: Vector, delay: int) -> Vector:
    return leakage(shift_raw(v, delay))


def inner(v: Vector, w: Vector) -> Gaussian:
    out: Gaussian = (0, 0)
    for e in set(v).intersection(w):
        out = gadd(out, gmul(gconj(v[e]), w[e]))
    return out


def norm2(v: Vector) -> int:
    z = inner(v, v)
    assert z[1] == 0 and z[0] >= 0
    return z[0]


def packet_sum(vectors: Iterable[Vector], delays: Iterable[int], coeffs: Iterable[Gaussian], part: str) -> Vector:
    pieces = []
    for v, k, c in zip(vectors, delays, coeffs, strict=True):
        raw = shift_raw(v, k)
        if part == "raw":
            chosen = raw
        elif part == "resident":
            chosen = resident(raw)
        elif part == "leakage":
            chosen = leakage(raw)
        else:
            raise ValueError(part)
        pieces.append(vscale(c, chosen))
    return vadd(*pieces)


def deterministic_vectors(m: int) -> list[Vector]:
    vectors: list[Vector] = []
    seeds = (3, 5, 8, 13, 21)
    for j, seed in enumerate(seeds):
        v: Vector = {}
        for e in range(m):
            re = ((seed * (e + 1) + 2 * j) % 11) - 5
            im = ((seed * (e + 3) + 3 * j) % 13) - 6
            if re != 0 or im != 0:
                v[e] = (re, im)
        vectors.append(v)
    return vectors


def run() -> dict:
    m = 17
    vectors = deterministic_vectors(m)
    delays = [0, 1, 3, 5, 8]
    coeffs: list[Gaussian] = [(2, -1), (-1, 3), (4, 1), (-2, -2), (1, 5)]

    pairwise_checks = 0
    for i, (vi, ki) in enumerate(zip(vectors, delays, strict=True)):
        for j, (vj, kj) in enumerate(zip(vectors, delays, strict=True)):
            raw_gram = inner(shift_raw(vi, ki), shift_raw(vj, kj))
            split_gram = gadd(
                inner(compressed_delay(vi, ki), compressed_delay(vj, kj)),
                inner(escaped_prefix(vi, ki), escaped_prefix(vj, kj)),
            )
            if raw_gram != split_gram:
                raise AssertionError(f"pairwise Gram failure at {(i, j)}")
            pairwise_checks += 1

    semigroup_checks = 0
    for v in vectors:
        for k in range(0, 7):
            for ell in range(0, 7):
                lhs = compressed_delay(compressed_delay(v, k), ell)
                rhs = compressed_delay(v, k + ell)
                if lhs != rhs:
                    raise AssertionError(f"semigroup failure at {(k, ell)}")
                if any(e < 0 or e >= m for e in lhs):
                    raise AssertionError("compressed delay left K_{z^m}")
                semigroup_checks += 1

    raw_packet = packet_sum(vectors, delays, coeffs, "raw")
    resident_packet = packet_sum(vectors, delays, coeffs, "resident")
    leakage_packet = packet_sum(vectors, delays, coeffs, "leakage")

    if raw_packet != vadd(resident_packet, leakage_packet):
        raise AssertionError("packet decomposition failure")

    raw_norm = norm2(raw_packet)
    resident_norm = norm2(resident_packet)
    leakage_norm = norm2(leakage_packet)
    if raw_norm != resident_norm + leakage_norm:
        raise AssertionError("packet Pythagorean identity failure")

    counterexample = shift_raw(vectors[1], 3)
    negative_exponents = sorted(e for e in counterexample if e < 0)
    if not negative_exponents:
        raise AssertionError("raw delay unexpectedly preserved the model space")

    return {
        "verdict": "PASS_COMPRESSED_DELAY_DILATION",
        "arithmetic": "exact Gaussian integers; no floating point",
        "finite_model": "K_{z^m}=span{1,z,...,z^(m-1)} inside Laurent l2",
        "dimension_m": m,
        "packet_size": len(vectors),
        "delays": delays,
        "pairwise_cross_gram_identities_checked": pairwise_checks,
        "semigroup_identities_checked": semigroup_checks,
        "raw_delay_counterexample_negative_exponents": negative_exponents,
        "packet_raw_norm_squared": raw_norm,
        "packet_resident_norm_squared": resident_norm,
        "packet_leakage_norm_squared": leakage_norm,
        "pythagorean_identity": raw_norm == resident_norm + leakage_norm,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is None:
        print(text, end="")
    else:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
