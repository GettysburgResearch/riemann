#!/usr/bin/env python3
"""All15 original-kernel activation faces on fixed actual boundary-layer primes."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1
from itertools import combinations
from math import prod
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PROTOTYPE_COMMIT = "e44e99b59593eacc943ac526193516357d25d34e"
PROTOTYPE_PATH = (
    "research/riemann-structures/native-six-hour/native_finite_face_scout.py"
)
PROTOTYPE_BLOB = "4a89777b8a04815799df2d147ceec98cb3394856"
ACQUISITION_COMMIT = "5f0cc1cb0231901d15dafaa8d7d4fcbb3c25b508"
ACQUISITION_PATH = (
    "research/riemann-structures/native-six-hour/boundary_layer_prime_acquisition.json"
)
ACQUISITION_BLOB = "a5587b96bf621133c6fcb112483abcec858e9cdb"
PRIME_PATH = "research/riemann-structures/native-six-hour/boundary_layer_prime_scout.py"
PRIME_BLOB = "c0f073e211c923eebe9119c718ca2d3bef09c39a"
PREREG_PATH = (
    "research/riemann-structures/native-six-hour/BOUNDARY_LAYER_PREREGISTRATION.md"
)
PREREG_BLOB = "2085e359f908e39fefa0df1d6c46854d1cb329f4"
MAX_BYTES = 2097152
INTERVAL_BITS = 512


def require(condition, message):
    if not condition:
        raise ValueError(message)


def frozen_bytes(commit, path, blob):
    require(len(commit) == len(blob) == 40, "completed fixed discovery freeze")
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
    require(0 < size <= MAX_BYTES, "bounded frozen source size")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen source authentication",
    )
    return raw


def load_module(commit, path, blob):
    raw = frozen_bytes(commit, path, blob)
    namespace = {
        "__name__": "authenticated_boundary_source",
        "__file__": str(ROOT / path),
    }
    # Execute only the exact declared commit/blob-authenticated source.
    exec(compile(raw, str(ROOT / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def rounded(value):
    require(
        type(value) is tuple
        and len(value) == 2
        and all(type(x) is F for x in value)
        and value[0] <= value[1],
        "ordered exact interval bounds",
    )
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 131072
            for x in value
        ),
        "explicit pre-rounding arithmetic bit cap",
    )
    scale = 1 << INTERVAL_BITS
    lower = F((value[0].numerator * scale) // value[0].denominator, scale)
    upper = F(-((-value[1].numerator * scale) // value[1].denominator), scale)
    require(lower <= value[0] <= value[1] <= upper, "outward interval containment")
    return lower, upper


def point(value):
    require(type(value) in (int, F), "exact interval point")
    return rounded((F(value), F(value)))


def plus(a, b):
    return rounded((a[0] + b[0], a[1] + b[1]))


def negative(a):
    return -a[1], -a[0]


def times(a, b):
    products = tuple(x * y for x in a for y in b)
    return rounded((min(products), max(products)))


def inverse(a):
    require(a[0] > 0 or a[1] < 0, "certified nonzero interval inverse")
    return rounded((min(1 / a[0], 1 / a[1]), max(1 / a[0], 1 / a[1])))


def determinant(matrix):
    n = len(matrix)
    require(
        n <= 3 and all(len(row) == n for row in matrix),
        "at most3x3 tangent determinant",
    )
    if not n:
        return point(1)
    if n == 1:
        return matrix[0][0]
    result = point(0)
    for j in range(n):
        minor = tuple(tuple(row[k] for k in range(n) if k != j) for row in matrix[1:])
        term = times(matrix[0][j], determinant(minor))
        result = plus(result, term if j % 2 == 0 else negative(term))
    return result


def interval_json(value):
    value = rounded(value)
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 2048
            for x in value
        ),
        "bounded dyadic interval serialization",
    )
    return {
        "lower": str(value[0]),
        "upper": str(value[1]),
        "approximate_midpoint": float((value[0] + value[1]) / 2),
        "outward_dyadic_bits": INTERVAL_BITS,
    }


def difference(kernel, left, right):
    return kernel.ea(left, kernel.es(right, -1))


def face(kernel, gram, support):
    require(
        type(support) is tuple
        and support
        and len(support) <= 4
        and tuple(sorted(set(support))) == support
        and all(type(i) is int and 0 <= i < 4 for i in support),
        "one of15 nonempty original supports",
    )
    reference, free = support[-1], support[:-1]
    tangent = tuple(
        tuple(
            rounded(
                kernel.ei(
                    kernel.ea(
                        difference(
                            kernel,
                            difference(kernel, gram[i][j], gram[i][reference]),
                            gram[reference][j],
                        ),
                        gram[reference][reference],
                    )
                )
            )
            for j in free
        )
        for i in free
    )
    rhs = tuple(
        rounded(
            kernel.ei(
                difference(kernel, gram[reference][reference], gram[i][reference])
            )
        )
        for i in free
    )
    leading = [
        determinant(tuple(tuple(tangent[i][j] for j in range(k)) for i in range(k)))
        for k in range(1, len(free) + 1)
    ]
    if any(bound[0] <= 0 for bound in leading):
        return {
            "support": support,
            "positive_tangent_metric_certified": False,
            "leading_minor_intervals": [interval_json(x) for x in leading],
            "full_KKT_certified": False,
        }
    denom = determinant(tangent)
    q = [point(0) for _ in range(4)]
    for column, i in enumerate(free):
        replacement = tuple(
            tuple(
                rhs[row] if j == column else tangent[row][j] for j in range(len(free))
            )
            for row in range(len(free))
        )
        q[i] = times(determinant(replacement), inverse(denom))
    q[reference] = point(1)
    for i in free:
        q[reference] = plus(q[reference], negative(q[i]))
    feasible = all(q[i][0] > 0 for i in support)
    inactive = []
    for i in range(4):
        if i in support:
            continue
        slack = point(0)
        for j in support:
            coefficient = rounded(
                kernel.ei(difference(kernel, gram[i][j], gram[reference][j]))
            )
            slack = plus(slack, times(coefficient, q[j]))
        inactive.append(
            {
                "coordinate": i,
                "half_gradient_slack": interval_json(slack),
                "strict_positive": slack[0] > 0,
                "strict_negative": slack[1] < 0,
            }
        )
    energy = point(0)
    for i in support:
        for j in support:
            energy = plus(
                energy, times(rounded(kernel.ei(gram[i][j])), times(q[i], q[j]))
            )
    return {
        "support": support,
        "positive_tangent_metric_certified": True,
        "leading_minor_intervals": [interval_json(x) for x in leading],
        "activation_intervals": [interval_json(x) for x in q],
        "all_active_masses_strictly_positive": feasible,
        "all_active_stationarity_equations_exact_by_Cramer_definition": True,
        "all_inactive_KKT": inactive,
        "bare_original_energy_interval": interval_json(energy),
        "full_KKT_certified": feasible
        and all(row["strict_positive"] for row in inactive),
    }


def panel(prototype, kernel, primes, predicted_support):
    gram, records, pair_count = prototype.source_gram(kernel, primes)
    faces = [
        face(kernel, gram, support)
        for k in range(1, 5)
        for support in combinations(range(4), k)
    ]
    certified = [row for row in faces if row["full_KKT_certified"]]
    require(
        len(faces) == 15 and len(certified) <= 1,
        "all original faces and unique certified optimum",
    )
    scale = F(4, 4**4 * prod(primes))
    if certified:
        bare = tuple(
            F(certified[0]["bare_original_energy_interval"][side])
            for side in ("lower", "upper")
        )
        physical_energy = interval_json(times(bare, point(scale)))
        observed_support = certified[0]["support"]
    else:
        physical_energy, observed_support = None, None
    return {
        "primes": primes,
        "K": prod(primes),
        "all16_source_records": records,
        "complete_same_band_ordered_pair_count": pair_count,
        "exact_original_Gram": [
            [prototype.expression_json(x) for x in row] for row in gram
        ],
        "all15_face_certificates": faces,
        "certified_support": observed_support,
        "predicted_support": predicted_support,
        "prediction_certified": observed_support == predicted_support,
        "physical_Gram_multiplier": str(scale),
        "original_energy_interval": physical_energy,
        "failed_predictions_retained": True,
        "quadratic_kernel_substitution": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    prototype = load_module(PROTOTYPE_COMMIT, PROTOTYPE_PATH, PROTOTYPE_BLOB)
    kernel = prototype.load_module(
        prototype.KERNEL_COMMIT, prototype.KERNEL_PATH, prototype.KERNEL_BLOB
    )
    kernel.authenticate()
    prototype.frozen_bytes(prototype.OLD, prototype.GE_PATH, prototype.GE_BLOB)
    acquisition = json.loads(
        frozen_bytes(ACQUISITION_COMMIT, ACQUISITION_PATH, ACQUISITION_BLOB)
    )
    prime_scout = load_module(ACQUISITION_COMMIT, PRIME_PATH, PRIME_BLOB)
    frozen_bytes(ACQUISITION_COMMIT, PREREG_PATH, PREREG_BLOB)
    prime_source = prime_scout.prime_module()
    for multiplier, row in zip(
        prime_scout.MULTIPLIERS, acquisition["windows"], strict=True
    ):
        require(
            canonical(prime_scout.window(prime_source, multiplier)) == canonical(row),
            "complete first-prime fixed-window replay",
        )
    if not acquisition["all_windows_succeeded"]:
        print(
            json.dumps(
                {
                    "schema": "riemann.native_six_hour.boundary_layer_kernel_discovery.v1",
                    "acquisition_failed": True,
                    "models": [],
                },
                sort_keys=True,
                indent=2,
            )
        )
        return
    prefix = tuple(acquisition["fixed_prefix"])
    require(
        len(prefix) == 3 and all(prime_source.prime(p) for p in prefix),
        "literal fixed prime prefix",
    )
    fourths = [acquisition["original_fourth_prime"]] + [
        row["first_prime"] for row in acquisition["windows"]
    ]
    require(
        all(prime_source.prime(p) and p > prefix[-1] for p in fourths),
        "every literal fourth prime independently verified",
    )
    supports = ((1, 2), (1, 2, 3), (0, 1, 2, 3))
    models = [
        panel(prototype, kernel, prefix + (fourth,), support)
        for fourth, support in zip(fourths, supports, strict=True)
    ]
    result = {
        "schema": "riemann.native_six_hour.boundary_layer_kernel_discovery.v1",
        "acquisition_failed": False,
        "all_interval_operations_outward_rounded_bits": INTERVAL_BITS,
        "sources": [
            {
                "commit": PROTOTYPE_COMMIT,
                "path": PROTOTYPE_PATH,
                "blob": PROTOTYPE_BLOB,
            },
            {
                "commit": ACQUISITION_COMMIT,
                "path": ACQUISITION_PATH,
                "blob": ACQUISITION_BLOB,
            },
            {"commit": ACQUISITION_COMMIT, "path": PRIME_PATH, "blob": PRIME_BLOB},
            {"commit": ACQUISITION_COMMIT, "path": PREREG_PATH, "blob": PREREG_BLOB},
        ],
        "models": models,
        "full_retained_gamma_identified": False,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
