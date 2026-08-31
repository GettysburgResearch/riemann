#!/usr/bin/env python3
"""Original-kernel affine floor and fixed source-halfspace lower bounds."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import pairwise, permutations
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
CURVATURE = "6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537"
TANGENT = "c251614fa6ff2367c7c6dd30c1d6b5f33fbc5161"
PINS = (
    (CURVATURE, "NATIVE_CURVATURE_SPAN.md", "a61a6fb8bbf63a4cb838f806afe64da0d8ef10a4"),
    (
        CURVATURE,
        "native_curvature_span_certificate.py",
        "ad435c1ff24b22620f817299197b7bc270f125d4",
    ),
    (
        CURVATURE,
        "native_curvature_span_certificate.json",
        "4ec6ca34165a1967e47b05d4f5919e04e3adcab8",
    ),
    (
        TANGENT,
        "global_tangent_metric_certificate.json",
        "9c5bb89b5f093e53a50cb5aaa3c42a1ace4f7cf2",
    ),
)
DENOMINATOR = 2**192
MAX_BYTES = 4 * 1024 * 1024
ORIGIN = (F(),) * 3
END = (F(1),) * 3


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def rounded(value):
    lo, hi = map(F, value)
    require(lo <= hi, "valid interval order")
    require(
        max(x.numerator.bit_length() for x in (lo, hi)) <= 8192
        and max(x.denominator.bit_length() for x in (lo, hi)) <= 8192,
        "exact intermediate bit cap",
    )
    return F((lo * DENOMINATOR).__floor__(), DENOMINATOR), F(
        (hi * DENOMINATOR).__ceil__(), DENOMINATOR
    )


def point(value):
    return rounded((value, value))


def ia(a, b):
    return rounded((a[0] + b[0], a[1] + b[1]))


def neg(a):
    return -a[1], -a[0]


def im(a, b):
    values = [x * y for x in a for y in b]
    return rounded((min(values), max(values)))


def reciprocal(a):
    require(a[0] > 0 or a[1] < 0, "interval divisor certified nonzero")
    values = [1 / x for x in a]
    return rounded((min(values), max(values)))


def inner(kernel, left, right):
    value = kernel.ex()
    for ratio, a in left.items():
        for other, b in right.items():
            if a and b:
                value = kernel.ea(
                    value, kernel.er(kernel.gamma(ratio / other), kernel.rm(a, b))
                )
    return value


def source_field(curve, kernel, vector, records, ratios):
    image = curve.ratio_image(vector, records, ratios)
    return {
        F(a, b): kernel.rs(kernel.sqrt_rational(F(1, a * b)), value)
        for (a, b), value in zip(ratios, image, strict=True)
    }


def literal_path(curve, points, records):
    source = {n: curve.half_source(n) for n in curve.panel_numbers()}
    return [
        sum(
            (
                curve.edge_integral(source[row["n"]], source[row["m"]], a, b)
                for a, b in pairwise(points)
            ),
            F(),
        )
        for row in records
    ]


def authenticate():
    raw, provenance = {}, []
    for commit, name, blob in PINS:
        ref = f"{commit}:{PREFIX}{name}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "source byte cap")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(data) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "exact frozen source blob",
        )
        raw[name] = data
        provenance.append({"commit": commit, "path": PREFIX + name, "blob": blob})
    name = "native_curvature_span_certificate.py"
    namespace = {
        "__name__": "authenticated_affine_curvature",
        "__file__": str(HERE / name),
    }
    exec(compile(raw[name], str(HERE / name), "exec"), namespace)  # noqa: S102
    certificate = SimpleNamespace(**namespace)
    require(
        canonical(certificate.build())
        == canonical(json.loads(raw["native_curvature_span_certificate.json"])),
        "full primitive curvature replay",
    )
    curve, data, _ = certificate.source()
    kernel, _, _ = curve.authenticate()
    tangent = json.loads(raw["global_tangent_metric_certificate.json"])
    return curve, kernel, data, tangent, provenance


def inverse_and_solution(matrix, cross):
    require(
        len(matrix) == len(cross) == 6 and all(len(row) == 6 for row in matrix),
        "fixed six-dimensional system",
    )
    work = [
        list(row) + [neg(cross[i])] + [point(int(i == j)) for j in range(6)]
        for i, row in enumerate(matrix)
    ]
    pivots = []
    for k in range(6):
        pivot = work[k][k]
        require(pivot[0] > 0, "positive interval elimination pivot")
        pivots.append(pivot)
        inverse = reciprocal(pivot)
        work[k] = [im(entry, inverse) for entry in work[k]]
        for i in range(6):
            if i == k:
                continue
            factor = work[i][k]
            work[i] = [
                ia(entry, neg(im(factor, other)))
                for entry, other in zip(work[i], work[k], strict=True)
            ]
    return [row[6] for row in work], [row[7:] for row in work], pivots


def linear(intervals, coefficients):
    value = point(0)
    for entry, coefficient in zip(intervals, coefficients, strict=True):
        value = ia(value, im(entry, point(coefficient)))
    return value


def halfspaces():
    result = []

    def add(name, coefficients, bound):
        require(
            len(coefficients) == 6 and any(coefficients),
            "nonzero six-coordinate source functional",
        )
        result.append((name, tuple(map(F, coefficients)), F(bound)))

    for index, name in ((0, "A"), (3, "D"), (5, "F")):
        for sign, bound, label in ((-1, 0, "lower"), (1, 1, "upper")):
            row = [0] * 6
            row[index] = sign
            add(name + "_" + label, row, bound)
    add("C_lower", (0, 0, -2, 0, 0, 0), 0)
    add("C_le_A", (-1, 0, 2, 0, 0, 0), 0)
    add("B_ge_A_half", (F(1, 2), -1, 0, 0, 0, 0), 0)
    add("E_ge_D_half", (0, 0, 0, F(1, 2), -1, 0), 0)
    add("cycle_lower", (-1, 0, 0, 1, 0, -1), 0)
    add("cycle_upper", (1, 0, 0, -1, 0, 1), 1)
    for t in (F(i, 8) for i in range(9)):
        add(f"Jensen_{t}", (2 * t, 0, -2, 0, 0, 0), t * t)
        add(f"B_rearrangement_{t}", (t - 1, 1, 0, 0, 0, 0), t * t / 2)
        add(f"E_rearrangement_{t}", (0, 0, 0, t - 1, 1, 0), t * t / 2)
    add("synchronization_square", (0, 2, -2, 0, 0, 0), F(1, 3))
    for s in (F(-1), F(-1, 2), F(), F(1, 2), F(1)):
        for t in (F(-1), F(-1, 2), F(), F(1, 2), F(1)):
            add(
                f"Gram_square_{s}_{t}",
                (2 * s, 2 * t, -2, 0, 0, 0),
                s * s + s * t + t * t / 3,
            )
    require(len(result) == 65, "complete fixed halfspace coverage")
    return result


def interval_json(value):
    lo, hi = value
    require(
        max(max(x.numerator.bit_length(), x.denominator.bit_length()) for x in value)
        <= 1024,
        "serialized endpoint bit cap",
    )
    return {
        "lower": str(lo),
        "upper": str(hi),
        "approximate_midpoint": float((lo + hi) / 2),
    }


def discover():
    curve, kernel, data, tangent, provenance = authenticate()
    records = data["complete_ordered_records"]
    ratios = [(row["a"], row["b"]) for row in data["ratio_order"]]
    columns = [
        list(map(F, row["complete_source_vector"]))
        for row in data["coefficient_columns"]
    ]
    fields = [
        source_field(curve, kernel, column, records, ratios) for column in columns
    ]
    paths = []
    for order in permutations(range(3)):
        points = [ORIGIN]
        for coordinate in order:
            point_ = list(points[-1])
            point_[coordinate] = F(1)
            points.append(tuple(point_))
        paths.append(
            (
                "axis_" + "".join(str((2, 3, 5)[i]) for i in order),
                literal_path(curve, points, records),
            )
        )
    paths.append(("diagonal", literal_path(curve, (ORIGIN, END), records)))
    selected = next(
        row
        for row in tangent["all18_shared_source_paths"]
        if row["epsilon"] == ["1", "0", "-1"]
    )
    require(
        [(row["n"], row["m"]) for row in selected["all63_records"]]
        == [(row["n"], row["m"]) for row in records],
        "all63 comparison records",
    )
    paths.append(
        (
            "quadratic_1_0_minus1",
            [
                F(row["coefficient_before_physical_weight"])
                for row in selected["all63_records"]
            ],
        )
    )
    reference = paths[0][1]
    reference_field = source_field(curve, kernel, reference, records, ratios)
    gram = [[inner(kernel, left, right) for right in fields] for left in fields]
    cross = [inner(kernel, field, reference_field) for field in fields]
    constant = inner(kernel, reference_field, reference_field)
    require(
        all(gram[i][j] == gram[j][i] for i in range(6) for j in range(6)),
        "exact physical Gram symmetry",
    )
    matrix = [[rounded(kernel.ei(value)) for value in row] for row in gram]
    g = [rounded(kernel.ei(value)) for value in cross]
    c = rounded(kernel.ei(constant))
    optimum, inverse, pivots = inverse_and_solution(matrix, g)
    floor = c
    for gi, xi in zip(g, optimum, strict=True):
        floor = ia(floor, im(gi, xi))
    require(floor[0] > 0, "strict positive affine physical floor")
    lookup = {
        (row["n"], row["m"]): value
        for row, value in zip(records, reference, strict=True)
    }
    symmetric = [
        (lookup[row["n"], row["m"]] + lookup[row["m"], row["n"]]) / 2 for row in records
    ]
    symmetric_field = source_field(curve, kernel, symmetric, records, ratios)
    orthogonal = [inner(kernel, symmetric_field, field) for field in fields]
    require(
        all(all(not coefficient for coefficient in value) for value in orthogonal),
        "exact fixed-even and variable-odd orthogonality",
    )
    require(
        reference_field[F(16)] == kernel.scalar(F(11, 256))
        and all(not field[F(16)] for field in fields),
        "fixed physical ratio16 obstruction",
    )
    bounds = []
    best = floor[0]
    best_name = "affine"
    for name, row, bound in halfspaces():
        violation = ia(linear(optimum, row), point(-bound))
        inverse_row = [linear(inverse[i], row) for i in range(6)]
        denominator = linear(inverse_row, row)
        require(denominator[0] > 0, "strict positive dual metric")
        record = {
            "name": name,
            "L": list(map(str, row)),
            "b": str(bound),
            "affine_violation": interval_json(violation),
            "dual_squared_norm": interval_json(denominator),
        }
        if violation[0] > 0:
            correction = im(im(violation, violation), reciprocal(denominator))
            corrected = ia(floor, correction)
            record.update(
                {
                    "status": "strictly_violated",
                    "correction": interval_json(correction),
                    "corrected_floor": interval_json(corrected),
                }
            )
            if corrected[0] > best:
                best, best_name = corrected[0], name
        elif violation[1] <= 0:
            record["status"] = "affine_point_satisfies"
        else:
            record["status"] = "uncertified_sign"
        bounds.append(record)
    comparisons = []
    for name, vector in paths:
        field = source_field(curve, kernel, vector, records, ratios)
        energy = inner(kernel, field, field)
        interval = rounded(kernel.ei(energy))
        require(
            best <= interval[1], "certified lower bound compatible with actual path"
        )
        if name == "quadratic_1_0_minus1":
            require(
                kernel.expr_json(energy) == selected["exact_observed_energy"],
                "independent quadratic physical energy replay",
            )
        comparisons.append(
            {
                "name": name,
                "complete_source": list(map(str, vector)),
                "exact_energy": kernel.expr_json(energy),
                "energy": interval_json(interval),
            }
        )
    moments = [entry for entry in optimum]
    moments[2] = im(point(2), moments[2])
    owned = {}
    for path in (
        HERE / "NATIVE_AFFINE_PHYSICAL_FLOOR.md",
        HERE / "NATIVE_AFFINE_FLOOR_PREREGISTRATION.md",
        Path(__file__),
    ):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned byte cap")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.affine_floor_discovery.v1",
        "sources": provenance,
        "owned_sha256_lf": owned,
        "complete_ordered_records": records,
        "basis_order": data["coefficient_columns"],
        "exact_Gram": [[kernel.expr_json(value) for value in row] for row in gram],
        "exact_cross_terms": [kernel.expr_json(value) for value in cross],
        "exact_reference_energy": kernel.expr_json(constant),
        "interval_Gram": [[interval_json(value) for value in row] for row in matrix],
        "positive_elimination_pivots": [interval_json(value) for value in pivots],
        "affine_coordinates": [interval_json(value) for value in optimum],
        "affine_occupation_moments": [interval_json(value) for value in moments],
        "inverse_Gram": [[interval_json(value) for value in row] for row in inverse],
        "affine_energy_floor": interval_json(floor),
        "fixed_symmetric_energy": interval_json(
            rounded(kernel.ei(inner(kernel, symmetric_field, symmetric_field)))
        ),
        "all_six_even_odd_cross_terms_exactly_zero": True,
        "fixed_ratio16_physical_amplitude": "11/256",
        "halfspaces": bounds,
        "best_single_halfspace_bound": {
            "name": best_name,
            "certified_lower": str(best),
            "approximate_lower": float(best),
        },
        "actual_paths": comparisons,
        "scope": {
            "all65_fixed_source_halfspaces_retained": True,
            "original_Mellin_measure": True,
            "affine_minimizer_claimed_native": False,
            "best_bound_claimed_optimal_over_all_paths": False,
            "complete_gamma_principal_member_identified": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    output = json.dumps(discover(), sort_keys=True, indent=2, allow_nan=False) + "\n"
    require(len(output.encode()) <= MAX_BYTES, "scout output byte cap")
    print(output, end="")


if __name__ == "__main__":
    main()
