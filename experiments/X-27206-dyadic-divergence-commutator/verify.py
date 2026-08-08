#!/usr/bin/env python3
"""Exact finite regression for L-27207/L-27208; no RH claim."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json


def mobius(N):
    mu=[0]*(N+1); mu[1]=1; ps=[]; comp=[False]*(N+1)
    for n in range(2,N+1):
        if not comp[n]: ps.append(n); mu[n]=-1
        for p in ps:
            if n*p>N: break
            comp[n*p]=True
            if n%p==0: mu[n*p]=0; break
            mu[n*p]=-mu[n]
    return mu


def chi(n,j,q): return n//q-j//q-(n-j)//q


def add(*terms):
    out=defaultdict(Q)
    for scale,flow in terms:
        for e,v in flow.items(): out[e]+=scale*v
    return {e:v for e,v in out.items() if v}


@lru_cache(None)
def tree(n):
    if n<=1: return {}
    j=n//2; out=defaultdict(Q); out[(n,j)]+=1
    for e,v in tree(j).items(): out[e]+=v
    for e,v in tree(n-j).items(): out[e]+=v
    return dict(out)


def E(n): return add((Q(1),tree(n+1)),(Q(-1),tree(n)))


def boundary(flow,X):
    out=defaultdict(Q)
    for (n,j),v in flow.items(): out[n]+=v; out[j]-=v; out[n-j]-=v
    return {m:out[m] for m in range(1,X+1)}


def loads(flow,X):
    return {q:sum(v*chi(n,j,q) for (n,j),v in flow.items()) for q in range(2,X+1)}


def divergence(w,X):
    mu=mobius(X); u={}
    for m in range(2,X+1):
        u[m]=sum(Q(mu[k])*w[m*k] for k in range(1,X//m+1))
    u[X+1]=Q(0); r={m:u[m]-u[m+1] for m in range(2,X+1)}
    r[1]=-sum(Q(m)*r[m] for m in range(2,X+1))
    return r


def tree_flow(r,X):
    return add(*[(r[m],tree(m)) for m in range(2,X+1)])


def targets(Y,a,salt=0):
    lo={q:Q(((q*q+3*q+7+salt)%19)+1,q+5) for q in range(2,Y+1)}
    hi={2:Q(7+salt,11+salt)}
    for q in range(3,2*Y+1):
        hi[q]=a*lo[q//2] if q%2==0 else Q(((5*q*q+2*q+9+salt)%23)+1,q+7)
    return lo,hi


def rhs(rY,rX,w2,Y,a,omit_bottom=False,omit=None,reverse=False):
    out=defaultdict(Q)
    for m,v in rY.items(): out[2*m]+=a*v
    if not omit_bottom: out[2]+=w2; out[1]-=2*w2
    sign=-1 if reverse else 1
    for k in range(1,Y):
        if k==omit: continue
        c=sign*rX[2*k+1]; out[2*k+1]+=c; out[2*k]-=c; out[1]-=c
    return {m:out[m] for m in range(1,2*Y+1)}


def upper_flow(dY,rX,w2,Y,a):
    terms=[(a,{(2*n,2*j):v for (n,j),v in dY.items()}),(w2,tree(2))]
    terms += [(rX[2*k+1],E(2*k)) for k in range(1,Y)]
    return add(*terms)


def run():
    counts={'divergence_cases':0,'flow_cases':0,'doubled_carry_cells':0,
            'commutator_recursions':0,'balanced_commutator_edges':0,
            'endpoint_increment_cases':0}
    for n in range(1,129):
        obs=boundary(E(n),n+1); exp={m:Q(0) for m in range(1,n+2)}
        exp[n+1]+=1; exp[n]-=1; exp[1]-=1
        assert obs==exp
        for parent,child in E(n): assert 4*child>=parent; counts['balanced_commutator_edges']+=1
        if n>1:
            m=n; h=m//2
            if m%2==0:
                rec=add((Q(1),{(m+1,h):Q(1)}),(Q(-1),{(m,h):Q(1)}),(Q(1),E(h)))
            else:
                rec=add((Q(1),{(m+1,h+1):Q(1)}),(Q(-1),{(m,h):Q(1)}),(Q(1),E(h)))
            assert E(m)==rec
        assert sum(abs(v) for v in E(n).values())<=2*(n.bit_length()-1)+1
        counts['commutator_recursions']+=1
    for n in range(2,65):
        for j in range(1,n//2+1):
            for q in range(2,n+1):
                assert chi(2*n,2*j,2*q)==chi(n,j,q)
                counts['doubled_carry_cells']+=1
    a=Q(3,5)
    for Y in range(2,65):
        for salt in range(3):
            wY,wX=targets(Y,a,salt); rY=divergence(wY,Y); rX=divergence(wX,2*Y)
            assert rhs(rY,rX,wX[2],Y,a)==rX; counts['divergence_cases']+=1
            d=upper_flow(tree_flow(rY,Y),rX,wX[2],Y,a)
            assert boundary(d,2*Y)==rX and loads(d,2*Y)==wX
            counts['flow_cases']+=1
    for X in range(3,129):
        w={q:(Q(5,13*q) if q<X else Q(0)) for q in range(2,X+1)}
        r=divergence(w,X); d=tree_flow(r,X)
        assert boundary(d,X)==r and loads(d,X)==w
        counts['endpoint_increment_cases']+=1
    wY,wX=targets(31,a,4); rY=divergence(wY,31); rX=divergence(wX,62)
    mutations={
      'omit_bottom_charge':rhs(rY,rX,wX[2],31,a,omit_bottom=True)!=rX,
      'omit_odd_commutator':rhs(rY,rX,wX[2],31,a,omit=7)!=rX,
      'reverse_commutator_sign':rhs(rY,rX,wX[2],31,a,reverse=True)!=rX,
      'wrong_even_scaling':rhs(rY,rX,wX[2],31,Q(4,7))!=rX}
    assert all(mutations.values()); counts['mutations']=mutations
    result={'classification':'EXACT_DYADIC_DIVERGENCE_COMMUTATOR_INTERFACES_VERIFIED',
      'scope':{'certifies':['target-divergence half-scale identity','central-tree adjacent-commutator recursion','exact signed flow and carry-column replay','endpoint-increment exact realization'],
      'does_not_certify':['Dyadic Commutator Debt','Cycle Debt','a cofinal prime-ramp estimate','the Riemann Hypothesis']},'counts':counts}
    raw=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    result['proof_object_sha256']=sha256(raw).hexdigest(); return result


if __name__=='__main__':
    result=run(); out=Path(__file__).parent/'results'/'verification.json'; out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps(result,indent=2,sort_keys=True))
