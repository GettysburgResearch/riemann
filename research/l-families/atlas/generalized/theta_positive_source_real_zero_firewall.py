"""Exact rational Taylor/sign controls for a synthetic positive-source firewall.
No floating exponential, theta evaluation, or numerical zero census is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
STEM = "theta_positive_source_real_zero_firewall"
BASE = "b0e3b18e690accdee6d77b3b3c4c68850f6cb671"
DESIGN = "67f88c148bb5914897cc13b6cbce61960a277cd1"
BINDINGS = [
    {
        "commit": "b0e3b18e690accdee6d77b3b3c4c68850f6cb671",
        "path": "research/l-families/atlas/generalized/THETA_SOURCE_QUOTIENT_TENSOR_COHERENCE.md",
        "git_blob": "9873196dcaf7f5ed92c429fe17b146531f2325ac",
        "sha256_lf": "3472b74946925ca4ac6a8f8fe80853d5a96ef0e2e52a5142ff2ba5ac3901c9bd",
    },
    {
        "commit": "b0e3b18e690accdee6d77b3b3c4c68850f6cb671",
        "path": "research/l-families/atlas/generalized/theta_source_quotient_tensor_coherence.py",
        "git_blob": "a184b4a0460d9450a23b3b3c15741a54700f9e8a",
        "sha256_lf": "b04d4f8ca1088d39b1efef9aa8b6e412bd76590d3ba10b70f0a1be620faa5ed1",
    },
    {
        "commit": "b0e3b18e690accdee6d77b3b3c4c68850f6cb671",
        "path": "research/l-families/atlas/generalized/theta_source_quotient_tensor_coherence.json",
        "git_blob": "e51c72d319e61929e4b82c007c3568d82a328285",
        "sha256_lf": "6413c704116108ab3f1a06400087b8154297ffe13f3631436a96b49502ee3419",
    },
    {
        "commit": "b0e3b18e690accdee6d77b3b3c4c68850f6cb671",
        "path": "research/l-families/atlas/generalized/theta_source_quotient_tensor_coherence.sources.json",
        "git_blob": "4b94a34636da981d05c48fab8690eb93745d346b",
        "sha256_lf": "12ebd09865d1b184d08fd519a8801970457854d42f93789ecd69e2ddbb0d0f7a",
    },
    {
        "commit": "b0e3b18e690accdee6d77b3b3c4c68850f6cb671",
        "path": "tests/test_theta_source_quotient_tensor_coherence.py",
        "git_blob": "2d59d62afcbdb2b35926cc9cf2ce420e7ba403ae",
        "sha256_lf": "a29dcc3059a3a1a7c9c9cd41ee7d62ee5033bf8b1628e2f59d07a278b60a8f32",
    },
    {
        "commit": "67f88c148bb5914897cc13b6cbce61960a277cd1",
        "path": "research/l-families/atlas/generalized/THETA_POSITIVE_SOURCE_REAL_ZERO_FIREWALL.md",
        "git_blob": "f96926a2b075ef76adaa53d8235881a9874d1d3a",
        "sha256_lf": "4937a44b9ce0cb2cd484c22471bc86af6453b4ebbc23ddf38ca303ace3f74abf",
    },
]
ARTIFACTS = [
    DIR + STEM.upper() + ".md",
    DIR + STEM + ".py",
    DIR + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
]
CAPS = {
    "integer_bits": 4096,
    "taylor_order": 32,
    "polynomial_length": 8,
    "work_units": 100000,
    "json_bytes": 1000000,
    "json_nodes": 50000,
    "json_depth": 24,
    "container_length": 2000,
    "string_length": 4096,
}
WORK = 0


def need(ok, message):
    if not ok:
        raise ValueError(message)


def integer(n, lo, hi):
    need(type(n) is int and lo <= n <= hi, "integer type/range")
    return n


def rational(v):
    need(type(v) in (int, Q), "exact rational type")
    q = Q(v)
    need(
        max(q.numerator.bit_length(), q.denominator.bit_length())
        <= CAPS["integer_bits"],
        "rational bit cap",
    )
    return q


def charge():
    global WORK
    WORK += 1
    need(WORK <= CAPS["work_units"], "work cap")


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("ascii")


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def typed(value):
    visits = 0

    def walk(v, depth):
        nonlocal visits
        visits += 1
        need(
            visits <= CAPS["json_nodes"] and depth <= CAPS["json_depth"],
            "JSON depth/node cap",
        )
        if type(v) is dict:
            need(len(v) <= CAPS["container_length"], "JSON object length")
            need(
                all(type(k) is str and len(k) <= CAPS["string_length"] for k in v),
                "JSON key cap/type",
            )
            for item in v.values():
                walk(item, depth + 1)
        elif type(v) is list:
            need(len(v) <= CAPS["container_length"], "JSON list length")
            for item in v:
                walk(item, depth + 1)
        elif type(v) is str:
            need(
                len(v) <= CAPS["string_length"] and v.isascii(), "JSON string cap/ASCII"
            )
        elif type(v) is int:
            need(v.bit_length() <= CAPS["integer_bits"], "JSON integer bit cap")
        else:
            need(type(v) is bool, "JSON primitive type")

    walk(value, 0)


def decode(raw):
    need(type(raw) is bytes and len(raw) <= CAPS["json_bytes"], "JSON byte cap/type")

    def pairs(items):
        out = {}
        for k, v in items:
            need(k not in out, "duplicate JSON key")
            out[k] = v
        return out

    def reject(_):
        raise ValueError("noninteger JSON numeric primitive")

    value = json.loads(
        raw, object_pairs_hook=pairs, parse_float=reject, parse_constant=reject
    )
    typed(value)
    return value


def file_bytes(path):
    need(path.stat().st_size <= CAPS["json_bytes"], "artifact byte cap")
    return path.read_bytes()


def interval(v):
    need(type(v) in (tuple, list) and len(v) == 2, "interval shape")
    lo, hi = map(rational, v)
    need(lo <= hi, "interval orientation")
    return lo, hi


def plus(a, b):
    a, b = interval(a), interval(b)
    charge()
    return interval((a[0] + b[0], a[1] + b[1]))


def scale(a, c):
    a, c = interval(a), rational(c)
    charge()
    return interval((a[0] * c, a[1] * c) if c >= 0 else (a[1] * c, a[0] * c))


def exp_bounds(x, n=16):
    x = rational(x)
    need(0 <= x <= 1, "Taylor x range")
    integer(n, 1, CAPS["taylor_order"])
    term = Q(1)
    total = term
    for j in range(1, n + 1):
        charge()
        term = rational(term * x / j)
        total = rational(total + term)
    first = rational(term * x / (n + 1))
    ratio = rational(x / (n + 2))
    upper = rational(total + first / (1 - ratio))
    return interval((total, upper))


def encoded(v):
    return [str(x) for x in interval(v)]


def sign(v):
    lo, hi = interval(v)
    need(lo > 0 or hi < 0, "sign unresolved")
    return 1 if lo > 0 else -1


def z_bounds(a, s):
    a, s = rational(a), rational(s)
    need(0 < a <= 4 and 0 <= s <= 1, "declared amplitude/point cap")
    if s in (0, 1):
        return Q(1, 2), Q(1, 2)
    inside = plus(
        (1, 1), plus(scale(exp_bounds(s), s - 1), scale(exp_bounds(1 - s), -s))
    )
    return plus((Q(1, 2), Q(1, 2)), scale(inside, a))


def polynomial(p):
    need(
        type(p) in (list, tuple) and 1 <= len(p) <= CAPS["polynomial_length"],
        "polynomial shape/cap",
    )
    return [rational(v) for v in p]


def polyadd(a, b):
    a, b = polynomial(a), polynomial(b)
    out = [Q(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] = rational(out[j] + x)
    for j, x in enumerate(b):
        out[j] = rational(out[j] + x)
    return out


def polyscale(a, c):
    return [rational(x * rational(c)) for x in polynomial(a)]


def polymul(a, b):
    a, b = polynomial(a), polynomial(b)
    need(len(a) + len(b) - 1 <= CAPS["polynomial_length"], "product polynomial cap")
    out = [Q(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            charge()
            out[j + k] = rational(out[j + k] + x * y)
    return out


def reflect(p):
    p = polynomial(p)
    out = [Q(0)]
    power = [Q(1)]
    for index, x in enumerate(p):
        out = polyadd(out, polyscale(power, x))
        if index + 1 < len(p):
            power = polymul(power, [1, -1])
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def formal_controls():
    j0 = [Q(-2), Q(2)]
    # antiderivative: exp(x/2)*(2*x^2-8*x+16).
    antiderivative = [Q(16), Q(-8), Q(2)]
    derivative = [antiderivative[1], 2 * antiderivative[2], Q(0)]
    integrand = polyadd(derivative, polyscale(antiderivative, Q(1, 2)))
    need(integrand == [0, 0, 1], "J second-moment antiderivative")
    j2 = [Q(-16), sum(antiderivative)]
    c = polyadd(polyscale(j0, 2), polyscale(j2, Q(-1, 4)))
    need(c == [0, Q(3, 2)], "b1 curvature")
    numerator = polymul(j0, j0)
    denominator = polyscale(c, 2)
    need(numerator == [4, -8, 4] and denominator == [0, 3], "pitchfork coefficient")
    original = {
        "constant": [Q(1)],
        "exp_s": [Q(-1), Q(1)],
        "exp_one_minus_s": [Q(0), Q(-1)],
    }
    reflected = {
        "constant": reflect(original["constant"]),
        "exp_s": reflect(original["exp_one_minus_s"]),
        "exp_one_minus_s": reflect(original["exp_s"]),
    }
    need(original == reflected, "exact exponential-polynomial reflection")
    for s in (0, 1):
        coeff = lambda p, point=s: sum(x * point**j for j, x in enumerate(p))
        e0 = coeff(original["constant"]) + coeff(
            original["exp_s"] if s == 0 else original["exp_one_minus_s"]
        )
        e1 = coeff(original["exp_one_minus_s"] if s == 0 else original["exp_s"])
        need(e0 == 0 and e1 == 0, "amplitude-free endpoint value")
    enc = lambda p: [str(x) for x in p]
    return {
        "J0_E": enc(j0),
        "J2_E": enc(j2),
        "curvature_E": enc(c),
        "pitchfork_numerator_E": enc(numerator),
        "pitchfork_denominator_E": enc(denominator),
        "J2_antiderivative_x": enc(antiderivative),
        "reflection_original": {k: enc(v) for k, v in original.items()},
        "reflection_transformed": {k: enc(v) for k, v in reflected.items()},
        "endpoint_Z": ["1/2", "1/2"],
    }


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "design": DESIGN,
        "frozen_sources": BINDINGS,
        "remote_bytes_authenticated": False,
        "references": [
            {
                "url": "https://dlmf.nist.gov/1.10",
                "passage": "sectioniv argument principle and Rouche theorem; local persistence only",
            }
        ],
        "contract": {
            "arithmetic_class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
            "caps": CAPS,
            "analytic_proof_machine_certified": False,
            "actual_modular_source": False,
            "RH_counterexample": False,
            "all_complex_zero_count": False,
            "fixed_b": "1",
            "Taylor_order": 16,
            "candidate_A2_bracket_expected_failure_not_blinded": True,
            "smooth_persistence_is_written_existence_proof": True,
        },
    }


def authenticate():
    need(
        canonical(decode(file_bytes(ROOT / (DIR + STEM + ".sources.json"))))
        == canonical(manifest()),
        "fixed source manifest",
    )
    for row in BINDINGS:
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
        )
        need(len(raw) <= CAPS["json_bytes"], "source byte cap")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and digest(lf(raw)) == row["sha256_lf"],
            "frozen source authentication",
        )


def payload():
    global WORK
    WORK = 0
    xs = (Q(1, 8), Q(3, 8), Q(1, 2), Q(5, 8), Q(7, 8), Q(1))
    exponentials = [
        {
            "x": str(x),
            "N": 16,
            "enclosure": encoded(exp_bounds(x)),
            "both_inequalities_strict": True,
        }
        for x in xs
    ]
    e = exp_bounds(Q(1, 2))
    ac = interval((1 / (2 * (e[1] - 1)), 1 / (2 * (e[0] - 1))))
    need(Q(3, 4) < ac[0] <= ac[1] < Q(4, 5), "threshold rational bracket")
    values = [
        {
            "A": str(a),
            "s": str(s),
            "enclosure": encoded(z_bounds(a, s)),
            "sign": sign(z_bounds(a, s)),
        }
        for a in (Q(1, 2), Q(1), Q(2))
        for s in (Q(1, 8), Q(3, 8), Q(1, 2))
    ]
    brackets = []
    for a in (Q(1), Q(2)):
        signs = [sign(z_bounds(a, s)) for s in (Q(1, 8), Q(3, 8))]
        brackets.append(
            {
                "A": str(a),
                "candidate": ["1/8", "3/8"],
                "endpoint_signs": signs,
                "opposite_signs": signs[0] != signs[1],
                "preregistered_expected_success": a == 1,
            }
        )
    need(
        [r["opposite_signs"] for r in brackets] == [True, False],
        "candidate failure retained, not moved",
    )
    margins = []
    for b2 in (Q(1), Q(4), Q(8)):
        for zz in (Q(1, 8), Q(1, 4), Q(3, 8)):
            value = 2 - b2 / 4 + b2 * zz * zz
            need(value >= b2 * zz * zz > 0, "strict monotonicity margin")
            margins.append(
                {
                    "b_squared": str(b2),
                    "z": str(zz),
                    "margin": str(value),
                    "lower_bound": str(b2 * zz * zz),
                }
            )
    out = {
        "schema": STEM + "-v1",
        "contract": manifest()["contract"],
        "sources": BINDINGS,
        "exponential_enclosures": exponentials,
        "A_c_enclosure": encoded(ac),
        "A_c_rational_outer_bracket": ["3/4", "4/5"],
        "Z_sign_panel": values,
        "candidate_brackets": brackets,
        "monotonicity_margins": margins,
        "formal": formal_controls(),
        "coverage": {
            "exponentials": 6,
            "signs": 9,
            "amplitudes": ["1/2", "1", "2"],
            "points": ["1/8", "3/8", "1/2"],
            "monotonicity": 9,
            "candidate_brackets": 2,
            "candidate_successes": 1,
            "candidate_failures": 1,
            "formal_b": 1,
        },
        "not_claimed": [
            "actual modular theta source",
            "RH or GRH counterexample",
            "all complex zero census",
            "smooth-source finite evaluation",
            "analytic theorem machine certification",
        ],
        "work_units": WORK,
    }
    typed(out)
    return out


def fixture():
    authenticate()
    out = payload()
    out["artifact_sha256_lf"] = {p: digest(lf(file_bytes(ROOT / p))) for p in ARTIFACTS}
    out["payload_sha256"] = digest(canonical(out))
    need(len(canonical(out)) <= CAPS["json_bytes"], "fixture byte cap")
    return out


def check(value):
    typed(value)
    need(type(value) is dict, "fixture object")
    need(
        canonical(value) == canonical(fixture()),
        "complete source-authenticated primitive replay",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--emit", action="store_true")
    group.add_argument("--emit-sources", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        print(json.dumps(manifest(), sort_keys=True, indent=2))
    elif args.emit:
        print(json.dumps(fixture(), sort_keys=True, indent=2))
    else:
        raw = file_bytes(ROOT / (DIR + STEM + ".json"))
        check(decode(raw))
        print(
            "PASS six Taylor enclosures,nine signs,nine margins,two retained brackets"
        )
        print("fixture_sha256_lf=" + digest(lf(raw)))


if __name__ == "__main__":
    main()
