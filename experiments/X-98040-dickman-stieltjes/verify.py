#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

VERDICT = "PASS_T98040_DICKMAN_STIELTJES_CORRIDOR"


def mobius_squarefree(n: int) -> int:
    x=n; s=1; p=2
    while p*p<=x:
        if x%p==0:
            x//=p; s=-s
            if x%p==0: return 0
            while x%p==0: x//=p
        p += 1 if p==2 else 2
    if x>1: s=-s
    return s


def rough_prefix(t: Fraction, z: int) -> Fraction:
    total=Fraction(0)
    for m in range(1, int(t)+1):
        mu=mobius_squarefree(m)
        if not mu: continue
        x=m; least=None; p=2
        while p*p<=x:
            if x%p==0:
                least=p; break
            p += 1 if p==2 else 2
        if least is None and x>1: least=x
        if m==1 or least>=z: total += Fraction(mu,m)
    return total


def exact_stieltjes_fixture() -> bool:
    # h(x) has jumps 3/5 at x=2, -1/7 at x=3, 2/9 at x=5.
    jumps=[(2,Fraction(3,5)),(3,Fraction(-1,7)),(5,Fraction(2,9))]
    Y=Fraction(120); z=5
    direct=Fraction(0)
    for m in range(1,121):
        mu=mobius_squarefree(m)
        if not mu: continue
        x=m; least=None; p=2
        while p*p<=x:
            if x%p==0: least=p; break
            p += 1 if p==2 else 2
        if least is None and x>1: least=x
        if m!=1 and least<z: continue
        h=sum((c for q,c in jumps if Y/m>=q),Fraction())
        direct += Fraction(mu,m)*h
    transfer=sum((c*rough_prefix(Y/q,z) for q,c in jumps),Fraction())
    return direct==transfer


def constants():
    mp.mp.dps=80
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
    P=mp.mpf(1); logder=mp.mpf(0)
    for p in primes:
        P*=1-mp.mpf(1)/p
        logder += mp.log(p)/(p-1)
    a=12*P
    J=2*(6*P*logder+(6*mp.euler-mp.mpf(9)/4)*P)+6*(2*mp.log(4)-8)*P
    assert mp.mpf('1.5790') < a < mp.mpf('1.5791')
    assert mp.mpf('2.0695') < J < mp.mpf('2.0697')
    return str(a),str(J)


def exponent_check() -> bool:
    # u=N^(3/8)(log N)^(-3/4). In
    # u^(8/5) log(u) log(N/u)^(1/5), N exponent is 3/5 and
    # log exponent is -6/5+1+1/5=0.
    n_exp=Fraction(3,8)*Fraction(8,5)
    log_exp=Fraction(-3,4)*Fraction(8,5)+1+Fraction(1,5)
    return n_exp==Fraction(3,5) and log_exp==0


def main():
    assert exact_stieltjes_fixture()
    assert exponent_check()
    a,J=constants()
    core={
      "schema":"riemann.x98040.dickman-stieltjes.v1",
      "frozen_head_pr603":"1dac3eeccb5a01183067c00722d92fbcf2df12c5",
      "exact_stieltjes_fixture":True,
      "complete_base_mass_a_star":a,
      "mellin_finite_part_J_star":J,
      "J_star_interval":["2.0695","2.0697"],
      "corridor":{"logY_power":"3/8","loglogY_power":"-3/4"},
      "vinogradov_korobov_used":True,
      "gpc67_proved":False,
      "rh_established":False,
      "verdict":VERDICT,
    }
    canon=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    core["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    out=Path(__file__).resolve().parent/"results/verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(core,indent=2,sort_keys=True)+"\n",encoding="utf-8",newline="\n")
    print(core["verdict"])
    print(core["proof_object_sha256"])


if __name__=="__main__":
    main()
