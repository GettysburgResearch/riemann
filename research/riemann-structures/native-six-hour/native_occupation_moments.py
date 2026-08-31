#!/usr/bin/env python3
"""Exact native occupation moments and complete iid event-order laws."""

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
FREEZE = "bae7184724093d3589ad16b278dc104322428d6a"
PINS = {
    "scout": (
        "native_curvature_span_scout.py",
        "e660bfaa86ca3562189d47c89390984fc1e3117c",
    ),
    "discovery": (
        "native_curvature_span.discovery.json",
        "1bb6e7fba73d796d064d397ef95bda1ee770f48a",
    ),
    "preregistration": (
        "NATIVE_CURVATURE_SPAN_PREREGISTRATION.md",
        "1452d6977f817818c67c7e5244dd03de4228a992",
    ),
}
MAX_BYTES = 4 * 1024 * 1024
ORIGIN = (F(),) * 3
END = (F(1),) * 3
CURVED = (
    (F(), F()),
    (F(1), F(1)),
    (F(1, 4), F(1, 16)),
    (F(1, 4), F(1, 8)),
    (F(1, 4), F(1, 4)),
    (F(1, 2), F(1, 4)),
    (F(1, 2), F(3, 8)),
    (F(1, 2), F(1, 2)),
    (F(3, 4), F(9, 16)),
    (F(3, 4), F(21, 32)),
    (F(3, 4), F(3, 4)),
)
MOMENT_FORMS = (
    ((0, 1, 0), 0),
    ((1, 1, 0), 0),
    ((0, 2, 0), 0),
    ((0, 0, 1), 0),
    ((1, 0, 1), 0),
    ((0, 0, 1), 1),
)
FIXTURE = HERE / "native_occupation_moments.json"
OWNED = (
    HERE / "NATIVE_OCCUPATION_MOMENTS.md",
    HERE / "NATIVE_OCCUPATION_PREREGISTRATION.md",
    HERE / "NATIVE_OCCUPATION_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_native_six_hour_occupation.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected),
        "strict typed occupation replay differs",
    )


def strict_load(data):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def invalid(value):
        raise ValueError("floating or nonfinite JSON value: " + value)

    return json.loads(
        data, object_pairs_hook=pairs, parse_float=invalid, parse_constant=invalid
    )


def authenticate():
    raw, provenance = {}, []
    for name, (filename, blob) in PINS.items():
        path = PREFIX + filename
        ref = f"{FREEZE}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "frozen source size")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(data) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "exact frozen blob",
        )
        raw[name] = data
        provenance.append(
            {
                "commit": FREEZE,
                "path": path,
                "blob": blob,
                "sha256": sha256(data).hexdigest(),
            }
        )
    namespace = {
        "__name__": "authenticated_occupation_source",
        "__file__": str(HERE / PINS["scout"][0]),
    }
    exec(compile(raw["scout"], namespace["__file__"], "exec"), namespace)  # noqa: S102
    module = SimpleNamespace(**namespace)
    frozen = strict_load(raw["discovery"])
    strict_equal(module.discover(), frozen)
    return module, frozen, provenance


def all_words():
    words = sorted(set(permutations((2, 2, 3, 3, 5))))
    require(len(words) == 30, "complete multiset word enumeration")
    return words


def word_moments(word):
    require(
        type(word) is tuple and sorted(word) == [2, 2, 3, 3, 5], "literal word domain"
    )
    twos = [i for i, label in enumerate(word) if label == 2]
    threes = [i for i, label in enumerate(word) if label == 3]
    five = word.index(5)
    return (
        F(sum(i < j for i in threes for j in twos), 4),
        F(sum(i < max(twos) for i in threes), 4),
        F(sum(i > max(threes) for i in twos), 2),
        F(sum(i > five for i in twos), 2),
        F(five < max(twos), 2),
        F(sum(i > five for i in threes), 2),
    )


def valid_path(module, points):
    require(type(points) is tuple and 2 <= len(points) <= 7, "fixed path segment cap")
    require(points[0] == ORIGIN and points[-1] == END, "whole path endpoints")
    for start, end in pairwise(points):
        module.restrict_segment({(0, 0, 0): F(1)}, start, end)
    return points


def curve_path(a, c):
    require(
        type(a) is F and type(c) is F and 0 <= a <= 1 and a * a <= c <= a,
        "curved projection domain",
    )
    if not a:
        return (ORIGIN, (F(1), F(), F()), (F(1), F(1), F()), END)
    height = c / a
    start = 1 - a * a / c
    return (
        ORIGIN,
        (start, F(), F()),
        (start, height, F()),
        (F(1), height, F()),
        (F(1), F(1), F()),
        END,
    )


