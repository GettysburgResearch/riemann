"""Exact finite algebra supporting the separate mixed low/high source theorem."""

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
FREEZE = "686df46fab25eadfc4564808f036e2b4fc1e4b3e"
PINS = (
    (
        FREEZE,
        PREFIX + "FOUR_NODE_HIGH_AXIS.md",
        "39509c6babd3f943e986805946e7f02ea4cc7285",
    ),
    (
        FREEZE,
        PREFIX + "FOUR_NODE_PREREGISTRATION.md",
        "dd5fcd818ba9a5c97fc990b1fd14741783cf67cf",
    ),
    (
        FREEZE,
        PREFIX + "four_node_replay.py",
        "f7702c04422a5430c35594ff0e3f5d0836fa6ab6",
    ),
    (
        FREEZE,
        PREFIX + "four_node_verification.json",
        "bb0c4254f103fe27fe1b98e7f7d9be9d9c201dd8",
    ),
    (
        FREEZE,
        "tests/test_architecture_e_pass_four_node.py",
        "3aeded75526037885eb748a8ed33e0f7cf01940f",
    ),
    (
        "8f01064df805624c045877655893c324a220975d",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
    ),
)
R = 2**30
PANELS = (
    (Q(1, 2), R, R, R),
    (1, R, 2**31, 2**40),
    (256, R, 2**31, 2**32),
)
ARTIFACT = HERE / "mixed_packet_verification.json"
TEST = ROOT / "tests/test_architecture_e_pass_mixed.py"
MAX_BYTES = 2_000_000
MAX_BITS = 4096


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen(commit, path, blob):
    need(
        type(commit) is str and len(commit) == 40 and len(blob) == 40,
        "source pin pending",
    )
    raw = subprocess.check_output(
        ["git", "cat-file", "blob", f"{commit}:{path}"], cwd=ROOT
    )
    need(len(raw) <= MAX_BYTES, "source byte cap")
    actual = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    need(actual == blob, "source blob mismatch")
    return raw


def load_source():
    # No inherited code is compiled until every mathematical/source input is authenticated.
    raw = {path: frozen(commit, path, blob) for commit, path, blob in PINS}
    e = types.ModuleType("authenticated_e4_for_mixed")
    e.__file__ = str(HERE / "four_node_replay.py")
    exec(compile(raw[PREFIX + "four_node_replay.py"], e.__file__, "exec"), e.__dict__)  # noqa: S102 -- exact frozen definitions
    artifact = e.strict_load(raw[PREFIX + "four_node_verification.json"].decode())
    proof = artifact["proof_sha256"]
    body = {key: value for key, value in artifact.items() if key != "proof_sha256"}
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest() == proof,
        "E4 artifact digest",
    )
    for path in (
        PREFIX + "FOUR_NODE_HIGH_AXIS.md",
        PREFIX + "FOUR_NODE_PREREGISTRATION.md",
        PREFIX + "four_node_replay.py",
        "tests/test_architecture_e_pass_four_node.py",
    ):
        need(
            artifact["owned_sources"][path] == hashlib.sha256(raw[path]).hexdigest(),
            "E4 owned source binding",
        )
    need(
        e.decode_fraction(artifact["constants"]["claimed_real_operator_margin"])
        == Q(1, 8),
        "E4 required margin",
    )
    records = [
        {
            "commit": commit,
            "path": path,
            "blob": blob,
            "sha256": hashlib.sha256(raw[path]).hexdigest(),
        }
        for commit, path, blob in PINS
    ]
    return e, records, proof


def checked(e, nodes):
    need(2 <= len(nodes) <= 4, "mixed dimension cap")
    nodes = tuple(e.rational(x) for x in nodes)
    need(Q(1, 2) <= nodes[0] <= 256 and min(nodes[1:]) >= R, "mixed node domain")
    return nodes


def row_product(e, nodes):
    nodes = checked(e, nodes)
    x = nodes[0]
    out, product = [], Q(1)
    for y in nodes[1:]:
        out.append(e.rational(2 * y / (y - x) * product))
        product *= -(y + x) / (y - x)
    return out


