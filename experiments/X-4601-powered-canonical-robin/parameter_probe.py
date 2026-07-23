#!/usr/bin/env python3
"""Replay one certificate with replacement dyadic parameters.

This intentionally calls ``Verifier.replay`` rather than ``Verifier.verify``:
the terminal stream and exact powered proofs are retained, while every Robin
interval is recomputed under the requested arithmetic parameters. A weak
configuration must fail closed if it cannot justify one of the stored terminals.
"""
from __future__ import annotations

import argparse
import copy
import json

from verify import Verifier, load_certificate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--log-terms", type=int, required=True)
    parser.add_argument("--exp-terms", type=int, required=True)
    parser.add_argument("--harmonic-cutoff", type=int, required=True)
    args = parser.parse_args()

    certificate = load_certificate(args.certificate)
    candidate = copy.deepcopy(certificate)
    candidate["parameters"] = {
        "bits": args.bits,
        "log_terms": args.log_terms,
        "exp_terms": args.exp_terms,
        "harmonic_cutoff": args.harmonic_cutoff,
    }
    try:
        replay = Verifier(candidate).replay()
    except Exception as exc:
        print(
            json.dumps(
                {
                    "accepted": False,
                    "parameters": candidate["parameters"],
                    "reason": f"{type(exc).__name__}: {exc}",
                },
                sort_keys=True,
            )
        )
        return 2

    print(
        json.dumps(
            {
                "accepted": True,
                "parameters": candidate["parameters"],
                "status": replay["status"],
                "counts": replay["counts"],
                "all_integer_normalized_ratio_upper": replay[
                    "all_integer_consequence"
                ]["normalized_ratio_upper"],
                "all_integer_normalized_ratio_upper_decimal_outward": replay[
                    "all_integer_consequence"
                ]["normalized_ratio_upper_decimal_outward"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
