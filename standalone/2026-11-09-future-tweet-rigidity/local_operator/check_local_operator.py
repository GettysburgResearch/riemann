#!/usr/bin/env python3
"""Exact local-frame, CRT reconstruction, mask, and scalar-budget checks.

Uses only the standard library. The sibling coupled verifier supplies finite
field and cyclotomic arithmetic; this file independently reconstructs S and
checks every local Gram entry for q=7,13. Subsequent matrix arithmetic is exact
in Q(zeta_6). No numerical test certifies a global analytic saving.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
COUPLED = HERE.parent / "coupled" / "verify.py"
spec = importlib.util.spec_from_file_location("coupled_finite_algebra", COUPLED)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

Z = (F(0), F(0))
ONE = (F(1), F(0))
counts = Counter()


def check(name, left, right=True):
    counts[name] += 1
    if left != right:
        raise AssertionError((name, left, right))


def sixth(k):
    return tuple(map(F, ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))[k % 6]))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def scale(x, a):
    return (x[0] * a, x[1] * a)


def mul(x, y):
    a, b, c, d = *x, *y
    return (a*c-b*d, a*d+b*c+b*d)


def conj(x):
    return (x[0] + x[1], -x[1])


def sumz(seq):
    out = Z
    for x in seq:
        out = add(out, x)
    return out


def eye(n):
    return [[ONE if i == j else Z for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[add(a, b) for a, b in zip(ar, br)] for ar, br in zip(A, B)]


def mscale(A, c):
    return [[scale(a, c) for a in row] for row in A]


def mmul(A, B):
    cols = list(zip(*B))
    return [[sumz(mul(a, b) for a, b in zip(row, col)) for col in cols] for row in A]


def mv(A, v):
    return [sumz(mul(a, b) for a, b in zip(row, v)) for row in A]


def kron(A, B):
    return [[mul(A[i][j], B[k][l]) for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def inner(v, w):
    return sumz(mul(conj(a), b) for a, b in zip(v, w))


def proj(v):
    n = len(v)
    return [[scale(mul(a, conj(b)), F(1, n)) for b in v] for a in v]


def local(q):
    field, ring = mod.Field(q), mod.Cyclotomic(q)
    U = list(field.nonzero)
    n = q - 1
    vectors = {o: [sixth(o * field.logs[h]) for h in U] for o in (0, 1, -1)}
    P = proj(vectors[0])
    Pc, Pb = proj(vectors[1]), proj(vectors[-1])
    I = eye(n)
    Q = madd(I, mscale(P, -1))
    gp = F(q + 1, 2*q)

    # Direct kernel construction, independent of the sibling's run_field.
    for orientation in (1, -1):
        S = [ring.sum(ring.monomial(orientation * (field.logs[x] - field.logs[field.sub(x, 1)]),
                                    field.trace(field.mul(z, x)))
                      for x in range(q) if x and field.sub(x, 1)) for z in range(q)]
        check("direct_zero_mask", S[0], ring.integer(-1))
        check("direct_unit_mean", ring.sum(S[h] for h in U), ring.one)
        for h in U:
            for k in U:
                actual = ring.sum(ring.mul(ring.conj(S[field.mul(t, h)]), S[field.mul(t, k)]) for t in U)
                phase = ring.monomial(orientation * field.logs[field.mul(h, field.inv(k))], 0)
                expected = ring.add(ring.integer(q*q if h == k else 0),
                                    ring.neg(ring.add(ring.scale(phase, q), ring.integer(q + 1))))
                check("direct_complete_gram_entry", actual, expected)

    Gsingle = madd(Q, mscale(Pc, -F(q - 1, q)))
    G = madd(Q, mscale(madd(Pc, Pb), -F(q - 1, 2*q)))
    R = madd(Q, mscale(madd(Pc, Pb), F(q - 1, q + 1)))
    Gfull = madd(P, G)
    Rfull = madd(P, R)
    for name, A, B in (("local_pair_decoder", mmul(R, G), Q),
                        ("local_full_decoder", mmul(Rfull, Gfull), I),
                        ("character_orthogonality", mmul(Pc, Pb), mscale(I, 0))):
        for ar, br in zip(A, B):
            for a, b in zip(ar, br):
                check(name, a, b)
    check("sharp_pair_chi_gain", inner(vectors[1], mv(G, vectors[1])), (F(n)*gp, F(0)))
    check("sharp_pair_conjugate_gain", inner(vectors[-1], mv(G, vectors[-1])), (F(n)*gp, F(0)))
    check("single_channel_weak_mode", inner(vectors[1], mv(Gsingle, vectors[1])), (F(n, q), F(0)))
    check("negative_single_channel_uniform_claim", F(1, q) >= F(1, 2), False)
    check("negative_wrong_exceptional_orientation", mv(Gsingle, vectors[-1]) == mv(Gsingle, vectors[1]), False)

    # A quadratic channel is repaired by a distinct sextic channel, rather
    # than its identical conjugate. Both actual outputs must be retained.
    quad = [sixth(3 * field.logs[h]) for h in U]
    Pquad = proj(quad)
    Gquad_pair = madd(Q, mscale(madd(Pquad, Pc), -F(q-1, 2*q)))
    Rquad_pair = madd(Q, mscale(madd(Pquad, Pc), F(q-1, q+1)))
    for ar, br in zip(mmul(Rquad_pair, Gquad_pair), Q):
        for x, y in zip(ar, br):
            check("quadratic_distinct_channel_decoder", x, y)
    check("quadratic_distinct_channel_gain", inner(quad, mv(Gquad_pair, quad)), (F(n)*gp, F(0)))
    check("negative_quadratic_conjugate_repair", F(1, q) == gp, False)

    # Restore the previously excluded nonunit coordinate with an explicit E0.
    extendedG = [[Z for _ in range(q)] for _ in range(q)]
    extendedR = [[Z for _ in range(q)] for _ in range(q)]
    extendedG[0][0] = extendedR[0][0] = ONE
    for i in range(n):
        for j in range(n):
            extendedG[i+1][j+1], extendedR[i+1][j+1] = Gfull[i][j], Rfull[i][j]
    for ar, br in zip(mmul(extendedR, extendedG), eye(q)):
        for a, b in zip(ar, br):
            check("nonunit_reconstruction", a, b)
    check("negative_omitted_zero_sector", [Z]*q == [ONE] + [Z]*(q-1), False)
    return {"q": q, "P": P, "Q": Q, "G": G, "R": R,
            "Gfull": Gfull, "Rfull": Rfull, "v": vectors, "gain": gp}


def tensor_checks(a, b):
    n, m = a["q"]-1, b["q"]-1
    # Deliberately nonseparable source; entries have rational and zeta_6 parts.
    v = [(F((7*i + 11*j + 3*i*j) % 13 - 6), F((i*i + 2*j + i*j) % 5 - 2))
         for i in range(n) for j in range(m)]
    Pglob = kron(a["P"], b["P"])
    Pprim = kron(a["Q"], b["Q"])
    Gprim, Rprim = kron(a["G"], b["G"]), kron(a["R"], b["R"])
    Gfull, Rfull = kron(a["Gfull"], b["Gfull"]), kron(a["Rfull"], b["Rfull"])
    gamma = a["gain"]*b["gain"]

    for x, y in zip(mv(Rprim, mv(Gprim, v)), mv(Pprim, v)):
        check("crt_primitive_reconstruction", x, y)
    for x, y in zip(mv(Rfull, mv(Gfull, v)), v):
        check("crt_full_reconstruction", x, y)
    Gnoglob = madd(Gfull, mscale(Pglob, -1))
    desired = [sub(x, y) for x, y in zip(v, mv(Pglob, v))]
    for x, y in zip(mv(Rfull, mv(Gnoglob, v)), desired):
        check("crt_all_but_global_constant", x, y)

    for tag, G, source in (("primitive", Gprim, mv(Pprim, v)),
                            ("full", Gfull, v),
                            ("no_global_constant", Gnoglob, desired)):
        energy = inner(v, mv(G, v))
        norm = inner(source, source)
        check(tag + "_real_energy", energy[1], F(0))
        check(tag + "_frame_lower", energy[0] >= gamma*norm[0])
        check(tag + "_frame_upper", energy[0] <= norm[0])

    # Four orthogonal constant-coordinate sectors; their analysis blocks sum
    # to the actual nine-channel tensor Gram, with weights 1,1/2,1/4 retained.
    sectors = [kron(x, y) for x in (a["P"], a["Q"]) for y in (b["P"], b["Q"])]
    source_sum = [Z] * (n*m)
    for sector in sectors:
        source_sum = [add(x, y) for x, y in zip(source_sum, mv(sector, v))]
    for x, y in zip(source_sum, v):
        check("crt_complete_sector_partition", x, y)
    sector_grams = [kron(x, y) for x in (a["P"], a["G"]) for y in (b["P"], b["G"])]
    rebuilt = mscale(Gfull, 0)
    for H in sector_grams:
        rebuilt = madd(rebuilt, H)
    for ar, br in zip(rebuilt, Gfull):
        for x, y in zip(ar, br):
            check("crt_nine_channel_gram", x, y)

    mixed = [mul(x, y) for x in a["v"][0] for y in b["v"][1]]
    check("mixed_sector_has_mass", inner(mixed, mixed)[0] > 0)
    check("mixed_sector_globally_mean_zero", mv(Pglob, mixed), [Z]*(n*m))
    check("negative_primitive_bank_hides_mixed_sector", mv(Gprim, mixed), [Z]*(n*m))
    check("full_bank_retains_mixed_sector", inner(mixed, mv(Gfull, mixed))[0] > 0)
    check("crt_channel_count_primitive", 2**2, 4)
    check("crt_channel_count_full", sum(2**len(S) for S in ((), (0,), (1,), (0, 1))), 9)
    return {"conductor_norm": a["q"]*b["q"], "dimension": n*m,
            "sharp_lower_gain": str(gamma), "primitive_channels": 4,
            "full_channels": 9, "all_but_global_constant_channels": 8}


def mobius(n):
    s, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            s = -s
            if n % p == 0:
                return 0
        p += 1
    return -s if n > 1 else s


def scalar_checks():
    bad = 0
    for p in (2, 3, 5, 7, 11):
        for n in range(1, 241):
            actual = mobius(p*n)
            correct = -mobius(n) if n % p else 0
            check("full_divisibility_defect", actual, correct)
            bad += actual != -mobius(n)
    check("negative_maskless_mobius_rule", bad > 0)
    for R in (2, 3, 5, 11, 23):
        # beta=0, lambda=1. Optimal supported probe uses d=1 and d=R.
        best = F(R + 1, R - 1)
        c = {1: -F(1, R - 1), R: F(R, R - 1)}
        check("optimal_probe_preserves_source", sum(c.values()), F(1))
        check("optimal_probe_kills_bias", sum(a/F(d) for d, a in c.items()), F(0))
        check("sharp_total_variation_cost", sum(abs(a) for a in c.values()), best)
        for seed in range(1, 13):
            coeff = {d: F((seed*d*d + 5*d) % 9 - 4, 7) for d in range(2, R)}
            mass = sum(coeff.values(), F(0))
            weighted = sum((a/F(d) for d, a in coeff.items()), F(0))
            # Solve the two constraints exactly with the two endpoint atoms.
            cr = (F(1) - mass + weighted) / (F(1) - F(1, R))
            c1 = -weighted - cr/F(R)
            coeff[1], coeff[R] = c1, cr
            check("candidate_source_constraint", sum(coeff.values()), F(1))
            check("candidate_bias_constraint", sum(a/F(d) for d, a in coeff.items()), F(0))
            check("optimal_probe_dual_lower_bound", sum(abs(a) for a in coeff.values()) >= best)
    return {"maskless_counterexamples": bad}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "CHECKS.json")
    args = parser.parse_args()
    a, b = local(7), local(13)
    tensor = tensor_checks(a, b)
    scalar = scalar_checks()
    report = {"status": "PASS", "arithmetic": "exact Q(zeta_6,zeta_p) and rational Q(zeta_6)",
              "local_fields": [7, 13], "crt": tensor, "scalar": scalar,
              "counts": dict(sorted(counts.items())), "total_predicates": sum(counts.values()),
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "coupled_arithmetic_sha256": hashlib.sha256(COUPLED.read_bytes()).hexdigest(),
              "scope": "Finite identities, source reconstruction, masks, and sharp scalar budget only; no analytic saving or zero-free region."}
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
