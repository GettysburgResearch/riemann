#!/usr/bin/env python3
"""Bounded rational controls; these do not prove the analytic zero-density input."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'result.json', 'SHA256SUMS'}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def mm(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return [list(x) for x in zip(*A)]

def inv2(A):
    a,b=A[0];c,d=A[1]
    det=a*d-b*c
    need(det!=0,'singular matrix')
    return [[d/det,-b/det],[-c/det,a/det]]

def dot(u,v):
    return sum((x*y for x,y in zip(u,v)), F(0))

def reconstruct():
    pairs=[]
    for n in range(3,27):
        t=F(1,n)
        a=(1-t*t)/(1+t*t); b=2*t/(1+t*t)
        u=[a,b]; v=[a,-b]; c=dot(u,v)
        need(dot(u,u)==dot(v,v)==1 and 0<c<1,'unit pair')
        # Exact metric making the two eigenvectors orthogonal.
        G=[[b*b,F(0)],[F(0),a*a]]
        V=[[a,a],[b,-b]]
        Vi=inv2(V)
        D=[[F(1),F(0)],[F(0),F(2)]]
        L=mm(mm(V,D),Vi)
        need(mm(G,L)==mm(tr(L),G),'metric symmetry')
        need(dot(u, [b*b*v[0],a*a*v[1]])==0,'G orthogonality')
        ratio=a*a/(b*b)
        need(ratio==(1+c)/(1-c),'sharp metric constant')
        # Spectral projector onto u along v.
        P=mm(mm(V,[[F(1),F(0)],[F(0),F(0)]]),Vi)
        need(mm(P,P)==P,'projection idempotence')
        need(mm(P,[[u[0]],[u[1]]])==[[u[0]],[u[1]]],'projection keeps u')
        need(mm(P,[[v[0]],[v[1]]])==[[F(0)],[F(0)]],'projection removes v')
        PP=mm(tr(P),P)
        need(PP[0][0]+PP[1][1]==1/(1-c*c),'sharp projector norm')
        need(PP[0][0]*PP[1][1]-PP[0][1]*PP[1][0]==0,'rank one')
        pairs.append([n,str(c),str(ratio),str(PP[0][0]+PP[1][1])])
    # Finite pigeonhole controls, not zeta zeros.
    for n in range(3,27):
        U=F(n+1)
        pts=[U+3*U*F(j*j,n*n) for j in range(n+1)]
        gaps=[pts[j+1]-pts[j] for j in range(n)]
        need(sum(gaps)==3*U and min(gaps)<=3*U/n,'gap accounting')
    # Constants in the elementary threshold and norm conversions.
    need(F(4,1)/24**2==F(1,144),'exponential metric height constant')
    need(F(1,4)/24**2==F(1,2304),'sine metric height constant')
    need(F(2,5)*4-1==F(3,5),'density difference')
    need(F(3,5)/2>F(1,4),'safe point-count coefficient')
    need(F(3)/(F(1,8))==24,'point versus gap slack')
    need(F(1)/24==F(1,24),'exponential projector constant')
    need(F(1,4)/24==F(1,96),'sine projector constant')
    need(F(4)**2/2==8,'normalized sine overlap constant')
    payload=json.dumps(pairs,separators=(',',':')).encode()
    return {
        'schema':1,
        'status':'PROPOSED_COMPONENT_PROOF_NOT_RH',
        'parent_commit':'f0e34780f4fe91bd5d07e791e8855189838c3df5',
        'bounded_groups':{
            'rational_eigenvector_metric_projection_pairs':len(pairs),
            'synthetic_pigeonhole_configurations':24,
            'rational_constant_identities':8},
        'pair_sha256':hashlib.sha256(payload).hexdigest(),
        'rh_proved':False,
        'actual_zeros_computed':0,
        'analytic_theorems_machine_proved':False}

def strict_load(path):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key')
            out[k]=v
        return out
    def nofloat(s):
        raise ValueError('floating JSON literal not accepted')
    return json.loads(Path(path).read_text(encoding='utf-8'),
                      object_pairs_hook=pairs,parse_float=nofloat,
                      parse_constant=nofloat)

def authenticate():
    actual={p.name for p in ROOT.iterdir()}
    need(actual==FILES,'file inventory differs')
    need(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in FILES),
         'non-regular or symlink packet entry')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,n=line.split('  ',1)
        need(n not in entries and n in FILES-{'SHA256SUMS'},'manifest path')
        need(len(h)==64,'manifest hash length')
        entries[n]=h
    need(set(entries)==FILES-{'SHA256SUMS'},'incomplete manifest')
    for n,h in entries.items():
        need(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h,'hash mismatch: '+n)
    source=strict_load(ROOT/'SOURCES.json')
    need(source['parent_commit']=='f0e34780f4fe91bd5d07e791e8855189838c3df5',
         'source drift')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',action='store_true',help='producer mode; does not authenticate')
    group.add_argument('--check',type=Path)
    args=ap.parse_args()
    expected=reconstruct()
    if args.check:
        authenticate()
        got=strict_load(args.check)
        need(json.dumps(got,sort_keys=True,separators=(',',':'))==
             json.dumps(expected,sort_keys=True,separators=(',',':')),'result differs')
    print(json.dumps(expected,indent=2,sort_keys=True))

if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError) as e:
        print('REJECT: '+str(e),file=sys.stderr)
        sys.exit(1)
