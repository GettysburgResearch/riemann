#!/usr/bin/env python3
"""Full native face replay and independent three-phase boundary-layer controls."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "FOUR_PRIME_NATIVE_BOUNDARY_LAYER.md"
FIXTURE = HERE / "boundary_layer_certificate.json"
TEST = ROOT / "tests/test_native_six_hour_boundary_layer.py"
COMMIT = "a5e4bb182ca8c7629938cc43a47eece70c61e7ae"
SCOUT = "research/riemann-structures/native-six-hour/boundary_layer_kernel_scout.py"
SCOUT_BLOB = "ad2b526960e0d170a9643c61a0e83fc4ac449f1a"
DISCOVERY = (
    "research/riemann-structures/native-six-hour/boundary_layer_kernel.discovery.json"
)
DISCOVERY_BLOB = "23d7b6ae6ec3c52571bac2a89b79417c46c9a887"
PROOF_SOURCES = (
    (
        "755b27c2c9747f3db255238c59c2622dee6cad8b",
        "research/riemann-structures/native-six-hour/HIGHER_NATIVE_CLUSTER_ATLAS.md",
        "13ddf1515da1913008290a75465f77cc137e7728",
    ),
    (
        "2e772b2048a00af9b6d59aa594f2e64ec96a5529",
        "research/riemann-structures/native-six-hour/SECOND_ORDER_NATIVE_FACE_SELECTION.md",
        "eb6d54a9e82b5d8e5cfd64e2d7929c6a3fa76f37",
    ),
)
MAX_BYTES = 2097152


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed exact native replay")


def frozen(path, blob):
    require(len(COMMIT) == len(blob) == 40, "completed exact kernel discovery freeze")
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
    require(0 < size <= MAX_BYTES, "bounded authenticated native source")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact native source authentication",
    )
    return raw


def scout_module():
    raw = frozen(SCOUT, SCOUT_BLOB)
    namespace = {
        "__name__": "authenticated_boundary_layer_scout",
        "__file__": str(ROOT / SCOUT),
    }
    # The executable bytes are checked against the declared frozen commit/blob first.
    exec(compile(raw, str(ROOT / SCOUT), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def dimensionless_phase(z):
    """z=4h/C; endpoint masses U=16a*u/C,V=16a*v/C."""
    require(type(z) in (int, F) and -8 <= z <= 8, "bounded exact boundary parameter")
    z = F(z)
    require(
        max(z.numerator.bit_length(), z.denominator.bit_length()) <= 64,
        "boundary parameter bit cap",
    )
    reflected = z < 0
    z = abs(z)
    if z in (1, 3):
        return {
            "z": str(-z if reflected else z),
            "threshold_case": True,
            "exact_finite_zero_pattern_assigned": False,
        }
    if z < 1:
        u, v, active = F(), F(), ()
    elif z < 3:
        u, v, active = F(), z - 1, (1,)
    else:
        u, v, active = F(2, 3) * (z - 3), F(2, 3) * (2 * z - 3), (0, 1)
    derivatives = (-u + v / 2 - 1, u / 2 - v + z - 1)
    require(
        all(
            value == 0 if i in active else value < 0
            for i, value in enumerate(derivatives)
        ),
        "every limiting KKT equation and strict inactive sign",
    )
    if reflected:
        u, v = v, u
        derivatives = derivatives[::-1]
        active = tuple(sorted(1 - i for i in active))
    return {
        "z": str(-z if reflected else z),
        "threshold_case": False,
        "dimensionless_endpoint_masses": [str(u), str(v)],
        "all_dimensionless_gradients": [str(x) for x in derivatives],
        "active_endpoint_indices": active,
        "reflection_applied": reflected,
        "finite_zero_pattern_requires_uniform_separation_from_thresholds": True,
    }


def second_moment_control(a, b):
    require(
        type(a) is int and type(b) is int and 1 <= a <= 8 and 1 <= b <= 8,
        "bounded independent source shape control",
    )
    shape = (0, a, a + b, 2 * a + b)
    J = [[0] * 4 for _ in range(4)]
    count = 0
    for k in range(1, 5):
        supports = tuple(combinations(range(4), k))
        for left in supports:
            for right in supports:
                count += 1
                difference = sum(shape[i] for i in left) - sum(shape[i] for i in right)
                for i in left:
                    for j in right:
                        J[i][j] += difference**2
    gradient = [J[i][1] + J[i][2] for i in range(4)]
    gaps = [x - gradient[1] for x in gradient]
    expected = [-4 * a * (a + b), 0, 0, -4 * a * (a + b)]
    require(
        count == 69 and gaps == expected,
        "independent full source second-moment normalization",
    )
    return {
        "a": a,
        "b": b,
        "shape": shape,
        "all69_ordered_source_pairs": count,
        "exact_second_moment_matrix": J,
        "endpoint_gradient_gaps": gaps,
    }


def build():
    scout = scout_module()
    for commit, path, blob in PROOF_SOURCES:
        scout.frozen_bytes(commit, path, blob)
    discovery = json.loads(frozen(DISCOVERY, DISCOVERY_BLOB))
    require(
        discovery["schema"]
        == "riemann.native_six_hour.boundary_layer_kernel_discovery.v1"
        and not discovery["acquisition_failed"],
        "executed actual-prime kernel test",
    )
    prototype = scout.load_module(
        scout.PROTOTYPE_COMMIT, scout.PROTOTYPE_PATH, scout.PROTOTYPE_BLOB
    )
    kernel = prototype.load_module(
        prototype.KERNEL_COMMIT, prototype.KERNEL_PATH, prototype.KERNEL_BLOB
    )
    kernel.authenticate()
    prototype.frozen_bytes(prototype.OLD, prototype.GE_PATH, prototype.GE_BLOB)
    acquisition = json.loads(
        scout.frozen_bytes(
            scout.ACQUISITION_COMMIT, scout.ACQUISITION_PATH, scout.ACQUISITION_BLOB
        )
    )
    prime_scout = scout.load_module(
        scout.ACQUISITION_COMMIT, scout.PRIME_PATH, scout.PRIME_BLOB
    )
    scout.frozen_bytes(scout.ACQUISITION_COMMIT, scout.PREREG_PATH, scout.PREREG_BLOB)
    prime_source = prime_scout.prime_module()
    for multiplier, row in zip(
        prime_scout.MULTIPLIERS, acquisition["windows"], strict=True
    ):
        replay_equal(prime_scout.window(prime_source, multiplier), row)
    require(
        len(discovery["models"]) == 3, "old control and exactly two new source tuples"
    )
    models = []
    for original in discovery["models"]:
        primes, predicted = (
            tuple(original["primes"]),
            tuple(original["predicted_support"]),
        )
        require(
            all(prime_source.prime(p) for p in primes),
            "every literal prime independently verified",
        )
        replay = scout.panel(prototype, kernel, primes, predicted)
        replay_equal(replay, original)
        models.append(replay)
    result = {
        "schema": "riemann.native_six_hour.boundary_layer_certificate.v1",
        "sources": [
            {"commit": COMMIT, "path": SCOUT, "blob": SCOUT_BLOB},
            {"commit": COMMIT, "path": DISCOVERY, "blob": DISCOVERY_BLOB},
        ]
        + discovery["sources"]
        + [
            {"commit": commit, "path": path, "blob": blob}
            for commit, path, blob in PROOF_SOURCES
        ],
        "all_original_kernel_face_models": models,
        "independent_dimensionless_phase_controls": [
            dimensionless_phase(z)
            for z in (F(-4), F(-2), F(-1, 2), F(0), F(1, 2), F(2), F(4), F(1), F(3))
        ],
        "independent_original_source_moment_controls": [
            second_moment_control(a, b) for a, b in ((1, 1), (2, 3), (1, 4), (5, 2))
        ],
        "threshold_equality_cases_resolved": False,
        "uniformity_claimed_without_threshold_separation": False,
        "native_measure_replaced": False,
        "full_retained_gamma_identified": False,
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
        require(FIXTURE.stat().st_size <= MAX_BYTES, "bounded replay artifact")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
