#!/usr/bin/env python3
from __future__ import annotations

import heapq
import json
import math
from pathlib import Path
from fractions import Fraction

PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
    37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
]
P79 = math.prod(PRIMES)
DEN = 10**30


def half_products(primes: list[int]) -> list[tuple[int, int]]:
    values = [(1, 1)]
    for prime in primes:
        values += [(d * prime, -mu) for d, mu in list(values)]
    values.sort()
    return values


LEFT = half_products(PRIMES[:11])
RIGHT = half_products(PRIMES[11:])


def divisor_stream():
    heap: list[tuple[int, int, int, int]] = []
    for i, (a, sa) in enumerate(LEFT):
        b, sb = RIGHT[0]
        heapq.heappush(heap, (a * b, i, 0, sa * sb))
    while heap:
        value, i, j, sign = heapq.heappop(heap)
        yield value, sign
        j += 1
        if j < len(RIGHT):
            a, sa = LEFT[i]
            b, sb = RIGHT[j]
            heapq.heappush(heap, (a * b, i, j, sa * sb))


def invsqrt_floor(value: int) -> int:
    square = DEN * DEN
    root = math.isqrt(square // value)
    while (root + 1) * (root + 1) * value <= square:
        root += 1
    while root * root * value > square:
        root -= 1
    return root


def main() -> None:
    full = divisor_stream()
    next_full = next(full, None)
    future_even: list[tuple[int, int, int]] = []

    raw_even_num = 0
    shifted_even_num = 0
    shifted_even_sqrt_upper = 0
    odd_num = 0
    odd_sqrt_lower = 0

    minimum_raw = None
    minimum_shifted = None
    maximum_shifted_sqrt = None
    odd_count = 0

    for threshold, sign in divisor_stream():
        if sign != -1:
            continue
        odd_count += 1

        still_future = []
        for value, numerator, sqrt_lower in future_even:
            if value <= threshold:
                raw_even_num += numerator
            else:
                still_future.append((value, numerator, sqrt_lower))
        future_even = still_future

        while next_full is not None and next_full[0] <= threshold + 8:
            value, current_sign = next_full
            if current_sign == 1:
                numerator = P79 // value
                sqrt_lower = invsqrt_floor(value)
                shifted_even_num += numerator
                shifted_even_sqrt_upper += sqrt_lower + 1
                if value <= threshold:
                    raw_even_num += numerator
                else:
                    future_even.append((value, numerator, sqrt_lower))
            next_full = next(full, None)

        numerator = P79 // threshold
        sqrt_lower = invsqrt_floor(threshold)
        odd_num += numerator
        odd_sqrt_lower += sqrt_lower

        raw_numerator = raw_even_num - odd_num
        shifted_numerator = shifted_even_num - odd_num
        shifted_sqrt_upper = shifted_even_sqrt_upper - odd_sqrt_lower

        if threshold >= 83:
            record = (raw_numerator, threshold)
            if minimum_raw is None or record[0] < minimum_raw[0]:
                minimum_raw = record

        record = (shifted_numerator, threshold)
        if minimum_shifted is None or record[0] < minimum_shifted[0]:
            minimum_shifted = record

        record = (shifted_sqrt_upper, threshold)
        if maximum_shifted_sqrt is None or record[0] > maximum_shifted_sqrt[0]:
            maximum_shifted_sqrt = record

    assert odd_count == 2**21
    assert minimum_raw is not None
    assert minimum_shifted is not None
    assert maximum_shifted_sqrt is not None

    assert 25 * minimum_raw[0] > P79
    assert 5000 * minimum_shifted[0] > P79
    assert 2 * maximum_shifted_sqrt[0] < 3 * DEN

    result = {
        "classification": "PASS_P79_PREFIX_RESERVE",
        "divisors_streamed": 2**22,
        "odd_thresholds": odd_count,
        "raw_reciprocal_minimum": {
            "threshold": minimum_raw[1],
            "numerator": str(minimum_raw[0]),
            "denominator": str(P79),
            "decimal": float(Fraction(minimum_raw[0], P79)),
            "certified_above": "1/25",
        },
        "shifted_reciprocal_minimum": {
            "threshold": minimum_shifted[1],
            "numerator": str(minimum_shifted[0]),
            "denominator": str(P79),
            "decimal": float(Fraction(minimum_shifted[0], P79)),
            "certified_above": "1/5000",
        },
        "shifted_inverse_sqrt_maximum": {
            "threshold": maximum_shifted_sqrt[1],
            "directed_upper_decimal": maximum_shifted_sqrt[0] / DEN,
            "certified_below": "3/2",
        },
        "scope": (
            "The reciprocal-prefix gates are exact integer comparisons over "
            "the common denominator P79. The inverse-square-root gate uses "
            "directed rational enclosures. This checker does not certify the "
            "finite low-prefix upward-correction theorem or RH."
        ),
    }

    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
