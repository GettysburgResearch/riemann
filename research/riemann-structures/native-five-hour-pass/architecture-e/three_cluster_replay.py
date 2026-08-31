"""Exact finite source algebra for the three-moderate/one-high theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import types
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREFIX = "research/riemann-structures/native-five-hour-pass/architecture-e/"
FREEZE = "a7334a169cfa8ca5b1f0721692d9c888e79ba5cb"
PINS = (
    (PREFIX + "MIXED_LOW_HIGH_PACKET.md", "8af68df8d2a5e84469ba032139b20d904ce3dc3c"),
    (
        PREFIX + "MIXED_PACKET_PREREGISTRATION.md",
        "80b68a480b05f44d138dd7007fc701428f3cadbd",
    ),
    (PREFIX + "mixed_packet_replay.py", "6e4b6cb22d59ed6761ab8b62d09b449848b134b6"),
    (
        PREFIX + "mixed_packet_verification.json",
        "c44841dc2fb810371950ee86dc6b5e5fd67de487",
    ),
    (
        "tests/test_architecture_e_pass_mixed.py",
        "8c3c33495794e27680379522c96652f2384f9e2d",
    ),
)
R = 2**34
PANELS = ((64, 64, 64, R), (64, 128, 256, R), (256, 256, 256, 2**48))
ARTIFACT = HERE / "three_cluster_verification.json"
TEST = ROOT / "tests/test_architecture_e_pass_three_cluster.py"
MAX_BYTES = 2_000_000


def need(c, m):
    if not c:
        raise ValueError(m)


def canonical(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen(path, blob):
    raw = subprocess.check_output(
        ["git", "cat-file", "blob", f"{FREEZE}:{path}"], cwd=ROOT
    )
    actual = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    need(len(raw) <= MAX_BYTES and actual == blob, "dependency blob mismatch")
    return raw


def load_source():
    raw = {p: frozen(p, b) for p, b in PINS}
    m = types.ModuleType("authenticated_mixed_for_three_cluster")
    m.__file__ = str(HERE / "mixed_packet_replay.py")
    exec(  # noqa: S102 -- authenticated frozen definitions
        compile(raw[PREFIX + "mixed_packet_replay.py"], m.__file__, "exec"), m.__dict__
    )
    e, sources, e4 = m.load_source()
    artifact = e.strict_load(raw[PREFIX + "mixed_packet_verification.json"].decode())
    body = {k: v for k, v in artifact.items() if k != "proof_sha256"}
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest()
        == artifact["proof_sha256"],
        "mixed artifact digest",
    )
    for path in (
        PREFIX + "MIXED_LOW_HIGH_PACKET.md",
        PREFIX + "MIXED_PACKET_PREREGISTRATION.md",
        PREFIX + "mixed_packet_replay.py",
        "tests/test_architecture_e_pass_mixed.py",
    ):
        need(
            artifact["owned_sources"][path] == hashlib.sha256(raw[path]).hexdigest(),
            "mixed owned source",
        )
    need(
        artifact["E4_proof_sha256"] == e4 and artifact["sources"] == e.encode(sources),
        "mixed predecessor chain",
    )
    records = [
        {
            "commit": FREEZE,
            "path": p,
            "blob": b,
            "sha256": hashlib.sha256(raw[p]).hexdigest(),
        }
        for p, b in PINS
    ]
    return e, records, artifact["proof_sha256"]


def solve(a, b):
    aug = [[Q(x) for x in row] + [Q(y)] for row, y in zip(a, b, strict=True)]
    n = len(aug)
    for j in range(n):
        p = next((i for i in range(j, n) if aug[i][j]), None)
        need(p is not None, "singular")
        aug[j], aug[p] = aug[p], aug[j]
        q = aug[j][j]
        aug[j] = [x / q for x in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                q = aug[i][j]
                aug[i] = [x - q * y for x, y in zip(aug[i], aug[j], strict=True)]
    return [row[-1] for row in aug]


def column(e, low, y):
    low = tuple(e.rational(x) for x in low)
    y = e.rational(y)
    need(
        len(low) == 3 and 64 <= min(low) <= max(low) <= 256 and y >= R,
        "three-cluster domain",
    )
    l = e.source_matrix(low)
    v = [2 * y] * 3
    matrix = [[(-l[i][j] + (y if i == j else 0)) for j in range(3)] for i in range(3)]
    r = solve(matrix, v)
    need(
        [sum(matrix[i][j] * r[j] for j in range(3)) for i in range(3)] == v,
        "complete Sylvester column",
    )
    return l, v, r


def add(a, b):
    return [
        [x + y for x, y in zip(row, other, strict=True)]
        for row, other in zip(a, b, strict=True)
    ]


def cubic(e, a):
    return add(
        add(e.mm(e.mm(a, a), a), [[2 * x for x in row] for row in a]), e.ident(len(a))
    )


def panel(e, nodes):
    nodes = tuple(e.rational(x) for x in nodes)
    need(len(nodes) == 4, "panel dimension")
    l, v, r = column(e, nodes[:3], nodes[3])
    y = nodes[3]
    a = [l[i] + [v[i]] for i in range(3)] + [[Q(0), Q(0), Q(0), y]]
    p = [e.ident(3)[i] + [r[i]] for i in range(3)] + [[Q(0), Q(0), Q(0), Q(1)]]
    pinv = [e.ident(3)[i] + [-r[i]] for i in range(3)] + [[Q(0), Q(0), Q(0), Q(1)]]
    diag = [l[i] + [Q(0)] for i in range(3)] + [[Q(0), Q(0), Q(0), y]]
    need(a == e.source_matrix(nodes), "original source block")
    need(e.mm(a, p) == e.mm(p, diag), "block similarity")
    need(e.mm(p, pinv) == e.ident(4) and e.mm(pinv, p) == e.ident(4), "block inverses")
    fa = cubic(e, a)
    need(fa == e.mm(e.mm(p, cubic(e, diag)), pinv), "polynomial calculus")
    funcs = e.source_functions(nodes)
    gram = [[e.inner(f, g) for g in funcs] for f in funcs]
    need(
        gram
        == [[nodes[i] / 2 if i == j else Q(0) for j in range(4)] for i in range(4)],
        "literal source Gram",
    )
    for j in range(4):
        need(
            e.derivative_minus(funcs[j]) == e.combine(funcs, [row[j] for row in a]),
            "literal derivative source",
        )
    newton = e.newton_functions(nodes)
    ng = [[e.inner(f, g) for g in newton] for f in newton]
    pivot = e.det(ng) / e.det([row[:-1] for row in ng[:-1]])
    expected = 1 / (2 * y)
    for x in nodes[:-1]:
        expected /= (x + y) ** 2
    need(pivot == expected, "Newton residual")
    return {
        "nodes": nodes,
        "moderate_source": l,
        "coupling": v,
        "sylvester_column": r,
        "block_transform": p,
        "block_transform_inverse": pinv,
        "polynomial_control": fa,
        "literal_source_functions": [e.function_record(f) for f in funcs],
        "literal_source_gram": gram,
        "cauchy_newton_residual": pivot,
        "xi_residual_proved_lower_bound": pivot / 200,
    }


def constants(e):
    c = Q(1, 2)
    r = Q(64)
    q = (r + c) / (r - c)
    j = 1 / (r - c) + 2 * r / (r - c) ** 2 * (1 + q)
    need(j == Q(163330, 2048383) and c * j * j < Q(1, 300), "J3 bound")
    exp = e.exp_upper(Q(23, 10), 16)[1]
    need(exp < 10 and Q(903, 88) > 10, "log reserve")
    prime = 37 * (Q(1, 2**31) + Q(1, 30 * 2**30))
    need(prime == Q(37, 2013265920) and prime < Q(1, 10**7), "prime remainder")
    margin = Q(3, 20) - Q(1, 300) - Q(6, 43) - Q(1, 10**7)
    need(margin > Q(1, 200), "moderate coercivity")
    cross = Q(2856, 2**17)
    need(cross < Q(7, 200), "cross bound")
    schur = Q(1, 400) * Q(49, 400) - Q(7, 400) ** 2
    need(schur == 0, "strict Schur boundary identity")
    return {
        "moderate_interval": [64, 256],
        "high_minimum": R,
        "dimension_split": [3, 1],
        "exp_23_over_10_upper": exp,
        "negative_resolvent_majorant": j,
        "prime_remainder_majorant": prime,
        "moderate_real_F_margin_lower": margin,
        "claimed_moderate_margin": Q(1, 200),
        "moderate_F_norm_upper": 7,
        "sylvester_column_bound": 112,
        "cross_norm_majorant": cross,
        "claimed_cross_upper": Q(7, 200),
        "real_operator_margin": Q(1, 400),
        "relative_kernel_margin": Q(1, 200),
    }


def owned():
    paths = [
        HERE / "THREE_MODERATE_ONE_HIGH.md",
        HERE / "THREE_CLUSTER_PREREGISTRATION.md",
        Path(__file__),
        TEST,
    ]
    return {
        p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in paths
    }


def build():
    e, sources, prior = load_source()
    result = e.encode(
        {
            "schema": "architecture-e-three-cluster-v1",
            "sources": sources,
            "mixed_proof_sha256": prior,
            "owned_sources": owned(),
            "constants": constants(e),
            "panels": [panel(e, n) for n in PANELS],
            "scope": {
                "finite_source_algebra_recomputed": True,
                "xi_values_sampled": False,
                "finite_replay_proves_continuum_theorem": False,
                "written_source_proof_required": True,
                "moderate_nodes_below_64": "OUTSIDE_THEOREM",
                "four_all_moderate": "OPEN",
                "rh": "OPEN",
            },
        }
    )
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "artifact cap")
    return result, e


def accept(candidate, fresh):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str, "shape"
    )
    body = {k: v for k, v in candidate.items() if k != "proof_sha256"}
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest()
        == candidate["proof_sha256"],
        "body digest",
    )
    need(canonical(candidate) == canonical(fresh), "fresh typed mismatch")


def main():
    parser = argparse.ArgumentParser()
    m = parser.add_mutually_exclusive_group(required=True)
    m.add_argument("--write", action="store_true")
    m.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, e = build()
    if args.write:
        ARTIFACT.write_text(
            json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
    else:
        accept(e.strict_load(ARTIFACT.read_text(encoding="utf-8")), result)
    print(
        canonical(
            {
                "result": "PASS",
                "proof_sha256": result["proof_sha256"],
                "panels": len(PANELS),
                "xi_values_sampled": False,
            }
        )
    )


if __name__ == "__main__":
    main()
