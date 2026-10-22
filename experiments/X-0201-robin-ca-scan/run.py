#!/usr/bin/env python3
"""Empirical colossally-abundant search for a Robin-inequality witness.

For a prime p and a >= 1, the transition a-1 -> a for a colossally
abundant maximizer occurs at

  epsilon(p,a) = log((1-p**(-a-1))/(1-p**(-a))) / log(p).

The a=1 transitions are monotone in p, so they are streamed in ascending-prime
order. Only the few a>=2 transitions above the cutoff are sorted and merged.
All transition ordering and Robin quotients in this file use IEEE-754 binary64;
therefore every result is EMPIRICAL, never a proof.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import asdict, dataclass
import heapq
import json
import math
import platform
import sys
import time
from typing import Iterator, Sequence

EULER_GAMMA_BINARY64 = 0.577215664901532860606512090082402431
ROBIN_EXCEPTION = 5040
DEFAULT_SEGMENT_ODDS = 1 << 20
DEFAULT_TIE_ULPS = 64


@dataclass(frozen=True)
class Transition:
    boundary: float
    prime: int
    exponent: int


@dataclass(frozen=True)
class Record:
    ratio: float
    log_n: float
    decimal_digits: float
    prime: int
    exponent: int
    distinct_primes: int
    event_index: int
    boundary: float


@dataclass(frozen=True)
class ScanSummary:
    status: str
    p_max: int
    b_min: float
    prime_count: int
    event_count: int
    distinct_primes: int
    log_n: float
    decimal_digits: float
    best_ratio: float | None
    margin_to_violation: float | None
    best_event: Record | None
    top_events: list[Record]
    last_record_highs: list[Record]
    record_high_count: int
    small_prime_exponents: list[tuple[int, int]]
    near_ties: list[dict[str, float | int]]
    elapsed_seconds: float
    python: str
    platform: str
    numerical_backend: str
    interpretation: str


def transition_boundary(p: int, a: int) -> float:
    if p < 2 or a < 1:
        raise ValueError("transition_boundary requires p >= 2 and a >= 1")
    log_p = math.log(p)
    x = math.exp(-a * log_p)
    if x == 0.0:
        return 0.0
    return (math.log1p(-x / p) - math.log1p(-x)) / log_p


def simple_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            count = ((limit - start) // p) + 1
            sieve[start : limit + 1 : p] = b"\x00" * count
    return [n for n, flag in enumerate(sieve) if flag]


def segmented_primes(limit: int, segment_odds: int = DEFAULT_SEGMENT_ODDS) -> Iterator[int]:
    """Yield primes <= limit with O(segment_odds + sqrt(limit)) memory."""
    if segment_odds < 1:
        raise ValueError("segment_odds must be positive")
    if limit < 2:
        return
    yield 2
    if limit < 3:
        return
    base_primes = [p for p in simple_primes(math.isqrt(limit)) if p != 2]
    low = 3
    while low <= limit:
        high = min(limit, low + 2 * (segment_odds - 1))
        if high % 2 == 0:
            high -= 1
        size = ((high - low) // 2) + 1
        segment = bytearray(b"\x01") * size
        for p in base_primes:
            if p * p > high:
                break
            start = max(p * p, ((low + p - 1) // p) * p)
            if start % 2 == 0:
                start += p
            index = (start - low) // 2
            count = ((size - 1 - index) // p) + 1
            segment[index::p] = b"\x00" * count
        for index, flag in enumerate(segment):
            if flag:
                yield low + 2 * index
        low = high + 2


def higher_exponent_transitions(p_max: int) -> tuple[float, list[Transition]]:
    if p_max < 2:
        raise ValueError("p_max must be at least 2")
    b_min = transition_boundary(p_max, 1)
    p_limit = 2
    while p_limit < p_max and transition_boundary(p_limit, 2) >= b_min:
        p_limit *= 2
    p_limit = min(p_limit, p_max)
    transitions: list[Transition] = []
    for p in segmented_primes(p_limit, min(DEFAULT_SEGMENT_ODDS, 1 << 16)):
        for a in range(2, 1024):
            boundary = transition_boundary(p, a)
            if boundary < b_min:
                break
            transitions.append(Transition(boundary, p, a))
        else:  # pragma: no cover
            raise RuntimeError(f"exponent cap reached for p={p}")
    transitions.sort(key=lambda event: event.boundary, reverse=True)
    return b_min, transitions


def _near_equal(x: float, y: float, tie_ulps: int) -> bool:
    scale = max(abs(x), abs(y), sys.float_info.min)
    return abs(x - y) <= tie_ulps * sys.float_info.epsilon * scale


def scan_ca_transitions(
    p_max: int,
    *,
    top_k: int = 20,
    segment_odds: int = DEFAULT_SEGMENT_ODDS,
    tie_ulps: int = DEFAULT_TIE_ULPS,
    allow_near_ties: bool = False,
) -> ScanSummary:
    if p_max < 2:
        raise ValueError("p_max must be at least 2")
    if top_k < 1 or tie_ulps < 1:
        raise ValueError("top_k and tie_ulps must be positive")

    started = time.perf_counter()
    b_min, extras = higher_exponent_transitions(p_max)
    extra_index = 0

    # Only primes with an a>=2 event need an exponent map. This avoids storing
    # millions of uninformative exponent-one entries.
    tracked_primes = {event.prime for event in extras}
    tracked_exponents: dict[int, int] = {}
    display_exponents: dict[int, int] = {}
    distinct_prime_count = 0
    log_n = 0.0
    log_abundancy = 0.0
    event_count = 0
    prime_count = 0
    best: Record | None = None
    top_heap: list[tuple[float, int, Record]] = []
    record_highs: deque[Record] = deque(maxlen=20)
    record_high_count = 0
    near_ties: list[dict[str, float | int]] = []

    def process(event: Transition) -> None:
        nonlocal log_n, log_abundancy, event_count, best, record_high_count
        nonlocal distinct_prime_count

        if event.exponent == 1:
            distinct_prime_count += 1
            if event.prime in tracked_primes:
                tracked_exponents[event.prime] = 1
            if len(display_exponents) < 30:
                display_exponents[event.prime] = 1
        else:
            previous = tracked_exponents.get(event.prime, 0)
            if event.exponent != previous + 1:
                raise RuntimeError(
                    "transition order is inconsistent: "
                    f"p={event.prime}, a={event.exponent}, previous={previous}"
                )
            tracked_exponents[event.prime] = event.exponent
            if event.prime in display_exponents:
                display_exponents[event.prime] = event.exponent

        log_p = math.log(event.prime)
        log_n += log_p
        x = math.exp(-event.exponent * log_p)
        log_abundancy += math.log1p(-x / event.prime) - math.log1p(-x)
        event_count += 1
        if log_n <= math.log(ROBIN_EXCEPTION):
            return

        abundancy = math.exp(log_abundancy)
        denominator = math.exp(EULER_GAMMA_BINARY64) * math.log(log_n)
        ratio = abundancy / denominator
        record = Record(
            ratio=ratio,
            log_n=log_n,
            decimal_digits=log_n / math.log(10.0),
            prime=event.prime,
            exponent=event.exponent,
            distinct_primes=distinct_prime_count,
            event_index=event_count,
            boundary=event.boundary,
        )
        if best is None or ratio > best.ratio:
            best = record
            record_highs.append(record)
            record_high_count += 1
        entry = (ratio, event_count, record)
        if len(top_heap) < top_k:
            heapq.heappush(top_heap, entry)
        elif ratio > top_heap[0][0]:
            heapq.heapreplace(top_heap, entry)

    for p in segmented_primes(p_max, segment_odds):
        prime_count += 1
        prime_event = Transition(transition_boundary(p, 1), p, 1)
        while extra_index < len(extras):
            extra = extras[extra_index]
            if _near_equal(extra.boundary, prime_event.boundary, tie_ulps):
                collision = {
                    "prime_event_prime": p,
                    "prime_event_boundary": prime_event.boundary,
                    "extra_prime": extra.prime,
                    "extra_exponent": extra.exponent,
                    "extra_boundary": extra.boundary,
                }
                near_ties.append(collision)
                if not allow_near_ties:
                    raise RuntimeError(
                        "binary64 cannot safely order a near-tied transition; "
                        "use --allow-near-ties only for exploration"
                    )
                if extra.boundary >= prime_event.boundary:
                    process(extra)
                    extra_index += 1
                    continue
                break
            if extra.boundary > prime_event.boundary:
                process(extra)
                extra_index += 1
                continue
            break
        process(prime_event)

    while extra_index < len(extras):
        process(extras[extra_index])
        extra_index += 1

    top_events = [entry[2] for entry in sorted(top_heap, reverse=True)]
    elapsed = time.perf_counter() - started
    return ScanSummary(
        status="EMPIRICAL",
        p_max=p_max,
        b_min=b_min,
        prime_count=prime_count,
        event_count=event_count,
        distinct_primes=distinct_prime_count,
        log_n=log_n,
        decimal_digits=log_n / math.log(10.0),
        best_ratio=None if best is None else best.ratio,
        margin_to_violation=None if best is None else 1.0 - best.ratio,
        best_event=best,
        top_events=top_events,
        last_record_highs=list(record_highs),
        record_high_count=record_high_count,
        small_prime_exponents=sorted(display_exponents.items()),
        near_ties=near_ties,
        elapsed_seconds=elapsed,
        python=sys.version.split()[0],
        platform=platform.platform(),
        numerical_backend="CPython math / IEEE-754 binary64 (non-rigorous)",
        interpretation=(
            "No certified conclusion. A ratio >= 1 would be only a candidate "
            "until independently enclosed with rigorous interval arithmetic."
        ),
    )


def first_ca_numbers(count: int, *, prime_limit: int = 100, exponent_cap: int = 64) -> list[int]:
    """Materialize an initial CA prefix for regression tests."""
    if count < 0:
        raise ValueError("count must be nonnegative")
    events: list[Transition] = []
    for p in simple_primes(prime_limit):
        for a in range(1, exponent_cap + 1):
            boundary = transition_boundary(p, a)
            if boundary == 0.0:
                break
            events.append(Transition(boundary, p, a))
    events.sort(key=lambda event: event.boundary, reverse=True)
    exponents: dict[int, int] = {}
    n = 1
    values: list[int] = []
    for event in events:
        previous = exponents.get(event.prime, 0)
        if event.exponent != previous + 1:
            continue
        exponents[event.prime] = event.exponent
        n *= event.prime
        values.append(n)
        if len(values) == count:
            return values
    raise ValueError("prime_limit/exponent_cap too small for requested prefix")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--p-max", type=int, required=True)
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--segment-odds", type=int, default=DEFAULT_SEGMENT_ODDS)
    parser.add_argument("--tie-ulps", type=int, default=DEFAULT_TIE_ULPS)
    parser.add_argument("--allow-near-ties", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        summary = scan_ca_transitions(
            args.p_max,
            top_k=args.top_k,
            segment_odds=args.segment_odds,
            tie_ulps=args.tie_ulps,
            allow_near_ties=args.allow_near_ties,
        )
    except (ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(asdict(summary), indent=2, sort_keys=True))
    else:
        print(f"status: {summary.status}")
        print(f"p_max: {summary.p_max}")
        print(f"primes/events: {summary.prime_count}/{summary.event_count}")
        print(f"log(n): {summary.log_n:.17g}")
        print(f"decimal digits (approx): {summary.decimal_digits:.6f}")
        print(f"best Robin ratio: {summary.best_ratio!r}")
        print(f"margin to 1: {summary.margin_to_violation!r}")
        print(summary.interpretation)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
