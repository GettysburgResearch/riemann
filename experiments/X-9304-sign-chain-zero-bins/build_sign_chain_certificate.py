#!/usr/bin/env python3
"""Build a production saturated Hardy-Z sign-chain certificate.

Approximate guide zeros choose sample locations only. Every accepted sample sign
is a directed python-flint/Arb interval at an exact dyadic ordinate. A wrong
guide can lose alternations but cannot manufacture one.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import multiprocessing as multiprocessing
import platform
import sys
import time
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


def load_module(name: str, filename: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CHECKER = load_module("verify_sign_chain", "verify_sign_chain.py")
REFINER = load_module("refine_hardy_z_bins", "refine_hardy_z_bins.py")


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def decimal_fraction(text: str) -> Fraction:
    return Fraction(Decimal(text.strip()))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def nearest_dyadic(value: Fraction, bits: int) -> Fraction:
    scale = 1 << bits
    scaled = value * scale
    quotient, remainder = divmod(scaled.numerator, scaled.denominator)
    twice_remainder = 2 * remainder
    if twice_remainder > scaled.denominator or (
        twice_remainder == scaled.denominator and quotient & 1
    ):
        quotient += 1
    return Fraction(quotient, scale)


def sample_points(
    guide: list[Fraction], lower: Fraction, upper: Fraction, bits: int
) -> list[Fraction]:
    inside = sorted(value for value in guide if lower < value < upper)
    if not inside:
        raise ValueError("guide has no ordinates inside the slab")
    midpoints = [(lower + inside[0]) / 2]
    midpoints.extend((left + right) / 2 for left, right in zip(inside, inside[1:]))
    midpoints.append((inside[-1] + upper) / 2)
    points = [nearest_dyadic(value, bits) for value in midpoints]
    if any(not lower < value < upper for value in points):
        raise ValueError("rounded sample left the open slab")
    if any(left >= right for left, right in zip(points, points[1:])):
        raise ValueError("rounded samples collide; increase --bits")
    return points


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--guide", type=Path, required=True)
    parser.add_argument("--total-count-source", type=Path, required=True)
    parser.add_argument("--slab-lower", required=True)
    parser.add_argument("--slab-upper", required=True)
    parser.add_argument("--total-count", type=int, required=True)
    parser.add_argument("--target")
    parser.add_argument("--bits", type=int, default=30)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--precision-ladder", default="96,160,256,448")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.total_count < 1 or args.bits < 1 or args.workers < 1:
        raise SystemExit("positive total count, bits, and workers are required")
    lower = parse_fraction(args.slab_lower)
    upper = parse_fraction(args.slab_upper)
    if not lower < upper:
        raise SystemExit("slab endpoints are reversed")

    guide = [
        decimal_fraction(line)
        for line in args.guide.read_text().splitlines()
        if line.strip()
    ]
    points = sample_points(guide, lower, upper, args.bits)
    if len(points) != args.total_count + 1:
        raise SystemExit(
            f"guide generated {len(points)} samples; "
            f"expected total_count+1={args.total_count + 1}"
        )

    ladder = tuple(
        sorted(
            {
                int(piece)
                for piece in args.precision_ladder.split(",")
                if piece.strip()
            }
        )
    )
    tasks = [
        (index, point.numerator, point.denominator, ladder)
        for index, point in enumerate(points)
    ]
    started = time.time()
    rows: list[dict[str, Any]] = []
    with multiprocessing.Pool(args.workers) as pool:
        for done, row in enumerate(
            pool.imap_unordered(REFINER.evaluate_one, tasks, chunksize=1), 1
        ):
            rows.append(row)
            if done % 25 == 0 or done == len(tasks):
                print(
                    json.dumps(
                        {
                            "done": done,
                            "total": len(tasks),
                            "elapsed_seconds": time.time() - started,
                        }
                    ),
                    flush=True,
                )
    rows.sort(key=lambda row: row["bin_index"])
    unresolved = [row for row in rows if "unresolved" in row]
    if unresolved:
        args.output.write_text(
            json.dumps(
                {
                    "verdict": "INCOMPLETE_UNRESOLVED_SIGNS",
                    "unresolved": unresolved,
                },
                indent=2,
            )
            + "\n"
        )
        return 1

    samples = [
        {
            "t": row["t"],
            "z_interval": row["z_interval"],
            "producer_precision_bits": row["precision_bits"],
        }
        for row in rows
    ]
    semantic_samples = [
        {"t": row["t"], "z_interval": row["z_interval"]} for row in rows
    ]
    sign_digest = CHECKER.canonical_sha(semantic_samples)
    data: dict[str, Any] = {
        "schema": CHECKER.SCHEMA,
        "classification": CHECKER.PRODUCTION,
        "slab": {"lower": CHECKER.fj(lower), "upper": CHECKER.fj(upper)},
        "total_count_interval": {
            "lower": CHECKER.fj(Fraction(args.total_count)),
            "upper": CHECKER.fj(Fraction(args.total_count)),
        },
        "gates": {
            "total_count_status": "CERTIFIED_TOTAL_ZETA_ZERO_COUNT",
            "sign_status": "CERTIFIED_HARDY_Z_INTERVALS",
            "total_count_sha256": sha256_file(args.total_count_source),
            "sign_table_sha256": sign_digest,
            "total_count_source": str(args.total_count_source),
            "guide_sha256": sha256_file(args.guide),
        },
        "samples": samples,
        "refinements": [],
        "producer": {
            "name": "build_sign_chain_certificate.py",
            "python": platform.python_version(),
            "guide": str(args.guide),
            "bits": args.bits,
            "workers": args.workers,
            "precision_ladder": list(ladder),
            "elapsed_seconds": time.time() - started,
        },
    }
    if args.target:
        data["target_ordinate"] = CHECKER.fj(parse_fraction(args.target))
    verification = CHECKER.verify(data)
    data["initial_verification"] = {
        "verdict": verification["verdict"],
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": verification["verdict"],
                "sample_count": len(samples),
                "certificate_sha256": verification["certificate_sha256"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
