#!/usr/bin/env python3
"""Bounded acquisition of eleven tiny primes for the dense-owner source replay."""

import json
from math import isqrt

U = 1 << 20
MAX_CANDIDATES_PER_WINDOW = 200
LABELS = ("p", "q", "r", "s", "g", "ell", "rho")


def main():
    windows = {}
    for j, label in enumerate(LABELS, 1):
        lower_numerator = (1000+j)*U
        upper_numerator = (1001+j)*U
        first = lower_numerator//1000+1
        first += int(first % 2 == 0)
        found = []
        examined = 0
        required = 2 if j <= 4 else 1
        for candidate in range(first, first+2*MAX_CANDIDATES_PER_WINDOW, 2):
            if candidate*1000 >= upper_numerator:
                break
            examined += 1
            if all(candidate % d for d in range(2,isqrt(candidate)+1)):
                found.append(candidate)
                if len(found) == required:
                    break
        if len(found) != required:
            raise RuntimeError(f"bounded prime fixture unavailable in {label}")
        windows[label] = {"index":j,"primes":found,"candidates_examined":examined}
    print(json.dumps({"U":U,"candidate_cap_per_window":MAX_CANDIDATES_PER_WINDOW,
                      "primality":"EXACT_TRIAL_DIVISION","windows":windows},indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
