#!/usr/bin/env python3
"""Fresh pass-three reconstruction of RC's three one-jet minimum brackets.

The free-coordinate KKT routine is adapted from the earlier locally prepared
reviewer draft (not executed in the published pass-two record). This execution
is new. No author mathematical or numerical module is imported.
"""
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
spec=importlib.util.spec_from_file_location('reviewer_checks',Path(__file__).with_name('checks.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
mu=m.mu;solve=m.solve;need=m.need

def fingerprint(values):
    return hashlib.sha256(''.join(hex(F(q).numerator)+'/'+hex(F(q).denominator)+'\n' for q in values).encode()).hexdigest()

def residual_minimum(Y,N,H):
    """Full free coordinates + one KKT balance constraint, not author basis elimination.
    Integer common denominator forms every finite cell, then gcd covariance forms V.
    """
    free=list(range(Y,N+1)); dim=len(free)
    prefix={n:mu(n) for n in range(1,Y)}
    L=math.lcm(*range(1,H+1))
    G=[[0]*dim for _ in free]; ell=[0]*dim; c0=0
    for x in range(1,H):
        weight=L//(x*(x+1)); c=1-sum(a*(x//n) for n,a in prefix.items())
        row=[-(x//n) for n in free]
        c0+=weight*c*c
        for i in range(dim):
            ell[i]+=weight*c*row[i]
            for j in range(i+1): G[i][j]+=weight*row[i]*row[j]
    for i in range(dim):
        for j in range(i): G[j][i]=G[i][j]
    def covariance(m,n): return F(math.gcd(m,n)**2,12*m*n)
    mean0=1+F(sum(prefix.values()),2)
    VC=mean0*mean0+sum((F(a*b)*covariance(m,n) for m,a in prefix.items() for n,b in prefix.items()),F(0))
    VL=[mean0/2+sum((F(a)*covariance(m,n) for m,a in prefix.items()),F(0)) for n in free]
    VG=[[F(1,4)+covariance(m,n) for n in free] for m in free]
    constraint=[F(1,n) for n in free]; target=-sum((F(a,n) for n,a in prefix.items()),F(0))
    CN=N*N*(1+2*(N-1).bit_length()); radius=F(CN,H*(H+1)); outputs=[]
    for sign in (-1,0,1):
        t=F(1,H)+sign*radius
        A=[[F(G[i][j],L)+t*VG[i][j] for j in range(dim)] for i in range(dim)]
        b=[F(ell[i],L)+t*VL[i] for i in range(dim)]
        KKT=[row+[constraint[i]] for i,row in enumerate(A)]+[constraint+[F(0)]]
        sol=solve(KKT,[-x for x in b]+[target]); a=sol[:-1]
        value=F(c0,L)+t*VC+2*sum((x*y for x,y in zip(a,b)),F(0))
        value+=sum((a[i]*A[i][j]*a[j] for i in range(dim) for j in range(dim)),F(0))
        need(sum((x*y for x,y in zip(a,constraint)),F(0))==target,'KKT balance')
        need(value>0,'positive fixed-support minimum')
        outputs.append(value)
    need(outputs[0]<=outputs[1]<=outputs[2],'comparison minima order')
    need(all(d>0 for d in m.ldl_pivots(A)),'positive last comparison form')
    return {'Y':Y,'N':N,'H':H,'lower':m.decimal(outputs[0],12),
            'upper':m.decimal(outputs[2],12,True),'comparison_minima_sha256':fingerprint(outputs),
            'constraint':'native prefix and p(1)=0 only; no derivative normalization'}


def main():
    results=[residual_minimum(Y,4*Y,4096) for Y in (2,3,4)]
    expected=[('0.025607338825','0.025616531671'),('0.021620272026','0.021647203122'),('0.019070164807','0.019120804411')]
    need([(r['lower'],r['upper']) for r in results]==expected,'all three published brackets')
    print(json.dumps({'marker':'PASS_REVIEWER_RC_MINIMA','results':results,'checks':m.COUNTS,
        'tail_comparison':'separate minima of Q_H+(1/H +/- C_N/(H(H+1)))V, paper (18)',
        'author_code_executed':False,'unbounded_estimate_proved':False,'rh_proved':False},sort_keys=True,indent=2))

if __name__=='__main__':main()
