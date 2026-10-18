"""Exact complete moments after adding the positive triangle on roots 3,6,8.

This is generic scalar arithmetic: rational, Decimal, outward interval or Dual.
"""
from explore_added_edge import exp_moments,convolve,quotient
import exact_polynomial as tree_core

ROOTS=(3,6,8)
EDGES=((3,6),(3,8),(6,8))

def evaluate(z,ts,degree=22):
    zero=z[0]*0;one=zero+1;eta=one/10**10
    counts=(256,10)+(1,)*14;caps=[];total=[zero]*(degree+1);mixed={}
    for i,count in enumerate(counts):
        A,B,p=z[3*i:3*i+3]
        mu=[one]+[(A**n if i==0 else p*A**n+(one-p)*B**n)
                   *(one if n%2==0 else eta) for n in range(1,degree+1)]
        cap=tree_core.cumulants(mu);caps.append(cap)
        total=[a+count*b for a,b in zip(total,cap)]
        if i in ROOTS:
            mixed[i]=[(p*A**j+(one-p)*B**j)*(eta if j%2==0 else one)
                       for j in range(degree+1)]
    base=exp_moments(total);joint=[]
    for left,right in EDGES:
        excluded=exp_moments([a-b-c for a,b,c in zip(total,caps[left],caps[right])])
        joint.append(convolve(excluded,convolve(mixed[left],mixed[right])))
    t1,t2,t3=ts;c0=one+t1*t2*t3
    coefficients=(t1+t2*t3,t2+t1*t3,t3+t1*t2)
    denominator=c0+eta*eta*sum(coefficients,zero)
    mu=[quotient(c0*base[n]+sum((c*m[n] for c,m in zip(coefficients,joint)),zero),denominator)
        if n%2==0 else zero for n in range(degree+1)]
    k=tree_core.cumulants(mu);unit=tree_core.unit_cumulants(degree)
    return [k[n]/unit[n] for n in range(2,degree+1,2)],mu

def jet(z,ts,active,degree=22):
    zero=z[0]*0;one=zero+1
    dual=[tree_core.Dual(x,[one if i==j else zero for j in active])
          for i,x in enumerate(z+list(ts))]
    values,_=evaluate(dual[:48],dual[48:],degree)
    return [x.v for x in values],[list(x.d) for x in values]
