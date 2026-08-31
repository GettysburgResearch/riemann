"""Exact higher change-of-rings d2 in three complete highest-weight blocks."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
import time
import types
from fractions import Fraction
from functools import lru_cache
from math import factorial, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
WEIGHTS = ((6, 4, 2), (5, 5, 2), (5, 4, 3))
CHAR_FREEZE = "08147ccecfe684af76a8417861fcccda61abe601"
CHAR_BLOB = "4ea01d1d6fbb0383e31f03f060a8511dd3c7a1e4"
Q_FREEZE = "c7ea79747208dfa6e164cb87c2e4f9ee523cbb3d"
Q_PREFIX = PREFIX + "five-hour-equivariant-pass/"
Q_PINS = {
    "PREREGISTRATION.md": (
        Q_PREFIX + "PREREGISTRATION.md",
        "58d9ecd25fa6a89ac6532605f9cff9d8b6462a66",
    ),
    "Q_ACTION_MATHEMATICS.md": (
        Q_PREFIX + "Q_ACTION_MATHEMATICS.md",
        "699fa66fc6f501208a9f9374d17cc32928473d37",
    ),
    "Q_ACTION_REPLAY.md": (
        Q_PREFIX + "Q_ACTION_REPLAY.md",
        "b481b351b1f7ab78f8bc00e936db5c75d2a06b65",
    ),
    "q_action.py": (
        Q_PREFIX + "q_action.py",
        "9d78ff4cb7417436806d816050006dff251635bb",
    ),
    "q_action.verification.json": (
        Q_PREFIX + "q_action.verification.json",
        "fbc9982a067db22e42e8fb49231581c6d48f8dd5",
    ),
    "sources/PR782_THEOREM_I.md": (
        Q_PREFIX + "sources/PR782_THEOREM_I.md",
        "749cc53453e4842ca010c4028d2a9b35024e3208",
    ),
    "test_equivariant_pass_q_action.py": (
        "tests/test_equivariant_pass_q_action.py",
        "b26386d1fb88a3d5bb0715bca356082ec737d5a6",
    ),
}
MAX_BLOCK = 512
MAX_BYTES = 16 * 1024 * 1024
SHAPE = HERE / "d2.shape.json"
FIXTURE = HERE / "d2.verification.json"
TEST = ROOT / "tests/test_equivariant_pass_d2.py"
OWNED = (
    "D2_PREREGISTRATION.md",
    "ACTUAL_CHANGE_OF_RINGS_D2.md",
    "D2_REPLAY.md",
    "d2_replay.py",
    "d2.shape.json",
)
INITIAL_PINS = (
    (
        "a895f47628b0bc7c7ee5e0392df2f79c24166f92",
        "MATHEMATICS.md",
        "bbd847461b4955a93b4533fa687cdd8724e2347c",
    ),
    (
        "a895f47628b0bc7c7ee5e0392df2f79c24166f92",
        "replay.py",
        "795566f6ec91bf68dd7ee2f77450e73afd131032",
    ),
    (
        "a895f47628b0bc7c7ee5e0392df2f79c24166f92",
        "verification.json",
        "310ffc95cb6eaf19281de52dd18d2f2884bc0f49",
    ),
    (
        CHAR_FREEZE,
        "TERNARY_CUBE_TOR_CHARACTERS.md",
        "f8edf2aac25e96434f77e1fc1681b8f22c609071",
    ),
    (CHAR_FREEZE, "tor_characters.verification.json", CHAR_BLOB),
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def blob_id(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def strict_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, "duplicate key")
            result[key] = value
        return result

    def forbidden(_):
        raise ValueError("floating/nonfinite JSON")

    return json.loads(
        raw.decode(),
        object_pairs_hook=pairs,
        parse_float=forbidden,
        parse_constant=forbidden,
    )


def frozen(commit, path, expected):
    need(
        type(commit) is str
        and len(commit) == 40
        and type(expected) is str
        and len(expected) == 40,
        "frozen source pin pending",
    )
    raw = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
    need(
        len(raw) <= MAX_BYTES and blob_id(raw) == expected,
        "frozen source blob mismatch",
    )
    return raw


@lru_cache(maxsize=16)
def compositions(n, length=3):
    need(
        type(n) is int and 0 <= n <= 4 and type(length) is int and 1 <= length <= 3,
        "composition cap",
    )
    if length == 1:
        return ((n,),)
    return tuple(
        (a, *tail) for a in range(n + 1) for tail in compositions(n - a, length - 1)
    )


def plus(*weights):
    return tuple(sum(a) for a in zip(*weights, strict=True))


@lru_cache(maxsize=5)
def source_by_weight(grade):
    need(type(grade) is int and 0 <= grade <= 4, "source grade cap")
    result = {}
    for record in itertools.product(compositions(grade), repeat=3):
        result.setdefault(plus(*record), []).append(record)
    return result


@lru_cache(maxsize=20)
def weight_chain(h, weight):
    need(
        type(h) is int and 0 <= h <= 4 and weight in WEIGHTS,
        "registered chain/weight required",
    )
    w = compositions(3)
    records = source_by_weight(4 - h)
    result = []
    for wedge in itertools.combinations(range(10), h):
        wedge_weight = plus(*(w[i] for i in wedge)) if wedge else (0, 0, 0)
        remaining = tuple(a - b for a, b in zip(weight, wedge_weight, strict=True))
        result.extend((wedge, record) for record in records.get(remaining, []))
    return tuple(result)


def character_weights(character, h, grade):
    entries = [
        row
        for row in character["complete_Tor_table"]
        if row["homological_degree"] == h and row["internal_degree"] == grade
    ]
    need(len(entries) == 1, "Tor character row coverage")
    return [
        tuple(row["weight"])
        for row in entries[0]["complete_weight_character"]
        for _ in range(row["class_traces"][0])
    ]


def shape_report(character):
    qw = [
        weight
        for weight in compositions(3)
        for _ in range(factorial(3) // prod(factorial(a) for a in weight) - 1)
    ]
    lower = character_weights(character, 1, 2)
    upper = character_weights(character, 1, 3)
    result = []
    for weight in WEIGHTS:
        dims = [len(weight_chain(h, weight)) for h in range(5)]
        source = sum(
            plus(qw[i], qw[j], b) == weight
            for i, j in itertools.combinations(range(len(qw)), 2)
            for b in lower
        )
        target = sum(plus(q, b) == weight for q in qw for b in upper)
        result.append(
            {
                "weight": list(weight),
                "W_chain_dimensions": dims,
                "Q_delta_source": source,
                "Q_delta_target": target,
                "within_registered_512_cap": max(*dims, source, target) <= MAX_BLOCK,
            }
        )
    return {
        "schema": "equivariant-pass/d2-shape/v1",
        "character_freeze": CHAR_FREEZE,
        "character_blob": CHAR_BLOB,
        "blocks": result,
        "rank_calculation_performed": False,
    }


def load_input():
    need(
        Q_FREEZE is not None and Q_PINS,
        "Q-action frozen pins pending; no differential acquisition",
    )
    q_raw = {
        name: frozen(Q_FREEZE, path, blob) for name, (path, blob) in Q_PINS.items()
    }
    old_raw = {
        name: frozen(commit, PREFIX + name, blob) for commit, name, blob in INITIAL_PINS
    }
    # Every load-bearing source is authenticated before compiling or parsing any input.
    q = types.ModuleType("authenticated_equivariant_q_action")
    q.__file__ = str(HERE / "q_action.py")
    exec(compile(q_raw["q_action.py"], q.__file__, "exec"), q.__dict__)  # noqa: S102 -- authenticated frozen definitions only
    q._deadline = time.monotonic() + 240
    first = strict_json(q_raw["q_action.verification.json"])
    q.check_record(first, first)
    primitive = strict_json(old_raw["verification.json"])
    proof = primitive.pop("proof_object_sha256")
    need(
        hashlib.sha256(canonical(primitive).encode()).hexdigest() == proof,
        "primitive digest",
    )
    character = strict_json(old_raw["tor_characters.verification.json"])
    panels = [p for p in first["panels"] if p["m"] == 3]
    need(len(panels) == 1, "ternary Q-action panel coverage")
    panel = panels[0]
    complexes = {j: q.Complex(3, j) for j in (2, 3)}
    for j, complex_ in complexes.items():
        record = next(
            p
            for p in primitive["result"]["literal_koszul_sources"]
            if (p["dimension"], p["factor_count"], p["grade"]) == (3, 3, j)
        )
        complex_.compare(record)
    homology = {}
    for j in (2, 3):
        record = next(r for r in panel["homology"] if r["h"] == 1 and r["grade"] == j)
        cycles = [
            q.decode_vector(row, len(complexes[j].chains[1]))
            for row in record["cycles"]
        ]
        weights = [tuple(w) for w in record["cycle_weights"]]
        need(len(cycles) == len(weights) == (20 if j == 2 else 65), "H1 cycle coverage")
        for cycle, weight in zip(cycles, weights, strict=True):
            need(
                not q.apply(complexes[j].maps[1], cycle),
                "imported H1 representative is not a cycle",
            )
            need(
                {complexes[j].weights[1][i] for i in cycle} == {weight},
                "imported cycle weight",
            )
        homology[j] = types.SimpleNamespace(
            complex=complexes[j],
            h=1,
            cycles=cycles,
            weights=weights,
            boundaries=complexes[j].maps[2],
        )
    qb = q.complementary_basis(3)
    encoded_q = [
        {
            "weight": list(w),
            "terms": [
                [list(word), a.numerator, a.denominator]
                for word, a in sorted(terms.items())
            ],
        }
        for w, terms in qb
    ]
    need(
        canonical(encoded_q) == canonical(panel["Q_basis"]),
        "Q complement differs from frozen source",
    )
    q.verify_action_rows(homology[2], homology[3], qb, panel["B1_action"])
    matrices, lifts = [], []
    for qi in range(17):
        rows = panel["B1_action"][qi * 20 : (qi + 1) * 20]
        matrices.append([q.decode_vector(row["image"], 65) for row in rows])
        lifts.append(
            [
                q.decode_vector(row["boundary"], len(complexes[3].chains[2]))
                for row in rows
            ]
        )
    return types.SimpleNamespace(
        q=q,
        first=first,
        character=character,
        complexes=complexes,
        homology=homology,
        qb=qb,
        matrices=matrices,
        lifts=lifts,
    )


class WeightComplex:
    """New grade-four source, enumerated only in one complete registered weight."""

    def __init__(self, q, weight):
        need(weight in WEIGHTS, "unregistered target weight")
        self.m, self.grade, self.w = 3, 4, compositions(3)
        self.chains = [weight_chain(h, weight) for h in range(5)]
        need(
            all(len(basis) <= MAX_BLOCK for basis in self.chains),
            "original target block exceeds512",
        )
        self.index = [
            {entry: i for i, entry in enumerate(basis)} for basis in self.chains
        ]
        self.weights = [[weight] * len(basis) for basis in self.chains]
        self.groups = [{weight: list(range(len(basis)))} for basis in self.chains]
        self.maps = [[]]
        matrix_hash = hashlib.sha256()
        for h in range(1, 5):
            columns = []
            for wedge, record in self.chains[h]:
                column = {}
                for place, wi in enumerate(wedge):
                    smaller = wedge[:place] + wedge[place + 1 :]
                    for word in q.orbit_words(self.w[wi]):
                        row = self.index[h - 1][smaller, q.word_product(record, word)]
                        q.add(column, {row: (-1) ** place})
                matrix_hash.update(canonical(q.encode_vector(column)).encode() + b"\n")
                columns.append(column)
            self.maps.append(columns)
        for h in range(2, 5):
            for column in self.maps[h]:
                need(
                    not q.apply(self.maps[h - 1], column),
                    "grade-four W differential does not square to zero",
                )
        ranks = []
        for h in range(1, 5):
            span = q.Span()
            for column in self.maps[h]:
                span.insert(column)
            ranks.append(span.rank)
        dimensions = list(map(len, self.chains))
        hom = [dimensions[h] - ([0] + ranks)[h] - (ranks + [0])[h] for h in range(5)]
        need(all(a >= 0 for a in hom), "target negative homology")
        self.rank_rows = [
            {
                "weight": list(weight),
                "differential_ranks": ranks,
                "homology_dimensions": hom,
            }
        ]
        self.hash = matrix_hash.hexdigest()


def q_delta(data, weight):
    qw = [w for w, _ in data.qb]
    domain = [
        (i, j, b)
        for i, j in itertools.combinations(range(17), 2)
        for b, bw in enumerate(data.homology[2].weights)
        if plus(qw[i], qw[j], bw) == weight
    ]
    target = [
        (i, b)
        for i in range(17)
        for b, bw in enumerate(data.homology[3].weights)
        if plus(qw[i], bw) == weight
    ]
    need(
        len(domain) <= MAX_BLOCK and len(target) <= MAX_BLOCK,
        "Q differential block cap",
    )
    index = {entry: i for i, entry in enumerate(target)}
    columns = []
    for i, j, b in domain:
        column = {}
        for k, a in data.matrices[i][b].items():
            data.q.add(column, {index[j, k]: a})
        for k, a in data.matrices[j][b].items():
            data.q.add(column, {index[i, k]: -a})
        columns.append(column)
    return domain, target, columns


def lift_kernel(data, domain, kernel):
    lift = {}
    for index, a in kernel.items():
        i, j, b = domain[index]
        for ci, coefficient in data.lifts[i][b].items():
            data.q.add(lift, {(j, ci): a * coefficient})
        for ci, coefficient in data.lifts[j][b].items():
            data.q.add(lift, {(i, ci): -a * coefficient})
    need(len(lift) <= 4096, "sparse lift cap")
    return lift


def source_delta(data, domain, kernel):
    out = {}
    lower, upper = data.complexes[2], data.complexes[3]
    for index, a in kernel.items():
        i, j, b = domain[index]
        cycle = data.homology[2].cycles[b]
        for remaining, multiplier, sign in ((j, i, 1), (i, j, -1)):
            product = data.q.product_vector(
                lower, upper, 1, cycle, data.qb[multiplier][1]
            )
            for row, value in product.items():
                data.q.add(out, {(remaining, row): sign * a * value})
    return out


def w_differential_of_lift(data, lift):
    out = {}
    for (remaining, index), a in lift.items():
        for row, coefficient in data.complexes[3].maps[2][index].items():
            data.q.add(out, {(remaining, row): a * coefficient})
    return out


def q_differential_of_lift(data, target, lift):
    out = {}
    for (remaining, index), a in lift.items():
        wedge, record = data.complexes[3].chains[2][index]
        for word, coefficient in data.qb[remaining][1].items():
            key = (wedge, data.q.word_product(record, word))
            need(key in target.index[2], "lift leaves registered complete weight")
            data.q.add(out, {target.index[2][key]: a * coefficient})
    return out


def encode_lift(lift):
    return [
        [qi, ci, a.numerator, a.denominator] for (qi, ci), a in sorted(lift.items())
    ]


def decode_lift(q, rows, chain_size):
    need(type(rows) is list and len(rows) <= 4096, "lift encoding cap")
    result = {}
    previous = (-1, -1)
    for row in rows:
        need(type(row) is list and len(row) == 4, "lift term shape")
        qi = q.integer(row[0], 0, 16, "lift Q index")
        ci = q.integer(row[1], 0, chain_size - 1, "lift chain index")
        need((qi, ci) > previous, "lift index order/uniqueness")
        scalar = q.decode_vector([[0, row[2], row[3]]], 1)[0]
        result[qi, ci] = scalar
        previous = (qi, ci)
    return result


def verify_d2_row(data, domain, delta, target_h, row):
    need(
        type(row) is dict
        and set(row) == {"kernel", "lift", "source_cycle", "image", "boundary"},
        "d2 row fields",
    )
    q = data.q
    target = target_h.complex
    kernel = q.decode_vector(row["kernel"], len(domain))
    need(kernel and not q.apply(delta, kernel), "not a nonzero Q-Koszul kernel vector")
    lift = decode_lift(q, row["lift"], len(data.complexes[3].chains[2]))
    need(
        w_differential_of_lift(data, lift) == source_delta(data, domain, kernel),
        "W boundary lift identity fails",
    )
    cycle = q.decode_vector(row["source_cycle"], len(target.chains[2]))
    need(
        cycle == q_differential_of_lift(data, target, lift),
        "d2 source cycle differs from delta of lift",
    )
    need(not q.apply(target.maps[2], cycle), "d2 representative is not W closed")
    image = q.decode_vector(row["image"], len(target_h.cycles))
    boundary = q.decode_vector(row["boundary"], len(target_h.boundaries))
    residual = dict(cycle)
    q.add(residual, q.apply(target_h.cycles, image), -1)
    q.add(residual, q.apply(target_h.boundaries, boundary), -1)
    need(not residual, "d2 target quotient identity fails")


def image_characters(q, target_h, columns):
    span = q.Span()
    basis = []
    for column in columns:
        if span.reduce(column)[0]:
            span.insert(column, {len(basis): Fraction(1)})
            basis.append(column)
    traces, target_traces = [span.rank], [len(target_h.cycles)]
    for permutation in ((1, 0, 2), (1, 2, 0)):
        matrix = q.homology_permutation(target_h, permutation)
        target_traces.append(sum(matrix[i].get(i, 0) for i in range(len(matrix))))
        trace = sum(
            (
                span.coordinates(q.apply(matrix, column)).get(i, 0)
                for i, column in enumerate(basis)
            ),
            Fraction(0),
        )
        traces.append(trace)
    need(
        all(Fraction(a).denominator == 1 for a in (*traces, *target_traces)),
        "nonintegral class trace",
    )
    return [int(a) for a in traces], [int(a) for a in target_traces]


def build_block(data, weight):
    q = data.q
    target = WeightComplex(q, weight)
    target_h = q.Homology(target, 2)
    domain, target_entries, delta = q_delta(data, weight)
    span = q.Span()
    kernels = []
    for i, column in enumerate(delta):
        independent, witness = span.insert(column, {i: Fraction(1)})
        if not independent:
            kernels.append(q.primitive(witness))
    need(span.rank + len(kernels) == len(domain), "Q kernel completeness")
    rows, images = [], []
    for kernel in kernels:
        lift = lift_kernel(data, domain, kernel)
        need(
            w_differential_of_lift(data, lift) == source_delta(data, domain, kernel),
            "assembled lift not a W boundary",
        )
        cycle = q_differential_of_lift(data, target, lift)
        need(
            not q.apply(target.maps[2], cycle),
            "assembled higher differential not closed",
        )
        image, boundary = target_h.reduce(cycle, weight)
        row = {
            "kernel": q.encode_vector(kernel),
            "lift": encode_lift(lift),
            "source_cycle": q.encode_vector(cycle),
            "image": q.encode_vector(image),
            "boundary": q.encode_vector(boundary),
        }
        verify_d2_row(data, domain, delta, target_h, row)
        rows.append(row)
        images.append(image)
    image_traces, target_traces = image_characters(q, target_h, images)
    target_record = next(
        r
        for r in data.character["complete_Tor_table"]
        if r["homological_degree"] == 2 and r["internal_degree"] == 4
    )
    expected = next(
        row["class_traces"]
        for row in target_record["complete_weight_character"]
        if tuple(row["weight"]) == weight
    )
    need(
        canonical(target_traces) == canonical(expected),
        "actual degree-four target differs from frozen Tor character",
    )
    q.guard(True)
    return {
        "weight": list(weight),
        "W_chain_dimensions": list(map(len, target.chains)),
        "W_differential_sha256": target.hash,
        "W_rank_and_homology": target.rank_rows[0],
        "target_H2_cycles": [q.encode_vector(v) for v in target_h.cycles],
        "Q_delta_domain": [list(entry) for entry in domain],
        "Q_delta_target": [list(entry) for entry in target_entries],
        "Q_delta_columns": [q.encode_vector(v) for v in delta],
        "Q_delta_rank": span.rank,
        "complete_Q_kernel_dimension": len(kernels),
        "d2_rows": rows,
        "d2_image_class_traces": image_traces,
        "target_H2_class_traces": target_traces,
        "surjective_at_complete_weight": image_traces[0] == target_traces[0],
    }


def build():
    data = load_input()
    shapes = shape_report(data.character)
    need(
        all(row["within_registered_512_cap"] for row in shapes["blocks"]),
        "registered full block cap refused",
    )
    blocks = [build_block(data, weight) for weight in WEIGHTS]
    surjective = all(row["surjective_at_complete_weight"] for row in blocks)
    result = {
        "schema": "equivariant-pass/source-d2/v1",
        "Q_action_freeze": Q_FREEZE,
        "Q_action_pins": {name: list(pin) for name, pin in Q_PINS.items()},
        "Q_action_proof_sha256": data.first["proof_sha256"],
        "primitive_pins": [list(pin) for pin in INITIAL_PINS],
        "owned_sha256_lf": {
            name: hashlib.sha256(
                (HERE / name).read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for name in OWNED
        },
        "test_sha256_lf": hashlib.sha256(
            TEST.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "complete_registered_weights": [list(w) for w in WEIGHTS],
        "shape": shapes,
        "blocks": blocks,
        "status": "VERIFIED_SURJECTIVE_D2"
        if surjective
        else "VERIFIED_PARTIAL_D2_IMAGE",
        "global_d2_rank": 65 if surjective else None,
        "global_rank_uses_highest_weight_quotient_theorem": surjective,
        "ambient_Tor_vanishing_assumed": False,
    }
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "artifact byte cap")
    return result, data.q._peak_working


def check_record(candidate, expected):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str,
        "d2 artifact shape",
    )
    body = dict(candidate)
    claimed = body.pop("proof_sha256")
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest() == claimed,
        "d2 body digest",
    )
    need(
        canonical(candidate) == canonical(expected),
        "typed complete source-d2 replay mismatch",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--shape", action="store_true")
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.shape:
        character = strict_json(
            frozen(CHAR_FREEZE, PREFIX + "tor_characters.verification.json", CHAR_BLOB)
        )
        record = shape_report(character)
        SHAPE.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(json.dumps(record))
        return
    started = time.monotonic()
    record, peak = build()
    if args.write:
        text = json.dumps(record, sort_keys=True, indent=2) + "\n"
        need(len(text.encode()) <= MAX_BYTES, "pretty artifact byte cap")
        FIXTURE.write_text(text, encoding="utf-8", newline="\n")
    else:
        need(FIXTURE.exists(), "missing d2 artifact")
        check_record(strict_json(FIXTURE.read_bytes()), record)
    print(
        json.dumps(
            {
                "status": record["status"],
                "proof_sha256": record["proof_sha256"],
                "elapsed_ms": round(1000 * (time.monotonic() - started)),
                "peak_working_bytes": peak,
                "weight_ranks": [
                    [b["d2_image_class_traces"][0], b["target_H2_class_traces"][0]]
                    for b in record["blocks"]
                ],
                "global_d2_rank": record["global_d2_rank"],
            }
        )
    )


if __name__ == "__main__":
    main()
