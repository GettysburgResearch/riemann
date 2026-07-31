#!/usr/bin/env python3
"""Exact Fraction-only verifier for L-15610/T-15603 terminal-prime visible gates."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
from typing import Any

class CertificateError(ValueError): pass

def integer(x: Any, name: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int): raise CertificateError(f"{name} must be integer")
    return x

def frac(x: Any, name: str) -> Fraction:
    if not isinstance(x, dict): raise CertificateError(f"{name} must be rational object")
    n=integer(x.get('numerator'), name+'.numerator'); d=integer(x.get('denominator'), name+'.denominator')
    if d<=0: raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n,d)

def fj(x: Fraction): return {'numerator':x.numerator,'denominator':x.denominator}

def vec(x: Any,name:str):
    if not isinstance(x,list) or not x: raise CertificateError(f"{name} must be nonempty list")
    return [frac(v,f"{name}[{i}]") for i,v in enumerate(x)]

def mat(x: Any,name:str):
    if not isinstance(x,list) or not x: raise CertificateError(f"{name} must be nonempty matrix")
    rows=[]; n=len(x)
    for i,row in enumerate(x):
        if not isinstance(row,list) or len(row)!=n: raise CertificateError(f"{name} must be square")
        rows.append([frac(v,f"{name}[{i}][{j}]") for j,v in enumerate(row)])
    if any(rows[i][j]!=rows[j][i] for i in range(n) for j in range(n)): raise CertificateError(f"{name} must be symmetric")
    return rows

def eye(n): return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A))] for i in range(len(A))]
def scale(c,A): return [[c*v for v in row] for row in A]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def outer(v,w): return [[v[i]*w[j] for j in range(len(w))] for i in range(len(v))]

def inverse(A):
    n=len(A); aug=[A[i][:]+eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if aug[i][k]),None)
        if pivot is None: raise CertificateError('singular matrix')
        aug[k],aug[pivot]=aug[pivot],aug[k]
        p=aug[k][k]; aug[k]=[x/p for x in aug[k]]
        for i in range(n):
            if i!=k:
                q=aug[i][k]
                aug[i]=[aug[i][j]-q*aug[k][j] for j in range(2*n)]
    return [row[n:] for row in aug]

def ldl_pivots(A, strict=True):
    n=len(A); L=eye(n); D=[]
    for j in range(n):
        d=A[j][j]-sum(L[j][k]*L[j][k]*D[k] for k in range(j))
        if strict and d<=0: raise CertificateError('matrix is not positive definite')
        if not strict and d<0: raise CertificateError('matrix is not positive semidefinite')
        D.append(d)
        if d==0:
            for i in range(j+1,n):
                r=A[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j))
                if r: raise CertificateError('zero pivot has nonzero column')
        else:
            for i in range(j+1,n):
                L[i][j]=(A[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/d
    return D

def canonical_sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def verify(data):
    if data.get('schema')!='riemann.x15604-terminal-visible.v1': raise CertificateError('bad schema')
    if data.get('classification')!='SYNTHETIC_MODEL': raise CertificateError('bad classification')
    G=mat(data['metric'],'metric'); E=mat(data['centered_terminal'],'centered_terminal'); n=len(G)
    if len(E)!=n: raise CertificateError('dimension mismatch')
    vm=vec(data['v_minus'],'v_minus'); vp=vec(data['v_plus'],'v_plus')
    if len(vm)!=n or len(vp)!=n: raise CertificateError('vector dimension mismatch')
    p=frac(data['pole_scale'],'pole_scale')
    if p<=0: raise CertificateError('pole scale must be positive')
    raw=mat(data['raw_terminal'],'raw_terminal')
    u=[p*vm[i]-vp[i]/p for i in range(n)]
    polar=scale(Fraction(-2),outer(u,u))
    finite=add(scale(2,add(outer(vm,vp),outer(vp,vm))),scale(Fraction(-2,p*p),outer(vp,vp)))
    if add(raw,polar)!=add(E,finite): raise CertificateError('pole cancellation identity failed')
    theta=frac(data['theta'],'theta'); sigma=frac(data['sigma_squared'],'sigma_squared')
    omega=frac(data['omega'],'omega'); h=frac(data['h'],'h')
    if theta<0 or sigma<0 or omega<0 or h<=0: raise CertificateError('invalid scalar gate')
    Gi=inverse(G)
    norm_moat=sub(scale(theta*theta,G),mm(mm(E,Gi),E))
    norm_piv=ldl_pivots(norm_moat,strict=False)
    beta=sigma-theta-omega-omega*omega/h
    if beta<=0: raise CertificateError('visible margin is not positive')
    radical=frac(data['radical_loss'],'radical_loss'); cross=frac(data['radical_cross_loss'],'radical_cross_loss'); delta=frac(data['assembly_radius'],'assembly_radius')
    if min(radical,cross,delta)<0: raise CertificateError('losses must be nonnegative')
    floor=-(radical+cross+delta)
    proof={'metric':[[fj(x) for x in r] for r in G], 'centered_terminal':[[fj(x) for x in r] for r in E], 'theta':fj(theta),'norm_moat_pivots':[fj(x) for x in norm_piv], 'visible_margin':fj(beta),'ambient_floor':fj(floor)}
    return {'schema':'riemann.x15604-terminal-visible-verification.v1','classification':'SYNTHETIC_MODEL','analytic_claims':['L-15610','T-15603'],'visible_margin':fj(beta),'ambient_floor':fj(floor),'norm_moat_pivots':[fj(x) for x in norm_piv], 'pole_cancellation_verified':True,'exact_proof_object_sha256':canonical_sha(proof),'verdict':'CERTIFIED_TERMINAL_VISIBLE_MARGIN'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('certificate',type=Path); ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    try: out=verify(json.loads(a.certificate.read_text()))
    except (OSError,json.JSONDecodeError,CertificateError) as e:
        print(json.dumps({'verified':False,'error':str(e)},indent=2),file=sys.stderr); return 2
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output: a.output.write_text(text)
    print(text,end=''); return 0
if __name__=='__main__': raise SystemExit(main())