def row_triangular(e, nodes):
    nodes = checked(e, nodes)
    x = nodes[0]
    out = []
    for y in nodes[1:]:
        out.append(e.rational((2 * y - 2 * y * sum(out, Q(0))) / (y - x)))
    return out


def matrix_add(a, b):
    return [
        [x + y for x, y in zip(row, other, strict=True)]
        for row, other in zip(a, b, strict=True)
    ]


def cubic(e, a):
    identity = e.ident(len(a))
    return matrix_add(
        matrix_add(e.mm(e.mm(a, a), a), [[2 * x for x in row] for row in a]), identity
    )


def panel_record(e, raw_nodes):
    nodes = checked(e, raw_nodes)
    n, x = len(nodes), nodes[0]
    a = e.source_matrix(nodes)
    b = e.source_matrix(nodes[1:])
    r = row_product(e, nodes)
    need(r == row_triangular(e, nodes), "independent triangular row")
    shifted = [
        [b[i][j] - (x if i == j else 0) for j in range(n - 1)] for i in range(n - 1)
    ]
    need(e.mm([r], shifted)[0] == a[0][1:], "complete row resolvent identity")
    transform, inverse = e.ident(n), e.ident(n)
    transform[0][1:] = r
    inverse[0][1:] = [-v for v in r]
    diagonal = [row[:] for row in a]
    diagonal[0][1:] = [Q(0)] * (n - 1)
    need(e.mm(a, transform) == e.mm(transform, diagonal), "source block similarity")
    need(
        e.mm(transform, inverse) == e.ident(n)
        and e.mm(inverse, transform) == e.ident(n),
        "both block inverse products",
    )
    fa, fb = cubic(e, a), cubic(e, b)
    fx = x**3 + 2 * x + 1
    w = [v - fx * rj for v, rj in zip(e.mm([r], fb)[0], r, strict=True)]
    need(w == fa[0][1:], "polynomial functional-calculus row")
    need(
        e.mm(e.mm(transform, cubic(e, diagonal)), inverse) == fa,
        "complete polynomial similarity",
    )
    functions = e.source_functions(nodes)
    gram = [[e.inner(f, g) for g in functions] for f in functions]
    need(
        gram
        == [[nodes[i] / 2 if i == j else Q(0) for j in range(n)] for i in range(n)],
        "literal mixed exponential Gram",
    )
    for j in range(n):
        need(
            e.derivative_minus(functions[j])
            == e.combine(functions, [row[j] for row in a]),
            "literal mixed derivative source",
        )
    newton = e.newton_functions(nodes)
    ng = [[e.inner(f, g) for g in newton] for f in newton]
    pivot = e.det(ng) / e.det([row[:-1] for row in ng[:-1]])
    expected = 1 / (2 * nodes[-1])
    for y in nodes[:-1]:
        expected /= (nodes[-1] + y) ** 2
    need(pivot == expected, "mixed confluent Newton residual")
    return {
        "nodes": nodes,
        "source_matrix_diagonal_similarity": a,
        "literal_source_functions": [e.function_record(f) for f in functions],
        "literal_source_gram": gram,
        "block_row": r,
        "block_transform": transform,
        "block_transform_inverse": inverse,
        "polynomial_control_offdiagonal": w,
        "polynomial_control_matrix": fa,
        "cauchy_newton_residual": pivot,
        "xi_residual_proved_lower_bound": pivot / 100,
    }


def taylor_lower(e, x, degree):
    x = e.rational(x)
    need(type(degree) is int and 0 <= degree <= 32 and x >= 0, "Taylor domain/cap")
    result, term = Q(1), Q(1)
    for k in range(1, degree + 1):
        term *= x / k
        result += term
    return e.rational(result)


