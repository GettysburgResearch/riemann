#!/usr/bin/env python3
"""Command-line complete-prime leading carrier screen.

This evaluates every prime power q<=c. The output is EMPIRICAL: it omits the
small high-carrier correction terms and uses ordinary floating-point linear
algebra. A negative output is a nomination for full interval evaluation, not
a counterexample.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone

from carrier_matrix import build_leading_coefficients, leading_normalized_minimum


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c", type=int, required=True)
    parser.add_argument("--carrier", required=True, help="decimal carrier, preferably an integer")
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    coeffs = build_leading_coefficients(args.c)
    value, prime_max, vector = leading_normalized_minimum(args.carrier, args.N, coeffs)
    result = {
        "experiment_id": "X-0701",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "c": args.c,
        "carrier": args.carrier,
        "N": args.N,
        "dimension": 2 * args.N + 1,
        "prime_power_terms": int(len(coeffs.logs)),
        "leading_normalized_minimum": float(value),
        "largest_complete_prime_matrix_eigenvalue": float(prime_max),
        "eigenvector": [float(x) for x in vector],
        "warning": (
            "All prime powers through c are included, but this is a high-carrier "
            "leading screen using ordinary floating point. Exact Gram, archimedean, "
            "pole, and negative-frequency corrections still require interval bounds."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
