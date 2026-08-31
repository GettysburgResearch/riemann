"""Bounded exact/directed controls; analytic theorems are in the companion note."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import acb, acb_series, arb, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_source_polarization_four_node"
NOTE = HERE / "XI_SOURCE_POLARIZATION_FOUR_NODE.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "8f01064df805624c045877655893c324a220975d"
PREREG = "a15673eb301cc49ae055dcb9a0253e6ff750f0f8"
BITS = 512
MAX_BYTES = 2_000_000
PANELS = (
    (Q(3, 4), Q(1), Q(3, 2), Q(2)),
    (Q(1), Q(2), Q(4), Q(8)),
    (Q(1), Q(65, 64), Q(33, 32), Q(67, 64)),
    (Q(2), Q(3), Q(5), Q(7)),
    (Q(8), Q(16), Q(32), Q(64)),
    (Q(16), Q(32), Q(64), Q(128)),
)
SOURCES = (
    (PREREG, "research/exploratory/XI_SOURCE_POLARIZATION_FOUR_NODE.md"),
    (BASE, "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md"),
    (BASE, "research/exploratory/XI_POSITIVE_KERNEL_DESCENT_FIREWALL.md"),
    (BASE, "research/integrated/xi_pick/ORDER_THREE_CANONICAL.md"),
    (BASE, "research/integrated/xi_pick/SOURCE_MANIFEST.tsv"),
    (
        "c079c2ef21022be951027de1316aecf1168422c1",
        "claims/lemmas/L-92000-three-node-caratheodory-determinant-factors-into-two-scalar-curvatures.md",
    ),
    (
        "bb7327d21c47410820cda2671f45dbe709a72eea",
        "claims/lemmas/L-91904-the-infinitesimal-safe-pick-kernel-is-a-countable-rh-criterion.md",
    ),
    (
        "db9a767e312d9928f5ef827762dcb4ef95494af0",
        "claims/theorems/T-92201-the-safe-xi-impedance-is-matrix-monotone-of-order-two.md",
    ),
    (
        "db9a767e312d9928f5ef827762dcb4ef95494af0",
        "claims/lemmas/L-92202-verified-critical-reserve-closes-the-schwarzian-xi-impedance-curvature.md",
    ),
    (
        "9497db89e34669e2167c632c918c491bf6ee73ab",
        "research/exploratory/prs-765-766-770-781-proof-review/GENERALIZED_SCHUR_ZERO_INDEX.md",
    ),
    (
        "552fe0b78fd96b02fe5836269e6795a992c935be",
        "standalone/2026-08-31-segre-chow-equivariant-synthesis/README.md",
    ),
)
CONTRACT = {
    "schema": "xi-source-polarization-four-node-v1",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "normalization": "X(z)=xi_R(1/2+iz); Phi=2phi0; Y(x)=xi_R(1/2+x)=X(ix)",
    "primitive": "completed Xi through a fresh first acb_series jet of literal zeta and Gamma at s=x+1/2",
    "native_domain": "exact rational 1/2<x<=128; six frozen quadruples; 512 bits; no escalation",
    "rounding": "FLINT outward complex balls, projected real only after imaginary zero enclosure; outward exact rational endpoints",
    "runtime": "python-flint 0.9.0; FLINT 3.6.0; CPython 3.12",
    "finite_scope": "six actual-Xi quadruples; no finite-to-global positivity inference",
    "theorems": "source polarization; full-core closability iff RH; four-node algebra and source residual; local Volterra coefficient no-go",
    "older_order_three": "repaired PSD only, not strict anchor invertibility; one shared reserve; grouped C2 and multiplicities",
    "old_schwarzian": "separately identified historical input, not independently re-certified by this producer",
    "no_claim": "RH, all-order positivity, unconditional closability, prime-positive factorization, external novelty",
    "caps": {
        "matrix": 4,
        "bits": BITS,
        "jet": 2,
        "panels": 6,
        "bytes": MAX_BYTES,
        "integer_bits": 4096,
        "nodes": 100000,
        "depth": 24,
    },
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def validate_tree(value, depth=0, visits=None):
    visits = [0] if visits is None else visits
    visits[0] += 1
    require(depth <= 24 and visits[0] <= 100000, "tree cap")
    if value is None or type(value) is bool:
        return
    if type(value) is int:
        require(value.bit_length() <= 4096, "integer cap")
        return
    if type(value) is str:
        require(value.isascii() and len(value) <= 4096, "string cap")
        return
    require(type(value) in (dict, list) and len(value) <= 4096, "container/type cap")
    if type(value) is dict:
        require(
            all(type(k) is str and k.isascii() and len(k) <= 4096 for k in value),
            "key cap",
        )
    for item in value.values() if type(value) is dict else value:
        validate_tree(item, depth + 1, visits)


def load(path):
    data = path.read_bytes()
    require(len(data) <= MAX_BYTES, "file cap")

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    value = json.loads(
        data,
        object_pairs_hook=pairs,
        parse_constant=lambda _: require(False, "nonfinite JSON"),
    )
    validate_tree(value)
    return value


def pack(q):
    q = Q(q)
    return [q.numerator, q.denominator]


def unpack(pair):
    require(type(pair) is list and len(pair) == 2, "rational pair")
    require(
        all(type(v) is int and v.bit_length() <= 4096 for v in pair),
        "rational integer type/cap",
    )
    require(pair[1] > 0 and math.gcd(*pair) == 1, "canonical rational")
    return Q(*pair)


def qarb(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator


def interval(a):
    require(a.is_finite(), "nonfinite native enclosure")
    return [pack(Q(str(a.lower().fmpq()))), pack(Q(str(a.upper().fmpq())))]


def matrix_ok(a):
    n = len(a)
    require(1 <= n <= 4 and all(len(row) == n for row in a), "matrix dimension cap")
    return n


def determinant(a):
    n = matrix_ok(a)
    result = 0
    for perm in itertools.permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = sign
        for i in range(n):
            term *= a[i][perm[i]]
        result += term
    return result


def elimination(a):
    n = matrix_ok(a)
    require(all(type(v) is Q for row in a for v in row), "exact elimination type")
    a = [row[:] for row in a]
    result = Q(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            result = -result
        q = a[k][k]
        result *= q
        for i in range(k + 1, n):
            multiplier = a[i][k] / q
            for j in range(k + 1, n):
                a[i][j] -= multiplier * a[k][j]
    return result


def minor(a, rows, cols=None):
    cols = rows if cols is None else cols
    return [[a[i][j] for j in cols] for i in rows]


def adjugate3(a):
    require(matrix_ok(a) == 3, "adjugate dimension")
    return [
        [
            (-1) ** (i + j)
            * determinant(
                minor(
                    a, [k for k in range(3) if k != j], [k for k in range(3) if k != i]
                )
            )
            for j in range(3)
        ]
        for i in range(3)
    ]


def divided(t, f):
    require(len(t) == len(f) and 1 <= len(t) <= 4, "divided difference cap")
    require(all(t[i] < t[i + 1] for i in range(len(t) - 1)), "strict nodes")
    return sum(
        f[i] / scalar(math.prod(t[i] - t[j] for j in range(len(t)) if j != i), f[i])
        for i in range(len(t))
    )


def scalar(q, sample):
    return qarb(q) if isinstance(sample, arb) else Q(q)


def residual(t, f):
    return divided(t[:3], f[:3]) * divided(t[1:], f[1:]) - divided(
        t[1:3], f[1:3]
    ) * divided(t, f)


def algebra(x, p):
    require(len(x) == len(p) == 4, "four-node coverage")
    require(
        all(type(v) is Q for v in p) or all(type(v) is arb for v in p),
        "homogeneous exact or directed values",
    )
    require(
        all(type(v) is Q for v in x) and all(Q(1, 2) < v <= 128 for v in x),
        "safe node type/domain",
    )
    require(all(x[i] < x[i + 1] for i in range(3)), "distinct ordered nodes")
    t = [v * v for v in x]
    tx = [scalar(v, p[0]) for v in t]
    xx = [scalar(v, p[0]) for v in x]
    tp = [tx[i] * p[i] for i in range(4)]
    h = [
        [(xx[i] * p[i] + xx[j] * p[j]) / (xx[i] + xx[j]) for j in range(4)]
        for i in range(4)
    ]
    af = determinant([[1, tx[i], p[i], tp[i]] for i in range(4)])
    bf = determinant([[1, tx[i], tp[i], tx[i] * tp[i]] for i in range(4)])
    vandermonde = math.prod(t[j] - t[i] for i in range(4) for j in range(i + 1, 4))
    plus = math.prod((x[i] + x[j]) ** 2 for i in range(4) for j in range(i + 1, 4))
    m = minor(h, list(range(3)))
    delta = determinant(m)
    adj = adjugate3(m)
    v = [h[i][3] for i in range(3)]
    alpha = [sum(adj[i][j] * v[j] for j in range(3)) for i in range(3)]
    bordered = delta * h[3][3] - sum(v[i] * alpha[i] for i in range(3))
    c = [-a for a in alpha] + [delta]
    source_charge = sum(c[i] * h[i][j] * c[j] for i in range(4) for j in range(4))
    return {
        "h": h,
        "A": af,
        "B": bf,
        "Dp": residual(t, p),
        "Dtp": residual(t, tp),
        "vandermonde": vandermonde,
        "plus": plus,
        "det": determinant(h),
        "delta": delta,
        "bordered": bordered,
        "source_charge": source_charge,
        "alpha": alpha,
    }


def exact_control(x, p):
    a = algebra(x, p)
    require(a["det"] == elimination(a["h"]), "independent determinant route")
    require(a["det"] * a["plus"] == a["A"] * a["B"], "four-node factorization")
    require(
        a["A"] == a["vandermonde"] * a["Dp"] and a["B"] == a["vandermonde"] * a["Dtp"],
        "divided-difference route",
    )
    require(a["bordered"] == a["det"], "bordered determinant")
    require(a["source_charge"] == a["delta"] * a["det"], "fraction-free charge")
    return {
        k: pack(a[k]) for k in ("A", "B", "Dp", "Dtp", "det", "delta", "source_charge")
    }


def exact_panel():
    rows = []
    for index, x in enumerate(PANELS):
        t = [v * v for v in x]
        models = {
            "gaussian_rank_one": [Q(1, 2)] * 4,
            "one_atom": [1 / (v + 1) for v in t],
            "two_atoms": [2 / (v + 1) + 3 / (v + 4) for v in t],
            "constant_one_atom": [1 + 1 / (v + 1) for v in t],
            "zero_one_atom": [1 / v + 1 / (v + 1) for v in t],
        }
        for name, p in models.items():
            rows.append({"panel": index, "model": name, "values": exact_control(x, p)})
    grid = []
    for index, x in enumerate(PANELS):
        for p in itertools.product((Q(-1), Q(0), Q(2)), repeat=4):
            grid.append(
                {
                    "panel": index,
                    "p": [pack(v) for v in p],
                    "values": exact_control(x, p),
                }
            )
    return {
        "models": rows,
        "grid_count": len(grid),
        "grid_sha256": sha(canonical(grid)),
        "discovery": exact_control(
            tuple(map(Q, (1, 2, 3, 4))), list(map(Q, (1, 3, 2, 7)))
        ),
        "volterra_determinants": [
            {"u": u, "v": v, "det": -((u - v) ** 2)}
            for u in range(1, 5)
            for v in range(u + 1, 6)
        ],
    }


def native_jet(x):
    require(type(x) is Q and Q(1, 2) < x <= 128, "native domain/type")
    require(ctx.prec == BITS and ctx.cap == 2, "native precision/jet cap")
    s = acb_series([acb(qarb(x + Q(1, 2))), acb(1)], 2)
    y = s * (s - 1) / 2 * (-s / 2 * arb.pi().log()).exp() * (s / 2).gamma() * s.zeta()
    require(
        all(y[i].is_finite() and y[i].imag.contains(0) for i in range(2)),
        "native finite real jet",
    )
    require(y[0].real.lower() > 0, "native Y positivity guard")
    f = y[1] / y[0]
    require(f.is_finite() and f.imag.contains(0), "native log jet")
    return y[0].real, y[1].real, f.real


def native_panel():
    require(sys.version_info[:2] == (3, 12), "CPython runtime")
    require(
        flint.__version__ == "0.9.0" and flint.__FLINT_VERSION__ == "3.6.0",
        "FLINT runtime",
    )
    old_prec, old_cap = ctx.prec, ctx.cap
    ctx.prec, ctx.cap = BITS, 2
    try:
        rows = []
        for index, x in enumerate(PANELS):
            jets = [native_jet(v) for v in x]
            p = [jets[i][2] / qarb(x[i]) for i in range(4)]
            a = algebra(x, p)
            identities = (
                a["det"] * qarb(a["plus"]) - a["A"] * a["B"],
                a["A"] - qarb(a["vandermonde"]) * a["Dp"],
                a["B"] - qarb(a["vandermonde"]) * a["Dtp"],
                a["bordered"] - a["det"],
                a["source_charge"] - a["delta"] * a["det"],
            )
            require(all(v.contains(0) for v in identities), "native identity enclosure")
            principal = []
            for size in range(1, 5):
                for inds in itertools.combinations(range(4), size):
                    val = determinant(minor(a["h"], list(inds)))
                    principal.append(
                        {
                            "indices": list(inds),
                            "enclosure": interval(val),
                            "status": "POSITIVE"
                            if val.lower() > 0
                            else "NEGATIVE"
                            if val.upper() < 0
                            else "UNRESOLVED",
                        }
                    )
            rows.append(
                {
                    "index": index,
                    "x": [pack(v) for v in x],
                    "jet_Y_Yprime_F": [[interval(v) for v in jet] for jet in jets],
                    "matrix": [[interval(v) for v in row] for row in a["h"]],
                    "principal": principal,
                    "factors": {
                        key: interval(a[key])
                        for key in (
                            "A",
                            "B",
                            "Dp",
                            "Dtp",
                            "det",
                            "delta",
                            "bordered",
                            "source_charge",
                        )
                    },
                    "alpha": [interval(v) for v in a["alpha"]],
                    "identity_zero_enclosures": [interval(v) for v in identities],
                }
            )
        return rows
    finally:
        ctx.prec, ctx.cap = old_prec, old_cap


def git(*args):
    data = subprocess.check_output(
        ["git", "-C", str(ROOT), *args], stderr=subprocess.PIPE
    )
    require(len(data) <= 4_000_000, "source byte cap")
    return data


def source_manifest():
    records = []
    for commit, path in SOURCES:
        data = git("show", commit + ":" + path)
        records.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": git("rev-parse", commit + ":" + path).decode().strip(),
                "sha256_lf": sha(lf(data)),
            }
        )
    return {
        "schema": "xi-source-polarization-four-node-sources-v1",
        "authoring_base": BASE,
        "preregistered_design": git("rev-parse", PREREG).decode().strip(),
        "sources": records,
        "external_primary": [
            "https://dlmf.nist.gov/25.4.E4",
            "https://arxiv.org/abs/1412.5969",
            "https://arxiv.org/abs/math/0411280",
        ],
        "external_content_machine_authenticated": False,
    }


def artifacts():
    return [
        {
            "path": str(p.relative_to(ROOT)).replace("\\", "/"),
            "sha256_lf": sha(lf(p.read_bytes())),
        }
        for p in (NOTE, Path(__file__), TEST, MANIFEST)
    ]


def build():
    require(
        canonical(load(MANIFEST)) == canonical(source_manifest()),
        "source manifest mismatch",
    )
    result = {
        "contract": CONTRACT,
        "artifacts": artifacts(),
        "exact": exact_panel(),
        "native": native_panel(),
    }
    result["payload_sha256"] = sha(canonical(result))
    validate_tree(result)
    return result


def validate(value):
    validate_tree(value)
    require(
        type(value) is dict
        and set(value)
        == {"contract", "artifacts", "exact", "native", "payload_sha256"},
        "fixture schema",
    )
    core = {k: v for k, v in value.items() if k != "payload_sha256"}
    require(value["payload_sha256"] == sha(canonical(core)), "payload seal")
    require(canonical(value["contract"]) == canonical(CONTRACT), "contract mismatch")
    require(canonical(value["artifacts"]) == canonical(artifacts()), "artifact seal")
    require(
        canonical(load(MANIFEST)) == canonical(source_manifest()),
        "source authentication",
    )
    require(
        canonical(value) == canonical(build()),
        "fresh semantic reconstruction mismatch",
    )
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit", action="store_true")
    mode.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        print(canonical(source_manifest()).decode(), end="")
    elif args.check:
        validate(load(FIXTURE))
        print(
            "PASS: six frozen native quadruples, exact controls, source/artifact seals"
        )
    else:
        print(canonical(build()).decode(), end="")


if __name__ == "__main__":
    main()
