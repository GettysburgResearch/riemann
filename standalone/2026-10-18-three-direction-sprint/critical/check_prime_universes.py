"""Independent directed Fourier-integral and prime-universe checks.

This checker does not import certify_sectors.py or read any deposited report.
Small prime universes are evaluated in TWO independent coordinates: a complete
primitive-pair sum with its geometric whole-tail bound, and interval Riemann
integration of the positive Fourier Euler product with its Gaussian tail.
Larger universes get complete analytic integral lower/upper bounds, not a
numerical quadrature claim. Requires python-flint==0.9.0.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time


def need(ok, why):
    if not ok:
        raise ValueError(why)


def primes_to(n):
    flags = bytearray(b'\x01')*(n+1)
    flags[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(n)+1):
        if flags[p]:
            flags[p*p:n+1:p] = b'\x00'*((n-p*p)//p+1)
    return [p for p in range(2, n+1) if flags[p]]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dependency-dir', type=Path)
    ap.add_argument('--bits', type=int, default=192)
    ap.add_argument('--largest-prime-cutoff', type=int, default=1000000)
    ap.add_argument('--mesh', type=int, default=512)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    if args.dependency_dir:
        sys.path.insert(0, str(args.dependency_dir.resolve()))
    import flint
    from flint import arb, ctx
    need(flint.__version__ == '0.9.0', 'Pinned python-flint required.')
    need(args.bits >= 128 and args.mesh >= 128, 'Replay accuracy too small.')
    need(args.largest_prime_cutoff >= 100, 'Missing growing-universe fixtures.')
    ctx.prec = args.bits
    started = time.monotonic()

    def rational(q):
        return arb(q.numerator)/q.denominator

    def render(x):
        need(x.is_finite(), 'Nonfinite interval.')
        out = x.str(60, more=True)
        need(arb(out).contains(x), 'Serialization lost an enclosure.')
        return out

    allps = primes_to(args.largest_prime_cutoff)

    def locals_for(ps):
        return [(p, arb(p).log(), 1/(arb(p)*arb(p).sqrt()),
                 rational(Fraction(p*p-1, p+2))) for p in ps]

    def lam(t, loc):
        p, logp, h, cp = loc
        cosine = (t*logp).cos()
        den = 1-2*h*cosine+h*h
        need(den > 0, 'Local denominator positivity failed.')
        return 1-2*cp*(h*cosine-h*h)/den

    def pair_sum(ps, limits):
        # Independent exact beta prime-power source, no table/sieve import.
        entries = []
        for p, jmax in zip(ps, limits):
            cp = Fraction(p*p-1, p+2)
            choices = [(1, 1, Fraction(1))]
            for j in range(1, jmax+1):
                value = -cp/Fraction(p**j)
                choices.extend(((p**j, 1, value), (1, p**j, value)))
            entries.append(choices)
        total = arb(0)
        for choice in itertools.product(*entries):
            r = math.prod(z[0] for z in choice)
            s = math.prod(z[1] for z in choice)
            coeff = math.prod((z[2] for z in choice), start=Fraction(1))
            u = (arb(r)/s).log()
            total += rational(coeff)/arb(r*s).sqrt()*(-u*u/8).exp()
        full_mass = arb(1)
        truncated_mass = arb(1)
        for p, jmax in zip(ps, limits):
            h = 1/(arb(p)*arb(p).sqrt())
            cp = rational(Fraction(p*p-1, p+2))
            full_mass *= 1+2*cp*h/(1-h)
            truncated_mass *= 1+2*cp*h*(1-h**jmax)/(1-h)
        tail = full_mass-truncated_mass
        need(tail > 0, 'Positive geometric whole-tail required.')
        return total+arb(0, tail.upper()), tail

    def integral_sum(ps):
        ls = locals_for(ps)
        upper = arb(1)
        for p, logp, h, cp in ls:
            need(1-2*cp*h/(1-h) > 0, 'Exact local minimum not positive.')
            upper *= 1+2*cp*h/(1+h)
        total = arb(0)
        R = 8
        for j in range(R*args.mesh):
            left = arb(j)/args.mesh
            # Entire closed cell represented as an interval.
            t = (arb(2*j+1)+arb(0, 1))/(2*args.mesh)
            prod = (-2*t*t).exp()
            for loc in ls:
                prod *= lam(t, loc)
            total += prod/args.mesh
        total *= 2*(2/arb.pi()).sqrt()
        tail = upper*(arb(2).sqrt()*R).erfc()
        need(tail > 0, 'Positive whole real-line Gaussian tail required.')
        return total+arb(0, tail.upper()), tail

    comparisons = []
    for ps, limits in (((2,), (48,)), ((2, 3), (48, 32))):
        direct, d_tail = pair_sum(ps, limits)
        integral, i_tail = integral_sum(ps)
        need(direct.overlaps(integral), 'Independent coordinates disagree.')
        need(direct > 0 and integral > 0, 'Complete small-universe sign failed.')
        rec = {'primes': list(ps), 'max_exponents': list(limits),
               'complete_pair_sum': render(direct),
               'whole_exponent_tail': render(d_tail),
               'independent_complete_fourier_integral': render(integral),
               'whole_fourier_integral_tail': render(i_tail)}
        comparisons.append(rec)
        print(json.dumps({'independent_comparison': rec}), flush=True)

    # A single whole interval in (23) is enough for a rigorous LOWER bound.
    # Taking logarithms avoids large product widths and under/overflow.
    bounds = []
    cutoffs = sorted(set([100, 1000, 10000, 100000,
                          args.largest_prime_cutoff]))
    cutoffs = [x for x in cutoffs if x <= args.largest_prime_cutoff]
    for P in cutoffs:
        ps = [p for p in allps if p <= P]
        lp = arb(P).log()
        center = arb.pi()/lp
        half = 1/(lp*lp)
        t = center+arb(0, half.upper())
        lower_log = arb(0)
        upper_log = arb(0)
        for loc in locals_for(ps):
            p, logp, h, cp = loc
            q = lam(t, loc)
            need(q > 0, 'Interval escaped a globally positive local factor.')
            lower_log += q.log().lower()
            upper_log += (1+2*cp*h/(1+h)).log()
        # Integrate over [center-half,center+half]; use the maximum |t|.
        gaussian_log_lower = -2*(center+half)**2
        lower_log += (2*half*(2/arb.pi()).sqrt()).log()+gaussian_log_lower
        need(lower_log < upper_log, 'Whole-integral bounds inconsistent.')
        scale = arb(P).sqrt()/lp
        rec = {'prime_cutoff': P, 'prime_count': len(ps),
               'log_integral_lower_bound': render(lower_log),
               'log_integral_upper_bound': render(upper_log),
               'normalized_log_lower': render(lower_log/scale),
               'normalized_log_upper': render(upper_log/scale),
               'whole_integral_not_pointwise_sample': True}
        bounds.append(rec)
        print(json.dumps({'whole_integral_bounds': rec}), flush=True)

    result = {'status': 'PASS', 'arithmetic': 'DIRECTED_INTERVAL',
              'python_flint': flint.__version__, 'precision_bits': args.bits,
              'independent_small_universes': comparisons,
              'complete_growing_universe_bounds': bounds,
              'prime_list_sha256': hashlib.sha256(
                  ','.join(map(str, allps)).encode()).hexdigest(),
              'asymptotic_theorem_certified_by_this_script': False,
              'elapsed_seconds': time.monotonic()-started}
    out = args.output or Path(__file__).with_name('PRIME_UNIVERSE_CHECKS.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'output': str(out),
                      'elapsed_seconds': result['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
