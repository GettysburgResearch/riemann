#!/usr/bin/env python3
"""Frozen original-source optimizer replay with independent exact root controls."""

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
COMMIT = "bff003bc35b10c83fc1afa02533aec9dd478bb23"
PINS = {
    "scout": (
        PREFIX + "native_synchronized_face_scout.py",
        "c57fd63aca304e110146e7c53532deaca49461c8",
    ),
    "discovery": (
        PREFIX + "native_synchronized_face.discovery.json",
        "378df8cba2921d47dc65d2f151fa7d4a8b80bc3f",
    ),
    "preregistration": (
        PREFIX + "SYNCHRONIZED_FACE_MINIMIZER_PREREGISTRATION.md",
        "63bc77076b83d046d1e0bf6a0201de937fd72072",
    ),
}
MAX_BYTES = 4 * 1024 * 1024
NOTE = HERE / "OPTIMAL_SYNCHRONIZED_NATIVE_PATH.md"
CONTROLS_NOTE = HERE / "SYNCHRONIZED_FACE_VALIDATION_CONTROLS.md"
TEST = ROOT / "tests/test_native_six_hour_synchronized_minimum.py"
FIXTURE = HERE / "native_synchronized_face_certificate.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected), "typed original optimizer replay"
    )


def frozen(name):
    path, blob = PINS[name]
    require(len(COMMIT) == len(blob) == 40, "completed native discovery pins")
    ref = f"{COMMIT}:{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen source")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen original source authentication",
    )
    return raw


def scout_module():
    raw = frozen("scout")
    path = PINS["scout"][0]
    namespace = {
        "__name__": "authenticated_original_optimizer",
        "__file__": str(ROOT / path),
    }
    # Execute only the declared exact Git commit/blob-authenticated bytes.
    exec(compile(raw, str(ROOT / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def root_controls(scout):
    cases = (
        ((F(-4, 75), F(37, 75), F(-4, 3), F(1)), (F(1, 5), F(1, 3), F(4, 5))),
        ((F(2, 15), F(-11, 15), F(1)), (F(1, 3), F(2, 5))),
        ((F(-1, 3), F(1)), (F(1, 3),)),
        ((F(1), F(), F(1)), ()),
    )
    result = []
    for coefficients, expected in cases:
        sequence, roots, nodes = scout.isolate_roots(
            tuple(scout.point(x) for x in coefficients)
        )
        require(len(roots) == len(expected), "independent exact polynomial root count")
        require(
            all(
                a <= x <= b and b - a <= scout.ROOT_WIDTH
                for (a, b), x in zip(roots, expected, strict=True)
            ),
            "all known rational roots contained in certified intervals",
        )
        result.append(
            {
                "rational_polynomial": list(map(str, coefficients)),
                "known_roots": list(map(str, expected)),
                "isolating_intervals": [scout.interval_json(x) for x in roots],
                "sturm_sequence_length": len(sequence),
                "nodes": nodes,
            }
        )
    return result


def retained_symmetric_guard(scout):
    coefficients = (F(-3, 32), F(11, 16), F(-3, 2), F(1))
    try:
        scout.isolate_roots(tuple(scout.point(x) for x in coefficients))
    except ValueError as error:
        require(
            str(error) == "Sturm evaluation sign is not certified",
            "retain the specific observed symmetric-control refusal",
        )
        return {
            "rational_polynomial": list(map(str, coefficients)),
            "known_roots": ["1/4", "1/2", "3/4"],
            "status": "retained_uncertified_dyadic_control",
            "guard": str(error),
            "frozen_scout_changed": False,
        }
    raise ValueError("expected frozen symmetric-control refusal was not reproduced")


def build():
    scout = scout_module()
    frozen("preregistration")
    discovery = json.loads(frozen("discovery"))
    require(
        discovery["status"] == "certified", "actual original source optimum certified"
    )
    strict_equal(scout.discover(), discovery)
    require(
        discovery["unique_certified_candidate"] == "endpoint_zero",
        "executed original source winner",
    )
    winner = next(
        row for row in discovery["all_candidates"] if row["name"] == "endpoint_zero"
    )
    require(
        all(
            F(row["lower"]) > 5
            for row in winner["details"]["endpoint_tangent_half_gradients"]
        ),
        "original global energy coercivity coefficient exceeds10",
    )
    poly = tuple(
        tuple(F(row[side]) for side in ("lower", "upper"))
        for row in discovery["upper_boundary_derivative_coefficients"]
    )
    endpoint_values = [scout.polynomial_value(poly, scout.point(x)) for x in (0, 1)]
    require(
        all(value[0] > 0 for value in endpoint_values),
        "actual cubic endpoints are nonzero so the isolated root list is strictly interior",
    )
    for row, bound in zip(
        discovery["all_declared_comparisons"],
        (F(839, 100), F(497, 100), F(222, 100)),
        strict=True,
    ):
        require(
            F(row["energy_minus_best_face"]["lower"]) > bound,
            "certified improvement over every declared original source comparison",
        )
    controls = root_controls(scout)
    result = {
        "schema": "riemann.native_six_hour.synchronized_face_certificate.v1",
        "sources": [
            {"commit": COMMIT, "path": path, "blob": blob}
            for path, blob in PINS.values()
        ],
        "complete_original_discovery": discovery,
        "independent_rational_root_controls": controls,
        "retained_symmetric_control_failure": retained_symmetric_guard(scout),
        "certified_original_cubic_endpoint_values": [
            scout.interval_json(x) for x in endpoint_values
        ],
        "global_source_face_energy_gap_at_least_10D": True,
        "attained_global_minimum_on_exact_source_face": True,
        "all_native_paths_optimized": False,
        "primitive_site_diagonal_optimized": False,
        "full_gamma_identified": False,
        "owned_sha256_lf": {
            "note": sha256(NOTE.read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
            "validation_controls": sha256(
                CONTROLS_NOTE.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest(),
            "producer": sha256(
                Path(__file__).read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest(),
            "tests": sha256(TEST.read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
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
    result = build()
    if args.write:
        raw = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
        require(len(raw) <= MAX_BYTES, "bounded original optimizer artifact")
        FIXTURE.write_bytes(raw)
    else:
        require(
            FIXTURE.stat().st_size <= MAX_BYTES, "bounded original optimizer replay"
        )
        strict_equal(json.loads(FIXTURE.read_bytes()), result)
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
