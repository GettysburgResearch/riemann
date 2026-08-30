#!/usr/bin/env python3
"""Reconnaissance scan for the zeta screw function.

This is deliberately NOT a proof-producing program.  It implements the
prime-knot reduction from Issue #95: after log(2), each prime-power cell is a
strictly convex smooth function minus a fixed affine prime prefix.  The script
scans all knot values and the unique stationary point of every cell that has
one.  It can also form small anchored screw and Schoenberg-Gaussian matrices
from the best separated scalar candidates.

A proof run must replace every transcendental and prefix sum by directed
interval/ball arithmetic and must independently audit contiguous prime-power
coverage.
"""

from __future__ import annotations

import argparse
import bisect
import dataclasses
import hashlib
import heapq
import json
import math
import platform
import sys
import time
from pathlib import Path
from typing import Iterable, Sequence

# Enough digits for binary64 reconnaissance.  A directed implementation must
# obtain these constants from a rigorous special-function backend.
EULER_GAMMA = 0.577215664901532860606512090082402431
CATALAN = 0.915965594177219015054603514932384111
LOG2 = math.log(2.0)
B = (-EULER_GAMMA - math.pi / 2.0 - 3.0 * LOG2 - math.log(math.pi)) / 2.0
C = math.pi * math.pi + 8.0 * CATALAN


@dataclasses.dataclass(frozen=True)
class PrimePower:
    q: int
    p: int
    log_q: float
    weight: float  # Lambda(q)/sqrt(q) = log(p)/sqrt(q)


@dataclasses.dataclass(frozen=True)
class Candidate:
    kind: str
    value: float
    t: float
    left_q: int
    right_q: int | None
    derivative: float

    def as_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)


class Smallest:
    """Keep the k smallest candidates without storing every knot."""

    def __init__(self, k: int) -> None:
        self.k = max(1, k)
        self._heap: list[tuple[float, int, Candidate]] = []
        self._counter = 0

    def add(self, candidate: Candidate) -> None:
        item = (-candidate.value, self._counter, candidate)
        self._counter += 1
        if len(self._heap) < self.k:
            heapq.heappush(self._heap, item)
        elif candidate.value < -self._heap[0][0]:
            heapq.heapreplace(self._heap, item)

    def sorted(self) -> list[Candidate]:
        return sorted((item[2] for item in self._heap), key=lambda c: c.value)


def sieve_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n, flag in enumerate(flags) if flag]


def enumerate_prime_powers(limit: int) -> list[PrimePower]:
    powers: list[PrimePower] = []
    for p in sieve_primes(limit):
        log_p = math.log(p)
        q = p
        while q <= limit:
            powers.append(
                PrimePower(
                    q=q,
                    p=p,
                    log_q=math.log(q),
                    weight=log_p / math.sqrt(q),
                )
            )
            if q > limit // p:
                break
            q *= p
    powers.sort(key=lambda item: item.q)
    for a, b in zip(powers, powers[1:]):
        if a.q >= b.q:
            raise AssertionError("prime-power manifest is not strictly increasing")
    return powers


def smooth_a(t: float, *, abs_tail: float = 2.0e-16) -> float:
    """Evaluate A(t), the non-prime part of Psi(t), for t>0.

    We use

      A(t) = 4(exp(t/2)-2) + B*t + C/4
             - 4 sum_{m>=1} exp(-(4m+1)t/2)/(4m+1)^2.

    The positive series has term ratio at most exp(-2t).  The stopping rule
    bounds the omitted contribution geometrically.  It is extremely fast on
    the proof-relevant post-log(2) cells.
    """

    if t == 0.0:
        return 0.0
    if t < 0.0 or not math.isfinite(t):
        raise ValueError("smooth_a requires a finite t >= 0")

    x = math.exp(-t / 2.0)
    ratio_cap = math.exp(-2.0 * t)
    total = 0.0
    m = 1
    while True:
        n = 4 * m + 1
        term = math.exp(-n * t / 2.0) / (n * n)
        total += term
        next_n = n + 4
        next_term = math.exp(-next_n * t / 2.0) / (next_n * next_n)
        tail = next_term / (1.0 - ratio_cap)
        if 4.0 * tail <= abs_tail:
            break
        m += 1
        if m > 5_000_000:
            raise RuntimeError(
                "smooth series converges too slowly; use a special-function backend"
            )

    return 4.0 * (math.exp(t / 2.0) - 2.0) + B * t + C / 4.0 - 4.0 * total


def smooth_a_prime(t: float) -> float:
    if t <= 0.0:
        raise ValueError("smooth_a_prime requires t > 0")
    x = math.exp(-t / 2.0)
    return (
        2.0 * math.exp(t / 2.0)
        + B
        + math.atanh(x)
        + math.atan(x)
        - 2.0 * x
    )


