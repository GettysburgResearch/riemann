#!/usr/bin/env python3
"""Parametric fixed-cutoff data for the reviewed exclusion/activation contracts."""
import sys
from exclusion_moments import ExclusionMoments
from verify_four_label import prime_power_sum
from verify_horizon_stitch import require
from verify_weighted_stitch import nonnegative_lower,smaller_upper
from weighted_moments import normalized_level_bounds


def build_power_data(power,mu,product_cutoff,endpoints,progress=False):
    require(1<power<2,'power domain')
    require(type(product_cutoff) is int and product_cutoff>=134,'native product cutoff')
    weights=ExclusionMoments((power+1)/2,product_cutoff)
    require(weights.labels.count(67)==2,'two native distinct 67 labels')
    if product_cutoff==100000000:
        require(len(weights.primes)==3001134 and weights.primes[-1]==49999991,
                'complete large prime sieve control')
    infinite_one=prime_power_sum((power+1)/2,1,mu)
    require(bool(infinite_one<3),'positive first-pair coefficient')
    finite={}
    for endpoint in endpoints:
        require(type(endpoint) is int and 1<=endpoint<=product_cutoff,'finite endpoint domain')
        single=weights.cumulative(1,min(endpoint,weights.prime_cap))
        _,odd=normalized_level_bounds(power,endpoint,single)
        if endpoint>weights.prime_cap:
            omitted=infinite_one-single[0]
            require(bool(omitted>0),'complete omitted prime tail')
            odd+=omitted
        triple=weights.cumulative(3,endpoint)
        _,triple_upper=normalized_level_bounds(power,endpoint,triple)
        row={'odd':smaller_upper(odd,infinite_one),'triple':triple_upper.upper()}
        for level in [2,4,6]:
            vector=weights.marked_cumulative(level,endpoint)
            ordinary,_=normalized_level_bounds(power,endpoint,vector.ordinary)
            marked,_=normalized_level_bounds(power,endpoint,vector.marked)
            row[level]=(nonnegative_lower(ordinary),nonnegative_lower(marked))
        finite[endpoint]=row
    selected={level:weights.marked_cumulative(level,product_cutoff) for level in [2,4,6]}
    single=weights.cumulative(1,weights.prime_cap)
    if progress:print(f'Certified N={product_cutoff} marked moments at m={power}',file=sys.stderr,flush=True)
    return {'power':power,'finite':finite,'selected':selected,
            'one':single,'infinite_one':infinite_one}
