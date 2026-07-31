#!/usr/bin/env python3
"""Exact Fraction replay for L-14316 cellwise symbol floors."""
import argparse,json,hashlib
from fractions import Fraction as Q
from pathlib import Path
S="riemann.x14309-symbol-bathtub-floor.v1"
class E(ValueError): pass
def z(x,n):
    if isinstance(x,bool) or not isinstance(x,int): raise E(n+" must be integer")
    return x
def q(x,n):
    if not isinstance(x,dict): raise E(n+" must be object")
    a=z(x.get("numerator"),n+".numerator"); b=z(x.get("denominator"),n+".denominator")
    if b<=0: raise E(n+" denominator must be positive")
    return Q(a,b)
def j(x): return {"numerator":x.numerator,"denominator":x.denominator}
def h(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def verify(d):
    if d.get("schema")!=S: raise E("schema mismatch")
    cls=d.get("classification")
    if cls not in ("SYNTHETIC_MODEL","SUZUKI_SYMBOL_DIRECTED"): raise E("bad classification")
    L=q(d.get("time_interval_length"),"time_interval_length")
    if L<=0: raise E("nonpositive interval length")
    p=q(d.get("pi_lower"),"pi_lower")
    if p!=Q(333,106): raise E("pi_lower must equal 333/106")
    gate=d.get("tail_gate")
    if not isinstance(gate,dict): raise E("tail gate missing")
    want="SYNTHETIC_SYMBOL_TAIL_FLOOR" if cls=="SYNTHETIC_MODEL" else "CERTIFIED_SYMBOL_TAIL_FLOOR"
    if gate.get("status")!=want: raise E("wrong tail gate")
    sh=gate.get("sha256")
    if not isinstance(sh,str) or len(sh)!=64: raise E("bad gate digest")
    T=q(gate.get("symbol_lower_outside_cells"),"tail floor")
    raw=d.get("cells")
    if not isinstance(raw,list) or not raw: raise E("cells missing")
    C=[]; ids=set()
    for c in raw:
        if not isinstance(c,dict): raise E("bad cell")
        name=c.get("id")
        if not isinstance(name,str) or not name or name in ids: raise E("bad cell id")
        ids.add(name); a=q(c.get("left"),"left"); b=q(c.get("right"),"right")
        lo=q(c.get("symbol_lower"),"symbol_lower")
        if a>=b: raise E("reversed cell")
        C.append((a,b,lo,name))
    C.sort()
    if any(C[i][1]>C[i+1][0] for i in range(len(C)-1)): raise E("overlapping cells")
    expected=sorted({T,*(lo for _,_,lo,_ in C if lo<=T)})
    levels=[q(x,"candidate level") for x in d.get("candidate_levels",[])]
    if levels!=expected: raise E("incomplete breakpoint levels")
    c=L/(2*p); rows=[]; best=None
    for G in levels:
        D=sum((b-a)*max(G-lo,Q(0)) for a,b,lo,_ in C)
        F=G-c*D; rows.append({"level":j(G),"deficit_integral_upper":j(D),"floor":j(F)})
        if best is None or (F,-G)>(best[1],-best[0]): best=(G,F)
    G,F=best; ex=d.get("expected")
    if not isinstance(ex,dict): raise E("expected missing")
    if q(ex.get("best_level"),"best level")!=G or q(ex.get("best_floor"),"best floor")!=F:
        raise E("claimed optimum mismatch")
    status="CERTIFIED_NONNEGATIVE_SYMBOL_COMPRESSION" if F>=0 else "CERTIFIED_LOWER_FLOOR_ONLY"
    if ex.get("status")!=status: raise E("status mismatch")
    out={"schema":S,"classification":cls,"density_cap_upper":j(c),"tail_floor":j(T),
         "cells":[{"id":n,"left":j(a),"right":j(b),"symbol_lower":j(lo)} for a,b,lo,n in C],
         "rows":rows,"best_level":j(G),"best_floor":j(F),"status":status}
    out["proof_object_sha256"]=h(out); return out
def main():
    a=argparse.ArgumentParser(); a.add_argument("certificate",type=Path); a.add_argument("--output",type=Path)
    x=a.parse_args()
    try: out=verify(json.loads(x.certificate.read_text())); code=0
    except Exception as e: out={"schema":S,"status":"REJECTED","reason":str(e)}; code=2
    t=json.dumps(out,indent=2,sort_keys=True)+"\n"
    x.output.write_text(t) if x.output else print(t,end="")
    return code
if __name__=="__main__": raise SystemExit(main())
