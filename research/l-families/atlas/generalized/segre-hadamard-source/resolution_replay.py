"""Actual higher Chow-module differential scout, using the frozen D1 matrix.

Current execution scope is degree four only. All kernels retain exact
original-coordinate witnesses; no Betti-fitted differential is constructed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "4c635b2ee8d7cf6caa41efde2d2e0c7baea1b787"
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = {
    "TERNARY_CUBE_PRESENTATION.md": "ff8bcf95ef425ac976718d8037cedc6a5374ee4e",
    "presentation_replay.py": "cf6bf60d04301c71881fe312511ec3c43bd9402a",
    "presentation.verification.json": "06eec475eac92726ede0a6c342b81904eae7bf99",
}
MAX_BLOCK = 512
MAX_BITS = 4096
MAX_BYTES = 32 * 1024 * 1024
MAX_ROWS = 90000
MAX_COLUMNS = 16000


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label="integer"):
    need(type(value) is int and low <= value <= high, f"{label} outside declared cap")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate():
    blobs = {}
    for name, expected in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen D1 source object mismatch")
        raw = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(raw) <= MAX_BYTES, "frozen D1 source byte cap")
        current = (HERE / name).read_bytes().replace(b"\r\n", b"\n")
        need(current == raw.replace(b"\r\n", b"\n"), "working D1 source changed")
        blobs[name] = raw
    payload = json.loads(blobs["presentation.verification.json"])
    need(payload["summary"]["D1_columns"] == 85, "full frozen D1 required")
    return payload


@lru_cache(maxsize=128)
def _compositions(n, length):
    if length == 1:
        return ((n,),)
    return tuple(
        (a, *tail) for a in range(n + 1) for tail in _compositions(n - a, length - 1)
    )


def compositions(n, length):
    integer(n, 0, 7, "composition degree")
    integer(length, 1, 10, "composition length")
    return _compositions(n, length)


def exponent(value, length=10):
    need(type(value) in (list, tuple) and len(value) == length, "exponent arity")
    for a in value:
        integer(a, 0, 21, "exponent")
    return tuple(value)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def polynomial_weight(exp):
    exp = exponent(exp)
    return tuple(
        sum(a * content[k] for a, content in zip(exp, compositions(3, 3), strict=True))
        for k in range(3)
    )


def validate_modules(generators, columns):
    need(
        type(generators) is list and len(generators) == 29,
        "actual F0 generator coverage",
    )
    need(type(columns) is list and len(columns) == 85, "actual D1 column coverage")
    need(Counter(g["degree"] for g in generators) == {0: 1, 1: 17, 2: 11}, "F0 shifts")
    need(Counter(c["degree"] for c in columns) == {2: 20, 3: 65}, "F1 shifts")
    for g in generators:
        integer(g["degree"], 0, 2, "F0 degree")
        need(sum(exponent(g["weight"], 3)) == 3 * g["degree"], "F0 total weight")
    for column in columns:
        integer(column["degree"], 2, 3, "D1 degree")
        weight = exponent(column["weight"], 3)
        need(sum(weight) == 3 * column["degree"], "D1 total weight")
        need(type(column["terms"]) is list and column["terms"], "nonzero D1 column")
        seen = set()
        for term in column["terms"]:
            target = integer(term["generator"], 0, 28, "D1 target")
            exp = exponent(term["S_exponent"])
            coefficient = term["coefficient"]
            need(
                type(coefficient) is int and coefficient != 0,
                "literal D1 integer entry",
            )
            need((target, exp) not in seen, "duplicate D1 polynomial monomial")
            seen.add((target, exp))
            need(
                sum(exp) > 0
                and sum(exp) + generators[target]["degree"] == column["degree"],
                "D1 minimal positive degree",
            )
            need(
                add(polynomial_weight(exp), generators[target]["weight"]) == weight,
                "D1 weight homogeneity",
            )


def module_basis(generators, grade):
    integer(grade, 0, 7, "module grade")
    basis = tuple(
        (j, exp)
        for j, generator in enumerate(generators)
        if generator["degree"] <= grade
        for exp in compositions(grade - generator["degree"], 10)
    )
    need(len(basis) <= MAX_ROWS, "free-module basis cap")
    return basis


def evaluated_map(target_generators, columns, grade):
    target = module_basis(target_generators, grade)
    domain = module_basis(columns, grade)
    need(len(domain) <= MAX_COLUMNS, "differential column cap")
    target_index = {entry: j for j, entry in enumerate(target)}
    matrix, weights = [], []
    for column_id, multiplier in domain:
        column = columns[column_id]
        weight = add(column["weight"], polynomial_weight(multiplier))
        vector = {}
        for term in column["terms"]:
            target_id = term["generator"]
            exp = add(multiplier, term["S_exponent"])
            need(
                add(target_generators[target_id]["weight"], polynomial_weight(exp))
                == weight,
                "multiplied differential weight",
            )
            index = target_index[(target_id, exp)]
            vector[index] = vector.get(index, 0) + term["coefficient"]
        matrix.append({i: a for i, a in vector.items() if a})
        weights.append(weight)
    return {
        "grade": grade,
        "target_basis": target,
        "domain_basis": domain,
        "columns": matrix,
        "weights": weights,
    }


def subtract_multiple(vector, pivot, scalar):
    for key, value in pivot.items():
        result = vector.get(key, 0) - scalar * value
        if result:
            vector[key] = result
        else:
            vector.pop(key, None)


def check_bits(vector):
    bits = max(
        (
            max(
                abs(Fraction(a).numerator).bit_length(),
                Fraction(a).denominator.bit_length(),
            )
            for a in vector.values()
        ),
        default=0,
    )
    need(bits <= MAX_BITS, "rational elimination bit cap")
    return bits


def primitive_integer(vector):
    need(bool(vector), "nonzero kernel witness")
    denominator = lcm(*(Fraction(a).denominator for a in vector.values()))
    result = {i: int(Fraction(a) * denominator) for i, a in vector.items()}
    divisor = gcd(*result.values())
    if result[max(result)] < 0:
        divisor = -divisor
    result = {i: a // divisor for i, a in result.items()}
    check_bits(result)
    return result


def image_of_relation(matrix, relation):
    out = Counter()
    for column, scalar in relation.items():
        for row, value in matrix[column].items():
            out[row] += scalar * value
    return {row: value for row, value in out.items() if value}


def exact_kernel(evaluation):
    blocks = defaultdict(list)
    for index, weight in enumerate(evaluation["weights"]):
        blocks[weight].append(index)
    relations, weights, stats = [], [], []
    for weight, indices in sorted(blocks.items()):
        support = set().union(*(evaluation["columns"][j] for j in indices))
        need(max(len(indices), len(support)) <= MAX_BLOCK, "weight-block dimension cap")
        pivots, local = {}, []
        max_bits = 0
        for column in indices:
            vector = {i: Fraction(a) for i, a in evaluation["columns"][column].items()}
            witness = {column: Fraction(1)}
            while vector:
                leading = min(vector)
                if leading in pivots:
                    image, old_witness = pivots[leading]
                    scalar = vector[leading]
                    subtract_multiple(vector, image, scalar)
                    subtract_multiple(witness, old_witness, scalar)
                else:
                    scalar = vector[leading]
                    image = {i: a / scalar for i, a in vector.items()}
                    witness = {i: a / scalar for i, a in witness.items()}
                    max_bits = max(max_bits, check_bits(image), check_bits(witness))
                    pivots[leading] = (image, witness)
                    break
            if not vector:
                relation = primitive_integer(witness)
                need(
                    not image_of_relation(evaluation["columns"], relation),
                    "actual differential composition is nonzero",
                )
                local.append(relation)
        need(len(indices) == len(pivots) + len(local), "exact rank-nullity")
        relations.extend(local)
        weights.extend([weight] * len(local))
        stats.append(
            {
                "weight": weight,
                "rows": len(support),
                "columns": len(indices),
                "rank": len(pivots),
                "nullity": len(local),
                "max_exact_bits": max_bits,
            }
        )
    return relations, weights, stats


def differential_columns(evaluation, relations, weights):
    result = []
    for relation, weight in zip(relations, weights, strict=True):
        terms = []
        for coordinate, coefficient in sorted(relation.items()):
            generator, exp = evaluation["domain_basis"][coordinate]
            need(sum(exp) > 0, "new differential has a nonminimal constant entry")
            terms.append(
                {"generator": generator, "S_exponent": exp, "coefficient": coefficient}
            )
        result.append({"degree": evaluation["grade"], "weight": weight, "terms": terms})
    return result


def grade_four_scout():
    payload = authenticate()
    source = payload["result"]
    generators, d1 = source["generators"], source["D1_columns"]
    validate_modules(generators, d1)
    need(
        tuple(tuple(x) for x in source["literal_W_contents"]) == compositions(3, 3),
        "literal W coordinate order",
    )
    evaluation = evaluated_map(generators, d1, 4)
    relations, weights, stats = exact_kernel(evaluation)
    actual = Counter(weights)
    expected = Counter(
        tuple(7 - a for a in column["weight"]) for column in d1 if column["degree"] == 3
    )
    need(actual == expected, "actual degree-four kernel versus full dual Tor weights")
    d2 = differential_columns(evaluation, relations, weights)
    rank = sum(block["rank"] for block in stats)
    need(
        (
            len(evaluation["target_basis"]),
            len(evaluation["domain_basis"]),
            rank,
            len(d2),
        )
        == (5060, 1750, 1685, 65),
        "degree-four higher-differential prediction",
    )
    return {
        "source_freeze": FREEZE,
        "source_blobs": PINS,
        "internal_degree": 4,
        "full_target_rows": len(evaluation["target_basis"]),
        "domain_columns": len(evaluation["domain_basis"]),
        "rank": rank,
        "kernel_dimension": len(d2),
        "largest_block_rows": max(block["rows"] for block in stats),
        "largest_block_columns": max(block["columns"] for block in stats),
        "max_exact_bits": max(block["max_exact_bits"] for block in stats),
        "weight_blocks": stats,
        "all_D1_D2_compositions_zero": True,
        "complete_dual_Tor_weight_match": True,
        "D2_degree_four_columns_sha256": hashlib.sha256(
            canonical(d2).encode()
        ).hexdigest(),
        "higher_stages_run": False,
        "fixture_written": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scout", action="store_true", required=True)
    parser.parse_args()
    print(json.dumps(grade_four_scout(), sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
