#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

MAGIC = "RIEMANN_D0801_AUTOCORRELATION_V1"
EXPECTED_NORMALIZATION = "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be"


class BindingError(ValueError):
    pass


def canonical_sha(value: Any) -> str:
    text = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def load_vector(path: Path) -> tuple[dict[str, Any], list[int], list[int], int, str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BindingError(f"cannot read vector: {exc}") from exc
    if not isinstance(data, dict):
        raise BindingError("vector root must be an object")
    raw = data.get("dyadic_vector", data.get("vector"))
    if not isinstance(raw, dict):
        raise BindingError("dyadic_vector/vector missing")
    bits = raw.get("scale_bits")
    real = raw.get("real_numerators")
    imag = raw.get("imag_numerators")
    if isinstance(bits, bool) or not isinstance(bits, int) or bits < 0:
        raise BindingError("bad scale_bits")
    if (
        not isinstance(real, list)
        or not isinstance(imag, list)
        or not real
        or len(real) != len(imag)
        or any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag)
    ):
        raise BindingError("bad vector numerator arrays")
    canonical = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    return data, real, imag, bits, canonical_sha(canonical)


def parse_manifest(path: Path) -> tuple[dict[str, str], list[tuple[int, int]], str]:
    try:
        raw_bytes = path.read_bytes()
        text = raw_bytes.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise BindingError(f"cannot read manifest: {exc}") from exc
    tokens = text.split()
    if not tokens or tokens[0] != MAGIC:
        raise BindingError("bad manifest magic")
    fields: dict[str, str] = {}
    coefficients: dict[int, tuple[int, int]] = {}
    index = 1
    scalar_fields = {
        "cells",
        "vector_scale_bits",
        "autocorr_scale_bits",
        "vector_sha256",
        "normalization_sha256",
        "parameter_sha256",
        "cutoff_power10",
        "cutoff",
        "carrier_num",
        "carrier_den",
        "segment_size",
        "total_segments",
        "a_count",
    }
    while index < len(tokens):
        key = tokens[index]
        index += 1
        if key in scalar_fields:
            if key in fields or index >= len(tokens):
                raise BindingError(f"duplicate or incomplete field {key}")
            fields[key] = tokens[index]
            index += 1
        elif key == "a":
            if index + 2 >= len(tokens):
                raise BindingError("incomplete a record")
            try:
                lag = int(tokens[index])
                real = int(tokens[index + 1])
                imag = int(tokens[index + 2])
            except ValueError as exc:
                raise BindingError("noninteger a record") from exc
            index += 3
            if lag in coefficients:
                raise BindingError(f"duplicate lag {lag}")
            coefficients[lag] = (real, imag)
        else:
            raise BindingError(f"unrecognized manifest field {key!r}")
    missing = scalar_fields - fields.keys()
    if missing:
        raise BindingError(f"missing fields: {sorted(missing)}")
    try:
        count = int(fields["a_count"])
    except ValueError as exc:
        raise BindingError("a_count must be an integer") from exc
    if set(coefficients) != set(range(count)):
        raise BindingError("lag set is not exactly 0 through a_count-1")
    ordered = [coefficients[index] for index in range(count)]
    return fields, ordered, hashlib.sha256(raw_bytes).hexdigest()


def exact_autocorrelations(real: list[int], imag: list[int]) -> list[tuple[int, int]]:
    cells = len(real)
    values: list[tuple[int, int]] = []
    for lag in range(cells):
        real_sum = 0
        imag_sum = 0
        for index in range(cells - lag):
            r0, i0 = real[index], imag[index]
            r1, i1 = real[index + lag], imag[index + lag]
            real_sum += r0 * r1 + i0 * i1
            imag_sum += r0 * i1 - i0 * r1
        values.append((real_sum, imag_sum))
    values.append((0, 0))
    return values


def verify(
    vector_path: Path,
    manifest_path: Path,
    expected_manifest_sha: str | None = None,
) -> dict[str, Any]:
    _data, real, imag, bits, vector_sha = load_vector(vector_path)
    fields, observed, manifest_sha = parse_manifest(manifest_path)
    expected = exact_autocorrelations(real, imag)
    cells = len(real)

    def integer_field(name: str) -> int:
        try:
            return int(fields[name])
        except ValueError as exc:
            raise BindingError(f"{name} must be an integer") from exc

    if integer_field("cells") != cells:
        raise BindingError("cell count mismatch")
    if integer_field("vector_scale_bits") != bits:
        raise BindingError("vector scale mismatch")
    if integer_field("autocorr_scale_bits") != 2 * bits:
        raise BindingError("autocorrelation scale mismatch")
    if integer_field("a_count") != cells + 1:
        raise BindingError("a_count mismatch")
    if fields["vector_sha256"] != vector_sha:
        raise BindingError("canonical vector digest mismatch")
    if fields["normalization_sha256"] != EXPECTED_NORMALIZATION:
        raise BindingError("normalization digest mismatch")
    if observed != expected:
        for lag, (left, right) in enumerate(zip(observed, expected)):
            if left != right:
                raise BindingError(
                    f"autocorrelation mismatch at lag {lag}: {left} != {right}"
                )
        raise BindingError("autocorrelation length mismatch")
    if observed[-1] != (0, 0):
        raise BindingError("terminal lag must be zero")
    if expected_manifest_sha is not None and manifest_sha != expected_manifest_sha:
        raise BindingError("raw manifest SHA-256 mismatch")

    return {
        "schema": "riemann.d0801-autocorrelation-binding.v1",
        "status": "EXACT_AUTOCORRELATION_BINDING_VERIFIED",
        "cells": cells,
        "vector_scale_bits": bits,
        "autocorrelation_scale_bits": 2 * bits,
        "coefficient_count": len(expected),
        "vector_sha256": vector_sha,
        "manifest_sha256": manifest_sha,
        "normalization_sha256": fields["normalization_sha256"],
        "parameter_sha256": fields["parameter_sha256"],
        "terminal_lag_zero": True,
        "proof_boundary": (
            "Exact integer binding of vector to coefficient manifest only; producer "
            "execution, prime enumeration, directed phases, and final sign remain separate."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vector", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-manifest-sha256")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify(
            args.vector,
            args.manifest,
            args.expected_manifest_sha256,
        )
    except BindingError as exc:
        print(
            json.dumps(
                {
                    "schema": "riemann.d0801-autocorrelation-binding.v1",
                    "status": "REJECTED",
                    "reason": str(exc),
                },
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
