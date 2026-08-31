#!/usr/bin/env python3
"""Complete bounded actual-path grids scored in the frozen original source metric."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from math import factorial, isqrt
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
# Exact discovery commit; kept separately from any later certificate implementation.
COMMIT = "46c8453e3976d242479202bf4d58489282a64d2a"
PINS = {
    "scout": (
        "native_affine_floor_scout.py",
        "e2ba2418fd842976d0a486db62c8a954baa7303a",
    ),
    "data": (
        "native_affine_floor.discovery.json",
        "350f264fb314d075388564089c04a080d8cb2c28",
    ),
}
MAX_BYTES = 8 * 1024 * 1024
MAX_PATHS = 35000
MAX_CLASSES = 40000
BITS = 512
DYADIC = 1 << BITS
SYMBOLS = "235"
SCHEMA = "riemann.native_six_hour.complete_monotone_grid.v1"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen(name, execute=False):
    path, blob = PINS[name]
    ref = f"{COMMIT}:{PREFIX}{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded exact source size")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen original Gram source",
    )
    if not execute:
        return raw
    namespace = {"__name__": "authenticated_grid_source", "__file__": str(HERE / path)}
    # Only the declared exact Git commit/blob-authenticated source is executable.
    exec(compile(raw, str(HERE / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def expression(kernel, value):
    require(
        type(value) is dict and set(value) == {"constant", "log2", "log3", "log5"},
        "exact original four-component expression",
    )
    result = tuple(
        {int(d): F(c) for d, c in value[name].items()}
        for name in ("constant", "log2", "log3", "log5")
    )
    require(
        kernel.expr_json(result) == value, "canonical exact expression coefficients"
    )
    return result


def coefficient_interval(value):
    lo, hi = map(F, value)
    require(lo <= hi, "coefficient interval order")
    require(
        max(max(x.numerator.bit_length(), x.denominator.bit_length()) for x in (lo, hi))
        <= 32768,
        "bounded exact coefficient arithmetic",
    )
    return (lo * DYADIC).__floor__(), (hi * DYADIC).__ceil__()


def interval_json(value):
    lo, hi = map(F, value)
    lo = F((lo * DYADIC).__floor__(), DYADIC)
    hi = F((hi * DYADIC).__ceil__(), DYADIC)
    require(
        max(max(x.numerator.bit_length(), x.denominator.bit_length()) for x in (lo, hi))
        <= 2048,
        "bounded outward interval serialization",
    )
    return {
        "lower": str(lo),
        "upper": str(hi),
        "approximate_midpoint": float((lo + hi) / 2),
    }


def source():
    affine = frozen("scout", True)
    discovery = json.loads(frozen("data"))
    curve, kernel, data, _tangent, provenance = affine.authenticate()
    records = data["complete_ordered_records"]
    ratios = [(row["a"], row["b"]) for row in data["ratio_order"]]
    require(len(records) == 63 and len(ratios) == 45, "whole H25 physical source")
    require(
        records == discovery["complete_ordered_records"]
        and data["coefficient_columns"] == discovery["basis_order"],
        "same source records and six ordered columns",
    )
    columns = [
        list(map(F, row["complete_source_vector"]))
        for row in data["coefficient_columns"]
    ]
    require(
        len(columns) == 6 and all(len(row) == 63 for row in columns),
        "complete six-column chart",
    )
    reference = list(
        map(
            F,
            next(row for row in discovery["actual_paths"] if row["name"] == "axis_235")[
                "complete_source"
            ],
        )
    )
    gram = [
        [expression(kernel, entry) for entry in row] for row in discovery["exact_Gram"]
    ]
    cross = [expression(kernel, entry) for entry in discovery["exact_cross_terms"]]
    constant = expression(kernel, discovery["exact_reference_energy"])
    require(
        len(gram) == len(cross) == 6 and all(len(row) == 6 for row in gram),
        "six-dimensional physical Gram",
    )
    fields = [
        affine.source_field(curve, kernel, vector, records, ratios)
        for vector in columns
    ]
    reference_field = affine.source_field(curve, kernel, reference, records, ratios)
    require(
        all(
            affine.inner(kernel, fields[i], fields[j]) == gram[i][j]
            for i in range(6)
            for j in range(6)
        ),
        "independent complete original Gram reconstruction",
    )
    require(
        [affine.inner(kernel, field, reference_field) for field in fields] == cross
        and affine.inner(kernel, reference_field, reference_field) == constant,
        "independent original cross terms and endpoint reference",
    )
    intervals = {
        "constant": coefficient_interval(kernel.ei(constant)),
        "cross": [coefficient_interval(kernel.ei(x)) for x in cross],
        "gram": [[coefficient_interval(kernel.ei(x)) for x in row] for row in gram],
    }
    return SimpleNamespace(
        affine=affine,
        curve=curve,
        kernel=kernel,
        discovery=discovery,
        records=records,
        ratios=ratios,
        columns=columns,
        reference=reference,
        gram=gram,
        cross=cross,
        constant=constant,
        intervals=intervals,
        provenance=provenance,
    )


def valid_grid(n):
    require(type(n) is int and 1 <= n <= 4, "bounded exact grid size")


def increment(n, state, coordinate):
    valid_grid(n)
    require(
        type(state) is tuple
        and len(state) == 3
        and all(type(x) is int and 0 <= x <= n for x in state),
        "bounded exact grid state",
    )
    require(
        type(coordinate) is int and 0 <= coordinate < 3 and state[coordinate] < n,
        "available exact axis step",
    )
    k, ell, m = state
    if coordinate == 0:
        return (
            2 * n * ell,
            ell * (2 * k + 1),
            ell * ell,
            2 * n * m,
            m * (2 * k + 1),
            0,
        )
    if coordinate == 1:
        return (0, 0, 0, 0, 0, 2 * n * m)
    return (0,) * 6


def word_path(n, word):
    valid_grid(n)
    require(
        type(word) is str
        and len(word) == 3 * n
        and all(word.count(s) == n for s in SYMBOLS),
        "complete exact monotone grid word",
    )
    state = (0, 0, 0)
    numerators = (0,) * 6
    points = [(F(),) * 3]
    for symbol in word:
        coordinate = SYMBOLS.index(symbol)
        delta = increment(n, state, coordinate)
        numerators = tuple(x + y for x, y in zip(numerators, delta, strict=True))
        state = tuple(x + int(i == coordinate) for i, x in enumerate(state))
        points.append(tuple(F(x, n) for x in state))
    return numerators, points


def scores(intervals, numerators, denominator):
    require(
        len(numerators) == 6 and all(type(x) is int and x >= 0 for x in numerators),
        "nonnegative exact source numerators",
    )
    require(
        type(denominator) is int and denominator > 0,
        "positive exact source denominator",
    )
    result = []
    for side in (0, 1):
        value = intervals["constant"][side] * denominator * denominator
        value += (
            2
            * denominator
            * sum(intervals["cross"][i][side] * numerators[i] for i in range(6))
        )
        value += sum(
            intervals["gram"][i][j][side] * numerators[i] * numerators[j]
            for i in range(6)
            for j in range(6)
        )
        result.append(value)
    require(result[0] <= result[1], "outward exact integer energy scores")
    return tuple(result)


def energy(model, coordinates):
    kernel = model.kernel
    result = model.constant
    for i in range(6):
        result = kernel.ea(
            result, kernel.er(model.cross[i], kernel.scalar(2 * coordinates[i]))
        )
        for j in range(6):
            result = kernel.ea(
                result,
                kernel.er(
                    model.gram[i][j], kernel.scalar(coordinates[i] * coordinates[j])
                ),
            )
    return result


def enumerate_paths(n, intervals):
    valid_grid(n)
    expected = factorial(3 * n) // factorial(n) ** 3
    require(expected <= MAX_PATHS, "complete path cap")
    denominator = 2 * n**3
    digest = sha256()
    count = 0
    best_upper = None
    candidates = {}

    def visit(state, numerators, word):
        nonlocal count, best_upper, candidates
        if len(word) == 3 * n:
            count += 1
            require(count <= MAX_PATHS, "streamed leaf cap")
            lo, hi = scores(intervals, numerators, denominator)
            digest.update(
                (
                    word
                    + "|"
                    + ",".join(map(str, numerators))
                    + "|"
                    + str(lo)
                    + "|"
                    + str(hi)
                    + "\n"
                ).encode()
            )
            if best_upper is None or hi < best_upper:
                best_upper = hi
                candidates = {
                    key: row
                    for key, row in candidates.items()
                    if row["lower_score"] <= hi
                }
            if lo <= best_upper:
                if numerators in candidates:
                    row = candidates[numerators]
                    require(
                        (row["lower_score"], row["upper_score"]) == (lo, hi),
                        "identical occupation class score",
                    )
                    row["word_multiplicity"] += 1
                else:
                    candidates[numerators] = {
                        "first_word": word,
                        "word_multiplicity": 1,
                        "lower_score": lo,
                        "upper_score": hi,
                    }
                    require(len(candidates) <= MAX_CLASSES, "candidate class cap")
            return
        for coordinate, symbol in enumerate(SYMBOLS):
            if state[coordinate] == n:
                continue
            delta = increment(n, state, coordinate)
            next_state = tuple(x + int(i == coordinate) for i, x in enumerate(state))
            next_numerators = tuple(
                x + y for x, y in zip(numerators, delta, strict=True)
            )
            visit(next_state, next_numerators, word + symbol)

    visit((0, 0, 0), (0,) * 6, "")
    require(count == expected and candidates, "complete nonempty exhaustive census")
    return {
        "count": count,
        "expected": expected,
        "digest": digest.hexdigest(),
        "denominator": denominator,
        "best_upper": best_upper,
        "candidates": candidates,
    }


def exact_sqrt_upper(value):
    value = F(value)
    require(value >= 0, "nonnegative norm-square upper bound")
    answer = isqrt(value.numerator // value.denominator)
    return answer + int(F(answer * answer) < value)


def convergence_constants(model):
    widths = (F(2), F(3, 2), F(3, 2), F(2), F(3, 2), F(2))
    maxima = (F(1), F(1, 2), F(1, 2), F(1), F(1, 2), F(1))
    norms = [
        exact_sqrt_upper(F(model.intervals["gram"][i][i][1], DYADIC)) for i in range(6)
    ]
    reference = exact_sqrt_upper(F(model.intervals["constant"][1], DYADIC))
    c_source = sum(a * b for a, b in zip(widths, norms, strict=True))
    uniform = reference + sum(a * b for a, b in zip(maxima, norms, strict=True))
    return {
        "source_vector_norm_upper_integers": norms,
        "reference_norm_upper_integer": reference,
        "C_source_upper": str(c_source),
        "uniform_field_norm_upper": str(uniform),
        "energy_rate_constant_upper": str(2 * uniform * c_source),
    }


def certify_panel(model, n, constants):
    census = enumerate_paths(n, model.intervals)
    denominator = census["denominator"]
    full_denominator = DYADIC * denominator**2
    rows, expressions = [], []
    for numerators, candidate in sorted(census["candidates"].items()):
        coordinates = tuple(F(x, denominator) for x in numerators)
        replay_numerators, points = word_path(n, candidate["first_word"])
        require(replay_numerators == numerators, "independent winner word replay")
        literal = model.affine.literal_path(model.curve, points, model.records)
        predicted = [
            model.reference[k]
            + sum(coordinates[i] * model.columns[i][k] for i in range(6))
            for k in range(63)
        ]
        require(literal == predicted, "all63 original derivative records agree")
        image = model.curve.ratio_image(literal, model.records, model.ratios)
        field = model.affine.source_field(
            model.curve, model.kernel, literal, model.records, model.ratios
        )
        exact_energy = energy(model, coordinates)
        require(
            model.affine.inner(model.kernel, field, field) == exact_energy,
            "all45 physical ratios and full original cross-energy replay",
        )
        exact_interval = model.kernel.ei(exact_energy)
        score_interval = (
            F(candidate["lower_score"], full_denominator),
            F(candidate["upper_score"], full_denominator),
        )
        require(
            score_interval[0] <= exact_interval[1]
            and exact_interval[0] <= score_interval[1],
            "independent interval evaluations overlap",
        )
        expressions.append(exact_energy)
        rows.append(
            {
                "source_numerators": list(numerators),
                "coordinates": list(map(str, coordinates)),
                **candidate,
                "energy_interval": interval_json(score_interval),
                "exact_original_energy": model.kernel.expr_json(exact_energy),
                "complete63_literal_source": list(map(str, literal)),
                "complete45_rational_ratio_image": list(map(str, image)),
            }
        )
    all_equal = all(x == expressions[0] for x in expressions)
    minimum_interval = (
        F(
            min(x["lower_score"] for x in census["candidates"].values()),
            full_denominator,
        ),
        F(census["best_upper"], full_denominator),
    )
    controls = []
    for row in model.discovery["actual_paths"]:
        control = expression(model.kernel, row["exact_energy"])
        difference = model.kernel.ea(control, model.kernel.es(expressions[0], -1))
        controls.append(
            {
                "name": row["name"],
                "control_minus_first_candidate": interval_json(
                    model.kernel.ei(difference)
                ),
            }
        )
    synchronized = energy(model, (F(1, 2), F(1, 3), F(1, 6), F(), F(), F()))
    controls.append(
        {
            "name": "exact_synchronized_face_minimum",
            "control_minus_first_candidate": interval_json(
                model.kernel.ei(
                    model.kernel.ea(synchronized, model.kernel.es(expressions[0], -1))
                )
            ),
        }
    )
    rate = F(constants["energy_rate_constant_upper"])
    inherited = F(model.discovery["best_single_halfspace_bound"]["certified_lower"])
    return {
        "N": n,
        "path_count": census["count"],
        "expected_path_count": census["expected"],
        "complete_word_coordinate_score_sha256": census["digest"],
        "coordinate_denominator": denominator,
        "integer_score_denominator": str(full_denominator),
        "surviving_coordinate_class_count": len(rows),
        "surviving_word_count": sum(row["word_multiplicity"] for row in rows),
        "minimum_status": "exact_all_surviving_classes_tie"
        if all_equal
        else "certified_minimum_bracket_unresolved_class_order",
        "all_surviving_classes": rows,
        "minimum_energy_interval": interval_json(minimum_interval),
        "all_declared_comparisons": controls,
        "all_path_infimum_bounds": {
            "lower": str(max(inherited, minimum_interval[0] - rate / n)),
            "upper": str(minimum_interval[1]),
            "source_halfspace_lower": str(inherited),
            "grid_approximation_lower": str(minimum_interval[0] - rate / n),
        },
        "all_path_optimizer_claimed": False,
    }


def discover(mode):
    require(mode in ("calibration", "heldout"), "preregistered grid phase")
    model = source()
    constants = convergence_constants(model)
    panels = (2, 3) if mode == "calibration" else (4,)
    owned = {}
    for path in (
        Path(__file__),
        HERE / "NATIVE_MONOTONE_GRID_PREREGISTRATION.md",
        HERE / "NATIVE_MONOTONE_GRID_CONVERGENCE.md",
    ):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "bounded owned source")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": SCHEMA,
        "phase": mode,
        "sources": [
            {"commit": COMMIT, "path": PREFIX + path, "blob": blob}
            for path, blob in PINS.values()
        ],
        "transitive_source_provenance": model.provenance,
        "owned_sha256_lf": owned,
        "complete63_record_order": model.records,
        "complete45_ratio_order": [{"a": a, "b": b} for a, b in model.ratios],
        "dyadic_coefficient_denominator": str(DYADIC),
        "quantized_original_metric": model.intervals,
        "convergence_constants": constants,
        "panels": [certify_panel(model, n, constants) for n in panels],
        "all_source_cross_terms_retained": True,
        "literal_source_measure": "2ds",
        "original_Mellin_measure": True,
        "floating_selection_used": False,
        "full_gamma_source_identified": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "heldout"), required=True)
    args = parser.parse_args()
    output = (
        json.dumps(discover(args.phase), sort_keys=True, indent=2, allow_nan=False)
        + "\n"
    )
    require(len(output.encode()) <= MAX_BYTES, "bounded complete-grid artifact")
    print(output, end="")


if __name__ == "__main__":
    main()
