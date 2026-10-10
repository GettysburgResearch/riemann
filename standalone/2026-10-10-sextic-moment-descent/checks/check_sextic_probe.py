"""Reproduce the additional exact source-symbol checks, without floating moments.

Checks the actual probe's residue-symbol exponents against independent algebraic
identities: the value at -1, the complete sixth-power zero mask, and conjugation
in each inert residue field. This is a scoped identity check, not an independent
implementation of every finite-field operation or a certified moment estimate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe", type=Path,
                        default=Path(__file__).with_name("sextic_moment_probe.py"))
    parser.add_argument("--prime-limit", type=int, default=8192)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 2 <= args.prime_limit <= 8192:
        parser.error("This scoped int64 check supports 2 <= prime-limit <= 8192")
    spec = importlib.util.spec_from_file_location("sextic_probe_under_test", args.probe)
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    counts = {"minus_one": 0, "sixth_power_and_zero_mask": 0,
              "inert_conjugation": 0}
    raw = [(a, b) for a in range(-3, 4) for b in range(-3, 4)]
    a = np.array([x[0] for x in raw], dtype=np.int64)
    b = np.array([x[1] for x in raw], dtype=np.int64)
    powers = [probe.power(x, 6) for x in raw]
    pa = np.array([x[0] for x in powers], dtype=np.int64)
    pb = np.array([x[1] for x in powers], dtype=np.int64)
    # The fixed sample and modulus ceiling make all array operations exact.
    max_coord = max(abs(t) for pair in powers for t in pair)
    if 4 * args.prime_limit**2 >= np.iinfo(np.int64).max:
        raise OverflowError("Residue products exceed the supported int64 bound")
    if 2 * args.prime_limit * max_coord >= np.iinfo(np.int64).max:
        raise OverflowError("Sample coordinates exceed the supported int64 bound")
    ideals = probe.prime_ideals(args.prime_limit)
    for q in ideals:
        neg = int(probe.symbols(q, np.array([-1], dtype=np.int64),
                                np.array([0], dtype=np.int64))[0])
        if neg != 3 * (((q["norm"]-1)//6) % 2):
            raise RuntimeError(f"Sextic value at -1 failed: {q}")
        counts["minus_one"] += 1
        sx = probe.symbols(q, a, b)
        ps = probe.symbols(q, pa, pb)
        if not np.array_equal(ps, np.where(sx == -1, -1, 0)):
            raise RuntimeError(f"Sixth-power or zero-mask identity failed: {q}")
        counts["sixth_power_and_zero_mask"] += len(raw)
        if q["root"] is None:
            sc = probe.symbols(q, a-b, -b)
            if not np.array_equal(sc, np.where(sx == -1, -1, (-sx) % 6)):
                raise RuntimeError(f"Inert conjugation identity failed: {q}")
            counts["inert_conjugation"] += len(raw)
    result = {
        "status": "PASS_SCOPED_EXACT_SYMBOL_IDENTITIES",
        "probe_sha256": hashlib.sha256(args.probe.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "prime_ideal_norm_limit": args.prime_limit,
        "prime_ideals": len(ideals),
        "base_sample": "all a+b*omega with a,b in {-3,...,3}",
        "base_sample_size": len(raw),
        "maximum_sixth_power_coordinate": max_coord,
        "exact_predicates_by_kind": counts,
        "exact_predicates_total": sum(counts.values()),
        "arithmetic": "integer identities and safely bounded int64 residue arithmetic",
        "not_checked": ["full independent finite-field implementation",
                        "floating moment sums", "asymptotic moment bound", "RH"],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