def path_panel(module):
    result = []
    for order in permutations(range(3)):
        points, point = [ORIGIN], list(ORIGIN)
        for coordinate in order:
            point = point.copy()
            point[coordinate] = F(1)
            points.append(tuple(point))
        result.append(
            ("axis_" + "".join(str((2, 3, 5)[i]) for i in order), tuple(points), None)
        )
    result.append(("diagonal", (ORIGIN, END), None))
    result.append(
        (
            "irregular_one",
            (ORIGIN, (F(1, 5), F(1, 3), F(1, 7)), (F(2, 3), F(3, 4), F(4, 5)), END),
            None,
        )
    )
    result.append(
        (
            "irregular_two",
            (ORIGIN, (F(1, 2), F(), F(1, 4)), (F(1, 2), F(2, 3), F(1, 4)), END),
            None,
        )
    )
    for a, c in CURVED:
        result.append((f"curve_{a}_{c}", curve_path(a, c), (a, c)))
    require(len(result) == 20, "all fixed paths retained")
    for _, points, _ in result:
        valid_path(module, points)
    return result


def path_moments(module, points):
    result = [F()] * 6
    for start, end in pairwise(points):
        for i, (power, coordinate) in enumerate(MOMENT_FORMS):
            restriction = module.restrict_segment({power: F(1)}, start, end)
            result[i] += (end[coordinate] - start[coordinate]) * sum(
                (value / F(degree + 1) for degree, value in restriction.items()), F()
            )
    return tuple(module.rational(value) for value in result)


def word_probability(module, points, word, multiplicity=4):
    require(
        type(multiplicity) is int and multiplicity in (1, 4),
        "declared iid multiplicity control",
    )
    cumulatives = [F(1)] + [F()] * 5
    coordinates = {2: 0, 3: 1, 5: 2}
    for start, end in pairwise(points):
        previous = {0: F(1)}
        updated = [F(1)]
        for length, label in enumerate(word, 1):
            delta = end[coordinates[label]] - start[coordinates[label]]
            polynomial = {0: cumulatives[length]}
            for degree, value in previous.items():
                polynomial[degree + 1] = module.rational(delta * value / F(degree + 1))
            polynomial = module.upoly(polynomial)
            updated.append(module.rational(sum(polynomial.values(), F())))
            previous = polynomial
        cumulatives = updated
    return module.rational(multiplicity * cumulatives[-1])


def source_vector(module, points, records):
    numbers = module.panel_numbers()
    source = {n: module.half_source(n) for n in numbers}
    return [
        module.rational(
            sum(
                (
                    module.edge_integral(source[row["n"]], source[row["m"]], start, end)
                    for start, end in pairwise(points)
                ),
                F(),
            )
        )
        for row in records
    ]


def affine_source(module, reference, columns, moments):
    a, b, c, d, e, f = moments
    coefficients = (a, b, c / 2, d, e, f)
    return [
        module.rational(
            reference[i]
            + sum(
                (
                    weight * column[i]
                    for weight, column in zip(coefficients, columns, strict=True)
                ),
                F(),
            )
        )
        for i in range(len(reference))
    ]


def constraints(moments):
    a, b, c, d, e, f = moments
    return {
        "Jensen_C_minus_A_squared": c - a * a,
        "C_upper_A_minus_C": a - c,
        "B_lower": b - a / 2,
        "B_upper": a - a * a / 2 - b,
        "E_lower": e - d / 2,
        "E_upper": d - d * d / 2 - e,
        "three_label_lower": a + f - d,
        "three_label_upper": 1 - a - f + d,
    }


