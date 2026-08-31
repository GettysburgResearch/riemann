#!/usr/bin/env python3
"""Exact rational support controls with all63 original native source records."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import pairwise
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
OCCUPATION = "a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc"
PINS = (
    (
        OCCUPATION,
        "NATIVE_OCCUPATION_MOMENTS.md",
        "bea7d2be82e752ffe471a4e9902ca5bbc73c50aa",
    ),
    (
        OCCUPATION,
        "native_occupation_moments.py",
        "1ce1ee9a5227d40fd441f9d7fc8eb9c5e66891bd",
    ),
    (
        OCCUPATION,
        "native_occupation_moments.json",
        "0bd978b7280f88cd60f2f020647f39868948d163",
    ),
    (
        "46c8453e3976d242479202bf4d58489282a64d2a",
        "NATIVE_AFFINE_PHYSICAL_FLOOR.md",
        "50cb1abef7865f540e8322f0609c2c6e3bdb2a83",
    ),
)
MAX_BYTES = 4 * 1024 * 1024
ORIGIN = (F(), F(), F())
END = (F(1), F(1), F(1))
PANELS = (
    ("increasing_target", (1, -4, 1, 0, 0, 0), ((F(1, 2), F(1, 2)),)),
    ("decreasing_target", (-3, 4, 1, 1, 0, F(-1, 2)), ((F(1, 2), F(1, 2)),)),
    (
        "constant_target_endpoints",
        (-1, 0, 1, 0, F(1, 2), 1),
        ((F(), F(1, 4)), (F(1), F(3, 4))),
    ),
    ("order_positive", (0, 0, 0, 0, 0, 1), ()),
    ("order_negative", (0, 0, 0, 0, 0, -1), ()),
    ("concave_interior", (2, -4, -1, 1, -2, F(1, 2)), ()),
    ("concave_flat", (1, 0, -1, 0, 0, 0), ()),
    ("concave_boundary", (-1, 2, -1, 1, 2, -1), ()),
)
FIXTURE = HERE / "native_occupation_support.json"
OWNED = (
    HERE / "NATIVE_OCCUPATION_SUPPORT_REDUCTION.md",
    HERE / "NATIVE_OCCUPATION_SUPPORT_PREREGISTRATION.md",
    HERE / "NATIVE_OCCUPATION_SUPPORT_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_native_six_hour_support.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def exact(value):
    require(type(value) in (int, F, str), "literal exact rational")
    if type(value) is str:
        require(len(value) <= 2500, "rational text cap")
    result = F(value)
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= 4096,
        "exact bit cap",
    )
    return result


def coefficient_tuple(value):
    require(type(value) is tuple and len(value) == 6, "six fixed coefficients")
    result = tuple(exact(x) for x in value)
    require(
        all(abs(x) <= 8 and x.denominator <= 16 for x in result),
        "declared coefficient cap",
    )
    return result


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(left, right):
    require(canonical(left) == canonical(right), "strict typed support replay differs")


def read_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def invalid(_value):
        raise ValueError("floating or nonfinite source value")

    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate source key")
            result[key] = value
        return result

    return json.loads(
        raw, parse_float=invalid, parse_constant=invalid, object_pairs_hook=unique
    )


def authenticate():
    raw, provenance = {}, []
    for commit, name, blob in PINS:
        ref = f"{commit}:{PREFIX}{name}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "frozen source byte cap")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            size == len(data)
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "frozen support source authentication",
        )
        raw[name] = data
        provenance.append({"commit": commit, "path": PREFIX + name, "blob": blob})
    return raw, provenance


def source():
    raw, provenance = authenticate()
    name = "native_occupation_moments.py"
    namespace = {
        "__name__": "authenticated_support_occupation",
        "__file__": str(HERE / name),
    }
    exec(compile(raw[name], str(HERE / name), "exec"), namespace)  # noqa: S102
    occupation = SimpleNamespace(**namespace)
    snapshot = read_json(raw["native_occupation_moments.json"])
    curve, data, inherited = occupation.authenticate()
    equal(snapshot["complete_ordered_records"], data["complete_ordered_records"])
    return occupation, curve, data, snapshot, provenance, inherited


def distinct(points):
    result = []
    for point in points:
        if not result or point != result[-1]:
            result.append(point)
    return tuple(result)


def unit(value):
    value = exact(value)
    require(0 <= value <= 1, "unit interval")
    return value


def clip(value, lower, upper):
    return min(upper, max(lower, value))


def planar_integral(points, a, b, c):
    total = F()
    for (left, low), (right, high) in pairwise(points):
        require(left <= right and low <= high, "monotone planar path")
        if left == right:
            continue
        slope = (high - low) / (right - left)
        intercept = low - slope * left
        terms = (
            c * intercept**2 + a * intercept,
            2 * c * slope * intercept + a * slope + b * intercept,
            c * slope**2 + b * slope,
        )
        total += sum(
            value * (right ** (i + 1) - left ** (i + 1)) / (i + 1)
            for i, value in enumerate(terms)
        )
    return exact(total)


def planar_optimizer(coefficients, left, right, lower, upper):
    a, b, c, *_ = coefficient_tuple(coefficients)
    left, right, lower, upper = map(unit, (left, right, lower, upper))
    require(left <= right and lower <= upper, "ordered isotonic interval")
    if left == right or lower == upper:
        points = distinct(((left, lower), (right, upper)))
        mode = "zero_length_or_constant"
    elif c > 0:
        if b <= 0:
            cuts = {left, right}
            if b:
                cuts.update(
                    x
                    for level in (lower, upper)
                    if left < (x := -(a + 2 * c * level) / b) < right
                )
            graph = tuple(
                (x, clip(-(a + b * x) / (2 * c), lower, upper)) for x in sorted(cuts)
            )
            mode = "increasing_affine_clip"
        else:
            value = clip(-(a + b * (left + right) / 2) / (2 * c), lower, upper)
            graph = ((left, value), (right, value))
            mode = "isotonic_constant"
        points = distinct(((left, lower),) + graph + ((right, upper),))
    else:
        cuts = {left, right}
        if b:
            candidate = -(a + c * (lower + upper)) / b
            if left <= candidate <= right:
                cuts.add(candidate)
        candidates = []
        for threshold in sorted(cuts):
            path = distinct(
                ((left, lower), (threshold, lower), (threshold, upper), (right, upper))
            )
            candidates.append((planar_integral(path, a, b, c), threshold, path))
        _, _, points = min(candidates)
        mode = "concave_single_threshold"
    return points, planar_integral(points, a, b, c), mode


def marked_optimizer(coefficients, s, t):
    coefficients = coefficient_tuple(coefficients)
    s, t = unit(s), unit(t)
    left, first, mode_left = planar_optimizer(coefficients, 0, s, 0, t)
    right, second, mode_right = planar_optimizer(coefficients, s, 1, t, 1)
    points = distinct(
        tuple((u, v, F()) for u, v in left)
        + ((s, t, F(1)),)
        + tuple((u, v, F(1)) for u, v in right)
    )
    _, _, _, d, e, f = coefficients
    value = first + second + d * (1 - s) + e * (1 - s**2) / 2 + f * (1 - t)
    return points, exact(value), (mode_left, mode_right)


def triangle_value(coefficients, s, r, order):
    a, b, c, d, e, f = coefficient_tuple(coefficients)
    s, r = unit(s), unit(r)
    require(order in ("w_before_v", "v_before_w"), "literal activation order")
    require(s <= r if order == "w_before_v" else r <= s, "activation triangle")
    return exact(
        (a + c) * (1 - r)
        + b * (1 - r**2) / 2
        + d * (1 - s)
        + e * (1 - s**2) / 2
        + (f if order == "w_before_v" else 0)
    )


def triangle_candidates(coefficients, order):
    a, b, c, d, e, _f = coefficient_tuple(coefficients)
    require(c <= 0, "two-triangle oracle requires c<=0")
    require(order in ("w_before_v", "v_before_w"), "literal activation order")
    vertices = (
        ((F(), F()), (F(), F(1)), (F(1), F(1)))
        if order == "w_before_v"
        else ((F(), F()), (F(1), F()), (F(1), F(1)))
    )
    points = set(vertices)
    for first, second in zip(vertices, vertices[1:] + vertices[:1], strict=True):
        s, r = first
        ds, dr = second[0] - s, second[1] - r
        linear = -d * ds - e * s * ds - (a + c) * dr - b * r * dr
        quadratic = -(e * ds**2 + b * dr**2) / 2
        if quadratic:
            t = -linear / (2 * quadratic)
            if 0 <= t <= 1:
                points.add((s + t * ds, r + t * dr))
    if b and e:
        s, r = -d / e, -(a + c) / b
        if (
            0 <= s <= 1
            and 0 <= r <= 1
            and (s <= r if order == "w_before_v" else r <= s)
        ):
            points.add((s, r))
    require(len(points) <= 12, "registered finite triangle candidate cap")
    return [
        (triangle_value(coefficients, s, r, order), s, r, order)
        for s, r in sorted(points)
    ]


def activation_path(s, r, order):
    s, r = unit(s), unit(r)
    triangle_value((0, 0, 0, 0, 0, 0), s, r, order)
    labels = ("w", "v") if order == "w_before_v" else ("v", "w")
    events = sorted(
        ((s, "w"), (r, "v")), key=lambda item: (item[0], labels.index(item[1]))
    )
    points, v, w = [ORIGIN], F(), F()
    for position, label in events:
        points.append((position, v, w))
        if label == "v":
            v = F(1)
        else:
            w = F(1)
        points.append((position, v, w))
    points.append(END)
    return distinct(points)


def collapse_w(coefficients, points):
    _, _, _, d, e, f = coefficient_tuple(coefficients)
    candidates = []
    for index, (start, end) in enumerate(pairwise(points)):
        u, v = start[:2]
        du, dv = end[0] - u, end[1] - v
        linear, quadratic = (d + e * u) * du + f * dv, e * du**2 / 2
        times = {F(), F(1)}
        if quadratic:
            value = -linear / (2 * quadratic)
            if 0 <= value <= 1:
                times.add(value)
        for value in sorted(times):
            s, t = u + value * du, v + value * dv
            candidates.append((d * s + e * s**2 / 2 + f * t, index, value, s, t))
    maximum = max(value[0] for value in candidates)
    _, index, _time, s, t = next(value for value in candidates if value[0] == maximum)
    before = tuple((x[0], x[1], F()) for x in points[: index + 1])
    after = tuple((x[0], x[1], F(1)) for x in points[index + 1 :])
    path = distinct(before + ((s, t, F()), (s, t, F(1))) + after)
    return path, (s, t), maximum


def path_certificate(occupation, curve, data, reference, points, coefficients):
    occupation.valid_path(curve, points)
    moments = occupation.path_moments(curve, points)
    actual = occupation.source_vector(curve, points, data["complete_ordered_records"])
    columns = [
        list(map(F, row["complete_source_vector"]))
        for row in data["coefficient_columns"]
    ]
    predicted = occupation.affine_source(curve, reference, columns, moments)
    require(
        actual == predicted and len(actual) == 63,
        "actual complete source versus occupation readout",
    )
    value = exact(
        sum(
            x * y for x, y in zip(coefficient_tuple(coefficients), moments, strict=True)
        )
    )
    return {
        "points": [list(map(str, point)) for point in points],
        "moments_A_B_C_D_E_F": list(map(str, moments)),
        "literal_functional_value": str(value),
        "all63_actual_source_records": list(map(str, actual)),
        "all63_match_frozen_affine_readout": True,
    }


def build():
    occupation, curve, data, snapshot, provenance, inherited = source()
    panels = occupation.path_panel(curve)
    reference_points = next(points for name, points, _ in panels if name == "axis_235")
    reference = occupation.source_vector(
        curve, reference_points, data["complete_ordered_records"]
    )
    equal(
        list(map(str, reference)),
        next(
            row["complete_source"]
            for row in snapshot["fixed_paths"]
            if row["name"] == "axis_235"
        ),
    )
    irregular = next(points for name, points, _ in panels if name == "irregular_one")
    equal(
        list(map(str, occupation.path_moments(curve, irregular))),
        next(
            row["moments"]
            for row in snapshot["fixed_paths"]
            if row["name"] == "irregular_one"
        ),
    )
    results = []
    for name, raw_coefficients, marks in PANELS:
        coefficients = coefficient_tuple(raw_coefficients)
        row = {"name": name, "coefficients_a_b_c_d_e_f": list(map(str, coefficients))}
        if coefficients[2] > 0:
            controls = []
            for s, t in marks:
                points, predicted, modes = marked_optimizer(coefficients, s, t)
                actual = path_certificate(
                    occupation, curve, data, reference, points, coefficients
                )
                require(
                    F(actual["literal_functional_value"]) == predicted,
                    "closed fixed-mark optimum versus actual native source",
                )
                controls.append(
                    {
                        "marked_s_t": [str(s), str(t)],
                        "isotonic_modes": list(modes),
                        "exact_planar_and_activation_value": str(predicted),
                        "source": actual,
                    }
                )
            row.update(
                {
                    "mode": "exact_fixed_marked_problem_only",
                    "global_two_dimensional_support_value_claimed": False,
                    "marked_controls": controls,
                }
            )
        else:
            candidates = triangle_candidates(
                coefficients, "w_before_v"
            ) + triangle_candidates(coefficients, "v_before_w")
            winner = min(candidates)
            value, s, r, order = winner
            actual = path_certificate(
                occupation,
                curve,
                data,
                reference,
                activation_path(s, r, order),
                coefficients,
            )
            require(
                F(actual["literal_functional_value"]) == value,
                "exact triangle support versus actual native path",
            )
            row.update(
                {
                    "mode": "exact_global_linear_support",
                    "candidate_values": [
                        {"value": str(v), "s": str(x), "r": str(y), "order": label}
                        for v, x, y, label in candidates
                    ],
                    "global_support_value": str(value),
                    "selected_source": actual,
                }
            )
        original = path_certificate(
            occupation, curve, data, reference, irregular, coefficients
        )
        collapsed, mark, maximum = collapse_w(coefficients, irregular)
        reduced = path_certificate(
            occupation, curve, data, reference, collapsed, coefficients
        )
        require(
            F(reduced["literal_functional_value"])
            <= F(original["literal_functional_value"]),
            "signed single-w source collapse cannot increase cost",
        )
        row["signed_single_w_control"] = {
            "original_value": original["literal_functional_value"],
            "marked_s_t": list(map(str, mark)),
            "maximum_Q_on_fixed_planar_path": str(maximum),
            "collapsed_source": reduced,
        }
        results.append(row)
    tied = []
    for order in ("w_before_v", "v_before_w"):
        tied.append(
            {
                "order": order,
                "source": path_certificate(
                    occupation,
                    curve,
                    data,
                    reference,
                    activation_path(F(1, 2), F(1, 2), order),
                    (0, 0, 0, 0, 0, 1),
                ),
            }
        )
    require(
        [row["source"]["literal_functional_value"] for row in tied] == ["1", "0"],
        "vertical activation order survives tied u coordinate",
    )
    result = {
        "schema": "riemann.native_six_hour.occupation_support.v1",
        "sources": provenance,
        "inherited_curvature_sources": inherited,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "complete_ordered_records": data["complete_ordered_records"],
        "registered_panels": results,
        "tied_vertical_orders": tied,
        "scope": {
            "all63_literal_records_for_selected_paths": True,
            "arbitrary_linear_support_reduction_proved": True,
            "positive_c_global_two_dimensional_solver_executed": False,
            "negative_c_finite_triangle_oracle_executed": True,
            "original_physical_quadratic_optimized": False,
            "convex_hull_minimum_identified_as_single_path": False,
            "full_retained_gamma_identified": False,
        },
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
        raw = (
            json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
        ).encode()
        require(len(raw) <= MAX_BYTES, "fixture byte cap")
        FIXTURE.write_bytes(raw)
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        equal(read_json(FIXTURE.read_bytes()), result)
    print(
        "PASS native support reduction, exact triangle oracle and all63 source controls"
    )


if __name__ == "__main__":
    main()
