#!/usr/bin/env python3
"""Original-kernel KKT certificates and the source second-order face selection."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations
from math import comb
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "SECOND_ORDER_NATIVE_FACE_SELECTION.md"
FIXTURE = HERE / "native_finite_face_certificate.json"
TEST = ROOT / "tests" / "test_native_six_hour_finite_face.py"
COMMIT = "e44e99b59593eacc943ac526193516357d25d34e"
SCOUT = "research/riemann-structures/native-six-hour/native_finite_face_scout.py"
SCOUT_BLOB = "4a89777b8a04815799df2d147ceec98cb3394856"
DISCOVERY = (
    "research/riemann-structures/native-six-hour/native_finite_face.discovery.json"
)
DISCOVERY_BLOB = "ec786d04f7c26a36dcd01634e8e7315eb562b563"
HIGHER_COMMIT = "755b27c2c9747f3db255238c59c2622dee6cad8b"
HIGHER_NOTE = (
    "research/riemann-structures/native-six-hour/HIGHER_NATIVE_CLUSTER_ATLAS.md"
)
HIGHER_NOTE_BLOB = "13ddf1515da1913008290a75465f77cc137e7728"
HIGHER_JSON = (
    "research/riemann-structures/native-six-hour/higher_native_cluster_certificate.json"
)
HIGHER_JSON_BLOB = "ced1a86e2923f8cdbddf94f0166c6f23d56cf1f0"
MAX_BYTES = 2097152


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def frozen_bytes(commit, path, blob):
    require(len(commit) == len(blob) == 40, "completed exact source freeze")
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
    require(0 < size <= MAX_BYTES, "bounded frozen source")
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
        "__name__": "authenticated_finite_face_scout",
        "__file__": str(ROOT / SCOUT),
    }
    # Execute only exact commit/blob-authenticated discovery bytes.
    exec(compile(raw, str(ROOT / SCOUT), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def second_order_control(arity):
    """Direct ordered-subset moments, independently of the actual-kernel scout."""
    require(
        type(arity) is int and arity in (4, 6),
        "four- or six-source second-order control",
    )
    H = [[0] * arity for _ in range(arity)]
    J = [[0] * arity for _ in range(arity)]
    pair_count = 0
    for k in range(1, arity + 1):
        supports = tuple(combinations(range(arity), k))
        for left in supports:
            for right in supports:
                pair_count += 1
                delta = sum(left) - sum(right)
                for i in left:
                    for j in right:
                        H[i][j] += abs(delta)
                        J[i][j] += delta**2
    active = (arity // 2 - 1, arity // 2)
    h_gradient = [H[i][active[0]] + H[i][active[1]] for i in range(arity)]
    j_gradient = [J[i][active[0]] + J[i][active[1]] for i in range(arity)]
    h_gap = [x - h_gradient[active[0]] for x in h_gradient]
    j_gap = [x - j_gradient[active[0]] for x in j_gradient]
    expected_h = [0, 0, 0, 0] if arity == 4 else [-16, 0, 0, 0, 0, -16]
    expected_j = [-8, 0, 0, -8] if arity == 4 else [-168, -56, 0, 0, -56, -168]
    require(
        h_gap == expected_h and j_gap == expected_j,
        "all individual second-order KKT gaps",
    )
    coefficient = sum(
        2
        * choose(arity - 1, k - 1)
        * (
            choose(arity - 1, k - 1)
            - 3 * choose(arity - 2, k - 2)
            + 2 * choose(arity - 3, k - 3)
        )
        for k in range(1, arity + 1)
    )
    closed = -F(2 * comb(2 * arity - 4, arity - 2), arity - 1)
    require(
        coefficient == closed, "independent inclusion-count second moment coefficient"
    )
    require(
        pair_count == comb(2 * arity, arity) - 1,
        "complete ordered same-band source count",
    )
    return {
        "arity": arity,
        "leading_H_matrix": H,
        "quadratic_J_matrix": J,
        "all_H_gradient_gaps": h_gap,
        "all_J_gradient_gaps": j_gap,
        "reflection_fixed_X2_coefficient": str(closed),
        "ordered_pair_count": pair_count,
        "normalized_order_epsilon_gap_multipliers_before_1_over_A": [
            72 * x for x in j_gap
        ],
    }


def face_source_records(arity, central_powers=(1, 1)):
    """Actual two-stage squarefree path: inactive first, central pair second."""
    require(type(arity) is int and arity in (4, 6), "bounded original source arity")
    require(
        type(central_powers) is tuple
        and len(central_powers) == 2
        and all(type(a) is int and 1 <= a <= 16 for a in central_powers),
        "bounded positive source path powers",
    )
    active = (arity // 2 - 1, arity // 2)
    total = sum(central_powers)
    rows = []
    for k in range(arity + 1):
        for support in combinations(range(arity), k):
            sites = [
                F(2 * (-1) ** arity * central_powers[j], 2**arity * total)
                if active[j] in support
                else F()
                for j in range(2)
            ]
            rows.append(
                {
                    "support": support,
                    "second_stage_integrated_sites": [str(x) for x in sites],
                    "actual_two_ds_coefficient": str(sum(sites, F())),
                }
            )
    require(len(rows) == 2**arity, "zero activations do not delete factor allocations")
    return {
        "arity": arity,
        "central_powers": central_powers,
        "all_source_records": rows,
        "first_stage_full_monomial_coefficient": "0",
        "native_measure": "2 ds",
        "inactive_prime_factors_deleted": False,
    }


def cusp_control(kernel):
    endpoint0, endpoint1 = kernel.q(108, 48), kernel.q(72, 72)
    require(
        kernel.qi(endpoint0)[1] < 180 and kernel.qi(endpoint1)[1] < 180,
        "native third derivative endpoint bound",
    )
    return {
        "cusp_A_Q_sqrt2": [144, 64],
        "Gamma_second_derivative_at_zero": -72,
        "third_derivative_endpoints_Q_sqrt2": [[108, 48], [72, 72]],
        "third_derivative_absolute_bound": 180,
        "cubic_Taylor_remainder_bound": 30,
        "ideal_frequency_comparison_is_a_literal_prime_tuple": False,
    }


def build():
    scout = scout_module()
    discovery = json.loads(frozen_bytes(COMMIT, DISCOVERY, DISCOVERY_BLOB))
    require(
        discovery["schema"] == "riemann.native_six_hour.finite_face_discovery.v1"
        and not discovery["acquisition_failed"],
        "executed actual-prime discovery",
    )
    frozen_bytes(HIGHER_COMMIT, HIGHER_NOTE, HIGHER_NOTE_BLOB)
    higher = json.loads(frozen_bytes(HIGHER_COMMIT, HIGHER_JSON, HIGHER_JSON_BLOB))
    require(type(higher) is dict, "frozen leading source atlas")
    kernel = scout.load_module(
        scout.KERNEL_COMMIT, scout.KERNEL_PATH, scout.KERNEL_BLOB
    )
    kernel.authenticate()
    acquisition = json.loads(
        scout.frozen_bytes(
            scout.ACQUISITION_COMMIT, scout.ACQUISITION_PATH, scout.ACQUISITION_BLOB
        )
    )
    prime_source = scout.load_module(
        scout.ACQUISITION_COMMIT, scout.PRIME_PATH, scout.PRIME_BLOB
    )
    scout.frozen_bytes(scout.ACQUISITION_COMMIT, scout.PREREG_PATH, scout.PREREG_BLOB)
    scout.frozen_bytes(scout.OLD, scout.GE_PATH, scout.GE_BLOB)
    require(len(acquisition["windows"]) == 6, "six preregistered actual windows")
    for i, row in enumerate(acquisition["windows"]):
        replay_equal(prime_source.window(i), row)
    primes = tuple(row["first_prime"] for row in acquisition["windows"])
    models = [scout.panel(kernel, primes[:4]), scout.panel(kernel, primes)]
    replay_equal(models, discovery["models"])
    result = {
        "schema": "riemann.native_six_hour.finite_face_certificate.v1",
        "sources": [
            {"commit": COMMIT, "path": SCOUT, "blob": SCOUT_BLOB},
            {"commit": COMMIT, "path": DISCOVERY, "blob": DISCOVERY_BLOB},
            {"commit": HIGHER_COMMIT, "path": HIGHER_NOTE, "blob": HIGHER_NOTE_BLOB},
            {"commit": HIGHER_COMMIT, "path": HIGHER_JSON, "blob": HIGHER_JSON_BLOB},
        ]
        + discovery["sources"],
        "actual_original_kernel_models": models,
        "independent_second_order_controls": [second_order_control(r) for r in (4, 6)],
        "actual_source_path_controls": [
            face_source_records(r, powers)
            for r in (4, 6)
            for powers in ((1, 1), (2, 3))
        ],
        "native_cubic_kernel_control": cusp_control(kernel),
        "cofinal_prime_theorem_requires_uniform_shrinking_interval_PNT": False,
        "exact_finite_KKT_replaced_by_asymptotic_surrogate": False,
        "all_inactive_prime_factors_deleted": False,
        "full_post_renewal_gamma_identified": False,
        "file_sha256": {
            "note": sha256(NOTE.read_bytes()).hexdigest(),
            "producer": sha256(Path(__file__).read_bytes()).hexdigest(),
            "tests": sha256(TEST.read_bytes()).hexdigest(),
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
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(
        json.dumps(
            {
                "status": "PASS",
                "proof_object_sha256": result["proof_object_sha256"],
                "exact_finite_faces": [
                    m["unique_full_source_simplex_minimizer_certified"]
                    for m in result["actual_original_kernel_models"]
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
