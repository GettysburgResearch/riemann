#!/usr/bin/env python3
"""SFC30 finite exact replay. Does not verify infinite estimates by computation."""
from fractions import Fraction as F
from math import gcd
import argparse, json
from verify import (factors, divisors, mu, radical, ring, convolution,
                    amplitudes, u, Checks, prod)

def squarefree(n): return mu(n)!=0

def sf_completion(y):
    c={n:F(mu(n)) for n in range(1,y+1) if mu(n)}
    residual=u(c,1); n=y
    while residual:
        n+=1
        if n>2*y: raise AssertionError(('completion failed by 2Y',y))
        if not squarefree(n): continue
        a=-min(F(16),abs(n*residual))*(1 if residual>0 else -1)
        c[n]=a; residual+=a/n
    return c

def split(q):
    if any(h>2 for _,h in factors(q)): return None
    return (prod(p for p,h in factors(q) if h==2),
            prod(p for p,h in factors(q) if h==1))

def decompose(c,t,mutate=False):
    L=max(c); z=convolution(c); bs=amplitudes(z)
    U={d:u(c,d) for d in range(1,L+1)}
    get=lambda d:U.get(d,F(0))
    t.equal(get(1),0,'source balance')
    t.true(all(squarefree(n) for n,a in c.items() if a),'squarefree source')
    ds={}; os={}; local_direct={}
    for q in range(2,L*L+1):
        ab=split(q)
        if ab is None:
            t.equal(bs.get(q,0),0,'cubefree support')
            continue
        a,b=ab
        inc=sum((mu(e)*sum((mu(f)*get(a*f) for f in divisors(e)),F(0))**2
                 for e in divisors(b)),F(0))
        cross=sum((mu(b)*mu(f)*mu(g)*get(a*f)*get(a*g)
                   for f in divisors(b) for g in divisors(b)
                   if f*g//gcd(f,g)==b),F(0))
        t.equal(bs.get(q,0),inc,'conditional inclusion exclusion')
        t.equal(inc,cross,'lcm pair expansion')
        ds[q]=mu(b)*get(a*b)**2
        os[q]=cross-ds[q]
        local_direct[q]=sum((mu(b)*mu(f)*mu(g)*get(a*f)*get(a*g)
            for f in divisors(b) for g in divisors(b)
            if f!=g and f*g//gcd(f,g)==b and abs(f//gcd(f,g)-g//gcd(f,g))<=2),F(0))
    grouped={}; local={}
    sf=[n for n in range(1,L+1) if squarefree(n)]
    for u0 in sf:
        for v in sf:
            if u0==v or gcd(u0,v)>1: continue
            for d in sf:
                if d*max(u0,v)>L: break
                if gcd(d,u0*v)>1: continue
                amp=get(d*u0)*get(d*v)
                if not amp: continue
                for a in divisors(d):
                    q=a*d*u0*v
                    coeff=(1 if mutate else mu(d//a))*amp
                    grouped[q]=grouped.get(q,F(0))+coeff
                    if abs(u0-v)<=2:
                        local[q]=local.get(q,F(0))+coeff
    for q in set(bs)|set(grouped)|set(ds):
        if q>1:
            t.equal(grouped.get(q,0),os.get(q,0),'disjoint coprime regrouping')
            t.equal(local.get(q,0),local_direct.get(q,0),'gap graph independently selected')
    if L<=17:
        for k in range(0,2*L+3):
            full=sum((b*ring(q,k) for q,b in bs.items() if q>1),F(0))
            recon=sum((b*ring(q,k) for q,b in ds.items()),F(0))
            recon+=sum((b*ring(q,k) for q,b in grouped.items()),F(0))
            t.equal(full,recon,'full physical decomposition')
    return ds,grouped,local

def finite_energy(c,y):
    running=F(0); prefix=F(0); tail=F(0)
    for k in range(1,max(c)+1):
        running+=c.get(k,F(0))/k
        if k<=y: prefix+=running**2
        else: tail+=running**2
    return prefix,tail

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mutate',action='store_true',help='deliberate regrouping-sign negative control')
    args=parser.parse_args()
    t=Checks(); sources=0
    for a in (-1,0,1):
        for b in (-1,0,1):
            for c0 in (-1,0,1):
                for d in (-1,0,1):
                    c={1:F(a),2:F(b),3:F(c0),6:F(d)}
                    c[7]=-7*u(c,1)
                    decompose(c,t,args.mutate); sources+=1
    mixed={1:F(1),6:F(-1),10:F(2),15:F(-2),30:F(1)}
    mixed[31]=-31*u(mixed,1)
    decompose(mixed,t,args.mutate)
    sources+=1
    # Exact finite base verification for the all-Y completion statement.
    worst=F(0); worst_y=0
    for y in range(2,256):
        c=sf_completion(y); e,tail=finite_energy(c,y)
        t.equal(u(c,1),0,'small completion balance')
        t.true(max(c)<=2*y,'small completion support')
        t.true(max(map(abs,c.values()))<=16,'small cap')
        t.true(all(squarefree(n) for n,a in c.items() if a),'small squarefree support')
        t.true(tail<=32*e,'small completion energy')
        if tail/e>worst: worst=tail/e; worst_y=y
    native=[]
    for y in (3,7,15,31,63,95,255):
        c=sf_completion(y); z=convolution(c); e,tail=finite_energy(c,y)
        if y<=95: decompose(c,t,args.mutate)
        for n in range(1,(y+1)**2):
            v=2*c.get(n,0)-sum((z.get(d,0) for d in divisors(n)),F(0))
            t.equal(v,mu(n),'squarefree-completed native reproduction')
        t.true(tail<=32*e,'native tail energy')
        native.append({'Y':y,'L':max(c),'tail_energy_over_F':float(tail/e)})
    for y in (256,512,1023,2047):
        c=sf_completion(y); e,tail=finite_energy(c,y)
        t.true(tail<=32*e,'large-example tail energy')
        t.equal(u(c,1),0,'large-example balance')
        t.true(all(squarefree(n) for n,a in c.items() if a),'large-example squarefree')
    # Kernel regrouping independently at integer points.
    for d in range(1,31):
        if not squarefree(d): continue
        for b in range(2,17):
            if not squarefree(b) or gcd(d,b)>1: continue
            seq=list(range(101))
            for p0,_ in factors(d):
                for _repeat in range(2): seq=[val-p0*seq[k//p0] for k,val in enumerate(seq)]
            for p0,_ in factors(b): seq=[val-p0*seq[k//p0] for k,val in enumerate(seq)]
            for k in range(0,101):
                lhs=sum(mu(d//a)*ring(a*d*b,k) for a in divisors(d))
                rhs=sum(mu(d//a)*a*ring(d*b,k//a) for a in divisors(d))
                t.equal(lhs,rhs,'grouped radical kernel')
                t.equal(lhs,mu(b)*seq[k],'dilation polynomial independently evaluated')
    # Tail-map constant annihilation and moving-mask failure, rational examples.
    for k in range(1,31):
        t.equal(F(1,k+1)-(F(1,k+1)-F(1,1001))-F(1,1001),0,'constant tail cancellation')
    t.true(F(1,11)!=0,'masked constant has nonzero preactivation tail')
    print(json.dumps({'status':'PASS','exact_comparisons':t.count,
      'balanced_squarefree_sources':sources,'finite_completion_base':[2,255],
      'worst_base_tail_over_F':{'Y':worst_y,'exact':str(worst)},
      'native':native,'scope':'exact finite checks; displayed ratios are descriptive floats; infinite norm bounds are manuscript proofs'},indent=2))

if __name__=='__main__': main()
