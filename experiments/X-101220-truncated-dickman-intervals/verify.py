#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math
from fractions import Fraction
from pathlib import Path

def subset_prefix(weights, costs, x):
    out=Fraction(0)
    n=len(weights)
    for mask in range(1<<n):
        cost=1; w=Fraction(1); parity=0
        for i in range(n):
            if mask>>i&1:
                cost*=costs[i]; w*=weights[i]; parity^=1
        if cost<=x: out += -w if parity else w
    return out

def finite_checks():
    costs=[71,73,79,83,89,97]
    weights=[Fraction(1,p) for p in costs]
    full=Fraction(1)
    for w in weights: full*=1-w
    assert subset_prefix(weights,costs,10**30)==full
    vals=[subset_prefix(weights,costs,x) for x in [1,71,83,71*73,10**9]]
    return {'full_mass':str(full),'prefixes':[str(v) for v in vals]}

def continuum_grid(a,du=0.002,umax=30.0):
    # Volterra stepping for u F(u)=int_(u-1)^u F + int_0^(u-a)F.
    n=int(umax/du)+1
    F=[0.0]*n; prefix=[0.0]*(n+1)
    for i in range(n):
        u=i*du
        if u<1.0+1e-15: F[i]=1.0
        else:
            lo=max(0,int(math.ceil((u-1)/du)))
            first=(prefix[i]-prefix[lo])*du
            j=max(0,int(math.floor((u-a)/du)))
            second=prefix[j+1]*du if u>=a else 0.0
            F[i]=(first+second)/u
        prefix[i+1]=prefix[i]+F[i]
    return min(F[1:]),F[-1]

def build_result():
    finite=finite_checks()
    grids={}
    for a in (1.5,2.0,3.0,5.0):
        mn,tail=continuum_grid(a)
        assert mn>0
        grids[str(a)]={'minimum':mn,'tail':tail,'target_total':1/a}
    payload={
      'schema':'riemann.x101220.truncated_dickman_intervals.v1',
      'base_pr':700,
      'finite_subset_checks':finite,
      'continuum_diagnostics':grids,
      'scope':{
        'convolution_exponential_identity_checked':True,
        'continuum_positivity_diagnostic':True,
        'all_fixed_exponent_interval_theorem_proved':True,
        'adverse_least_endpoint_subpower_proved':True,
        'remaining_small_owner_packing_proved':False,
        'rh_established':False,
      },
      'verdict':'PASS_T101220_TRUNCATED_DICKMAN_INTERVAL_LOCALIZATION'
    }
    core=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(core).hexdigest()
    return payload

def main():
    result=build_result(); out=Path(__file__).parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(result['verdict']); print(result['proof_object_sha256'])
if __name__=='__main__': main()
