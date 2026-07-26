#!/usr/bin/env python3
"""Build a saturated Hardy-Z sign-chain certificate from Gram-point sampling.

Gram points and adaptive subdivision are only search heuristics. Every retained
sample sign is a directed python-flint/Arb interval at an exact dyadic ordinate.
Once the number of certified alternations equals the independent exact total
count, the selected alternating subsequence is a proof-grade saturated chain.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import multiprocessing
import platform
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

from mpmath import mp

HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CHECKER = load_module("verify_sign_chain", HERE / "verify_sign_chain.py")
REFINER = load_module("refine_hardy_z_bins", HERE / "refine_hardy_z_bins.py")


class ProducerError(RuntimeError):
    pass


def fraction_json(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


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
    if bits < 1:
        raise ProducerError("dyadic precision must be positive")
    scale = 1 << bits
    scaled = value * scale
    quotient, remainder = divmod(scaled.numerator, scaled.denominator)
    doubled = 2 * remainder
    if doubled > scaled.denominator or (
        doubled == scaled.denominator and quotient & 1
    ):
        quotient += 1
    return Fraction(quotient, scale)


def gram_points(lower: Fraction, upper: Fraction) -> list[Fraction]:
    """Return high-precision approximate Gram points as exact decimal rationals."""

    mp.dps = max(60, max(len(str(abs(lower.numerator))), len(str(abs(upper.numerator)))) + 20)
    a = mp.mpf(lower.numerator) / lower.denominator
    b = mp.mpf(upper.numerator) / upper.denominator

    def theta(value: mp.mpf) -> mp.mpf:
        return (
            value * mp.log(value / (2 * mp.pi)) / 2
            - value / 2
            - mp.pi / 8
            + 1 / (48 * value)
            + 7 / (5760 * value**3)
        )

    def theta_prime(value: mp.mpf) -> mp.mpf:
        return mp.log(value / (2 * mp.pi)) / 2

    theta_a = theta(a)
    theta_b = theta(b)
    first_index = int(mp.floor(theta_a / mp.pi)) + 1
    last_index = int(mp.floor(theta_b / mp.pi))
    output: list[Fraction] = []
    for index in range(first_index, last_index + 1):
        target = mp.mpf(index) * mp.pi
        value = a + (target - theta_a) / theta_prime(a)
        for _ in range(4):
            value -= (theta(value) - target) / theta_prime(value)
        rational = Fraction(mp.nstr(value, 70, strip_zeros=False))
        if lower < rational < upper:
            output.append(rational)
    return sorted(set(output))


def evaluate_points(
    points: list[Fraction],
    cache: dict[Fraction, dict[str, Any]],
    workers: int,
    ladder: tuple[int, ...],
) -> None:
    pending = [point for point in points if point not in cache]
    tasks = [
        (index, point.numerator, point.denominator, ladder)
        for index, point in enumerate(pending)
    ]
    if not tasks:
        return
    with multiprocessing.Pool(workers) as pool:
        for result in pool.imap_unordered(REFINER.evaluate_one, tasks, chunksize=4):
            point = pending[result["bin_index"]]
            cache[point] = result


def decided_rows(
    points: list[Fraction], cache: dict[Fraction, dict[str, Any]]
) -> list[tuple[Fraction, dict[str, Any]]]:
    return [
        (point, cache[point])
        for point in points
        if "unresolved" not in cache[point]
    ]


def count_changes(rows: list[tuple[Fraction, dict[str, Any]]]) -> int:
    return sum(
        left[1]["sign"] != right[1]["sign"]
        for left, right in zip(rows, rows[1:])
    )


def alternating_subsequence(
    rows: list[tuple[Fraction, dict[str, Any]]]
) -> list[tuple[Fraction, dict[str, Any]]]:
    if not rows:
        return []
    selected = [rows[0]]
    for row in rows[1:]:
        if row[1]["sign"] != selected[-1][1]["sign"]:
            selected.append(row)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slab-lower", required=True)
    parser.add_argument("--slab-upper", required=True)
    parser.add_argument("--total-count", type=int, required=True)
    parser.add_argument("--total-count-source", type=Path, required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--bits", type=int, default=34)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--max-rounds", type=int, default=8)
    parser.add_argument("--precision-ladder", default="128,192,256,384,512,768")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    lower = Fraction(args.slab_lower)
    upper = Fraction(args.slab_upper)
    target = Fraction(args.target)
    if not lower < target < upper:
        raise SystemExit("target must lie strictly inside the slab")
    if args.total_count < 1 or args.bits < 1 or args.workers < 1:
        raise SystemExit("positive total count, bits, and workers are required")
    if args.max_rounds < 0:
        raise SystemExit("max rounds must be nonnegative")
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

    started = time.time()
    approximate_gram = gram_points(lower, upper)
    if not approximate_gram:
        raise SystemExit("no Gram points found inside the slab")
    points = sorted(
        {
            nearest_dyadic(value, args.bits)
            for value in approximate_gram
            if lower < value < upper
        }
    )
    points.extend(
        [
            nearest_dyadic((lower + points[0]) / 2, args.bits),
            nearest_dyadic((points[-1] + upper) / 2, args.bits),
        ]
    )
    points = sorted({point for point in points if lower < point < upper})

    cache: dict[Fraction, dict[str, Any]] = {}
    rounds: list[dict[str, Any]] = []
    for round_index in range(args.max_rounds + 1):
        evaluate_points(points, cache, args.workers, ladder)
        unresolved = [point for point in points if "unresolved" in cache[point]]
        decided = decided_rows(points, cache)
        changes = count_changes(decided)
        rounds.append(
            {
                "round": round_index,
                "sample_count": len(points),
                "decided_count": len(decided),
                "unresolved_count": len(unresolved),
                "certified_changes": changes,
                "elapsed_seconds": time.time() - started,
            }
        )
        print(json.dumps(rounds[-1], sort_keys=True), flush=True)
        if not unresolved and changes == args.total_count:
            break
        if changes > args.total_count:
            raise ProducerError(
                "certified sign changes exceed the independent total count"
            )
        if round_index == args.max_rounds:
            raise ProducerError(
                f"failed to saturate: {changes} changes, "
                f"{len(unresolved)} unresolved, target {args.total_count}"
            )

        added: list[Fraction] = []
        precision_bits = args.bits + 2 * (round_index + 1)
        for left, right in zip(points, points[1:]):
            left_result = cache[left]
            right_result = cache[right]
            if (
                "unresolved" not in left_result
                and "unresolved" not in right_result
                and left_result["sign"] != right_result["sign"]
            ):
                continue
            for numerator in (1, 2, 3):
                candidate = nearest_dyadic(
                    left + (right - left) * Fraction(numerator, 4),
                    precision_bits,
                )
                if left < candidate < right:
                    added.append(candidate)
        added.extend(
            [
                nearest_dyadic((lower + points[0]) / 2, precision_bits),
                nearest_dyadic((points[-1] + upper) / 2, precision_bits),
            ]
        )
        points = sorted(
            set(points)
            | {candidate for candidate in added if lower < candidate < upper}
        )

    decided = decided_rows(points, cache)
    chain = alternating_subsequence(decided)
    if len(chain) != args.total_count + 1:
        raise ProducerError(
            f"alternating compression produced {len(chain)} samples, "
            f"expected {args.total_count + 1}"
        )
    if any(
        left[1]["sign"] == right[1]["sign"] for left, right in zip(chain, chain[1:])
    ):
        raise ProducerError("compressed chain does not alternate")

    samples = [
        {
            "t": row[1]["t"],
            "z_interval": row[1]["z_interval"],
            "producer_precision_bits": row[1]["precision_bits"],
        }
        for row in chain
    ]
    semantic_samples = [
        {"t": sample["t"], "z_interval": sample["z_interval"]}
        for sample in samples
    ]
    data: dict[str, Any] = {
        "schema": CHECKER.SCHEMA,
        "classification": CHECKER.PRODUCTION,
        "slab": {
            "lower": fraction_json(lower),
            "upper": fraction_json(upper),
        },
        "total_count_interval": {
            "lower": fraction_json(Fraction(args.total_count)),
            "upper": fraction_json(Fraction(args.total_count)),
        },
        "gates": {
            "total_count_status": "CERTIFIED_TOTAL_ZETA_ZERO_COUNT",
            "sign_status": "CERTIFIED_HARDY_Z_INTERVALS",
            "total_count_sha256": sha256_file(args.total_count_source),
            "sign_table_sha256": CHECKER.canonical_sha(semantic_samples),
            "total_count_source": str(args.total_count_source),
        },
        "samples": samples,
        "refinements": [],
        "target_ordinate": fraction_json(target),
        "producer": {
            "name": "build_gram_sign_chain_certificate.py",
            "python": platform.python_version(),
            "search_method": "asymptotic Gram points plus adaptive exact-dyadic subdivision",
            "bits": args.bits,
            "workers": args.workers,
            "precision_ladder": list(ladder),
            "rounds": rounds,
            "evaluated_sample_count": len(cache),
            "retained_chain_sample_count": len(samples),
            "elapsed_seconds": time.time() - started,
        },
    }
    verification = CHECKER.verify(data)
    data["initial_verification"] = {
        "verdict": verification["verdict"],
        "certificate_sha256": verification["certificate_sha256"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "verdict": verification["verdict"],
                "total_count": args.total_count,
                "retained_samples": len(samples),
                "evaluated_samples": len(cache),
                "certificate_sha256": verification["certificate_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
