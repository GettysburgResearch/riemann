#!/usr/bin/env python3
"""Complete directed Gamma/prime heat trace at exactly u=1/64, r=0."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import flint
from flint import acb, arb, ctx, fmpq

HERE = Path(__file__).resolve().parent


def need(ok: bool, reason: str) -> None:
    if not ok:
        raise SystemExit('FAIL: '+reason)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def interval(value: arb) -> list[str]:
    need(value.is_finite(), 'finite directed endpoint interval')
    return [str(value.lower().fmpq()),str(value.upper().fmpq())]


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=HERE/'native_heat_point.json')
    args=parser.parse_args()
    need(flint.__version__=='0.9.0' and flint.__FLINT_VERSION__=='3.6.0','backend versions')
    ctx.prec=320
    u=arb(fmpq(1,64))
    pi=arb.pi()
    quarter=acb(fmpq(3,4))

    def integrand(q: acb, analytic: bool) -> acb:
        # Entire 1F1 regularizes q=0. The quotient is meromorphic;
        # a denominator ball meeting a pole gives a nonfinite result.
        h=q*(quarter-4*q)
        return -(-q).exp()*(quarter-4*q)*h.hypgeom_1f1(1,2)/(-q).hypgeom_1f1(1,2)

    pieces=[]
    total=arb(0)
    for left,right in [(0,1),(1,4),(4,16),(16,100)]:
        value=acb.integral(integrand,left,right,
                           rel_tol=arb(fmpq(1,2**220)),abs_tol=arb(fmpq(1,2**220)),
                           deg_limit=100,eval_limit=100000,depth_limit=60)
        need(value.is_finite() and value.imag.contains(0),'finite real certified Gamma integral')
        total+=value.real
        pieces.append({'segment':[left,right],'native_real_interval':interval(value.real)})
        print('DIRECTED_GAMMA_SEGMENT',left,right,flush=True)
    Q=arb(100)
    need((-Q).exp()<arb(fmpq(1,2)),'Gamma tail denominator lower bound')
    gamma_tail=2*(-Q).exp()+8*(-Q/4-4*Q*Q).exp()
    gamma_radius=gamma_tail.upper().fmpq()
    complete_integral=total+arb(0,gamma_radius)
    gamma_term=(-arb.const_euler()-pi.log()+complete_integral)/(4*(pi*u).sqrt())

    primes=[]
    for number in range(2,65):
        divisor=2
        while divisor*divisor<=number and number%divisor:
            divisor+=1
        if divisor*divisor>number:
            primes.append(number)
    prime_sum=arb(0)
    terms=[]
    for prime in primes:
        number=prime
        exponent=1
        while number<=64:
            log_number=arb(number).log()
            term=arb(prime).log()/arb(number).sqrt()*(-log_number**2/(4*u)).exp()
            prime_sum+=term
            terms.append({'prime':prime,'exponent':exponent,'prime_power':number,
                          'native_term_interval':interval(term)})
            number*=prime
            exponent+=1
    need(len(primes)==18 and len(terms)==27,'exact complete prime/power inventory through64')
    log_N=arb(64).log()
    need(log_N>2 and log_N>4*u,'complete derivative-zero prime tail guard')
    prime_tail=2*u.sqrt()/pi.sqrt()*(-log_N**2/(8*u)).exp()
    tail_upper=prime_tail.upper().fmpq()
    prime_complement=arb(tail_upper/2,tail_upper/2)
    K=(u/4).exp()+gamma_term-prime_sum/(2*(pi*u).sqrt())-prime_complement
    need(K>0,'strict complete actual heat trace positivity')

    sources=[Path(__file__).resolve(),HERE/'NATIVE_HEAT_POINT.md',HERE/'COMPLETE_PRIME_HEAT_TRACE.md']
    package=Path(flint.__file__).resolve().parent
    bins=[package/'types'/name for name in ['arb.abi3.so','acb.abi3.so']]
    bins.extend(sorted((package.parent/'python_flint.libs').glob('lib*.so*')))
    result={'status':'PASS_DIRECTED_COMPLETE_NATIVE_HEAT_TRACE_POINT',
            'normalization':'K(u)=sum_(Re rho>0) m_rho exp(-rho^2*u), Xi(z)=xi(1/2+i*z)',
            'fixed_heat_time':'1/64','derivative_order':0,'precision_bits':320,
            'actual_Gamma_prime_source_replayed':True,
            'root_inventory_or_zero_count_used':False,'complete_prime_power_cutoff':64,
            'actual_primes':primes,'actual_prime_power_terms':terms,
            'Gamma_finite_segments':pieces,'Gamma_complete_tail_interval':interval(gamma_tail),
            'Gamma_complete_integral_interval':interval(complete_integral),
            'complete_prime_contribution_tail_interval':interval(prime_tail),
            'complete_heat_trace_interval':interval(K),'strict_lower_endpoint_positive':True,
            'all_times_or_all_derivatives_authenticated':False,'RH_proved_or_refuted':False,
            'infinite_source_formula_is_explicitly_imported':True,
            'source_sha256':{p.name:sha(p) for p in sources},
            'backend_binary_sha256':{p.name:sha(p) for p in bins}}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],flush=True)


if __name__=='__main__':
    main()
