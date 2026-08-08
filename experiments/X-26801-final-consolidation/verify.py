#!/usr/bin/env python3
"""Exact consolidation checks for PR #268.

Standard library only. Verifies the positive inverse/source convolution,
formal renewal algebra, and the exact X=4 counterexample bounds used in
R-26801. It does not prove BCP, F5PBT, Landau's analytic hypotheses, or RH.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib, json
from pathlib import Path

MAX_N = 128


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x=n; p=2; sign=1
    while p*p<=x:
        if x%p==0:
            x//=p; sign=-sign
            if x%p==0:
                return 0
            while x%p==0:
                x//=p
        p += 1 if p==2 else 2
    if x>1: sign=-sign
    return sign


def divisors(n: int):
    return [d for d in range(1,n+1) if n%d==0]


def omega(n: int) -> Fraction:
    out=Fraction(mobius(n))
    if n%2==0:
        out -= Fraction(3,2)*mobius(n//2)
    if n%4==0:
        out += Fraction(1,2)*mobius(n//4)
    return out


def aomega(n: int) -> Fraction:
    v=0
    while n%2==0:
        n//=2; v+=1
    return Fraction(2*v,1)+Fraction(1,2**v)


def conv(f,g,n):
    return sum((f(d)*g(n//d) for d in divisors(n)), Fraction(0))


def main():
    inverse_rows=0
    for n in range(1,MAX_N+1):
        got=conv(aomega,omega,n)
        want=Fraction(1 if n==1 else 0)
        assert got==want,(n,got,want)
        inverse_rows += 1

    # Mutation controls: each altered sibling must break inverse convolution.
    def om_drop4(n):
        out=Fraction(mobius(n))
        if n%2==0: out-=Fraction(3,2)*mobius(n//2)
        return out
    def om_wrong2(n):
        out=Fraction(mobius(n))
        if n%2==0: out-=mobius(n//2)
        if n%4==0: out+=Fraction(1,2)*mobius(n//4)
        return out
    mutations=0
    for bad in (om_drop4,om_wrong2):
        assert any(conv(aomega,bad,n)!=(1 if n==1 else 0) for n in range(1,33))
        mutations += 1

    # Exact rational bounds used to prove R_tilde_omega(4)<0.
    # sqrt(2)<99/70 and sqrt(3)<26/15.
    assert 99*99 > 2*70*70
    assert 26*26 > 3*15*15
    # These imply sqrt(3)*(2-5/(2sqrt(2))) < 598/1485 < 41/100.
    assert Fraction(598,1485) < Fraction(41,100)
    # log(4/3)/log(2)>41/100 iff 2^159>3^100.
    assert 2**159 > 3**100
    # Independent elementary proof of the last integer inequality:
    # (256/243)^20 > 1+20*(13/243)>2.
    assert Fraction(256,243)**20 > 1 + 20*Fraction(13,243) > 2

    script=Path(__file__).read_bytes()
    script_sha=hashlib.sha256(script).hexdigest()
    result={
        "schema":"X-26801-final-consolidation-v1",
        "classification":"EXACT_FINAL_CONSOLIDATION_FIREWALLS_VERIFIED",
        "max_n":MAX_N,
        "positive_inverse_convolution_rows":inverse_rows,
        "mutations_rejected":mutations,
        "x4_counterexample":"inclusive dyadic renewal state is strictly negative",
        "integer_log_comparison":"2^159 > 3^100",
        "proof_boundary":"exact finite algebra and rational/integer inequalities only; BCP, F5PBT, Landau transfer, and RH remain unproved",
        "verifier_sha256":script_sha,
    }
    out=Path(__file__).parent/'results'/'verification.json'
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__': main()