def constants(e):
    log10 = taylor_lower(e, Q(2303, 1000), 16)
    log4pi = taylor_lower(e, Q(127, 50), 16)
    log257 = taylor_lower(e, Q(6), 7)
    need(log10 > 10 and log4pi > Q(88, 7) and log257 > 257, "endpoint logarithm bounds")
    harmonic = sum((Q(1, k) for k in range(1, 11)), Q(0))
    gamma_lower = harmonic - Q(2303, 1000) - Q(1, 20)
    need(gamma_lower > Q(57, 100), "Euler constant lower bound")
    low = 1 + Q(57, 200) - Q(127, 100)
    need(low == Q(3, 200), "low actual-source bound")
    row = 32 * Q(256, 255) * Q(257, 255) ** 2
    need(row < 36, "similarity row majorant")
    offdiag = 1 + Q(1, 32) + Q(7, 256) + Q(27, 256) + Q(1, 1024)
    need(
        offdiag == Q(1193, 1024) and offdiag < 2,
        "high literal-source offdiagonal bound",
    )
    cross = Q(1764, 32768)
    need(cross < Q(1, 16), "low-high cross bound")
    delta = Q(1, 200)
    schur = (low - delta) * (Q(1, 8) - delta) - Q(1, 32) ** 2
    need(schur == Q(3, 2500) - Q(1, 1024) and schur > 0, "uniform block Schur margin")
    return {
        "low_interval": [Q(1, 2), Q(256)],
        "high_minimum": R,
        "maximum_total_dimension": 4,
        "exp_log10_lower": log10,
        "exp_log4pi_lower": log4pi,
        "exp_6_lower": log257,
        "harmonic_10": harmonic,
        "gamma_lower": gamma_lower,
        "low_F_lower": low,
        "low_F_upper": 4,
        "row_majorant": row,
        "high_F_offdiagonal_upper": offdiag,
        "cross_row_upper": cross,
        "real_operator_margin": delta,
        "relative_kernel_margin": 2 * delta,
        "positive_block_schur_margin": schur,
    }


def owned_sources():
    paths = [
        HERE / "MIXED_LOW_HIGH_PACKET.md",
        HERE / "MIXED_PACKET_PREREGISTRATION.md",
        Path(__file__),
        TEST,
    ]
    return {
        p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in paths
    }


def build():
    e, sources, e4_proof = load_source()
    record = e.encode(
        {
            "schema": "architecture-e-mixed-packet-v1",
            "sources": sources,
            "E4_proof_sha256": e4_proof,
            "owned_sources": owned_sources(),
            "constants": constants(e),
            "panels": [panel_record(e, nodes) for nodes in PANELS],
            "scope": {
                "literal_finite_source_algebra_recomputed": True,
                "endpoint_constants_exactly_recomputed": True,
                "xi_values_sampled": False,
                "polynomial_control_replaces_xi": False,
                "finite_replay_proves_continuum_theorem": False,
                "written_source_proof_required": True,
                "two_low_nodes": "OUTSIDE_THEOREM",
                "unrestricted_four_node_safe_axis": "OPEN",
                "rh": "OPEN",
            },
        }
    )
    record["proof_sha256"] = hashlib.sha256(canonical(record).encode()).hexdigest()
    need(len(canonical(record).encode()) <= MAX_BYTES, "artifact byte cap")
    return record, e


def accept(candidate, fresh):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str,
        "artifact shape",
    )
    body = {key: value for key, value in candidate.items() if key != "proof_sha256"}
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest()
        == candidate["proof_sha256"],
        "body digest mismatch",
    )
    need(
        canonical(candidate) == canonical(fresh), "fresh typed reconstruction mismatch"
    )


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    record, e = build()
    if args.write:
        ARTIFACT.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
    else:
        accept(e.strict_load(ARTIFACT.read_text(encoding="utf-8")), record)
    print(
        canonical(
            {
                "result": "PASS",
                "proof_sha256": record["proof_sha256"],
                "panels": len(PANELS),
                "xi_values_sampled": False,
            }
        )
    )


if __name__ == "__main__":
    main()
