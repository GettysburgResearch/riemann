#!/usr/bin/env python3
"""Exact algebra and independent small-packet contractions for MWR26.
This is not an RH proof checker and makes no transcendental zero evaluation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from math import comb,factorial
from pathlib import Path
import sys
import sympy as sp
import certify as c

class Failed(ValueError):pass

def need(ok:bool,label:str)->None:
    if not ok:raise Failed(label)

def midpoint_interval_overlap(a:c.IV,b:c.IV)->bool:
    return max(a.lo,b.lo)<=min(a.hi,b.hi)

def trial_mu(n:int)->int:
    if n==1:return 1
    p=2;ans=1
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -ans if n>1 else ans

def run()->dict:
    named=[]
    def done(name,count=1):named.append({'name':name,'bounded_cases':count})
    z,t,v=sp.symbols('z t v',real=True)
    A=-sp.eye(4)
    for j in range(1,4):A[j,j-1]=1
    B=sp.eye(4)[:,0];C=sp.Matrix([[1,-sp.Rational(5,2),sp.Rational(7,4),-sp.Rational(3,8)]])
    Q=sp.Matrix(c.QNUM)/2048
    Phi=(z-sp.Rational(1,2))*(z+sp.Rational(1,2))**2/(z+1)**4
    need(sp.cancel((C*(z*sp.eye(4)-A).inv()*B)[0]-Phi)==0,'transfer')
    done('rational_transfer')
    need(A.T*Q+Q*A+C.T*C==sp.zeros(4),'Lyapunov sign')
    done('exact_Lyapunov_matrix',16)
    piv=list(Q.LDLdecomposition()[1].diagonal())
    expected=[sp.Rational(385,2048),sp.Rational(946109,788480),sp.Rational(6400405,484407808),sp.Rational(6561,3277007360)]
    need(piv==expected and all(p>0 for p in piv),'Q positive pivots')
    done('exact_LDL_pivots',4)
    Epoly=sp.Matrix(4,4,lambda i,j:t**(i-j)/sp.factorial(i-j) if i>=j else 0)
    for i in range(4):
        for j in range(4):
            pol=sp.Poly(sp.expand((C*Epoly)[i]*(C*Epoly)[j]),t)
            value=sum(v*sp.factorial(k[0])/2**(k[0]+1) for k,v in pol.terms())
            need(value==Q[i,j],'independent complete Gram integration')
    done('independent_output_polynomial_integrals',16)
    r=(B.T*Q*Epoly*B)[0]
    need(sp.expand(r-(385-639*t+162*t*t-9*t**3)/2048)==0,'correlation polynomial')
    done('complete_correlation')
    x=sp.Matrix(sp.symbols('x0:4'));amp=sp.symbols('amp')
    need(sp.expand(((x+amp*B).T*Q*(x+amp*B))[0]-(x.T*Q*x)[0]-2*amp*(B.T*Q*x)[0]-amp*amp*Q[0,0])==0,'jump identity')
    done('symbolic_full_jump_identity')
    # Complex test of the conjugate-amplitude cross term.
    for amp in [sp.I,1+sp.I,sp.Rational(2,3)-2*sp.I]:
        x=sp.Matrix([1+sp.I,2-sp.I,sp.Rational(1,2),-sp.I])
        value=sp.expand(((x+amp*B).conjugate().T*Q*(x+amp*B))[0]-(x.conjugate().T*Q*x)[0])
        rhs=2*sp.re(sp.conjugate(amp)*(B.T*Q*x)[0])+abs(amp)**2*Q[0,0]
        need(sp.simplify(value-rhs)==0,'complex jump')
    done('complex_jump_conjugation',3)
    # Exact synthetic controls that saturate the resonance coefficient.
    controls=[]
    for m in range(1,6):
        for beta,gamma in [(1,1),(2,3)]:
            lam=sp.I*gamma
            D=(z-lam)**m/(z+beta)**(m+1)
            Ft=sp.factorial(m-1)/(z+beta)**(m+1)
            derivative=sp.factorial(m)/(lam+beta)**(m+1)
            need(sp.simplify(m*Ft.subs(z,lam)/derivative)==1,'resonance constant')
            need(sp.cancel(D*sp.factorial(m-1)/(z-lam)**m-Ft)==0,'synthetic local convolution')
            controls.append([m,beta,gamma,str(F(1,2*m-1))])
    done('sharp_resonance_family',10)
    # Independently check all small mu values by trial factorization.
    mu=c.mobius(1024)
    need(all(mu[n]==trial_mu(n) for n in range(1,1025)),'sieve independently factored')
    done('trial_factorization_Mobius',1024)
    # Separate direct pair contractions at each of twelve small cutoffs.
    checkpoints=(1,2,3,4,5,6,8,12,16,24,32,64)
    log=[c.ZERO]*65
    for n in range(2,65):log[n]=log[n-1]+c.log_step(n)
    x=[c.ZERO]*4;diag=c.ZERO;work=c.ZERO
    overlaps=[]
    for n in range(1,65):
        x=c.shift(x,n);amp=c.reciprocal_sqrt(n).scale(mu[n])
        work=work+(amp*c.add(x[j].scale(c.QNUM[0][j],2048) for j in range(4))).scale(2)
        diag=diag+c.IV.rat(385*mu[n]*mu[n],2048*n);x[0]=x[0]+amp
        if n in checkpoints:
            direct=c.IV.rat(sum(F(385*mu[k]*mu[k],2048*k) for k in range(1,n+1)))
            for j in range(1,n+1):
                for k in range(j+1,n+1):
                    vv=log[k]-log[j];v2=vv.sq();v3=v2*vv
                    pol=c.IV.rat(385)+vv.scale(-639)+v2.scale(162)+v3.scale(-9)
                    direct=direct+(pol*c.reciprocal_sqrt(j*k)).scale(mu[j]*mu[k]*j,1024*k)
            need(midpoint_interval_overlap(direct,diag+work),f'direct pair reconstruction {n}')
            overlaps.append({'N':n,'direct':direct.obj(),'state':(diag+work).obj()})
    done('independent_pairwise_complete_norm',len(checkpoints))
    # Real-remainder inequalities used in the elementary finite-T corollary.
    pf=t+sp.Rational(3,2)*t*t+sp.Rational(3,8)*t**3
    envelope=sp.Rational(3,8)*t**3+sp.Rational(21,8)*t*t+sp.Rational(25,4)*t+sp.Rational(25,4)
    need(sp.expand(envelope-sp.diff(envelope,t)-pf)==0,'complete absolute target tail')
    need(sum(F(factorial(j),1)*2**(j+1) for j in [1,2])==20,'stable moment20')
    done('elementary_tail_and_moment',2)
    # Fixed interval primitives checked against elementary exact bounds.
    for n in range(1,65):
        iv=c.reciprocal_sqrt(n)
        need(iv.lo*iv.lo*n<=c.S*c.S<=iv.hi*iv.hi*n,'radical containment')
    done('inverse_radical_enclosures',64)
    for n in range(2,65):
        iv=c.log_step(n)
        # x/(1+x) <= log(1+x) <= x, x=1/(n-1).
        need(iv.lo*n>=c.S and iv.hi*(n-1)<=c.S,'log elementary enclosure check')
    done('log_step_elementary_comparisons',63)
    ans={'schema':'MWR26.exact-controls.v1','groups':named,'group_count':len(named),
         'bounded_cases':sum(x['bounded_cases'] for x in named),'Q_LDL_pivots':[str(p) for p in piv],
         'resonance_sharpness_controls':controls,'pairwise_controls':overlaps,
         'boundary':'Finite algebra and small-packet interval consistency; no machine proof of the analytic resonance or RH.'}
    return ans

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--expect',type=Path);a=ap.parse_args()
    try:
        r=run()
        if a.expect:need(json.loads(a.expect.read_text())==r,'retained exact controls differ')
        txt=json.dumps(r,sort_keys=True,indent=2)+'\n'
        if a.output:a.output.write_text(txt)
        else:print(txt,end='')
        return 0
    except (Failed,c.VerificationError,OSError,json.JSONDecodeError) as e:
        print(e,file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
