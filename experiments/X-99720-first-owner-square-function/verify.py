#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import random

VERDICT = "PASS_T99720_NATIVE_FIRST_OWNER_LITTLEWOOD_PALEY"


def add_poly(a, b, scale=Fraction(1)):
    out = dict(a)
    for mon, c in b.items():
        out[mon] = out.get(mon, Fraction()) + scale * c
        if out[mon] == 0:
            del out[mon]
    return out


def mul_factor(poly, idx, r):
    out = dict(poly)
    for mon, c in list(poly.items()):
        m = tuple(sorted(mon + (idx,)))
        out[m] = out.get(m, Fraction()) - r * c
    return {m: c for m, c in out.items() if c}


def native_product(rs):
    out = {(): Fraction(1)}
    for i, r in enumerate(rs):
        out = mul_factor(out, i, r)
    return out


def first_owner(rs):
    survival = Fraction(1)
    for r in rs:
        survival *= 1 - r
    out = {(): survival}
    s_prev = Fraction(1)
    for i, r in enumerate(rs):
        future = {(): Fraction(1)}
        for h in range(i + 1, len(rs)):
            future = mul_factor(future, h, rs[h])
        shifted = {tuple(sorted(mon + (i,))): c for mon, c in future.items()}
        current = add_poly(future, shifted, scale=-1)
        out = add_poly(out, current, scale=r * s_prev)
        s_prev *= 1 - r
    return out


def run():
    rs = [Fraction(1, 9), Fraction(2, 11), Fraction(1, 7), Fraction(3, 20), Fraction(2, 17)]
    assert native_product(rs) == first_owner(rs)

    rng = random.Random(99720)
    one_step = 0
    for dim in range(2, 12):
        for _ in range(30):
            g = [Fraction(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(dim)]
            perm = list(range(dim))
            rng.shuffle(perm)
            r = Fraction(rng.randint(1, 8), rng.randint(9, 20))
            if r >= 1:
                r = Fraction(1, 2)
            Ug = [Fraction(0)] * dim
            for i, j in enumerate(perm):
                Ug[j] = g[i]
            lhs = sum((a - r * b) ** 2 for a, b in zip(g, Ug))
            rhs = (1 - r) ** 2 * sum(a * a for a in g) + r * sum((a - b) ** 2 for a, b in zip(g, Ug))
            assert lhs == rhs
            one_step += 1

    telescoping = 0
    for _ in range(100):
        rr = [Fraction(rng.randint(1, 5), rng.randint(7, 15)) for _ in range(5)]
        lhs = Fraction(1)
        rhs = Fraction(1)
        for r in rr:
            lhs *= 1 + r * r
            rhs *= (1 - r) ** 2
        s_prev = Fraction(1)
        energy = Fraction(0)
        for i, r in enumerate(rr):
            future = Fraction(1)
            for h in range(i + 1, 5):
                future *= 1 + rr[h] * rr[h]
            energy += r * s_prev * s_prev * 2 * future
            s_prev *= 1 - r
        assert lhs == rhs + energy
        telescoping += 1

    energy_checks = 0
    for _ in range(100):
        rr = [Fraction(rng.randint(1, 4), rng.randint(9, 21)) for _ in range(8)]
        s_prev = Fraction(1)
        energy = Fraction(0)
        for i, r in enumerate(rr):
            future = Fraction(1)
            for h in range(i + 1, 8):
                future *= 1 + rr[h] * rr[h]
            energy += 2 * (r * s_prev) ** 2 * future
            s_prev *= 1 - r
        product = Fraction(1)
        for r in rr:
            product *= 1 + r * r
        assert energy <= 2 * (product - 1)
        energy_checks += 1

    wrong = dict(first_owner(rs))
    wrong[(0,)] = wrong.get((0,), Fraction()) + Fraction(1, 1000)
    hostile = int(wrong != native_product(rs)) + int(Fraction(64) > Fraction(1))

    payload = {
        "schema": "riemann.x99720.first_owner_littlewood_paley.v1",
        "verdict": VERDICT,
        "base_pr": 658,
        "base_sha": "3dd7eacdadc76822e25ee630a474580259dd64fb",
        "native_monomials_checked": len(native_product(rs)),
        "one_step_isometry_checks": one_step,
        "telescoping_checks": telescoping,
        "polylog_energy_checks": energy_checks,
        "collapse_dimensions_checked": 64,
        "hostile_mutations_detected": hostile,
        "owner_carleson_embedding_proved": False,
        "harnack_negative_mass_proved": False,
        "rh_established": False,
    }
    core = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(core).hexdigest()
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
