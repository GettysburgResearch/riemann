"""Bounded exact replay for the native Koszul23 analytic-parent proof.

No approximate arithmetic, builds, sweeps, or external algebra packages.
The source relations are reconstructed before any Hilbert-series comparison.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIXTURE = HERE / "verification.json"
FREEZE = "8834fdc7a0dfe15f6bb95eefe0729cb77c93c807"
PRECURSOR = (
    "research/l-families/atlas/generalized/MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md",
    "e34fa2ba38981f37109d6f734c03a67a240e02f3",
    "bcd7ae6890bad68b9b52f896f59cd305edbb7b3d5a5d4f32210e0afef1135b2f",
)
OWNED = (
    "MATHEMATICS.md",
    "README.md",
    "source.json",
    "replay.py",
    "tests/test_replay.py",
)
SOURCE = {
    "schema": "koszul23-primitive-source-v1",
    "field": "C",
    "ranks": [2, 3],
    "generators_row_column": [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]],
    "quadratic_map": "ordered words map to row totals and column totals",
    "dual_relations": "one sum of all ordered words in each quadratic-map fibre",
    "generator_parity": "odd",
    "parent": "dual of the Lie superalgebra generated in the quadratic-dual quotient",
    "arithmetic": "integers, fractions, and Gaussian fractions; no floats",
    "coverage": "all words and all source relation fibres through tensor degree 3; finite controls do not prove Koszulness or analytic continuation",
    "caps": {
        "tensor_degree": 3,
        "tensor_dimension": 216,
        "series_degree": 24,
        "multiplicity_degree": 64,
    },
}
G = tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))
I: G = (Fraction(0), Fraction(1))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("integer, not Boolean or float, required")
    need(low <= value <= high, "integer exceeds bounded replay domain")
    return value


def rational(value: object) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("exact rational required")
    answer = Fraction(value)
    need(
        max(answer.numerator.bit_length(), answer.denominator.bit_length()) <= 64,
        "input rational exceeds 64-bit cap",
    )
    return answer


def add(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def mul(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def neg(a: G) -> G:
    return -a[0], -a[1]


def power(a: G, exponent: int) -> G:
    integer(exponent, 0, 24)
    result = ONE
    for _ in range(exponent):
        result = mul(result, a)
    return result


def unitary_roots(roots: object, rank: int) -> tuple[G, ...]:
    integer(rank, 2, 3)
    need(isinstance(roots, tuple) and len(roots) == rank, "wrong source rank")
    out = []
    for root in roots:
        need(isinstance(root, tuple) and len(root) == 2, "Gaussian pair required")
        item = rational(root[0]), rational(root[1])
        need(item[0] ** 2 + item[1] ** 2 == 1, "unitarity is required")
        out.append(item)
    return tuple(out)


def qjson(value: Fraction | int) -> list[int]:
    value = Fraction(value)
    return [value.numerator, value.denominator]


def gjson(value: G) -> list[list[int]]:
    return [qjson(value[0]), qjson(value[1])]


def normalized(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def sha(data: bytes) -> str:
    return hashlib.sha256(normalized(data)).hexdigest()


def authenticate_source(source: object) -> None:
    # Equality alone would admit True == 1; canonical JSON also binds types.
    need(
        json.dumps(source, sort_keys=True) == json.dumps(SOURCE, sort_keys=True),
        "primitive source contract mismatch",
    )


def authenticate() -> dict[str, object]:
    authenticate_source(json.loads((HERE / "source.json").read_text(encoding="utf-8")))
    path, blob, digest = PRECURSOR
    got_blob = subprocess.check_output(
        ["git", "rev-parse", FREEZE + ":" + path], cwd=ROOT, text=True
    ).strip()
    need(got_blob == blob, "frozen precursor blob mismatch")
    frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
    need(sha(frozen) == digest, "frozen precursor content mismatch")
    need(sha((ROOT / path).read_bytes()) == digest, "working precursor changed")
    return {
        "precursor_commit": FREEZE,
        "precursor_blob": blob,
        "precursor_sha256_lf": digest,
        "owned_sha256_lf": {name: sha((HERE / name).read_bytes()) for name in OWNED},
        "external_theorems": "read and cited in proof; not authenticated by this replay",
    }


def word_weight(word: tuple[int, ...]) -> tuple[int, ...]:
    rows = [0, 0]
    columns = [0, 0, 0]
    for letter in word:
        integer(letter, 0, 5)
        rows[letter // 3] += 1
        columns[letter % 3] += 1
    return tuple(rows + columns)


@cache
def quadratic_fibres() -> tuple[tuple[tuple[int, ...], ...], ...]:
    fibres: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for word in itertools.product(range(6), repeat=2):
        fibres[word_weight(word)].append(word)
    return tuple(tuple(fibres[key]) for key in sorted(fibres))


class Echelon:
    """Sparse exact row reduction; input is bounded by the source word space."""

    def __init__(self, dimension: int):
        self.dimension = integer(dimension, 1, 216)
        self.rows: dict[int, dict[int, Fraction]] = {}

    def insert(self, original: dict[int, Fraction | int]) -> bool:
        need(len(original) <= self.dimension, "oversized sparse row")
        row: dict[int, Fraction] = {}
        for column, value in original.items():
            integer(column, 0, self.dimension - 1)
            value = rational(value)
            if value:
                row[column] = value
        for pivot in sorted(self.rows):
            factor = row.get(pivot, Fraction(0))
            if factor:
                for column, value in self.rows[pivot].items():
                    new = row.get(column, Fraction(0)) - factor * value
                    if new:
                        row[column] = new
                    else:
                        row.pop(column, None)
        if not row:
            return False
        pivot = min(row)
        scale = row[pivot]
        self.rows[pivot] = {column: value / scale for column, value in row.items()}
        return True


def bracket(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
    left_degree: int,
    right_degree: int,
) -> dict[tuple[int, ...], int]:
    integer(left_degree, 1, 2)
    integer(right_degree, 1, 2)
    need(left_degree + right_degree <= 3, "tensor degree cap exceeded")
    out: Counter[tuple[int, ...]] = Counter()
    sign = -1 if (left_degree * right_degree) % 2 else 1
    for a, ac in left.items():
        for b, bc in right.items():
            out[a + b] += ac * bc
            out[b + a] -= sign * ac * bc
    return {word: coefficient for word, coefficient in out.items() if coefficient}


@cache
def source_grade(degree: int) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
    integer(degree, 1, 3)  # enforced before word-space allocation
    words = tuple(itertools.product(range(6), repeat=degree))
    positions = {word: i for i, word in enumerate(words)}
    basis = Echelon(len(words))
    if degree >= 2:
        for split in range(degree - 1):
            for prefix in itertools.product(range(6), repeat=split):
                for suffix in itertools.product(range(6), repeat=degree - 2 - split):
                    for fibre in quadratic_fibres():
                        basis.insert(
                            {positions[prefix + term + suffix]: 1 for term in fibre}
                        )
    ideal_rank = len(basis.rows)
    generators = [{(i,): 1} for i in range(6)]
    seconds = [
        bracket(generators[i], generators[j], 1, 1)
        for i in range(6)
        for j in range(i, 6)
    ]
    candidates = generators if degree == 1 else seconds
    if degree == 3:
        candidates = [
            bracket(generator, second, 1, 2)
            for generator in generators
            for second in seconds
        ]
    weights = []
    for candidate in candidates:
        if not candidate:
            continue
        candidate_weights = {word_weight(word) for word in candidate}
        need(len(candidate_weights) == 1, "source bracket is not weight homogeneous")
        if basis.insert({positions[word]: value for word, value in candidate.items()}):
            weights.append(next(iter(candidate_weights)))
    return len(words) - ideal_rank, ideal_rank, tuple(sorted(weights))


def mobius(n: int) -> int:
    integer(n, 1, 64)
    count, divisor, remaining = 0, 2, n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            count += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        count += 1
    return (-1) ** count


def multiplicity(n: int) -> int:
    integer(n, 1, 64)
    total = sum(
        mobius(d) * (4 + (-1) ** (n // d + 1) * 2 ** (n // d))
        for d in range(1, n + 1)
        if n % d == 0
    )
    signed = (-1) ** (n + 1) * total
    need(signed % n == 0 and signed >= 0, "finite deviation integrality failed")
    return signed // n


def hilbert(degree: int) -> list[int]:
    integer(degree, 0, 24)
    return [(r + 1) * math.comb(r + 2, 2) for r in range(degree + 1)]


def signed_euler_series(degree: int) -> list[int]:
    integer(degree, 0, 24)
    out = [1] + [0] * degree
    for n in range(1, degree + 1):
        count = multiplicity(n)
        factor = [0] * (degree + 1)
        for k in range(degree // n + 1):
            factor[n * k] = (
                (-1) ** k * math.comb(count, k)
                if n % 2 == 0
                else math.comb(count + k - 1, k)
            )
        out = [
            sum(out[j] * factor[i - j] for j in range(i + 1)) for i in range(degree + 1)
        ]
    return out


def complete_symmetric(roots: tuple[G, ...], degree: int) -> list[G]:
    integer(degree, 0, 24)
    out = [ONE] + [ZERO] * degree
    for root in roots:
        for r in range(1, degree + 1):
            out[r] = add(out[r], mul(root, out[r - 1]))
    return out


def gpoly_mul(a: list[G], b: list[G]) -> list[G]:
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = add(out[i + j], mul(left, right))
    return out


def character(
    weights: tuple[tuple[int, ...], ...], a: tuple[G, ...], b: tuple[G, ...]
) -> G:
    answer = ZERO
    for weight in weights:
        term = ONE
        for root, exponent in zip(a + b, weight, strict=True):
            term = mul(term, power(root, exponent))
        answer = add(answer, term)
    return answer


def equivariant_control(a: object, b: object, degree: int = 12) -> dict[str, object]:
    integer(degree, 3, 24)
    a = unitary_roots(a, 2)
    b = unitary_roots(b, 3)
    det_a, det_b = mul(a[0], a[1]), mul(mul(b[0], b[1]), b[2])
    tr_a = add(a[0], a[1])
    tr_b = add(add(b[0], b[1]), b[2])
    wedge_b = add(add(mul(b[0], b[1]), mul(b[0], b[2])), mul(b[1], b[2]))
    expected_chars = (
        mul(tr_a, tr_b),
        mul(det_a, wedge_b),
        mul(mul(tr_a, det_a), det_b),
    )
    source_chars = tuple(character(source_grade(n)[2], a, b) for n in (1, 2, 3))
    need(
        source_chars == expected_chars,
        "source Lie characters do not match native modules",
    )
    denominator = [ONE]
    for x in a:
        for y in b:
            denominator = gpoly_mul(denominator, [ONE, neg(mul(x, y))])
    ha, hb = complete_symmetric(a, degree), complete_symmetric(b, degree)
    sequence = [mul(x, y) for x, y in zip(ha, hb, strict=True)]
    actual = gpoly_mul(denominator, sequence)[: degree + 1]
    expected = [ONE, ZERO, neg(expected_chars[1]), expected_chars[2]] + [ZERO] * (
        degree - 3
    )
    need(actual == expected, "native finite-resolution character identity failed")
    return {
        "a": [gjson(x) for x in a],
        "b": [gjson(x) for x in b],
        "source_characters_M1_M2_M3": [gjson(x) for x in source_chars],
        "numerator": [gjson(x) for x in actual[:4]],
        "coverage_through_degree": degree,
    }


def log_tail_bound(radius: int | Fraction, cut: int) -> Fraction:
    radius = rational(radius)
    integer(cut, 1, 10)
    need(0 <= radius < Fraction(1, 2), "strict trace-class radius required")
    return 3 * (2 * radius) ** (cut + 1) / ((1 - radius) * (1 - 2 * radius))


def enclosure(t: int | Fraction, cut: int) -> dict[str, object]:
    t = rational(t)
    delta = log_tail_bound(abs(t), cut)
    need(delta < 1, "tail bound too large for rational exponential enclosure")
    finite = Fraction(1)
    for n in range(1, cut + 1):
        factor = (1 - t**n) ** multiplicity(n)
        finite = finite * factor if n % 2 == 0 else finite / factor
    exact = (1 + 2 * t) / (1 - t) ** 4
    lower, upper = (1 - delta) * finite, finite / (1 - delta)
    need(lower <= exact <= upper, "certified finite-product enclosure failed")
    return {
        "t": qjson(t),
        "cut": cut,
        "log_tail_bound": qjson(delta),
        "exact_shadow": qjson(exact),
        "lower": qjson(lower),
        "upper": qjson(upper),
    }


def polynomial_control() -> dict[str, object]:
    """Check the native Hilbert--Burch maps with sparse integer polynomials."""
    zero = (0,) * 6

    def variable(index: int) -> dict[tuple[int, ...], int]:
        term = list(zero)
        term[index] = 1
        return {tuple(term): 1}

    def product(left, right):
        out = Counter()
        for a, ac in left.items():
            for b, bc in right.items():
                out[tuple(x + y for x, y in zip(a, b, strict=True))] += ac * bc
        return {term: value for term, value in out.items() if value}

    def combine(*terms):
        out = Counter()
        for scale, poly in terms:
            for monomial, value in poly.items():
                out[monomial] += scale * value
        return {term: value for term, value in out.items() if value}

    a, b, c, d, e, f = [variable(j) for j in range(6)]
    minors = [
        combine((1, product(a, e)), (-1, product(b, d))),
        combine((1, product(a, f)), (-1, product(c, d))),
        combine((1, product(b, f)), (-1, product(c, e))),
    ]
    for x, y, z in ((c, b, a), (f, e, d)):
        need(
            not combine(
                (1, product(x, minors[0])),
                (-1, product(y, minors[1])),
                (1, product(z, minors[2])),
            ),
            "native syzygy composition is nonzero",
        )
    rank_minor = combine((1, product(b, f)), (-1, product(c, e)))
    need(bool(rank_minor), "source syzygy matrix lacks witnessed rank two")
    return {
        "ordered_minors": ["ae-bd", "af-cd", "bf-ce"],
        "syzygies": [["c", "-b", "a"], ["f", "-e", "d"]],
        "composition_zero": True,
        "nonzero_rank_minor": "bf-ce",
    }


def build_payload() -> dict[str, object]:
    provenance = authenticate()
    grades = []
    for n in (1, 2, 3):
        quotient, ideal, weights = source_grade(n)
        need(len(weights) == multiplicity(n), "low-grade source/Mobius disagreement")
        grades.append(
            {
                "degree": n,
                "word_dimension": 6**n,
                "ideal_rank": ideal,
                "quadratic_dual_dimension": quotient,
                "Lie_dimension": len(weights),
                "parent_torus_weights": [list(weight) for weight in weights],
            }
        )
    euler = signed_euler_series(24)
    need(euler == hilbert(24), "formal signed Euler product fails")
    dual = [
        sum(math.comb(4, i) * 2 ** (n - i) for i in range(min(4, n) + 1))
        for n in range(25)
    ]
    need(
        all(
            sum((-1) ** j * hilbert(24)[j] * dual[n - j] for j in range(n + 1))
            == (1 if n == 0 else 0)
            for n in range(25)
        ),
        "Koszul Hilbert inverse fails",
    )
    pythagoras = (Fraction(3, 5), Fraction(4, 5))
    cases = [
        ((ONE, ONE), (ONE, ONE, ONE)),
        ((ONE, I), (ONE, ONE, ONE)),
        ((I, neg(ONE)), (ONE, I, neg(I))),
        ((pythagoras, neg(I)), (neg(ONE), pythagoras, I)),
    ]
    equivariant = [equivariant_control(a, b) for a, b in cases]
    wrong_dual = character(source_grade(1)[2], (ONE, I), (ONE, ONE, ONE))
    need(
        wrong_dual != (wrong_dual[0], -wrong_dual[1]),
        "wrong-dual control did not separate",
    )
    return {
        "schema": "koszul23-exact-replay-v1",
        "provenance": provenance,
        "source": SOURCE,
        "quadratic_fibre_count": len(quadratic_fibres()),
        "grades": grades,
        "multiplicities_through_64": [multiplicity(n) for n in range(1, 65)],
        "hilbert_through_24": euler,
        "dual_hilbert_through_24": dual,
        "equivariant_cases": equivariant,
        "native_resolution": polynomial_control(),
        "certified_enclosures": [
            enclosure(t, 8) for t in (Fraction(1, 4), Fraction(-1, 4), Fraction(1, 3))
        ],
        "hostile_controls": {
            "wrong_dual_character": gjson((wrong_dual[0], -wrong_dual[1])),
            "correct_M1_character": gjson(wrong_dual),
            "positive_only_degree_2": 24,
            "source_degree_2": 18,
        },
        "not_machine_proved": [
            "Koszul exactness and super PBW",
            "all-grade multiplicity asymptotic",
            "sharp Schatten boundary",
            "all-input equivariant identity",
        ],
    }


def check_payload(candidate: object) -> None:
    expected = build_payload()
    need(
        json.dumps(candidate, sort_keys=True) == json.dumps(expected, sort_keys=True),
        "fixture differs from authenticated complete replay",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        need(
            json.dumps(candidate, sort_keys=True)
            == json.dumps(payload, sort_keys=True),
            "fixture differs from authenticated complete replay",
        )
    print("PASS koszul23 authenticated exact source replay")


if __name__ == "__main__":
    main()
