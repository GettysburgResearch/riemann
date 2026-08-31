"""Fresh resealed SC attacks and frozen scientific command replay."""

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
STEM = "theta_source_quotient_tensor_coherence"
spec = importlib.util.spec_from_file_location(
    "sc_hostile_target", ROOT / (DIR + STEM + ".py")
)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def change(path, value):
    def operation(r):
        target = r
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value

    return operation


def main():
    fixture_path = ROOT / (DIR + STEM + ".json")
    original = M.decode(fixture_path.read_bytes())
    mutations = [
        (
            "source_energy",
            change(["base_cells", 0, "source", "quotient", 0, 0, 0], "99"),
        ),
        (
            "vacuum_energy",
            change(["base_cells", 1, "vacuum", "quotient", 0, 0, 0], "99"),
        ),
        ("reciprocal", change(["base_cells", 2, "reciprocal_excess", 0, 0, 0], "0")),
        ("coordinate_map", change(["base_cells", 3, "transformed_pi", 0, 0, 1], "0")),
        ("tensor_weight", change(["tensor_cells", 0, "weight"], 1)),
        ("tensor_cross_term", change(["tensor_cells", 1, "excess", 0, 0, 0], "0")),
        ("sum_weight", change(["same_weight_sums", 0, "weight"], 3)),
        (
            "nested_lift",
            change(
                ["nested_chains", 0, "chains", 0, "stages", 0, "lift", 0, 0, 0], "99"
            ),
        ),
        ("averaging_variance", change(["averaging", 0, "variance", 0, 0, 0], "0")),
        ("averaging_equality", change(["averaging", 1, "common_lift"], False)),
        (
            "observation_polynomial",
            change(["observation", "numerator_ascending", 3], 0),
        ),
        ("unequal_weight", change(["unequal_weight_sum", "common_scalar"], True)),
        ("weak_tensor", change(["regularity_failure", "local_L1_tensor_closed"], True)),
        (
            "tensor_class",
            change(
                ["contract", "tensor_closed_source_class"], "all locally integrable"
            ),
        ),
        ("source_pin", change(["sources", 0, "commit"], "0" * 40)),
        ("no_scope_firewall", change(["not_claimed"], [])),
    ]
    rejected = []
    for name, modify in mutations:
        trial = copy.deepcopy(original)
        modify(trial)
        trial.pop("payload_sha256")
        trial["payload_sha256"] = M.digest(M.canonical(trial))
        try:
            M.check(trial)  # No fixture/build/authentication mocking.
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError("accepted fresh resealed attack: " + name)
    runs = []
    prefix = [sys.executable, "-B"] + ([] if __debug__ else ["-O"])
    for option, suffix in (
        ("--emit", ".json"),
        ("--emit-sources", ".sources.json"),
        ("--check", None),
    ):
        proc = subprocess.run(
            prefix + [DIR + STEM + ".py", option],
            cwd=ROOT,
            capture_output=True,
            check=True,
        )
        if suffix:
            need(
                M.lf(proc.stdout) == M.lf((ROOT / (DIR + STEM + suffix)).read_bytes()),
                "canonical emitted bytes differ",
            )
        runs.append({"mode": option, "stdout_sha256_lf": M.digest(M.lf(proc.stdout))})
    need(
        M.lf(fixture_path.read_bytes()) == M.lf(M.canonical(original))
        or M.decode(fixture_path.read_bytes()) == original,
        "fixture changed",
    )
    print(
        json.dumps(
            {
                "schema": "SC-hostile-independent-replay-v1",
                "science_head": "b0e3b18e690accdee6d77b3b3c4c68850f6cb671",
                "optimized": not __debug__,
                "fresh_resealed_attacks_rejected": rejected,
                "producer_replays": runs,
                "status": "PASS",
                "script_sha256_lf": hashlib.sha256(
                    M.lf(Path(__file__).read_bytes())
                ).hexdigest(),
            },
            sort_keys=True,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
