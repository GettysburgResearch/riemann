#!/usr/bin/env python3
"""Exact algebra replay for T-105220.

This checker authenticates:
  * the three-height positive localizer partial fraction identity;
  * the common boundary weights and mass;
  * first-order and Bell-correction cancellation in the formal coherence defect;
  * the exact quartic debt firewall;
  * the elementary theta growth exponents.

It does not authenticate the analytic Stirling/Bell asymptotics or prove RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Tuple

Monomial = Tuple[int, ...]
Poly = Dict[Monomial, F]
Series = Dict[int, Poly]

VARS = ("D", "Q", "Q2", "R", "k")
NV = len(VARS)


def pconst(x: F | int) -> Poly:
    x = F(x)
    return {} if x == 0 else {(0,) * NV: x}


def pvar(i: int) -> Poly:
    e = [0] * NV
    e[i] = 1
    return {tuple(e): F(1)}


def padd(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, F(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def pneg(a: Poly) -> Poly:
    return {m: -c for m, c in a.items()}


def psub(a: Poly, b: Poly) -> Poly:
    return padd(a, pneg(b))


def pmul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, F(0)) + ca * cb
    return {m: c for m, c in out.items() if c}


def pscale(a: Poly, q: F | int) -> Poly:
    q = F(q)
    return {m: q * c for m, c in a.items() if q * c}


def smul(a: Series, b: Series) -> Series:
    out: Series = {}
    for ea, pa in a.items():
        for eb, pb in b.items():
            e = ea + eb
            out[e] = padd(out.get(e, {}), pmul(pa, pb))
    return {e: p for e, p in out.items() if p}


def ssub(a: Series, b: Series) -> Series:
    out = dict(a)
    for e, p in b.items():
        out[e] = padd(out.get(e, {}), pneg(p))
        if not out[e]:
            del out[e]
    return out


def omega_u(u: F) -> F:
    return F(36) / ((u + 1) * (u + 4) * (u + 9))


def verify() -> dict:
    def mul2(a: Tuple[F, ...], b: Tuple[F, ...]) -> Tuple[F, ...]:
        out = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return tuple(out)

    rhs = [F(0), F(0), F(0)]
    terms = [
        (F(3, 2), mul2((F(4), F(1)), (F(9), F(1)))),
        (F(-12, 5), mul2((F(1), F(1)), (F(9), F(1)))),
        (F(9, 10), mul2((F(1), F(1)), (F(4), F(1)))),
    ]
    for c, poly in terms:
        for i, v in enumerate(poly):
            rhs[i] += c * v
    assert tuple(rhs) == (F(36), F(0), F(0))

    d = (F(3, 2), F(-6, 5), F(3, 10))
    Dmass = sum(d, F(0))
    assert Dmass == F(3, 5)

    D, Q, Q2, R, k = (pvar(i) for i in range(NV))
    one = pconst(1)
    n1 = pmul(k, R)
    m3 = psub(Q2, pmul(psub(k, one), R))
    m5 = padd(pscale(Q2, 6), pmul(psub(pconst(2), pscale(k, 3)), R))

    N = {-1: D, 0: Q, 1: n1}
    A = {1: D, 2: pneg(Q), 3: m3}
    B = {3: D, 4: pscale(Q, -3), 5: m5}
    defect = ssub(smul(N, B), smul(A, A))

    assert defect.get(2, {}) == {}
    assert defect.get(3, {}) == {}

    target4 = pscale(psub(pmul(D, Q2), pmul(Q, Q)), 4)
    assert defect.get(4, {}) == target4

    N_actual = omega_u(F(0)) + 2 * omega_u(F(5, 2))
    A_actual = -(
        omega_u(F(0)) * F(-1, 5)
        + 2 * omega_u(F(5, 2)) * F(-17, 80)
    )
    B_actual = (
        omega_u(F(0)) * F(1, 25)
        + 2 * omega_u(F(5, 2)) * F(289, 6400)
    )
    debt = 2 * omega_u(F(5, 6)) * F(-2809, 172800)
    B_raw = B_actual + debt

    assert N_actual == F(2669, 2093)
    assert A_actual == F(541, 2093)
    assert B_actual == F(10973, 209300)
    assert debt == F(-25281, 1882100)
    assert B_raw == F(1536097, 39392353)

    C_actual = A_actual * A_actual / (N_actual * B_actual)
    C_raw = A_actual * A_actual / (N_actual * B_raw)
    assert C_actual == F(29268100, 29286937)
    assert C_actual < 1
    assert C_raw == F(5508549101, 4099842893)
    assert C_raw > 1

    core_floor = omega_u(F(1))
    assert core_floor == F(9, 25)

    q0 = F(11, 2)
    assert F(4) - q0 == F(-3, 2)

    payload = {
        "schema": "riemann.x105220.multipole_poisson.v1",
        "classification": "PASS_T105220_MULTIPOLE_POISSON_SAFE_LINE_ALGEBRA",
        "arithmetic": "EXACT_RATIONAL_AND_FORMAL_POLYNOMIAL",
        "verified": {
            "positive_kernel_partial_fraction": True,
            "boundary_mass": str(Dmass),
            "formal_first_order_cancellation": True,
            "formal_second_order_defect": "4*(D*Q2-Q^2)",
            "quartic_debt_firewall": True,
            "unit_core_weight_floor": str(core_floor),
            "theta_growth_exponent": str(F(4) - q0),
        },
        "fixtures": {
            "quartic": "x^4-5x^2+2",
            "actual_coherence": str(C_actual),
            "raw_coherence": str(C_raw),
            "weighted_debt": str(debt),
        },
        "analytic_safe_line_asymptotics_replayed": False,
        "entire_bezout_interpolation_proved": False,
        "nonreal_correction_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = verify()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
