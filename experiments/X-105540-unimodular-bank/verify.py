#!/usr/bin/env python3
"""Exact replay for T-105540.

Authenticates finite polynomial/operator algebra and exact threshold arithmetic.
It does not machine-prove the pinned Xi safe-line estimates, MATRIXLERC105541,
90%, a new record, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

VERDICT = "PASS_T105540_UNIMODULAR_BANK_REALIZATION"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    "README_105540.md",
    "PR_BODY_105540_ADDENDUM.md",
    "PACKET_METADATA_105540.json",
    "claims/lemmas/L-105540-unimodular-bezout-bank.md",
    "claims/lemmas/L-105541-two-boundary-hardy-bank.md",
    "claims/lemmas/L-105542-horizontal-xi-bank-transfer.md",
    "claims/refutations/R-105540-unimodular-bank-is-not-a-free-carrier.md",
    "claims/theorems/T-105540-single-flux-ninety-percent-frontier.md",
    "claims/methodology/M-105540-hostile-review-contract.md",
    "standalone/2026-08-24-unimodular-bank-realization/PROOF.md",
    "reports/gpt56-pro/2026-08-24-unimodular-bank-realization.md",
    "experiments/X-105540-unimodular-bank/README.md",
    "experiments/X-105540-unimodular-bank/replay.sh",
    "experiments/X-105540-unimodular-bank/verify.py",
    "experiments/X-105540-unimodular-bank/tests/test_verify.py",
    "integration/2026-08-24/t105540-source-lock.json",
)

Poly = Dict[int, F]
Bivar = Dict[Tuple[int, int], F]
Matrix = List[List[F]]


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def pclean(p: Poly) -> Poly:
    return {k: v for k, v in p.items() if v}


def padd(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return pclean(out)


def pscale(p: Poly, c: F) -> Poly:
    return pclean({k: c * v for k, v in p.items()})


def pmul(p: Poly, q: Poly, degree: int = 16) -> Poly:
    out: Poly = {}
    for i, a in p.items():
        for j, b in q.items():
            if i + j <= degree:
                out[i + j] = out.get(i + j, F(0)) + a * b
    return pclean(out)


def badd(*ps: Bivar) -> Bivar:
    out: Bivar = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def bmul(p: Bivar, q: Bivar, degree: int = 12) -> Bivar:
    out: Bivar = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            if i + j + k + ell <= degree:
                key = (i + k, j + ell)
                out[key] = out.get(key, F(0)) + a * b
    return {k: v for k, v in out.items() if v}


def bezout_polynomial_checks() -> dict:
    I = {0: F(1)}
    x = {1: F(1)}
    x2 = {2: F(1)}
    w0 = padd(I, pscale(x, F(-1, 2)), pscale(x2, F(-1, 4)))
    w1 = pscale(x, F(1, 2))
    b = padd(I, pscale(x, F(1, 2)))
    require(padd(w0, pmul(b, w1)) == I, "Bezout identity")

    # U=[[w0,-b],[w1,1]], V=[[1,b],[-w1,w0]].
    uv00 = padd(w0, pmul(b, w1))
    uv01 = padd(pmul(w0, b), pscale(pmul(b, w0), F(-1)))
    uv10 = padd(w1, pscale(w1, F(-1)))
    uv11 = padd(pmul(w1, b), w0)
    require(uv00 == I and uv01 == {} and uv10 == {} and uv11 == I,
            "right block inverse")

    vu00 = padd(w0, pmul(b, w1))
    vu01 = padd(pscale(b, F(-1)), b)
    vu10 = padd(pscale(pmul(w1, w0), F(-1)), pmul(w0, w1))
    vu11 = padd(pmul(w1, b), w0)
    require(vu00 == I and vu01 == {} and vu10 == {} and vu11 == I,
            "left block inverse")
    return {
        "W0": {str(k): str(v) for k, v in w0.items()},
        "W1": {str(k): str(v) for k, v in w1.items()},
        "B": {str(k): str(v) for k, v in b.items()},
        "determinant": "1",
    }


def zeros(n: int, m: int | None = None) -> Matrix:
    if m is None:
        m = n
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n: int) -> Matrix:
    a = zeros(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def madd(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mscale(a: Matrix, c: F) -> Matrix:
    return [[c * x for x in r] for r in a]


def mmul(a: Matrix, b: Matrix) -> Matrix:
    n, k, m = len(a), len(b), len(b[0])
    require(len(a[0]) == k, "matrix dimensions")
    return [[sum((a[i][t] * b[t][j] for t in range(k)), F(0))
             for j in range(m)] for i in range(n)]


def mv(a: Matrix, v: Sequence[F]) -> List[F]:
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def block(a: Matrix, b: Matrix, c: Matrix, d: Matrix) -> Matrix:
    n = len(a)
    return [a[i] + b[i] for i in range(n)] + [c[i] + d[i] for i in range(n)]


def random_strict_upper(n: int, rng: random.Random) -> Matrix:
    a = zeros(n)
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j] = F(rng.randint(-3, 3), rng.randint(1, 5))
    return a


def matrix_bank_checks(seed: int = 105540, cases: int = 1000) -> dict:
    rng = random.Random(seed)
    checks = 0
    for _ in range(cases):
        n = rng.randint(1, 10)
        x = random_strict_upper(n, rng)
        I = eye(n)
        x2 = mmul(x, x)
        w0 = madd(madd(I, mscale(x, F(-1, 2))), mscale(x2, F(-1, 4)))
        w1 = mscale(x, F(1, 2))
        b = madd(I, mscale(x, F(1, 2)))
        z = zeros(n)
        U = block(w0, mscale(b, F(-1)), w1, I)
        V = block(I, b, mscale(w1, F(-1)), w0)
        require(mmul(U, V) == eye(2 * n), "U V exact")
        require(mmul(V, U) == eye(2 * n), "V U exact")
        v = [F(rng.randint(-5, 5), rng.randint(1, 7)) for _ in range(n)]
        g0, g1 = mv(w0, v), mv(w1, v)
        recovered = [a + c for a, c in zip(g0, mv(b, g1))]
        require(recovered == v, "bank left inverse")
        checks += 3
    return {"seed": seed, "matrix_cases": cases, "exact_identities": checks,
            "maximum_dimension": 10}


def two_boundary_checks() -> dict:
    w0z: Bivar = {(0, 0): F(1), (1, 0): F(-1, 2), (2, 0): F(-1, 4)}
    w0y: Bivar = {(0, 0): F(1), (0, 1): F(-1, 2), (0, 2): F(-1, 4)}
    w1z: Bivar = {(1, 0): F(1, 2)}
    w1y: Bivar = {(0, 1): F(1, 2)}
    S = badd(bmul(w0z, w0y), bmul(w1z, w1y))
    # r = 1/2(sum z^i + sum y^j), enough through total degree 8.
    r: Bivar = {(0, 0): F(1)}
    for k in range(1, 9):
        r[(k, 0)] = F(1, 2)
        r[(0, k)] = F(1, 2)
    lam = bmul(S, r, degree=8)
    require(lam.get((0, 0)) == 1, "bank constant")
    for i in range(3):
        for j in range(3 - i):
            if i + j in (1, 2):
                require(lam.get((i, j), F(0)) == 0,
                        f"uncancelled bidegree {(i,j)}")
    require(lam.get((3, 0)) == F(1, 8), "z^3 coefficient")
    require(lam.get((0, 3)) == F(1, 8), "y^3 coefficient")

    # Common-denominator numerator in L-105541.
    numerator = {
        (3, 0): F(4), (0, 3): F(4),
        (3, 1): F(-2), (1, 3): F(-2), (2, 2): F(-2),
        (3, 2): F(-1), (2, 3): F(-1),
    }
    denom_inv: Bivar = {}
    for i in range(7):
        for j in range(7 - i):
            denom_inv[(i, j)] = F(1, 32)
    reconstructed = bmul(numerator, denom_inv, degree=8)
    for key in set(lam) | set(reconstructed) | {(0, 0)}:
        if sum(key) <= 8:
            require(lam.get(key, F(0)) - (F(1) if key == (0, 0) else F(0))
                    == reconstructed.get(key, F(0)),
                    f"common denominator mismatch {key}")
    return {
        "cancelled_total_degrees": [1, 2],
        "first_nonzero_bidegrees": {"3,0": "1/8", "0,3": "1/8"},
        "common_denominator_terms": len(numerator),
    }


def threshold_checks() -> dict:
    require(F(2) * F(19, 20) - F(1) == F(9, 10), "90 percent threshold")
    require(F(9139, 9216) / F(20) == F(9139, 184320), "old fixed cut")
    return {
        "asymptotic_bank_anchor": "1-o(1)",
        "negative_trace_cut": "1/20-o(1)",
        "positive_index_fraction": "19/20-o(1)",
        "line_fraction_boundary": "9/10",
    }


def hashes() -> dict:
    return {
        p: hashlib.sha256((ROOT / p).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        for p in CONTENT
    }


def build_payload() -> dict:
    out = {
        "verdict": VERDICT,
        "bezout_polynomial": bezout_polynomial_checks(),
        "operator_regression": matrix_bank_checks(),
        "two_boundary_source": two_boundary_checks(),
        "ninety_percent_threshold": threshold_checks(),
        "content_sha256": hashes(),
        "bankreal105530_proved": True,
        "bank_induced_partial_index_zero": True,
        "pinned_analytic_transfer_machine_proved": False,
        "matrixlerc105541_proved": False,
        "ninety_percent_established": False,
        "public_record_beaten": False,
        "rh_established": False,
    }
    out["proof_object_sha256"] = hashlib.sha256(
        json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(payload["proof_object_sha256"])
    print("BANKREAL105530_PROVED")
    print("MATRIXLERC105541_OPEN")
    print("NINETY_PERCENT_UNPROVED")
    print("RH_UNPROVED")
