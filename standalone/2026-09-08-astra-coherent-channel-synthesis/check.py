#!/usr/bin/env python3
"""Bounded primitive replay. No numerical experiment establishes an infinite claim."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
INVENTORY = {'README.md','PROOF.md','COHERENT_SOURCE.md','SYNTHESIS.md',
             'SOURCE_LOCK.json','VALIDATION.md','check.py','test_check.py',
             'verification.json','SHA256SUMS'}
BASE = 'f99d9e3908dde4865377c75d9ca051c1f545bf4f'
PR825 = 'e4a486d3fd4009e3722e9e93f35710b834fbd195'
PR826 = '3a82b80da82edbcd65d4538418a3d51d6030f058'
PRIMES = (2,3,5,7,11,13,17,19)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def no_duplicates(pairs):
    out = {}
    for k,v in pairs:
        require(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def clean_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=no_duplicates,
                      parse_float=lambda _: (_ for _ in ()).throw(ValueError('float rejected')),
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('constant rejected')))


def rat(x: F):
    return [x.numerator, x.denominator]


def enclosure(lo: F, hi: F, places: int = 12):
    d = 10**places
    return [[lo.numerator*d//lo.denominator,d],
            [-((-hi.numerator*d)//hi.denominator),d]]


def log_unit(x: F, terms: int = 64):
    require(F(1) <= x <= 2, 'log reduction domain')
    z = (x-1)/(x+1)
    total = sum((2*z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    rem = 2*z**(2*terms+1)/F(2*terms+1)/(1-z*z)
    return total, total+rem


@lru_cache(None)
def log_bounds(n: int):
    require(type(n) is int and n >= 1, 'bad log input')
    m = n.bit_length()-1
    u = F(n, 1 << m)
    l2, u2 = log_unit(F(2))
    a,b = log_unit(u)
    a += m*l2; b += m*u2
    d = 1 << 160
    return F(a.numerator*d//a.denominator,d), F(-((-b.numerator*d)//b.denominator),d)


def factor(n: int):
    require(n>=1,'bad factor input')
    out=[]; p=2
    while p*p<=n:
        k=0
        while n%p==0:
            n//=p; k+=1
        if k: out.append((p,k))
        p+=1
    if n>1:out.append((n,1))
    return out


def mobius_trial(n: int):
    fac=factor(n)
    return 0 if any(k>1 for _,k in fac) else (-1)**len(fac)


def mobius_sieve(limit: int):
    mu=[1]*(limit+1); prime=[True]*(limit+1)
    for p in range(2,limit+1):
        if prime[p]:
            for n in range(p,limit+1,p):
                prime[n]=False; mu[n]*=-1
            for n in range(p*p,limit+1,p*p):mu[n]=0
    mu[0]=0
    return mu


def cube(primes):
    nodes=[]
    for mask in range(1<<len(primes)):
        n=1
        for i,p in enumerate(primes):
            if mask>>i&1:n*=p
        nodes.append(n)
    return nodes


def eta(mask: int, eigenmask: int, primes):
    y=F(1)
    for i,p in enumerate(primes):
        if eigenmask>>i&1:y*=F(1) if mask>>i&1 else F(-1,p)
    return y


def apply_generator(values, primes, weights):
    out=[F(0)]*len(values)
    for mask in range(len(values)):
        for i,p in enumerate(primes):
            if mask>>i&1:
                rate=weights[i]; other=mask^(1<<i)
            else:
                rate=weights[i]/p; other=mask|(1<<i)
            out[mask]+=rate*(values[mask]-values[other])
    return out


def cube_checks():
    rows=[]
    for r in range(1,5):
        ps=PRIMES[:r]; nodes=cube(ps); z=sum((F(1,n) for n in nodes),F(0))
        pi=[F(1,n)/z for n in nodes]
        functions=[[eta(m,f,ps) for m in range(len(nodes))] for f in range(len(nodes))]
        for f,fn in enumerate(functions):
            for g,gn in enumerate(functions):
                ip=sum((w*x*y for w,x,y in zip(pi,fn,gn)),F(0))
                require(ip==(F(1,nodes[f]) if f==g else F(0)), 'cube orthogonality')
            for i in range(r):
                ws=[F(0)]*r; ws[i]=F(1)
                out=apply_generator(fn,ps,ws)
                eigen=F(ps[i]+1,ps[i]) if f>>i&1 else F(0)
                require(out==[eigen*x for x in fn], 'coefficientwise eigenvalue')
        # Positive rational rates are a SYNTHETIC algebraic panel, not logarithms.
        ws=[F(p) for p in ps]
        lam=[sum((ws[i]*F(p+1,p) for i,p in enumerate(ps) if f>>i&1),F(0))
             for f in range(len(nodes))]
        u=[sum((F((-1)**f.bit_count(),1)/lam[f]*functions[f][m]
                for f in range(1,len(nodes))),F(0)) for m in range(len(nodes))]
        b=[z-1]+[F(-1)]*(len(nodes)-1)
        require(apply_generator(u,ps,ws)==b,'root Poisson equation')
        K=sum((F(1,nodes[f])/lam[f] for f in range(1,len(nodes))),F(0))
        K2=sum((F(1,nodes[f])/lam[f]**2 for f in range(1,len(nodes))),F(0))
        require(u[0]==K,'root Green value')
        require(sum((w*x for w,x in zip(pi,u)),F(0))==0,'Green mean')
        require(sum((w*x*x for w,x in zip(pi,u)),F(0))==K2,'Green norm')
        require(sum((w*x*y for w,x,y in zip(pi,u,b)),F(0))==K,'Green energy')
        rows.append({'prime_count':r,'vertices':len(nodes),'synthetic_K':rat(K),'synthetic_K2':rat(K2)})
    return rows


def directed_sum(values, upper=False):
    scale=1<<160; total=0
    for value in values:
        a=value.numerator*scale; b=value.denominator
        total += -((-a)//b) if upper else a//b
    return F(total,scale)


def root_certificate(primes):
    nodes=cube(primes); modes=[]
    for mask,n in enumerate(nodes):
        if not mask:continue
        low=high=F(0)
        for i,p in enumerate(primes):
            if mask>>i&1:
                lo,hi=log_bounds(p); low+=F(p+1,p)*lo; high+=F(p+1,p)*hi
        modes.append((n,low,high))
    nu0=F(3,2)*log_bounds(2)[0]
    nu1=F(3,2)*log_bounds(2)[1]
    Klo=directed_sum((F(1,n)/hi for n,lo,hi in modes))
    Khi=directed_sum((F(1,n)/lo for n,lo,hi in modes),True)
    def secular(A):
        require(all(A*lo>1 for _,lo,_ in modes),'secular pole crossing')
        lower=directed_sum((F(1,n)/(A*hi-1) for n,lo,hi in modes))
        upper=directed_sum((F(1,n)/(A*lo-1) for n,lo,hi in modes),True)
        return lower,upper
    a=1/nu0+F(1,1000); bound=Khi+1/nu0; b=F(bound.numerator//bound.denominator+2)
    require(secular(a)[0]>1 and secular(b)[1]<1,'initial root bracket')
    for _ in range(44):
        mid=(a+b)/2; lo,hi=secular(mid)
        if lo>1:a=mid
        elif hi<1:b=mid
        else:break
    require(b-a<F(1,10**10),'root bracket too wide')
    al,au=enclosure(a,b)
    require(secular(F(*al))[0]>1 and secular(F(*au))[1]<1,'rounded root bracket')
    require(b>=Klo and a<=Khi+1/nu0,'root comparison')
    return {'primes':list(primes),'vertices':len(nodes),'K':enclosure(Klo,Khi),
            'optimal_anchored_constant':[al,au],'centered_constant':enclosure(1/nu1,1/nu0)}


def native_checks(mu):
    rows=[]
    choices=(1,2,3,4,5,6,8,12,16,24,32,64,128)
    M=[0]
    for x in mu[1:]:M.append(M[-1]+x)
    previous=F(0)
    for N in range(1,129):
        energy=sum((F(M[k]**2,k*(k+1)) for k in range(1,N)),F(0))+F(M[N]**2,N)
        require(energy-previous==F(2*mu[N]*M[N-1]+mu[N]**2,N),'work recurrence')
        previous=energy
        if N not in choices:continue
        pairs=sum((F(mu[m]*mu[n],max(m,n)) for m in range(1,N+1) for n in range(1,N+1)),F(0))
        require(pairs==energy,'full pair kernel')
        H=sum((F(1,n) for n in range(1,N+1)),F(0)); sf=sum(x*x for x in mu[1:N+1])
        require(0<=energy/H<=sf,'coherent projection')
        # Coefficients of each formal log(p), computed two independent ways.
        direct={}; formula={}
        edges=0; higher=0
        for p in range(2,N+1):
            if factor(p)!=[(p,1)]:continue
            q=p; coefficient=F(0)
            while q<=N:
                for j in range(1,N//q+1):
                    n=q*j; coefficient+=mu[n]**2+F(mu[j]**2-2*mu[n]*mu[j],q)
                    edges+=1; higher+=int(q!=p)
                q*=p
            direct[p]=coefficient
            incoming=sum(F(mu[n]**2*dict(factor(n)).get(p,0)) for n in range(1,N+1))
            outgoing=F(0); q=p
            while q<=N:
                outgoing+=sum((F(mu[j]**2,q) for j in range(1,N//q+1)),F(0)); q*=p
            cross=F(2,p)*sum(mu[j]**2 for j in range(1,N//p+1) if j%p)
            formula[p]=incoming+outgoing+cross
        require(direct==formula,'complete prime-power edge formula')
        tail=F(M[N]**2,N)
        rows.append({'N':N,'J':rat(energy),'future_tail':rat(tail),'coherent_squared_norm':rat(energy/H),
                     'vertex_squared_norm':sf,'edges':edges,'higher_power_edges':higher})
    return rows


def reconstruct():
    mu=mobius_sieve(256)
    require(all(mu[n]==mobius_trial(n) for n in range(1,257)),'primitive Mobius mismatch')
    for n in range(1,257):
        require(sum(mu[d] for d in range(1,n+1) if n%d==0)==int(n==1),'divisor inversion')
        require(mu[n]**2==sum(mu[d] for d in range(1,n+1) if n%(d*d)==0),'squarefree expansion')
    return {'format':'CCS26-v1','status':'component-proofs; RH estimate OPEN',
            'rh_proved':False,'primitive_range':256,
            'cube_algebra':cube_checks(),
            'literal_root_certificates':[root_certificate(PRIMES[:r]) for r in (1,2,3,4,6,8)],
            'native_coherent_panels':native_checks(mu),
            'scope':{'infinite_theorems_machine_proved':False,'actual_zero_data_used':False,
                     'literal_prime_power_formula_checked':True,'broad_campaign':False}}


def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b


def authenticate():
    actual={p.name for p in ROOT.iterdir()}
    require(actual==INVENTORY,'inventory mismatch')
    require(all((ROOT/name).is_file() and not (ROOT/name).is_symlink() for name in INVENTORY),'nonregular input')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ')
        require(name not in entries and name in INVENTORY and name!='SHA256SUMS','bad manifest member')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'bad digest')
        entries[name]=digest
    require(set(entries)==INVENTORY-{'SHA256SUMS'},'manifest coverage')
    for name,digest in entries.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'hash mismatch: '+name)
    lock=clean_json(ROOT/'SOURCE_LOCK.json')
    require(lock['base_main']==BASE and lock['pr825']==PR825 and lock['pr826']==PR826,'source lock mismatch')


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--emit',action='store_true'); args=parser.parse_args()
    if args.emit:
        print(json.dumps(reconstruct(),indent=2,sort_keys=True)); return
    authenticate(); expected=reconstruct(); supplied=clean_json(ROOT/'verification.json')
    require(same(expected,supplied),'primitive replay differs from retained result')
    data=json.dumps(expected,sort_keys=True,separators=(',',':')).encode()
    print(json.dumps({'status':'PASS_CCS26_BOUNDED_REPLAY','sha256':hashlib.sha256(data).hexdigest(),
                      'native_panels':len(expected['native_coherent_panels']),
                      'root_certificates':len(expected['literal_root_certificates']),
                      'rh_proved':False},sort_keys=True))

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError,TypeError,ZeroDivisionError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);sys.exit(1)
