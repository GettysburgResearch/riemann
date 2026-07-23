#!/usr/bin/env python3
"""Verify a frozen vector, exact norm, autocorrelations, digest, and rounding bound."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from exact_vector import (
    parse_vector,
    norm_numerator,
    autocorrelation_numerators,
    target_rounding_bound,
)


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def verify(path: Path, operator_norm_upper: int) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    cells, bits, real, imag, digest = parse_vector(data)
    norm_num = norm_numerator(real, imag)
    auto_real, auto_imag = autocorrelation_numerators(real, imag)
    if auto_real[0] != norm_num or auto_imag[0] != 0:
        raise ValueError("lag-zero autocorrelation must equal the real norm")
    bound = target_rounding_bound(
        cells=cells, bits=bits, operator_norm_upper=operator_norm_upper
    )
    autocorrelation = {
        "imag": auto_imag,
        "real": auto_real,
        "scale_bits": 2 * bits,
    }
    return {
        "verified": True,
        "cells": cells,
        "scale_bits": bits,
        "vector_sha256": digest,
        "norm_squared": fraction_json(Fraction(norm_num, 1 << (2 * bits))),
        "autocorrelation_scale_bits": 2 * bits,
        "autocorrelation_sha256": hashlib.sha256(
            json.dumps(
                autocorrelation, sort_keys=True, separators=(",", ":")
            ).encode()
        ).hexdigest(),
        "rayleigh_rounding_bound": fraction_json(bound),
        "rayleigh_rounding_bound_decimal": float(bound),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("--operator-norm-upper", type=int, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            verify(args.vector, args.operator_norm_upper),
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
