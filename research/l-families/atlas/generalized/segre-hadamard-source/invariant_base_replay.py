"""Actual binary Chow quotient and its invariant-base matrix factorization.

No third-party package, executable predecessor, or numerical rank is used.
Nontrivial execution belongs to the parent's serialized job queue.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "a895f47628b0bc7c7ee5e0392df2f79c24166f92"
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = (
    ("MATHEMATICS.md", "bbd847461b4955a93b4533fa687cdd8724e2347c"),
    ("verification.json", "310ffc95cb6eaf19281de52dd18d2f2884bc0f49"),
)
OWNED = (
    "INVARIANT_BASE_MATRIX_FACTORIZATION.md",
    "INVARIANT_BASE_REPLAY.md",
    "invariant_base_replay.py",
)
TEST = ROOT / "tests/test_segre_hadamard_invariant_base.py"
FIXTURE = HERE / "invariant_base.verification.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label="integer"):
    need(type(value) is int and low <= value <= high, f"{label} outside declared cap")
    return value


def canonical_bytes(path):
    return path.read_bytes().replace(b"\r\n", b"\n")


def blob_id(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def authenticate_source():
    for name, expected in PINS:
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"],
            cwd=ROOT,
            text=True,
        ).strip()
        need(actual == expected, "frozen Git source binding differs")
        need(
            blob_id(canonical_bytes(HERE / name)) == expected, "working source differs"
        )
    return {"freeze": FREEZE, "pins": [list(row) for row in PINS]}


def rank(columns, row_count):
    integer(row_count, 0, 200, "matrix rows")
    need(len(columns) <= 200, "matrix column cap")
    pivots = {}
    for column in columns:
        current = {}
        for row, value in column.items():
            integer(row, 0, row_count - 1, "matrix row index")
            need(type(value) in (int, Fraction), "exact matrix entry required")
            if value:
                current[row] = Fraction(value)
        while current:
            leading = min(current)
            if leading not in pivots:
                scale = current[leading]
                pivots[leading] = {r: v / scale for r, v in current.items()}
                break
            scale = current[leading]
            for row, value in pivots[leading].items():
                updated = current.get(row, 0) - scale * value
                if updated:
                    current[row] = updated
                else:
                    current.pop(row, None)
    return len(pivots)


def compose(left, right):
    """Sparse column matrices: left after right."""
    answer = []
    for column in right:
        current = {}
        for middle, coefficient in column.items():
            need(0 <= middle < len(left), "composition index outside source")
            for row, value in left[middle].items():
                current[row] = current.get(row, 0) + coefficient * value
        answer.append({r: v for r, v in current.items() if v})
    return answer


def binary_chow_quotient(degree):
    integer(degree, 0, 3, "binary Chow degree")
    basis = list(itertools.product(range(degree + 1), repeat=3))
    index = {word: i for i, word in enumerate(basis)}
    columns = []
    parity_columns = [[], []]
    if degree:
        for previous in itertools.product(range(degree), repeat=3):
            for negative_degree in range(4):
                column = {}
                for subset in itertools.combinations(range(3), negative_degree):
                    word = tuple(a + int(i in subset) for i, a in enumerate(previous))
                    column[index[word]] = 1
                columns.append(column)
                parity_columns[(sum(previous) + negative_degree) % 2].append(column)
    source_parity = [sum(sum(word) % 2 == p for word in basis) for p in (0, 1)]
    image_parity = [rank(part, len(basis)) for part in parity_columns]
    need(sum(image_parity) == rank(columns, len(basis)), "parity rank decomposition")
    quotient = [a - b for a, b in zip(source_parity, image_parity, strict=True)]
    return {
        "grade": degree,
        "source_dimension": len(basis),
        "literal_W_multiplication_columns": len(columns),
        "source_plus_minus": source_parity,
        "image_plus_minus": image_parity,
        "quotient_plus_minus": quotient,
    }


def normal_form(a, b):
    integer(a, 0, 32, "y1 exponent")
    integer(b, 0, 32, "y2 exponent")
    need((a + b) % 2 == 0, "invariant monomial requires even total degree")
    v = a % 2
    return ((a - v) // 2, v, (b - v) // 2)


def invariant_presentation(max_degree=12):
    integer(max_degree, 0, 12, "presentation cutoff")
    rows = []
    for degree in range(0, max_degree + 1, 2):
        forms = [normal_form(a, degree - a) for a in range(degree + 1)]
        need(len(set(forms)) == degree + 1, "invariant normal forms not distinct")
        for a, (u, v, w) in enumerate(forms):
            need((2 * u + v, v + 2 * w) == (a, degree - a), "wrong source monomial")
        rows.append({"degree": degree, "normal_form_count": len(forms)})
    return rows


def polynomial_product(left, right):
    answer = {}
    for a, x in left.items():
        for b, y in right.items():
            weight = tuple(i + j for i, j in zip(a, b, strict=True))
            answer[weight] = answer.get(weight, 0) + x * y
    return {w: c for w, c in answer.items() if c}


def matrix_factorization():
    u, v, w = {(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
    matrix = [[{e: -c for e, c in v.items()}, {e: -c for e, c in w.items()}], [u, v]]
    square = [[{} for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for monomial, value in polynomial_product(
                    matrix[i][k], matrix[k][j]
                ).items():
                    square[i][j][monomial] = square[i][j].get(monomial, 0) + value
            square[i][j] = {e: c for e, c in square[i][j].items() if c}
    expected = {(1, 0, 1): -1, (0, 2, 0): 1}
    need(square == [[expected, {}], [{}, expected]], "polynomial D squared identity")
    return {
        "relation": "u*w-v^2",
        "D_squared": "-(u*w-v^2)*I_2",
        "identity_checked_before_quotient": True,
        "entries_have_degree": 2,
    }


def pi_columns(internal_degree):
    integer(internal_degree, 1, 13, "module internal degree")
    need(internal_degree % 2 == 1, "odd module degree required")
    d = internal_degree - 1
    return [{a + 1: 1} for a in range(d + 1)] + [{a: 1} for a in range(d + 1)]


def differential_columns(internal_degree, homological_degree):
    integer(internal_degree, 1, 13, "module internal degree")
    need(internal_degree % 2 == 1, "odd module degree required")
    integer(homological_degree, 1, (internal_degree - 1) // 2, "homological degree")
    d = internal_degree - 1 - 2 * homological_degree
    target_half = d + 3
    first = [{a + 1: -1, target_half + a + 2: 1} for a in range(d + 1)]
    second = [{a: -1, target_half + a + 1: 1} for a in range(d + 1)]
    return first + second


def resolution_slice(internal_degree):
    integer(internal_degree, 1, 13, "module internal degree")
    need(internal_degree % 2 == 1, "odd module degree required")
    top = (internal_degree - 1) // 2
    dimensions = [2 * (internal_degree - 2 * i) for i in range(top + 1)]
    maps = [pi_columns(internal_degree)] + [
        differential_columns(internal_degree, i) for i in range(1, top + 1)
    ]
    target_dimensions = [internal_degree + 1, *dimensions[:-1]]
    ranks = [
        rank(matrix, target)
        for matrix, target in zip(maps, target_dimensions, strict=True)
    ]
    need(ranks[0] == internal_degree + 1, "augmentation not onto odd source")
    for left, right in itertools.pairwise(maps):
        need(not any(compose(left, right)), "matrix complex composition is nonzero")
    for i, dimension in enumerate(dimensions):
        next_rank = ranks[i + 1] if i < top else 0
        need(dimension - ranks[i] == next_rank, "nonexact bounded source slice")
    return {
        "internal_degree": internal_degree,
        "odd_source_dimension": internal_degree + 1,
        "free_slice_dimensions": dimensions,
        "augmentation_then_differential_ranks": ranks,
        "all_compositions_zero": True,
        "exact_in_every_present_homological_degree": True,
    }


def a_dimension(n):
    if n < 0:
        return 0
    return sum((n - d + 1) * (d + 1) for d in range(0, n + 1, 2))


def m_dimension(n):
    if n < 0:
        return 0
    return sum((n - d + 1) * (d + 1) for d in range(1, n + 1, 2))


def hilbert_controls(cut=16):
    integer(cut, 4, 24, "Hilbert cutoff")
    source, decomposition, free = [], [], []
    for n in range(cut + 1):
        literal = sum(
            sum(word) % 2 == 0 for word in itertools.product(range(n + 1), repeat=3)
        )
        need(literal == ((n + 1) ** 3 + int(n % 2 == 0)) // 2, "literal source parity")
        module = (
            a_dimension(n)
            + 2 * a_dimension(n - 1)
            + 2 * m_dimension(n - 1)
            + m_dimension(n - 2)
        )
        false_free = (
            a_dimension(n)
            + 2 * a_dimension(n - 1)
            + 4 * a_dimension(n - 2)
            + 2 * a_dimension(n - 3)
        )
        need(literal == module, "actual module/source Hilbert mismatch")
        alternating = false_free
        for i in range(1, n // 2 + 1):
            alternating += (-1) ** i * (
                4 * a_dimension(n - 2 - 2 * i) + 2 * a_dimension(n - 3 - 2 * i)
            )
        need(alternating == literal, "minimal-resolution Euler series mismatch")
        source.append(literal)
        decomposition.append(module)
        free.append(false_free)
    need((source[4], free[4]) == (63, 67), "false finite-free control changed")
    return {
        "cutoff": cut,
        "literal_source_invariants": source,
        "full_invariant_base_decomposition": decomposition,
        "false_free_on_minimal_generators": free,
        "first_false_free_difference": next(
            i for i, (a, b) in enumerate(zip(source, free, strict=True)) if a != b
        ),
        "all_present_minimal_resolution_rows_used": True,
    }


def build_payload():
    provenance = authenticate_source()
    provenance["owned_sha256_lf"] = {
        name: hashlib.sha256(canonical_bytes(HERE / name)).hexdigest() for name in OWNED
    }
    provenance["test_sha256_lf"] = hashlib.sha256(canonical_bytes(TEST)).hexdigest()
    quotient = [binary_chow_quotient(n) for n in range(4)]
    need(
        [row["quotient_plus_minus"] for row in quotient]
        == [[1, 0], [2, 2], [0, 1], [0, 0]],
        "actual binary quotient changed",
    )
    return {
        "schema": "segre-hadamard-full-invariant-base/v1",
        "provenance": provenance,
        "literal_Chow_quotient": quotient,
        "invariant_base_normal_forms": invariant_presentation(),
        "polynomial_matrix_factorization": matrix_factorization(),
        "exact_source_resolution_slices": [
            resolution_slice(n) for n in range(1, 14, 2)
        ],
        "source_module_Hilbert_comparison": hilbert_controls(),
        "proved_not_inferred_from_cutoff": [
            "infinite exact minimal resolution",
            "infinite projective dimension over the singular invariant base",
            "finite maximal Cohen-Macaulay module of rank six",
        ],
        "not_claimed": [
            "canonical choice of the free or invariant-module splitting",
            "finite free resolution after taking invariants",
            "a new abstract hypersurface periodicity theorem",
            "arithmetic or infinite-operator completion",
        ],
    }


def serialized(payload):
    return json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def check_payload(candidate):
    need(
        serialized(candidate) == serialized(build_payload()),
        "payload differs from exact source replay",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.write:
        FIXTURE.write_text(serialized(payload), encoding="utf-8", newline="\n")
    else:
        need(FIXTURE.exists(), "missing invariant-base fixture")
        need(
            FIXTURE.read_text(encoding="utf-8") == serialized(payload),
            "fixture differs from exact source replay",
        )
    print(
        json.dumps(
            {"status": "PASS", "schema": payload["schema"], "resolution_slices": 7}
        )
    )


if __name__ == "__main__":
    main()
