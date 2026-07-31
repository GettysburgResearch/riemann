#!/usr/bin/env python3
"""Exact verifier for L-15601 counted inverse-Ritz lower floors.

The checker uses only Python integers and fractions.Fraction.  It either:

1. reconstructs every form from a finite exact synthetic operator; or
2. consumes directed rational Loewner bounds plus an externally certified
   ambient low-eigenvalue count gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15601-counted-inverse-ritz.v1"
OUTPUT_SCHEMA = "riemann.x15601-counted-inverse-ritz-verification.v1"
SYNTHETIC = "SYNTHETIC_MODEL"
PRODUCTION = "RIEMANN_WEIL_DIRECTED"
COUNT_STATUS = "CERTIFIED_AT_MOST_D_EIGENVALUES_BELOW_GAMMA"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def frac(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be a rational object")
    n = exact_int(raw.get("numerator"), f"{name}.numerator")
    d = exact_int(raw.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def parse_matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    out: list[list[Fraction]] = []
    width: int | None = None
    for i, row in enumerate(raw):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        parsed = [frac(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)]
        if width is None:
            width = len(parsed)
        if len(parsed) != width:
            raise CertificateError(f"{name} has ragged rows")
        out.append(parsed)
    return out


def mj(a: list[list[Fraction]]) -> list[list[dict[str, int]]]:
    return [[fj(x) for x in row] for row in a]


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    m, k = shape(a)
    k2, n = shape(b)
    if k != k2:
        raise CertificateError("matrix multiplication dimension mismatch")
    return [[sum(a[i][r] * b[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def add(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise CertificateError("matrix addition dimension mismatch")
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if shape(a) != shape(b):
        raise CertificateError("matrix subtraction dimension mismatch")
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(c: Fraction, a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def symmetric(a: list[list[Fraction]]) -> bool:
    m, n = shape(a)
    return m == n and all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def swap_symmetric(a: list[list[Fraction]], i: int, j: int) -> None:
    if i == j:
        return
    a[i], a[j] = a[j], a[i]
    for row in a:
        row[i], row[j] = row[j], row[i]


def psd_pivots(matrix: list[list[Fraction]], *, strict: bool) -> list[Fraction]:
    """Pivoted exact Schur test for a symmetric PSD/PD matrix.

    A zero diagonal in a PSD matrix forces the complete row and column to vanish.
    Positive diagonal pivots may therefore be selected in any order.
    """
    if not symmetric(matrix):
        raise CertificateError("matrix is not symmetric")
    a = [row[:] for row in matrix]
    pivots: list[Fraction] = []
    while a:
        n = len(a)
        if any(a[i][i] < 0 for i in range(n)):
            raise CertificateError("negative diagonal in proposed PSD matrix")
        positive = next((i for i in range(n) if a[i][i] > 0), None)
        if positive is None:
            if any(a[i][j] != 0 for i in range(n) for j in range(n)):
                raise CertificateError("zero diagonal with nonzero PSD row")
            if strict:
                raise CertificateError("singular matrix where positive definite required")
            pivots.extend([Fraction(0)] * n)
            break
        swap_symmetric(a, 0, positive)
        p = a[0][0]
        if p <= 0:
            raise CertificateError("nonpositive Schur pivot")
        pivots.append(p)
        if n == 1:
            break
        col = [a[i][0] for i in range(1, n)]
        a = [[a[i + 1][j + 1] - col[i] * col[j] / p for j in range(n - 1)] for i in range(n - 1)]
    if strict and any(p <= 0 for p in pivots):
        raise CertificateError("nonpositive strict pivot")
    return pivots


def rank(a: list[list[Fraction]]) -> int:
    m, n = shape(a)
    x = [row[:] for row in a]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if x[i][c] != 0), None)
        if pivot is None:
            continue
        x[r], x[pivot] = x[pivot], x[r]
        p = x[r][c]
        x[r] = [v / p for v in x[r]]
        for i in range(m):
            if i != r and x[i][c] != 0:
                q = x[i][c]
                x[i] = [u - q * v for u, v in zip(x[i], x[r])]
        r += 1
        if r == m:
            break
    return r


def nullspace(a: list[list[Fraction]]) -> list[list[Fraction]]:
    """Return basis vectors as columns for null(a)."""
    m, n = shape(a)
    x = [row[:] for row in a]
    pivots: list[int] = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if x[i][c] != 0), None)
        if pivot is None:
            continue
        x[r], x[pivot] = x[pivot], x[r]
        p = x[r][c]
        x[r] = [v / p for v in x[r]]
        for i in range(m):
            if i != r and x[i][c] != 0:
                q = x[i][c]
                x[i] = [u - q * v for u, v in zip(x[i], x[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    cols: list[list[Fraction]] = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = -x[i][f]
        cols.append(v)
    if not cols:
        return [[] for _ in range(n)]
    return [list(row) for row in zip(*cols)]


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_sha(value: Any, name: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or any(c not in string.hexdigits for c in value):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def full_operator_forms(data: dict[str, Any], gamma: Fraction, t: Fraction, d: int) -> tuple[list[list[Fraction]], list[list[Fraction]], list[list[Fraction]], dict[str, Any]]:
    a = parse_matrix(data.get("full_operator"), "full_operator")
    n, n2 = shape(a)
    if n != n2 or not symmetric(a):
        raise CertificateError("full_operator must be symmetric square")
    j = parse_matrix(data.get("trial_basis"), "trial_basis")
    if shape(j) != (n, d) or rank(j) != d:
        raise CertificateError("trial_basis must have full declared rank")
    s = parse_matrix(data.get("count_subspace"), "count_subspace")
    if shape(s) != (n, d) or rank(s) != d:
        raise CertificateError("count_subspace must have full declared rank")

    # Exact count cap: A >= gamma on the orthogonal complement of count_subspace.
    e = nullspace(transpose(s))
    if shape(e) != (n, n - d):
        raise CertificateError("count complement dimension mismatch")
    if n - d:
        ge = matmul(transpose(e), e)
        ce = matmul(matmul(transpose(e), a), e)
        count_slack = sub(ce, scale(gamma, ge))
        count_pivots = psd_pivots(count_slack, strict=False)
    else:
        count_slack = []
        count_pivots = []

    shifted = sub(a, scale(t, eye(n)))
    h = matmul(matmul(transpose(j), shifted), j)
    k = matmul(matmul(transpose(j), matmul(shifted, shifted)), j)
    details = {
        "full_dimension": n,
        "count_complement_dimension": n - d,
        "count_slack": mj(count_slack) if count_slack else [],
        "count_slack_pivots": [fj(x) for x in count_pivots],
    }
    return h, k, k, details


def directed_forms(data: dict[str, Any], gamma: Fraction, d: int) -> tuple[list[list[Fraction]], list[list[Fraction]], list[list[Fraction]], dict[str, Any]]:
    gate = data.get("count_gate")
    if not isinstance(gate, dict) or gate.get("status") != COUNT_STATUS:
        raise CertificateError("production count gate missing or wrong")
    if exact_int(gate.get("cap"), "count_gate.cap") != d:
        raise CertificateError("count gate cap does not match packet dimension")
    if frac(gate.get("gamma"), "count_gate.gamma") != gamma:
        raise CertificateError("count gate gamma mismatch")
    validate_sha(gate.get("source_sha256"), "count_gate.source_sha256")
    analytic_claim = gate.get("analytic_claim")
    if not isinstance(analytic_claim, str) or not analytic_claim:
        raise CertificateError("count gate analytic claim missing")
    h = parse_matrix(data.get("H_upper"), "H_upper")
    kl = parse_matrix(data.get("K_lower"), "K_lower")
    ku = parse_matrix(data.get("K_upper"), "K_upper")
    for name, matrix in (("H_upper", h), ("K_lower", kl), ("K_upper", ku)):
        if shape(matrix) != (d, d) or not symmetric(matrix):
            raise CertificateError(f"{name} has wrong dimension or symmetry")
    psd_pivots(sub(ku, kl), strict=False)
    return h, kl, ku, {"count_gate": gate}


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    classification = data.get("classification")
    if classification not in (SYNTHETIC, PRODUCTION):
        raise CertificateError("unsupported classification")
    d = exact_int(data.get("dimension"), "dimension")
    if d < 1:
        raise CertificateError("dimension must be positive")
    gamma = frac(data.get("gamma"), "gamma")
    t = frac(data.get("t"), "t")
    q = frac(data.get("q_upper"), "q_upper")
    claimed = frac(data.get("claimed_floor"), "claimed_floor")
    if not t < gamma:
        raise CertificateError("require t < gamma")
    if q >= 0:
        raise CertificateError("q_upper must be strictly negative")

    if classification == SYNTHETIC:
        h, kl, ku, details = full_operator_forms(data, gamma, t, d)
    else:
        h, kl, ku, details = directed_forms(data, gamma, d)

    h_negative = psd_pivots(scale(Fraction(-1), h), strict=True)
    k_positive = psd_pivots(kl, strict=True)
    moat_matrix = sub(scale(q, ku), h)
    moat_pivots = psd_pivots(moat_matrix, strict=False)

    floor = t + Fraction(1, 1) / q
    if claimed > floor:
        raise CertificateError("claimed floor exceeds certified inverse-Ritz floor")

    proof_object = {
        "classification": classification,
        "dimension": d,
        "gamma": fj(gamma),
        "t": fj(t),
        "q_upper": fj(q),
        "H_upper": mj(h),
        "K_lower": mj(kl),
        "K_upper": mj(ku),
        "certified_floor": fj(floor),
        "claimed_floor": fj(claimed),
        "H_negative_pivots": [fj(x) for x in h_negative],
        "K_positive_pivots": [fj(x) for x in k_positive],
        "inverse_ritz_moat_pivots": [fj(x) for x in moat_pivots],
        "count_details": details,
    }
    digest = canonical_sha(proof_object)
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-15601",
        "dimension": d,
        "gamma": fj(gamma),
        "t": fj(t),
        "q_upper": fj(q),
        "certified_floor": fj(floor),
        "claimed_floor": fj(claimed),
        "H_negative_pivots": [fj(x) for x in h_negative],
        "K_positive_pivots": [fj(x) for x in k_positive],
        "inverse_ritz_moat_pivots": [fj(x) for x in moat_pivots],
        "exact_proof_object_sha256": digest,
        "verdict": "CERTIFIED_COUNTED_INVERSE_RITZ_AMBIENT_FLOOR",
        "proof_boundary": (
            "Exact rational finite algebra. Production use inherits the complete "
            "ambient low-eigenvalue count, common localized-Weil normalization, and "
            "directed A/A^2 form enclosures."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
