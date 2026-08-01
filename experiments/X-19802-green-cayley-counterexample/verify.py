#!/usr/bin/env python3
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path


def q(x):
    if isinstance(x, bool):
        raise ValueError("booleans are not rationals")
    if isinstance(x, int):
        return Fraction(x)
    if not isinstance(x, str):
        raise ValueError("rational must be string or integer")
    return Fraction(x)


def mat(raw):
    if not isinstance(raw, list) or not raw or not all(isinstance(r, list) for r in raw):
        raise ValueError("matrix required")
    n = len(raw[0])
    if n == 0 or any(len(r) != n for r in raw):
        raise ValueError("ragged matrix")
    return [[q(v) for v in r] for r in raw]


def transpose(a):
    return [list(r) for r in zip(*a)]


def mm(a, b):
    if len(a[0]) != len(b):
        raise ValueError("dimension mismatch")
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def as_text(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify(data):
    expected_fields = {"schema", "G_plus", "G_minus", "trace", "C", "E", "K"}
    if set(data) != expected_fields:
        raise ValueError("unexpected or missing fields")
    if data["schema"] != "riemann.green-cayley-counterexample.v1":
        raise ValueError("wrong schema")

    gp, gm, trace, c, e, k = map(
        mat,
        [data["G_plus"], data["G_minus"], data["trace"], data["C"], data["E"], data["K"]],
    )
    if (len(gp), len(gp[0]), len(gm), len(gm[0])) != (1, 2, 1, 2):
        raise ValueError("feature shape")
    if trace != [[Fraction(1), Fraction(0)]]:
        raise ValueError("trace must select first coordinate")
    if (len(c), len(c[0])) != (1, 2) or (len(e), len(e[0])) != (2, 1):
        raise ValueError("lift shape")
    if (len(k), len(k[0])) != (2, 2):
        raise ValueError("multiplier shape")

    form = sub(mm(transpose(gp), gp), mm(transpose(gm), gm))
    expected_form = [
        [Fraction(-5, 4), Fraction(0)],
        [Fraction(0), Fraction(5, 4)],
    ]
    if form != expected_form:
        raise ValueError("unexpected Green form")
    if form[0][1] != 0 or form[1][0] != 0:
        raise ValueError("Euler cross term not zero")
    if form[1][1] <= 0:
        raise ValueError("kernel form not positive")

    if mm(c, e) != [[Fraction(1)]]:
        raise ValueError("CE is not identity")
    if k[0][1] != 0 or k[1][0] != 0:
        raise ValueError("K must be diagonal")
    k_norm = max(abs(k[0][0]), abs(k[1][1]))
    if k_norm >= 1:
        raise ValueError("K is not a strict contraction")

    observed = mm(mm(c, k), e)[0][0]
    if observed <= 1:
        raise ValueError("counterexample does not expand")
    if gp[0][0] != 1 or gm[0][0] != observed:
        raise ValueError("lift does not match Green minimizer features")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    return {
        "schema": "riemann.green-cayley-counterexample.result.v1",
        "verdict": "PASS_EXACT_COUNTEREXAMPLE",
        "Q": [[as_text(v) for v in row] for row in form],
        "kernel_floor": as_text(form[1][1]),
        "green_value": as_text(form[0][0]),
        "K_norm": as_text(k_norm),
        "CKE_norm": as_text(observed),
        "proof_object_sha256": digest,
    }


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py certificate.json")
    data = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
