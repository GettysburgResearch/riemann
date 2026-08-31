"""Source-derived complementary-variable action on Chow Tor, over Q.

No executable predecessor import. All original Koszul maps, cycle representatives,
products and boundary witnesses are reconstructed in bounded exact weight blocks.
"""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import itertools
import json
import os
import subprocess
import time
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
TEST = ROOT / "tests/test_equivariant_pass_q_action.py"
FIXTURE = HERE / "q_action.verification.json"
OWNED = (
    "PREREGISTRATION.md",
    "Q_ACTION_MATHEMATICS.md",
    "Q_ACTION_REPLAY.md",
    "q_action.py",
    "sources/PR782_THEOREM_I.md",
)
PINS = (
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
        "08147ccecfe684af76a8417861fcccda61abe601",
        "TERNARY_CUBE_TOR_CHARACTERS.md",
        "f8edf2aac25e96434f77e1fc1681b8f22c609071",
    ),
    (
        "08147ccecfe684af76a8417861fcccda61abe601",
        "tor_characters.verification.json",
        "4ea01d1d6fbb0383e31f03f060a8511dd3c7a1e4",
    ),
)
EXTERNAL = {
    "commit": "552fe0b78fd96b02fe5836269e6795a992c935be",
    "path": "standalone/2026-08-31-segre-chow-equivariant-synthesis/THEOREM_I.md",
    "blob": "749cc53453e4842ca010c4028d2a9b35024e3208",
}
MAX_BLOCK = 512
MAX_CHAIN = 5000
MAX_BITS = 4096
MAX_BYTES = 16 * 1024 * 1024
MAX_SECONDS = 240
MAX_WORKING = 1024**3
_deadline = None
_guard_count = 0
_peak_working = 0


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, name="integer"):
    need(type(value) is int and low <= value <= high, f"{name} outside cap")
    return value


def rational(value):
    need(type(value) in (int, Fraction), "exact rational required")
    value = Fraction(value)
    need(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= MAX_BITS,
        "rational bit cap",
    )
    return value


def memory_bytes():
    if os.name != "nt":
        return 0

    class Counters(ctypes.Structure):
        _fields_ = [("cb", ctypes.c_ulong), ("faults", ctypes.c_ulong)] + [
            (name, ctypes.c_size_t)
            for name in (
                "peak",
                "working",
                "peak_paged",
                "paged",
                "peak_nonpaged",
                "nonpaged",
                "pagefile",
                "peak_pagefile",
            )
        ]

    kernel = ctypes.windll.kernel32
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    query = ctypes.windll.psapi.GetProcessMemoryInfo
    query.argtypes = [ctypes.c_void_p, ctypes.POINTER(Counters), ctypes.c_ulong]
    data = Counters()
    data.cb = ctypes.sizeof(data)
    need(
        query(kernel.GetCurrentProcess(), ctypes.byref(data), data.cb),
        "working-set query failed",
    )
    return int(data.working)


def guard(force=False):
    global _guard_count, _peak_working
    _guard_count += 1
    if force or _guard_count % 1024 == 0:
        if _deadline is not None:
            need(time.monotonic() <= _deadline, "240-second acquisition cap")
        working = memory_bytes()
        _peak_working = max(_peak_working, working)
        need(working <= MAX_WORKING, "one-GiB working-set cap")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def forbidden(_):
        raise ValueError("floating or nonfinite JSON number")

    return json.loads(
        raw.decode("utf-8"),
        object_pairs_hook=pairs,
        parse_float=forbidden,
        parse_constant=forbidden,
    )


