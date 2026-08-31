"""Literal grouped native source, curvature ranks and monotone path witnesses."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations, pairwise
from math import comb, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PRIMES = (2, 3, 5, 7)
GROUPINGS = (((2, 3, 5), (7,)), ((2, 3), (5, 7)))
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
MAX_BYTES = 8 * 1024 * 1024


def need(condition, message):
    if not condition:
        raise ValueError(message)


def exact(value):
    need(type(value) in (int, F), "literal exact rational")
    value = F(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 4096,
        "rational bit cap",
    )
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate():
    provenance = []
    for commit, path, expected in PINS:
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        need(0 < size <= MAX_BYTES, "source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        blob = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
        need(len(raw) == size and blob == expected, "exact source authentication")
        provenance.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": sha256(raw).hexdigest(),
            }
        )
    return provenance


def poly2(values=None):
    result = {}
    for power, value in (values or {}).items():
        need(
            type(power) is tuple
            and len(power) == 2
            and all(type(entry) is int for entry in power)
            and 0 <= power[0] <= 6
            and 0 <= power[1] <= 4,
            "source bidegree cap",
        )
        value = exact(value)
        if value:
            result[power] = value
    return result


def add2(left, right):
    result = dict(left)
    for power, value in right.items():
        result[power] = result.get(power, F()) + value
    return poly2(result)


def scale2(value, scalar):
    scalar = exact(scalar)
    return poly2({power: scalar * coefficient for power, coefficient in value.items()})


def multiply2(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            power = i + k, j + ell
            result[power] = result.get(power, F()) + a * b
    return poly2(result)


def derivative2(value, coordinate):
    need(
        type(coordinate) is int and coordinate in (0, 1),
        "literal derivative coordinate",
    )
    result = {}
    for power, coefficient in value.items():
        if power[coordinate]:
            target = list(power)
            target[coordinate] -= 1
            result[tuple(target)] = power[coordinate] * coefficient
    return poly2(result)


def half_coefficient(degree):
    need(type(degree) is int and 0 <= degree <= 1, "squarefree local source only")
    value = F(1)
    for k in range(1, degree + 1):
        value *= -(F(1, 2) - k + 1) / k
    return exact(value)


def squarefree_indices():
    return sorted(
        prod(subset) for count in range(5) for subset in combinations(PRIMES, count)
    )


def source_polynomial(n, groups):
    need(
        type(n) is int and n in squarefree_indices(), "declared squarefree source index"
    )
    need(groups in GROUPINGS, "preregistered prime grouping")
    value = {(0, 0): F(1)}
    residual = n
    for coordinate, group in enumerate(groups):
        for prime in group:
            degree = int(residual % prime == 0)
            if degree:
                residual //= prime
            start = half_coefficient(degree // 2) if degree % 2 == 0 else F()
            slope = half_coefficient(degree) - start
            power = (1, 0) if coordinate == 0 else (0, 1)
            factor = add2({(0, 0): start}, {power: slope})
            value = multiply2(value, factor)
    need(residual == 1, "complete literal prime factorization")
    return value


def curvature(left, right):
    positive = multiply2(derivative2(left, 0), derivative2(right, 1))
    negative = multiply2(derivative2(left, 1), derivative2(right, 0))
    return scale2(add2(positive, scale2(negative, -1)), 2)


def rank_columns(columns):
    need(type(columns) is list and 1 <= len(columns) <= 15, "registered column cap")
    size = len(columns[0])
    need(
        1 <= size <= 256 and all(len(column) == size for column in columns),
        "registered row cap",
    )
    pivots = {}
    selected = []
    for index, column in enumerate(columns):
        vector = {row: exact(value) for row, value in enumerate(column) if value}
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                leading = vector[pivot]
                pivots[pivot] = {
                    row: exact(value / leading) for row, value in vector.items()
                }
                selected.append(index)
                break
            leading = vector[pivot]
            for row, value in pivots[pivot].items():
                entry = exact(vector.get(row, F()) - leading * value)
                if entry:
                    vector[row] = entry
                else:
                    vector.pop(row, None)
    return {
        "rank": len(pivots),
        "selected_columns": selected,
        "pivot_rows": list(pivots),
        "complete_matrix_sha256": sha256(
            canonical([list(map(str, column)) for column in columns]).encode()
        ).hexdigest(),
    }


def poly1(values=None):
    result = {}
    for degree, value in (values or {}).items():
        need(type(degree) is int and 0 <= degree <= 8, "path degree cap")
        value = exact(value)
        if value:
            result[degree] = value
    return result


def add1(left, right):
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, F()) + value
    return poly1(result)


def multiply1(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F()) + a * b
    return poly1(result)


def derivative1(value):
    return poly1(
        {
            degree - 1: degree * coefficient
            for degree, coefficient in value.items()
            if degree
        }
    )


def integrate1(value):
    return exact(
        sum((coefficient / (degree + 1) for degree, coefficient in value.items()), F())
    )


def restrict(value, start, end):
    need(len(start) == len(end) == 2, "two path coordinates")
    result = {}
    for (i, j), coefficient in value.items():
        term = {0: coefficient}
        for degree, a, b in ((i, start[0], end[0]), (j, start[1], end[1])):
            a, b = exact(a), exact(b)
            need(0 <= a <= b <= 1, "actual monotone source segment")
            factor = {
                k: F(comb(degree, k)) * a ** (degree - k) * (b - a) ** k
                for k in range(degree + 1)
            }
            term = multiply1(term, factor)
        result = add1(result, term)
    return result


def path_vector(source, rows, points):
    need(
        points[0] == (F(), F()) and points[-1] == (F(1), F(1)),
        "actual source endpoints",
    )
    result = [F()] * len(rows)
    for start, end in pairwise(points):
        local = {n: restrict(value, start, end) for n, value in source.items()}
        differentials = {n: derivative1(value) for n, value in local.items()}
        for index, (n, m) in enumerate(rows):
            contribution = 2 * integrate1(multiply1(differentials[n], local[m]))
            result[index] = exact(result[index] + contribution)
    return result


def rectangle_integral(value, center, halfwidth):
    result = F()
    for (i, j), coefficient in value.items():
        term = coefficient
        for degree, middle in ((i, center[0]), (j, center[1])):
            low, high = middle - halfwidth, middle + halfwidth
            need(0 < low < high < 1, "interior registered rectangle")
            term *= (high ** (degree + 1) - low ** (degree + 1)) / (degree + 1)
        result += term
    return exact(result)


def polynomial_json(value):
    return [
        {"powers": list(power), "coefficient": str(coefficient)}
        for power, coefficient in sorted(value.items())
    ]


def panel(groups):
    p, q = map(len, groups)
    indices = squarefree_indices()
    need(len(indices) == 16 and indices[-1] == 210, "complete squarefree basis panel")
    rows = [(n, m) for n in indices for m in indices]
    source = {n: source_polynomial(n, groups) for n in indices}
    source_powers = sorted(set().union(*(set(value) for value in source.values())))
    source_columns = [
        [source[n].get(power, F()) for n in indices] for power in source_powers
    ]
    source_rank = rank_columns(source_columns)
    need(
        source_rank["rank"] == (p + 1) * (q + 1),
        "actual full polynomial source rectangle",
    )
    values = [curvature(source[n], source[m]) for n, m in rows]
    powers = sorted(set().union(*(set(value) for value in values)))
    top = (2 * p - 1, 2 * q - 1)
    expected = [(r, s) for r in range(2 * p) for s in range(2 * q) if (r, s) != top]
    columns = [[value.get(power, F()) for value in values] for power in powers]
    computed_rank = rank_columns(columns)
    need(
        powers == expected and computed_rank["rank"] == 4 * p * q - 1,
        "registered literal curvature prediction",
    )
    need(
        all(value.get(top, F()) == 0 for value in values),
        "top-corner independence counterfeit rejected",
    )
    need(
        all(
            not value
            for (n, m), value in zip(rows, values, strict=True)
            if n == m or n == 1 or m == 1
        ),
        "unit and diagonal curvature vanish",
    )
    by_pair = dict(zip(rows, values, strict=True))
    need(
        all(value == scale2(by_pair[m, n], -1) for (n, m), value in by_pair.items()),
        "ordered source exchange antisymmetry",
    )

    halfwidth = F(1, 8 * (2 * p + 1) * (2 * q + 1))
    centers = [
        (F(a, 2 * p + 1), F(b, 2 * q + 1))
        for a in range(1, 2 * p + 1)
        for b in range(1, 2 * q + 1)
        if (a, b) != (2 * p, 2 * q)
    ]
    witnesses = []
    for center in centers:
        low = tuple(x - halfwidth for x in center)
        high = tuple(x + halfwidth for x in center)
        prefix = ((F(), F()), (low[0], F()), low)
        suffix = (high, (F(1), high[1]), (F(1), F(1)))
        path_w = prefix + ((low[0], high[1]), high) + suffix[1:]
        path_u = prefix + ((high[0], low[1]), high) + suffix[1:]
        vector_w = path_vector(source, rows, path_w)
        vector_u = path_vector(source, rows, path_u)
        difference = [exact(a - b) for a, b in zip(vector_w, vector_u, strict=True)]
        areas = [rectangle_integral(value, center, halfwidth) for value in values]
        need(
            difference == areas and any(difference),
            "complete literal path integral equals curvature area",
        )
        need(
            [-entry for entry in difference] != areas,
            "reversed path orientation counterfeit rejected",
        )
        witnesses.append(
            {
                "center": list(map(str, center)),
                "halfwidth": str(halfwidth),
                "path_w_then_u": [list(map(str, point)) for point in path_w],
                "path_u_then_w": [list(map(str, point)) for point in path_u],
                "complete_w_path_source": list(map(str, vector_w)),
                "complete_u_path_source": list(map(str, vector_u)),
                "complete_source_difference": list(map(str, difference)),
                "complete_curvature_rectangle_integral": list(map(str, areas)),
                "reversed_orientation_rejected": True,
            }
        )
    witness_rank = rank_columns(
        [list(map(F, row["complete_source_difference"])) for row in witnesses]
    )
    need(witness_rank["rank"] == 4 * p * q - 1, "actual monotone source variation rank")
    return {
        "group_u": list(groups[0]),
        "group_w": list(groups[1]),
        "p": p,
        "q": q,
        "K": 210,
        "safe_product_horizon": 44100,
        "squarefree_indices": indices,
        "complete_ordered_basis_pairs": [list(row) for row in rows],
        "complete_source_functions": [
            {"n": n, "polynomial": polynomial_json(source[n])} for n in indices
        ],
        "source_monomials": [list(power) for power in source_powers],
        "source_rank": source_rank,
        "complete_pair_curvatures": [polynomial_json(value) for value in values],
        "curvature_monomials": [list(power) for power in powers],
        "complete_curvature_columns": [list(map(str, column)) for column in columns],
        "curvature_rank": computed_rank,
        "excluded_top_corner": list(top),
        "naive_full_rectangle_rank_rejected": 4 * p * q,
        "all_unit_diagonal_and_exchange_checks": True,
        "all_actual_rectangle_witnesses": witnesses,
        "actual_witness_rank": witness_rank,
        "complete_physical_horizon_census": False,
        "single_cutoff_physical_rank_claimed": False,
    }


def discover():
    sources = authenticate()
    panels = [panel(groups) for groups in GROUPINGS]
    owned = {}
    for path in (
        HERE / "GROUPED_NATIVE_CURVATURE_ENRICHMENT.md",
        HERE / "GROUPED_CURVATURE_PREREGISTRATION.md",
        Path(__file__),
    ):
        raw = path.read_bytes()
        need(len(raw) <= MAX_BYTES, "owned source byte cap")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.grouped_curvature_discovery.v1",
        "sources": sources,
        "owned_sha256_lf": owned,
        "panels": panels,
        "scope": {
            "actual_squarefree_source_basis_not_generic_monomial_fit": True,
            "allheight_source_theorem_proved_separately": True,
            "physical_prefix_reconstruction_is_proof_only": True,
            "arbitrary_moment_tuple_attainment_claimed": False,
            "single_cutoff_physical_rank_claimed": False,
            "full_retained_gamma_decoder_identified": False,
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "discovery artifact byte cap")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    output = json.dumps(discover(), sort_keys=True, indent=2, allow_nan=False) + "\n"
    need(len(output.encode()) <= MAX_BYTES, "formatted artifact byte cap")
    print(output, end="")


if __name__ == "__main__":
    main()