def smooth_a_second(t: float) -> float:
    if t <= 0.0:
        raise ValueError("smooth_a_second requires t > 0")
    return math.exp(t / 2.0) - math.exp(-2.5 * t) / (1.0 - math.exp(-2.0 * t))


def psi_from_prefix(t: float, s0: float, s1: float) -> float:
    return smooth_a(t) - t * s0 + s1


def stationary_point(left: float, right: float, s0: float) -> float:
    """Bisect the unique solution of A'(t)=s0 in a convex cell."""

    f_left = smooth_a_prime(left) - s0
    f_right = smooth_a_prime(right) - s0
    if not (f_left < 0.0 < f_right):
        raise ValueError("cell does not bracket a stationary point")
    lo, hi = left, right
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if smooth_a_prime(mid) - s0 < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def scan_scalar(
    manifest: Sequence[PrimePower],
    cutoff: int,
    keep: int,
    diversity_bin_width: float,
) -> tuple[list[Candidate], list[Candidate], dict[str, int | float]]:
    if not manifest or manifest[0].q != 2:
        raise ValueError("manifest must begin with q=2")

    smallest = Smallest(keep)
    diverse_bins: dict[int, Candidate] = {}

    def record(candidate: Candidate) -> None:
        smallest.add(candidate)
        bucket = int(candidate.t / diversity_bin_width)
        old = diverse_bins.get(bucket)
        if old is None or candidate.value < old.value:
            diverse_bins[bucket] = candidate

    s0 = 0.0
    s1 = 0.0
    roots = 0
    knot_count = 0
    convexity_floor = smooth_a_second(LOG2)

    for index, item in enumerate(manifest):
        t = item.log_q

        # The term deposited at q vanishes at t=log(q), so the knot value can
        # be evaluated from the prefix immediately before or after inclusion.
        knot_value = psi_from_prefix(t, s0, s1)
        left_derivative = smooth_a_prime(t) - s0
        record(
            Candidate(
                kind="knot",
                value=knot_value,
                t=t,
                left_q=item.q,
                right_q=None,
                derivative=left_derivative,
            )
        )
        knot_count += 1

        s0 += item.weight
        s1 += item.weight * t
        right_derivative = smooth_a_prime(t) - s0

        if index + 1 < len(manifest):
            next_item = manifest[index + 1]
            right_t = next_item.log_q
            right_q: int | None = next_item.q
        else:
            right_t = math.log(cutoff)
            right_q = cutoff
            if right_t <= t:
                continue

        next_left_derivative = smooth_a_prime(right_t) - s0
        if right_derivative < 0.0 < next_left_derivative:
            root_t = stationary_point(t, right_t, s0)
            root_value = psi_from_prefix(root_t, s0, s1)
            record(
                Candidate(
                    kind="stationary",
                    value=root_value,
                    t=root_t,
                    left_q=item.q,
                    right_q=right_q,
                    derivative=smooth_a_prime(root_t) - s0,
                )
            )
            roots += 1

        # If the declared cutoff is not itself a prime power, its right
        # boundary is an additional endpoint of the finite search interval.
        if index + 1 == len(manifest) and right_t > t:
            record(
                Candidate(
                    kind="cutoff",
                    value=psi_from_prefix(right_t, s0, s1),
                    t=right_t,
                    left_q=item.q,
                    right_q=cutoff,
                    derivative=next_left_derivative,
                )
            )

    stats: dict[str, int | float] = {
        "cutoff": cutoff,
        "prime_power_count": len(manifest),
        "knot_count": knot_count,
        "stationary_cell_count": roots,
        "post_log2_convexity_floor": convexity_floor,
    }
    return smallest.sorted(), sorted(diverse_bins.values(), key=lambda c: c.value), stats


class PrefixEvaluator:
    def __init__(self, manifest: Sequence[PrimePower]) -> None:
        self.logs = [item.log_q for item in manifest]
        self.s0: list[float] = []
        self.s1: list[float] = []
        total0 = 0.0
        total1 = 0.0
        for item in manifest:
            total0 += item.weight
            total1 += item.weight * item.log_q
            self.s0.append(total0)
            self.s1.append(total1)

    def psi(self, t: float) -> float:
        t = abs(t)
        if t == 0.0:
            return 0.0
        index = bisect.bisect_right(self.logs, t) - 1
        if index < 0:
            return smooth_a(t)
        return psi_from_prefix(t, self.s0[index], self.s1[index])


def separated_candidates(
    candidates: Iterable[Candidate], size: int, separation: float
) -> list[Candidate]:
    if size <= 0:
        return []
    selected: list[Candidate] = []
    for candidate in sorted(candidates, key=lambda c: c.value):
        if candidate.t < LOG2:
            continue
        if all(abs(candidate.t - old.t) >= separation for old in selected):
            selected.append(candidate)
            if len(selected) == size:
                break
    return sorted(selected, key=lambda c: c.t)


