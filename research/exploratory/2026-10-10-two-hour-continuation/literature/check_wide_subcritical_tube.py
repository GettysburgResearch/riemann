"""Directed corner controls for the complete wider source Mellin tube."""
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
from flint import arb,acb,ctx


def need(ok,detail):
    if not ok:
        raise ArithmeticError(detail)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=192
    here=Path(__file__).resolve()
    source=here.with_name('PRIME_SLOT_CANCELLATION.md')
    source_hash='d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13'
    need(hashlib.sha256(source.read_bytes()).hexdigest()==source_hash,
         'frozen complete source pair factorization')
    sigma=arb(2)/5
    omega=acb(-arb(1)/2,arb(3).sqrt()/2)
    units=[acb(a)+b*omega for a,b in
           [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]]
    controls=0
    orders=[]
    for k in range(1,5):
        kappa=arb(1)/(2*arb(k).sqrt())
        half=arb(k)/2
        floor=arb(k)*(1-2*k*kappa.sin()**2)
        need(floor>half,'explicit wider half-floor width')
        need(kappa>arb(1)/(4*(2*k-1)),'strict enlargement of old width')
        pair_count=k*(2*k-1)
        perturb={e:acb(0,-e*kappa).exp() for e in (-1,1)}
        count=0
        for q in (7,13,19,31):
            x=(-2*sigma*arb(q).log()).exp()
            for phase in units:
                for central in (arb(0),arb(1)/5,arb(1)):
                    a=phase*acb(0,-central*arb(q).log()).exp()
                    for signs in product((-1,1),repeat=2*k):
                        slots=[a*perturb[signs[i]] for i in range(k)]
                        slots += [a.conjugate()*perturb[signs[k+j]] for j in range(k)]
                        pair_sum=acb(0)
                        pair_product=acb(1)
                        for i in range(2*k):
                            for j in range(i+1,2*k):
                                v=slots[i]*slots[j]
                                pair_sum+=v
                                pair_product*=1-x*v
                        need(pair_sum.real>half,'all actual corner pairs retain positive half floor')
                        error=pair_count*x*x/(2*(1-x))
                        need(abs(pair_product).log()<-half*x+error,
                             'complete pair logarithm directed upper bound')
                        count+=1
        controls+=count
        orders.append(dict(k=k,slots=2*k,corner_controls=count,
                           width_exact='1/(2*sqrt('+str(k)+'))',
                           positive_pair_floor_ball=floor.str(40,more=True),
                           certified_smaller_floor_exact=[k,2]))
    record=dict(status='PASS_DIRECTED_WIDE_SUBCRITICAL_TUBE_CONTROLS',
                precision_bits=192,sigma_exact=[2,5],orders=orders,
                total_complete_pair_corner_controls=controls,
                actual_prime_norms=[7,13,19,31],sextic_phase_count=6,
                proof_sha256=hashlib.sha256(here.with_name('WIDE_SUBCRITICAL_TUBE.md').read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(here.read_bytes()).hexdigest(),
                source_factorization_sha256=source_hash,
                continuum_tube_proved_by_finite_checker=False,
                arbitrary_ray_phase_bound_proved_by_finite_checker=False,
                complementary_frequencies_bounded=False,
                generalized_moment_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':
    main()
