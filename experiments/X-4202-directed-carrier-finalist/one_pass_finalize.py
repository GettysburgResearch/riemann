#!/usr/bin/env python3
"""Checkpoint and finalize the one-pass directed carrier coefficient stream.

The historical c=10^11 discovery vector was not committed.  L-2812 permits a
replacement proof path: first produce simultaneous directed boxes for all
Toeplitz lags, then choose and freeze an exact vector, and finally contract the
same boxes.  This program implements the exact post-processing layer.

Checkpoint mode accepts any nonoverlapping subset of coefficient shards and
emits a resumable hash/count manifest.  Final mode requires complete contiguous
coverage, exactly one higher-prime-power stream, and the target term counts.
It emits:

* an exact Gaussian-dyadic finalist;
* compact scalar contractions of every coefficient shard;
* the existing X-4202 exact correction composition; and
* ``complete-result.json`` with source-shard provenance.
"""
from __future__ import annotations

import argparse
from decimal import Decimal
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys
from typing import Any, Sequence

import numpy as np

COEFFICIENT_SCHEMA = "riemann.mpfr-toeplitz-box-shard.v1"
CHECKPOINT_SCHEMA = "riemann.mpfr-toeplitz-checkpoint-manifest.v1"
FINALIST_SCHEMA = "riemann.piecewise-carrier-finalist.v1"
SCALAR_SHARD_SCHEMA = "riemann.piecewise-carrier-directed-shard.v1"
TARGET_CUTOFF = 100_000_000_000
TARGET_CELLS = 1024
TARGET_CARRIER = Fraction(94_184_072_727_073, 20)
EXPECTED_PRIME_COUNT = 4_118_054_813
EXPECTED_HIGHER_COUNT = 28_156


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def fraction_json(value: Fraction) -> dict[str, str]:
    value = Fraction(value)
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def interval_json(lower: Fraction, upper: Fraction) -> dict[str, object]:
    lower = Fraction(lower)
    upper = Fraction(upper)
    if lower > upper:
        raise ValueError("reversed interval")
    return {
        "lower": fraction_json(lower),
        "upper": fraction_json(upper),
        "width": fraction_json(upper - lower),
    }


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON root must be an object")
    return value


def hex_fraction(value: Any) -> Fraction:
    if not isinstance(value, str):
        raise ValueError("hex endpoint must be a string")
    return Fraction.from_float(float.fromhex(value))


def parse_lag_boxes(
    value: dict[str, Any],
) -> tuple[list[Fraction], list[Fraction], list[Fraction], list[Fraction]]:
    cells = int(value["cells"])
    rows = value.get("lags")
    if not isinstance(rows, list) or len(rows) != cells:
        raise ValueError("wrong lag count")
    real_lower: list[Fraction] = []
    real_upper: list[Fraction] = []
    imag_lower: list[Fraction] = []
    imag_upper: list[Fraction] = []
    for lag, row in enumerate(rows):
        if not isinstance(row, dict) or int(row.get("lag", -1)) != lag:
            raise ValueError(f"lag order mismatch at {lag}")
        rl = hex_fraction(row["real_lower_hex"])
        ru = hex_fraction(row["real_upper_hex"])
        il = hex_fraction(row["imag_lower_hex"])
        iu = hex_fraction(row["imag_upper_hex"])
        if rl > ru or il > iu:
            raise ValueError(f"reversed lag box at {lag}")
        real_lower.append(rl)
        real_upper.append(ru)
        imag_lower.append(il)
        imag_upper.append(iu)
    return real_lower, real_upper, imag_lower, imag_upper