def matrix_reconnaissance(
    evaluator: PrefixEvaluator,
    candidates: Sequence[Candidate],
    lambdas: Sequence[float],
) -> dict[str, object]:
    try:
        import numpy as np
    except ImportError:
        return {"status": "skipped", "reason": "numpy is not installed"}

    times = np.array([candidate.t for candidate in candidates], dtype=float)
    n = len(times)
    if n < 2:
        return {"status": "skipped", "reason": "fewer than two separated candidates"}

    values = np.array([evaluator.psi(float(t)) for t in times])
    distance = np.empty((n, n), dtype=float)
    screw = np.empty((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            dij = evaluator.psi(float(abs(times[i] - times[j])))
            distance[i, j] = dij
            screw[i, j] = values[i] + values[j] - dij

    screw_eigs = np.linalg.eigvalsh((screw + screw.T) / 2.0)

    pair_best: dict[str, float | int] | None = None
    for i in range(n):
        for j in range(i + 1, n):
            determinant = (
                4.0 * values[i] * values[j]
                - (values[i] + values[j] - distance[i, j]) ** 2
            )
            scale = 4.0 * values[i] * values[j]
            normalized = determinant / scale if scale > 0.0 else math.nan
            if pair_best is None or normalized < float(pair_best["normalized"]):
                pair_best = {
                    "i": i,
                    "j": j,
                    "determinant": determinant,
                    "normalized": normalized,
                }

    gaussian: list[dict[str, float]] = []
    for lam in lambdas:
        kernel = np.exp(-lam * distance)
        eigs = np.linalg.eigvalsh((kernel + kernel.T) / 2.0)
        gaussian.append(
            {
                "lambda": lam,
                "min_eigenvalue": float(eigs[0]),
                "max_eigenvalue": float(eigs[-1]),
            }
        )

    return {
        "status": "heuristic_binary64",
        "numpy_version": np.__version__,
        "times": [float(t) for t in times],
        "psi": [float(v) for v in values],
        "anchored_screw_min_eigenvalue": float(screw_eigs[0]),
        "anchored_screw_max_eigenvalue": float(screw_eigs[-1]),
        "best_pair_determinant": pair_best,
        "gaussian": gaussian,
    }


def parse_lambdas(text: str) -> list[float]:
    values = [float(piece.strip()) for piece in text.split(",") if piece.strip()]
    if not values or any(value <= 0.0 or not math.isfinite(value) for value in values):
        raise argparse.ArgumentTypeError("lambdas must be finite positive numbers")
    return values


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int, default=1_000_000)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--matrix-size", type=int, default=8)
    parser.add_argument("--matrix-separation", type=float, default=LOG2)
    parser.add_argument("--lambdas", type=parse_lambdas, default=[0.1, 1.0, 10.0])
    parser.add_argument("--json-out", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.cutoff < 2:
        raise SystemExit("--cutoff must be at least 2")
    if args.top < 1 or args.matrix_size < 0:
        raise SystemExit("--top must be positive and --matrix-size nonnegative")
    if args.matrix_separation <= 0.0 or not math.isfinite(args.matrix_separation):
        raise SystemExit("--matrix-separation must be finite and positive")

    started = time.perf_counter()
    manifest = enumerate_prime_powers(args.cutoff)
    manifest_seconds = time.perf_counter() - started

    # Keep extra records so the separation filter has room to work.
    keep = max(args.top, max(1, args.matrix_size) * 100)
    candidates, diverse_candidates, stats = scan_scalar(
        manifest,
        args.cutoff,
        keep,
        max(args.matrix_separation / 2.0, 1.0e-6),
    )
    scan_seconds = time.perf_counter() - started - manifest_seconds

    selected = separated_candidates(
        diverse_candidates, args.matrix_size, args.matrix_separation
    )
    evaluator = PrefixEvaluator(manifest)
    matrix = matrix_reconnaissance(evaluator, selected, args.lambdas)

    script_bytes = Path(__file__).read_bytes()
    result = {
        "classification": "EMPIRICAL_RECONNAISSANCE_ONLY",
        "arithmetic": "binary64; not directed",
        "implementation": {
            "script": str(Path(__file__).name),
            "sha256": hashlib.sha256(script_bytes).hexdigest(),
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "stats": stats,
        "timing_seconds": {
            "manifest": manifest_seconds,
            "scalar_scan": scan_seconds,
            "total": time.perf_counter() - started,
        },
        "smallest_candidates": [
            candidate.as_dict() for candidate in candidates[: args.top]
        ],
        "matrix_reconnaissance": matrix,
    }

    encoded = json.dumps(result, indent=2, sort_keys=True)
    print(encoded)
    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(encoded + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
