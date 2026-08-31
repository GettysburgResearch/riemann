#!/usr/bin/env python3
"""Acquire two fixed fourth-prime controls for the native boundary-layer test."""

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COMMIT = "1d1088d36f0d873ffc94d786415616df95b00edc"
PREFIX = "research/riemann-structures/native-six-hour/"
SOURCE = PREFIX + "native_face_prime_scout.py"
SOURCE_BLOB = "ad1a0c502b151fdb6b3c2729f3df6764da19485f"
ACQUISITION = PREFIX + "native_face_prime_acquisition.json"
ACQUISITION_BLOB = "4dcfad8765a0e9f52f56c1a77f3c28dc27ad760e"
MULTIPLIERS = (F(2501, 2500), F(2503, 2500))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def frozen(path, blob):
    raw = subprocess.run(
        ["git", "show", f"{COMMIT}:{path}"], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        0 < len(raw) <= 65536
        and sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == blob,
        "exact bounded inherited prime acquisition",
    )
    return raw


def prime_module():
    raw = frozen(SOURCE, SOURCE_BLOB)
    namespace = {
        "__name__": "authenticated_boundary_prime_source",
        "__file__": str(ROOT / SOURCE),
    }
    # Execute only the exact authenticated prior trial-division implementation.
    exec(compile(raw, str(ROOT / SOURCE), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def window(source, multiplier):
    require(
        type(multiplier) is F and multiplier in MULTIPLIERS,
        "two fixed fourth-prime windows only",
    )
    target = source.X * source.RATIO**3 * multiplier
    left, right = target - 100, target + 100
    lower = -((-left.numerator) // left.denominator)
    upper = right.numerator // right.denominator
    first = lower if lower % 2 else lower + 1
    require(0 < (upper - first) // 2 + 1 <= 101, "complete bounded window")
    prime, attempted = None, 0
    for candidate in range(first, upper + 1, 2):
        attempted += 1
        require(attempted <= 101, "fixed acquisition budget")
        if source.prime(candidate):
            prime = candidate
            break
    return {
        "multiplier": str(multiplier),
        "exact_target": str(target),
        "lower": lower,
        "upper": upper,
        "odd_candidates_attempted": attempted,
        "first_prime": prime,
        "complete_trial_division": True,
        "window_changed": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    source = prime_module()
    old = json.loads(frozen(ACQUISITION, ACQUISITION_BLOB))
    prefix = tuple(row["first_prime"] for row in old["windows"][:3])
    require(
        prefix == (99999931, 101999927, 104039917)
        and all(source.prime(p) for p in prefix),
        "unchanged literal three-prime prefix",
    )
    rows = [window(source, multiplier) for multiplier in MULTIPLIERS]
    result = {
        "schema": "riemann.native_six_hour.boundary_layer_prime_acquisition.v1",
        "sources": [
            {"commit": COMMIT, "path": SOURCE, "blob": SOURCE_BLOB},
            {"commit": COMMIT, "path": ACQUISITION, "blob": ACQUISITION_BLOB},
        ],
        "fixed_prefix": prefix,
        "original_fourth_prime": old["windows"][3]["first_prime"],
        "windows": rows,
        "all_windows_succeeded": all(row["first_prime"] is not None for row in rows),
        "total_candidates": sum(row["odd_candidates_attempted"] for row in rows),
        "kernel_phase_known_at_acquisition": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