def inspect_shards(
    paths: Sequence[Path],
    *,
    require_complete: bool,
) -> tuple[dict[str, Any], list[tuple[Path, dict[str, Any]]], dict[str, Any]]:
    if not paths:
        raise ValueError("at least one coefficient shard is required")
    loaded: list[tuple[Path, dict[str, Any]]] = []
    for path in paths:
        value = load_json(path)
        if value.get("schema") != COEFFICIENT_SCHEMA:
            raise ValueError(f"{path}: unsupported coefficient shard schema")
        if int(value.get("ambiguous_lags", -1)) != 0:
            raise ValueError(f"{path}: ambiguous support lag")
        parse_lag_boxes(value)
        loaded.append((path, value))

    reference = loaded[0][1]
    keys = (
        "cutoff",
        "carrier",
        "cells",
        "precision_bits",
        "segment_size",
        "total_segments",
    )
    for path, value in loaded:
        for key in keys:
            if value.get(key) != reference.get(key):
                raise ValueError(f"{path}: parameter mismatch for {key}")
        if int(value["total_terms"]) != (
            int(value["prime_count"]) + int(value["higher_prime_power_count"])
        ):
            raise ValueError(f"{path}: term-count identity failed")

    ordered = sorted(loaded, key=lambda row: int(row[1]["segment_start"]))
    previous_end = -1
    covered_segments = 0
    prime_count = 0
    higher_count = 0
    higher_streams = 0
    source_manifest: list[dict[str, object]] = []
    for path, value in ordered:
        start = int(value["segment_start"])
        end = int(value["segment_end"])
        if not (0 <= start < end <= int(reference["total_segments"])):
            raise ValueError(f"{path}: invalid segment range [{start}, {end})")
        if start < previous_end:
            raise ValueError(f"{path}: overlapping segment range")
        previous_end = end
        covered_segments += end - start
        prime_count += int(value["prime_count"])
        higher_count += int(value["higher_prime_power_count"])
        include_higher = bool(value["include_higher_powers"])
        higher_streams += int(include_higher)
        source_manifest.append(
            {
                "path": str(path),
                "sha256": sha256(path),
                "segment_range": {"start": start, "end": end},
                "include_higher_prime_powers": include_higher,
                "prime_count": int(value["prime_count"]),
                "higher_prime_power_count": int(
                    value["higher_prime_power_count"]
                ),
                "total_prime_power_terms": int(value["total_terms"]),
            }
        )

    complete = (
        covered_segments == int(reference["total_segments"])
        and ordered[0][1]["segment_start"] == 0
        and all(
            int(left[1]["segment_end"]) == int(right[1]["segment_start"])
            for left, right in zip(ordered, ordered[1:])
        )
        and int(ordered[-1][1]["segment_end"])
        == int(reference["total_segments"])
    )
    if higher_streams > 1:
        raise ValueError("more than one higher-prime-power stream")
    if require_complete:
        if not complete:
            raise ValueError("coefficient shards do not provide complete coverage")
        if higher_streams != 1:
            raise ValueError("exactly one higher-prime-power stream is required")
        if (
            int(reference["cutoff"]) == TARGET_CUTOFF
            and int(reference["cells"]) == TARGET_CELLS
        ):
            if prime_count != EXPECTED_PRIME_COUNT:
                raise ValueError(
                    f"target prime count mismatch: {prime_count} "
                    f"!= {EXPECTED_PRIME_COUNT}"
                )
            if higher_count != EXPECTED_HIGHER_COUNT:
                raise ValueError(
                    f"target higher-power count mismatch: {higher_count} "
                    f"!= {EXPECTED_HIGHER_COUNT}"
                )

    checkpoint = {
        "schema": CHECKPOINT_SCHEMA,
        "experiment_id": "X-4202",
        "status": (
            "COMPLETE_DIRECTED_COEFFICIENT_COVERAGE"
            if complete
            else "PARTIAL_DIRECTED_COEFFICIENT_COVERAGE"
        ),
        "parameters": {key: reference[key] for key in keys},
        "coverage": {
            "complete": complete,
            "completed_shards": len(ordered),
            "covered_segments": covered_segments,
            "total_segments": int(reference["total_segments"]),
            "completion_fraction": fraction_json(
                Fraction(covered_segments, int(reference["total_segments"]))
            ),
            "prime_count": prime_count,
            "higher_prime_power_count": higher_count,
            "total_prime_power_terms": prime_count + higher_count,
            "higher_prime_power_streams": higher_streams,
            "manifest": source_manifest,
        },
        "counterexample_candidate": None,
        "warning": (
            "A partial checkpoint has no mathematical sign. Complete coverage "
            "must be post-selected, contracted, and correction-composed."
        ),
    }
    return reference, ordered, checkpoint


def merge_lag_boxes(
    ordered: Sequence[tuple[Path, dict[str, Any]]],
    cells: int,
) -> tuple[list[Fraction], list[Fraction], list[Fraction], list[Fraction]]:
    merged = [[Fraction(0) for _ in range(cells)] for _ in range(4)]
    for _, value in ordered:
        boxes = parse_lag_boxes(value)
        for component in range(4):
            for lag in range(cells):
                merged[component][lag] += boxes[component][lag]
    return merged[0], merged[1], merged[2], merged[3]


def nearest_integer(value: Fraction) -> int:
    quotient, remainder = divmod(value.numerator, value.denominator)
    doubled = 2 * remainder
    if doubled > value.denominator or (
        doubled == value.denominator and quotient & 1
    ):
        quotient += 1
    return quotient


