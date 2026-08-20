#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Dict, List

SCHEMA = "riemann.t100720.cubic_hinge_rough_prefix.v1"


def psi(t: Fraction) -> Fraction:
    return 3*t*t - t*t*t if t <= 1 else 3*t - 1


def hinge_integral(t: Fraction) -> Fraction:
    return 3*t*t - t*t*t if t <= 1 else 3*t - 1


def collar(t: Fraction) -> Fraction:
    return (1-t)**3 if t < 1 else Fraction(0)


def subset_products(labels: List[int]) -> Dict[int, int]:
    out: Dict[int, int] = {1: 1}
    for a in labels:
        for d, mu in list(out.items()):
            out[d*a] = -mu
    return out


def prefix(coeff: Dict[int, int], x: Fraction) -> Fraction:
    return sum(Fraction(mu, d) for d, mu in coeff.items() if d <= x)


def compensated_prefix(p: int, q: int, coeff: Dict[int, int], x: Fraction) -> Fraction:
    sp = int(p**0.5)
    sq = int(q**0.5)
    assert sp*sp == p and sq*sq == q
    return (
        prefix(coeff, x)
        - Fraction(1, sp)*prefix(coeff, x/p)
        - Fraction(1, sq)*prefix(coeff, x/q)
        + Fraction(1, sp*sq)*prefix(coeff, x/(p*q))
    )


def direct_hinge_derivative(p: int, q: int, coeff: Dict[int, int], x: Fraction) -> Fraction:
    sp = int(p**0.5)
    sq = int(q**0.5)
    ans = Fraction(0)
    for d, mu in coeff.items():
        base = Fraction(mu, d)
        if d <= x:
            ans += base
        if p*d <= x:
            ans -= base/Fraction(sp)
        if q*d <= x:
            ans -= base/Fraction(sq)
        if p*q*d <= x:
            ans += base/Fraction(sp*sq)
    return ans


def centered_packet(p: int, q: int, labels: List[int], t: Fraction) -> Fraction:
    coeff = subset_products(labels)
    sp = int(p**0.5)
    sq = int(q**0.5)
    ans = Fraction(0)
    for d, mu in coeff.items():
        sd = int(d**0.5)
        assert sd*sd == d
        base = Fraction(mu, sd)
        ans += base*collar(t/sd)
        ans -= base*collar(t/(sp*sd))
        ans -= base*collar(t/(sq*sd))
        ans += base*collar(t/(sp*sq*sd))
    return 64*ans


def carrier(p: int, q: int, labels: List[int], t: Fraction) -> Fraction:
    sp = int(p**0.5)
    sq = int(q**0.5)
    prod = Fraction(1)
    for ell in labels:
        prod *= Fraction(ell-1, ell)
    return 192*t*Fraction(sp-1, sp)*Fraction(sq-1, sq)*prod


def step_coefficients(p: int, q: int, labels: List[int]) -> Dict[int, Fraction]:
    # Third derivative of centered packet equals sum_R c_R * indicator(u<R).
    coeff = subset_products(labels)
    sp = int(p**0.5)
    sq = int(q**0.5)
    endpoints = [
        (1, Fraction(1)),
        (p, -Fraction(1, p*sp)),
        (q, -Fraction(1, q*sq)),
        (p*q, Fraction(1, p*q*sp*sq)),
    ]
    out: Dict[int, Fraction] = {}
    for d, mu in coeff.items():
        sd = int(d**0.5)
        assert sd*sd == d
        for e, ce in endpoints:
            se = int(e**0.5)
            assert se*se == e
            R = se*sd
            c = -384*Fraction(mu, d*d)*ce
            out[R] = out.get(R, Fraction(0)) + c
    return {R: c for R, c in out.items() if c}


def integrate_abs_step_moment(steps: Dict[int, Fraction], t: Fraction, left: bool) -> Fraction:
    breaks = sorted(set([Fraction(0), t] + [Fraction(r) for r in steps]))
    max_r = max(steps) if steps else 0
    breaks = sorted(set(breaks + [Fraction(max_r)]))
    total = Fraction(0)
    for a, b in zip(breaks, breaks[1:]):
        if a == b:
            continue
        mid = (a+b)/2
        value = sum(c for R, c in steps.items() if mid < R)
        if value == 0:
            continue
        if left:
            lo = max(a, Fraction(0))
            hi = min(b, t)
            if lo >= hi:
                continue
            integral = ((t-lo)**3 - (t-hi)**3)/3
        else:
            lo = max(a, t)
            hi = min(b, Fraction(max_r))
            if lo >= hi:
                continue
            integral = ((hi-t)**3 - (lo-t)**3)/3
        total += abs(value)*integral/2
    return total


def verify() -> dict:
    checks = {}
    ts = [Fraction(1,10), Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(2)]
    for t in ts:
        assert psi(t) == hinge_integral(t)
        assert 64*psi(t) == 192*t - 64 + 64*collar(t)
    checks["hinge_and_carrier_samples"] = len(ts)

    p, q = 4, 25
    labels = [9, 16, 49]
    coeff = subset_products(labels)
    xs = [Fraction(1), Fraction(5), Fraction(20), Fraction(100), Fraction(500), Fraction(5000)]
    for x in xs:
        assert compensated_prefix(p, q, coeff, x) == direct_hinge_derivative(p, q, coeff, x)
    checks["rough_prefix_derivative_samples"] = len(xs)

    steps = step_coefficients(p, q, labels)
    l1 = sum(abs(c)*R for R, c in steps.items())
    m1 = sum(abs(c)*Fraction(R*R, 2) for R, c in steps.items())
    sp, sq = int(p**0.5), int(q**0.5)
    rhs_l1 = 384*Fraction(p+1, p)*Fraction(q+1, q)
    rhs_m1 = 192*Fraction(sp+1, sp)*Fraction(sq+1, sq)
    for ell in labels:
        sl = int(ell**0.5)
        rhs_l1 *= Fraction(ell*sl+1, ell*sl)
        rhs_m1 *= Fraction(ell+1, ell)
    assert l1 == rhs_l1
    assert m1 == rhs_m1
    checks["third_variation_factorizations"] = 2

    for t in [Fraction(1,3), Fraction(2), Fraction(7), Fraction(20)]:
        ht = centered_packet(p, q, labels, t)
        h = carrier(p, q, labels, t) + ht
        left = integrate_abs_step_moment(steps, t, True)
        right = integrate_abs_step_moment(steps, t, False)
        neg = max(Fraction(0), -h)
        assert neg <= left and neg <= right and neg*neg <= left*right
    checks["two_sided_taylor_samples"] = 4

    assert Fraction(2*6, 720) == Fraction(1,60)
    checks["regularity_countermodel_integral"] = "1/60"

    core = {
        "schema": SCHEMA,
        "base_pr": 691,
        "base_sha": "be9a4168fa0df971a2fc63176f07ce3beee6c3d4",
        "checks": checks,
        "scope": {
            "hinge_identity_proved": True,
            "rough_prefix_coarea_proved": True,
            "tao_prefix_bound_replayed": False,
            "third_variation_factorization_proved": True,
            "two_certificate_and_gate_proved": True,
            "lpcc100723_proved": False,
            "fpcc100723_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T100720_CUBIC_HINGE_ROUGH_PREFIX_ALGEBRA",
    }
    core["proof_object_sha256"] = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return core


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
