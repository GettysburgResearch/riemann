#!/usr/bin/env python3
"""Fraction-only replay for L-14317 packet-leverage symbol floors."""
import argparse,json,hashlib
from fractions import Fraction as Q
from pathlib import Path
S="riemann.x14310-packet-leverage-floor.v1"
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
    if cls not in ("SYNTHETIC_MODEL","SUZUKI_PACKET_DIRECTED"): raise E("bad classification")
    gate=d.get("tail_gate")
    if not isinstance(gate,dict): raise E("tail gate missing")
    want="SYNTHETIC_SYMBOL_TAIL_FLOOR" if cls=="SYNTHETIC_MODEL" else "CERTIFIED_SYMBOL_TAIL_FLOOR"
    if gate.get("status")!=want: raise E("wrong tail gate")
    sh=gate.get("sha256")
    if not isinstance(sh,str) or len(sh)!=64: raise E("bad gate digest")
    T=q(gate.get("symbol_lower_outside_cells"),"tail floor")
    packet=d.get("packet_gate")
    if not isinstance(packet,dict): raise E("packet gate missing")
    pwant="SYNTHETIC_EXACT_PACKET" if cls=="SYNTHETIC_MODEL" else "CERTIFIED_EXACT_PACKET_SUBSPACE"
    if packet.get("status")!=pwant: raise E("wrong packet gate")
    psha=packet.get("sha256")
    if not isinstance(psha,str) or len(psha)!=64: raise E("bad packet digest")
    raw=d.get("cells")
    if not isinstance(raw,list) or not raw: raise E("cells missing")
    C=[]; ids=set()
    for c in raw:
        if not isinstance(c,dict): raise E("bad cell")
        n=c.get("id")
        if not isinstance(n,str) or not n or n in ids: raise E("bad cell id")
        ids.add(n); a=q(c.get("left"),"left"); b=q(c.get("right"),"right")
        lo=q(c.get("symbol_lower"),"symbol_lower"); cap=q(c.get("density_cap_upper"),"density cap")
        if a>=b or cap<0: raise E("bad cell geometry or cap")
        C.append((a,b,lo,cap,n))
    C.sort()
    if any(C[i][1]>C[i+1][0] for i in range(len(C)-1)): raise E("overlapping cells")
    expected=sorted({T,*(lo for _,_,lo,_,_ in C if lo<=T)})
    levels=[q(x,"candidate level") for x in d.get("candidate_levels",[])]
    if levels!=expected: raise E("incomplete breakpoint levels")
    rows=[]; best=None
    for G in levels:
        D=sum((b-a)*cap*max(G-lo,Q(0)) for a,b,lo,cap,_ in C)
        F=G-D; rows.append({"level":j(G),"weighted_deficit_upper":j(D),"floor":j(F)})
        if best is None or (F,-G)>(best[1],-best[0]): best=(G,F)
    G,F=best; ex=d.get("expected")
    if not isinstance(ex,dict): raise E("expected missing")
    if q(ex.get("best_level"),"best level")!=G or q(ex.get("best_floor"),"best floor")!=F:
        raise E("claimed optimum mismatch")
    status="CERTIFIED_NONNEGATIVE_PACKET_COMPLEMENT" if F>=0 else "CERTIFIED_COMPLEMENT_FLOOR_ONLY"
    if ex.get("status")!=status: raise E("status mismatch")
    out={"schema":S,"classification":cls,"tail_floor":j(T),
         "cells":[{"id":n,"left":j(a),"right":j(b),"symbol_lower":j(lo),"density_cap_upper":j(cap)} for a,b,lo,cap,n in C],
         "rows":rows,"best_level":j(G),"best_floor":j(F),"status":status}
    out["proof_object_sha256"]=h(out); return out
def main():
    p=argparse.ArgumentParser(); p.add_argument("certificate",type=Path); p.add_argument("--output",type=Path)
    a=p.parse_args()
    try: out=verify(json.loads(a.certificate.read_text())); code=0
    except Exception as e: out={"schema":S,"status":"REJECTED","reason":str(e)}; code=2
    t=json.dumps(out,indent=2,sort_keys=True)+"\n"
    a.output.write_text(t) if a.output else print(t,end="")
    return code
if __name__=="__main__": raise SystemExit(main())
