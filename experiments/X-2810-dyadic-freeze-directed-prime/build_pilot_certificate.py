#!/usr/bin/env python3
"""Build an exact PR #49 fixed-vector certificate from directed producer output."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

NORMALIZATION_SHA256 = (
    "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"
)


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def interval_json(lower: Fraction, upper: Fraction):
    return {"lower": fraction_json(lower), "upper": fraction_json(upper)}


def canonical_sha256(value) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def parameter_sha(n: int, cells: int, carrier: Fraction, total_segments: int) -> str:
    return canonical_sha256(
        {
            "carrier": fraction_json(carrier),
            "cells": cells,
            "cutoff_power10": n,
            "total_segments": total_segments,
        }
    )


def variation(n: int, cells: int, carrier: Fraction) -> Fraction:
    m = (cells - 1).bit_length()
    log_cells_upper = Fraction(7 * m, 10)
    log_cutoff_lower = 2 * n
    pi_lower = 3
    sqrt_cutoff_upper = isqrt(10**n - 1) + 1
    arch = (
        Fraction(cells, log_cutoff_lower) * (log_cells_upper + 2)
        + 6 * cells
        + 5
        + Fraction(1, log_cutoff_lower)
    ) / (pi_lower * carrier)
    pole = Fraction(
        4 * sqrt_cutoff_upper * cells * cells,
        pi_lower * log_cutoff_lower,
    ) / (carrier * carrier)
    return arch + pole


def exact_from_hex(raw: str) -> Fraction:
    return Fraction.from_float(float.fromhex(raw))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vector", type=Path)
    parser.add_argument("directed", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    vector_data = json.loads(args.vector.read_text(encoding="utf-8"))
    directed = json.loads(args.directed.read_text(encoding="utf-8"))
    n = len(str(directed["cutoff"])) - 1
    if directed["cutoff"] != 10**n:
        raise ValueError("pilot checker requires a decimal-power cutoff")
    carrier = Fraction(94184072727073, 20)
    cells = directed["cells"]
    total_segments = 1
    vector = vector_data["vector"]
    vector_digest = vector_data["vector_sha256"]
    parameter_digest = parameter_sha(n, cells, carrier, total_segments)

    alpha_lower = exact_from_hex(directed["alpha_lower_hex"])
    alpha_upper = exact_from_hex(directed["alpha_upper_hex"])
    prime_lower = exact_from_hex(directed["prime_rayleigh_lower_hex"])
    prime_upper = exact_from_hex(directed["prime_rayleigh_upper_hex"])

    certificate = {
        "schema": "riemann.piecewise-carrier-fixed-vector.v1",
        "normalization_sha256": NORMALIZATION_SHA256,
        "cutoff_power10": n,
        "cells": cells,
        "total_segments": total_segments,
        "carrier": fraction_json(carrier),
        "vector": vector,
        "vector_sha256": vector_digest,
        "parameter_sha256": parameter_digest,
        "alpha_interval": interval_json(alpha_lower, alpha_upper),
        "shards": [
            {
                "segment_start": 0,
                "segment_end": 1,
                "vector_sha256": vector_digest,
                "parameter_sha256": parameter_digest,
                "include_higher_powers": True,
                "prime_count": directed["prime_count"],
                "higher_prime_power_count": directed["higher_prime_power_count"],
                "total_terms": directed["total_terms"],
                "prime_rayleigh_interval": interval_json(
                    prime_lower, prime_upper
                ),
                "producer": {
                    "schema": directed["schema"],
                    "precision_bits": directed["precision_bits"],
                    "directed_endpoint_encoding": (
                        "MPFR interval rounded outward to IEEE-754 binary64 "
                        "then converted exactly"
                    ),
                },
            }
        ],
    }
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    denominator = 1 << vector["scale_bits"]
    norm_squared = sum(
        Fraction(re, denominator) ** 2 + Fraction(im, denominator) ** 2
        for re, im in zip(
            vector["real_numerators"], vector["imag_numerators"]
        )
    )
    leading_lower = norm_squared * alpha_lower - prime_upper
    leading_upper = norm_squared * alpha_upper - prime_lower
    correction = variation(n, cells, carrier) * norm_squared
    full_lower = leading_lower - correction
    full_upper = leading_upper + correction
    print(
        json.dumps(
            {
                "certificate_sha256": hashlib.sha256(
                    args.output.read_bytes()
                ).hexdigest(),
                "normalization_sha256": NORMALIZATION_SHA256,
                "vector_sha256": vector_digest,
                "norm_squared": fraction_json(norm_squared),
                "leading_interval": interval_json(
                    leading_lower, leading_upper
                ),
                "correction_radius": fraction_json(correction),
                "full_interval": interval_json(full_lower, full_upper),
                "certified_positive": full_lower > 0,
                "certified_negative": full_upper < 0,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
