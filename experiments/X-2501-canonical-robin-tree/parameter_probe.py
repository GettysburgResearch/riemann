#!/usr/bin/env python3
"""Run one terminal-stream replay in a fresh process."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import time
from typing import Sequence

from certmath import RobinParameters
from verify import IndependentVerifier


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--label", required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--log-terms", type=int, required=True)
    parser.add_argument("--exp-terms", type=int, required=True)
    parser.add_argument("--harmonic-cutoff", type=int, required=True)
    args = parser.parse_args(argv)

    params = RobinParameters(
        args.bits, args.log_terms, args.exp_terms, args.harmonic_cutoff
    )
    certificate = json.loads(Path(args.certificate).read_text(encoding="utf-8"))
    certificate["parameters"] = asdict(params)
    started = time.perf_counter()
    try:
        replay = IndependentVerifier(certificate).replay()
    except (ValueError, RuntimeError) as exc:
        result = {
            "label": args.label,
            "parameters": asdict(params),
            "accepted": False,
            "first_failure": str(exc),
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        }
    else:
        result = {
            "label": args.label,
            "parameters": asdict(params),
            "accepted": True,
            "status": replay["status"],
            "normalized_ratio_upper_decimal_outward": (
                replay["all_integer_consequence"][
                    "normalized_ratio_upper_decimal_outward"
                ]
                if replay["all_integer_consequence"] is not None
                else None
            ),
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
