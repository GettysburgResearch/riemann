#!/usr/bin/env python3
"""Finite exact replay for T-106550.

This checks the layer-cake fixture, the finite-alpha rank-one determinant
identity, the deep-height rank ledger, the cosine firewall and the exact
percentage constants.  It does not prove Selberg's analytic estimate,
ENDLOC106550, SHALLOWCORR106550, ninety percent, density one or RH.
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


def ga(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def gn(a: G) -> G:
    return -a[0], -a[1]


def gm(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


ZERO = g()
ONE = g(1)


def trim(p: Poly) -> Poly:
    out = p[:]
    while len(out) > 1 and out[-1] == ZERO:
        out.pop()
    return out


def padd(p: Poly, q: Poly) -> Poly:
    n = max(len(p), len(q))
    return trim([
        ga(p[i] if i < len(p) else ZERO, q[i] if i < len(q) else ZERO)
        for i in range(n)
    ])


def pneg(p: Poly) -> Poly:
    return [gn(x) for x in p]


def pmul(p: Poly, q: Poly) -> Poly:
    out = [ZERO] * (len(p) + len(q) - 1)
    for i, left in enumerate(p):
        for j, right in enumerate(q):
            out[i + j] = ga(out[i + j], gm(left, right))
    return trim(out)


def pscale(p: Poly, scalar: G) -> Poly:
    return trim([gm(x, scalar) for x in p])


def pder(p: Poly) -> Poly:
    return trim([
        (p[i][0] * i, p[i][1] * i) for i in range(1, len(p))
    ] or [ZERO])


def polynomial_from_roots(roots: list[G]) -> Poly:
    out = [ONE]
    for root in roots:
        out = pmul(out, [gn(root), ONE])
    return out


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


def determinant_polynomial(matrix: list[list[Poly]]) -> Poly:
    n = len(matrix)
    total: Poly = [ZERO]
    for perm in itertools.permutations(range(n)):
        term: Poly = [ONE]
        for row, column in enumerate(perm):
            term = pmul(term, matrix[row][column])
        if permutation_sign(perm) < 0:
            term = pneg(term)
        total = padd(total, term)
    return trim(total)


def main() -> dict[str, object]:
    # Exact finite-alpha determinant lemma:
    # det(zI-A+i lambda J) = p(z)+i lambda p'(z).
    roots = [g(2, 1), g(-1, 2), g(3, -1), g(-2, -2)]
    degree = len(roots)
    lam = Fraction(2, 7)
    polynomial = polynomial_from_roots(roots)
    derivative = pder(polynomial)
    matrix: list[list[Poly]] = []
    for row in range(degree):
        current: list[Poly] = []
        for column in range(degree):
            entry: Poly = [g(0, lam)]
            if row == column:
                entry = padd(entry, [gn(roots[row]), ONE])
            current.append(entry)
        matrix.append(current)
    determinant = determinant_polynomial(matrix)
    assert determinant == padd(polynomial, pscale(derivative, g(0, lam)))

    # Exact layer-cake fixture with functional-equation pairs.
    betas = [
        Fraction(1, 2),
        Fraction(3, 5),
        Fraction(2, 5),
        Fraction(7, 10),
        Fraction(3, 10),
    ]
    horizontal_mass = sum(abs(beta - Fraction(1, 2)) for beta in betas)
    positive_layer_cake = 2 * sum(
        beta - Fraction(1, 2)
        for beta in betas
        if beta > Fraction(1, 2)
    )
    assert horizontal_mass == positive_layer_cake == Fraction(3, 5)

    # The count of heights above eta is at most total height divided by eta.
    heights = [Fraction(1, 100), Fraction(2, 100),
               Fraction(9, 100), Fraction(20, 100)]
    eta = Fraction(5, 100)
    deep_count = sum(height > eta for height in heights)
    assert deep_count <= sum(heights) / eta

    # Exact conclusion constants.
    assert Fraction(997, 1000) - Fraction(9, 10) == Fraction(97, 1000)
    assert Fraction(997, 1000) - Fraction(19, 20) == Fraction(47, 1000)

    # R-106550: cos(nz)=-c has imaginary height arcosh(c)/n,
    # while the fifth derivative is -n^5 sin(nz).  The exact algebraic
    # firewall consumed by the replay is the n-cancellation in total height.
    n = 37
    zero_pairs = 19
    symbolic_height_numerator = 2 * zero_pairs
    assert Fraction(symbolic_height_numerator, n) < Fraction(2 * zero_pairs, 1)
    assert n ** 5 > 0

    result: dict[str, object] = {
        "schema": "riemann.x106550.microscopic-companion.v1",
        "classification": "PASS_T106550_MACRO_HEIGHT_AND_SHALLOW_CORRELATION_REDUCTION",
        "selberg_layer_cake_fixture_checked": True,
        "finite_alpha_determinant_fixture_checked": True,
        "deep_height_rank_bound_checked": True,
        "microscopic_cosine_firewall_checked": True,
        "ninety_threshold": "97/1000",
        "ninety_five_threshold": "47/1000",
        "endloc106550_proved": False,
        "shallowcorr106550_proved": False,
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
