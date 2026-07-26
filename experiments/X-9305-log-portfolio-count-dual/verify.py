#!/usr/bin/env python3
"""Exact verifier for RH-valid logarithmic portfolios plus exact count duals."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.xi-log-portfolio-count-dual.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
COUNT_GATE = "UNCONDITIONAL_TOTAL_ZERO_COUNT_EXACT"

class CertificateError(ValueError):
    pass

@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction
    def __post_init__(self):
        if self.lower > self.upper:
            raise CertificateError("reversed interval")
    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)
    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)
    def scale(self, scalar: Fraction) -> "Interval":
        return Interval(self.lower*scalar, self.upper*scalar) if scalar >= 0 else Interval(self.upper*scalar, self.lower*scalar)

def exact_int(v: Any, name: str) -> int:
    if isinstance(v, bool) or not isinstance(v, int):
        raise CertificateError(f"{name} must be integer")
    return v

def rat(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be object")
    n=exact_int(raw.get("numerator"), name+".numerator")
    d=exact_int(raw.get("denominator"), name+".denominator")
    if d <= 0: raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n,d)

def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict): raise CertificateError(f"{name} must be object")
    return Interval(rat(raw.get("lower"), name+".lower"), rat(raw.get("upper"), name+".upper"))

def fj(x: Fraction): return {"numerator":x.numerator,"denominator":x.denominator}
def ij(x: Interval): return {"lower":fj(x.lower),"upper":fj(x.upper)}

def poly_add(a,b):
    out=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def poly_mul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def response_numerator(nodes, beta):
    out=[Fraction(0)]
    for i,b in enumerate(beta):
        term=[Fraction(1)]
        for j,u in enumerate(nodes):
            if i != j: term=poly_mul(term,[u,Fraction(1)])
        out=poly_add(out,[-b*x for x in term])
    return out

def log_unit(x: Fraction, terms: int) -> Interval:
    if not (1 <= x <= 2): raise CertificateError("internal log reduction")
    z=(x-1)/(x+1); z2=z*z; p=z; s=Fraction(0)
    for k in range(terms):
        s += p/(2*k+1); p*=z2
    lo=2*s
    tail=Fraction(0) if z==0 else 2*p/((2*terms+1)*(1-z2))
    return Interval(lo,lo+tail)

def log_fraction(x: Fraction, terms: int) -> Interval:
    if x <= 0: raise CertificateError("log argument nonpositive")
    r=x; k=0
    while r >= 2: r/=2; k+=1
    while r < 1: r*=2; k-=1
    u=log_unit(r,terms); l2=log_unit(Fraction(2),terms)
    return u.add(l2.scale(Fraction(k)))

def log_interval(x: Interval, terms: int) -> Interval:
    if x.lower <= 0: raise CertificateError("H interval touches zero")
    return Interval(log_fraction(x.lower,terms).lower, log_fraction(x.upper,terms).upper)

def status(x: Interval):
    if x.upper < 0: return "CERTIFIED_NEGATIVE"
    if x.lower >= 0: return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"

def verify(data: dict[str,Any]) -> dict[str,Any]:
    if data.get("schema") != SCHEMA: raise CertificateError("bad schema")
    if data.get("normalization_id") != NORMALIZATION: raise CertificateError("normalization mismatch")
    cls=data.get("classification")
    if cls not in ("SYNTHETIC_MODEL","RIEMANN_XI_DIRECTED"): raise CertificateError("bad classification")
    terms=exact_int(data.get("log_terms",160),"log_terms")
    points=data.get("points")
    if not isinstance(points,list) or len(points)<2: raise CertificateError("points missing")
    ids=[]; nodes=[]; logs=[]
    for i,p in enumerate(points):
        if not isinstance(p,dict) or not isinstance(p.get("id"),str) or p["id"] in ids: raise CertificateError("bad point")
        ids.append(p["id"]); u=rat(p.get("u"),f"points[{i}].u")
        if u <= 0 or (nodes and u <= nodes[-1]): raise CertificateError("nodes must increase")
        nodes.append(u); logs.append(log_interval(interval(p.get("h_interval"),f"points[{i}].h_interval"),terms))
    raw_beta=data.get("beta")
    if not isinstance(raw_beta,list) or len(raw_beta)!=len(nodes): raise CertificateError("bad beta")
    beta=[rat(x,f"beta[{i}]") for i,x in enumerate(raw_beta)]
    if sum(beta) != 0: raise CertificateError("beta must sum to zero")
    P=response_numerator(nodes,beta)
    cert=data.get("response_certificate")
    if not isinstance(cert,dict) or cert.get("type")!="MONOMIAL_NONNEGATIVE": raise CertificateError("unsupported response certificate")
    declared=cert.get("negative_derivative_numerator_coefficients")
    if not isinstance(declared,list): raise CertificateError("missing polynomial certificate")
    declared=[rat(x,f"response_certificate.coefficients[{i}]") for i,x in enumerate(declared)]
    while len(declared)>1 and declared[-1]==0: declared.pop()
    if declared != P: raise CertificateError("polynomial identity mismatch")
    if any(x<0 for x in P): raise CertificateError("polynomial coefficient is negative")
    row=Interval(Fraction(0),Fraction(0))
    for b,L in zip(beta,logs): row=row.add(L.scale(b))

    atoms=data.get("atoms")
    if not isinstance(atoms,list) or not atoms: raise CertificateError("atoms missing")
    atom_ids=[]; bounds=[]
    for i,a in enumerate(atoms):
        if not isinstance(a,dict) or not isinstance(a.get("id"),str) or a["id"] in atom_ids: raise CertificateError("bad atom")
        atom_ids.append(a["id"]); lo=rat(a.get("lower_offset"),f"atoms[{i}].lower"); hi=rat(a.get("upper_offset"),f"atoms[{i}].upper")
        if lo>hi: raise CertificateError("reversed atom")
        bounds.append(max(lo*lo,hi*hi))
    costs_raw=data.get("cell_cost_lower_bounds")
    if not isinstance(costs_raw,list) or len(costs_raw)!=len(atoms): raise CertificateError("bad costs")
    costs=[]; exact_costs=[]
    for j,(B,raw) in enumerate(zip(bounds,costs_raw)):
        c=rat(raw,f"cell_cost[{j}]")
        if c<0: raise CertificateError("negative cell cost")
        phi=Interval(Fraction(0),Fraction(0))
        for b,u in zip(beta,nodes): phi=phi.add(log_fraction(u+B,terms).scale(b))
        if c > phi.lower: raise CertificateError("unsafe cell lower cost")
        costs.append(c); exact_costs.append(phi)
    windows=data.get("count_windows")
    if not isinstance(windows,list) or not windows: raise CertificateError("count windows missing")
    idx={x:i for i,x in enumerate(atom_ids)}; win=[]
    for r,w in enumerate(windows):
        if not isinstance(w,dict) or w.get("gate")!=COUNT_GATE: raise CertificateError("count gate mismatch")
        aids=w.get("atoms")
        if not isinstance(aids,list) or not aids or any(x not in idx for x in aids): raise CertificateError("bad window atoms")
        inds=[idx[x] for x in aids]
        if inds != list(range(inds[0],inds[-1]+1)): raise CertificateError("window not consecutive")
        m=exact_int(w.get("count"),f"window[{r}].count")
        if m<0: raise CertificateError("negative count")
        win.append((inds,m))
    primal=data.get("primal",{}).get("atom_counts")
    dual=data.get("dual",{}).get("lambdas")
    if not isinstance(primal,list) or len(primal)!=len(atoms): raise CertificateError("bad primal")
    if not isinstance(dual,list) or len(dual)!=len(win): raise CertificateError("bad dual")
    x=[exact_int(v,f"primal[{i}]") for i,v in enumerate(primal)]
    if any(v<0 for v in x): raise CertificateError("negative primal")
    lam=[rat(v,f"dual[{i}]") for i,v in enumerate(dual)]
    for inds,m in win:
        if sum(x[j] for j in inds)!=m: raise CertificateError("primal equation failed")
    for j in range(len(atoms)):
        if sum(lam[r] for r,(inds,_) in enumerate(win) if j in inds)>costs[j]: raise CertificateError("dual inequality failed")
    po=sum(c*v for c,v in zip(costs,x)); do=sum(lam[r]*m for r,(_,m) in enumerate(win))
    if po != do: raise CertificateError("primal-dual objective mismatch")
    adapted=row.sub(Interval(do,do))

    controls=[]
    for q,ctl in enumerate(data.get("two_point_controls",[])):
        left=ids.index(ctl["left"]); right=ids.index(ctl["right"])
        if right != left+1: raise CertificateError("control must be adjacent")
        raw=logs[right].sub(logs[left])
        c=rat(ctl.get("cell_cost_lower_bound"),f"control[{q}].cost")
        B=bounds[0]
        exact=log_fraction((nodes[right]+B)/(nodes[left]+B),terms)
        if c>exact.lower: raise CertificateError("unsafe control cost")
        residual=raw.sub(Interval(c*x[0],c*x[0]))
        controls.append({"id":ctl["id"],"interval":ij(residual),"status":status(residual)})

    verdict=("SYNTHETIC_PORTFOLIO_SEPARATION" if cls=="SYNTHETIC_MODEL" and adapted.upper<0 else
             "NEGATIVE_RIEMANN_XI_PORTFOLIO_PENDING_REPRODUCTION_AND_REVIEW" if cls=="RIEMANN_XI_DIRECTED" and adapted.upper<0 else
             "UNRESOLVED" if adapted.lower<=0<=adapted.upper else "NO_NEGATIVE_PORTFOLIO")
    return {"schema":SCHEMA,"classification":cls,"beta":[fj(b) for b in beta],"negative_derivative_numerator_coefficients":[fj(c) for c in P],
            "raw_portfolio_interval":ij(row),"cell_exact_cost_intervals":[ij(c) for c in exact_costs],"dual_objective":fj(do),
            "adapted_portfolio_interval":ij(adapted),"adapted_status":status(adapted),"two_point_controls":controls,"verdict":verdict,
            "scope_warning":"Exact finite arithmetic only; a Riemann-xi negative requires independent directed primitives, exact unconditional counts, and analytic review."}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("certificate",type=Path); ap.add_argument("--output",type=Path); ns=ap.parse_args()
    try:
        d=json.loads(ns.certificate.read_text()); out=verify(d)
    except (OSError,json.JSONDecodeError,CertificateError,ValueError,ZeroDivisionError) as e:
        print(json.dumps({"verified":False,"error":str(e)},indent=2),file=sys.stderr); return 2
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if ns.output: ns.output.write_text(text)
    print(text,end=""); return 0 if out["verdict"]!="UNRESOLVED" else 1
if __name__=="__main__": raise SystemExit(main())
