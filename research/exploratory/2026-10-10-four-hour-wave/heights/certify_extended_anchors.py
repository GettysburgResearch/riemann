#!/usr/bin/env python3
"""Directed low critical-pair endpoint signs, with a placement-only zero finder.

Requires python-flint==0.9.0. The acb.zeta_zero routine chooses short rational
intervals; only the independently evaluated strict Hardy-Z endpoint signs
and disjointness establish the existence used by the Pick theorem.
"""
from __future__ import annotations

import argparse
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import acb, arb, ctx


def exact_json(value: Q) -> int | str:
    return value.numerator if value.denominator == 1 else str(value)


def hardy_z(t: Q):
    value = arb(t.numerator) / t.denominator
    theta = acb(arb(1)/4, value/2).lgamma().imag
    theta -= value/2 * arb.pi().log()
    return acb(arb(1)/2, value).zeta() * acb(0,theta).exp()


def certificate(precision: int, count: int = 48, mesh: int = 16) -> dict:
    if precision < 96 or not 1 <= count <= 64 or mesh < 1:
        raise ValueError("Expected precision>=96, 1<=count<=64, positive mesh")
    ctx.prec = precision
    anchors = []
    endpoint_records = []
    previous_right = Q(0)
    for j in range(1,count+1):
        # Placement only: no mathematical conclusion depends on this float.
        approximate_t = float(acb.zeta_zero(j).imag)
        left = Q(int(approximate_t * mesh),mesh)
        right = left+Q(1,mesh)
        if left <= previous_right:
            raise RuntimeError("Placement intervals are not disjoint")
        previous_right = right
        pair_signs = []
        for t in (left,right):
            value = hardy_z(t)
            sign = 1 if value.real > 0 else -1 if value.real < 0 else 0
            if sign == 0 or not value.imag.contains(0):
                raise RuntimeError(f"Uncertified real Hardy-Z endpoint at {t}")
            pair_signs.append(sign)
            endpoint_records.append({"t":exact_json(t),"sign":sign,
                                     "real_enclosure":str(value.real),
                                     "imaginary_enclosure":str(value.imag)})
        if pair_signs[0] == pair_signs[1]:
            raise RuntimeError(f"No sign change in placement interval {left},{right}")
        anchors.append((left,right))

    xi_half = -(arb(1)/8) * (-(arb(1)/4)*arb.pi().log()).exp()
    xi_half *= (arb(1)/4).gamma()
    xi_half *= (arb(1)/2).zeta()
    if not xi_half > arb(1)/4:
        raise RuntimeError("xi(1/2)>1/4 was not certified")
    return {"status":"DIRECTED_INTERVAL_ENDPOINT_CERTIFICATE",
            "python":platform.python_version(),"python_flint":flint.__version__,
            "precision_bits":precision,"mesh":mesh,
            "placement":"acb.zeta_zero finder and binary-float floor; existence uses endpoint signs only",
            "endpoints":endpoint_records,
            "critical_ordinate_intervals":[[exact_json(a),exact_json(b)] for a,b in anchors],
            "critical_squared_ordinate_intervals":[[exact_json(a*a),exact_json(b*b)] for a,b in anchors],
            "xi_half":{"real_enclosure":str(xi_half),"proved_strict_lower_bound":"1/4"},
            "scope":"Distinct low critical pairs, multiplicity>=1; no simplicity/completeness or high-zero replay"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=256)
    parser.add_argument("--count",type=int,default=48)
    parser.add_argument("--mesh",type=int,default=16)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    result = certificate(args.precision,args.count,args.mesh)
    rendered = json.dumps(result,indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered,end="")


if __name__ == "__main__":
    main()
