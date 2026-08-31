"""Reviewer reconstruction from Eisenstein series; no author arithmetic imports."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as F
from pathlib import Path

import sympy as S

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized"
STEM = "cusp_weight36_subspace_divisors"
SCIENCE = "0c07ba0e9c6464d3b623f7d997e471544f4e807e"
FIXTURE_HASH = "2c388024ebf80c28abb8eeb049601516568c68219c9f738e53a1a2a8d1a02073"


def need(value, reason):
    if not value:
        raise ValueError(reason)


def sha(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def encoded(v):
    return (json.dumps(v, sort_keys=True, indent=2) + "\n").encode("ascii")


def git(commit, path):
    return subprocess.check_output(
        ["git", "--no-replace-objects", "show", f"{commit}:{path}"], cwd=ROOT
    )


def source():
    raw = git(SCIENCE, f"{DIR}/{STEM}.json")
    need(
        sha(raw) == FIXTURE_HASH == sha((ROOT / DIR / (STEM + ".json")).read_bytes()),
        "fixture SHA",
    )
    data = json.loads(raw)
    unsealed = dict(data)
    expected = unsealed.pop("payload_sha256")
    need(sha(encoded(unsealed)) == expected, "payload seal")
    for path, expected in data["artifact_sha256_lf"].items():
        need(
            sha(git(SCIENCE, path)) == expected == sha((ROOT / path).read_bytes()),
            "science artifact",
        )
    manifest = json.loads(git(SCIENCE, f"{DIR}/{STEM}.sources.json"))
    for row in manifest["frozen_sources"]:
        raw = git(row["commit"], row["path"])
        need(sha(raw) == row["sha256_lf"], "source SHA")
        need(
            hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            == row["git_blob"],
            "source blob",
        )
    return data


def wire(q):
    q = F(q)
    return [q.numerator, q.denominator]


def qmul(a, b):
    return [sum(a[j] * b[n - j] for j in range(n + 1)) for n in range(19)]


def power(a, k):
    out = [1] + [0] * 18
    for _ in range(k):
        out = qmul(out, a)
    return out


def primitive():
    e4 = [1] + [
        240 * sum(d**3 for d in range(1, n + 1) if n % d == 0) for n in range(1, 19)
    ]
    e6 = [1] + [
        -504 * sum(d**5 for d in range(1, n + 1) if n % d == 0) for n in range(1, 19)
    ]
    delta = [F(a - b, 1728) for a, b in zip(power(e4, 3), power(e6, 2))]
    raw = S.Matrix([qmul(power(delta, j), power(e4, 3 * (3 - j))) for j in range(1, 4)])
    basis = raw[:, 1:4].inv() * raw
    need(all(v.q == 1 for v in basis), "integral Miller basis")
    return [[int(basis[i, n]) for n in range(19)] for i in range(3)]


def dconv(a, b):
    out = [F(0)] * 37
    for n in range(1, 37):
        out[n] = sum(a[d] * b[n // d] for d in range(1, n + 1) if n % d == 0)
    return out


def complexq(value):
    return S.Rational(*value[0]) + S.I * S.Rational(*value[1])


VARIABLES = S.symbols("x y z a b c")
x, y, z, a, b, c = VARIABLES
MATRIX = S.Matrix([[x, a, b], [a, y, c], [b, c, z]])
DELTA = S.expand(MATRIX.det())


def polynomial(rows):
    return S.expand(
        sum(
            complexq(r["coefficient"])
            * math.prod(v**e for v, e in zip(VARIABLES, r["exponents"]))
            for r in rows
        )
    )


def run():
    data = source()
    basis = primitive()
    need(basis == data["native_source"]["basis"], "E4/E6 identity primitive basis")
    matrices = {}
    action_cells = 0
    for p in (2, 3):
        t = S.Matrix(
            [
                [
                    basis[j][p * n] + (p**35 * basis[j][n // p] if n % p == 0 else 0)
                    for j in range(3)
                ]
                for n in range(1, 4)
            ]
        )
        need(t.tolist() == data["native_source"][f"T{p}"], "native Hecke matrix")
        for n in range(1, 18 // p + 1):
            for j in range(3):
                lhs = basis[j][p * n] + (p**35 * basis[j][n // p] if n % p == 0 else 0)
                need(
                    lhs == sum(t[i, j] * basis[i][n] for i in range(3)),
                    "complete Hecke action",
                )
                action_cells += 1
        matrices[p] = t
    p = matrices[2].charpoly().as_poly()
    need(
        list(reversed([wire(v) for v in p.all_coeffs()])) == data["native_source"]["P"],
        "charpoly",
    )
    disc = S.discriminant(p.as_expr(), p.gen)
    opposite = S.resultant(p.as_expr(), p.as_expr().subs(p.gen, -p.gen), p.gen)
    need(wire(disc) == data["native_source"]["discriminant"], "discriminant")
    need(
        wire(opposite) == data["native_source"]["opposite_resultant"],
        "opposite resultant",
    )
    need(
        S.gcd(p.as_expr(), p.as_expr().subs(p.gen, -p.gen)) == 1,
        "no opposite or zero root",
    )
    need(matrices[2] * matrices[3] == matrices[3] * matrices[2], "commute")
    need(
        72 * matrices[3]
        == 34416831456 * S.eye(3) + 194184 * matrices[2] - matrices[2] ** 2,
        "q3 polynomial",
    )
    for row in data["native_source"]["root_intervals"]:
        left, right = row["interval"]
        need(p.count_roots(left, right) == 1, "independent Sturm interval")
    entries = [
        [
            [F(0)] + [F(f[n] * g[n], n**35) if n <= 18 else F(0) for n in range(1, 37)]
            for g in basis
        ]
        for f in basis
    ]
    coefficients = [F(0)] * 37
    for perm in itertools.permutations(range(3)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        term = [F(0), F(sign)] + [F(0)] * 35
        for i in range(3):
            term = dconv(term, entries[i][perm[i]])
        coefficients = [a + b for a, b in zip(coefficients, term)]
    square_support = [F(int(n > 0 and math.isqrt(n) ** 2 == n)) for n in range(37)]
    for _ in range(3):
        coefficients = dconv(coefficients, square_support)
    actual = [wire(F(disc) * q / 72**2) for q in coefficients[1:]]
    need(
        actual == [r["coefficient"] for r in data["full_determinant_coefficients"]],
        "all36 convolution coefficients",
    )
    need(S.factor_list(DELTA)[1] == [(DELTA, 1)], "irreducible symmetric determinant")
    need(DELTA == polynomial(data["symmetric_determinant"]), "symmetric determinant")
    target_count = 0
    poly_stream = hashlib.sha256()
    for row in data["subspaces"]:
        v = S.Matrix([[complexq(q) for q in r] for r in row["coefficient_matrix"]])
        restriction = S.expand((S.conjugate(v).T * MATRIX * v).det())
        need(
            restriction == polynomial(row["P_W"]), "full complex restriction polynomial"
        )
        diagonal = S.expand(restriction.subs({a: 0, b: 0, c: 0}))
        need(diagonal == polynomial(row["diagonal_character"]), "Pluecker diagonal")
        need(
            S.expand(complexq(row["gram_determinant"]) - (S.conjugate(v).T * v).det())
            == 0,
            "Gram normalization",
        )
        monomial = len(S.Poly(restriction, *VARIABLES).terms()) == 1
        need(monomial == (row["class"] == "pole_free_Hecke_line"), "classification")
        for label, target in [("zero", row["zero"])] + [
            ("pole", t) for t in row["pole"]
        ]:
            point = [complexq(q) for q in target["matrix_entries"]]
            need(all(q != 0 for q in point), "torus target")
            sub = dict(zip(VARIABLES, point))
            pv, dv = S.expand(restriction.subs(sub)), S.expand(DELTA.subs(sub))
            need(
                (dv == 0 and pv != 0) if label == "zero" else (pv == 0 and dv != 0),
                "protected divisor target",
            )
            target_count += 1
        poly_stream.update(str(restriction).encode())
    # Explicitly declared independent held-out algebra panel, not a Grassmannian census.
    pool = (-2, -1 + S.I, S.Rational(1, 2) + S.I / 3, 2 * S.I, 3 - S.I)
    heldout = 0
    for u, v in itertools.product(pool, repeat=2):
        for matrix in (S.Matrix([1, u, v]), S.Matrix([[1, 0], [0, 1], [u, v]])):
            restriction = S.expand((S.conjugate(matrix).T * MATRIX * matrix).det())
            need(
                len(S.Poly(restriction, *VARIABLES).terms()) > 1, "heldout nonmonomial"
            )
            need(S.gcd(DELTA, restriction) == 1, "heldout coprime denominator")
            need(
                S.expand(restriction.subs({x: 1, y: 1, z: 1, a: 0, b: 0, c: 0})) > 0,
                "heldout positive rank",
            )
            heldout += 1
    report = {
        "schema": "weight36-independent-review-v1",
        "science_commit": SCIENCE,
        "fixture_sha256_lf": FIXTURE_HASH,
        "author_arithmetic_executed": False,
        "native_route": "Delta=(E4^3-E6^2)/1728; inverse pivot matrix",
        "complete_hecke_action_cells": action_cells,
        "source_pins": 7,
        "charpoly_ascending": [wire(v) for v in reversed(p.all_coeffs())],
        "discriminant": wire(disc),
        "opposite_resultant": wire(opposite),
        "full_dirichlet_coefficients": 36,
        "coefficient_stream_sha256": sha(encoded(actual)),
        "complex_subspace_polynomials": 27,
        "protected_targets": target_count,
        "restriction_stream_sha256": poly_stream.hexdigest(),
        "heldout_subspace_controls": heldout,
        "script_sha256_lf": sha(Path(__file__).read_bytes()),
    }
    report["payload_sha256"] = sha(encoded(report))
    return report


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
