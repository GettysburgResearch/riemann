#!/usr/bin/env python3
"""Bounded exact controls only; does not verify the analytic growth theorem."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent / '2026-09-08-residual-normalization-and-minima' / 'PROOF.md'
PARENT_SHA256 = 'c6085aff0dba9d58b146fdced61bf5f9cb241e2d67893c102248dd0837895a5a'
PARENT_BLOB = 'd5192fab330a92f336b7cb2c1c93ba517754d307'
FILES = {'README.md','PROOF.md','REVIEW.md','SOURCES.json','VALIDATION.md',
         'verify.py','result.json','test_rejections.py','SHA256SUMS'}

def need(x, message):
    if not x:
        raise ValueError(message)

def unique(pairs):
    d = {}
    for k, v in pairs:
        need(k not in d, 'duplicate JSON key')
        d[k] = v
    return d

def load(path):
    return json.loads(path.read_text(), object_pairs_hook=unique)

def strict_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(strict_equal(x, y) for x,y in zip(a,b))
    return a == b

def inventory():
    need({p.name for p in ROOT.iterdir()} == FILES, 'exact inventory')
    need(all(p.is_file() and not p.is_symlink() for p in ROOT.iterdir()), 'file type')
    lines = (ROOT/'SHA256SUMS').read_text().splitlines()
    parsed = {}
    for line in lines:
        h, n = line.split('  ')
        need(n not in parsed and n in FILES-{'SHA256SUMS'}, 'manifest paths')
        need(len(h)==64 and all(c in '0123456789abcdef' for c in h), 'manifest hash')
        parsed[n] = h
    need(set(parsed)==FILES-{'SHA256SUMS'}, 'manifest coverage')
    for n,h in parsed.items():
        need(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h, 'hash: '+n)
    need(PARENT.is_file() and not PARENT.is_symlink(), 'parent missing or symlink')
    data = PARENT.read_bytes()
    need(hashlib.sha256(data).hexdigest()==PARENT_SHA256, 'parent SHA256')
    need(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==PARENT_BLOB,
         'parent Git blob')
    source = load(ROOT/'SOURCES.json')
    need(source['parent']['commit']=='6c86b5fbfe92c97ecccf17b81585744ccde33b10', 'parent ref')
    need(source['parent']['blob']==PARENT_BLOB, 'source blob')

# Exact multivariate polynomials in the symbols log(prime).
# Monomials are sorted tuples of prime integers; coefficients are Fractions.
def poly(x=0):
    return {} if x==0 else {(): F(x)}
def plus(a,b):
    r=a.copy()
    for k,v in b.items():
        r[k]=r.get(k,F(0))+v
        if not r[k]: del r[k]
    return r

def scale(a,b): return {k:v*F(b) for k,v in a.items() if v*F(b)}
def times(a,b):
    r={}
    for k,v in a.items():
        for l,w in b.items():
            key=tuple(sorted(k+l)); r[key]=r.get(key,F(0))+v*w
    return {k:v for k,v in r.items() if v}
def minus(a,b): return plus(a,scale(b,-1))
def lpoly(n):
    r={}; p=2
    while p*p<=n:
        c=0
        while n%p==0: n//=p; c+=1
        if c: r[(p,)]=F(c)
        p+=1
    if n>1: r[(n,)]=F(1)
    return r

def sieve(n):
    mu=[1]*(n+1); mu[0]=0
    prime=[True]*(n+1)
    for p in range(2,n+1):
        if prime[p]:
            for j in range(p,n+1,p): mu[j]=-mu[j]; prime[j]=False
            for j in range(p*p,n+1,p*p): mu[j]=0
    return mu

def trial_mu(n):
    v=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; v=-v
            if n%p==0: return 0
        p+=1
    return -v if n>1 else v

# Outward rational intervals. Exact primitives, no binary floating point.
def iv(x): return (F(x),F(x))
def ia(a,b): return a[0]+b[0], a[1]+b[1]
def ine(a): return -a[1],-a[0]
def im(a,b):
    v=[x*y for x in a for y in b]; return min(v),max(v)
def isc(a,s): return im(a,iv(s))
def idiv(a,b):
    need(not b[0]<=0<=b[1], 'interval division zero')
    return im(a,(1/b[1],1/b[0]))
def sq(a):
    return (F(0) if a[0]<=0<=a[1] else min(a[0]*a[0],a[1]*a[1]),
            max(a[0]*a[0],a[1]*a[1]))
def log_ratio(n,d=1):
    need(n>=d and d>0, 'log domain')
    z=F(n-d,n+d); T=100
    s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(T)),F(0))
    rem=2*z**(2*T+1)/(F(2*T+1)*(1-z*z)) if z else F(0)
    return s,s+rem
LOG2=log_ratio(2)
def logint(n):
    k=n.bit_length()-1
    return ia(isc(LOG2,k),log_ratio(n,1<<k))
def evalpoly(p):
    z=iv(0)
    for mon,c in p.items():
        term=iv(c)
        for prime in mon: term=im(term,logint(prime))
        z=ia(z,term)
    return z

def endpoint(Y,mu):
    # Store C_n=(log2)*a_n, keeping the normalization tests polynomial.
    ell=lpoly(2); M=sum((F(mu[n],n) for n in range(1,Y)),F(0))
    Fy={}
    for n in range(1,Y): Fy=plus(Fy,scale(minus(lpoly(Y),lpoly(n)),F(mu[n],n)))
    U=minus(Fy,poly(1))
    C={n:scale(ell,mu[n]) for n in range(1,Y) if mu[n]}
    C[Y]=scale(minus(scale(ell,-M),U),Y)
    C[2*Y]=scale(U,2*Y)
    return C,M,Fy

def encode(a):
    S=1<<112
    lo=(a[0].numerator*S)//a[0].denominator
    hi=-((-a[1].numerator*S)//a[1].denominator)
    return [[lo,S],[hi,S]]

def periodic_energy(Y,mu,Q):
    C,_,_=endpoint(Y,mu)
    a={n:idiv(evalpoly(p),LOG2) for n,p in C.items()}
    K=4096; scale2=1<<112
    lower=F(0); upper=F(0)
    for r in range(1,Q+1):
        u=iv(1)
        for n,c in a.items(): u=ia(u,isc(c,-(r//n)))
        uu=sq(u); lo=0; hi=0
        for k in range(K):
            x=r+k*Q; den=x*(x+1)
            lo+=scale2//den; hi+=(scale2+den-1)//den
        tailden=Q*(r+Q*(K-1))
        hi+=(scale2+tailden-1)//tailden
        lower+=uu[0]*F(lo,scale2); upper+=uu[1]*F(hi,scale2)
    return lower,upper

def reconstruct():
    groups={}; mu=sieve(128)
    for n in range(1,129): need(mu[n]==trial_mu(n),'Mobius trial comparison')
    groups['independent_mobius']=128
    Ys=[2,3,4,5,8,12,16,24,32]; horizon=0
    for Y in Ys:
        C,M,Fy=endpoint(Y,mu); ell=lpoly(2)
        balance={}; deriv={}; exactS={}
        for n,v in C.items():
            balance=plus(balance,scale(v,F(1,n)))
            deriv=plus(deriv,scale(times(v,lpoly(n)),F(1,n)))
            exactS=plus(exactS,scale(times(v,v),F(1,n)))
        need(not balance, 'formal balance')
        need(deriv==scale(ell,-1),'formal derivative jet')
        U=minus(Fy,poly(1)); A=minus(scale(ell,-M),U)
        predicted=plus(scale(times(ell,ell),sum((F(mu[n]**2,n) for n in range(1,Y)),F(0))),
                       scale(plus(times(A,A),scale(times(U,U),2)),Y))
        need(exactS==predicted, 'coefficient norm identity')
        for j in range(1,Y):
            value={}
            for n,v in C.items(): value=plus(value,scale(v,j//n))
            need(value==ell,'exact prefix horizon'); horizon+=1
        need(abs(M)<=1, 'harmonic prefix')
        fi=evalpoly(minus(Fy,poly(1)))
        need(-2<fi[0] and fi[1]<2, 'finite harmonic log bound')
        ai={n:idiv(evalpoly(v),LOG2) for n,v in C.items()}
        mass=F(1)
        energy_diag=iv(0)
        for n,v in ai.items():
            mass+=max(abs(v[0]),abs(v[1])); energy_diag=ia(energy_diag,isc(sq(v),F(1,n)))
        need(mass<14*Y, 'elementary complete residual bound')
        need(energy_diag[1]<60*Y, 'elementary diagonal bound')
    groups['formal_two_jets_and_norm']=3*len(Ys)
    groups['exact_floor_horizon']=horizon
    groups['bounded_endpoint_enclosures']=4*len(Ys)
    # These rational cases check inequalities in the proof's exponent choices;
    # they do not check a zero-free half-plane or a limiting theorem.
    count=0
    for theta,q in [(F(1,2),F(3,5)),(F(7,10),F(4,5)),(F(9,10),F(19,20))]:
        sigma=(theta+q)/2
        for B in [1,4,8]:
            eta=(q-sigma)/(4*(B+4))
            need(sigma-F(1,2)+(B+4)*eta<q-F(1,2),'Perron exponent')
            need(F(1,2)-(B+4)*(1-eta)<q-F(1,2),'horizontal exponent')
            count+=2
    need(1+4*(-F(3,8))==-F(1,2),'full tail exponent')
    need(2+4*(-F(11,8))==-F(7,2),'tail offdiagonal exponent')
    groups['strict_strip_and_tail_budgets']=count+2
    # Exact two-point Hardy norm identity for rational synthetic complex nodes.
    count=0
    for beta in [F(3,5),F(3,4),F(9,10)]:
        for gamma in [F(1),F(2),F(7,3)]:
            c=beta-F(1,2); rho2=beta*beta+gamma*gamma
            comp=1/(2*c)-1/rho2
            rhs=((beta-1)**2+gamma*gamma)/(2*c*rho2)
            need(comp==rhs and rhs>0,'synthetic kernel residual'); count+=1
    groups['synthetic_hardy_identity']=count
    norms={}
    for Y,Q,lo,hi in [(2,4,F(189,1000),F(191,1000)),(4,24,F(57,1000),F(59,1000))]:
        z=periodic_energy(Y,mu,Q)
        need(lo<z[0] and z[1]<hi,'full periodic energy enclosure')
        norms[str(Y)]={'period':Q,'terms_per_weight':4096,'energy_interval':encode(z)}
    groups['small_complete_energy_replays']=2
    return {'status':'PROPOSED_COMPONENT_PROOFS', 'rh_proved':False,
            'zero_edge_evaluated':False,'new_minimum_certificate':False,
            'parent_commit':'6c86b5fbfe92c97ecccf17b81585744ccde33b10',
            'groups':groups,'total_bounded_checks':sum(groups.values()),
            'endpoint_prefixes':Ys,'small_norms':norms,
            'analytic_limit_verified_by_code':False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true')
    ap.add_argument('--check',default='result.json'); args=ap.parse_args()
    if args.write:
        (ROOT/'result.json').write_text(json.dumps(reconstruct(),sort_keys=True,indent=2)+'\n')
        print('WROTE bounded controls; no analytic theorem or RH checked')
    else:
        inventory(); got=reconstruct(); wanted=load(ROOT/args.check)
        need(strict_equal(got,wanted),'reconstructed result differs')
        print(json.dumps(got,sort_keys=True,indent=2))
if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,OSError,TypeError,ZeroDivisionError) as exc:
        raise SystemExit('REFUSE: '+str(exc))
