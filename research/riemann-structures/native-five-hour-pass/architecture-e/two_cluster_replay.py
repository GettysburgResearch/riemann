"""Exact finite source algebra for the two-moderate/two-high theorem."""

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
R = 2**40
PANELS = ((32, 32, R, R), (32, 256, R, 2**41), (256, 256, R, 2**56))
ARTIFACT = HERE / "two_cluster_verification.json"
TEST = ROOT / "tests/test_architecture_e_pass_two_cluster.py"
MAX_BYTES = 2_000_000


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def blob_id(raw):
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def frozen(path, blob):
    need(type(path) is str and type(blob) is str and len(blob) == 40, "dependency pin")
    raw = subprocess.check_output(
        ["git", "cat-file", "blob", f"{FREEZE}:{path}"], cwd=ROOT
    )
    need(len(raw) <= MAX_BYTES and blob_id(raw) == blob, "dependency blob mismatch")
    return raw


def load_source():
    # Authenticate the complete direct mixed dependency before compiling its helper.
    raw = {path: frozen(path, blob) for path, blob in PINS}
    m = types.ModuleType("authenticated_mixed_for_two_cluster")
    m.__file__ = str(HERE / "mixed_packet_replay.py")
    exec(
        compile(raw[PREFIX + "mixed_packet_replay.py"], m.__file__, "exec"), m.__dict__
    )  # noqa: S102 -- authenticated frozen definitions
    e, sources, e4_proof = m.load_source()
    artifact = e.strict_load(raw[PREFIX + "mixed_packet_verification.json"].decode())
    body = {key: value for key, value in artifact.items() if key != "proof_sha256"}
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
            "mixed owned source binding",
        )
    need(
        artifact["E4_proof_sha256"] == e4_proof
        and artifact["sources"] == e.encode(sources),
        "mixed predecessor chain",
    )
    records = [
        {
            "commit": FREEZE,
            "path": path,
            "blob": blob,
            "sha256": hashlib.sha256(raw[path]).hexdigest(),
        }
        for path, blob in PINS
    ]
    return e, records, artifact["proof_sha256"]


