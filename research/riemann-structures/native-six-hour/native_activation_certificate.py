#!/usr/bin/env python3
"""Exact source-owned minimizers from the frozen original-kernel discovery."""

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
NOTE = HERE / "NATIVE_ACTIVATION_KERNEL_MINIMIZER.md"
PREREGISTRATION = HERE / "ACTIVATION_KERNEL_PREREGISTRATION.md"
FIXTURE = HERE / "native_activation_certificate.json"
TEST = ROOT / "tests" / "test_native_six_hour_activation_kernel.py"
KERNEL_COMMIT = "033bc967f8fd9b5e23e00386dfe81e92b25dc012"
KERNEL_PATH = "research/riemann-structures/native-six-hour/native_activation_kernel.py"
KERNEL_BLOB = "1846674ad08e9f070cc6884c3928d619552f8011"
PREREGISTRATION_PATH = (
    "research/riemann-structures/native-six-hour/ACTIVATION_KERNEL_PREREGISTRATION.md"
)
PREREGISTRATION_BLOB = "890806504f452243a4fffa67d7f25c39fa89f76d"
DISCOVERY_PATH = (
    "research/riemann-structures/native-six-hour/activation_kernel.discovery.json"
)
DISCOVERY_BLOB = "52d6e454e8a639ede1d6547ea858bf28f8f4f424"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
GEODESIC_PATH = "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md"
GEODESIC_BLOB = "6810bcece309b0c54ae6c8fc84b314990004549c"
MAX_BYTES = 1048576


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(commit, path, blob):
    require(len(commit) == len(blob) == 40, "parent-frozen discovery source required")
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
        "frozen source authentication",
    )
    return raw


