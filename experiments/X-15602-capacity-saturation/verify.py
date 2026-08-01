#!/usr/bin/env python3
"""Exact checker for L-15603/L-15604/T-15602 capacity saturation.

The checker uses only Python integers and fractions.Fraction.  It verifies a
finite exact operator model in which:

* a d-dimensional trial packet lies strictly below t;
* its complete orthogonal complement lies above Gamma;
* the counted inverse-Ritz moat gives an explicit ambient floor.

The spectral count equality follows from min--max; no numerical eigensolver is
used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15602-capacity-saturation.v1"
OUT_SCHEMA = "riemann.x15602-capacity-saturation-verification.v1"


class CertificateError(ValueError):
    pass


def integer(x: Any, name: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise CertificateError(f"{name} must be an integer")
    return x


def frac(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be a rational object")
    n = integer(raw.get("numerator"), f"{name}.numerator")
    d = integer(raw.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    result = []
    width = None
    for i, row in enumerate(raw):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        parsed = [frac(v, f"{name}[{i}][{j}]") for j, v in enumerate(row)]
        if width is None:
            width = len(parsed)
        if len(parsed) != width:
            raise CertificateError(f"{name} has ragged rows")
        result.append(parsed)
    return result


def mj(a: list[list[Fraction]]) -> list[list[dict[str, int]]]:
    return [[fj(x) for x in row] for row in a]


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    m, k = shape(a)
    k2, n = shape(b)
    if k != k2:
        raise CertificateError("matrix multiplication dimension mismatch")
    return [[sum(a[i][r] * b[r][j] for r in range(k))
             for j in range(n)] for i in range(m)]


def sub(a, b):
    if shape(a) != shape(b):
        raise CertificateError("matrix subtraction dimension mismatch")
    return [[x-y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def scale(c: Fraction, a):
    return [[c*x for x in row] for row in a]


def eye(n: int):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def symmetric(a) -> bool:
    m,n=shape(a)
    return m==n and all(a[i][j] == a[j][i] for i in range(n) for j in range(n))


def rank(a) -> int:
    m,n=shape(a)
    x=[row[:] for row in a]
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if x[i][c] != 0),None)
        if p is None:
            continue
        x[r],x[p]=x[p],x[r]
        pivot=x[r][c]
        x[r]=[v/pivot for v in x[r]]
        for i in range(m):
            if i != r and x[i][c] != 0:
                q=x[i][c]
                x[i]=[u-q*v for u,v in zip(x[i],x[r])]
        r += 1
        if r==m:
            break
    return r


def nullspace(a):
    m,n=shape(a)
    x=[row[:] for row in a]
    piv=[]
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if x[i][c] != 0),None)
        if p is None:
            continue
        x[r],x[p]=x[p],x[r]
        pivot=x[r][c]
        x[r]=[v/pivot for v in x[r]]
        for i in range(m):
            if i != r and x[i][c] != 0:
                q=x[i][c]
                x[i]=[u-q*v for u,v in zip(x[i],x[r])]
        piv.append(c)
        r += 1
        if r==m:
            break
    free=[c for c in range(n) if c not in piv]
    cols=[]
    for f in free:
        v=[Fraction(0)]*n
        v[f]=1
        for i,c in enumerate(piv):
            v[c]=-x[i][f]
        cols.append(v)
    if not cols:
        return [[] for _ in range(n)]
    return [list(row) for row in zip(*cols)]


def swap_sym(a,i,j):
    if i==j:
        return
    a[i],a[j]=a[j],a[i]
    for row in a:
        row[i],row[j]=row[j],row[i]


def psd_pivots(a, *, strict: bool):
    if not symmetric(a):
        raise CertificateError("matrix must be symmetric")
    a=[row[:] for row in a]
    piv=[]
    while a:
        n=len(a)
        if any(a[i][i] < 0 for i in range(n)):
            raise CertificateError("negative diagonal in proposed PSD matrix")
        pidx=next((i for i in range(n) if a[i][i] > 0),None)
        if pidx is None:
            if any(a[i][j] != 0 for i in range(n) for j in range(n)):
                raise CertificateError("zero diagonal with nonzero PSD row")
            if strict:
                raise CertificateError("singular matrix where PD required")
            piv += [Fraction(0)]*n
            break
        swap_sym(a,0,pidx)
        p=a[0][0]
        piv.append(p)
        if n==1:
            break
        c=[a[i][0] for i in range(1,n)]
        a=[[a[i+1][j+1]-c[i]*c[j]/p for j in range(n-1)]
           for i in range(n-1)]
    return piv


def canonical_sha(value: Any) -> str:
    raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    if data.get("classification") != "SYNTHETIC_MODEL":
        raise CertificateError("only exact synthetic full-operator packets are accepted")
    a=matrix(data.get("full_operator"),"full_operator")
    n,n2=shape(a)
    if n != n2 or not symmetric(a):
        raise CertificateError("full_operator must be symmetric square")
    j=matrix(data.get("trial_basis"),"trial_basis")
    n3,d=shape(j)
    if n3 != n or rank(j) != d or d < 1:
        raise CertificateError("trial_basis must have positive full column rank")
    expected=integer(data.get("expected_capacity"),"expected_capacity")
    if expected != d:
        raise CertificateError("expected_capacity differs from packet dimension")
    t=frac(data.get("t"),"t")
    gamma=frac(data.get("gamma"),"gamma")
    q=frac(data.get("q_upper"),"q_upper")
    claimed=frac(data.get("claimed_floor"),"claimed_floor")
    if not t < gamma:
        raise CertificateError("require t < gamma")
    if q >= 0:
        raise CertificateError("q_upper must be negative")

    jt=transpose(j)
    g=matmul(jt,j)
    b=matmul(matmul(jt,a),j)
    trial_slack=sub(scale(t,g),b)
    trial_piv=psd_pivots(trial_slack,strict=True)

    e=nullspace(jt)
    if shape(e) != (n,n-d):
        raise CertificateError("orthogonal complement dimension mismatch")
    if n-d:
        et=transpose(e)
        eg=matmul(et,e)
        ea=matmul(matmul(et,a),e)
        complement_slack=sub(ea,scale(gamma,eg))
        complement_piv=psd_pivots(complement_slack,strict=False)
    else:
        complement_slack=[]
        complement_piv=[]

    shifted=sub(a,scale(t,eye(n)))
    h=matmul(matmul(jt,shifted),j)
    k=matmul(matmul(jt,matmul(shifted,shifted)),j)
    hneg=psd_pivots(scale(Fraction(-1),h),strict=True)
    kpos=psd_pivots(k,strict=True)
    moat=sub(scale(q,k),h)
    moat_piv=psd_pivots(moat,strict=False)
    floor=t+Fraction(1,1)/q
    if claimed > floor:
        raise CertificateError("claimed_floor exceeds inverse-Ritz floor")

    proof={
        "dimension":d,
        "full_operator":mj(a),
        "trial_basis":mj(j),
        "t":fj(t),
        "gamma":fj(gamma),
        "trial_slack":mj(trial_slack),
        "complement_slack":mj(complement_slack) if complement_slack else [],
        "H":mj(h),
        "K":mj(k),
        "q_upper":fj(q),
        "inverse_ritz_moat":mj(moat),
        "certified_floor":fj(floor),
    }
    return {
        "schema":OUT_SCHEMA,
        "classification":"SYNTHETIC_MODEL",
        "analytic_claims":["L-15603","L-15604","L-15601"],
        "capacity":d,
        "saturated_count_below_t":d,
        "saturated_count_below_gamma":d,
        "trial_slack_pivots":[fj(x) for x in trial_piv],
        "complement_slack_pivots":[fj(x) for x in complement_piv],
        "H_negative_pivots":[fj(x) for x in hneg],
        "K_positive_pivots":[fj(x) for x in kpos],
        "inverse_ritz_moat_pivots":[fj(x) for x in moat_piv],
        "certified_floor":fj(floor),
        "claimed_floor":fj(claimed),
        "exact_proof_object_sha256":canonical_sha(proof),
        "verdict":"CERTIFIED_EXACT_CAPACITY_SATURATION_AND_AMBIENT_FLOOR",
        "proof_boundary":"Exact rational finite operator algebra; no Riemann-zeta operator is certified by this synthetic packet.",
    }


def main() -> int:
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
