#!/usr/bin/env python3
"""Exact source matrices, the four-prime atlas, and held-out KKT faces."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import pairwise
from math import comb
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "HIGHER_NATIVE_CLUSTER_ATLAS.md"
FIXTURE = HERE / "higher_native_cluster_certificate.json"
TEST = ROOT / "tests" / "test_native_six_hour_higher_cluster.py"
COMMIT = "0eb242a5ae1f0e29ab725587fc63a973ff6354c1"
SCOUT = "research/riemann-structures/native-six-hour/higher_cluster_scout.py"
SCOUT_BLOB = "0a7d3a66ebca252d099c76dd7409325e2eec2981"
DISCOVERY = "research/riemann-structures/native-six-hour/higher_cluster.discovery.json"
DISCOVERY_BLOB = "007e7b24e86b93b72f3eb0aa62f95bed40cecd2e"
PREREG = "research/riemann-structures/native-six-hour/HIGHER_CLUSTER_PREREGISTRATION.md"
PREREG_BLOB = "5fc2a6c600ea93f745e6e8915eb4d985acc17635"
CLUSTER_COMMIT = "004ffa7563372e3c00a197a12e13164bfd91e9da"
CLUSTER_NOTE = "research/riemann-structures/native-six-hour/CLUSTERED_NATIVE_ACTIVATION_SELECTION.md"
CLUSTER_NOTE_BLOB = "927cf75d92cf402d2807cb3d83ece88dc7f955cb"
CLUSTER_JSON = "research/riemann-structures/native-six-hour/clustered_native_activation_selection.json"
CLUSTER_JSON_BLOB = "584dcc19a04d47e4ab7f0803225f8389edbf54b9"
MAX_BYTES = 1048576


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(commit, path, blob):
    ref = f"{commit}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
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
    raw = frozen_bytes(COMMIT, SCOUT, SCOUT_BLOB)
    namespace = {
        "__name__": "authenticated_higher_source",
        "__file__": str(ROOT / SCOUT),
    }
    # Execute only exact frozen bytes after commit/blob authentication.
    exec(compile(raw, str(ROOT / SCOUT), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def atlas_matrix(shape):
    require(
        type(shape) is tuple
        and len(shape) == 4
        and all(type(x) is int and 0 <= x <= 12 for x in shape),
        "exact four-source shape cap",
    )
    require(all(a < b for a, b in pairwise(shape)), "strict source shape order")
    a, b, c = (right - left for left, right in pairwise(shape))
    reflected = c < a
    if reflected:
        a, c = c, a
    ones, cumulative, first, last = (
        (1, 1, 1, 1),
        (1, 1, 0, 0),
        (1, 0, 0, 0),
        (0, 0, 0, 1),
    )
    matrix = tuple(
        tuple(
            8 * (a + b + c)
            + 4 * b * (cumulative[i] * ones[j] + ones[i] * cumulative[j])
            - 8 * b * cumulative[i] * cumulative[j]
            - 8 * a * first[i] * first[j]
            + 4 * a * (first[i] * last[j] + last[i] * first[j])
            - 4 * (3 * c - a) * last[i] * last[j]
            + 2 * (c - a) * (last[i] * ones[j] + ones[i] * last[j])
            for j in range(4)
        )
        for i in range(4)
    )
    return (
        tuple(tuple(matrix[3 - i][3 - j] for j in range(4)) for i in range(4))
        if reflected
        else matrix
    )


def bilinear(matrix, left, right):
    require(len(matrix) == len(left) == len(right) <= 6, "bounded bilinear certificate")
    return sum(
        (
            F(matrix[i][j]) * left[i] * right[j]
            for i in range(len(matrix))
            for j in range(len(matrix))
        ),
        F(),
    )


def symmetric_reduction(matrix, arity):
    require(
        type(arity) is int and arity in (5, 6) and len(matrix) == arity,
        "held-out symmetric source reduction",
    )
    if arity == 5:
        base = (0, 0, 1, 0, 0)
        da, db = (1, 0, -2, 0, 1), (0, 1, -2, 1, 0)
        expected = (128, 8, 20, -32, -48, -32)
    else:
        base = (0, 0, F(1, 2), F(1, 2), 0, 0)
        da, db = (1, 0, -1, -1, 0, 1), (0, 1, -1, -1, 1, 0)
        expected = (625, -32, 0, -32, -32, -24)
    polynomial = (
        bilinear(matrix, base, base),
        2 * bilinear(matrix, base, da),
        2 * bilinear(matrix, base, db),
        bilinear(matrix, da, da),
        2 * bilinear(matrix, da, db),
        bilinear(matrix, db, db),
    )
    require(polynomial == expected, "independent exact symmetric polynomial")
    return {
        "monomials": ["1", "a", "b", "a^2", "a*b", "b^2"],
        "coefficients": [str(x) for x in polynomial],
    }


def source_constants(arity):
    require(type(arity) is int and 2 <= arity <= 32, "fixed-arity normalization cap")
    masses = tuple(comb(arity - 1, k - 1) for k in range(1, arity + 1))
    constant = sum(value**2 for value in masses)
    require(
        constant == comb(2 * arity - 2, arity - 1), "complete native band mass identity"
    )
    amplitude_square = F(4, 4**arity)
    require(
        2 * amplitude_square == F(8, 4**arity),
        "original cusp scale from actual two-ds amplitude",
    )
    return {
        "arity": arity,
        "band_masses": masses,
        "constant_band_mass": constant,
        "physical_amplitude_square_before_1_over_K": str(amplitude_square),
        "leading_multiplier_before_A_epsilon_over_K": str(2 * amplitude_square),
    }


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def build():
    module = scout_module()
    module.authenticate()
    discovery = json.loads(frozen_bytes(COMMIT, DISCOVERY, DISCOVERY_BLOB))
    frozen_bytes(COMMIT, PREREG, PREREG_BLOB)
    frozen_bytes(CLUSTER_COMMIT, CLUSTER_NOTE, CLUSTER_NOTE_BLOB)
    cluster = json.loads(frozen_bytes(CLUSTER_COMMIT, CLUSTER_JSON, CLUSTER_JSON_BLOB))
    require(
        cluster.get("schema") == "riemann.native_six_hour.cluster_selection.v1"
        and cluster["cusp"]["jump_squared_half_sum"] == ["144", "64"]
        and type(cluster["cusp"]["Taylor_remainder_constant"]) is int
        and cluster["cusp"]["Taylor_remainder_constant"] == 36
        and cluster["original_Mellin_measure_and_physical_normalization"] is True,
        "frozen original-kernel cusp and measure",
    )
    require(
        discovery.get("schema")
        == "riemann.native_six_hour.higher_cluster_discovery.v1",
        "frozen leading-source schema",
    )
    require(
        tuple(tuple(row["shape"]) for row in discovery["models"]) == module.PANELS,
        "complete preregistered panel list",
    )
    verified = []
    for original in discovery["models"]:
        shape = tuple(original["shape"])
        replay = module.discover(shape)
        replay_equal(replay, original)
        matrix, _, _ = module.matrices(shape)
        extra = {}
        if len(shape) == 4:
            require(
                matrix == atlas_matrix(shape),
                "symbolic four-source atlas equals full source matrix",
            )
            a, b, c = (right - left for left, right in pairwise(shape))
            large, small = max(a, c), min(a, c)
            optimum = F(8 * (a + b + c) + 2 * b) + F(
                2 * (large - small) ** 2, 3 * (2 * large - small)
            )
            gain = F(
                2 * large**2 + 5 * large * small - small**2, 12 * (2 * large - small)
            )
            require(
                F(replay["exact_objective"]) == optimum
                and F(replay["objective_gain"]) == gain,
                "closed four-source optimum and uniform gain",
            )
            extra = {
                "analytical_full_matrix_equal": True,
                "closed_optimum": str(optimum),
                "closed_gain": str(gain),
            }
        elif len(shape) in (5, 6):
            extra = {"symmetric_polynomial": symmetric_reduction(matrix, len(shape))}
            if len(shape) == 5:
                require(
                    replay["unique_activation"] == ["0", "5/16", "3/8", "5/16", "0"]
                    and replay["inactive_KKT_slacks"] == ["7/4", "0", "0", "0", "7/4"],
                    "strict five-source face",
                )
                extra["all_limiting_zero_activations_strict"] = True
            else:
                require(
                    replay["unique_activation"] == ["0", "0", "1/2", "1/2", "0", "0"]
                    and replay["inactive_KKT_slacks"] == ["8", "0", "0", "0", "0", "8"],
                    "mixed strict and zero six-source slacks",
                )
                extra["all_four_zeros_proved_stable_from_leading_order"] = False
        verified.append(
            {
                "shape": shape,
                "complete_source_matrix": matrix,
                "unique_activation": replay["unique_activation"],
                "inactive_KKT_slacks": replay["inactive_KKT_slacks"],
                "objective": replay["exact_objective"],
                "uniform_gain": replay["objective_gain"],
                "active_supports_checked": replay["all_active_supports_checked"],
                **extra,
            }
        )
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.higher_cluster_certificate.v1",
        "source_hashes": bindings,
        "sources": [
            {"commit": COMMIT, "path": path, "blob": blob}
            for path, blob in (
                (SCOUT, SCOUT_BLOB),
                (DISCOVERY, DISCOVERY_BLOB),
                (PREREG, PREREG_BLOB),
            )
        ]
        + [
            {"commit": CLUSTER_COMMIT, "path": CLUSTER_NOTE, "blob": CLUSTER_NOTE_BLOB},
            {"commit": CLUSTER_COMMIT, "path": CLUSTER_JSON, "blob": CLUSTER_JSON_BLOB},
        ]
        + [
            {"commit": module.OLD, "path": path, "blob": blob}
            for path, blob in module.SOURCES.items()
        ],
        "verified_panels": verified,
        "physical_source_constants": [source_constants(r) for r in range(2, 7)],
        "source_shape_wall_is_literal_distinct_prime_product_equality": False,
        "finite_kernel_remainder_replaced_by_leading_matrix": False,
        "all_arity_theorem_inferred_only_from_bounded_panels": False,
        "full_post_renewal_gamma_identified": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
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
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS higher native cluster certificate {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
