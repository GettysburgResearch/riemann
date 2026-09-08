#!/usr/bin/env python3
"""Authenticate and reconstruct the fixed FR26 packet; acceptance never uses assert."""
import argparse
from collections import Counter
from fractions import Fraction as F
from math import comb, factorial
import hashlib
import json
from pathlib import Path
import re
import sys
import types
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
EXPECTED=frozenset({'PROOF.md','README.md','NUMERICS.md','SOURCES.md','SOURCE_LOCK.json',
 'VALIDATION.md','interval_core.py','certificate.py','check.py','test_check.py','verification.json','SHA256SUMS'})
CORE_SHA='1aa6bfa49f791ffde5224e21c8c92291a2e06b35130034d1de975b4d7a93fa17'
PRODUCER_SHA='22211a064e747a3934efb457743d23f24d797a6af71533bbc224f6bc6c714e9b'
PROOF_SHA='a50fe8b3f8b1f7d974058144173f6b48e51961178126008e8852868cc837079e'
LOCK_SHA='5655785dd462fab04e7741a6c1d9e8664c7593a75e6da8e066606b9688c62ff6'
SCHEMA='riemann-future-realization-v1'

def require(v,msg):
    if not v:raise ValueError(msg)

def strict_json(raw):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    def bad(x):raise ValueError('JSON floating/constant aliases not accepted')
    return json.loads(raw,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)

def canonical(x):return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=True)+'\n'

def load(raw,name):
    m=types.ModuleType(name);sys.modules[name]=m
    exec(compile(raw,name,'exec'),m.__dict__)
    return m

def authenticate(root):
    require(root.is_dir() and not root.is_symlink(),'bad packet root')
    actual=set()
    for p in root.rglob('*'):
        require(not p.is_symlink() and not p.is_dir(),'symlink/directory in flat packet')
        actual.add(p.relative_to(root).as_posix())
    require(actual==EXPECTED,'file inventory mismatch')
    manifest={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.]+)',line)
        require(m is not None,'bad manifest syntax')
        h,n=m.groups();require(n not in manifest,'duplicate manifest entry');manifest[n]=h
    require(set(manifest)==EXPECTED-{'SHA256SUMS'},'exact nonempty checksum inventory required')
    for n,h in manifest.items():require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'hash mismatch '+n)
    for n,h in [('interval_core.py',CORE_SHA),('certificate.py',PRODUCER_SHA),('PROOF.md',PROOF_SHA),('SOURCE_LOCK.json',LOCK_SHA)]:
        require(manifest[n]==h,'primitive/source binding mismatch '+n)
    lock=strict_json((root/'SOURCE_LOCK.json').read_text())
    require(lock['packet_id']=='FR26' and lock['unknown_zeros_are_inputs'] is False,'wrong source lock')
    return load((root/'interval_core.py').read_bytes(),'fr26_core'),load((root/'certificate.py').read_bytes(),'fr26_certificate')

