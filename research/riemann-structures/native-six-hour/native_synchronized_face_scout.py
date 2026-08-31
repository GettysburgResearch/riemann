#!/usr/bin/env python3
"""Original-kernel global optimization over an exactly attainable native source face."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1
from itertools import pairwise
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COMMIT = "a455dbe07c8d32fa3e7f3e74361abcfcafc681f9"
SOURCE = "research/riemann-structures/native-six-hour/native_path_synchronization.py"
SOURCE_BLOB = "76037d5997d287fd8b8385182708379440ccfae8"
BITS = 512
MAX_DEPTH = 80
MAX_NODES = 1024
ROOT_WIDTH = F(1, 2**64)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_module():
    require(
        len(COMMIT) == len(SOURCE_BLOB) == 40, "completed source synchronization freeze"
    )
    ref = f"{COMMIT}:{SOURCE}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= 4 * 1024 * 1024, "bounded pinned synchronization source")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
        == SOURCE_BLOB,
        "exact source synchronization authentication",
    )
    namespace = {
        "__name__": "authenticated_native_face_source",
        "__file__": str(ROOT / SOURCE),
    }
    # Execute only exact commit/blob-authenticated bytes.
    exec(compile(raw, str(ROOT / SOURCE), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def rounded(value):
    require(
        type(value) is tuple
        and len(value) == 2
        and all(type(x) is F for x in value)
        and value[0] <= value[1],
        "exact ordered interval",
    )
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 131072
            for x in value
        ),
        "pre-rounding rational cap",
    )
    scale = 1 << BITS
    return F(value[0].numerator * scale // value[0].denominator, scale), F(
        -((-value[1].numerator * scale) // value[1].denominator), scale
    )


def point(x):
    require(type(x) in (int, F), "exact rational point")
    return rounded((F(x), F(x)))


def add(a, b):
    return rounded((a[0] + b[0], a[1] + b[1]))


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = tuple(x * y for x in a for y in b)
    return rounded((min(values), max(values)))


def div(a, b):
    require(b[0] > 0 or b[1] < 0, "certified interval denominator")
    inverse = min(1 / b[0], 1 / b[1]), max(1 / b[0], 1 / b[1])
    return mul(a, rounded(inverse))


def scale(a, value):
    return mul(a, point(value))


def interval_json(value):
    value = rounded(value)
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 2048
            for x in value
        ),
        "bounded outward serialization",
    )
    return {
        "lower": str(value[0]),
        "upper": str(value[1]),
        "approximate_midpoint": float((value[0] + value[1]) / 2),
        "outward_bits": BITS,
    }


def strip(poly):
    poly = list(poly)
    while poly and poly[-1] == point(0):
        poly.pop()
    return tuple(poly)


def polynomial_value(poly, x):
    result = point(0)
    for coefficient in reversed(poly):
        result = add(mul(result, x), coefficient)
    return result


def derivative(poly):
    return strip(tuple(scale(poly[i], i) for i in range(1, len(poly))))


def remainder(left, right):
    require(
        right and len(left) <= 4 and len(right) <= 4,
        "bounded nonzero polynomial divisor",
    )
    result = list(left)
    degree = len(right) - 1
    for k in range(len(result) - 1, degree - 1, -1):
        quotient = div(result[k], right[-1])
        for j in range(degree):
            result[k - degree + j] = sub(
                result[k - degree + j], mul(quotient, right[j])
            )
        # This coefficient vanishes by the exact algebraic division definition.
        result[k] = point(0)
    return strip(tuple(result[:degree]))


def sturm_sequence(poly):
    poly = strip(poly)
    require(2 <= len(poly) <= 4, "declared degree1..3 derivative polynomial")
    sequence = [poly, derivative(poly)]
    while len(sequence[-1]) > 1:
        rem = remainder(sequence[-2], sequence[-1])
        require(rem, "non-squarefree derivative requires a separate retained analysis")
        sequence.append(tuple(neg(x) for x in rem))
        require(len(sequence) <= 4, "bounded native Sturm sequence")
    require(
        sequence[-1][0][0] > 0 or sequence[-1][0][1] < 0,
        "certified nonzero terminal Sturm constant",
    )
    return tuple(sequence)


def variations(sequence, x):
    signs = []
    for poly in sequence:
        value = polynomial_value(poly, point(x))
        if value == point(0):
            continue
        require(value[0] > 0 or value[1] < 0, "Sturm evaluation sign is not certified")
        signs.append(1 if value[0] > 0 else -1)
    return sum(a != b for a, b in pairwise(signs))


def isolate_roots(poly):
    sequence = sturm_sequence(poly)
    va, vb = variations(sequence, F()), variations(sequence, F(1))
    total = va - vb
    require(0 <= total <= len(poly) - 1, "native cubic real-root count")
    stack = [(F(), F(1), va, vb, 0)]
    roots, nodes = [], 0
    while stack:
        a, b, left, right, depth = stack.pop()
        nodes += 1
        require(
            nodes <= MAX_NODES and depth <= MAX_DEPTH,
            "fixed native root isolation budget",
        )
        count = left - right
        if count == 0:
            continue
        require(0 < count <= total, "positive local Sturm count")
        if count == 1 and b - a <= ROOT_WIDTH:
            roots.append((a, b))
            continue
        middle = (a + b) / 2
        vm = variations(sequence, middle)
        require(right <= vm <= left, "consistent exact root subdivision")
        stack.append((middle, b, vm, right, depth + 1))
        stack.append((a, middle, left, vm, depth + 1))
    roots.sort()
    require(len(roots) == total, "all interior cubic stationary roots isolated")
    return sequence, roots, nodes


def objective(c0, b, gram, d, e):
    values = (d, e)
    result = c0
    for i in range(2):
        result = add(result, scale(mul(b[i], values[i]), 2))
        for j in range(2):
            result = add(result, mul(gram[i][j], mul(values[i], values[j])))
    return result


def half_gradient(b, gram, d, e):
    return tuple(
        add(b[i], add(mul(gram[i][0], d), mul(gram[i][1], e))) for i in range(2)
    )


def candidate(name, c0, b, gram, d, e, certified, details):
    return {
        "name": name,
        "D": interval_json(d),
        "E": interval_json(e),
        "energy": interval_json(objective(c0, b, gram, d, e)),
        "half_gradients": [interval_json(x) for x in half_gradient(b, gram, d, e)],
        "full_convex_body_KKT_certified": bool(certified),
        "details": details,
    }


def discover():
    source = source_module()
    occupation, module, data, quadratic, kernel = source.source_modules()
    records = data["complete_ordered_records"]
    ratios = [(row["a"], row["b"]) for row in data["ratio_order"]]
    columns = [
        list(map(F, row["complete_source_vector"]))
        for row in data["coefficient_columns"]
    ]
    reference = occupation.source_vector(
        module, occupation.path_panel(module)[0][1], records
    )
    base_vector = occupation.affine_source(
        module, reference, columns, (F(1, 2), F(1, 3), F(1, 3), F(), F(), F())
    )
    r0 = [a + b for a, b in zip(columns[3], columns[5], strict=True)]
    r1 = columns[4]
    fields = [
        source.observed_field(module, kernel, x, records, ratios)
        for x in (base_vector, r0, r1)
    ]
    inner = [[quadratic.inner(kernel, x, y) for y in fields] for x in fields]
    c0 = rounded(kernel.ei(inner[0][0]))
    b = tuple(rounded(kernel.ei(inner[0][i])) for i in (1, 2))
    gram = tuple(tuple(rounded(kernel.ei(inner[i][j])) for j in (1, 2)) for i in (1, 2))
    det = sub(mul(gram[0][0], gram[1][1]), mul(gram[0][1], gram[1][0]))
    require(
        gram[0][0][0] > 0 and det[0] > 0,
        "strict original two-direction Gram positivity",
    )
    candidates = []
    d = div(sub(mul(b[1], gram[0][1]), mul(b[0], gram[1][1])), det)
    e = div(sub(mul(b[0], gram[1][0]), mul(b[1], gram[0][0])), det)
    lower = sub(e, scale(d, F(1, 2)))
    upper = sub(sub(d, scale(mul(d, d), F(1, 2))), e)
    feasible = d[0] > 0 and d[1] < 1 and lower[0] > 0 and upper[0] > 0
    candidates.append(
        candidate(
            "interior",
            c0,
            b,
            gram,
            d,
            e,
            feasible,
            {
                "stationarity_exact_by_Cramer_definition": True,
                "lower_constraint_slack": interval_json(lower),
                "upper_constraint_slack": interval_json(upper),
            },
        )
    )
    denominator = add(add(gram[0][0], gram[0][1]), scale(gram[1][1], F(1, 4)))
    require(denominator[0] > 0, "straight boundary positive curvature")
    d = div(neg(add(b[0], scale(b[1], F(1, 2)))), denominator)
    e = scale(d, F(1, 2))
    ge = half_gradient(b, gram, d, e)[1]
    candidates.append(
        candidate(
            "lower_boundary",
            c0,
            b,
            gram,
            d,
            e,
            d[0] > 0 and d[1] < 1 and ge[0] > 0,
            {
                "tangent_stationarity_exact_by_ratio_definition": True,
                "inward_E_half_gradient": interval_json(ge),
            },
        )
    )
    poly = (
        scale(add(b[0], b[1]), 2),
        scale(sub(add(add(gram[0][0], scale(gram[0][1], 2)), gram[1][1]), b[1]), 2),
        scale(add(gram[0][1], gram[1][1]), -3),
        gram[1][1],
    )
    sequence, roots, nodes = isolate_roots(poly)
    for index, root in enumerate(roots):
        d = rounded(root)
        e = sub(d, scale(mul(d, d), F(1, 2)))
        ge = half_gradient(b, gram, d, e)[1]
        candidates.append(
            candidate(
                f"upper_boundary_root_{index}",
                c0,
                b,
                gram,
                d,
                e,
                d[0] > 0 and d[1] < 1 and ge[1] < 0,
                {
                    "stationarity_exact_by_unique_original_cubic_root": True,
                    "outward_normal_E_half_gradient": interval_json(ge),
                },
            )
        )
    for name, d0, e0 in (("endpoint_zero", F(), F()), ("endpoint_one", F(1), F(1, 2))):
        d, e = point(d0), point(e0)
        gd, ge = half_gradient(b, gram, d, e)
        first = add(gd, scale(ge, F(1, 2)))
        second = add(gd, ge) if d0 == 0 else gd
        sign = (
            first[0] > 0 and second[0] > 0
            if d0 == 0
            else first[1] < 0 and second[1] < 0
        )
        candidates.append(
            candidate(
                name,
                c0,
                b,
                gram,
                d,
                e,
                sign,
                {
                    "endpoint_tangent_half_gradients": [
                        interval_json(first),
                        interval_json(second),
                    ]
                },
            )
        )
    selected = [row for row in candidates if row["full_convex_body_KKT_certified"]]
    require(len(selected) <= 1, "unique original-metric convex-body optimum")
    comparisons = []
    for name, parameters, expected in (
        ("diagonal", (0, 0, 0), (F(1, 2), F(1, 3))),
        ("w_equals_s_squared", (0, 0, -1), (F(1, 3), F(1, 4))),
        ("fixed_joint_quadratic", (1, 0, -1), None),
    ):
        _, observed, _, _ = quadratic.native_field(kernel, parameters)
        actual = quadratic.inner(kernel, observed, observed)
        if expected is not None:
            d0, e0 = expected
            predicted = kernel.ea(
                inner[0][0],
                kernel.ea(
                    kernel.es(inner[0][1], 2 * d0), kernel.es(inner[0][2], 2 * e0)
                ),
            )
            for i, x in enumerate(expected):
                for j, y in enumerate(expected):
                    predicted = kernel.ea(
                        predicted, kernel.es(inner[i + 1][j + 1], x * y)
                    )
            require(
                all(not part for part in kernel.ea(actual, kernel.es(predicted, -1))),
                "independent literal source path equals original face quadratic",
            )
        energy = rounded(kernel.ei(actual))
        gain = None
        if selected:
            best = tuple(F(selected[0]["energy"][side]) for side in ("lower", "upper"))
            gain = interval_json(sub(energy, best))
        comparisons.append(
            {
                "name": name,
                "parameters": parameters,
                "original_energy": interval_json(energy),
                "energy_minus_best_face": gain,
                "all_comparison_signs_retained": True,
            }
        )
    rational_witness = None
    if selected:
        chosen = selected[0]

        def dyadic_midpoint(row):
            midpoint = (F(row["lower"]) + F(row["upper"])) / 2
            scale48 = 1 << 48
            shifted = midpoint * scale48 + F(1, 2)
            return F(shifted.numerator // shifted.denominator, scale48)

        rational_d = dyadic_midpoint(chosen["D"])
        if chosen["name"].startswith("upper_boundary"):
            rational_e = rational_d - rational_d * rational_d / 2
        elif chosen["name"] == "lower_boundary":
            rational_e = rational_d / 2
        else:
            rational_e = dyadic_midpoint(chosen["E"])
        require(
            0 <= rational_d <= 1
            and rational_d / 2
            <= rational_e
            <= rational_d - rational_d * rational_d / 2,
            "fixed rounded path remains source-feasible",
        )
        mixture = (
            (rational_e - rational_d / 2) / (rational_d * (1 - rational_d) / 2)
            if 0 < rational_d < 1
            else F()
        )
        path = occupation.valid_path(module, source.face_path(rational_d, mixture))
        expected_moments = (
            F(1, 2),
            F(1, 3),
            F(1, 3),
            rational_d,
            rational_e,
            rational_d,
        )
        require(
            occupation.path_moments(module, path) == expected_moments,
            "literal rounded path occupation values",
        )
        actual_source = occupation.source_vector(module, path, records)
        require(
            actual_source
            == occupation.affine_source(module, reference, columns, expected_moments),
            "all63 original rounded-path coefficients independently integrated",
        )
        actual_field = source.observed_field(
            module, kernel, actual_source, records, ratios
        )
        actual_energy = rounded(
            kernel.ei(quadratic.inner(kernel, actual_field, actual_field))
        )
        best_energy = tuple(F(chosen["energy"][side]) for side in ("lower", "upper"))
        rational_witness = {
            "fixed_dyadic_bits": 48,
            "D": str(rational_d),
            "E": str(rational_e),
            "mixture": str(mixture),
            "five_equal_time_path_vertices": [list(map(str, p)) for p in path],
            "complete_original_source": list(map(str, actual_source)),
            "complete_physical_rational_ratio_image": list(
                map(str, module.ratio_image(actual_source, records, ratios))
            ),
            "original_energy": interval_json(actual_energy),
            "energy_above_certified_minimum": interval_json(
                sub(actual_energy, best_energy)
            ),
        }
    return {
        "schema": "riemann.native_six_hour.synchronized_face_discovery.v1",
        "status": "certified" if selected else "uncertified",
        "sources": [{"commit": COMMIT, "path": SOURCE, "blob": SOURCE_BLOB}],
        "all63_original_source_records": records,
        "all45_original_ratios": data["ratio_order"],
        "exact_original_augmented_Gram": [
            [kernel.expr_json(x) for x in row] for row in inner
        ],
        "strict_metric_determinant": interval_json(det),
        "upper_boundary_derivative_coefficients": [interval_json(x) for x in poly],
        "complete_Sturm_sequence": [[interval_json(x) for x in p] for p in sequence],
        "all_upper_boundary_root_intervals": [interval_json(x) for x in roots],
        "root_isolation_nodes": nodes,
        "all_candidates": candidates,
        "unique_certified_candidate": selected[0]["name"] if selected else None,
        "all_declared_comparisons": comparisons,
        "fixed_rational_actual_path": rational_witness,
        "full_all_path_optimum_claimed": False,
        "literal_site_diagonal_minimum_claimed": False,
        "full_gamma_identified": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    try:
        result = discover()
    except ValueError as error:
        result = {
            "schema": "riemann.native_six_hour.synchronized_face_discovery.v1",
            "status": "uncertified",
            "retained_guard_failure": str(error),
            "source_or_search_changed": False,
        }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
