"""New 640-column Chow kernels with lazy original-coordinate matrices."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from bisect import bisect_right
from collections import Counter
from collections.abc import Sequence
from fractions import Fraction
from itertools import zip_longest
from math import comb
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
ROW_FREEZE = "a9c78452768df3f3be643afbbfe1661e4f14bd85"
ROW_PINS = {
    PREFIX
    + "ROW_RESTRICTED_RESOLUTION_PREREGISTRATION.md": "7f3ab0fdc833b4b6004df7e8b1c59c4c4aa22dda",
    PREFIX
    + "ROW_RESTRICTED_RESOLUTION_REPLAY.md": "29163a7bb3c59cb2202c90671a06745874e1bffe",
    PREFIX + "row_restricted_resolution.py": "0a43b7ebce8e4a868952fa53a96ca42be76998b3",
    "tests/test_segre_hadamard_row_restricted_resolution.py": "d30a8ebdd65214453def0d986929c8848856417b",
}
SHAPE_FREEZE = "5cb770ce6ef7e20535de155d9b232698424d2e3c"
SHAPE_PINS = {
    PREFIX
    + "RESOLUTION_SHAPE_PREREGISTRATION.md": "acba78d69b017771a6af608184e024ebf180ce71",
    PREFIX
    + "resolution_shape_preflight.py": "c38e375c626962eebc653700ab84d40ba75619c1",
    PREFIX
    + "resolution_shape.discovery.json": "53dd114fd6eedb179c6b0fe2e4730f2909d1bc4d",
}
PROOF_FREEZE = "423a25c35996ec5bf2c4dfaac6594d31f89f1081"
PROOF_PINS = {
    PREFIX
    + "GLOBAL_EXACTNESS_FROM_CERTIFIED_KERNELS.md": "79e3792aad018275ba90353e470f1fa234bd76d5",
    PREFIX
    + "TERNARY_CUBE_FULL_RESOLUTION.md": "daa8d3f42701dbc6ba5a22c18782e4568bec22cf",
}
# Root-accepted complete discovery, not an assertion that the old42 suite ran.
STAGE6_FREEZE = "d3bda0446a379ce0bd8dfe4024f0184451adb1d5"
STAGE6_PINS = {
    PREFIX
    + "row_restricted_grade6.discovery.json": "b9131081876be381c43237ea42c5695767bd73ae"
}
MODULI = (65521, 1000003)
MAX_ROWS = 4096
MAX_COLUMNS = 640
MAX_BYTES = 64 * 1024 * 1024
DIRECTORY = HERE / "streamed640_weightblocks"
FIXTURE = HERE / "streamed640_resolution.verification.json"
COORDINATE_FIXTURE = HERE / "streamed640_coordinate.discovery.json"
PREREG = HERE / "STREAMED_RESOLUTION640_PREREGISTRATION.md"
OWNED = (
    PREREG,
    HERE / "STREAMED_RESOLUTION640_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_segre_hadamard_streamed640.py",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal integer outside cap")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def normalized(value):
    return json.loads(canonical(value))


def digest(value):
    result = hashlib.sha256()
    size = 0
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    for chunk in encoder.iterencode(value):
        raw = chunk.encode()
        size += len(raw)
        need(size < MAX_BYTES, "canonical object byte cap")
        result.update(raw)
    return result.hexdigest()


def check_payload(candidate, expected):
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    missing = object()
    for left, right in zip_longest(
        encoder.iterencode(candidate), encoder.iterencode(expected), fillvalue=missing
    ):
        need(left == right, "typed complete streamed640 replay differs")


def no_float(_value):
    raise ValueError("floating or nonfinite JSON")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "bounded JSON source")
    return json.loads(
        raw,
        parse_float=no_float,
        parse_constant=no_float,
        object_pairs_hook=unique_object,
    )


def authenticate_group(freeze, pins):
    need(
        type(freeze) is str
        and len(freeze) == 40
        and all(c in "0123456789abcdef" for c in freeze),
        "exact freeze required before source access",
    )
    need(
        all(
            type(value) is str
            and len(value) == 40
            and all(c in "0123456789abcdef" for c in value)
            for value in pins.values()
        ),
        "exact frozen blob identities required",
    )
    raw, provenance = {}, {}
    need(type(pins) is dict and pins, "nonempty exact source binding")
    for path, expected in pins.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{freeze}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen streamed640 source mismatch")
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", actual], cwd=ROOT, text=True
            )
        )
        need(0 < size <= MAX_BYTES, "frozen source byte cap")
        data = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        current = (ROOT / path).read_bytes()
        need(len(data) == size and len(current) <= MAX_BYTES, "source length")
        need(
            current.replace(b"\r\n", b"\n") == data.replace(b"\r\n", b"\n"),
            "current certified source changed",
        )
        raw[path] = data
        provenance[path] = {
            "blob": actual,
            "sha256_lf": hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest(),
        }
    return raw, provenance


def authenticate():
    raw, row = authenticate_group(ROW_FREEZE, ROW_PINS)
    shape_raw, shape = authenticate_group(SHAPE_FREEZE, SHAPE_PINS)
    proof_raw, proof = authenticate_group(PROOF_FREEZE, PROOF_PINS)
    raw.update(shape_raw)
    raw.update(proof_raw)
    return raw, {
        "row_freeze": ROW_FREEZE,
        "row": row,
        "shape_freeze": SHAPE_FREEZE,
        "shape": shape,
        "proof_freeze": PROOF_FREEZE,
        "proof": proof,
    }


def load_frozen():
    raw, provenance = authenticate()
    path = PREFIX + "row_restricted_resolution.py"
    namespace = {
        "__name__": "authenticated_unchanged_row512_source",
        "__file__": str(ROOT / path),
    }
    exec(compile(raw[path], str(ROOT / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace), provenance


def verified_source():
    prior, provenance = load_frozen()
    context = prior.verified_source()
    context.prior = prior
    context.source_provenance = provenance
    return context


def composition_rank(exponent):
    """Lexicographic address, independently checked against literal enumeration."""
    need(
        type(exponent) in (list, tuple) and len(exponent) == 10,
        "ten polynomial coordinates",
    )
    need(
        all(type(value) is int and 0 <= value <= 7 for value in exponent),
        "literal bounded polynomial exponents",
    )
    remaining = sum(exponent)
    integer(remaining, 0, 7)
    address = 0
    for i, value in enumerate(exponent[:-1]):
        length = 10 - i
        address += comb(remaining + length - 1, length - 1)
        address -= comb(remaining - value + length - 1, length - 1)
        remaining -= value
    return address


class ModuleBasis(Sequence):
    """Original module order without a full target list or reverse dictionary."""

    def __init__(self, helper, generators, grade):
        integer(grade, 0, 7)
        self.helper, self.generators, self.grade = helper, generators, grade
        self.offsets, self.starts, self.active = [], [], []
        size = 0
        for i, generator in enumerate(generators):
            degree = integer(generator["degree"], 0, 7)
            self.offsets.append(size)
            if degree <= grade:
                self.starts.append(size)
                self.active.append(i)
                size += comb(grade - degree + 9, 9)
        need(size <= 90000, "lazy target module cap")
        self.size = size

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in self.active:
            for exponent in self.helper.compositions(
                self.grade - self.generators[i]["degree"], 10
            ):
                yield i, exponent

    def __getitem__(self, index):
        need(type(index) is int, "literal module coordinate")
        if index < 0:
            index += self.size
        if not 0 <= index < self.size:
            raise IndexError(index)
        generator = self.active[bisect_right(self.starts, index) - 1]
        exponent = self.helper.compositions(
            self.grade - self.generators[generator]["degree"], 10
        )[index - self.offsets[generator]]
        return generator, exponent

    def address(self, generator, exponent):
        integer(generator, 0, len(self.generators) - 1)
        local = composition_rank(exponent)
        need(
            sum(exponent) == self.grade - self.generators[generator]["degree"],
            "target generator degree plus exponent",
        )
        return self.offsets[generator] + local


class LazyColumns(Sequence):
    """Reconstruct each actual sparse column only in its original coordinates."""

    def __init__(self, helper, target, columns, domain, weights):
        self.helper, self.target, self.source = helper, target, columns
        self.domain, self.weights = domain, weights

    def __len__(self):
        return len(self.domain)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __getitem__(self, index):
        need(type(index) is int, "literal original column coordinate")
        if index < 0:
            index += len(self)
        if not 0 <= index < len(self):
            raise IndexError(index)
        source_index, multiplier = self.domain[index]
        result = Counter()
        for term in self.source[source_index]["terms"]:
            exponent = self.helper.add(term["S_exponent"], multiplier)
            generator = term["generator"]
            need(
                self.helper.add(
                    self.target.generators[generator]["weight"],
                    self.helper.polynomial_weight(exponent),
                )
                == self.weights[index],
                "streamed actual term torus weight",
            )
            row = self.target.address(generator, exponent)
            coefficient = term["coefficient"]
            need(
                type(coefficient) is int and coefficient != 0,
                "literal actual source coefficient",
            )
            result[row] += coefficient
        return {row: value for row, value in result.items() if value}


def lazy_evaluation(helper, targets, columns, grade):
    target = ModuleBasis(helper, targets, grade)
    domain = tuple(ModuleBasis(helper, columns, grade))
    need(len(domain) <= 16000, "complete domain module cap")
    weights = [
        helper.add(columns[i]["weight"], helper.polynomial_weight(exp))
        for i, exp in domain
    ]
    return {
        "grade": grade,
        "target_basis": target,
        "domain_basis": domain,
        "weights": weights,
        "columns": LazyColumns(helper, target, columns, domain, weights),
    }


def coordinate_check(context):
    """Exhaustive grade-six comparison; no elimination or kernel conclusion."""
    helper, upstream, maps = context.helper, context.upstream, context.maps
    original = helper.evaluated_map(maps["D1_columns"], maps["D2_columns"], 6)
    streamed = lazy_evaluation(helper, maps["D1_columns"], maps["D2_columns"], 6)
    need(
        (len(original["target_basis"]), len(original["domain_basis"])) == (28600, 3775),
        "declared complete grade-six coordinate comparison",
    )
    need(
        original["domain_basis"] == streamed["domain_basis"],
        "every original domain descriptor",
    )
    need(original["weights"] == streamed["weights"], "every original column weight")
    for i, old in enumerate(original["target_basis"]):
        need(old == streamed["target_basis"][i], "every lazy target descriptor")
        need(
            streamed["target_basis"].address(*old) == i,
            "every combinatorial target address",
        )
    for i, column in enumerate(original["columns"]):
        need(column == streamed["columns"][i], "every full original sparse column")
    digests = {
        "target_basis": upstream.digest_rows(streamed["target_basis"]),
        "domain_basis": upstream.digest_rows(streamed["domain_basis"]),
        "weights": upstream.digest_rows(streamed["weights"]),
        "matrix": upstream.digest_rows(upstream.sparse(c) for c in streamed["columns"]),
    }
    need(
        digests["matrix"]
        == upstream.digest_rows(upstream.sparse(c) for c in original["columns"]),
        "independent matrix digest",
    )
    return {
        "grade": 6,
        "target_rows": 28600,
        "domain_columns": 3775,
        "all_descriptors_addresses_weights_columns_compared": True,
        "digests": digests,
        "kernel_or_rank_computed": False,
    }


def source_ownership(context):
    return {
        "cache_provenance": context.cache_provenance,
        "source_provenance": context.source_provenance,
        "accepted_stage6": context.stage6_provenance,
        "algorithm_sha256_lf": hashlib.sha256(
            Path(__file__).read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "preregistration_sha256_lf": hashlib.sha256(
            PREREG.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "moduli": list(MODULI),
        "full_rows_per_weight": MAX_ROWS,
        "columns_per_weight": MAX_COLUMNS,
        "new640_algorithm_old512_unchanged": True,
    }


def preflight_full(upstream, evaluation):
    need(
        len(evaluation["target_basis"]) <= 90000
        and len(evaluation["domain_basis"]) <= 16000,
        "unchanged full basis caps",
    )
    need(
        len(evaluation["columns"])
        == len(evaluation["weights"])
        == len(evaluation["domain_basis"]),
        "complete matrix column metadata",
    )
    need(
        all(
            type(weight) in (tuple, list)
            and len(weight) == 3
            and all(type(value) is int and 0 <= value <= 21 for value in weight)
            for weight in evaluation["weights"]
        ),
        "literal source weights before grouping",
    )
    profiles = []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        need(
            len(weight) == 3
            and all(type(value) is int and 0 <= value <= 21 for value in weight),
            "literal source weight",
        )
        columns = [evaluation["columns"][i] for i in indices]
        support = (
            set().union(*(set(column) for column in columns)) if columns else set()
        )
        need(
            len(indices) <= MAX_COLUMNS and len(support) <= MAX_ROWS,
            "new full weight-block cap",
        )
        for column in columns:
            need(
                all(
                    type(row) is int
                    and 0 <= row < len(evaluation["target_basis"])
                    and type(value) is int
                    and value != 0
                    for row, value in column.items()
                ),
                "literal full original integer matrix",
            )
        profiles.append(
            {"weight": list(weight), "rows": len(support), "columns": len(indices)}
        )
    return profiles


def select_original_rows(columns, modulus):
    need(type(modulus) is int and modulus in MODULI, "fixed row-selection modulus")
    need(1 <= len(columns) <= MAX_COLUMNS, "row-selection column cap")
    support = sorted(set().union(*(set(column) for column in columns)))
    need(len(support) <= MAX_ROWS, "streamed row cap")
    need(
        all(
            type(row) is int and row >= 0 and type(value) is int
            for column in columns
            for row, value in column.items()
        ),
        "literal integer row selection input",
    )
    pivots, selected = {}, []
    for row in support:
        vector = {
            i: column[row] % modulus
            for i, column in enumerate(columns)
            if row in column and column[row] % modulus
        }
        while vector:
            leading = min(vector)
            if leading not in pivots:
                inverse = pow(vector[leading], modulus - 2, modulus)
                pivots[leading] = {
                    i: value * inverse % modulus for i, value in vector.items()
                }
                selected.append(row)
                break
            scalar = vector[leading]
            for i, value in pivots[leading].items():
                result = (vector.get(i, 0) - scalar * value) % modulus
                if result:
                    vector[i] = result
                else:
                    vector.pop(i, None)
    return {
        "modulus": modulus,
        "selected_original_rows": selected,
        "pivot_local_column_indices": list(pivots),
        "modular_row_rank": len(selected),
    }


def restricted_columns(columns, selected):
    need(
        type(selected) is list
        and all(type(row) is int and row >= 0 for row in selected)
        and selected == sorted(set(selected)),
        "ordered literal selected original rows",
    )
    retained = set(selected)
    return [
        {row: value for row, value in column.items() if row in retained}
        for column in columns
    ]


def modular_rank640(columns, modulus):
    """The frozen column-rank formula, under this NEW 640 identity only."""
    need(type(modulus) is int and modulus in MODULI, "fixed prime rank certificate")
    need(len(columns) <= MAX_COLUMNS, "new640 modular column cap")
    support = set().union(*(set(c) for c in columns)) if columns else set()
    need(len(support) <= MAX_COLUMNS, "new640 modular selected-row cap")
    pivots, selected = {}, []
    for index, column in enumerate(columns):
        need(
            all(
                type(row) is int and row >= 0 and type(value) is int
                for row, value in column.items()
            ),
            "literal modular matrix",
        )
        vector = {
            row: value % modulus for row, value in column.items() if value % modulus
        }
        while vector:
            row = min(vector)
            if row not in pivots:
                inverse = pow(vector[row], modulus - 2, modulus)
                pivots[row] = {
                    key: value * inverse % modulus for key, value in vector.items()
                }
                selected.append(index)
                break
            scalar = vector[row]
            for key, value in pivots[row].items():
                new = (vector.get(key, 0) - scalar * value) % modulus
                if new:
                    vector[key] = new
                else:
                    vector.pop(key, None)
    return {
        "modulus": modulus,
        "rank": len(pivots),
        "pivot_rows_in_insertion_order": list(pivots),
        "independent_local_column_indices": selected,
    }


def preflight640(upstream, evaluation):
    need(
        len(evaluation["columns"]) == len(evaluation["weights"]),
        "complete new640 column weights",
    )
    need(
        all(
            type(weight) in (list, tuple)
            and len(weight) == 3
            and all(type(value) is int and 0 <= value <= 21 for value in weight)
            for weight in evaluation["weights"]
        ),
        "literal new640 weights",
    )
    profiles = []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        support = set().union(*(evaluation["columns"][i] for i in indices))
        need(
            len(indices) <= MAX_COLUMNS and len(support) <= MAX_COLUMNS,
            "new640 exact selected-row or quotient block cap",
        )
        need(
            all(
                type(row) is int and row >= 0 and type(value) is int and value != 0
                for i in indices
                for row, value in evaluation["columns"][i].items()
            ),
            "literal new640 exact matrix",
        )
        profiles.append(
            {"weight": weight, "rows": len(support), "columns": len(indices)}
        )
    return profiles


def kernel640(helper, upstream, evaluation):
    """Literal frozen rational elimination formula; only the declared cap is new."""
    preflight640(upstream, evaluation)
    for column in evaluation["columns"]:
        helper.check_bits(column)
    relations, weights, stats = [], [], []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        support = set().union(*(evaluation["columns"][i] for i in indices))
        pivots, local, bits = {}, [], 0
        for i in indices:
            vector = {j: Fraction(a) for j, a in evaluation["columns"][i].items()}
            witness = {i: Fraction(1)}
            while vector:
                leading = min(vector)
                if leading in pivots:
                    old_image, old_witness = pivots[leading]
                    scalar = vector[leading]
                    helper.subtract_multiple(vector, old_image, scalar)
                    helper.subtract_multiple(witness, old_witness, scalar)
                else:
                    scalar = vector[leading]
                    image = {j: a / scalar for j, a in vector.items()}
                    witness = {j: a / scalar for j, a in witness.items()}
                    bits = max(
                        bits, helper.check_bits(image), helper.check_bits(witness)
                    )
                    pivots[leading] = (image, witness)
                    break
            if not vector:
                relation = helper.primitive_integer(witness)
                need(
                    not helper.image_of_relation(evaluation["columns"], relation),
                    "new640 kernel has nonzero actual composition",
                )
                local.append(relation)
        need(len(indices) == len(pivots) + len(local), "new640 kernel rank-nullity")
        relations.extend(local)
        weights.extend([weight] * len(local))
        stats.append(
            {
                "weight": weight,
                "rows": len(support),
                "columns": len(indices),
                "rank": len(pivots),
                "nullity": len(local),
                "max_exact_bits": bits,
            }
        )
    return relations, weights, stats


def certify_attempt(verifier, helper, columns, weight, attempt):
    need(
        type(attempt) is dict
        and set(attempt)
        == {
            "row_selection",
            "restricted_kernel",
            "restricted_statistics",
            "certificate",
        },
        "complete row-selection attempt",
    )
    selection = attempt["row_selection"]
    need(
        type(selection) is dict and type(selection.get("modulus")) is int,
        "literal row-selection metadata",
    )
    expected = select_original_rows(columns, selection["modulus"])
    check_payload(selection, expected)
    restricted = restricted_columns(columns, expected["selected_original_rows"])
    rank = expected["modular_row_rank"]
    modular = modular_rank640(restricted, expected["modulus"])
    need(modular["rank"] == rank, "independent selected-row modular rank")
    vectors = [
        verifier.parse_vector(raw, len(columns), helper)
        for raw in attempt["restricted_kernel"]
    ]
    need(len(vectors) == len(columns) - rank, "complete restricted kernel dimension")
    peaks = [max(vector) for vector in vectors]
    need(len(set(peaks)) == len(peaks), "restricted kernel triangular independence")
    need(
        all(not helper.image_of_relation(restricted, vector) for vector in vectors),
        "actual restricted kernel compositions",
    )
    stat = attempt["restricted_statistics"]
    need(
        type(stat) is dict
        and set(stat)
        == {"weight", "rows", "columns", "rank", "nullity", "max_exact_bits"},
        "original restricted kernel statistics",
    )
    check_payload(
        {key: stat[key] for key in ("weight", "rows", "columns", "rank", "nullity")},
        {
            "weight": list(weight),
            "rows": rank,
            "columns": len(columns),
            "rank": rank,
            "nullity": len(vectors),
        },
    )
    integer(stat["max_exact_bits"], 0, 4096)
    failures = []
    for i, vector in enumerate(vectors):
        residual = helper.image_of_relation(columns, vector)
        helper.check_bits(residual)
        if residual:
            failures.append(
                {
                    "kernel_vector": i,
                    "full_original_residual": [
                        [row, value] for row, value in sorted(residual.items())
                    ],
                }
            )
    certificate = {
        "selected_modular_rank_certificate": modular,
        "kernel_dimension": len(vectors),
        "largest_local_kernel_coordinates": peaks,
        "verified_kernel_coefficient_bits": max(
            (helper.check_bits(vector) for vector in vectors), default=0
        ),
        "every_full_original_row_checked": True,
        "full_composition_failures": failures,
        "full_and_restricted_kernels_equal": not failures,
    }
    return vectors, certificate


def fresh_attempt(context, columns, weight, grade, modulus):
    selection = select_original_rows(columns, modulus)
    restricted = restricted_columns(columns, selection["selected_original_rows"])
    evaluation = {
        "grade": grade,
        "columns": restricted,
        "weights": [weight] * len(columns),
    }
    vectors, weights, stats = kernel640(context.helper, context.upstream, evaluation)
    need(
        weights == [weight] * len(vectors) and len(stats) == 1,
        "new640 exact one-weight kernel",
    )
    attempt = {
        "row_selection": selection,
        "restricted_kernel": [context.upstream.sparse(vector) for vector in vectors],
        "restricted_statistics": normalized(stats[0]),
        "certificate": None,
    }
    vectors, certificate = certify_attempt(
        context.verifier, context.helper, columns, weight, attempt
    )
    attempt["certificate"] = certificate
    return attempt, vectors


def checkpoint_input(upstream, evaluation, matrix, weight, indices, ownership):
    return {
        "ownership": ownership,
        "matrix": matrix,
        "grade": evaluation["grade"],
        "weight": list(weight),
        "original_column_indices": indices,
        "complete_block_columns_sha256": upstream.digest_rows(
            upstream.sparse(evaluation["columns"][i]) for i in indices
        ),
    }


def verify_checkpoint(payload, expected_input, context, columns, weight):
    need(
        type(payload) is dict
        and set(payload)
        == {"schema", "status", "input", "attempts", "proof_object_sha256"},
        "complete certified checkpoint schema",
    )
    need(
        payload["schema"] == "certified-streamed640-original-row-kernel-v1"
        and payload["status"] == "FULL_KERNEL_CERTIFIED",
        "only completed full kernels are reusable",
    )
    check_payload(payload["input"], expected_input)
    need(
        payload["proof_object_sha256"]
        == digest(
            {
                key: value
                for key, value in payload.items()
                if key != "proof_object_sha256"
            }
        ),
        "checkpoint body digest",
    )
    attempts = payload["attempts"]
    need(
        type(attempts) is list and 1 <= len(attempts) <= 2,
        "fixed fallback attempt count",
    )
    vectors = None
    for i, attempt in enumerate(attempts):
        need(
            attempt["row_selection"]["modulus"] == MODULI[i],
            "fixed modulus order with no hidden fallback",
        )
        vectors, certificate = certify_attempt(
            context.verifier, context.helper, columns, weight, attempt
        )
        check_payload(attempt["certificate"], certificate)
        need(
            certificate["full_and_restricted_kernels_equal"]
            is (i == len(attempts) - 1),
            "all failed attempts retained before one success",
        )
    return vectors


def write_atomic(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    size = 0
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    with temporary.open("wb") as output:
        for text in encoder.iterencode(payload):
            raw = text.encode()
            size += len(raw)
            need(size <= MAX_BYTES, "atomic object byte cap")
            output.write(raw)
        need(size + 1 <= MAX_BYTES, "atomic object byte cap")
        output.write(b"\n")
        output.flush()
        os.fsync(output.fileno())
    os.replace(temporary, path)


def certified_kernel(context, evaluation, directory=DIRECTORY):
    upstream, helper = context.upstream, context.helper
    preflight_full(upstream, evaluation)
    for column in evaluation["columns"]:
        helper.check_bits(column)
    matrix = {
        "grade": evaluation["grade"],
        "full_target_rows": len(evaluation["target_basis"]),
        "domain_columns": len(evaluation["domain_basis"]),
        "target_basis_sha256": upstream.digest_rows(evaluation["target_basis"]),
        "domain_basis_sha256": upstream.digest_rows(evaluation["domain_basis"]),
        "complete_weights_sha256": upstream.digest_rows(evaluation["weights"]),
        "full_original_matrix_sha256": upstream.digest_rows(
            upstream.sparse(column) for column in evaluation["columns"]
        ),
    }
    ownership = source_ownership(context)
    relations, weights, stats, certificates = [], [], [], []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        columns = [evaluation["columns"][i] for i in indices]
        expected_input = checkpoint_input(
            upstream, evaluation, matrix, weight, indices, ownership
        )
        path = Path(directory) / (digest(expected_input) + ".json")
        if path.is_file():
            need(path.stat().st_size <= MAX_BYTES, "completed checkpoint byte cap")
            payload = read_json(path.read_bytes())
            vectors = verify_checkpoint(
                payload, expected_input, context, columns, weight
            )
        else:
            attempts, vectors = [], None
            for modulus in MODULI:
                attempt, vectors = fresh_attempt(
                    context, columns, weight, evaluation["grade"], modulus
                )
                attempts.append(attempt)
                if attempt["certificate"]["full_and_restricted_kernels_equal"]:
                    break
            if not attempts[-1]["certificate"]["full_and_restricted_kernels_equal"]:
                failure = {
                    "schema": "certified-streamed640-original-row-kernel-v1",
                    "status": "FIXED_MODULI_FAILED",
                    "input": expected_input,
                    "attempts": attempts,
                }
                failure["proof_object_sha256"] = digest(failure)
                write_atomic(path.with_suffix(".failure.json"), failure)
                raise ValueError(
                    "both fixed row-selection moduli failed; full residuals retained"
                )
            payload = {
                "schema": "certified-streamed640-original-row-kernel-v1",
                "status": "FULL_KERNEL_CERTIFIED",
                "input": expected_input,
                "attempts": attempts,
            }
            payload["proof_object_sha256"] = digest(payload)
            write_atomic(path, payload)
        accepted = payload["attempts"][-1]
        translated = [
            {indices[i]: value for i, value in vector.items()} for vector in vectors
        ]
        need(
            all(
                not helper.image_of_relation(evaluation["columns"], vector)
                for vector in translated
            ),
            "full global original-coordinate compositions",
        )
        relations.extend(translated)
        weights.extend([weight] * len(vectors))
        support = set().union(*(set(column) for column in columns))
        stats.append(
            {
                "weight": weight,
                "rows": len(support),
                "columns": len(indices),
                "rank": accepted["row_selection"]["modular_row_rank"],
                "nullity": len(vectors),
                "max_exact_bits": max(
                    accepted["restricted_statistics"]["max_exact_bits"],
                    accepted["certificate"]["verified_kernel_coefficient_bits"],
                ),
                "selected_original_rows": len(
                    accepted["row_selection"]["selected_original_rows"]
                ),
                "successful_modulus": accepted["row_selection"]["modulus"],
                "every_full_original_row_checked": True,
            }
        )
        certificates.append(payload)
    return relations, weights, stats, certificates


def select_quotient640(context, evaluation, relations, weights, previous, generators):
    """Actual frozen quotient formula, with this separately declared block cap."""
    helper, upstream = context.helper, context.upstream
    old = helper.evaluated_map(generators, previous, evaluation["grade"])
    need(
        old["target_basis"] == evaluation["domain_basis"],
        "old multiple coordinate basis differs",
    )
    preflight640(upstream, old)
    spans = {}
    for i, weight in enumerate(old["weights"]):
        need(
            not helper.image_of_relation(evaluation["columns"], old["columns"][i]),
            "old multiple has nonzero full composition",
        )
        spans.setdefault(weight, upstream.Span(helper)).add(old["columns"][i])
    old_rank = sum(len(span.pivots) for span in spans.values())
    chosen, chosen_weights = [], []
    for relation, weight in zip(relations, weights, strict=True):
        if spans.setdefault(weight, upstream.Span(helper)).add(relation):
            chosen.append(relation)
            chosen_weights.append(weight)
    need(
        sum(len(span.pivots) for span in spans.values()) == len(relations),
        "actual old plus new does not span full kernel",
    )
    return chosen, chosen_weights, old, old_rank


def accepted_stage6():
    # PENDING fails here, before expensive source loading or a grade-seven matrix.
    raw, provenance = authenticate_group(STAGE6_FREEZE, STAGE6_PINS)
    need(len(raw) == 1, "one complete accepted stage-six payload")
    payload = read_json(next(iter(raw.values())))
    need(
        payload["schema"] == "actual-ternary-Chow-certified-original-row-resolution-v1",
        "accepted original512 stage-six identity",
    )
    need(
        type(payload["result"]["stage"]) is int
        and payload["result"]["stage"] == 6
        and payload["result"]["complete_resolution_constructed"] is False,
        "actual stage six only",
    )
    need(
        payload["proof_object_sha256"]
        == digest({k: v for k, v in payload.items() if k != "proof_object_sha256"}),
        "accepted stage-six payload body digest",
    )
    return payload, {
        "freeze": STAGE6_FREEZE,
        "bindings": provenance,
        "proof_object_sha256": payload["proof_object_sha256"],
    }


def extend_stage7(context, directory=DIRECTORY):
    upstream, helper, maps = context.upstream, context.helper, context.maps
    need(
        type(maps["stage"]) is int
        and maps["stage"] == 6
        and (len(maps["D2_columns"]), len(maps["D3_columns"])) == (85, 28),
        "complete accepted and freshly reverified stage-six maps",
    )
    d1, d2, d3 = maps["D1_columns"], maps["D2_columns"], maps["D3_columns"]
    evaluation = lazy_evaluation(helper, d1, d2, 7)
    need(
        (len(evaluation["target_basis"]), len(evaluation["domain_basis"]))
        == (86515, 15400),
        "full source grade-seven module sizes",
    )
    profiles = preflight_full(upstream, evaluation)
    need(
        max(row["columns"] for row in profiles) == 592,
        "frozen shape acquisition maximum",
    )
    need(
        next(row["columns"] for row in profiles if row["weight"] == [7, 7, 7]) == 592,
        "frozen central weight shape",
    )
    relations, weights, stats, certificates = certified_kernel(
        context, evaluation, directory
    )
    need(len(relations) == 776, "actual complete grade-seven kernel")
    chosen, chosen_weights, old, old_rank = select_quotient640(
        context, evaluation, relations, weights, d3, d2
    )
    need(
        (len(old["columns"]), old_rank, len(chosen)) == (775, 775, 1),
        "actual grade-seven old/new minimal quotient",
    )
    added = helper.differential_columns(evaluation, chosen, chosen_weights)
    maps["complete_Tor_weight_checks"]["D3_degree7"] = upstream.weight_check(
        added, maps["F0_generators"], 0
    )
    d3.extend(added)
    maps["stages"].append(
        {
            "map": "D2",
            "evaluation": upstream.evaluation_record(evaluation, stats, relations),
            "minimal_quotient": upstream.quotient_record(old, old_rank, chosen),
            "complete_streamed640_certificates": certificates,
        }
    )
    maps["stage"] = 7
    maps["complete_resolution_constructed"] = True
    maps["all_old_and_new_compositions_zero"] = True
    return maps


def build_maps(directory=DIRECTORY):
    accepted, stage6_provenance = accepted_stage6()
    context = verified_source()
    coordinates = coordinate_check(context)
    # The old function keeps its original __file__, PREREG and checkpoint keys.
    context.prior.extend_maps(context, 6, context.prior.DIRECTORY)
    check_payload(context.maps, accepted["result"])
    context.stage6_provenance = stage6_provenance
    maps = extend_stage7(context, directory)
    provenance = {
        "cache": context.cache_provenance,
        "frozen_sources": context.source_provenance,
        "accepted_stage6": stage6_provenance,
        "stage6_replayed_by_unchanged512_with_original_checkpoint_keys": True,
    }
    return maps, provenance, coordinates, context.upstream.summary(maps)


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def build(directory=DIRECTORY):
    maps, provenance, coordinates, summary = build_maps(directory)
    payload = {
        "schema": "actual-ternary-Chow-streamed640-resolution-v1",
        "owned_sha256_lf": owned_bindings(),
        "source_provenance": provenance,
        "coordinate_comparison": coordinates,
        "summary": summary,
        "result": maps,
        "streamed640_contract": {
            "prior_898_row_preflight_succeeded": False,
            "full_rows_cap": MAX_ROWS,
            "columns_cap": MAX_COLUMNS,
            "every_original_row_verified": True,
            "fixed_moduli": list(MODULI),
            "old_26_test_contract_replaced": False,
            "old_42_test_contract_replaced": False,
            "prior512_degree7_shape_eligible": False,
            "degree7_full_target_basis_or_matrix_materialized": False,
            "grade6_original_constructor_exhaustively_compared": True,
        },
    }
    payload["proof_object_sha256"] = digest(payload)
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scout", action="store_true")
    mode.add_argument("--coordinate-check", action="store_true")
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.coordinate_check:
        context = verified_source()
        result = {
            "schema": "streamed640-exhaustive-coordinate-comparison-v1",
            "source_provenance": context.source_provenance,
            "owned_sha256_lf": owned_bindings(),
            "result": coordinate_check(context),
        }
        result["proof_object_sha256"] = digest(result)
        write_atomic(COORDINATE_FIXTURE, result)
        print(canonical(result))
        return
    payload = build()
    if args.scout:
        # Root captures the complete maps; successful stdout is not a final fixture.
        json.dump(
            payload, sys.stdout, sort_keys=True, separators=(",", ":"), allow_nan=False
        )
        sys.stdout.write("\n")
        return
    if args.write:
        write_atomic(FIXTURE, payload)
    else:
        need(FIXTURE.stat().st_size <= MAX_BYTES, "final fixture byte cap")
        check_payload(read_json(FIXTURE.read_bytes()), payload)
    print(
        canonical(
            {
                "status": "PASS",
                "summary": payload["summary"],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
