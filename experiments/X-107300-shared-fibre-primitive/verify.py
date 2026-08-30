#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from random import Random


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm2(u):
    return dot(u, u)


def aggregate(values, cells, n_cells):
    out = [Fraction(0) for _ in range(n_cells)]
    for value, cell in zip(values, cells):
        out[cell] += value
    return out


def h_form(v, q):
    return norm2(v) - Fraction(1, q) * sum(v) ** 2


def wick_direct(a, b, left_cells, right_cells, ell, rho):
    z = []
    cells = []
    n_right_cells = max(right_cells) + 1
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            z.append(ai * bj)
            cells.append(right_cells[j] * (max(left_cells) + 1) + left_cells[i])
    agg = aggregate(z, cells, n_right_cells * (max(left_cells) + 1))
    # reshape and apply H_ell tensor H_rho directly
    nr = n_right_cells
    nl = max(left_cells) + 1
    matrix = [[agg[x * nl + y] for y in range(nl)] for x in range(nr)]
    term = Fraction(0)
    for x in range(nr):
        for y in range(nl):
            for xp in range(nr):
                for yp in range(nl):
                    sx = Fraction(int(x == xp)) - Fraction(1, ell)
                    sy = Fraction(int(y == yp)) - Fraction(1, rho)
                    term += matrix[x][y] * matrix[xp][yp] * sx * sy
    d = (1 - Fraction(1, ell)) * (1 - Fraction(1, rho))
    return term - d * norm2(z)


def wick_factor(a, b, left_cells, right_cells, ell, rho):
    al = aggregate(a, left_cells, max(left_cells) + 1)
    br = aggregate(b, right_cells, max(right_cells) + 1)
    d = (1 - Fraction(1, ell)) * (1 - Fraction(1, rho))
    return h_form(al, rho) * h_form(br, ell) - d * norm2(a) * norm2(b)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    rng = Random(107300)
    exact_checks = 0
    for _ in range(120):
        nx, ny = rng.randint(1, 5), rng.randint(1, 5)
        lc, rc = rng.randint(1, 3), rng.randint(1, 3)
        a = [Fraction(rng.randint(-4, 4)) for _ in range(nx)]
        b = [Fraction(rng.randint(-4, 4)) for _ in range(ny)]
        left_cells = [rng.randrange(lc) for _ in range(nx)]
        right_cells = [rng.randrange(rc) for _ in range(ny)]
        ell, rho = rng.choice([(5, 7), (7, 11), (11, 13)])
        assert wick_direct(a, b, left_cells, right_cells, ell, rho) == \
            wick_factor(a, b, left_cells, right_cells, ell, rho)
        exact_checks += 1

    pattern = [Fraction(3), Fraction(3)] + [Fraction(-1)] * 8
    assert sum(pattern) == -2
    assert norm2(pattern) == 26
    mean_energy = sum(pattern) ** 2 / 10
    primitive_energy = norm2(pattern) - mean_energy
    assert mean_energy == Fraction(2, 5)
    assert primitive_energy == Fraction(128, 5)
    grades = [
        mean_energy * mean_energy,
        primitive_energy * mean_energy,
        mean_energy * primitive_energy,
        primitive_energy * primitive_energy,
    ]
    assert sum(grades) == 676
    assert grades == [
        Fraction(4, 25),
        Fraction(256, 25),
        Fraction(256, 25),
        Fraction(16384, 25),
    ]
    assert sum(pattern) ** 4 - norm2(pattern) ** 2 == -660
    exact_checks += 10

    equal = [Fraction(1), Fraction(1)]
    assert sum(equal) ** 4 - norm2(equal) ** 2 == 12
    exact_checks += 1

    a1, b1 = [Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]
    a2, b2 = [Fraction(2), Fraction(0)], [Fraction(1), Fraction(1)]
    assert sum(a1) * sum(b1) == sum(a2) * sum(b2) == 4
    assert norm2(a1) * norm2(b1) == 4
    assert norm2(a2) * norm2(b2) == 8
    exact_checks += 3

    payload = {
        "schema": "riemann.x107300.shared-fibre-primitive.v1",
        "classification": "PASS_T107300_SHARED_FIBRE_PRIMITIVE_TRACE",
        "exact_checks": exact_checks,
        "rectangular_factorization_checked": True,
        "augmentation_primitive_split_checked": True,
        "live_history_wick_coefficient": "-660*d_(ell,rho)",
        "rectglue107300_proved": False,
        "primtrace107300_proved": False,
        "prinbind107300_proved": False,
        "rh_established": False,
        "grh_established": False,
    }
    digest_source = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(digest_source).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
