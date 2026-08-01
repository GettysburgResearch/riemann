#!/usr/bin/env python3
"""Exact source-sewing and linear-scalar obstruction checker.

Uses only Python integers, fractions.Fraction, JSON, and SHA-256.
It certifies:
  * the Moore--Penrose reconstruction associated with a surjective finite
    synthesis map U;
  * the order-4 and all-retained-order pseudoinverse cyclic sewing identity;
  * invariance under a redundant invertible coordinate change;
  * the exact homogeneity mismatch between a fixed linear scalar readout and
    an ell-fold sewn coefficient;
  * one uniform Hilbert--Schmidt geometric-series majorant.

This is a finite algebraic control. It does not evaluate xi or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.classical-source-sewing.v1"


def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = x["numerator"], x["denominator"]
        if isinstance(n, bool) or isinstance(d, bool):
            raise ValueError("boolean numerator/denominator")
        if not isinstance(n, int) or not isinstance(d, int) or d == 0:
            raise ValueError("malformed rational")
        return Fraction(n, d)
    raise ValueError(f"unsupported rational {x!r}")


def dump_rat(x: Fraction) -> Any:
    if x.denominator == 1:
        return x.numerator
    return {"numerator": x.numerator, "denominator": x.denominator}


def parse_matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw or not all(isinstance(r, list) and r for r in raw):
        raise ValueError(f"{name} must be a nonempty matrix")
    width = len(raw[0])
    if any(len(r) != width for r in raw):
        raise ValueError(f"{name} rows have inconsistent lengths")
    return [[rat(x) for x in r] for r in raw]


def zeros(m: int, n: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n)] for _ in range(m)]


def eye(n: int) -> list[list[Fraction]]:
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = Fraction(1)
    return a


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    m, n = shape(a)
    return [[a[i][j] for i in range(m)] for j in range(n)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    m, k = shape(a)
    k2, n = shape(b)
    if k != k2:
        raise ValueError("matrix dimension mismatch")
    out = zeros(m, n)
    for i in range(m):
        for t in range(k):
            if a[i][t] == 0:
                continue
            for j in range(n):
                out[i][j] += a[i][t] * b[t][j]
    return out


def matscale(c: Fraction, a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in a]


def trace(a: list[list[Fraction]]) -> Fraction:
    m, n = shape(a)
    if m != n:
        raise ValueError("trace requires square matrix")
    return sum(a[i][i] for i in range(n))


def power(a: list[list[Fraction]], k: int) -> list[list[Fraction]]:
    n, m = shape(a)
    if n != m or k < 0:
        raise ValueError("invalid matrix power")
    out = eye(n)
    base = a
    while k:
        if k & 1:
            out = matmul(out, base)
        base = matmul(base, base)
        k >>= 1
    return out


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n, m = shape(a)
    if n != m:
        raise ValueError("inverse requires square matrix")
    ident = eye(n)
    aug = [a[i][:] + ident[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col or aug[r][col] == 0:
                continue
            q = aug[r][col]
            aug[r] = [x - q * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def equal(a: list[list[Fraction]], b: list[list[Fraction]]) -> bool:
    return shape(a) == shape(b) and all(x == y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def pseudoinverse_gram_from_surjective_u(
    u: list[list[Fraction]],
) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    r"""For full-row-rank U, return G=U^T U and G^dagger.

    If H=UU^T, then (U^T U)^dagger=U^T H^(-2) U.
    """
    ut = transpose(u)
    h = matmul(u, ut)
    h_inv = inverse(h)
    h_inv_sq = matmul(h_inv, h_inv)
    g = matmul(ut, u)
    g_dag = matmul(matmul(ut, h_inv_sq), u)
    return g, g_dag


def penrose_checks(g: list[list[Fraction]], gd: list[list[Fraction]]) -> None:
    if not equal(matmul(matmul(g, gd), g), g):
        raise ValueError("G Gdag G != G")
    if not equal(matmul(matmul(gd, g), gd), gd):
        raise ValueError("Gdag G Gdag != Gdag")
    if not equal(transpose(matmul(g, gd)), matmul(g, gd)):
        raise ValueError("G Gdag is not symmetric")
    if not equal(transpose(matmul(gd, g)), matmul(gd, g)):
        raise ValueError("Gdag G is not symmetric")


def cyclic_index_contraction(
    b: list[list[Fraction]], gd: list[list[Fraction]], ell: int
) -> Fraction:
    """Direct index contraction with ell B and ell Gdag factors."""
    n, n2 = shape(b)
    if n != n2 or shape(gd) != (n, n):
        raise ValueError("cyclic contraction requires same-size square matrices")
    m = matmul(b, gd)
    total = Fraction(0)
    for idx in itertools.product(range(n), repeat=ell):
        prod = Fraction(1)
        for j in range(ell):
            prod *= m[idx[j]][idx[(j + 1) % ell]]
        total += prod
    return total


def linear_pairing(weights: list[list[Fraction]], b: list[list[Fraction]]) -> Fraction:
    if shape(weights) != shape(b):
        raise ValueError("linear weights shape mismatch")
    return sum(w * x for rw, rb in zip(weights, b) for w, x in zip(rw, rb))


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise ValueError("wrong schema")
    u = parse_matrix(data["synthesis_U"], "synthesis_U")
    s = parse_matrix(data["seam_S"], "seam_S")
    hdim, cdim = shape(u)
    if shape(s) != (hdim, hdim) or not equal(s, transpose(s)):
        raise ValueError("seam_S must be symmetric on the synthesis target")

    g, gd = pseudoinverse_gram_from_surjective_u(u)
    penrose_checks(g, gd)
    b = matmul(matmul(transpose(u), s), u)
    quotient_projection = matmul(gd, g)
    if not equal(matmul(quotient_projection, b), b) or not equal(
        matmul(b, quotient_projection), b
    ):
        raise ValueError("seam form does not descend to the Gram quotient")

    supplied_g = parse_matrix(data["claimed_gram"], "claimed_gram")
    supplied_gd = parse_matrix(
        data["claimed_gram_pseudoinverse"], "claimed_gram_pseudoinverse"
    )
    supplied_b = parse_matrix(data["claimed_seam_form"], "claimed_seam_form")
    if not equal(supplied_g, g):
        raise ValueError("claimed Gram mismatch")
    if not equal(supplied_gd, gd):
        raise ValueError("claimed Gram pseudoinverse mismatch")
    if not equal(supplied_b, b):
        raise ValueError("claimed seam form mismatch")

    t = matmul(gd, b)
    max_order = data["max_order"]
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 4:
        raise ValueError("max_order must be an integer >=4")
    claimed = {int(k): rat(v) for k, v in data["claimed_trace_moments"].items()}
    if set(claimed) != set(range(2, max_order + 1)):
        raise ValueError("claimed_trace_moments must cover 2..max_order")
    moments: dict[int, Fraction] = {}
    for ell in range(2, max_order + 1):
        val = trace(power(t, ell))
        if val != trace(power(s, ell)):
            raise ValueError(f"source sewing mismatch at order {ell}")
        if claimed[ell] != val:
            raise ValueError(f"claimed trace mismatch at order {ell}")
        moments[ell] = val

    direct4 = cyclic_index_contraction(b, gd, 4)
    if direct4 != moments[4]:
        raise ValueError("direct order-four index contraction mismatch")
    if rat(data["claimed_direct_order_four"]) != direct4:
        raise ValueError("claimed direct order-four mismatch")

    c = parse_matrix(data["coordinate_change_C"], "coordinate_change_C")
    if shape(c) != (cdim, cdim):
        raise ValueError("coordinate change shape mismatch")
    inverse(c)
    u2 = matmul(u, c)
    g2, gd2 = pseudoinverse_gram_from_surjective_u(u2)
    penrose_checks(g2, gd2)
    b2 = matmul(matmul(transpose(u2), s), u2)
    t2 = matmul(gd2, b2)
    for ell in range(2, max_order + 1):
        if trace(power(t2, ell)) != moments[ell]:
            raise ValueError(f"coordinate invariance failed at order {ell}")

    weights = parse_matrix(data["fixed_linear_probe_weights"], "fixed_linear_probe_weights")
    scalar0 = linear_pairing(weights, b)
    if scalar0 != moments[4]:
        raise ValueError("base normalization does not match order-four sewn value")
    scale = rat(data["scaling_test"])
    if scale in (0, 1, -1):
        raise ValueError("scaling_test must expose different homogeneities")
    linear_scaled = linear_pairing(weights, matscale(scale, b))
    sewn_scaled = trace(power(matmul(gd, matscale(scale, b)), 4))
    if linear_scaled == sewn_scaled:
        raise ValueError("homogeneity obstruction was not exposed")
    if linear_scaled != scale * scalar0 or sewn_scaled != scale**4 * moments[4]:
        raise ValueError("incorrect scaling laws")
    claimed_gap = rat(data["claimed_homogeneity_gap"])
    if claimed_gap != sewn_scaled - linear_scaled:
        raise ValueError("claimed homogeneity gap mismatch")

    c_bound = rat(data["hilbert_schmidt_bound"])
    radius = rat(data["series_radius"])
    if c_bound <= 0 or radius <= 0 or c_bound * radius >= 1:
        raise ValueError("invalid geometric-series majorant parameters")
    if c_bound**2 < moments[2]:
        raise ValueError("hilbert_schmidt_bound is too small")
    for ell, val in moments.items():
        if abs(val) > c_bound**ell:
            raise ValueError(f"moment exceeds geometric majorant at order {ell}")
    closed_majorant = c_bound**2 * radius / (1 - c_bound * radius)
    if rat(data["claimed_series_majorant"]) != closed_majorant:
        raise ValueError("claimed series majorant mismatch")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    return {
        "status": "CERTIFIED_SOURCE_SEWING_AND_LINEAR_SCALAR_OBSTRUCTION",
        "target_dimension": hdim,
        "readout_dimension": cdim,
        "gram_rank": hdim,
        "trace_moments": {str(k): dump_rat(v) for k, v in moments.items()},
        "direct_order_four": dump_rat(direct4),
        "basis_invariance": "PASS",
        "linear_base_value": dump_rat(scalar0),
        "linear_scaled_value": dump_rat(linear_scaled),
        "sewn_scaled_value": dump_rat(sewn_scaled),
        "homogeneity_gap": dump_rat(sewn_scaled - linear_scaled),
        "series_majorant": dump_rat(closed_majorant),
        "certificate_sha256": digest,
        "scope": "finite source sewing and exact obstruction; no xi pullback or RH claim",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps(verify(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
