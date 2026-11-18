#!/usr/bin/env python3
"""Portable exact certificate of strict log-concavity of Q(D)exp(-c cosh(2u)).
Parameters: 6<=c<=7, a=1/4, T>=32. Python standard library only.
No numerical transcendental function, sampled point, or external CAS is used.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

ZERO=(0,0,0)
def const(q): return {ZERO:F(q)} if q else {}
def add(*args):
    out={}
    for p in args:
        for k,v in p.items(): out[k]=out.get(k,F())+v
    return {k:v for k,v in out.items() if v}
def scale(p,q): return {k:v*q for k,v in p.items() if v*q}
def mul(p,q):
    out={}
    for a,v in p.items():
        for b,w in q.items():
            k=tuple(i+j for i,j in zip(a,b))
            out[k]=out.get(k,F())+v*w
    return {k:v for k,v in out.items() if v}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def derivative_x(p):
    return {(i-1,j,k):v*i for (i,j,k),v in p.items() if i}

def certificate():
    # Symbolic variables x=v-1>=0, y=T²-1024>=0, z=c-6 in [0,1].
    x={(1,0,0):F(1)}; y={(0,1,0):F(1)}; z={(0,0,1):F(1)}
    v=add(const(1),x); c=add(const(6),z); t2=add(const(1024),y)
    a2=F(1,16); b=add(t2,const(-a2)); vm1=add(power(v,2),const(-1))
    # Exact f''''/f and f''/f polynomials, independently checked by the
    # derivative recurrence in positive_kernel_bessel_skeptic_round3.py.
    p4=add(scale(mul(power(c,4),power(vm1,2)),16),
           scale(mul(power(c,3),mul(v,vm1)),-96),
           scale(mul(power(c,2),power(v,2)),112),
           scale(power(c,2),-64),scale(mul(c,v),-16))
    p2=add(scale(mul(power(c,2),vm1),4),scale(mul(c,v),-4))
    p=add(p4,scale(mul(b,p2),2),power(add(t2,const(a2)),2))
    dp=derivative_x(p); ddp=derivative_x(dp)
    # (log(f P))'' = -4R/P², using v'=2sinh2u and (v')²=4(v²-1).
    r=add(mul(mul(c,v),power(p,2)),scale(mul(mul(v,p),dp),-1),
          scale(mul(vm1,add(mul(ddp,p),scale(power(dp,2),-1))),-1))
    grouped={}
    for (i,j,k),q in r.items(): grouped.setdefault((i,j),{})[k]=q
    rows=[]
    for (i,j),d in sorted(grouped.items()):
        n=max(d)
        # z^k = sum_{ell=k}^n binom(ell,k)/binom(n,k) B_{ell,n}(z).
        bs=[sum((d.get(k,F())*F(comb(ell,k),comb(n,k))
                 for k in range(ell+1)),F()) for ell in range(n+1)]
        if not all(q>0 for q in bs):
            raise ArithmeticError(f'Nonpositive coefficient in group {(i,j)}: {bs}')
        rows.append({'x_power':i,'y_power':j,'z_degree':n,
                     'z_power_coefficients':[str(d.get(k,F())) for k in range(n+1)],
                     'z_bernstein_coefficients':[str(q) for q in bs],
                     'minimum_bernstein_coefficient':str(min(bs))})
    if (0,0) not in grouped:
        raise ArithmeticError('Need a strictly positive constant x,y group.')
    return r,rows

def main():
    r,rows=certificate()
    result={'status':'PASS: all Bernstein coefficients strictly positive',
            'arithmetic':'integer/Fraction, no external packages or floating point',
            'domain':{'x':'[0,infinity)','y':'[0,infinity)','z':'[0,1]'},
            'substitution':'v=1+x, T²=1024+y, c=6+z, a²=1/16',
            'formula':'R=c v P²-v P P_v-(v²-1)(P_vv P-P_v²); (log(fP))_uu=-4R/P²',
            'number_of_nonzero_monomials':len(r),'number_of_xy_groups':len(rows),
            'maximum_z_degree':max(q['z_degree'] for q in rows),
            'minimum_bernstein_coefficient':str(min(F(q['minimum_bernstein_coefficient']) for q in rows)),
            'coefficient_certificate':rows,
            'scope':'P>0 is proved separately; this certificate then proves strict log-concavity for every real u.'}
    p=(Path(__file__).resolve().parents[1]/'results'/'positive_kernel_bessel_logconcavity_skeptic_round3.json')
    p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='coefficient_certificate'},ensure_ascii=False))
if __name__=='__main__': main()
