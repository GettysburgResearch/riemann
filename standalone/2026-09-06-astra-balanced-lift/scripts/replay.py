#!/usr/bin/env python3
"""Bounded rational balanced-source replay. No RH or subpower estimate verified."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
PARENT = BASE / '2026-09-06-astra-dilation-observability'
HEAD = '0f8724bbd86c1de8f40eacbf30129321e0ebc8aa'
PINS = {
 '2026-09-06-astra-dilation-observability/PROOF.md':'be2fbf1f146c412cfdda0cfd9c613a4beb88c7b77191c4eb2af3e769c6d71b22',
 '2026-09-06-astra-dilation-observability/NUMERICS.md':'de19939b3150f0a47cce7da8ba306a520346e396bbeb0860bf3ce18f775beb64',
 '2026-09-06-astra-dilation-observability/scripts/intervals.py':'91b6448681d88ba5aa7fd0093c6ab2590bd2575d4b0c6e59082fe196fc5fb304',
 '2026-09-06-astra-dilation-observability/scripts/replay.py':'6c252d214d9ff27d76a4b3bd7c0b087e04798aac1f20b125877915b588c66f1b',
 '2026-09-06-astra-block-gain/PROOF.md':'4843591a9cf21122d5b0e695d3d93c93f53ba89ba542a77a994d67672d07078a',
}
FILES = {'README.md','PROOF.md','NUMERICS.md','SOURCES.md','SOURCE_LOCK.json',
         'VALIDATION.md','scripts/replay.py','scripts/test_replay.py','verification.json'}
CONFIG = {'algebra_M':[3,4,5,8,9,16,24,32], 'full_M':[4,8,16],
          'coherent_K':[2,4,8,16], 'local_cells':128, 'arithmetic_cap':128,
          'gram_cap':32, 'max_consumed_gram_index':30, 'prefix_terms':512,
          'directed_bits':224, 'no_float_acceptance':True,
          'all_infinite_gram_tails_enclosed':True}
SCHEMA='riemann-balanced-rational-source-v1'
class Refusal(Exception): pass

def need(ok:bool, message:str)->None:
    if ok is not True: raise Refusal(message)

def canonical(x:object)->bytes:
    return (json.dumps(x,sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode()

def strict_json(path:Path)->object:
    def pairs(items):
        ans={}
        for k,v in items:
            if k in ans: raise Refusal('duplicate JSON key')
            ans[k]=v
        return ans
    def reject(x): raise Refusal('nonexact JSON number')
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=reject,parse_constant=reject)

def authenticate(base:Path=BASE)->dict[str,bytes]:
    result={}
    need(not base.is_symlink(),'symbolic source root')
    for name,digest in PINS.items():
        file=base/name
        need(file.is_file() and not file.is_symlink(),'missing or symbolic parent file')
        need(not any(q.is_symlink() for q in file.parents),'symbolic parent directory')
        raw=file.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==digest,'parent source hash mismatch: '+name)
        result[name]=raw
    return result

def load_parent():
    acquired=authenticate(); modules={}
    for mod,rel in [('intervals','scripts/intervals.py'),('bl26_parent','scripts/replay.py')]:
        path=PARENT/rel
        spec=importlib.util.spec_from_file_location(mod,path)
        need(spec is not None,'missing module spec')
        obj=importlib.util.module_from_spec(spec);sys.modules[mod]=obj
        raw=acquired['2026-09-06-astra-dilation-observability/'+rel]
        exec(compile(raw,str(path),'exec'),obj.__dict__)
        modules[mod]=obj
    return modules['intervals'],modules['bl26_parent']

iv,parent=load_parent()
I,SCALE=iv.I,iv.SCALE

def check_manifest(root:Path=ROOT)->None:
    need(not root.is_symlink() and not any(p.is_symlink() for p in root.parents),
         'symbolic manifest root or parent')
    file=root/'SHA256SUMS'
    need(file.is_file() and not file.is_symlink(),'missing/symbolic manifest')
    seen=set()
    for line in file.read_text(encoding='utf-8').splitlines():
        need('  ' in line,'manifest syntax')
        digest,name=line.split('  ',1);p=PurePosixPath(name)
        need(re.fullmatch('[0-9a-f]{64}',digest) is not None,'invalid digest')
        need(name in FILES and name not in seen and '\\' not in name and
             not p.is_absolute() and '..' not in p.parts,'unsafe/duplicate/unknown path')
        seen.add(name);target=root/name
        need(target.is_file() and not target.is_symlink(),'missing/symbolic payload')
        need(hashlib.sha256(target.read_bytes()).hexdigest()==digest,'payload hash mismatch')
    actual=set()
    for p in root.rglob('*'):
        if '__pycache__' in p.parts: continue
        need(not p.is_symlink(),'symbolic payload path')
        if p.is_file() and p.name!='SHA256SUMS': actual.add(p.relative_to(root).as_posix())
    need(seen==FILES==actual,'nonempty exact inventory required')

def integer(n:int,lo:int=1,hi:int=128)->int:
    if type(n) is not int or not lo<=n<=hi: raise ValueError('integer outside fixed scope')
    return n

@lru_cache(maxsize=None, typed=True)
def mu(n:int)->int:
    integer(n);sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign

@lru_cache(maxsize=None, typed=True)
def phi(n:int)->int:
    integer(n);return sum(gcd(n,k)==1 for k in range(1,n+1))

@lru_cache(maxsize=None, typed=True)
def jordan(n:int)->int:
    integer(n);return sum(mu(n//d)*d*d for d in range(1,n+1) if n%d==0)

def R(k:int,l:int)->F:
    return F(gcd(k,l)**2,k*k*l*l)

@lru_cache(maxsize=None, typed=True)
def weights(M:int):
    integer(M,3);o=tuple(range(1,M+1,2))
    S=sum((F(mu(k)**2,jordan(k)) for k in o),F())
    A=sum((F(mu(k)*phi(k),jordan(k)) for k in o),F())
    D=sum((F(phi(k)**2,jordan(k)) for k in o),F())
    K=S*D-A*A;need(K>0,'nonpositive capacity determinant')
    v={k:k*k*sum((F(mu(d//k)*mu(d),jordan(d)) for d in o if d%k==0),F()) for k in o}
    w={k:k*k*sum((F(mu(d//k)*phi(d),jordan(d)) for d in o if d%k==0),F()) for k in o}
    lam={k:(D*v[k]-A*w[k])/K for k in o}
    return lam,(S,A,D,K),v,w

def solve_rational(matrix,rhs):
    n=len(rhs); a=[list(row)+[rhs[j]] for j,row in enumerate(matrix)]
    need(all(len(row)==n+1 for row in a),'invalid matrix')
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        need(pivot is not None,'singular rational system')
        a[j],a[pivot]=a[pivot],a[j]
        q=a[j][j];a[j]=[x/q for x in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return [a[i][-1] for i in range(n)]

def primitive(a:dict[int,F],n:int)->F:
    return sum((v*(n//k-n//(2*k)) for k,v in a.items()),F())

def jumps(a:dict[int,F],n:int)->F:
    return sum((v for k,v in a.items() if n%k==0),F()) if n%2 else F()

def source_coefficients(a:dict[int,F])->dict[int,F]:
    c={}
    for k,v in a.items():
        c[2*k]=c.get(2*k,F())+v
        if k>1:c[k]=c.get(k,F())-v
    return {k:v for k,v in c.items() if v}

@lru_cache(maxsize=None, typed=True)
def gram(k:int,l:int)->I:
    integer(k,2,CONFIG['gram_cap']);integer(l,2,CONFIG['gram_cap'])
    if k>l:return gram(l,k)
    period=k*l//gcd(k,l);out=I.of(0)
    for r in range(1,period):
        a=F((r%k)*(r%l),k*l)
        if a:out+=a*(iv.psi_q(F(r+1,period))-iv.psi_q(F(r,period)))/period
    return out

def full_energy(c:dict[int,F])->I:
    return sum((v*w*gram(k,l) for k,v in c.items() for l,w in c.items()),I.of(0))

def check_source_lock()->None:
    data=strict_json(ROOT/'SOURCE_LOCK.json')
    need(isinstance(data,dict) and data.get('schema')=='riemann-balanced-lift-source-lock-v1',
         'invalid source lock')
    need(data.get('parent_head')==HEAD and data.get('parent_sha256')==PINS,'source lock drift')
    need(data.get('primitive_source')=='fractional_parts_all_odd_indices_two_exact_constraints',
         'primitive source drift')
    need(data.get('zero_data_used') is False and data.get('rh_proved') is False,'false source status')

EXPECTED={
4:('0.906899682117','0.906899682118','0.549306144334','0.549306144335'),
8:('0.810154169731','0.810154169732','0.734600804710','0.734600804711'),
16:('0.888710277691','0.888710277692','0.842755232154','0.842755232155'),
}

def reconstruct()->dict:
    counts=Counter();rows=[];pi=iv.pi_interval()
    def check(ok,label): need(ok,label);counts[label]+=1
    for n in range(1,129):
        check(sum(mu(d) for d in range(1,n+1) if n%d==0)==(n==1),'mobius_divisor')
        check(jordan(n)>0 and sum(jordan(d) for d in range(1,n+1) if n%d==0)==n*n,'jordan_identity')
        check(sum(d*mu(n//d) for d in range(1,n+1) if n%d==0)==phi(n),'totient_identity')
    for M in CONFIG['algebra_M']:
        lam,(S,A,D,K),v,w=weights(M);o=list(lam);q=len(o)
        check(lam[1]==1 and sum((a/F(k) for k,a in lam.items()),F())==0,'two_constraints')
        matrix=[[R(k,l) for l in o]+[-F(k==1),-F(1,k)] for k in o]
        matrix += [[F(l==1) for l in o]+[F(),F()], [F(1,l) for l in o]+[F(),F()]]
        solution=solve_rational(matrix,[F()]*q+[F(1),F()])
        check(solution[:q]==list(lam.values()),'independent_KKT')
        for k in o:
            check(sum(R(k,l)*v[l] for l in o)==(k==1),'inverse_column_one')
            check(sum(R(k,l)*w[l] for l in o)==F(1,k),'inverse_column_moment')
        check(sum(lam[k]*lam[l]*R(k,l) for k in o for l in o)==D/K,'capacity_value')
        c=source_coefficients(lam)
        for n in range(1,129):
            f=primitive(lam,n)
            by_basis=sum((a*F(n%k,k) for k,a in c.items()),F())
            check(f==by_basis,'primitive_vs_fractional_source')
            check(f-primitive(lam,n-1)==jumps(lam,n),'odd_jump_identity')
            check(sum(mu(k)*(n//k-n//(2*k)) for k in range(1,n+1,2))==1,'mobius_local_target')
        check(primitive(lam,1)==primitive(lam,2)==1,'first_two_cells')
    check(weights(4)[0]=={1:F(1),3:F(-3)},'exact_M4_weights')
    check(weights(16)[0][9]==F(-20880,57769),'nonsquarefree_retained')
    for M in range(32,129):
        D=sum((F(phi(k)**2,jordan(k)) for k in range(1,M+1,2)),F())
        check(D>=F(M,5),'bounded_D_lower_check')
    for k in range(2,17):
        for l in range(k,17):
            check(gram(k,l).overlaps(parent.gram(k,l)),'unchanged_parent_Gram_overlap')
    for M in CONFIG['full_M']:
        lam,(S,A,D,K),_,_=weights(M);c=source_coefficients(lam)
        energy=full_energy(c)
        target=sum((a*iv.log_q(F(k))/k for k,a in c.items()),I.of(0))
        err=1-2*target+energy
        eta=pi*pi*F(D,16*K)-F(1,2)
        low,high,tlow,thigh=map(F,EXPECTED[M])
        check(energy.lo>I.of(low).hi and energy.hi<I.of(high).lo,'directed_energy_enclosure')
        check(target.lo>I.of(tlow).hi and target.hi<I.of(thigh).lo,'directed_target_enclosure')
        check(energy.lo>0 and eta.lo>0 and err.lo>0,'positive_directed_quantities')
        pref=sum((primitive(lam,n)**2/F(n*(n+1)) for n in range(1,513)),F())
        amplitude=sum((abs(a) for a in lam.values()),F())/2
        check(energy.overlaps(I.bounds(pref,pref+amplitude*amplitude/513)), 'independent_prefix_tail')
        # Independent removable s=1 formula from the polynomial, not basis coefficients.
        logmoment=-sum((a*iv.log_q(F(k))/k for k,a in lam.items()),I.of(0))/2
        check(target.overlaps(logmoment),'removable_Mellin_value')
        rows.append({'M':M,'weights':{str(k):str(a) for k,a in lam.items()},
                     'rational_capacity':{'S':str(S),'A':str(A),'D':str(D),'K':str(K)},
                     'full_energy':energy.record(),'target_pairing':target.record(),
                     'full_squared_error':err.record(),'detail_error':eta.record()})
    coherent=[]
    for K in CONFIG['coherent_K']:
        M=4*K;lam,_,_,_=weights(M)
        z={k:F(k if K<k<=2*K else -k if 3*K<k<=4*K else 0) for k in range(1,M+1,2)}
        check(z[1]==0 and sum((a/F(k) for k,a in z.items()),F())==0,'coherent_constraints')
        q=sum((a*b*R(k,l) for k,a in z.items() for l,b in z.items()),F())
        check(F(10,16)*q<=F(25*K,2),'coherent_detail_upper')
        check(sum((lam[k]*z[l]*R(k,l) for k in lam for l in z),F())==0,'coherent_KKT_orthogonality')
        for n in range(2*K,3*K+1):
            check(primitive(z,n)==F(3*K*K,4),'coherent_exact_plateau')
        lower=F(9*K**4,16)*(F(1,2*K)-F(1,3*K+1))
        check(lower>F(3*K**3,32),'coherent_full_energy_lower')
        for t in (F(1,2),F(-1,3)):
            aa={k:lam[k]+t*z[k] for k in lam}
            norm=sum((aa[k]*aa[l]*R(k,l) for k in aa for l in aa),F())
            old=sum((lam[k]*lam[l]*R(k,l) for k in lam for l in lam),F())
            check(norm-old==t*t*q,'exact_detail_perturbation')
        coherent.append({'K':K,'M':M,'detail_norm_over_pi_squared':str(q/16),
                         'plateau':str(F(3*K*K,4)),'full_norm_lower':str(lower)})
    return {'schema':SCHEMA,'rh_proved':False,'uniform_full_gain_proved':False,
            'subpower_full_energy_proved':False,'scientific_status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED',
            'arithmetic':'EXACT_RATIONAL_SOURCES_AND_OUTWARD_DYADIC_FULL_GRAM_TAILS',
            'config':CONFIG,'controls':dict(sorted(counts.items())),
            'control_total':sum(counts.values()),'sources':rows,'coherent_controls':coherent}

def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--check',action='store_true')
    group.add_argument('--write',type=Path)
    opts=parser.parse_args()
    try:
        check_source_lock()
        if opts.check:check_manifest()
        result=reconstruct();raw=canonical(result)
        if opts.write:
            opts.write.write_bytes(raw)
        else:
            expected=strict_json(ROOT/'verification.json')
            need(canonical(expected)==raw,'reconstruction mismatch')
        print('PASS_BALANCED_SOURCE_BOUNDED_REPLAY controls='+str(result['control_total']))
        print('RH_NOT_PROVED SUBPOWER_FULL_ENERGY_NOT_PROVED')
        return 0
    except (Refusal,ValueError,TypeError,KeyError,ZeroDivisionError,OSError) as error:
        print('REFUSED: '+str(error),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
