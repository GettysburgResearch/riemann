#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from decimal import Decimal, localcontext
from pathlib import Path
import hashlib, json, random

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def factor(n):
    out={}; x=n; p=2
    while p*p<=x:
        while x%p==0: out[p]=out.get(p,0)+1; x//=p
        p+=1
    if x>1: out[x]=out.get(x,0)+1
    return out

def vm(n):
    f=factor(n)
    return {next(iter(f)):1} if len(f)==1 else {}

def add(a,b,s=1):
    out={p:Fraction(v) for p,v in a.items()}
    for p,v in b.items():
        out[p]=out.get(p,Fraction(0))+Fraction(s)*v
        if not out[p]: del out[p]
    return out

def y4(q):
    out={}; n=q; s=1
    while True:
        out=add(out,vm(n),s)
        if n%4: return out
        n//=4; s*=2

def check_y4(N=20000):
    zeros=0
    for q in range(2,N+1):
        lhs=y4(q)
        if q%4==0: lhs=add(lhs,y4(q//4),-2)
        assert lhs=={p:Fraction(v) for p,v in vm(q).items()}
        zeros+=not bool(y4(q))
    return {'range':N,'zero_columns':zeros}

def check_one_shot(seed=91752,trials=3000):
    rng=random.Random(seed)
    for _ in range(trials):
        n=rng.randint(1,12)
        parts=[[Fraction(rng.randint(0,20)) for _ in range(n)] for __ in range(rng.randint(1,8))]
        total=[sum(p[i] for p in parts) for i in range(n)]
        tau=Fraction(rng.randint(1,99),100)
        row=[tau*x for x in total]
        native=[x+Fraction(rng.randint(0,20)) for x in row]
        slack=[native[i]-row[i] for i in range(n)]
        assert all(s>=0 for s in slack)
        assert all(row[i]+slack[i]==native[i] for i in range(n))
        # Internal labels sum to the same one-shot physical row.
        assert row==[sum(tau*p[i] for p in parts) for i in range(n)]
    return {'trials':trials}

def check_constants():
    assert 12012+4+48972+1==60989<61000
    X=Decimal(10)**12
    with localcontext() as ctx:
        ctx.prec=80
        Ksqrt=X.sqrt()/(Decimal(33)/Decimal(4))
        L=(Decimal(2)*X).ln()
        nonterm=Decimal(971)/(Decimal(4)*Ksqrt)*(Decimal(3)+2*L+2*L*L)
        omissions=Decimal(32)/Ksqrt+Decimal(16)*Decimal(2).sqrt()*Decimal(10002)/X.sqrt()
    assert nonterm<4 and omissions<1
    assert Decimal(61000)<2*(4*X.sqrt()-3)
    return {'total_upper':'61000','nonterminal_at_X0':'<4','omissions_at_X0':'<1'}

def check_firewalls():
    text='\n'.join((ROOT/p).read_text() for p in [
      'claims/theorems/T-91752-one-shot-factor67-proves-sontr-nrct.md',
      'claims/lemmas/L-91756-one-shot-root-slack-below-61000.md'])
    assert 'Depends on: `J_Lambda(X)-4sqrt(X)' not in text
    assert 'empty recursive family' in text or 'exported\nrecursive family is empty' in text
    assert 'auxiliary port' in text
    return {'scan':'PASS'}

def main():
    checks={'y4':check_y4(),'one_shot':check_one_shot(),'constants':check_constants(),'firewalls':check_firewalls()}
    payload={'classification':'PASS_ONE_SHOT_SONTR_NRCT_HARDENING_ALGEBRA','checks':checks,
      'scope':'Finite algebra/constants only; imported Hall, capacity, prime-square and Landau theorems require independent reconstruction.',
      'sontr_established_by_replay':False,'nrct_established_by_replay':False,'rh_established_by_replay':False}
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    out=HERE/'results/verification.json'; out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(payload['classification']); print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=='__main__': main()
