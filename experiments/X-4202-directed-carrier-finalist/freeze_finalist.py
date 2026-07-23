#!/usr/bin/env python3
"""Freeze the committed X-0901 carrier finalist as an exact dyadic vector.

The source branch already contains a machine-readable discovery vector and the
complete floating prime coefficient vector.  This script does not trust a file
name or a supplied label: it locates candidate arrays structurally, requires a
unique high-scoring vector, and checks that its ordinary normalized Rayleigh
value reproduces the committed c=10^11 margin before defining the exact dyadic
object.

The ordinary check identifies the intended discovery vector only.  Every later
certificate uses the rounded dyadic coordinates and exact dyadic
autocorrelations emitted here.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_FLOOR, getcontext
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable, Sequence

EXPERIMENT_ID = "X-4202"
SCHEMA = "riemann.piecewise-carrier-finalist.v1"
K = 1024
CUTOFF = 100_000_000_000
CARRIER = Fraction(94_184_072_727_073, 20)
TARGET_MARGIN = 0.00026896626427230785
getcontext().prec = 120


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def decimal_fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean is not a numeric coordinate")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, Decimal):
        return Fraction(value)
    if isinstance(value, float):
        return Fraction(Decimal(repr(value)))
    if isinstance(value, str):
        return Fraction(Decimal(value))
    raise ValueError(f"unsupported numeric coordinate {value!r}")


def numeric_list(value: Any, length: int) -> tuple[Fraction, ...] | None:
    if not isinstance(value, list) or len(value) != length:
        return None
    try:
        return tuple(decimal_fraction(item) for item in value)
    except (ValueError, ArithmeticError):
        return None


def complex_candidates(value: Any, path: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], tuple[tuple[Fraction, Fraction], ...]]]:
    if isinstance(value, dict):
        for real_key, imag_key in (
            ("real", "imag"),
            ("re", "im"),
            ("real_parts", "imag_parts"),
        ):
            real = numeric_list(value.get(real_key), K)
            imag = numeric_list(value.get(imag_key), K)
            if real is not None and imag is not None:
                yield path + (f"{real_key}+{imag_key}",), tuple(zip(real, imag))
        for key, child in value.items():
            yield from complex_candidates(child, path + (str(key),))
    elif isinstance(value, list):
        if len(value) == K:
            real = numeric_list(value, K)
            if real is not None:
                yield path, tuple((item, Fraction(0)) for item in real)
            else:
                parsed: list[tuple[Fraction, Fraction]] = []
                ok = True
                for item in value:
                    try:
                        if isinstance(item, dict):
                            parsed.append(
                                (
                                    decimal_fraction(item.get("real", item.get("re"))),
                                    decimal_fraction(item.get("imag", item.get("im", 0))),
                                )
                            )
                        elif isinstance(item, list) and len(item) == 2:
                            parsed.append((decimal_fraction(item[0]), decimal_fraction(item[1])))
                        else:
                            ok = False
                            break
                    except (ValueError, ArithmeticError):
                        ok = False
                        break
                if ok:
                    yield path, tuple(parsed)
        for index, child in enumerate(value):
            if isinstance(child, (dict, list)):
                yield from complex_candidates(child, path + (str(index),))


def candidate_score(path: Path, json_path: Sequence[str], raw_text: str) -> int:
    text = (str(path) + " " + ".".join(json_path) + " " + raw_text[:20000]).lower()
    score = 0
    for token, weight in (
        ("vector", 14),
        ("eigenvector", 12),
        ("finalist", 10),
        ("leading", 5),
        ("4709203636353.65", 12),
        ("100000000000", 10),
        ("1024", 5),
    ):
        if token in text:
            score += weight
    for token, penalty in (("coefficient", 20), ("moment", 12), ("synthetic", 30)):
        if token in text:
            score -= penalty
    return score


def find_vector(repo: Path) -> tuple[Path, tuple[str, ...], tuple[tuple[Fraction, Fraction], ...]]:
    rows: list[tuple[int, Path, tuple[str, ...], tuple[tuple[Fraction, Fraction], ...]]] = []
    for path in repo.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            raw = path.read_text(encoding="utf-8")
            value = json.loads(raw, parse_float=Decimal)
        except Exception:
            continue
        for json_path, vector in complex_candidates(value):
            score = candidate_score(path.relative_to(repo), json_path, raw)
            rows.append((score, path, json_path, vector))
    if not rows:
        raise RuntimeError("no length-1024 complex vector candidate found")
    rows.sort(key=lambda row: row[0], reverse=True)
    best = rows[0]
    if best[0] < 20:
        raise RuntimeError(f"best vector candidate score is too weak: {best[0]}")
    if len(rows) > 1 and rows[1][0] == best[0]:
        raise RuntimeError(
            "vector discovery is ambiguous: "
            f"{best[1].relative_to(repo)} and {rows[1][1].relative_to(repo)}"
        )
    return best[1], best[2], best[3]


def find_coefficient_arrays(repo: Path) -> list[tuple[Path, tuple[str, ...], tuple[complex, ...]]]:
    rows: list[tuple[Path, tuple[str, ...], tuple[complex, ...]]] = []
    for path in repo.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except Exception:
            continue
        lower = raw.lower()
        if "100000000000" not in lower and "10^11" not in lower:
            continue
        try:
            value = json.loads(raw, parse_float=Decimal)
        except Exception:
            continue
        for json_path, vector in complex_candidates(value):
            joined = (str(path.relative_to(repo)) + "." + ".".join(json_path)).lower()
            if "coefficient" not in joined:
                continue
            rows.append(
                (
                    path,
                    json_path,
                    tuple(complex(float(real), float(imag)) for real, imag in vector),
                )
            )
    return rows


def ordinary_normalized_margin(
    vector: Sequence[tuple[Fraction, Fraction]], coefficients: Sequence[complex]
) -> float:
    values = [complex(float(real), float(imag)) for real, imag in vector]
    norm = sum(abs(value) ** 2 for value in values)
    if norm <= 0:
        raise ValueError("zero source vector")
    prime = coefficients[0].real * norm
    for lag in range(1, K):
        correlation = sum(
            values[index].conjugate() * values[index + lag]
            for index in range(K - lag)
        )
        prime += (coefficients[lag] * correlation).real
    carrier = float(CARRIER)
    alpha = math.log(carrier / (2 * math.pi)) / (2 * math.pi)
    return (alpha * norm - prime) / norm


def identify_coefficients(
    repo: Path,
    vector: Sequence[tuple[Fraction, Fraction]],
) -> tuple[Path, tuple[str, ...], float]:
    candidates = find_coefficient_arrays(repo)
    if not candidates:
        raise RuntimeError("no c=10^11 coefficient array found")
    rows: list[tuple[float, Path, tuple[str, ...], float]] = []
    for path, json_path, coefficients in candidates:
        margin = ordinary_normalized_margin(vector, coefficients)
        rows.append((abs(margin - TARGET_MARGIN), path, json_path, margin))
    rows.sort(key=lambda row: row[0])
    error, path, json_path, margin = rows[0]
    if error >= 1e-10:
        raise RuntimeError(
            "source vector did not reproduce the committed target margin: "
            f"margin={margin:.17g}, error={error:.3g}"
        )
    return path, json_path, margin


def nearest_integer(value: Fraction) -> int:
    quotient, remainder = divmod(value.numerator, value.denominator)
    doubled = 2 * remainder
    if doubled > value.denominator or (doubled == value.denominator and quotient & 1):
        quotient += 1
    return quotient


def dyadic_round(value: Fraction, bits: int) -> int:
    return nearest_integer(value * (1 << bits))


def fraction_json(value: Fraction) -> dict[str, str]:
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def freeze(
    repo: Path,
    *,
    bits: int,
) -> dict[str, object]:
    if bits < 53:
        raise ValueError("at least 53 dyadic bits are required")
    source_path, json_path, source_vector = find_vector(repo)
    coefficient_path, coefficient_json_path, ordinary_margin = identify_coefficients(
        repo, source_vector
    )
    real = [dyadic_round(value[0], bits) for value in source_vector]
    imag = [dyadic_round(value[1], bits) for value in source_vector]
    if not any(real) and not any(imag):
        raise RuntimeError("rounded vector vanished")

    correlations: list[dict[str, str]] = []
    for lag in range(K):
        real_sum = 0
        imag_sum = 0
        for index in range(K - lag):
            r0, i0 = real[index], imag[index]
            r1, i1 = real[index + lag], imag[index + lag]
            real_sum += r0 * r1 + i0 * i1
            imag_sum += r0 * i1 - i0 * r1
        correlations.append(
            {"real_numerator": str(real_sum), "imag_numerator": str(imag_sum)}
        )

    norm = Fraction(int(correlations[0]["real_numerator"]), 1 << (2 * bits))
    max_coordinate_error = Fraction(1, 1 << (bits + 1))
    l2_error_squared = Fraction(2 * K, 1 << (2 * bits + 2))
    return {
        "schema": SCHEMA,
        "experiment_id": EXPERIMENT_ID,
        "status": "EXACT_DYADIC_FINALIST",
        "parameters": {
            "cutoff": CUTOFF,
            "cells": K,
            "carrier": fraction_json(CARRIER),
            "dyadic_bits": bits,
            "autocorrelation_denominator_power": 2 * bits,
        },
        "source": {
            "vector_path": str(source_path.relative_to(repo)),
            "vector_json_path": list(json_path),
            "vector_sha256": sha256(source_path),
            "coefficient_path": str(coefficient_path.relative_to(repo)),
            "coefficient_json_path": list(coefficient_json_path),
            "coefficient_sha256": sha256(coefficient_path),
            "ordinary_normalized_margin": format(ordinary_margin, ".17g"),
            "ordinary_target_margin": format(TARGET_MARGIN, ".17g"),
            "warning": "This ordinary check identifies the source vector only; it is not a sign certificate.",
        },
        "rounding": {
            "rule": "nearest dyadic with ties to even, independently on real and imaginary coordinates",
            "maximum_coordinate_component_error": fraction_json(max_coordinate_error),
            "l2_error_squared_upper": fraction_json(l2_error_squared),
        },
        "vector": [
            {"real_numerator": str(r), "imag_numerator": str(i)}
            for r, i in zip(real, imag)
        ],
        "autocorrelations": correlations,
        "norm_squared": fraction_json(norm),
        "counterexample_candidate": None,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--bits", type=int, default=80)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = freeze(args.repo.resolve(), bits=args.bits)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "source": result["source"],
        "norm_squared": result["norm_squared"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
