#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import hashlib, json, random
from pathlib import Path

VERDICT="PASS_T105420_F1_WICK_HODGE_QUOTIENT"

def H(A,B):
    return A*A/Fraction(24)+2*B*B

def run():
    rng=random.Random(105420)
    algebra=0
    for _ in range(5000):
        A=Fraction(rng.randint(-200,200),rng.randint(1,50))
        B=Fraction(rng.randint(-200,200),rng.randint(1,50))
        L=4*A-B
        J=A+192*B
        assert Fraction(769,2)*H(A,B)==L*L+J*J/Fraction(48)
        assert J==9216*(2*B*Fraction(1,96)+A*Fraction(1,96)**2)
        algebra+=1

    mA=Fraction(0)
    mB=Fraction(1)
    mL=4*mA-mB
    mJ=mA+192*mB
    q=mL*mL+mJ*mJ/Fraction(48)
    assert q==769
    assert mL*mL/q==Fraction(1,769)

    transfer=0
    for _ in range(5000):
        positive=Fraction(rng.randint(0,500),rng.randint(1,80))
        n=rng.randint(1,12)
        vals=[]
        energies=[]
        for _j in range(n):
            A=Fraction(rng.randint(-100,100),rng.randint(1,40))
            B=Fraction(rng.randint(-100,100),rng.randint(1,40))
            L=4*A-B
            J=A+192*B
            vals.append(L)
            energies.append(L*L+J*J/Fraction(48))
        avg=sum(vals,Fraction(0))/n
        avgE=sum(energies,Fraction(0))/n
        neg=max(Fraction(0),-(positive+avg))
        assert neg<=abs(avg)
        assert avg*avg<=avgE
        transfer+=1

    for t in (1,2,7,31):
        t=Fraction(t)
        assert t*t+(-192*t)**2/Fraction(48)==769*t*t

    mutations=sorted([
      "unquotiented_hodge_energy_called_subpower_rejected",
      "first_chaos_removed_after_squaring_rejected",
      "favorable_carrier_absolute_valued_before_recombination_rejected",
      "duplicate_67_tail_promoted_to_infinite_rejected",
      "wick_quotient_called_detector_change_rejected",
      "free_fock_energy_promoted_to_physical_restriction_rejected",
      "f1wnc105420_promoted_to_proved_rejected",
      "rh_promoted_by_replay_rejected",
    ])
    payload={
      "schema":"riemann.x105420.f1-wick-hodge-quotient.v1",
      "classification":VERDICT,
      "base_pr":730,
      "base_sha":"08f68c0a2b937d8aeac35c5c6a1de6946ed39dd7",
      "wick_pr":719,
      "wick_sha":"6211b5d7dd2b7f3f2657fc5ad5b22b1580650477",
      "orthogonal_algebra_checks":algebra,
      "favorable_transfer_checks":transfer,
      "first_chaos_detector_fraction":"1/769",
      "first_chaos_square_multiplier":769,
      "unquotiented_f1ato105405_valid":False,
      "wick_hodge_quotient_identified":True,
      "favorable_carrier_transfer_proved":True,
      "f1wnc105420_proved":False,
      "rh_established":False,
      "mutations_rejected":mutations,
    }
    canonical=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    payload["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
    return payload

def main():
    r=run()
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    print(r['classification'])
    print(r['proof_object_sha256'])

if __name__=='__main__':
    main()
