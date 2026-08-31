"""Exact multiset characters and Sturm chambers; no floating root fitting."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import pairwise
from math import factorial
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "SEGRE_HIGHER_POWER_UNITARY_CHAMBERS.md"
MANIFEST = HERE / "segre_higher_power_unitary_chambers.sources.json"
FIXTURE = HERE / "segre_higher_power_unitary_chambers.json"
TEST = ROOT / "tests/test_segre_higher_power_unitary_chambers.py"
MAX_BYTES = 2097152
MAX_BITS = 65536
MAX_JSON_DEPTH = 32
MAX_POWER = 6
MAX_STATES = 250000
MAX_TERMS = 10000
MAX_DEGREE = 80
MAX_WALLS = 64
X, T, Z, U = sp.symbols("x T z t")
EXPECTED_MANIFEST = json.loads(r"""{
  "schema": "segre-higher-power-sources-v1",
  "parents": [
    {
      "commit": "4a317ea5c9d7aa016fba58a1d74746e437329ec7",
      "path": "research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md",
      "git_blob": "acc3a0382f3ad919037b156749b4a07a971b429a",
      "sha256_lf": "7dd4af9c9f14c73413d7a233cf64d7b608d94b60af334d08e1a0e0561a5f94a2",
      "current_copy_required": true
    },
    {
      "commit": "4a317ea5c9d7aa016fba58a1d74746e437329ec7",
      "path": "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.py",
      "git_blob": "cd7bddb3953106ded6a923a916e2f4c6d72c328f",
      "sha256_lf": "650b709402a6d79e5263c629377b195b7dbeaa57a6c054d2f08b5886b25d2771",
      "current_copy_required": true
    },
    {
      "commit": "4a317ea5c9d7aa016fba58a1d74746e437329ec7",
      "path": "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.json",
      "git_blob": "13f8fcc7d527d00ec97835d4c224af065dd698b7",
      "sha256_lf": "6b7bc07acebf80812e0b743acfd7476d6a1e7694b9689236cdd5dbdb8f75abac",
      "current_copy_required": true
    },
    {
      "commit": "4a317ea5c9d7aa016fba58a1d74746e437329ec7",
      "path": "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.sources.json",
      "git_blob": "87f2fbc59137b41eb89a6a2553e33026eb1ea3ba",
      "sha256_lf": "6e9780e76a33e4f7de7e4f06c2bfdc29696d028dccbdf913b9cb2b708dd61448",
      "current_copy_required": true
    },
    {
      "commit": "4a317ea5c9d7aa016fba58a1d74746e437329ec7",
      "path": "tests/test_segre_recurrence_syzygy_bridge.py",
      "git_blob": "ae6b004d2c758208148593e914a28786850a5026",
      "sha256_lf": "e4974748050c8087160103a17c889c8ba92a309e763ee9d369deb71f43db7590",
      "current_copy_required": true
    },
    {
      "commit": "e21e44d84077b7703c6795a81c91fc305b3fe344",
      "path": "research/l-families/atlas/generalized/SEGRE_HIGHER_POWER_UNITARY_CHAMBERS.md",
      "git_blob": "b1f9b328f9852919200ffca33a294fb1d2b69014",
      "sha256_lf": "5ea3ed98e388f34b4986d60dcc6cdcf2db8b3d2e903ce273d5307dad175dcf4f",
      "current_copy_required": false
    },
    {
      "commit": "acd91a621244872d49e0e4dfde76775879eadfc1",
      "path": "research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE_AUDIT_4A317EA5.md",
      "git_blob": "9917525809b5c22627d216e8180a4ea29ae32b0c",
      "sha256_lf": "b5abd8d8c788563a241242e4b83d70640643c1b1898df5eb0b358b5e79191ae7",
      "current_copy_required": false
    }
  ],
  "prior_art": [
    {
      "id": "CARNEVALE_VOLL_MACMAHON",
      "title": "Orbit Dirichlet Series and Multiset Permutations",
      "url": "https://angelacarnevale.github.io/papers/orbit.pdf",
      "locator": "Proposition 1.2; equations (2.1)--(2.3); Lemma 2.5; section 2.2",
      "role": "classical Hadamard/Gaussian-binomial/multiset Eulerian dictionary; their bivariate unitary-factor notion differs from pointwise torus purity"
    }
  ]
}""")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    require(type(value) is int and low <= value <= high, "strict integer/range")
    return value


def rational(value):
    require(type(value) in (int, Fraction), "strict rational type")
    value = Fraction(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 1024,
        "rational input bit cap",
    )
    return sp.Rational(value.numerator, value.denominator)


def pair(value):
    value = sp.Rational(value)
    require(
        max(int(value.p).bit_length(), int(value.q).bit_length()) <= MAX_BITS,
        "rational result bit cap",
    )
    return [int(value.p), int(value.q)]


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode()


def render(value):
    def pretty(item, level):
        short = canonical(item).decode()
        if len(short) <= 160 or type(item) not in (list, dict):
            return short
        indent = "  " * (level + 1)
        if type(item) is list:
            rows = [pretty(v, level + 1) for v in item]
            left, right = "[", "]"
        else:
            rows = [
                canonical(k).decode() + ": " + pretty(item[k], level + 1)
                for k in sorted(item)
            ]
            left, right = "{", "}"
        return (
            left
            + "\n"
            + indent
            + (",\n" + indent).join(rows)
            + "\n"
            + "  " * level
            + right
        )

    return pretty(value, 0) + "\n"


def digest(raw):
    require(type(raw) is bytes, "digest bytes type")
    return hashlib.sha256(raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def bounded_bytes(path):
    require(path.stat().st_size <= MAX_BYTES, "file byte cap")
    with path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    require(len(raw) <= MAX_BYTES, "file byte cap")
    return raw


def strict_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON bytes cap/type")
    depth = 0
    quoted = escaped = False
    for byte in raw:
        if quoted:
            if escaped:
                escaped = False
            elif byte == 92:
                escaped = True
            elif byte == 34:
                quoted = False
        elif byte == 34:
            quoted = True
        elif byte in (91, 123):
            depth += 1
            require(depth <= MAX_JSON_DEPTH, "JSON depth cap")
        elif byte in (93, 125):
            depth -= 1

    def pairs(rows):
        out = {}
        for k, v in rows:
            require(k not in out, "duplicate JSON key")
            out[k] = v
        return out

    def bad(_):
        raise ValueError("noninteger JSON number")

    def parse_int(s):
        require(len(s) <= 2000, "JSON integer digit cap")
        return int(s)

    try:
        return json.loads(
            raw,
            object_pairs_hook=pairs,
            parse_float=bad,
            parse_constant=bad,
            parse_int=parse_int,
        )
    except (UnicodeError, RecursionError) as error:
        raise ValueError("JSON encoding/depth") from error


def same_json(actual, expected):
    require(canonical(actual) == canonical(expected), "typed canonical replay differs")


def source_locks():
    same_json(strict_json(bounded_bytes(MANIFEST)), EXPECTED_MANIFEST)
    for row in EXPECTED_MANIFEST["parents"]:
        target = row["commit"] + ":" + row["path"]
        blob = subprocess.check_output(
            ["git", "rev-parse", "--verify", target], cwd=ROOT, text=True
        ).strip()
        require(blob == row["git_blob"], "frozen source blob mismatch")
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", blob], cwd=ROOT, text=True
            )
        )
        require(size <= MAX_BYTES, "source byte cap")
        raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        require(digest(raw) == row["sha256_lf"], "frozen source digest mismatch")
        if row["current_copy_required"]:
            require(
                digest(bounded_bytes(ROOT / row["path"])) == row["sha256_lf"],
                "current source digest mismatch",
            )
    return EXPECTED_MANIFEST


def bounded_poly(expr, *variables):
    p = sp.Poly(expr, *variables, domain=sp.QQ)
    require(p.total_degree() <= MAX_DEGREE, "polynomial degree cap")
    require(len(p.terms()) <= MAX_TERMS, "polynomial term cap")
    for coefficient in p.coeffs():
        pair(coefficient)
    return p


def polynomial_rows(expr, *variables):
    return [
        [list(monomial), pair(coefficient)]
        for monomial, coefficient in bounded_poly(expr, *variables).terms()
    ]


def chebyshev(variable, maximum):
    integer(maximum, 1, MAX_POWER)
    rows = [sp.Integer(2), variable]
    for _ in range(2, maximum + 1):
        rows.append(sp.expand(variable * rows[-1] - rows[-2]))
    return rows


@lru_cache(maxsize=6)
def native_polynomials_cached(m):
    c = chebyshev(X, m)
    d = sp.Poly(1 - T, T)
    for j in range(1, m + 1):
        d *= sp.Poly(1 - c[j] * T + T**2, T)
    h = [sp.Integer(1)]
    for r in range(1, 2 * m + 3):
        h.append(
            sp.expand(
                (X + 1) * h[-1]
                - ((X + 1) * h[-2] if r >= 2 else 0)
                + (h[-3] if r >= 3 else 0)
            )
        )
    powers = [(sp.Poly(value, X, domain=sp.ZZ) ** m).as_expr() for value in h]
    a = [
        sp.expand(sum(d.nth(j) * powers[r - j] for j in range(min(r, d.degree()) + 1)))
        for r in range(len(h))
    ]
    require(all(value == 0 for value in a[2 * m - 1 :]), "annihilator tail identities")
    p = sp.expand(sum(a[j] * T**j for j in range(2 * m - 1)))
    require(
        a[: 2 * m - 1] == list(reversed(a[: 2 * m - 1])), "palindromic coefficients"
    )
    require(a[0] == 1 and a[2 * m - 2] == 1, "monic constant/top")
    cz = chebyshev(Z, m)
    reciprocal = sp.expand(a[m - 1] + sum(a[m - 1 + j] * cz[j] for j in range(1, m)))
    require(
        sp.expand(T ** (m - 1) * reciprocal.subs(Z, T + 1 / T) - p) == 0,
        "reciprocal coordinate identity",
    )
    bounded_poly(p, X, T)
    bounded_poly(reciprocal, X, Z)
    return d.as_expr(), p, reciprocal


def native_polynomials(m):
    integer(m, 1, MAX_POWER)
    return native_polynomials_cached(m)


def multiset_character(m):
    """All words with two copies of each label; counts, last, descents, comajor."""
    integer(m, 1, MAX_POWER)
    n = 2 * m
    # Structural cap before the dynamic state map is built.
    require(3**m * m * (n + 1) * (n * n + 1) <= 10000000, "structural DP cap")
    current = {((0,) * m, -1, 0, 0): 1}
    peak = 1
    transitions = 0
    for length in range(n):
        following = Counter()
        for (counts, last, descents, comajor), value in current.items():
            for letter in range(m):
                if counts[letter] == 2:
                    continue
                new = list(counts)
                new[letter] += 1
                descent = int(last > letter)
                key = (
                    tuple(new),
                    letter,
                    descents + descent,
                    comajor + descent * (n - length),
                )
                following[key] += value
                transitions += 1
                require(len(following) <= MAX_STATES, "dynamic DP state cap")
                require(following[key].bit_length() <= MAX_BITS, "DP integer bit cap")
        current = following
        peak = max(peak, len(current))
    char = Counter()
    for (_, _, descents, comajor), value in current.items():
        char[descents, comajor - m * descents] += value
    require(
        sum(char.values()) == factorial(n) // 2**m, "complete multiset word coverage"
    )
    return char, peak, transitions


def laurent_character(p):
    out = Counter()
    for (degree,), coefficient in sp.Poly(p, T).terms():
        expanded = sp.expand(coefficient.subs(X, U + 1 / U))
        for term in sp.Add.make_args(expanded):
            scalar, exponent = term.as_coeff_exponent(U)
            require(
                scalar.is_Integer and exponent.is_Integer, "Laurent integer character"
            )
            out[degree, int(exponent)] += int(scalar)
    require(all(value >= 0 for value in out.values()), "nonnegative Laurent character")
    return +out


def primitive_sturm(p):
    """Integer pseudo-remainders, sign-corrected, then positive-content division."""
    p = p.clear_denoms(convert=True)[1]
    require(p.degree() >= 1, "positive degree Sturm input")
    sequence = [p.primitive()[1], p.diff().primitive()[1]]
    while sequence[-1].degree() > 0:
        a, b = sequence[-2:]
        exponent = a.degree() - b.degree() + 1
        remainder = -a.prem(b)
        if b.LC() < 0 and exponent % 2:
            remainder = -remainder
        if remainder.is_zero:
            break
        remainder = remainder.primitive()[1]
        bounded_poly(remainder.as_expr(), *p.gens)
        sequence.append(remainder)
    return sequence


def sturm_variations(sequence, at):
    signs = [int(sp.sign(item.eval(at))) for item in sequence]
    signs = [sign for sign in signs if sign]
    return sum(a != b for a, b in pairwise(signs))


def sturm_count(expr, variable, left=-2, right=2):
    p = bounded_poly(expr, variable)
    left, right = sp.Rational(left), sp.Rational(right)
    require(left < right, "ordered Sturm interval")
    require(
        p.eval(left) != 0 and p.eval(right) != 0, "Sturm endpoints must avoid roots"
    )
    sequence = primitive_sturm(p)
    vl, vr = sturm_variations(sequence, left), sturm_variations(sequence, right)
    answer = vl - vr
    require(
        answer == int(p.count_roots(left, right)), "independent Sturm/count agreement"
    )
    return answer, [vl, vr]


def membership(m, x):
    integer(m, 1, MAX_POWER)
    value = rational(x)
    require(-2 <= value <= 2, "unitary x interval")
    _, _, polynomial = native_polynomials(m)
    p = bounded_poly(polynomial.subs(X, value), Z)
    # Used only away from exceptional/torsion walls.
    require(sp.discriminant(p.as_expr(), Z) != 0, "membership requires simple roots")
    count, variations = sturm_count(p.as_expr(), Z)
    return {
        "x": pair(value),
        "roots_in_open_interval": count,
        "sturm_variations": variations,
        "pure": count == m - 1,
    }


def factor_records(expr):
    content, factors = sp.factor_list(expr, X)
    rows = []
    for factor, power in factors:
        p = sp.Poly(factor, X, domain=sp.ZZ)
        require(p.LC() > 0 and p.content() == 1, "primitive positive factor")
        rows.append(
            {
                "coefficients_descending": [int(c) for c in p.all_coeffs()],
                "multiplicity": int(power),
            }
        )
    return {"content": pair(content), "factors": rows}


def chamber_table(m):
    integer(m, 4, 6)
    _, _, polynomial = native_polynomials(m)
    expressions = {
        "discriminant": sp.discriminant(polynomial, Z),
        "minus_endpoint": polynomial.subs(Z, -2),
        "plus_endpoint": polynomial.subs(Z, 2),
    }
    records = {key: factor_records(value) for key, value in expressions.items()}
    unique = {}
    for expr in expressions.values():
        for factor, _ in sp.factor_list(expr, X)[1]:
            p = bounded_poly(factor, X)
            key = tuple(int(c) for c in p.all_coeffs())
            unique[key] = p
    factors = sorted(unique.items(), key=lambda row: (len(row[0]), row[0]))
    walls = []
    factor_rows = []
    for index, (key, p) in enumerate(factors):
        identifier = "f" + str(index)
        intervals = p.intervals(eps=sp.Rational(1, 10**8), inf=-2, sup=2)
        sequence = primitive_sturm(p)
        outer_variations = [
            sturm_variations(sequence, -2),
            sturm_variations(sequence, 2),
        ]
        require(
            len(intervals) == outer_variations[0] - outer_variations[1],
            "complete wall root isolation",
        )
        for rank, ((lo, hi), multiplicity) in enumerate(intervals, 1):
            require(multiplicity == 1, "squarefree wall factor")
            require(hi - lo <= sp.Rational(1, 10**8), "wall bracket width")
            if lo != hi:
                bracket_variations = [
                    sturm_variations(sequence, lo),
                    sturm_variations(sequence, hi),
                ]
                require(
                    bracket_variations[0] - bracket_variations[1] == 1,
                    "one root in wall bracket",
                )
            else:
                require(p.eval(lo) == 0, "rational wall equality")
                bracket_variations = None
            walls.append(
                {
                    "factor": identifier,
                    "root_index_in_minus2_plus2": rank,
                    "bracket": [pair(lo), pair(hi)],
                    "sturm_bracket_variations": bracket_variations,
                }
            )
        factor_rows.append(
            {
                "id": identifier,
                "coefficients_descending": list(key),
                "real_roots_in_minus2_plus2": len(intervals),
                "sturm_outer_variations": outer_variations,
                "sturm_chain_length": len(sequence),
            }
        )
    require(len(walls) <= MAX_WALLS, "wall number cap")
    walls.sort(key=lambda row: sp.Rational(*row["bracket"][0]))
    cells = []
    previous = sp.Rational(-2)
    for index in range(len(walls) + 1):
        lo = (
            sp.Rational(2)
            if index == len(walls)
            else sp.Rational(*walls[index]["bracket"][0])
        )
        require(previous < lo, "disjoint ordered wall brackets")
        sample = (previous + lo) / 2
        count, variations = sturm_count(polynomial.subs(X, sample), Z)
        cells.append(
            {
                "left_wall": index - 1,
                "right_wall": index,
                "sample": pair(sample),
                "roots_in_open_interval": count,
                "sturm_variations": variations,
                "pure": count == m - 1,
            }
        )
        if index < len(walls):
            walls[index]["index"] = index
            previous = sp.Rational(*walls[index]["bracket"][1])
    components = []
    for cell in cells:
        if cell["pure"]:
            if components and components[-1][1] == cell["left_wall"]:
                components[-1][1] = cell["right_wall"]
            else:
                components.append([cell["left_wall"], cell["right_wall"]])
    require(
        len(components) == {4: 3, 5: 4, 6: 6}[m], "observed chamber component census"
    )
    # Check the exceptional-wall set used in the written no-isolated-wall proof.
    exception = X * (X + 1) * (X - 1) * (X**2 + X - 1)
    for name, expr in expressions.items():
        for other_name, other in expressions.items():
            if name < other_name:
                common = sp.Poly(sp.gcd(expr, other), X).sqf_part().as_expr()
                require(sp.rem(exception, common, X) == 0, "unhandled shared wall")
    for name, expr in expressions.items():
        for f, exponent in sp.factor_list(expr, X)[1]:
            if exponent > 1:
                require(sp.rem(exception, f, X) == 0, "unhandled multiple wall")
            if name == "discriminant" and sp.degree(f, X) > 2:
                require(exponent == 1, "ordinary discriminant not simple")
                for endpoint in ("minus_endpoint", "plus_endpoint"):
                    require(
                        sp.gcd(f, expressions[endpoint]) == 1,
                        "unhandled discriminant endpoint intersection",
                    )
    for i, (ki, pi) in enumerate(factors):
        for kj, pj in factors[i + 1 :]:
            require(sp.gcd(pi, pj).degree() == 0, "distinct wall factors coprime")
    return {
        "power": m,
        "M_terms": polynomial_rows(polynomial, X, Z),
        "factorizations": records,
        "wall_factors": factor_rows,
        "walls": walls,
        "cells": cells,
        "pure_closed_components_wall_indices": components,
    }


def torsion_controls():
    rows = []
    for m in (4, 5, 6):
        d, p, reciprocal = native_polynomials(m)
        for x, np, dp in [
            (-1, sp.Integer(1), 1 - T**3),
            (0, sp.Integer(1), (1 - T) * (1 + T**2)),
            (1, 1 + (2**m - 1) * T + T**2, sp.cancel((1 - T**6) / (1 + T))),
        ]:
            require(
                sp.expand(p.subs(X, x) * dp - d.subs(X, x) * np) == 0,
                "torsion rational identity",
            )
            require(sp.gcd(np, dp) == 1, "torsion reduced coprimality")
            rows.append(
                {
                    "power": m,
                    "x": x,
                    "M_coefficients_descending": [
                        int(c) for c in sp.Poly(reciprocal.subs(X, x), Z).all_coeffs()
                    ],
                    "reduced_numerator": polynomial_rows(np, T),
                    "reduced_denominator": polynomial_rows(dp, T),
                }
            )
        # Fifth roots, both conjugate x branches, via exact quotient ring.
        difference = sp.Poly(
            sp.expand(p * (1 - T**5) - d * (1 + (X + 1) ** m * T + T**2)), T
        )
        require(
            all(sp.rem(c, X**2 + X - 1, X) == 0 for c in difference.all_coeffs()),
            "fifth-root quotient identity",
        )
        # +/-2 endpoints are not pure, including multiplicities.
        for x in (-2, 2):
            q = sp.Poly(reciprocal.subs(X, x), Z)
            require(sp.discriminant(q.as_expr(), Z) != 0, "simple endpoint control")
            require(
                q.eval(-2) != 0 and q.eval(2) != 0, "endpoint control boundary root"
            )
            count, _ = sturm_count(q.as_expr(), Z)
            require(count < m - 1, "nonpure slice boundary")
    return rows


def cubic_torus_control():
    reciprocal = Z**2 - Z - sp.Rational(3, 8)
    p = sp.expand(T**2 * reciprocal.subs(Z, T + 1 / T))
    extra = (1 - T) * (1 + sp.Rational(3, 2) * T + T**2)
    universal = sp.expand(p * extra)
    count, variations = sturm_count(reciprocal, Z)
    require(
        count == 2 and sp.discriminant(reciprocal, Z) == sp.Rational(5, 2),
        "cubic two simple interior z roots",
    )
    require(reciprocal.subs(Z, 2) == sp.Rational(13, 8), "separation from T=1")
    require(
        reciprocal.subs(Z, -sp.Rational(3, 2)) == sp.Rational(27, 8),
        "separation from extra quadratic",
    )
    require(
        sp.gcd(universal, sp.diff(universal, T)) == 1, "seven simple universal roots"
    )
    require(
        sp.expand(universal + T**7 * universal.subs(T, 1 / T)) == 0,
        "cubic anti-reciprocity at slice",
    )
    weights = [(a, b, 3 - a - b) for a in range(4) for b in range(4 - a)]
    restricted = {(a - c, b - c) for a, b, c in weights}
    require(len(restricted) == 10, "distinct SU3 torus monomial characters")
    return {
        "reciprocal_polynomial": polynomial_rows(reciprocal, Z),
        "universal_polynomial": polynomial_rows(universal, T),
        "sturm_variations": variations,
        "simple_unit_roots": 7,
        "separation_values": [[13, 8], [27, 8]],
        "distinct_restricted_characters": [list(v) for v in sorted(restricted)],
        "effective_neighborhood_radius_claimed": False,
    }


def build_report():
    sources = source_locks()
    character_rows = []
    for m in (4, 5, 6):
        d, p, _ = native_polynomials(m)
        char, peak, transitions = multiset_character(m)
        require(
            char == laurent_character(p), "full multiset Laurent character equality"
        )
        character_rows.append(
            {
                "power": m,
                "denominator_degree": sp.degree(d, T).__int__(),
                "numerator_degree": sp.degree(p, T).__int__(),
                "word_total": sum(char.values()),
                "peak_DP_states": peak,
                "DP_transitions": transitions,
                "full_character": [[a, b, v] for (a, b), v in sorted(char.items())],
            }
        )
    tables = [chamber_table(m) for m in (4, 5, 6)]
    heldout = []
    for value, prediction in [
        (Fraction(-49, 30), False),
        (Fraction(-3, 2), True),
        (Fraction(-1, 2), True),
        (Fraction(-2, 5), False),
        (Fraction(-1, 4), True),
    ]:
        row = membership(6, value)
        row["preregistered_prediction"] = prediction
        row["prediction_passed"] = row["pure"] == prediction
        heldout.append(row)
    require(
        [row["prediction_passed"] for row in heldout] == [True] * 4 + [False],
        "failed prediction must remain visible",
    )
    nonnesting = []
    for value in (Fraction(-407, 250), Fraction(-1, 4)):
        nonnesting.append(
            {
                "x": pair(rational(value)),
                "power5": membership(5, value),
                "power6": membership(6, value),
            }
        )
    require(
        [row["power5"]["pure"] for row in nonnesting] == [False, True]
        and [row["power6"]["pure"] for row in nonnesting] == [True, False],
        "two-way nonnesting controls",
    )
    report = {
        "schema": "segre-higher-power-controls-v1",
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        },
        "claims": [
            "GLO764.SEGRE_HIGHER_POWER_CHAMBERS_V1",
            "GLO764.SEGRE_OPEN_SU3_CUBIC_CHAMBER_V1",
        ],
        "scope": "exact finite polynomials, full characters, exhaustive Sturm cells; written all-power and open-neighborhood proofs",
        "sources": sources,
        "resources": {
            "max_bytes": MAX_BYTES,
            "max_power": MAX_POWER,
            "max_bits": MAX_BITS,
            "max_states": MAX_STATES,
            "max_terms": MAX_TERMS,
            "max_degree": MAX_DEGREE,
            "max_walls": MAX_WALLS,
            "max_JSON_depth": MAX_JSON_DEPTH,
        },
        "characters": character_rows,
        "chambers": tables,
        "torsion": torsion_controls(),
        "heldout_power6": heldout,
        "nonnesting": nonnesting,
        "open_SU3_control": cubic_torus_control(),
        "preregistered_component_count": 5,
        "observed_power6_component_count": 6,
        "global_or_automorphic_conclusion": False,
        "artifact_sha256_lf": {
            p.relative_to(ROOT).as_posix(): digest(bounded_bytes(p))
            for p in (NOTE, SCRIPT, MANIFEST, TEST)
        },
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report)).hexdigest()
    require(len(render(report).encode()) <= MAX_BYTES, "report byte cap")
    return report


def check_fixture():
    actual = strict_json(bounded_bytes(FIXTURE))
    expected = build_report()
    same_json(actual, expected)
    return {
        "status": "PASS",
        "payload_sha256": expected["payload_sha256"],
        "pure_component_counts": [3, 4, 6],
        "failed_predictions_preserved": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    print(render(check_fixture() if args.check else build_report()), end="")


if __name__ == "__main__":
    main()
