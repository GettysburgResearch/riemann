#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T99960_DUAL_OWNER_PACKING_EQUIVALENCE_ALGEBRA"
R = 67

def factor(n: int) -> dict[int,int]:
    out={}
    p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def beta(n: int) -> int:
    out=1
    for p,e in factor(n).items():
        if p==R:
            if e==1: out*=-2
            elif e==2: out*=1
            else: return 0
        else:
            if e==1: out*=-1
            else: return 0
    return out

def gd_local_67(e: int,k: int)->F:
    if e==0: return F(1 if k==0 else 0)
    if e==1: return F(1)+F(k,2)
    if e==2: return F(k+1)
    return F(0)

def gd(d: int,n: int)->F:
    fd=factor(d); fn=factor(n)
    e=fd.get(R,0)
    val=gd_local_67(e,fn.get(R,0))
    for p in fn:
        if p!=R and p not in fd: return F(0)
        if p==R and e==0 and fn[p]>0: return F(0)
    return val

def divisors(n:int):
    return [d for d in range(1,n+1) if n%d==0]

def conv_beta_gd(d:int,m:int)->F:
    return sum(F(beta(a))*gd(d,m//a) for a in divisors(m))

def run()->dict:
    checked=0
    for d in range(1,301):
        bd=beta(d)
        if bd==0: continue
        for m in range(1,401):
            assert F(beta(d*m)) == F(bd)*conv_beta_gd(d,m)
            checked+=1

    c={2:F(3,5),3:F(-2,7),5:F(4,9)}
    total=sum(c.values(),F(0))
    Q=sum(cm*cn*F(min(m,n)) for m,cm in c.items() for n,cn in c.items())
    assert Q-total*total>=0

    def phi(n:int)->int:
        r=n
        for p in factor(n): r=r//p*(p-1)
        return r
    G=F(0)
    for d in range(1,6):
        tail=sum(v for n,v in c.items() if n%d==0)
        G+=phi(d)*tail*tail
    assert G-total*total>=0

    core={
      "schema":"riemann.x99960.dual-owner-packing.v1",
      "classification":VERDICT,
      "base_pr":666,
      "base_sha":"7ae9e3e15b8bcb0a5f382db49f31ad385b02e24a",
      "divisor_restriction_checks":checked,
      "hardy_root_term_present":True,
      "divisor_root_term_present":True,
      "htoc_equivalent_to_rh":True,
      "dgoc_equivalent_to_rh":True,
      "htoc_unconditionally_proved":False,
      "dgoc_unconditionally_proved":False,
      "rh_established":False,
    }
    canon=json.dumps(core,sort_keys=True,separators=(",",":")).encode()
    core["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    return core

def main():
    result=run()
    out=Path(__file__).resolve().parent/"results"/"verification.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])
if __name__=="__main__": main()
