#!/usr/bin/env python3
"""Exact whole-source synchronization, sharp staircases, and template accessibility."""

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
PINS = {
    "occupation": (
        "a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc",
        PREFIX + "native_occupation_moments.py",
        "1ce1ee9a5227d40fd441f9d7fc8eb9c5e66891bd",
    ),
    "occupation_proof": (
        "a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc",
        PREFIX + "NATIVE_OCCUPATION_MOMENTS.md",
        "bea7d2be82e752ffe471a4e9902ca5bbc73c50aa",
    ),
    "quadratic": (
        "b3a8a85021cedefae034aaef7c14a6976429142b",
        PREFIX + "global_tangent_metric_scout.py",
        "07d13eb8ca1d8999c81bbb2a74feeefd25ea2f99",
    ),
}
MAX_BYTES = 4 * 1024 * 1024
H = F(1, 4)
PARAMETERS = (
    (0, 0, 0),
    (0, H, 0),
    (0, -H, 0),
    (0, 0, H),
    (H, 2 * H, H),
    (H, H, 2 * H),
    (1, 0, -1),
    (-1, 1, 0),
    (H, H, H),
)
DELTAS = (F(1, 2), F(1, 4), F(1, 8), F(1, 16))
FACE_MASSES = (F(), F(1, 4), F(1, 2), F(3, 4), F(1))
FACE_MIXTURES = (F(), F(1, 2), F(1))
NOTE = HERE / "NATIVE_PATH_SYNCHRONIZATION_AND_TEMPLATE_ACCESSIBILITY.md"
FIXTURE = HERE / "native_path_synchronization.json"
TEST = ROOT / "tests/test_native_six_hour_path_synchronization.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(left, right):
    require(canonical(left) == canonical(right), "strict typed synchronization replay")


def exact(value):
    require(type(value) in (int, F), "exact rational source input")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 128,
        "bounded source rational input",
    )
    return value


