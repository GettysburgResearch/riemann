#!/usr/bin/env python3
"""Exact algebraic checks plus explicitly nonvalidated Bessel observations.
The all-parameter theorem is proved in the companion campaign, not by these samples.
Exact portion uses standard library; numerical portion requires mpmath.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
ROOT=Path(__file__).resolve().parents[2]

def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}

def mono(p,dc=0,dx=0,dy=0,factor=1):
    return {(c+dc,x+dx,y+dy):factor*v for (c,x,y),v in p.items()}

def deriv(p,index):
    out={}
    for powers,v in p.items():
        if not powers[index]:continue
        k=list(powers);k[index]-=1;out[tuple(k)]=v*powers[index]
    return out

def reduce_y(p):
    out={}
    for (c,x,y),v in p.items():
        q,r=divmod(y,2)
        for j in range(q+1):
            key=(c,x+2*j,r)
            out[key]=out.get(key,0)+v*comb(q,j)*(-1)**(q-j)
    return {k:v for k,v in out.items() if v}

def exact_checks():
    p={(0,0,0):1};derivatives={}
    for k in range(1,5):
        p=reduce_y(add(mono(deriv(p,1),dy=1,factor=2),mono(deriv(p,2),dx=1,factor=2),mono(p,dc=1,dy=1,factor=-2)))
        derivatives[k]=p
    expected2={(2,2,0):4,(2,0,0):-4,(1,1,0):-4}
    expected4={(4,4,0):16,(4,2,0):-32,(4,0,0):16,(3,3,0):-96,(3,1,0):96,(2,2,0):112,(2,0,0):-64,(1,1,0):-16}
    assert derivatives[2]==expected2 and derivatives[4]==expected4
    threshold=32**4-56*32**2-197792
    assert threshold==793440>0
    prefix=[]
    for N in [1,2,5,10,100,1000]:
        G=8*N*N+50;T=10*N*G
        baseline=F(1,6*G*G);variation=F(8*N*N,T*T)
        assert T>=32 and variation<baseline/2
        prefix.append({'N':N,'G_N':G,'T_N':T,'baseline_Li_lower':str(baseline),'quartet_Li_absolute_upper':str(variation),'positive_margin_lower':str(baseline-variation)})
    out={'status':'exact standard-library polynomial differentiation and rational finite-prefix bounds','variables':['c','x=cosh(2u)','y=sinh(2u)'],'relation':'y^2=x^2-1','P2':[{'powers':k,'coefficient':v} for k,v in sorted(expected2.items())],'P4':[{'powers':k,'coefficient':v} for k,v in sorted(expected4.items())],'global_kernel_threshold_T':32,'global_margin_at_threshold':threshold,'prefix_samples':prefix}
    (ROOT/'experiments/results/bessel_round3_exact.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

def quartet_li(n,T):
    # Exact symmetric zero contribution for s-roots1/4+-iT,3/4+-iT.
    A=16*T*T-3;B=16*T;x,y=1,0
    for _ in range(n):x,y=A*x-B*y,B*x+A*y
    return 4-2*F(x)*(F(1,(1+16*T*T)**n)+F(1,(9+16*T*T)**n))

def numerical_observations():
    import mpmath as mp
    mp.mp.dps=85;c=2*mp.pi
    def Ac(tau):
        term=total=mp.mpc(1)
        for k in range(1,81):term*=c*c/(4*k*(k+1j*tau));total+=term
        return total
    def phase(tau):return tau*mp.log(c/2)-mp.im(mp.loggamma(1+1j*tau))+mp.arg(Ac(tau))
    roots=[]
    for m in [50,100,200]:
        p=mp.pi*(m-mp.mpf(1)/4)
        guess=p/mp.lambertw(2*p/(mp.e*c))
        tau=mp.findroot(lambda t:phase(t)+m*mp.pi,(guess*.99,guess*1.01))
        res=mp.exp(mp.pi*tau/2)*mp.sqrt(tau)*mp.besselk(1j*tau,c)
        roots.append({'phase_integer':m,'tau':mp.nstr(tau,35),'w_positive_ordinate':mp.nstr(2*tau,35),'scaled_K_residual':mp.nstr(abs(res),12),'scope':'sample phase roots; absolute zero index/completeness not numerically certified'})
    N=6
    coeff=mp.taylor(lambda s:mp.log(mp.besselk((s-mp.mpf('.5'))/2,c)),mp.mpf(1),N)
    lis=[]
    for n in range(1,N+1):
        base=n*mp.fsum(mp.binomial(n-1,k-1)*coeff[k] for k in range(1,n+1))
        q=quartet_li(n,32);model=base+mp.mpf(q.numerator)/q.denominator
        lis.append({'n':n,'baseline_lambda':mp.nstr(base,30),'model_T32_lambda':mp.nstr(model,30),'quartet_contribution_exact':str(q)})
    T=32;a=mp.mpf(1)/4
    def Q(w):return ((w-a)**2+T*T)*((w+a)**2+T*T)
    norm=mp.besselk(mp.mpf(1)/4,c)*Q(mp.mpf('.5'))
    predicted=(2*mp.pi)**(mp.mpf(1)/4)/norm
    growth=[]
    for s in [100,1000,10000]:
        ss=mp.mpf(s);value=mp.besselk((ss-mp.mpf('.5'))/2,c)*Q(ss-mp.mpf('.5'))/norm
        completion=ss*(ss-1)*mp.power(mp.pi,-ss/2)*mp.gamma(ss/2)/2
        ratio=value/completion/mp.power(ss,mp.mpf(7)/4)
        growth.append({'positive_real_s':s,'L_model_over_s_pow_7_4':mp.nstr(ratio,30)})
    out={'status':'nonvalidated85-digit observations; proofs and exact certificates separate','phase_roots':roots,'Li_samples':lis,'predicted_uncompleted_growth_constant':mp.nstr(predicted,30),'growth_samples':growth}
    (ROOT/'experiments/results/bessel_round3_numeric.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

def main():
    exact=exact_checks();numerical=numerical_observations()
    print(json.dumps({'exact_global_kernel_margin_T32':exact['global_margin_at_threshold'],'exact_prefix_Ns':[r['N'] for r in exact['prefix_samples']],'sample_phase_roots':numerical['phase_roots'],'growth_samples':numerical['growth_samples']},indent=2))
if __name__=='__main__':main()
