"""Exact finite controls for the auxiliary Xi-current radial heat limit.

The producer does not evaluate Xi or certify an analytic limit. It authenticates
its exact source theorem and reconstructs the declared rational controls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from itertools import pairwise
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_current_radial_semigroup"
BASE = "af809698fe6cb5046a5bcc00e9175296e4597060"
PREREG = "980801ae4c23d9482975f363390249a1b3a14ac2"
NOTE = HERE / "XI_CURRENT_RADIAL_SEMIGROUP.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BINDINGS = [
    {
        "commit": "af809698fe6cb5046a5bcc00e9175296e4597060",
        "git_blob": "682e5b89ae99dee92741a290b5d7357bf8feef73",
        "path": "research/exploratory/XI_ODD_CURRENT_DOUBLE_SCALING.md",
        "sha256_lf": "3c7c16677311d40d8219a88ffb236984ea8704a8ef4e1a30f8b9da1637342e41",
    },
    {
        "commit": "af809698fe6cb5046a5bcc00e9175296e4597060",
        "git_blob": "1fe1f33b9c6e5812f0d1f60f88622659e95e7521",
        "path": "research/exploratory/xi_odd_current_scaling.py",
        "sha256_lf": "3ec353766ba53206af647adc84eec139503d7404a5113057fd00de985b62bd95",
    },
    {
        "commit": "af809698fe6cb5046a5bcc00e9175296e4597060",
        "git_blob": "40b457271e96cb9d08b8eae0ec975529bd489331",
        "path": "research/exploratory/xi_odd_current_scaling.json",
        "sha256_lf": "359f64f45165db33318f714689912efa68e4e0935139ab9a6195a7b858ad7749",
    },
    {
        "commit": "af809698fe6cb5046a5bcc00e9175296e4597060",
        "git_blob": "ab9d950ea9b28b121a640ea5b15ee9907968bd39",
        "path": "research/exploratory/xi_odd_current_scaling.sources.json",
        "sha256_lf": "40faa58ea354d2f7f86ee9859d1112227ed5b12e716546c28b6d20320142bdda",
    },
    {
        "commit": "af809698fe6cb5046a5bcc00e9175296e4597060",
        "git_blob": "55f713ec9182fd607aa75751fd7b22ae5bd02e9e",
        "path": "tests/test_xi_odd_current_scaling.py",
        "sha256_lf": "98ae7beab3a0d970b5760076783dcbf30e71d025503f1db96451e62219cb96e9",
    },
    {
        "commit": "3f00e46e79cf928f724a9170116cb69e14f7b02f",
        "git_blob": "551c55d32e8013f7b963287be6371a5d1893e0fb",
        "path": "research/exploratory/XI_ODD_CURRENT_SCALING_AUDIT_AF809698.md",
        "sha256_lf": "dd86a7c0449b9cd26300767a7b13c348c63e2a8e3842c29390f300c6a6dc2d87",
    },
    {
        "commit": "980801ae4c23d9482975f363390249a1b3a14ac2",
        "git_blob": "dba123e0af5296571e800f8235789bbab97ca9c8",
        "path": "research/exploratory/XI_CURRENT_RADIAL_SEMIGROUP.md",
        "sha256_lf": "0b61d44e82756f0c3d3a7d2c8fe7335d97e9358eaf5901b1b1fa62805fb1dc80",
    },
]
TIMES = (Q(1, 3), Q(1), Q(2))
LAPLACE = (Q(0), Q(1, 7), Q(1), Q(3))
MAX_MOMENT, MAX_ORDER = 12, 63
CONTRACT = {
    "arithmetic_class": "MIXED",
    "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
    "rounding": "none; integers and canonical rational strings only",
    "source": "literal source-pinned Xi odd-current compact-kappa theorem",
    "finite_work": "Gaussian multinomial moments, radial generator, full finite composition and MLR polynomial panels",
    "analytic_boundary": "all-order and limit quantifiers are written proofs, not certified by finite rows",
    "auxiliary": "order-to-radius Markov kernel with declared odd-order quantization, not a native physical time",
    "semigroup": "fixed finite compositions converge; finite-xi family fails exact semigroup identity",
    "universality": "same limit for substituted Gaussian kernels; not a source-faithfulness criterion",
    "exclusions": "no growing-step diffusion limit, iterated unbounded-moment convergence, Xi zeros, capture, decoder, or RH",
}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()


def lfhash(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def exact(value):
    need(type(value) in (int, Q), "exact rational input; bool/float rejected")
    q = Q(value)
    need(
        max(q.numerator.bit_length(), q.denominator.bit_length()) <= 256,
        "input bit cap",
    )
    return q


def index(value, upper):
    need(type(value) is int and 0 <= value <= upper, "bounded integer index")
    return value


def load_json(raw):
    need(type(raw) is bytes and len(raw) <= 2_000_000, "input byte cap")

    def unique(pairs):
        result = {}
        for key, value in pairs:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def forbidden(_):
        raise ValueError("floating or nonfinite JSON number")

    value = json.loads(
        raw, object_pairs_hook=unique, parse_float=forbidden, parse_constant=forbidden
    )
    validate_tree(value)
    return value


def validate_tree(value):
    count = 0

    def walk(obj, depth):
        nonlocal count
        count += 1
        need(count <= 100_000 and depth <= 16, "JSON node/depth cap")
        if type(obj) is dict:
            need(all(type(k) is str for k in obj), "string keys")
            for item in obj.values():
                walk(item, depth + 1)
        elif type(obj) is list:
            for item in obj:
                walk(item, depth + 1)
        elif type(obj) is int:
            need(obj.bit_length() <= 1024, "JSON integer cap")
        elif type(obj) is str:
            need(
                len(obj) <= 2000 and all(ord(c) >= 32 or c in "\t\n\r" for c in obj),
                "text cap/control",
            )
        else:
            need(type(obj) in (bool, type(None)), "JSON primitive type")

    walk(value, 0)


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration": PREREG,
        "sources": BINDINGS,
        "contract": CONTRACT,
        "classical_reference": {
            "title": "Pitman--Yor, A guide to Brownian motion and related stochastic processes",
            "url": "https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf",
            "location": "section4.4.2, pp17--18",
            "role": "classical radial Brownian identification; Gaussian proof supplied in note",
        },
    }


def authenticate():
    need(
        canonical(load_json(MANIFEST.read_bytes())) == canonical(manifest()),
        "source manifest",
    )
    for row in BINDINGS:
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
        )
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and lfhash(raw) == row["sha256_lf"],
            "frozen source identity",
        )
        if row["commit"] == BASE:
            need(
                lfhash((ROOT / row["path"]).read_bytes()) == row["sha256_lf"],
                "local parent drift",
            )
    parent = load_json((HERE / "xi_odd_current_scaling.sources.json").read_bytes())
    need(len(parent["sources"]) == 4, "complete transitive source panel")
    for row in parent["sources"]:
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
        )
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and lfhash(raw) == row["sha256_lf"],
            "transitive frozen source identity",
        )
    return len(BINDINGS) + len(parent["sources"])


def gaussian_even(n):
    n = index(n, MAX_MOMENT)
    return Q(math.factorial(2 * n), 4**n * math.factorial(n))


def radial_multinomial(m):
    """Coefficient of x^d t^(m-d), x=r^2; three independent Gaussian coordinates."""
    m = index(m, MAX_MOMENT)
    result = [Q(0)] * (m + 1)
    for i in range(m + 1):
        for j in range(m - i + 1):
            k = m - i - j
            multi = Q(
                math.factorial(m),
                math.factorial(i) * math.factorial(j) * math.factorial(k),
            )
            for ell in range(i + 1):
                result[i - ell] += (
                    multi
                    * math.comb(2 * i, 2 * ell)
                    * gaussian_even(ell)
                    * gaussian_even(j)
                    * gaussian_even(k)
                )
    return tuple(result)


def radial_generator(m):
    m = index(m, MAX_MOMENT)
    result = [Q(0)] * (m + 1)
    factor = Q(1)
    for j in range(m + 1):
        if j:
            degree = m - j + 1
            factor *= Q(degree) * (degree + Q(1, 2)) / j
        result[m - j] = factor
    return tuple(result)


def compose_moment(m, s, t):
    m, s, t = index(m, MAX_MOMENT), exact(s), exact(t)
    need(s > 0 and t > 0, "positive times")
    result = [Q(0)] * (m + 1)
    outer = radial_multinomial(m)
    for d, coeff in enumerate(outer):
        for e, inner in enumerate(radial_multinomial(d)):
            result[e] += coeff * t ** (m - d) * inner * s ** (d - e)
    expected = tuple(c * (s + t) ** (m - e) for e, c in enumerate(radial_generator(m)))
    need(tuple(result) == expected, "independent moment composition")
    return tuple(result)


def current(k):
    need(type(k) is int and 1 <= k <= MAX_ORDER and k % 2 == 1, "bounded odd order")
    return tuple(Q(math.comb(k, 2 * j + 1), k) for j in range((k + 1) // 2))


def mul(a, b):
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def derivative(a):
    return [j * a[j] for j in range(1, len(a))] or [Q(0)]


def mlr_control(k):
    need(type(k) is int and 1 <= k <= MAX_ORDER - 2 and k % 2 == 1, "adjacent pair cap")
    a, b = current(k), current(k + 2)
    first, second = mul(derivative(b), a), mul(b, derivative(a))
    degree = max(len(first), len(second))
    first += [Q(0)] * (degree - len(first))
    second += [Q(0)] * (degree - len(second))
    determinant = [x - y for x, y in zip(first, second)]
    while len(determinant) > 1 and determinant[-1] == 0:
        determinant.pop()
    ratios = [b[j] / a[j] for j in range(len(a))]
    expected = [Q(k * (k + 1), (k + 1 - 2 * j) * (k - 2 * j)) for j in range(len(a))]
    need(ratios == expected, "binomial likelihood ratios")
    need(all(x < y for x, y in pairwise(ratios)), "strict ratio order")
    need(
        len(determinant) == k and all(v > 0 for v in determinant),
        "strict positive MLR polynomial",
    )
    return {
        "K": k,
        "next_K": k + 2,
        "coefficient_ratios": list(map(str, ratios)),
        "derivative_numerator": list(map(str, determinant)),
    }


def laplace_control(a, s, t):
    a, s, t = map(exact, (a, s, t))
    need(a >= 0 and s > 0 and t > 0, "Laplace domain")
    first = 1 + a * t
    rate = a / first
    second = 1 + rate * s
    total = 1 + a * (s + t)
    need(
        first * second == total and rate / second == a / total,
        "Laplace composition algebra",
    )
    return {
        "a": str(a),
        "s": str(s),
        "t": str(t),
        "first_base": str(first),
        "second_base": str(second),
        "combined_base": str(total),
        "combined_rate": str(a / total),
    }


def seal(value):
    need(type(value) is dict and "payload_sha256" not in value, "unsigned report")
    return {**value, "payload_sha256": hashlib.sha256(canonical(value)).hexdigest()}


def build_report():
    authenticate()
    moments, compositions, mlr, laplace = [], [], [], []
    for m in range(MAX_MOMENT + 1):
        value = radial_multinomial(m)
        need(value == radial_generator(m), "independent Gaussian/generator moment")
        moments.append(
            {"moment_index": m, "x_d_t_m_minus_d_coefficients": list(map(str, value))}
        )
        for s in TIMES:
            for t in TIMES:
                compositions.append(
                    {
                        "moment_index": m,
                        "s": str(s),
                        "t": str(t),
                        "x_coefficients": list(map(str, compose_moment(m, s, t))),
                    }
                )
    for k in range(1, MAX_ORDER - 1, 2):
        mlr.append(mlr_control(k))
    for a in LAPLACE:
        for s in TIMES:
            for t in TIMES:
                laplace.append(laplace_control(a, s, t))
    need(
        (len(moments), len(compositions), len(mlr), len(laplace)) == (13, 117, 31, 36),
        "complete declared coverage",
    )
    return seal(
        {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "sources": BINDINGS,
            "coverage": {
                "moments": 13,
                "moment_compositions": 117,
                "adjacent_odd_orders": 31,
                "laplace_compositions": 36,
            },
            "moments": moments,
            "moment_compositions": compositions,
            "mlr_controls": mlr,
            "laplace_controls": laplace,
            "artifacts": {
                p.relative_to(ROOT).as_posix(): lfhash(p.read_bytes())
                for p in (NOTE, Path(__file__), TEST, MANIFEST)
            },
        }
    )


def check_report(value):
    validate_tree(value)
    need(type(value) is dict and "payload_sha256" in value, "report shape")
    raw = {k: v for k, v in value.items() if k != "payload_sha256"}
    need(
        value["payload_sha256"] == hashlib.sha256(canonical(raw)).hexdigest(),
        "payload seal",
    )
    need(
        canonical(value) == canonical(build_report()),
        "fresh full rational/source reconstruction",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--emit-sources", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        result = manifest()
    elif args.check:
        check_report(load_json(FIXTURE.read_bytes()))
        print(
            "PASS exact radial-current controls; auxiliary fixed-composition limit only; physical/RH OPEN"
        )
        return
    else:
        result = build_report()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
