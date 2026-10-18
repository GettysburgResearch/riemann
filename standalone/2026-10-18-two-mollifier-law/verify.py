#!/usr/bin/env python3
"""Exact finite transfer and exponent checks; not analytic certification."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import itertools
import json

COUNTS = Counter()
MUTATION = ''

class Rejected(Exception):
    pass

def require(ok, group):
    COUNTS[group] += 1
    if not ok:
        raise Rejected(group)

def kn(n, v):
    v = F(v)
    return max(F(1), v, 1-F(1,n)+2*v/n, F(2,n)+(1-F(1,n))*v)

def mexp(n,d,a,j):
    return max(F(1),kn(n,j*a)-d*j*a)

def bexp(n,d,x,j):
    return kn(n,j*(1-x))-j*d*x

def envelope(n,d,a,x,r,p):
    main=max(kn(n,r*a)-d*r*a,kn(n,r*(a+x))-d*r*(a+x))
    mix=(mexp(n,d,a,p*r)+(p-2)*bexp(n,d,x,r)+bexp(n,d,x,2*r))/p
    return max(main,mix,F(0),r*a*(1-d))

def long_choice(k):
    if k==1: return F(3,5),1,F(3,5),3,F(4,15)
    if k==2: return F(1,2),1,F(3,4),3,F(1,4)
    if k<=5: return F(1,5),2,F(1,2),5,F(1,5)
    if k<=10: return F(1,k),2,F(1,2),5,F(1,k)
    if k<=15: return F(19,291),3,F(293,582),11,F(19,194)
    return F(1,k),3,F(293,582),11,F(3,2*k)

# Gaussian rationals for the finite transfer, independent of residue arithmetic.
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cadd(z,w): return (z[0]+w[0],z[1]+w[1])
def cscale(t,z): return (t*z[0],t*z[1])
def nsq(z): return z[0]**2+z[1]**2

def inv(z):
    q=nsq(z)
    if q==0: raise ValueError('Inverse of zero')
    return (z[0]/q,-z[1]/q)

ZERO=(F(0),F(0)); ONE=(F(1),F(0))

def capped(z,k,T):
    q=nsq(z)
    if q==0: return F(0) if MUTATION=='erase_zero_cap' else T
    return min(q**(-k),T)

# Exact Q[zeta_6]; basis (1,zeta), zeta^2=zeta-1.
def zmul(u,v):
    a,b=u; c,d=v
    return (a*c-b*d,a*d+b*c+b*d)

def zpow(z,k):
    out=(F(1),F(0))
    for _ in range(k): out=zmul(out,z)
    return out

def znorm(z): return z[0]**2+z[0]*z[1]+z[1]**2

def zadd(u,v): return (u[0]+v[0],u[1]+v[1])

def zscale(t,z): return (t*z[0],t*z[1])

ROOT=(F(0),F(1))

def choose(n,k):
    if k<0 or k>n: return 0
    v=1
    for j in range(1,k+1): v=v*(n-j+1)//j
    return v


def run():
    # Exact certificate for EVERY active branch in the declared finite k range.
    for k in range(1,257):
        a,r,x,p,delta=long_choice(k)
        b=F(2,4*k+1); e=F(1,8*k+2)
        require(F(0)<a<=x<=1,'legal_long_parameters')
        require(a<=F(1,k),'long_4k_length')
        require(mexp(6,F(1,2),a,2*k)==1,'long_4k_norm')
        require(envelope(6,F(1,2),a,x,r,p)<=1-delta,'complete_long_residual')
        require(mexp(6,F(1,2),b,2*k)==1,'short_4k_norm')
        require(envelope(6,F(1,2),b,F(3,4),1,3)<=1-b/2,'complete_short_residual')
        require(b/4==e and F(1,2)+k*b==1-e,'short_error_balance')
        require(delta>=2*e,'delta_dominates_twice_error')
        theta=delta-e
        require(F(0)<theta<delta,'balanced_cap_legal')
        require(min(e,theta,delta-theta,delta/2)==e,'full_transfer_minimum')
        require(theta<1-e,'finite_prescribed_member_cost')
        if k>=16:
            require(theta==F(11*k+3,2*k*(4*k+1)),'high_order_cap_formula')
            require(theta>F(1,k),'high_order_cap_comparison')
    # The whole intervals are proved in prose by affine inequalities;
    # these panels test every declared rational point, not uncountable coverage.
    for j in range(1,129):
        for amax,r,x,p,factor in ((F(1,2),1,F(3,4),3,F(1,2)),
                    (F(1,5),2,F(1,2),5,F(1)),
                    (F(19,291),3,F(293,582),11,F(3,2))):
            a=amax*j/128
            require(envelope(6,F(1,2),a,x,r,p)<=1-factor*a,'interval_residual_panels')
        a=F(j,640)
        require(mexp(6,F(1,2),a,10)==1,'fourth_interval_m10')
        require(bexp(6,F(1,2),F(1,2),2)==F(2,3),'fourth_fixed_dual')
        require(bexp(6,F(1,2),F(1,2),4)==1,'fourth_fixed_dual')
        require(F(1,3)+a+F(293,582)<=1-3*a/2 if a<=F(19,291) else True,'sixth_affine_comparison')
    require(mexp(6,F(1,2),F(19,291),33)==F(209,194),'sixth_endpoint_m66')
    require(bexp(6,F(1,2),F(293,582),3)==F(159,194),'sixth_endpoint_dual6')
    require(bexp(6,F(1,2),F(293,582),6)==F(285,194),'sixth_endpoint_dual12')

    # Theorem B: exact finite panels in n,d,k, retaining all minimum branches.
    for n,d,k in itertools.product((3,4,6,8,12),[F(j,20) for j in range(1,20)],range(1,25)):
        a=min(d/2,F(1,4*k)); b=a/2; delta=d*a
        require(F(0)<b<a<=d/2,'general_old_residual_scope')
        require(2*k*a<=F(1,2),'general_polynomial_length')
        require(mexp(n,d,a,2*k)==mexp(n,d,b,2*k)==1,'general_4k_norms')
        require(F(1,2)+k*b*(F(3,2)-d)<=F(11,16),'general_nonneutral_error')
        require(delta/4<F(1,16),'general_delta_margin')
        theta=3*delta/4
        require(min(d*b/2,delta/4,delta/2,theta,delta-theta)==delta/4,'general_transfer_minimum')
    # Exact comparison constants and controls for omitted terms.
    delta=F(4,15)
    require(min(F(1,10),F(1,6),delta-F(1,6))==F(1,10),'explicit_first_law')
    theta=F(1,4)
    costs=[F(1,10),theta]
    if MUTATION!='omit_bad_cap_cost': costs.append(delta-theta)
    require(min(costs)==F(1,60),'explicit_large_cap_error')
    require(F(1,60)>F(1,128) and F(1,10)>F(1,128),'strict_predecessor_error_comparison')
    require(theta/F(1,80)==20,'twentyfold_cap_exponent')
    lam=F(1,5)
    transfer=lam if MUTATION=='unsquared_cauchy_gain' else lam/2
    require(transfer==F(1,10),'cauchy_half_saving')
    delta_used=F(1,5) if MUTATION=='use_short_for_bad_count' else delta
    require(theta<delta_used,'long_and_short_roles')

    # Complete finite transfer panels with zeros and an active cap on a good row.
    vals=[ZERO,ONE,(F(-1),F(0)),(F(0),F(1)),(F(1,8),F(0)),(F(8),F(0)),
          (F(1,2),F(1,2)),(F(2),F(-1))]
    for L,P,Q in itertools.product(vals,repeat=3):
        EP=cadd(cmul(L,P),cscale(-1,ONE)); EQ=cadd(cmul(L,Q),cscale(-1,ONE))
        good=nsq(EP)<=F(1,4)
        if nsq(L)==0:
            require(not good,'zero_is_bad_for_every_mollifier')
            require(capped(L,1,F(7))==7,'zero_receives_cap')
        if good:
            I=inv(L)
            require(nsq(I)<=4*nsq(P),'good_inverse_control')
            require(cadd(I,cscale(-1,Q))==cscale(-1,cmul(I,EQ)),'same_row_inverse_identity')
            for k in range(1,7):
                diff=abs(nsq(I)**k-nsq(Q)**k)
                C=4*k*(2**(2*k-1)+1)
                require(diff**2<=C*C*nsq(EQ)*(nsq(P)**k+nsq(Q)**k)**2,'power_difference_bound')
                for T in (F(2),F(7),F(100)):
                    loss=nsq(I)**k-capped(L,k,T)
                    require(F(0)<=loss<=2**(4*k)*nsq(P)**(2*k)/T,'good_cap_loss_retained')
    L=(F(1,8),F(0)); P=(F(8),F(0)); T=F(2)
    require(nsq(cadd(cmul(L,P),cscale(-1,ONE)))==0,'exact_inverse_good_row')
    loss=F(0) if MUTATION=='cap_inactive_on_good' else nsq(inv(L))-capped(L,1,T)
    require(loss==62,'cap_can_be_active_on_good_row')

    # Cauchy and Markov on complete specified rational arrays, with zero weights.
    choices=(F(0),F(1,2),F(1),F(2))
    for w,x,y in itertools.product(itertools.product(choices,repeat=2),repeat=3):
        dot=sum(ww*xx*yy for ww,xx,yy in zip(w,x,y))
        require(dot**2<=sum(ww*xx**2 for ww,xx in zip(w,x))*sum(ww*yy**2 for ww,yy in zip(w,y)),'weighted_cauchy')
        for r in (1,2,3):
            bad=sum(ww for ww,xx in zip(w,x) if xx>F(1,2))
            require(bad<=2**(2*r)*sum(ww*xx**(2*r) for ww,xx in zip(w,x)),'weighted_markov')
    # Exact local n-free coprimality probability from all allowed valuations.
    for q,n in itertools.product((2,3,7,13,49),(3,4,6,8)):
        true=F((q-1)*q**(n-1),q**n-1)
        formula=1-F(1,q) if MUTATION=='wrong_nfree_probability' else (1-F(1,q))/(1-F(1,q**n))
        require(true==formula,'nfree_local_probability')
        require(sum(F((q-1)*q**(n-j-1),q**n-1) for j in range(n))==1,'valuation_probability_total')
    # Cyclotomic local Euler moments, including ALL aliases when k>=6.
    for k,t,phase in itertools.product(range(1,9),(F(1,3),F(1,5)),range(6)):
        psi=zpow(ROOT,phase)
        avg=F(0)
        for e in range(6):
            z=zmul(psi,zpow(ROOT,e))
            avg+=znorm(zadd((F(1),F(0)),zscale(-t,z)))**k/6
        expanded=(F(0),F(0))
        for i,j in itertools.product(range(k+1),repeat=2):
            neutral=(i==j) if MUTATION=='drop_sextic_aliases' else ((i-j)%6==0)
            if neutral:
                coeff=choose(k,i)*choose(k,j)*(-t)**(i+j)
                expanded=zadd(expanded,zscale(coeff,zpow(ROOT,(phase*(i-j))%6)))
        require(expanded==(avg,F(0)),'complete_cyclotomic_euler_moment')
        require(avg>0,'positive_local_euler_factor')
    # Exact monomial integral with cap C=N^(2km), radius1, leading coefficient1.
    for k,m,N in itertools.product(range(1,9),range(1,7),(2,3,5,11)):
        q=2*k*m
        exponent=2*k if MUTATION=='lost_zero_multiplicity' else q
        direct=2*F(N**(q-1))+F(2,q-1)*(N**(q-1)-1)
        formula=F(2*exponent,exponent-1)*N**(exponent-1)-F(2,exponent-1)
        require(direct==formula,'vertical_monomial_full_tail')
        require(F(1,4)*(1-F(1,q))<1,'vertical_fixed_zero_fits_family_scale')
    return {
       'status':'FINITE_CHECKS_PASS_NOT_ANALYTIC_CERTIFICATION',
       'groups':dict(sorted(COUNTS.items())), 'total_predicates':sum(COUNTS.values()),
       'k_panels':256, 'general_parameter_panels':5*19*24,
       'first_moment_laws':[
          {'reciprocal_order':2,'cap':'1/6','error_saving':'1/10'},
          {'reciprocal_order':2,'cap':'1/4','error_saving':'1/60'}],
       'general_sigma_law':'Delta=d*min(d/2,1/(4k)); cap=3Delta/4; saving=Delta/4',
       'analytic_inputs_reproved':False, 'independent_referee':False,
       'rh_proved':False,
       'coverage':'Complete declared rational finite arrays and cyclotomic local fixtures; no actual L-values or full number-field census.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',default='')
    args=parser.parse_args(); MUTATION=args.mutation
    try:
        print(json.dumps(run(),indent=2,sort_keys=True))
    except Rejected as exc:
        raise SystemExit('REJECT:'+str(exc))
