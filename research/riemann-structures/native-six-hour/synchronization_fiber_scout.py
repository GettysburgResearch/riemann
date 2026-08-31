#!/usr/bin/env python3
"""Exact native source fibres, synchronization failure, and curvature enrichment."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import pairwise
from math import comb, gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = (
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
        "6810bcece309b0c54ae6c8fc84b314990004549c",
    ),
    (
        "6b18fbd9bc0a493e739166e6fcb9fbefd8e4d537",
        PREFIX + "NATIVE_CURVATURE_SPAN.md",
        "a61a6fb8bbf63a4cb838f806afe64da0d8ef10a4",
    ),
    (
        "a75f3bbef5f75bb6a4bd7f3c91d051cfb132f3dc",
        PREFIX + "NATIVE_OCCUPATION_MOMENTS.md",
        "bea7d2be82e752ffe471a4e9902ca5bbc73c50aa",
    ),
)
PRIMES = (2, 3, 5)
MAX_BYTES = 8 * 1024 * 1024
RECTANGLES = (
    (F(1, 8), F(1, 4)),
    (F(3, 8), F(1, 4)),
    (F(5, 8), F(1, 4)),
    (F(7, 8), F(1, 4)),
    (F(1, 8), F(3, 4)),
    (F(3, 8), F(3, 4)),
    (F(5, 8), F(3, 4)),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rational(value):
    require(type(value) in (int, F), "literal rational arithmetic")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 4096,
        "rational bit cap",
    )
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate():
    result = []
    for commit, path, blob in PINS:
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(raw) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
            "exact source authentication",
        )
        result.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": sha256(raw).hexdigest(),
            }
        )
    return result


def poly(values=None):
    result = {}
    for degree, value in (values or {}).items():
        require(type(degree) is int and 0 <= degree <= 24, "path polynomial degree cap")
        value = rational(value)
        if value:
            result[degree] = value
    return result


def add(left, right):
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, F()) + value
    return poly(result)


def scale(value, factor):
    return poly({degree: coefficient * factor for degree, coefficient in value.items()})


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F()) + a * b
    return poly(result)


def derivative(value):
    return poly(
        {
            degree - 1: degree * coefficient
            for degree, coefficient in value.items()
            if degree
        }
    )


def integral(value):
    return rational(
        sum((coefficient / F(degree + 1) for degree, coefficient in value.items()), F())
    )


def evaluate(value, t):
    return rational(
        sum((coefficient * t**degree for degree, coefficient in value.items()), F())
    )


def moments(value):
    return [integral(multiply(value, {degree: F(1)})) for degree in range(5)]


def null_polynomial():
    exponents = (0, 1, 3, 4)
    matrix = [
        [F(2, (j + k + 4) * (j + k + 5) * (j + k + 6)) for k in range(5)]
        for j in exponents
    ]
    reduced = [row.copy() for row in matrix]
    pivots = []
    row = 0
    for column in range(5):
        selected = next((r for r in range(row, 4) if reduced[r][column]), None)
        if selected is None:
            continue
        reduced[row], reduced[selected] = reduced[selected], reduced[row]
        leading = reduced[row][column]
        reduced[row] = [rational(value / leading) for value in reduced[row]]
        for r in range(4):
            if r != row:
                factor = reduced[r][column]
                reduced[r] = [
                    rational(a - factor * b)
                    for a, b in zip(reduced[r], reduced[row], strict=True)
                ]
        pivots.append(column)
        row += 1
        if row == 4:
            break
    require(len(pivots) == 4, "full rank four moment equations")
    free = next(k for k in range(5) if k not in pivots)
    vector = [F()] * 5
    vector[free] = F(1)
    for row, column in enumerate(pivots):
        vector[column] = -reduced[row][free]
    denominator = lcm(*(value.denominator for value in vector))
    integers = [int(value * denominator) for value in vector]
    common = gcd(*integers)
    integers = [value // common for value in integers]
    if next(value for value in reversed(integers) if value) < 0:
        integers = [-value for value in integers]
    q = poly(dict(enumerate(integers)))
    p = multiply({3: F(1), 4: F(-2), 5: F(1)}, q)
    observed = moments(p)
    require(
        all(observed[j] == 0 for j in exponents) and observed[2] != 0,
        "orthogonal moments and nonzero missing moment",
    )
    tangent = derivative(p)
    require(all(degree >= 2 for degree in tangent), "P prime divisible by t squared")
    normalized = poly({degree - 2: value for degree, value in tangent.items()})
    norm = sum(map(abs, normalized.values()), F())
    delta = 1 / (1 + norm)
    plus = add({3: F(1)}, scale(p, delta))
    minus = add({3: F(1)}, scale(p, -delta))
    require(3 - delta * norm > 2, "uniform polynomial monotonicity certificate")
    for value in (plus, minus):
        require(
            evaluate(value, F()) == 0 and evaluate(value, F(1)) == 1,
            "actual schedule endpoints",
        )
    return (
        q,
        p,
        delta,
        plus,
        minus,
        {
            "matrix": [list(map(str, row)) for row in matrix],
            "row_exponents": list(exponents),
            "pivot_columns": pivots,
            "primitive_Q_coefficients": integers,
            "P_coefficients": poly_json(p),
            "P_moments_0_through_4": list(map(str, observed)),
            "P_prime_div_t_squared": poly_json(normalized),
            "coefficient_l1_norm": str(norm),
            "delta": str(delta),
            "normalized_derivative_lower": str(3 - delta * norm),
        },
    )


def binomial_half(degree):
    require(
        type(degree) is int and 0 <= degree <= 8, "declared local coefficient degree"
    )
    value = F(1)
    for k in range(1, degree + 1):
        value *= -(F(1, 2) - k + 1) / k
    return rational(value)


def exponents(n):
    require(type(n) is int and 1 <= n <= 300, "declared source horizon")
    result = []
    for prime in PRIMES:
        degree = 0
        while n % prime == 0:
            n //= prime
            degree += 1
        result.append(degree)
    require(n == 1, "declared prime support")
    return result


def numbers(horizon):
    require(horizon in (60, 300) and type(horizon) is int, "fixed horizon")
    result = []
    for n in range(1, horizon + 1):
        residual = n
        for prime in PRIMES:
            while residual % prime == 0:
                residual //= prime
        if residual == 1:
            result.append(n)
    return result


def local(degree):
    start = binomial_half(degree // 2) if degree % 2 == 0 else F()
    return start, binomial_half(degree) - start


def path_source(n, schedules):
    result = {0: F(1)}
    for degree, schedule in zip(exponents(n), schedules, strict=True):
        start, slope = local(degree)
        result = multiply(result, add({0: start}, scale(schedule, slope)))
    return result


def pair_integral(left, right):
    return integral(scale(multiply(derivative(left), right), 2))


def records(horizon):
    result = []
    for n in numbers(horizon):
        for m in numbers(horizon):
            if n * m <= horizon:
                common = gcd(n, m)
                result.append(
                    {"n": n, "m": m, "d": common, "a": n // common, "b": m // common}
                )
    require(len(result) <= 2000, "complete record cap")
    return result


def vector_paths(rows, plus, minus):
    panel = sorted({r["n"] for r in rows} | {r["m"] for r in rows})
    first = {n: path_source(n, ({}, {1: F(1)}, {})) for n in panel}
    result = {}
    for name, w in (("plus", plus), ("minus", minus)):
        original = {n: path_source(n, ({1: F(1)}, {0: F(1)}, w)) for n in panel}
        synchronized = {n: path_source(n, ({1: F(1)}, {1: F(1)}, w)) for n in panel}
        result[name] = [
            pair_integral(first[r["n"]], first[r["m"]])
            + pair_integral(original[r["n"]], original[r["m"]])
            for r in rows
        ]
        result["sync_" + name] = [
            pair_integral(synchronized[r["n"]], synchronized[r["m"]]) for r in rows
        ]
    return result


def ratio_image(vector, rows):
    result = {}
    for value, row in zip(vector, rows, strict=True):
        key = (row["a"], row["b"])
        result[key] = rational(result.get(key, F()) + value / row["d"])
    return result


def poly2(values=None):
    result = {}
    for key, value in (values or {}).items():
        require(
            type(key) is tuple
            and len(key) == 2
            and all(type(v) is int for v in key)
            and 0 <= key[0] <= 4
            and 0 <= key[1] <= 2,
            "bivariate source degree cap",
        )
        value = rational(value)
        if value:
            result[key] = value
    return result


def add2(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, F()) + value
    return poly2(result)


def scale2(value, scalar):
    return poly2({key: scalar * coefficient for key, coefficient in value.items()})


def multiply2(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            key = (i + k, j + l)
            result[key] = result.get(key, F()) + a * b
    return poly2(result)


def derivative2(value, coordinate):
    result = {}
    for key, coefficient in value.items():
        if key[coordinate]:
            target = list(key)
            target[coordinate] -= 1
            result[tuple(target)] = key[coordinate] * coefficient
    return poly2(result)


def source2(n, synchronized):
    result = {(0, 0): F(1)}
    for index, degree in enumerate(exponents(n)):
        start, slope = local(degree)
        if index == 1 and not synchronized:
            factor = {(0, 0): start + slope}
        else:
            power = (0, 1) if index == 2 else (1, 0)
            factor = {(0, 0): start, power: slope}
        result = multiply2(result, poly2(factor))
    return result


def rank_columns(columns):
    require(
        len(columns) <= 7 and all(len(col) <= 2000 for col in columns),
        "rank matrix cap",
    )
    pivots = {}
    selected = []
    for index, column in enumerate(columns):
        vector = {i: rational(value) for i, value in enumerate(column) if value}
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                lead = vector[pivot]
                pivots[pivot] = {
                    i: rational(value / lead) for i, value in vector.items()
                }
                selected.append(index)
                break
            lead = vector[pivot]
            for row, value in pivots[pivot].items():
                new = rational(vector.get(row, F()) - lead * value)
                if new:
                    vector[row] = new
                else:
                    vector.pop(row, None)
    return {
        "rank": len(pivots),
        "selected_columns": selected,
        "pivot_rows": list(pivots),
    }


def rectangle_integral(value, center):
    result = F()
    for (i, j), coefficient in value.items():
        term = coefficient
        for degree, middle in ((i, center[0]), (j, center[1])):
            lo, hi = middle - F(1, 32), middle + F(1, 32)
            term *= (hi ** (degree + 1) - lo ** (degree + 1)) / F(degree + 1)
        result += term
    return rational(result)


def restrict2(value, start, end):
    result = {}
    for (i, j), coefficient in value.items():
        term = {0: coefficient}
        for degree, a, b in ((i, start[0], end[0]), (j, start[1], end[1])):
            require(0 <= a <= b <= 1, "monotone actual two-coordinate segment")
            factor = {
                k: F(comb(degree, k)) * a ** (degree - k) * (b - a) ** k
                for k in range(degree + 1)
            }
            term = multiply(term, poly(factor))
        result = add(result, term)
    return result


def integrate2_path(left, right, points):
    return rational(
        sum(
            (
                pair_integral(restrict2(left, a, b), restrict2(right, a, b))
                for a, b in pairwise(points)
            ),
            F(),
        )
    )


def curvature_enrichment(rows):
    outputs = []
    for synchronized in (False, True):
        source = {n: source2(n, synchronized) for n in numbers(300)}
        curvatures = []
        for row in rows:
            left, right = source[row["n"]], source[row["m"]]
            value = scale2(
                add2(
                    multiply2(derivative2(left, 0), derivative2(right, 1)),
                    scale2(multiply2(derivative2(left, 1), derivative2(right, 0)), -1),
                ),
                2,
            )
            curvatures.append(value)
        powers = sorted(set().union(*(set(value) for value in curvatures)))
        expected = (
            [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0)]
            if synchronized
            else [(0, 0), (0, 1), (1, 0)]
        )
        columns = [[value.get(power, F()) for value in curvatures] for power in powers]
        image = [ratio_image(column, rows) for column in columns]
        ratio_order = sorted(image[0], key=lambda key: F(*key))
        physical = [[column[key] for key in ratio_order] for column in image]
        source_rank = rank_columns(columns)
        require(
            powers == expected and source_rank["rank"] == len(expected),
            "complete literal source curvature prediction",
        )
        witnesses = []
        if synchronized:
            for center in RECTANGLES:
                lo = tuple(x - F(1, 32) for x in center)
                hi = tuple(x + F(1, 32) for x in center)
                mid_w = (lo[0], hi[1])
                mid_u = (hi[0], lo[1])
                prefix = ((F(), F()), (lo[0], F()), lo)
                suffix = (hi, (F(1), hi[1]), (F(1), F(1)))
                path_w = prefix + (mid_w, hi) + suffix[1:]
                path_u = prefix + (mid_u, hi) + suffix[1:]
                direct = []
                for row, value in zip(rows, curvatures, strict=True):
                    left, right = source[row["n"]], source[row["m"]]
                    difference = integrate2_path(left, right, path_w) - integrate2_path(
                        left, right, path_u
                    )
                    require(
                        difference == rectangle_integral(value, center),
                        "actual synchronized path rectangle equals full source curvature",
                    )
                    direct.append(difference)
                witnesses.append(
                    {
                        "center": list(map(str, center)),
                        "path_w_then_u": [list(map(str, p)) for p in path_w],
                        "path_u_then_w": [list(map(str, p)) for p in path_u],
                        "source_difference": list(map(str, direct)),
                    }
                )
            witness_rank = rank_columns(
                [list(map(F, row["source_difference"])) for row in witnesses]
            )
            require(witness_rank["rank"] == 7, "seven actual source path witnesses")
        outputs.append(
            {
                "synchronized": synchronized,
                "curvature_monomials": [list(power) for power in powers],
                "complete_record_columns": [list(map(str, col)) for col in columns],
                "source_rank": source_rank,
                "ratio_order": [list(key) for key in ratio_order],
                "complete_rational_ratio_columns": [
                    list(map(str, col)) for col in physical
                ],
                "physical_rank_measured": rank_columns(physical),
                "actual_rectangle_witnesses": witnesses,
            }
        )
    return outputs


def poly_json(value):
    return [[degree, str(coefficient)] for degree, coefficient in sorted(value.items())]


def discover():
    provenance = authenticate()
    _, p, delta, plus, minus, construction = null_polynomial()
    sufficient = {}
    for name, w in (("plus", plus), ("minus", minus)):
        square = multiply(w, w)
        sufficient[name] = [
            integral(w),
            integral(multiply({1: F(1)}, w)),
            integral(square),
            integral(multiply({1: F(1)}, square)),
        ]
    require(
        sufficient["plus"] == sufficient["minus"],
        "all four sufficient original moments agree",
    )
    rows = records(60)
    vectors = vector_paths(rows, plus, minus)
    require(
        vectors["plus"] == vectors["minus"],
        "all original complete horizon60 source pairs agree",
    )
    differences = [
        a - b for a, b in zip(vectors["sync_plus"], vectors["sync_minus"], strict=True)
    ]
    image = ratio_image(differences, rows)
    target = delta * moments(p)[2] / 4
    require(
        image[3, 5] == target and target != 0,
        "actual weighted ratio3/5 synchronization obstruction",
    )
    support = [(r["n"], r["m"]) for r in rows if (r["a"], r["b"]) == (3, 5)]
    require(support == [(3, 5), (6, 10)], "complete physical-ratio support through60")
    original_image = ratio_image(
        [a - b for a, b in zip(vectors["plus"], vectors["minus"], strict=True)], rows
    )
    require(not any(original_image.values()), "all original observed fields agree")
    large_rows = records(300)
    enrichment = curvature_enrichment(large_rows)
    owned = {}
    for path in (
        HERE / "NATIVE_SYNCHRONIZATION_FIBER_OBSTRUCTION.md",
        HERE / "SYNCHRONIZATION_FIBER_PREREGISTRATION.md",
        Path(__file__),
    ):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "owned byte cap")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.synchronization_fiber_discovery.v1",
        "sources": provenance,
        "owned_sha256_lf": owned,
        "exact_path_construction": construction,
        "w_plus": poly_json(plus),
        "w_minus": poly_json(minus),
        "four_sufficient_original_moments": {
            key: list(map(str, value)) for key, value in sufficient.items()
        },
        "horizon60_complete_records": rows,
        "horizon60_original_and_synchronized_sources": {
            key: list(map(str, value)) for key, value in vectors.items()
        },
        "horizon60_sync_source_difference": list(map(str, differences)),
        "horizon60_sync_ratio_difference": [
            {
                "a": a,
                "b": b,
                "rational_amplitude": str(value),
                "remaining_weight": f"1/sqrt({a * b})",
            }
            for (a, b), value in sorted(image.items(), key=lambda item: F(*item[0]))
        ],
        "ratio3_over5": {
            "complete_pairs": [list(pair) for pair in support],
            "rational_coalesced_difference": str(target),
            "physical_squared_amplitude": str(target * target / 15),
        },
        "horizon300_complete_records": large_rows,
        "curvature_enrichment": enrichment,
        "scope": {
            "allheight_original_equality_proved_by_polynomial_forms": True,
            "bounded_horizon_used_to_infer_allheight_equality": False,
            "synchronization_descends_to_original_source_fibres": False,
            "H25_source_retraction_refuted": False,
            "physical_enrichment_rank_forced": False,
            "full_retained_gamma_decoder_identified": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    output = json.dumps(discover(), sort_keys=True, indent=2, allow_nan=False) + "\n"
    require(len(output.encode()) <= MAX_BYTES, "artifact byte cap")
    print(output, end="")


if __name__ == "__main__":
    main()
