#!/usr/bin/env python3
"""Exact continuum certificate for a CONDITIONAL 0.874 scalar consumer.

This checks polynomial identities and strict rational margins, NOT the open
native inverse-moment bound or its imported analytic interfaces.
"""
from fractions import Fraction as F
from math import comb
import json

# Monomials use (degree in delta, degree in x), in that order.
def clean(p):
    return {k: F(v) for k,v in p.items() if v}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F(0))+v
    return clean(out)
def scale(p,a):
    return clean({k:v*a for k,v in p.items()})
def mul(p,q):
    out={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            z=(i+k,j+l);out[z]=out.get(z,F(0))+a*b
    return clean(out)
def power(p,n):
    out={(0,0):F(1)}
    for _ in range(n):out=mul(out,p)
    return out
def require(ok,name):
    if not ok: raise ValueError(name)

def main():
    one={(0,0):F(1)}; d={(1,0):F(1)};x={(0,1):F(1)}
    p=add(scale(one,2),scale(x,F(-26,9)),scale(power(x,2),F(8,9)))
    j=add(scale(one,F(12,5)),scale(x,F(-68,45)),
          mul(d,add(scale(one,-1),scale(x,-1),scale(power(x,2),F(8,9)))))
    left=add(scale(one,F(1487,42000)),
             mul(d,add(scale(one,F(3,35)),scale(x,F(-6,35)))))
    q=add(mul(left,j),scale(mul(mul(d,p),
              add(scale(one,F(11,30)),scale(d,F(-1,2)))),F(-53,70)))
    rows=[
      (F(1487,17500), F(-5389,14000), F(47,70)),
      (F(43123,567000), F(-787721,2268000), F(1903,3780)),
      (F(23792,354375), F(-173539,567000), F(121,315)),
      (F(55019,945000), F(-197441,756000), F(53,180))]
    expected=[F(15687639,196000000),F(167301088559,5143824000000),
              F(3048360119,321489000000),F(208185599,571536000000)]
    reconstruction={}; receipt=[]
    for k,((a,b,c),disc) in enumerate(zip(rows,expected)):
        require(c>0,'POSITIVE_QUADRATIC_LEADING_COEFFICIENT')
        require(4*a*c-b*b==disc and disc>0,'POSITIVE_QUADRATIC_DISCRIMINANT')
        quad={(0,0):a,(1,0):b,(2,0):c}
        weight=scale(mul(power(scale(x,2),k),
                    power(add(one,scale(x,-2)),3-k)),comb(3,k))
        reconstruction=add(reconstruction,mul(weight,quad))
        receipt.append({'index':k,'a':str(a),'b':str(b),'c':str(c),
                        '4ac_minus_b2':str(disc),'global_minimum':str(disc/(4*c))})
    require(q==reconstruction,'FULL_POLYNOMIAL_IDENTITY')
    ell=F(6,35); y=F(29,70); h=F(53,70); B=F(437,500)
    base=F(1,6)-ell/2-B+h
    margins={'low':F(11,12)-ell/4-B,
             'frequency_zero':h*(F(7,8)+F(17,50)-F(1,6))-B-ell,
             'floor_high':base+h/F(50),
             'small_rows':h*(F(17,50)-F(1,6))-y/2+F(63,5000),
             'second_regime':base}
    require(all(v<0 for v in margins.values()),'ALL_STRICT_PHYSICAL_MARGINS')
    require(ell/h-F(7,37)==F(73,1961),'PRIME_SUPPLY')
    require(ell<F(1,5) and y/F(20)>0 and h/F(600)>0,'LOW_AND_TAIL_DOMAINS')
    require(base==F(-377,10500),'BASE_IDENTITY')
    require(F(377,10500)-F(1,2000)==F(1487,42000),'CERTIFICATE_MARGIN')
    print(json.dumps({'status':'PASS','conditional_boundary':str(B),
        'inverse_D_exponent':'4/5','high_endpoint_margin':'1/2000',
        'delta_domain':['1/50','11/15'],'x_domain':['0','1/2'],
        'quadratic_certificates':receipt,'margins':{k:str(v) for k,v in margins.items()},
        'all_delta_quadratics_positive':True,'full_bivariate_identity':True,
        'open_inverse_estimate_proved':False,'new_unconditional_boundary':False},
        indent=2,sort_keys=True))
if __name__=='__main__':main()