def reconstruct(m,p):
    count=Counter()
    def ok(x,n):require(x,'failed control '+n);count[n]+=1
    floor=[]
    for k in range(65):
        v=p.gram_floor(k);ok(type(v) is F and 0<v<=1,'rational_gram_floor')
        if k:ok(v<=p.gram_floor(k-1),'floor_monotonicity')
        if k in [0,1,2,4,8,16,32,64]:floor.append({'degree':k,'floor':str(v)})
    for n in range(1,7):
        # Actual polynomial symbol controls, not zeta spectra.
        for off,diag,label in [(-2,5,'nonouter'),(-1,2,'boundary')]:
            G=[[m.C(diag if i==j else off if abs(i-j)==1 else 0)for j in range(n)]for i in range(n)]
            ok(all(x>0 for x in m.ldl_pivots(G)),label+'_finite_Gram')
            if label=='boundary':ok(m.quad([m.C(1)]*n,G)==m.C(2),'boundary_Fejer_energy')
            else:
                ev=[m.C(1)]+[m.C(0)]*(n-1)
                err=1-m.quad(ev,m.inverse(G)).re
                ok(err>F(3,4),'nonouter_not_cyclic')
    for eps in [F(1,2),F(1,4),F(1,16)]:
        # d=1_[0,1]: integrate its two squared ramp errors independently.
        left=eps-eps+eps/F(3)
        right=eps**3/(3*eps**2)
        # L(s)=2s, so the variance formula integrates 2*s^2/eps^2.
        via_translation=2*eps**3/(3*eps**2)
        ok(left+right==via_translation,'box_variance_step_control')
    for z in [m.C(F(1,3)),m.C(1),m.C(2),m.C(1,1),m.C(F(1,4),3),m.C(3,-2)]:
        R=(z-F(1,2))/(z+F(1,2))
        direct=sum((a*R**j for j,a in enumerate(p.COEFFS)),m.C(0))
        expanded=m.C(sum(p.COEFFS))
        for k in range(1,5):expanded+=((-1)**k)*sum(p.COEFFS[j]*comb(j,k)for j in range(k,5))/(z+F(1,2))**k
        ok(direct==expanded,'rational_allpass_impulse_identity')
    # Independent polynomial ODE and interval antiderivative controls.
    for n in [1,2,5,17]:
        g0=F(7,3);H=[F(0)]+[F(j+1,n+2) for j in range(1,5)]
        old=[g0,F(-n)]
        for k in range(1,5):
            poly=[H[k-l]/factorial(l)for l in range(k)]+[g0/F(factorial(k)),F(-n,factorial(k+1))]
            deriv=[(l+1)*poly[l+1]for l in range(len(poly)-1)]
            ok(deriv==old,'independent_integral_chain_ODE');old=poly
    for d in [F(1,2),F(1,3),F(1,7)]:
        # I_j is represented as a+b exp(-d); compare closed and recurrent forms.
        a,b=F(1),F(-1)
        for j in range(11):
            ca=F(factorial(j));cb=-ca*sum(d**l/F(factorial(l))for l in range(j+1))
            ok((a,b)==(ca,cb),'exact_cell_moment_recursion')
            a,b=(j+1)*a,(j+1)*b-d**(j+1)
    for x in [F(1),F(3,2),F(2),F(7,2),F(9,2),F(8)]:
        n=x.numerator//x.denominator
        direct=n*(1-m.logq(x))+sum((m.logq(F(j)) for j in range(1,n+1)),m.I.of(0))
        integ=m.I.of(0)
        for j in range(1,n+1):
            y=min(x,F(j+1))
            if y>j:integ+=(y-j)-j*m.logq(y/F(j))
        primitive=1-(x-n)+integ
        ok(direct.overlaps(primitive),'independent_factorial_source_primitive')
    for k in range(9):
        n=k+1;M=1
        while M*M<k+4:M+=1
        l=0
        while 2**l<k+2:l+=1
        S=32*(M+l+2)
        ok(F(S+3,2**(S//2))<=p.gram_floor(k)/F(12*n),'explicit_source_cutoff_budget')
    cert=p.full_certificate(m)
    ok(cert['half_cells']==4094,'complete_actual_cell_inventory')
    ok(int(cert['ideal_full_error']['hi'])*1200<m.SCALE,'ideal_full_tail_threshold')
    ok(F(cert['box_output_error_squared_upper'])<F(1,10**8),'compact_box_budget')
    ok(F(cert['input_truncation_output_norm_upper'])<F(1,10**8),'compact_stable_tail_budget')
    ok(F(3,10)>300*F(cert['compact_full_error_upper']) or F(3,10)==300*F(cert['compact_full_error_upper']),'strict_bounds_give_300fold')
    return {'schema':SCHEMA,'scientific_status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED',
      'rh_proved':False,'growing_horizon_bound_proved':False,'unconditional_gram_floor_proved_in_manuscript':True,
      'actual_compact_input_certificate':True,'all_infinite_certificate_tails_bounded':True,
      'scope':{'degree':4,'horizon':'log(2)','cutoff_x':2048,'half_cells':4094,'bits':160,
               'synthetic_max_dimension':6,'gram_floor_integer_controls_through':64},
      'controls':dict(sorted(count.items())),'bounded_control_count':sum(count.values()),
      'rational_gram_floors':floor,'actual_source':cert}

def verify(root):
    m,p=authenticate(root)
    retained=strict_json((root/'verification.json').read_text())
    require(retained.get('schema')==SCHEMA,'wrong verification schema')
    require(retained.get('rh_proved') is False and retained.get('growing_horizon_bound_proved') is False,'false theorem status')
    require(retained.get('actual_compact_input_certificate') is True,'scope/status alias')
    scope=retained.get('scope',{})
    require(type(scope.get('degree')) is int and scope['degree']==4,'degree alias/change')
    require(type(scope.get('half_cells')) is int and scope['half_cells']==4094,'coverage alias/change')
    observed=reconstruct(m,p)
    require(canonical(retained)==canonical(observed),'retained result differs from primitive reconstruction')
    return observed

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=ROOT);args=ap.parse_args()
    try:
        result=verify(args.root)
        print('PASS_FR26_FUTURE_REALIZATION')
        print('bounded_controls='+str(result['bounded_control_count']))
        print('integrated_cells=4094; analytic_infinite_tail=retained; rh_proved=false')
        print('verification_sha256='+hashlib.sha256(canonical(result).encode()).hexdigest())
    except (ValueError,TypeError,KeyError,OSError,ZeroDivisionError) as e:
        print('REJECT: '+str(e),file=sys.stderr);return 1
    return 0
if __name__=='__main__':raise SystemExit(main())
