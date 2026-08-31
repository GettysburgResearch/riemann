"""Nonauthor primitive controls for the frozen Segre bridge.

No code from the source producer is imported. Coordinate-swap connectivity
replaces its syzygy rank elimination. Nondiagonal symmetric-power matrices
replace its eigenvalue recurrence inputs. All arithmetic is exact.
"""

import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = "4a317ea5c9d7aa016fba58a1d74746e437329ec7"
SOURCE_PATHS = (
    "research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md",
    "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.py",
    "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.json",
    "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.sources.json",
    "tests/test_segre_recurrence_syzygy_bridge.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_locks():
    result = {}
    for path in SOURCE_PATHS:
        raw = subprocess.check_output(["git", "show", f"{SOURCE}:{path}"], cwd=ROOT)
        current = (ROOT / path).read_bytes()
        require(
            raw.replace(b"\r\n", b"\n") == current.replace(b"\r\n", b"\n"),
            "frozen source changed",
        )
        result[path] = hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()
    return result


def swap_graph():
    axes = list(product(range(3), repeat=3))
    index = {axis: i for i, axis in enumerate(axes)}
    monomials = list(combinations_with_replacement(range(27), 3))
    positions = {monomial: i for i, monomial in enumerate(monomials)}
    forest = list(range(len(monomials)))

    def find(i):
        while forest[i] != i:
            forest[i] = forest[forest[i]]
            i = forest[i]
        return i

    def weight(monomial):
        return tuple(tuple(sorted(axes[i][j] for i in monomial)) for j in range(3))

    edges = set()
    for row, monomial in enumerate(monomials):
        for first, second in combinations(range(3), 2):
            for coordinate in range(3):
                a, b = list(axes[monomial[first]]), list(axes[monomial[second]])
                a[coordinate], b[coordinate] = b[coordinate], a[coordinate]
                changed = list(monomial)
                changed[first], changed[second] = index[tuple(a)], index[tuple(b)]
                other = positions[tuple(sorted(changed))]
                if other != row:
                    edges.add(tuple(sorted((row, other))))
                    forest[find(row)] = find(other)
    by_weight = defaultdict(set)
    cubic_dimensions = Counter()
    for i, monomial in enumerate(monomials):
        w = weight(monomial)
        by_weight[w].add(find(i))
        cubic_dimensions[w] += 1
    require(
        len(by_weight) == 1000 and all(len(v) == 1 for v in by_weight.values()),
        "a cubic weight fibre is disconnected",
    )

    pair_dimensions = Counter(
        weight(pair) for pair in combinations_with_replacement(range(27), 2)
    )
    domain_dimensions = Counter()
    for w, dimension in pair_dimensions.items():
        for a in axes:
            out = tuple(tuple(sorted(w[j] + (a[j],))) for j in range(3))
            domain_dimensions[out] += dimension - 1
    character = {
        w: domain_dimensions[w] - dimension + 1
        for w, dimension in cubic_dimensions.items()
    }
    require(all(v >= 0 for v in character.values()), "negative syzygy weight")
    rows = [
        {"weight": [list(axis) for axis in w], "multiplicity": n}
        for w, n in sorted(character.items())
        if n
    ]
    source_fixture = json.loads((ROOT / SOURCE_PATHS[2]).read_text(encoding="utf-8"))
    require(
        rows == source_fixture["native_cubic_maps"]["cubic_character"],
        "independent whole character mismatch",
    )
    cyclic = [
        sum(n for w, n in character.items() if sum(map(sum, w)) % 3 == residue)
        for residue in range(3)
    ]
    require(cyclic == [568, 576, 576], "independent cyclic character mismatch")
    return {
        "vertices": len(monomials),
        "distinct_swap_edges": len(edges),
        "weight_fibres": len(by_weight),
        "connected_components": len({find(i) for i in forest}),
        "cubic_rank": len(monomials) - len(by_weight),
        "quadrics": sum(n - 1 for n in pair_dimensions.values()),
        "linear_syzygy_domain": sum(domain_dimensions.values()),
        "syzygies": sum(character.values()),
        "nonzero_character_weights": len(rows),
        "cyclic_character": cyclic,
        "character_sha256": hashlib.sha256(canonical(rows).encode()).hexdigest(),
        "author_rank_algorithm_imported": False,
    }


def weak(total):
    return [
        (a, b, total - a - b) for a in range(total + 1) for b in range(total - a + 1)
    ]


def poly_multiply(left, right):
    answer = defaultdict(lambda: sp.Integer(0))
    for a, ca in left.items():
        for b, cb in right.items():
            answer[tuple(a[j] + b[j] for j in range(3))] += ca * cb
    return {key: value for key, value in answer.items() if value}


def symmetric_action(matrix, degree, full=False):
    basis = weak(degree)
    column_powers = []
    for column in range(3):
        linear = {
            tuple(int(i == j) for i in range(3)): matrix[j, column]
            for j in range(3)
            if matrix[j, column]
        }
        powers = [{(0, 0, 0): sp.Integer(1)}]
        for _ in range(degree):
            powers.append(poly_multiply(powers[-1], linear))
        column_powers.append(powers)
    result = sp.zeros(len(basis)) if full else sp.Integer(0)
    lookup = {key: i for i, key in enumerate(basis)}
    for column, exponents in enumerate(basis):
        expansion = {(0, 0, 0): sp.Integer(1)}
        for j, exponent in enumerate(exponents):
            expansion = poly_multiply(expansion, column_powers[j][exponent])
        if full:
            for exponent, coefficient in expansion.items():
                result[lookup[exponent], column] = coefficient
        else:
            result += expansion.get(exponents, 0)
    return result


def matrix_recurrence(matrix):
    sym3 = symmetric_action(matrix, 3, full=True)
    denominator = sym3.charpoly().all_coeffs()
    coefficients = [symmetric_action(matrix, r) ** 3 for r in range(21)]
    numerator = [
        sum(denominator[j] * coefficients[r - j] for j in range(min(r, 10) + 1))
        for r in range(21)
    ]
    require(not any(numerator[8:]), "nondiagonal recurrence failed")
    require(numerator[7] == -(matrix.det() ** 7), "nonzero universal top coefficient")
    t = sp.Symbol("T")
    n = sp.Poly(sum(numerator[j] * t**j for j in range(8)), t)
    d = sp.Poly(sum(denominator[j] * t**j for j in range(11)), t)
    common = sp.gcd(n, d)
    p, q = n.exquo(common), d.exquo(common)
    constant = q.nth(0)
    p, q = sp.Poly(p.as_expr() / constant, t), sp.Poly(q.as_expr() / constant, t)
    hankel = sp.Matrix(10, 10, lambda i, j: coefficients[i + j])
    rank = hankel.rank()
    require(
        rank == q.degree() and q.degree() - p.degree() == 3,
        "nondiagonal Hankel/codimension mismatch",
    )
    return {
        "matrix": [[str(v) for v in matrix.row(i)] for i in range(3)],
        "universal_numerator": [str(n.nth(j)) for j in range(8)],
        "reduced_numerator": [str(p.nth(j)) for j in range(p.degree() + 1)],
        "reduced_denominator": [str(q.nth(j)) for j in range(q.degree() + 1)],
        "Hankel_rank": rank,
        "literal_symmetric_power_traces": 21,
        "eigenvalues_used_to_construct_recurrence": False,
    }


def purity_symbolic():
    x, z = sp.symbols("x z")
    b, c = 2 * x**2 + 5 * x + 2, x**3 + 6 * x**2 + 7 * x + 2
    delta = sp.expand(b**2 - 4 * (c - 2))
    require(sp.Poly(delta, x).count_roots(-2, -1) == 1, "Sturm first interval")
    require(sp.Poly(delta, x).count_roots(-1, 0) == 0, "Sturm second interval")
    require(
        sp.Poly(delta, x).count_roots(sp.Rational(-5, 3), sp.Rational(-13, 8)) == 1,
        "Sturm exact bracket",
    )
    spectrum = z**2 + b * z + c - 2
    require(
        sp.expand(spectrum.subs(z, -2) - x * (x + 3) * (x - 1)) == 0,
        "negative spectral endpoint",
    )
    require(
        sp.expand(spectrum.subs(z, 2) - (x + 1) ** 2 * (x + 8)) == 0,
        "positive spectral endpoint",
    )
    return {
        "discriminant": str(delta),
        "exact_Sturm_counts": [1, 0, 1],
        "rounded_roots_used": False,
    }


def main():
    locks = source_locks()
    matrices = [
        sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]]),
        sp.Matrix([[0, 0, 6], [1, 0, -11], [0, 1, 6]]),
        sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    ]
    report = {
        "review_producer_sha256_lf": hashlib.sha256(
            Path(__file__).read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "source_commit": SOURCE,
        "source_sha256_lf": locks,
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        },
        "independent_swap_graph": swap_graph(),
        "nondiagonal_matrix_panels": [matrix_recurrence(matrix) for matrix in matrices],
        "purity_control": purity_symbolic(),
        "sympy_version": sp.__version__,
        "all_parameter_proof_machine_verified": False,
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report).encode()).hexdigest()
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
