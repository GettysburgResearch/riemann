#!/usr/bin/env python3
"""CD26 bounded exact controls; no infinite estimate is authenticated here."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path
import certificate as C


def need(p, label):
    if not p: raise ValueError(label)


def trial_mu(n):
    ans=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -ans if n>1 else ans


def records():
    out=[]
    def add(name,count):out.append({'name':name,'fixtures':count,'status':'PASS'})
    mu=C.mobius(128)
    for n in range(1,129):need(mu[n]==trial_mu(n),'independent Mobius')
    add('independent_trial_factor_Mobius',128)
    count=0
    for N in range(1,129):
        _,cs=C.coefficients(N)
        need(sum((cs[n]/n for n in range(1,N+2)),F(0))==0,'pole balance')
        for k in range(1,N+1):
            need(sum(cs[n] for n in range(1,k+1) if k%n==0)==(1 if k==1 else 0),'divisor inverse')
            count+=1
    add('complete_finite_divisor_reproduction',count)
    add('all_compact_inverse_pole_balances',128)
    count=0
    for N in range(1,33):
        _,cs=C.coefficients(N)
        for w in (2,3,4,5):
            m=F(0);direct=F(0)
            for k in range(1,N+1):
                m+=F(mu[k],k)
                direct+=m*(F(1,k**(w-1))-F(1,(k+1)**(w-1)))/(w-1)
            pn=sum((cs[n]/n**w for n in range(1,N+2)),F(0))
            need(direct==pn/(w-1),'step integral vs transform')
            count+=1
    add('compact_transform_by_independent_step_integration',count)
    m=F(0);ss=F(0);mixed=F(0);diag=F(0)
    for N in range(1,129):
        m+=F(mu[N],N);ss+=m*m;mixed+=mu[N]*m;diag+=F(mu[N]**2,N)
        need(ss==(N+1)*m*m-2*mixed+diag,'signed norm telescoping')
        need(abs(m)<=1,'elementary mass')
        need(sum(mu[n]*(N//n) for n in range(1,N+1))==1,'floor inversion')
    add('exact_input_norm_signed_identity',128)
    add('complete_floor_identity_and_mass_bound',128)
    count=0
    for N in (1,2,4,8,16,32,64,128):
        _,cs=C.coefficients(N)
        prefix=F(0)
        for k in range(1,513):
            prefix+=sum(cs[n] for n in range(1,min(k,N+1)+1) if k%n==0)
            need(prefix==sum(cs[n]*(k//n) for n in range(1,N+2)),'floor vs divisor prefix')
            count+=1
    add('output_cell_slopes_two_independent_constructions',count)
    # Rodrigues expansion L_j(x)=sum (-1)^k binom(j,k)x^k/k!.
    for j in range(9):
        for k in range(9):
            val=sum((F((-1)**(r+s)*math.comb(j,r)*math.comb(k,s)*math.factorial(r+s),
                       math.factorial(r)*math.factorial(s))
                     for r in range(j+1) for s in range(k+1)),F(0))
            need(val==(1 if j==k else 0),'Laguerre orthogonality')
    add('Laguerre_jet_orthogonality_exact',81)
    # Compare two algebraic orders of expansion for shifted repeated-pole jets.
    for j in range(9):
        alpha=F(2,7);rho=F(5,4);T=F(11,3)
        lhs=sum((F(math.comb(j,k),math.factorial(k))*(2*alpha)**k *
                 sum((math.comb(k,l)*T**(k-l)*(-1)**l*math.factorial(l+1)/rho**(l+2)
                      for l in range(k+1)),F(0)) for k in range(j+1)),F(0))
        rhs=sum(((-1)**l*math.factorial(l+1)/rho**(l+2) *
                 sum((F(math.comb(j,k)*math.comb(k,l),math.factorial(k))*(2*alpha)**k*T**(k-l)
                      for k in range(l,j+1)),F(0)) for l in range(j+1)),F(0))
        need(lhs==rhs,'multiplicity expansion')
        need(F(1,math.factorial(j))**2*(2*alpha)**(2*j+1)/rho**4>0,'leading jet norm')
    add('shifted_multiplicity_jet_recombination',9)
    # Derivative of -exp(-u)[(a u+d)^2+2a(a u+d)+2a^2].
    for a in range(-6,7):
        for d in range(-6,7):
            H=[d*d+2*a*d+2*a*a,2*a*d+2*a*a,a*a]
            diff=[H[0]-H[1],H[1]-2*H[2],H[2]]
            need(diff==[d*d,2*a*d,a*a],'norm-cell antiderivative')
    add('norm_cell_antiderivative_coefficients',169)
    # B2=(x-1/2)^2-1/12, so -1/12<=B2<=1/6 on [0,1].
    need(F(1,4)-F(1,12)==F(1,6),'Bernoulli remainder maximum')
    need(F(1,12)+F(1,12)==F(1,6),'two endpoint remainder terms')
    need(math.factorial(2)/F(1)**3==2,'critical target norm')
    need(F(1,36*3)==F(1,108),'tail remainder constant')
    add('tail_and_target_normalizations',4)
    count=0
    for x in (F(-7,3),F(-1,7),F(0),F(2,5),F(19,6)):
        for y in (F(-5,4),F(-1,3),F(2,7),F(17,5)):
            ix=C.I.rat(x);iy=C.I.rat(y)
            for ob,exact in ((ix+iy,x+y),(ix-iy,x-y),(ix*iy,x*y),(ix/iy,x/y)):
                need(F(ob.lo,C.Q)<=exact<=F(ob.hi,C.Q),'directed operation');count+=1
    for p,q in ((0,1),(1,3),(2,1),(17,13)):
        r=C.I.rat(p,q).sqrt()
        need(F(r.lo,C.Q)**2<=F(p,q)<=F(r.hi,C.Q)**2,'directed sqrt');count+=1
    add('directed_interval_endpoint_contracts',count)
    need(C.I.rat(3).hi<C.PI.lo<C.PI.hi<C.I.rat(22,7).lo,'Machin pi enclosure')
    need(C.I.rat(2,3).hi<C.LOG2.lo<C.LOG2.hi<C.I.rat(7,10).lo,'log2 enclosure')
    for k in range(1,15):
        a=C.log_fraction(1<<k);b=k*C.LOG2
        need(a.lo==b.lo and a.hi==b.hi,'binary log reduction')
    add('directed_transcendental_calibration',16)
    for bad in (True,False,0,-1,129,1.0,'8'):
        try:C.mobius(bad)
        except ValueError:pass
        else:raise ValueError('unsafe resource input accepted')
    for p,q in ((True,1),(1,False),(1,0),(1,-1)):
        try:C.I.rat(p,q)
        except ValueError:pass
        else:raise ValueError('bad interval primitive accepted')
    add('resource_and_primitive_refusals',11)
    return {'schema':'CD26.exact-controls.v1','arithmetic':'EXACT_RATIONAL_AND_INTEGER_INTERVAL',
            'checks':out,'named_checks':len(out),'fixtures':sum(r['fixtures'] for r in out),
            'scope':'Bounded identities only; no RH, domain completion or unbounded norm estimate.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path)
    p.add_argument('--compare',type=Path);a=p.parse_args()
    text=json.dumps(records(),sort_keys=True,indent=2)+'\n'
    if a.compare and a.compare.read_text()!=text:raise ValueError('exact result mismatch')
    if a.output:a.output.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
