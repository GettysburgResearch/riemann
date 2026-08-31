#!/usr/bin/env python3
"""Frozen complete-grid replay with independent census and signed-score controls."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
CALIBRATION = "fd24a4acb3b9a041bce4fb8701d2a887e77d2def"
PINS = {
    "scout": (
        CALIBRATION,
        "native_monotone_grid_scout.py",
        "01f94b1576e36319b6b3ed42a1e49057f2e70b85",
    ),
    "calibration": (
        CALIBRATION,
        "native_monotone_grid.calibration.json",
        "82f2d4c5f78f3cf8221ae49a2abc1aa3e1b35d22",
    ),
    "heldout": (
        "885fff1b92897d604dbec971a2945c76191c7dfd",
        "native_monotone_grid.heldout.json",
        "543ab3cf0e4a7dc6f04e05bc781d2a3ed9260e36",
    ),
}
MAX_BYTES = 8 * 1024 * 1024
FIXTURE = HERE / "native_monotone_grid_certificate.json"
NOTE = HERE / "NATIVE_MONOTONE_GRID_RESULTS.md"
TEST = ROOT / "tests/test_native_six_hour_monotone_grid.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(left, right):
    require(canonical(left) == canonical(right), "typed complete-grid equality")


def frozen(name, execute=False):
    commit, path, blob = PINS[name]
    require(len(commit) == len(blob) == 40, "complete frozen grid pins")
    ref = f"{commit}:{PREFIX}{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen grid artifact")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact source/executable/artifact authentication",
    )
    if not execute:
        return raw
    namespace = {
        "__name__": "authenticated_complete_grid",
        "__file__": str(HERE / path),
    }
    # Execute only the exact declared Git commit/blob-authenticated bytes.
    exec(compile(raw, str(HERE / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def synthetic_controls(scout):
    zero = {
        "constant": (0, 0),
        "cross": [(0, 0)] * 6,
        "gram": [[(0, 0)] * 6 for _ in range(6)],
    }
    tied = scout.enumerate_paths(2, zero)
    require(
        tied["count"] == 90
        and sum(x["word_multiplicity"] for x in tied["candidates"].values()) == 90,
        "every tied source word and multiplicity retained",
    )
    quadratic = {
        "constant": (scout.DYADIC // 4,) * 2,
        "cross": [(-scout.DYADIC // 2,) * 2] + [(0, 0)] * 5,
        "gram": [
            [(scout.DYADIC,) * 2 if i == j == 0 else (0, 0) for j in range(6)]
            for i in range(6)
        ],
    }
    middle = scout.enumerate_paths(2, quadratic)
    require(
        middle["best_upper"] == 0 and all(key[0] == 8 for key in middle["candidates"]),
        "negative cross term selects exact A=1/2 rather than endpoint",
    )
    axis = {
        "235": (0, 0, 0, 0, 0, 0),
        "253": (0, 0, 0, 0, 0, 1),
        "325": (1, F(1, 2), F(1, 2), 0, 0, 0),
        "352": (1, F(1, 2), F(1, 2), 1, F(1, 2), 0),
        "523": (0, 0, 0, 1, F(1, 2), 1),
        "532": (1, F(1, 2), F(1, 2), 1, F(1, 2), 1),
    }
    for word, expected in axis.items():
        numerators, _ = scout.word_path(1, word)
        require(
            tuple(F(x, 2) for x in numerators) == expected,
            "six independent exact ordered-activation moments",
        )
    original, _ = scout.word_path(2, "232355")
    refined, _ = scout.word_path(4, "".join(symbol * 2 for symbol in "232355"))
    require(
        refined == tuple(8 * x for x in original),
        "same actual N2 path represented on N4",
    )
    return {
        "zero_metric_all90_words_retained": True,
        "zero_metric_coordinate_classes": len(tied["candidates"]),
        "signed_quadratic_A_half_word_count": sum(
            x["word_multiplicity"] for x in middle["candidates"].values()
        ),
        "six_exact_axis_moments": {
            word: list(map(str, values)) for word, values in axis.items()
        },
        "nested_refinement_numerators_factor": 8,
        "synthetic_controls_claimed_native_metrics": False,
    }


def build():
    scout = frozen("scout", True)
    data = {name: json.loads(frozen(name)) for name in ("calibration", "heldout")}
    for name, value in data.items():
        strict_equal(scout.discover(name), value)
    strict_equal(
        data["calibration"]["owned_sha256_lf"], data["heldout"]["owned_sha256_lf"]
    )
    strict_equal(
        data["calibration"]["quantized_original_metric"],
        data["heldout"]["quantized_original_metric"],
    )
    panels = data["calibration"]["panels"] + data["heldout"]["panels"]
    require(
        [(x["N"], x["path_count"]) for x in panels] == [(2, 90), (3, 1680), (4, 34650)],
        "complete preregistered calibration and heldout census",
    )
    for panel in panels:
        require(
            panel["minimum_status"] == "exact_all_surviving_classes_tie",
            "executed exact candidate ordering",
        )
        require(
            panel["surviving_coordinate_class_count"]
            == len(panel["all_surviving_classes"]),
            "all candidate classes retained",
        )
        require(
            all(
                len(row["complete63_literal_source"]) == 63
                and len(row["complete45_rational_ratio_image"]) == 45
                for row in panel["all_surviving_classes"]
            ),
            "every winner has whole-source replay",
        )
    result = {
        "schema": "riemann.native_six_hour.complete_grid_certificate.v1",
        "sources": [
            {"commit": commit, "path": PREFIX + path, "blob": blob}
            for commit, path, blob in PINS.values()
        ],
        "complete_calibration": data["calibration"],
        "complete_heldout": data["heldout"],
        "independent_exact_controls": synthetic_controls(scout),
        "same_frozen_executable_and_metric_in_heldout": True,
        "all_continuous_paths_optimized_by_finite_grid": False,
        "all_height_source_claimed": False,
        "full_gamma_identified": False,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in (Path(__file__), NOTE, TEST)
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        raw = (
            json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n"
        ).encode()
        require(len(raw) <= MAX_BYTES, "bounded final complete-grid artifact")
        FIXTURE.write_bytes(raw)
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "bounded final grid read")
        strict_equal(json.loads(FIXTURE.read_bytes()), payload)
    print("PASS frozen complete native grid census, physical replay and exact controls")


if __name__ == "__main__":
    main()
