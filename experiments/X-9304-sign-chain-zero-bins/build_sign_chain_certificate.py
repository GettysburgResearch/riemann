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
COUNT_SCHEMA = "riemann.x5604-slab-discrepancy.v1"


def load_module(name: str, filename: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
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


def exact_integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def count_endpoint(data: dict[str, Any], name: str) -> Fraction:
    raw = data.get(name)
    if not isinstance(raw, dict) or not isinstance(raw.get("fraction"), str):
        raise ValueError(f"count source {name}.fraction is missing")
    return Fraction(raw["fraction"])


def verify_total_count_source(
    path: Path,
    lower: Fraction,
    upper: Fraction,
    total_count: int,
    target: Fraction | None,
) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("total-count source must contain an object")
    if data.get("schema") != COUNT_SCHEMA:
        raise ValueError("total-count source schema mismatch")
    classification = data.get("classification")
    if not isinstance(classification, str) or not classification.startswith("RIGOROUS"):
        raise ValueError("total-count source is not rigorously classified")
    if count_endpoint(data, "a") != lower or count_endpoint(data, "b") != upper:
        raise ValueError("total-count source slab does not match requested slab")
    source_total = exact_integer(
        data.get("N_total_in_slab"), "count_source.N_total_in_slab"
    )
    if source_total != total_count:
        raise ValueError(
            f"total-count source proves {source_total}, not requested {total_count}"
        )
    n_a = data.get("N_a")
    n_b = data.get("N_b")
    if not isinstance(n_a, dict) or not isinstance(n_b, dict):
        raise ValueError("count source endpoint records are missing")
    n_a_integer = exact_integer(n_a.get("integer"), "count_source.N_a.integer")
    n_b_integer = exact_integer(n_b.get("integer"), "count_source.N_b.integer")
    if n_b_integer - n_a_integer != total_count:
        raise ValueError("count source endpoint integers do not reproduce total count")
    if not isinstance(n_a.get("ball"), str) or not isinstance(n_b.get("ball"), str):
        raise ValueError("count source endpoint balls are missing")
    if target is not None:
        target_record = data.get("target")
        if (
            not isinstance(target_record, dict)
            or target_record.get("strictly_inside") is not True
            or Fraction(target_record.get("fraction")) != target
        ):
            raise ValueError("count source target gate does not match requested target")
    return data


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
    target = parse_fraction(args.target) if args.target else None
    if target is not None and not lower < target < upper:
        raise SystemExit("target is not strictly inside the slab")

    try:
        count_source = verify_total_count_source(
            args.total_count_source,
            lower,
            upper,
            args.total_count,
            target,
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        raise SystemExit(f"invalid total-count source: {error}") from error

    guide = [
        decimal_fraction(line)
        for line in args.guide.read_text(encoding="utf-8").splitlines()
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
    if not ladder or ladder[0] < 64:
        raise SystemExit("precision ladder must begin at 64 bits or more")
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
            + "\n",
            encoding="utf-8",
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
    count_digest = sha256_file(args.total_count_source)
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
            "total_count_sha256": count_digest,
            "sign_table_sha256": sign_digest,
            "total_count_source": str(args.total_count_source),
            "total_count_schema": count_source["schema"],
            "total_count_N_a": count_source["N_a"]["integer"],
            "total_count_N_b": count_source["N_b"]["integer"],
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
    if target is not None:
        data["target_ordinate"] = CHECKER.fj(target)
    verification = CHECKER.verify(data)
    data["initial_verification"] = {
        "verdict": verification["verdict"],
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
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