def frozen(name, execute=False):
    commit, path, blob = PINS[name]
    ref = f"{commit}:{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded pinned source size")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact pinned native source authentication",
    )
    if not execute:
        return raw
    namespace = {
        "__name__": "authenticated_synchronization_source",
        "__file__": str(ROOT / path),
    }
    # Execute only the declared Git commit/blob-authenticated bytes.
    exec(compile(raw, str(ROOT / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def source_modules():
    occupation = frozen("occupation", True)
    frozen("occupation_proof")
    module, discovery, _ = occupation.authenticate()
    quadratic = frozen("quadratic", True)
    kernel = quadratic.frozen_module()
    return occupation, module, discovery, quadratic, kernel


def moments(parameters):
    require(
        type(parameters) is tuple and len(parameters) == 3, "three source parameters"
    )
    a, b, c = map(exact, parameters)
    require(all(-1 <= x <= 1 for x in (a, b, c)), "monotone quadratic cube")
    return (
        F(1, 2) + (b - a) / 6,
        F(1, 3) + (b - a) * (5 + a) / 60,
        F(1, 3) + (b - a) * (5 + b) / 30,
        F(1, 2) + (c - a) / 6,
        F(1, 3) + (c - a) * (5 + a) / 60,
        F(1, 2) + (c - b) / 6,
    )


def projection(values):
    require(type(values) is tuple and len(values) == 6, "six occupation coordinates")
    values = tuple(map(exact, values))
    return F(1, 2), F(1, 3), F(1, 3), values[3], values[4], values[3]


def square(values):
    return values[2] - 2 * values[1] + F(1, 3)


def gram_slack(values):
    a, b, c = values[:3]
    return c - a * a - 12 * (b - a / 2) ** 2


def determinant(matrix):
    require(
        type(matrix) is tuple
        and len(matrix) <= 5
        and all(type(row) is tuple and len(row) == len(matrix) for row in matrix),
        "bounded square accessibility matrix",
    )
    a = [list(map(exact, row)) for row in matrix]
    result = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F()
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        value = a[i][i]
        result *= value
        for j in range(i + 1, len(a)):
            multiplier = a[j][i] / value
            for k in range(i, len(a)):
                a[j][k] -= multiplier * a[i][k]
    return result


def face_path(d, mixture):
    d, mixture = exact(d), exact(mixture)
    require(0 <= d <= 1 and 0 <= mixture <= 1, "bounded exact source face parameters")
    lower = (1 - mixture) * d
    return (
        (F(),) * 3,
        (F(), F(), lower),
        (1 - d, 1 - d, lower),
        (1 - d, 1 - d, lower + mixture),
        (F(1), F(1), lower + mixture),
        (F(1),) * 3,
    )


def staircase(delta):
    delta = exact(delta)
    require(0 < delta < 1, "nondegenerate sharp staircase")
    return (
        (F(),) * 3,
        (F(), delta, F()),
        (F(), delta, F(1)),
        (delta, delta, F(1)),
        (F(1),) * 3,
    )


def synchronized_path(path):
    return tuple((u, u, w) for u, _, w in path)


def physical_identity(kernel, ratios, terms, constant=F()):
    result = {1: constant} if constant else {}
    for ratio, multiplier, root in terms:
        term = kernel.rm(ratios[ratio], kernel.sqrt_rational(F(root)))
        result = kernel.ra(result, kernel.rs(term, multiplier))
    require(set(result) <= {1}, "original physical functional is rational")
    return result.get(1, F())


def original_functionals(kernel, ratios):
    source_square = physical_identity(
        kernel, ratios, ((F(1, 2), 24, 2), (F(1, 3), 16, 3)), F(-29, 12)
    )
    cycle = physical_identity(
        kernel,
        ratios,
        ((F(2, 3), 2, 6), (F(1, 3), F(3, 2), 3), (F(3, 5), 2, 15), (F(2, 5), -2, 10)),
    )
    return source_square, cycle


def source_vector(records, order):
    by_pair = {
        (row["n"], row["m"]): F(row["coefficient_before_physical_weight"])
        for row in records
    }
    require(len(by_pair) == 63, "complete original factor census")
    return [by_pair[(row["n"], row["m"])] for row in order]


def observed_field(module, kernel, vector, records, ratios):
    coefficients = module.ratio_image(vector, records, ratios)
    return {
        F(a, b): kernel.rs(kernel.sqrt_rational(F(1, a * b)), value)
        for (a, b), value in zip(ratios, coefficients, strict=True)
    }


def build():
    occupation, module, data, quadratic, kernel = source_modules()
    records = data["complete_ordered_records"]
    ratios = [(row["a"], row["b"]) for row in data["ratio_order"]]
    columns = [
        list(map(F, row["complete_source_vector"]))
        for row in data["coefficient_columns"]
    ]
    reference_path = occupation.path_panel(module)[0][1]
    reference = occupation.source_vector(module, reference_path, records)
    panels = []
    for parameters in PARAMETERS:
        expected = moments(parameters)
        original, observed, endpoints, diagonals = quadratic.native_field(
            kernel, parameters
        )
        actual = source_vector(original, records)
        require(
            actual == occupation.affine_source(module, reference, columns, expected),
            "complete literal polynomial source equals independent six-form formula",
        )
        sync_parameters = (parameters[0], parameters[0], parameters[2])
        sync_records, sync_observed, _, sync_diagonals = quadratic.native_field(
            kernel, sync_parameters
        )
        synchronized = source_vector(sync_records, records)
        require(
            synchronized
            == occupation.affine_source(
                module, reference, columns, projection(expected)
            ),
            "actual synchronized source equals affine retraction",
        )
        require(
            projection(projection(expected)) == projection(expected),
            "source projection idempotence",
        )
        L, cycle = original_functionals(kernel, observed)
        require(
            L == square(expected) == (F(parameters[1]) - F(parameters[0])) ** 2 / 30
            and cycle == F(1, 2),
            "original physical readout square and missing template observable",
        )
        require(
            original_functionals(kernel, sync_observed)[0] == 0
            and gram_slack(expected) >= 0,
            "source synchronization face and full Gram square",
        )
        panels.append(
            {
                "parameters": list(map(str, parameters)),
                "moments": list(map(str, expected)),
                "complete_source": list(map(str, actual)),
                "synchronized_source": list(map(str, synchronized)),
                "physical_square": str(L),
                "physical_cycle": str(cycle),
                "Gram_PSD_slack": str(gram_slack(expected)),
                "all_original_diagonals": {
                    key: str(value) for key, value in diagonals.items()
                },
                "all_synchronized_diagonals": {
                    key: str(value) for key, value in sync_diagonals.items()
                },
                "complete_product_endpoints": {
                    str(key): str(value) for key, value in endpoints.items()
                },
            }
        )
    baseline = moments(PARAMETERS[0])
    coordinate_order = (0, 3, 1, 2, 4)
    witness_matrix = tuple(
        tuple(moments(p)[i] - baseline[i] for i in coordinate_order)
        for p in PARAMETERS[1:6]
    )
    det = determinant(witness_matrix)
    require(
        abs(det) == 2 * H**8 / (36 * 60 * 30 * 60),
        "five open source witnesses span the complete affine hyperplane",
    )
    require(
        panels[-1]["complete_source"] == panels[0]["complete_source"]
        and panels[-1]["all_original_diagonals"]["primitive_2ds_site"]
        != panels[0]["all_original_diagonals"]["primitive_2ds_site"],
        "actual reparameterization preserves current but not primitive2ds site square",
    )
    stairs = []
    for delta in DELTAS:
        path = occupation.valid_path(module, staircase(delta))
        sync_path = occupation.valid_path(module, synchronized_path(path))
        values = occupation.path_moments(module, path)
        expected = (
            F(1, 2) + delta**2 / 2,
            F(1, 3) + delta**3 / 6,
            F(1, 3) + 2 * delta**3 / 3,
            F(1),
            F(1, 2),
            1 - delta,
        )
        require(
            values == expected and square(values) == delta**3 / 3,
            "exact sharp native staircase moments",
        )
        require(
            occupation.path_moments(module, sync_path) == projection(values),
            "whole-path synchronization",
        )
        actual = occupation.source_vector(module, path, records)
        synced = occupation.source_vector(module, sync_path, records)
        difference = [a - b for a, b in zip(actual, synced, strict=True)]
        expected_difference = [
            delta**2 * columns[0][i] / 2
            + delta**3 * columns[1][i] / 6
            + delta**3 * columns[2][i] / 3
            - delta * columns[5][i]
            for i in range(63)
        ]
        require(
            difference == expected_difference,
            "complete physical sharpness direction and higher-order terms",
        )
        image = module.ratio_image(difference, records, ratios)
        require(
            image[ratios.index((3, 5))] == -delta / 2,
            "nonzero original observed sharpness witness",
        )
        L, cycle = original_functionals(
            kernel, observed_field(module, kernel, actual, records, ratios)
        )
        require(
            L == delta**3 / 3 and cycle == values[0] + values[5] - values[3],
            "sharp source after all ratio coalescence",
        )
        stairs.append(
            {
                "delta": str(delta),
                "moments": list(map(str, values)),
                "L": str(L),
                "sup_gap_cubed": str(delta**3),
                "F_minus_D": str(-delta),
                "complete_source_difference": list(map(str, difference)),
                "physical_rational_ratio_difference": list(map(str, image)),
            }
        )
    faces = []
    for d in FACE_MASSES:
        for mixture in FACE_MIXTURES:
            path = occupation.valid_path(module, face_path(d, mixture))
            expected_e = (1 - mixture) * d / 2 + mixture * (d - d * d / 2)
            values = occupation.path_moments(module, path)
            require(
                values == (F(1, 2), F(1, 3), F(1, 3), d, expected_e, d),
                "entire two-dimensional exposed-face construction on declared controls",
            )
            actual = occupation.source_vector(module, path, records)
            require(
                actual == occupation.affine_source(module, reference, columns, values),
                "full original exposed-face source",
            )
            faces.append(
                {
                    "D": str(d),
                    "mixture": str(mixture),
                    "moments": list(map(str, values)),
                    "complete_source": list(map(str, actual)),
                }
            )
    # These original-metric probes are all retained; no orthogonality is assumed.
    fields = [observed_field(module, kernel, col, records, ratios) for col in columns]
    ranges = (quadratic.field_add(kernel, fields[3], fields[5]), fields[4])
    probes = []
    for ki in (0, 1, 2, 5):
        for ri, value in enumerate(ranges):
            expression = quadratic.inner(kernel, fields[ki], value)
            interval = kernel.ei(expression)
            probes.append(
                {
                    "kernel_column": ki,
                    "range_column": ri,
                    "original_inner_product": kernel.expr_json(expression),
                    "interval": kernel.interval_json(interval),
                    "certified_nonzero": interval[0] > 0 or interval[1] < 0,
                }
            )
    result = {
        "schema": "riemann.native_six_hour.path_synchronization.v1",
        "sources": [
            {"commit": commit, "path": path, "blob": blob}
            for commit, path, blob in PINS.values()
        ],
        "complete_ordered_records": records,
        "ratio_order": data["ratio_order"],
        "quadratic_profiles": panels,
        "open_basis_determinant": str(det),
        "sharp_staircases": stairs,
        "exposed_face_controls": faces,
        "all_eight_original_metric_orthogonality_probes": probes,
        "source_projection_is_orthogonal": False
        if any(p["certified_nonzero"] for p in probes)
        else None,
        "finite_six_dimensional_source_observation_commutes": True,
        "primitive_diagonal_isometry_claimed": False,
        "whole_affine_hyperplane_attainable_claimed": False,
        "full_post_renewal_gamma_identified": False,
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
        raw = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
        require(len(raw) <= MAX_BYTES, "bounded original source replay")
        FIXTURE.write_bytes(raw)
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "bounded original source artifact")
        strict_equal(json.loads(FIXTURE.read_bytes()), result)
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]},
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
