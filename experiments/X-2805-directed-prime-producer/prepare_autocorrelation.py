#!/usr/bin/env python3
"""Prepare exact dyadic autocorrelations for the directed D-0801 producer."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

NORMALIZATION_SHA = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"


def canonical_sha(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def total_segments(cutoff: int, segment_size: int) -> int:
    if cutoff < 2 or segment_size < 1:
        raise ValueError("cutoff >= 2 and segment_size >= 1 are required")
    return (cutoff - 2) // segment_size + 1


def prepare(data: dict[str, Any], cutoff_power10: int, segment_size: int) -> str:
    vector = data.get("dyadic_vector", data.get("vector"))
    if not isinstance(vector, dict):
        raise ValueError("dyadic_vector/vector object required")
    bits = vector.get("scale_bits")
    real = vector.get("real_numerators")
    imag = vector.get("imag_numerators")
    if isinstance(bits, bool) or not isinstance(bits, int) or bits < 0:
        raise ValueError("scale_bits must be a nonnegative integer")
    if (
        not isinstance(real, list)
        or not isinstance(imag, list)
        or len(real) != len(imag)
        or not real
    ):
        raise ValueError("real and imaginary arrays must have the same positive length")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag):
        raise ValueError("vector numerators must be integers")
    if cutoff_power10 < 1 or cutoff_power10 > 19:
        raise ValueError("cutoff_power10 must lie in [1,19]")

    cells = len(real)
    canonical_vector = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    vector_sha = canonical_sha(canonical_vector)

    carrier_raw = data.get("parameters", {}).get("carrier") or data.get("carrier")
    if isinstance(carrier_raw, str):
        carrier_fraction = Fraction(carrier_raw)
        carrier = {
            "numerator": carrier_fraction.numerator,
            "denominator": carrier_fraction.denominator,
        }
    elif isinstance(carrier_raw, dict):
        numerator = carrier_raw.get("numerator")
        denominator = carrier_raw.get("denominator")
        if any(isinstance(x, bool) or not isinstance(x, int) for x in (numerator, denominator)):
            raise ValueError("carrier numerator and denominator must be integers")
        if denominator <= 0 or numerator <= 0:
            raise ValueError("carrier must be positive")
        carrier_fraction = Fraction(numerator, denominator)
        carrier = {
            "numerator": carrier_fraction.numerator,
            "denominator": carrier_fraction.denominator,
        }
    else:
        raise ValueError("carrier missing")

    cutoff = 10**cutoff_power10
    total = total_segments(cutoff, segment_size)
    parameters = {
        "carrier": carrier,
        "cells": cells,
        "cutoff_power10": cutoff_power10,
        "total_segments": total,
    }
    parameter_sha = canonical_sha(parameters)

    autocorrelations: list[tuple[int, int]] = []
    for d in range(cells):
        real_num = 0
        imag_num = 0
        for j in range(cells - d):
            r1, i1 = real[j + d], imag[j + d]
            r0, i0 = real[j], imag[j]
            real_num += r1 * r0 + i1 * i0
            imag_num += i1 * r0 - r1 * i0
        autocorrelations.append((real_num, imag_num))
    autocorrelations.append((0, 0))

    lines = [
        "RIEMANN_D0801_AUTOCORRELATION_V1",
        f"cells {cells}",
        f"vector_scale_bits {bits}",
        f"autocorr_scale_bits {2 * bits}",
        f"vector_sha256 {vector_sha}",
        f"normalization_sha256 {NORMALIZATION_SHA}",
        f"parameter_sha256 {parameter_sha}",
        f"cutoff_power10 {cutoff_power10}",
        f"cutoff {cutoff}",
        f"carrier_num {carrier['numerator']}",
        f"carrier_den {carrier['denominator']}",
        f"segment_size {segment_size}",
        f"total_segments {total}",
        f"a_count {cells + 1}",
    ]
    lines.extend(
        f"a {d} {real_num} {imag_num}"
        for d, (real_num, imag_num) in enumerate(autocorrelations)
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("--cutoff-power10", type=int, required=True)
    parser.add_argument("--segment-size", type=int, default=20_000_000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.vector.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("vector file must contain a JSON object")
    args.output.write_text(
        prepare(data, args.cutoff_power10, args.segment_size), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
