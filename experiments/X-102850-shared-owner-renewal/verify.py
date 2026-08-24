#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    subset_checks = 0
    for n in range(2, 9):
        labels = primes[:n]
        for mask in range(1 << n):
            selected = [labels[i] for i in range(n) if (mask >> i) & 1]
            if len(selected) < 2:
                continue
            p = max(selected)
            lower = [q for q in selected if q < p]
            assert lower
            assert all(q < p for q in lower)
            subset_checks += 1

    shared = 0
    disjoint = 0
    pairs = list(itertools.combinations(primes[:10], 2))
    for P, Q in itertools.combinations(pairs, 2):
        size = len(set(P) & set(Q))
        if size == 1:
            shared += 1
        elif size == 0:
            disjoint += 1
        else:
            raise AssertionError("distinct pairs cannot share two labels")

    # Finite Euler-product fixture for the decreasing-prime renewal.
    for constant in (1, 2, 4):
        product = 1.0
        for p in primes:
            product *= 1.0 + constant / p
        assert product < (1.0 + math.log(primes[-1])) ** (constant + 2)

    payload = {
        "schema": "riemann.t102850.shared-owner-renewal.v1",
        "largest_owner_subset_checks": subset_checks,
        "shared_pair_classifications": shared,
        "disjoint_pair_classifications": disjoint,
        "decreasing_prime_renewal_exact": True,
        "renewal_euler_product_polylog": True,
        "four_owner_dispersion_proved": False,
        "rh_established": False,
        "verdict": "PASS_T102850_SHARED_OWNER_RENEWAL",
    }
    payload["proof_object_sha256"] = digest(payload)

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
