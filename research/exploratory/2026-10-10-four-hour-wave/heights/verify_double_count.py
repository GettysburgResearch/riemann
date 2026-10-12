#!/usr/bin/env python3
"""Exact uniform controls for the twice-integrated complete-count proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
from verify_annular import H,require
from verify_volterra_refinement import D,C1,C2,N0,exponential_upper,largest_even

HERE = Path(__file__).resolve().parent


def bernoulli_controls():
    u = sp.symbols("u", real=True)
    b2 = u*u-u+sp.Rational(1,6)
    b3 = u**3-sp.Rational(3,2)*u*u+u/2
    b4 = u**4-2*u**3+u*u-sp.Rational(1,30)
    require(sp.expand(sp.diff(b3,u)-3*b2)==0,"first periodic integration identity")
    require(sp.expand(sp.diff(b4,u)-4*b3)==0,"second periodic integration identity")
    require(b3.subs(u,0)==b3.subs(u,1)==0,"no cubic boundary term")
    require(b4.subs(u,0)==b4.subs(u,1)==-sp.Rational(1,30),
            "explicit quartic boundary term")
    require(sp.expand(b4-(u*u*(1-u)**2-sp.Rational(1,30)))==0,
            "complete Bernoulli maximum identity")
    require(Q(1,16)-Q(1,30)<Q(1,30),"B4 absolute bound from 0<=u(1-u)<=1/4")
    explicit = Q(1,3)*Q(1,4)*Q(1,30)
    require(explicit==Q(1,360),"required explicit z^-3 coefficient")
    remainder_explicit = 8*explicit
    remainder_integral_pi = Q(1,4)*Q(1,30)*Q(1,4)*8
    require(remainder_explicit==Q(1,45) and remainder_integral_pi==Q(1,60),
            "native complex remainder normalization")
    lo = Q(7,384)+Q(1,45)+Q(22,420)
    hi = Q(1,24)+Q(1,45)+Q(22,420)
    require(0<lo<hi<Q(1,8),"uniform theta cubic errors")
    require(Q(1,48)-Q(1,8*32**2)>0,"strict positive theta error for all t>=32")
    require(Q(1,48)+Q(1,8*32**2)<Q(1,47),"sharp native theta bound for all t>=32")
    return {"explicit_gamma_coefficient":"-1/360",
            "cubic_remainder_explicit":str(remainder_explicit),
            "cubic_remainder_pi_coefficient":str(remainder_integral_pi),
            "theta_lower_cubic_upper":str(lo),"theta_upper_cubic_upper":str(hi),
            "theta_bound":"0 < epsilon(t) < 1/(47*t), all t>=32"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    bernoulli = bernoulli_controls()
    require(H>32,"entire tail within native Gamma bound")
    ca = Q(2067,28729)+Q(59,1000)+Q(1,141)
    require(ca==Q(559172551,4050789000),"complete discrepancy primitive coefficient")
    coefficient = C2+C1*C1
    j = 4*ca*coefficient
    require(j==Q(45562883070469639,101269725000000000),"twice-integrated quadrature coefficient")
    require(D+Q(3,N0)<C1,"unshifted first derivative uniform guard")
    require(D*D+(Q(6,N0)+Q(1,N0*N0))*D+Q(9,N0*N0)+Q(7,N0**3)<C2,
            "unshifted second derivative uniform guard")
    q,kappa = Q(131,200),Q(38,25)
    exponent = Q(4181,10000)
    require((D+Q(2,N0))*q<exponent,"arbitrary-variable full displacement exponent")
    exp_upper = exponential_upper(exponent)
    require(exp_upper<kappa,"whole exponential uniform enclosure")
    lower = Q(113,355)*(1-Q(1838,28729))
    upper = Q(106,333)
    gap = lower-j*q*q-coefficient*kappa*kappa*q*q*(upper+j*q*q)/4
    require(gap==Q(133326033815066275292957582984782363769,
                   79810670272500000000000000000000000000000)>0,
            "strict complete-source twice-integrated gap")
    require(200*1400000**2<131*H,"global order paid at all selected cutoffs")
    require(largest_even(H,131,200)==1401784,"exact maximal global even order")
    require(3000175332800>H+20,"entire selected cutoff interval within imported census")
    output = {"status":"PASS_EXACT_DOUBLE_COUNT_PICK","minimum_height":H,
              "minimum_order":N0,"condition":"200*n^2 <= 131*T at Delta(T)=0",
              "global_order":1400000,"maximal_even_order_at_H":1401784,
              "native_bernoulli_controls":bernoulli,
              "primitive_coefficient_exact":str(ca),"quadrature_coefficient_exact":str(j),
              "strict_gap_exact":str(gap),"strict_gap_decimal":float(gap),
              "amplification_exact":str(kappa),"exponential_upper_exact":str(exp_upper),
              "examples":[{"height":t,"selectable_tail_order":largest_even(t,131,200)}
                          for t in (H,10**14,10**18,10**24,10**36)],
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                 for name in ("DOUBLE_COUNT_PICK.md","verify_double_count.py",
                              "GOOD_CUTOFF_PICK.md","DENSITY_RATIONAL_REFINEMENT.md",
                              "VOLTERRA_RATIONAL_REFINEMENT.md")},
              "Turing_source_record_sha256":hashlib.sha256(
                  (HERE.parent/"literature/TRUDGIAN_TURING_SOURCE_RECORD.md").read_bytes()).hexdigest(),
              "published_inputs_replayed":False,"tail_critical_census_used":False,
              "global_critical_census_used":True,"cutoff_computed":False,"RH_proved":False}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(content)
    else: print(content,end="")


if __name__ == "__main__":
    main()
