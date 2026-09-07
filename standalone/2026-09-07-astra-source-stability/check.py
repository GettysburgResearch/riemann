#!/usr/bin/env python3
"""Bounded exact controls, not machine verification of the analytic theorem."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

FILES = ('PROOF.md','README.md','REVIEW.md','SOURCES.md','SOURCE_LOCK.json',
         'VALIDATION.md','check.py','test_check.py','verification.json')
PARENT = {
 'repository':'GettysburgResearch/riemann', 'pr':812,
 'commit':'cc5277c34fdbc48787cf650b4627a44a77862f1d',
 'path':'standalone/2026-09-07-astra-future-realization/PROOF.md',
 'size':17291,
 'git_blob':'cd5d68c82169f32da6b41eb788b7313ed5d7e547',
 'sha256':'a50fe8b3f8b1f7d974058144173f6b48e51961178126008e8852868cc837079e'}
CONFIG = {'ranks':[0,1,2,3,7,15,31,255,65535,2**32-1,2**64-1],
          'constant_n_max':256, 'synthetic_gram_n_max':16,
          'rational_model_m':[1,2,3], 'eta_denominators':[1024,4096,16384]}

class Rejection(ValueError): pass

def require(condition: bool, message: str) -> None:
    if not condition: raise Rejection(message)

def pairs_no_duplicates(pairs):
    result={}
    for k,v in pairs:
        require(k not in result,'duplicate JSON key')
        result[k]=v
    return result

def bad_number(s):
    raise Rejection('floating or nonfinite JSON number prohibited')

def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=pairs_no_duplicates,
                      parse_float=bad_number, parse_constant=bad_number)

def canonical(obj):
    return json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=True)+'\n'

def strict_same(a,b):
    if type(a) is not type(b): return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(strict_same(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(strict_same(x,y) for x,y in zip(a,b))
    return a==b

def sha(data): return hashlib.sha256(data).hexdigest()

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def powpoly(a,n):
    out=[Q(1)]
    for _ in range(n): out=mul(out,a)
    return out

def solve(a,b):
    n=len(b); m=[[Q(x) for x in row]+[Q(y)] for row,y in zip(a,b)]
    for j in range(n):
        k=next((k for k in range(j,n) if m[k][j]),None)
        require(k is not None,'singular finite rational matrix')
        m[j],m[k]=m[k],m[j]
        t=m[j][j]; m[j]=[x/t for x in m[j]]
        for k in range(n):
            if k!=j:
                t=m[k][j]; m[k]=[x-t*y for x,y in zip(m[k],m[j])]
    return [row[-1] for row in m]

def parameters(k):
    require(type(k) is int and k>=0,'bad rank')
    n=k+1; ell=n.bit_length(); L=23+6*ell; a=16+4*ell
    q=3+2*L*(4*a+15)
    r=isqrt(k+4); r+=int(r*r<k+4)
    old_bits=13*r+2*(n-1).bit_length()
    return {'K':k,'n':n,'ell':ell,'L':L,'a':a,'floor_bits':q,
            'prior_conservative_floor_bits':old_bits,
            'combined_floor_bits':min(q,old_bits),
            'source_time_cutoff':4*(q+ell+10)}

def rational_model(m,eta):
    # Error: [(z+eta)^m-z^m]/[(z+eta)^m(z+1)^(m+1)].
    den=mul(powpoly([eta,1],m),powpoly([1,1],m+1))
    size=len(den)-1
    columns=[]; labels=[]
    for r,kmax in [(eta,m),(Q(1),m+1)]:
        for k in range(1,kmax+1):
            if r==eta:
                col=mul(powpoly([eta,1],m-k),powpoly([1,1],m+1))
            else:
                col=mul(powpoly([eta,1],m),powpoly([1,1],m+1-k))
            columns.append(col+[Q(0)]*(size-len(col)))
            labels.append((r,k))
    numerator=powpoly([eta,1],m); numerator[-1]-=1
    numerator +=[Q(0)]*(size-len(numerator))
    coeff=solve([[c[i] for c in columns] for i in range(size)],numerator)
    terms=[(r,k-1,c/Q(factorial(k-1))) for (r,k),c in zip(labels,coeff)]
    energy=Q(0)
    for r,j,c in terms:
        for s,k,d in terms:
            energy+=c*d*factorial(j+k)/(r+s)**(j+k+1)
    input_energy=Q(factorial(2*m-2),factorial(m-1)**2)/(2*eta)**(2*m-1)
    return energy,input_energy,coeff,columns,numerator

def reconstruct():
    counts=Counter()
    def check(ok,group):
        require(bool(ok),'control failed: '+group); counts[group]+=1
    B=[Q(1)]
    for n in range(1,6): B.append(-sum(Q(comb(n+1,k))*B[k] for k in range(n))/Q(n+1))
    poly=[Q(comb(5,k))*B[5-k] for k in range(6)]
    check(poly==[0,Q(-1,6),0,Q(5,3),Q(-5,2),1],'bernoulli_source')
    check(sum(abs(c) for c in poly)==Q(16,3),'bernoulli_source')
    check(sum(poly)==0 and poly[0]==0,'bernoulli_source')
    check(sum(c/Q(i+1) for i,c in enumerate(poly))==0,'bernoulli_source')
    U=Q(10)
    check(1+U/2+U**2/12+U**4/720+U**6/40 <=U**6,'euler_maclaurin_majorant')
    check(2*12**6<2**23,'euler_maclaurin_majorant')
    check(Q(4,3)-1>0 and Q(1,3)/Q(4,3)==Q(1,4),'jensen_harnack_constants')
    check(Q(1,7)/Q(8,7)==Q(1,8),'jensen_harnack_constants')
    for R in [Q(5,2),Q(8,3),Q(11,4),Q(17,6),Q(3)]:
        check((R+Q(3,2))/(R-Q(3,2))<=4 and R+Q(3,2)<8,'jensen_harnack_constants')
    for n in range(1,CONFIG['constant_n_max']+1):
        p=parameters(n-1); ell,L,a=p['ell'],p['L'],p['a']
        check(n+1<=2**ell and 2**(ell-1)<n+1,'rank_constants')
        check(4*n+14<=12*(n+1),'rank_constants')
        check(8*(8*n+9)*L<=72*(n+1)*L,'cover_constants')
        check(L<=2**(ell+4),'cover_constants')
        lost=Q(96*n*(n+1)*L,2**a)
        check(lost<=Q(3,256)<Q(1,64),'cover_constants')
        check(1-Q(1,12)-lost>Q(1,2),'cover_constants')
        check(p['floor_bits']==3+2*L*(4*a+15),'floor_formula')
    # All-H proof reduces these exponential comparison inequalities to induction.
    check(4*5+3<=2**5,'cutoff_induction')
    for H in range(5,65):
        check(4*(H+1)+3<=2*(4*H+3),'cutoff_induction')
    panels=[parameters(k) for k in CONFIG['ranks']]
    for p in panels:
        check(p['floor_bits']>=1 and p['source_time_cutoff']==4*(p['floor_bits']+p['ell']+10),'rank_panels')
    check(panels[-1]['floor_bits']<panels[-1]['prior_conservative_floor_bits'],'asymptotic_comparison_fixture')
    synth=[]
    for n in range(1,CONFIG['synthetic_gram_n_max']+1):
        G=[[Q(5 if i==j else (-2 if abs(i-j)==1 else 0)) for j in range(n)] for i in range(n)]
        c=solve(G,[Q(1)]+[Q(0)]*(n-1))
        fitted=mul([1,-2],c); err=[-x for x in fitted]; err[0]+=1
        energy=sum(x*x for x in err)
        expected=Q(3*4**n,4**(n+1)-1)
        check(energy==1-c[0]==expected,'nonouter_projection')
        check(energy>Q(3,4),'nonouter_projection')
        for seed in [1,2,3]:
            v=[Q((j+seed)%5-2,j+1) for j in range(n)]
            vnorm=sum(x*x for x in v)
            inorm=sum(x*x for x in mul([1,-2],v))
            onorm=sum(x*x for x in mul([2,-1],v))
            check(inorm==onorm and inorm>=vnorm,'inner_modulus_control')
        synth.append({'n':n,'squared_error':str(energy)})
    models=[]
    for m in CONFIG['rational_model_m']:
        for N in CONFIG['eta_denominators']:
            eta=Q(1,N); ee,vv,cc,cols,nn=rational_model(m,eta)
            check(all(sum(c*col[j] for c,col in zip(cc,cols))==nn[j] for j in range(len(nn))),'rational_model_transform')
            check(ee>0 and vv>0,'rational_model_energy')
            check(ee<=Q(1,16*(m+1)),'rational_model_small_error')
            check(vv*ee**(2*m-1)>=Q(1,8**(2*m)),'input_blowup_bound')
            models.append({'m':m,'eta':str(eta),'error_squared':str(ee),'input_norm_squared':str(vv)})
    return {'schema':'QP26-source-stability-v1','status':'PROPOSED_COMPONENT_PROOFS_REVIEW_REQUIRED',
       'rh_proved':False,'growing_horizon_bound_proved':False,
       'new_actual_source_numerical_energy_certificate':False,'config':CONFIG,
       'parent':PARENT,'groups':dict(sorted(counts.items())),'bounded_controls':sum(counts.values()),
       'rank_panels':panels,'nonouter_controls':synth,'rational_boundary_models':models}

def inventory(root):
    require(root.is_dir() and not root.is_symlink(),'bad packet root')
    seen=set()
    for p in root.rglob('*'):
        require(not p.is_symlink(),'symlink in packet')
        if p.is_file(): seen.add(p.relative_to(root).as_posix())
    require(seen==set(FILES)|{'SHA256SUMS'},'missing or extra packet file')
    entries={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        parts=line.split('  ')
        require(len(parts)==2,'bad manifest line')
        digest,name=parts
        require(name in FILES and name not in entries,'bad or duplicate manifest path')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'bad hash')
        entries[name]=digest
    require(set(entries)==set(FILES),'empty or incomplete manifest')
    for name,digest in entries.items(): require(sha((root/name).read_bytes())==digest,'hash mismatch: '+name)
    require(strict_same(load(root/'SOURCE_LOCK.json'),PARENT),'source lock mismatch')

def authenticate_parent(path):
    require(path.is_file() and not path.is_symlink(),'missing parent proof')
    b=path.read_bytes(); blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    require(len(b)==PARENT['size'] and sha(b)==PARENT['sha256'] and blob==PARENT['git_blob'],'parent proof identity')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--parent',type=Path); ap.add_argument('--reconstruct',action='store_true')
    args=ap.parse_args()
    try:
        if args.reconstruct:
            print(canonical(reconstruct()),end=''); return 0
        inventory(args.root)
        if args.parent: parent=args.parent
        else: parent=args.root.parent/'2026-09-07-astra-future-realization'/'PROOF.md'
        authenticate_parent(parent)
        out=reconstruct()
        require(strict_same(load(args.root/'verification.json'),out),'primitive result mismatch')
        print(canonical({'result':'PASS_SCOPED_BOUNDED_CONTROLS','bounded_controls':out['bounded_controls'],
                         'groups':out['groups'],'rh_proved':False,
                         'verification_sha256':sha(canonical(out).encode())}),end='')
        return 0
    except (Rejection,ValueError,OSError,TypeError,KeyError) as e:
        print('REJECT: '+str(e),file=sys.stderr); return 2
if __name__=='__main__': raise SystemExit(main())
