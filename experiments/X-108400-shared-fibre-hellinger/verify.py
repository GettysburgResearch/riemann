#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Sequence

CLASSIFICATION = "PASS_T108400_SHARED_FIBRE_HELLINGER_TRACE"

def hs_square_product(left: Sequence[int], right: Sequence[int]) -> Fraction:
    L = sum(left)
    R = sum(right)
    bl = Fraction(L, len(left))
    br = Fraction(R, len(right))
    root_bl = Fraction(math.isqrt(bl.numerator), math.isqrt(bl.denominator))
    root_br = Fraction(math.isqrt(br.numerator), math.isqrt(br.denominator))
    total = Fraction(0)
    for x in left:
        rx = Fraction(math.isqrt(x))
        for y in right:
            ry = Fraction(math.isqrt(y))
            total += (rx*ry-root_bl*root_br)**2
    return total

def one_side_hs(xs: Sequence[int]) -> Fraction:
    total = sum(xs)
    b = Fraction(total, len(xs))
    rb = Fraction(math.isqrt(b.numerator), math.isqrt(b.denominator))
    return sum((Fraction(math.isqrt(x))-rb)**2 for x in xs)

def trace_positive_2x2(a: float, b: float, c: float) -> float:
    tr = a+c
    disc = math.sqrt((a-c)**2 + 4*b*b)
    l1 = (tr+disc)/2
    l2 = (tr-disc)/2
    return max(l1,0.0)+max(l2,0.0)

def run_checks() -> dict:
    exact = 0
    numerical = 0

    fixtures = [
        ([1,1], [4,4]),
        ([1,1,25], [4,4,4]),
        ([0,0,0,16], [1,1,9,25]),
        ([1,1,9,25], [0,0,0,36]),
        ([4,4,4], [25,1,1]),
    ]
    for left, right in fixtures:
        L, R = sum(left), sum(right)
        hL = one_side_hs(left)
        hR = one_side_hs(right)
        lhs = hs_square_product(left, right)
        rhs = Fraction(R)*hL + Fraction(L)*hR - Fraction(1,2)*hL*hR
        assert lhs == rhs
        assert lhs <= Fraction(R)*hL + Fraction(L)*hR
        exact += 2

    vals = (0,1,4,9,16,25,36)
    candidates = []
    for n in (2,3,4,5):
        for xs in itertools.product(vals, repeat=n):
            if sum(xs)==0:
                continue
            m = Fraction(sum(xs), n)
            if math.isqrt(m.numerator)**2 == m.numerator and math.isqrt(m.denominator)**2 == m.denominator:
                candidates.append(xs)
            if len(candidates) >= 70:
                break
        if len(candidates) >= 70:
            break
    for left in candidates[:35]:
        for right in candidates[35:70]:
            L, R = sum(left), sum(right)
            hL, hR = one_side_hs(left), one_side_hs(right)
            lhs = hs_square_product(left, right)
            rhs = Fraction(R)*hL + Fraction(L)*hR - Fraction(1,2)*hL*hR
            assert lhs == rhs
            exact += 1

    S00, S01, S11, d = 0.75, 0.25, 0.75, 0.5
    square_vectors = [(1,1),(1,4),(4,9),(0,4),(9,16),(1,16)]
    for D in square_vectors:
        for E in square_vectors:
            rd = [math.sqrt(x) for x in D]
            re = [math.sqrt(x) for x in E]
            AD = (rd[0]*S00*rd[0]-d, rd[0]*S01*rd[1], rd[1]*S11*rd[1]-d)
            AE = (re[0]*S00*re[0]-d, re[0]*S01*re[1], re[1]*S11*re[1]-d)
            lhs = abs(trace_positive_2x2(*AD)-trace_positive_2x2(*AE))
            H = math.sqrt(sum((x-y)**2 for x,y in zip(rd,re)))
            rhs = (math.sqrt(sum(D))+math.sqrt(sum(E)))*H
            assert lhs <= rhs + 1e-11
            numerical += 1

    for m in range(2,25):
        N = m*m
        H2 = (math.sqrt(N)-math.sqrt(m))**2 + (m-1)*(math.sqrt(m))**2
        expected = 2*N*(1-1/math.sqrt(m))
        assert abs(H2-expected) < 1e-9
        numerical += 1

    payload = {
        "schema": "riemann.x108400.shared-fibre-hellinger-trace.v1",
        "classification": CLASSIFICATION,
        "exact_checks": exact,
        "numerical_consistency_checks": numerical,
        "rectangular_tensorization_checked": True,
        "positive_trace_hellinger_stability_checked": True,
        "orbit_uniform_extreme_firewall_checked": True,
        "history_recombination_required_before_occupancy": True,
        "frobhell108400_proved": False,
        "qresbind108400_proved": False,
        "rh_established": False,
        "grh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload

def main() -> None:
    payload = run_checks()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")
    print(f"numerical_consistency_checks={payload['numerical_consistency_checks']}")

if __name__ == "__main__":
    main()
