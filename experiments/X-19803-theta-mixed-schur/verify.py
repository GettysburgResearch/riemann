#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def q(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("booleans are not rationals")
    if isinstance(x, int):
        return Fraction(x)
    if not isinstance(x, str):
        raise ValueError("rational must be encoded as string or integer")
    return Fraction(x)


def mat(raw: Any) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("matrix must be a nonempty list")
    out = [[q(x) for x in row] for row in raw]
    width = len(out[0])
    if width == 0 or any(len(row) != width for row in out):
        raise ValueError("ragged matrix")
    return out


def transpose(a):
    return [list(col) for col in zip(*a)]


def mm(a, b):
    if len(a[0]) != len(b):
        raise ValueError("matrix dimension mismatch")
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix dimension mismatch")
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix dimension mismatch")
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def block(a, b, c, d):
    if len(a) != len(b) or len(c) != len(d) or len(a[0]) != len(c[0]) or len(b[0]) != len(d[0]):
        raise ValueError("block dimension mismatch")
    return [a[i]+b[i] for i in range(len(a))] + [c[i]+d[i] for i in range(len(c))]


def zero(r, c):
    return [[Fraction(0) for _ in range(c)] for _ in range(r)]


def canonical_digest(payload):
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def verify(data):
    if data.get("schema") != "riemann.theta-mixed-schur.v1":
        raise ValueError("wrong schema")

    p = [q(x) for x in data["probabilities"]]
    y = [q(x) for x in data["mode_coordinates"]]
    if len(p) != len(y) or len(p) < 2:
        raise ValueError("mode data mismatch")
    if any(x <= 0 for x in p) or sum(p) != 1:
        raise ValueError("probabilities must be positive and sum to one")

    mean = sum(pi*yi for pi, yi in zip(p, y))
    mean2 = sum(pi*yi*yi for pi, yi in zip(p, y))
    var = mean2-mean*mean
    a = mean-Fraction(1,4)
    scalar = 4*(a-Fraction(5,4))*(a+Fraction(1,4))
    pair = 2*sum(p[i]*p[j]*(y[i]-y[j])**2 for i in range(len(p)) for j in range(len(p)))
    mu = 4*mean2-6*mean
    if scalar != q(data["expected_scalar_channel"]):
        raise ValueError("scalar channel mismatch")
    if pair != q(data["expected_pair_channel"]):
        raise ValueError("pair channel mismatch")
    if mu != q(data["expected_mu"]) or scalar+pair != mu:
        raise ValueError("theta variance identity failed")
    if var <= 0:
        raise ValueError("control must contain genuine mode mixing")

    V = mat(data["tail_matrix"])
    G = mat(data["mixer"])
    D = mat(data["trace_schur"])
    if len(G) != len(V) or len(D) != len(D[0]) or len(G[0]) != len(D):
        raise ValueError("operator dimensions incompatible")

    A = mm(transpose(V), V)
    B = mm(transpose(V), G)
    C = add(mm(transpose(G), G), D)
    S = block(A, B, transpose(B), C)

    n = len(A)
    xdim = len(D)
    RDR = block(zero(n,n), zero(n,xdim), zero(xdim,n), D)
    J = [V[i]+G[i] for i in range(len(V))]
    fourJstarJ = mm(transpose(J), J)
    if sub(S, RDR) != fourJstarJ:
        raise ValueError("mixed Schur identity failed")

    result = {
        "schema": data["schema"],
        "mean": str(mean),
        "variance": str(var),
        "a": str(a),
        "mu": str(mu),
        "scalar_channel": str(scalar),
        "pair_channel": str(pair),
        "tail_rank": len(V),
        "null_dimension": n,
        "trace_dimension": xdim,
        "trace_schur": [[str(x) for x in row] for row in D],
        "identity": "S-R*D*R=4J_mix*J_mix",
        "verdict": "PASS"
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py CERTIFICATE.json")
    data = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
