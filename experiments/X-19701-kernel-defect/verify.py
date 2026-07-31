#!/usr/bin/env python3
"""Exact verifier for X-19701.

Standard-library only.  The proof object demonstrates that a conjugate off-line
cardinal block retains a strict negative direction after eliminating a positive
ambient complement, while the corresponding all-real control has a positive
Schur complement.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


class VerificationError(ValueError):
    pass


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise VerificationError("booleans are not rationals")
    if isinstance(x, int):
        return Fraction(x)
    if not isinstance(x, dict) or set(x) != {"numerator", "denominator"}:
        raise VerificationError("rational must be integer or {numerator,denominator}")
    n, d = x["numerator"], x["denominator"]
    if isinstance(n, bool) or isinstance(d, bool) or not isinstance(n, int) or not isinstance(d, int):
        raise VerificationError("rational numerator and denominator must be integers")
    if d <= 0:
        raise VerificationError("rational denominator must be positive")
    return Fraction(n, d)


def enc(q: Fraction) -> dict[str, int]:
    return {"numerator": q.numerator, "denominator": q.denominator}


def vec(xs: Any) -> list[Fraction]:
    if not isinstance(xs, list):
        raise VerificationError("vector must be a list")
    return [rat(x) for x in xs]


def mat(xs: Any) -> list[list[Fraction]]:
    if not isinstance(xs, list) or not xs or not all(isinstance(r, list) for r in xs):
        raise VerificationError("matrix must be a nonempty list of rows")
    rows = [[rat(x) for x in r] for r in xs]
    n = len(rows[0])
    if n == 0 or any(len(r) != n for r in rows):
        raise VerificationError("matrix rows have inconsistent lengths")
    return rows


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(col) for col in zip(*a)]


def mm(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise VerificationError("matrix multiplication dimension mismatch")
    return [[sum(a[i][k] * b[k][j] for k in range(ac)) for j in range(bc)] for i in range(ar)]


def mv(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    if shape(a)[1] != len(x):
        raise VerificationError("matrix-vector dimension mismatch")
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def sub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise VerificationError("matrix subtraction dimension mismatch")
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    if len(x) != len(y):
        raise VerificationError("dot-product dimension mismatch")
    return sum(a * b for a, b in zip(x, y))


def quad(a: list[list[Fraction]], x: list[Fraction]) -> Fraction:
    return dot(x, mv(a, x))


def symmetric(a: list[list[Fraction]]) -> bool:
    r, c = shape(a)
    return r == c and all(a[i][j] == a[j][i] for i in range(r) for j in range(c))


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n, m = shape(a)
    if n != m:
        raise VerificationError("inverse requires a square matrix")
    aug = [row[:] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if aug[i][col] != 0), None)
        if pivot is None:
            raise VerificationError("matrix is singular")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [v / p for v in aug[col]]
        for i in range(n):
            if i == col:
                continue
            f = aug[i][col]
            if f:
                aug[i] = [aug[i][j] - f * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def ldl_pivots(a: list[list[Fraction]], *, semidefinite: bool = False) -> list[Fraction]:
    if not symmetric(a):
        raise VerificationError("LDL requires a symmetric matrix")
    n = len(a)
    l = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    d = [Fraction(0) for _ in range(n)]
    for j in range(n):
        d[j] = a[j][j] - sum(l[j][k] * l[j][k] * d[k] for k in range(j))
        if semidefinite:
            if d[j] < 0:
                raise VerificationError("matrix is not positive semidefinite")
        elif d[j] <= 0:
            raise VerificationError("matrix is not positive definite")
        for i in range(j + 1, n):
            num = a[i][j] - sum(l[i][k] * l[j][k] * d[k] for k in range(j))
            if d[j] == 0:
                if num != 0:
                    raise VerificationError("zero LDL pivot with nonzero column residue")
                l[i][j] = Fraction(0)
            else:
                l[i][j] = num / d[j]
    return d


def canonical_hash(obj: dict[str, Any]) -> str:
    payload = dict(obj)
    payload.pop("proof_object_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("schema") != "riemann.x19701-kernel-defect.v1":
        raise VerificationError("unexpected schema")

    metric = mat(data["kernel_metric"])
    b_off = mat(data["offline_kernel_block"])
    b_line = mat(data["line_only_kernel_block"])
    c = mat(data["complement_block"])
    z = mat(data["kernel_complement_cross"])
    eval_real = mat(data["selected_real_evaluation"])
    witness = vec(data["offline_witness"])
    multiplicity = rat(data["offline_multiplicity"])

    kdim = shape(metric)[0]
    if shape(metric) != (kdim, kdim) or not symmetric(metric):
        raise VerificationError("kernel metric must be symmetric square")
    if shape(b_off) != (kdim, kdim) or shape(b_line) != (kdim, kdim):
        raise VerificationError("kernel block dimension mismatch")
    if not symmetric(b_off) or not symmetric(b_line):
        raise VerificationError("kernel blocks must be symmetric")
    cdim = shape(c)[0]
    if shape(c) != (cdim, cdim) or not symmetric(c):
        raise VerificationError("complement block must be symmetric square")
    if shape(z) != (cdim, kdim):
        raise VerificationError("cross block dimension mismatch")
    if len(witness) != kdim or not any(witness):
        raise VerificationError("offline witness must be nonzero and match kernel dimension")
    if shape(eval_real)[1] != kdim:
        raise VerificationError("selected evaluation dimension mismatch")
    if multiplicity <= 0:
        raise VerificationError("offline multiplicity must be positive")

    metric_pivots = ldl_pivots(metric)
    complement_pivots = ldl_pivots(c)

    expected_off = [[Fraction(0), multiplicity], [multiplicity, Fraction(0)]]
    if kdim != 2 or b_off != expected_off:
        raise VerificationError("offline block is not the exact conjugate-cardinal signature block")

    if any(mv(eval_real, witness)):
        raise VerificationError("offline witness is not invisible at selected real zeros")

    cinv = inverse(c)
    correction = mm(mm(transpose(z), cinv), z)
    s_off = sub(b_off, correction)
    s_line = sub(b_line, correction)

    raw_q = quad(b_off, witness)
    corrected_q = quad(s_off, witness)
    metric_q = quad(metric, witness)
    if metric_q <= 0:
        raise VerificationError("witness metric norm is not positive")
    if raw_q != -2 * multiplicity:
        raise VerificationError("raw off-line cardinal quadratic is not -2m")
    if not corrected_q <= raw_q < 0:
        raise VerificationError("Schur elimination did not preserve/strengthen the negative witness")

    line_pivots = ldl_pivots(s_line)

    expected_raw = rat(data["expected_raw_offline_quadratic"])
    expected_corrected = rat(data["expected_corrected_offline_quadratic"])
    expected_line_floor = rat(data["expected_line_floor"])
    if raw_q != expected_raw:
        raise VerificationError("raw quadratic does not match declared value")
    if corrected_q != expected_corrected:
        raise VerificationError("corrected quadratic does not match declared value")

    plus = [Fraction(1), Fraction(1)]
    minus = [Fraction(1), Fraction(-1)]
    lam_plus = quad(s_line, plus) / quad(metric, plus)
    lam_minus = quad(s_line, minus) / quad(metric, minus)
    line_floor = min(lam_plus, lam_minus)
    if line_floor != expected_line_floor or line_floor <= 0:
        raise VerificationError("line-only Schur floor does not match the positive control")

    digest = canonical_hash(data)
    declared = data.get("proof_object_sha256")
    if declared is not None and declared != digest:
        raise VerificationError("proof-object SHA-256 mismatch")

    return {
        "schema": "riemann.x19701-kernel-defect.result.v1",
        "verified": True,
        "verdict": "CERTIFIED_OFFLINE_CARDINAL_NEGATIVE_GAP_SURVIVES_SCHUR",
        "proof_object_sha256": digest,
        "kernel_dimension": kdim,
        "complement_dimension": cdim,
        "metric_ldl_pivots": [enc(q) for q in metric_pivots],
        "complement_ldl_pivots": [enc(q) for q in complement_pivots],
        "line_only_schur_ldl_pivots": [enc(q) for q in line_pivots],
        "raw_offline_quadratic": enc(raw_q),
        "corrected_offline_quadratic": enc(corrected_q),
        "offline_metric_norm_squared": enc(metric_q),
        "corrected_offline_rayleigh": enc(corrected_q / metric_q),
        "line_only_schur_floor": enc(line_floor),
        "proof_boundary": (
            "Exact finite Schur and cardinal-signature arithmetic only. "
            "The zeta application additionally requires the Xi-cardinal domain, "
            "finite-support repair, form/metric capture, and normalization gates."
        ),
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} CERTIFICATE.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(argv[1]).read_text())
        result = verify(data)
    except (OSError, json.JSONDecodeError, VerificationError, KeyError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
