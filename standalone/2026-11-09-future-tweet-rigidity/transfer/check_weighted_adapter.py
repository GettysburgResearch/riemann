#!/usr/bin/env python3
"""Exact checks of weighted completion, affine reindexing, and chirp obstruction.

Uses the companion checker's independently specified cyclotomic arithmetic.
No floating-point tolerances or assertions about asymptotic cancellation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE / "coupled"))
from verify import Cyclotomic, Field  # noqa: E402


def run_case(q: int, orientation: int) -> dict:
    field, ring = Field(q), Cyclotomic(q)
    counts = Counter()

    def check(name, actual, expected):
        counts[name] += 1
        if actual != expected:
            raise AssertionError((q, orientation, name, actual, expected))

    def character(x):
        return ring.zero if not x else ring.monomial(orientation * field.logs[x], 0)

    def atom(x, y):
        return ring.mul(character(x), ring.conj(character(y)))

    def phase(x):
        return ring.monomial(0, x % q)

    f = [ring.scale(ring.monomial(x % 6, 0), (3 * x + 1) % 7 - 3) for x in range(q)]
    g = [ring.scale(ring.monomial((2 * x + 1) % 6, 0), (5 * x + 2) % 9 - 4) for x in range(q)]
    w = [(7 * h + 2) % 11 - 5 for h in range(q)]
    packets = [[ring.mul(f[x], ring.conj(g[(x-h) % q])) for x in range(q)] for h in range(q)]
    hats = [[ring.sum(ring.mul(packets[h][x], phase(-t*x)) for x in range(q))
             for t in range(q)] for h in range(q)]
    kernels = [ring.sum(ring.mul(atom(y, (y-1) % q), phase(z*y)) for y in range(q))
               for z in range(q)]

    direct = ring.sum(ring.scale(ring.mul(packets[h][x], atom(x, (x-h) % q)), w[h])
                      for h in range(q) for x in range(q))
    diag = ring.scale(ring.sum(packets[0][x] for x in range(1, q)), q * w[0])
    zero_frequency = ring.neg(ring.sum(ring.scale(hats[h][0], w[h]) for h in range(1, q)))
    off = ring.sum(ring.scale(ring.mul(hats[h][t], kernels[h*t % q]), w[h])
                   for h in range(1, q) for t in range(1, q))
    check("axis_separated_completion", ring.scale(direct, q), ring.add(ring.add(diag, zero_frequency), off))

    f_energy = ring.sum(ring.mul(z, ring.conj(z)) for z in f)
    g_energy = ring.sum(ring.mul(z, ring.conj(z)) for z in g)
    hat_energy = ring.sum(ring.mul(z, ring.conj(z)) for row in hats for z in row)
    check("distinct_vector_moyal", hat_energy, ring.scale(ring.mul(f_energy, g_energy), q))

    for a, b in ((1, 1), (2, 3), (q-1, 2)):
        lhs = ring.sum(ring.scale(ring.mul(ring.mul(f[p], ring.conj(g[s])), atom(a*p % q, b*s % q)),
                                 w[(a*p-b*s) % q]) for p in range(q) for s in range(q))
        ai, bi = field.inv(a), field.inv(b)
        rhs = ring.sum(ring.scale(ring.mul(ring.mul(f[ai*x % q], ring.conj(g[bi*y % q])), atom(x, y)),
                                 w[(x-y) % q]) for x in range(q) for y in range(q))
        check("affine_reindexing", lhs, rhs)
    for a, b in ((0, 1), (2, 0), (0, 0)):
        lhs = ring.sum(ring.scale(ring.mul(ring.mul(f[p], ring.conj(g[s])), atom(a*p % q, b*s % q)),
                                 w[(a*p-b*s) % q]) for p in range(q) for s in range(q))
        check("affine_nonunit_mask", lhs, ring.zero)

    chirp_sizes = []
    for c in (1, 2):
        for h in range(q):
            for t in range(q):
                actual = ring.sum(phase(c*x*x-c*(x-h)*(x-h)-t*x) for x in range(q))
                expected = ring.scale(phase(-c*h*h), q) if t == 2*c*h % q else ring.zero
                check("exact_chirp_support", actual, expected)
        # Independently recover row support by exponent counting. Every nonzero
        # row has a distinct nonzero column and modulus q: singular values q.
        columns = [2*c*h % q for h in range(1, q)]
        check("chirp_nonzero_permutation", sorted(columns), list(range(1, q)))
        chirp_sizes.append({"c": c, "nonzero_matrix_rank": q-1,
                            "singular_value": q, "multiplicity": q-1,
                            "nuclear_over_frobenius_squared": q-1})
    # Deleting the actual h=0 axis gives a false answer for this signed example.
    check("negative_erased_diagonal", ring.add(zero_frequency, off) == ring.scale(direct, q), False)

    return {"q": q, "orientation": orientation, "checks": dict(sorted(counts.items())),
            "chirp": chirp_sizes}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [run_case(q, orientation) for q in (7, 13, 19) for orientation in (1, 5)]
    result = {"status": "PASS", "arithmetic": "exact integers in Q(zeta_6,zeta_q)",
              "cases": cases, "total_predicates": sum(sum(c["checks"].values()) for c in cases),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "arithmetic_dependency_sha256": hashlib.sha256((PACKAGE / "coupled/verify.py").read_bytes()).hexdigest(),
              "scope": "finite identity and separation-cost checks; no native asymptotic claim"}
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
