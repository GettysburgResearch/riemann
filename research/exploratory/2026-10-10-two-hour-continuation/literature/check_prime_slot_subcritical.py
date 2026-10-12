"""Directed finite controls for the source collision-factor subcritical tube."""
import argparse
from collections import Counter
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import hashlib
import json
from flint import arb, acb, ctx


def need(ok, detail):
    if not ok:raise ArithmeticError(detail)


def norm(z):
    a,b=z
    return a*a-a*b+b*b


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=192
    here=Path(__file__).resolve()
    prior=here.with_name('PRIME_SLOT_CANCELLATION.md')
    prior_hash='d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13'
    need(hashlib.sha256(prior.read_bytes()).hexdigest()==prior_hash,'frozen exact pair/remainder proof')
    source=Path('/workspace/.riemann-research/sources/qrh11-12.tex')
    source_hash='d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d'
    need(hashlib.sha256(source.read_bytes()).hexdigest()==source_hash,'literal fixed source')
    sigma=arb(2)/5
    alpha=2*sigma
    omega=acb(-arb(1)/2,arb(3).sqrt()/2)
    units=[acb(a)+b*omega for a,b in
           [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]]
    field_count=0
    native_phases=Counter()
    for q in (7,13,19,31):
        for root in (r for r in range(q) if (r*r+r+1)%q==0):
            generator=next(g for g in range(2,q)
                           if len({pow(g,j,q) for j in range(q-1)})==q-1)
            logs={pow(generator,j,q):j for j in range(q-1)}
            beta=(1+root)%q
            c=logs[beta]//((q-1)//6)
            need(logs[beta]%((q-1)//6)==0 and gcd(c,6)==1,'native sixth-unit log embedding')
            inv=pow(c,-1,6)
            for x in range(1,q):native_phases[q,logs[x]*inv%6]+=1
            field_count+=1
    need(field_count==8 and len(native_phases)==24,'all actual prime-field sixth phases')
    tube_checks=common_checks=negative_controls=0
    records=[]
    for k in range(1,5):
        r=2*k
        kappa=arb(1)/(4*(2*k-1))
        lam=arb(k)/2
        pairs=r*(r-1)//2
        perturb={sign:acb(0,-sign*kappa).exp() for sign in (-1,1)}
        for q in (7,13,19,31):
            x=(-sigma*arb(q).log()).exp()
            v=x*x
            for phase in range(6):
                for central in (arb(0),arb(1)/5,arb(1)):
                    a=units[phase]*acb(0,-central*arb(q).log()).exp()
                    common=abs(1-a*a*v)**(k*(k-1))*(1-v)**(k*k)
                    need(common<(1-v)**k or k==1,
                         'source-phase common conjugate pair bound')
                    common_checks+=1
                    for signs in product((-1,1),repeat=r):
                        normalized=[a*perturb[signs[i]] for i in range(k)]
                        normalized += [a.conjugate()*perturb[signs[k+j]] for j in range(k)]
                        pair_sum=acb(0)
                        pair_product=acb(1)
                        for i in range(r):
                            for j in range(i+1,r):
                                xi=normalized[i]*normalized[j]
                                pair_sum+=xi
                                pair_product*=1-v*xi
                        need(pair_sum.real>lam,'complete independent-slot tube real pair floor')
                        error=pairs*v*v/(2*(1-v))
                        need(abs(pair_product).log() < -lam*v+error,
                             'directed all-pair logarithmic upper bound')
                        tube_checks+=1
            # Actual character value eta=-1: suppressed collision need not suppress C.
            C=1+2*k*x
            Q=C/(1+x)**(2*k)
            need(C>1 and Q<1,'full finite Euler factor versus collision negative control')
            negative_controls+=1
        records.append({'k':k,'slots':r,'sigma':'2/5',
                        'tube_kappa_exact':[1,4*(2*k-1)],
                        'lambda_exact':[k,2],
                        'common_saving_exponent_exact':[k,5],
                        'tube_saving_exponent_exact':[k,10]})
    for q in (7,13,19,31):
        x=(-sigma*arb(q).log()).exp()
        need((1-x*x)**(-2)>1,'outside-tube local collision growth control')
        negative_controls+=1

    # Independent fixed-S ideal census at Y=31, using all six generators.
    Y=31
    counts=Counter()
    amax=isqrt(4*Y//3)
    for a in range(-amax,amax+1):
        t=isqrt(4*Y-3*a*a)
        for b in range(-(-(a-t)//2),(a+t)//2+1):
            n=norm((a,b))
            if n and (a+b)%3 and not (a%2==0 and b%2==0):counts[n]+=1
    need(all(c%6==0 for c in counts.values()),'ideal census divides complete unit orbits')
    ideal_counts={n:c//6 for n,c in counts.items()}
    need(ideal_counts=={1:1,7:2,13:2,19:2,25:1,31:2},'complete actual good-prime ideal census')
    inverse=arb(1)
    for q,multiplicity in ((7,2),(13,2),(19,2),(25,1),(31,2)):
        inverse*=(1-(-alpha*arb(q).log()).exp())**(-multiplicity)
    short_sum=sum(c*(-alpha*arb(n).log()).exp() for n,c in sorted(ideal_counts.items()))
    need(inverse>short_sum,'positive Euler product contains every short ideal')
    record={'status':'PASS_DIRECTED_SOURCE_PRIME_SLOT_SUBCRITICAL_TUBE_CONTROLS',
            'precision_bits':192,'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),
            'proof_sha256':hashlib.sha256(here.with_name('PRIME_SLOT_SUBCRITICAL_TUBE.md').read_bytes()).hexdigest(),
            'prior_pair_proof_sha256':prior_hash,'source_sha256':source_hash,
            'actual_prime_fields':field_count,'native_sixth_phase_classes':len(native_phases),
            'common_slice_local_pair_controls':common_checks,
            'all_corner_tube_local_pair_controls':tube_checks,
            'negative_controls':negative_controls,'priced_regions':records,
            'independent_good_ideal_census_31':ideal_counts,
            'finite_positive_inverse_Euler_ball':inverse.str(40,more=True),
            'included_short_ideal_sum_ball':short_sum.str(40,more=True),
            'infinite_factor_bound_proved_by_finite_checker':False,
            'individual_reciprocal_factors_bounded':False,
            'complementary_Mellin_region_bounded':False,
            'generalized_moment_proved':False,'rh_proved':False}
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':main()
