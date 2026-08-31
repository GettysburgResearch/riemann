"""Non-author frozen review: direct Laurent composition and Fraction Sturm routes."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
from collections import defaultdict
from fractions import Fraction as Q
from itertools import pairwise
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[4]
SHA = "1c3c6880ce4db8b15a5e26c3c27e822f3f46365a"
DIRECTORY = "research/l-families/atlas/generalized/"
STEM = "segre_higher_power_unitary_chambers"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source(path, commit=SHA):
    return subprocess.check_output(["git", "show", commit + ":" + path], cwd=ROOT)


def digest(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def normalize(p):
    p = trim(p[:])
    denominator = math.lcm(*(v.denominator for v in p))
    integers = [int(v * denominator) for v in p]
    content = math.gcd(*integers)
    return [Q(v // content) for v in integers] if content else [Q(0)]


def remainder(a, b):
    a = a[:]
    while len(a) >= len(b) and any(a):
        scale = a[-1] / b[-1]
        shift = len(a) - len(b)
        for j, v in enumerate(b):
            a[j + shift] -= scale * v
        trim(a)
    return a


def sturm(p):
    p = normalize([Q(v) for v in p])
    require(len(p) >= 2, "nonconstant Sturm polynomial")
    seq = [p, normalize([j * p[j] for j in range(1, len(p))])]
    while len(seq[-1]) > 1:
        rem = remainder(seq[-2], seq[-1])
        if not any(rem):
            break
        seq.append(normalize([-v for v in rem]))
    return seq


def evaluate(p, x):
    result = Q(0)
    for v in reversed(p):
        result = result * x + v
    return result


def variation(seq, x):
    values = [evaluate(p, x) for p in seq]
    signs = [1 if v > 0 else -1 for v in values if v]
    return sum(a != b for a, b in pairwise(signs))


def lmul(a, b):
    c = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] += x * y
    return {k: v for k, v in c.items() if v}


def ladd(a, b, scale=1):
    c = defaultdict(int, a)
    for i, v in b.items():
        c[i] += scale * v
    return {k: v for k, v in c.items() if v}


def character(m):
    # Complete h_r directly from all triples i+j+k=r, not a recurrence or word DP.
    maximum = 2 * m + 2
    powers = []
    for r in range(maximum + 1):
        h = defaultdict(int)
        for i in range(r + 1):
            for k in range(r - i + 1):
                h[i - k] += 1
        value = {0: 1}
        for _ in range(m):
            value = lmul(value, h)
        powers.append(value)
    denominator = [{0: 1}]
    for exponent in range(-m, m + 1):
        new = [dict(v) for v in denominator] + [{}]
        for j, v in enumerate(denominator):
            new[j + 1] = ladd(new[j + 1], {k + exponent: a for k, a in v.items()}, -1)
        denominator = new
    coefficients = []
    for r in range(maximum + 1):
        value = {}
        for j in range(min(r, len(denominator) - 1) + 1):
            value = ladd(value, lmul(denominator[j], powers[r - j]))
        coefficients.append(value)
    require(not any(coefficients[2 * m - 1 :]), "independent recurrence tail")
    result = {
        (j, e): v
        for j, row in enumerate(coefficients[: 2 * m - 1])
        for e, v in row.items()
    }
    require(sum(result.values()) == math.factorial(2 * m) // 2**m, "word dimension")
    return coefficients[: 2 * m - 1], result


def cheb(maximum):
    result = [[2], [0, 1]]
    for j in range(2, maximum + 1):
        row = [0] + result[-1]
        for k, v in enumerate(result[-2]):
            row[k] -= v
        result.append(trim(row))
    return result


def fold(coefficients, m):
    cx = cheb(max(abs(k) for row in coefficients for k in row))
    xcoeff = []
    for row in coefficients:
        require(all(v == row.get(-k, 0) for k, v in row.items()), "Laurent reciprocity")
        polynomial = [row.get(0, 0)]
        for e, value in row.items():
            if e > 0:
                while len(polynomial) < len(cx[e]):
                    polynomial.append(0)
                for j, v in enumerate(cx[e]):
                    polynomial[j] += value * v
        xcoeff.append(trim(polynomial))
    cz = cheb(m - 1)
    terms = defaultdict(int)
    for i, value in enumerate(xcoeff[m - 1]):
        terms[i, 0] += value
    for j in range(1, m):
        for i, a in enumerate(xcoeff[m - 1 + j]):
            for k, b in enumerate(cz[j]):
                terms[i, k] += a * b
    return {k: Q(v) for k, v in terms.items() if v}


def specialize(terms, x, m):
    p = [Q(0)] * m
    for (i, j), value in terms.items():
        p[j] += value * x**i
    return trim(p)


def audit():
    report = json.loads(source(DIRECTORY + STEM + ".json"))
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    canonical = json.dumps(
        unsigned, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    require(
        hashlib.sha256(canonical).hexdigest() == report["payload_sha256"], "payload SHA"
    )
    for path, sha in report["artifact_sha256_lf"].items():
        require(digest(source(path)) == sha, "artifact SHA")
    for row in report["sources"]["parents"]:
        raw = source(row["path"], row["commit"])
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and digest(raw) == row["sha256_lf"], "source seal"
        )
        if row["current_copy_required"]:
            require(
                digest(source(row["path"])) == row["sha256_lf"],
                "current source binding",
            )
    x, z = sp.symbols("x z")
    results = []
    all_terms = {}
    for table, words in zip(report["chambers"], report["characters"]):
        m = table["power"]
        coefficients, char = character(m)
        require(
            char == {(a, b): n for a, b, n in words["full_character"]},
            "complete independent character",
        )
        terms = fold(coefficients, m)
        all_terms[m] = terms
        require(
            terms == {tuple(a): Q(*b) for a, b in table["M_terms"]}, "folded polynomial"
        )
        expression = sum(
            sp.Rational(v.numerator, v.denominator) * x**i * z**j
            for (i, j), v in terms.items()
        )
        polynomials = {
            "discriminant": sp.discriminant(expression, z),
            "minus_endpoint": expression.subs(z, -2),
            "plus_endpoint": expression.subs(z, 2),
        }
        for name, item in table["factorizations"].items():
            product = sp.Rational(*item["content"])
            for factor in item["factors"]:
                product *= (
                    sp.Poly.from_list(factor["coefficients_descending"], x).as_expr()
                    ** factor["multiplicity"]
                )
            require(
                sp.expand(product - polynomials[name]) == 0, "factorization identity"
            )
        exception = x * (x + 1) * (x - 1) * (x**2 + x - 1)
        for item in table["factorizations"].values():
            for factor in item["factors"]:
                if factor["multiplicity"] > 1:
                    polynomial = sp.Poly.from_list(
                        factor["coefficients_descending"], x
                    ).as_expr()
                    require(
                        sp.rem(exception, polynomial, x) == 0,
                        "exceptional multiple wall",
                    )
        for i, p in enumerate(polynomials.values()):
            for q in list(polynomials.values())[i + 1 :]:
                common = sp.Poly(sp.gcd(p, q), x).sqf_part().as_expr()
                require(sp.rem(exception, common, x) == 0, "exceptional shared wall")
        factors = {}
        root_total = 0
        for row in table["wall_factors"]:
            p = [Q(v) for v in reversed(row["coefficients_descending"])]
            seq = sturm(p)
            require(len(seq[-1]) == 1, "squarefree factor")
            counts = [variation(seq, Q(-2)), variation(seq, Q(2))]
            require(
                counts == row["sturm_outer_variations"], "independent factor variations"
            )
            require(
                counts[0] - counts[1] == row["real_roots_in_minus2_plus2"],
                "wall root total",
            )
            root_total += counts[0] - counts[1]
            factors[row["id"]] = p, seq
        require(root_total == len(table["walls"]), "all wall roots accounted")
        previous = Q(-2)
        for row in table["walls"]:
            lo, hi = (Q(*v) for v in row["bracket"])
            require(
                previous < lo <= hi < 2 and hi - lo <= Q(1, 10**8),
                "ordered wall isolators",
            )
            p, seq = factors[row["factor"]]
            if lo == hi:
                require(evaluate(p, lo) == 0, "rational wall")
            else:
                variations = [variation(seq, lo), variation(seq, hi)]
                require(
                    variations == row["sturm_bracket_variations"]
                    and variations[0] - variations[1] == 1,
                    "single wall root",
                )
            previous = hi
        components = []
        for cell in table["cells"]:
            parameter = Q(*cell["sample"])
            polynomial = specialize(terms, parameter, m)
            seq = sturm(polynomial)
            require(len(seq[-1]) == 1, "simple cell polynomial")
            require(
                evaluate(polynomial, Q(-2)) and evaluate(polynomial, Q(2)),
                "no endpoint root",
            )
            variations = [variation(seq, Q(-2)), variation(seq, Q(2))]
            count = variations[0] - variations[1]
            require(
                variations == cell["sturm_variations"]
                and count == cell["roots_in_open_interval"],
                "independent cell Sturm",
            )
            require((count == m - 1) is cell["pure"], "pure cell iff all roots")
            if cell["pure"]:
                if components and components[-1][1] == cell["left_wall"]:
                    components[-1][1] = cell["right_wall"]
                else:
                    components.append([cell["left_wall"], cell["right_wall"]])
        require(
            components == table["pure_closed_components_wall_indices"],
            "component closure table",
        )
        results.append(
            {
                "m": m,
                "character_terms": len(char),
                "word_total": sum(char.values()),
                "walls": root_total,
                "cells": len(table["cells"]),
                "components": len(components),
            }
        )
    for item in report["heldout_power6"]:
        seq = sturm(specialize(all_terms[6], Q(*item["x"]), 6))
        require(
            (variation(seq, Q(-2)) - variation(seq, Q(2)) == 5) is item["pure"],
            "heldout verdict",
        )
    for item in report["nonnesting"]:
        for m in (5, 6):
            seq = sturm(specialize(all_terms[m], Q(*item["x"]), m))
            require(
                (variation(seq, Q(-2)) - variation(seq, Q(2)) == m - 1)
                is item["power" + str(m)]["pure"],
                "nonnesting witness",
            )
    for parameter, target in (
        (-1, (z - 2) ** 2 * (z + 1) ** 3),
        (0, z**2 * (z - 2) * (z + 2) ** 2),
        (1, (z - 2) * (z - 1) * (z + 1) * (z + 2) * (z + 63)),
    ):
        coefficients = specialize(all_terms[6], Q(parameter), 6)
        require(
            coefficients == [Q(v) for v in reversed(sp.Poly(target, z).all_coeffs())],
            "heldout sixth torsion polynomial",
        )
    cubic = fold(character(3)[0], 3)
    require(
        specialize(cubic, Q(-3, 2), 3) == [Q(-3, 8), Q(-1), Q(1)],
        "independent SU3 base polynomial",
    )
    print(
        json.dumps(
            {
                "status": "PASS",
                "source": SHA,
                "independent_routes": "direct Laurent compositions; ordinary Fraction Euclidean Sturm, not pseudo-remainders",
                "results": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    audit()
