#!/usr/bin/env python3
"""Proof-bound complete native curvature vectors and physical ratio pivots."""

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
FREEZE = "bae7184724093d3589ad16b278dc104322428d6a"
PINS = {
    "scout": (
        PREFIX + "native_curvature_span_scout.py",
        "e660bfaa86ca3562189d47c89390984fc1e3117c",
    ),
    "discovery": (
        PREFIX + "native_curvature_span.discovery.json",
        "1bb6e7fba73d796d064d397ef95bda1ee770f48a",
    ),
    "preregistration": (
        PREFIX + "NATIVE_CURVATURE_SPAN_PREREGISTRATION.md",
        "1452d6977f817818c67c7e5244dd03de4228a992",
    ),
}
FIXTURE = HERE / "native_curvature_span_certificate.json"
OWNED = (
    HERE / "NATIVE_CURVATURE_SPAN.md",
    HERE / "NATIVE_CURVATURE_SPAN_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_native_six_hour_curvature_span.py",
)
MAX_BYTES = 4 * 1024 * 1024
TABLE = (
    (
        (2, 3),
        (0, 0, 0),
        {
            (2, 3): F(1, 2),
            (3, 4): F(3, 8),
            (2, 9): F(-3, 8),
            (2, 12): F(-1, 4),
            (3, 8): F(-1, 16),
        },
    ),
    ((2, 3), (1, 0, 0), {(2, 6): F(-1, 4), (2, 12): F(3, 16), (4, 6): F(3, 16)}),
    ((2, 3), (0, 1, 0), {(3, 6): F(1, 4)}),
    ((2, 5), (0, 0, 0), {(2, 5): F(1, 2), (4, 5): F(-3, 8)}),
    ((2, 5), (1, 0, 0), {(2, 10): F(-1, 4)}),
    ((3, 5), (0, 0, 0), {(3, 5): F(1, 2)}),
)
PIVOTS = ((3, 4), (1, 3), (1, 2), (4, 5), (1, 5), (3, 5))
PIVOT_VALUES = (F(3, 8), F(-1, 8), F(1, 12), F(-3, 8), F(-1, 8), F(1, 2))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def json_tree(value):
    if type(value) in (type(None), bool, int, float, str):
        return True
    if type(value) is list:
        return all(json_tree(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and json_tree(item) for key, item in value.items())
    return False


def canonical(value):
    require(json_tree(value), "literal JSON tree required")
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected),
        "strict curvature certificate differs",
    )


def authenticate():
    raw, provenance = {}, []
    for name, (path, blob) in PINS.items():
        ref = f"{FREEZE}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "frozen byte cap")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(data) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "frozen source authentication",
        )
        raw[name] = data
        provenance.append({"commit": FREEZE, "path": path, "blob": blob})
    return raw, provenance


def source():
    raw, provenance = authenticate()
    namespace = {
        "__name__": "authenticated_curvature_span",
        "__file__": str(ROOT / PINS["scout"][0]),
    }
    exec(compile(raw["scout"], namespace["__file__"], "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace), json.loads(raw["discovery"]), provenance


def proof_table_control(module, data):
    records = data["complete_ordered_records"]
    require(
        len(records) == 63 and len(data["coefficient_columns"]) == 6,
        "complete proof-table domain",
    )
    for actual, (pair, monomial, positive) in zip(
        data["coefficient_columns"], TABLE, strict=True
    ):
        require(
            actual["coordinate_pair"] == list(pair)
            and actual["monomial"] == list(monomial),
            "proof basis order",
        )
        expected = []
        for row in records:
            n, m = row["n"], row["m"]
            expected.append(positive.get((n, m), -positive.get((m, n), F())))
        require(
            list(map(F, actual["complete_source_vector"])) == expected,
            "complete independent proof coordinate table",
        )
        module.coefficient_identities(expected, records)
    ratios = [(row["a"], row["b"]) for row in data["ratio_order"]]
    pivot_matrix = [
        [
            F(column["rational_ratio_image"][ratios.index(ratio)])
            for column in data["coefficient_columns"]
        ]
        for ratio in PIVOTS
    ]
    expected_matrix = [
        [PIVOT_VALUES[i] if i == j else F() for j in range(6)] for i in range(6)
    ]
    require(
        pivot_matrix == expected_matrix,
        "six physical ratio pivots with complete off-diagonal zeros",
    )
    pivot_determinant = module.determinant(pivot_matrix)
    require(pivot_determinant == F(-3, 32768), "weighted ratio pivot determinant")
    return {
        "all_63_signed_coordinates_checked": True,
        "ratio_pivots": [list(row) for row in PIVOTS],
        "rational_pivot_matrix": [
            [str(value) for value in row] for row in pivot_matrix
        ],
        "pivot_determinant": str(pivot_determinant),
    }


def build():
    module, frozen, provenance = source()
    current = module.discover()
    replay_equal(current, frozen)
    require(
        all(type(value) is bool and value for value in current["predictions"].values()),
        "all preregistered source predictions hold",
    )
    controls = proof_table_control(module, current)
    for key in (
        "coefficient_rank",
        "rationalized_observation_rank",
        "rectangle_rank",
        "rectangle_observation_rank",
    ):
        require(current[key]["rank"] == 6, "actual source and witness rank")
    require(
        F(current["rectangle_transition_determinant"]) == F(1, 8 * 64**6),
        "full six-witness transition",
    )
    bindings = {}
    for path in OWNED:
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.curvature_span_certificate.v1",
        "sources": provenance,
        "owned_sha256_lf": bindings,
        "acquisition_proof_object_sha256": current["proof_object_sha256"],
        "complete_native_acquisition": current,
        "independent_proof_table_and_pivots": controls,
        "scope": {
            "complete_finite_native_path_variation_span_dimension": 6,
            "original_physical_observation_injective_on_span": True,
            "each_coefficient_basis_vector_claimed_as_one_monotone_path_difference": False,
            "all_six_rectangle_differences_are_actual_paths": True,
            "arbitrary_affine_minimizer_attainment_claimed": False,
            "full_post_renewal_gamma_identified": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def check(candidate):
    replay_equal(candidate, build())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        output = (
            json.dumps(build(), sort_keys=True, indent=2, allow_nan=False) + "\n"
        ).encode()
        require(len(output) <= MAX_BYTES, "artifact byte cap")
        FIXTURE.write_bytes(output)
    else:
        data = FIXTURE.read_bytes()
        require(len(data) <= MAX_BYTES, "artifact byte cap")
        check(json.loads(data))
    print("PASS complete native curvature span certificate")


if __name__ == "__main__":
    main()
