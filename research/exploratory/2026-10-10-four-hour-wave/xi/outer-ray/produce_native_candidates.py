#!/usr/bin/env python3
"""Produce candidate brackets only; check_native_slab.py must accept them.

acb.zeta_zeros is used as a search aid. The separate checker replays every
actual Hardy-Z endpoint and the named complete-count library contract.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import flint
from flint import acb, arb, ctx


def main() -> None:
    ctx.prec = 128
    height, denominator = 8192, 2**24
    complete_count = arb(height).zeta_nzeros()
    count = complete_count.unique_fmpz()
    if count is None or not complete_count.is_exact():
        raise SystemExit("FAIL: no exact candidate count")
    count = int(count)
    intervals = []
    for start in range(1, count+1, 256):
        for candidate in acb.zeta_zeros(start, min(256, count+1-start)):
            lower = (candidate.imag.mid()*denominator).floor().unique_fmpz()
            if lower is None:
                raise SystemExit("FAIL: candidate midpoint quantization")
            lower = int(lower)
            intervals.append([lower, lower+1])
    directory = Path(__file__).resolve().parent
    output = directory/"native_candidates.json"
    output.write_text(json.dumps({
        "status": "CANDIDATES_ONLY_NOT_A_ZERO_CENSUS",
        "normalization": "Xi(z)=xi(1/2+i*z)",
        "height": height,
        "denominator": denominator,
        "candidate_count": count,
        "interval_numerators": intervals,
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_flint_version": flint.__version__,
        "flint_version": flint.__FLINT_VERSION__,
    }, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print("PRODUCED_NATIVE_CANDIDATES", f"count={count}",
          "acceptance_requires=check_native_slab.py", flush=True)


if __name__ == "__main__":
    main()