def freeze_from_boxes(
    boxes: tuple[
        list[Fraction], list[Fraction], list[Fraction], list[Fraction]
    ],
    *,
    bits: int,
) -> tuple[dict[str, Any], dict[str, object]]:
    if bits < 53:
        raise ValueError("at least 53 dyadic bits are required")
    real_lower, real_upper, imag_lower, imag_upper = boxes
    cells = len(real_lower)
    midpoint = np.array(
        [
            complex(
                float((real_lower[lag] + real_upper[lag]) / 2),
                float((imag_lower[lag] + imag_upper[lag]) / 2),
            )
            for lag in range(cells)
        ],
        dtype=np.complex128,
    )
    midpoint[0] = midpoint[0].real
    first_row = np.empty(cells, dtype=np.complex128)
    first_row[0] = midpoint[0].real
    first_row[1:] = 0.5 * midpoint[1:]
    matrix = np.empty((cells, cells), dtype=np.complex128)
    for lag in range(cells):
        diagonal = np.arange(cells - lag)
        matrix[diagonal, diagonal + lag] = first_row[lag]
        if lag:
            matrix[diagonal + lag, diagonal] = np.conj(first_row[lag])
    matrix = (matrix + matrix.conj().T) / 2
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    vector = eigenvectors[:, -1]
    pivot = int(np.argmax(np.abs(vector)))
    vector *= np.exp(-1j * np.angle(vector[pivot]))
    if vector[pivot].real < 0:
        vector = -vector

    scale = 1 << bits
    real = [
        nearest_integer(Fraction.from_float(float(value.real)) * scale)
        for value in vector
    ]
    imag = [
        nearest_integer(Fraction.from_float(float(value.imag)) * scale)
        for value in vector
    ]
    canonical = {
        "real_numerators": real,
        "imag_numerators": imag,
        "scale_bits": bits,
    }
    vector_digest = canonical_sha(canonical)
    residual = float(
        np.max(
            np.abs(
                matrix @ vector - float(eigenvalues[-1]) * vector
            )
        )
    )
    discovery = {
        "largest_midpoint_prime_eigenvalue": float(eigenvalues[-1]),
        "residual_inf_norm": residual,
        "pivot": pivot,
        "postselected_from_simultaneous_directed_boxes": True,
        "floating_eigensolve_role": (
            "Selects an exact dyadic vector only; no floating value enters "
            "the final interval."
        ),
    }
    return {
        "real": real,
        "imag": imag,
        "bits": bits,
        "sha256": vector_digest,
    }, discovery


def autocorrelations(
    real: Sequence[int], imag: Sequence[int]
) -> tuple[list[int], list[int]]:
    if len(real) != len(imag):
        raise ValueError("vector component length mismatch")
    real_rows: list[int] = []
    imag_rows: list[int] = []
    for lag in range(len(real)):
        real_sum = 0
        imag_sum = 0
        for index in range(len(real) - lag):
            r0, i0 = real[index], imag[index]
            r1, i1 = real[index + lag], imag[index + lag]
            real_sum += r0 * r1 + i0 * i1
            imag_sum += r0 * i1 - i0 * r1
        real_rows.append(real_sum)
        imag_rows.append(imag_sum)
    return real_rows, imag_rows


def multiply_interval_scalar(
    lower: Fraction, upper: Fraction, scalar: Fraction
) -> tuple[Fraction, Fraction]:
    left = lower * scalar
    right = upper * scalar
    return min(left, right), max(left, right)


def contract_boxes(
    boxes: tuple[
        list[Fraction], list[Fraction], list[Fraction], list[Fraction]
    ],
    *,
    correlation_real: Sequence[int],
    correlation_imag: Sequence[int],
    denominator_power: int,
) -> tuple[Fraction, Fraction]:
    real_lower, real_upper, imag_lower, imag_upper = boxes
    scale = Fraction(1, 1 << denominator_power)
    lower = Fraction(0)
    upper = Fraction(0)
    for lag in range(len(real_lower)):
        components = (
            (
                real_lower[lag],
                real_upper[lag],
                Fraction(correlation_real[lag]) * scale,
            ),
            (
                imag_lower[lag],
                imag_upper[lag],
                -Fraction(correlation_imag[lag]) * scale,
            ),
        )
        for component_lower, component_upper, scalar in components:
            part_lower, part_upper = multiply_interval_scalar(
                component_lower, component_upper, scalar
            )
            lower += part_lower
            upper += part_upper
    return lower, upper


