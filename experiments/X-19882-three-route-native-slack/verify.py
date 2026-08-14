#!/usr/bin/env python3
"""Exact regression for the three-route native-slack packet.

The checker uses fractions.Fraction only.  It verifies:

1. the native detail-slack cocycle and Y4 scalar recurrence;
2. a subcritical affine-cost recurrence on a finite scale tower;
3. the four depth graph-Gram identities and exact generator intertwining;
4. a positive double-Laplace/Stieltjes finite-string analogue;
5. the two truncated Hankel tests of the passive-string finite datum;
6. the discrete geometric-ramp transform analogue.

It does not reconstruct PR #473, DGGC_a, PSI_a, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x19882-three-route-native-slack.v1"
OUTPUT_SCHEMA = "riemann.x19882-three-route-native-slack-verification.v1"


class CertificateError(ValueError):
    pass


def rat(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} must be rational text") from exc
    if isinstance(value, dict) and set(value) == {"numerator", "denominator"}:
        n = value["numerator"]
        d = value["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise CertificateError(f"{name} fraction entries must not be Boolean")
        try:
            n_i = int(n)
            d_i = int(d)
        except (TypeError, ValueError) as exc:
            raise CertificateError(f"{name} fraction entries must be integers") from exc
        if d_i <= 0:
            raise CertificateError(f"{name}.denominator must be positive")
        return Fraction(n_i, d_i)
    raise CertificateError(f"{name} must be an exact rational")


def fj(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def vec(values: Any, name: str) -> list[Fraction]:
    if not isinstance(values, list) or not values:
        raise CertificateError(f"{name} must be a nonempty list")
    return [rat(v, f"{name}[{i}]") for i, v in enumerate(values)]


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    if len(a) != len(b):
        raise CertificateError("vector dimension mismatch")
    return [x + y for x, y in zip(a, b)]


def sub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    if len(a) != len(b):
        raise CertificateError("vector dimension mismatch")
    return [x - y for x, y in zip(a, b)]


def scale(c: Fraction, a: list[Fraction]) -> list[Fraction]:
    return [c * x for x in a]


def dot(a: list[Fraction], b: list[Fraction]) -> Fraction:
    if len(a) != len(b):
        raise CertificateError("dot-product dimension mismatch")
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a or not b or len(a[0]) != len(b):
        raise CertificateError("matrix multiplication dimension mismatch")
    if any(len(row) != len(a[0]) for row in a) or any(len(row) != len(b[0]) for row in b):
        raise CertificateError("ragged matrix")
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a or any(len(row) != len(a[0]) for row in a):
        raise CertificateError("ragged matrix")
    return [list(row) for row in zip(*a)]


def madd(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise CertificateError("matrix addition dimension mismatch")
    return [[x + y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def msub(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise CertificateError("matrix subtraction dimension mismatch")
    return [[x - y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def diag(values: list[Fraction]) -> list[list[Fraction]]:
    n = len(values)
    return [[values[i] if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def gram(features: list[list[Fraction]], operator: list[list[Fraction]] | None = None) -> list[list[Fraction]]:
    transformed = features if operator is None else matmul(operator, features)
    return matmul(transpose(transformed), transformed)


def cross_gram(
    features: list[list[Fraction]],
    left: list[list[Fraction]] | None,
    right: list[list[Fraction]] | None,
) -> list[list[Fraction]]:
    lf = features if left is None else matmul(left, features)
    rf = features if right is None else matmul(right, features)
    return matmul(transpose(lf), rf)


def ldl_psd(matrix: list[list[Fraction]], name: str) -> list[Fraction]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise CertificateError(f"{name} must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
        raise CertificateError(f"{name} must be symmetric")
    lower = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    pivots: list[Fraction] = []
    for j in range(n):
        pivot = matrix[j][j] - sum(
            lower[j][k] * lower[j][k] * pivots[k] for k in range(j)
        )
        if pivot < 0:
            raise CertificateError(f"{name} has negative LDL pivot at {j}")
        pivots.append(pivot)
        for i in range(j + 1, n):
            numerator = matrix[i][j] - sum(
                lower[i][k] * lower[j][k] * pivots[k] for k in range(j)
            )
            if pivot == 0:
                if numerator != 0:
                    raise CertificateError(f"{name} has nonzero entry below zero pivot {j}")
                lower[i][j] = Fraction(0)
            else:
                lower[i][j] = numerator / pivot
    return pivots


def matrix_json(matrix: list[list[Fraction]]) -> list[list[dict[str, str]]]:
    return [[fj(x) for x in row] for row in matrix]


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def parse_matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw or not all(isinstance(row, list) for row in raw):
        raise CertificateError(f"{name} must be a nonempty matrix")
    out = [[rat(v, f"{name}[{i}][{j}]") for j, v in enumerate(row)] for i, row in enumerate(raw)]
    width = len(out[0])
    if width == 0 or any(len(row) != width for row in out):
        raise CertificateError(f"{name} must not be ragged")
    return out


def verify_slack(data: dict[str, Any]) -> dict[str, Any]:
    y4 = vec(data.get("y4"), "slack.y4")
    omega = vec(data.get("omega"), "slack.omega")
    current = vec(data.get("current_response"), "slack.current_response")
    root_slack = vec(data.get("root_slack"), "slack.root_slack")
    n = len(y4)
    if any(len(v) != n for v in (omega, current, root_slack)):
        raise CertificateError("slack vectors must have one common dimension")
    if any(x < 0 for x in omega + current + root_slack):
        raise CertificateError("native capacities, current response and root slack must be nonnegative")

    raw_children = data.get("children")
    if not isinstance(raw_children, list) or not raw_children:
        raise CertificateError("slack.children must be nonempty")
    full_reserved = [Fraction(0) for _ in range(n)]
    inserted_response = current[:]
    scalar_children = Fraction(0)
    child_records: list[dict[str, Any]] = []
    for i, raw in enumerate(raw_children):
        if not isinstance(raw, dict):
            raise CertificateError(f"slack.children[{i}] must be an object")
        alpha = rat(raw.get("alpha"), f"slack.children[{i}].alpha")
        capacity = vec(raw.get("capacity"), f"slack.children[{i}].capacity")
        child_slack = vec(raw.get("slack"), f"slack.children[{i}].slack")
        if len(capacity) != n or len(child_slack) != n:
            raise CertificateError("child vectors have wrong dimension")
        if alpha < 0 or any(x < 0 for x in capacity + child_slack):
            raise CertificateError("child alpha/capacity/slack must be nonnegative")
        if any(s > c for s, c in zip(child_slack, capacity)):
            raise CertificateError("child slack exceeds full child capacity")
        response = sub(capacity, child_slack)
        full_reserved = add(full_reserved, scale(alpha, capacity))
        inserted_response = add(inserted_response, scale(alpha, response))
        child_delta = dot(y4, child_slack)
        scalar_children += alpha * child_delta
        child_records.append(
            {
                "alpha": fj(alpha),
                "capacity": [fj(x) for x in capacity],
                "slack": [fj(x) for x in child_slack],
                "response": [fj(x) for x in response],
                "weighted_slack": fj(child_delta),
            }
        )

    if sum((rat(c.get("alpha"), "child.alpha") for c in raw_children), Fraction(0)) >= Fraction(1, 8):
        raise CertificateError("subcritical test requires total child coefficient below 1/8")

    reconstructed_omega = add(add(current, root_slack), full_reserved)
    if reconstructed_omega != omega:
        raise CertificateError("root current + root slack + full child capacities does not equal omega")

    final_slack = sub(omega, inserted_response)
    cocycle_slack = root_slack[:]
    for raw in raw_children:
        alpha = rat(raw.get("alpha"), "child.alpha")
        child_slack = vec(raw.get("slack"), "child.slack")
        cocycle_slack = add(cocycle_slack, scale(alpha, child_slack))
    if final_slack != cocycle_slack:
        raise CertificateError("native slack cocycle failed")
    if any(x < 0 for x in final_slack):
        raise CertificateError("final native slack is negative")

    root_delta = dot(y4, root_slack)
    final_delta = dot(y4, final_slack)
    if final_delta != root_delta + scalar_children:
        raise CertificateError("Y4 scalar cocycle failed")

    return {
        "dimension": n,
        "y4": [fj(x) for x in y4],
        "omega": [fj(x) for x in omega],
        "current_response": [fj(x) for x in current],
        "root_slack": [fj(x) for x in root_slack],
        "children": child_records,
        "total_child_alpha": fj(sum((rat(c.get("alpha"), "child.alpha") for c in raw_children), Fraction(0))),
        "final_response": [fj(x) for x in inserted_response],
        "final_slack": [fj(x) for x in final_slack],
        "root_weighted_slack": fj(root_delta),
        "child_weighted_contribution": fj(scalar_children),
        "final_weighted_slack": fj(final_delta),
        "verdict": "PASS_EXACT_NATIVE_SLACK_COCYCLE",
    }


def verify_recurrence(data: dict[str, Any]) -> dict[str, Any]:
    rho = rat(data.get("rho"), "recurrence.rho")
    a = rat(data.get("local_constant"), "recurrence.local_constant")
    b = rat(data.get("local_slope"), "recurrence.local_slope")
    depth_raw = data.get("depth")
    if isinstance(depth_raw, bool) or not isinstance(depth_raw, int) or depth_raw < 1:
        raise CertificateError("recurrence.depth must be a positive integer")
    if not 0 <= rho < 1:
        raise CertificateError("recurrence.rho must lie in [0,1)")
    if a < 0 or b < 0:
        raise CertificateError("recurrence local costs must be nonnegative")
    values = [Fraction(0)]
    closed_values = [Fraction(0)]
    for n in range(1, depth_raw + 1):
        values.append(a + b * n + rho * values[-1])
        closed = sum((rho**k * (a + b * (n - k)) for k in range(n)), Fraction(0))
        closed_values.append(closed)
        if values[-1] != closed:
            raise CertificateError("subcritical recurrence closed form failed")
    envelope = (a + b * depth_raw) / (1 - rho)
    if values[-1] > envelope:
        raise CertificateError("subcritical affine envelope failed")
    return {
        "rho": fj(rho),
        "local_constant": fj(a),
        "local_slope": fj(b),
        "depth": depth_raw,
        "values": [fj(x) for x in values],
        "closed_values": [fj(x) for x in closed_values],
        "final_envelope": fj(envelope),
        "verdict": "PASS_SUBCRITICAL_LOGARITHMIC_ENVELOPE_ANALOGUE",
    }


def verify_graph(data: dict[str, Any]) -> dict[str, Any]:
    ds_diag = vec(data.get("source_depth_diagonal"), "graph.source_depth_diagonal")
    dt_diag = vec(data.get("model_depth_diagonal"), "graph.model_depth_diagonal")
    de_diag = vec(data.get("environment_depth_diagonal"), "graph.environment_depth_diagonal")
    vs = parse_matrix(data.get("source_features"), "graph.source_features")
    vm = parse_matrix(data.get("model_features"), "graph.model_features")
    ve = parse_matrix(data.get("environment_features"), "graph.environment_features")
    if len(vs) != len(ds_diag) or len(vm) != len(dt_diag) or len(ve) != len(de_diag):
        raise CertificateError("graph feature ambient dimensions do not match depth operators")
    feature_count = len(vs[0])
    if len(vm[0]) != feature_count or len(ve[0]) != feature_count:
        raise CertificateError("graph feature families must have one common index count")
    ds = diag(ds_diag)
    dt = diag(dt_diag)
    de = diag(de_diag)
    source_blocks: dict[str, list[list[Fraction]]] = {}
    target_blocks: dict[str, list[list[Fraction]]] = {}
    operators_s = [None, ds]
    operators_m = [None, dt]
    operators_e = [None, de]
    for i in range(2):
        for j in range(2):
            key = f"{i}{j}"
            source = cross_gram(vs, operators_s[i], operators_s[j])
            target = madd(
                cross_gram(vm, operators_m[i], operators_m[j]),
                cross_gram(ve, operators_e[i], operators_e[j]),
            )
            if source != target:
                raise CertificateError(f"graph Gram block {key} failed")
            source_blocks[key] = source
            target_blocks[key] = target

    total_target_dim = len(dt_diag) + len(de_diag)
    source_dim = len(ds_diag)
    w_raw = data.get("splitting_isometry")
    w = parse_matrix(w_raw, "graph.splitting_isometry")
    if len(w) != total_target_dim or len(w[0]) != source_dim:
        raise CertificateError("splitting_isometry has wrong dimension")
    dte = diag(dt_diag + de_diag)
    if matmul(transpose(w), w) != diag([Fraction(1) for _ in range(source_dim)]):
        raise CertificateError("splitting_isometry is not isometric")
    if matmul(dte, w) != matmul(w, ds):
        raise CertificateError("depth generator intertwining failed")
    combined_features = vm + ve
    if matmul(w, vs) != combined_features:
        raise CertificateError("splitting isometry does not map source features to model+environment features")

    return {
        "source_depth_diagonal": [fj(x) for x in ds_diag],
        "model_depth_diagonal": [fj(x) for x in dt_diag],
        "environment_depth_diagonal": [fj(x) for x in de_diag],
        "feature_count": feature_count,
        "graph_blocks": {k: matrix_json(v) for k, v in source_blocks.items()},
        "intertwining_verified": True,
        "verdict": "PASS_FOUR_DEPTH_GRAPH_GRAMS_AND_INTERTWINING",
    }


def barycentric_moments(qs: list[Fraction], ys: list[Fraction]) -> list[Fraction]:
    n = len(qs)
    moments: list[Fraction] = []
    for k in range(n):
        value = Fraction(0)
        for j, qj in enumerate(qs):
            delta = Fraction(1)
            for i, qi in enumerate(qs):
                if i != j:
                    delta *= qi - qj
            if delta == 0:
                raise CertificateError("passive nodes must be distinct")
            value += ys[j] * ((-qj) ** k) / delta
        moments.append(value)
    return moments


def verify_passive(data: dict[str, Any]) -> dict[str, Any]:
    z = rat(data.get("geometric_parameter"), "passive.geometric_parameter")
    if not 0 < z < 1:
        raise CertificateError("passive geometric_parameter must lie in (0,1)")
    atoms_raw = data.get("atoms")
    if not isinstance(atoms_raw, list) or not atoms_raw:
        raise CertificateError("passive.atoms must be nonempty")
    atoms: list[tuple[int, Fraction, Fraction]] = []
    for i, raw in enumerate(atoms_raw):
        if not isinstance(raw, dict):
            raise CertificateError(f"passive.atoms[{i}] must be an object")
        x = raw.get("location")
        if isinstance(x, bool) or not isinstance(x, int) or x < 0:
            raise CertificateError("passive atom locations must be nonnegative integers")
        weight = rat(raw.get("weight"), f"passive.atoms[{i}].weight")
        if weight < 0:
            raise CertificateError("passive atom weights must be nonnegative")
        damped = weight * z**x
        atoms.append((x, weight, damped))

    derivative_order_raw = data.get("derivative_order")
    if isinstance(derivative_order_raw, bool) or not isinstance(derivative_order_raw, int) or derivative_order_raw < 1:
        raise CertificateError("passive.derivative_order must be a positive integer")
    moments = [
        sum((damped * Fraction(x) ** k for x, _, damped in atoms), Fraction(0))
        for k in range(2 * derivative_order_raw + 1)
    ]
    derivative_hankel = [
        [moments[i + j] for j in range(derivative_order_raw + 1)]
        for i in range(derivative_order_raw + 1)
    ]
    derivative_pivots = ldl_psd(derivative_hankel, "derivative Hankel")

    qs = vec(data.get("nodes"), "passive.nodes")
    if len(set(qs)) != len(qs) or any(q <= 0 for q in qs):
        raise CertificateError("passive nodes must be distinct and positive")
    ys = [
        sum((damped / (q + x) for x, _, damped in atoms), Fraction(0))
        for q in qs
    ]
    bm = barycentric_moments(qs, ys)
    terminal_degree = len(qs) - 1
    if terminal_degree % 2 == 0:
        m = terminal_degree // 2
        h0 = [[bm[i + j] for j in range(m + 1)] for i in range(m + 1)]
        h1 = [[bm[i + j + 1] for j in range(m)] for i in range(m)] if m > 0 else [[Fraction(0)]]
    else:
        m = (terminal_degree - 1) // 2
        h0 = [[bm[i + j] for j in range(m + 1)] for i in range(m + 1)]
        h1 = [[bm[i + j + 1] for j in range(m + 1)] for i in range(m + 1)]
    h0_pivots = ldl_psd(h0, "finite string H0")
    h1_pivots = ldl_psd(h1, "finite string H1")

    activation_raw = data.get("ramp_activation")
    if isinstance(activation_raw, bool) or not isinstance(activation_raw, int) or activation_raw < 0:
        raise CertificateError("passive.ramp_activation must be a nonnegative integer")
    partial_terms_raw = data.get("ramp_partial_terms")
    if isinstance(partial_terms_raw, bool) or not isinstance(partial_terms_raw, int) or partial_terms_raw < 1:
        raise CertificateError("passive.ramp_partial_terms must be a positive integer")
    u = activation_raw
    nmax = u + partial_terms_raw - 1
    partial = sum((z**n * (n - u) for n in range(u, nmax + 1)), Fraction(0))
    start = nmax + 1
    tail = z**start * (
        z / (1 - z) ** 2 + Fraction(start - u, 1) / (1 - z)
    )
    closed = z ** (u + 1) / (1 - z) ** 2
    if partial + tail != closed:
        raise CertificateError("geometric ramp transform analogue failed")

    return {
        "geometric_parameter": fj(z),
        "atoms": [
            {"location": x, "weight": fj(weight), "damped_weight": fj(damped)}
            for x, weight, damped in atoms
        ],
        "derivative_moments": [fj(x) for x in moments],
        "derivative_hankel": matrix_json(derivative_hankel),
        "derivative_hankel_pivots": [fj(x) for x in derivative_pivots],
        "nodes": [fj(x) for x in qs],
        "stieltjes_values": [fj(x) for x in ys],
        "barycentric_moments": [fj(x) for x in bm],
        "finite_string_h0": matrix_json(h0),
        "finite_string_h1": matrix_json(h1),
        "finite_string_h0_pivots": [fj(x) for x in h0_pivots],
        "finite_string_h1_pivots": [fj(x) for x in h1_pivots],
        "geometric_ramp_closed_value": fj(closed),
        "verdict": "PASS_POSITIVE_STIELTJES_DOUBLE_LAPLACE_ANALOGUE",
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    slack_raw = data.get("slack_cocycle")
    recurrence_raw = data.get("subcritical_recurrence")
    graph_raw = data.get("depth_graph")
    passive_raw = data.get("passive_string")
    if not all(isinstance(x, dict) for x in (slack_raw, recurrence_raw, graph_raw, passive_raw)):
        raise CertificateError("all four certificate sections must be objects")
    slack_result = verify_slack(slack_raw)
    recurrence_result = verify_recurrence(recurrence_raw)
    graph_result = verify_graph(graph_raw)
    passive_result = verify_passive(passive_raw)
    proof = {
        "slack_cocycle": slack_result,
        "subcritical_recurrence": recurrence_result,
        "depth_graph": graph_result,
        "passive_string": passive_result,
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": "EXACT_SYNTHETIC_THREE_ROUTE_REGRESSION",
        **proof,
        "proof_object_sha256": canonical_sha(proof),
        "verdict": "PASS_THREE_ROUTE_NATIVE_SLACK_PACKET",
        "proof_boundary": (
            "Fraction-only regression of the exact slack cocycle, subcritical affine recurrence, "
            "four graph-Gram blocks, generator intertwining, positive derivative Hankel tower, "
            "finite Stieltjes string tests, and a geometric-ramp transform analogue. It does not "
            "reconstruct PR #473, prove DGGC_a or PSI_a, or establish RH."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
