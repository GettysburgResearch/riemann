"""Exact finite controls for the conditional zero-feature form theorem."""

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
STEM = "xi_zero_feature_form_domain_obstruction"
NOTE = HERE / "XI_ZERO_FEATURE_FORM_DOMAIN_OBSTRUCTION.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "8f01064df805624c045877655893c324a220975d"
SP = "e5e43625b157ecc5f602532e16a1197679594824"
FR = "13c236591b144dd69502e831874c0505b6d8267d"
PREREG = "ca0dae696803b729f8ba618451208a533ba14224"
MAX_BYTES = 1_000_000
MODELS = (
    ((Q(1), 2),),
    ((Q(1), 1), (Q(3), 2)),
    ((Q(1), 1), (Q(2), 2), (Q(5), 3)),
)
PANELS = (
    (Q(3, 4), Q(1), Q(3, 2), Q(2), Q(3)),
    (Q(1), Q(2), Q(4), Q(8), Q(16)),
    (Q(2, 3), Q(5, 6), Q(7, 6), Q(5, 3), Q(5, 2)),
)
MINIMAL_X = (Q(3, 4), Q(1), Q(3, 2), Q(2), Q(3), Q(4))
SOURCES = (
    (PREREG, "research/exploratory/XI_ZERO_FEATURE_FORM_DOMAIN_OBSTRUCTION.md"),
    (SP, "research/exploratory/XI_SOURCE_POLARIZATION_FOUR_NODE.md"),
    (SP, "research/exploratory/xi_source_polarization_four_node.py"),
    (FR, "research/exploratory/XI_FOUR_NODE_FAR_ZERO_RESERVE.md"),
    (BASE, "research/integrated/xi_pick/ORDER_THREE_CANONICAL.md"),
)
CONTRACT = {
    "schema": "xi-zero-feature-form-domain-obstruction-v1",
    "arithmetic_class": "EXACT_RATIONAL",
    "normalization": "H=L2(0,infinity); e_x=exp(-xt); F=Y'/Y; inner products conjugate-linear first",
    "conditional_premise": "RH only for the actual-Xi zero-feature representation",
    "finite_scope": "three synthetic critical spectral measures and three five-node safe panels",
    "finite_role": "algebra/minimality/schema regression only; no Xi zero or prime evaluation",
    "domain_result": "formal V on exponential core has D(V*)={0}; the real-part quadratic form is not closable",
    "operator_boundary": "no T+T*=V*V operator equality and no termwise adjoint of the Euler pieces",
    "no_claim": "RH, source-kernel PSD, prime-positive square root, order-five actual-Xi positivity, external novelty",
    "caps": {
        "bytes": MAX_BYTES,
        "integer_bits": 8192,
        "nodes": 100000,
        "depth": 24,
        "matrix": 6,
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
        require(value.bit_length() <= 8192, "integer cap")
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
    require(n <= 6 and all(len(row) == n for row in matrix), "matrix cap")
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


def features(x, gamma):
    den = x * x + gamma * gamma
    return x / den, gamma / den


def f_value(x, model):
    return sum(Q(2 * m) * x / (x * x + gamma * gamma) for gamma, m in model)


def kernel_direct(x, y, model):
    return (f_value(x, model) + f_value(y, model)) / (x + y)


def kernel_gram(x, y, model, sine=True, pole_sign=1):
    out = Q(0)
    for gamma, m in model:
        x0, x1 = features(x, gamma)
        y0, y1 = features(y, gamma)
        out += Q(2 * m) * (x0 * y0 + (x1 * y1 if sine else 0) * pole_sign)
    return out


def panel(model, xs):
    h = [[kernel_direct(x, y, model) for y in xs] for x in xs]
    gram = [[kernel_gram(x, y, model) for y in xs] for x in xs]
    require(h == gram, "kernel/Gram mismatch")
    minors = []
    for n in range(1, len(xs) + 1):
        for indices in itertools.combinations(range(len(xs)), n):
            sub = [[h[i][j] for j in indices] for i in indices]
            left, right = det_elimination(sub), det_permutation(sub)
            require(left == right and left >= 0, "minor route/sign mismatch")
            minors.append({"indices": list(indices), "det": pack(left)})
    rank_cap = 2 * len(model)
    if len(xs) > rank_cap:
        require(det_elimination(h) == 0, "feature rank cap")
    return {
        "model": [[pack(g), m] for g, m in model],
        "x": [pack(x) for x in xs],
        "rank_cap": rank_cap,
        "minors": minors,
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
        "schema": "xi-zero-feature-form-domain-obstruction-sources-v1",
        "authoring_base": FR,
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
    panels = [panel(model, xs) for model in MODELS for xs in PANELS]
    matrix = []
    for x in MINIMAL_X:
        row = []
        for gamma, _ in MODELS[-1]:
            row.extend(features(x, gamma))
        matrix.append(row)
    minimal_det = det_elimination(matrix)
    require(
        minimal_det == det_permutation(matrix) and minimal_det != 0,
        "finite minimality control",
    )
    x, y, model = Q(1), Q(2), MODELS[-1]
    missing_sine = kernel_gram(x, y, model, sine=False)
    wrong_pole = kernel_gram(x, y, model, pole_sign=-1)
    correct = kernel_direct(x, y, model)
    require(
        missing_sine != correct and wrong_pole != correct, "hostile channel control"
    )
    value = {
        "schema": CONTRACT["schema"],
        "contract": CONTRACT,
        "panels": panels,
        "minimality": {
            "gammas": [pack(g) for g, _ in MODELS[-1]],
            "x": [pack(x) for x in MINIMAL_X],
            "feature_determinant": pack(minimal_det),
        },
        "residues": {
            "plus_coefficients": [[1, 0], [0, -1]],
            "minus_coefficients": [[1, 0], [0, 1]],
            "stacked_determinant_modulus_squared": 4,
            "same_height_multiplicity_aggregated": True,
        },
        "hostile": {
            "correct": pack(correct),
            "missing_sine": pack(missing_sine),
            "wrong_pole_sign": pack(wrong_pole),
            "operator_identity_allowed": False,
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
            "panels",
            "minimality",
            "residues",
            "hostile",
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