def blob_id(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def authenticate():
    raw = {}
    for commit, name, expected in PINS:
        data = subprocess.check_output(
            ["git", "show", f"{commit}:{PREFIX}{name}"], cwd=ROOT
        )
        need(
            len(data) <= MAX_BYTES and blob_id(data) == expected,
            f"frozen source mismatch: {name}",
        )
        raw[name] = data
    capture = (HERE / "sources/PR782_THEOREM_I.md").read_bytes().replace(b"\r\n", b"\n")
    need(blob_id(capture) == EXTERNAL["blob"], "proposed external proof mismatch")
    # All five frozen objects and the external capture are authenticated before parsing.
    primitive = strict_json(raw["verification.json"])
    proof = primitive.pop("proof_object_sha256")
    need(
        hashlib.sha256(canonical(primitive).encode()).hexdigest() == proof,
        "primitive body digest",
    )
    characters = strict_json(raw["tor_characters.verification.json"])
    need(
        characters["schema"] == "segre-hadamard-ternary-cube-Tor-characters/v1",
        "Tor character schema",
    )
    return primitive["result"]["literal_koszul_sources"], characters


@lru_cache(maxsize=128)
def compositions(n, length=3):
    integer(n, 0, 9, "composition degree")
    integer(length, 1, 3, "composition length")
    if length == 1:
        return ((n,),)
    return tuple(
        (a, *tail) for a in range(n + 1) for tail in compositions(n - a, length - 1)
    )


def add_weight(*weights):
    return tuple(sum(parts) for parts in zip(*weights, strict=True))


@lru_cache(maxsize=16)
def source_basis(m, grade):
    integer(m, 2, 3, "factor count")
    integer(grade, 0, 3, "source grade")
    basis = tuple(itertools.product(compositions(grade), repeat=m))
    need(len(basis) <= MAX_CHAIN, "source basis cap")
    return basis


@lru_cache(maxsize=32)
def orbit_words(content):
    return tuple(
        word
        for word in itertools.product(range(3), repeat=sum(content))
        if tuple(word.count(i) for i in range(3)) == content
    )


def word_product(record, word):
    need(len(record) == len(word), "source product arity")
    out = []
    for row, letter in zip(record, word, strict=True):
        new = list(row)
        new[letter] += 1
        out.append(tuple(new))
    return tuple(out)


def add(target, source, factor=1):
    factor = rational(factor)
    for key, value in source.items():
        new = rational(target.get(key, 0) + factor * value)
        if new:
            target[key] = new
        else:
            target.pop(key, None)
    guard()


def primitive(vector):
    if not vector:
        return {}
    denominator = lcm(*(a.denominator for a in vector.values()))
    need(denominator.bit_length() <= MAX_BITS, "primitive denominator cap")
    values = {i: int(a * denominator) for i, a in vector.items()}
    divisor = gcd(*values.values())
    sign = 1 if values[max(values)] > 0 else -1
    return {i: rational(sign * a // divisor) for i, a in values.items()}


class Span:
    """Exact column span, retaining original generating-column coordinates."""

    def __init__(self):
        self.pivots = {}

    def reduce(self, vector, witness=None):
        vector = {i: rational(a) for i, a in vector.items() if a}
        witness = dict(witness or {})
        while vector:
            pivot = min(vector)
            if pivot not in self.pivots:
                break
            coefficient = vector[pivot]
            column, record = self.pivots[pivot]
            add(vector, column, -coefficient)
            add(witness, record, -coefficient)
        return vector, witness

    def insert(self, vector, witness=None):
        vector, witness = self.reduce(vector, witness)
        if not vector:
            return False, witness
        need(len(self.pivots) < MAX_BLOCK, "span rank cap")
        pivot = min(vector)
        a = vector[pivot]
        self.pivots[pivot] = (
            {i: rational(v / a) for i, v in vector.items()},
            {i: rational(v / a) for i, v in witness.items()},
        )
        return True, witness

    def coordinates(self, vector):
        residual, witness = self.reduce(vector)
        need(not residual, "vector outside certified span")
        return {i: -a for i, a in witness.items()}

    @property
    def rank(self):
        return len(self.pivots)


def apply(columns, vector):
    out = {}
    for index, coefficient in vector.items():
        integer(index, 0, len(columns) - 1, "matrix index")
        add(out, columns[index], coefficient)
    return out


def encode_vector(vector):
    return [
        [i, a.numerator, a.denominator]
        for i, a in sorted((i, rational(a)) for i, a in vector.items())
        if a
    ]


def decode_vector(rows, dimension):
    need(type(rows) is list and len(rows) <= dimension, "sparse vector shape")
    out = {}
    previous = -1
    for row in rows:
        need(type(row) is list and len(row) == 3, "sparse entry shape")
        index = integer(row[0], 0, dimension - 1, "sparse index")
        need(index > previous, "sparse indices must be unique and sorted")
        numerator = row[1]
        denominator = row[2]
        need(
            type(numerator) is int
            and numerator != 0
            and type(denominator) is int
            and denominator > 0,
            "sparse exact number",
        )
        value = rational(Fraction(numerator, denominator))
        need(
            value.numerator == numerator and value.denominator == denominator,
            "unreduced rational",
        )
        out[index] = value
        previous = index
    return out


class Complex:
    def __init__(self, m, grade):
        integer(m, 2, 3, "factor count")
        integer(grade, 1, 3, "Koszul grade")
        self.m, self.grade = m, grade
        self.w = compositions(m)
        total = sum(
            comb(len(self.w), h) * comb(grade - h + 2, 2) ** m for h in range(grade + 1)
        )
        need(total <= MAX_CHAIN, "total chain cap")
        self.chains, self.index, self.weights, self.groups = [], [], [], []
        for h in range(grade + 1):
            basis = tuple(
                (wedge, record)
                for wedge in itertools.combinations(range(len(self.w)), h)
                for record in source_basis(m, grade - h)
            )
            self.chains.append(basis)
            self.index.append({entry: i for i, entry in enumerate(basis)})
            weights = [
                add_weight(*(tuple(self.w[a] for a in wedge) + record))
                for wedge, record in basis
            ]
            self.weights.append(weights)
            groups = defaultdict(list)
            for i, weight in enumerate(weights):
                groups[weight].append(i)
            need(
                all(len(indices) <= MAX_BLOCK for indices in groups.values()),
                "chain weight-block cap",
            )
            self.groups.append(groups)
        self.maps = [[]]
        digest = hashlib.sha256()
        for h in range(1, grade + 1):
            columns = []
            for wedge, record in self.chains[h]:
                column = Counter()
                for place, wi in enumerate(wedge):
                    smaller = wedge[:place] + wedge[place + 1 :]
                    for word in orbit_words(self.w[wi]):
                        row = self.index[h - 1][smaller, word_product(record, word)]
                        column[row] += (-1) ** place
                column = {i: a for i, a in column.items() if a}
                digest.update(
                    json.dumps(sorted(column.items()), separators=(",", ":")).encode()
                    + b"\n"
                )
                columns.append(column)
            self.maps.append(columns)
        for h in range(2, grade + 1):
            for column in self.maps[h]:
                need(not apply(self.maps[h - 1], column), "literal Koszul d squared")
        self.hash = digest.hexdigest()
        self.rank_rows = []
        for weight in sorted(self.groups[0]):
            ranks = []
            for h in range(1, grade + 1):
                span = Span()
                for i in self.groups[h].get(weight, []):
                    span.insert(self.maps[h][i])
                ranks.append(span.rank)
            dimensions = [len(groups.get(weight, [])) for groups in self.groups]
            homology = [
                dimensions[h] - ([0] + ranks)[h] - (ranks + [0])[h]
                for h in range(grade + 1)
            ]
            need(all(n >= 0 for n in homology), "negative homology dimension")
            self.rank_rows.append(
                {
                    "weight": list(weight),
                    "differential_ranks": ranks,
                    "homology_dimensions": homology,
                }
            )
        guard(True)

    def compare(self, source):
        need(
            source["dimension"] == 3
            and source["factor_count"] == self.m
            and source["grade"] == self.grade,
            "primitive panel identity",
        )
        need(
            source["literal_differential_sha256"] == self.hash,
            "literal differential hash differs from frozen primitive",
        )
        expected = [
            {
                "weight": row["weight"],
                "differential_ranks": row["differential_ranks"],
                "homology_dimensions": [h["identity"] for h in row["homology"]],
            }
            for row in source["homology_weight_rows"]
        ]
        need(
            canonical(expected) == canonical(self.rank_rows),
            "full primitive weight/rank mismatch",
        )

    def summary(self):
        return {
            "m": self.m,
            "grade": self.grade,
            "chain_dimensions": list(map(len, self.chains)),
            "literal_differential_sha256": self.hash,
            "weight_rows": self.rank_rows,
        }


class Homology:
    def __init__(self, complex_, h):
        integer(h, 0, complex_.grade, "homological degree")
        self.complex, self.h = complex_, h
        self.cycles, self.weights, self.spaces = [], [], {}
        self.boundaries = complex_.maps[h + 1] if h < complex_.grade else []
        self.offset = len(self.boundaries)
        for weight in sorted(complex_.groups[h]):
            space = Span()
            if h < complex_.grade:
                for col in complex_.groups[h + 1].get(weight, []):
                    space.insert(self.boundaries[col], {col: Fraction(1)})
            incoming_rank = space.rank
            image = Span()
            for col in complex_.groups[h][weight]:
                if h:
                    independent, witness = image.insert(
                        complex_.maps[h][col], {col: Fraction(1)}
                    )
                    if independent:
                        continue
                    cycle = primitive(witness)
                else:
                    cycle = {col: Fraction(1)}
                need(
                    not h or not apply(complex_.maps[h], cycle),
                    "selected cycle not closed",
                )
                if space.reduce(cycle)[0]:
                    label = self.offset + len(self.cycles)
                    added, _ = space.insert(cycle, {label: Fraction(1)})
                    need(added, "homology selection lost independence")
                    self.cycles.append(cycle)
                    self.weights.append(weight)
            need(
                space.rank + image.rank == len(complex_.groups[h][weight]),
                "kernel/boundary coverage",
            )
            predicted = next(
                row["homology_dimensions"][h]
                for row in complex_.rank_rows
                if tuple(row["weight"]) == weight
            )
            need(space.rank - incoming_rank == predicted, "homology quotient dimension")
            self.spaces[weight] = space

    def reduce(self, vector, weight=None):
        if not vector:
            return {}, {}
        actual = {self.complex.weights[self.h][i] for i in vector}
        need(len(actual) == 1, "inhomogeneous source vector")
        actual = next(iter(actual))
        need(weight is None or actual == weight, "source weight mismatch")
        coords = self.spaces[actual].coordinates(vector)
        homology = {i - self.offset: a for i, a in coords.items() if i >= self.offset}
        boundary = {i: a for i, a in coords.items() if i < self.offset}
        residual = dict(vector)
        add(residual, apply(self.cycles, homology), -1)
        if boundary:
            add(residual, apply(self.boundaries, boundary), -1)
        need(not residual, "boundary identity failed")
        return homology, boundary

    def record(self):
        return {
            "h": self.h,
            "grade": self.complex.grade,
            "dimension": len(self.cycles),
            "cycle_weights": [list(w) for w in self.weights],
            "cycles": [encode_vector(c) for c in self.cycles],
        }


def complementary_basis(m):
    integer(m, 2, 3, "factor count")
    result = []
    for content in compositions(m):
        words = orbit_words(content)
        for word in words[1:]:
            terms = {other: Fraction(-1, len(words)) for other in words}
            terms[word] += 1
            need(sum(terms.values()) == 0, "Q symmetrizer kernel")
            result.append((content, terms))
    need(len(result) == 3**m - comb(m + 2, 2), "complement dimension")
    return result


def product_vector(source, target, h, vector, terms):
    need(
        source.m == target.m and target.grade == source.grade + 1,
        "chain product degree",
    )
    out = {}
    for index, a in vector.items():
        wedge, record = source.chains[h][index]
        for word, b in terms.items():
            row = target.index[h][wedge, word_product(record, word)]
            add(out, {row: a * b})
    return out


def action(source_h, target_h, q_basis):
    rows, matrices = [], []
    for qi, (qw, terms) in enumerate(q_basis):
        columns = []
        for ci, cycle in enumerate(source_h.cycles):
            product = product_vector(
                source_h.complex, target_h.complex, source_h.h, cycle, terms
            )
            if source_h.h:
                need(
                    not apply(target_h.complex.maps[source_h.h], product),
                    "multiplication failed to preserve cycles",
                )
            image, boundary = target_h.reduce(
                product, add_weight(qw, source_h.weights[ci])
            )
            rows.append(
                {
                    "q": qi,
                    "cycle": ci,
                    "image": encode_vector(image),
                    "boundary": encode_vector(boundary),
                }
            )
            columns.append(image)
        matrices.append(columns)
    return rows, matrices


def verify_action_rows(source_h, target_h, q_basis, rows):
    need(
        type(rows) is list and len(rows) == len(q_basis) * len(source_h.cycles),
        "complete action coverage",
    )
    for n, row in enumerate(rows):
        need(
            type(row) is dict and set(row) == {"q", "cycle", "image", "boundary"},
            "action record fields",
        )
        qi, ci = divmod(n, len(source_h.cycles))
        need(
            type(row["q"]) is int
            and type(row["cycle"]) is int
            and row["q"] == qi
            and row["cycle"] == ci,
            "action address/coverage",
        )
        image = decode_vector(row["image"], len(target_h.cycles))
        boundary = decode_vector(row["boundary"], len(target_h.boundaries))
        residual = product_vector(
            source_h.complex,
            target_h.complex,
            source_h.h,
            source_h.cycles[ci],
            q_basis[qi][1],
        )
        add(residual, apply(target_h.cycles, image), -1)
        add(residual, apply(target_h.boundaries, boundary), -1)
        need(not residual, "reported action is not the original source identity")


def permute_record(record, permutation):
    inverse = [0] * len(permutation)
    for old, new in enumerate(permutation):
        inverse[new] = old
    return tuple(record[i] for i in inverse)


def homology_permutation(homology, permutation):
    complex_ = homology.complex
    columns = []
    for cycle in homology.cycles:
        moved = {}
        for index, value in cycle.items():
            wedge, record = complex_.chains[homology.h][index]
            row = complex_.index[homology.h][wedge, permute_record(record, permutation)]
            add(moved, {row: value})
        coordinates, _ = homology.reduce(moved)
        columns.append(coordinates)
    return columns


def q_permutation(q_basis, permutation):
    word_basis = tuple(itertools.product(range(3), repeat=len(permutation)))
    positions = {word: i for i, word in enumerate(word_basis)}
    space = Span()
    for i, (_, terms) in enumerate(q_basis):
        added, _ = space.insert(
            {positions[word]: a for word, a in terms.items()}, {i: Fraction(1)}
        )
        need(added, "Q basis dependence")
    return [
        space.coordinates(
            {
                positions[permute_record(word, permutation)]: a
                for word, a in terms.items()
            }
        )
        for _, terms in q_basis
    ]


def equivariance(source_h, target_h, q_basis, matrices, permutation):
    qs = q_permutation(q_basis, permutation)
    ss = homology_permutation(source_h, permutation)
    ts = homology_permutation(target_h, permutation)
    for qi in range(len(q_basis)):
        for ci in range(len(source_h.cycles)):
            left = apply(ts, matrices[qi][ci])
            right = {}
            for qj, a in qs[qi].items():
                add(right, apply(matrices[qj], ss[ci]), a)
            need(left == right, "factor-permutation equivariance failed")
    return {
        "permutation": list(permutation),
        "Q": [encode_vector(v) for v in qs],
        "source_homology": [encode_vector(v) for v in ss],
        "target_homology": [encode_vector(v) for v in ts],
        "verified": True,
    }


def w_homotopies(source_h, target_h):
    source, target = source_h.complex, target_h.complex
    records = []
    for wi, content in enumerate(source.w):
        for ci, cycle in enumerate(source_h.cycles):
            homotopy = {}
            for index, a in cycle.items():
                wedge, record = source.chains[source_h.h][index]
                if wi not in wedge:
                    place = sum(index_ < wi for index_ in wedge)
                    new = tuple(sorted((*wedge, wi)))
                    row = target.index[source_h.h + 1][new, record]
                    add(homotopy, {row: (-1) ** place * a})
            product = product_vector(
                source,
                target,
                source_h.h,
                cycle,
                {word: 1 for word in orbit_words(content)},
            )
            need(
                apply(target.maps[source_h.h + 1], homotopy) == product,
                "W null-homotopy sign/source failure",
            )
            records.append({"w": wi, "cycle": ci, "homotopy": encode_vector(homotopy)})
    return records


def action_rank(matrices):
    span = Span()
    for columns in matrices:
        for column in columns:
            span.insert(column)
    return span.rank


def q_annihilator_dimension(matrices):
    target_count = (
        max(
            (i for columns in matrices for column in columns for i in column),
            default=-1,
        )
        + 1
    )
    vectors = [
        {
            j * target_count + i: a
            for j, column in enumerate(columns)
            for i, a in column.items()
        }
        for columns in matrices
    ]
    # Exact positive Gram rank equals column rank over Q; elimination has <=17 rows.
    span = Span()
    for vector in vectors:
        span.insert(
            {
                i: sum((a * other.get(k, 0) for k, a in vector.items()), Fraction(0))
                for i, other in enumerate(vectors)
            }
        )
    return len(matrices) - span.rank


def build_panel(m, frozen_panels):
    complexes = {j: Complex(m, j) for j in (1, 2, 3)}
    for j, complex_ in complexes.items():
        matching = [
            p
            for p in frozen_panels
            if p["dimension"] == 3 and p["factor_count"] == m and p["grade"] == j
        ]
        need(len(matching) == 1, "primitive panel coverage")
        complex_.compare(matching[0])
    h0 = {j: Homology(complexes[j], 0) for j in (1, 2, 3)}
    h1 = {j: Homology(complexes[j], 1) for j in (2, 3)}
    expected0, expected1 = ((3, 0, 0), (3, 1)) if m == 2 else ((17, 11, 0), (20, 65))
    need(
        tuple(len(h0[j].cycles) for j in (1, 2, 3)) == expected0,
        "calibration B0 dimensions",
    )
    need(
        tuple(len(h1[j].cycles) for j in (2, 3)) == expected1,
        "calibration B1 dimensions",
    )
    qb = complementary_basis(m)
    q_to_h0 = []
    q_source = []
    zero_record = source_basis(m, 0)[0]
    for _, terms in qb:
        vector = {
            complexes[1].index[0][(), word_product(zero_record, word)]: a
            for word, a in terms.items()
        }
        q_source.append(vector)
        q_to_h0.append(h0[1].reduce(vector)[0])
    iso = Span()
    for column in q_to_h0:
        iso.insert(column)
    need(iso.rank == len(qb), "Q to degree-one quotient not isomorphism")
    a0_rows, a0 = action(h0[1], h0[2], qb)
    top0_rows, top0 = action(h0[2], h0[3], qb)
    a1_rows, a1 = action(h1[2], h1[3], qb)
    verify_action_rows(h0[1], h0[2], qb, a0_rows)
    verify_action_rows(h0[2], h0[3], qb, top0_rows)
    verify_action_rows(h1[2], h1[3], qb, a1_rows)
    need(
        not any(column for columns in top0 for column in columns),
        "top B0 is not annihilated",
    )
    products = []
    for i in range(len(qb)):
        for j in range(i, len(qb)):
            left = apply(a0[i], q_to_h0[j])
            right = apply(a0[j], q_to_h0[i])
            need(left == right, "quotient multiplication is not commutative")
            source_product_ = product_vector(
                complexes[1], complexes[2], 0, q_source[j], qb[i][1]
            )
            actual, boundary = h0[2].reduce(source_product_)
            need(actual == left, "quotient product differs from source")
            products.append(
                {
                    "left": i,
                    "right": j,
                    "image": encode_vector(actual),
                    "boundary": encode_vector(boundary),
                }
            )
    permutations = [(1, 0)] if m == 2 else [(1, 0, 2), (1, 2, 0)]
    symmetry = [
        {
            "B0": equivariance(h0[1], h0[2], qb, a0, p),
            "B1": equivariance(h1[2], h1[3], qb, a1, p),
        }
        for p in permutations
    ]
    return {
        "m": m,
        "complexes": [complexes[j].summary() for j in (1, 2, 3)],
        "Q_basis": [
            {
                "weight": list(weight),
                "terms": [
                    [list(word), a.numerator, a.denominator]
                    for word, a in sorted(terms.items())
                ],
            }
            for weight, terms in qb
        ],
        "homology": [h0[j].record() for j in (1, 2, 3)]
        + [h1[j].record() for j in (2, 3)],
        "Q_to_B01": [encode_vector(v) for v in q_to_h0],
        "B0_action": a0_rows,
        "B02_annihilation": top0_rows,
        "B1_action": a1_rows,
        "symmetric_Q_products": products,
        "W_null_homotopies": w_homotopies(h1[2], h1[3]),
        "factor_equivariance": symmetry,
        "B0_positive_action_rank": action_rank(a0),
        "B1_action_rank": action_rank(a1),
        "Q_annihilator_on_B01_dimension": q_annihilator_dimension(a0),
        "Q_annihilator_on_B12_dimension": q_annihilator_dimension(a1),
        "all_reported_actions_have_source_boundary_witnesses": True,
        "E2_page_computed": False,
        "higher_differentials_computed": False,
    }


def build():
    global _deadline
    _deadline = time.monotonic() + MAX_SECONDS
    guard(True)
    primitive_panels, characters = authenticate()
    need(
        characters["total_free_ranks"] == [29, 85, 85, 29],
        "frozen character rank contract",
    )
    result = {
        "schema": "five-hour-equivariant-pass/Q-action/v1",
        "source_pins": [list(pin) for pin in PINS],
        "proposed_external_proof": EXTERNAL,
        "owned_sha256_lf": {
            name: hashlib.sha256(
                (HERE / name).read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for name in OWNED
        },
        "test_sha256_lf": hashlib.sha256(
            TEST.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "caps": {
            "source_grade": 3,
            "total_chain": MAX_CHAIN,
            "block": MAX_BLOCK,
            "bits": MAX_BITS,
            "artifact_bytes": MAX_BYTES,
            "working_set_bytes": MAX_WORKING,
            "seconds": MAX_SECONDS,
        },
        "panels": [build_panel(m, primitive_panels) for m in (2, 3)],
        "scope": "Actual complementary-variable module action; no ambient Tor or higher-differential inference.",
    }
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "artifact byte cap")
    return result


def check_record(candidate, expected):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str,
        "proof record shape",
    )
    body = dict(candidate)
    claimed = body.pop("proof_sha256")
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest() == claimed,
        "proof body digest mismatch",
    )
    need(
        canonical(candidate) == canonical(expected),
        "typed fresh source replay mismatch",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    payload = build()
    if args.write:
        data = json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n"
        need(len(data.encode()) <= MAX_BYTES, "pretty artifact byte cap")
        FIXTURE.write_text(data, encoding="utf-8", newline="\n")
    else:
        need(FIXTURE.exists(), "missing verification artifact")
        check_record(strict_json(FIXTURE.read_bytes()), payload)
    print(
        json.dumps(
            {
                "status": "PASS",
                "proof_sha256": payload["proof_sha256"],
                "elapsed_ms": round(1000 * (time.monotonic() - started)),
                "peak_working_bytes": _peak_working,
                "B1_action_ranks": [p["B1_action_rank"] for p in payload["panels"]],
            }
        )
    )


if __name__ == "__main__":
    main()
