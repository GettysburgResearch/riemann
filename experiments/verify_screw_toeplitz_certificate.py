#!/usr/bin/env python3
"""Independent standard-library checker for X-9502 screw certificates.

The checker reconstructs the zero-sum FIR difference vector from the frozen
integer vector, recomputes all autocorrelations with exact Python integers, and
contracts the serialized directed Psi intervals with exact Fractions.  With
``--recount-manifest`` it independently regenerates all primes and prime powers
through the declared cutoff and checks the canonical SHA-256 stream.

The MPFR producer interval and the exact contraction of serialized primitive
rows are independently rounded enclosures of the same quantity.  MPFR
accumulation can make the producer interval wider, while outward decimal
serialization can make the reconstructed interval wider.  Soundness requires
overlap and strict positivity of both, not a preselected containment direction.
The exact serialized contraction is the checker verdict.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

getcontext().prec = 260


def exact_decimal(text: str) -> Fraction:
    return Fraction(Decimal(text))


def sieve_flags(limit: int) -> bytearray:
    if limit < 2:
        raise ValueError("prime cutoff must be at least 2")
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return flags


def manifest_digest(limit: int) -> tuple[int, int, str]:
    flags = sieve_flags(limit)
    digest = hashlib.sha256()
    prime_count = 0
    power_count = 0
    for p in range(2, limit + 1):
        if not flags[p]:
            continue
        prime_count += 1
        q = p
        exponent = 1
        while q <= limit:
            digest.update(q.to_bytes(8, "big"))
            digest.update(p.to_bytes(8, "big"))
            digest.update(exponent.to_bytes(4, "big"))
            power_count += 1
            if q > limit // p:
                break
            q *= p
            exponent += 1
    return prime_count, power_count, digest.hexdigest()


def exact_filter_data(data: dict[str, Any]) -> tuple[list[int], list[int]]:
    n = int(data["matrix_size"])
    numerators = [int(value) for value in data["b_numerators"]]
    if len(numerators) != n:
        raise ValueError("frozen vector length does not equal matrix_size")

    differences = [numerators[0]]
    differences.extend(
        numerators[index] - numerators[index - 1]
        for index in range(1, n)
    )
    differences.append(-numerators[-1])
    if sum(differences) != 0:
        raise ValueError("difference vector is not exactly zero-sum")

    autocorrelations = [
        sum(
            differences[index] * differences[index + lag]
            for index in range(n + 1 - lag)
        )
        for lag in range(1, n + 1)
    ]
    return differences, autocorrelations


def exact_contraction(data: dict[str, Any]) -> tuple[Fraction, Fraction]:
    n = int(data["matrix_size"])
    _, autocorrelations = exact_filter_data(data)
    rows = data["psi_intervals"]
    if len(rows) != n:
        raise ValueError("wrong number of Psi rows")
    if [int(row["k"]) for row in rows] != list(range(1, n + 1)):
        raise ValueError("Psi rows are not contiguous from 1 through matrix_size")

    lower = Fraction(0)
    upper = Fraction(0)
    for correlation, row in zip(autocorrelations, rows):
        coefficient = -2 * correlation
        lo = exact_decimal(row["lo"])
        hi = exact_decimal(row["hi"])
        if lo > hi:
            raise ValueError("reversed Psi interval")
        if coefficient >= 0:
            lower += coefficient * lo
            upper += coefficient * hi
        else:
            lower += coefficient * hi
            upper += coefficient * lo

    denominator = 1 << (2 * int(data["vector_denominator_power"]))
    return lower / denominator, upper / denominator


def decimal_string(value: Fraction) -> str:
    return str(Decimal(value.numerator) / Decimal(value.denominator))


def intervals_overlap(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def interval_relation(
    producer: tuple[Fraction, Fraction], serialized: tuple[Fraction, Fraction]
) -> str:
    if producer[0] <= serialized[0] <= serialized[1] <= producer[1]:
        return "producer_contains_serialized"
    if serialized[0] <= producer[0] <= producer[1] <= serialized[1]:
        return "serialized_contains_producer"
    if intervals_overlap(producer, serialized):
        return "overlap_without_containment"
    return "disjoint"


def nested(outer: tuple[Fraction, Fraction], inner: tuple[Fraction, Fraction]) -> bool:
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def check_exact_cutoff(data: dict[str, Any]) -> None:
    n = int(data["matrix_size"])
    cutoff = int(data["prime_cutoff"])
    step = data.get("step", {})
    if step.get("kind") != "symbolic-log-ratio" or int(step.get("p", 0)) != 2:
        raise ValueError("checker expects h=log(2)/d")
    denominator = int(step.get("denominator", 0))
    if denominator <= 0:
        raise ValueError("invalid step denominator")
    if not cutoff**denominator <= 2**n < (cutoff + 1) ** denominator:
        raise ValueError("prime cutoff is inconsistent with n*log(2)/d")
    expected_rule = f"q^{denominator} <= 2^k at t=k*log(2)/{denominator}"
    if data.get("threshold_rule") != expected_rule:
        raise ValueError("unexpected exact threshold rule")


def verify_one(path: Path, recount: bool) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "riemann.screw.toeplitz-control.v1":
        raise ValueError(f"{path}: unsupported schema")
    if data.get("classification") != "DIRECTED_POSITIVE_CONTROL":
        raise ValueError(f"{path}: unexpected classification")
    if data.get("normalization") != "D-9501":
        raise ValueError(f"{path}: unexpected normalization")
    if data.get("filter_theorem") != "L-9504":
        raise ValueError(f"{path}: unexpected filter theorem")
    if data.get("manifest_order") != "prime-major: p ascending, exponent ascending":
        raise ValueError(f"{path}: unexpected manifest order")
    if data.get("manifest_row_encoding") != "q:u64be || p:u64be || exponent:u32be":
        raise ValueError(f"{path}: unexpected manifest row encoding")
    check_exact_cutoff(data)

    differences, autocorrelations = exact_filter_data(data)
    serialized = exact_contraction(data)
    producer = tuple(map(exact_decimal, data["rayleigh_interval"]))
    if producer[0] > producer[1]:
        raise ValueError(f"{path}: reversed producer Rayleigh interval")
    if not intervals_overlap(producer, serialized):
        raise ValueError(f"{path}: producer and serialized contractions are disjoint")
    if producer[0] <= 0:
        raise ValueError(f"{path}: producer lower endpoint is not positive")
    if serialized[0] <= 0:
        raise ValueError(f"{path}: exact serialized lower endpoint is not positive")
    if data.get("strict_positive") is not True:
        raise ValueError(f"{path}: producer did not mark strict positivity")

    manifest_checked = False
    if recount:
        prime_count, power_count, digest = manifest_digest(int(data["prime_cutoff"]))
        if prime_count != int(data["prime_count"]):
            raise ValueError(f"{path}: prime count mismatch")
        if power_count != int(data["prime_power_count"]):
            raise ValueError(f"{path}: prime-power count mismatch")
        if digest != data["manifest_sha256"]:
            raise ValueError(f"{path}: manifest SHA-256 mismatch")
        manifest_checked = True

    filter_digest = hashlib.sha256()
    for value in differences:
        filter_digest.update(f"c:{value}\n".encode())
    for lag, value in enumerate(autocorrelations, 1):
        filter_digest.update(f"r:{lag}:{value}\n".encode())

    return {
        "path": path.name,
        "precision_bits": int(data["precision_bits"]),
        "manifest_sha256": data["manifest_sha256"],
        "filter_sha256": filter_digest.hexdigest(),
        "producer_rayleigh_interval": data["rayleigh_interval"],
        "serialized_rayleigh_interval": [
            decimal_string(serialized[0]),
            decimal_string(serialized[1]),
        ],
        "enclosure_relation": interval_relation(producer, serialized),
        "producer_lower_positive": True,
        "serialized_lower_positive": True,
        "manifest_recounted": manifest_checked,
        "raw": data,
        "producer_fraction_interval": producer,
        "serialized_fraction_interval": serialized,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path, nargs="+")
    parser.add_argument(
        "--recount-manifest",
        action="store_true",
        help="independently rebuild the highest-precision manifest",
    )
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    ordered_paths = sorted(
        args.certificates,
        key=lambda path: int(json.loads(path.read_text())["precision_bits"]),
    )
    results = [
        verify_one(
            path,
            recount=args.recount_manifest and index == len(ordered_paths) - 1,
        )
        for index, path in enumerate(ordered_paths)
    ]

    reference = results[0]["raw"]
    for result in results[1:]:
        current = result["raw"]
        for key in (
            "normalization",
            "filter_theorem",
            "prime_cutoff",
            "prime_count",
            "prime_power_count",
            "manifest_sha256",
            "step",
            "threshold_rule",
            "matrix_size",
            "vector_denominator_power",
            "smooth_series_terms",
            "b_numerators",
        ):
            if current[key] != reference[key]:
                raise ValueError(f"cross-precision metadata mismatch in {key}")

    for low, high in zip(results, results[1:]):
        if not nested(
            low["producer_fraction_interval"], high["producer_fraction_interval"]
        ):
            raise ValueError("producer Rayleigh intervals fail precision nesting")
        if not nested(
            low["serialized_fraction_interval"], high["serialized_fraction_interval"]
        ):
            raise ValueError("serialized Rayleigh intervals fail precision nesting")
        for low_row, high_row in zip(
            low["raw"]["psi_intervals"], high["raw"]["psi_intervals"]
        ):
            low_interval = (
                exact_decimal(low_row["lo"]),
                exact_decimal(low_row["hi"]),
            )
            high_interval = (
                exact_decimal(high_row["lo"]),
                exact_decimal(high_row["hi"]),
            )
            if not nested(low_interval, high_interval):
                raise ValueError(
                    f"Psi interval at k={low_row['k']} fails precision nesting"
                )

    output = {
        "status": "PASS",
        "verdict": "STRICTLY_POSITIVE_EXACT_SERIALIZED_CONTRACTION",
        "scope": "excludes only the committed exact finite vector",
        "certificate_count": len(results),
        "precision_sequence": [result["precision_bits"] for result in results],
        "all_producer_lower_endpoints_positive": True,
        "all_serialized_lower_endpoints_positive": True,
        "all_primitive_and_contraction_intervals_nested": True,
        "manifest_recounted_at_highest_precision": bool(
            results[-1]["manifest_recounted"]
        ),
        "certificates": [
            {
                key: value
                for key, value in result.items()
                if key
                not in {
                    "raw",
                    "producer_fraction_interval",
                    "serialized_fraction_interval",
                }
            }
            for result in results
        ],
    }
    encoded = json.dumps(output, indent=2, sort_keys=True)
    print(encoded)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(encoded + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
