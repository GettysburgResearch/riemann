#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

Q = Fraction


def q(x: Any) -> Q:
    if isinstance(x, int):
        return Q(x)
    if isinstance(x, str):
        return Q(x)
    raise TypeError(f"unsupported rational {x!r}")


def vec(xs):
    return [q(x) for x in xs]


def mat(rows):
    return [[q(x) for x in row] for row in rows]


def dot(x, y):
    if len(x) != len(y):
        raise ValueError("dot dimension mismatch")
    return sum((a * b for a, b in zip(x, y)), Q(0))


def mv(A, x):
    if any(len(row) != len(x) for row in A):
        raise ValueError("matrix-vector mismatch")
    return [dot(row, x) for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def outer(x, y):
    return [[a * b for b in y] for a in x]


def inv2(A):
    if len(A) != 2 or any(len(row) != 2 for row in A):
        raise ValueError("inv2 requires 2x2")
    a, b = A[0]
    c, d = A[1]
    det = a * d - b * c
    if det == 0:
        raise ValueError("singular 2x2")
    return [[d / det, -b / det], [-c / det, a / det]]


def ldl_pivots(A):
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("LDL requires square")
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    D = [Q(0) for _ in range(n)]
    for i in range(n):
        L[i][i] = Q(1)
        D[i] = A[i][i] - sum(L[i][k] * L[i][k] * D[k] for k in range(i))
        if D[i] == 0:
            raise ValueError("zero LDL pivot")
        for j in range(i + 1, n):
            L[j][i] = (
                A[j][i] - sum(L[j][k] * L[i][k] * D[k] for k in range(i))
            ) / D[i]
    return D


def fstr(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def canonical_sha(obj) -> str:
    payload = (json.dumps(obj, indent=2, sort_keys=True) + "\n").encode()
    return hashlib.sha256(payload).hexdigest()


def verify(cert: dict) -> dict:
    if cert.get("schema") != "riemann.x20805.harmonic-trial-erasure.v1":
        raise ValueError("bad schema")

    C0 = mat(cert["C0"])
    r0 = vec(cert["r0"])
    S0 = q(cert["comparator_schur"])
    alpha = q(cert["negative_channel"]["source"])
    B = vec(cert["negative_channel"]["W"])
    trials = [vec(t) for t in cert["trials"]]

    if len(C0) != 2 or any(len(row) != 2 for row in C0) or len(r0) != 2 or len(B) != 2:
        raise ValueError("expected source plus two-dimensional W")
    if C0 != transpose(C0):
        raise ValueError("C0 not symmetric")

    C0_piv = ldl_pivots(C0)
    if min(C0_piv) <= 0:
        raise ValueError("C0 not positive")
    C0i = inv2(C0)
    c0ir = mv(C0i, r0)
    a0 = S0 + dot(r0, c0ir)
    H0 = [
        [a0, r0[0], r0[1]],
        [r0[0], C0[0][0], C0[0][1]],
        [r0[1], C0[1][0], C0[1][1]],
    ]
    H0_piv = ldl_pivots(H0)
    if min(H0_piv) <= 0:
        raise ValueError("H0 not positive")

    y_expected = [Q(1), -c0ir[0], -c0ir[1]]
    harmonic = []
    raw_residual_norms = []
    for t in trials:
        if len(t) != 3 or t[0] != 1:
            raise ValueError("trial must have source coordinate one")
        rw = mv(C0, t[1:])
        rw = [rw[i] + r0[i] for i in range(2)]
        corr = mv(C0i, rw)
        y = [t[0], t[1] - corr[0], t[2] - corr[1]]
        if y != y_expected:
            raise ValueError("harmonic trial erasure failed")
        harmonic.append([fstr(v) for v in y])
        raw_residual_norms.append(fstr(dot(rw, mv(C0i, rw))))

    u = [alpha] + B
    H = sub(H0, outer(u, u))
    C = sub(C0, outer(B, B))
    C_piv = ldl_pivots(C)
    if min(C_piv) <= 0:
        raise ValueError("actual W block not positive")
    Ci = inv2(C)
    r = [H[1][0], H[2][0]]
    direct = H[0][0] - dot(r, mv(Ci, r))

    defect = Q(1) - dot(B, mv(C0i, B))
    if defect <= 0:
        raise ValueError("negative-channel defect not positive")
    conditional = alpha - dot(B, c0ir)
    woodbury = S0 - conditional * conditional / defect
    if direct != woodbury:
        raise ValueError("Woodbury Schur formula mismatch")
    if direct >= 0:
        raise ValueError("negative control failed to remain negative")

    result = {
        "schema": "riemann.x20805.harmonic-trial-erasure.result.v1",
        "verdict": "CERTIFIED_HARMONIC_TRIAL_ERASURE_AND_NEGATIVE_CHANNEL_UPDATE",
        "certificate_sha256": canonical_sha(cert),
        "C0_ldl_pivots": [fstr(x) for x in C0_piv],
        "H0_ldl_pivots": [fstr(x) for x in H0_piv],
        "actual_W_ldl_pivots": [fstr(x) for x in C_piv],
        "comparator_harmonic_source_vector": [fstr(x) for x in y_expected],
        "harmonic_vectors_from_trials": harmonic,
        "trial_comparator_residual_dual_norms": raw_residual_norms,
        "negative_channel_defect": fstr(defect),
        "conditional_negative_amplitude": fstr(conditional),
        "comparator_source_schur": fstr(S0),
        "actual_source_schur_direct": fstr(direct),
        "actual_source_schur_woodbury": fstr(woodbury),
    }
    result["proof_object_sha256"] = canonical_sha(result)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    cert = json.loads(args.certificate.read_text())
    result = verify(cert)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
