#!/usr/bin/env python3
"""Finite exact controls for GCP26. These do not prove its infinite asymptotics."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

BITS = 160
SCALE = 1 << BITS
ROOT = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def strict_object(pairs):
    d = {}
    for k, v in pairs:
        require(k not in d, 'duplicate JSON key')
        d[k] = v
    return d


def load_json(path):
    def bad(x):
        raise ValueError('non-integer numeric literal')
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=strict_object,
                      parse_float=bad, parse_constant=bad)


def ceildiv(a, b):
    return -((-a)//b)


class I:
    def __init__(self, lo, hi):
        require(type(lo) is int and type(hi) is int and lo <= hi, 'invalid interval')
        self.lo, self.hi = lo, hi
    @staticmethod
    def exact(x):
        x = F(x)
        return I((x.numerator*SCALE)//x.denominator,
                 ceildiv(x.numerator*SCALE, x.denominator))
    def __add__(self, other):
        if not isinstance(other, I): other = I.exact(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        if not isinstance(other, I): other = I.exact(other)
        return self+-other
    def __mul__(self, other):
        if not isinstance(other, I): other = I.exact(other)
        p = [self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi]
        return I(min(p)//SCALE, ceildiv(max(p), SCALE))
    __rmul__ = __mul__
    def __truediv__(self, other):
        if not isinstance(other, I): other = I.exact(other)
        require(other.lo > 0, 'division denominator not strictly positive')
        vals = [F(a*SCALE,b) for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        low, high = min(vals), max(vals)
        return I(low.numerator//low.denominator, ceildiv(high.numerator,high.denominator))
    def enclosed_by(self, a, b):
        return F(self.lo,SCALE)>F(a) and F(self.hi,SCALE)<F(b)
    def data(self):
        return {'lo': str(self.lo), 'hi': str(self.hi), 'denominator': '2^160'}


def log_bounds(n):
    require(type(n) is int and n >= 1, 'log input')
    k=n.bit_length()-1
    def series(x):
        acc=F(0); power=x
        for j in range(100):
            acc += 2*power/(2*j+1)
            power *= x*x
        rem=2*power/(201*(1-x*x))
        return acc, acc+rem
    lo2,hi2=series(F(1,3))
    x=F(n-(1<<k), n+(1<<k))
    lo,hi=series(x)
    lo+=k*lo2; hi+=k*hi2
    return I((lo.numerator*SCALE)//lo.denominator,
             ceildiv(hi.numerator*SCALE,hi.denominator))


def prime_list(N):
    flags=[True]*(N+1)
    if N>=0:flags[0]=False
    if N>=1:flags[1]=False
    for p in range(2, math.isqrt(N)+1):
        if flags[p]:
            for n in range(p*p,N+1,p):flags[n]=False
    out=[n for n in range(2,N+1) if flags[n]]
    trial=[n for n in range(2,N+1) if all(n%d for d in range(2,math.isqrt(n)+1))]
    require(out==trial, 'prime sieve mismatch')
    return out


def rows(ps, mode, directed=False):
    row=[(F(1), I.exact(0) if directed else F(0), ())]
    for i,p in enumerate(ps):
        b=F(1,p if mode=='sf' else p-1)
        rate=log_bounds(p) if directed else F(i+1)
        a=rate*(1+b)
        row += [(w*b,l+a,D+(p,)) for w,l,D in row[:]]
    return row[1:]


def solve(A,b):
    n=len(b); a=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        require(k is not None,'singular finite matrix')
        a[j],a[k]=a[k],a[j]
        c=a[j][j];a[j]=[v/c for v in a[j]]
        for i in range(n):
            if i!=j:
                c=a[i][j]
                a[i]=[u-c*v for u,v in zip(a[i],a[j])]
    return [a[i][-1] for i in range(n)]


def graph_panel(ps,caps):
    states=list(itertools.product(*[range(m+1) for m in caps]))
    values=[math.prod(p**e for p,e in zip(ps,st)) for st in states]
    Z=sum((F(1,n) for n in values),F(0));mu=[F(1,n)/Z for n in values]
    ind={st:i for i,st in enumerate(states)};n=len(states)
    L=[[F(0) for _ in states] for __ in states];edges=0
    for i,st in enumerate(states):
        for h,(p,m) in enumerate(zip(ps,caps)):
            rate=F(h+1) # formal positive rational log-prime surrogate
            for k in range(1,m-st[h]+1):
                st2=list(st);st2[h]+=k;j=ind[tuple(st2)]
                birth=rate/F(p**k);death=rate
                L[i][i]+=birth;L[i][j]-=birth
                L[j][j]+=death;L[j][i]-=death;edges+=1
    eigen=[]
    one=[]
    for h,(p,m) in enumerate(zip(ps,caps)):
        vec=[([F(1)]*(m+1),F(0))]
        for j in range(1,m+1):
            a=sum((F(1,p**l) for l in range(1,m-j+2)),F(0))
            v=[F(0) if e<j-1 else -a if e==j-1 else F(1) for e in range(m+1)]
            vec.append((v,F(h+1)*(j+a)))
        one.append(vec)
    for choice in itertools.product(*[range(m+1) for m in caps]):
        v=[math.prod(one[h][choice[h]][0][st[h]] for h in range(len(ps))) for st in states]
        lam=sum((one[h][choice[h]][1] for h in range(len(ps))),F(0))
        Lv=[sum((a*b for a,b in zip(row,v)),F(0)) for row in L]
        require(Lv==[lam*u for u in v],'one-prime or tensor eigen identity')
        norm=sum((mi*vi*vi for mi,vi in zip(mu,v)),F(0))
        require(norm>0,'zero spectral vector')
        eigen.append((lam,v,norm))
    for i in range(n):
        for j in range(i):
            require(sum((m*a*b for m,a,b in zip(mu,eigen[i][1],eigen[j][1])),F(0))==0,'orthogonality')
    G=sum((v[0]**2/(norm*lam) for lam,v,norm in eigen if lam),F(0))
    H=sum((v[0]**2/(norm*lam**2) for lam,v,norm in eigen if lam),F(0))
    green=[sum((v[0]*v[i]/(norm*lam) for lam,v,norm in eigen if lam),F(0)) for i in range(n)]
    require(sum((m*v for m,v in zip(mu,green)),F(0))==0,'Green mean')
    require(green[0]==G,'Green root')
    Lg=[sum((a*b for a,b in zip(row,green)),F(0)) for row in L]
    require(sum((m*a*b for m,a,b in zip(mu,green,Lg)),F(0))==G,'Green energy')
    require(sum((m*a*a for m,a in zip(mu,green)),F(0))==H,'Green norm')
    anchored=sum((m*(v-G)**2 for m,v in zip(mu,green)),F(0))
    require(anchored==H+G*G,'anchor and center differ')
    for tau in [F(1),F(-2),F(2,3)]:
        for sign in [-1,1]:
            c=tau*tau*G+F(sign,3)
            trial=[-tau*x for x in green]
            Lt=[sum((a*b for a,b in zip(row,trial)),F(0)) for row in L]
            energy=sum((m*a*b for m,a,b in zip(mu,trial,Lt)),F(0))
            require(c+2*tau*trial[0]+energy==F(sign,3),'complete root Schur test')
    # Independently invert the shifted full generator, not its eigen formula.
    mat=[[L[i][j]+(1 if i==j else 0) for j in range(n)] for i in range(n)]
    xi=[F(1)/mu[0]]+[F(0)]*(n-1)
    x=solve(mat,xi)
    pred=sum((v[0]**2/(norm*(lam+1)) for lam,v,norm in eigen),F(0))
    require(x[0]==pred,'resolvent spectral formula')
    return {'primes':ps,'caps':caps,'vertices':n,'edges':edges,
            'G_formal':str(G),'H_formal':str(H)}


def make_result():
    ps=prime_list(257)
    panels=[graph_panel([2],[m]) for m in [1,2,3,5]]
    panels += [graph_panel([2,3],[1,1]),graph_panel([2,3],[2,2]),
               graph_panel([2,3,5],[1,1,1]),graph_panel([2,3,5,7],[1,1,1,1])]
    numerical={}
    brackets={
      'sf':('1.18532285971072','1.18532285971074','1.91594153472685','1.91594153472687'),
      'geo':('1.82250119177775','1.82250119177777','2.37221708831717','2.37221708831720')}
    for mode in ['sf','geo']:
        rr=rows([p for p in ps if p<=13],mode,True)
        G=I.exact(0);H=I.exact(0)
        for w,l,D in rr:
            G+=I.exact(w)/l;H+=I.exact(w)/(l*l)
        gl,gh,cl,ch=brackets[mode]
        require(G.enclosed_by(gl,gh),'actual root-cost bracket')
        endpoints=[]
        for c in [cl,ch]:
            Fval=I.exact(0)
            for w,l,D in rr:Fval+=I.exact(w)/(l*F(c)-1)
            endpoints.append(Fval)
        require(endpoints[0].lo>SCALE and endpoints[1].hi<SCALE,'actual secular root bracket')
        numerical[mode]={'prime_cutoff':13,'visible_nonempty_subsets':len(rr),
                         'G':G.data(),'H':H.data(),'G_readable_bracket':[gl,gh],
                         'C_readable_bracket':[cl,ch],
                         'secular_at_lower':endpoints[0].data(),
                         'secular_at_upper':endpoints[1].data()}
    require(log_bounds(2).enclosed_by(F(2,3),F(3,4)),'log2 endpoints')
    # Sharpness and root modes for the one-prime formula, at many rational rates.
    oneprime=0
    for p in [2,3,5,7,11,13]:
        for m in [1,2,3,4]:
            b=sum((F(1,p**j) for j in range(1,m+1)),F(0))
            rate=F(p+1,p);lam=(1+b)*rate;c=1/rate
            require(b/(c*lam-1)==1,'one-prime grounded rate')
            require(b/lam<c<=b/lam+1/lam,'contrast bounds')
            oneprime+=1
    return {'status':'PROPOSED_COMPONENT_THEOREMS','rh_proved':False,
            'all_set_centered_constant_gap_proved':False,
            'arithmetic_implementation':'integer/Fraction and 160-bit outward dyadic intervals',
            'prime_sieve_trial_range':257,'prime_count':len(ps),
            'exact_formal_graph_panels':panels,'one_prime_secular_controls':oneprime,
            'actual_root_certificates':numerical,
            'scope':'Finite identities and two finite-prime root costs. Infinite asymptotics are paper proofs; geo spectra are analytically reduced to finitely many visible modes.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--write',type=Path)
    args=ap.parse_args();r=make_result()
    text=json.dumps(r,sort_keys=True,indent=2)+'\n'
    if args.check:
        old=load_json(args.check)
        require(json.dumps(old,sort_keys=True,separators=(',',':'))==json.dumps(r,sort_keys=True,separators=(',',':')),'retained result mismatch')
    if args.write:args.write.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':
    main()
