#!/usr/bin/env python3
"""Complete rational curvature vectors and literal monotone rectangle witnesses."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations
from math import comb, gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
GLOBAL = "7ff5ddbb8f35055085faca7d46fdddb0f12715ae"
ACQUISITION = "5d7ea752ee84765a7690bdc36bb2bbcaddb38bb4"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
PINS = (
    (
        GLOBAL,
        PREFIX + "GLOBAL_NATIVE_GEODESIC_VARIATION.md",
        "e90ea1a25e9958c1b34dcf8a4848c04324960221",
    ),
    (
        GLOBAL,
        PREFIX + "global_native_geodesic_certificate.py",
        "41a8488cdc0af20aedec6d8422f24fb1e4e0bd10",
    ),
    (
        GLOBAL,
        PREFIX + "global_native_geodesic_certificate.json",
        "945981157ee44ab25d005724d13451382b59ae98",
    ),
    (
        ACQUISITION,
        PREFIX + "global_geodesic_scout.py",
        "32a4c01750e99a37c4d1992fa6bddafeaea8fe06",
    ),
    (
        ACQUISITION,
        PREFIX + "global_geodesic.discovery.json",
        "86d7301d1fd510d4b0f6d47f3e660d4f81695b2f",
    ),
    (
        ACQUISITION,
        PREFIX + "GLOBAL_GEODESIC_PREREGISTRATION.md",
        "e6206bc344082b1ad1398bfc0ddc793df0d5a993",
    ),
    (
        OLD,
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
        "6810bcece309b0c54ae6c8fc84b314990004549c",
    ),
    (
        OLD,
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
        "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
    ),
)
PRIMES = (2, 3, 5)
HORIZON = 25
ZERO = (0, 0, 0)
MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_OUTPUT_BYTES = 4 * 1024 * 1024
MAX_BITS = 512
MAX_COLUMNS = 12
EXPECTED = {
    (0, 1): (ZERO, (1, 0, 0), (0, 1, 0)),
    (0, 2): (ZERO, (1, 0, 0)),
    (1, 2): (ZERO,),
}
RECTANGLES = (
    ((0, 1), (F(1, 4), F(1, 4))),
    ((0, 1), (F(3, 4), F(1, 4))),
    ((0, 1), (F(1, 4), F(3, 4))),
    ((0, 2), (F(1, 4), F(1, 2))),
    ((0, 2), (F(3, 4), F(1, 2))),
    ((1, 2), (F(1, 2), F(1, 2))),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rational(value):
    require(type(value) in (int, F), "exact rational coefficient required")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= MAX_BITS,
        "rational bit cap",
    )
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate():
    raw, records = {}, []
    for commit, path, blob in PINS:
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_SOURCE_BYTES, "frozen source byte cap")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(data) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "exact source commit/blob authentication",
        )
        raw[path] = data
        records.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": sha256(data).hexdigest(),
            }
        )
    # All proof, discovery and executable bytes are authenticated before import.
    path = PREFIX + "global_geodesic_scout.py"
    namespace = {
        "__name__": "authenticated_curvature_half_source",
        "__file__": str(ROOT / path),
    }
    exec(compile(raw[path], str(ROOT / path), "exec"), namespace)  # noqa: S102
    module = SimpleNamespace(**namespace)
    discovery = json.loads(raw[PREFIX + "global_geodesic.discovery.json"])
    certificate = json.loads(raw[PREFIX + "global_native_geodesic_certificate.json"])
    require(
        discovery["schema"] == "riemann.native_six_hour.global_geodesic_discovery.v1",
        "source discovery schema",
    )
    require(
        certificate["schema"]
        == "riemann.native_six_hour.global_geodesic_certificate.v1",
        "source certificate schema",
    )
    require(
        certificate["source_curvature"]["physical_record_count"] == 63,
        "frozen complete curvature record count",
    )
    return module, discovery, records


def poly(values=None):
    result = {}
    for key, value in (values or {}).items():
        require(
            type(key) is tuple
            and len(key) == 3
            and all(type(x) is int and 0 <= x <= 2 for x in key)
            and sum(key) <= 6,
            "three-variable degree cap",
        )
        value = rational(value)
        if value:
            result[key] = value
    require(len(result) <= 64, "polynomial term cap")
    return result


def add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, F()) + value
    return poly(result)


def scale(value, coefficient):
    coefficient = rational(coefficient)
    return poly({key: coefficient * entry for key, entry in value.items()})


def multiply(left, right):
    result = {}
    for key, a in left.items():
        for other, b in right.items():
            target = tuple(x + y for x, y in zip(key, other, strict=True))
            result[target] = result.get(target, F()) + a * b
    return poly(result)


def derivative(value, coordinate):
    require(type(coordinate) is int and 0 <= coordinate < 3, "source coordinate")
    result = {}
    for key, coefficient in value.items():
        if key[coordinate]:
            target = list(key)
            target[coordinate] -= 1
            result[tuple(target)] = coefficient * key[coordinate]
    return poly(result)


def sqrt_coefficient(degree):
    require(type(degree) is int and 0 <= degree <= 4, "local half-source degree cap")
    value = F(1)
    for k in range(1, degree + 1):
        value *= -(F(1, 2) - k + 1) / k
    return value


def factor_exponents(n):
    require(type(n) is int and 1 <= n <= HORIZON, "physical source index")
    residual, result = n, []
    for p in PRIMES:
        exponent = 0
        while residual % p == 0:
            residual //= p
            exponent += 1
        result.append(exponent)
    require(residual == 1, "declared prime support")
    return tuple(result)


def panel_numbers():
    result = []
    for n in range(1, HORIZON + 1):
        residual = n
        for p in PRIMES:
            while residual % p == 0:
                residual //= p
        if residual == 1:
            result.append(n)
    return tuple(result)


def half_source(n):
    result = poly({ZERO: 1})
    for coordinate, exponent in enumerate(factor_exponents(n)):
        start = sqrt_coefficient(exponent // 2) if exponent % 2 == 0 else F()
        end = sqrt_coefficient(exponent)
        key = tuple(int(i == coordinate) for i in range(3))
        result = multiply(result, poly({ZERO: start, key: end - start}))
    return result


def upoly(values=None):
    result = {}
    for degree, value in (values or {}).items():
        require(type(degree) is int and 0 <= degree <= 8, "edge polynomial degree cap")
        value = rational(value)
        if value:
            result[degree] = value
    return result


def umul(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F()) + a * b
    return upoly(result)


def restrict_segment(value, start, end):
    require(len(start) == len(end) == 3, "three source coordinates")
    start, end = tuple(map(rational, start)), tuple(map(rational, end))
    require(
        all(0 <= a <= b <= 1 for a, b in zip(start, end, strict=True)),
        "monotone source segment",
    )
    result = {}
    for key, coefficient in value.items():
        term = upoly({0: coefficient})
        for degree, a, b in zip(key, start, end, strict=True):
            local = upoly(
                {
                    k: comb(degree, k) * a ** (degree - k) * (b - a) ** k
                    for k in range(degree + 1)
                }
            )
            term = umul(term, local)
        for degree, entry in term.items():
            result[degree] = result.get(degree, F()) + entry
    return upoly(result)


def edge_integral(left, right, start, end):
    # Differentiate the restricted literal source, independently of C_ij.
    a, b = restrict_segment(left, start, end), restrict_segment(right, start, end)
    tangent = upoly(
        {degree - 1: degree * value for degree, value in a.items() if degree}
    )
    return rational(
        sum(
            (2 * value / (degree + 1) for degree, value in umul(tangent, b).items()),
            F(),
        )
    )


def integrate_rectangle(value, pair, lower, upper):
    i, j = pair
    result = F()
    for key, coefficient in value.items():
        term = coefficient
        for k, degree in enumerate(key):
            if k in (i, j):
                term *= (upper[k] ** (degree + 1) - lower[k] ** (degree + 1)) / (
                    degree + 1
                )
            else:
                require(lower[k] == upper[k], "fixed unused rectangle coordinate")
                term *= lower[k] ** degree
        result += term
    return rational(result)


def axis_path(start, end):
    point, edges = list(start), []
    for coordinate in range(3):
        target = point.copy()
        target[coordinate] = end[coordinate]
        if target != point:
            edges.append((tuple(point), tuple(target)))
        point = target
    require(tuple(point) == tuple(end), "path reaches its endpoint")
    return edges


def rank_columns(columns):
    require(
        type(columns) is list and len(columns) <= MAX_COLUMNS, "exact rank column cap"
    )
    rows = len(columns[0]) if columns else 0
    require(
        rows <= 63 and all(len(column) == rows for column in columns),
        "exact rank row cap",
    )
    pivots, selected = {}, []
    for index, column in enumerate(columns):
        vector = {i: rational(value) for i, value in enumerate(column) if value}
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                leading = vector[pivot]
                vector = {i: rational(value / leading) for i, value in vector.items()}
                pivots[pivot] = vector
                selected.append(index)
                break
            leading = vector[pivot]
            for row, value in pivots[pivot].items():
                update = rational(vector.get(row, F()) - leading * value)
                if update:
                    vector[row] = update
                else:
                    vector.pop(row, None)
    return {
        "rank": len(pivots),
        "row_count": rows,
        "column_count": len(columns),
        "independent_columns": selected,
        "pivot_rows": sorted(pivots),
        "normalized_pivot_vectors": [
            {
                "pivot_row": row,
                "coordinates": [[i, str(value)] for i, value in sorted(vector.items())],
            }
            for row, vector in sorted(pivots.items())
        ],
    }


def determinant(matrix):
    require(
        len(matrix) <= MAX_COLUMNS and all(len(row) == len(matrix) for row in matrix),
        "small square determinant",
    )
    matrix = [[rational(value) for value in row] for row in matrix]
    result = F(1)
    for column in range(len(matrix)):
        pivot = next(
            (row for row in range(column, len(matrix)) if matrix[row][column]), None
        )
        if pivot is None:
            return F()
        if pivot != column:
            matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
            result = -result
        leading = matrix[column][column]
        result *= leading
        for row in range(column + 1, len(matrix)):
            factor = matrix[row][column] / leading
            for j in range(column, len(matrix)):
                matrix[row][j] = rational(matrix[row][j] - factor * matrix[column][j])
    return rational(result)


def coefficient_identities(vector, records):
    lookup = {
        (row["n"], row["m"]): value for row, value in zip(records, vector, strict=True)
    }
    products = {}
    for (n, m), value in lookup.items():
        require(value == -lookup[(m, n)], "literal exchange oddness")
        if n == 1 or m == 1:
            require(value == 0, "unit coordinate curvature vanishes")
        products[n * m] = products.get(n * m, F()) + value
    require(
        all(value == 0 for value in products.values()),
        "literal product collapse vanishes",
    )
    return {
        "exchange_odd": True,
        "unit_rows_zero": True,
        "every_product_collapse": {
            str(k): str(value) for k, value in sorted(products.items())
        },
    }


def ratio_image(vector, records, ratios, physical=True):
    require(type(physical) is bool, "literal physical-weight switch")
    result = {ratio: F() for ratio in ratios}
    for row, value in zip(records, vector, strict=True):
        result[(row["reduced_a"], row["reduced_b"])] += (
            value / row["common_factor"] if physical else value
        )
    return [rational(result[ratio]) for ratio in ratios]


def poly_json(value):
    return [
        {"monomial": list(key), "coefficient": str(entry)}
        for key, entry in sorted(value.items())
    ]


def vector_json(vector):
    return [str(value) for value in vector]


def discover():
    module, discovery, provenance = authenticate()
    numbers = panel_numbers()
    require(numbers == module.panel_numbers(), "independent complete source indices")
    source = {n: half_source(n) for n in numbers}
    origin, endpoint = (F(),) * 3, (F(1),) * 3
    for n in numbers:
        actual = restrict_segment(source[n], origin, endpoint)
        frozen = module.source(n, 2)[0]
        expected = {
            degree: value for (epsilon, degree), value in frozen.items() if epsilon == 0
        }
        require(
            actual == expected,
            "independent source equals frozen literal diagonal polynomial",
        )
    records = []
    for n in numbers:
        for m in numbers:
            if n * m <= HORIZON:
                common = gcd(n, m)
                records.append(
                    {
                        "n": n,
                        "m": m,
                        "product": n * m,
                        "common_factor": common,
                        "reduced_a": n // common,
                        "reduced_b": m // common,
                        "rational_observation_weight": str(F(1, common)),
                    }
                )
    require(len(records) == 63, "complete original physical product horizon")
    baseline = next(row for row in discovery["models"] if row["deformed_prime"] == 2)[
        "records"
    ]
    require(len(baseline) == len(records), "frozen record coverage")
    for row, expected in zip(records, baseline, strict=True):
        require(
            (row["n"], row["m"]) == (expected["n"], expected["m"]),
            "frozen physical record order",
        )
        require(
            edge_integral(source[row["n"]], source[row["m"]], origin, endpoint)
            == F(expected["epsilon_coefficients_before_physical_weight"][0]),
            "complete 63-record native normalization",
        )
    ratios = sorted(
        {(row["reduced_a"], row["reduced_b"]) for row in records},
        key=lambda ratio: F(*ratio),
    )
    derivatives = {(n, i): derivative(source[n], i) for n in numbers for i in range(3)}
    curvature, columns, labels, support_records = {}, [], [], []
    for pair in combinations(range(3), 2):
        i, j = pair
        rows = []
        for row in records:
            n, m = row["n"], row["m"]
            rows.append(
                scale(
                    add(
                        multiply(derivatives[n, i], derivatives[m, j]),
                        scale(multiply(derivatives[n, j], derivatives[m, i]), -1),
                    ),
                    2,
                )
            )
        curvature[pair] = rows
        actual_support = set().union(*(set(row) for row in rows))
        preferred = list(EXPECTED[pair])
        ordered = [key for key in preferred if key in actual_support] + sorted(
            actual_support - set(preferred)
        )
        support_records.append(
            {
                "coordinate_pair": [PRIMES[i], PRIMES[j]],
                "predicted_monomials": [list(key) for key in preferred],
                "actual_monomials": [list(key) for key in ordered],
                "prediction_passed": actual_support == set(preferred),
            }
        )
        for monomial in ordered:
            vector = [value.get(monomial, F()) for value in rows]
            coefficient_identities(vector, records)
            columns.append(vector)
            labels.append(
                {"coordinate_pair": [PRIMES[i], PRIMES[j]], "monomial": list(monomial)}
            )
    coefficient_rank = rank_columns(columns)
    observed_columns = [ratio_image(vector, records, ratios) for vector in columns]
    observed_rank = rank_columns(observed_columns)
    indexed = {(row["n"], row["m"]): k for k, row in enumerate(records)}
    require(
        curvature[(0, 1)][indexed[2, 3]] == poly({ZERO: F(1, 2)}),
        "primitive factor-two curvature control",
    )
    require(
        curvature[(0, 1)][indexed[4, 6]] == poly({(1, 0, 0): F(3, 16)}),
        "prime-power half-source curvature control",
    )
    u2_index = labels.index({"coordinate_pair": [2, 3], "monomial": [1, 0, 0]})
    ratio_index = ratios.index((2, 3))
    require(
        observed_columns[u2_index][ratio_index] == F(3, 32),
        "actual common-factor observation weight",
    )
    unweighted = ratio_image(columns[u2_index], records, ratios, physical=False)
    require(
        unweighted[ratio_index] == F(3, 16), "omitted common-factor weight counterfeit"
    )
    rectangles, rectangle_columns, transition_columns = [], [], []
    for pair, center in RECTANGLES:
        i, j = pair
        lower = [F(1, 2)] * 3
        upper = lower.copy()
        for k, middle in zip(pair, center, strict=True):
            lower[k], upper[k] = middle - F(1, 16), middle + F(1, 16)
        lower, upper = tuple(lower), tuple(upper)
        after_j, after_i = list(lower), list(lower)
        after_j[j], after_i[i] = upper[j], upper[i]
        after_j, after_i = tuple(after_j), tuple(after_i)
        edges = ((lower, after_j), (after_j, upper), (lower, after_i), (after_i, upper))
        prefix, suffix = axis_path(origin, lower), axis_path(upper, endpoint)
        vector, edge_records = [], []
        for index, row in enumerate(records):
            left, right = source[row["n"]], source[row["m"]]
            edge_values = [
                edge_integral(left, right, start, end) for start, end in edges
            ]
            path_difference = (
                edge_values[0] + edge_values[1] - edge_values[2] - edge_values[3]
            )
            surface = integrate_rectangle(curvature[pair][index], pair, lower, upper)
            require(
                surface == path_difference,
                "native four-edge integral equals the complete curvature rectangle",
            )
            common_prefix = sum(
                (edge_integral(left, right, start, end) for start, end in prefix), F()
            )
            common_suffix = sum(
                (edge_integral(left, right, start, end) for start, end in suffix), F()
            )
            full_ji = common_prefix + edge_values[0] + edge_values[1] + common_suffix
            full_ij = common_prefix + edge_values[2] + edge_values[3] + common_suffix
            require(
                full_ji - full_ij == surface,
                "common monotone prefix and suffix cancel exactly",
            )
            vector.append(surface)
            edge_records.append(
                {
                    "n": row["n"],
                    "m": row["m"],
                    "four_monotone_edge_integrals": vector_json(edge_values),
                    "common_prefix_integral": str(common_prefix),
                    "common_suffix_integral": str(common_suffix),
                    "full_j_then_i": str(full_ji),
                    "full_i_then_j": str(full_ij),
                    "surface_integral": str(surface),
                }
            )
        require(any(vector), "declared nonzero rectangle witness")
        coefficient_identities(vector, records)
        transition = []
        for label in labels:
            matching_pair = label["coordinate_pair"] == [PRIMES[i], PRIMES[j]]
            transition.append(
                integrate_rectangle(
                    poly({tuple(label["monomial"]): 1}), pair, lower, upper
                )
                if matching_pair
                else F()
            )
        reconstructed = [
            sum(
                (
                    weight * column[row]
                    for weight, column in zip(transition, columns, strict=True)
                ),
                F(),
            )
            for row in range(len(records))
        ]
        require(reconstructed == vector, "actual coefficient-to-rectangle transition")
        rectangle_columns.append(vector)
        transition_columns.append(transition)
        rectangles.append(
            {
                "coordinate_pair": [PRIMES[i], PRIMES[j]],
                "center": vector_json(center),
                "half_width": "1/16",
                "lower_corner": vector_json(lower),
                "upper_corner": vector_json(upper),
                "edge_endpoints": [
                    [vector_json(start), vector_json(end)] for start, end in edges
                ],
                "original_record_integrals": edge_records,
                "complete_source_vector": vector_json(vector),
                "ratio_image": vector_json(ratio_image(vector, records, ratios)),
                "coefficient_transition_column": vector_json(transition),
                "reversed_edge_difference_is_wrong": True,
            }
        )
    rectangle_rank = rank_columns(rectangle_columns)
    rectangle_observed_rank = rank_columns(
        [ratio_image(vector, records, ratios) for vector in rectangle_columns]
    )
    transition_det = (
        determinant([list(row) for row in zip(*transition_columns, strict=True)])
        if len(columns) == len(rectangle_columns)
        else None
    )
    expected_det = F(1, 8 * 64**6)
    own = (HERE / "NATIVE_CURVATURE_SPAN_PREREGISTRATION.md", Path(__file__))
    result = {
        "schema": "riemann.native_six_hour.curvature_span_discovery.v1",
        "sources": provenance,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in own
        },
        "primes": list(PRIMES),
        "physical_product_horizon": HORIZON,
        "complete_half_source": [
            {"n": n, "polynomial": poly_json(source[n])} for n in numbers
        ],
        "complete_ordered_records": records,
        "ratio_order": [
            {"a": a, "b": b, "factored_physical_weight": f"1/sqrt({a * b})"}
            for a, b in ratios
        ],
        "coefficient_supports": support_records,
        "coefficient_columns": [
            {
                **label,
                "complete_source_vector": vector_json(column),
                "rational_ratio_image": vector_json(observed),
                "identities": coefficient_identities(column, records),
            }
            for label, column, observed in zip(
                labels, columns, observed_columns, strict=True
            )
        ],
        "coefficient_rank": coefficient_rank,
        "rationalized_observation_rank": observed_rank,
        "independent_complete_basis": [
            vector_json(columns[index])
            for index in coefficient_rank["independent_columns"]
        ],
        "common_factor_control": {
            "pair_2_3_constant": "1/2",
            "pair_4_6_u2": "3/16",
            "ratio_2_over_3_u2": str(observed_columns[u2_index][ratio_index]),
            "wrong_unweighted_ratio_value": str(unweighted[ratio_index]),
        },
        "rectangles": rectangles,
        "rectangle_rank": rectangle_rank,
        "rectangle_observation_rank": rectangle_observed_rank,
        "rectangle_transition_determinant": str(transition_det)
        if transition_det is not None
        else None,
        "predictions": {
            "all_declared_coefficient_supports": all(
                row["prediction_passed"] for row in support_records
            ),
            "source_rank_six": coefficient_rank["rank"] == 6,
            "observed_rank_six": observed_rank["rank"] == 6,
            "rectangle_rank_six": rectangle_rank["rank"] == 6,
            "rectangle_observed_rank_six": rectangle_observed_rank["rank"] == 6,
            "transition_determinant": transition_det == expected_det,
        },
        "scope": {
            "all_63_original_pairs_retained": True,
            "original_inverse_square_root_weights_in_ratio_map": True,
            "arbitrary_coefficient_observation_substituted": False,
            "monotone_global_path_differences_realized": True,
            "full_post_renewal_gamma_identified": False,
            "all_path_holonomy_classified_by_finite_scout": False,
            "T106140_diagonal_identified": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    result = discover()
    output = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    require(len(output.encode()) <= MAX_OUTPUT_BYTES, "discovery output byte cap")
    print(output, end="")


if __name__ == "__main__":
    main()
