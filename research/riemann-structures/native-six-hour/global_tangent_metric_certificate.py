#!/usr/bin/env python3
"""Authenticated complete-path replay and literal tangent/translation witnesses."""

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
NOTE = HERE / "GLOBAL_NATIVE_TANGENT_METRIC.md"
FIXTURE = HERE / "global_tangent_metric_certificate.json"
TEST = ROOT / "tests/test_native_six_hour_tangent_metric.py"
COMMIT = "b3a8a85021cedefae034aaef7c14a6976429142b"
SCOUT = "research/riemann-structures/native-six-hour/global_tangent_metric_scout.py"
SCOUT_BLOB = "07d13eb8ca1d8999c81bbb2a74feeefd25ea2f99"
DISCOVERY = (
    "research/riemann-structures/native-six-hour/global_tangent_metric.discovery.json"
)
DISCOVERY_BLOB = "ebfd564898fb897aaff8e49743af8c299b295eea"
PREREG = "research/riemann-structures/native-six-hour/GLOBAL_TANGENT_METRIC_PREREGISTRATION.md"
PREREG_BLOB = "0d39d9ce308c83cf8f8aa09d897da102667f3902"
MAX_BYTES = 2097152


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected), "typed canonical source replay"
    )


def frozen_bytes(path, blob):
    require(len(COMMIT) == len(blob) == 40, "completed exact discovery freeze")
    ref = f"{COMMIT}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "frozen source byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen source authentication",
    )
    return raw


def scout_module():
    raw = frozen_bytes(SCOUT, SCOUT_BLOB)
    namespace = {
        "__name__": "authenticated_tangent_metric_scout",
        "__file__": str(ROOT / SCOUT),
    }
    # Execute only exact source bytes after commit/blob authentication.
    exec(compile(raw, str(ROOT / SCOUT), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def literal_mixed_square(left, right):
    require(
        type(left) in (int, F)
        and type(right) in (int, F)
        and -1 <= left <= 1
        and -1 <= right <= 1,
        "exact admissible mixed-square source parameters",
    )
    left, right = F(left), F(right)
    return -F(1, 12) - (right - left) * (5 + left) / 240


def tangent_witnesses(source):
    expected_rows = ((F(1, 3), 12, (1, -1, 0)), (F(1, 5), 20, (1, 0, -1)))
    fields = {p: source.native_field(p)[1] for p in source.PRIMES}
    result = []
    for ratio, K, incidence in expected_rows:
        expected = [
            source.rs(source.sqrt_rational(F(1, K)), F(sign, 48)) for sign in incidence
        ]
        actual = [fields[p][ratio][1] for p in source.PRIMES]
        require(actual == expected, "independent physical rank-two tangent witnesses")
        result.append(
            {
                "ratio": str(ratio),
                "physical_product": K,
                "integer_incidence_after_multiplying_48_sqrtK": incidence,
                "exact_tangent_coefficients": [
                    {str(d): str(x) for d, x in row.items()} for row in actual
                ],
            }
        )
    return result


def build():
    scout = scout_module()
    discovery = json.loads(frozen_bytes(DISCOVERY, DISCOVERY_BLOB))
    frozen_bytes(PREREG, PREREG_BLOB)
    require(
        discovery["schema"]
        == "riemann.native_six_hour.global_tangent_metric_discovery.v1",
        "executed complete tangent-metric discovery",
    )
    source = scout.frozen_module()
    baseline, _, selected, tangent = scout.tangent_metric(source)
    replay_equal(tangent, discovery["tangent"])
    baseline_energy = scout.inner(source, baseline, baseline)
    require(len(discovery["all_fixed_paths"]) == 18, "all preregistered paths retained")
    paths = []
    energy_by_parameters = {}
    for original in discovery["all_fixed_paths"]:
        parameters = tuple(map(F, original["epsilon"]))
        replay, _, energy = scout.result_for_path(
            source, parameters, baseline, baseline_energy
        )
        replay_equal(replay, original)
        for n, m, p in ((2, 6, 1), (2, 10, 2)):
            record = next(
                row for row in replay["all63_records"] if (row["n"], row["m"]) == (n, m)
            )
            require(
                F(record["coefficient_before_physical_weight"])
                == literal_mixed_square(parameters[0], parameters[p]),
                "literal polynomial integration versus closed mixed-square formula",
            )
        paths.append(replay)
        energy_by_parameters[parameters] = energy
    common = []
    for value in (F(1, 2), F(-1, 2)):
        _, field, _, _ = scout.native_field(source, (value, value, value))
        require(field == baseline, "actual common reparameterization invariance")
        common.append({"epsilon": str(value), "complete_current_unchanged": True})
    replay_equal(common, discovery["common_reparameterization_controls"])
    first, second = (F(1, 2), F(), F(-1, 2)), (F(3, 4), F(1, 4), F(-1, 4))
    _, f1, _, _ = scout.native_field(source, first)
    _, f2, _, _ = scout.native_field(source, second)
    defect = scout.field_add(source, f2, f1, -1)
    expected = source.rs(source.sqrt_rational(F(1, 12)), F(1, 1920))
    require(
        defect[F(1, 3)] == expected,
        "nonlinear obstruction in original coalesced readout",
    )
    obstruction = {
        "first": [str(x) for x in first],
        "second": [str(x) for x in second],
        "literal_2_6_difference": "1/1920",
        "exact_ratio_one_third_difference": {
            str(d): str(x) for d, x in expected.items()
        },
        "observed_squared_defect_interval": source.interval_json(
            source.ei(scout.inner(source, defect, defect))
        ),
    }
    replay_equal(obstruction, discovery["nonlinear_common_translation_obstruction"])
    comparisons = []
    best_axis = energy_by_parameters[(F(), F(), F(-1))]
    for values, energy in energy_by_parameters.items():
        comparison = source.ea(best_axis, source.es(energy, -1))
        comparisons.append(
            {
                "epsilon": [str(x) for x in values],
                "best_frozen_axis_minus_energy_interval": source.interval_json(
                    source.ei(comparison)
                ),
            }
        )
    replay_equal(comparisons, discovery["comparison_to_frozen_best_axis"])
    result = {
        "schema": "riemann.native_six_hour.global_tangent_metric_certificate.v1",
        "sources": [
            {"commit": COMMIT, "path": SCOUT, "blob": SCOUT_BLOB},
            {"commit": COMMIT, "path": DISCOVERY, "blob": DISCOVERY_BLOB},
            {"commit": COMMIT, "path": PREREG, "blob": PREREG_BLOB},
            {"commit": scout.COMMIT, "path": scout.SOURCE, "blob": scout.SOURCE_BLOB},
        ],
        "original_metric_tangent": tangent,
        "literal_physical_rank_witnesses": tangent_witnesses(source),
        "declared_selected_direction": [str(x) for x in selected],
        "all18_shared_source_paths": paths,
        "comparison_to_best_frozen_axis": comparisons,
        "nonlinear_common_translation_obstruction": obstruction,
        "source_current_global_affine_augmentation_claimed": False,
        "full_path_optimality_claimed": False,
        "complete_retained_gamma_identified": False,
        "owned_sha256_lf": {
            "note": sha256(NOTE.read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
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
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