def finalist_document(
    *,
    reference: dict[str, Any],
    vector: dict[str, Any],
    discovery: dict[str, object],
    correlation_real: Sequence[int],
    correlation_imag: Sequence[int],
    source_manifest: Sequence[dict[str, object]],
) -> dict[str, object]:
    bits = int(vector["bits"])
    norm = Fraction(int(correlation_real[0]), 1 << (2 * bits))
    carrier = Fraction(Decimal(str(reference["carrier"])))
    return {
        "schema": FINALIST_SCHEMA,
        "experiment_id": "X-4202",
        "status": "EXACT_DYADIC_FINALIST",
        "parameters": {
            "cutoff": int(reference["cutoff"]),
            "cells": int(reference["cells"]),
            "carrier": fraction_json(carrier),
            "dyadic_bits": bits,
            "autocorrelation_denominator_power": 2 * bits,
        },
        "source": {
            "kind": "postselection from complete simultaneous coefficient boxes",
            "coefficient_shards": list(source_manifest),
        },
        "discovery": discovery,
        "vector_sha256": vector["sha256"],
        "vector": [
            {
                "real_numerator": str(real),
                "imag_numerator": str(imag),
            }
            for real, imag in zip(vector["real"], vector["imag"])
        ],
        "autocorrelations": [
            {
                "real_numerator": str(real),
                "imag_numerator": str(imag),
            }
            for real, imag in zip(correlation_real, correlation_imag)
        ],
        "norm_squared": fraction_json(norm),
        "counterexample_candidate": None,
    }


def scalar_shard_document(
    *,
    path: Path,
    value: dict[str, Any],
    finalist_path: Path,
    finalist_sha256: str,
    finalist: dict[str, Any],
    interval: tuple[Fraction, Fraction],
) -> dict[str, object]:
    start = int(value["segment_start"])
    end = int(value["segment_end"])
    segment_size = int(value["segment_size"])
    cutoff = int(value["cutoff"])
    low = 2 + start * segment_size
    high = min(cutoff + 1, 2 + end * segment_size)
    norm = Fraction(
        int(finalist["norm_squared"]["numerator"]),
        int(finalist["norm_squared"]["denominator"]),
    )
    return {
        "schema": SCALAR_SHARD_SCHEMA,
        "experiment_id": "X-4202",
        "status": "DIRECTED_PRIME_RAYLEIGH_SHARD",
        "parameters": {
            "cutoff": cutoff,
            "cells": int(value["cells"]),
            "carrier": finalist["parameters"]["carrier"],
            "segment_size": segment_size,
            "total_segments": int(value["total_segments"]),
            "precision_bits": int(value["precision_bits"]),
        },
        "finalist": {
            "path": str(finalist_path),
            "sha256": finalist_sha256,
            "norm_squared": interval_json(norm, norm),
        },
        "source_coefficient_shard": {
            "path": str(path),
            "sha256": sha256(path),
        },
        "segment_range": {"start": start, "end": end},
        "integer_coverage": {
            "low_inclusive": low,
            "high_exclusive": high,
        },
        "include_higher_prime_powers": bool(value["include_higher_powers"]),
        "prime_count": int(value["prime_count"]),
        "higher_prime_power_count": int(value["higher_prime_power_count"]),
        "total_prime_power_terms": int(value["total_terms"]),
        "prime_rayleigh_interval": interval_json(*interval),
        "environment": {
            "postprocessor_python": sys.version,
            "postprocessor_platform": platform.platform(),
            "numpy": np.__version__,
        },
        "counterexample_candidate": None,
        "warning": (
            "This exact scalar contraction is one shard. The complete sign "
            "requires coverage merging and the nonprime correction moat."
        ),
    }


