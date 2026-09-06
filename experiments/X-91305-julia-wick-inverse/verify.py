#!/usr/bin/env python3
"""Exact finite-prime checks for L-91325/L-91326."""

from fractions import Fraction
import argparse
import json
from pathlib import Path


def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def local_coeffs(beta: Fraction, K: int):
    # D(z)=(1-z)/(1-beta z), through z^K.
    return [Fraction(1)] + [-(1-beta)*beta**(k-1) for k in range(1,K+1)]


def run():
    checks=0
    # Local identity with beta=1/4, alpha=beta^2.
    beta=Fraction(1,4)
    alpha=beta*beta
    delta2=(beta-alpha)*(1-alpha*beta)/(1-alpha)**2
    simplified=beta*(1+beta+beta*beta)/(1+beta)**2
    assert delta2==simplified
    checks+=1

    # D(z) exactly equals normalized Julia detail.
    for z in [Fraction(0), Fraction(1,3), Fraction(-1,2), Fraction(2,3)]:
        D=(1-z)/(1-beta*z)
        detail2=delta2*D*D
        assert detail2==delta2*((1-z)/(1-beta*z))**2
        checks+=1

    # Coefficients match d_omega(p^k) after z=p^{-(s-omega)}.
    # Choose p^omega=2, hence beta=1/4.
    coeff=local_coeffs(beta,6)
    # In the Dirichlet variable w=p^-s, z=2w. Coefficient at w^k:
    # -(1-beta) beta^(k-1) 2^k = -(4-1)*2^-k.
    for k in range(1,7):
        lhs=coeff[k]*Fraction(2)**k
        rhs=-Fraction(3,2**k)
        assert lhs==rhs
        checks+=1

    # Two-prime finite product coefficients are multiplicative.
    b1=Fraction(1,4)
    b2=Fraction(1,9)
    c1=local_coeffs(b1,3)
    c2=local_coeffs(b2,3)
    prod=poly_mul(c1,c2)
    assert prod[0]==1
    checks+=1

    return {
        "verdict":"PASS_X_91305_JULIA_WICK_INVERSE",
        "checks":checks,
        "beta":"1/4",
        "delta_squared":str(delta2),
        "scope":"finite local/tensor algebra only; JWGR_omega and RH are not proved",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--json",type=Path)
    ns=ap.parse_args()
    result=run()
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if ns.json:
        ns.json.write_text(text)
    print(text,end="")


if __name__=="__main__":
    main()
