#!/usr/bin/env python3
"""Exact finite algebra supporting the anchor follow-up manuscripts.

Fraction arithmetic only for acceptance predicates. The written proofs, rather
than finite samples, establish the strong limits and spectral-floor theorem.
"""
from fractions import Fraction as F
from math import comb,factorial
import json

counts={}
def check(kind,value):
    if not value:raise ArithmeticError(kind)
    counts[kind]=counts.get(kind,0)+1

def laguerre(n):
    return [F((-1)**k*comb(n,k),factorial(k)) for k in range(n+1)]

def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return r

def multiply(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return r

for a in [F(2),F(5),F(20)]:
    for b in [F(1,2),F(1),F(7,3)]:
        for c in [F(1,3),F(2),F(5,2)]:
            ratio=(a-b)*(a-c)/((a+b)*(a+c))
            for N in [0,1,4,10,30]:
                lhs=2*a/((a+b)*(a+c))*sum((ratio**n for n in range(N+1)),F(0))
                rhs=(1-ratio**(N+1))/(b+c)
                check('cross_projection_geometric_identity',lhs==rhs)

for q in [F(7,6),F(4,3),F(3,2)]:
    for n in range(16):
        lhs=[v*q**j for j,v in enumerate(laguerre(n))]
        rhs=[F(0)]*(n+1)
        for k in range(n+1):
            d=F(comb(n,k))*q**k*(1-q)**(n-k)
            for j,v in enumerate(laguerre(k)):rhs[j]+=d*v
        check('laguerre_dilation_polynomial_identity',lhs==rhs)
    for N in [0,1,2,4,8]:
        D=[[F(comb(n,k))*q**k*(1-q)**(n-k) if k<=n else F(0)
            for n in range(N+1)] for k in range(N+1)]
        col=max(sum((abs(D[k][n]) for k in range(N+1)),F(0)) for n in range(N+1))
        row=max(sum((abs(v) for v in D[k]),F(0)) for k in range(N+1))
        check('dilation_column_norm_exact',col==(2*q-1)**N)
        check('dilation_row_norm_majorant',row<=q**N/(2-q)**(N+1))
        W=q/(2-q)*((2*q-1)*q/(2-q))**N
        check('weighted_schur_majorant',q*row*col<=W)
        for n in range(N+1):
            for m in range(N+1):
                p=[v*q**j for j,v in enumerate(laguerre(n))]
                r=[v*q**j for j,v in enumerate(laguerre(m))]
                gram=sum((v*factorial(j) for j,v in enumerate(multiply(p,r))),F(0))
                dot=sum((D[k][n]*D[k][m] for k in range(N+1)),F(0))
                check('weighted_gram_identity',gram==dot)

for a in [F(1),F(3,2),F(3)]:
    for p in [[F(1)], [F(2),F(-3)], [F(1),F(0),F(-2),F(1)], [F(1,3),F(2),F(-1),F(4,5),F(1,7)]]:
        autocorr=[F(0)]*len(p)
        for i,pi in enumerate(p):
            for j,pj in enumerate(p):
                for k in range(j+1):
                    autocorr[k]+=pi*pj*comb(j,k)*F(factorial(i+j-k),(2*a)**(i+j-k+1))
        integral=sum((c*factorial(k)*((a-F(1,2))**(-k-1)+(a+F(1,2))**(-k-1))
                      for k,c in enumerate(autocorr)),F(0))
        plus=sum((c*factorial(k)/(a-F(1,2))**(k+1) for k,c in enumerate(p)),F(0))
        minus=sum((c*factorial(k)/(a+F(1,2))**(k+1) for k,c in enumerate(p)),F(0))
        check('pole_autocorrelation_moment_identity',integral==plus*minus)

log2_lower=2*sum((F(1,(2*k+1)*3**(2*k+1)) for k in range(3)),F(0))
check('budget_safe_constant',F(1,2)+F(1,400)+F(4,19)<F(3,4))
check('log2_lower_above_two_thirds',log2_lower>F(2,3))
check('ratio_128_excludes_old_budget',F(7,2)*log2_lower>F(29,12))
check('relative_budget_control_lower_bound',200*F(49,4840)==F(245,121)>2)
B=[[F(0),F(1)],[F(1),F(2)]]
B2=[[sum((B[i][k]*B[k][j] for k in range(2)),F(0)) for j in range(2)] for i in range(2)]
check('positive_part_control_polynomial',all(B2[i][j]==2*B[i][j]+(1 if i==j else 0) for i in range(2) for j in range(2)))
check('control_null_direction',B[0][0]-B[0][1]-B[1][0]+B[1][1]==0)

print(json.dumps({'status':'PASS','arithmetic':'Python Fraction; no floats in acceptance predicates',
 'counts':counts,'total_exact_checks':sum(counts.values()),
 'certified_scalar_margins':{'fejer_constant':str(F(1,2)+F(1,400)+F(4,19)),
 'log2_positive_series_lower':str(log2_lower),'ratio_128_margin_lower':str(F(7,2)*log2_lower-F(29,12)),
 'relative_counterexample_lower':str(F(245,121))},
 'scope':'Finite algebra, normalization, and rational margins supporting the manuscripts; not a proof of infinite-dimensional convergence, imported compact-window certificates, or RH.'},indent=2,sort_keys=True))
