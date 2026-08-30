"""Bounded exact replay for fixed-label directed-cycle responses.

No numerical eigenvalues, zero searches, external packages, or assert-based
acceptance. Matrices in this replay are rational; the complex-unitary theorem
is a prose theorem, not a claim that a finite census proves it.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_DIM = 8
MAX_DET_DIM = 6
MAX_TRACE = 8
MAX_CYCLE = 6
MAX_BITS = 128
SOURCE = {
    "schema": "riemann.fixed-label-cycle-source.v1",
    "vertices": [0, 1],
    "edges": [[0, 1, "a"], [1, 0, "b"], [0, 0, "c"]],
    "reversal": "reverse incidence, retain every color and numerical label",
    "cycle_convention": "directed edge words modulo rotation, not reversal; returns allowed",
    "sheet_trivialization": "one fixed labeled copy at each vertex",
    "s3_U": [1, 0, 2],
    "s3_V": [0, 2, 1],
    "alignment": "W=(UV)^T for the exact real-orthogonal fixtures",
    "held_out_s4_pairs": [
        [[1, 0, 2, 3], [0, 2, 3, 1]],
        [[1, 2, 3, 0], [1, 0, 2, 3]],
        [[1, 0, 3, 2], [2, 3, 0, 1]],
    ],
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int, name: str) -> int:
    require(type(value) is int and low <= value <= high, f"invalid {name}")
    return value


def matrix(rows):
    require(type(rows) in (list, tuple), "matrix must be a list or tuple")
    n = integer(len(rows), 1, MAX_DIM, "dimension")
    out = []
    for row in rows:
        require(type(row) in (list, tuple) and len(row) == n, "matrix must be square")
        values = []
        for x in row:
            require(type(x) in (int, Q), "matrix entries must be exact rationals")
            q = Q(x)
            require(
                max(abs(q.numerator).bit_length(), q.denominator.bit_length())
                <= MAX_BITS,
                "rational entry too large",
            )
            values.append(q)
        out.append(tuple(values))
    return tuple(out)


def eye(n):
    integer(n, 1, MAX_DIM, "dimension")
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    require(len(a) == len(b), "matrix dimensions differ")
    n = len(a)
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(n)), Q(0)) for j in range(n))
        for i in range(n)
    )


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def traces(a, count):
    a = matrix(a)
    integer(count, 1, MAX_TRACE, "trace count")
    power = eye(len(a))
    out = []
    for _ in range(count):
        power = mul(power, a)
        out.append(trace(power))
    return out


def permutation(values):
    require(type(values) in (tuple, list), "permutation must be a list or tuple")
    n = integer(len(values), 1, MAX_DIM // 2, "permutation degree")
    require(
        all(type(x) is int for x in values) and sorted(values) == list(range(n)),
        "invalid permutation",
    )
    return matrix([[int(values[i] == j) for j in range(n)] for i in range(n)])


def lift(u, v, w, reverse=False):
    u, v, w = matrix(u), matrix(v), matrix(w)
    d = len(u)
    require(len(v) == len(w) == d and 2 * d <= MAX_DIM, "invalid label dimensions")
    require(type(reverse) is bool, "reverse must be boolean")
    upper, lower = (v, u) if reverse else (u, v)
    return matrix(
        [list(w[i]) + list(upper[i]) for i in range(d)]
        + [list(lower[i]) + [Q(0)] * d for i in range(d)]
    )


def source_lift(labels, reverse=False):
    """Construct from primitive edge incidence, separately from the block formula."""
    require(
        type(labels) is dict and set(labels) == {"a", "b", "c"}, "three labels required"
    )
    require(type(reverse) is bool, "reverse must be boolean")
    checked = {key: matrix(value) for key, value in labels.items()}
    d = len(checked["a"])
    require(
        all(len(a) == d for a in checked.values()) and 2 * d <= MAX_DIM,
        "invalid source label dimensions",
    )
    out = [[Q(0)] * (2 * d) for _ in range(2 * d)]
    for start, end, color in SOURCE["edges"]:
        if reverse:
            start, end = end, start
        for i in range(d):
            for j in range(d):
                out[start * d + i][end * d + j] += checked[color][i][j]
    return matrix(out)


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def det_poly_leibniz(a):
    """Independent exact determinant of I-tA by finite permutation expansion."""
    a = matrix(a)
    n = integer(len(a), 1, MAX_DET_DIM, "determinant dimension")
    out = [Q(0)] * (n + 1)
    for p in itertools.permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        product = [Q((-1) ** inversions)]
        for i, j in enumerate(p):
            product = pmul(product, [Q(i == j), -a[i][j]])
        for i, value in enumerate(product):
            out[i] += value
    return trim(out)


def det_poly_newton(a):
    """Independent trace/Newton construction, including the full degree."""
    a = matrix(a)
    ts = traces(a, len(a))
    coefficients = [Q(1)]
    for k in range(1, len(a) + 1):
        coefficients.append(
            -sum((coefficients[k - j] * ts[j - 1] for j in range(1, k + 1)), Q(0)) / k
        )
    return trim(coefficients)


def inverse_series(poly, limit):
    integer(limit, 0, MAX_TRACE, "series limit")
    require(poly and poly[0] == 1, "constant coefficient must be one")
    out = [Q(1)]
    for n in range(1, limit + 1):
        out.append(
            -sum((poly[j] * out[n - j] for j in range(1, min(n + 1, len(poly)))), Q(0))
        )
    return out


def edge_list(a):
    a = matrix(a)
    require(
        all(x.denominator == 1 and 0 <= x <= 2 for row in a for x in row),
        "cycle fixture needs nonnegative integer adjacency of multiplicity <=2",
    )
    edges = []
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            edges.extend((i, j) for _ in range(int(value)))
    require(len(edges) <= 16, "too many edges for bounded cycle replay")
    return edges


def walk_counts(a, count):
    """Edge-list dynamic programming, independent of matrix multiplication."""
    integer(count, 1, MAX_TRACE, "walk count")
    edges = edge_list(a)
    n = len(a)
    counts = [0] * count
    for start in range(n):
        current = [int(j == start) for j in range(n)]
        for step in range(count):
            nxt = [0] * n
            for src, dst in edges:
                nxt[dst] += current[src]
            counts[step] += nxt[start]
            current = nxt
    return counts


def primitive_cycles(a, limit):
    """Enumerate primitive closed EDGE words; rotations identified, reversal retained."""
    integer(limit, 1, MAX_CYCLE, "primitive cycle limit")
    edges = edge_list(a)
    outgoing = [[] for _ in range(len(a))]
    for idx, (src, _) in enumerate(edges):
        outgoing[src].append(idx)
    seen = [set() for _ in range(limit + 1)]
    visits = 0

    def visit(start, vertex, word):
        nonlocal visits
        visits += 1
        require(visits <= 200_000, "cycle visit cap exceeded")
        if word and vertex == start:
            size = len(word)
            primitive = not any(
                size % k == 0 and word == word[:k] * (size // k) for k in range(1, size)
            )
            if primitive:
                seen[size].add(min(word[k:] + word[:k] for k in range(size)))
        if len(word) == limit:
            return
        for edge in outgoing[vertex]:
            visit(start, edges[edge][1], word + (edge,))

    for start in range(len(a)):
        visit(start, start, ())
    return [len(seen[n]) for n in range(1, limit + 1)]


def euler_coefficients(cycles):
    limit = integer(len(cycles), 1, MAX_CYCLE, "Euler truncation")
    out = [Q(1)] + [Q(0)] * limit
    for length, count in enumerate(cycles, start=1):
        integer(count, 0, 10_000, "primitive count")
        for _ in range(count):
            # Multiplication by (1-t^length)^(-1), increasing order is essential.
            for j in range(length, limit + 1):
                out[j] += out[j - length]
    return out


def commutator_energy(u, v):
    u, v = matrix(u), matrix(v)
    require(len(u) == len(v), "label dimensions differ")
    ident = eye(len(u))
    require(
        mul(transpose(u), u) == ident and mul(transpose(v), v) == ident,
        "exact replay of energy requires real orthogonal labels",
    )
    uv, vu = mul(u, v), mul(v, u)
    w = transpose(uv)
    gap = traces(lift(u, v, w), 3)[2] - traces(lift(u, v, w, True), 3)[2]
    norm = sum(
        ((uv[i][j] - vu[i][j]) ** 2 for i in range(len(u)) for j in range(len(u))), Q(0)
    )
    require(gap == Q(3, 2) * norm, "commutator energy identity failed")
    return gap, norm


def strings(values):
    return [str(x) for x in values]


def cycle_fixture(name, a):
    determinant = det_poly_leibniz(a)
    require(determinant == det_poly_newton(a), "determinant methods disagree")
    ts = traces(a, MAX_CYCLE)
    walks = walk_counts(a, MAX_CYCLE)
    cycles = primitive_cycles(a, MAX_CYCLE)
    require(ts == walks, "matrix traces disagree with edge-list walks")
    for n in range(1, MAX_CYCLE + 1):
        require(
            sum(d * cycles[d - 1] for d in range(1, n + 1) if n % d == 0)
            == walks[n - 1],
            "primitive/rooted walk identity failed",
        )
    require(
        euler_coefficients(cycles) == inverse_series(determinant, MAX_CYCLE),
        "primitive Euler product disagrees with determinant inverse",
    )
    return {
        "name": name,
        "determinant": strings(determinant),
        "traces": strings(ts),
        "closed_walks": walks,
        "primitive_cycles": cycles,
        "inverse_series": strings(inverse_series(determinant, MAX_CYCLE)),
    }


def build_payload():
    loaded = json.loads((HERE / "source.json").read_text(encoding="utf-8"))
    require(loaded == SOURCE, "primitive source contract differs")
    u, v = permutation(SOURCE["s3_U"]), permutation(SOURCE["s3_V"])
    w = transpose(mul(u, v))
    base = source_lift({key: [[1]] for key in ("a", "b", "c")})
    labels = {"a": u, "b": v, "c": w}
    original, reverse = source_lift(labels), source_lift(labels, True)
    require(
        original == lift(u, v, w) and reverse == lift(u, v, w, True),
        "source incidence and independent block construction disagree",
    )
    fixtures = [
        cycle_fixture("base", base),
        cycle_fixture("s3", original),
        cycle_fixture("s3_reversed_source", reverse),
    ]
    require(
        det_poly_newton(original) == [1, 0, 0, -4, 0, 0, -1], "S3 polynomial mismatch"
    )
    require(
        det_poly_newton(reverse) == [1, 0, 0, -1, -3, -3, -1],
        "reversed S3 polynomial mismatch",
    )
    require(
        lift(transpose(u), transpose(v), transpose(w), True) == transpose(original),
        "simultaneous transpose duality failed",
    )
    # Every assignment in S1 and S2, not just aligned pairs.
    small_count = 0
    for d in (1, 2):
        perms = [permutation(p) for p in itertools.permutations(range(d))]
        for a, b, c in itertools.product(perms, repeat=3):
            require(
                det_poly_newton(lift(a, b, c)) == det_poly_newton(lift(a, b, c, True)),
                "small-cover blindness failed",
            )
            small_count += 1
    s3_rows = []
    for p, q in itertools.product(itertools.permutations(range(3)), repeat=2):
        gap, norm = commutator_energy(permutation(p), permutation(q))
        s3_rows.append(
            {
                "U": list(p),
                "V": list(q),
                "trace_gap": str(gap),
                "norm_squared": str(norm),
            }
        )
    held_out = []
    for p, q in SOURCE["held_out_s4_pairs"]:
        gap, norm = commutator_energy(permutation(p), permutation(q))
        held_out.append(
            {"U": p, "V": q, "trace_gap": str(gap), "norm_squared": str(norm)}
        )
    a, b = matrix([[0, 1], [1, 0]]), matrix([[1, 0], [0, -1]])
    gap, norm = commutator_energy(a, b)
    aligned = transpose(mul(a, b))
    d1, d2 = (
        det_poly_leibniz(lift(a, b, aligned)),
        det_poly_leibniz(lift(a, b, aligned, True)),
    )
    require(
        d1 == [1, 0, 1, -2, 1] and d2 == [1, 0, 1, 2, 1],
        "orthogonal polynomials mismatch",
    )
    source_hashes = {}
    for path in (
        "source.json",
        "cycle_response.py",
        "tests/test_cycle_response.py",
        "MATHEMATICS.md",
        "README.md",
    ):
        source_hashes[path] = hashlib.sha256(
            (HERE / path).read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
    return {
        "schema": "riemann.fixed-label-cycle-response.verification.v1",
        "status": "PASS",
        "arithmetic": "EXACT_RATIONAL",
        "rh_established": False,
        "source_hash_normalization": "bytes with CRLF normalized to LF",
        "source_sha256": source_hashes,
        "caps": {
            "matrix_dimension": MAX_DIM,
            "Leibniz_dimension": MAX_DET_DIM,
            "trace_length": MAX_TRACE,
            "cycle_length": MAX_CYCLE,
            "cycle_visits": 200000,
        },
        "cycle_fixtures": fixtures,
        "all_small_permutation_assignments_checked": small_count,
        "all_s3_aligned_pairs": s3_rows,
        "held_out_s4_pairs": held_out,
        "orthogonal_dimension_two": {
            "determinant": strings(d1),
            "reversed_determinant": strings(d2),
            "trace_gap": str(gap),
            "norm_squared": str(norm),
        },
        "not_computationally_proved": [
            "all-size prose theorems",
            "external novelty",
            "arithmetic transfer",
            "RH or GRH",
        ],
    }


def canonical(value):
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    payload["payload_sha256"] = hashlib.sha256(canonical(payload).encode()).hexdigest()
    rendered = canonical(payload)
    path = HERE / "verification.json"
    if args.write:
        path.write_bytes(rendered.encode("utf-8"))
    else:
        require(
            path.read_bytes() == rendered.encode("utf-8"),
            "fixture differs from complete replay",
        )
    print("PASS_FIXED_LABEL_CYCLE_RESPONSE")
    print("proof_object=" + payload["payload_sha256"])
    print("RH_UNPROVEN")


if __name__ == "__main__":
    main()
