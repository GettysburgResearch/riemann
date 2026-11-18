#!/usr/bin/env python3
"""Exact certificates for the positive-kernel round3 construction.
Standard library only. Uses the separately audited elementary log interval backend.
No infinite product, numerical Euler constant, or unverified floor is substituted.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import importlib.util,json

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('elementary_intervals',ROOT/'experiments/code/lagarias_compact_integer.py')
bk=importlib.util.module_from_spec(spec);spec.loader.exec_module(bk)
S=bk.S

def harmonic_enclosures(indices):
    want=set(indices);out={};lo=hi=0
    for k in range(1,max(want)+1):
        lo+=S//k;hi+=-((-S)//k)
        if k in want:out[k]=(F(lo,S),F(hi,S))
    return out

def gamma_bounds(n,H):
    h0,h1=H[n]
    ln=bk.I(n).log();ln1=bk.I(n+1).log()
    # H_n-log(n+1) < gamma < H_n-logn.
    return h0-F(ln1.hi,S),h1-F(ln.lo,S)

def divisor_sum(X):
    r=isqrt(X)
    return 2*sum(X//j for j in range(1,r+1))-r*r

def main():
    xs=[100,10000,1000000,100000000]
    ns=[10*isqrt(X) for X in xs]
    H=harmonic_enclosures(ns)
    H13=sum((F(1,j) for j in range(1,14)),F(0))
    assert H13==F(1145993,360360)
    gl,gu=gamma_bounds(100,H)
    assert F(57,100)<gl<gu<F(59,100)
    dl=H13/2-1-gu;du=H13/2-1-gl
    assert F(0)<dl<du<F(1,26)
    assert H13/2-1-F(59,100)==F(241,3603600)>0
    prefix=[]
    for N in [1,2,5,10,100]:
        a=F(1,10*(N+88)*5**N)
        baseline=F(1,6*(N+88)**2)
        perturb=8*N*a*a*5**(N-1)
        assert 0<a<F(1,2) and perturb<baseline/2
        prefix.append({'N':N,'a_N':str(a),'baseline_Li_lower_bound':str(baseline),'perturbation_upper_bound_using_eta_le_a_squared':str(perturb),'strict_positive_margin_lower_bound':str(baseline-perturb)})
    counts=[]
    for X,n in zip(xs,ns):
        gl,gu=gamma_bounds(n,H)
        dlo,dhi=H13/2-1-gu,H13/2-1-gl
        base=divisor_sum(X)-sum(X//j for j in range(1,14))+2*X
        nl=base+(2*dlo*X).__floor__();nu=base+(2*dhi*X).__floor__()
        logX=bk.I(X).log()
        mainlo=F(X*logX.lo,S)-X;mainhi=F(X*logX.hi,S)-X
        errlo=F(nl)-mainhi;errhi=F(nu)-mainlo
        root=isqrt(X);assert root*root==X
        counts.append({'X_with_T_equal_2piX':X,'harmonic_gamma_index':n,'exact_D_X':divisor_sum(X),'zero_count_lower':nl,'zero_count_upper':nu,'gamma_lower':str(gl),'gamma_upper':str(gu),'normalized_count_remainder_lower':str(errlo/root),'normalized_count_remainder_upper':str(errhi/root),'normalized_remainder_display_only':[float(errlo/root),float(errhi/root)]})
    result={'status':'exact rational/integer enclosures and analytic finite-prefix bounds; no full infinite-product numerical audit','scale_bits':bk.BITS,'gamma_bounds_are_integral_test':True,'gamma_coarse_verified':['57/100','59/100'],'delta_star_coarse_bounds':[str(H13/2-1-F(59,100)),str(H13/2-1-F(57,100))],'prefix_certificates':prefix,'zero_count_brackets':counts}
    out=ROOT/'experiments/results/positive_kernel_round3.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'gamma_calibration_passed':True,'delta_star_positive':True,'prefix_bounds_checked':[r['N'] for r in prefix],'count_brackets':[{'X':r['X_with_T_equal_2piX'],'lower':r['zero_count_lower'],'upper':r['zero_count_upper'],'normalized_remainder_display_only':r['normalized_remainder_display_only']} for r in counts]},indent=2))
if __name__=='__main__':main()