def build():
    module, data, provenance = authenticate()
    words = all_words()
    word_coordinates = [word_moments(word) for word in words]
    records = data["complete_ordered_records"]
    ratios = [(row["a"], row["b"]) for row in data["ratio_order"]]
    columns = [
        list(map(F, column["complete_source_vector"]))
        for column in data["coefficient_columns"]
    ]
    require(len(records) == 63 and len(columns) == 6, "complete native domain")
    panel = path_panel(module)
    reference = source_vector(module, panel[0][1], records)
    require(
        path_moments(module, panel[0][1]) == (F(),) * 6, "reference source axis order"
    )
    paths = []
    for name, points, curve in panel:
        moments = path_moments(module, points)
        probabilities = [word_probability(module, points, word) for word in words]
        require(
            all(value >= 0 for value in probabilities) and sum(probabilities, F()) == 1,
            "complete nonnegative iid word law",
        )
        expectations = tuple(
            sum(
                (
                    p * coords[i]
                    for p, coords in zip(probabilities, word_coordinates, strict=True)
                ),
                F(),
            )
            for i in range(6)
        )
        require(
            expectations == moments,
            "six exact word expectations equal native one-forms",
        )
        actual = source_vector(module, points, records)
        predicted = affine_source(module, reference, columns, moments)
        require(
            actual == predicted,
            "all63 original native records equal occupation reconstruction",
        )
        observed = module.ratio_image(actual, records, ratios)
        require(
            observed == module.ratio_image(predicted, records, ratios),
            "complete physical ratio observation",
        )
        slack = constraints(moments)
        require(
            all(value >= 0 for value in slack.values()),
            "necessary nonlinear native constraints",
        )
        if curve is not None:
            a, c = curve
            expected_b = a - a**3 / (2 * c) if a else F()
            require(
                moments == (a, expected_b, c, F(), F(), F()),
                "constructive whole-curve formula on fixed rational panel",
            )
        if name == "diagonal":
            require(
                probabilities == [F(1, 30)] * 30,
                "all iid diagonal words equally likely",
            )
            require(
                moments == (F(1, 2), F(1, 3), F(1, 3), F(1, 2), F(1, 3), F(1, 2)),
                "diagonal one-form moments",
            )
        if name.startswith("axis_"):
            require(
                sum(value == 1 for value in probabilities) == 1,
                "deterministic cohort axis law",
            )
        paths.append(
            {
                "name": name,
                "vertices": [list(map(str, point)) for point in points],
                "moments": list(map(str, moments)),
                "all_word_probabilities": list(map(str, probabilities)),
                "word_expectations": list(map(str, expectations)),
                "complete_source": list(map(str, actual)),
                "physical_rational_ratio_image": list(map(str, observed)),
                "necessary_constraint_slacks": {
                    key: str(value) for key, value in slack.items()
                },
            }
        )
    bad_word = (3, 2, 2, 3, 5)
    bad = word_moments(bad_word)
    require(
        bad == (F(1, 2), F(1, 4), F(), F(), F(), F()), "fixed counterfeit event order"
    )
    require(
        constraints(bad)["Jensen_C_minus_A_squared"] == F(-1, 4),
        "non-native order point",
    )
    wrong_mass = sum(
        (word_probability(module, (ORIGIN, END), word, 1) for word in words), F()
    )
    require(wrong_mass == F(1, 4), "omitted iid factorial counterfeit")
    bindings = {}
    for path in OWNED:
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned source byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.occupation_moments.v1",
        "sources": provenance,
        "owned_sha256_lf": bindings,
        "curvature_discovery_object": data["proof_object_sha256"],
        "moment_order": ["A", "B", "C", "D", "E", "F"],
        "complete_ordered_records": records,
        "ratio_order": data["ratio_order"],
        "words": [
            {"word": list(word), "moments": list(map(str, moments))}
            for word, moments in zip(words, word_coordinates, strict=True)
        ],
        "fixed_paths": paths,
        "counterfeit": {
            "word": list(bad_word),
            "moments": list(map(str, bad)),
            "Jensen_slack": "-1/4",
            "formal_affine_source": list(
                map(str, affine_source(module, reference, columns, bad))
            ),
            "native_path_claimed": False,
        },
        "missing_factorial_total_probability": str(wrong_mass),
        "scope": {
            "all_63_original_source_records_retained": True,
            "original_physical_ratio_weights": True,
            "all_native_moment_body_claimed_as_word_polytope": False,
            "projection_A_C_characterized_by_proof": True,
            "six_dimensional_body_fully_characterized": False,
            "full_post_renewal_gamma_decoder_identified": False,
            "native_energy_minimizer_claimed": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def check(candidate):
    strict_equal(candidate, build())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        output = (
            json.dumps(build(), sort_keys=True, indent=2, allow_nan=False) + "\n"
        ).encode()
        require(len(output) <= MAX_BYTES, "artifact byte cap")
        FIXTURE.write_bytes(output)
    else:
        raw = FIXTURE.read_bytes()
        require(len(raw) <= MAX_BYTES, "artifact byte cap")
        check(strict_load(raw))
    print("PASS native occupation moments, all20 paths and30 iid words")


if __name__ == "__main__":
    main()
