#!/usr/bin/env python3
"""Exact finite structural checks for the cofinal-companion manuscript.

This uses rational Laurent polynomials in a and nu. It compares the order
recurrence with a separate Chebyshev differential-operator recurrence using
the Bessel ODE, thereby checking the radial derivative convention. It also
checks the recurrence coefficient signs and the rational concentration margin.
The analytic cusp, approximation, and asymptotic theorems are proved in prose.
"""
from fractions import Fraction as F
from math import factorial
import json

def tidy(p):return {k:v for k,v in p.items() if v}
def add(*args):
    out={}
    for p in args:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return tidy(out)
def scale(p,c):return tidy({k:v*c for k,v in p.items()})
def mul(p,q):
    out={}
    for (j,k),v in p.items():
        for (r,s),w in q.items():out[(j+r,k+s)]=out.get((j+r,k+s),F(0))+v*w
    return tidy(out)
def da(p):return tidy({(j-1,k):j*v for (j,k),v in p.items() if j})
def even_pair(p):return tidy({(j,k):2*v for (j,k),v in p.items() if k%2==0})

one={(0,0):F(1)}; inva={(-1,0):F(1)}; a={(1,0):F(1)}; nu={ (0,1):F(1)}
nu2_over_a={(-1,2):F(1)}

def radial_differential(A,B):
    # d_a(A*K+B*a*K') = [A'+B*(a+nu²/a)]K+[A/a+B']a*K'.
    return add(da(A),mul(B,add(a,nu2_over_a))),add(mul(A,inva),da(B))

def pair_add(x,y):return add(x[0],y[0]),add(x[1],y[1])
def pair_scale(x,c):return scale(x[0],c),scale(x[1],c)

P=[one,mul(nu,inva)];Q=[{},scale(inva,-1)]
# D_n=2*T_n(-d/da) applied to K and reduced by the Bessel ODE.
D=[(scale(one,2),{}),({},scale(inva,-2))]
maximum_order=24
order_equalities=0;sign_checks=0
for n in range(1,maximum_order+1):
    if n>=2:
        factor=scale(mul(add(nu,scale(one,n-1)),inva),2)
        P.append(add(P[-2],mul(factor,P[-1])))
        Q.append(add(Q[-2],mul(factor,Q[-1])))
        deriv=radial_differential(*D[-1])
        D.append(pair_add(pair_scale(deriv,-2),pair_scale(D[-2],-1)))
    expected=(even_pair(P[n]),even_pair(Q[n]))
    if D[n]!=expected:raise ArithmeticError(('order-vs-differential mismatch',n))
    order_equalities+=1
    if any(v<0 for v in P[n].values()):raise ArithmeticError(('P sign',n))
    if any(v>0 for v in Q[n].values()):raise ArithmeticError(('Q sign',n))
    sign_checks+=2

# Check the first three explicit paired-order formulas independently.
explicit=[
    ({},{(-1,0):F(-2)}),
    ({(0,0):F(2),(-2,2):F(4)},{(-2,0):F(-4)}),
    ({(-1,0):F(8),(-3,2):F(24)},
     {(-1,0):F(-2),(-3,0):F(-16),(-3,2):F(-8)})]
for n,pair in enumerate(explicit,1):
    if D[n]!=pair:raise ArithmeticError(('explicit low order',n))

# Rational upper bounds for cosh(1/10)-1 and sinh(1/10)-1/10.
x=F(1,10)
def exp_upper(x,n=30):
    partial=sum((x**k/F(factorial(k)) for k in range(n+1)),F(0))
    nxt=x**(n+1)/F(factorial(n+1))
    return partial+nxt/(1-x/F(n+2))
# Each series has positive terms; a geometric majorant bounds its full tail.
cosh_partial=sum((x**(2*k)/F(factorial(2*k)) for k in range(1,16)),F(0))
cosh_next=x**32/F(factorial(32))
cosh_upper=cosh_partial+cosh_next/(1-x*x/F(33*34))
sinh_partial=sum((x**(2*k+1)/F(factorial(2*k+1)) for k in range(1,16)),F(0))
sinh_next=x**33/F(factorial(33))
sinh_upper=sinh_partial+sinh_next/(1-x*x/F(34*35))
if not(cosh_upper<x*x and sinh_upper<x*x):raise ArithmeticError('concentration series bounds')
chernoff_margin=x/2-F(5,2)*x*x
if chernoff_margin!=F(1,40):raise ArithmeticError('Chernoff margin')

# The ODE factor in the exact companion control vanishes at nu=1/4.
if 2*F(1,4)**2-F(1,8)!=0:raise ArithmeticError('special-value ODE factor')

print(json.dumps({'status':'PASS','arithmetic':'exact rational Laurent polynomials and rational positive-series tails',
                  'maximum_order':maximum_order,'order_vs_differential_equalities':order_equalities,
                  'coefficient_sign_checks':sign_checks,'independent_explicit_low_order_formulas':len(explicit),
                  'chernoff_margin':str(chernoff_margin),'cosh_remainder_upper':str(cosh_upper),
                  'sinh_remainder_upper':str(sinh_upper),
                  'scope':'finite algebra, sign structure, concentration constants and special-value factor; analytic theorems and RH are not certified by this program'},indent=2))
