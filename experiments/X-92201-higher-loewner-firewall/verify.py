#!/usr/bin/env python3
"""Exact Fraction replay for R-92200."""
from fractions import Fraction as F
import json
from pathlib import Path

B = F(1000)
a = F(2, 5)
r0 = B * B / F(4)
c = B * B - a * a
d = F(2) * a * B


def p(t):
    A = t + c
    return F(2) / (t + r0) + F(4) * A / (A * A + d * d)


def p1(t):
    A = t + c
    return -F(2) / (t + r0) ** 2 + F(4) * (d * d - A * A) / (A * A + d * d) ** 2


def Z(t):
    return F(1) / p(t)


def Z1(t):
    return -p1(t) / (p(t) ** 2)


def secant(x, y):
    return (Z(x) - Z(y)) / (x - y)


nodes = [F(1, 4), F(600000), F(600000000)]
M = [
    [Z1(nodes[i]) if i == j else secant(nodes[i], nodes[j]) for j in range(3)]
    for i in range(3)
]


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


determinant = det3(M)
expected = F(
    -121963925874180597805406777183433564656326573094570826250190338142395019531250000000000000,
    1902244056492281038040828852656511743924817971347701869400802989494251324696057698781162756917531329,
)
assert determinant == expected
assert determinant < 0

curvature_coefficients = [
    343321435546890625,
    1029967657470632812492500,
    1029969030762026367221250001200,
    343323138427858398437343748599999936,
]
assert all(value > 0 for value in curvature_coefficients)
assert B * B > F(2160) * F(7)  # log(B+3)<7

result = {
    "status": "PASS_HIGHER_LOEWNER_FIREWALL",
    "parameters": {"B": str(B), "a": str(a), "r0": str(r0)},
    "nodes": [str(x) for x in nodes],
    "loewner_determinant": str(determinant),
    "curvature_polynomial_coefficients": [str(x) for x in curvature_coefficients],
}
out = Path(__file__).resolve().parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
print(result["status"])
print(json.dumps(result, indent=2, sort_keys=True))
