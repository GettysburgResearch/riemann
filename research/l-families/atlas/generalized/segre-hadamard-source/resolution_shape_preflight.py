"""Count frozen D2 domain weights without evaluating or eliminating any map."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from hashlib import sha1, sha256
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = (
    (
        "742d68b6d3c37191589b0e6463bc122af6d90f76",
        PREFIX + "resolution_stage5.cache.json",
        "3f1689a7388de3b4cf3f33e3cc7057d51a94118b",
    ),
    (
        "1a5a63f1148fb884e9ae7aae9e9324a40aee9f33",
        PREFIX + "resolution_replay.py",
        "610f50d0e7ef2a47e361ba61a6b4caf53b0fb543",
    ),
)
MAX_SOURCE = 16 * 1024 * 1024
MAX_OUTPUT = 256 * 1024
COLUMN_CAP = 512


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def no_float(_value):
    raise ValueError("literal integer source required")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate source JSON key")
        result[key] = value
    return result


def frozen(commit, path, blob):
    ref = f"{commit}:{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    need(0 < size <= MAX_SOURCE, "bounded exact source blob")
    raw = subprocess.check_output(["git", "cat-file", "blob", ref], cwd=ROOT)
    need(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen source identity",
    )
    return raw


def source_weights():
    # Authenticate the convention source too, but never compile either source.
    helper = frozen(*PINS[1])
    helper_hash = sha256(helper).hexdigest()
    del helper
    raw = frozen(*PINS[0])
    cache_hash = sha256(raw).hexdigest()
    text = raw.decode("utf-8")
    del raw
    marker = '"D2_columns":'
    need(text.count(marker) == 1, "unique array in exact frozen cache")
    start = text.index(marker) + len(marker)
    while text[start].isspace():
        start += 1
    decoder = json.JSONDecoder(
        parse_float=no_float, parse_constant=no_float, object_pairs_hook=unique_object
    )
    columns, end = decoder.raw_decode(text, start)
    while text[end].isspace():
        end += 1
    need(text[end] == ",", "complete source array delimiter")
    del text
    need(
        type(columns) is list and len(columns) == 85,
        "complete frozen D2 generator coverage",
    )
    weights = []
    for index, column in enumerate(columns):
        degree, weight = column["degree"], column["weight"]
        need(type(degree) is int and degree in (4, 5), "literal frozen D2 degree")
        need(
            type(weight) is list
            and len(weight) == 3
            and all(type(x) is int and 0 <= x <= 15 for x in weight),
            "literal frozen D2 weight",
        )
        need(sum(weight) == 3 * degree, "actual generator weight sum")
        weights.append({"generator": index, "degree": degree, "weight": weight})
    need(
        Counter(row["degree"] for row in weights) == {4: 65, 5: 20},
        "complete actual D2 shift counts",
    )
    return weights, [
        {"commit": commit, "path": path, "blob": blob, "sha256": value}
        for (commit, path, blob), value in zip(
            PINS, (cache_hash, helper_hash), strict=True
        )
    ]


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for value in range(total + 1):
        for remaining in compositions(total - value, length - 1):
            yield (value, *remaining)


def weight_sum(left, right):
    return tuple(a + b for a, b in zip(left, right, strict=True))


def complete_homogeneous(variable_weights):
    tables = [Counter({(0, 0, 0): 1}), Counter(), Counter(), Counter()]
    # Ascending degrees allow arbitrary powers of each variable, each once.
    for weight in variable_weights:
        for degree in range(1, 4):
            for old, count in list(tables[degree - 1].items()):
                tables[degree][weight_sum(old, weight)] += count
    return tables


def shape(weights, variable_weights, grade, tables):
    need(type(grade) is int and grade in (6, 7), "two declared degrees only")
    direct = Counter()
    for generator in weights:
        multiplier_degree = grade - generator["degree"]
        need(1 <= multiplier_degree <= 3, "declared multiplier degree")
        for exponent in compositions(multiplier_degree, 10):
            polynomial_weight = tuple(
                sum(a * w[k] for a, w in zip(exponent, variable_weights, strict=True))
                for k in range(3)
            )
            direct[weight_sum(generator["weight"], polynomial_weight)] += 1
    alternate = Counter()
    for generator in weights:
        for weight, count in tables[grade - generator["degree"]].items():
            alternate[weight_sum(generator["weight"], weight)] += count
    need(
        direct == alternate,
        "independent monomial and homogeneous-product distributions",
    )
    dimension = sum(direct.values())
    predicted = 65 * comb(grade - 4 + 9, 9) + 20 * comb(grade - 5 + 9, 9)
    need(
        dimension == predicted == {6: 3775, 7: 15400}[grade] and dimension <= 16000,
        "complete domain dimension and cap",
    )
    need(
        len(direct) <= 512 and all(sum(weight) == 3 * grade for weight in direct),
        "complete total-weight support",
    )
    maximum = max(direct.values())
    return {
        "grade": grade,
        "domain_dimension": dimension,
        "complete_weight_distribution": [
            {"weight": weight, "columns": count}
            for weight, count in sorted(direct.items())
        ],
        "largest_weight_columns": maximum,
        "all_maximizing_weights": [
            weight for weight, count in sorted(direct.items()) if count == maximum
        ],
        "unchanged_column_cap": COLUMN_CAP,
        "eligible_for_unchanged_column_cap": maximum <= COLUMN_CAP,
        "independent_enumerations_agree": True,
        "kernel_rank_or_nullity_computed": False,
    }


def discover():
    weights, provenance = source_weights()
    variables = tuple(compositions(3, 3))
    need(
        len(variables) == 10 and len(set(variables)) == 10,
        "ten source polynomial-variable weights",
    )
    tables = complete_homogeneous(variables)
    result = {
        "schema": "frozen-D2-domain-weight-shape-only-v1",
        "sources": provenance,
        "complete_frozen_generator_weights": weights,
        "ordered_polynomial_variable_weights": variables,
        "degrees": [shape(weights, variables, grade, tables) for grade in (6, 7)],
        "full_cache_mathematics_reverified": False,
        "evaluated_matrix_constructed": False,
        "any_kernel_or_resolution_certified": False,
        "existing_column_cap_changed": False,
        "executable_source_imported": False,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in (Path(__file__), HERE / "RESOLUTION_SHAPE_PREREGISTRATION.md")
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    raw = canonical(result)
    need(len(raw.encode()) + 1 <= MAX_OUTPUT, "bounded full shape artifact")
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    print(discover())


if __name__ == "__main__":
    main()
