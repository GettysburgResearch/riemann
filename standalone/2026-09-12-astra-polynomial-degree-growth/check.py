#!/usr/bin/env python3
"""DG26 finite arithmetic/interval reconstruction; not an RH proof.

Integer/Fraction acceptance. The interval design and Machin/Bernoulli versus
Euler--Maclaurin comparison are adapted from the pinned AC28 checker. No
repository or third-party module is imported. Floating reconnaissance only
selected the integer Rayleigh probes embedded below.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BITS=768
SCALE=1<<BITS
RECEIPT_BITS=160
RSCALE=1<<RECEIPT_BITS
MAXN=32
SIZES=(1,2,4,8,16,32)
FILES={'README.md','PROOF.md','ATTEMPT.md','LATEST_WORK.tsv','SOURCES.json',
       'VALIDATION.md','check.py','results.json'}
PARENT='59384bcdea88bdedb86c503479c6c26c681daf5e'
WITNESSES={
1:[173205081],2:[151192988,-129079772],
4:[-142120469,121693953,-93126426,73812022],
8:[-138138008,118399707,-90613378,71797701,-62652217,58346401,-54595829,50281386],
16:[-136219460,116807167,-89396216,70827155,-61809295,57556136,-53850180,49601883,-45629430,42540167,-40169435,38359837,-37379449,37323987,-37501809,36818530],
32:[-135277376,116022604,-88799430,70352742,-61389820,57168375,-53490015,49267781,-45320527,42253758,-39900969,38103300,-37126291,37066812,-37242403,36569356,-34564016,31786698,-29269343,27657886,-26958945,26902856,-27274214,27857863,-28298900,28245061,-27639209,26752103,-25883321,25102433,-24327661,23574769]}

def need(ok,msg):
    if not ok: raise ValueError(msg)

def down(x):
    x=F(x);return F((x.numerator*SCALE)//x.denominator,SCALE)
def up(x):return -down(-F(x))
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        lo=F(lo);hi=lo if hi is None else F(hi)
        need(lo<=hi,'inverted interval');self.lo,self.hi=down(lo),up(hi)
    def __add__(self,o):
        o=iv(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o);need(o.lo*o.hi>0,'division across zero');return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return iv(o)/self
    def __pow__(self,n):
        need(type(n) is int and n>=0,'invalid power');r=I(1);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def pair(self):
        lo=(self.lo.numerator*RSCALE)//self.lo.denominator
        hi=-((-self.hi.numerator*RSCALE)//self.hi.denominator)
        return [lo,hi]
def iv(x):return x if isinstance(x,I) else I(x)
def overlap(a,b):return max(a.lo,b.lo)<=min(a.hi,b.hi)
def intersection(a,b):
    need(overlap(a,b),'disjoint primitive enclosures');return I(max(a.lo,b.lo),min(a.hi,b.hi))
def encf(x):
    x=F(x);return [x.numerator,x.denominator]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(x):return sha256(canonical(x)).hexdigest()
def bernoulli(n):
    b=[F(1)]
    for j in range(1,n+1):b.append(-sum(F(comb(j+1,k))*b[k] for k in range(j))/F(j+1))
    return b

def atan(q,n):
    s=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F())
    t=s+F((-1)**n,(2*n+1)*q**(2*n+1))
    return I(min(s,t),max(s,t))
def pi_interval():return 16*atan(5,220)-4*atan(239,80)
def zeven(k,pi,b):
    s=2*k;factor=(1-F(1,2**s))*(-1)**(k+1)*b[s]*F(2**(s-1),factorial(s))
    return factor*pi**s

def em(k,b,N=128,K=64):
    s=2*k;v=sum((F(1,n**s) for n in range(1,N)),F())+F(1,(s-1)*N**(s-1))+F(1,2*N**s)
    rising=1;last=F()
    for j in range(1,K+1):
        rising=1
        for h in range(2*j-1):rising*=s+h
        last=b[2*j]*F(rising,factorial(2*j)*N**(s+2*j-1));v+=last
    # Full periodic-Bernoulli remainder, not a fitted asymptotic error.
    return (1-F(1,2**s))*I(v-abs(last),v+abs(last))

@lru_cache(None)
def legendre(l):
    if l==0:return (F(1),)
    if l==1:return (F(),F(1))
    a=list(legendre(l-1));b=list(legendre(l-2));c=[F()]*(l+1)
    for i,x in enumerate(a):c[i+1]+=F(2*l-1,l)*x
    for i,x in enumerate(b):c[i]-=F(l-1,l)*x
    return tuple(c)
def rodrigues(l):
    c=[F()]*(l+1)
    for k in range(l//2+1):
        c[l-2*k]=F((-1)**k*factorial(2*l-2*k),2**l*factorial(k)*factorial(l-k)*factorial(l-2*k))
    return tuple(c)
def inner(p,q,lo=0,hi=1):
    return sum((a*b*F(hi**(i+j+1)-lo**(i+j+1),i+j+1)
                for i,a in enumerate(p) if a for j,b in enumerate(q) if b),F())
def product_mellin(j,s):
    val=F(1)/(s+1)
    for k in range(1,j+1):val*= (s-2*k)/(s+2*k+1)
    return val

def mu_trial(n):
    v=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;v=-v
            if n%p==0:return 0
        p+=1
    return -v if n>1 else v

def mu_sieve(n):
    mu=[1]*(n+1);mu[0]=0;seen=[False]*(n+1)
    for p in range(2,n+1):
        if not seen[p]:
            for k in range(p,n+1,p):seen[k]=True;mu[k]=-mu[k]
            for k in range(p*p,n+1,p*p):mu[k]=0
    return mu

def ldl(a):
    n=len(a);L=[[I(0) for _ in range(n)] for _ in range(n)];piv=[]
    for i in range(n):
        d=a[i][i]-sum((L[i][k]*L[i][k]*piv[k] for k in range(i)),I(0))
        need(d.lo>0,'uncertified positive pivot');piv.append(d);L[i][i]=I(1)
        for j in range(i+1,n):
            L[j][i]=(a[j][i]-sum((L[j][k]*L[i][k]*piv[k] for k in range(i)),I(0)))/d
    return [p.pair() for p in piv]

def mono_gram(z):
    n=len(z);hs=[1/x-1 for x in z];r=[2*j+1 for j in range(n)]
    J=lambda a:F(3**(a+1)-1,a+1)
    return [[(2+hs[i]*J(r[i])+hs[j]*J(r[j])+hs[i]*hs[j]*J(r[i]+r[j]))/(r[i]*r[j])
             for j in range(n)] for i in range(n)]

def leg_gram(z):
    n=len(z);M=mono_gram(z);c=[[legendre(2*i+1)[2*j+1] if j<=i else F() for j in range(n)] for i in range(n)]
    T=[[sum((c[i][k]*M[k][j] for k in range(i+1)),I(0)) for j in range(n)] for i in range(n)]
    return [[sum((T[i][k]*c[j][k] for k in range(j+1)),I(0)) for j in range(n)] for i in range(n)]

def output_poly(l,z):
    c=rodrigues(l);out={0:I(0)}
    for r,a in enumerate(c):
        if a:
            out[0]+=a/F(r);out[r]=(a/F(r))*(1/z[(r-1)//2]-1)
    return out

@lru_cache(None)
def raw_payload():
    b=bernoulli(128);pi=pi_interval();need(3<pi.lo<pi.hi<F(22,7),'pi range')
    z1=[zeven(k,pi,b) for k in range(1,MAXN+1)]
    z2=[em(k,b) for k in range(1,MAXN+1)]
    z=[intersection(a,b) for a,b in zip(z1,z2)]
    for x in z:need(1<x.lo<x.hi<F(5,4),'odd even zeta range')
    for l in range(64):need(legendre(l)==rodrigues(l),'Legendre generator mismatch')
    orth=0
    for i in range(MAXN):
        for j in range(i+1):
            need(inner(legendre(2*i+1),legendre(2*j+1))==(F(1,4*i+3) if i==j else 0),'orthogonality');orth+=1
    mell=[]
    for j in range(32):
        for s in [F(1,3),F(1,2),F(3,4),F(1),F(3,2),F(2),F(7,2),F(10)]:
            a=sum((c/(s+k) for k,c in enumerate(legendre(2*j+1)) if c),F())
            need(a==product_mellin(j,s),'Mellin rational product')
            mell.append([j,encf(s),encf(a)])
    mu=mu_sieve(2048)
    for n in range(1,2049):need(mu[n]==mu_trial(n),'primitive Mobius mismatch')
    inv=[]
    for k in range(1,17):
        s=2*k;total=sum((F(mu[n],n**s) for n in range(1,2049,2)),F())
        tail=F(1,(s-1)*2048**(s-1))
        source=I(total-tail,total+tail)
        need(overlap(source,1/z[k-1]),'complete reciprocal Mobius tail')
        inv.append({'k':k,'partial_interval':I(total).pair(),'whole_tail':encf(tail),'reciprocal':(1/z[k-1]).pair()})
    G=leg_gram(z)
    direct=[]
    for i in range(8):
        p=output_poly(2*i+1,z2)
        for j in range(i+1):
            q=output_poly(2*j+1,z2)
            v=sum((a*b*F(3**(r+s+1)-1,r+s+1) for r,a in p.items() for s,b in q.items()),I(0))
            need(overlap(v,G[i][j]),'direct whole-output Gram mismatch');direct.append([i,j,v.pair()])
    bounds=[]
    for n in SIZES:
        tr=sum(((4*j+3)*G[j][j] for j in range(n)),I(0))
        need(tr.hi<4 and tr.lo>0,'finite trace ceiling 4 not proved')
        w=WITNESSES[n];den=sum((F(w[j]**2,4*j+3) for j in range(n)),F())
        q=sum((w[i]*w[j]*G[i][j] for i in range(n) for j in range(n)),I(0))/den
        need(q.lo>2 and q.lo<=tr.hi and q.hi<4,'Rayleigh bounds')
        C=[[4*F(i==j,4*i+3)-G[i][j] for j in range(n)] for i in range(n)]
        piv=ldl(C)
        bounds.append({'N':n,'degree':2*n-1,'trace':tr.pair(),'rayleigh':q.pair(),'integer_probe':w,
                       'input_norm_squared':encf(den),'upper':4,'upper_ldl':piv})
    # Algebraic exponents in the all-degree lower bound; beta values are
    # synthetic proof parameters, never asserted zeros of zeta.
    expo=[]
    for beta in [F(3,5),F(2,3),F(3,4),F(4,5),F(9,10),F(99,100)]:
        delta=beta-F(1,2)
        bern=(3-beta)/10-F(1,4)
        need(bern==-delta/10,'quantitative degree balance')
        need(delta/5==(2*beta-1)/10,'squared norm exponent')
        expo.append([encf(beta),encf(bern),encf(delta/5)])
    # Full odd Bernstein-primitive identity for polynomial derivatives;
    # direct binomial summation is separate from monomial expectation.
    bern=[]
    for M in [4,8,16,32]:
        for k in range(4):
            for x in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
                v=sum((F(j,M)**k*comb(M,j)*x**j*(1-x)**(M-j) for j in range(M+1)),F())
                # Direct finite probability normalization and moment bound.
                mass=sum((comb(M,j)*x**j*(1-x)**(M-j) for j in range(M+1)),F())
                var=sum(((F(j,M)-x)**2*comb(M,j)*x**j*(1-x)**(M-j) for j in range(M+1)),F())
                need(mass==1 and var==x*(1-x)/M,'Bernstein primitive moments')
                need(abs(v-x**k)**4<=F(max(1,k)**4,4*M),'Holder/Jensen bound')
                bern.append([M,k,encf(x),encf(v),encf(var)])
    return {'schema':'DG26-polynomial-degree-growth/v1','source_head':PARENT,'status':'PROPOSED component theorems; subpower growth OPEN',
      'rh_proved':False,'full_growth_bound_proved':False,'bits':BITS,'receipt_bits':RECEIPT_BITS,'finite_degree_cap':63,
      'pi':pi.pair(),'even_zeta_pi':[v.pair() for v in z1],'even_zeta_EM':[v.pair() for v in z2],
      'orthogonal_pairs':orth,'mellin_coefficients':mell,'mobius_compared':2048,'reciprocal_checks':inv,
      'direct_gram_checks':direct,'finite_norm_bounds':bounds,'degree_exponents_not_zero_data':expo,
      'bernstein_controls':bern,'scope':'Six finite all-vector bounds. No arbitrary-degree upper bound or numerical zeta-zero input.'}

def payload():
    r=raw_payload()
    groups=['even_zeta_pi','even_zeta_EM','mellin_coefficients','reciprocal_checks',
            'direct_gram_checks','degree_exponents_not_zero_data','bernstein_controls']
    out={k:r[k] for k in ['schema','source_head','status','rh_proved','full_growth_bound_proved',
                         'bits','receipt_bits','finite_degree_cap','orthogonal_pairs','mobius_compared','scope']}
    out['pi']=r['pi']
    out['complete_payload_sha256']=digest(r)
    out['groups']={k:{'count':len(r[k]),'sha256':digest(r[k])} for k in groups}
    out['finite_norm_bounds']=[]
    for b in r['finite_norm_bounds']:
        v={k:b[k] for k in ['N','degree','trace','rayleigh','input_norm_squared','upper']}
        v['pivot_count']=len(b['upper_ldl']);v['pivots_sha256']=digest(b['upper_ldl'])
        v['probe_sha256']=digest(b['integer_probe']);out['finite_norm_bounds'].append(v)
    return out

def sealed(p):return {'payload':p,'sha256':digest(p)}
def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b

def accept(report,expected):
    need(type(report) is dict and set(report)=={'payload','sha256'},'envelope')
    need(report['sha256']==digest(report['payload']),'digest')
    need(same(report['payload'],expected),'primitive reconstruction mismatch')
def fail(_):raise ValueError('noninteger JSON forbidden')
def unique(items):
    out={}
    for k,v in items:need(k not in out,'duplicate key');out[k]=v
    return out

def read(path):return json.loads(path.read_text(),parse_float=fail,parse_constant=fail,object_pairs_hook=unique)
def self_test(p):
    accept(sealed(p),p)
    edits=[lambda q:q.update(rh_proved=True),lambda q:q.update(full_growth_bound_proved=True),
      lambda q:q.update(source_head='0'*40),lambda q:q.update(bits=256),
      lambda q:q['finite_norm_bounds'].pop(),lambda q:q['finite_norm_bounds'][0].update(upper=3),
      lambda q:q['finite_norm_bounds'][-1].update(probe_sha256='0'*64),
      lambda q:q['groups']['even_zeta_pi'].update(sha256='0'*64),
      lambda q:q.update(orthogonal_pairs=True),lambda q:q.update(finite_degree_cap=127),
      lambda q:q['groups']['degree_exponents_not_zero_data'].update(count=0),
      lambda q:q['groups']['reciprocal_checks'].update(sha256='0'*64)]
    for edit in edits:
        bad=deepcopy(p);edit(bad);need(not same(p,bad),'no-op mutation')
        try:accept(sealed(bad),p)
        except ValueError:pass
        else:raise ValueError('resealed corruption accepted')
    try:json.loads('{"x":1,"x":2}',object_pairs_hook=unique)
    except ValueError:pass
    else:raise ValueError('duplicate JSON accepted')
    return len(edits)

def manifest():
    got={}
    for line in (ROOT/'MANIFEST.sha256').read_text().splitlines():
        h,p=line.split('  ',1);need(p in FILES and p not in got,'manifest coverage')
        f=ROOT/p;need(f.is_file() and not f.is_symlink(),'regular file')
        need(sha256(f.read_bytes()).hexdigest()==h,'file hash '+p);got[p]=h
    need(set(got)==FILES,'manifest omissions')
    need({p.name for p in ROOT.iterdir()}==FILES|{'MANIFEST.sha256'},'unexpected file')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path);ap.add_argument('--self-test',action='store_true');ap.add_argument('--detail',type=Path);a=ap.parse_args()
    need(bool(a.write)^bool(a.check),'choose write xor check')
    if a.check:manifest()
    p=payload()
    if a.write:a.write.write_bytes(canonical(sealed(p))+b'\n')
    else:accept(read(a.check),p)
    if a.detail:a.detail.write_bytes(canonical(sealed(raw_payload()))+b'\n')
    t=self_test(p) if a.self_test else 0
    print('PASS_DG26',digest(p),'resealed_rejections='+str(t),'finite_degrees='+str(list(SIZES)))
if __name__=='__main__':main()
