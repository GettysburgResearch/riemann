#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = 'riemann.x18508.deficit-projector-bridge.v1'

def q(x: Any) -> Fraction:
    if isinstance(x, bool): raise ValueError('bool is not a rational')
    if isinstance(x, int): return Fraction(x)
    if isinstance(x, str): return Fraction(x)
    raise ValueError(f'unsupported rational {x!r}')
def mat(x: Any):
    if not isinstance(x,list) or not x or not all(isinstance(r,list) for r in x): raise ValueError('matrix')
    n=len(x[0])
    if n==0 or any(len(r)!=n for r in x): raise ValueError('ragged matrix')
    return [[q(v) for v in r] for r in x]
def shape(A): return len(A),len(A[0])
def transpose(A): return [list(r) for r in zip(*A)]
def mm(A,B):
    if shape(A)[1]!=shape(B)[0]: raise ValueError('product mismatch')
    return [[sum((a*b for a,b in zip(r,c)),Fraction(0)) for c in transpose(B)] for r in A]
def add(A,B,sign=1):
    if shape(A)!=shape(B): raise ValueError('sum mismatch')
    return [[A[i][j]+sign*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,s): return [[s*v for v in r] for r in A]
def congr(A,Y): return mm(transpose(Y),mm(A,Y))
def sym(A): return A==transpose(A)
def zero(A): return all(v==0 for r in A for v in r)
def hcat(A,B):
    if len(A)!=len(B): raise ValueError('hcat')
    return [A[i]+B[i] for i in range(len(A))]
def rank(A):
    M=[r[:] for r in A];m,n=shape(M);row=0
    for col in range(n):
        piv=next((i for i in range(row,m) if M[i][col]),None)
        if piv is None: continue
        M[row],M[piv]=M[piv],M[row];p=M[row][col];M[row]=[v/p for v in M[row]]
        for i in range(m):
            if i!=row and M[i][col]:
                f=M[i][col];M[i]=[M[i][j]-f*M[row][j] for j in range(n)]
        row+=1
        if row==m: break
    return row
def ldl_pivots(A):
    if not sym(A) or len(A)!=len(A[0]): raise ValueError('LDL square symmetric')
    n=len(A);L=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)];D=[]
    for k in range(n):
        p=A[k][k]-sum((L[k][j]*L[k][j]*D[j] for j in range(k)),Fraction(0))
        if p==0: raise ValueError('zero LDL pivot')
        D.append(p)
        for i in range(k+1,n):
            L[i][k]=(A[i][k]-sum((L[i][j]*L[k][j]*D[j] for j in range(k)),Fraction(0)))/p
    return D
def pd(A):
    p=ldl_pivots(A)
    if not all(v>0 for v in p): raise ValueError(f'not positive definite: {p}')
    return p
def canonical_sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def outmat(A): return [[str(v) for v in r] for r in A]

def verify(doc):
    if doc.get('schema')!=SCHEMA: raise ValueError('schema')
    G,D,Q0,YD,YC,YS=map(mat,(doc['G'],doc['D'],doc['Q0'],doc['Y_D'],doc['Y_C'],doc['source_Y']));theta=q(doc['theta']);n=len(G)
    if shape(G)!=(n,n) or shape(D)!=(n,n) or not sym(G) or not sym(D): raise ValueError('ambient matrices')
    gp=pd(G);dp=pd(D)
    if shape(Q0)[0]!=n: raise ValueError('Q0 dimension')
    m=shape(Q0)[1]
    if any(shape(Y)[0]!=m for Y in (YD,YC,YS)): raise ValueError('coordinate dimension')
    r=shape(YD)[1]
    if shape(YS)[1]!=r or shape(YC)[1]!=m-r: raise ValueError('split dimensions')
    if rank(hcat(YD,YC))!=m or rank(YS)!=r: raise ValueError('rank')
    G0=congr(G,Q0);D0=congr(D,Q0);g0p=pd(G0)
    mc=mm(transpose(YC),mm(G0,YD));dc=mm(transpose(YC),mm(D0,YD))
    if not zero(mc): raise ValueError('metric cross')
    if not zero(dc): raise ValueError('deficit cross')
    high=congr(add(D0,scale(G0,theta),-1),YD);low=congr(add(scale(G0,theta),D0,-1),YC)
    hp=pd(high);lp=pd(low);same=rank(hcat(YD,YS))==r;actual='EQUAL' if same else 'NOT_EQUAL'
    if doc.get('expected_source_relation')!=actual: raise ValueError('source relation')
    out={'schema':'riemann.x18508.deficit-projector-verification.v1','theta':str(theta),'ambient_metric_pivots':[str(v) for v in gp],'ambient_deficit_pivots':[str(v) for v in dp],'complement_metric_pivots':[str(v) for v in g0p],'high_gap_pivots':[str(v) for v in hp],'low_gap_pivots':[str(v) for v in lp],'metric_cross':outmat(mc),'deficit_cross':outmat(dc),'Q_D':outmat(mm(Q0,YD)),'Q_C':outmat(mm(Q0,YC)),'source_equals_deficit':same,'verdict':'CERTIFIED_SOURCE_EQUALS_DEFICIT_CANONICAL' if same else 'CERTIFIED_DEFICIT_CANONICAL_SOURCE_NOT_IDENTIFIED','proof_boundary':'Exact finite spectral bridge. Application requires a production complete positive deficit D_lambda in the declared metric.'}
    out['verification_sha256']=canonical_sha(out);return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();out=verify(json.loads(a.certificate.read_text()));a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
