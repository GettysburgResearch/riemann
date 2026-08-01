#!/usr/bin/env python3
"""Fraction-only verifier for L-18501 sacrificial-subspace count certificates."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as Q
from pathlib import Path

SCHEMA="riemann.x18501-sacrificial-count.v1"
class Reject(ValueError): pass

def integer(x,name):
    if isinstance(x,bool) or not isinstance(x,int): raise Reject(f"{name} must be integer")
    return x

def rat(x,name):
    if not isinstance(x,dict): raise Reject(f"{name} must be rational object")
    a=integer(x.get("numerator"),name+".numerator")
    b=integer(x.get("denominator"),name+".denominator")
    if b<=0: raise Reject(f"{name} denominator must be positive")
    return Q(a,b)

def matrix(x,name):
    if not isinstance(x,list) or not x or not all(isinstance(r,list) for r in x):
        raise Reject(f"{name} must be nonempty matrix")
    m=[[rat(v,f"{name}[{i}][{j}]") for j,v in enumerate(r)] for i,r in enumerate(x)]
    if len({len(r) for r in m})!=1: raise Reject(f"{name} ragged")
    return m

def shape(a): return len(a),len(a[0])
def transpose(a): return [list(x) for x in zip(*a)]
def add(a,b,s=Q(1)):
    return [[a[i][j]+s*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(a,s): return [[s*z for z in row] for row in a]
def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def contract(b,a): return mul(transpose(b),mul(a,b))
def symmetric(a): return shape(a)[0]==shape(a)[1] and all(a[i][j]==a[j][i] for i in range(len(a)) for j in range(len(a)))

def rank(a):
    m=[r[:] for r in a]; nr,nc=shape(m); row=0
    for col in range(nc):
        p=next((i for i in range(row,nr) if m[i][col]),None)
        if p is None: continue
        m[row],m[p]=m[p],m[row]; v=m[row][col]
        m[row]=[z/v for z in m[row]]
        for i in range(nr):
            if i!=row and m[i][col]:
                c=m[i][col]; m[i]=[m[i][j]-c*m[row][j] for j in range(nc)]
        row+=1
        if row==nr: break
    return row

def pd_pivots(a,name):
    if not symmetric(a): raise Reject(f"{name} not symmetric")
    n=len(a); l=[[Q(0) for _ in range(n)] for _ in range(n)]; d=[]
    for i in range(n):
        v=a[i][i]-sum(l[i][k]*l[i][k]*d[k] for k in range(i))
        if v<=0: raise Reject(f"{name} nonpositive pivot {i}")
        d.append(v); l[i][i]=1
        for j in range(i+1,n):
            l[j][i]=(a[j][i]-sum(l[j][k]*l[i][k]*d[k] for k in range(i)))/v
    return d

def require_psd(a,name):
    """Exact congruence elimination; a zero diagonal in a PSD matrix has zero row."""
    if not symmetric(a): raise Reject(f"{name} not symmetric")
    m=[r[:] for r in a]
    while m:
        if any(m[i][i]<0 for i in range(len(m))): raise Reject(f"{name} negative diagonal")
        p=next((i for i in range(len(m)) if m[i][i]>0),None)
        if p is None:
            if any(z for row in m for z in row): raise Reject(f"{name} zero diagonal with nonzero row")
            return
        if p:
            m[0],m[p]=m[p],m[0]
            for row in m: row[0],row[p]=row[p],row[0]
        v=m[0][0]
        b=[m[i][0] for i in range(1,len(m))]
        m=[[m[i+1][j+1]-b[i]*b[j]/v for j in range(len(b))] for i in range(len(b))]

def outq(x): return {"numerator":x.numerator,"denominator":x.denominator}
def digest(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def verify(d):
    if d.get("schema")!=SCHEMA: raise Reject("schema mismatch")
    G=matrix(d.get("metric"),"metric"); K=matrix(d.get("evaluation_gram"),"evaluation_gram")
    if shape(G)!=shape(K) or shape(G)[0]!=shape(G)[1]: raise Reject("matrix shape mismatch")
    n=len(G); gp=pd_pivots(G,"metric"); require_psd(K,"evaluation_gram")
    W=matrix(d.get("witness_basis"),"witness_basis")
    wr=rank(W)
    if len(W)!=n or wr!=len(W[0]): raise Reject("witness basis not full column rank")
    r=integer(d.get("radical_rank"),"radical_rank")
    if r<0 or n-wr>r: raise Reject("codimension exceeds radical rank")
    tau=rat(d.get("threshold"),"threshold")
    wp=pd_pivots(contract(W,add(K,G,-tau)),"strict witness floor")
    R=matrix(d.get("radical_basis"),"radical_basis")
    if len(R)!=n or rank(R)!=r: raise Reject("radical basis rank mismatch")
    eps=rat(d.get("radical_evaluation_upper"),"radical_evaluation_upper")
    if eps>=tau: raise Reject("radical endpoint must be below threshold")
    rp=pd_pivots(contract(R,add(scale(G,eps),K,-1)),"strict radical upper moat")
    result={
      "schema":SCHEMA,
      "status":"CERTIFIED_SHARP_COUNT_AND_ANGLE",
      "ambient_dimension":n,
      "witness_rank":wr,
      "witness_codimension":n-wr,
      "radical_rank":r,
      "threshold":outq(tau),
      "radical_evaluation_upper":outq(eps),
      "count_upper":r,
      "count_lower":r,
      "angle_squared_upper":outq(eps/tau),
      "metric_ldl_pivots":[outq(x) for x in gp],
      "witness_floor_ldl_pivots":[outq(x) for x in wp],
      "radical_moat_ldl_pivots":[outq(x) for x in rp],
    }
    result["proof_object_sha256"]=digest(result)
    exp=d.get("expected")
    if not isinstance(exp,dict): raise Reject("expected missing")
    for key in ("status","count_upper","count_lower"):
        if exp.get(key)!=result[key]: raise Reject(f"expected {key} mismatch")
    return result

def main():
    p=argparse.ArgumentParser(); p.add_argument("certificate",type=Path); p.add_argument("--output",type=Path)
    a=p.parse_args()
    try: out=verify(json.loads(a.certificate.read_text())); code=0
    except Exception as e: out={"schema":SCHEMA,"status":"REJECTED","reason":str(e)}; code=2
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if a.output: a.output.write_text(text)
    else: print(text,end="")
    return code
if __name__=="__main__": raise SystemExit(main())
