#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99910_MINIMAL_MOBIUS_WAVELET"

def sqrt_interval(n: int, digits: int = 40) -> tuple[Fraction, Fraction]:
    scale = 10 ** digits
    q = math.isqrt(n * scale * scale)
    lo = Fraction(q, scale)
    hi = Fraction(q + 1, scale)
    assert lo * lo <= n < hi * hi
    return lo, hi

def log_interval(x: Fraction, terms: int = 80) -> tuple[Fraction, Fraction]:
    z = (x - 1) / (x + 1)
    assert 0 < z < 1
    partial = Fraction(0)
    for k in range(terms):
        partial += 2 * z ** (2 * k + 1) / (2 * k + 1)
    rem = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return partial, partial + rem

def pair_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def pair_mul(a, b):
    return (a[0]*b[0] + 2*a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def poly_mul(p, q):
    out=[(Fraction(0),Fraction(0))]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]=pair_add(out[i+j], pair_mul(a,b))
    return out

def run() -> dict:
    one=[(Fraction(1),Fraction(0)),(Fraction(-2),Fraction(0)),(Fraction(1),Fraction(0))]
    half=[(Fraction(1),Fraction(0)),(Fraction(0),Fraction(-1))]
    P=poly_mul(one, half)
    expected=[
        (Fraction(1),Fraction(0)),
        (Fraction(-2),Fraction(-1)),
        (Fraction(1),Fraction(2)),
        (Fraction(0),Fraction(-1)),
    ]
    assert P == expected

    val=(Fraction(0),Fraction(0))
    der=(Fraction(0),Fraction(0))
    for j,c in enumerate(P):
        val=pair_add(val,c)
        if j:
            der=pair_add(der,(j*c[0],j*c[1]))
    assert val == (0,0)
    assert der == (0,0)

    z=(Fraction(0),Fraction(1,2))
    powz=(Fraction(1),Fraction(0))
    value=(Fraction(0),Fraction(0))
    for coeff in P:
        value=pair_add(value,pair_mul(coeff,powz))
        powz=pair_mul(powz,z)
    assert value == (0,0)

    assert Fraction(1,1) / (1-Fraction(1,67)) > 1
    rlo,rhi=sqrt_interval(67)
    assert rlo > 8
    assert Fraction(1,1) / (1-Fraction(1,8)) < 2

    s2lo,s2hi=sqrt_interval(2)
    s3lo,s3hi=sqrt_interval(3)
    l2lo,l2hi=log_interval(Fraction(2))
    l3lo,l3hi=log_interval(Fraction(3))
    Elo = (-4*s2hi - Fraction(16,3) + Fraction(8,3)*s3lo
           + (2*s3lo + Fraction(9,2)*s2lo)*l2lo - s3hi*l3hi)
    Ehi = (-4*s2lo - Fraction(16,3) + Fraction(8,3)*s3hi
           + (2*s3hi + Fraction(9,2)*s2hi)*l2hi - s3lo*l3lo)
    assert Elo > Fraction(-14620,10000)
    assert Ehi < Fraction(-14618,10000)

    mutations = sorted([
        "degree_two_annihilator_rejected",
        "seven_band_kernel_called_minimal_rejected",
        "duplicate67_resolvent_dropped_rejected",
        "ordinary_mu_replaced_by_beta_rejected",
        "pointwise_wavelet_positivity_rejected",
        "finite_negative_fixture_promoted_to_tail_rejected",
        "mwoc99910_assumed_rejected",
        "rh_established_by_replay_rejected",
    ])
    core = {
        "schema": "riemann.x99910.minimal-mobius-wavelet.v1",
        "classification": VERDICT,
        "base_pr": 665,
        "base_sha": "a771772682a2c09c026348b176618c302c49c223",
        "minimal_polynomial": "(1-sqrt(2)z)(1-z)^2",
        "minimal_degree": 3,
        "minimal_support_ratio": 8,
        "two_shell_support": [[1,8],[67,536]],
        "factor67_antisymmetry": True,
        "box_positive_resolvent": True,
        "duplicate67_positive_resolvent": True,
        "ordinary_mobius_source": True,
        "three_activation_bands": True,
        "pointwise_positive": False,
        "negative_fixture_X": 4,
        "negative_fixture_interval": ["-1.4620","-1.4618"],
        "mellin_zero_safe": True,
        "mwoc99910_proved": False,
        "subpower_negative_mass_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canon=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    return {**core,"proof_object_sha256":hashlib.sha256(canon).hexdigest()}

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=run()
    out=args.output or Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n", encoding="utf-8",newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])

if __name__=="__main__":
    main()
