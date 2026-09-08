#!/usr/bin/env python3
"""Reconstruct the fixed rational sources and complete finite Green energies."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, sys
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT.parent/'2026-09-06-astra-balanced-lift'
HEAD='7919f443c0c2c2a87f95d3237d4fe77fb87f9a74'
PINS={'PROOF.md':'b3f4ec2c4b85fa64e13370176dac3a3529ce315411752c553411623c7fff2a39',
      'verification.json':'350ee09fce4f639a6ee06b327f6423c3ae8c6e79e02fbe4dbb260b496bc15f98'}
FILES={'README.md','PROOF.md','NUMERICS.md','SOURCES.md','SOURCE_LOCK.json','VALIDATION.md',
       'scripts/mathcore.py','scripts/replay.py','scripts/test_replay.py','verification.json'}
CONFIG={'full_M':[4,8,16,32],'coefficient_checks':[128,256],'primitive_cap':256,
        'paired_cells':64,'prefix_terms':512,'cotangent_odd_max':63,'bits':224,
        'taylor_terms':80,'all_energy_tails_included':True,'broad_campaign':False}
SCHEMA='riemann-finite-green-energy-v1'
class Refusal(Exception):pass

def need(condition,message):
    if condition is not True:raise Refusal(message)

def canonical(x):return (json.dumps(x,sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode()

def strict_json(path):
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise Refusal('duplicate JSON key')
            d[k]=v
        return d
    def reject(x):raise Refusal('nonexact JSON numeric token')
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=reject,parse_constant=reject)

def authentic_parent():
    result={}
    for name,digest in PINS.items():
        path=PARENT/name
        need(path.is_file() and not path.is_symlink(),'missing/symbolic parent')
        need(not any(p.is_symlink() for p in path.parents),'symbolic source ancestor')
        raw=path.read_bytes()
        need(hashlib.sha256(raw).hexdigest()==digest,'parent digest mismatch')
        result[name]=raw
    lock=strict_json(ROOT/'SOURCE_LOCK.json')
    need(lock=={'schema':'green-energy-source-lock-v1','head':HEAD,'parent_directory':PARENT.name,
                'parent_sha256':PINS,'parent_code_executed':False},'source lock mismatch')
    return result

def manifest(root=ROOT):
    need(not root.is_symlink() and not any(p.is_symlink() for p in root.parents),'symbolic root')
    file=root/'SHA256SUMS';need(file.is_file() and not file.is_symlink(),'missing manifest')
    seen=set()
    for line in file.read_text(encoding='utf-8').splitlines():
        need('  ' in line,'manifest syntax')
        digest,name=line.split('  ',1);pp=PurePosixPath(name)
        need(re.fullmatch('[0-9a-f]{64}',digest) is not None,'digest syntax')
        need(name in FILES and name not in seen and '\\' not in name and
             not pp.is_absolute() and '..' not in pp.parts,'unknown/duplicate/unsafe path')
        seen.add(name);path=root/name
        need(path.is_file() and not path.is_symlink(),'missing/symbolic payload')
        need(hashlib.sha256(path.read_bytes()).hexdigest()==digest,'payload digest mismatch')
    actual=set()
    for path in root.rglob('*'):
        need(not path.is_symlink(),'symbolic payload')
        if '__pycache__' in path.parts:continue
        if path.is_file() and path.name!='SHA256SUMS':actual.add(path.relative_to(root).as_posix())
    need(seen==FILES==actual,'nonempty exact inventory required')

def load_math():
    path=ROOT/'scripts/mathcore.py'
    spec=importlib.util.spec_from_file_location('green_exact_math',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    exec(compile(path.read_bytes(),str(path),'exec'),module.__dict__)
    return module

def reconstruct():
    authentic_parent();m=load_math();I=m.I
    counts=Counter()
    def check(ok,name):
        need(ok,name);counts[name]+=1
    check(m.pi().lo>I.of(3).hi and m.pi().hi<I.of(4).lo,'pi_range')
    for n in range(1,257):
        ds=[d for d in range(1,n+1) if n%d==0]
        check(sum(m.mu(d) for d in ds)==(1 if n==1 else 0),'primitive_mobius')
        check(sum(m.phi(d) for d in ds)==n,'primitive_totient')
        check(sum(m.j2(d) for d in ds)==n*n,'primitive_jordan')
    coeff_rows=[]
    for M in CONFIG['coefficient_checks']:
        lam,(S,A,D,K),v,w=m.balanced(M)
        check(lam[1]==1 and sum((a/F(k) for k,a in lam.items()),F())==0,'coefficient_constraints')
        check(abs(A)<F(5,2) and D>=F(M,5),'scalar_bound_fixture')
        for k,a in lam.items():
            check(abs(w[k])<F(5*k,2),'w_bound_fixture')
            check(abs(a-m.mu(k))<F(72*k,M),'coefficient_bound_fixture')
        check(sum(lam.values())==(D*sum(m.mu(k) for k in lam)-A*sum(m.phi(k) for k in lam))/K,'total_coefficient_formula')
        eta=m.pi()*m.pi()*F(D,16*K)-F(1,2)
        check(eta.lo>0 and eta.hi<I.of(F(18,M)).lo,'detail_bound_fixture')
        coeff_rows.append({'M':M,'A':str(A),'D':str(D),'total_coefficient':str(sum(lam.values())),
                           'detail_error':eta.record()})
    old={s['M']:s for s in strict_json(PARENT/'verification.json')['sources']}
    results=[]
    for M in CONFIG['full_M']:
        lam,(S,A,D,K),v,w=m.balanced(M);E,rows,tails,pieces=m.energy(lam)
        ks=list(lam)
        check(lam[1]==1 and sum((a/F(k) for k,a in lam.items()),F())==0,'source_constraints')
        for k in ks:
            kkt=sum((lam[l]*F(gcd(k,l)**2,k*k*l*l) for l in ks),F())
            check(kkt==((D if k==1 else 0)-A/F(k))/K,'source_KKT')
        qcoeff={q:sum((a/F(k) for k,a in lam.items() if k%q==0),F()) for q in ks}
        for k in ks:
            recovered=sum((m.mu(d)*qcoeff[k*d] for d in range(1,M//k+1,2)),F())
            check(recovered==lam[k]/k,'frequency_source_inverse')
        check(len(rows)==sum(m.phi(q)//2 for q in range(3,M+1,2)),'complete_frequency_count')
        for j in range(1,CONFIG['paired_cells']+1):
            value=m.source(lam,2*j)
            check(value==m.source(lam,2*j-1),'paired_cells')
            check(m.source(lam,-2*j)==-value,'odd_periodic_source')
            check(m.sine_value(rows,j).contains(value),'finite_sine_reconstruction')
        # Direct quadratic form with min-kernel versus cumulative interval factorization.
        q=I.of(0)
        for i,a in enumerate(rows):
            for j,b in enumerate(rows):
                q+=a['charge']*b['charge']*rows[min(i,j)]['tan']
        check(E.overlaps(m.pi()/2*q),'Green_quadratic_vs_intervals')
        check(E.lo>I.of(F(2,3)).hi,'two_cell_lower_bound')
        check(E.hi-E.lo < I.of(F(1,10**40)).lo,'energy_width')
        if M in old:
            v=old[M]['full_energy'];prior=I(int(v['lo']),int(v['hi']))
            check(E.overlaps(prior),'independent_infinite_Gram_comparison')
            check({str(k):str(a) for k,a in lam.items()}==old[M]['weights'],'independent_rational_source_comparison')
        prefix=sum((m.source(lam,n)**2/F(n*(n+1)) for n in range(1,513)),F())
        amplitude=sum(map(abs,lam.values()),F())/2
        check(E.overlaps(I.bounds(prefix,prefix+amplitude**2/513)),'independent_physical_prefix_tail')
        tau=1/m.logq(F(2*M));low=m.partial_energy(rows,tails,tau)
        high=E-low;B=sum((abs(a)/k for k,a in lam.items()),F())
        check(high.hi<(m.pi()*B*B/(2*tau)).lo,'entire_complement_bound_fixture')
        check(low.lo>=0 and low.hi<=E.hi,'endpoint_partition')
        expanded=I.of(0)
        for k,a in lam.items():
            for r in range(1,(k+1)//2):
                sn,cs=m.trig(F(r,k));expanded+=a/F(k)*(-1)**(r+1)*cs/sn
        check(expanded.overlaps(tails[0]),'unreduced_endpoint_current')
        T=sum(lam.values(),F());endpoint_err=tails[0]-m.logq(F(2))/m.pi()*T
        e_bound=m.pi()/12*sum((abs(a)/F(k*k) for k,a in lam.items()),F())
        check(endpoint_err.lo>=-e_bound.hi and endpoint_err.hi<=e_bound.hi,'endpoint_scalar_error_fixture')
        if M==4:
            check((2*E/m.pi()).square().contains(F(1,3)),'exact_M4_algebraic_value')
        results.append({'M':M,'weights':{str(k):str(a) for k,a in lam.items()},
          'frequency_count':len(rows),'full_energy':E.record(),'first_interval_energy':pieces[0].record(),
          'endpoint_energy_at_inverse_log':low.record(),'endpoint_current':tails[0].record(),
          'total_coefficient':str(T),'B':str(B),
          'mesh':[str(r['x']) for r in rows],
          'frequency_coefficients':{str(q):str(v) for q,v in qcoeff.items()},
          'directed_mesh_sha256':hashlib.sha256(canonical([{'x':str(r['x']),
               'L':str(r['L']),'charge':r['charge'].record(),'tan':r['tan'].record()}
               for r in rows])).hexdigest()})
    # All odd k in this small fixed panel test the general alternating-cotangent enclosure.
    for k in range(1,64,2):
        a=I.of(0)
        for r in range(1,(k+1)//2):
            sn,cs=m.trig(F(r,k));a+=(-1)**(r+1)*cs/sn
        eps=k*m.logq(F(2))/m.pi()-a
        check(eps.lo>0 and eps.hi<(m.pi()/F(12*k)).lo,'cotangent_remainder_fixture')
    # Independent rational Green inverse: no trigonometric or number-theory code.
    for ts in ([F(1,7)],[F(1,7),F(2,3),F(5,2),F(9)],[F(1),F(2),F(4),F(8),F(16)]):
        n=len(ts);ds=[ts[0]]+[ts[i]-ts[i-1] for i in range(1,n)]
        K=[[min(a,b) for b in ts] for a in ts];D=[[F() for j in ts] for i in ts]
        for i in range(n):
            D[i][i]=1/ds[i]+(1/ds[i+1] if i+1<n else 0)
            if i+1<n:D[i][i+1]=D[i+1][i]=-1/ds[i+1]
        for i in range(n):
            for j in range(n):check(sum(K[i][k]*D[k][j] for k in range(n))==(1 if i==j else 0),'rational_tridiagonal_inverse')
    return {'schema':SCHEMA,'rh_proved':False,'uniform_full_gain_proved':False,
       'subpower_full_energy_proved':False,'status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED',
       'config':CONFIG,'parent_head':HEAD,'counts':dict(sorted(counts.items())),
       'control_total':sum(counts.values()),'sources':results,'coefficient_fixtures':coeff_rows}

def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--check',action='store_true');g.add_argument('--write',type=Path);args=p.parse_args()
    try:
        authentic_parent()
        if args.check:
            manifest();expected=strict_json(ROOT/'verification.json')
            need(expected.get('schema')==SCHEMA and expected.get('config')==CONFIG,'schema/config mismatch')
            for key in ['rh_proved','uniform_full_gain_proved','subpower_full_energy_proved']:
                need(expected.get(key) is False,'forbidden mathematical promotion')
        result=reconstruct();raw=canonical(result)
        if args.write:args.write.write_bytes(raw)
        else:need(canonical(expected)==raw,'primitive reconstruction mismatch')
        print('PASS_FINITE_GREEN_ENERGY controls='+str(result['control_total']))
        print('RH_NOT_PROVED ENDPOINT_SUBPOWER_NOT_PROVED');return 0
    except (Refusal,ValueError,TypeError,KeyError,OSError,ZeroDivisionError) as e:
        print('REFUSED: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
