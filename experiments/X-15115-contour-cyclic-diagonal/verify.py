#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, itertools, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.gw-contour-cyclic-diagonal.v1"

def rat(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("boolean is not rational")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, dict) and set(x)=={"numerator","denominator"}:
        n,d=x["numerator"],x["denominator"]
        if isinstance(n,bool) or isinstance(d,bool) or not isinstance(n,int) or not isinstance(d,int) or d==0:
            raise ValueError("malformed rational")
        return Fraction(n,d)
    raise ValueError(f"unsupported rational {x!r}")

def dr(x: Fraction) -> Any:
    return x.numerator if x.denominator==1 else {"numerator":x.numerator,"denominator":x.denominator}

def mat(data: Any) -> list[list[Fraction]]:
    if not isinstance(data,list) or not data or any(not isinstance(r,list) for r in data):
        raise ValueError("matrix required")
    A=[[rat(x) for x in r] for r in data]
    n=len(A)
    if any(len(r)!=n for r in A):
        raise ValueError("square matrix required")
    return A

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def tp(A):
    return [list(r) for r in zip(*A)]

def eye(n):
    return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]

def inv(A):
    n=len(A)
    aug=[A[i][:]+eye(n)[i] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if aug[i][k]),None)
        if p is None: raise ValueError("singular matrix")
        aug[k],aug[p]=aug[p],aug[k]
        q=aug[k][k]
        aug[k]=[v/q for v in aug[k]]
        for i in range(n):
            if i==k: continue
            q=aug[i][k]
            if q:
                aug[i]=[aug[i][j]-q*aug[k][j] for j in range(2*n)]
    return [r[n:] for r in aug]

def det(A):
    n=len(A); B=[r[:] for r in A]; ans=Fraction(1)
    for k in range(n):
        p=next((i for i in range(k,n) if B[i][k]),None)
        if p is None:return Fraction(0)
        if p!=k:B[k],B[p]=B[p],B[k];ans=-ans
        q=B[k][k]; ans*=q
        for i in range(k+1,n):
            if B[i][k]:
                f=B[i][k]/q
                for j in range(k+1,n): B[i][j]-=f*B[k][j]
    return ans

def require_spd(A):
    vals=[]
    for k in range(1,len(A)+1):
        d=det([r[:k] for r in A[:k]])
        if d<=0: raise ValueError("Gram not positive definite")
        vals.append(d)
    return vals

def powm(A,n):
    P=eye(len(A))
    for _ in range(n): P=mm(P,A)
    return P

def direct_cycle(B,Gi,ell):
    n=len(B); out=Fraction(0)
    for inds in itertools.product(range(n),repeat=2*ell):
        aa=inds[0::2]; bb=inds[1::2]; z=Fraction(1)
        for j in range(ell):
            z*=B[aa[j]][bb[j]]*Gi[bb[j]][aa[(j+1)%ell]]
        out+=z
    return out

def verify(data):
    if data.get("schema")!=SCHEMA: raise ValueError("wrong schema")
    G=mat(data["gram"]); B=mat(data["seam"])
    if len(G)!=len(B):raise ValueError("dimension mismatch")
    piv=require_spd(G); Gi=inv(G); T=mm(Gi,B)
    supplied={int(k):rat(v) for k,v in data["orders"].items()}
    if set(supplied)!=set(range(2,7)): raise ValueError("orders 2..6 required")
    moments={}
    for ell in range(2,7):
        v=tr(powm(T,ell)); moments[ell]=v
        if supplied[ell]!=v: raise ValueError(f"moment mismatch {ell}")
    q4=direct_cycle(B,Gi,4)
    if rat(data["order_four_direct"])!=q4 or q4!=moments[4]:
        raise ValueError("order-four contour cycle mismatch")
    disc=moments[2]**2
    if rat(data["order_four_disconnected"])!=disc:
        raise ValueError("disconnected order-four mismatch")
    if disc==q4: raise ValueError("control does not separate connected/disconnected contractions")
    if rat(data["one_contour_order_four_compatible"])!=q4:
        raise ValueError("compatible diagonal value mismatch")
    alt=rat(data["one_contour_order_four_alternative"])
    if alt==q4:
        raise ValueError("alternative diagonal lift must demonstrate nonuniqueness")
    C=rat(data["hs_bound"]); r=rat(data["series_radius"])
    if C<=0 or r<=0 or C*r>=1:raise ValueError("invalid majorant parameters")
    for ell,v in moments.items():
        if abs(v)>C**ell:raise ValueError("HS geometric moment bound fails")
    maj=C*C*r/(1-C*r)
    if rat(data["series_majorant"])!=maj:raise ValueError("series majorant mismatch")
    Cb=mat(data["basis_change"])
    if len(Cb)!=len(G):raise ValueError("basis dimension mismatch")
    inv(Cb)
    Gp=mm(tp(Cb),mm(G,Cb)); Bp=mm(tp(Cb),mm(B,Cb))
    Tp=mm(inv(Gp),Bp)
    for ell,v in moments.items():
        if tr(powm(Tp,ell))!=v:raise ValueError("basis invariance failure")
    canon=json.dumps(data,sort_keys=True,separators=(",",":")).encode()
    return {
      "status":"CERTIFIED_CONTOUR_CYCLIC_OBJECT_AND_DIAGONAL_GAP",
      "dimension":len(G),
      "gram_leading_minors":[dr(x) for x in piv],
      "trace_moments":{str(k):dr(v) for k,v in moments.items()},
      "connected_order_four":dr(q4),
      "disconnected_order_four":dr(disc),
      "alternative_one_contour_order_four":dr(alt),
      "series_majorant":dr(maj),
      "basis_invariance":"PASS",
      "scope":"constructed product-contour cyclic pullback; one-contour diagonal identity not supplied",
      "certificate_sha256":hashlib.sha256(canon).hexdigest()
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument("certificate",type=Path)
    a=p.parse_args(); print(json.dumps(verify(json.loads(a.certificate.read_text())),indent=2,sort_keys=True))

if __name__=="__main__":main()
