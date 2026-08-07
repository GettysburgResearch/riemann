#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

F = Fraction
Matrix = list[list[Fraction]]
Vector = list[Fraction]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def inner(x: Vector, y: Vector) -> Fraction:
    return sum(a * b for a, b in zip(x, y))


def norm2(x: Vector) -> Fraction:
    return inner(x, x)


def add(x: Vector, y: Vector) -> Vector:
    return [a + b for a, b in zip(x, y)]


def canonical_json(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def build_certificate() -> dict:
    # Exact three-dimensional cyclic representation.  These commuting
    # orthogonal matrices distinguish product from factor-ratio geometry.
    I: Matrix = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
    ]
    P: Matrix = [
        [F(0), F(0), F(1)],
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
    ]
    P2 = matmul(P, P)

    U: dict[int, Matrix] = {1: I, 2: P, 3: P2, 4: P2, 6: I}
    f: Vector = [F(1), F(2), F(4)]

    # Rational symbolic prime-log model:
    # log(2)=1, log(3)=2, Lambda(2)=Lambda(4)=1, Lambda(3)=2.
    lam = {2: F(1), 3: F(2), 4: F(1)}
    logn = {2: F(1), 3: F(2), 4: F(2)}

    channels: list[tuple[int, int, Fraction, str]] = []
    for n in (2, 3, 4):
        channels.append((1, n, lam[n] * logn[n], "derivative"))
    for d in (2, 3, 4):
        for e in (2, 3, 4):
            if d * e in U:
                channels.append((d, e, lam[d] * lam[e], "convolution"))

    lambda2: defaultdict[int, Fraction] = defaultdict(F)
    for d, e, weight, _kind in channels:
        lambda2[d * e] += weight

    expected = {2: F(1), 3: F(4), 4: F(3), 6: F(4)}
    if dict(lambda2) != expected:
        raise AssertionError("complete Lambda_2 ledger mismatch")

    direct = sum(
        weight * inner(f, matvec(U[d * e], f))
        for d, e, weight, _kind in channels
    )
    grouped = sum(
        weight * inner(f, matvec(U[n], f))
        for n, weight in lambda2.items()
    )

    polarized = F(0)
    channel_rows = []
    for d, e, weight, kind in channels:
        ud_star_f = matvec(transpose(U[d]), f)
        ue_f = matvec(U[e], f)
        row = F(1, 2) * weight * (
            norm2(add(ud_star_f, ue_f)) - norm2(ud_star_f) - norm2(ue_f)
        )
        polarized += row
        channel_rows.append(
            {
                "d": d,
                "e": e,
                "kind": kind,
                "weight": frac(weight),
                "polarized_value": frac(row),
            }
        )

    if not (direct == grouped == polarized):
        raise AssertionError("product-dilation polarization failed")

    product_23 = inner(f, matvec(U[6], f))
    ratio_23 = inner(matvec(U[2], f), matvec(U[3], f))
    if product_23 == ratio_23:
        raise AssertionError("orientation control did not separate product and ratio")

    result = {
        "schema": "X-15124-v1",
        "verdict": "CERTIFIED_PRODUCT_DILATION_POLARIZATION",
        "vector": [frac(v) for v in f],
        "lambda2": {str(n): frac(v) for n, v in sorted(lambda2.items())},
        "direct_product_form": frac(direct),
        "grouped_lambda2_form": frac(grouped),
        "polarized_channel_form": frac(polarized),
        "p2_p3_product_value": frac(product_23),
        "p2_p3_ratio_value": frac(ratio_23),
        "orientation_distinct": True,
        "channels": channel_rows,
    }
    result["proof_sha256"] = hashlib.sha256(canonical_json(result)).hexdigest()
    return result


def main() -> None:
    result = build_certificate()
    out = Path(__file__).with_name("results") / "exact-verification.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
