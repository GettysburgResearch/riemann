#!/usr/bin/env python3
"""Acquire the first literal prime in six preregistered fixed windows."""

import argparse
import json
from fractions import Fraction as F
from math import isqrt

X = 100000000
RATIO = F(51, 50)
HALF_WIDTH = 100
MAX_CANDIDATES = 101
MAX_PRIME = 120000000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prime(value):
    require(
        type(value) is int and 2 <= value <= MAX_PRIME,
        "exact bounded trial-division input",
    )
    if value % 2 == 0:
        return value == 2
    limit = isqrt(value)
    require(limit < 11000, "literal trial divisor cap")
    return all(value % divisor for divisor in range(3, limit + 1, 2))


def window(index):
    require(type(index) is int and 0 <= index < 6, "fixed source window index")
    target = X * RATIO**index
    left, right = target - HALF_WIDTH, target + HALF_WIDTH
    lower = -((-left.numerator) // left.denominator)
    upper = right.numerator // right.denominator
    first_odd = lower if lower % 2 else lower + 1
    require(
        0 < (upper - first_odd) // 2 + 1 <= MAX_CANDIDATES,
        "complete fixed-window candidate cap",
    )
    found, attempted = None, 0
    for candidate in range(first_odd, upper + 1, 2):
        attempted += 1
        require(attempted <= MAX_CANDIDATES, "hard acquisition budget")
        if prime(candidate):
            found = candidate
            break
    return {
        "index": index,
        "exact_target": str(target),
        "lower": lower,
        "upper": upper,
        "odd_candidates_attempted": attempted,
        "first_prime": found,
        "complete_trial_division": True,
        "window_changed": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    windows = [window(i) for i in range(6)]
    result = {
        "schema": "riemann.native_six_hour.face_prime_acquisition.v1",
        "X": X,
        "ratio": str(RATIO),
        "half_width": HALF_WIDTH,
        "windows": windows,
        "all_windows_succeeded": all(row["first_prime"] is not None for row in windows),
        "candidate_count": sum(row["odd_candidates_attempted"] for row in windows),
        "kernel_face_result_known_at_acquisition": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
