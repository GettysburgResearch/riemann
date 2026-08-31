#!/usr/bin/env python3
"""Proof-bound original-metric affine floor and complete source-feasibility controls."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
FREEZE = "46c8453e3976d242479202bf4d58489282a64d2a"
PINS = (
    ("NATIVE_AFFINE_PHYSICAL_FLOOR.md", "50cb1abef7865f540e8322f0609c2c6e3bdb2a83"),
    (
        "NATIVE_AFFINE_FLOOR_PREREGISTRATION.md",
        "c4b95ffd94439212ee37e5fb50f51002a3937637",
    ),
    ("native_affine_floor_scout.py", "e2ba2418fd842976d0a486db62c8a954baa7303a"),
    ("native_affine_floor.discovery.json", "350f264fb314d075388564089c04a080d8cb2c28"),
)
MAX_BYTES = 4 * 1024 * 1024
FIXTURE = HERE / "native_affine_floor_certificate.json"
OWNED = (
    HERE / "NATIVE_AFFINE_FLOOR_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_native_six_hour_affine_floor.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected),
        "typed complete affine replay mismatch",
    )


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def finite_float(value):
    result = float(value)
    require(math.isfinite(result), "nonfinite display value")
    return result


def no_nonfinite(_value):
    raise ValueError("nonfinite JSON value")


def read_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")
    return json.loads(
        raw,
        parse_float=finite_float,
        parse_constant=no_nonfinite,
        object_pairs_hook=unique_object,
    )


def rational(value):
    require(type(value) in (str, int, F), "literal exact rational value")
    if type(value) is str:
        require(len(value) <= 2500, "rational input character cap")
    result = F(value)
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= 4096,
        "exact rational bit cap",
    )
    return result


def interval(row):
    require(
        type(row) is dict and "lower" in row and "upper" in row,
        "rational endpoint interval",
    )
    lo, hi = rational(row["lower"]), rational(row["upper"])
    require(lo <= hi, "ordered rational interval")
    return lo, hi


def authenticate():
    sources, provenance = {}, []
    for name, expected in PINS:
        ref = f"{FREEZE}:{PREFIX}{name}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "frozen source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        blob = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
        require(size == len(raw) and blob == expected, "exact frozen affine source")
        if not name.endswith(".json"):
            current = (HERE / name).read_bytes()
            require(
                len(current) <= MAX_BYTES
                and current.replace(b"\r\n", b"\n") == raw.replace(b"\r\n", b"\n"),
                "frozen scout bound source changed",
            )
        sources[name] = raw
        provenance.append(
            {
                "commit": FREEZE,
                "path": PREFIX + name,
                "blob": blob,
                "sha256": sha256(raw).hexdigest(),
            }
        )
    return sources, provenance


def load_source():
    raw, provenance = authenticate()
    name = "native_affine_floor_scout.py"
    namespace = {
        "__name__": "authenticated_final_affine_scout",
        "__file__": str(HERE / name),
    }
    exec(compile(raw[name], str(HERE / name), "exec"), namespace)  # noqa: S102
    return (
        SimpleNamespace(**namespace),
        read_json(raw["native_affine_floor.discovery.json"]),
        provenance,
    )


def row_vector(row, size=6):
    require(type(row) in (list, tuple) and len(row) == size, "exact six-coordinate row")
    return [rational(x) for x in row]


def solve_exact(matrix, target):
    require(type(matrix) is list and len(matrix) == 6, "six-row exact system")
    rhs = row_vector(target)
    work = [row_vector(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for k in range(6):
        pivot = next((i for i in range(k, 6) if work[i][k]), None)
        require(pivot is not None, "exact physical source matrix rank six")
        work[k], work[pivot] = work[pivot], work[k]
        divisor = work[k][k]
        work[k] = [rational(x / divisor) for x in work[k]]
        for i in range(6):
            if i != k:
                multiple = work[i][k]
                work[i] = [
                    rational(x - multiple * y)
                    for x, y in zip(work[i], work[k], strict=True)
                ]
    return [row[6] for row in work]


def literal_pivot_rows(columns):
    require(
        type(columns) is list
        and len(columns) == 6
        and all(type(column) is list and len(column) == 63 for column in columns),
        "complete six by63 source columns",
    )
    pivots, chosen = {}, []
    for i in range(63):
        row = [rational(column[i]) for column in columns]
        for pivot in sorted(pivots):
            multiple = row[pivot]
            row = [
                rational(x - multiple * y)
                for x, y in zip(row, pivots[pivot], strict=True)
            ]
        first = next((j for j, x in enumerate(row) if x), None)
        if first is not None:
            divisor = row[first]
            pivots[first] = [rational(x / divisor) for x in row]
            chosen.append(i)
            if len(chosen) == 6:
                break
    require(len(chosen) == 6, "literal complete source rank six")
    return chosen


def source_coordinates(columns, reference, vector, pivots):
    require(
        type(reference) is list
        and type(vector) is list
        and len(reference) == len(vector) == 63,
        "all63 source path entries",
    )
    require(
        type(pivots) is list
        and len(pivots) == 6
        and all(type(i) is int and 0 <= i < 63 for i in pivots),
        "six literal source pivot indices",
    )
    differences = [
        rational(a) - rational(b) for a, b in zip(vector, reference, strict=True)
    ]
    system = [[rational(column[i]) for column in columns] for i in pivots]
    coordinates = solve_exact(system, [differences[i] for i in pivots])
    require(
        all(
            sum(coordinates[j] * rational(columns[j][i]) for j in range(6))
            == differences[i]
            for i in range(63)
        ),
        "reconstructed coordinates retain every source record",
    )
    return coordinates


def source_feasibility(replay, halfspaces):
    require(
        type(replay) is dict
        and len(replay["actual_paths"]) == 8
        and len(halfspaces) == 65,
        "fixed full source comparison coverage",
    )
    columns = [row["complete_source_vector"] for row in replay["basis_order"]]
    pivots = literal_pivot_rows(columns)
    reference = replay["actual_paths"][0]
    require(reference["name"] == "axis_235", "declared actual reference path")
    controls = []
    for row in replay["actual_paths"]:
        x = source_coordinates(
            columns, reference["complete_source"], row["complete_source"], pivots
        )
        slacks = []
        for name, coefficients, bound in halfspaces:
            slack = rational(bound) - sum(
                a * rational(b) for a, b in zip(x, coefficients, strict=True)
            )
            require(slack >= 0, "actual source path satisfies every declared halfspace")
            slacks.append({"name": name, "exact_slack": str(slack)})
        moments = list(x)
        moments[2] *= 2
        controls.append(
            {
                "name": row["name"],
                "coordinates_A_B_C_half_D_E_F": list(map(str, x)),
                "occupation_moments_A_B_C_D_E_F": list(map(str, moments)),
                "all63_source_records_reconstructed": True,
                "all65_halfspace_slacks": slacks,
            }
        )
    records = replay["complete_ordered_records"]
    fixed = [i for i, row in enumerate(records) if row["n"] == 16 * row["m"]]
    require(
        len(fixed) == 1 and (records[fixed[0]]["n"], records[fixed[0]]["m"]) == (16, 1),
        "unique fixed physical ratio16 record",
    )
    index = fixed[0]
    require(
        rational(reference["complete_source"][index]) == F(11, 64)
        and all(rational(column[index]) == 0 for column in columns),
        "literal fixed nonzero affine component",
    )
    return {
        "source_pivot_indices": pivots,
        "pivot_ordered_pairs": [[records[i]["n"], records[i]["m"]] for i in pivots],
        "actual_paths": controls,
        "fixed_ratio16": {
            "ordered_pair": [16, 1],
            "unweighted_coefficient": "11/64",
            "physical_amplitude": "11/256",
            "all_six_variations_zero": True,
        },
        "coordinate_reconstruction_used_as_metric": False,
    }


def certify_bounds(replay):
    floor = interval(replay["affine_energy_floor"])
    require(
        F(10220, 100) < floor[0] <= floor[1] < F(10222, 100),
        "affine floor102.20 to102.22",
    )
    best = rational(replay["best_single_halfspace_bound"]["certified_lower"])
    require(best > F(13877, 100), "actual-source universal lower bound138.77")
    winning = next(
        row
        for row in replay["halfspaces"]
        if row["name"] == replay["best_single_halfspace_bound"]["name"]
    )
    require(
        winning["status"] == "strictly_violated"
        and interval(winning["affine_violation"])[0] > 0,
        "winning source constraint strictly excludes affine optimum",
    )
    require(
        best == interval(winning["corrected_floor"])[0],
        "best lower endpoint belongs to actual certified constraint",
    )
    quadratic = next(
        row for row in replay["actual_paths"] if row["name"] == "quadratic_1_0_minus1"
    )
    upper = interval(quadratic["energy"])[1]
    require(upper < F(16056, 100), "actual quadratic upper bound160.56")
    require(
        all(best < interval(row["energy"])[0] for row in replay["actual_paths"]),
        "certified universal lower bound below every actual comparison",
    )
    moments = [interval(row) for row in replay["affine_occupation_moments"]]
    require(
        len(moments) == 6
        and moments[2][1] < -19
        and moments[1][0] > 3
        and moments[4][0] > 7,
        "affine optimum has impossible C,B,E source moments",
    )
    return {
        "affine_energy_interval": replay["affine_energy_floor"],
        "all_source_energy_strictly_greater_than": "13877/100",
        "certified_best_single_halfspace": replay["best_single_halfspace_bound"],
        "actual_quadratic_energy_strictly_less_than": "4014/25",
        "actual_quadratic_energy_interval": quadratic["energy"],
        "affine_moments_C_less_than_minus19_B_greater_than3_E_greater_than7": True,
        "all_path_infimum_bracket": {
            "strict_lower": "13877/100",
            "strict_upper": "4014/25",
        },
        "infimum_attainment_or_optimizer_claimed": False,
    }


def build():
    scout, frozen, provenance = load_source()
    replay = scout.discover()
    replay_equal(replay, frozen)
    require(
        replay["schema"] == "riemann.native_six_hour.affine_floor_discovery.v1",
        "exact complete affine discovery schema",
    )
    require(
        len(replay["complete_ordered_records"]) == 63
        and len(replay["basis_order"]) == 6,
        "complete source and curvature directions",
    )
    require(
        len(replay["positive_elimination_pivots"]) == 6
        and all(interval(row)[0] > 0 for row in replay["positive_elimination_pivots"]),
        "all six positive original-metric interval pivots",
    )
    feasibility = source_feasibility(replay, scout.halfspaces())
    bounds = certify_bounds(replay)
    result = {
        "schema": "riemann.native_six_hour.affine_floor_certificate.v1",
        "sources": provenance,
        "complete_primitive_replay": replay,
        "independent_literal_source_feasibility": feasibility,
        "certified_numerical_scope": bounds,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "scope": {
            "original_physical_Gram_metric": True,
            "all63_records_and_cross_frequency_terms_retained": True,
            "all65_preregistered_halfspaces_retained": True,
            "source_coordinate_pivots_replace_energy_metric": False,
            "affine_minimizer_is_native": False,
            "finite_panel_proves_all_path_optimum": False,
            "complete_retained_gamma_identified": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    require(len(canonical(result).encode()) <= MAX_BYTES, "final certificate byte cap")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "final fixture byte cap")
        replay_equal(read_json(FIXTURE.read_bytes()), result)
    print(
        canonical(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
