#!/usr/bin/env python3
"""Scaled global SHARP certificate using reviewed marked-pair and prime-bin contracts."""
from fractions import Fraction as Q
import argparse,hashlib,importlib.metadata,json
from pathlib import Path
from flint import ctx
from activation_tail import numerator_polynomial
from check_threshold_arb import mobius_sieve
from exclusion_power_data import build_power_data
from exclusion_tail import certify_positive_tail
from verify_exclusion_stitch import ENDPOINTS as SMALL_ENDPOINTS
from verify_horizon_stitch import primes_through,require

PRODUCT_CUTOFF=100000000
POWER_POINTS=(Q(19,15),)+tuple(map(Q,('1.267','1.2675','1.2682','1.2692',
    '1.2706','1.2726','1.2754','1.2794','1.284')))+(Q(9,7),)
ENDPOINTS=SMALL_ENDPOINTS+(20000000,40000000,80000000,PRODUCT_CUTOFF)


def verify_slab(low_data,high_data,primes):
    low,high=low_data['power'],high_data['power'];bounded=[]
    for left,right in zip(ENDPOINTS[:-1],ENDPOINTS[1:]):
        odd=low_data['finite'][right];even=high_data['finite'][left]
        require(bool(odd['odd']<5),'positive bounded four-level coefficient')
        margin=1-odd['odd']+even[2][0]-odd['triple']+(1-odd['odd']/5)*even[4][0]
        require(bool(margin>0),f'large bounded margin [{left},{right}], [{low},{high}]')
        bounded.append({'endpoint_interval':[left,right],'margin_ball':str(margin),
                        'entire_margin_ball_positive':True})
    polynomial,constants=numerator_polynomial(low,high,low_data['one'],
        high_data['selected'],low_data['infinite_one'],PRODUCT_CUTOFF,primes)
    tail=certify_positive_tail(polynomial,PRODUCT_CUTOFF)
    return {'power_interval':[str(low),str(high)],'bounded_endpoint_certificates':bounded,
            'tail_constants':constants,'tail_numerator_coefficient_balls':[str(c) for c in polynomial],
            'unbounded_tail_certificate':tail}


def run(progress=False,only_first=False):
    ctx.prec=192
    require(POWER_POINTS[0]==Q(19,15) and POWER_POINTS[-1]==Q(9,7),'power coverage endpoints')
    require(all(a<b for a,b in zip(POWER_POINTS[:-1],POWER_POINTS[1:])),'strict power order')
    require(ENDPOINTS[0]==1 and ENDPOINTS[-1]==PRODUCT_CUTOFF
            and all(a<b for a,b in zip(ENDPOINTS[:-1],ENDPOINTS[1:])),'endpoint coverage chain')
    primes=primes_through(3*PRODUCT_CUTOFF//2)
    require(len(primes)==8444396 and primes[-1]==149999957,'complete large prime bin sieve')
    mu=mobius_sieve(80);records=[]
    low=build_power_data(POWER_POINTS[0],mu,PRODUCT_CUTOFF,ENDPOINTS,progress)
    for high_power in POWER_POINTS[1:]:
        high=build_power_data(high_power,mu,PRODUCT_CUTOFF,ENDPOINTS,progress)
        records.append(verify_slab(low,high,primes));low=high
        if only_first:break
    return {'status':'PASS_FIRST_LARGE_SLAB_ONLY' if only_first else 'PASS_GLOBAL_SHARP_LARGE_ACTIVATION_STITCH',
            'arithmetic':'ARB_DIRECTED_BALLS_EXACT_RATIONAL_POWERS_AND_BERNSTEIN_TAILS',
            'precision_bits':ctx.prec,'python_flint_version':importlib.metadata.version('python-flint'),
            'global_sufficient_power':None if only_first else '19/15',
            'covered_power_interval':['19/15',str(POWER_POINTS[1] if only_first else POWER_POINTS[-1])],
            'larger_power_input':'ACTIVATION_ENVELOPES.md A-PA1, threshold 9/7',
            'power_slab_count':len(records),'bounded_intervals_per_power_slab':len(ENDPOINTS)-1,
            'selected_even_product_cutoff':PRODUCT_CUTOFF,
            'complete_even_prime_cap':PRODUCT_CUTOFF//2,'complete_even_prime_count':3001134,
            'complete_prime_bin_cap':3*PRODUCT_CUTOFF//2,'complete_prime_bin_count':len(primes),
            'prime_tail_kernel_order':32,'retained_even_levels':[2,4,6],
            'power_slabs':records,'critical_power_one_proved':False,'rh_proved':False,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependency_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                for name in ['exclusion_power_data.py','activation_tail.py','exclusion_moments.py',
                             'exclusion_tail.py','weighted_moments.py','polynomial_tail.py',
                             'check_threshold_arb.py','verify_four_label.py','verify_horizon_stitch.py',
                             'verify_exclusion_stitch.py','verify_weighted_stitch.py','verify_two_label.py']}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path);parser.add_argument('--progress',action='store_true')
    parser.add_argument('--only-first',action='store_true')
    args=parser.parse_args();result=run(args.progress,args.only_first)
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
