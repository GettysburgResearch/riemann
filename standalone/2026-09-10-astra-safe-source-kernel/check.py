#!/usr/bin/env python3
"""Bounded exact/interval checks, not a proof of Q-AC28 or RH.

Standard library only; no parent modules imported. Native even zeta values
are enclosed in two ways: Machin pi plus Bernoulli; rational Euler--Maclaurin.
Normal and optimized interpreters execute the same explicit checks.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json

BITS=256
SCALE=1<<BITS
ROOT=Path(__file__).resolve().parent
FILES={'README.md','PROOF.md','ATTEMPT.md','SOURCES.json','VALIDATION.md','check.py','results.json'}

def need(ok, message):
    if not ok: raise ValueError(message)

def down(x): return F((x.numerator*SCALE)//x.denominator,SCALE)
def up(x): return -down(-x)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        lo=F(lo);hi=lo if hi is None else F(hi)
        need(lo<=hi,'inverted interval')
        self.lo,self.hi=down(lo),up(hi)
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
        o=iv(o);need(o.lo*o.hi>0,'division interval contains zero')
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return iv(o)/self
    def __pow__(self,n):
        need(type(n) is int and n>=0,'invalid power')
        r=I(1);b=self
        while n:
            if n&1:r=r*b
            b=b*b;n//=2
        return r
    def pair(self):return [int(self.lo*SCALE),int(self.hi*SCALE)]

def iv(x):return x if isinstance(x,I) else I(x)
def frac(x):return [x.numerator,x.denominator]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(x):return sha256(canonical(x)).hexdigest()

def bernoulli(n):
    b=[F(1)]
    for j in range(1,n+1):
        b.append(-sum(F(comb(j+1,k))*b[k] for k in range(j))/F(j+1))
    return b

def rising(s,k):
    x=1
    for j in range(k):x*=s+j
    return x

def atan_bounds(q,N):
    s=sum((F(1 if j%2==0 else -1,(2*j+1)*q**(2*j+1)) for j in range(N)),F(0))
    t=s+F(1 if N%2==0 else -1,(2*N+1)*q**(2*N+1))
    return I(min(s,t),max(s,t))

def pi_bounds():return 16*atan_bounds(5,100)-4*atan_bounds(239,50)

def even_values(k,pi,b):
    s=2*k
    factor=(1-F(1,2**s))*((-1)**(k+1))*b[s]*F(2**(s-1),factorial(s))
    return factor*(pi**s)

def em_value(k,b,N=64,K=24):
    s=2*k
    value=sum((F(1,n**s) for n in range(1,N)),F(0))+F(1,(s-1)*N**(s-1))+F(1,2*N**s)
    last=F(0)
    for j in range(1,K+1):
        last=b[2*j]*F(rising(s,2*j-1),factorial(2*j)*N**(s+2*j-1))
        value+=last
    # Euler--Maclaurin with the full periodic B_(2K) remainder:
    # |R| <= |B_(2K)| (s)_(2K-1) N^(-s-2K+1)/(2K)!.
    return (1-F(1,2**s))*I(value-abs(last),value+abs(last))

def integral_exp(k):
    need(k.denominator==1 and k>0,'this finite protocol uses positive integer exponents')
    return F(3**k.numerator-1,k.numerator)

def kernel(z,w,U,W,eta,C):
    J=(1-U)*(1-W)*integral_exp(z+w)+(1-U)*W*integral_exp(z+F(1,2))
    J+=U*(1-W)*integral_exp(w+F(1,2))+2*U*W
    return (eta+4*C*(z-F(1,2))*(w-F(1,2))*U*W)/(z+w)-J

def kernel_poly(z,w,U,W,eta,C):
    # Independent expansion with x=exp(r/2), dr=2dx/x.
    pp={int(2*z):1-U,1:U};qq={int(2*w):1-W,1:W}
    J=iv(0)
    for j,c in pp.items():
        for k,d in qq.items():
            need((j+k)%2==0,'bad polynomial integration power')
            J+=c*d*F(2*(3**((j+k)//2)-1),j+k)
    az=(z-F(1,2))*U;aw=(w-F(1,2))*W
    return eta/(z+w)+4*C*az*aw/(z+w)-J

def ldl(K):
    n=len(K);L=[[I(0) for _ in range(n)] for _ in range(n)];D=[]
    for i in range(n):
        p=K[i][i]-sum((L[i][j]*L[i][j]*D[j] for j in range(i)),I(0))
        need(p.lo>0,'native interval LDL not positive')
        D.append(p);L[i][i]=I(1)
        for k in range(i+1,n):
            L[k][i]=(K[k][i]-sum((L[k][j]*L[i][j]*D[j] for j in range(i)),I(0)))/p
    return [p.pair() for p in D]

def bareiss_interval(K):
    a=[[iv(x) for x in row] for row in K];n=len(a);prev=I(1)
    if n==1:return a[0][0]
    for k in range(n-1):
        pivot=a[k][k]
        need(pivot.lo>0,'interval Bareiss pivot not positive')
        for i in range(k+1,n):
            for j in range(k+1,n):a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])/prev
        prev=pivot
    return a[-1][-1]

def determinant(a):
    a=[list(row) for row in a];n=len(a);prev=F(1)
    for k in range(n-1):
        need(a[k][k]!=0,'zero exact pivot')
        for i in range(k+1,n):
            for j in range(k+1,n):a[i][j]=(a[i][j]*a[k][k]-a[i][k]*a[k][j])/prev
        prev=a[k][k]
    return a[-1][-1]

def monomial_integral(power,lo,hi):
    return F(hi**(power+1)-lo**(power+1),power+1)

def polynomial_checks(U,W,zs):
    rows=[]
    for n in [2,4,6,8]:
        vectors=[[F(1) for i in range(n)],
                 [F((-1)**i,i+1) for i in range(n)],
                 [F((i%3)-1) for i in range(n)],
                 [F((-1)**i*(i+1)) for i in range(n)]]
        for ci,c in enumerate(vectors):
            eta=F(1,100);C=F(1)
            degrees=[2*i+1 for i in range(n)]
            pnorm=sum((c[i]*c[j]*monomial_integral(degrees[i]+degrees[j],0,1)
                       for i in range(n) for j in range(n)),F(0))
            ep={0:sum((c[i]*U[i] for i in range(n)),I(0))}
            gp={}
            for i,d in enumerate(degrees):
                ep[d]=c[i]*(1-U[i]);gp[d]=c[i]*d*U[i]
            en=sum((a*b*monomial_integral(i+j,1,3)
                    for i,a in ep.items() for j,b in ep.items()),I(0))
            gn=sum((a*b*monomial_integral(i+j,0,1)
                    for i,a in gp.items() for j,b in gp.items()),I(0))
            energy=eta*pnorm+4*C*gn-en
            other=sum((c[i]*c[j]*kernel(zs[i],zs[j],W[i],W[j],eta,C)
                       for i in range(n) for j in range(n)),I(0))
            need(max(energy.lo,other.lo)<=min(energy.hi,other.hi),'polynomial isometry mismatch')
            need(energy.lo>0,'finite polynomial inequality failed')
            derivative=sum((c[i]*c[j]*degrees[i]*degrees[j]/F(degrees[i]+degrees[j]-1)
                           for i in range(n) for j in range(n)),F(0))
            tail=sum((c[i]*c[j]*degrees[i]*degrees[j]*(U[i]-1)*(U[j]-1)/F(degrees[i]+degrees[j]-1)
                      for i in range(n) for j in range(n)),I(0))
            need((F(16,25)*derivative-tail).lo>0,'noncritical derivative bound failed')
            rows.append({'n':n,'vector':ci,'p_coefficients':[frac(x) for x in c],
                         'pnorm':frac(pnorm),'polynomial_defect':energy.pair(),
                         'kernel_defect':other.pair(),'derivative_square':frac(derivative),
                         'derivative_tail_square':tail.pair()})
    need(400<432,'4/(3sqrt(3)) < 4/5 integer margin')
    return rows

def payload():
    b=bernoulli(48);pi=pi_bounds();need(F(3)<pi.lo<pi.hi<F(22,7),'pi enclosure')
    zs=[F(4*k-1,2) for k in range(1,9)]
    U=[even_values(k,pi,b) for k in range(1,9)]
    W=[em_value(k,b) for k in range(1,9)]
    for u,w in zip(U,W):need(max(u.lo,w.lo)<=min(u.hi,w.hi),'native zeta enclosure disagreement')
    mats=[]
    for eta in [F(0),F(1,100)]:
        for n in [2,4,6,8]:
            K=[[kernel(z,w,U[i],U[j],eta,F(1)) for j,w in enumerate(zs[:n])] for i,z in enumerate(zs[:n])]
            KK=[[kernel_poly(z,w,W[i],W[j],eta,F(1)) for j,w in enumerate(zs[:n])] for i,z in enumerate(zs[:n])]
            for i in range(n):
                for j in range(n):need(max(K[i][j].lo,KK[i][j].lo)<=min(K[i][j].hi,KK[i][j].hi),'kernel paths disagree')
            pivots=ldl(K);minors=[]
            for j in range(1,n+1):
                d=bareiss_interval([row[:j] for row in KK[:j]])
                need(d.lo>0,'native Sylvester certificate failed');minors.append(d.pair())
            mats.append({'n':n,'eta':frac(eta),'C':[1,1],'ldl_pivots':pivots,'principal_minors':minors,
                         'matrix_digest':digest([[a.pair() for a in row] for row in K])})
    controls=[]
    for ps,n in [([],1),([3],2),([3,5],2),([3,5,7],3)]:
        z=zs[:n];zz=[]
        for t in z:
            value=F(1)
            for p in ps:value/=1-F(1,p**int(t+F(1,2)))
            zz.append(value)
        K=[[kernel(t,s,zz[i],zz[j],F(1,100),F(1)) for j,s in enumerate(z)] for i,t in enumerate(z)]
        d=determinant(K);need(d<0,'Euler control failed')
        controls.append({'primes':ps,'n':n,'determinant':frac(d)})
    model=[]
    for eta in [F(1,2),F(1,10),F(1,100)]:
        for length in [F(1),F(2),F(3,2)]:
            C=length*length/(4*eta);rate=eta/length
            residual=eta/(2*rate)+4*C*rate/2-length
            wrong=eta/(2*rate)+3*C*rate/2-length
            need(residual==0 and wrong<0,'sharp marginal model')
            model.append({'eta':frac(eta),'length':frac(length),'C':frac(C),'equality':frac(residual),'lower_C_failure':frac(wrong)})
    # Pure rational, no actual zeta zero: remove the ell/c factors from (3.3).
    costs=[]
    for m in range(1,9):
        k=F(2*m,2*m-1);best=(k-1)/k**(2*m)
        need(best==F((2*m-1)**(2*m-1),(2*m)**(2*m)),'multiplicity optimization')
        for t in [k/F(2),k*2]:
            if t>1:need((t-1)/t**(2*m)<=best,'model cost maximum')
        costs.append([m,frac(k),frac(best)])
    return {'schema':'AC28-safe-source-kernel/v1','parent':'e6dbb8ef4e458ea4c8d1b17ced77ec28905a7472',
      'status':'PROPOSED; all-order positivity OPEN','rh_proved':False,'bits':BITS,
      'scope':'Eight finite native matrices and exact controls; not all orders or all heights',
      'native_nodes':[frac(z) for z in zs],'pi':pi.pair(),
      'zeta_odd_even_pi':[x.pair() for x in U],'zeta_odd_even_EM':[x.pair() for x in W],
      'native_matrices':mats,'Euler_controls':controls,'marginal_models':model,'multiplicity_controls':costs,
      'polynomial_isometries':polynomial_checks(U,W,zs), 'noncritical_integer_margin':32}

def sealed(p):return {'payload':p,'sha256':digest(p)}

def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b

def accept(report,expected):
    need(type(report) is dict and set(report)=={'payload','sha256'},'wrong envelope')
    need(report['sha256']==digest(report['payload']),'digest mismatch')
    need(same(report['payload'],expected),'primitive payload mismatch')

def reject_atom(_):raise ValueError('floating or nonfinite JSON prohibited')
def unique(items):
    out={}
    for k,v in items:
        need(k not in out,'duplicate JSON key');out[k]=v
    return out

def load(path):return json.loads(path.read_text(),parse_float=reject_atom,parse_constant=reject_atom,object_pairs_hook=unique)

def self_test(expected):
    accept(sealed(expected),expected)
    changes=[lambda p:p.update(rh_proved=True),lambda p:p.update(bits=128),
      lambda p:p['native_matrices'].pop(),lambda p:p['native_nodes'].pop(),
      lambda p:p['Euler_controls'][0].update(determinant=[199,300]),
      lambda p:p['native_matrices'][0]['ldl_pivots'][0].__setitem__(0,0),
      lambda p:p.update(scope='all orders proved'),lambda p:p.update(parent='0'*40),
      lambda p:p['marginal_models'][0].update(C=[0,1]),
      lambda p:p['multiplicity_controls'][-1].__setitem__(0,1)]
    for change in changes:
        bad=deepcopy(expected);change(bad);need(not same(bad,expected),'no-op corruption')
        try:accept(sealed(bad),expected)
        except ValueError:pass
        else:raise ValueError('resealed mutation accepted')
    return len(changes)

def manifest():
    path=ROOT/'MANIFEST.sha256';need(path.is_file(),'missing manifest')
    found={}
    for line in path.read_text().splitlines():
        h,n=line.split('  ',1);need(n in FILES and n not in found,'manifest membership')
        p=ROOT/n;need(p.is_file() and not p.is_symlink(),'file/symlink gate')
        need(sha256(p.read_bytes()).hexdigest()==h,'manifest mismatch: '+n);found[n]=h
    need(set(found)==FILES,'manifest coverage')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--write',type=Path);ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args();need(bool(args.check)^bool(args.write),'choose exactly one of --check/--write')
    if args.check:manifest()
    p=payload()
    if args.write:args.write.write_bytes(canonical(sealed(p))+b'\n')
    else:accept(load(args.check),p)
    tests=self_test(p) if args.self_test else 0
    print('PASS_AC28',digest(p),'resealed_rejections='+str(tests))
if __name__=='__main__':main()
