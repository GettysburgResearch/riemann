#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
from fractions import Fraction
from pathlib import Path
from typing import Any

Interval = tuple[Fraction, Fraction]
MatrixI = list[list[Interval]]


def F(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("booleans are not numbers")
    if isinstance(x, int):
        return Fraction(x)
    if not isinstance(x, str):
        raise ValueError(f"expected rational string, got {type(x).__name__}")
    return Fraction(x)


def endpoint(e: dict[str, Any]) -> Fraction:
    if set(e) != {"mantissa", "exponent"}:
        raise ValueError("malformed dyadic endpoint")
    m = e["mantissa"]
    p = e["exponent"]
    if isinstance(m, bool) or isinstance(p, bool):
        raise ValueError("boolean endpoint")
    return Fraction(int(m)) * (Fraction(2) ** int(p))


def parse_iv(x: dict[str, Any]) -> Interval:
    lo = endpoint(x["lower"])
    hi = endpoint(x["upper"])
    if lo > hi:
        raise ValueError("reversed interval")
    return lo, hi


def iv(x: Fraction | int) -> Interval:
    q = Fraction(x)
    return q, q


def iadd(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def isub(a: Interval, b: Interval) -> Interval:
    return a[0] - b[1], a[1] - b[0]


def ineg(a: Interval) -> Interval:
    return -a[1], -a[0]


def imul(a: Interval, b: Interval) -> Interval:
    vals = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(vals), max(vals)


def idiv(a: Interval, b: Interval) -> Interval:
    if b[0] <= 0 <= b[1]:
        raise ValueError("division interval contains zero")
    reciprocal = (Fraction(1, b[1]), Fraction(1, b[0]))
    return imul(a, reciprocal)


def isquare(a: Interval) -> Interval:
    if a[0] >= 0:
        return a[0] * a[0], a[1] * a[1]
    if a[1] <= 0:
        return a[1] * a[1], a[0] * a[0]
    return Fraction(0), max(a[0] * a[0], a[1] * a[1])


def mat_add(A: MatrixI, B: MatrixI) -> MatrixI:
    return [[iadd(A[i][j], B[i][j]) for j in range(len(A))] for i in range(len(A))]


def mat_sub(A: MatrixI, B: MatrixI) -> MatrixI:
    return [[isub(A[i][j], B[i][j]) for j in range(len(A))] for i in range(len(A))]


def mat_scale(q: Fraction, A: MatrixI) -> MatrixI:
    return [[imul(iv(q), A[i][j]) for j in range(len(A))] for i in range(len(A))]


def mat_vec(A: MatrixI, x: list[int | Fraction]) -> list[Interval]:
    out: list[Interval] = []
    for row in A:
        s = iv(0)
        for a, b in zip(row, x):
            s = iadd(s, imul(a, iv(Fraction(b))))
        out.append(s)
    return out


def quad(A: MatrixI, x: list[int | Fraction], y: list[int | Fraction] | None = None) -> Interval:
    if y is None:
        y = x
    Ay = mat_vec(A, y)
    s = iv(0)
    for a, b in zip(x, Ay):
        s = iadd(s, imul(iv(Fraction(a)), b))
    return s


def compress(A: MatrixI, Y: list[list[int]]) -> MatrixI:
    n = len(A)
    k = len(Y[0])
    cols = [[Y[r][j] for r in range(n)] for j in range(k)]
    return [[quad(A, cols[i], cols[j]) for j in range(k)] for i in range(k)]


def interval_ldl(A: MatrixI, label: str) -> list[Interval]:
    n = len(A)
    L: list[list[Interval | None]] = [[None] * n for _ in range(n)]
    pivots: list[Interval] = []
    for i in range(n):
        for j in range(i):
            s = A[i][j]
            for k in range(j):
                assert L[i][k] is not None and L[j][k] is not None
                s = isub(s, imul(imul(L[i][k], L[j][k]), pivots[k]))
            L[i][j] = idiv(s, pivots[j])
        p = A[i][i]
        for k in range(i):
            assert L[i][k] is not None
            p = isub(p, imul(isquare(L[i][k]), pivots[k]))
        if p[0] <= 0:
            raise ValueError(f"{label}: nonpositive directed LDL pivot {i}: {p}")
        pivots.append(p)
        L[i][i] = iv(1)
    return pivots


def sqrt_upper(q: Fraction, bits: int = 512) -> Fraction:
    if q < 0:
        raise ValueError("negative square root")
    scaled_num = q.numerator << (2 * bits)
    scaled = (scaled_num + q.denominator - 1) // q.denominator
    root = math.isqrt(scaled)
    if root * root < scaled:
        root += 1
    return Fraction(root, 1 << bits)


def frac_s(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def iv_s(a: Interval) -> dict[str, str]:
    return {"lower": frac_s(a[0]), "upper": frac_s(a[1])}


def decimal(q: Fraction, digits: int = 30) -> str:
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole, rem = divmod(q.numerator, q.denominator)
    out = []
    for _ in range(digits):
        rem *= 10
        d, rem = divmod(rem, q.denominator)
        out.append(str(d))
    return f"{sign}{whole}." + "".join(out)


def verify(primitive: dict[str, Any], cfg: dict[str, Any]) -> dict[str, Any]:
    if primitive.get("schema") != "riemann.x18506.local-directed-source-canonical.v1":
        raise ValueError("wrong primitive schema")
    support = primitive["support"]
    if support.get("c") != cfg["support"]["c"] or support.get("N") != cfg["support"]["N"]:
        raise ValueError("support mismatch")
    if primitive.get("precision_bits", 0) < 512:
        raise ValueError("insufficient primitive precision")

    primitive_bytes = json.dumps(primitive, sort_keys=True, separators=(",", ":")).encode()
    semantic_primitive_sha = hashlib.sha256(primitive_bytes).hexdigest()

    d = support["N"] + 1
    diag = cfg["metric_diagonal"]
    if diag != primitive["metric_diagonal"] or len(diag) != d:
        raise ValueError("metric mismatch")
    G = [[iv(0) for _ in range(d)] for _ in range(d)]
    for i, x in enumerate(diag):
        if isinstance(x, bool) or x <= 0:
            raise ValueError("bad metric diagonal")
        G[i][i] = iv(x)

    P = [[parse_iv(primitive["P_even"][i][j]) for j in range(d)] for i in range(d)]
    E = [[parse_iv(primitive["E_even"][i][j]) for j in range(d)] for i in range(d)]
    A = mat_add(P, E)

    g = F(cfg["g"])
    Gamma = F(cfg["Gamma"])
    theta = F(cfg["theta"])
    if theta != g - Gamma or not (0 < Gamma < g):
        raise ValueError("inconsistent thresholds")
    D = mat_sub(mat_scale(g, G), A)
    D_pivots = interval_ldl(D, "complete positive deficit")

    Q0 = cfg["Q_0"]
    if Q0 != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
        raise ValueError("this production certificate requires Q_0=I")

    c = cfg["Y_C_center"]
    if len(c) != d or any(isinstance(x, bool) for x in c):
        raise ValueError("bad Y_C center")
    c0, c1, c2 = map(int, c)
    if c0 == 0:
        raise ValueError("Y_C center has zero first coordinate")
    YD = [[-2 * c1, -2 * c2], [c0, 0], [0, c0]]
    YC = [[c0], [c1], [c2]]

    GD_cross = compress(G, [[YD[r][0], YD[r][1], YC[r][0]] for r in range(d)])
    if GD_cross[0][2] != iv(0) or GD_cross[1][2] != iv(0):
        raise ValueError("center frames are not exactly G-orthogonal")

    high_center = compress(mat_sub(D, mat_scale(theta, G)), YD)
    high_pivots = interval_ldl(high_center, "high-deficit center LMI")
    low_center = quad(mat_sub(mat_scale(theta, G), D), c)
    if low_center[0] <= 0:
        raise ValueError("low-deficit center LMI is not strict")

    below_gamma = compress(mat_sub(mat_scale(Gamma, G), A), YD)
    below_gamma_pivots = interval_ldl(below_gamma, "A below Gamma on center complement")
    above_gamma = quad(mat_sub(A, mat_scale(Gamma, G)), c)
    if above_gamma[0] <= 0:
        raise ValueError("center Rayleigh quotient is not above Gamma")

    den = quad(G, c)
    rayleigh = idiv(quad(A, c), den)
    if rayleigh[0] <= Gamma:
        raise ValueError("Rayleigh gap is not strict")
    Ac = mat_vec(A, c)
    Gc = mat_vec(G, c)
    residual: list[Interval] = []
    for i in range(d):
        residual.append(isub(Ac[i], imul(rayleigh, Gc[i])))
    rho_num = iv(0)
    inv_diag = [Fraction(1, x) for x in diag]
    for ri, wi in zip(residual, inv_diag):
        rho_num = iadd(rho_num, imul(iv(wi), isquare(ri)))
    rho2 = idiv(rho_num, den)
    rho_upper = sqrt_upper(rho2[1])
    eta = rho_upper / (rayleigh[0] - Gamma)
    declared_eta = F(cfg["projector_radius"])
    if eta >= declared_eta:
        raise ValueError("projector enclosure radius too small")

    source = cfg["source_flag"]
    source_comp = cfg["source_complement"]
    if source != [[-2, -2], [1, 0], [0, 1]] or source_comp != [1, 1, 1]:
        raise ValueError("unexpected source flag")
    source_metric_cross = compress(G, [[source[r][0], source[r][1], source_comp[r]] for r in range(d)])
    if source_metric_cross[0][2] != iv(0) or source_metric_cross[1][2] != iv(0):
        raise ValueError("source split not G-orthogonal")
    source_deficit_cross = [quad(D, source_comp, [source[r][j] for r in range(d)]) for j in range(2)]
    if all(x[0] <= 0 <= x[1] for x in source_deficit_cross):
        raise ValueError("source/deficit non-invariance was not certified")

    canonical_floor = F(cfg["canonical_floor"])
    whole_floor_pivots = interval_ldl(mat_sub(A, mat_scale(canonical_floor, G)), "canonical direct-short floor")
    safe_floor = F(cfg["safe_floor"])
    safe_center = quad(mat_sub(A, mat_scale(safe_floor, G)), c)
    if safe_center[0] <= 0:
        raise ValueError("safe spectral complement floor not certified")

    cGc = den[0]
    if den[0] != den[1]:
        raise ValueError("metric norm of rational center should be exact")
    P_C_center = [[Fraction(c[i]) * Fraction(c[j]) * Fraction(diag[j], 1) / cGc for j in range(d)] for i in range(d)]
    P_D_center = [[(Fraction(1) if i == j else Fraction(0)) - P_C_center[i][j] for j in range(d)] for i in range(d)]

    result = {
        "schema": "riemann.x18509.complete-finite-spectral-deficit.result.v1",
        "support": cfg["support"],
        "classification": "CERTIFIED_SOURCE_NOT_CANONICAL_TRUE_DEFICIT_PACKET_DIRECT_SHORT_POSITIVE",
        "lower_model": {
            "identity": "A = g G - D",
            "g": frac_s(g),
            "Gamma": frac_s(Gamma),
            "theta": frac_s(theta),
            "Q_0": Q0,
            "D_positive_ldl_pivots": [iv_s(x) for x in D_pivots],
        },
        "source_flag": {
            "Y_S": source,
            "G_orthogonal_complement": source_comp,
            "D_cross": [iv_s(x) for x in source_deficit_cross],
            "equals_deficit_canonical": False,
        },
        "canonical_projector": {
            "definition": "P_D = 1_(theta,infinity)(G^(-1/2) D G^(-1/2)); P_C=I-P_D",
            "rank_P_D": 2,
            "rank_P_C": 1,
            "Y_D_center": YD,
            "Y_C_center": c,
            "P_D_center": [[frac_s(x) for x in row] for row in P_D_center],
            "P_C_center": [[frac_s(x) for x in row] for row in P_C_center],
            "G_operator_radius": frac_s(declared_eta),
            "computed_radius_upper": frac_s(eta),
            "rayleigh_interval": iv_s(rayleigh),
            "residual_norm_squared_interval": iv_s(rho2),
            "high_center_ldl_pivots": [iv_s(x) for x in high_pivots],
            "low_center_quadratic": iv_s(low_center),
            "below_Gamma_center_ldl_pivots": [iv_s(x) for x in below_gamma_pivots],
            "strict_gap": {
                "lambda_2_upper": frac_s(Gamma),
                "lambda_3_lower_from_center_rayleigh": frac_s(rayleigh[0]),
                "deficit_high_lower_strict": frac_s(theta),
                "deficit_low_upper_strict": frac_s(g - safe_floor),
            },
        },
        "direct_short": {
            "canonical_packet_floor": frac_s(canonical_floor),
            "canonical_packet_floor_ldl_pivots": [iv_s(x) for x in whole_floor_pivots],
            "safe_complement_floor": frac_s(safe_floor),
            "safe_center_quadratic": iv_s(safe_center),
            "exact_cross": "0 by spectral invariance of P_D and P_C",
            "trial_solve": "X=0",
            "residual": "0",
            "Delta": "0",
        },
        "primitive": {
            "file_sha256_expected": cfg["primitive_sha256"],
            "semantic_sha256": semantic_primitive_sha,
            "producer_sha256": cfg["producer_sha256"],
        },
    }
    digest_payload = copy.deepcopy(result)
    digest = hashlib.sha256(json.dumps(digest_payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    result["proof_object_sha256"] = digest
    result["display"] = {
        "rayleigh_lower": decimal(rayleigh[0], 36),
        "projector_radius_upper": decimal(eta, 60),
        "source_cross_0": decimal(source_deficit_cross[0][0], 36),
        "source_cross_1": decimal(source_deficit_cross[1][0], 36),
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("primitive", type=Path)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    primitive_bytes = args.primitive.read_bytes()
    cfg = json.loads(args.config.read_text())
    actual_sha = hashlib.sha256(primitive_bytes).hexdigest()
    if actual_sha != cfg["primitive_sha256"]:
        raise SystemExit(f"primitive file SHA mismatch: {actual_sha}")
    primitive = json.loads(primitive_bytes)
    result = verify(primitive, cfg)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
