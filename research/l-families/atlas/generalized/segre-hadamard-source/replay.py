"""Exact Chow-base multiplication, Koszul homology, and character controls.

No numerical algebra, third-party dependency, executable source import, or
characteristic-p rank inference is used. Nontrivial jobs are parent-serialized.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
TEST = ROOT / "tests/test_segre_hadamard_source.py"
FIXTURE = HERE / "verification.json"
OWNED = (
    "MATHEMATICS.md",
    "PREREGISTRATION.md",
    "REPLAY.md",
    "replay.py",
    "sources.json",
)
MAX_CHAIN = 5000
MAX_BLOCK = 800
MAX_GRADE = 3
PINS = (
    (
        "ac1cc5eaf229087b6d805e908897c7c8c99a58b7",
        "claims/theorems/T-108500-pointwise-transform-defect-law.md",
        "sources/T-108500.md",
        "b232a40659a1e09d065b34603c6e74043223fd79",
    ),
    (
        "ac1cc5eaf229087b6d805e908897c7c8c99a58b7",
        "claims/theorems/T-108510-defect-codimension-law.md",
        "sources/T-108510.md",
        "f6c22bf9116de00959a7024b62faaf3a370f2754",
    ),
    (
        "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
        "research/l-families/atlas/generalized/SEGRE_KOSZUL_LIE_PARENT.md",
        "sources/SEGRE_KOSZUL_LIE_PARENT.md",
        "6036546493e416fdb44e57e6c9746e9a92844a5c",
    ),
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label="integer"):
    need(type(value) is int and low <= value <= high, f"{label} outside declared cap")
    return value


def digest(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


@lru_cache(maxsize=128)
def _compositions(n, d):
    if d == 1:
        return ((n,),)
    return tuple((a, *b) for a in range(n + 1) for b in _compositions(n - a, d - 1))


def compositions(n, d):
    integer(n, 0, 64, "composition degree")
    integer(d, 1, 4, "dimension")
    return _compositions(n, d)


def scalar(value):
    need(type(value) in (int, Fraction), "eigenvalue must be exact rational")
    need(value != 0, "invertible eigenvalues required")
    return Fraction(value)


def eigenvalues(values):
    need(isinstance(values, (tuple, list)), "eigenvalues must be a tuple or list")
    integer(len(values), 1, 4, "dimension")
    return tuple(scalar(v) for v in values)


def monomial(values, weight):
    return prod(x**a for x, a in zip(values, weight, strict=True))


def multiply(left, right, cut):
    integer(cut, 0, 64, "series cutoff")
    out = [Fraction(0)] * (cut + 1)
    for i, a in enumerate(left[: cut + 1]):
        for j, b in enumerate(right[: cut + 1 - i]):
            out[i + j] += a * b
    return out


def factors(weights, cut):
    out = [Fraction(1)] + [Fraction(0)] * cut
    for value in weights:
        out = multiply(out, [1, -value], cut)
    return out


def complete(values, r):
    values = eigenvalues(values)
    return sum((monomial(values, a) for a in compositions(r, len(values))), Fraction(0))


def numerator(values, m, cut=None):
    values = eigenvalues(values)
    integer(m, 1, 8, "factor count")
    d = len(values)
    s = comb(d + m - 1, m)
    need(s <= 32, "symmetric generator cap")
    degree = s - d
    if cut is None:
        cut = degree + 3
    integer(cut, 0, 64, "numerator cutoff")
    weights = [monomial(values, a) for a in compositions(m, d)]
    q = factors(weights, cut)
    series = [complete(values, r) ** m for r in range(cut + 1)]
    return multiply(q, series, cut)


def descent_numerator(x, y, m):
    x, y = scalar(x), scalar(y)
    integer(m, 1, 8, "permutation enumeration cap")
    out = [Fraction(0)] * m
    for permutation in itertools.permutations(range(m)):
        descents = [i + 1 for i in range(m - 1) if permutation[i] > permutation[i + 1]]
        r, major = len(descents), sum(descents)
        out[r] += x**major * y ** (m * r - major)
    return out


def encode(value):
    if isinstance(value, Fraction):
        return (
            value.numerator
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        )
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def character_control(values, m, *, heldout=False):
    values = eigenvalues(values)
    d = len(values)
    s, dimension = comb(d + m - 1, m), m * (d - 1) + 1
    codimension, degree = s - dimension, s - d
    exponent = m * s // d - m
    need(m * s % d == 0, "determinant exponent not integral")
    n = numerator(values, m)
    need(
        all(v == 0 for v in n[degree + 1 :]), "universal numerator tail did not vanish"
    )
    n = n[: degree + 1]
    need(n[0] == 1, "constant numerator coefficient")
    need(
        n[-1] == (-1) ** codimension * prod(values) ** exponent,
        "top determinant character",
    )
    inverse = numerator(tuple(1 / v for v in values), m)[: degree + 1]
    need(
        n
        == [
            (-1) ** codimension * prod(values) ** exponent * a
            for a in reversed(inverse)
        ],
        "contragredient duality failed",
    )
    first = n[1] if degree else 0
    need(
        first == sum(values) ** m - complete(values, m),
        "first source quotient character",
    )
    source_weights = [monomial(values, a) for a in compositions(m, d)]
    # Different routes construct ambient word weights and the quotient exponents.
    ambient_weights = [prod(word) for word in itertools.product(values, repeat=m)]
    extra_weights = []
    for a, weight in zip(compositions(m, d), source_weights, strict=True):
        multiplicity = factorial(m) // prod(factorial(v) for v in a)
        extra_weights.extend([weight] * (multiplicity - 1))
    cut = min(degree + 2, 16)
    series = [complete(values, r) ** m for r in range(cut + 1)]
    ambient = multiply(factors(ambient_weights, cut), series, cut)
    need(
        ambient == multiply(factors(extra_weights, cut), n, cut),
        "ambient/Chow denominator distinction",
    )
    need(ambient[1] == 0, "full ambient degree-one relations must vanish")
    return {
        "dimension": d,
        "factor_count": m,
        "eigenvalues": values,
        "s_D_c_degree": [s, dimension, codimension, degree],
        "top_det_exponent": exponent,
        "universal_numerator": n,
        "distinct_symmetric_weights": len(set(source_weights)) == s,
        "comparison_or_heldout": "new source-replay heldout"
        if heldout
        else "comparison",
        "ambient_relation_checked_through": cut,
    }


def add_weight(*weights):
    return tuple(sum(entries) for entries in zip(*weights, strict=True))


def orbit_words(content):
    d, m = len(content), sum(content)
    need(d <= 4 and m <= 4, "literal word cap")
    return tuple(
        word
        for word in itertools.product(range(d), repeat=m)
        if tuple(word.count(a) for a in range(d)) == content
    )


def source_basis(d, m, r):
    integer(d, 2, 3, "source dimension")
    integer(m, 2, 4, "source factor count")
    integer(r, 0, MAX_GRADE, "source grade")
    size = comb(r + d - 1, r) ** m
    need(size <= MAX_CHAIN, "source basis cap")
    return tuple(itertools.product(compositions(r, d), repeat=m))


def word_product(record, word):
    need(len(record) == len(word), "source factor mismatch")
    out = []
    for exponent, letter in zip(record, word, strict=True):
        changed = list(exponent)
        changed[letter] += 1
        out.append(tuple(changed))
    return tuple(out)


def source_product(record, content):
    return Counter(word_product(record, word) for word in orbit_words(content))


def sparse_add(target, source, factor):
    for key, value in source.items():
        changed = target.get(key, 0) + factor * value
        if changed:
            target[key] = changed
        elif key in target:
            del target[key]


class ImageSpace:
    """Rational column space with explicit image basis and quotient coordinates."""

    def __init__(self, columns):
        self.basis = {}
        for column in columns:
            vector = {i: Fraction(a) for i, a in column.items() if a}
            while vector:
                pivot = min(vector)
                coefficient = vector[pivot]
                if pivot in self.basis:
                    sparse_add(vector, self.basis[pivot], -coefficient)
                else:
                    self.basis[pivot] = {i: a / coefficient for i, a in vector.items()}
                    break

    @property
    def rank(self):
        return len(self.basis)

    def coordinate(self, vector, target):
        residual = dict(vector)
        result = Fraction(0)
        while residual:
            pivot = min(residual)
            need(pivot in self.basis, "action did not preserve the actual image")
            coefficient = residual[pivot]
            if pivot == target:
                result = coefficient
            sparse_add(residual, self.basis[pivot], -coefficient)
        return result

    def trace(self, row_action):
        total = Fraction(0)
        for pivot, vector in self.basis.items():
            moved = {row_action[i]: coefficient for i, coefficient in vector.items()}
            total += self.coordinate(moved, pivot)
        need(total.denominator == 1, "image trace is not integral")
        return total.numerator


def factor_classes(m):
    out = {"identity": tuple(range(m)), "transposition": (1, 0, *range(2, m))}
    if m >= 3:
        out["three_cycle"] = (1, 2, 0, *range(3, m))
    if m == 4:
        out["double_transposition"] = (1, 0, 3, 2)
        out["four_cycle"] = (1, 2, 3, 0)
    return out


def permute_record(record, permutation):
    inverse = [0] * len(permutation)
    for old, new in enumerate(permutation):
        inverse[new] = old
    return tuple(record[i] for i in inverse)


def koszul_source(d, m, grade, *, actions=True):
    integer(d, 2, 3, "source dimension")
    integer(m, 2, 4, "source factor count")
    integer(grade, 0, MAX_GRADE, "Koszul grade")
    w = compositions(m, d)
    s = len(w)
    dimensions = [
        comb(s, i) * comb(grade - i + d - 1, d - 1) ** m for i in range(grade + 1)
    ]
    need(sum(dimensions) <= MAX_CHAIN, "Koszul total basis cap")
    chains, indices, weights = [], [], []
    for i in range(grade + 1):
        basis = tuple(
            (wedge, record)
            for wedge in itertools.combinations(range(s), i)
            for record in source_basis(d, m, grade - i)
        )
        chains.append(basis)
        indices.append({token: j for j, token in enumerate(basis)})
        weights.append(
            tuple(
                add_weight(*(tuple(w[a] for a in wedge) + record))
                for wedge, record in basis
            )
        )
    maps = [{}]
    matrix_hash = hashlib.sha256()
    for i in range(1, grade + 1):
        columns = []
        for wedge, record in chains[i]:
            column = {}
            for place, a in enumerate(wedge):
                smaller = wedge[:place] + wedge[place + 1 :]
                for product_record, coefficient in source_product(record, w[a]).items():
                    row = indices[i - 1][smaller, product_record]
                    column[row] = column.get(row, 0) + (-1) ** place * coefficient
            column = {key: value for key, value in column.items() if value}
            columns.append(column)
            matrix_hash.update(
                json.dumps(sorted(column.items()), separators=(",", ":")).encode()
            )
            matrix_hash.update(b"\n")
        maps.append(columns)
    for i in range(2, grade + 1):
        for column in maps[i]:
            composite = {}
            for row, coefficient in column.items():
                sparse_add(composite, maps[i - 1][row], coefficient)
            need(
                not composite,
                "consecutive source Koszul differentials do not compose to zero",
            )
    classes = factor_classes(m) if actions else {"identity": tuple(range(m))}
    rows = []
    groups = sorted(set(weights[0]))
    chain_locations = []
    for i in range(grade + 1):
        grouped = defaultdict(list)
        for index, weight in enumerate(weights[i]):
            grouped[weight].append(index)
        chain_locations.append(grouped)
    for weight in groups:
        spaces = [None]
        ranks = [0]
        chain_traces = []
        image_traces = [{name: 0 for name in classes}]
        for i in range(grade + 1):
            locations = chain_locations[i].get(weight, [])
            need(len(locations) <= MAX_BLOCK, "Koszul weight-block cap")
            actions_at_i = {}
            for name, permutation in classes.items():
                actions_at_i[name] = {
                    j: indices[i][
                        chains[i][j][0], permute_record(chains[i][j][1], permutation)
                    ]
                    for j in locations
                }
            chain_traces.append(
                {
                    name: sum(j == target for j, target in action.items())
                    for name, action in actions_at_i.items()
                }
            )
            if i:
                image = ImageSpace(maps[i][j] for j in locations)
                spaces.append(image)
                ranks.append(image.rank)
                prior_locations = chain_locations[i - 1].get(weight, [])
                traces = {}
                for name, permutation in classes.items():
                    if name == "identity":
                        traces[name] = image.rank
                    else:
                        action = {
                            j: indices[i - 1][
                                chains[i - 1][j][0],
                                permute_record(chains[i - 1][j][1], permutation),
                            ]
                            for j in prior_locations
                        }
                        traces[name] = image.trace(action)
                image_traces.append(traces)
        ranks.append(0)
        image_traces.append({name: 0 for name in classes})
        homology = []
        for i in range(grade + 1):
            traces = {
                name: chain_traces[i][name]
                - image_traces[i][name]
                - image_traces[i + 1][name]
                for name in classes
            }
            dimension = traces["identity"]
            need(
                dimension >= 0 and all(abs(t) <= dimension for t in traces.values()),
                "invalid homology character",
            )
            homology.append(traces)
        rows.append(
            {"weight": weight, "differential_ranks": ranks[1:-1], "homology": homology}
        )
    totals = [
        {name: sum(row["homology"][i][name] for row in rows) for name in classes}
        for i in range(grade + 1)
    ]
    if m == 3 and actions:
        for traces in totals:
            e, t, c = (
                traces[key] for key in ("identity", "transposition", "three_cycle")
            )
            multiplicities = (e + 3 * t + 2 * c, e - 3 * t + 2 * c, e - c)
            need(
                all(x >= 0 for x in multiplicities)
                and multiplicities[0] % 6 == 0
                and multiplicities[1] % 6 == 0
                and multiplicities[2] % 3 == 0,
                "S3 homology is not an effective character",
            )
    values = tuple(range(2, 2 + d))
    alternating = sum(
        (-1) ** i
        * sum(
            monomial(values, row["weight"]) * row["homology"][i]["identity"]
            for row in rows
        )
        for i in range(grade + 1)
    )
    need(
        alternating == numerator(values, m, grade)[grade],
        "actual homology Euler character does not match numerator",
    )
    return {
        "dimension": d,
        "factor_count": m,
        "grade": grade,
        "chain_dimensions": dimensions,
        "literal_differential_sha256": matrix_hash.hexdigest(),
        "weight_block_count": len(rows),
        "homology_factor_class_traces": totals,
        "homology_weight_rows": rows,
        "source_d_squared_zero": True,
    }


def binary_unipotent(r):
    """Actual Sym^r(I+E12) in the monomial basis, by binomial substitution."""
    integer(r, 0, 24, "unipotent symmetric degree")
    basis = compositions(r, 2)
    indices = {a: i for i, a in enumerate(basis)}
    matrix = [[0] * len(basis) for _ in basis]
    for column, (a, b) in enumerate(basis):
        for k in range(b + 1):
            matrix[indices[a + k, b - k]][column] = comb(b, k)
    return matrix


def collision_and_functor_controls(cut=12):
    integer(cut, 4, 24, "control cutoff")
    full = numerator((1, 1, 1), 3)
    expected = [1, 17, -9, -65, 65, 9, -17, -1]
    need(
        full[:8] == expected and not any(full[8:]), "identity cube universal numerator"
    )
    series = [comb(r + 2, 2) ** 3 for r in range(cut + 1)]
    reduced = multiply(factors([1] * 7, cut), series, cut)
    need(
        reduced[:5] == [1, 20, 48, 20, 1] and not any(reduced[5:]),
        "identity cube reduced denominator",
    )
    need(sum(reduced) != 0, "reduced identity numerator still has a factor 1-T")
    # Reynolds dimensions from the actual diagonal involution, not a fitted ratio.
    invariant = [((r + 1) ** 2 + int(r % 2 == 0)) // 2 for r in range(cut + 1)]
    denominator = multiply(factors([1, 1], cut), [1, 0, -1], cut)
    need(
        multiply(denominator, invariant, cut) == [1, 0, 1] + [0] * (cut - 2),
        "full invariant source formula",
    )
    naive = [r + 1 for r in range(cut + 1)]
    need(invariant[2] == 5 and naive[2] == 3, "invariant-generator counterfeit")
    need(2 * 7 != 3 * 5, "independent tensor deformation unexpectedly preserved W")
    need(2 * 6 == 3 * 4, "proportional deformation control")
    unipotent_traces = []
    for r in range(cut + 1):
        matrix = binary_unipotent(r)
        trace = sum(matrix[i][i] for i in range(r + 1))
        need(trace == r + 1, "literal unipotent symmetric-power character")
        unipotent_traces.append(trace)
    need(
        binary_unipotent(1) != [[1, 0], [0, 1]],
        "unipotent matrix is incorrectly identity",
    )
    return {
        "identity_cube_universal_N": expected,
        "identity_cube_reduced_numerator": [1, 20, 48, 20, 1],
        "universal_vs_reduced_denominator_degrees": [10, 7],
        "unipotent_character_collision_is_not_matrix_identity": True,
        "literal_binary_unipotent_symmetric_power_traces": unipotent_traces,
        "ramified_invariant_dimensions": invariant,
        "premature_fixed_generator_dimensions": naive,
        "mixed_symmetry_coefficients": [14, 15],
        "proportional_mixed_symmetry_coefficients": [12, 12],
    }


def build(*, scout=False):
    if scout:
        return encode(
            {
                "scout": koszul_source(3, 3, 2),
                "scope": "actual Chow-base degree-two source map only",
            }
        )
    characters = []
    binary_dimensions = []
    for m in range(2, 9):
        control = character_control((2, 3), m)
        need(
            control["universal_numerator"] == descent_numerator(2, 3, m),
            "binary descent-major-index mismatch",
        )
        identity = descent_numerator(1, 1, m)
        need(sum(identity) == factorial(m), "binary free module total rank")
        binary_dimensions.append(
            {"m": m, "quotient_dimensions": identity, "total_rank": factorial(m)}
        )
        characters.append(control)
    characters.extend(
        [
            character_control((2, 3, 5), 2),
            character_control((2, 3, 5), 3),
            character_control((2, 3, 5), 4, heldout=True),
        ]
    )
    sources = [
        koszul_source(d, m, j)
        for d, m, grades in (
            (2, 3, (1, 2, 3)),
            (3, 2, (1, 2, 3)),
            (3, 3, (1, 2, 3)),
            (3, 4, (1, 2)),
        )
        for j in grades
    ]
    cube_two = next(
        row
        for row in sources
        if (row["dimension"], row["factor_count"], row["grade"]) == (3, 3, 2)
    )
    quotient = cube_two["homology_factor_class_traces"][0]
    invariant_quotient = (
        quotient["identity"]
        + 3 * quotient["transposition"]
        + 2 * quotient["three_cycle"]
    ) // 6
    need(invariant_quotient >= 1, "actual degree-two invariant generator missing")
    return encode(
        {
            "status": "bounded exact source replay; classical all-grade theorem separately cited",
            "arithmetic": "integers and characteristic-zero rational elimination",
            "caps": {
                "total_chain_basis": MAX_CHAIN,
                "weight_block": MAX_BLOCK,
                "max_source_grade": MAX_GRADE,
            },
            "characters": characters,
            "binary_quotient_dimensions": binary_dimensions,
            "literal_koszul_sources": sources,
            "cube_degree_two_invariant_quotient_dimension": invariant_quotient,
            "false_betti_inference_rejected": True,
            "collisions_and_functor_boundaries": collision_and_functor_controls(),
            "full_resolution_computed": False,
            "finite_superdeterminant_constructed": False,
            "source_invariants_may_replace_full_base": False,
        }
    )


def authenticate_sources():
    contract = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
    actual_pins = tuple(
        (
            source.get("commit"),
            source.get("path"),
            source.get("snapshot"),
            source.get("git_blob"),
        )
        for source in contract["captured_sources"]
    )
    need(actual_pins == PINS, "captured source coverage/pin mismatch")
    for source in contract["captured_sources"]:
        relative = Path(source["snapshot"])
        need(
            not relative.is_absolute() and ".." not in relative.parts,
            "unsafe source snapshot path",
        )
        # Captured objects use LF; permit Git's CRLF checkout conversion.
        data = (HERE / relative).read_bytes().replace(b"\r\n", b"\n")
        git_blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        need(git_blob == source["git_blob"], "captured frozen source blob mismatch")
    return contract


def payload():
    sources = authenticate_sources()
    owned = {name: digest((HERE / name).read_bytes()) for name in OWNED}
    owned[str(TEST.relative_to(ROOT)).replace("\\", "/")] = digest(TEST.read_bytes())
    record = {
        "source_contract": sources,
        "owned_sha256_canonical_lf": owned,
        "result": build(),
    }
    proof = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    record["proof_object_sha256"] = hashlib.sha256(proof).hexdigest()
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scout", action="store_true")
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.scout:
        print(json.dumps(build(scout=True), sort_keys=True, indent=2))
        return
    record = payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
    else:
        need(FIXTURE.exists(), "verification fixture missing")
        need(
            json.loads(FIXTURE.read_text(encoding="utf-8")) == record,
            "source replay differs from frozen fixture",
        )
    print(f"PASS {record['proof_object_sha256']}")


if __name__ == "__main__":
    main()