def kernel_module():
    raw = frozen_bytes(KERNEL_COMMIT, KERNEL_PATH, KERNEL_BLOB)
    namespace = {
        "__name__": "authenticated_activation_kernel",
        "__file__": str(ROOT / KERNEL_PATH),
    }
    # Only exact Git bytes authenticated against a frozen commit and blob execute.
    exec(compile(raw, str(ROOT / KERNEL_PATH), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def expression_json(value):
    return {
        "constant": [str(x) for x in value[0]],
        "logs": [
            {
                "positive_rational_base": str(base),
                "Q_sqrt2_coefficient": [str(x) for x in coefficient],
            }
            for base, coefficient in sorted(value[1].items())
        ],
    }


def quadratic_expression(kernel, matrix, activation):
    require(
        type(activation) is tuple
        and len(activation) == 3
        and all(type(x) in (int, F) for x in activation),
        "exact activation vector",
    )
    require(all(x >= 0 for x in activation) and sum(activation) == 1, "source simplex")
    value = kernel.expr()
    for i in range(3):
        for j in range(3):
            value = kernel.ea(
                value, kernel.es(matrix[i][j], activation[i] * activation[j])
            )
    return value


def optimizer(kernel, matrix):
    intervals = tuple(tuple(kernel.ei(value) for value in row) for row in matrix)
    det = kernel.determinant(intervals)
    require(det[0] > 0, "certified positive determinant")
    # adj(G) has the transposed cofactor matrix; no symmetry shortcut is needed.
    adjugate = tuple(
        tuple(kernel.cofactor(intervals, j, i) for j in range(3)) for i in range(3)
    )
    rows = tuple(kernel.ia(kernel.ia(row[0], row[1]), row[2]) for row in adjugate)
    total = kernel.ia(kernel.ia(rows[0], rows[1]), rows[2])
    require(total[0] > 0, "positive constrained normalization")
    probabilities = tuple(kernel.im(row, kernel.inv(total)) for row in rows)
    require(all(row[0] > 0 for row in probabilities), "true interior simplex minimizer")
    minimum = kernel.im(det, kernel.inv(total))
    return intervals, det, probabilities, minimum


def model_certificate(kernel, primes, scout_powers):
    require(
        type(scout_powers) is tuple
        and len(scout_powers) == 3
        and all(type(a) is int and 1 <= a <= 1000 for a in scout_powers),
        "frozen scout power cap",
    )
    model = kernel.kernel_gram(primes)
    require(
        all(value == kernel.expr() for value in model["even_odd_cross"]),
        "exact even-odd orthogonality",
    )
    intervals, det, probabilities, minimum = optimizer(kernel, model["gram"])
    uniform = quadratic_expression(kernel, model["gram"], (F(1, 3),) * 3)
    simple = quadratic_expression(kernel, model["gram"], (F(2, 5), F(3, 10), F(3, 10)))
    scout_q = tuple(F(a, sum(scout_powers)) for a in scout_powers)
    scout = quadratic_expression(kernel, model["gram"], scout_q)
    gap = kernel.ea(uniform, kernel.es(simple, -1))
    gap_interval = kernel.ei(gap)
    if primes == (3, 5, 7):
        require(gap_interval[0] > F(2, 25), "primary simple-path physical improvement")
        boxes = (
            (F(3992, 10000), F(3993, 10000)),
            (F(2960, 10000), F(2961, 10000)),
            (F(3047, 10000), F(3048, 10000)),
        )
    elif primes == (2, 3, 5):
        require(gap_interval[0] > F(9, 100), "independent crowded control improvement")
        boxes = (
            (F(3959, 10000), F(3961, 10000)),
            (F(2904, 10000), F(2906, 10000)),
            (F(3135, 10000), F(3136, 10000)),
        )
    else:
        require(primes == (3, 11, 101), "declared three-prime panels")
        boxes = ((F(1, 3) - F(1, 10**20), F(1, 3) + F(1, 10**20)),) * 3
        diagonal = kernel.es(kernel.gamma_square_ratio(F(1)), F(1, 8))
        require(
            model["mean"] == diagonal
            and all(
                model["gram"][i][j] == (diagonal if i == j else kernel.expr())
                for i in range(3)
                for j in range(3)
            ),
            "separated original-kernel Gram",
        )
    for row, box in zip(probabilities, boxes, strict=True):
        require(box[0] < row[0] <= row[1] < box[1], "certified optimizer enclosure")
    gradient = tuple(
        kernel.im(kernel.point(F(1, 3)), kernel.ia(kernel.ia(row[0], row[1]), row[2]))
        for row in intervals
    )
    return {
        "primes": primes,
        "K": model["K"],
        "full_factor_count": 8,
        "all_physical_divisors": model["divisors"],
        "exact_Gram_expressions": [
            [expression_json(value) for value in row] for row in model["gram"]
        ],
        "exact_mean_expression": expression_json(model["mean"]),
        "Gram_intervals": [
            [kernel.summarize_interval(value) for value in row] for row in intervals
        ],
        "mean_energy_K_scaled_interval": kernel.summarize_interval(
            kernel.ei(model["mean"])
        ),
        "determinant_interval": kernel.summarize_interval(det),
        "unique_interior_activation": [
            kernel.summarize_interval(value) for value in probabilities
        ],
        "optimizer_boxes": [[str(x) for x in box] for box in boxes],
        "minimum_odd_energy_K_scaled_interval": kernel.summarize_interval(minimum),
        "uniform_gradient": [kernel.summarize_interval(value) for value in gradient],
        "preregistered_discovery_integer_powers": scout_powers,
        "uniform_minus_scout_K_scaled_interval": kernel.summarize_interval(
            kernel.ei(kernel.ea(uniform, kernel.es(scout, -1)))
        ),
        "postdiscovery_simple_integer_powers": (4, 3, 3),
        "uniform_minus_simple_exact_K_scaled_expression": expression_json(gap),
        "uniform_minus_simple_K_scaled_interval": kernel.summarize_interval(
            gap_interval
        ),
        "physical_improvement_interval": kernel.summarize_interval(
            kernel.im(gap_interval, kernel.point(F(1, model["K"])))
        ),
        "source_endpoint_and_signed_Hankel_current_unchanged": True,
        "arbitrary_independent_arithmetic_coefficients_fitted": False,
    }


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def build():
    kernel = kernel_module()
    kernel.authenticate()
    frozen_bytes(OLD, GEODESIC_PATH, GEODESIC_BLOB)
    frozen_bytes(KERNEL_COMMIT, PREREGISTRATION_PATH, PREREGISTRATION_BLOB)
    discovery = json.loads(frozen_bytes(KERNEL_COMMIT, DISCOVERY_PATH, DISCOVERY_BLOB))
    require(
        [tuple(row["primes"]) for row in discovery["models"]]
        == [(3, 5, 7), (2, 3, 5), (3, 11, 101)],
        "preregistered discovery panels preserved",
    )
    require(
        [tuple(row["candidate_integer_power_schedule"]) for row in discovery["models"]]
        == [(399, 296, 305), (396, 290, 314), (333, 333, 333)],
        "original discovery candidates preserved",
    )
    require(
        kernel.gamma_square_ratio(F(1))
        == kernel.expr(kernel.q(-288), {F(2): kernel.q(384, 128)}),
        "exact native Gamma(0)",
    )
    require(
        kernel.gamma_square_ratio(F(2))
        == kernel.expr(kernel.q(-48), {F(2): kernel.q(0, 64)}),
        "independent Gamma(log4) anchor",
    )
    bindings = {}
    for path in (NOTE, PREREGISTRATION, Path(__file__), TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned file cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.activation_certificate.v1",
        "frozen_discovery_code": {
            "commit": KERNEL_COMMIT,
            "path": KERNEL_PATH,
            "blob": KERNEL_BLOB,
        },
        "frozen_preregistration": {
            "commit": KERNEL_COMMIT,
            "path": PREREGISTRATION_PATH,
            "blob": PREREGISTRATION_BLOB,
        },
        "frozen_original_discovery_output": {
            "commit": KERNEL_COMMIT,
            "path": DISCOVERY_PATH,
            "blob": DISCOVERY_BLOB,
        },
        "geodesic_source": {
            "commit": OLD,
            "path": GEODESIC_PATH,
            "blob": GEODESIC_BLOB,
        },
        "original_kernel_source": {
            "commit": kernel.SOURCE_COMMIT,
            "path": kernel.SOURCE_PATH,
            "blob": kernel.SOURCE_BLOB,
        },
        "source_hashes": bindings,
        "models": [
            model_certificate(kernel, primes, powers)
            for primes, powers in (
                ((3, 5, 7), (399, 296, 305)),
                ((2, 3, 5), (396, 290, 314)),
                ((3, 11, 101), (333, 333, 333)),
            )
        ],
        "original_kernel_and_physical_normalization_retained": True,
        "source_primewise_schedules_not_tuple_coefficient_fits": True,
        "single_global_schedule_optimizing_all_models_claimed": False,
        "complete_post_renewal_gamma_identified": False,
        "RH_conclusion": False,
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
    print(f"PASS native activation certificate {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
