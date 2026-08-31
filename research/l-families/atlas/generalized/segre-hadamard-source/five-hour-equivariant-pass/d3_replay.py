"""First possible actual d3, in the complete highest-weight 744 block."""

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
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/five-hour-equivariant-pass/"
SOURCE_FREEZE = "2c65d7ba3f02786bf827868d9a9446dd1971ee07"
SOURCE_PINS = {
    "HIGHER_SYZYGY_MATHEMATICS.md": "abc4f9eea675267cf0aaf6e53217293260db4a46",
    "HIGHER_SYZYGY_PREREGISTRATION.md": "b3e0563f031d053e9f179e406b58d32f973a6e5b",
    "HIGHER_SYZYGY_REPLAY.md": "dbc06208b44ad72e240b512297a0382b7ec45601",
    "higher_syzygy.py": "18e030a371ead80e7dcd985dbe017fd37ee1ac57",
    "higher_syzygy.shape.json": "2c52393913235972c9b52028f6e78d50deafa03d",
    "higher_syzygy.verification.json": "c2e0c3fe915752e541847bb49cb3cab87216bbf6",
    "test_equivariant_pass_higher_syzygy.py": "0aa1c68cbd608b418cc442f4209ee98f897441c5",
}
TARGET_WEIGHT = (7, 4, 4)
MAX_BLOCK = 512
MAX_BYTES = 16 * 1024 * 1024
FULL_STATUS = "PENDING_TIMEOUT"
SHAPE = HERE / "d3.shape.json"
SIGN_SHAPE = HERE / "d3.sign.shape.json"
FIXTURE = HERE / "d3.verification.json"
TEST = ROOT / "tests/test_equivariant_pass_d3.py"
OWNED = (
    "D3_PREREGISTRATION.md",
    "D3_SIGN_PREREGISTRATION.md",
    "ACTUAL_CHANGE_OF_RINGS_D3.md",
    "D3_REPLAY.md",
    "d3_replay.py",
    "d3.shape.json",
    "d3.sign.shape.json",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def blob_id(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def frozen(name, expected):
    need(
        type(name) is str and type(expected) is str and len(expected) == 40,
        "source pin shape",
    )
    path = ("tests/" if name.startswith("test_") else PREFIX) + name
    raw = subprocess.check_output(["git", "show", f"{SOURCE_FREEZE}:{path}"], cwd=ROOT)
    need(
        len(raw) <= MAX_BYTES and blob_id(raw) == expected,
        "higher-syzygy source mismatch",
    )
    return raw


def strict_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def forbidden(_):
        raise ValueError("floating/nonfinite JSON")

    return json.loads(
        raw, object_pairs_hook=pairs, parse_float=forbidden, parse_constant=forbidden
    )


def load_input():
    raw = {name: frozen(name, blob) for name, blob in SOURCE_PINS.items()}
    h = types.ModuleType("authenticated_complete_higher_syzygy")
    h.__file__ = str(HERE / "higher_syzygy.py")
    exec(compile(raw["higher_syzygy.py"], h.__file__, "exec"), h.__dict__)  # noqa: S102 -- authenticated frozen definitions
    accepted = h.strict_json(raw["higher_syzygy.verification.json"])
    h.check_record(accepted, accepted)
    need(
        accepted["status"] == "VERIFIED_COMPLETE_Q_SYZYGY"
        and accepted["global_rank"] == 1105,
        "complete higher-syzygy source",
    )
    source = h.load_input()
    return types.SimpleNamespace(
        h=h, d=source.d, q=source.q, data=source.data, accepted=accepted
    )


@lru_cache(maxsize=32)
def compositions(n, length=3):
    need(
        type(n) is int and 0 <= n <= 5 and type(length) is int and 1 <= length <= 3,
        "composition domain",
    )
    if length == 1:
        return ((n,),)
    return tuple(
        (a, *tail) for a in range(n + 1) for tail in compositions(n - a, length - 1)
    )


def plus(*weights):
    return tuple(sum(row) for row in zip(*weights, strict=True))


@lru_cache(maxsize=8)
def source_by_weight(grade):
    result = {}
    for record in itertools.product(compositions(grade), repeat=3):
        result.setdefault(plus(*record), []).append(record)
    return result


@lru_cache(maxsize=64)
def weight_chain(grade, h, weight):
    need(
        type(grade) is int and 0 <= grade <= 5 and type(h) is int and 0 <= h <= grade,
        "W chain domain",
    )
    w = compositions(3)
    records = source_by_weight(grade - h)
    result = []
    for wedge in itertools.combinations(range(10), h):
        ww = plus(*(w[i] for i in wedge)) if wedge else (0, 0, 0)
        remaining = tuple(a - b for a, b in zip(weight, ww, strict=True))
        result.extend((wedge, record) for record in records.get(remaining, ()))
    return tuple(result)


def q3_shape(source):
    qw = [weight for weight, _ in source.data.qb]
    lower = source.data.homology[2].weights
    upper = source.data.homology[3].weights
    domain = sum(
        plus(qw[i], qw[j], qw[k], weight) == TARGET_WEIGHT
        for i, j, k in itertools.combinations(range(17), 3)
        for weight in lower
    )
    target = sum(
        plus(qw[i], qw[j], weight) == TARGET_WEIGHT
        for i, j in itertools.combinations(range(17), 2)
        for weight in upper
    )
    return domain, target


def shape_report(source):
    qdomain, qtarget = q3_shape(source)
    qw = [weight for weight, _ in source.data.qb]
    grade4_weights = sorted(
        {
            tuple(a - b for a, b in zip(TARGET_WEIGHT, weight, strict=True))
            for weight in qw
            if all(a >= b for a, b in zip(TARGET_WEIGHT, weight, strict=True))
        },
        reverse=True,
    )
    grade4 = [
        {
            "weight": list(weight),
            "chain_dimensions": [len(weight_chain(4, h, weight)) for h in range(5)],
        }
        for weight in grade4_weights
    ]
    grade5 = [len(weight_chain(5, h, TARGET_WEIGHT)) for h in range(6)]
    maximum = max(
        [
            qdomain,
            qtarget,
            *grade5,
            *(value for row in grade4 for value in row["chain_dimensions"]),
        ]
    )
    return {
        "schema": "equivariant-pass/d3-shape/v1",
        "source_freeze": SOURCE_FREEZE,
        "target_weight": list(TARGET_WEIGHT),
        "Q_delta_domain": qdomain,
        "Q_delta_target": qtarget,
        "internal4_W_blocks": grade4,
        "internal5_W_chain_dimensions": grade5,
        "maximum_dimension": maximum,
        "within_registered_512_cap": maximum <= MAX_BLOCK,
        "rank_calculation_performed": False,
    }


def sign_chain(grade, h, weight=TARGET_WEIGHT):
    """Disjoint-pivot labels for the exact factor-sign chain space."""
    return tuple(
        (wedge, record)
        for wedge, record in weight_chain(grade, h, weight)
        if len(set(record)) == 3 and record == tuple(sorted(record))
    )


def sign_shape_report(source):
    full = shape_report(source)
    dimensions = [len(sign_chain(5, h)) for h in range(6)]
    maximum = max(
        [
            full["Q_delta_domain"],
            full["Q_delta_target"],
            *dimensions,
            *(
                value
                for row in full["internal4_W_blocks"]
                for value in row["chain_dimensions"]
            ),
        ]
    )
    return {
        "schema": "equivariant-pass/d3-sign-shape/v1",
        "source_freeze": SOURCE_FREEZE,
        "target_weight": list(TARGET_WEIGHT),
        "complete_Q_dimensions": [full["Q_delta_domain"], full["Q_delta_target"]],
        "complete_internal4_W_blocks": full["internal4_W_blocks"],
        "full_internal5_refused_dimensions": full["internal5_W_chain_dimensions"],
        "sign_internal5_chain_dimensions": dimensions,
        "maximum_eliminated_dimension": maximum,
        "within_registered_512_cap": maximum <= MAX_BLOCK,
        "rank_calculation_performed": False,
    }


class WWeightComplex:
    """One complete W-Koszul weight block, with no inherited grade cap."""

    def __init__(self, q, grade, weight):
        self.q, self.m, self.grade, self.w = q, 3, grade, compositions(3)
        self.chains = [weight_chain(grade, h, weight) for h in range(grade + 1)]
        need(
            all(len(basis) <= MAX_BLOCK for basis in self.chains),
            "complete local W block exceeds512",
        )
        self.index = [
            {entry: i for i, entry in enumerate(basis)} for basis in self.chains
        ]
        self.weights = [[weight] * len(basis) for basis in self.chains]
        self.groups = [{weight: list(range(len(basis)))} for basis in self.chains]
        self.maps = [[]]
        digest = hashlib.sha256()
        for h in range(1, grade + 1):
            columns = []
            for wedge, record in self.chains[h]:
                column = {}
                for place, wi in enumerate(wedge):
                    smaller = wedge[:place] + wedge[place + 1 :]
                    for word in q.orbit_words(self.w[wi]):
                        row = self.index[h - 1][smaller, q.word_product(record, word)]
                        q.add(column, {row: (-1) ** place})
                digest.update(canonical(q.encode_vector(column)).encode() + b"\n")
                columns.append(column)
            self.maps.append(columns)
        for h in range(2, grade + 1):
            for column in self.maps[h]:
                need(
                    not q.apply(self.maps[h - 1], column),
                    "local W differential does not square zero",
                )
        ranks = []
        for h in range(1, grade + 1):
            span = q.Span()
            for column in self.maps[h]:
                span.insert(column)
            ranks.append(span.rank)
        dimensions = list(map(len, self.chains))
        hom = [
            dimensions[h] - ([0] + ranks)[h] - (ranks + [0])[h]
            for h in range(grade + 1)
        ]
        self.rank_rows = [
            {
                "weight": list(weight),
                "differential_ranks": ranks,
                "homology_dimensions": hom,
            }
        ]
        self.hash = digest.hexdigest()


PERMUTATIONS = tuple(itertools.permutations(range(3)))


def permutation_sign(permutation):
    return (
        -1
        if sum(
            permutation[i] > permutation[j] for i in range(3) for j in range(i + 1, 3)
        )
        % 2
        else 1
    )


class SignComplex:
    """Exact alternating factor-isotypic subcomplex in original coordinates."""

    def __init__(self, q):
        self.q, self.m, self.grade, self.weight = q, 3, 5, TARGET_WEIGHT
        self.full_chains = [weight_chain(5, h, TARGET_WEIGHT) for h in range(6)]
        self.full_index = [
            {entry: i for i, entry in enumerate(basis)} for basis in self.full_chains
        ]
        self.chains = [sign_chain(5, h) for h in range(6)]
        need(
            all(len(basis) <= MAX_BLOCK for basis in self.chains),
            "sign W block exceeds512",
        )
        self.index = [
            {entry: i for i, entry in enumerate(basis)} for basis in self.chains
        ]
        self.weights = [[TARGET_WEIGHT] * len(basis) for basis in self.chains]
        self.groups = [
            {TARGET_WEIGHT: list(range(len(basis)))} for basis in self.chains
        ]
        self.maps = [[]]
        self.embeddings = [
            [self.embed(h, label) for label in basis]
            for h, basis in enumerate(self.chains)
        ]
        digest = hashlib.sha256()
        for h in range(1, 6):
            columns = []
            for embedded in self.embeddings[h]:
                full = self.full_apply(h, embedded)
                coordinates = self.sign_coordinates(h - 1, full)
                need(
                    self.expand(h - 1, coordinates) == full,
                    "sign differential reconstruction",
                )
                digest.update(canonical(q.encode_vector(coordinates)).encode() + b"\n")
                columns.append(coordinates)
            self.maps.append(columns)
        for h in range(2, 6):
            for column in self.maps[h]:
                need(
                    not q.apply(self.maps[h - 1], column),
                    "sign differential does not square zero",
                )
        ranks = []
        for h in range(1, 6):
            span = q.Span()
            for column in self.maps[h]:
                span.insert(column)
            ranks.append(span.rank)
        dimensions = list(map(len, self.chains))
        hom = [dimensions[h] - ([0] + ranks)[h] - (ranks + [0])[h] for h in range(6)]
        self.rank_rows = [
            {
                "weight": list(TARGET_WEIGHT),
                "differential_ranks": ranks,
                "homology_dimensions": hom,
            }
        ]
        self.hash = digest.hexdigest()

    def embed(self, h, label):
        wedge, ordered = label
        result = {}
        for permutation in PERMUTATIONS:
            record = tuple(ordered[i] for i in permutation)
            self.q.add(
                result,
                {self.full_index[h][wedge, record]: permutation_sign(permutation)},
            )
        need(len(result) == 6, "alternating orbit completeness")
        return result

    def full_column(self, h, index):
        wedge, record = self.full_chains[h][index]
        result = {}
        for place, wi in enumerate(wedge):
            smaller = wedge[:place] + wedge[place + 1 :]
            for word in self.q.orbit_words(compositions(3)[wi]):
                row = self.full_index[h - 1][smaller, self.q.word_product(record, word)]
                self.q.add(result, {row: (-1) ** place})
        return result

    def full_apply(self, h, vector):
        result = {}
        for index, coefficient in vector.items():
            self.q.add(result, self.full_column(h, index), coefficient)
        return result

    def sign_coordinates(self, h, vector):
        result = {}
        for i, (wedge, record) in enumerate(self.chains[h]):
            coefficient = vector.get(self.full_index[h][wedge, record], 0)
            if coefficient:
                result[i] = coefficient
        return result

    def expand(self, h, coordinates):
        result = {}
        for i, coefficient in coordinates.items():
            self.q.add(result, self.embeddings[h][i], coefficient)
        return result

    def project(self, h, vector):
        result = {}
        for index, coefficient in vector.items():
            wedge, record = self.full_chains[h][index]
            for permutation in PERMUTATIONS:
                moved = tuple(record[i] for i in permutation)
                row = self.full_index[h][wedge, moved]
                self.q.add(
                    result,
                    {row: coefficient * Fraction(permutation_sign(permutation), 6)},
                )
        return result


def q3_delta(source):
    data = source.data
    qw = [weight for weight, _ in data.qb]
    domain = [
        (i, j, k, b)
        for i, j, k in itertools.combinations(range(17), 3)
        for b, weight in enumerate(data.homology[2].weights)
        if plus(qw[i], qw[j], qw[k], weight) == TARGET_WEIGHT
    ]
    target = [
        (i, j, b)
        for i, j in itertools.combinations(range(17), 2)
        for b, weight in enumerate(data.homology[3].weights)
        if plus(qw[i], qw[j], weight) == TARGET_WEIGHT
    ]
    need(len(domain) <= MAX_BLOCK and len(target) <= MAX_BLOCK, "complete Q3 block cap")
    index = {entry: i for i, entry in enumerate(target)}
    columns = []
    for i, j, k, b in domain:
        column = {}
        wedge = (i, j, k)
        for place, removed in enumerate(wedge):
            remaining = wedge[:place] + wedge[place + 1 :]
            for image, coefficient in data.matrices[removed][b].items():
                source.q.add(
                    column, {index[*remaining, image]: coefficient * (-1) ** place}
                )
        columns.append(column)
    return domain, target, columns


def complete_kernel(q, columns):
    span, kernels = q.Span(), []
    for i, column in enumerate(columns):
        independent, witness = span.insert(column, {i: Fraction(1)})
        if not independent:
            kernels.append(q.primitive(witness))
    need(span.rank + len(kernels) == len(columns), "complete Q3 kernel")
    return span.rank, kernels


def eta1_for(source, domain, kernel):
    result = {}
    for index, scalar in kernel.items():
        wedge = domain[index][:3]
        b = domain[index][3]
        for place, removed in enumerate(wedge):
            remaining = wedge[:place] + wedge[place + 1 :]
            for ci, coefficient in source.data.lifts[removed][b].items():
                source.q.add(
                    result, {(*remaining, ci): scalar * coefficient * (-1) ** place}
                )
    need(len(result) <= 8192, "eta1 sparse cap")
    return result


def delta_z_original(source, domain, kernel):
    q, data = source.q, source.data
    result = {}
    for index, scalar in kernel.items():
        wedge = domain[index][:3]
        b = domain[index][3]
        for place, removed in enumerate(wedge):
            remaining = wedge[:place] + wedge[place + 1 :]
            product = q.product_vector(
                data.complexes[2],
                data.complexes[3],
                1,
                data.homology[2].cycles[b],
                data.qb[removed][1],
            )
            for ci, coefficient in product.items():
                q.add(result, {(*remaining, ci): scalar * coefficient * (-1) ** place})
    return result


def d_eta1(source, eta1):
    result = {}
    for (i, j, ci), scalar in eta1.items():
        for row, coefficient in source.data.complexes[3].maps[2][ci].items():
            source.q.add(result, {(i, j, row): scalar * coefficient})
    return result


def grade4_complexes(source):
    qw = [weight for weight, _ in source.data.qb]
    return {
        i: WWeightComplex(
            source.q,
            4,
            tuple(a - b for a, b in zip(TARGET_WEIGHT, weight, strict=True)),
        )
        for i, weight in enumerate(qw)
        if all(a >= b for a, b in zip(TARGET_WEIGHT, weight, strict=True))
    }


def delta_eta1(source, eta1, complexes):
    q, data = source.q, source.data
    result = {}
    for (i, j, ci), scalar in eta1.items():
        wedge, record = data.complexes[3].chains[2][ci]
        for remaining, removed, sign in ((j, i, 1), (i, j, -1)):
            complex_ = complexes[remaining]
            for word, coefficient in data.qb[removed][1].items():
                row = complex_.index[2][wedge, q.word_product(record, word)]
                q.add(result, {(remaining, row): scalar * coefficient * sign})
    return result


def reduce_first_obstruction(source, residual, complexes, homologies):
    obstruction, eta2 = {}, {}
    for qi, complex_ in complexes.items():
        vector = {
            row: coefficient
            for (actual, row), coefficient in residual.items()
            if actual == qi
        }
        if not vector:
            continue
        image, boundary = homologies[qi].reduce(vector)
        for row, coefficient in image.items():
            source.q.add(obstruction, {(qi, row): coefficient})
        for row, coefficient in boundary.items():
            source.q.add(eta2, {(qi, row): -coefficient})
        need(
            not source.q.apply(complex_.maps[2], vector),
            "first obstruction is not W closed",
        )
    return obstruction, eta2


def combine(q, vectors, coefficients):
    result = {}
    for index, coefficient in coefficients.items():
        q.add(result, vectors[index], coefficient)
    return result


def d_eta2(source, eta2, complexes):
    result = {}
    for (qi, ci), scalar in eta2.items():
        for row, coefficient in complexes[qi].maps[3][ci].items():
            source.q.add(result, {(qi, row): scalar * coefficient})
    return result


def d3_cycle(source, eta2, complexes, target):
    result = {}
    for (qi, ci), scalar in eta2.items():
        wedge, record = complexes[qi].chains[3][ci]
        for word, coefficient in source.data.qb[qi][1].items():
            row = target.full_index[3][wedge, source.q.word_product(record, word)]
            source.q.add(result, {row: -scalar * coefficient})
    return result


def encode_labeled(vector):
    return [
        [*key, value.numerator, value.denominator]
        for key, value in sorted(vector.items())
    ]


def build():
    source = load_input()
    signed_shape = sign_shape_report(source)
    need(signed_shape["within_registered_512_cap"], "sign-isotypic shape exceeds cap")
    domain, _, delta = q3_delta(source)
    delta_rank, kernels = complete_kernel(source.q, delta)
    complexes = grade4_complexes(source)
    homologies = {
        qi: source.q.Homology(complex_, 2) for qi, complex_ in complexes.items()
    }
    eta1s, residuals, obstructions, eta2s = [], [], [], []
    for kernel in kernels:
        eta1 = eta1_for(source, domain, kernel)
        need(
            d_eta1(source, eta1) == delta_z_original(source, domain, kernel),
            "first lift identity",
        )
        residual = delta_eta1(source, eta1, complexes)
        obstruction, eta2 = reduce_first_obstruction(
            source, residual, complexes, homologies
        )
        eta1s.append(eta1)
        residuals.append(residual)
        obstructions.append(obstruction)
        eta2s.append(eta2)
    obstruction_span, survivors = source.q.Span(), []
    for i, column in enumerate(obstructions):
        independent, witness = obstruction_span.insert(column, {i: Fraction(1)})
        if not independent:
            survivors.append(source.q.primitive(witness))
    target = SignComplex(source.q)
    target_h = source.q.Homology(target, 3)
    need(len(target_h.cycles) == 1, "target sign H3 must be one dimensional")
    rows, images = [], []
    for survivor in survivors:
        kernel = combine(source.q, kernels, survivor)
        eta1 = combine(source.q, eta1s, survivor)
        residual = combine(source.q, residuals, survivor)
        eta2 = combine(source.q, eta2s, survivor)
        need(
            not combine(source.q, obstructions, survivor),
            "E3 source obstruction survives",
        )
        opposite = dict(residual)
        source.q.add(opposite, d_eta2(source, eta2, complexes))
        need(not opposite, "second lift identity")
        full_cycle = d3_cycle(source, eta2, complexes, target)
        need(not target.full_apply(3, full_cycle), "d3 target is not W closed")
        projected = target.project(3, full_cycle)
        sign_cycle = target.sign_coordinates(3, projected)
        need(
            target.expand(3, sign_cycle) == projected,
            "Reynolds projection leaves sign chain",
        )
        image, boundary = target_h.reduce(sign_cycle)
        images.append(image)
        rows.append(
            {
                "source_kernel": source.q.encode_vector(kernel),
                "eta1": encode_labeled(eta1),
                "eta2": encode_labeled(eta2),
                "projected_target_cycle": source.q.encode_vector(sign_cycle),
                "target_image": source.q.encode_vector(image),
                "target_boundary": source.q.encode_vector(boundary),
            }
        )
    image_span = source.q.Span()
    for image in images:
        image_span.insert(image)
    status = (
        "VERIFIED_NONZERO_D3_744_SIGN"
        if image_span.rank
        else ("VERIFIED_ZERO_D3_744_SIGN" if survivors else "VERIFIED_NO_E3_SOURCE_744")
    )
    result = {
        "schema": "equivariant-pass/d3-sign/v1",
        "source_freeze": SOURCE_FREEZE,
        "source_pins": SOURCE_PINS,
        "source_proof_sha256": source.accepted["proof_sha256"],
        "owned_sha256_lf": {
            name: hashlib.sha256(
                (HERE / name).read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for name in OWNED
        },
        "test_sha256_lf": hashlib.sha256(
            TEST.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "full_refused_shape": shape_report(source),
        "sign_shape": signed_shape,
        "Q_delta_rank": delta_rank,
        "E2_source_dimension": len(kernels),
        "d2_obstruction_rank": obstruction_span.rank,
        "E3_source_dimension": len(survivors),
        "grade4_W_blocks": [
            {
                "Q_index": qi,
                "weight": list(complex_.weights[0][0]),
                "dimensions": list(map(len, complex_.chains)),
                "differential_sha256": complex_.hash,
            }
            for qi, complex_ in complexes.items()
        ],
        "sign_target_dimensions": list(map(len, target.chains)),
        "sign_target_differential_sha256": target.hash,
        "sign_target_H3_dimension": len(target_h.cycles),
        "rows": rows,
        "d3_image_rank": image_span.rank,
        "reaches_complete_744_sign_constituent": image_span.rank == 1,
        "global_d3_surjectivity_claimed": False,
        "status": status,
    }
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "artifact byte cap")
    return result, source.q._peak_working


def check_record(candidate, expected):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str,
        "d3 artifact shape",
    )
    body = dict(candidate)
    claimed = body.pop("proof_sha256")
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest() == claimed,
        "d3 body digest",
    )
    need(
        canonical(candidate) == canonical(expected), "typed complete d3 replay mismatch"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--shape", action="store_true")
    modes.add_argument("--sign-shape", action="store_true")
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = load_input()
    shape = shape_report(source)
    if args.shape:
        SHAPE.write_text(
            json.dumps(shape, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(json.dumps(shape))
        return
    if args.sign_shape:
        record = sign_shape_report(source)
        SIGN_SHAPE.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(json.dumps(record))
        return
    need(
        False,
        "PENDING_TIMEOUT: exact sign acquisition exceeded the registered 240-second cap; no d3 artifact",
    )
    started = time.monotonic()
    record, peak = build()
    if args.write:
        text = json.dumps(record, sort_keys=True, indent=2) + "\n"
        need(len(text.encode()) <= MAX_BYTES, "pretty artifact byte cap")
        FIXTURE.write_text(text, encoding="utf-8", newline="\n")
    else:
        need(FIXTURE.exists(), "missing d3 artifact")
        check_record(strict_json(FIXTURE.read_bytes()), record)
    print(
        json.dumps(
            {
                "status": record["status"],
                "proof_sha256": record["proof_sha256"],
                "E2_source_dimension": record["E2_source_dimension"],
                "E3_source_dimension": record["E3_source_dimension"],
                "d3_image_rank": record["d3_image_rank"],
                "elapsed_ms": round(1000 * (time.monotonic() - started)),
                "peak_working_bytes": peak,
            }
        )
    )


if __name__ == "__main__":
    main()
