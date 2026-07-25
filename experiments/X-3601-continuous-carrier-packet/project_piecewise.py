#!/usr/bin/env python3
"""Exact rational Legendre-energy ledger for a dyadic D-0801 finalist."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Any


def canonical_sha(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def parse_vector(data: dict[str, Any]) -> tuple[list[Fraction], list[Fraction], str]:
    raw = data.get("dyadic_vector", data.get("vector", data))
    if not isinstance(raw, dict):
        raise ValueError("dyadic vector object required")
    bits = raw.get("scale_bits")
    real = raw.get("real_numerators")
    imag = raw.get("imag_numerators")
    if (
        isinstance(bits, bool)
        or not isinstance(bits, int)
        or bits < 0
        or not isinstance(real, list)
        or not isinstance(imag, list)
        or len(real) != len(imag)
        or not real
        or any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag)
    ):
        raise ValueError("malformed dyadic vector")
    denominator = 1 << bits
    canonical = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    return (
        [Fraction(x, denominator) for x in real],
        [Fraction(x, denominator) for x in imag],
        canonical_sha(canonical),
    )


def endpoint_legendre(max_degree: int, x: Fraction) -> list[Fraction]:
    values = [Fraction(1)]
    if max_degree == 0:
        return values
    values.append(x)
    for n in range(1, max_degree):
        values.append(((2 * n + 1) * x * values[n] - n * values[n - 1]) / (n + 1))
    return values


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def project(data: dict[str, Any], max_degree: int) -> dict[str, Any]:
    if max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    real, imag, vector_sha = parse_vector(data)
    cells = len(real)
    norm_squared = sum(r * r + i * i for r, i in zip(real, imag))
    if norm_squared == 0:
        raise ValueError("vector must be nonzero")

    endpoints = [Fraction(-1) + Fraction(2 * j, cells) for j in range(cells + 1)]
    values = [endpoint_legendre(max_degree + 1, x) for x in endpoints]
    cumulative = Fraction(0)
    rows = []
    for n in range(max_degree + 1):
        sum_real = Fraction(0)
        sum_imag = Fraction(0)
        for j in range(cells):
            if n == 0:
                integral = Fraction(2, cells)
            else:
                upper = (values[j + 1][n + 1] - values[j + 1][n - 1]) / (2 * n + 1)
                lower = (values[j][n + 1] - values[j][n - 1]) / (2 * n + 1)
                integral = upper - lower
            sum_real += real[j] * integral
            sum_imag += imag[j] * integral
        energy = Fraction(cells * (2 * n + 1), 4) * (
            sum_real * sum_real + sum_imag * sum_imag
        ) / norm_squared
        cumulative += energy
        if cumulative > 1:
            raise ArithmeticError("captured energy exceeds exact unit norm")
        rows.append(
            {
                "degree": n,
                "mode_energy": fraction_json(energy),
                "captured_energy": fraction_json(cumulative),
                "tail_energy": fraction_json(1 - cumulative),
            }
        )
    return {
        "schema": "riemann.piecewise-legendre-energy.v1",
        "cells": cells,
        "maximum_degree": max_degree,
        "vector_sha256": vector_sha,
        "vector_norm_squared": fraction_json(norm_squared),
        "degrees": rows,
        "warning": (
            "This exact projection ledger quantifies representation energy only. "
            "It does not transfer or certify a Weil sign."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("--max-degree", type=int, default=32)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.vector.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("vector file must contain a JSON object")
    result = project(data, args.max_degree)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
