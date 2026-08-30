"""Exact bounded based-word holonomy replay; no assertion-based acceptance."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
LIBRARY = HERE.parent / "fixed-label-cycle-response" / "cycle_response.py"
LIBRARY_COMMIT = "26314df4e5ed9a5c16b7da61e155a48d325789cc"
LIBRARY_SHA256 = "e269f7a32fe2bb4b8501b15350d02d2cc0b8ece6bab58df054872cf6ee98c883"
SOURCE = {
    "schema": "riemann.marked-holonomy-source.v1",
    "source_group": "free group on a,b; c=(ab)^-1",
    "clock": "one per automaton edge, not reduced free-group length",
    "words": [["c", "a", "b"], ["c", "b", "a"]],
    "equivalence": "simultaneous conjugation of the based representation",
    "census_degrees": [1, 2, 3],
    "held_out_s4_pairs": [
        [[1, 0, 2, 3], [0, 2, 3, 1]],
        [[1, 2, 3, 0], [1, 0, 2, 3]],
        [[1, 0, 3, 2], [2, 3, 0, 1]],
    ],
    "maximum_degree": 4,
    "maximum_full_transfer_dimension": 6,
    "maximum_sparse_lift_vertices": 12,
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


require(digest(LIBRARY.read_bytes()) == LIBRARY_SHA256, "matrix library changed")
_spec = importlib.util.spec_from_file_location("cycle_exact", LIBRARY)
c = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c)


def authenticate_library():
    require(digest(LIBRARY.read_bytes()) == LIBRARY_SHA256, "working library changed")
    path = LIBRARY.relative_to(REPO).as_posix()
    result = subprocess.run(
        ["git", "cat-file", "blob", f"{LIBRARY_COMMIT}:{path}"],
        cwd=REPO,
        capture_output=True,
        check=False,
        timeout=10,
    )
    require(result.returncode == 0, "frozen library Git source is unavailable")
    require(digest(result.stdout) == LIBRARY_SHA256, "frozen library hash mismatch")
    require(digest(LIBRARY.read_bytes()) == LIBRARY_SHA256, "working library changed")


def orthogonal_pair(u, v):
    u, v = c.matrix(u), c.matrix(v)
    require(len(u) == len(v) <= 4, "label dimension cap")
    identity = c.eye(len(u))
    require(c.mul(c.transpose(u), u) == identity, "U must be exactly orthogonal")
    require(c.mul(c.transpose(v), v) == identity, "V must be exactly orthogonal")
    return u, v


def word_operator(u, v, reverse=False):
    u, v = orthogonal_pair(u, v)
    require(type(reverse) is bool, "word choice must be boolean")
    labels = {"a": u, "b": v, "c": c.transpose(c.mul(u, v))}
    out = c.eye(len(u))
    for letter in SOURCE["words"][int(reverse)]:
        out = c.mul(out, labels[letter])
    return out


def transfer(u, v, reverse=False):
    """Independent edge/block construction, bounded before allocation."""
    u, v = orthogonal_pair(u, v)
    d = len(u)
    require(3 * d <= 6, "full transfer dimension cap")
    require(type(reverse) is bool, "word choice must be boolean")
    labels = {"a": u, "b": v, "c": c.transpose(c.mul(u, v))}
    out = [[c.Q(0)] * (3 * d) for _ in range(3 * d)]
    for i, letter in enumerate(SOURCE["words"][int(reverse)]):
        for r in range(d):
            for s in range(d):
                out[i * d + r][((i + 1) % 3) * d + s] = labels[letter][r][s]
    return c.matrix(out)


def substitute_clock(poly):
    require(1 <= len(poly) <= 5, "return polynomial degree cap")
    out = [c.Q(0)] * (3 * (len(poly) - 1) + 1)
    for i, x in enumerate(poly):
        out[3 * i] = x
    return c.trim(out)


def permutation_cycle_lengths(a):
    a = c.matrix(a)
    require(len(a) <= 4, "permutation degree cap")
    require(all(x in (0, 1) for row in a for x in row), "not a permutation")
    require(all(sum(row) == 1 for row in a), "not a permutation")
    require(all(sum(row) == 1 for row in c.transpose(a)), "not a permutation")
    mapping = [row.index(1) for row in a]
    seen, lengths = set(), []
    for i in range(len(a)):
        if i in seen:
            continue
        length, j = 0, i
        while j not in seen:
            seen.add(j)
            length += 1
            j = mapping[j]
        lengths.append(length)
    return sorted(lengths)


def cycle_product(lengths):
    require(type(lengths) is list and 1 <= len(lengths) <= 4, "cycle count cap")
    require(all(type(n) is int and 1 <= n <= 4 for n in lengths), "cycle length cap")
    require(sum(lengths) <= 4, "total degree cap")
    out = [c.Q(1)]
    for n in lengths:
        out = c.pmul(out, [c.Q(1)] + [c.Q(0)] * (3 * n - 1) + [c.Q(-1)])
    return out


def literal_lift_cycles(u, v, reverse=False):
    """Walk the finite lifted permutation graph, without a dense lift matrix."""
    u, v = orthogonal_pair(u, v)
    d = len(u)
    require(3 * d <= 12, "sparse lift vertex cap")
    require(type(reverse) is bool, "word choice must be boolean")
    labels = {"a": u, "b": v, "c": c.transpose(c.mul(u, v))}
    for label in labels.values():
        permutation_cycle_lengths(label)
    mapping = []
    for i, letter in enumerate(SOURCE["words"][int(reverse)]):
        for r in range(d):
            mapping.append(((i + 1) % 3) * d + labels[letter][r].index(1))
    seen, lengths = set(), []
    for i in range(3 * d):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            j = mapping[j]
            length += 1
        lengths.append(length)
    return sorted(lengths)


def row(p, q):
    u, v = c.permutation(p), c.permutation(q)
    a, b = word_operator(u, v), word_operator(u, v, True)
    require(a == c.eye(len(p)), "identity word failed")
    polynomials = []
    cycles = []
    for reverse, operator in enumerate((a, b)):
        direct = c.det_poly_leibniz(operator)
        require(
            direct == c.det_poly_newton(operator), "independent determinant mismatch"
        )
        polynomial = substitute_clock(direct)
        lengths = permutation_cycle_lengths(operator)
        require(polynomial == cycle_product(lengths), "lifted cycle product mismatch")
        require(
            literal_lift_cycles(u, v, bool(reverse)) == [3 * n for n in lengths],
            "literal lifted graph contradicts return-cycle prediction",
        )
        polynomials.append([str(x) for x in polynomial])
        cycles.append([3 * n for n in lengths])
    gap = 3 * (c.trace(a) - c.trace(b))
    uv, vu = c.mul(u, v), c.mul(v, u)
    norm = sum((uv[i][j] - vu[i][j]) ** 2 for i in range(len(p)) for j in range(len(p)))
    require(gap == c.Q(3, 2) * norm, "commutator energy mismatch")
    return {
        "U": list(p),
        "V": list(q),
        "determinants": polynomials,
        "lifted_cycle_lengths": cycles,
        "trace_gap": str(gap),
        "norm_squared": str(norm),
    }


def payload():
    require(
        json.loads((HERE / "source.json").read_text(encoding="utf-8")) == SOURCE,
        "primitive word source mismatch",
    )
    authenticate_library()
    census = []
    for d in SOURCE["census_degrees"]:
        for p, q in itertools.product(itertools.permutations(range(d)), repeat=2):
            census.append(row(p, q))
    held_out = [row(p, q) for p, q in SOURCE["held_out_s4_pairs"]]
    u, v = c.matrix([[0, 1], [1, 0]]), c.matrix([[1, 0], [0, -1]])
    full_controls = []
    for reverse in (False, True):
        a = transfer(u, v, reverse)
        direct = c.det_poly_leibniz(a)
        require(direct == c.det_poly_newton(a), "full transfer determinant mismatch")
        require(
            direct
            == substitute_clock(c.det_poly_leibniz(word_operator(u, v, reverse))),
            "word/full transfer mismatch",
        )
        full_controls.append([str(x) for x in direct])
    files = (
        "README.md",
        "source.json",
        "holonomy_response.py",
        "tests/test_holonomy_response.py",
    )
    return {
        "schema": "riemann.marked-holonomy-verification.v1",
        "status": "PASS",
        "arithmetic": "EXACT_RATIONAL",
        "rh_established": False,
        "source": SOURCE,
        "library": {"commit": LIBRARY_COMMIT, "sha256": LIBRARY_SHA256},
        "source_sha256": {path: digest((HERE / path).read_bytes()) for path in files},
        "census": census,
        "held_out": held_out,
        "orthogonal_full_controls": full_controls,
        "not_computationally_proved": [
            "all-dimensional unitary theorem",
            "arithmetic adapter",
            "novelty",
        ],
    }


def canonical(value):
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = payload()
    result["payload_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    encoded = canonical(result).encode()
    path = HERE / "verification.json"
    if args.write:
        path.write_bytes(encoded)
    else:
        require(path.read_bytes() == encoded, "complete canonical replay differs")
    print("PASS_MARKED_HOLONOMY_RESPONSE")
    print("proof_object=" + result["payload_sha256"])
    print("FINITE_MODEL_ONLY; RH_UNPROVEN")


if __name__ == "__main__":
    main()
