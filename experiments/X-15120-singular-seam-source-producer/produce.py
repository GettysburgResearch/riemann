#!/usr/bin/env python3
"""Exact source-bound producer for a finite singular-seam quartic row.

The program has two modes.

1. A complete manifest containing concrete finite matrices for every factor in
   the manuscript's comparison chain is assembled exactly over Gaussian
   rationals. The producer emits c4, the raw and renormalized form matrices,
   represented operators, fourth traces, the jet S4 norm, and target verdicts.

2. An incomplete manuscript-source manifest is audited fail-closed. The program
   emits SOURCE_SPECIFICATION_INCOMPLETE and the exact missing data paths. It
   never substitutes a surrogate map or an arbitrary "standard" probe.

This is a finite source-binding tool. It does not evaluate omitted infinite
operators and does not certify RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "riemann.singular-seam-source-row.v1"

@dataclass(frozen=True)
class Q:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: Any) -> "Q":
        o = q(other)
        return Q(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self) -> "Q":
        return Q(-self.re, -self.im)

    def __sub__(self, other: Any) -> "Q":
        return self + (-q(other))

    def __rsub__(self, other: Any) -> "Q":
        return q(other) - self

    def __mul__(self, other: Any) -> "Q":
        o = q(other)
        return Q(self.re * o.re - self.im * o.im,
                 self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, other: Any) -> "Q":
        o = q(other)
        den = o.re * o.re + o.im * o.im
        if den == 0:
            raise ZeroDivisionError
        return Q((self.re * o.re + self.im * o.im) / den,
                 (self.im * o.re - self.re * o.im) / den)

    def conj(self) -> "Q":
        return Q(self.re, -self.im)

    def abs2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def is_real(self) -> bool:
        return self.im == 0


def frac(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational {x!r}")


def q(x: Any) -> Q:
    if isinstance(x, Q):
        return x
    if isinstance(x, dict) and set(x) == {"re", "im"}:
        return Q(frac(x["re"]), frac(x["im"]))
    return Q(frac(x), Fraction(0))


def out_frac(x: Fraction) -> Any:
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def out_q(x: Q) -> Any:
    if x.im == 0:
        return out_frac(x.re)
    return {"re": out_frac(x.re), "im": out_frac(x.im)}


def matrix(data: Any, name: str) -> list[list[Q]]:
    if not isinstance(data, list) or not data:
        raise ValueError(f"{name} must be a nonempty matrix")
    rows = [[q(x) for x in row] for row in data]
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError(f"{name} is ragged")
    return rows


def vector(data: Any, name: str) -> list[Q]:
    if not isinstance(data, list) or not data:
        raise ValueError(f"{name} must be a nonempty vector")
    return [q(x) for x in data]


def shape(A: list[list[Q]]) -> tuple[int, int]:
    return len(A), len(A[0])


def zeros(m: int, n: int) -> list[list[Q]]:
    return [[Q() for _ in range(n)] for _ in range(m)]


def eye(n: int) -> list[list[Q]]:
    return [[Q(Fraction(int(i == j))) for j in range(n)] for i in range(n)]


def adj(A: list[list[Q]]) -> list[list[Q]]:
    m, n = shape(A)
    return [[A[i][j].conj() for i in range(m)] for j in range(n)]


def add(A: list[list[Q]], B: list[list[Q]]) -> list[list[Q]]:
    if shape(A) != shape(B):
        raise ValueError("matrix shape mismatch")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def sub(A: list[list[Q]], B: list[list[Q]]) -> list[list[Q]]:
    if shape(A) != shape(B):
        raise ValueError("matrix shape mismatch")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def mm(A: list[list[Q]], B: list[list[Q]]) -> list[list[Q]]:
    m, k = shape(A)
    k2, n = shape(B)
    if k != k2:
        raise ValueError(f"matrix multiply mismatch {(m,k)} x {(k2,n)}")
    return [[sum((A[i][t] * B[t][j] for t in range(k)), Q())
             for j in range(n)] for i in range(m)]


def mv(A: list[list[Q]], v: list[Q]) -> list[Q]:
    m, n = shape(A)
    if n != len(v):
        raise ValueError("matrix-vector shape mismatch")
    return [sum((A[i][j] * v[j] for j in range(n)), Q())
            for i in range(m)]


def trace(A: list[list[Q]]) -> Q:
    m, n = shape(A)
    if m != n:
        raise ValueError("trace of nonsquare matrix")
    return sum((A[i][i] for i in range(n)), Q())


def mpow(A: list[list[Q]], exponent: int) -> list[list[Q]]:
    n, n2 = shape(A)
    if n != n2 or exponent < 0:
        raise ValueError("invalid matrix power")
    R = eye(n)
    X = A
    e = exponent
    while e:
        if e & 1:
            R = mm(R, X)
        X = mm(X, X)
        e //= 2
    return R


def is_hermitian(A: list[list[Q]]) -> bool:
    return A == adj(A)


def invert(A: list[list[Q]]) -> list[list[Q]]:
    n, n2 = shape(A)
    if n != n2:
        raise ValueError("inverse requires square matrix")
    aug = [A[i][:] + eye(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n)
                      if not aug[r][col].is_zero()), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            f = aug[r][col]
            if f.is_zero():
                continue
            aug[r] = [aug[r][j] - f * aug[col][j]
                      for j in range(2*n)]
    return [row[n:] for row in aug]


def require_pd_hermitian(G: list[list[Q]], name: str) -> None:
    """Exact Hermitian positive definiteness by Schur-complement LDL pivots."""
    n, n2 = shape(G)
    if n != n2 or not is_hermitian(G):
        raise ValueError(f"{name} must be Hermitian square")
    A = [row[:] for row in G]
    for k in range(n):
        p = A[k][k]
        if not p.is_real() or p.re <= 0:
            raise ValueError(f"{name} nonpositive LDL pivot at {k}: {p}")
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = A[i][j] - A[i][k] * A[k][j] / p


def norm2(v: list[Q]) -> Fraction:
    return sum((z.abs2() for z in v), Fraction(0))


def gram_norm2(v: list[Q], G: list[list[Q]]) -> Fraction:
    w = mv(G, v)
    z = sum((v[i].conj() * w[i] for i in range(len(v))), Q())
    if not z.is_real():
        raise ValueError("Gram norm is not real")
    return z.re


def real_trace(A: list[list[Q]], name: str) -> Fraction:
    z = trace(A)
    if not z.is_real():
        raise ValueError(f"{name} trace is not real: {z}")
    return z.re


def interval(data: Any, name: str) -> tuple[Fraction, Fraction]:
    if not isinstance(data, list) or len(data) != 2:
        raise ValueError(f"{name} must be [lower, upper]")
    lo, hi = frac(data[0]), frac(data[1])
    if lo > hi:
        raise ValueError(f"{name} is reversed")
    return lo, hi


def relation_point_interval(x: Fraction, iv: tuple[Fraction, Fraction]) -> str:
    lo, hi = iv
    if x < lo:
        return "BELOW_TARGET_INTERVAL"
    if x > hi:
        return "ABOVE_TARGET_INTERVAL"
    return "INSIDE_TARGET_INTERVAL"


def relation_intervals(a: tuple[Fraction, Fraction],
                       b: tuple[Fraction, Fraction]) -> str:
    if a[1] < b[0]:
        return "BELOW_TARGET_INTERVAL"
    if a[0] > b[1]:
        return "ABOVE_TARGET_INTERVAL"
    return "OVERLAPS_TARGET_INTERVAL"


REQUIRED_PATHS = [
    "bindings.manuscript_version",
    "bindings.normalization_sha256",
    "bindings.source_map_sha256",
    "window.identifier",
    "window.cutoff_definition",
    "parameters.alpha",
    "parameters.s_R",
    "parameters.a_tr",
    "readout.gram",
    "readout.quartic_jet_coordinate",
    "chain.raw_coordinate_matrix",
    "chain.jet_coordinate_matrix",
    "chain.seam_transpose_matrix",
    "chain.comparison_trace_matrix",
    "chain.lci_matrix",
    "chain.projection_matrix",
    "chain.seam_involution",
    "classical.a4_linear_interval",
    "target.tau4_interval",
]


def at_path(data: Any, path: str) -> Any:
    cur = data
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def missing_paths(data: dict[str, Any]) -> list[str]:
    return [p for p in REQUIRED_PATHS if at_path(data, p) is None]


def audit_incomplete(data: dict[str, Any]) -> dict[str, Any]:
    missing = missing_paths(data)
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return {
        "status": "SOURCE_SPECIFICATION_INCOMPLETE" if missing else "SOURCE_SPECIFICATION_COMPLETE",
        "missing_fields": missing,
        "missing_count": len(missing),
        "cannot_emit": [
            "c4_vector",
            "raw_operator_A",
            "renormalized_operator_K",
            "a4_linear",
            "trace_A4",
            "trace_K4",
            "quartic_target_verdict",
        ] if missing else [],
        "manifest_sha256": hashlib.sha256(canonical).hexdigest(),
        "scope": "source executability audit; no surrogate completion",
    }


def verify_complete(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    missing = missing_paths(data)
    if missing:
        return audit_incomplete(data)

    G = matrix(data["readout"]["gram"], "readout.gram")
    require_pd_hermitian(G, "readout.gram")
    n, n2 = shape(G)
    if n != n2:
        raise ValueError("Gram is not square")
    Ginv = invert(G)

    v4 = vector(data["readout"]["quartic_jet_coordinate"],
                "readout.quartic_jet_coordinate")
    if len(v4) != n:
        raise ValueError("quartic jet/readout dimension mismatch")
    v4_gnorm2 = gram_norm2(v4, G)
    if v4_gnorm2 <= 0:
        raise ValueError("quartic jet coordinate has zero Gram norm")

    raw_coord = matrix(data["chain"]["raw_coordinate_matrix"],
                       "chain.raw_coordinate_matrix")
    jet_coord = matrix(data["chain"]["jet_coordinate_matrix"],
                       "chain.jet_coordinate_matrix")
    if shape(raw_coord) != shape(jet_coord):
        raise ValueError("raw/jet coordinate shape mismatch")
    p, ncoord = shape(raw_coord)
    if ncoord != n:
        raise ValueError("coordinate/readout dimension mismatch")

    Nseam = matrix(data["chain"]["seam_transpose_matrix"],
                   "chain.seam_transpose_matrix")
    Tcmp = matrix(data["chain"]["comparison_trace_matrix"],
                  "chain.comparison_trace_matrix")
    LCI = matrix(data["chain"]["lci_matrix"], "chain.lci_matrix")
    P = matrix(data["chain"]["projection_matrix"],
               "chain.projection_matrix")
    S = matrix(data["chain"]["seam_involution"],
               "chain.seam_involution")

    if shape(Nseam)[1] != p:
        raise ValueError("seam transpose/source-coordinate mismatch")
    chain = mm(P, mm(LCI, mm(Tcmp, Nseam)))
    raw_map = mm(chain, raw_coord)
    jet_map = mm(chain, jet_coord)
    target_dim, source_dim = shape(raw_map)
    if source_dim != n or shape(jet_map) != (target_dim, n):
        raise ValueError("assembled comparison-map dimension mismatch")
    if shape(S) != (target_dim, target_dim):
        raise ValueError("seam involution/target dimension mismatch")
    if not is_hermitian(S):
        raise ValueError("seam involution is not Hermitian")
    if mm(S, S) != eye(target_dim):
        raise ValueError("seam involution does not square to identity")
    if shape(P)[0] != shape(P)[1] or not is_hermitian(P) or mm(P, P) != P:
        raise ValueError("projection matrix is not an orthogonal projection")

    ren_map = sub(raw_map, jet_map)
    BA = mm(adj(raw_map), mm(S, raw_map))
    BK = mm(adj(ren_map), mm(S, ren_map))
    A = mm(Ginv, BA)
    K = mm(Ginv, BK)
    trA4 = real_trace(mpow(A, 4), "A^4")
    trK4 = real_trace(mpow(K, 4), "K^4")

    c4 = mv(jet_map, v4)
    c4_norm2 = norm2(c4)
    c4_normalized_lower2 = c4_norm2 / v4_gnorm2

    CstarC = mm(adj(jet_map), jet_map)
    represented_CstarC = mm(Ginv, CstarC)
    jet_s4_fourth = real_trace(mpow(represented_CstarC, 2),
                               "jet Schatten-four fourth power")
    if jet_s4_fourth < 0:
        raise ValueError("negative Schatten-four fourth power")

    a4_iv = interval(data["classical"]["a4_linear_interval"],
                     "classical.a4_linear_interval")
    tau_iv = interval(data["target"]["tau4_interval"],
                      "target.tau4_interval")

    rel_a4 = relation_intervals(a4_iv, tau_iv)
    rel_A = relation_point_interval(trA4, tau_iv)
    rel_K = relation_point_interval(trK4, tau_iv)
    relations = [rel_a4, rel_A, rel_K]
    if all(x in {"OVERLAPS_TARGET_INTERVAL", "INSIDE_TARGET_INTERVAL"}
           for x in relations):
        verdict = "QUARTIC_ROW_OVERLAPS_TARGET"
    elif any(x in {"BELOW_TARGET_INTERVAL", "ABOVE_TARGET_INTERVAL"}
             for x in relations):
        verdict = "QUARTIC_TARGET_CHANGE_CERTIFIED"
    else:
        verdict = "UNRESOLVED_INTERVAL"

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return {
        "status": "CERTIFIED_SOURCE_BOUND_QUARTIC_ROW",
        "quartic_verdict": verdict,
        "dimensions": {
            "readout": n,
            "coordinate": p,
            "target": target_dim,
        },
        "c4_vector": [out_q(z) for z in c4],
        "c4_norm_squared": out_frac(c4_norm2),
        "quartic_jet_gram_norm_squared": out_frac(v4_gnorm2),
        "c4_normalized_lower_bound_squared": out_frac(c4_normalized_lower2),
        "jet_schatten4_fourth_power": out_frac(jet_s4_fourth),
        "raw_map": [[out_q(z) for z in row] for row in raw_map],
        "jet_map": [[out_q(z) for z in row] for row in jet_map],
        "renormalized_map": [[out_q(z) for z in row] for row in ren_map],
        "raw_form_matrix": [[out_q(z) for z in row] for row in BA],
        "renormalized_form_matrix": [[out_q(z) for z in row] for row in BK],
        "represented_A": [[out_q(z) for z in row] for row in A],
        "represented_K": [[out_q(z) for z in row] for row in K],
        "trace_A4": out_frac(trA4),
        "trace_K4": out_frac(trK4),
        "a4_linear_interval": [out_frac(x) for x in a4_iv],
        "tau4_interval": [out_frac(x) for x in tau_iv],
        "relations": {
            "a4_linear_vs_tau4": rel_a4,
            "trace_A4_vs_tau4": rel_A,
            "trace_K4_vs_tau4": rel_K,
        },
        "manifest_sha256": hashlib.sha256(canonical).hexdigest(),
        "scope": "finite source-bound row only; no infinite-window or RH claim",
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("manifest", type=Path)
    args = p.parse_args()
    data = json.loads(args.manifest.read_text())
    if data.get("schema") != SCHEMA:
        raise SystemExit("wrong schema")
    result = verify_complete(data)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
