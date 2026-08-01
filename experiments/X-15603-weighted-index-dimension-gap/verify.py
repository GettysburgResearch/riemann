#!/usr/bin/env python3
"""Exact regression for R-15601.

The checker proves that a source packet may have dimension at least the weighted
threshold index while failing to capture any of the corresponding deficit.
Only Python integers and fractions.Fraction are used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA="riemann.x15603-weighted-index-dimension-gap.v1"
OUT="riemann.x15603-weighted-index-dimension-gap-verification.v1"

class CertificateError(ValueError):
    pass


def integer(x: Any,name: str)->int:
    if isinstance(x,bool) or not isinstance(x,int):
        raise CertificateError(f"{name} must be an integer")
    return x


def frac(raw: Any,name: str)->Fraction:
    if not isinstance(raw,dict):
        raise CertificateError(f"{name} must be a rational object")
    n=integer(raw.get("numerator"),f"{name}.numerator")
    d=integer(raw.get("denominator"),f"{name}.denominator")
    if d<=0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n,d)


def fj(x: Fraction)->dict[str,int]:
    return {"numerator":x.numerator,"denominator":x.denominator}


def matrix(raw: Any,name: str)->list[list[Fraction]]:
    if not isinstance(raw,list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    out=[]
    width=None
    for i,row in enumerate(raw):
        if not isinstance(row,list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        p=[frac(v,f"{name}[{i}][{j}]") for j,v in enumerate(row)]
        if width is None:
            width=len(p)
        if len(p)!=width:
            raise CertificateError(f"{name} has ragged rows")
        out.append(p)
    return out


def shape(a):
    return len(a),len(a[0])


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a,b):
    m,k=shape(a); k2,n=shape(b)
    if k!=k2:
        raise CertificateError("matrix multiplication mismatch")
    return [[sum(a[i][r]*b[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def rank(a):
    m,n=shape(a); x=[row[:] for row in a]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if x[i][c]),None)
        if p is None:
            continue
        x[r],x[p]=x[p],x[r]
        q=x[r][c]
        x[r]=[v/q for v in x[r]]
        for i in range(m):
            if i!=r and x[i][c]:
                q=x[i][c]
                x[i]=[u-q*v for u,v in zip(x[i],x[r])]
        r+=1
        if r==m:
            break
    return r


def inverse(a):
    n,n2=shape(a)
    if n!=n2:
        raise CertificateError("inverse requires square matrix")
    x=[row[:] + [Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for c in range(n):
        p=next((i for i in range(c,n) if x[i][c]),None)
        if p is None:
            raise CertificateError("singular source Gram")
        x[c],x[p]=x[p],x[c]
        q=x[c][c]
        x[c]=[v/q for v in x[c]]
        for i in range(n):
            if i!=c and x[i][c]:
                q=x[i][c]
                x[i]=[u-q*v for u,v in zip(x[i],x[c])]
    return [row[n:] for row in x]


def trace(a):
    n,n2=shape(a)
    if n!=n2:
        raise CertificateError("trace requires square matrix")
    return sum(a[i][i] for i in range(n))


def canonical_sha(value: Any)->str:
    raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def verify(data: dict[str,Any])->dict[str,Any]:
    if data.get("schema")!=SCHEMA or data.get("classification")!="SYNTHETIC_MODEL":
        raise CertificateError("wrong schema or classification")
    t=matrix(data.get("weighted_deficit"),"weighted_deficit")
    n,n2=shape(t)
    if n!=n2 or any(t[i][j]!=t[j][i] for i in range(n) for j in range(n)):
        raise CertificateError("weighted_deficit must be symmetric square")
    eig_raw=data.get("deficit_eigenvalues")
    if not isinstance(eig_raw,list) or len(eig_raw)!=n:
        raise CertificateError("deficit_eigenvalues has wrong length")
    eig=[frac(v,f"deficit_eigenvalues[{i}]") for i,v in enumerate(eig_raw)]
    if any(t[i][j] for i in range(n) for j in range(n) if i!=j):
        raise CertificateError("this exact regression requires a diagonal deficit matrix")
    if [t[i][i] for i in range(n)]!=eig or any(v<0 for v in eig):
        raise CertificateError("declared deficit eigenvalues do not match a PSD diagonal matrix")
    kappa=frac(data.get("kappa"),"kappa")
    if kappa<=0:
        raise CertificateError("kappa must be positive")
    j=matrix(data.get("source_basis"),"source_basis")
    n3,d=shape(j)
    if n3!=n or d<1 or rank(j)!=d:
        raise CertificateError("source_basis must have positive full column rank")

    p_index=sum(v>kappa for v in eig)
    gram=matmul(transpose(j),j)
    captured=trace(matmul(inverse(gram),matmul(matmul(transpose(j),t),j)))
    total=trace(t)
    tail=total-captured
    dimension_condition=d>=p_index
    refuted=dimension_condition and tail>kappa
    if not refuted:
        raise CertificateError("packet does not exhibit the dimension-only refutation")

    proof={
        "weighted_deficit":[[fj(x) for x in row] for row in t],
        "source_basis":[[fj(x) for x in row] for row in j],
        "kappa":fj(kappa),
        "threshold_index":p_index,
        "source_dimension":d,
        "captured_trace":fj(captured),
        "uncaptured_trace":fj(tail),
    }
    return {
        "schema":OUT,
        "classification":"SYNTHETIC_MODEL",
        "analytic_claim":"R-15601",
        "threshold_index":p_index,
        "source_dimension":d,
        "dimension_comparison_holds":dimension_condition,
        "captured_trace":fj(captured),
        "uncaptured_trace":fj(tail),
        "required_trace_threshold":fj(kappa),
        "trace_saturation_fails":tail>kappa,
        "exact_proof_object_sha256":canonical_sha(proof),
        "verdict":"REFUTED_DIMENSION_ONLY_WEIGHTED_INDEX_COMPARISON",
    }


def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("certificate",type=Path)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    try:
        data=json.loads(args.certificate.read_text())
        if not isinstance(data,dict):
            raise CertificateError("certificate root must be object")
        result=verify(data)
    except (OSError,json.JSONDecodeError,CertificateError,ZeroDivisionError) as exc:
        print(json.dumps({"verified":False,"error":str(exc)},indent=2),file=sys.stderr)
        return 2
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
    print(text,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