def solve(a, b):
    need(len(a) == len(b) and all(len(row) == len(a) for row in a), "square solve")
    aug = [
        [Q(value) for value in row] + [Q(rhs)] for row, rhs in zip(a, b, strict=True)
    ]
    n = len(aug)
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        need(pivot is not None, "singular Sylvester system")
        aug[j], aug[pivot] = aug[pivot], aug[j]
        p = aug[j][j]
        aug[j] = [x / p for x in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                q = aug[i][j]
                aug[i] = [x - q * y for x, y in zip(aug[i], aug[j], strict=True)]
    return [row[-1] for row in aug]


def sylvester(e, low, high):
    low, high = tuple(e.rational(x) for x in low), tuple(e.rational(y) for y in high)
    need(
        len(low) == len(high) == 2
        and 32 <= min(low) <= max(low) <= 256
        and min(high) >= R,
        "two-cluster domain",
    )
    l, b = e.source_matrix(low), e.source_matrix(high)
    v = [[2 * y for y in high] for _ in low]
    coefficients = []
    rhs = []
    for i in range(2):
        for j in range(2):
            row = [Q(0)] * 4
            for k in range(2):
                row[2 * i + k] += b[k][j]
                row[2 * k + j] -= l[i][k]
            coefficients.append(row)
            rhs.append(v[i][j])
    flat = solve(coefficients, rhs)
    s = [flat[:2], flat[2:]]
    # Written without any helper alias: S B - L S = V.
    residual = [
        [e.mm(s, b)[i][j] - e.mm(l, s)[i][j] for j in range(2)] for i in range(2)
    ]
    need(residual == v, "complete Sylvester equation")
    return l, b, v, s


def join_blocks(a, b, c, d):
    return [a[i] + b[i] for i in range(len(a))] + [c[i] + d[i] for i in range(len(c))]


def matrix_add(a, b):
    return [
        [x + y for x, y in zip(row, other, strict=True)]
        for row, other in zip(a, b, strict=True)
    ]


def cubic(e, a):
    return matrix_add(
        matrix_add(e.mm(e.mm(a, a), a), [[2 * x for x in row] for row in a]),
        e.ident(len(a)),
    )


def panel_record(e, nodes):
    nodes = tuple(e.rational(x) for x in nodes)
    need(len(nodes) == 4, "four-node registered panel")
    l, b, v, s = sylvester(e, nodes[:2], nodes[2:])
    zero = [[Q(0), Q(0)], [Q(0), Q(0)]]
    identity = e.ident(2)
    a = join_blocks(l, v, zero, b)
    p = join_blocks(identity, s, zero, identity)
    pinv = join_blocks(identity, [[-x for x in row] for row in s], zero, identity)
    diagonal = join_blocks(l, zero, zero, b)
    need(e.mm(a, p) == e.mm(p, diagonal), "complete block similarity")
    need(
        e.mm(p, pinv) == e.ident(4) and e.mm(pinv, p) == e.ident(4),
        "both block inverse products",
    )
    fa = cubic(e, a)
    need(fa == e.mm(e.mm(p, cubic(e, diagonal)), pinv), "complete polynomial calculus")
    functions = e.source_functions(nodes)
    gram = [[e.inner(f, g) for g in functions] for f in functions]
    need(
        gram
        == [[nodes[i] / 2 if i == j else Q(0) for j in range(4)] for i in range(4)],
        "literal two-cluster source Gram",
    )
    source = e.source_matrix(nodes)
    need(source == a, "block source is original four-node matrix")
    for j in range(4):
        need(
            e.derivative_minus(functions[j])
            == e.combine(functions, [row[j] for row in source]),
            "literal derivative source",
        )
    newton = e.newton_functions(nodes)
    ng = [[e.inner(f, g) for g in newton] for f in newton]
    pivot = e.det(ng) / e.det([row[:-1] for row in ng[:-1]])
    expected = 1 / (2 * nodes[-1])
    for x in nodes[:-1]:
        expected /= (x + nodes[-1]) ** 2
    need(pivot == expected, "two-cluster Newton residual")
    return {
        "nodes": nodes,
        "low_source": l,
        "high_source": b,
        "coupling": v,
        "sylvester_solution": s,
        "block_transform": p,
        "block_transform_inverse": pinv,
        "polynomial_control": fa,
        "literal_source_functions": [e.function_record(f) for f in functions],
        "literal_source_gram": gram,
        "cauchy_newton_residual": pivot,
        "xi_residual_proved_lower_bound": pivot / 50,
    }


def constants(e):
    c = Q(1, 2)
    r = Q(32)
    j = 1 / (r - c) + 2 * r / (r - c) ** 2
    exp3_upper = e.exp_upper(Q(3), 16)[1]
    need(exp3_upper < Q(81, 4) and Q(455, 88) > Q(9, 2), "logarithm source bound")
    need(
        j == Q(382, 3969) and j < Q(1, 10) and c * j * j < Q(1, 200),
        "negative resolvent bound",
    )
    prime = 8 * (Q(1, 2**15) + Q(1, 14 * 2**14))
    need(prime == Q(1, 3584) and prime < Q(1, 3000), "Euler-prime remainder")
    low_margin = Q(1, 4) - Q(1, 200) - Q(1, 10) - Q(1, 3000)
    need(
        low_margin == Q(217, 1500) and low_margin > Q(1, 8), "moderate block coercivity"
    )
    inverse_poly = Q(2**16) ** 2 - 1280 * Q(2**16) + 131072
    need(inverse_poly > 0, "Sylvester inverse threshold")
    cross = 552 * Q(55, 2) + 184
    need(cross == 15364 and cross / Q(2**20) < Q(1, 64), "cross-block norm")
    schur = Q(23, 200) ** 2 - Q(1, 128) ** 2
    need(schur > 0, "two-cluster Schur margin")
    return {
        "moderate_interval": [32, 256],
        "high_minimum": R,
        "dimension_split": [2, 2],
        "exp_3_upper": exp3_upper,
        "negative_resolvent_majorant": j,
        "prime_remainder_majorant": prime,
        "moderate_real_F_margin": low_margin,
        "moderate_F_norm_upper": 6,
        "inverse_threshold_polynomial": inverse_poly,
        "sylvester_column_bounds": [92, 460],
        "cross_numerator": cross,
        "cross_norm_upper": Q(1, 64),
        "real_operator_margin": Q(1, 100),
        "relative_kernel_margin": Q(1, 50),
        "positive_schur_margin": schur,
    }


def owned_sources():
    paths = [
        HERE / "TWO_MODERATE_TWO_HIGH.md",
        HERE / "TWO_CLUSTER_PREREGISTRATION.md",
        Path(__file__),
        TEST,
    ]
    return {
        p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in paths
    }


def build():
    e, sources, mixed_proof = load_source()
    result = e.encode(
        {
            "schema": "architecture-e-two-cluster-v1",
            "sources": sources,
            "mixed_proof_sha256": mixed_proof,
            "owned_sources": owned_sources(),
            "constants": constants(e),
            "panels": [panel_record(e, nodes) for nodes in PANELS],
            "scope": {
                "finite_source_algebra_recomputed": True,
                "xi_values_sampled": False,
                "finite_replay_proves_continuum_theorem": False,
                "written_source_proof_required": True,
                "moderate_third_node": "OUTSIDE_THEOREM",
                "nodes_below_32_in_low_block": "OUTSIDE_THEOREM",
                "unrestricted_four_node_safe_axis": "OPEN",
                "rh": "OPEN",
            },
        }
    )
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "artifact byte cap")
    return result, e


def accept(candidate, fresh):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str,
        "artifact shape",
    )
    body = {key: value for key, value in candidate.items() if key != "proof_sha256"}
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest()
        == candidate["proof_sha256"],
        "body digest",
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
