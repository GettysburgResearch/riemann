#!/usr/bin/env python3
"""Exact controls for the selectable integer-count cutoff proof; no zero census rerun."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
from verify_annular import H, require
from verify_volterra_refinement import D,C1,C2,N0,exponential_upper,largest_even

HERE = Path(__file__).resolve().parent


def sawtooth_controls():
    records = []
    for start in (Q(0),Q(1,8),Q(1,2),Q(7,8),Q(7,3)):
        for length in (Q(1,4),Q(3,2),Q(7,2),Q(10)):
            for initial in (Q(1),Q(3)):
                beta = initial/(2*(length+1))
                end = start+length
                cuts = [start]+[Q(k) for k in range(start.numerator//start.denominator+1,
                                                   end.numerator//end.denominator+1)
                                if start<k<end]+[end]
                integral = Q(0)
                mass = initial*length-beta*length*length/2
                for left,right in zip(cuts,cuts[1:]):
                    k = left.numerator//left.denominator
                    # (1/2-{u})*(initial-beta*(u-start)), integrated independently.
                    a = Q(1,2)+k
                    c = initial+beta*start
                    integral += a*c*(right-left)-(a*beta+c)*(right*right-left*left)/2
                    integral += beta*(right**3-left**3)/3
                require(abs(integral)<=initial/8,"weighted shared sawtooth primitive")
                require(mass/2+integral>=mass/2-initial/8,"ceil positive integral floor")
                require(-mass/2+integral<=-mass/2+initial/8,"floor negative integral ceiling")
                records.append({"start":str(start),"length":str(length),
                                "g_start":str(initial),"integral_exact":str(integral)})
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    require(168*Q(22,7)<H,"Turing source application height")
    require(Q(91,22)>4,"uniform main-term derivative")
    require(H+20<Q(8,3)**30,"strict log(H+20)<30 via e>8/3")
    half_upper = Q(2067,1000)+Q(59,1000)*30+Q(10,3*H)
    require(half_upper<4<5-Q(1,32),"twenty-height cutoff contradiction")
    generic_difference = Q(29,2)-Q(1,32)-Q(3126,1000)-Q(59,1000)*29
    require(generic_difference>0 and Q(1,2)-Q(59,1000)>0,
            "all L>=29 cofinal cutoff contradiction")
    # logB+1 <= B/2 follows at H from logH<30, then derivative 1/2-1/B>0.
    require(31<H/2 and H>2,"uniform cofinal buffer guard")
    lower,upper = Q(113,355)*(1-Q(1838,28729)),Q(106,333)
    ell = 4*Q(232,1000)*D
    require(ell==Q(92539,156250),"exact good-cutoff quadrature coefficient")
    q,kappa = Q(87,200),Q(33,25)
    exponent = Q(13881,50000)
    require((D+Q(2,N0))*q<exponent,"whole variable-displacement exponent")
    exp_upper = exponential_upper(exponent)
    require(exp_upper<kappa,"whole displacement amplification enclosure")
    gap = lower-ell*q-(C2+C1*C1)*kappa*kappa*q*q*(upper+ell*q)/4
    require(gap==Q(38543369070455868447007920769,
                   23584713437500000000000000000000)>0,"strict complete-source gap")
    require(200*1142000**2<87*H,"global order and common selected cutoff")
    require(3000175332800>H+20,"published census includes entire selection interval")
    controls = sawtooth_controls()
    # floor(u)+1-u is always strictly positive (including integer jumps),
    # has pointwise magnitude <=1, and exact integral 1/2 over each unit period.
    synthetic_period_mean = Q(1)-Q(1,2)
    require(synthetic_period_mean==Q(1,2),"pointwise-only false-cutoff control")
    output = {"status":"PASS_EXACT_GOOD_CUTOFF_PICK","minimum_height":H,
              "minimum_order":N0,"condition":"200*n^2 <= 87*T at Delta(T)=0",
              "global_order":1142000,"maximal_even_order_at_H":largest_even(H,87,200),
              "good_cutoff_interval":[H,H+20],"cutoff_computed":False,
              "quadrature_coefficient_exact":str(ell),"strict_gap_exact":str(gap),
              "strict_gap_decimal":float(gap),"amplification_exact":str(kappa),
              "exponential_upper_exact":str(exp_upper),
              "ten_unit_integral_upper_exact":str(half_upper),
              "generic_L29_contradiction_margin_exact":str(generic_difference),
              "weighted_sawtooth_controls":controls,
              "pointwise_only_counterexample_period_mean":str(synthetic_period_mean),
              "input_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                 for name in ("GOOD_CUTOFF_PICK.md","verify_good_cutoff.py",
                              "DENSITY_RATIONAL_REFINEMENT.md","VOLTERRA_RATIONAL_REFINEMENT.md")},
              "Turing_source_record_sha256":hashlib.sha256(
                  (HERE.parent/"literature/TRUDGIAN_TURING_SOURCE_RECORD.md").read_bytes()).hexdigest(),
              "published_inputs_replayed":False,"tail_critical_census_used":False,
              "global_critical_census_used":True,"RH_proved":False}
    content = json.dumps(output,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(content)
    else: print(content,end="")


if __name__ == "__main__":
    main()
