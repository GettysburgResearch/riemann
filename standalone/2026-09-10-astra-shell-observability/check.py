#!/usr/bin/env python3
"""Exact finite AC27 regressions. No analytic proof or global RH test.

Standard library only; no parent, generator, numerical library or zero oracle.
All acceptance predicates remain active under -O and -OO. Only --write writes.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
PARENT='be78f076b9abe8d8d6a40c14f71d0df36a4e0407'
SCHEMA='AC27/native-shell-observability/v1'

def need(p, message):
    if not p: raise ValueError(message)

def primitive(n):
    """Trial factorization, with Liouville sign and squarefree test."""
    t=n; sign=1; squarefree=True; p=2
    while p*p<=t:
        e=0
        while t%p==0: t//=p; e+=1
        if e: sign*=(-1)**e
        if e>1: squarefree=False
        p+=1
    if t>1: sign=-sign
    return (sign if squarefree else 0),sign

def sieve(N):
    a=[1]*(N+1); marked=[False]*(N+1); a[0]=0
    for p in range(2,N+1):
        if not marked[p]:
            for j in range(p,N+1,p): a[j]*=-1; marked[j]=True
            for j in range(p*p,N+1,p*p): a[j]=0
    return a

def enc(x):
    if isinstance(x,F): return [x.numerator,x.denominator]
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [enc(v) for v in x]
    return x

def canonical(x): return json.dumps(enc(x),sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(x): return sha256(canonical(x)).hexdigest()
def lcm(a,b): return a//gcd(a,b)*b

def bracket(x):
    """Closed outward rational enclosure [lo/2^48,hi/2^48]."""
    den=1<<48; lo=(x*den).__floor__()
    return [lo,lo+1,den]

def native_inverse(X, mu):
    """Integer divisor recurrence first; rational prefix integration second."""
    ds=list(range(1,X,2)); size=len(ds); aa=[]; vv=[]; prev=[F(0)]*size
    for i,n in enumerate(ds):
        row=[0]*size; row[i]=1
        for j,d in enumerate(ds[:i]):
            if n%d==0:
                row=[x-y for x,y in zip(row,aa[j])]
        aa.append(row)
        v=[prev[j]+F(row[j],n) for j in range(size)]
        vv.append(v); prev=v
        for j,d in enumerate(ds):
            expected=mu[n//d] if n%d==0 else 0
            need(row[j]==expected,'divisor recurrence versus Mobius')
    return ds,vv,aa

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def mv(a,x): return [dot(r,x) for r in a]
def norm2(x): return dot(x,x)
def transpose(a): return list(map(list,zip(*a)))

def positive_certificate(a):
    """Independent rational LDL and integer Bareiss leading determinants."""
    N=len(a); work=[r[:] for r in a]; piv=[]
    for k in range(N):
        p=work[k][k]; need(p>0,'LDL not positive'); piv.append(p)
        for i in range(k+1,N):
            for j in range(i,N):
                val=work[j][i]-work[i][k]*work[j][k]/p
                work[j][i]=val; work[i][j]=val
    scale=1
    for r in a:
        for v in r: scale=lcm(scale,v.denominator)
    b=[[int(v*scale) for v in r]for r in a]; determinants=[]; last=1
    for k in range(N):
        p=b[k][k]; need(p>0,'Bareiss not positive'); determinants.append(p)
        for i in range(k+1,N):
            for j in range(k+1,N):
                num=b[i][j]*p-b[i][k]*b[k][j]
                need(num%last==0,'Bareiss divisibility')
                b[i][j]=num//last
        last=p
    running=F(1)
    for k,p in enumerate(piv):
        running*=p
        need(running==F(determinants[k],scale**(k+1)),'LDL versus Bareiss')
    return {'dimension':N,'positive_minors':len(piv),
            'pivots_sha256':digest(piv),'integer_minors_sha256':digest(determinants),
            'scale':scale}

def compute():
    N=729; mu=sieve(N); trial=[0]+[primitive(n)[0]for n in range(1,N+1)]
    need(mu==trial,'primitive Mobius mismatch')
    mob=[F(0)]*(N+1); M=[0]*(N+1)
    for n in range(1,N+1):
        mob[n]=mob[n-1]+(F(mu[n],n)if n%2 else 0)
        M[n]=M[n-1]+(mu[n]if n%2 else 0)
    def Q(x):
        x=F(x); k=x.numerator//x.denominator
        need(0<=k<=N,'Q range')
        return F(M[k])-x*mob[k]

    derivative=[]; deriv_entries=0; trace=F(0)
    cutoffs={3,9,27,81,243,729}
    for n in range(1,N+1,2):
        count=0
        for d in range(1,n+1,2):
            if n%d==0:
                val=F(mu[n//d],n); trace+=val*val
                _,ln=primitive(n); _,ld=primitive(d)
                need(ln*ld*val==F(mu[n//d]**2,n),'Liouville conjugacy')
                count+=mu[n//d]**2; deriv_entries+=1
        if n in cutoffs:
            H=sum((F(1,j)for j in range(1,n+1)),F(0))
            tail=2*(H+2)/n
            need(0<trace<F(3,2),'finite derivative trace')
            need(F(3,2)-trace<=tail,'complete analytic tail regression')
            derivative.append({'through':n,'trace_interval':bracket(trace),
                               'tail_upper_interval':bracket(tail),
                               'exact_sha256':digest([trace,tail])})

    means=[]; inverse_checks=0; mean_checks=0; allV={}
    for A in [3,9,27,81,243]:
        ns,V,aa=native_inverse(3*A,mu); ds=list(range(1,A,2)); L=len(ds)
        actual=[r[:L]for r in V]
        for i,n in enumerate(ns):
            for j,d in enumerate(ds):
                need(actual[i][j]==mob[n//d]/d,'inverse formula'); inverse_checks+=1
        old=actual[:L]; new=actual[L:]; allV[A]=(ds,old,new)
        b=[Q(F(A,d))-Q(F(3*A,d))for d in ds]
        for j in range(L):
            need(2*sum((r[j]for r in new),F(0))==b[j],'mean-row full endpoints')
            mean_checks+=1
        for q in [1,3,9]:
            bb=[b[j]if ds[j]*q<A else F(0) for j in range(L)]
            if norm2(bb)==0: continue
            low=norm2(bb)/(4*A); y=mv(new,bb); x=mv(old,bb)
            need(norm2(y)>=norm2(bb)*low,'native mean witness Cauchy')
            ratios=[low,norm2(y)/norm2(bb),norm2(x)/norm2(bb),
                    low-F(1,100)*norm2(x)/norm2(bb)]
            means.append({'A':A,'relative_q':q,'raw_lower':bracket(ratios[0]),
                          'actual_ratio':bracket(ratios[1]),'old_ratio':bracket(ratios[2]),
                          'C_1_100_lower':bracket(ratios[3]),'exact_sha256':digest(ratios)})

    A=81; ds,old,new=allV[A]; d=len(ds); eta=F(1,100)
    ot=transpose(old); nt=transpose(new)
    gram=[[dot(nt[i],nt[j])-eta*dot(ot[i],ot[j])for j in range(d)]for i in range(d)]
    bands=[]; band_indices=[]
    for lo,hi in [(27,81),(9,27),(3,9),(1,3)]:
        ids=[i for i,v in enumerate(ds)if lo<=v<hi]; band_indices.append(ids)
        block=[[F(3,5)*(i==j)-gram[ids[i]][ids[j]]for j in range(len(ids))]for i in range(len(ids))]
        bands.append({'lower':lo,'upper':hi,'certificate':positive_certificate(block)})
    full=positive_certificate([[F(i==j)-gram[i][j]for j in range(d)]for i in range(d)])
    coarse=[[sum((gram[i][j]for i in a for j in b),F(0))for b in band_indices]for a in band_indices]
    total=sum((sum(r,F(0))for r in coarse),F(0))/d
    diagonal=sum((coarse[i][i]for i in range(4)),F(0))/d
    need(total>F(94,100),'combined witness too small')
    need(diagonal<F(44,100),'band-only witness mismatch')
    need(total-diagonal>F(1,2),'off-diagonal contribution')
    bands_result={'A':A,'eta':eta,'band_C':F(3,5),'band_certificates':bands,
                  'complete_C1_certificate':full,'constant_vector_squared_norm':d,
                  'combined_ratio':bracket(total),'diagonal_ratio':bracket(diagonal),
                  'cross_ratio':bracket(total-diagonal),
                  'polarized_band_gram':[[bracket(x)for x in r]for r in coarse],
                  'exact_gram_sha256':digest(coarse)}

    strip_count=0; threshold_changes=0
    for A in [9,27,81]:
        h=F(2,A)
        for q in [2,3,9]:
            if q>A:continue
            cols=[d for d in range(1,A,2)if d*q>=A]
            chosen=sorted(set([cols[0],cols[len(cols)//2],cols[-1]]))
            for d in chosen:
                td=F(d,A)
                for k in range(1,3*q+1,2):
                    for n in [k*d-2,k*d,k*d+2]:
                        if not 1<=n<3*A:continue
                        sn=F(n,A)
                        for alpha in [F(1,3),F(2,3)]:
                            for beta in [F(1,3),F(2,3)]:
                                s=sn+alpha*h; t=td+beta*h
                                need(abs(1/t-1/td)<=q*q*h,'smooth cell bound')
                                if (sn>=k*td)!=(s>=k*t):
                                    need(abs(s-k*t)<=(1+k)*h,'complete activation strip')
                                    threshold_changes+=1
                                strip_count+=1
    # Algebra of the exact optimized pole-cost constant: not actual zero data.
    costs=[]
    for m in range(1,7):
        k=F(2*m,2*m-1); opt=(k-1)/k**(2*m)
        formula=F((2*m-1)**(2*m-1),(2*m)**(2*m))
        need(opt==formula,'critical multiplicity algebra')
        for z in [k-F(1,10*m),k+F(1,10*m)]:
            need((z-1)/z**(2*m)<opt,'pole-cost stationary control')
        costs.append({'multiplicity':m,'k':k,'normalized_optimum':opt})

    toy=[]
    for r in range(1,9):
        A=3**r; hsum=F(1)+sum((F(4**(k-1),9**k)for k in range(1,r+1)),F(0))
        need(F(6,5)-hsum==F(1,5)*F(4,9)**r,'synthetic compact derivative tail')
        energy=sum((F(2*3**k)*F(2,3)**(2*k)for k in range(r)),F(0))
        need(energy==6*(F(4,3)**r-1),'inherited control energy')
        toy.append({'r':r,'inverse_derivative_factor':hsum,'energy':energy})

    return enc({'schema':SCHEMA,'parent':PARENT,
       'status':'PROPOSED_COMPONENTS; Q_AC26_OPEN; RH_UNPROVED',
       'scope':'finite exact source/matrix/activation tests; analytic theorems are not machine-proved',
       'primitive_mobius_values':N,'native_inverse_entries':inverse_checks,
       'derivative_divisor_positions':deriv_entries,'derivative_traces':derivative,
       'mean_row_entries':mean_checks,'native_mean_probes':means,'cross_bands':bands_result,
       'continuum_strip_positions':strip_count,'threshold_changes':threshold_changes,
       'synthetic_cost_algebra':costs,'inherited_nonnative_controls':toy,
       'analytic_scope':{'derivative_HS_squared':[3,2], 'grid_error_bound':'200 q^6/A',
                        'native_transmission':'unbounded, proved analytically using a critical-line zero',
                        'Q_AC26':'OPEN', 'actual_zero_coordinates_used':0}})

def reject_duplicates(items):
    out={}
    for k,v in items:
        if k in out: raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def load(path):
    return json.loads(path.read_text(),object_pairs_hook=reject_duplicates,
                      parse_float=lambda _: (_ for _ in ()).throw(ValueError('float forbidden')),
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite forbidden')))

def seal(p): return {'payload':p,'sha256':digest(p)}

def accept(obj, expected):
    need(isinstance(obj,dict) and set(obj)=={'payload','sha256'},'envelope shape')
    need(obj['sha256']==digest(obj['payload']),'digest mismatch')
    need(canonical(obj['payload'])==canonical(expected),'primitive mathematical payload mismatch')

def self_test(p):
    accept(seal(p),p); variants=[]
    for key,value in [('parent','0'*40),('primitive_mobius_values',1),
                      ('native_inverse_entries',0),('continuum_strip_positions',0),
                      ('status','RH_PROVED')]:
        z=deepcopy(p); z[key]=value; variants.append(z)
    z=deepcopy(p); z['cross_bands']['band_C']=[1,10]; variants.append(z)
    z=deepcopy(p); z['cross_bands']['combined_ratio']=[0,1]; variants.append(z)
    z=deepcopy(p); z['native_mean_probes'][0]['raw_lower']=[0,1]; variants.append(z)
    z=deepcopy(p); z['derivative_traces'].pop(); variants.append(z)
    z=deepcopy(p); z['analytic_scope']['Q_AC26']='PROVED'; variants.append(z)
    need(len({digest(z)for z in variants})==10,'duplicate/noop mutation')
    for z in variants:
        need(z!=p,'no-op mutation')
        try: accept(seal(z),p)
        except ValueError: pass
        else: raise ValueError('resealed mutation accepted')
    return len(variants)

def authenticate():
    path=ROOT/'MANIFEST.sha256'; lines=path.read_text().splitlines(); seen=set()
    expected={'README.md','PROOF.md','ATTEMPT.md','SOURCES.json','VALIDATION.md','check.py','results.json'}
    for line in lines:
        h,name=line.split('  ')
        need(name in expected and name not in seen,'manifest names')
        f=ROOT/name; need(not f.is_symlink(),'symlink not accepted')
        need(sha256(f.read_bytes()).hexdigest()==h,'file hash '+name); seen.add(name)
    need(seen==expected,'manifest coverage')

def main():
    parser=argparse.ArgumentParser(); g=parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path); g.add_argument('--check',type=Path)
    parser.add_argument('--self-test',action='store_true'); args=parser.parse_args()
    p=compute(); sealed=seal(p)
    if args.write: args.write.write_bytes(canonical(sealed)+b'\n')
    else: authenticate(); accept(load(args.check),p)
    count=self_test(p)if args.self_test else 0
    print('PASS',sealed['sha256'],'resealed_rejections',count)
    print('native_inverse_entries',p['native_inverse_entries'],'mean_row_entries',p['mean_row_entries'],
          'strip_positions',p['continuum_strip_positions'])
if __name__=='__main__': main()
