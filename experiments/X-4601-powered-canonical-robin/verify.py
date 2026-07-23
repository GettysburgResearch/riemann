#!/usr/bin/env python3
"""Independent replay verifier for powered canonical Robin certificates."""
from __future__ import annotations
import argparse, gzip, hashlib, json, sys
sys.set_int_max_str_digits(0)
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from certmath import RobinParameters, robin_rhs

SCHEMA="riemann.robin.powered-canonical-tree.v1"; FINITE_EXCEPTION=5040

def primes_trial(n):
    out=[]; x=2
    while len(out)<n:
        ok=True
        d=2
        while d*d<=x:
            if x%d==0: ok=False; break
            d+=1
        if ok: out.append(x)
        x+=1
    return out

@lru_cache(maxsize=None)
def Ipp(p,e):
    if e<1: raise ValueError
    num=0; q=1
    for _ in range(e+1): num+=q; q*=p
    return Fraction(num,p**e)

def exact_floor_log(limit,base):
    e=0
    while pow(base,e+1)<=limit: e+=1
    return e

def fj(x): return {"numerator":str(x.numerator),"denominator":str(x.denominator)}

def fdec(x,digits=30):
    s=10**digits; z=x.numerator*s; q=-((-z)//x.denominator); raw=str(abs(q)).rjust(digits+1,'0'); sign='-' if q<0 else ''
    return sign+raw if digits==0 else f"{sign}{raw[:-digits]}.{raw[-digits:]}"

def digest_without(c):
    x=dict(c); x.pop('certificate_sha256',None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def direct_support_limit(B):
    prod=1; k=0; x=2
    while True:
        prime=True
        d=2
        while d*d<=x:
            if x%d==0: prime=False; break
            d+=1
        if prime:
            if prod*x>B: return k
            prod*=x; k+=1
        x+=1

def product(xs):
    z=1
    for x in xs: z*=x
    return z

def root_upper(q,d,bits):
    if q<0: raise ValueError
    scale=1<<bits; L=0; U=scale
    while L<U:
        m=(L+U)//2
        if pow(m,d)*q.denominator >= q.numerator*pow(scale,d): U=m
        else: L=m+1
    return Fraction(L,scale)

def direct_caps(prefix_n,tail,A,B):
    R=product(tail); caps=[]
    for p in tail:
        other=R//p; e=1
        while e<A and prefix_n*pow(p,e+1)*other<=B: e+=1
        if prefix_n*pow(p,e)*other>B: raise ValueError("invalid reachable tail")
        caps.append(e)
    return caps

def powered_joint(prefix_I,tail,A,caps,prefix_n,B,a,d):
    R=product(tail); M0=(B//prefix_n)//R
    base=prefix_I
    for p in tail: base*=Ipp(p,1)
    n=len(tail)
    prime_prefix_products=[1]
    for p in tail: prime_prefix_products.append(prime_prefix_products[-1]*p)
    levels=[]
    for r in range(2,A+1):
        licensed=sum(c>=r for c in caps); gain=Fraction(1); row=[]
        for ell in range(licensed+1):
            if ell:
                p=tail[ell-1]; gain*=Ipp(p,r)/Ipp(p,r-1)
            row.append(gain**d/Fraction(prime_prefix_products[ell]**a,1))
        levels.append((r,row))
    continuation=[Fraction(1)]*(n+1)
    for _,weights in reversed(levels):
        licensed=len(weights)-1; new=[]
        for m in range(n+1):
            best=None
            for ell in range(min(m,licensed)+1):
                val=weights[ell]*continuation[ell]
                if best is None or val>best: best=val
            new.append(best if best is not None else Fraction(1))
        continuation=new
    V=continuation[n] if levels else Fraction(1)
    powered=(base**d)*Fraction(M0**a,1)*V
    sep=prefix_I
    for p,e in zip(tail,caps): sep*=Ipp(p,e)
    return min(powered,sep**d),sep

class Cursor:
    def __init__(self,tokens):
        if not isinstance(tokens,list) or not all(isinstance(x,str) for x in tokens): raise ValueError("bad stream")
        self.t=tokens; self.i=0
    def peek(self): return None if self.i==len(self.t) else self.parse(self.t[self.i])
    def consume(self):
        x=self.peek()
        if x is None: raise ValueError("stream ended")
        self.i+=1; return x
    def done(self): return self.i==len(self.t)
    @staticmethod
    def parse(token):
        if token.startswith('J:'):
            parts=token.split(':',2)
            if len(parts)!=3: raise ValueError("bad J token")
            a_s,d_s=parts[1].split(',',1); a=int(a_s); d=int(d_s); payload=parts[2]
            code='J'; dual=(a,d)
        else:
            if len(token)<2 or token[1]!=':': raise ValueError("bad token")
            code=token[0]; payload=token[2:]; dual=None
            if code not in 'PSBUV': raise ValueError("bad code")
        prefix=() if payload=='' else tuple(int(x) for x in payload.split(','))
        if any(e<1 for e in prefix): raise ValueError("nonpositive exponent")
        return code,dual,prefix

class Verifier:
    def __init__(self,c):
        self.c=c
        if c.get('schema')!=SCHEMA: raise ValueError('schema')
        reg=c.get('finite_region'); self.B=int(reg['integer_upper']); self.k=int(reg['canonical_support_max'])
        if int(reg['integer_lower'])!=5041 or self.B<=5040: raise ValueError('region')
        rp=c.get('parameters'); self.params=RobinParameters(**{k:int(v) for k,v in rp.items()}); self.params.validate()
        self.root_bits=int(c.get('root_upper_bits'))
        dl=c.get('dual_ladder'); self.duals={(int(x['a']),int(x['d'])) for x in dl}
        self.primes=primes_trial(self.k)
        if c.get('prime_prefix')!=self.primes: raise ValueError('prime prefix')
        self.streams=c.get('terminal_streams')
        if not isinstance(self.streams,list) or len(self.streams)!=self.k: raise ValueError('streams')
        self.counts={"separate_prunes":0,"powered_prunes":0,"powered_candidate_nodes":0,"satisfied_leaves":0,"below_domain_leaves":0,"unresolved_leaves":0,"violation_leaves":0,"internal_nodes":0}
        self.dual_use={f"{a}/{d}":0 for a,d in sorted(self.duals,key=lambda x:list(self.duals).index(x) if False else (x[1],x[0]))}
        self.dual_use={k:0 for k in c.get('powered_dual_use',{})}
        self.tight_ratio=Fraction(0); self.tight=None; self.cur=None
    def consider(self,kind,K,prefix,nref,ratio,extra=None):
        if ratio>=1: raise ValueError('non-strict terminal')
        if ratio>self.tight_ratio:
            self.tight_ratio=ratio; obj={"kind":kind,"support":K,"prefix":list(prefix),"reference_n":str(nref),"normalized_ratio_upper":fj(ratio),"normalized_ratio_upper_decimal_outward":fdec(ratio)}
            if extra: obj.update(extra)
            self.tight=obj
    def replay(self):
        if self.k!=direct_support_limit(self.B): raise ValueError('support max')
        for K in range(1,self.k+1):
            self.cur=Cursor(self.streams[K-1]); ps=self.primes[:K]; suffix=[1]*(K+1)
            for i in range(K-1,-1,-1): suffix[i]=suffix[i+1]*ps[i]
            self.walk(K,ps,suffix,(),1,Fraction(1),None)
            if not self.cur.done(): raise ValueError(f'extra tokens support {K}')
        self.cur=None
        status=self.status(); complete=not self.counts['unresolved_leaves'] and not self.counts['violation_leaves']
        return {"status":status,"counts":self.counts,"powered_dual_use":self.dual_use,"global_canonical_normalized_ratio_upper":self.tight if complete else None,"all_integer_consequence":self.all_integer() if complete else None}
    def status(self):
        if self.counts['violation_leaves']: return 'CERTIFIED_VIOLATION_FOUND_PENDING_INDEPENDENT_VERIFICATION'
        if self.counts['unresolved_leaves']: return 'INCOMPLETE_UNRESOLVED_INTERVALS'
        return 'CERTIFIED_FINITE_REGION_PENDING_INDEPENDENT_VERIFICATION'
    def all_integer(self):
        a=Fraction(224,65)/Fraction(robin_rhs(5041,self.params).lo,1<<self.params.bits)
        b=Fraction(403,105)/Fraction(robin_rhs(5583,self.params).lo,1<<self.params.bits)
        cases={"finite_window_5041_5582":a,"canonical_image_at_most_5040_for_n_at_least_5583":b,"canonical_image_above_5040":self.tight_ratio}
        label,val=max(cases.items(),key=lambda z:z[1])
        return {"status":"PROPOSED_LOGICAL_CONSEQUENCE_WITH_VERIFIED_ARITHMETIC","dependencies":["T-2001","T-2002","L-3502"],"integer_range":[5041,str(self.B)],
                "case_bounds":{k:{"normalized_ratio_upper":fj(v),"decimal_outward":fdec(v)} for k,v in cases.items()},"controlling_case":label,
                "normalized_ratio_upper":fj(val),"normalized_ratio_upper_decimal_outward":fdec(val),"conclusion":"Assuming the named structural dependencies, every integer in the stated finite range satisfies Robin's strict inequality."}
    def walk(self,K,ps,suffix,prefix,prefix_n,prefix_I,prev):
        depth=len(prefix)
        if depth==K: self.leaf(K,prefix,prefix_n,prefix_I); return
        self.counts['internal_nodes']+=1
        nxt=self.cur.peek()
        if nxt is not None and nxt[2]==prefix:
            code,dual,_=self.cur.consume()
            if code=='P': self.verify_sep(K,ps,suffix,prefix,prefix_n,prefix_I); self.counts['separate_prunes']+=1; return
            if code=='J': self.verify_joint(K,ps,suffix,prefix,prefix_n,prefix_I,dual); self.counts['powered_prunes']+=1; self.counts['powered_candidate_nodes']+=1; return
            raise ValueError('leaf token at internal node')
        if prefix: self.counts['powered_candidate_nodes']+=1
        p=ps[depth]; tail_after=suffix[depth+1]; budget=self.B//(prefix_n*tail_after); mx=exact_floor_log(budget,p)
        if prev is not None: mx=min(prev,mx)
        if mx<1: raise ValueError('dead node')
        for e in range(mx,0,-1): self.walk(K,ps,suffix,prefix+(e,),prefix_n*p**e,prefix_I*Ipp(p,e),e)
    def verify_sep(self,K,ps,suffix,prefix,prefix_n,prefix_I):
        if not prefix: raise ValueError('root prune')
        depth=len(prefix); A=prefix[-1]; tail=list(ps[depth:]); nmin=prefix_n*suffix[depth]; caps=direct_caps(prefix_n,tail,A,self.B)
        sep=prefix_I
        for p,e in zip(tail,caps): sep*=Ipp(p,e)
        rhs=robin_rhs(nmin,self.params)
        if not rhs.lower_gt_fraction(sep): raise ValueError('invalid separate prune')
        self.consider('PRUNE_SEPARATE',K,prefix,nmin,sep/Fraction(rhs.lo,1<<self.params.bits),{"abundancy_ceiling":fj(sep),"rhs_lower":{"bits":self.params.bits,"lower_numerator":str(rhs.lo)}})
    def verify_joint(self,K,ps,suffix,prefix,prefix_n,prefix_I,dual):
        if not prefix or dual is None or dual not in self.duals: raise ValueError('unlicensed powered prune')
        a,d=dual; depth=len(prefix); A=prefix[-1]; tail=list(ps[depth:]); nmin=prefix_n*suffix[depth]; caps=direct_caps(prefix_n,tail,A,self.B)
        joint,_=powered_joint(prefix_I,tail,A,caps,prefix_n,self.B,a,d); rhs=robin_rhs(nmin,self.params); rq=Fraction(rhs.lo,1<<self.params.bits)
        if not joint<rq**d: raise ValueError('invalid powered prune')
        ratio=root_upper(joint/(rq**d),d,self.root_bits)
        if ratio>=1: raise ValueError('powered root not strict')
        key=f"{a}/{d}"
        if key not in self.dual_use: raise ValueError('dual summary missing key')
        self.dual_use[key]+=1
        self.consider('PRUNE_POWERED',K,prefix,nmin,ratio,{"dual":{"a":a,"d":d},"powered_proof_recomputed_from_token":True,"rhs_lower":{"bits":self.params.bits,"lower_numerator":str(rhs.lo)},"root_upper_bits":self.root_bits})
    def leaf(self,K,exps,n,I):
        code,dual,pref=self.cur.consume()
        if dual is not None or pref!=exps: raise ValueError('leaf identity')
        if n<=5040:
            if code!='B': raise ValueError('below label')
            self.counts['below_domain_leaves']+=1; return
        rhs=robin_rhs(n,self.params)
        if rhs.lower_gt_fraction(I):
            expected='S'; self.counts['satisfied_leaves']+=1
            self.consider('LEAF_SATISFIED',K,exps,n,I/Fraction(rhs.lo,1<<self.params.bits),{"abundancy_ceiling":fj(I),"rhs_lower":{"bits":self.params.bits,"lower_numerator":str(rhs.lo)}})
        elif rhs.upper_le_fraction(I): expected='V'; self.counts['violation_leaves']+=1
        else: expected='U'; self.counts['unresolved_leaves']+=1
        if code!=expected: raise ValueError('leaf class')
    def verify(self):
        r=self.replay()
        if self.c.get('counts')!=r['counts']: raise ValueError(f"counts mismatch {self.c.get('counts')} != {r['counts']}")
        if self.c.get('powered_dual_use')!=r['powered_dual_use']: raise ValueError('dual use')
        for k in ('status','global_canonical_normalized_ratio_upper','all_integer_consequence'):
            if self.c.get(k)!=r[k]: raise ValueError(f'{k} mismatch')
        dg=digest_without(self.c)
        if self.c.get('certificate_sha256')!=dg: raise ValueError('digest')
        return {"schema":"riemann.robin.powered-canonical-tree.verification.v1","verified":True,"status":r['status'],"finite_region":self.c['finite_region'],"counts":r['counts'],"powered_dual_use":r['powered_dual_use'],"global_canonical_normalized_ratio_upper":r['global_canonical_normalized_ratio_upper'],"all_integer_consequence":r['all_integer_consequence'],"certificate_sha256":dg,
                "proof_boundary":"Replays the exact finite forest and every separate/powered arithmetic proof. Structural transfer claims and the shared dyadic transcendental kernel retain their repository statuses."}

def load_certificate(path: str) -> dict[str, object]:
    file_path = Path(path)
    if file_path.suffix == '.gz':
        with gzip.open(file_path, 'rt', encoding='utf-8') as handle:
            value = json.load(handle)
    else:
        value = json.loads(file_path.read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError('certificate root must be an object')
    return value

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('certificate'); ap.add_argument('--output'); a=ap.parse_args(argv)
    c=load_certificate(a.certificate); out=Verifier(c).verify(); text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output: Path(a.output).write_text(text)
    else: print(text,end='')
    return 0
if __name__=='__main__': raise SystemExit(main())
