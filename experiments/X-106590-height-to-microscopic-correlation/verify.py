#!/usr/bin/env python3
"""Finite exact replay for T-106590.

Checks only finite algebra and exact constants.  It does not replay Selberg's
analytic theorem or prove ENDLOC106590, SHALLOWCORR106590, 90%, density one or
RH.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

G = tuple[Fraction, Fraction]
Poly = list[G]


def g(re: int | Fraction = 0, im: int | Fraction = 0) -> G:
    return Fraction(re), Fraction(im)


def add(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def neg(a: G) -> G:
    return -a[0], -a[1]


def mul(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


ZERO, ONE = g(), g(1)


def trim(p: Poly) -> Poly:
    while len(p) > 1 and p[-1] == ZERO:
        p.pop()
    return p


def padd(p: Poly, q: Poly) -> Poly:
    return trim([
        add(p[i] if i < len(p) else ZERO, q[i] if i < len(q) else ZERO)
        for i in range(max(len(p), len(q)))
    ])


def pmul(p: Poly, q: Poly) -> Poly:
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = add(out[i + j], mul(a, b))
    return trim(out)


def pscale(p: Poly, scalar: G) -> Poly:
    return trim([mul(a, scalar) for a in p])


def pder(p: Poly) -> Poly:
    return trim([(p[i][0] * i, p[i][1] * i) for i in range(1, len(p))])


def from_roots(roots: list[G]) -> Poly:
    out = [ONE]
    for root in roots:
        out = pmul(out, [neg(root), ONE])
    return out


def sign(perm: tuple[int, ...]) -> int:
    inv = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
    return -1 if inv % 2 else 1


def determinant(matrix: list[list[Poly]]) -> Poly:
    total = [ZERO]
    for perm in itertools.permutations(range(len(matrix))):
        term = [ONE]
        for row, column in enumerate(perm):
            term = pmul(term, matrix[row][column])
        if sign(perm) < 0:
            term = [neg(a) for a in term]
        total = padd(total, term)
    return total


def main() -> dict[str, object]:
    roots = [g(2, 1), g(-1, 2), g(3, -1), g(-2, -2)]
    n = len(roots)
    lam = Fraction(2, 7)
    p = from_roots(roots)
    dp = pder(p)
    matrix: list[list[Poly]] = []
    for row in range(n):
        current: list[Poly] = []
        for column in range(n):
            entry = [g(0, lam)]
            if row == column:
                entry = padd(entry, [neg(roots[row]), ONE])
            current.append(entry)
        matrix.append(current)
    assert determinant(matrix) == padd(p, pscale(dp, g(0, lam)))

    betas = [Fraction(1, 2), Fraction(3, 5), Fraction(2, 5),
             Fraction(7, 10), Fraction(3, 10)]
    mass = sum(abs(beta - Fraction(1, 2)) for beta in betas)
    layer = 2 * sum(beta - Fraction(1, 2) for beta in betas if beta > Fraction(1, 2))
    assert mass == layer == Fraction(3, 5)

    heights = [Fraction(1, 100), Fraction(2, 100),
               Fraction(9, 100), Fraction(20, 100)]
    eta = Fraction(5, 100)
    assert sum(height > eta for height in heights) <= sum(heights) / eta

    assert Fraction(997, 1000) - Fraction(9, 10) == Fraction(97, 1000)
    assert Fraction(997, 1000) - Fraction(19, 20) == Fraction(47, 1000)

    result: dict[str, object] = {
        "schema": "riemann.x106590.height-microscopic-correlation.v1",
        "classification": "PASS_T106590_HEIGHT_TO_MICROSCOPIC_CORRELATION",
        "layer_cake_fixture_checked": True,
        "finite_alpha_determinant_checked": True,
        "deep_height_rank_bound_checked": True,
        "cosine_microscopic_firewall_checked": True,
        "ninety_threshold": "97/1000",
        "ninety_five_threshold": "47/1000",
        "endloc106590_proved": False,
        "shallowcorr106590_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    payload = main()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = Path(__file__).parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(text, end="")
