"""Exact finite controls for the five-node Schwarzian no-go."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_five_node_schwarzian_no_go"
NOTE = HERE / "XI_FIVE_NODE_SCHWARZIAN_NO_GO.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
FR = "13c236591b144dd69502e831874c0505b6d8267d"
ZF = "b7112aa9c8c96aae60e8d0a8ad9fe3b36ffc88ea"
PREREG = "d593846375390b1ad76c5b5ff129003271009ea3"
MAX_BYTES = 1_000_000
DISCOVERY_X = tuple(map(Q, (1, 2, 3, 4, 5)))
DISCOVERY_ATOMS = ((Q(1), Q(2)), (Q(4), Q(4)))
HELDOUT_X = tuple(map(Q, (1, 2, 4, 6, 9)))
HELDOUT_ATOMS = ((Q(2), Q(3)), (Q(7), Q(5)))
SOURCES = (
    (PREREG, "research/exploratory/XI_FIVE_NODE_SCHWARZIAN_NO_GO.md"),
    (FR, "research/exploratory/XI_FOUR_NODE_FAR_ZERO_RESERVE.md"),
    (FR, "research/exploratory/xi_four_node_far_zero_reserve.py"),
    (ZF, "research/exploratory/XI_ZERO_FEATURE_FORM_DOMAIN_OBSTRUCTION.md"),
)
CONTRACT = {
    "schema": "xi-five-node-schwarzian-no-go-v1",
    "arithmetic_class": "EXACT_RATIONAL",
    "discovery": "x=1,2,3,4,5; atoms (1,2),(4,4); decrease p(1) by 1/100; scouted before preregistration",
    "heldout": "A same cell epsilon 1e-6; B fixed new base decrease p(1) 1e-5; C fixed new base increase p(16) 1e-5",
    "finite_scope": "two fixed two-atom bases; all five coordinate directions; exact polynomial reconstruction",
    "analytic_result": "global C-infinity countermodel preserves full lower scalar package and paired positive Schwarzians but fails one five-node determinant",
    "xi_boundary": "abstract countermodel only; actual-Xi order-five residual remains open",
    "no_claim": "an actual-Xi negative packet, order-five Xi positivity, RH, source-kernel positivity, external novelty",
    "caps": {
        "bytes": MAX_BYTES,
        "integer_bits": 16384,
        "nodes": 100000,
        "depth": 24,
        "matrix": 5,
    },
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def pack(q):
    q = Q(q)
    return [q.numerator, q.denominator]


def unpack(pair):
    require(
        type(pair) is list and len(pair) == 2 and all(type(x) is int for x in pair),
        "rational shape",
    )
    require(pair[1] > 0, "rational denominator")
    q = Q(*pair)
    require(pack(q) == pair, "noncanonical rational")
    return q


def validate_tree(value, depth=0, visits=None):
    visits = [0] if visits is None else visits
    visits[0] += 1
    require(depth <= 24 and visits[0] <= 100000, "tree cap")
    if value is None or type(value) is bool:
        return
    if type(value) is int:
        require(value.bit_length() <= 16384, "integer cap")
        return
    if type(value) is str:
        require(value.isascii() and len(value) <= 4096, "string cap")
        return
    require(type(value) in (dict, list) and len(value) <= 4096, "container/type cap")
    if type(value) is dict:
        require(
            all(type(k) is str and k.isascii() and len(k) <= 4096 for k in value),
            "key cap",
        )
    for item in value.values() if type(value) is dict else value:
        validate_tree(item, depth + 1, visits)


def load(path):
    data = path.read_bytes()
    require(len(data) <= MAX_BYTES, "file cap")

    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    value = json.loads(
        data,
        object_pairs_hook=pairs,
        parse_constant=lambda _: require(False, "nonfinite JSON"),
    )
    validate_tree(value)
    return value


def parity(perm):
    return (
        -1
        if sum(
            perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))
        )
        % 2
        else 1
    )


def det_permutation(matrix):
    n = len(matrix)
    require(n <= 5 and all(len(row) == n for row in matrix), "matrix cap")
    return sum(
        Q(parity(p)) * math.prod(matrix[i][p[i]] for i in range(n))
        for p in itertools.permutations(range(n))
    )


def det_elimination(matrix):
    a = [list(row) for row in matrix]
    out = Q(1)
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if a[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = -out
        p = a[col][col]
        out *= p
        for j in range(col, len(a)):
            a[col][j] /= p
        for i in range(col + 1, len(a)):
            f = a[i][col]
            for j in range(col, len(a)):
                a[i][j] -= f * a[col][j]
    return out


def minor(matrix, row, col):
    return [r[:col] + r[col + 1 :] for i, r in enumerate(matrix) if i != row]


def adjugate(matrix):
    n = len(matrix)
    return [
        [Q((-1) ** (i + j)) * det_elimination(minor(matrix, j, i)) for j in range(n)]
        for i in range(n)
    ]


def matvec(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def base_values(xs, atoms):
    return [sum(w / (x * x + s) for s, w in atoms) for x in xs]


def matrix(xs, ps):
    fs = [x * p for x, p in zip(xs, ps, strict=True)]
    return [
        [(fs[i] + fs[j]) / (xs[i] + xs[j]) for j in range(len(xs))]
        for i in range(len(xs))
    ]


def perturb(xs, atoms, index, epsilon, direction=-1):
    ps = base_values(xs, atoms)
    ps[index] += direction * epsilon
    h = matrix(xs, ps)
    minors = []
    for n in range(1, 6):
        for indices in itertools.combinations(range(5), n):
            sub = [[h[i][j] for j in indices] for i in indices]
            de, dp = det_elimination(sub), det_permutation(sub)
            require(de == dp, "determinant route mismatch")
            minors.append({"indices": list(indices), "det": pack(de)})
    return {
        "x": [pack(x) for x in xs],
        "atoms": [[pack(s), pack(w)] for s, w in atoms],
        "index": index,
        "epsilon": pack(epsilon),
        "direction": direction,
        "minors": minors,
    }


def polynomial(xs, atoms, index):
    def value(epsilon):
        ps = base_values(xs, atoms)
        ps[index] -= epsilon
        h = matrix(xs, ps)
        de, dp = det_elimination(h), det_permutation(h)
        require(de == dp, "polynomial determinant route mismatch")
        return de

    y0, y1, y2 = value(Q(0)), value(Q(1)), value(Q(2))
    c = (y2 - 2 * y1 + y0) / 2
    b = y1 - y0 - c
    for e in (Q(-2), Q(-1), Q(1, 10)):
        require(value(e) == y0 + b * e + c * e * e, "quadratic reconstruction mismatch")
    return {
        "index": index,
        "constant": pack(y0),
        "linear": pack(b),
        "quadratic": pack(c),
        "checks": [[pack(e), pack(value(e))] for e in (Q(-2), Q(-1), Q(1, 10))],
    }


def residual_control(xs, atoms, index=None, epsilon=Q(0), direction=-1):
    ps = base_values(xs, atoms)
    if index is not None:
        ps[index] += direction * epsilon
    h = matrix(xs, ps)
    m = [row[:4] for row in h[:4]]
    v = [row[4] for row in h[:4]]
    d = det_elimination(m)
    av = matvec(adjugate(m), v)
    c = [-z for z in av] + [d]
    left = dot(c, matvec(h, c))
    right = d * det_elimination(h)
    require(left == right, "adjugate residual mismatch")
    wrong = av + [d]
    wrong_value = dot(wrong, matvec(h, wrong))
    if d != 0:
        require(wrong_value != right, "orientation hostile failed")
    return {
        "anchor_det": pack(d),
        "full_det": pack(det_elimination(h)),
        "residual_identity": pack(left),
        "wrong_orientation": pack(wrong_value),
    }


def source_manifest():
    rows = []
    for commit, path in SOURCES:
        data = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
        blob = subprocess.check_output(
            ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
        ).strip()
        rows.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": blob,
                "sha256_lf": sha(lf(data)),
            }
        )
    return {
        "schema": "xi-five-node-schwarzian-no-go-sources-v1",
        "authoring_base": ZF,
        "preregistered_design": PREREG,
        "sources": rows,
        "external_primary": [],
        "external_content_machine_authenticated": False,
    }


def artifact_seals():
    return {
        str(path.relative_to(ROOT)).replace("\\", "/"): sha(lf(path.read_bytes()))
        for path in (NOTE, Path(__file__), TEST, MANIFEST)
    }


def build():
    discovery = perturb(DISCOVERY_X, DISCOVERY_ATOMS, 0, Q(1, 100))
    heldout = [
        {"label": "A", **perturb(DISCOVERY_X, DISCOVERY_ATOMS, 0, Q(1, 1_000_000))},
        {"label": "B", **perturb(HELDOUT_X, HELDOUT_ATOMS, 0, Q(1, 100_000))},
        {"label": "C", **perturb(HELDOUT_X, HELDOUT_ATOMS, 2, Q(1, 100_000), 1)},
    ]
    require(
        all(unpack(cell["det"]) > 0 for cell in discovery["minors"][:-1]),
        "discovery proper minor",
    )
    require(unpack(discovery["minors"][-1]["det"]) < 0, "discovery full sign")
    polynomials = {
        "discovery_base": [
            polynomial(DISCOVERY_X, DISCOVERY_ATOMS, k) for k in range(5)
        ],
        "heldout_base": [polynomial(HELDOUT_X, HELDOUT_ATOMS, k) for k in range(5)],
    }
    target = polynomials["discovery_base"][0]
    require(
        unpack(target["constant"]) == 0
        and unpack(target["linear"]) == Q(-243, 2169288277812500)
        and unpack(target["quadratic"]) == Q(-483, 533978653000000),
        "discovery polynomial",
    )
    singular = residual_control(DISCOVERY_X, ((Q(1), Q(2)),))
    require(
        unpack(singular["anchor_det"]) == 0
        and unpack(singular["residual_identity"]) == 0,
        "singular residual control",
    )
    value = {
        "schema": CONTRACT["schema"],
        "contract": CONTRACT,
        "discovery": discovery,
        "heldout": heldout,
        "polynomials": polynomials,
        "residual": {
            "regular": residual_control(DISCOVERY_X, DISCOVERY_ATOMS, 0, Q(1, 100)),
            "singular": singular,
        },
        "artifacts": artifact_seals(),
    }
    value["payload_sha256"] = sha(canonical(value))
    return value


def validate(value):
    require(
        type(value) is dict
        and set(value)
        == {
            "schema",
            "contract",
            "discovery",
            "heldout",
            "polynomials",
            "residual",
            "artifacts",
            "payload_sha256",
        },
        "top schema",
    )
    require(
        value["schema"] == CONTRACT["schema"] and value["contract"] == CONTRACT,
        "contract",
    )
    require(value == build(), "fresh reconstruction mismatch")
    payload = {k: v for k, v in value.items() if k != "payload_sha256"}
    require(value["payload_sha256"] == sha(canonical(payload)), "payload seal")
    require(load(MANIFEST) == source_manifest(), "source lock")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--emit-sources", action="store_true")
    parser.add_argument("--write-fixture", action="store_true")
    args = parser.parse_args()
    if args.write_fixture:
        FIXTURE.write_bytes(canonical(build()))
    elif args.emit_sources:
        print(canonical(source_manifest()).decode(), end="")
    elif args.emit:
        print(canonical(build()).decode(), end="")
    elif args.check:
        validate(load(FIXTURE))
        print("PASS")
    else:
        print(canonical(build()).decode(), end="")


if __name__ == "__main__":
    main()
