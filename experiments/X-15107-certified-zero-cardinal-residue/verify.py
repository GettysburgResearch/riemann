#!/usr/bin/env python3
"""Exact verifier for the selected-zero Cauchy/cardinal residue identity."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.certified-zero-cardinal-residue.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("Boolean is not a rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("Boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("Malformed rational")
        return Fraction(n, d)
    raise ValueError(f"Unsupported rational: {x!r}")


def dump_rat(x: Fraction) -> Any:
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def trim(a: list[Fraction]) -> list[Fraction]:
    out = a[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def padd(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pscale(c, a):
    return trim([c * x for x in a])


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def peval(a, x):
    out = Fraction(0)
    for c in reversed(a):
        out = out * x + c
    return out


def pder(a):
    if len(a) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * a[i] for i in range(1, len(a))])


def product_linear(nodes):
    out = [Fraction(1)]
    for lam in nodes:
        out = pmul(out, [lam, Fraction(-1)])
    return out


def phi_polys(nodes):
    result = []
    for i in range(len(nodes)):
        out = [Fraction(1)]
        for j, lam in enumerate(nodes):
            if j != i:
                out = pmul(out, [lam, Fraction(-1)])
        result.append(out)
    return result


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def complement_basis(p):
    n = len(p)
    r = next(i for i, value in enumerate(p) if value != 0)
    cols = []
    for j in range(n):
        if j == r:
            continue
        col = [Fraction(0)] * n
        col[j] = Fraction(1)
        col[r] = -p[j] / p[r]
        cols.append(col)
    return transpose(cols)


def ldl_positive_pivots(a):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Matrix is not square")
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError("Matrix is not symmetric")
    ell = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        ell[i][i] = Fraction(1)
        d = a[i][i] - sum(ell[i][k] ** 2 * pivots[k] for k in range(i))
        if d <= 0:
            raise ValueError(f"Nonpositive LDL pivot {i}: {d}")
        pivots.append(d)
        for j in range(i + 1, n):
            ell[j][i] = (
                a[j][i]
                - sum(ell[j][k] * ell[i][k] * pivots[k] for k in range(i))
            ) / d
    return pivots


def source_from_atoms(nodes, atoms):
    values = []
    for lam in nodes:
        total = Fraction(0)
        for r, weight in atoms:
            if r == 0 or r == lam:
                raise ValueError("Synthetic atom hits gauge origin or node")
            total += weight * (Fraction(1, r - lam) - Fraction(1, r))
        values.append(total)
    return values


def interpolate(phi, p, source):
    out = [Fraction(0)]
    for i in range(len(p)):
        out = padd(out, pscale(p[i] * source[i], phi[i]))
    return out


def target_matrix(nodes, p, beta, c):
    n = len(nodes)
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i][j] = (beta[i] - beta[j]) / (nodes[i] - nodes[j]) - c
    for i in range(n):
        out[i][i] = -sum(out[i][j] * p[j] for j in range(n) if j != i) / p[i]
    return out


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("Wrong schema")
    nodes = [rat(x) for x in data["nodes"]]
    p = [rat(x) for x in data["p"]]
    roots = [rat(x) for x in data["roots"]]
    c = rat(data.get("boundary_scalar", 0))

    if len(nodes) < 2 or len(p) != len(nodes) or len(roots) != len(nodes) - 1:
        raise ValueError("Dimension mismatch")
    if len(set(nodes)) != len(nodes) or len(set(roots)) != len(roots):
        raise ValueError("Repeated node or root")
    if any(x == 0 for x in p) or sum(p) != 1:
        raise ValueError("Invalid target")
    if any(root in nodes for root in roots):
        raise ValueError("Root equals a node")

    selected = []
    pair_for_root: dict[int, int] = {}
    for atom_index, raw in enumerate(data["selected_atoms"]):
        r = rat(raw["r"])
        w = rat(raw["weight"])
        k = raw["pair_root"]
        if isinstance(k, bool) or not isinstance(k, int) or not (0 <= k < len(roots)):
            raise ValueError("Invalid pairing index")
        if w <= 0 or r == 0 or r in nodes:
            raise ValueError("Invalid selected atom")
        if k in pair_for_root:
            raise ValueError("Duplicate root pairing")
        pair_for_root[k] = atom_index
        selected.append((r, w))
    if set(pair_for_root) != set(range(len(roots))):
        raise ValueError("Every root must have one selected pair")

    residual = []
    for raw in data["residual_atoms"]:
        r = rat(raw["r"])
        w = rat(raw["weight"])
        if w < 0 or r == 0 or r in nodes:
            raise ValueError("Invalid residual atom")
        residual.append((r, w))

    phi = phi_polys(nodes)
    omega = product_linear(nodes)
    ppoly = [Fraction(0)]
    for i in range(len(nodes)):
        ppoly = padd(ppoly, pscale(p[i], phi[i]))
    if len(ppoly) != len(nodes) or ppoly[-1] != 1:
        raise ValueError("Target polynomial degree/normalization mismatch")
    if any(peval(ppoly, u) != 0 for u in roots):
        raise ValueError("Declared root is not a target root")
    dp = pder(ppoly)
    if any(peval(dp, u) == 0 for u in roots):
        raise ValueError("Target root is not simple")

    beta_sel = source_from_atoms(nodes, selected)
    beta_rem = source_from_atoms(nodes, residual)
    beta = [beta_sel[i] + beta_rem[i] for i in range(len(nodes))]
    rrem = interpolate(phi, p, beta_rem)
    rfull = interpolate(phi, p, beta)

    selected_sums = []
    residual_weights = []
    full_weights = []
    capture_lowers = []
    cardinal_rows = []

    def cardinal(k, r):
        u = roots[k]
        if r == u:
            return Fraction(1)
        om_r = peval(omega, r)
        if om_r == 0:
            raise ValueError("Atom at a node")
        return (
            peval(omega, u)
            / peval(dp, u)
            * peval(ppoly, r)
            / (om_r * (r - u))
        )

    for k, u in enumerate(roots):
        row = [cardinal(k, r) for r, _ in selected + residual]
        cardinal_rows.append(row)
        ssum = sum(w * cardinal(k, r) for r, w in selected)
        erem = -peval(rrem, u) / peval(dp, u)
        wfull = -(peval(rfull, u) - c * peval(omega, u)) / peval(dp, u)
        v = peval(omega, u) / peval(dp, u)
        if wfull != ssum + erem + c * v:
            raise ValueError("Cardinal residue identity failed")
        selected_sums.append(ssum)
        residual_weights.append(erem)
        full_weights.append(wfull)

        paired_r, paired_w = selected[pair_for_root[k]]
        pair_error = abs(cardinal(k, paired_r) - 1)
        cross = sum(
            w * abs(cardinal(k, r))
            for idx, (r, w) in enumerate(selected)
            if idx != pair_for_root[k]
        )
        lower = paired_w * (1 - pair_error) - cross - abs(erem) + c * v
        if lower <= 0:
            raise ValueError(f"Root-capture lower bound failed at {k}: {lower}")
        if wfull <= 0:
            raise ValueError(f"Nonpositive exact residue at {k}: {wfull}")
        capture_lowers.append(lower)

    tmat = target_matrix(nodes, p, beta, c)
    if any(x != 0 for x in matvec(tmat, p)):
        raise ValueError("Target-pinning kernel failed")
    cauchy = [
        [
            sum(
                full_weights[k]
                / ((nodes[i] - roots[k]) * (nodes[j] - roots[k]))
                for k in range(len(roots))
            )
            for j in range(len(nodes))
        ]
        for i in range(len(nodes))
    ]
    if tmat != cauchy:
        raise ValueError("Cauchy-ray matrix reconstruction failed")

    u = complement_basis(p)
    restricted = matmul(transpose(u), matmul(tmat, u))
    pivots = ldl_positive_pivots(restricted)

    canonical_bytes = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical_bytes).hexdigest()
    return {
        "status": "CERTIFIED_SELECTED_ZERO_CARDINAL_RESIDUE_FLOOR",
        "beta_selected": [dump_rat(x) for x in beta_sel],
        "beta_residual": [dump_rat(x) for x in beta_rem],
        "beta_complete": [dump_rat(x) for x in beta],
        "cardinal_rows": [[dump_rat(x) for x in row] for row in cardinal_rows],
        "selected_residue_sums": [dump_rat(x) for x in selected_sums],
        "residual_residue_weights": [dump_rat(x) for x in residual_weights],
        "complete_residue_weights": [dump_rat(x) for x in full_weights],
        "capture_lower_bounds": [dump_rat(x) for x in capture_lowers],
        "arithmetic_complement_ldl_pivots": [dump_rat(x) for x in pivots],
        "certificate_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
