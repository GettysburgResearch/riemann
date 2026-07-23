#!/usr/bin/env python3
"""Proof-producing powered canonical Robin search.

The search traverses every consecutive-prime, nonincreasing positive exponent
vector under an exact integer bound unless a terminal proof covers the subtree.
It retains the separate-cap ceiling and optionally strengthens it with the exact
powered shared-budget envelope of L-3502. Floating point is used only to rank
candidate dual pairs; every emitted prune is proved with exact rational and
outward dyadic arithmetic.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
sys.set_int_max_str_digits(0)
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Sequence
from certmath import RobinParameters, robin_rhs

FINITE_EXCEPTION=5040
SCHEMA="riemann.robin.powered-canonical-tree.v1"
DEFAULT_DUALS=((1,128),(1,96),(1,64),(3,128),(1,32),(5,128),(3,64),(7,128),(1,16))

def prime_stream()->Iterable[int]:
    ps=[]; c=2
    while True:
        ok=True
        for p in ps:
            if p*p>c: break
            if c%p==0: ok=False; break
        if ok: ps.append(c); yield c
        c=3 if c==2 else c+2

def first_primes(n:int)->list[int]:
    out=[]
    for p in prime_stream():
        if len(out)==n: break
        out.append(p)
    return out

def support_limit(B:int)->int:
    prod=1; k=0
    for p in prime_stream():
        if prod*p>B: return k
        prod*=p; k+=1
    raise AssertionError

def floor_log_power(limit:int,base:int)->int:
    if limit<1 or base<2: raise ValueError
    e=0; power=1
    while power<=limit//base: power*=base; e+=1
    return e

@lru_cache(maxsize=None)
def abundancy_pp(p:int,e:int)->Fraction:
    if p<2 or e<1: raise ValueError
    return Fraction(p**(e+1)-1,p**e*(p-1))

def fraction_json(x:Fraction)->dict[str,str]: return {"numerator":str(x.numerator),"denominator":str(x.denominator)}

def fraction_decimal_outward(x:Fraction,digits:int=30,*,upper:bool=True)->str:
    scale=10**digits; z=x.numerator*scale
    q=-((-z)//x.denominator) if upper else z//x.denominator
    sign="-" if q<0 else ""; raw=str(abs(q)).rjust(digits+1,"0")
    return sign+raw if digits==0 else f"{sign}{raw[:-digits]}.{raw[-digits:]}"

def canonical_bytes(x:object)->bytes: return json.dumps(x,sort_keys=True,separators=(",",":")).encode()

def product(xs):
    z=1
    for x in xs: z*=x
    return z

def parse_duals(text:str)->tuple[tuple[int,int],...]:
    if not text: return DEFAULT_DUALS
    out=[]
    for chunk in text.split(','):
        a_s,d_s=chunk.strip().split('/',1); a=int(a_s); d=int(d_s)
        if a<0 or d<1: raise ValueError("invalid dual")
        out.append((a,d))
    if not out: raise ValueError("empty dual ladder")
    return tuple(out)

def compute_caps(tail:list[int],A:int,M0:int)->list[int]:
    caps=[]
    for p in tail:
        e=1
        while e<A and p**e<=M0: e+=1
        caps.append(e)
    if any(x<y for x,y in zip(caps,caps[1:])): raise AssertionError
    return caps

def separate_data(prefix_n:int,prefix_I:Fraction,tail:list[int],A:int,B:int):
    R=product(tail)
    if prefix_n*R>B: raise RuntimeError("unreachable tail")
    M=(B//prefix_n)//R
    caps=compute_caps(tail,A,M)
    sep=prefix_I
    for p,e in zip(tail,caps): sep*=abundancy_pp(p,e)
    return R,M,caps,sep

def powered_log_bound(prefix_I:Fraction,tail:list[int],A:int,M0:int,caps:list[int],a:int,d:int)->float:
    lam=a/d
    base_log=math.log(float(prefix_I))
    for p in tail: base_log+=math.log(float(abundancy_pp(p,1)))
    n=len(tail); logQ=[0.0]
    s=0.0
    for p in tail: s+=math.log(p); logQ.append(s)
    nxt=[0.0]*(n+1)
    for level in range(A,1,-1):
        licensed=sum(c>=level for c in caps)
        gain=0.0; cand=[]
        for ell in range(licensed+1):
            if ell:
                p=tail[ell-1]
                gain+=math.log(float(abundancy_pp(p,level)/abundancy_pp(p,level-1)))
            cand.append(gain-lam*logQ[ell]+nxt[ell])
        row=[]; cur=cand[0]
        for m in range(n+1):
            if m<=licensed and cand[m]>cur: cur=cand[m]
            row.append(cur)
        nxt=row
    return base_log + (lam*math.log(M0) if M0>0 and a else 0.0) + (nxt[n] if A>=2 else 0.0)

def exact_powered(prefix_I:Fraction,tail:list[int],A:int,M0:int,caps:list[int],a:int,d:int)->dict[str,object]:
    base=prefix_I
    for p in tail: base*=abundancy_pp(p,1)
    n=len(tail); Q=[1]
    for p in tail: Q.append(Q[-1]*p)
    nxt=[Fraction(1) for _ in range(n+1)]
    for level in range(A,1,-1):
        licensed=sum(c>=level for c in caps)
        gain=Fraction(1); cand=[]
        for ell in range(licensed+1):
            if ell:
                p=tail[ell-1]
                gain*=abundancy_pp(p,level)/abundancy_pp(p,level-1)
            cand.append((gain**d/Fraction(Q[ell]**a,1))*nxt[ell])
        row=[]; cur=cand[0]
        for m in range(n+1):
            if m<=licensed and cand[m]>cur: cur=cand[m]
            row.append(cur)
        nxt=row
    V=nxt[n] if A>=2 else Fraction(1)
    powered=(base**d)*Fraction(M0**a,1)*V
    sep=prefix_I
    for p,e in zip(tail,caps): sep*=abundancy_pp(p,e)
    sep_power=sep**d
    return {"powered":powered,"separate":sep,"separate_power":sep_power,"joint":min(powered,sep_power)}

def root_upper(r:Fraction,d:int,bits:int=160)->Fraction:
    if r<0: raise ValueError
    if r==0: return Fraction(0)
    scale=1<<bits; lo=0; hi=scale
    while lo<hi:
        m=(lo+hi)//2
        if m**d*r.denominator >= r.numerator*scale**d: hi=m
        else: lo=m+1
    return Fraction(lo,scale)

@dataclass
class Counts:
    separate_prunes:int=0
    powered_prunes:int=0
    powered_candidate_nodes:int=0
    satisfied_leaves:int=0
    below_domain_leaves:int=0
    unresolved_leaves:int=0
    violation_leaves:int=0
    internal_nodes:int=0

class Search:
    def __init__(self,B:int,params:RobinParameters,duals:tuple[tuple[int,int],...],root_bits:int=160):
        if B<=FINITE_EXCEPTION: raise ValueError
        params.validate(); self.B=B; self.params=params; self.duals=duals; self.root_bits=root_bits
        self.kmax=support_limit(B); self.primes=first_primes(self.kmax); self.streams=[[] for _ in range(self.kmax)]
        self.counts=Counts(); self.tight_ratio=Fraction(0); self.tight=None
        self.closest_score=-math.inf; self.closest_n=1; self.closest_exp=[]; self.closest_I=Fraction(0)
        self.powered_dual_use={f"{a}/{d}":0 for a,d in duals}
    def emit(self,K:int,code:str,prefix:Sequence[int],dual=None):
        payload=','.join(map(str,prefix))
        token=(f"J:{dual[0]},{dual[1]}:{payload}" if code=='J' else f"{code}:{payload}")
        self.streams[K-1].append(token)
    def consider(self,*,kind,K,prefix,nref,ratio:Fraction,extra=None):
        if ratio>=1: raise RuntimeError("non-strict ratio")
        if ratio>self.tight_ratio:
            self.tight_ratio=ratio
            obj={"kind":kind,"support":K,"prefix":list(prefix),"reference_n":str(nref),
                 "normalized_ratio_upper":fraction_json(ratio),
                 "normalized_ratio_upper_decimal_outward":fraction_decimal_outward(ratio)}
            if extra: obj.update(extra)
            self.tight=obj
    def run(self):
        for K in range(1,self.kmax+1):
            ps=self.primes[:K]; suffix=[1]*(K+1)
            for i in range(K-1,-1,-1): suffix[i]=suffix[i+1]*ps[i]
            self.visit(K,ps,suffix,(),1,Fraction(1),None)
        complete=self.counts.unresolved_leaves==0 and self.counts.violation_leaves==0
        body={"schema":SCHEMA,"status":self.status(),
              "finite_region":{"integer_lower":5041,"integer_upper":str(self.B),"canonical_support_max":self.kmax,
              "definition":"all consecutive-prime nonincreasing positive exponent vectors under integer_upper"},
              "parameters":asdict(self.params),"dual_ladder":[{"a":a,"d":d} for a,d in self.duals],
              "root_upper_bits":self.root_bits,"prime_prefix":self.primes,"counts":asdict(self.counts),
              "powered_dual_use":self.powered_dual_use,
              "terminal_stream_encoding":{"codes":{"P":"separate-cap prune","J":"powered shared-budget prune with exact a,d","S":"satisfied leaf","B":"below-domain leaf","U":"unresolved leaf","V":"violation leaf"},
              "forms":["P:e1,e2,...","J:a,d:e1,e2,...","S:e1,e2,..."],"order":"deterministic DFS, exponents descending"},
              "terminal_streams":self.streams,"global_canonical_normalized_ratio_upper":self.tight if complete else None,
              "all_integer_consequence":self.all_integer() if complete else None,
              "closest_checked_leaf_discovery_only":{"n":str(self.closest_n),"exponents":self.closest_exp,"abundancy":fraction_json(self.closest_I),
                  "normalized_ratio_binary64":None if self.closest_score==-math.inf else format(self.closest_score,'.17g')},
              "proof_boundary":"Covers only the exact finite region. Powered prune choices are proposal-only until exact rational replay; the all-integer transfer also depends on T-2001/T-2002."}
        body["certificate_sha256"]=hashlib.sha256(canonical_bytes(body)).hexdigest(); return body
    def status(self):
        if self.counts.violation_leaves: return "CERTIFIED_VIOLATION_FOUND_PENDING_INDEPENDENT_VERIFICATION"
        if self.counts.unresolved_leaves: return "INCOMPLETE_UNRESOLVED_INTERVALS"
        return "CERTIFIED_FINITE_REGION_PENDING_INDEPENDENT_VERIFICATION"
    def all_integer(self):
        r5041=robin_rhs(5041,self.params); r5583=robin_rhs(5583,self.params)
        cases={"finite_window_5041_5582":Fraction(224,65)/Fraction(r5041.lo,1<<self.params.bits),
               "canonical_image_at_most_5040_for_n_at_least_5583":Fraction(403,105)/Fraction(r5583.lo,1<<self.params.bits),
               "canonical_image_above_5040":self.tight_ratio}
        label,val=max(cases.items(),key=lambda z:z[1])
        if val>=1: raise RuntimeError
        return {"status":"PROPOSED_LOGICAL_CONSEQUENCE_WITH_VERIFIED_ARITHMETIC","dependencies":["T-2001","T-2002","L-3502"],
                "integer_range":[5041,str(self.B)],"case_bounds":{k:{"normalized_ratio_upper":fraction_json(v),"decimal_outward":fraction_decimal_outward(v)} for k,v in cases.items()},
                "controlling_case":label,"normalized_ratio_upper":fraction_json(val),"normalized_ratio_upper_decimal_outward":fraction_decimal_outward(val),
                "conclusion":"Assuming the named structural dependencies, every integer in the stated finite range satisfies Robin's strict inequality."}
    def visit(self,K,ps,suffix,prefix,prefix_n,prefix_I,prev):
        depth=len(prefix)
        if depth==K: self.leaf(K,prefix,prefix_n,prefix_I); return
        self.counts.internal_nodes+=1
        if prefix:
            A=prefix[-1]; nmin=prefix_n*suffix[depth]; tail=list(ps[depth:])
            R,M0,caps,sep=separate_data(prefix_n,prefix_I,tail,A,self.B)
            heuristic=math.exp(0.5772156649015329)*math.log(math.log(nmin))
            if float(sep)<heuristic*(1-1e-13):
                rhs=robin_rhs(nmin,self.params)
                if rhs.lower_gt_fraction(sep):
                    ratio=sep/Fraction(rhs.lo,1<<self.params.bits)
                    self.emit(K,'P',prefix); self.counts.separate_prunes+=1
                    self.consider(kind="PRUNE_SEPARATE",K=K,prefix=prefix,nref=nmin,ratio=ratio,
                                  extra={"abundancy_ceiling":fraction_json(sep),"rhs_lower":{"bits":self.params.bits,"lower_numerator":str(rhs.lo)}})
                    return
            self.counts.powered_candidate_nodes+=1
            log_rhs=math.log(heuristic)
            ranked=[]
            for a,d in self.duals:
                try: b=powered_log_bound(prefix_I,tail,A,M0,caps,a,d)
                except (OverflowError,ValueError): continue
                ranked.append((b,a,d))
            ranked.sort()
            for b,a,d in ranked[:3]:
                if b>=log_rhs-1e-10: continue
                ex=exact_powered(prefix_I,tail,A,M0,caps,a,d)
                rhs=robin_rhs(nmin,self.params); rhsq=Fraction(rhs.lo,1<<self.params.bits)
                if ex["joint"]<rhsq**d:
                    ratio=root_upper(ex["joint"]/(rhsq**d),d,self.root_bits)
                    if ratio>=1: raise RuntimeError("root enclosure lost strictness")
                    self.emit(K,'J',prefix,(a,d)); self.counts.powered_prunes+=1; self.powered_dual_use[f"{a}/{d}"]+=1
                    self.consider(kind="PRUNE_POWERED",K=K,prefix=prefix,nref=nmin,ratio=ratio,
                                  extra={"dual":{"a":a,"d":d},"powered_proof_recomputed_from_token":True,
                                         "rhs_lower":{"bits":self.params.bits,"lower_numerator":str(rhs.lo)},
                                         "root_upper_bits":self.root_bits})
                    return
        p=ps[depth]; tail_after=suffix[depth+1]; budget=self.B//(prefix_n*tail_after); mx=floor_log_power(budget,p)
        if prev is not None: mx=min(prev,mx)
        if mx<1: raise RuntimeError("dead internal node")
        for e in range(mx,0,-1):
            self.visit(K,ps,suffix,prefix+(e,),prefix_n*p**e,prefix_I*abundancy_pp(p,e),e)
    def leaf(self,K,exps,n,I):
        if n<=FINITE_EXCEPTION:
            self.emit(K,'B',exps); self.counts.below_domain_leaves+=1; return
        score=float(I)/(math.exp(0.5772156649015329)*math.log(math.log(n)))
        if score>self.closest_score: self.closest_score=score; self.closest_n=n; self.closest_exp=list(exps); self.closest_I=I
        rhs=robin_rhs(n,self.params)
        if rhs.lower_gt_fraction(I):
            self.emit(K,'S',exps); self.counts.satisfied_leaves+=1
            ratio=I/Fraction(rhs.lo,1<<self.params.bits)
            self.consider(kind="LEAF_SATISFIED",K=K,prefix=exps,nref=n,ratio=ratio,
                          extra={"abundancy_ceiling":fraction_json(I),"rhs_lower":{"bits":self.params.bits,"lower_numerator":str(rhs.lo)}})
        elif rhs.upper_le_fraction(I): self.emit(K,'V',exps); self.counts.violation_leaves+=1
        else: self.emit(K,'U',exps); self.counts.unresolved_leaves+=1

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--n-max',type=int,required=True); ap.add_argument('--bits',type=int,default=160)
    ap.add_argument('--log-terms',type=int,default=56); ap.add_argument('--exp-terms',type=int,default=56); ap.add_argument('--harmonic-cutoff',type=int,default=30000)
    ap.add_argument('--duals',default=''); ap.add_argument('--root-upper-bits',type=int,default=160); ap.add_argument('--output',required=True)
    a=ap.parse_args(argv); params=RobinParameters(a.bits,a.log_terms,a.exp_terms,a.harmonic_cutoff)
    cert=Search(a.n_max,params,parse_duals(a.duals),a.root_upper_bits).run(); Path(a.output).write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:cert[k] for k in ('status','finite_region','counts','powered_dual_use','global_canonical_normalized_ratio_upper','all_integer_consequence','certificate_sha256')},indent=2))
    return 2 if cert['status']=="INCOMPLETE_UNRESOLVED_INTERVALS" else 0
if __name__=='__main__': raise SystemExit(main())
