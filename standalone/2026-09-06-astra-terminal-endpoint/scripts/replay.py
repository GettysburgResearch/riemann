#!/usr/bin/env python3
"""Bounded primitive replay for harmonic transfer and terminal endpoint scalar."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT.parent/'2026-09-06-astra-green-energy'
HEAD='acb0a25a373b427c9694aff78cba396f26963e8b'
PINS={
 'PROOF.md':('b9bd9e4f12dc597197c895a9acf74d0f302dc52f8cef823ae7ee3ddf30d5c006','6894235335aa56340be2c993b4e729be2db04052',20904),
 'NUMERICS.md':('ff12fa17a42ad1f23dacf71bbbc83bb2977186b8392f4352bce128463beeee2e','ad88c8caf5b0ab4b793264a39eb0db628d50a812',4864),
 'scripts/mathcore.py':('db0d970ffa5955074f2a2ca8aa9c511e9d0d887720eabbb76875b9c5f7531b7e','d1443067d7dfe8da4548bc3af8a96f9b979f73c8',7094)}
FILES={'README.md','PROOF.md','SOURCES.md','SOURCE_LOCK.json','VALIDATION.md',
       'scripts/replay.py','scripts/test_replay.py','verification.json'}
CONFIG={'primitive_cap':513,'terminal_M':[3,5,9,15,31],
 'unchanged_optimum_M':[8,16],'scalar_grid_j':[1,2,3,4],
 'source_cells':96,'sine_cells':8,'physical_prefix':256,
 'all_infinite_gram_tails_included':True,'float_acceptance':False,'broad_campaign':False}
SCHEMA='riemann-terminal-endpoint-v1'
class Refusal(Exception):pass

def need(ok,message):
    if ok is not True:raise Refusal(message)

def exact(q):
    if type(q) is int:return F(q)
    if type(q) is F:return q
    raise TypeError('int or Fraction required')

def integer(n,low=1,high=513):
    if type(n) is not int or not low<=n<=high:raise ValueError('integer outside frozen scope')
    return n

def canonical(o):return (json.dumps(o,sort_keys=True,indent=2,ensure_ascii=True)+'\n').encode()

def strict(path):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise Refusal('duplicate JSON key')
            out[k]=v
        return out
    def reject(x):raise Refusal('floating/nonfinite JSON token')
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=reject,parse_constant=reject)

def manifest(root=ROOT):
    need(not root.is_symlink() and not any(p.is_symlink() for p in root.parents),'symbolic root')
    m=root/'SHA256SUMS';need(m.is_file() and not m.is_symlink(),'missing manifest')
    seen=set()
    for line in m.read_text().splitlines():
        need('  ' in line,'manifest syntax');digest,name=line.split('  ',1)
        q=PurePosixPath(name)
        need(re.fullmatch('[0-9a-f]{64}',digest) is not None,'digest syntax')
        need(name in FILES and name not in seen and '\\' not in name and
             not q.is_absolute() and '..' not in q.parts,'manifest path')
        seen.add(name);p=root/name
        need(p.is_file() and not p.is_symlink(),'missing/symbolic payload')
        need(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'payload digest')
    actual=set()
    for p in root.rglob('*'):
        need(not p.is_symlink(),'symbolic payload')
        if '__pycache__' in p.parts:continue
        if p.is_file() and p.name!='SHA256SUMS':actual.add(p.relative_to(root).as_posix())
    need(seen==FILES==actual,'exact nonempty inventory')

def parent():
    locks={};raw={}
    for n,(sha,blob,size) in PINS.items():
        p=PARENT/n
        need(p.is_file() and not p.is_symlink() and
             not any(q.is_symlink() for q in p.parents),'missing/symbolic parent')
        b=p.read_bytes();need(len(b)==size and hashlib.sha256(b).hexdigest()==sha,'parent digest')
        need(hashlib.sha1(b'blob '+str(size).encode()+b'\0'+b).hexdigest()==blob,'parent blob')
        locks[n]={'sha256':sha,'blob':blob,'bytes':size};raw[n]=b
    need(strict(ROOT/'SOURCE_LOCK.json')=={'schema':'terminal-endpoint-lock-v1',
      'parent_head':HEAD,'parent_directory':PARENT.name,'files':locks,
      'executed_parent_code':['scripts/mathcore.py']},'parent lock mismatch')
    spec=importlib.util.spec_from_file_location('terminal_frozen_green',PARENT/'scripts/mathcore.py')
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m
    exec(compile(raw['scripts/mathcore.py'],str(PARENT/'scripts/mathcore.py'),'exec'),m.__dict__)
    return m

def mobius_table(N):
    integer(N);mu=[1]*(N+1);prime=[True]*(N+1);mu[0]=0
    for p in range(2,N+1):
        if prime[p]:
            for k in range(p,N+1,p):prime[k]=False;mu[k]*=-1
            for k in range(p*p,N+1,p*p):mu[k]=0
    return mu

def scalar(x,mu):
    x=exact(x);need(F(1)<=x<=len(mu)-1,'scalar domain')
    n=x.numerator//x.denominator
    mo=sum(mu[k] for k in range(1,n+1,2))
    harmonic=sum((F(mu[k],k) for k in range(1,n+1,2)),F())
    return F(mo)-x*harmonic

def terminal(M,mu):
    integer(M,3,len(mu)-1);need(M%2==1,'odd cutoff required')
    lam={k:F(mu[k]) for k in range(1,M+1,2)}
    harmonic=sum((v/k for k,v in lam.items()),F())
    lam[M]-=M*harmonic
    return lam

def harmonic_polynomial(lam):
    T=sum(lam.values(),F());mesh={F(),F(1,4)}
    for k in lam:
        for r in range(1,(k+3)//4):
            if F(r,k)<F(1,4):mesh.add(F(r,k))
    mesh=sorted(mesh);a=b=c=F();rows=[]
    for lo,hi in zip(mesh,mesh[1:]):
        x=(lo+hi)/2
        v=sum((co*sum((F((-1)**(r+1),r) for r in range(1,k) if r<k*x),F())
               for k,co in lam.items()),F())
        width=hi-lo;a+=width*T*T;b-=2*width*T*v;c+=width*v*v
        rows.append([str(lo),str(hi),str(v)])
    return (a,b,c),rows

def reconstruct():
    m=parent();I=m.I;mu=mobius_table(CONFIG['primitive_cap']);counts=Counter()
    def check(ok,name):need(ok,name);counts[name]+=1
    for n in range(1,514):
        check(sum(mu[d] for d in range(1,n+1) if n%d==0)==(1 if n==1 else 0),'Mobius_divisor')
        if n<=256:check(mu[n]==m.mu(n),'independent_Mobius')
    scalars=[]
    for j in CONFIG['scalar_grid_j']:
        M=2*j**4+1;q=scalar(F(M),mu)
        direct=-sum((F(mu[k],k)*(M-k) for k in range(1,M+1,2)),F())
        check(q==direct,'scalar_hinge_formula')
        scalars.append({'j':j,'M':M,'Q':str(q),'R':str(q*q/M)})
    # Exact renewal for rational x and exact scalar Mellin identity for a finite source.
    for n in range(2,193):
        x=F(n,2)
        check(sum((scalar(x/d,mu) for d in range(1,n//2+1,2)),F())==1-x,'odd_renewal')
    for M in [3,5,9,15,31]:
        ks=list(range(1,M+1,2))
        for s in [2,3,4]:
            knots=ks+[M+1];total=F()
            for a,b in zip(knots,knots[1:]):
                P=sum(mu[k] for k in ks if k<=a)
                H=sum((F(mu[k],k) for k in ks if k<=a),F())
                total+=F(P,s)*(F(1,a**s)-F(1,b**s))-F(H,s-1)*(F(1,a**(s-1))-F(1,b**(s-1)))
            P=sum(mu[k] for k in ks);H=sum((F(mu[k],k) for k in ks),F());b=M+1
            total+=F(P,s*b**s)-F(H,(s-1)*b**(s-1))
            check(total==-sum((F(mu[k],k**s) for k in ks),F())/F(s*(s-1)),'finite_Mellin_integral')
    for j in [1,2,3]:
        a=2*j**4+1;b=2*(j+1)**4+1
        check(b<=16*a and b-a<=30*j**3,'quartic_mesh_constants')
        for q in range(1,10):
            x=F(a)+F(q,10)*(b-a);ell=((b-x)*scalar(F(a),mu)+(x-a)*scalar(F(b),mu))/(b-a)
            green=sum((F(mu[k],k)*(min(x,k)-a)*(b-max(x,k))/F(b-a)
                       for k in range(a+2,b,2)),F())
            check(scalar(x,mu)-ell==green,'interpolation_identity')
            check(abs(green)<=F((b-a)**2,8*a),'interpolation_bound')
    panels=[]
    cases=[('terminal',M,terminal(M,mu)) for M in CONFIG['terminal_M']]
    cases += [('constrained-parent',M,m.balanced(M)[0]) for M in CONFIG['unchanged_optimum_M']]
    for kind,M,lam in cases:
        m.validate_source(lam);check(lam[1]==1,'source_first_coefficient')
        T=sum(lam.values(),F());B=sum((abs(v)/k for k,v in lam.items()),F())
        if kind=='terminal':
            check(T==scalar(F(M),mu),'terminal_scalar_total')
            for n in range(1,M):check(m.source(lam,n)==1,'exact_horizon')
            if M==9:check(lam[9]!=0 and mu[9]==0,'nonsquarefree_terminal_retained')
            for n in range(1,CONFIG['source_cells']+1):
                left=m.source(lam,n)
                right=1+(n//M-n//(2*M))*T-sum(sum(mu[k] for k in range(1,n//j+1,2)) for j in range(1,n//M+1,2))
                check(left==right,'complete_physical_tail')
        E,rows,tails,pieces=m.energy(lam);(a,b,c),hrows=harmonic_polynomial(lam)
        H=a*m.logq(F(2)).square()+b*m.logq(F(2))+c
        check(H.lo>=0 and a==T*T/4,'complete_harmonic_polynomial')
        check(E.hi<(2*H+32*B*B).lo and H.hi<(4*E+8*B*B).lo,'full_norm_comparison')
        # Parent Green source is checked again, not merely its scalar energy.
        for j in range(1,CONFIG['sine_cells']+1):
            check(m.sine_value(rows,j).contains(m.source(lam,2*j)),'sine_vs_primitive')
        for x in [F(1,11),F(1,7),F(1,4),F(1,3)]:
            C=sum((row['charge'] for row in rows if row['x']>=x),I.of(0))
            V=sum((co*sum((F((-1)**(r+1),r) for r in range(1,k) if r<k*x),F()) for k,co in lam.items()),F())
            diff=m.pi()*C-(T*m.logq(F(2))-V)
            check(diff.lo>=-I.of(4*B).hi and diff.hi<=I.of(4*B).hi,'uniform_harmonic_transfer_fixture')
        prefix=sum((m.source(lam,n)**2/F(n*(n+1)) for n in range(1,257)),F())
        amp=sum(map(abs,lam.values()),F())/2
        check(E.overlaps(I.bounds(prefix,prefix+amp*amp/257)),'independent_physical_energy_enclosure')
        if kind=='terminal':
            R=T*T/M;J=pieces[0]
            check(J.lo>=(I.of(R/16-F(8,M))).lo and J.hi<=(I.of(2*R+F(32,M))).hi,'first_Green_scalar_comparison')
            check(E.lo>I.of(1-F(1,M)).hi and E.hi<I.of(128*M).lo,'unconditional_energy_bounds_fixture')
        panels.append({'kind':kind,'M':M,'weights':{str(k):str(v) for k,v in lam.items()},'T':str(T),'B':str(B),
          'full_energy':E.record(),'first_Green_energy':pieces[0].record(),'harmonic_energy':H.record(),
          'harmonic_polynomial':[str(a),str(b),str(c)],'harmonic_mesh_count':len(hrows),
          'harmonic_mesh_sha256':hashlib.sha256(canonical(hrows)).hexdigest()})
    hostile={1:F(1),3:F(-6),5:F(5)};m.validate_source(hostile)
    check(sum(hostile.values(),F())==0 and m.source(hostile,1)==m.source(hostile,2)==1,'zero_first_harmonic_positive_full')
    E,rows,tails,pieces=m.energy(hostile)
    check(E.lo>I.of(F(2,3)).hi,'hostile_full_energy')
    return {'schema':SCHEMA,'config':CONFIG,'parent_head':HEAD,
      'rh_proved':False,'uniform_full_gain_proved':False,'subpower_scalar_bound_proved':False,
      'scientific_status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED','scalar_grid':scalars,'panels':panels,
      'hostile_full_energy':E.record(),'counts':dict(sorted(counts.items())),'control_total':sum(counts.values())}

def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--check',action='store_true');g.add_argument('--write',type=Path);a=p.parse_args()
    try:
        if a.check:
            manifest();expected=strict(ROOT/'verification.json')
            need(expected.get('schema')==SCHEMA and canonical(expected.get('config'))==canonical(CONFIG),'schema/config')
            for k in ['rh_proved','uniform_full_gain_proved','subpower_scalar_bound_proved']:
                need(expected.get(k) is False,'forbidden mathematical promotion')
        result=reconstruct();raw=canonical(result)
        if a.write:a.write.write_bytes(raw)
        else:need(raw==canonical(expected),'primitive reconstruction mismatch')
        print('PASS_TERMINAL_ENDPOINT controls='+str(result['control_total']))
        print('RH_UNPROVED FULL_GAIN_UNPROVED SCALAR_BOUND_UNPROVED');return 0
    except (Refusal,ValueError,TypeError,KeyError,OSError,ZeroDivisionError) as e:
        print('REFUSED: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
