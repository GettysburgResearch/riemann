#!/usr/bin/env python3
"""Exact symbolic/rational checks for the independent Bessel-kernel audit.
No Bessel numerical roots are used as proof. Standard library only.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from math import comb

# Tiny exact polynomial arithmetic in the symbol v, with coefficients polynomial in c.
def add(a,b):
    z=dict(a)
    for k,x in b.items(): z[k]=z.get(k,F())+x
    return {k:x for k,x in z.items() if x}
def mul(a,b):
    z={}
    for (i,j),x in a.items():
        for (k,l),y in b.items(): z[i+k,j+l]=z.get((i+k,j+l),F())+x*y
    return {k:x for k,x in z.items() if x}
def scale(a,q): return {k:x*q for k,x in a.items() if x*q}

def derivative_uvw(p):
    # Variables (v,t,c), with v'=2t, t'=2v, c'=0.
    z={}
    for (i,j,k),x in p.items():
        if i: z[i-1,j+1,k]=z.get((i-1,j+1,k),F())+2*i*x
        if j: z[i+1,j-1,k]=z.get((i+1,j-1,k),F())+2*j*x
    return {k:x for k,x in z.items() if x}

def recur_derivative_ratio(p):
    # If f^(m)=p f and f'/f=-2ct, then f^(m+1)/f=p'-2ct p.
    z=derivative_uvw(p)
    for (i,j,k),x in p.items(): z[i,j+1,k+1]=z.get((i,j+1,k+1),F())-2*x
    return {k:x for k,x in z.items() if x}

def eliminate_even_t(p):
    z={}
    for (i,j,k),x in p.items():
        assert j%2==0
        for q in range(j//2+1):
            key=(i+2*q,k)
            z[key]=z.get(key,F())+x*comb(j//2,q)*(-1)**(j//2-q)
    return {k:x for k,x in z.items() if x}

def main():
    # f''''/f = g''''+4g'g'''+3(g'')²+6(g')²g''+(g')⁴,
    # g'=-2c sinh2u, g''=-4c v, g'''=-8c sinh2u,g''''=-16c v.
    v={(1,0):F(1)}; c={(0,1):F(1)}; one={(0,0):F(1)}
    vv=mul(v,v); cc=mul(c,c); sinh2=add(vv,scale(one,-1))
    result=add(scale(mul(c,v),-16),scale(mul(cc,sinh2),64))
    result=add(result,scale(mul(cc,vv),48))
    result=add(result,scale(mul(mul(cc,c),mul(v,sinh2)),-96))
    result=add(result,scale(mul(mul(cc,cc),mul(sinh2,sinh2)),16))
    expected={(4,4):F(16),(2,4):F(-32),(0,4):F(16),
              (3,3):F(-96),(1,3):F(96),(2,2):F(112),
              (0,2):F(-64),(1,1):F(-16)}
    assert result==expected
    # A separate derivative recurrence independently checks the hand formula.
    p={(0,0,0):F(1)}
    for order in range(1,5):
        p=recur_derivative_ratio(p)
        if order==2:
            assert eliminate_even_t(p)=={(2,2):F(4),(0,2):F(-4),(1,1):F(-4)}
    assert eliminate_even_t(p)==expected
    at32=32**4-56*32**2-197792
    assert at32==793440 and at32>0
    # derivative 4T(T²-28)>0 for T>=32.
    assert 32**2>28
    # Coefficient simplifications use only c<7, T²-a²>0.
    a=F(1,4)
    assert F(32**2)-a*a>0
    assert 576*7**3+32*7==197792
    out={'status':'exact algebra/constant checks passed',
         'arithmetic':'integer and Fraction only',
         'fourth_derivative_polynomial':{f'v^{i} c^{j}':str(x) for (i,j),x in sorted(result.items())},
         'positive_kernel_lower_at_T32':at32,
         'limitations':'Infinite spectral and phase arguments are analytic proofs in the accompanying audit, not numerical claims.'}
    p=(Path(__file__).resolve().parents[1]/'results'/'positive_kernel_bessel_skeptic_round3.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'positive_kernel_lower_at_T32':at32,'output':str(p)}))
if __name__=='__main__': main()
