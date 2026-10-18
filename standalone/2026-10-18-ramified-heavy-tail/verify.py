#!/usr/bin/env python3
"""Exact finite algebra tests. They do not certify an infinite analytic theorem."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F

class CheckFailure(RuntimeError):
    pass

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--mutation', choices=['ramified-zero','drop-square-branch','wrong-moment-exponent','erase-second-zeta'])
    args = ap.parse_args()
    counts: dict[str,int] = {}
    def check(condition: bool, group: str) -> None:
        if not condition:
            raise CheckFailure(group)
        counts[group] = counts.get(group, 0)+1

    # q=t^4 makes x=1/4 and square-root Gauss magnitudes rational.
    # These are abstract sign-phase fixtures, not actual Gauss-sum evaluations.
    for t in [5,7,11,13]:
        q=F(t**4)
        for h, theta, u1, u2, u3 in itertools.product([-1,1],repeat=5):
            g=F(-1,h*u1)
            a=g*h/theta/F(t**3)
            b=F(h**3,theta**3*t**7)
            r=F(theta,t**8)
            v=F(1,t**48)
            tau1,tau2,tau3,tau4,tau5=[F(t*t*u) for u in [u1,u2,u3,u2,u1]]
            d=-a*tau1
            e=q**6*b*b*v
            check(d==F(theta,t), 'source_phase_relation')
            check(tau1*tau5==q and tau2*tau4==q,'gauss_norm_relations')
            if args.mutation=='ramified-zero':
                a=b=r=d=F(0)
                e=F(0)
            N1=1-e/q+d*r*(1-q*v)
            T2=(1-v)*q*q*b*tau3
            if args.mutation=='drop-square-branch':
                T2=F(0)
            N2=1-e/q-(q-1)*d*r+T2
            N3=1-e/q-(q-1)*d*r+(1-v)*(q*q*b*tau1*tau2*r+q**3*a*b*tau4)
            N4=1-e/q-(q-1)*d*r+(1-v)*q**3*a*b*tau1*tau3*r
            N5=1-e/q-(q-1)*d*r-(1-v)*q**5*b*b
            H=[n/(1-e) for n in [N1,N2,N3,N4,N5]]
            W=r
            f0=1/(1-v)+W/(1-W)+e/(1-e)*((1-1/q)/(1-v)+W)-d/(1-e)*(1+(q-1)*W*v/(1-v))
            H0=(1-v)*(1-W)*f0/(1-d)
            check(abs(H0-1)<=F(8,t**9),'unramified_error_fixture')
            check(abs(H[0]-1)<=F(8,t**9),'valuation_one_error_fixture')
            check(abs(abs(H[1])/t**3-1)<=F(4,t**3),'square_branch_dominance')
            check(abs(H[2])<=4*t**4,'valuation_three_majorant')
            check(abs(H[3])<=4*t**3,'valuation_four_majorant')
            check(abs(H[4])<=4*t**6,'valuation_five_majorant')

    # Complete integer valuation census (not a number-field ideal census).
    limit=8192
    spf=list(range(limit+1))
    for p in range(2,math.isqrt(limit)+1):
        if spf[p]==p:
            for n in range(p*p,limit+1,p):
                if spf[n]==n: spf[n]=p
    factors=[{} for _ in range(limit+1)]
    for n in range(2,limit+1):
        p=spf[n]; m=n//p
        factors[n]=dict(factors[m]); factors[n][p]=factors[n].get(p,0)+1
    sixfree=0
    for n in range(1,limit+1):
        if any(e>=6 for e in factors[n].values()): continue
        sixfree+=1
        slots=[1]*5
        for p,e in factors[n].items(): slots[e-1]*=p
        check(math.prod(v**(j+1) for j,v in enumerate(slots))==n,'exact_valuation_reconstruction')
        check(all(math.gcd(slots[i],slots[j])==1 for i in range(5) for j in range(i)), 'slot_coprimality')

    # Prefix and formal-convolution identity for zeta(s)zeta(2s-A), with S={2,3}.
    allowed=[math.gcd(n,6)==1 for n in range(limit+1)]
    iprefix=[0]*(limit+1)
    for n in range(1,limit+1): iprefix[n]=iprefix[n-1]+int(allowed[n])
    digests={}
    for A in range(5):
        direct=[0]*(limit+1)
        for d in range(1,math.isqrt(limit)+1):
            if not allowed[d]: continue
            weight=d**A
            for b in range(1,limit//(d*d)+1):
                if allowed[b]: direct[b*d*d]+=weight
        factored=[0]*(limit+1); factored[1]=1
        for n in range(2,limit+1):
            if not allowed[n]:continue
            value=1
            for p,e in factors[n].items():
                value*=sum(p**(A*j) for j in range(e//2+1))
            factored[n]=value
        check(direct==factored,'two_zeta_coefficient_arrays')
        running=0
        for n in range(1,limit+1):
            running+=direct[n]
            if n in [1,2,7,13,64,512,2048,8192]:
                separate=sum(d**A*iprefix[n//(d*d)] for d in range(1,math.isqrt(n)+1) if allowed[d])
                check(running==separate,'weighted_square_prefix_identity')
        # W_p=1+z+p^A z^2, h_p=W_p(1-z)(1-p^A z^2).
        harr=[0]*(limit+1); harr[1]=1
        warr=[0]*(limit+1); warr[1]=1
        for n in range(2,limit+1):
            if not allowed[n]:continue
            hv=wv=1
            for p,e in factors[n].items():
                cp=[1,1,p**A]
                inv2=[1,0,-p**A]
                if args.mutation=='erase-second-zeta': inv2=[1]
                qpoly=[0]*(len(cp)+len(inv2)-1)
                for i,x in enumerate(cp):
                    for j,y in enumerate(inv2):qpoly[i+j]+=x*y
                hpoly=qpoly+[0]
                for j in range(len(qpoly)):hpoly[j+1]-=qpoly[j]
                hv*=hpoly[e] if e<len(hpoly) else 0
                wv*=cp[e] if e<len(cp) else 0
            harr[n]=hv; warr[n]=wv
        conv=[0]*(limit+1)
        for d in range(1,limit+1):
            if not harr[d]:continue
            for b in range(1,limit//d+1):conv[d*b]+=harr[d]*direct[b]
        for n in range(1,limit+1):check(conv[n]==warr[n],'signed_quotient_convolution')
        digests[str(A)]=hashlib.sha256(json.dumps(direct,separators=(',',':')).encode()).hexdigest()

    for A in [F(j,12) for j in range(121)]:
        sigma=max(F(1),(A+1)/2)
        check(-sigma<=-1 and A-2*sigma<=-1,'leading_critical_weights')
        check(F(4,3)*A-3*sigma<=-F(5,3),'third_branch_summability')
        check(A-4*sigma<=-3 and 2*A-5*sigma<=-3,'higher_branch_summability')
    delta=F(1,4)
    exponents={}
    for p in [F(1),F(4,3),F(2),F(4),F(8)]:
        A=3*p*delta
        sigma=max(F(1),(A+1)/2)
        exponents[str(p)]={'power':str(sigma),'log_power':int(A==1)}
    if args.mutation=='wrong-moment-exponent':exponents['2']['power']='7/4'
    check(exponents['2']['power']=='5/4' and exponents['4']['power']=='2','sharp_example_exponents')
    check(exponents['4/3']['log_power']==1,'critical_endpoint_log')
    check(F(3)-F(4,3)==F(5,3) and F(4)-1==3 and F(5)-2==3,'weak_tail_other_slot_exponents')
    print(json.dumps({'status':'PASS','coverage':counts,'predicate_total':sum(counts.values()),
        'abstract_local_configurations':128,'integer_census_limit':limit,'sixth_free_integer_count':sixfree,
        'moment_example_x':'1/4','moment_exponents':exponents,'two_zeta_array_sha256':digests,
        'scope':'Finite rational local fixtures and complete integer counting identities only. No actual Gauss sum, complete ideal census, or analytic certification.'},sort_keys=True,indent=2))

if __name__=='__main__':main()
