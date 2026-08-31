"""Actual marked Chow-module generators and first differential, over Q.

All elimination is weight-blocked and retains exact relation witnesses.
The parent runs scouts and validation; no executable predecessor is imported.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "a895f47628b0bc7c7ee5e0392df2f79c24166f92"
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = (
    ("MATHEMATICS.md", "bbd847461b4955a93b4533fa687cdd8724e2347c"),
    ("replay.py", "795566f6ec91bf68dd7ee2f77450e73afd131032"),
    ("verification.json", "310ffc95cb6eaf19281de52dd18d2f2884bc0f49"),
)
OWNED = (
    "TERNARY_CUBE_PRESENTATION_PREREGISTRATION.md",
    "TERNARY_CUBE_PRESENTATION.md",
    "PRESENTATION_REPLAY.md",
    "presentation_replay.py",
)
TEST = ROOT / "tests/test_segre_hadamard_presentation.py"
FIXTURE = HERE / "presentation.verification.json"
MAX_BLOCK = 512
MAX_BITS = 4096
MAX_BYTES = 16 * 1024 * 1024
ZERO_S = (0,) * 10
ZERO_R = (0,) * 9


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label="integer"):
    need(type(value) is int and low <= value <= high, f"{label} outside declared cap")
    return value


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def canonical_bytes(path):
    return path.read_bytes().replace(b"\r\n", b"\n")


def blob_id(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def authenticate_source():
    for name, expected in PINS:
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen Git source object mismatch")
        need(
            blob_id(canonical_bytes(HERE / name)) == expected,
            "working source bytes mismatch",
        )
    return json.loads((HERE / "verification.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=64)
def _compositions(n, length):
    if length == 1:
        return ((n,),)
    return tuple(
        (a, *b) for a in range(n + 1) for b in _compositions(n - a, length - 1)
    )


def compositions(n, length):
    integer(n, 0, 3, "composition degree")
    integer(length, 1, 10, "composition length")
    return _compositions(n, length)


def exponents(value, length, maximum, label):
    need(isinstance(value, (tuple, list)) and len(value) == length, f"{label} arity")
    for a in value:
        integer(a, 0, maximum, label)
    return tuple(value)


def source_weight(value):
    value = exponents(value, 9, 3, "source exponent")
    need(sum(value[:3]) == sum(value[3:6]) == sum(value[6:]), "unequal tensor degrees")
    return tuple(sum(value[j::3]) for j in range(3))


@lru_cache(maxsize=4)
def _source_basis(grade):
    return tuple(
        tuple(a for row in rows for a in row)
        for rows in itertools.product(compositions(grade, 3), repeat=3)
    )


def source_basis(grade):
    integer(grade, 0, 3, "source grade")
    result = _source_basis(grade)
    need(len(result) <= 1000, "source row cap")
    return result


def w_contents():
    return compositions(3, 3)


@lru_cache(maxsize=1)
def w_images():
    result = []
    for content in w_contents():
        terms = []
        for word in itertools.product(range(3), repeat=3):
            if tuple(word.count(j) for j in range(3)) == content:
                exponent = tuple(
                    int(word[row] == col) for row in range(3) for col in range(3)
                )
                terms.append((exponent, 1))
        need(
            terms and all(source_weight(a) == content for a, _ in terms),
            "literal W image",
        )
        result.append(tuple(sorted(terms)))
    return tuple(result)


def polynomial_product(left, right):
    result = Counter()
    for a, x in left:
        for b, y in right:
            result[tuple(u + v for u, v in zip(a, b, strict=True))] += x * y
    return tuple(sorted((a, x) for a, x in result.items() if x))


@lru_cache(maxsize=286)
def _s_image(exponent):
    if not any(exponent):
        return ((ZERO_R, 1),)
    j = next(j for j, a in enumerate(exponent) if a)
    previous = list(exponent)
    previous[j] -= 1
    return polynomial_product(_s_image(tuple(previous)), w_images()[j])


def s_image(exponent):
    exponent = exponents(exponent, 10, 3, "polynomial exponent")
    need(sum(exponent) <= 3, "polynomial total-degree cap")
    return _s_image(exponent)


def polynomial_weight(exponent):
    exponent = exponents(exponent, 10, 3, "polynomial exponent")
    need(sum(exponent) <= 3, "polynomial total-degree cap")
    return tuple(
        sum(a * content[k] for a, content in zip(exponent, w_contents(), strict=True))
        for k in range(3)
    )


def add_weights(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def subtract_multiple(vector, pivot, factor):
    for key, value in pivot.items():
        new = vector.get(key, 0) - factor * value
        if new:
            vector[key] = new
        else:
            vector.pop(key, None)


def check_bits(vector):
    bits = max(
        (
            max(
                Fraction(x).numerator.bit_length(), Fraction(x).denominator.bit_length()
            )
            for x in vector.values()
        ),
        default=0,
    )
    need(bits <= MAX_BITS, "exact arithmetic bit cap")
    return bits


def primitive_integer(vector):
    need(bool(vector), "nonzero relation required")
    denominator = lcm(*(Fraction(a).denominator for a in vector.values()))
    result = {j: int(Fraction(a) * denominator) for j, a in vector.items()}
    divisor = gcd(*result.values())
    if result[max(result)] < 0:
        divisor = -divisor
    result = {j: a // divisor for j, a in result.items()}
    check_bits(result)
    return result


class Span:
    """Sparse deterministic echelon basis, with no rank inference from counts."""

    def __init__(self):
        self.pivots = {}
        self.max_bits = 0

    def add(self, raw):
        vector = {j: Fraction(a) for j, a in raw.items() if a}
        while vector:
            leading = min(vector)
            if leading in self.pivots:
                subtract_multiple(vector, self.pivots[leading], vector[leading])
            else:
                factor = vector[leading]
                vector = {j: a / factor for j, a in vector.items()}
                self.max_bits = max(self.max_bits, check_bits(vector))
                self.pivots[leading] = vector
                return True
        return False

    def __len__(self):
        return len(self.pivots)


def domain_basis(generators, grade):
    integer(grade, 0, 3, "evaluation grade")
    result = tuple(
        (j, exponent)
        for j, generator in enumerate(generators)
        if generator["degree"] <= grade
        for exponent in compositions(grade - generator["degree"], 10)
    )
    need(len(result) <= 1265, "evaluation column cap")
    return result


def evaluate(generators, grade):
    rows = source_basis(grade)
    index = {a: j for j, a in enumerate(rows)}
    domain = domain_basis(generators, grade)
    columns, weights = [], []
    for generator_id, exponent in domain:
        generator = generators[generator_id]
        image = polynomial_product(
            ((generator["source_exponent"], 1),), s_image(exponent)
        )
        weight = add_weights(generator["weight"], polynomial_weight(exponent))
        need(
            all(source_weight(a) == weight for a, _ in image),
            "nonhomogeneous source column",
        )
        columns.append({index[a]: coefficient for a, coefficient in image})
        weights.append(weight)
    return {
        "grade": grade,
        "source_basis": rows,
        "domain_basis": domain,
        "columns": columns,
        "weights": weights,
    }


def blocks_of(weights):
    blocks = defaultdict(list)
    for j, weight in enumerate(weights):
        blocks[weight].append(j)
    return dict(sorted(blocks.items()))


def span_by_weight(evaluation):
    result = {}
    for weight, indices in blocks_of(evaluation["weights"]).items():
        need(len(indices) <= MAX_BLOCK, "weight-block column cap")
        span = Span()
        for j in indices:
            span.add(evaluation["columns"][j])
        result[weight] = span
    return result


def choose_generators():
    generators = [{"degree": 0, "source_exponent": ZERO_R, "weight": (0, 0, 0)}]
    selections = []
    for grade, expected_new in ((1, 17), (2, 11)):
        evaluation = evaluate(generators, grade)
        spans = span_by_weight(evaluation)
        old_rank = sum(len(span) for span in spans.values())
        new_indices = []
        for row, exponent in enumerate(evaluation["source_basis"]):
            weight = source_weight(exponent)
            span = spans.setdefault(weight, Span())
            if span.add({row: 1}):
                generators.append(
                    {"degree": grade, "source_exponent": exponent, "weight": weight}
                )
                new_indices.append(row)
        need(len(new_indices) == expected_new, "minimal-generator prediction failed")
        need(
            sum(len(span) for span in spans.values())
            == len(evaluation["source_basis"]),
            "generator span incomplete",
        )
        selections.append(
            {
                "grade": grade,
                "old_domain_dimension": len(evaluation["domain_basis"]),
                "old_image_rank": old_rank,
                "new_source_row_indices": new_indices,
            }
        )
    need(len(generators) == 29, "generator total")
    return generators, selections


def image_of_relation(columns, relation):
    result = Counter()
    for column, factor in relation.items():
        integer(column, 0, len(columns) - 1, "relation column")
        need(type(factor) is int, "integer relation coefficients required")
        for row, coefficient in columns[column].items():
            result[row] += factor * coefficient
    return {row: a for row, a in result.items() if a}


def exact_kernel(evaluation):
    relations, relation_weights, stats = [], [], []
    for weight, indices in blocks_of(evaluation["weights"]).items():
        row_support = set().union(*(evaluation["columns"][j] for j in indices))
        need(
            max(len(indices), len(row_support)) <= MAX_BLOCK,
            "weight-block dimension cap",
        )
        pivots = {}
        kernels = []
        max_bits = 0
        for j in indices:
            vector = {row: Fraction(a) for row, a in evaluation["columns"][j].items()}
            witness = {j: Fraction(1)}
            while vector:
                leading = min(vector)
                if leading in pivots:
                    image, old_witness = pivots[leading]
                    factor = vector[leading]
                    subtract_multiple(vector, image, factor)
                    subtract_multiple(witness, old_witness, factor)
                else:
                    factor = vector[leading]
                    image = {row: a / factor for row, a in vector.items()}
                    witness = {col: a / factor for col, a in witness.items()}
                    max_bits = max(max_bits, check_bits(image), check_bits(witness))
                    pivots[leading] = (image, witness)
                    break
            if not vector:
                relation = primitive_integer(witness)
                need(
                    not image_of_relation(evaluation["columns"], relation),
                    "kernel witness does not map to zero",
                )
                kernels.append(relation)
        need(len(indices) == len(pivots) + len(kernels), "rank-nullity mismatch")
        relations.extend(kernels)
        relation_weights.extend([weight] * len(kernels))
        stats.append(
            {
                "weight": weight,
                "rows": len(row_support),
                "columns": len(indices),
                "rank": len(pivots),
                "nullity": len(kernels),
                "max_exact_bits": max_bits,
            }
        )
    return relations, relation_weights, stats


def multiply_relation(relation, degree_two, degree_three, variable):
    integer(variable, 0, 9, "W variable")
    index = {entry: j for j, entry in enumerate(degree_three["domain_basis"])}
    answer = {}
    for j, coefficient in relation.items():
        generator, exponent = degree_two["domain_basis"][j]
        new = list(exponent)
        new[variable] += 1
        answer[index[(generator, tuple(new))]] = coefficient
    need(
        not image_of_relation(degree_three["columns"], answer),
        "multiplied relation fails source substitution",
    )
    return answer


def minimal_degree_three(
    degree_two, relations_two, weights_two, degree_three, kernels_three, weights_three
):
    old, old_weights, source_labels = [], [], []
    for j, (relation, weight) in enumerate(
        zip(relations_two, weights_two, strict=True)
    ):
        for variable in range(10):
            old.append(multiply_relation(relation, degree_two, degree_three, variable))
            old_weights.append(add_weights(weight, w_contents()[variable]))
            source_labels.append((j, variable))
    spans = {}
    for weight, indices in blocks_of(old_weights).items():
        span = Span()
        for j in indices:
            need(
                span.add(old[j]),
                "old-relation multiplication has a syzygy in degree three",
            )
        spans[weight] = span
    old_rank = sum(len(span) for span in spans.values())
    new, new_weights = [], []
    for relation, weight in zip(kernels_three, weights_three, strict=True):
        span = spans.setdefault(weight, Span())
        if span.add(relation):
            new.append(relation)
            new_weights.append(weight)
    need(old_rank == 200 and len(new) == 65, "old/new relation prediction failed")
    need(
        sum(len(span) for span in spans.values()) == len(kernels_three),
        "old/new relation span incomplete",
    )
    return (
        new,
        new_weights,
        {
            "source_labels_relation_variable": source_labels,
            "columns": old,
            "weights": old_weights,
            "rank": old_rank,
        },
    )


def permutation_section_control(generators):
    chosen = {g["source_exponent"] for g in generators if g["degree"] == 1}
    for exponent in sorted(chosen):
        rows = (exponent[:3], exponent[3:6], exponent[6:])
        for permutation in itertools.permutations(range(3)):
            image = tuple(a for j in permutation for a in rows[j])
            if image not in chosen:
                need(
                    source_weight(image) == source_weight(exponent),
                    "permutation changes GL weight",
                )
                return {
                    "chosen_source_monomial": exponent,
                    "factor_permutation": permutation,
                    "image_source_monomial": image,
                    "image_outside_marked_generator_span": True,
                    "equivariant_section_claimed": False,
                }
    raise ValueError("expected marked-section non-equivariance witness missing")


def sparse_record(vector):
    return [[j, a] for j, a in sorted(vector.items())]


def evaluation_record(evaluation, stats):
    return {
        "grade": evaluation["grade"],
        "source_basis": evaluation["source_basis"],
        "domain_basis_generator_and_S_exponents": evaluation["domain_basis"],
        "column_weights": evaluation["weights"],
        "sparse_columns_row_coefficient": [
            sparse_record(v) for v in evaluation["columns"]
        ],
        "weight_blocks": stats,
    }


def differential_columns(evaluation, relations, weights):
    answer = []
    for relation, weight in zip(relations, weights, strict=True):
        terms = []
        for j, coefficient in sorted(relation.items()):
            generator, exponent = evaluation["domain_basis"][j]
            need(
                sum(exponent) > 0,
                "constant entry would violate minimality of the presentation",
            )
            terms.append(
                {
                    "generator": generator,
                    "S_exponent": exponent,
                    "coefficient": coefficient,
                }
            )
        answer.append({"degree": evaluation["grade"], "weight": weight, "terms": terms})
    return answer


@lru_cache(maxsize=2)
def _build_maps(cut):
    generators, selections = choose_generators()
    degree_two = evaluate(generators, 2)
    relations_two, weights_two, stats_two = exact_kernel(degree_two)
    need(
        (
            len(degree_two["domain_basis"]),
            sum(x["rank"] for x in stats_two),
            len(relations_two),
        )
        == (236, 216, 20),
        "degree-two presentation prediction failed",
    )
    result = {
        "cutoff": cut,
        "generators": generators,
        "generator_selection": selections,
        "literal_W_contents": w_contents(),
        "literal_W_images": w_images(),
        "evaluations": [evaluation_record(degree_two, stats_two)],
        "D1_columns": differential_columns(degree_two, relations_two, weights_two),
        "section_countercontrol": permutation_section_control(generators),
        "all_displayed_relations_substitute_to_zero": True,
        "minimal_generator_degrees": [1, 17, 11],
    }
    if cut == 3:
        degree_three = evaluate(generators, 3)
        kernels_three, weights_three, stats_three = exact_kernel(degree_three)
        need(
            (
                len(degree_three["domain_basis"]),
                sum(x["rank"] for x in stats_three),
                len(kernels_three),
            )
            == (1265, 1000, 265),
            "degree-three presentation prediction failed",
        )
        new, new_weights, old = minimal_degree_three(
            degree_two,
            relations_two,
            weights_two,
            degree_three,
            kernels_three,
            weights_three,
        )
        result["evaluations"].append(evaluation_record(degree_three, stats_three))
        result["D1_columns"].extend(
            differential_columns(degree_three, new, new_weights)
        )
        result["old_relation_multiplication"] = {
            "source_labels_relation_variable": old["source_labels_relation_variable"],
            "weights": old["weights"],
            "rank": old["rank"],
            "sparse_columns_F0_degree3": [sparse_record(v) for v in old["columns"]],
        }
        result["full_degree3_kernel_basis"] = [sparse_record(v) for v in kernels_three]
        result["minimal_relation_degrees"] = [20, 65]
        need(len(result["D1_columns"]) == 85, "first differential column count")
    return result


def build_maps(cut=3):
    integer(cut, 2, 3, "presentation cutoff")
    return _build_maps(cut)


def compare_frozen_tor(source, maps):
    panels = {
        row["grade"]: row
        for row in source["result"]["literal_koszul_sources"]
        if (row["dimension"], row["factor_count"]) == (3, 3)
    }
    need(sorted(panels) == [1, 2, 3], "frozen cube grade coverage")
    checked = []
    for i, grade in ((0, 1), (0, 2), (1, 2), (1, 3)):
        if grade > maps["cutoff"]:
            continue
        records = maps["generators"] if i == 0 else maps["D1_columns"]
        actual = Counter(
            tuple(row["weight"]) for row in records if row["degree"] == grade
        )
        expected = {
            tuple(row["weight"]): row["homology"][i]["identity"]
            for row in panels[grade]["homology_weight_rows"]
        }
        need(
            all(type(a) is int for a in expected.values()),
            "frozen Tor dimensions must be integers",
        )
        need(
            actual == Counter({weight: a for weight, a in expected.items() if a}),
            "actual minimal-map weight dimensions disagree with frozen Tor",
        )
        checked.append(
            {
                "homological_degree": i,
                "internal_degree": grade,
                "dimension": sum(actual.values()),
                "complete_weight_match": True,
            }
        )
    return checked


def summary(maps):
    return {
        "cutoff": maps["cutoff"],
        "generators": len(maps["generators"]),
        "D1_columns": len(maps["D1_columns"]),
        "evaluations": [
            {
                "grade": row["grade"],
                "rows": len(row["source_basis"]),
                "columns": len(row["domain_basis_generator_and_S_exponents"]),
                "rank": sum(b["rank"] for b in row["weight_blocks"]),
                "nullity": sum(b["nullity"] for b in row["weight_blocks"]),
                "largest_block_rows": max(b["rows"] for b in row["weight_blocks"]),
                "largest_block_columns": max(
                    b["columns"] for b in row["weight_blocks"]
                ),
                "max_exact_bits": max(
                    b["max_exact_bits"] for b in row["weight_blocks"]
                ),
            }
            for row in maps["evaluations"]
        ],
    }


def build():
    source = authenticate_source()
    maps = build_maps()
    record = {
        "source_freeze": FREEZE,
        "source_blobs": dict(PINS),
        "owned_sha256_canonical_lf": {
            name: hashlib.sha256(canonical_bytes(HERE / name)).hexdigest()
            for name in OWNED
        },
        "test_sha256_canonical_lf": hashlib.sha256(canonical_bytes(TEST)).hexdigest(),
        "scope": {
            "actual_source_maps": True,
            "global_first_presentation_uses_frozen_Tor_and_duality": True,
            "marked_torus_homogeneous_choices": True,
            "GL3_or_factor_S3_equivariant_splittings_claimed": False,
            "second_and_third_differential_matrices_constructed": False,
            "new_untouched_rank3_power3_case_claimed": False,
        },
        "summary": summary(maps),
        "frozen_Tor_weight_checks": compare_frozen_tor(source, maps),
        "result": maps,
    }
    record["proof_object_sha256"] = hashlib.sha256(
        canonical_json(record).encode()
    ).hexdigest()
    need(
        len(json.dumps(record, indent=2, sort_keys=True, allow_nan=False).encode())
        <= MAX_BYTES,
        "serialized matrix record exceeds cap",
    )
    return record


def check_payload(candidate, expected):
    need(
        canonical_json(candidate) == canonical_json(expected),
        "typed canonical matrix record differs",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scout", action="store_true")
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.scout:
        source = authenticate_source()
        maps = build_maps(2)
        print(
            json.dumps(
                {
                    "summary": summary(maps),
                    "frozen_Tor_weight_checks": compare_frozen_tor(source, maps),
                    "fixture_written": False,
                },
                sort_keys=True,
            )
        )
        return
    record = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    else:
        check_payload(json.loads(FIXTURE.read_text(encoding="utf-8")), record)
    print(
        json.dumps(
            {
                "status": "PASS",
                "summary": record["summary"],
                "proof_object_sha256": record["proof_object_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