def write_checkpoint(paths: Sequence[Path], output: Path) -> dict[str, Any]:
    _, _, checkpoint = inspect_shards(paths, require_complete=False)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(checkpoint, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return checkpoint


def finalize(
    paths: Sequence[Path],
    *,
    output_directory: Path,
    correction_certificate: Path,
    vector_bits: int,
    merge_precision_bits: int,
) -> dict[str, Any]:
    reference, ordered, checkpoint = inspect_shards(
        paths, require_complete=True
    )
    if int(reference["cutoff"]) != TARGET_CUTOFF:
        raise ValueError("one-pass finalization is bound to cutoff 10^11")
    if int(reference["cells"]) != TARGET_CELLS:
        raise ValueError("one-pass finalization is bound to K=1024")
    if Fraction(Decimal(str(reference["carrier"]))) != TARGET_CARRIER:
        raise ValueError("one-pass finalization is bound to the target carrier")

    output_directory.mkdir(parents=True, exist_ok=True)
    merged_boxes = merge_lag_boxes(ordered, TARGET_CELLS)
    vector, discovery = freeze_from_boxes(merged_boxes, bits=vector_bits)
    correlation_real, correlation_imag = autocorrelations(
        vector["real"], vector["imag"]
    )
    finalist = finalist_document(
        reference=reference,
        vector=vector,
        discovery=discovery,
        correlation_real=correlation_real,
        correlation_imag=correlation_imag,
        source_manifest=checkpoint["coverage"]["manifest"],
    )
    finalist_path = output_directory / f"finalist-p{vector_bits}.json"
    finalist_path.write_text(
        json.dumps(finalist, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    finalist_digest = sha256(finalist_path)

    scalar_directory = output_directory / "scalar-shards"
    scalar_directory.mkdir(parents=True, exist_ok=True)
    scalar_paths: list[Path] = []
    for source_path, source in ordered:
        interval = contract_boxes(
            parse_lag_boxes(source),
            correlation_real=correlation_real,
            correlation_imag=correlation_imag,
            denominator_power=2 * vector_bits,
        )
        start = int(source["segment_start"])
        end = int(source["segment_end"])
        scalar_path = scalar_directory / f"shard-{start}-{end}.json"
        scalar = scalar_shard_document(
            path=source_path,
            value=source,
            finalist_path=finalist_path,
            finalist_sha256=finalist_digest,
            finalist=finalist,
            interval=interval,
        )
        scalar_path.write_text(
            json.dumps(scalar, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        scalar_paths.append(scalar_path)

    # Import lazily so checkpointing remains usable before python-flint is
    # installed on a continuation machine.
    import merge as fixed_vector_merge

    result = fixed_vector_merge.merge(
        scalar_paths,
        correction_certificate=correction_certificate,
        precision_bits=merge_precision_bits,
    )
    result["one_pass_provenance"] = {
        "schema": CHECKPOINT_SCHEMA,
        "coefficient_checkpoint": checkpoint,
        "postselection": discovery,
        "vector_sha256": vector["sha256"],
        "finalist_path": str(finalist_path),
        "finalist_sha256": finalist_digest,
        "method": (
            "Complete simultaneous directed Toeplitz boxes followed by "
            "floating selection of an exact dyadic vector and exact box "
            "contraction. The floating eigensolve supplies no interval endpoint."
        ),
    }
    result_path = output_directory / "complete-result.json"
    result_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    checkpoint_path = output_directory / "checkpoint-manifest.json"
    checkpoint_path.write_text(
        json.dumps(checkpoint, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {
        "schema": "riemann.piecewise-carrier-directed-summary.v1",
        "status": result["status"],
        "coverage": result["coverage"],
        "normalized_full_interval": result["normalized_full_interval"],
        "vector_sha256": vector["sha256"],
        "complete_result_path": str(result_path),
        "complete_result_sha256": sha256(result_path),
        "counterexample_candidate": None,
    }
    summary_path = output_directory / "complete-summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    hash_paths = [
        checkpoint_path,
        finalist_path,
        *scalar_paths,
        result_path,
        summary_path,
    ]
    sums_path = output_directory / "SHA256SUMS"
    sums_path.write_text(
        "".join(f"{sha256(path)}  {path}\n" for path in hash_paths),
        encoding="utf-8",
    )
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--checkpoint-output", type=Path)
    parser.add_argument("--checkpoint-only", action="store_true")
    parser.add_argument("--output-directory", type=Path)
    parser.add_argument("--correction-certificate", type=Path)
    parser.add_argument("--vector-bits", type=int, default=96)
    parser.add_argument("--merge-precision-bits", type=int, default=192)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.checkpoint_output is not None:
        checkpoint = write_checkpoint(args.shards, args.checkpoint_output)
        print(
            json.dumps(
                {
                    "status": checkpoint["status"],
                    "coverage": checkpoint["coverage"],
                },
                indent=2,
                sort_keys=True,
            )
        )
    if args.checkpoint_only:
        if args.checkpoint_output is None:
            raise SystemExit("--checkpoint-only requires --checkpoint-output")
        return 0
    if args.output_directory is None or args.correction_certificate is None:
        raise SystemExit(
            "final mode requires --output-directory and "
            "--correction-certificate"
        )
    result = finalize(
        args.shards,
        output_directory=args.output_directory,
        correction_certificate=args.correction_certificate,
        vector_bits=args.vector_bits,
        merge_precision_bits=args.merge_precision_bits,
    )
    print(
        json.dumps(
            {
                "status": result["status"],
                "coverage": result["coverage"],
                "normalized_full_interval": result[
                    "normalized_full_interval"
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
