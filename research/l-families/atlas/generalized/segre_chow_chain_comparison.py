"""Literal finite Koszul comparison; construction precedes character checks."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path

MAX_BITS = 4096
MAX_ROWS = 1152
MAX_COLS = 2048
MAX_CELLS = 100000
MAX_BYTES = 8 * 1024 * 1024
MAX_DEPTH = 48
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "segre_chow_chain_comparison"
NOTE = HERE / "SEGRE_CHOW_CHAIN_COMPARISON.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
PINS = [
    (
        "552fe0b78fd96b02fe5836269e6795a992c935be",
        "standalone/2026-08-31-segre-chow-equivariant-synthesis/THEOREM_I.md",
        "749cc53453e4842ca010c4028d2a9b35024e3208",
        "de9ca912fe206717db50ac6b27f2a56b686b33008099d78e3cf82d60c2004c59",
    ),
    (
        "552fe0b78fd96b02fe5836269e6795a992c935be",
        "standalone/2026-08-31-segre-chow-equivariant-synthesis/THEOREM_II.md",
        "ee2f721f855e6024efd48495562ed5b9a7d4e58c",
        "c39ef11fcbe4a583ec77a04467c82150f34cb6972c414a609334cfa4e898c740",
    ),
    (
        "f36576faf7853a56bd1f64edd29c4df662cae849",
        "research/l-families/atlas/generalized/segre-hadamard-source/MATHEMATICS.md",
        "bbd847461b4955a93b4533fa687cdd8724e2347c",
        "de7d8d8507a47fdd35d04bfdeee430a64e81c054ad8a8c61cb303d70a0d17e6a",
    ),
    (
        "f36576faf7853a56bd1f64edd29c4df662cae849",
        "research/l-families/atlas/generalized/segre-hadamard-source/TERNARY_CUBE_TOR_CHARACTERS.md",
        "f8edf2aac25e96434f77e1fc1681b8f22c609071",
        "32ef7f6db2ff7ef022f0881e44de965246637bdf586f64b8c4736586855d957e",
    ),
    (
        "f36576faf7853a56bd1f64edd29c4df662cae849",
        "research/l-families/atlas/generalized/segre-hadamard-source/COMPLETED_TERNARY_CUBE_RESOLUTION.md",
        "7301d9cbc50bde470fb3551a6262cf62378b523c",
        "22e4af08206b61c1baa2182f99164ba8696165a255187ff81666b559706fd2b7",
    ),
    (
        "4a317ea5c9d7aa016fba58a1d74746e437329ec7",
        "research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md",
        "acc3a0382f3ad919037b156749b4a07a971b429a",
        "7dd4af9c9f14c73413d7a233cf64d7b608d94b60af334d08e1a0e0561a5f94a2",
    ),
    (
        "acd91a621244872d49e0e4dfde76775879eadfc1",
        "research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE_AUDIT_4A317EA5.md",
        "9917525809b5c22627d216e8180a4ea29ae32b0c",
        "b5abd8d8c788563a241242e4b83d70640643c1b1898df5eb0b358b5e79191ae7",
    ),
    (
        "28c6d95ccf6842ec415c440c77a8036a187f176c",
        "research/l-families/atlas/generalized/SEGRE_CHOW_CHAIN_COMPARISON.md",
        "f07e6567f65aec5fa2a6db45cda667e6a4023d64",
        "ea80284648d9f63743f0146aeeb6d4b0cc5335ee12c08ff02ffc8ae0b540aeb9",
    ),
    (
        "6416a3c301c22fb674ef12947568da0ad341f801",
        "research/l-families/atlas/generalized/SEGRE_CHOW_CHAIN_COMPARISON.md",
        "a4234ed7bd3696867b092c83655d6c8be3e41c8c",
        "98415cdc702dbeba64559b18df91d9583613b5dea0000cc421e7a6801d3bc3c2",
    ),
    (
        "e3a9b2c56029fa41e4cbceb1fbf64de4e20c75b4",
        "research/l-families/atlas/generalized/SEGRE_CHOW_CHAIN_COMPARISON.md",
        "6a9bd38ae748762d616efaecf7c5fe4d7596b640",
        "50ec7cf8cacc7728f28a2a9a717734381f63967fdfb7514b752a7e305a3bf7a0",
    ),
]


def need(ok, message):
    if not ok:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "integer type/range")
    return value


def rat(value):
    need(type(value) in (int, Fraction), "rational type")
    if type(value) is int:
        value = Fraction(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= MAX_BITS,
        "rational bit cap",
    )
    return value


def axpy(target, source, scalar=1):
    scalar = rat(scalar)
    for key, value in source.items():
        z = rat(target.get(key, 0) + scalar * rat(value))
        if z:
            target[key] = z
        else:
            target.pop(key, None)
    return target


class Span:
    """Exact echelon basis with coordinates in its original independent columns."""

    def __init__(self, rows):
        integer(rows, 0, MAX_ROWS)
        self.rows = rows
        self.pivots = {}
        self.columns = []

    def reduce(self, vector):
        v = {}
        for i, x in vector.items():
            i, x = integer(i, 0, self.rows - 1), rat(x)
            if x:
                v[i] = x
        coords = {}
        for pivot in sorted(self.pivots):
            if not v:
                break
            if pivot in v:
                col, expr = self.pivots[pivot]
                scalar = v[pivot]
                axpy(v, col, -scalar)
                axpy(coords, expr, scalar)
        return v, coords

    def add(self, vector):
        residual, coords = self.reduce(vector)
        if not residual:
            return False
        need(len(self.columns) < MAX_COLS, "basis column cap")
        index = len(self.columns)
        self.columns.append(dict(vector))
        pivot = min(residual)
        scalar = residual[pivot]
        expr = {index: Fraction(1)}
        axpy(expr, coords, -1)
        self.pivots[pivot] = (
            {i: rat(x / scalar) for i, x in residual.items()},
            {i: rat(x / scalar) for i, x in expr.items()},
        )
        return True


def kernel(columns, rows):
    need(len(columns) <= MAX_COLS, "kernel column cap")
    space = Span(rows)
    independent = []
    answer = []
    for i, column in enumerate(columns):
        residual, coords = space.reduce(column)
        if residual:
            need(space.add(column), "independent column")
            independent.append(i)
        else:
            v = {i: Fraction(1)}
            for j, x in coords.items():
                axpy(v, {independent[j]: x}, -1)
            answer.append(v)
    return answer, len(independent)


def apply_columns(columns, vector):
    out = {}
    for i, x in vector.items():
        integer(i, 0, len(columns) - 1)
        axpy(out, columns[i], x)
    return out


def add_weight(a, b):
    return tuple(x + y for x, y in zip(a, b))


def wedge_order(items):
    if len(set(items)) != len(items):
        return None, 0
    inversions = sum(a > b for i, a in enumerate(items) for b in items[i + 1 :])
    return tuple(sorted(items)), (-1) ** inversions


class Homology:
    def __init__(self, basis, outgoing, target_rows, incoming):
        self.basis = basis
        self.space = Span(len(basis))
        self.outgoing = outgoing
        self.boundary_preimages = []
        for i, v in enumerate(incoming):
            need(
                not apply_columns(outgoing, v),
                "consecutive maps do not compose to zero",
            )
            if self.space.add(v):
                self.boundary_preimages.append(i)
        self.boundary_rank = len(self.space.columns)
        cycles, self.outgoing_rank = kernel(outgoing, target_rows)
        self.reps = []
        for cycle in cycles:
            if self.space.add(cycle):
                self.reps.append(cycle)
        need(
            len(self.reps) == len(basis) - self.outgoing_rank - self.boundary_rank,
            "homology dimension ledger",
        )

    def coordinates(self, vector):
        need(not apply_columns(self.outgoing, vector), "homology input is not a cycle")
        residue, coords = self.space.reduce(vector)
        need(not residue, "cycle outside complete kernel basis")
        return {
            i - self.boundary_rank: x
            for i, x in coords.items()
            if i >= self.boundary_rank and x
        }

    def boundary_lift(self, vector):
        residue, coords = self.space.reduce(vector)
        need(
            not residue and all(i < self.boundary_rank for i in coords),
            "requested lift is not a boundary",
        )
        return {self.boundary_preimages[i]: x for i, x in coords.items()}


class Source:
    def __init__(self, d, m, top, ambient=False):
        integer(d, 2, 3)
        integer(m, 2, 4)
        need(type(ambient) is bool, "ambient bool")
        integer(top, 0, (3 if ambient else 4) if m <= 3 else 2)
        self.d, self.m, self.top = d, m, top
        self.ambient = ambient
        self.zero = (0,) * d
        self.words = list(product(range(d), repeat=m))
        orbits = defaultdict(list)
        for word in self.words:
            orbits[self.word_weight(word)].append(word)
        self.w_weights = sorted(orbits)
        self.w_terms = [{word: 1 for word in orbits[w]} for w in self.w_weights]
        self.c_terms = []
        self.c_weights = []
        self.c_address = {}
        self.anchors = {}
        for weight in self.w_weights:
            anchor, *others = sorted(orbits[weight])
            self.anchors[weight] = anchor
            for word in others:
                self.c_address[word] = len(self.c_terms)
                self.c_terms.append({word: 1, anchor: -1})
                self.c_weights.append(weight)
        if ambient:
            self.w_terms = [{word: 1} for word in self.words]
            self.w_weights = [self.word_weight(word) for word in self.words]
            self.c_terms, self.c_weights = [], []
        self.word_index = {word: i for i, word in enumerate(self.words)}
        self.r_basis = {}
        for degree in range(top + 1):
            mono = list(combinations_with_replacement(range(d), degree))
            self.r_basis[degree] = list(product(mono, repeat=m))
        self.k_basis = {}
        self.k_index = {}
        self.k_maps = {}
        self.h = {}
        self.actions = {}
        self.e_basis = {}
        self.e_index = {}
        self.e_maps = {}
        self.e2 = {}
        self.cells = 0

    def word_weight(self, word):
        return tuple(word.count(i) for i in range(self.d))

    def r_weight(self, mono):
        return tuple(sum(part.count(i) for part in mono) for i in range(self.d))

    def multiply(self, terms, mono):
        out = {}
        for word, c in terms.items():
            dest = tuple(
                tuple(sorted((*part, letter))) for part, letter in zip(mono, word)
            )
            out[dest] = out.get(dest, 0) + c
        return {k: v for k, v in out.items() if v}

    def register_basis(self, target, index, key, blocks):
        count = sum(map(len, blocks.values()))
        self.cells += count
        need(self.cells <= MAX_CELLS, "total basis-cell cap")
        for weight, rows in blocks.items():
            need(len(rows) <= MAX_ROWS, "weight-block row cap")
            target[key, weight] = rows
            index[key, weight] = {row: i for i, row in enumerate(rows)}

    def build_w(self):
        for j in range(self.top + 1):
            for q in range(j + 1):
                blocks = defaultdict(list)
                for wedge in combinations(range(len(self.w_terms)), q):
                    ww = tuple(
                        sum(self.w_weights[i][a] for i in wedge) for a in range(self.d)
                    )
                    for mono in self.r_basis[j - q]:
                        blocks[add_weight(ww, self.r_weight(mono))].append(
                            (wedge, mono)
                        )
                self.register_basis(self.k_basis, self.k_index, (q, j), blocks)
            for q in range(j + 1):
                for (key, weight), rows in list(self.k_basis.items()):
                    if key != (q, j):
                        continue
                    target = self.k_index.get(((q - 1, j), weight), {})
                    columns = []
                    for wedge, mono in rows:
                        col = {}
                        for at, w in enumerate(wedge):
                            short = wedge[:at] + wedge[at + 1 :]
                            for r, c in self.multiply(self.w_terms[w], mono).items():
                                axpy(col, {target[short, r]: c}, (-1) ** at)
                        columns.append(col)
                    self.k_maps[q, j, weight] = columns
            for q in range(j + 1):
                for (key, weight), rows in list(self.k_basis.items()):
                    if key != (q, j):
                        continue
                    outgoing = self.k_maps[q, j, weight]
                    incoming = self.k_maps.get((q + 1, j, weight), [])
                    self.h[q, j, weight] = Homology(
                        rows,
                        outgoing,
                        len(self.k_basis.get(((q - 1, j), weight), [])),
                        incoming,
                    )

    def c_on_chain(self, q, j, weight, c, vector):
        target_weight = add_weight(weight, self.c_weights[c])
        target = self.k_index[(q, j + 1), target_weight]
        rows = self.k_basis[(q, j), weight]
        out = {}
        for i, value in vector.items():
            wedge, mono = rows[i]
            for dest, scalar in self.multiply(self.c_terms[c], mono).items():
                axpy(out, {target[wedge, dest]: scalar}, value)
        return out

    def build_actions(self):
        self.boundary_action_checks = 0
        for (q, j, weight), hom in self.h.items():
            if j == self.top:
                continue
            for c in range(len(self.c_terms)):
                tw = add_weight(weight, self.c_weights[c])
                target = self.h[q, j + 1, tw]
                for bi, b in enumerate(hom.space.columns[: hom.boundary_rank]):
                    image = self.c_on_chain(q, j, weight, c, b)
                    lift = self.c_on_chain(
                        q + 1, j, weight, c, {hom.boundary_preimages[bi]: Fraction(1)}
                    )
                    expected = apply_columns(self.k_maps[q + 1, j + 1, tw], lift)
                    need(image == expected, "C does not descend through boundaries")
                    self.boundary_action_checks += 1
                for i, rep in enumerate(hom.reps):
                    image = self.c_on_chain(q, j, weight, c, rep)
                    self.actions[q, j, weight, c, i] = target.coordinates(image)

    def build_horizontal(self):
        for j in range(self.top + 1):
            for q in range(j + 1):
                for p in range(j + 1):
                    degree = j - p
                    blocks = defaultdict(list)
                    for wedge in combinations(range(len(self.c_terms)), p):
                        cw = tuple(
                            sum(self.c_weights[i][a] for i in wedge)
                            for a in range(self.d)
                        )
                        for (hq, hj, weight), hom in self.h.items():
                            if (hq, hj) != (q, degree):
                                continue
                            for i in range(len(hom.reps)):
                                blocks[add_weight(cw, weight)].append(
                                    (wedge, weight, i)
                                )
                    self.register_basis(self.e_basis, self.e_index, (p, q, j), blocks)
                for p in range(j + 1):
                    for (key, weight), rows in list(self.e_basis.items()):
                        if key != (p, q, j):
                            continue
                        target = self.e_index.get(((p - 1, q, j), weight), {})
                        columns = []
                        for wedge, hw, i in rows:
                            col = {}
                            for at, c in enumerate(wedge):
                                short = wedge[:at] + wedge[at + 1 :]
                                tw = add_weight(hw, self.c_weights[c])
                                for h, value in self.actions[
                                    q, j - p, hw, c, i
                                ].items():
                                    axpy(col, {target[short, tw, h]: value}, (-1) ** at)
                            columns.append(col)
                        self.e_maps[p, q, j, weight] = columns
                for p in range(j + 1):
                    for (key, weight), rows in list(self.e_basis.items()):
                        if key != (p, q, j):
                            continue
                        self.e2[p, q, j, weight] = Homology(
                            rows,
                            self.e_maps[p, q, j, weight],
                            len(self.e_basis.get(((p - 1, q, j), weight), [])),
                            self.e_maps.get((p + 1, q, j, weight), []),
                        )

    def permute_r(self, mono, perm):
        return tuple(mono[perm[i]] for i in range(self.m))

    def h_permutation(self, q, j, weight, perm, rep):
        rows = self.k_basis[(q, j), weight]
        index = self.k_index[(q, j), weight]
        out = {}
        for i, value in rep.items():
            wedge, mono = rows[i]
            sign = 1
            if self.ambient:
                wedge, sign = wedge_order(
                    tuple(
                        self.word_index[tuple(self.words[w][a] for a in perm)]
                        for w in wedge
                    )
                )
            axpy(out, {index[wedge, self.permute_r(mono, perm)]: sign * value})
        return self.h[q, j, weight].coordinates(out)

    def transgression(self):
        """d2 from (p,q,j)=(2,1,4), by literal zigzags, not rank inference."""
        need(
            not self.ambient and (self.d, self.m, self.top) == (3, 3, 4),
            "transgression panel",
        )
        answer = []
        witness = None
        for (p, q, j, weight), hom in sorted(self.e2.items()):
            if (p, q, j) != (2, 1, 4) or not hom.reps:
                continue
            target = self.h[2, 4, weight]
            columns = []
            for rep in hom.reps:
                first = defaultdict(dict)
                for index, scalar in rep.items():
                    wedge, hw, h = hom.basis[index]
                    lifted = self.h[1, 2, hw].reps[h]
                    for at, c in enumerate(wedge):
                        other = wedge[1 - at]
                        tw = add_weight(hw, self.c_weights[c])
                        axpy(
                            first[other, tw],
                            self.c_on_chain(1, 2, hw, c, lifted),
                            scalar * (-1) ** at,
                        )
                second = {}
                lifts = []
                for (c, hw), chain in sorted(first.items()):
                    wh = self.h[1, 3, hw]
                    lift = wh.boundary_lift(chain)
                    need(
                        apply_columns(self.k_maps[2, 3, hw], lift) == chain,
                        "zigzag boundary equation",
                    )
                    axpy(second, self.c_on_chain(2, 3, hw, c, lift))
                    lifts.append((c, hw, chain, lift))
                image = target.coordinates(second)
                columns.append(image)
                if image and witness is None:
                    witness = (weight, rep, lifts, second, image)
            ker, rank = kernel(columns, len(target.reps))
            for vector in ker:
                need(not apply_columns(columns, vector), "d2 kernel certificate")
            answer.append((weight, len(hom.reps), len(target.reps), rank, columns))
        return answer, witness

    def c_permutation(self, c, perm):
        out = {}
        for word, value in self.c_terms[c].items():
            dest = tuple(word[perm[i]] for i in range(self.m))
            if dest in self.c_address:
                axpy(out, {self.c_address[dest]: value})
        return out

    def wedge_permutation(self, wedge, perm):
        out = {(): Fraction(1)}
        for c in wedge:
            new = {}
            for old, value in out.items():
                for target, scalar in self.c_permutation(c, perm).items():
                    dest, sign = wedge_order((*old, target))
                    if sign:
                        new[dest] = new.get(dest, 0) + sign * value * scalar
            out = {key: value for key, value in new.items() if value}
        return out

    def e_permutation(self, p, q, j, weight, perm, rep):
        rows = self.e_basis[(p, q, j), weight]
        index = self.e_index[(p, q, j), weight]
        out = {}
        for i, value in rep.items():
            wedge, hw, h = rows[i]
            hv = self.h_permutation(q, j - p, hw, perm, self.h[q, j - p, hw].reps[h])
            for cw, a in self.wedge_permutation(wedge, perm).items():
                for k, b in hv.items():
                    axpy(out, {index[cw, hw, k]: a * b}, value)
        return self.e2[p, q, j, weight].coordinates(out)

    def report(self):
        self.build_w()
        self.build_actions()
        self.build_horizontal()
        classes = [tuple(range(self.m)), (1, 0, *range(2, self.m))]
        if self.m == 3:
            classes += [(1, 2, 0)]
        elif self.m == 4:
            classes += [(1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0)]
        w_rows = []
        for (q, j, weight), hom in sorted(self.h.items()):
            if not hom.reps:
                continue
            traces = []
            for perm in classes:
                trace = sum(
                    self.h_permutation(q, j, weight, perm, rep).get(i, 0)
                    for i, rep in enumerate(hom.reps)
                )
                need(
                    Fraction(trace).denominator == 1, "nonintegral homology class trace"
                )
                traces.append(int(trace))
            w_rows.append([q, j, list(weight), len(hom.reps), traces])
        e_rows = []
        for (p, q, j, weight), hom in sorted(self.e2.items()):
            if not hom.reps:
                continue
            traces = []
            for perm in classes if j <= 3 else []:
                trace = sum(
                    self.e_permutation(p, q, j, weight, perm, rep).get(i, 0)
                    for i, rep in enumerate(hom.reps)
                )
                need(Fraction(trace).denominator == 1, "nonintegral E2 class trace")
                traces.append(int(trace))
            e_rows.append([p, q, j, list(weight), len(hom.reps), traces])
        totals = Counter()
        ranks = Counter()
        for row in e_rows:
            totals[tuple(row[:3])] += row[4]
        for (p, q, j, weight), hom in self.e2.items():
            ranks[p, q, j] += hom.outgoing_rank
        return {
            "d": self.d,
            "m": self.m,
            "internal_degree_cap": self.top,
            "W_dimension": len(self.w_terms),
            "C_dimension": len(self.c_terms),
            "basis_cells": self.cells,
            "boundary_action_checks": self.boundary_action_checks,
            "W_homology": w_rows,
            "E2_homology": e_rows,
            "E2_totals": [[*key, value] for key, value in sorted(totals.items())],
            "horizontal_ranks": [[*key, value] for key, value in sorted(ranks.items())],
        }


def sparse(vector):
    return [[i, str(value)] for i, value in sorted(vector.items()) if value]


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    )


def digest(value):
    return sha256(canonical(value).encode("ascii")).hexdigest()


def guard_json(value, depth=0):
    need(depth <= MAX_DEPTH, "JSON depth cap")
    if type(value) is dict:
        need(
            len(value) <= MAX_CELLS and all(type(k) is str for k in value),
            "JSON mapping",
        )
        for k, v in value.items():
            guard_json(k, depth + 1)
            guard_json(v, depth + 1)
    elif type(value) is list:
        need(len(value) <= MAX_CELLS, "JSON list cap")
        for v in value:
            guard_json(v, depth + 1)
    elif type(value) is int:
        need(value.bit_length() <= MAX_BITS, "JSON integer bit cap")
    elif type(value) is str:
        need(len(value) <= 262144, "JSON string cap")
    else:
        need(value is None or type(value) is bool, "JSON scalar type")


def strict_load(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def invalid(value):
        raise ValueError("inexact JSON scalar " + value)

    try:
        result = json.loads(
            raw, object_pairs_hook=pairs, parse_float=invalid, parse_constant=invalid
        )
    except (RecursionError, UnicodeError) as exc:
        raise ValueError("malformed JSON") from exc
    guard_json(result)
    return result


def lf_bytes(path):
    need(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
    return path.read_bytes().replace(b"\r\n", b"\n")


def expected_manifest():
    return {
        "schema": "segre-chow-chain-sources-v1",
        "parents": [
            {
                "commit": c,
                "path": p,
                "git_blob": b,
                "sha256_lf": h,
                "current_copy_required": i in (5, 6),
            }
            for i, (c, p, b, h) in enumerate(PINS)
        ],
        "prior_art": [
            {
                "authors": "Raicu--Sam--Weyman",
                "title": "On some modules supported in the Chow variety",
                "url": "https://arxiv.org/html/2108.10910",
                "locator": "Proposition 2.7; equations (3.2)--(3.5); Example 4.5",
                "role": "classical Chow module and duality, not computed transgression",
            }
        ],
    }


def authenticate_sources(manifest=None):
    manifest = strict_load(lf_bytes(MANIFEST)) if manifest is None else manifest
    need(canonical(manifest) == canonical(expected_manifest()), "fixed source manifest")
    for pin in manifest["parents"]:
        spec = pin["commit"] + ":" + pin["path"]

        def git(*args):
            return subprocess.check_output(
                ["git", "--no-replace-objects", *args], cwd=ROOT, timeout=20
            )

        need(git("cat-file", "-t", spec).strip() == b"blob", "source is not a blob")
        need(int(git("cat-file", "-s", spec)) <= MAX_BYTES, "source byte cap")
        need(
            git("rev-parse", spec).decode().strip() == pin["git_blob"],
            "source blob identity",
        )
        raw = git("show", spec).replace(b"\r\n", b"\n")
        need(sha256(raw).hexdigest() == pin["sha256_lf"], "source LF hash")
        if pin["current_copy_required"]:
            need(lf_bytes(ROOT / pin["path"]) == raw, "resident source changed")
    return manifest


def artifacts():
    return {
        str(p.relative_to(ROOT)).replace("\\", "/"): sha256(lf_bytes(p)).hexdigest()
        for p in (NOTE, Path(__file__).resolve(), TEST, MANIFEST)
    }


def build_report():
    manifest = authenticate_sources()
    payload = build_payload()
    report = {
        "schema": "segre-chow-chain-comparison-v1",
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding": "none",
        "source_manifest_sha256": digest(manifest),
        "artifacts_sha256_lf": artifacts(),
        "caps": {
            "rows": MAX_ROWS,
            "cols": MAX_COLS,
            "basis_cells": MAX_CELLS,
            "bits": MAX_BITS,
            "bytes": MAX_BYTES,
            "depth": MAX_DEPTH,
        },
        "scope": "finite literal Koszul maps; no spectral determinant or general degeneration",
        "payload": payload,
        "payload_sha256": digest(payload),
    }
    guard_json(report)
    need(len(canonical(report).encode("ascii")) < MAX_BYTES, "report byte cap")
    return report


def validate_report(report, fresh=None):
    guard_json(report)
    need(type(report) is dict and "payload" in report, "report schema")
    need(report.get("payload_sha256") == digest(report["payload"]), "payload seal")
    need(report.get("artifacts_sha256_lf") == artifacts(), "artifact seal")
    if fresh is None:
        fresh = build_report()
    need(canonical(report) == canonical(fresh), "fresh primitive replay mismatch")
    return True


def schur3(partition):
    a, b, c = partition
    out = Counter()
    for x in range(b, a + 1):
        for y in range(c, b + 1):
            for z in range(y, x + 1):
                out[z, x + y - z, a + b + c - x - y] += 1
    return out


CHOW_TABLE = {
    (0, 0): [((0, 0, 0), (1, 1, 1))],
    (0, 1): [((2, 1, 0), (2, 0, -1)), ((1, 1, 1), (1, -1, 1))],
    (0, 2): [((2, 2, 2), (1, 1, 1)), ((3, 3, 0), (1, -1, 1))],
    (1, 2): [((4, 1, 1), (2, 0, -1))],
    (1, 3): [((5, 2, 2), (3, 1, 0)), ((5, 3, 1), (1, -1, 1)), ((4, 3, 2), (1, -1, 1))],
    (2, 4): [((5, 5, 2), (3, 1, 0)), ((6, 4, 2), (1, -1, 1)), ((5, 4, 3), (1, -1, 1))],
}


def check_chow_characters(report):
    expected = defaultdict(lambda: [0, 0, 0])
    for (q, j), summands in CHOW_TABLE.items():
        if j > report["internal_degree_cap"]:
            continue
        for partition, traces in summands:
            for weight, multiplicity in schur3(partition).items():
                for c, trace in enumerate(traces):
                    expected[q, j, weight][c] += multiplicity * trace
    actual = {(q, j, tuple(w)): traces for q, j, w, dim, traces in report["W_homology"]}
    need(actual == dict(expected), "full Chow Schur/class character mismatch")
    return len(actual)


def check_ambient(chow, ambient):
    actual = defaultdict(lambda: [0] * (3 if chow["m"] == 3 else 5))
    for p, q, j, w, dim, traces in chow["E2_homology"]:
        if j <= ambient["internal_degree_cap"]:
            for c, trace in enumerate(traces):
                actual[p + q, j, tuple(w)][c] += trace
    expected = {
        (q, j, tuple(w)): traces for q, j, w, dim, traces in ambient["W_homology"]
    }
    need(dict(actual) == expected, "actual ambient Koszul character mismatch")
    return len(expected)


def map_record(source):
    actions = []
    for (q, j, weight, c, i), column in sorted(source.actions.items()):
        if (q, j) == (1, 2):
            actions.append([list(weight), c, i, sparse(column)])
    reps = []
    for (q, j, weight), hom in sorted(source.h.items()):
        if (q, j) in {(1, 2), (1, 3), (2, 4)}:
            reps.append([q, j, list(weight), [sparse(v) for v in hom.reps]])
    matrices = []
    for (p, q, j, weight), hom in sorted(source.e2.items()):
        if (p, q, j) in {(1, 1, 3), (2, 1, 4)}:
            cols = source.e_maps[p, q, j, weight]
            matrices.append(
                [
                    p,
                    q,
                    j,
                    list(weight),
                    len(cols),
                    hom.outgoing_rank,
                    [sparse(v) for v in cols],
                ]
            )
    return {
        "index_contract": "zero-based lexicographic combinations/product; graded bases reconstructed literally",
        "W_orbit_sums": [
            [[[*w], c] for w, c in sorted(t.items())] for t in source.w_terms
        ],
        "C_word_differences": [
            [[[*w], c] for w, c in sorted(t.items())] for t in source.c_terms
        ],
        "C_on_B12": actions,
        "W_cycle_representatives": reps,
        "horizontal_matrices": matrices,
        "all_W_matrices_digest": digest(
            [
                [q, j, list(w), [sparse(c) for c in cols]]
                for (q, j, w), cols in sorted(source.k_maps.items())
            ]
        ),
    }


def build_payload():
    main_source = Source(3, 3, 4)
    main_report = main_source.report()
    check_chow_characters(main_report)
    ambient3 = Source(3, 3, 3, True).report()
    check_ambient(main_report, ambient3)
    heldout = Source(3, 4, 2).report()
    ambient4 = Source(3, 4, 2, True).report()
    check_ambient(heldout, ambient4)
    d2, witness = main_source.transgression()
    d2_rows = [
        [list(w), cols, rows, rank, [sparse(c) for c in matrix]]
        for w, cols, rows, rank, matrix in d2
    ]
    need(witness is not None, "preregistered nonzero d2 witness absent")
    weight, rep, lifts, second, image = witness
    zigzag = {
        "weight": list(weight),
        "E2_source_cycle": sparse(rep),
        "boundary_lifts": [
            [c, list(w), sparse(chain), sparse(lift)] for c, w, chain, lift in lifts
        ],
        "second_C_image": sparse(second),
        "target_homology": sparse(image),
    }
    return {
        "main": main_report,
        "ambient3": ambient3,
        "heldout": heldout,
        "ambient4": ambient4,
        "literal_maps": map_record(main_source),
        "transgression_matrices": d2_rows,
        "nonzero_zigzag": zigzag,
    }


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--emit-sources", action="store_true")
    modes.add_argument("--write-fixture", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        print(json.dumps(expected_manifest(), indent=2))
        return
    report = build_report()
    if args.check:
        validate_report(strict_load(lf_bytes(FIXTURE)), report)
        print("PASS " + report["payload_sha256"])
    elif args.write_fixture:
        # Deterministic generated artifact, never a source-file mutation.
        FIXTURE.write_bytes((canonical(report) + "\n").encode("ascii"))
        print("WROTE " + str(FIXTURE.stat().st_size) + " " + report["payload_sha256"])
    else:
        print(canonical(report))


if __name__ == "__main__":
    main()
