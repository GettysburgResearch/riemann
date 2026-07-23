#!/usr/bin/env python3
"""Exact contraction of simultaneous Hermitian Toeplitz coefficient boxes."""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any
from exact_vector import parse_vector, autocorrelation_numerators

SCHEMA = "riemann.toeplitz-coefficient-box.v1"


class BoxError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self):
        if self.lower > self.upper:
            raise BoxError("reversed interval")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def subtract(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, value: Fraction) -> "Interval":
        first = self.lower * value
        second = self.upper * value
        return Interval(min(first, second), max(first, second))


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise BoxError(f"{name} must be an object")
    numerator = raw.get("numerator")
    denominator = raw.get("denominator")
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or denominator <= 0
    ):
        raise BoxError(f"bad rational {name}")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise BoxError(f"{name} must be an object")
    return Interval(
        rational(raw.get("lower"), name + ".lower"),
        rational(raw.get("upper"), name + ".upper"),
    )


def fraction_json(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(value: Interval):
    return {
        "lower": fraction_json(value.lower),
        "upper": fraction_json(value.upper),
    }


def contract(data: dict[str, Any], vector_data: dict[str, Any]):
    if data.get("schema") != SCHEMA:
        raise BoxError("bad schema")
    cells, bits, real, imag, digest = parse_vector(vector_data)
    if data.get("cells") != cells:
        raise BoxError("cell mismatch")
    if data.get("vector_sha256") not in (None, digest):
        raise BoxError("vector digest mismatch")
    lags = data.get("lags")
    if not isinstance(lags, list) or len(lags) != cells:
        raise BoxError("lags must have length cells")

    auto_real, auto_imag = autocorrelation_numerators(real, imag)
    scale = 1 << (2 * bits)
    total = Interval(Fraction(0), Fraction(0))
    for lag, raw in enumerate(lags):
        if not isinstance(raw, dict) or raw.get("lag") != lag:
            raise BoxError(f"bad lag {lag}")
        real_box = interval(raw.get("real_interval"), f"lags[{lag}].real")
        imag_box = interval(raw.get("imag_interval"), f"lags[{lag}].imag")
        if lag == 0 and (imag_box.lower != 0 or imag_box.upper != 0):
            raise BoxError("lag-zero imaginary box must be zero")
        term = real_box.scale(Fraction(auto_real[lag], scale)).subtract(
            imag_box.scale(Fraction(auto_imag[lag], scale))
        )
        total = total.add(term)
    return {
        "schema": SCHEMA,
        "cells": cells,
        "vector_sha256": digest,
        "prime_rayleigh_interval": interval_json(total),
        "strict_positive": total.lower > 0,
        "strict_negative": total.upper < 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("boxes", type=Path)
    parser.add_argument("vector", type=Path)
    args = parser.parse_args()
    result = contract(
        json.loads(args.boxes.read_text(encoding="utf-8")),
        json.loads(args.vector.read_text(encoding="utf-8")),
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
