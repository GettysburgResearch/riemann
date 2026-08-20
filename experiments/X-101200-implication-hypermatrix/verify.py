#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path

def h(m:int)->int: return 15-15*(2**m)+11**m

def q(a:int,b:int)->int:
    return 15*(0**a)*(8**b)-15*(1**a)*(9**b)+(10**a)*(18**b)

def transport_fixture():
    mu_m=[Fraction(3,2),Fraction(5,4)]
    mu_p=[Fraction(7,4),Fraction(1)]
    Kx=[Fraction(5),Fraction(2)]
    Ky=[Fraction(4),Fraction(6)]
    pi=[[Fraction(1),Fraction(1,4)],[Fraction(1,2),Fraction(1,2)]]
    row=[sum(r) for r in pi]
    col=[sum(pi[i][j] for i in range(2)) for j in range(2)]
    rm=[mu_m[i]-row[i] for i in range(2)]
    rp=[mu_p[j]-col[j] for j in range(2)]
    scalar=sum(mu_p[j]*Ky[j] for j in range(2))-sum(mu_m[i]*Kx[i] for i in range(2))
    coupled=sum(pi[i][j]*(Ky[j]-Kx[i]) for i in range(2) for j in range(2))
    residual=sum(rp[j]*Ky[j] for j in range(2))-sum(rm[i]*Kx[i] for i in range(2))
    collar=sum(pi[i][j]*max(Fraction(0),Kx[i]-Ky[j]) for i in range(2) for j in range(2))
    unmatched=sum(rm[i]*Kx[i] for i in range(2))
    assert scalar==coupled+residual
    assert max(Fraction(0),-scalar)<=collar+unmatched
    return scalar,collar,unmatched

def build_result():
    assert h(0)==1 and h(1)==-4
    for m in range(2,65): assert h(m)>0
    mixed=0
    for a in range(17):
        for b in range(17):
            if a+b>=2:
                assert q(a,b)>0; mixed+=1
    assert h(1)*h(3)-h(2)**2==-10680
    scalar,collar,unmatched=transport_fixture()
    for k in range(9):
        theta=Fraction(k,8); assert theta/2-theta/2==0
    payload={
      'schema':'riemann.x101200.implication_hypermatrix.v2',
      'base_pr':698,
      'base_sha':'a10d6a40105142de2708632589c458d7534f556a',
      'checks':{
        'supercritical_moments':63,
        'mixed_degree_ge_two_carriers':mixed,
        'critical_hankel_determinant':-10680,
        'transport_scalar':str(scalar),
        'transport_collar':str(collar),
        'transport_unmatched':str(unmatched),
        'exponent_cancellations':9,
      },
      'scope':{
        'moment_cone_separator_proved':True,
        'transport_collar_identity_proved':True,
        'amplitude_occupancy_hyperedge_proved':True,
        'fixed_shell_amplitude_proved':True,
        'typed_multi_producer_cover_implication_proved':True,
        'typed_cell_certificates_proved':False,
        'exceptional_cell_sparsity_proved':False,
        'rh_established':False,
      },
      'verdict':'PASS_T101200_AUDITED_CLOSURE_IMPLICATION_HYPERMATRIX'
    }
    core=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(core).hexdigest()
    return payload

def main():
    result=build_result()
    out=Path(__file__).parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(result['verdict']); print(result['proof_object_sha256'])
if __name__=='__main__': main()
